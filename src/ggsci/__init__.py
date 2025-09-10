"""
py-ggsci: Scientific journal color palettes for Python

A Python implementation of the R ggsci package, providing color palettes
inspired by scientific journals and sci-fi themes.
"""

from .palettes import bs5_pal, flatui_pal, gsea_pal, npg_pal
from .scales import (
    scale_color_bs5,
    scale_color_flatui,
    scale_color_gsea,
    scale_color_npg,
    scale_colour_bs5,
    scale_colour_flatui,
    scale_colour_gsea,
    scale_colour_npg,
    scale_fill_bs5,
    scale_fill_flatui,
    scale_fill_gsea,
    scale_fill_npg,
)

__version__ = "0.1.0"

__all__ = [
    "scale_color_npg",
    "scale_fill_npg",
    "scale_colour_npg",
    "scale_color_flatui",
    "scale_fill_flatui",
    "scale_colour_flatui",
    "scale_color_gsea",
    "scale_fill_gsea",
    "scale_colour_gsea",
    "scale_color_bs5",
    "scale_fill_bs5",
    "scale_colour_bs5",
    "npg_pal",
    "flatui_pal",
    "gsea_pal",
    "bs5_pal",
]
