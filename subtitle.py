import pysubs2
import glob
import re
import os
import os.path
import sys
from PIL import Image

PADDING = 70
FONTSIZE = 50
FPS = 5
IMAGE_FORMAT = "png"

MP4 = sys.argv[1]
SUB = re.sub("mp4", "sub", MP4)

MP4_FOLDER = os.path.dirname(MP4)
FRAMES_FOLDER = os.path.join(MP4_FOLDER, "frames")

GIF = os.path.join(MP4_FOLDER, os.path.split(MP4_FOLDER)[-1] + ".gif")

try:
    os.mkdir(FRAMES_FOLDER)
except FileExistsError:
    pass

# SPLIT VIDEO INTO FRAMES ---------------------------------------------------------------------------------------------

print("Splitting MP4 into frames... ", end="", flush=True)
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
print("Done!")

FILES = glob.glob(f"{FRAMES_FOLDER}/" + ("[0-9]" * 5) + f"-frame.{IMAGE_FORMAT}")
FILES.sort()

print(f"Created {len(FILES)} frames.")

# LOAD SUBTITLES ------------------------------------------------------------------------------------------------------

subs = pysubs2.load(SUB, encoding="utf-8", fps=1)

# Convert times (milliseconds) to frame number.
#
for line in subs:
    line.end = int(line.end / 1000)
    line.start = int(line.start / 1000)


def subtitle(frame_number):
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


PADDED = []

for frame in FILES:
    n = frame_number(frame)
    text = subtitle(n)

    padded = re.sub("/frame-", "/frame-padded-", frame)

    print(str(n) + ": " + (text or ""))

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
        padded,
    ]
    CMD = " ".join(CMD)

    os.system(CMD)

    PADDED.append(padded)

# Replicate last frame.
#
PADDED = PADDED + PADDED[-1:] * (FPS * 2)

# FIND IMAGE SIZE -----------------------------------------------------------------------------------------------------

widths, heights = set(), set()

for padded in list(set(PADDED)):
    img = Image.open(padded)
    #
    widths.add(img.width)
    heights.add(img.height)

assert len(widths) == 1
assert len(heights) == 1

PADDED_WIDTH = list(widths)[0]
PADDED_HEIGHT = list(heights)[0]

# CREATE COVER --------------------------------------------------------------------------------------------------------

# convert -size 1920x1150 canvas:black label-background.png
# convert label-background.png -fill white -font Arial -pointsize 120 -gravity center -annotate +0+0 'Importing Data from S3' -fill "#0072cd" -pointsize 48 -gravity southeast -annotate +32+16 'http://dominodatalab.com/' -pointsize 72 -annotate +32+64 "Domino Data Lab" label-title.png
# convert label-title.png \( domino-logo.png -scale 22% \) -gravity southeast -geometry +32+80 -composite 00000-title.png

TITLE = os.path.join(FRAMES_FOLDER, "00000-title.png")

# CREATE GIF ----------------------------------------------------------------------------------------------------------

CMD = (
    [
        "gifski",
        "-q",
        f"-o {GIF}",
        f"--fps {FPS}",
        "--width 1280",
        "--quality 100",
    ]
    + [TITLE] * 5
    + PADDED
)
CMD = " ".join(CMD)

print(CMD)

os.system(CMD)

print(f"Output file: {GIF}")

# CLEANUP -------------------------------------------------------------------------------------------------------------

# for padded in PADDED:
#     try:
#         os.remove(padded)
#     except FileNotFoundError:
#         pass
