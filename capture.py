import contextlib
import json
import os
import shutil
import time
from pathlib import Path
from dominocode.settings import settings
from pydub import AudioSegment

import typer
from playwright.sync_api import sync_playwright, Page, Browser
from dominocode.playwright.assistant import AssistentHelper
from dominocode.playwright import mouse_move_middle

HERE = Path(__file__).parent
app = typer.Typer()


timeout = 10000
time_step = 500

# if in a hurry, and want to test
# time_step = 0


def get_video_length(path):
    cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {path}"
    import subprocess

    print(cmd)
    output = subprocess.check_output(cmd, shell=True)
    length = float(output.strip())
    return length



class CaptureHelper:
    page: Page

    def __init__(
        self, browser: Browser, name, port, animation_time, height=1024, fast=False, screenshots=True,
    ):
        self.browser = browser
        self.name = name
        self.port = port
        self.animation_time = animation_time
        self.height = height
        self.N = 0  # screenshot number
        self.fast = fast
        self.screenshots = screenshots
        # TODO: this should actually happen at the server
        shutil.copy(
            "notebooks/empty.ipynb",
            f"notebooks/{self.name}.ipynb",
        )
        os.makedirs("scripts", exist_ok=True)
        self.script_file = Path("scripts") / f"{self.name}.txt"
        self.script_file.unlink(missing_ok=True)
        # list of timing to later attach the audio at the right moment
        self.timings_steps = []

        audio_files = Path(f"audio/{name}/").glob("*.mp3")
        files = list(sorted(audio_files))
        segments = [AudioSegment.from_file(file, format="mp3") for file in files]
        self.delays = [len(segment) for segment in segments]
        self.step_index = 0

    def __enter__(self):
        self.time_start = time.time()
        self.page = self.browser.new_page(
            device_scale_factor=2,
            record_video_dir="docs/videos",
            record_video_size={"width": 1024, "height": self.height},
            viewport={"width": 1024, "height": self.height},
        )  # , record_video_size=ViewportSize(width=1000, height=1000))
        self.time_initial = time.time()

        self.page.set_default_timeout(timeout=timeout)
        self.page.goto(f"http://localhost:{self.port}/notebooks/{self.name}.ipynb")

        # if we click the kernellink too fast, it can close again
        self.page.wait_for_timeout(1000)
        # restart kernel
        self.page.locator("#kernellink").click()
        self.page.locator('span:has-text("Restart")').click()
        self.page.locator('button:has-text("Restart")').click()
        self.assistant.initializer.wait_for()
        self.inject_js_and_css()
        # get rid of connected icon and make sure it's stable
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(200)

    def inject_js_and_css(self):
        self.page.add_style_tag(
            content="""
        .record-info {
            background-color: white;
            border: 1px solid black;
            font-size: 20pt;
            position: absolute;
            bottom: 70px;
            left: 85px;
            padding: 10px;
            transition: opacity 0.3s;
            z-index: 100000;
        }
        """
        )
        self.page.add_script_tag(
            content="""
            window.infoDiv = document.createElement('div')
            infoDiv.style.opacity = 0;
            infoDiv.classList.add('record-info')
            document.body.appendChild(infoDiv)
        """
        )

    def scroll_to_last_code_cell(self):
        last_code_cell = self.page.locator(".code_cell").last
        last_code_cell.scroll_into_view_if_needed()

    def add_msg(self, text, duration=None):
        js_code = f"""
            infoDiv.style.opacity = 0.7;
            infoDiv.innerHTML = {text!r}
        """
        if duration:
            js_code += f"""
            setTimeout(() => {{
                infoDiv.style.opacity = 0
            }}, {duration*1000!r})
            """
        self.page.evaluate(js_code)

    def insert_code(self, code, delay=7):
        input = self.page.locator("textarea").last
        input.type(code, delay=delay)

        input = self.page.locator("text=In [ ]:").last
        input.press("Shift+Enter")

    @property
    def assistant(self):
        return AssistentHelper(self.page)

    def shot(self, name, animation_time=None):
        self.page.wait_for_timeout(
            self.animation_time * 1000
            if animation_time is None
            else animation_time * 1000
        )
        if self.screenshots:
            self.page.screenshot(
                path=f"docs/screenshots/{self.name}/{self.N:02}-{name}.png"
            )
        self.page.wait_for_timeout(time_step)
        self.N += 1

    def start_video(self):
        # here is where we start the trim
        self.time_initial = time.time()

    def __exit__(self, exception, value, traceback):
        video_path = Path(self.page.video.path())
        self.page.close()
        self.browser.close()
        self.time_end = time.time()
        print("video took", self.time_end - self.time_start, "seconds")
        if exception is None and self.time_initial:
            with (Path("scripts") / f"{self.name}.json").open("w") as f:
                f.write(json.dumps(self.timings_steps, indent=4))
            skip = self.time_initial - self.time_start
            print("Trimming", skip)
            video_path_raw = video_path.parent / f"{self.name}-raw.webm"
            video_path_speedup = video_path.parent / f"{self.name}-speedup.mp4"
            video_path_cut = video_path.parent / f"{self.name}-cut.mp4"
            shutil.move(video_path, video_path_raw)

            length = get_video_length(video_path_raw)
            speedup = length / (self.time_end - self.time_start)

            print("speedup", speedup)
            cmd = f'ffmpeg -y -i {video_path_raw} -filter:v "setpts={1/speedup}*PTS" -vcodec libx264 -crf 23 {video_path_speedup}'
            print(cmd)
            os.system(cmd)

            cmd = f"ffmpeg -y -i {video_path_speedup}  -ss {self.time_initial - self.time_start} -vcodec libx264 -crf 23 {video_path_cut}"
            print(cmd)
            os.system(cmd)

    @contextlib.contextmanager
    def step(self, text, default_duration):
        duration = default_duration
        audio_duration = None
        skip = self.time_initial - self.time_start
        if self.step_index < len(self.delays):
            audio_duration = self.delays[self.step_index] / 1000
            self.step_index += 1
            duration = audio_duration
        else:
            print(
                f"WARNING: no audio delay know, please rerun after generating audio at audio/{self.name}"
            )
        t0 = time.time()
        self.timings_steps.append(dict(text=text, t_start=t0 - self.time_start - skip))
        self.add_msg(text, duration=duration)
        self.page.wait_for_timeout(duration * 1000)
        yield
        spend = time.time() - t0
        print("step: ", duration, spend, text)
        if not self.fast:
            self.page.wait_for_timeout(500)
        with self.script_file.open("a") as f:
            text = text.replace("™", "")  # remove trademark in script
            f.write(f"{text}\n")

    # TODO: deduplicate this code with dca.Notebook
    def last_cell_assistant_hover(self):
        last_input = self.last_code_cell.locator(".input")
        last_input.scroll_into_view_if_needed()
        mouse_move_middle(self.page, last_input)
        self.assistant.domino_logo.wait_for()
        self.page.wait_for_timeout(100)
        self.assistant.domino_logo.hover()
        self.page.wait_for_timeout(100)

    def remove_app_sh(self):
        root = Path(settings.domino_working_dir)
        path = root / "app.sh"
        path.unlink(missing_ok=True)

    def step_init(self):
        with self.step("Click the Domino Code Assist™ button", 2.0):
            self.assistant.initializer.click()
            self.assistant.initialized_text.click()
            self.shot("assistant-ready")

    def step_cell_insert_code(self, code, msg, delay=7):
        with self.step(msg, 2.0):
            if not self.fast:
                self.page.wait_for_timeout(1500)
            self.insert_code(code)

    def step_cell_insert_code_load_titanic(self):
        path_csv = HERE / "mydata/titanic.csv"
        code = f"""import pandas as pd

df = pd.read_csv("{path_csv}")
df.head(2)"""
        self.step_cell_insert_code(
            code,
            "Open a dataset using the Domino Code Assist™, or your own Python code.",
        )
        self.page.locator("text=pclass").wait_for()

    def step_hover_cell(self):
        with self.step(
            "Hover above the next code cell, to show the Domino Code Assist™ button",
            2.0,
        ):
            self.scroll_to_last_code_cell()
            mouse_move_middle(self.page, self.page.locator(".code_cell").last)
            self.page.wait_for_load_state("networkidle")
            self.shot("assistant-visible")

    def step_hover_assistant_fab(self):
        with self.step(
            "Hover above the Domino Code Assist™ button to expand the menu", 2.5
        ):
            self.assistant.domino_logo.hover()
            self.page.wait_for_timeout(500)
            self.shot("assistant-expand")

    def step_load_data_open(self):
        with self.step("Click on 'Load Data'", 2.5):
            self.assistant.load_data.menu_item.click()
            self.shot("load-data")

    def step_load_data_tab_dataset_open(self):
        with self.step("Go to the 'Datasets' tab to explore your filesystem", 2.5):
            self.assistant.load_data.dialog.locator("text=Datasets").click()
            self.shot("load-data-datasets")

    def step_load_data_tab_dataset_navigate(self):
        with self.step("Navigate to the right directory", 2.5):
            self.assistant.load_data.dialog.locator(
                'div[role="list"] div:has-text("..")'
            ).nth(1).click()
            self.shot("load-data-datasets-dir-up")

            self.page.wait_for_timeout(1000)

            self.assistant.load_data.dialog.locator("text=mydata").click()
            self.shot("load-data-datasets-dir-mydata")

    def step_load_data_tab_dataset_titanic_open(self):
        with self.step("Click the file you want to open", 2.5):
            self.assistant.load_data.dialog.locator("text=titanic.csv").click()

    def step_insert_code(self):
        with self.step(
            "Click 'Insert code' to insert the code snippet into your notebook", 2.5
        ):
            self.page.wait_for_timeout(1500)
            self.page.locator("button:has-text('Insert code')").last.click()

    def step_transform_open(self):
        with self.step('Click on "Transformations"', 2.5):
            self.assistant.transform.menu_item.click()
            self.shot("transformations")

    def step_transform_pick_df(self, df_name="df"):
        with self.step("Pick the right dataframe", 2.5):
            # we cannot use it before we need to do a screenshot in between
            # self.assistant.transform.choose_dataframe(df_name)
            self.page.locator('div[role="button"]:has-text("DataFrame")').click()
            self.page.wait_for_timeout(1000)
            self.shot("choose-dataframe")
            self.page.locator(f'div[role="option"] >> text={df_name}').click()
            self.page.wait_for_timeout(500)
            self.shot("pick-dataframe")

    def step_transform_table_cell_action_hover(self, row=10, column=10):
        with self.step(
            "Hover above the dotted icon in the table to show the cell actions", 2.5
        ):
            self.assistant.transform.table_cell(row, column + 1).hover()
            self.page.wait_for_timeout(300)  # animation
            self.shot("popup-menu")

    def step_transform_filter_values_like_open(self):
        with self.step(
            "Click 'Filter values like this' to open the filter dialog", 2.5
        ):
            # self.assistant.transform.filter_values_like.click()
            self.page.locator("text=Filter values like").first.click()
            self.shot("filter-values-like")

    def step_transform_filter_values_like_apply(self):
        with self.step("Click 'Apply' to apply the filter", 2.5):
            if not self.fast:
                self.page.wait_for_timeout(1500)
            self.assistant.transform.filter_like.apply.click()
            self.shot("filtered")

    def step_transform_toggle_code(self):
        with self.step("Click the 'Show code' toggle to preview the code", 2.5):
            if not self.fast:
                self.page.wait_for_timeout(1500)

    def step_viz_open(self):
        with self.step("Click on 'Visualizations'", 2.5):
            self.assistant.viz.menu_item.click()
            self.shot("open")

    def step_viz_pick_df(self, df_name="df"):
        with self.step("Pick the right dataframe", 2.5):
            self.assistant.viz.choose_dataframe(df_name)
            self.page.wait_for_timeout(500)
            self.shot("choose-dataframe")

    def step_viz_choose(self, viz_name="Scatter"):
        with self.step(
            f"Click on the visualization you want to use, for instance {viz_name.lower()}",
            2.5,
        ):
            self.assistant.viz.plot_type.click()
            self.shot("choose-type")
            self.assistant.viz.plot_type_option("Scatter").click()
            self.shot("choose-type-scatter")

    def step_viz_configure(self):
        viz_dialog = self.assistant.viz.dialog
        with self.step("Configure the visualization", 2.5):
            viz_dialog.locator('div[role="button"]:has-text("X-axis")').click()
            self.shot("choose-x")
            self.page.locator('div[role="option"] >> text=age').click()
            self.shot("choose-x-age")

            viz_dialog.locator('div[role="button"]:has-text("Y-axis")').click()
            self.shot("choose-y")
            self.page.locator('div[role="option"] >> text=fare').last.click()
            self.shot("choose-y-fare")

            viz_dialog.locator('div[role="button"]:has-text("Color")').click()
            self.shot("choose-color")
            self.page.locator('div[role="option"] >> text=pclass').last.click()
            self.shot("choose-color-pclass")

            viz_dialog.locator("text=Options").click()
            self.shot("expand-options")
            viz_dialog.locator('div[role="button"]:has-text("Theme")').click()
            self.shot("choose-theme")
            self.page.locator('div[role="option"] >> text=ggplot2').first.click()
            self.shot("choose-theme-ggplot2")

    def step_viz_choose_var(self, name):
        viz_dialog = self.assistant.viz.dialog
        with self.step("Choose a variable name", 2.5):
            viz_dialog.locator('text="Output variable" >> xpath=.. >> input').click()
            self.shot("choose-name")
            var_input = viz_dialog.locator(
                'text="Output variable" >> xpath=.. >> input'
            )
            var_input.fill("")
            var_input.type(name, delay=10)
            self.shot(f"choose-name-{name}")

    def step_cell_insert_code_histogram_survived(self):
        with self.step(
            "Create a histogram using the Domino Code Assist™, or your own Python code.",
            3.5,
        ):
            self.scroll_to_last_code_cell()
            self.insert_code(
                """
import plotly.express as px

histogram_survived = px.histogram(df, x="survived")
histogram_survived
""".strip(),
                delay=15,
            )
            self.page.wait_for_timeout(100)
            self.page.locator(".plotly-graph-div").last.scroll_into_view_if_needed()
            self.shot("create-viz-1")

    def step_cell_insert_code_scatter_age_fare_survived(self):
        with self.step(
            "Create a scatter plot using the Domino Code Assist™, or your own Python code.",
            3.5,
        ):
            self.scroll_to_last_code_cell()
            self.page.wait_for_timeout(time_step)
            self.insert_code(
                """
import plotly.express as px

scatter_age_fare = px.scatter(df, x="age", y="fare", color="survived")
scatter_age_fare
""".strip(),
                delay=15,
            )
            self.page.wait_for_timeout(100)
            self.page.locator(".plotly-graph-div").last.scroll_into_view_if_needed()
            self.shot("create-viz-2")

    def step_app_open(self):
        with self.step("Click on 'App'", 2.5):
            self.assistant.app.menu_item.click()
            # self.shot("open")

    def step_app_toggle(self, names=[]):
        with self.step("Toggle the visualizations you want to add to the app.", 4):
            self.shot("app-before")
            for name in names:
                self.page.locator(f'_vue=v-switch[label="{name}"]').click()
                self.page.wait_for_timeout(1000)

    def step_deploy_open(self):
        with self.step("Click on 'Deploy'", 2.5):
            self.assistant.deploy.menu_item.click()
            self.shot("open")

    def step_deploy_write_script(self):
        with self.step(
            "Click on 'Write script' to write the script for the application", 2.5
        ):
            self.assistant.deploy.write_script.click()
            self.shot("write-script")

    def step_deploy_continue(self, n):
        with self.step("Click on 'Continue'", 2.5):
            self.assistant.deploy.continue_.locator(f"nth={n}").click()

    def step_deploy_start_app(self):
        with self.step("Click on 'Start app', and wait till the app is running", 2.5):
            self.assistant.deploy.start_app.click()
            self.assistant.deploy.app_running.wait_for()

    def step_deploy_finish(self):
        with self.step("Click on 'Finish'", 2.5):
            self.assistant.deploy.finish.click()

    def step_deploy_view_app(self):
        with self.step("Click on 'View app' to view the app", 2.5):
            anchor = self.assistant.deploy.view_app.locator("..")
            anchor.evaluate("node => console.log")
            anchor.evaluate("node => node.setAttribute('target', '_self')")
            anchor.evaluate(
                "node => node.setAttribute('href', 'https://trial.dominodatalab.com/modelproducts/62d57ca85ffd7972e1f36948')"
            )
            self.assistant.deploy.view_app.click()
            self.shot("view-app")


