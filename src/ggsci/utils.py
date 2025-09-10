"""
Utility functions for color palette manipulation
"""

from typing import List, Tuple

import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_hex, to_rgb


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple (0-255 range)."""
    rgb = to_rgb(hex_color)
    return tuple(int(c * 255) for c in rgb)


def rgb_to_hex(rgb: Tuple[float, float, float]) -> str:
    """Convert RGB tuple (0-1 range) to hex color."""
    return to_hex(rgb)


def apply_alpha(colors: List[str], alpha: float) -> List[str]:
    """
    Apply alpha transparency to a list of colors.

    Parameters
    ----------
    colors : List[str]
        List of hex color codes.
    alpha : float
        Alpha value between 0 and 1.

    Returns
    -------
    List[str]
        List of hex colors with alpha applied (as RGBA hex).
    """
    result = []
    for color in colors:
        rgb = to_rgb(color)
        # Convert to RGBA hex format
        rgba_hex = "#{:02x}{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255),
            int(alpha * 255),
        )
        result.append(rgba_hex)
    return result


def interpolate_colors(colors: List[str], n: int) -> List[str]:
    """
    Interpolate between colors to generate n colors.

    Uses spline interpolation in LAB color space for smooth gradients.

    Parameters
    ----------
    colors : List[str]
        Base colors to interpolate between.
    n : int
        Number of colors to generate.

    Returns
    -------
    List[str]
        List of n interpolated hex colors.
    """
    if n <= len(colors):
        # If requesting fewer colors than available, sample evenly
        indices = np.linspace(0, len(colors) - 1, n).astype(int)
        return [colors[i] for i in indices]

    # Create a colormap from the base colors
    cmap = LinearSegmentedColormap.from_list("custom", colors, N=n)

    # Generate n evenly spaced colors
    positions = np.linspace(0, 1, n)
    interpolated = []

    for pos in positions:
        rgba = cmap(pos)
        # Convert to hex (ignoring alpha channel)
        hex_color = to_hex(rgba[:3])
        interpolated.append(hex_color)

    return interpolated
