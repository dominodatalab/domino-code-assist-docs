#!/bin/bash

FPS=5

MP4=$1

MP4_FOLDER=$(dirname $MP4)
MP4_FILENAME=$(basename $MP4)

GIF=$(echo $MP4 | sed 's/mp4/gif/')

IMAGE_FORMAT=png

PADDING=50

mkdir -p $MP4_FOLDER/frames

echo -n "Splitting MP4 into frames... "
ffmpeg -hide_banner -loglevel error -i $MP4  -r $FPS "$MP4_FOLDER/frames/frame-%03d.$IMAGE_FORMAT"
echo "Done!"

echo -n "Adding padding to frames... "
for frame in $MP4_FOLDER/frames/frame-*.$IMAGE_FORMAT
do
    padded=$(echo $frame | sed 's/frame-/padded-frame-/')

    # Add padding.
    # convert -background black $frame -extent 1920x1180 -gravity north $padded

    # Add padding and annotation.
    convert $frame \
        -gravity south \
        -background black \
        -fill white \
        -splice 0x$PADDING \
        -font Arial \
        -pointsize 40 \
        -annotate +0+2 'Faerie Dragon' \
        $padded
done
# echo "Done!"

echo -n "Compiling frames into GIF... "
gifski -q -o $GIF --fps 5 --width 1280 --quality 100 $MP4_FOLDER/frames/padded-frame-*.$IMAGE_FORMAT
echo "Done!"

echo "Output file: $GIF"