def general(locator, name):
    locator.screenshot(path=f"docs/screenshots/general/{name}.png")


@app.command()
def load_snowflake(
    port: int = 11111, headless: bool = True, animation_time: float = 0.3
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser, "load-snowflake", port=port, animation_time=animation_time
        )
        with helper:
            page = helper.page
            helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.assistant.click()
            page.locator("text=Domino Code Assist™ initialized").wait_for()
            helper.shot("assistant-read")

            mouse_move_middle(page, page.locator(".code_cell").last)
            page.wait_for_load_state("networkidle")
            helper.shot("assistant-visible")

            page.locator(".dominocode-assistant-menu").hover()
            page.wait_for_timeout(animation_time * 1000)  # animation
            helper.shot("assistant-expand")

            page.locator("text=Load Data").click()
            helper.shot("load-data")

            # Click on data source
            page.locator('div[role="button"]:has-text("Data Source")').click()
            helper.shot("choose-datasource")

            page.locator(
                'div[role="option"] div:has-text("mario_test_snowflake")'
            ).first.click()
            helper.shot("choose-datasource-first")

            page.locator('div[role="button"]:has-text("Database")').click()
            helper.shot("choose-database")

            page.locator('div[role="button"]:has-text("SNOWFLAKE_SAMPLE_DATA")').click()
            helper.shot("choose-database-first")

            page.locator('div[role="button"]:has-text("Schema")').click()
            helper.shot("choose-schema")

            page.locator("text=TPCDS_SF100TCL").click()
            helper.shot("choose-schema-first")

            page.locator('div[role="button"]:has-text("Table")').click()
            helper.shot("choose-table")

            page.locator("text=CALL_CENTER (60 rows)").click()
            helper.shot("choose-table-first")

            general(page.locator('button:has-text("insert code")'), "apply")
            page.locator('button:has-text("Insert code")').click()
            # wait for the dataframe to show
            page.locator("text=rows ×").wait_for()
            helper.shot("insert-code")


