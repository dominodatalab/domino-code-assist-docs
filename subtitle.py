import pysubs2
import glob
import re
import os
import os.path
import sys

PADDING = 70
FONTSIZE = 50
FPS = 5
IMAGE_FORMAT = "png"

MP4 = sys.argv[1]
GIF = re.sub("mp4", "gif", MP4)
SUB = re.sub("mp4", "sub", MP4)

MP4_FOLDER = os.path.dirname(MP4)
FRAMES_FOLDER = os.path.join(MP4_FOLDER, "frames")

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
    f"{FRAMES_FOLDER}/frame-%03d.{IMAGE_FORMAT}",
]

CMD = " ".join(CMD)

os.system(CMD)
print("Done!")

FILES = glob.glob(f"{FRAMES_FOLDER}/frame-" + ("[0-9]" * 3) + f".{IMAGE_FORMAT}")
FILES.sort()

print(f"Created {len(FILES)} frames.")

# LOAD SUBTITLES ------------------------------------------------------------------------------------------------------

subs = pysubs2.load(SUB, encoding="utf-8", fps=1)

# Convert times (milliseconds) to frame number.
#
for line in subs:
    line.end = int(line.end / 1000 + 1)
    line.start = int(line.start / 1000 + 1)


def subtitle(frame_number):
    for line in subs:
        if frame_number >= line.start and frame_number <= line.end:
            return line.text


# ADD SUBTITLES -------------------------------------------------------------------------------------------------------


def frame_number(filename):
    match = re.search("frame-(.*).png$", filename, re.IGNORECASE)
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

# CREATE GIF ----------------------------------------------------------------------------------------------------------

CMD = [
    "gifski",
    "-q",
    f"-o {GIF}",
    f"--fps {FPS}",
    "--width 1280",
    "--quality 100",
] + PADDED
CMD = " ".join(CMD)

os.system(CMD)

print(f"Output file: {GIF}")

# CLEANUP -------------------------------------------------------------------------------------------------------------

for padded in PADDED:
    try:
        os.remove(padded)
    except FileNotFoundError:
        pass
