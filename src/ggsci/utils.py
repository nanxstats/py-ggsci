"""
Utility functions for color palette manipulation.
"""

from collections.abc import Sequence

import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_hex, to_rgb


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """
    Convert a hex color to an RGB tuple.

    Args:
        hex_color: Color in hex form (e.g., "#RRGGBB").

    Returns:
        A tuple of three integers in the 0 to 255 range.
    """
    rgb = to_rgb(hex_color)
    return (
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255),
    )


def rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    """
    Convert an RGB tuple to a hex color.

    Args:
        rgb: A tuple of three floats in the 0 to 1 range.

    Returns:
        A hex color string (e.g., "#RRGGBB").
    """
    return to_hex(rgb)


def apply_alpha(colors: Sequence[str], alpha: float) -> Sequence[str]:
    """
    Apply alpha transparency to colors.

    Args:
        colors: Sequence of hex color codes.
        alpha: Alpha value between 0 and 1.

    Returns:
        Colors with alpha applied, as 8-digit RGBA hex strings.
    """
    result: list[str] = []
    for color in colors:
        rgb = to_rgb(color)
        rgba_hex = "#{:02x}{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255),
            int(alpha * 255),
        )
        result.append(rgba_hex)
    return result


def interpolate_colors(colors: Sequence[str], n: int) -> Sequence[str]:
    """
    Interpolate between colors to generate a sequence of length n.

    Args:
        colors: Base colors to interpolate between.
        n: Number of colors to generate.

    Returns:
        A list of n interpolated hex colors.
    """
    if n <= len(colors):
        # If requesting fewer colors than available, sample evenly
        indices = np.linspace(0, len(colors) - 1, n).astype(int)
        return [colors[i] for i in indices]

    # Create a colormap from the base colors
    cmap = LinearSegmentedColormap.from_list("custom", list(colors), N=n)

    # Generate n evenly spaced colors
    positions = np.linspace(0, 1, n)
    interpolated: list[str] = []

    for pos in positions:
        rgba = cmap(pos)
        # Convert to hex (ignore alpha channel)
        hex_color = to_hex(rgba[:3])
        interpolated.append(hex_color)

    return interpolated