@app.command()
def load_redshift(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    general_screenshots: bool = True,
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser, "load-redshift", port=port, animation_time=animation_time
        )
        with helper:
            page = helper.page
            if not general_screenshots:
                helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.add_msg("Click the Domino Code Assist button", 2)
            helper.assistant.click()
            page.locator("text=Domino Code Assist™ initialized").wait_for()
            helper.shot("assistant-read")

            helper.add_msg("Hover above the next code cell", 2)
            mouse_move_middle(page, page.locator(".code_cell").last)
            page.wait_for_load_state("networkidle")
            helper.shot("assistant-visible")
            page.wait_for_timeout(time_step * 3)

            helper.add_msg("Open the assistant menu", 2)
            page.locator(".dominocode-assistant-menu").hover()
            helper.shot("assistant-expand")

            page.locator("text=Load Data").click()
            helper.shot("load-data")

            page.wait_for_timeout(
                animation_time * 4000
            )  # wait for the data sources to populate
            helper.add_msg("Choose a data source", 2)
            # Click on data source
            page.locator('div[role="button"]:has-text("Data Source")').click()
            helper.shot("choose-datasource")

            page.locator(
                'div[role="option"] div:has-text("mario_test_redshift")'
            ).first.click()
            helper.shot("choose-datasource-first")

            page.locator('div[role="button"]:has-text("Database")').click()
            helper.add_msg("Choose a database, schema, and table", 2)
            helper.shot("choose-database")

            page.locator('div[role="option"] div:has-text("dev") >> nth=0').click()
            helper.shot("choose-database-first")

            page.locator('div[role="button"]:has-text("Schema")').click()
            helper.shot("choose-schema")

            page.locator('div[role="option"] div:has-text("public") >> nth=0').click()
            helper.add_msg(
                "Click 'INSERT CODE' to insert the Python code into the current cell", 2
            )
            helper.shot("choose-schema-first")

            page.locator('div[role="button"]:has-text("Table")').click()
            helper.shot("choose-table")

            page.locator("text=venue").click()
            helper.shot("choose-table-first")

            locator = page.locator('button:has-text("Insert code")')
            if general_screenshots:
                general(locator, "apply")
            else:
                locator.wait_for()

            page.locator('button:has-text("Insert code")').click()
            helper.scroll_to_last_code_cell()
            # wait for the dataframe to show
            page.locator("text=rows ×").wait_for()
            page.locator("text=San Francisco Opera").scroll_into_view_if_needed()
            # helper.scroll_to_last_code_cell()
            helper.shot("insert-code")


