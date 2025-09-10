#!/bin/sh

# Update palettes data from R ggsci package
echo "Updating palettes data from R package ggsci..."
Rscript scripts/update_palettes_data.R

# Format the generated Python file
echo "Formatting generated Python file..."
uv run ruff format src/ggsci/data.py

echo "Done!"
