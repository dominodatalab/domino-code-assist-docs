import pysubs2
import glob
import re
import os
import os.path
import shutil
import tempfile
import sys
from PIL import Image
import yaml
from yaml.loader import SafeLoader
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)7s] %(message)s",
)
logging.getLogger("PIL").setLevel(logging.WARNING)


# LOAD CONFIGURATION YAML ---------------------------------------------------------------------------------------------

FOLDER = os.path.normpath(sys.argv[1])

CONFIG = os.path.join(FOLDER, "config.yml")

with open(CONFIG) as f:
    config = yaml.load(f, Loader=SafeLoader)

TITLE = config.get("title")

# LOAD CAPTIONS -------------------------------------------------------------------------------------------------------

try:
    with tempfile.NamedTemporaryFile("wt", suffix=".sub") as f:
        f.write(config["captions"])
        f.seek(0)
        subs = pysubs2.load(f.name, encoding="utf-8", fps=1)
except KeyError:
    subs = None

# ---------------------------------------------------------------------------------------------------------------------

PADDING = 80
FONTSIZE = 60
FPS = 5
IMAGE_FORMAT = "png"

MP4 = os.path.join(FOLDER, "video.mp4")

DOMINO_LOGO_PATH = "docs/domino-logo.png"

FRAMES_FOLDER = os.path.join(FOLDER, "frames")

GIF = os.path.join(FOLDER, os.path.split(FOLDER)[-1] + ".gif")
GIF_TITLE = os.path.join(FOLDER, os.path.split(FOLDER)[-1] + "-title.gif")

# Delete frames folder (and all old frames files!).
try:
    shutil.rmtree(FRAMES_FOLDER)
except FileNotFoundError:
    pass

# Create frames folder.
try:
    os.mkdir(FRAMES_FOLDER)
except FileExistsError:
    pass

# SPLIT VIDEO INTO FRAMES ---------------------------------------------------------------------------------------------

logging.info("Splitting MP4 into frames... ")
CMD = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel error",
    f"-i {MP4}",
    f"-r {FPS}",
    f"{FRAMES_FOLDER}/%05d-frame.{IMAGE_FORMAT}",
]

CMD = " ".join(CMD)

os.system(CMD)
logging.info("Done!")

FILES = glob.glob(f"{FRAMES_FOLDER}/" + ("[0-9]" * 5) + f"-frame.{IMAGE_FORMAT}")
FILES.sort()

logging.info(f"Created {len(FILES)} frames.")

# LOAD SUBTITLES ------------------------------------------------------------------------------------------------------

# Convert times (milliseconds) to frame number.
#
if subs:
    for line in subs:
        line.end = int(line.end / 1000)
        line.start = int(line.start / 1000)


def subtitle(frame_number):
    if subs:
        for line in subs:
            if frame_number >= line.start and frame_number <= line.end:
                return line.text


# ADD SUBTITLES -------------------------------------------------------------------------------------------------------


def frame_number(filename):
    match = re.search("([0-9]*)-frame.png$", filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    else:
        return None


for frame in FILES:
    n = frame_number(frame)
    text = subtitle(n)

    padded = re.sub("/frame-", "/frame-padded-", frame)

    logging.debug(str(n) + ": " + (text or ""))

    CMD = [
        "convert",
        frame,
        "-gravity south",
        "-background black",
        "-fill white",
        f"-splice 0x{PADDING}",
        "-font Arial",
        f"-pointsize {FONTSIZE}",
        f"-annotate +0+8 '{text}'" if text else "",
        frame,
    ]
    CMD = " ".join(CMD)

    os.system(CMD)

# FIND IMAGE SIZE -----------------------------------------------------------------------------------------------------

widths, heights = set(), set()

for padded in FILES:
    img = Image.open(padded)
    #
    logging.debug(f"{padded:<20}: {img.width}x{img.height}")
    #
    widths.add(img.width)
    heights.add(img.height)

assert len(widths) == 1
assert len(heights) == 1

PADDED_WIDTH = list(widths)[0]
PADDED_HEIGHT = list(heights)[0]

# CREATE COVER --------------------------------------------------------------------------------------------------------

CMD = [
    "convert",
    f"-size {PADDED_WIDTH}x{PADDED_HEIGHT}",
    "canvas:black",
    "label-background.png",
]

os.system(" ".join(CMD))

CMD = [
    "convert",
    "label-background.png",
    "-fill white",
    "-font Arial",
    "-pointsize 120",
    "-gravity north",
    f"-annotate +0+450 '{TITLE}'",
    "-fill '#bbbbbb'",
    "-pointsize 64",
    f"-annotate +0+595 'with Low Code Assistant (LCA)'",
    "-fill '#0072cd'",
    "-pointsize 48",
    "-gravity southeast",
    "-annotate +32+16 'http://dominodatalab.com/'",
    "label-title.png",
]

os.system(" ".join(CMD))

CMD = [
    "convert",
    "label-title.png",
    f"\( {DOMINO_LOGO_PATH} -scale 22% \)",
    "-gravity southeast",
    "-geometry +32+80",
    f"-composite {FRAMES_FOLDER}/00000-title.png",
]

os.system(" ".join(CMD))

TITLE = os.path.join(FRAMES_FOLDER, "00000-title.png")

# CREATE GIF ----------------------------------------------------------------------------------------------------------

# Replicate last frame.
#
FILES = FILES + FILES[-1:] * (FPS * 2)


def create_gif(gif, title=False):
    CMD = [
        "gifski",
        "-q",
        f"-o {gif}",
        f"--fps {FPS}",
        f"--width {PADDED_WIDTH}",
        "--quality 100",
    ]

    if title:
        CMD += [TITLE] * 10

    CMD += FILES

    CMD = " ".join(CMD)

    os.system(CMD)

    logging.info(f"Output file: {gif}")


create_gif(GIF, title=False)
create_gif(GIF_TITLE, title=True)

# CREATE MP4 ----------------------------------------------------------------------------------------------------------


def create_mp4(gif, mp4):
    img = Image.open(gif)

    CMD = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel error",
        "-y",
        f"-i {gif}",
        f"-s {img.width}x{img.height}",
        "-vcodec libx264",
        f"-crf {FPS}",
        mp4,
    ]

    CMD = " ".join(CMD)

    os.system(CMD)

    logging.info(f"Output file: {mp4}")


MP4 = re.sub("gif$", "mp4", GIF)
MP4_TITLE = re.sub("gif$", "mp4", GIF_TITLE)


create_mp4(GIF, MP4)
create_mp4(GIF_TITLE, MP4_TITLE)