@app.command()
def load_redshift_sql(
    port: int = 11111, headless: bool = True, animation_time: float = 0.3
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser, "load-redshift-sql", port=port, animation_time=animation_time
        )
        with helper:
            page = helper.page
            helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.add_msg("Click the Domino Code Assist button", 2)
            helper.assistant.click()
            page.locator("text=Domino Code Assist™ initialized").wait_for()
            helper.shot("assistant-read")

            helper.add_msg("Hover above the next code cell", 2)
            mouse_move_middle(page, page.locator(".code_cell").last)
            page.wait_for_load_state("networkidle")
            helper.shot("assistant-visible")
            page.wait_for_timeout(time_step * 3)

            helper.add_msg("Open the assistant menu", 2)
            page.locator(".dominocode-assistant-menu").hover()
            helper.shot("assistant-expand")

            page.locator("text=Load Data").click()
            helper.shot("load-data")

            page.wait_for_timeout(
                animation_time * 4000
            )  # wait for the data sources to populate
            helper.add_msg("Choose a data source", 2)
            # Click on data source
            page.locator('div[role="button"]:has-text("Data Source")').click()
            helper.shot("choose-datasource")

            page.locator(
                'div[role="option"] div:has-text("mario_test_redshift")'
            ).first.click()
            helper.shot("choose-datasource-first")

            page.locator('div[role="button"]:has-text("Database")').click()
            helper.add_msg("Choose a database and schema", 2)
            helper.shot("choose-database")

            page.locator('div[role="option"] div:has-text("dev") >> nth=0').click()
            helper.shot("choose-database-first")

            page.locator('div[role="button"]:has-text("Schema")').click()
            helper.shot("choose-schema")

            helper.add_msg("Toggle 'Use query'", 2)
            page.locator(".v-input--selection-controls__ripple").click()

            # wait for the widget, and scroll
            page.locator("text=for auto-complete").wait_for()
            page.locator("text=for auto-complete").scroll_into_view_if_needed()
            # seems it needs some extra time (maybe codemirror expands slowly)
            page.wait_for_timeout(time_step)
            page.locator("text=for auto-complete").scroll_into_view_if_needed()

            sql_input = page.locator("textarea").first
            helper.add_msg(
                "Enter your SQL query, and use <kbd>Ctrl</kbd>+<kbd>Space</kbd> for autocomplete",
                4,
            )
            delay = 130
            sql_input.focus()
            for char in "SELECT ":
                sql_input.press(char, delay=delay)
            for char in "venue.":
                sql_input.press(char, delay=delay)
            sql_input.press("Control+ ", delay=delay)
            for i in range(3):
                sql_input.press("ArrowDown", delay=delay)
            sql_input.press("Enter", delay=delay)
            for char in " FROM venue WHERE venue.v":
                sql_input.press(char, delay=delay)
            sql_input.press("Control+ ", delay=delay)
            for i in range(4):
                sql_input.press("ArrowDown", delay=delay)
            sql_input.press("Enter", delay=delay)
            for char in " > 10":
                sql_input.press(char, delay=delay)

            helper.add_msg(
                "Click 'INSERT CODE' to insert the Python code into the current cell", 2
            )
            page.wait_for_timeout(time_step * 4)

            page.locator('button:has-text("Insert code")').click()
            # a unique string from printing the dataframe
            page.locator("text=56").wait_for()
            helper.shot("insert-code")


