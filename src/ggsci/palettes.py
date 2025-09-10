"""
Palette functions for ggsci

This module provides palette generation functions that return colors
based on the requested number and palette parameters.
"""

from typing import Callable, List

from .data import PALETTES
from .utils import apply_alpha, interpolate_colors


def npg_pal(palette: str = "nrc", alpha: float = 1.0) -> Callable[[int], List[str]]:
    """
    NPG journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "nrc" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["npg"]:
        raise ValueError(f"Unknown NPG palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["npg"][palette]

    def palette_func(n: int) -> List[str]:
        if n > len(colors):
            raise ValueError(
                f"Palette '{palette}' has only {len(colors)} colors, "
                f"but {n} were requested"
            )
        selected = colors[:n]
        if alpha < 1:
            return apply_alpha(selected, alpha)
        return selected

    return palette_func


def flatui_pal(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Flat UI color palette

    Parameters
    ----------
    palette : str
        Palette name: "default", "flattastic", or "aussie".
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["flatui"]:
        raise ValueError(f"Unknown Flat UI palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["flatui"][palette]

    def palette_func(n: int) -> List[str]:
        if n > len(colors):
            raise ValueError(
                f"Palette '{palette}' has only {len(colors)} colors, "
                f"but {n} were requested"
            )
        selected = colors[:n]
        if alpha < 1:
            return apply_alpha(selected, alpha)
        return selected

    return palette_func


def gsea_pal(
    palette: str = "default",
    n: int = 12,
    alpha: float = 1.0,
    reverse: bool = False,
) -> List[str]:
    """
    GSEA GenePattern color palette (continuous/diverging)

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    n : int
        Number of colors to generate.
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.

    Returns
    -------
    List[str]
        List of hex color codes.
    """
    if palette not in PALETTES["gsea"]:
        raise ValueError(f"Unknown GSEA palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    base_colors = PALETTES["gsea"][palette]
    colors = interpolate_colors(base_colors, n)

    if reverse:
        colors = colors[::-1]

    if alpha < 1:
        colors = apply_alpha(colors, alpha)

    return colors


def bs5_pal(
    palette: str = "blue",
    n: int = 10,
    alpha: float = 1.0,
    reverse: bool = False,
) -> List[str]:
    """
    Bootstrap 5 color palette (continuous/sequential)

    Parameters
    ----------
    palette : str
        Palette name: "blue", "indigo", "purple", "pink", "red",
        "orange", "yellow", "green", "teal", "cyan", or "gray".
    n : int
        Number of colors to generate.
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.

    Returns
    -------
    List[str]
        List of hex color codes.
    """
    if palette not in PALETTES["bs5"]:
        raise ValueError(f"Unknown BS5 palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    base_colors = PALETTES["bs5"][palette]
    colors = interpolate_colors(base_colors, n)

    if reverse:
        colors = colors[::-1]

    if alpha < 1:
        colors = apply_alpha(colors, alpha)

    return colors
