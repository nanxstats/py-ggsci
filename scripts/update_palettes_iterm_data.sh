#!/bin/sh

# Update iTerm palettes data from R ggsci package
echo "Updating iTerm palettes data from R package ggsci..."
Rscript scripts/update_palettes_iterm_data.R

# Format the generated Python file
echo "Formatting generated Python file..."
uv run ruff format src/ggsci/data_iterm.py

echo "Done!"