@app.command()
def viz_scatter(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    general_screenshots: bool = True,
    fast: bool = False,
):
    def screenshot_or_wait(selector, path):
        if general_screenshots:
            selector.screenshot(path=path)
        else:
            selector.wait_for()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "viz-scatter",
            port=port,
            animation_time=animation_time,
            height=1024,
            fast=fast,
        )
        with helper:
            page = helper.page
            if not general_screenshots:
                helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.step_init()

            helper.step_cell_insert_code_load_titanic()
            helper.shot("load-data-code")

            helper.step_hover_cell()
            helper.step_hover_assistant_fab()

            helper.step_viz_open()

            helper.step_viz_pick_df("df")
            helper.step_viz_choose("Scatter")

            helper.step_viz_configure()

            helper.step_viz_choose_var("scatter_age_fare")

            helper.step_insert_code()

            with helper.step(
                "The code is inserted, and will be automatically executed", 2.5
            ):
                page.locator(".plotly-graph-div").wait_for()
                page.wait_for_timeout(100)
                page.locator(".plotly-graph-div").scroll_into_view_if_needed()
                helper.scroll_to_last_code_cell()
                helper.shot("insert-code")


@app.command()
def load_csv(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    general_screenshots: bool = True,
):
    def screenshot_or_wait(selector, path):
        if general_screenshots:
            selector.screenshot(path=path)
        else:
            selector.wait_for()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "load-csv",
            port=port,
            animation_time=animation_time,
        )
        with helper:

            page = helper.page
            if not general_screenshots:
                helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.step_init()

            helper.step_hover_cell()

            screenshot_or_wait(
                helper.assistant.domino_logo,
                path="docs/screenshots/general/assistant-icon.png",
            )

            helper.step_hover_assistant_fab()

            screenshot_or_wait(
                helper.assistant.load_data.menu_item.locator("xpath=../../.."),
                path="docs/screenshots/general/assistant-popup-menu.png",
            )
            screenshot_or_wait(
                helper.assistant.load_data.menu_item.locator("xpath=../.."),
                path="docs/screenshots/general/assistant-load-data.png",
            )

            helper.step_load_data_open()
            page.wait_for_timeout(time_step * 2)

            helper.step_load_data_tab_dataset_open()

            helper.step_load_data_tab_dataset_navigate()

            screenshot_or_wait(
                page.locator("text=titanic.csv>> xpath=../.."),
                path="docs/screenshots/general/assistant-dataset-titanic.png",
            )

            helper.step_load_data_tab_dataset_titanic_open()

            helper.step_insert_code()

            with helper.step(
                "The code is inserted, and will be automatically executed", 2.5
            ):
                helper.scroll_to_last_code_cell()
                helper.shot("load-data-titanic")

            page.wait_for_timeout(time_step * 2)


