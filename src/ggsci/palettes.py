"""
Palette functions for ggsci

This module provides palette generation functions that return colors
based on the requested number and palette parameters.
"""

from typing import Callable, List

from .data import PALETTES
from .utils import apply_alpha, interpolate_colors


def pal_npg(palette: str = "nrc", alpha: float = 1.0) -> Callable[[int], List[str]]:
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


def pal_aaas(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    AAAS journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["aaas"]:
        raise ValueError(f"Unknown AAAS palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["aaas"][palette]

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


def pal_nejm(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    NEJM journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["nejm"]:
        raise ValueError(f"Unknown NEJM palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["nejm"][palette]

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


def pal_lancet(
    palette: str = "lanonc", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Lancet journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "lanonc" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["lancet"]:
        raise ValueError(f"Unknown Lancet palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["lancet"][palette]

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


def pal_jama(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    JAMA journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["jama"]:
        raise ValueError(f"Unknown JAMA palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["jama"][palette]

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


def pal_bmj(palette: str = "default", alpha: float = 1.0) -> Callable[[int], List[str]]:
    """
    BMJ journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["bmj"]:
        raise ValueError(f"Unknown BMJ palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["bmj"][palette]

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


def pal_jco(palette: str = "default", alpha: float = 1.0) -> Callable[[int], List[str]]:
    """
    JCO journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["jco"]:
        raise ValueError(f"Unknown JCO palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["jco"][palette]

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


def pal_ucscgb(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    UCSC Genome Browser color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["ucscgb"]:
        raise ValueError(f"Unknown UCSCGB palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["ucscgb"][palette]

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


def pal_d3(
    palette: str = "category10", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    D3.js color palette

    Parameters
    ----------
    palette : str
        Palette name: "category10", "category20", "category20b", or "category20c".
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["d3"]:
        raise ValueError(f"Unknown D3 palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["d3"][palette]

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


def pal_observable(
    palette: str = "observable10", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Observable color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "observable10" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["observable"]:
        raise ValueError(f"Unknown Observable palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["observable"][palette]

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


def pal_locuszoom(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    LocusZoom color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["locuszoom"]:
        raise ValueError(f"Unknown LocusZoom palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["locuszoom"][palette]

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


def pal_igv(palette: str = "default", alpha: float = 1.0) -> Callable[[int], List[str]]:
    """
    IGV color palette

    Parameters
    ----------
    palette : str
        Palette name: "default" or "alternating".
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["igv"]:
        raise ValueError(f"Unknown IGV palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["igv"][palette]

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


def pal_cosmic(
    palette: str = "hallmarks_dark", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    COSMIC color palette

    Parameters
    ----------
    palette : str
        Palette name: "hallmarks_dark", "hallmarks_light", or "signature_substitutions".
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["cosmic"]:
        raise ValueError(f"Unknown COSMIC palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["cosmic"][palette]

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


def pal_uchicago(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    University of Chicago color palette

    Parameters
    ----------
    palette : str
        Palette name: "default", "light", or "dark".
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["uchicago"]:
        raise ValueError(f"Unknown UChicago palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["uchicago"][palette]

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


def pal_startrek(
    palette: str = "uniform", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Star Trek color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "uniform" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["startrek"]:
        raise ValueError(f"Unknown Star Trek palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["startrek"][palette]

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


def pal_tron(palette: str = "legacy", alpha: float = 1.0) -> Callable[[int], List[str]]:
    """
    Tron Legacy color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "legacy" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["tron"]:
        raise ValueError(f"Unknown Tron palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["tron"][palette]

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


def pal_futurama(
    palette: str = "planetexpress", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Futurama color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "planetexpress" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["futurama"]:
        raise ValueError(f"Unknown Futurama palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["futurama"][palette]

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


def pal_rickandmorty(
    palette: str = "schwifty", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Rick and Morty color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "schwifty" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["rickandmorty"]:
        raise ValueError(f"Unknown Rick and Morty palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["rickandmorty"][palette]

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


def pal_simpsons(
    palette: str = "springfield", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    The Simpsons color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "springfield" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["simpsons"]:
        raise ValueError(f"Unknown Simpsons palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["simpsons"][palette]

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


def pal_flatui(
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


def pal_frontiers(
    palette: str = "default", alpha: float = 1.0
) -> Callable[[int], List[str]]:
    """
    Frontiers journal color palette

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.

    Returns
    -------
    Callable
        A function that takes n (number of colors) and returns a list of colors.
    """
    if palette not in PALETTES["frontiers"]:
        raise ValueError(f"Unknown Frontiers palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["frontiers"][palette]

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


def pal_gsea(
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


def pal_bs5(
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


def pal_material(
    palette: str = "red",
    n: int = 10,
    alpha: float = 1.0,
    reverse: bool = False,
) -> List[str]:
    """
    Material Design color palette (continuous/sequential)

    Parameters
    ----------
    palette : str
        Palette name: "red", "pink", "purple", "deep-purple", "indigo",
        "blue", "light-blue", "cyan", "teal", "green", "light-green",
        "lime", "yellow", "amber", "orange", "deep-orange", "brown",
        "grey", or "blue-grey".
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
    if palette not in PALETTES["material"]:
        raise ValueError(f"Unknown Material palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    base_colors = PALETTES["material"][palette]
    colors = interpolate_colors(base_colors, n)

    if reverse:
        colors = colors[::-1]

    if alpha < 1:
        colors = apply_alpha(colors, alpha)

    return colors


def pal_tw3(
    palette: str = "blue",
    n: int = 11,
    alpha: float = 1.0,
    reverse: bool = False,
) -> List[str]:
    """
    Tailwind CSS 3 color palette (continuous/sequential)

    Parameters
    ----------
    palette : str
        Palette name: "slate", "gray", "zinc", "neutral", "stone",
        "red", "orange", "amber", "yellow", "lime", "green", "emerald",
        "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
        "fuchsia", "pink", or "rose".
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
    if palette not in PALETTES["tw3"]:
        raise ValueError(f"Unknown Tailwind CSS 3 palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    base_colors = PALETTES["tw3"][palette]
    colors = interpolate_colors(base_colors, n)

    if reverse:
        colors = colors[::-1]

    if alpha < 1:
        colors = apply_alpha(colors, alpha)

    return colors
