#!/bin/bash

# Generate logo background
Rscript docs/scripts/logo.R
if [ -f "Rplots.pdf" ]; then
    rm Rplots.pdf
fi

# Generate text image and compose with background due to
# limited ligatures support in hexSticker and ImageMagick.
if [[ "$OSTYPE" == "darwin"* ]]; then
    CHROME_BIN="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    CHROME_BIN="/c/Program Files/Google/Chrome/Application/chrome.exe"
else
    CHROME_BIN="/usr/bin/google-chrome"
fi

if [ ! -f "$CHROME_BIN" ]; then
    echo "Chrome/Chromium not found at $CHROME_BIN"
    exit 1
fi

alias chrome="\"$CHROME_BIN\""

chrome --headless \
    --disable-gpu \
    --no-margins \
    --no-pdf-header-footer \
    --print-to-pdf-no-header \
    --print-to-pdf=docs/scripts/logo-text.pdf \
    docs/scripts/logo-text.svg

pdfcrop --quiet \
    docs/scripts/logo-text.pdf docs/scripts/logo-text.pdf

magick -density 2000 docs/scripts/logo-text.pdf \
    -resize 25% \
    -alpha set -background none -channel A \
    -evaluate multiply 1.3 +channel \
    -transparent white \
    docs/scripts/logo-text.png

magick docs/assets/logo.png docs/scripts/logo-text.png \
    -gravity center \
    -geometry +0-0 \
    -composite docs/assets/logo.png

rm docs/scripts/logo-text.pdf docs/scripts/logo-text.png

# Optimize PNG
pngquant docs/assets/logo.png \
    --force \
    --output docs/assets/logo.png

# Pad the logo to get square favicon and resize
magick docs/assets/logo.png \
    -gravity center \
    -background none \
    -extent 640x640 \
    -resize 512x512 \
    docs/assets/favicon.png

# Optimize PNG
pngquant docs/assets/favicon.png \
    --force \
    --output docs/assets/favicon.png