@app.command()
def transform(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    general_screenshots: bool = True,
):
    def screenshot_or_wait(selector, path):
        if general_screenshots:
            selector.screenshot(path=path)
        else:
            selector.wait_for()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "transform",
            port=port,
            animation_time=animation_time,
        )
        with helper:

            page = helper.page
            if not general_screenshots:
                helper.start_video()
            page.wait_for_timeout(time_step)
            helper.shot("initial")

            helper.step_init()

            helper.step_cell_insert_code_load_titanic()

            helper.step_hover_cell()
            helper.step_hover_assistant_fab()

            screenshot_or_wait(
                helper.assistant.transform.menu_item.locator("xpath=../.."),
                path="docs/screenshots/general/assistant-transformations.png",
            )

            helper.step_transform_open()
            helper.step_transform_pick_df("df")
            page.locator(".solara-data-table__viewport").wait_for()

            screenshot_or_wait(
                helper.assistant.transform.add_transformation,
                path="docs/screenshots/general/assistant-transformation-add.png",
            )

            helper.step_transform_table_cell_action_hover(10, 10)
            screenshot_or_wait(
                page.locator("text=Filter values like >> xpath=../.."),
                path="docs/screenshots/general/assistant-transformation-filter-like.png",
            )

            helper.step_transform_filter_values_like_open()

            helper.step_transform_filter_values_like_apply()
            screenshot_or_wait(
                page.locator("text=Apply >> xpath=.."),
                path="docs/screenshots/general/assistant-transformation-apply.png",
            )

            with helper.step("Click the 'Show code' toggle to preview the code", 2.5):
                page.wait_for_timeout(1500)
                toggle = (
                    ".v-input--switch:last-of-type .v-input--selection-controls__ripple"
                )

                screenshot_or_wait(
                    helper.assistant.transform.dialog.locator(f"{toggle}").last.locator(
                        "xpath=../.."
                    ),
                    path="docs/screenshots/general/assistant-transformation-toggle-code.png",
                )
                helper.assistant.transform.dialog.locator(toggle).last.click()
                page.wait_for_timeout(animation_time * 1000)  # animation
                page.locator(".solara-code-highlight").scroll_into_view_if_needed()
                helper.shot("show-code")
                page.wait_for_timeout(time_step)

            screenshot_or_wait(
                page.locator('button:has-text("Insert code")'),
                path="docs/screenshots/general/assistant-transformation-insert-code.png",
            )

            helper.step_insert_code()

            with helper.step(
                "The code is inserted, and will be automatically executed", 2.5
            ):
                helper.scroll_to_last_code_cell()
                helper.shot("insert-code")


