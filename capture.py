import os
import shutil
import time
from pathlib import Path

import typer
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
app = typer.Typer()


timeout = 5000


@app.command()
def load(port: int = 11111, headless: bool = True, animation_time: float = 0.3):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, timeout=timeout)
        # recordVideo: { dir: 'videos/' }
        time_start = time.time()
        page = browser.new_page(
            record_video_dir="docs/videos"
        )  # , record_video_size=ViewportSize(width=1000, height=1000))
        video_path = Path(page.video.path())
        succes = False
        try:
            shutil.copy(
                "notebooks/empty.ipynb",
                "notebooks/load-demo.ipynb",
            )
            page.set_default_timeout(timeout=timeout)
            page.goto(f"http://localhost:{port}/notebooks/load-demo.ipynb")

            # restart kernel
            page.locator("#kernellink").click()
            page.locator('span:has-text("Restart")').click()
            page.locator('button:has-text("Restart")').click()
            assistant = page.locator('[aria-label="Assistant"]')

            # get rid of connected icon and make sure it's stable
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(200)

            N = 0
            time_step = 500

            # here is where we start the trim
            time_initial = time.time()

            page.wait_for_timeout(time_step)
            page.screenshot(path=f"docs/screenshots/{N:02}-initial.png")
            page.wait_for_timeout(time_step)
            N += 1

            assistant.click()
            page.locator("text=Assistant initialized").wait_for()
            page.screenshot(path=f"docs/screenshots/{N:02}-assistant-ready.png")
            N += 1

            last_code_cell = page.locator(".code_cell").last
            box = last_code_cell.bounding_box()
            x, y = box["x"] + box["width"] / 2, box["y"] + box["height"] / 2
            page.mouse.move(0, 0)
            page.mouse.move(x, y, steps=1)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(100)
            page.screenshot(path=f"docs/screenshots/{N:02}-assistant-visible.png")
            page.wait_for_timeout(time_step)
            N += 1

            page.locator(".dominocode-assistant-menu").screenshot(
                path="docs/screenshots/general/assistant-icon.png"
            )

            page.locator(".dominocode-assistant-menu").hover()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/{N:02}-assistant-expand.png")
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=Load Data >> xpath=../../..").screenshot(
                path="docs/screenshots/general/assistant-popup-menu.png"
            )

            page.locator("text=Load Data >> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-load-data.png"
            )

            page.locator("text=Load Data").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/{N:02}-load-data.png")
            page.wait_for_timeout(time_step)
            N += 1

            # Click text=Datasets
            page.locator("text=Datasets").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/{N:02}-load-data-datasets.png")
            page.wait_for_timeout(time_step)
            N += 1

            # Click div[role="list"] div:has-text("..") >> nth=1
            page.locator('div[role="list"] div:has-text("..")').nth(1).click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/{N:02}-load-data-datasets-dir-up.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            # Click text=mydata
            page.locator("text=mydata").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(
                path=f"docs/screenshots/{N:02}-load-data-datasets-dir-mydata.png"
            )
            page.wait_for_timeout(time_step)
            N += 1

            page.locator("text=titanic.csv>> xpath=../..").screenshot(
                path="docs/screenshots/general/assistant-dataset-titanic.png"
            )

            # Click text=titanic.csv
            page.locator("text=titanic.csv").click()
            page.wait_for_timeout(animation_time * 1000)  # animation
            page.screenshot(path=f"docs/screenshots/{N:02}-load-data-titanic.png")
            page.wait_for_timeout(time_step)
            N += 1

            succes = True
        finally:
            page.close()
            browser.close()
            if succes:
                print("Trimming", time_initial - time_start)
                video_path_raw = video_path.parent / "intro-raw.webm"
                video_path_cut = video_path.parent / "intro.webm"
                shutil.move(video_path, video_path_raw)
                cmd = (
                    f"ffmpeg -y -i {video_path_raw}  -ss 2.38 -c copy {video_path_cut}"
                )
                os.system(cmd)


@app.command()
def transform(port: int = 11111, headless: bool = True, animation_time: float = 0.3):
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
