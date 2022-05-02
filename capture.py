import os
import shutil
import time
from pathlib import Path

import typer
from playwright.sync_api import sync_playwright, Page, Browser

HERE = Path(__file__).parent
app = typer.Typer()


timeout = 500000
time_step = 500

# if in a hurry, and want to test
# time_step = 0


class CaptureHelper:
    page: Page

    def __init__(self, browser: Browser, name, port, animation_time, height=720):
        self.browser = browser
        self.name = name
        self.port = port
        self.animation_time = animation_time
        self.height = height
        self.N = 0  # screenshot number
        # TODO: this should actually happen at the server
        shutil.copy(
            "notebooks/empty.ipynb",
            f"notebooks/{self.name}.ipynb",
        )

    def __enter__(self):
        self.time_start = time.time()
        self.page = self.browser.new_page(
            device_scale_factor=2,
            record_video_dir="docs/videos",
            viewport={"width": 1280, "height": self.height},
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
        self.assistant.wait_for()

        # get rid of connected icon and make sure it's stable
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(200)

    def insert_code(self, code, delay=7):
        input = self.page.locator("textarea").last
        input.type(code, delay=delay)

        input = self.page.locator("text=In [ ]:").last
        input.press("Shift+Enter")

    @property
    def assistant(self):
        return self.page.locator('[aria-label="Assistant"]')

    def shot(self, name):
        self.page.wait_for_timeout(self.animation_time * 1000)
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
        if exception is None:
            print("Trimming", self.time_initial - self.time_start)
            video_path_raw = video_path.parent / f"{self.name}-raw.webm"
            video_path_cut = video_path.parent / f"{self.name}.webm"
            video_path_cut_mp4 = video_path.parent / f"{self.name}.mp4"
            shutil.move(video_path, video_path_raw)
            cmd = f"ffmpeg -y -i {video_path_raw}  -ss 2.38 -c copy {video_path_cut}"
            os.system(cmd)
            cmd = f"ffmpeg -y -i {video_path_cut} -vcodec libx264 -crf 23 {video_path_cut_mp4}"
            os.system(cmd)


def general(locator, name):
    locator.screenshot(path="docs/screenshots/general/{name}.png")


def mouse_move_middle(page, locator):
    box = locator.bounding_box()
    x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
    page.mouse.move(0, 0)
    page.mouse.move(x, y, steps=1)


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
            page.locator("text=Assistant initialized").wait_for()
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

            page.locator("text=SNOWFLAKE_SAMPLE_DATA").click()
            helper.shot("choose-database-first")

            page.locator('div[role="button"]:has-text("Schema")').click()
            helper.shot("choose-schema")

            page.locator("text=TPCDS_SF100TCL").click()
            helper.shot("choose-schema-first")

            page.locator('div[role="button"]:has-text("Table")').click()
            helper.shot("choose-table")

            page.locator("text=CALL_CENTER (60 rows)").click()
            helper.shot("choose-table-first")

            general(page.locator('button:has-text("apply")'), "apply")
            page.locator('button:has-text("apply")').click()
            # wait for the dataframe to show
            page.locator("text=rows ×").wait_for()
            helper.shot("insert-code")


@app.command()
def viz_scatter(port: int = 11111, headless: bool = True, animation_time: float = 0.3):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        helper = CaptureHelper(
            browser,
            "viz-scatter",
            port=port,
            animation_time=animation_time,
            height=1024,
        )
        with helper:
            page = helper.page
            helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.assistant.click()
            page.locator("text=Assistant initialized").wait_for()
            helper.shot("assistant-ready")

            page.wait_for_load_state("networkidle")
            helper.shot("assistant-visible")

            path_csv = "../mydata/titanic.csv"
            helper.insert_code(
                f"""import pandas as pd
df = pd.read_csv("{path_csv}")
df.head(2)"""
            )
            page.locator("text=pclass").wait_for()
            helper.shot("load-data-code")

            mouse_move_middle(page, page.locator(".code_cell").last)
            page.locator(".dominocode-assistant-menu").hover()
            page.wait_for_timeout(animation_time * 1000)  # animation
            helper.shot("assistant-expand")

            page.locator("text=Visualizations").click()
            helper.shot("open")

            page.locator('div[role="button"]:has-text("DataFrame")').click()
            helper.shot("choose-df")
            page.locator('div[role="option"] div:has-text("df")').first.click()
            helper.shot("choose-df-first")
            page.locator("text=Variable name >> xpath=.. >> input").click()
            helper.shot("choose-name")
            page.locator("text=Variable name >> xpath=.. >> input").type(
                "scatter1", delay=10
            )
            helper.shot("choose-name-scatter1")
            page.locator('div[role="button"]:has-text("Plot Type")').click()
            helper.shot("choose-type")
            page.locator('div[role="option"] >> text=Scatter').first.click()
            helper.shot("choose-type-scatter")

            page.locator('div[role="button"]:has-text("X-axis")').click()
            helper.shot("choose-x")
            page.locator('div[role="option"] >> text=age').click()
            helper.shot("choose-x-age")
            page.locator('div[role="button"]:has-text("Y-axis")').click()
            helper.shot("choose-y")
            page.locator('div[role="option"] >> text=fare').last.click()
            helper.shot("choose-y-fare")

            # get viz into view
            page.locator(
                'button:has-text("Insert code")' ""
            ).scroll_into_view_if_needed()

            page.locator('div[role="button"]:has-text("Color")').click()
            helper.shot("choose-color")
            page.locator('div[role="option"] >> text=pclass').last.click()
            helper.shot("choose-color-pclass")
            page.locator("text=Options").click()
            helper.shot("expand-options")
            page.locator('div[role="button"]:has-text("Theme")').click()
            helper.shot("choose-theme")
            page.locator('div[role="option"] >> text=ggplot2').first.click()
            helper.shot("choose-theme-ggplot2")
            page.locator('button:has-text("Insert code")').click()
            page.locator(".plotly-graph-div").wait_for()
            # give some time to layout
            page.wait_for_timeout(100)
            page.locator(".plotly-graph-div").scroll_into_view_if_needed()
            helper.shot("insert-code")


@app.command()
def load_csv(port: int = 11111, headless: bool = True, animation_time: float = 0.3):
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
            helper.start_video()
            # a bit of rest
            page.wait_for_timeout(time_step)

            helper.shot("initial")

            helper.assistant.click()
            page.locator("text=Assistant initialized").wait_for()
            helper.shot("assistant-ready")

            mouse_move_middle(page, page.locator(".code_cell").last)
            page.wait_for_load_state("networkidle")
            helper.shot("assistant-visible")

            page.locator(".dominocode-assistant-menu").screenshot(
                path="docs/screenshots/general/assistant-icon.png"
            )

            page.locator(".dominocode-assistant-menu").hover()
            page.wait_for_timeout(animation_time * 1000)  # animation
            helper.shot("assistant-expand")

            page.locator("text=Load Data >> xpath=../../..").screenshot(
                path="docs/screenshots/general/assistant-popup-menu.png"
            )

            page.locator("text=Load Data >> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-load-data.png"
            )

            page.locator("text=Load Data").click()
            helper.shot("load-data")

            page.locator("text=Datasets").click()
            helper.shot("load-data-datasets")

            page.locator('div[role="list"] div:has-text("..")').nth(1).click()
            helper.shot("load-data-datasets-dir-up")

            page.locator("text=mydata").click()
            helper.shot("load-data-datasets-dir-mydata")

            page.locator("text=titanic.csv>> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-dataset-titanic.png"
            )

            page.locator("text=titanic.csv").click()
            helper.shot("load-data-titanic")


@app.command()
def transform(port: int = 11111, headless: bool = True, animation_time: float = 0.3):
    # TODO: needs refactor to use the Helper
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        # recordVideo: { dir: 'videos/' }
        time_start = time.time()
        page = browser.new_page(
            record_video_dir="docs/videos"
        )  # , record_video_size=ViewportSize(width=1000, height=1000))
        video_path = Path(page.video.path())
        succes = False
        shutil.copy(
            "notebooks/empty.ipynb",
            "notebooks/transform-demo.ipynb",
        )
        try:
            page.set_default_timeout(timeout=timeout)
            page.goto(f"http://localhost:{port}/notebooks/transform-demo.ipynb")

            # restart kernel
            page.locator("#kernellink").click()
            page.locator('span:has-text("Restart")').click()
            page.locator('button:has-text("Restart")').click()
            assistant = page.locator('[aria-label="Assistant"]')
            # box = assistant.bounding_box()
            # get rid of connected icon and make sure it's stable
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(200)

            N = 0
            time_step = 500

            # here is where we start the trim
            time_initial = time.time()

            page.wait_for_timeout(time_step)
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-initial.png")
            page.wait_for_timeout(time_step)
            N += 1

            assistant.click()
            page.locator("text=Assistant initialized").wait_for()
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-assistant-ready.png"
            )
            N += 1

            path_csv = HERE / "mydata/titanic.csv"
            code = f"""import pandas as pd

df = pd.read_csv("{path_csv}")
df.head(2)"""
            input = page.locator("text=In [ ]: ​ >> textarea").last
            input.type(code, delay=7)

            input = page.locator("text=In [ ]:").last
            input.press("Shift+Enter")

            page.locator("text=pclass").wait_for()

            page.wait_for_timeout(time_step)
            # page.evaluate("""window.scrollTo(0, document.body.scrollHeight);""")

            last_code_cell = page.locator(".code_cell").last
            last_code_cell.scroll_into_view_if_needed()
            box = last_code_cell.bounding_box()
            x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
            page.mouse.move(0, 0)
            page.mouse.move(x, y, steps=1)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(100)
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-assistant-visible.png"
            )
            page.wait_for_timeout(time_step)
            N += 1
            # page.evaluate("""window.scrollTo(0, document.body.scrollHeight);""")

            page.locator(".dominocode-assistant-menu").hover()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-assistant-expand.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=Transformations >> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-transformations.png"
            )

            page.locator("text=Transformations").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-transformations.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            page.locator('div[role="button"]:has-text("DataFrame")').click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-choose-dataframe.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            # page.locator("div[role=\"option\"] >> text=df").dispatch_event("mousedown")
            page.locator('div[role="option"] >> text=df').click()
            page.locator('div[role="option"] >> text=df').wait_for(state="detached")
            # page.locator("div[role=\"listbox\"]:has-text(\"df\")").dispatch_event("mousedown")
            # page.locator("div[role=\"listbox\"]:has-text(\"df\")").click()
            # page.locator("div[role=\"menuitem\"] i").click()

            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/transform/{N:02}-pick-dataframe.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=Add transformation >> xpath=..").screenshot(
                path="docs/screenshots/general/assistant-transformation-add.png"
            )

            page.locator("tr:nth-child(10) td:nth-child(11) span .v-icon").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-popup-menu.png")
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=Filter values like >> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-transformation-filter-like.png"
            )

            page.locator("text=Filter values like").click()
            page.locator("text=New dataframe name").wait_for()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-filter-nan.png")
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=Apply >> xpath=..").screenshot(
                path="docs/screenshots/general/assistant-transformation-apply.png"
            )

            page.locator("text=Apply").click()
            page.locator("text=New dataframe name").wait_for(state="detached")
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-filtered.png")
            page.wait_for_timeout(time_step)
            N += 1

            toggle = "div:nth-child(8) .v-input__control .v-input__slot .v-input--selection-controls__input .v-input--selection-controls__ripple"

            page.locator(f"{toggle} >> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-transformation-toggle-code.png"
            )
            page.locator(toggle).click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-show-code.png")
            page.wait_for_timeout(time_step)
            N += 1

            page.locator('button:has-text("Insert code")').screenshot(
                path="docs/screenshots/general/assistant-transformation-insert-code.png"
            )
            page.locator('button:has-text("Insert code")').click()
            page.locator("text=In [ ]:").last.scroll_into_view_if_needed()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.locator("text=In [ ]:").last.scroll_into_view_if_needed()
            page.screenshot(path=f"docs/screenshots/transform/{N:02}-insert-code.png")
            page.wait_for_timeout(time_step)
            N += 1

            # # Click text=Datasets
            # page.locator("text=Datasets").click()
            # page.wait_for_timeout(animation_time*1000)  # animation
            # page.screenshot(path=f"docs/screenshots/{N:02}-load-data-datasets.png")
            # page.wait_for_timeout(time_step)
            # N += 1

            succes = True
        finally:
            page.close()
            browser.close()
            if succes:
                print("Trimming", time_initial - time_start)
                video_path_raw = video_path.parent / "transform-raw.webm"
                video_path_cut = video_path.parent / "transform.webm"
                shutil.move(video_path, video_path_raw)
                cmd = (
                    f"ffmpeg -y -i {video_path_raw}  -ss 2.38 -c copy {video_path_cut}"
                )
                os.system(cmd)
            else:
                os.remove(video_path)


if __name__ == "__main__":
    # typer.run(main)
    app()