@app.command()
def app_create(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    general_screenshots: bool = False,
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "app-create",
            port=port,
            animation_time=animation_time,
            height=1024,
        )
        with helper:
            page = helper.page

            if not general_screenshots:
                helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.step_init()
            helper.step_cell_insert_code_load_titanic()
            helper.shot("load-data")

            helper.step_cell_insert_code_histogram_survived()
            helper.step_cell_insert_code_scatter_age_fare_survived()

            helper.step_hover_cell()
            helper.step_hover_assistant_fab()
            locator = helper.assistant.app.menu_item
            if general_screenshots:
                general(locator, "app-open")
            helper.step_app_open()
            helper.step_app_toggle(["histogram_survived", "scatter_age_fare"])

            with helper.step("Optionally drag and resize the visualizations", 1.5):
                pass

            helper.step_insert_code()
            helper.shot("insert-code")

            with helper.step("Edit the code, or click 'Preview'", 2.0):
                helper.scroll_to_last_code_cell()
            helper.shot("done")
            locator = page.locator('button:has-text("Preview")')
            if general_screenshots:
                general(locator, "app-preview")
            else:
                locator.wait_for()

            page.wait_for_timeout(time_step * 2)


@app.command()
def deploy(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    # general_screenshots: bool = True,
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "deploy",
            port=port,
            animation_time=animation_time,
        )
        with helper:

            page = helper.page
            # if not general_screenshots:
            #     helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.step_init()
            helper.step_cell_insert_code_load_titanic()

            helper.step_cell_insert_code_histogram_survived()
            helper.step_cell_insert_code_scatter_age_fare_survived()

            if True:
                helper.step_hover_cell()
                helper.step_hover_assistant_fab()
                helper.step_app_open()
                helper.step_app_toggle(["histogram_survived", "scatter_age_fare"])

                with helper.step("Optionally drag and resize the visualizations", 1.5):
                    pass

                helper.step_insert_code()

                locator = page.locator('button:has-text("Preview")')
            else:
                helper.insert_code(" # fast path needs no real code")

            helper.remove_app_sh()

            helper.step_hover_cell()
            helper.step_hover_assistant_fab()
            helper.step_deploy_open()

            helper.step_deploy_write_script()
            helper.step_deploy_continue(0)

            with helper.step(
                "Follow the instructions to synchronize the filesystem", 2.5
            ):
                pass
            helper.step_deploy_continue(0)

            helper.step_deploy_start_app()
            helper.step_deploy_finish()
            helper.step_deploy_view_app()

            page.wait_for_timeout(500)
            page.locator("text=All Apps").wait_for()
            # a locator for the iframe of the app, this depends on the deployed app
            # so this may change
            page.frame_locator("iframe").locator("text=Madison").wait_for()
            helper.inject_js_and_css()
            with helper.step("The app can now be shared with others", 2.5):
                pass


@app.command()
def overview(
    port: int = 11111,
    headless: bool = True,
    animation_time: float = 0.3,
    screenshots: bool = False,
):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "overview",
            port=port,
            animation_time=animation_time,
            screenshots=screenshots,
        )
        with helper:

            page = helper.page
            if not screenshots:
                helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            with helper.step(
                "This video will demonstrate many of the features of Domino Code Assist™",
                2.5,
            ):
                pass

            # with helper.step("We will demonstrate deploying an app mixing ", 2.5):

            # load data
            helper.step_init()
            if True:
                helper.step_hover_cell()
                helper.step_hover_assistant_fab()
                helper.step_load_data_open()
                helper.step_load_data_tab_dataset_open()
                helper.step_load_data_tab_dataset_navigate()
                helper.step_load_data_tab_dataset_titanic_open()
                helper.step_insert_code()
                with helper.step(
                    "The code is inserted, and will be automatically executed", 2.5
                ):
                    helper.scroll_to_last_code_cell()
                    helper.shot("load-data-titanic")
            else:
                helper.step_cell_insert_code_load_titanic()

            with helper.step(
                "Next, we will filter the data using the Domino Code Assist™", 2.5
            ):
                pass

            # filter
            if True:
                helper.step_hover_cell()
                helper.step_hover_assistant_fab()
                helper.step_transform_open()
                helper.step_transform_pick_df("df")
                page.locator(".solara-data-table__viewport").wait_for()

                helper.step_transform_table_cell_action_hover(10, 10)

                helper.step_transform_filter_values_like_open()

                helper.step_transform_filter_values_like_apply()

                with helper.step(
                    "Click the 'Show code' toggle to preview the code", 2.5
                ):
                    page.wait_for_timeout(1500)
                    toggle = ".v-input--switch:last-of-type .v-input--selection-controls__ripple"

                    helper.assistant.transform.dialog.locator(toggle).last.click()
                    page.wait_for_timeout(animation_time * 1000)  # animation
                    page.locator(".solara-code-highlight").scroll_into_view_if_needed()
                    helper.shot("show-code")
                    page.wait_for_timeout(time_step)

                helper.step_insert_code()

                with helper.step(
                    "The code is inserted, and will be automatically executed", 2.5
                ):
                    helper.scroll_to_last_code_cell()
                    helper.shot("insert-code")
            else:
                helper.insert_code("df = df[~df.cabin.isna()]")

            # viz
            if True:
                with helper.step("Next, we will create two visualizations", 1.5):
                    pass
                helper.step_hover_cell()
                helper.step_hover_assistant_fab()

                helper.step_viz_open()

                helper.step_viz_pick_df("df")
                helper.step_viz_choose("Scatter")

                helper.step_viz_configure()

                helper.step_viz_choose_var("scatter_age_fare")

                helper.step_insert_code()

                with helper.step(
                    "The code is inserted, and will be automatically executed", 2.5
                ):
                    page.locator(".plotly-graph-div").wait_for()
                    page.wait_for_timeout(100)
                    page.locator(".plotly-graph-div").scroll_into_view_if_needed()
                    helper.scroll_to_last_code_cell()
                    helper.shot("insert-code")
            else:
                helper.step_cell_insert_code_scatter_age_fare_survived()

            with helper.step(
                "Our second visualization, is done without the Domino Code Assist™", 1.5
            ):
                pass

            helper.step_cell_insert_code_histogram_survived()

            # create app
            helper.step_hover_cell()
            helper.step_hover_assistant_fab()
            helper.step_app_open()
            helper.step_app_toggle(["histogram_survived", "scatter_age_fare"])

            with helper.step("Optionally drag and resize the visualizations", 1.5):
                pass

            helper.step_insert_code()

            locator = page.locator('button:has-text("Preview")')
            # if general_screenshots:
            #     general(locator, "app-preview")
            # else:
            #     locator.wait_for()
            locator.wait_for()

            # deploy
            helper.remove_app_sh()

            helper.step_hover_cell()
            helper.step_hover_assistant_fab()
            helper.step_deploy_open()

            helper.step_deploy_write_script()
            helper.step_deploy_continue(0)

            with helper.step(
                "Follow the instructions to synchronize the filesystem", 2.5
            ):
                pass
            helper.step_deploy_continue(0)

            helper.step_deploy_start_app()
            helper.step_deploy_finish()
            helper.step_deploy_view_app()

            page.wait_for_timeout(500)
            page.locator("text=All Apps").wait_for()
            # a locator for the iframe of the app, this depends on the deployed app
            # so this may change
            page.frame_locator("iframe").locator("text=Madison").wait_for()
            helper.inject_js_and_css()
            with helper.step("The app can now be shared with others", 2.5):
                pass


@app.command()
def audio(name: str):
    # print(name, directory)
    from pydub import AudioSegment

    files = Path(f"audio/{name}/").glob("*.mp3")
    files = list(sorted(files))
    print(files)
    steps = json.loads(Path(f"scripts/{name}.json").read_text())
    segments = [AudioSegment.from_file(file, format="mp3") for file in files]
    sound_all = None
    offset = steps[0]["t_start"] * 1000
    offset = 0
    sound_all = AudioSegment.silent(
        duration=get_video_length(f'docs/videos/{name}-cut.mp4') * 1000
    )
    for step, file, segments in zip(steps, files, segments):
        print(step, offset)
        sound_all = sound_all.overlay(
            segments, position=step["t_start"] * 1000 - offset
        )
    sound_all.export(f"audio/{name}.mp3", format="mp3")

    cmd = f"ffmpeg -y -i docs/videos/{name}-cut.mp4 -i audio/{name}.mp3 -map 0:v -map 1:a -c:v copy -shortest docs/videos/{name}-audio.mp4"
    os.system(cmd)


if __name__ == "__main__":
    # typer.run(main)
    app()
