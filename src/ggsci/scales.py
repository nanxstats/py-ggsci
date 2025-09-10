"""
Plotnine scales for ggsci palettes
"""

from dataclasses import InitVar, dataclass
from typing import Literal

from plotnine.scales import scale_color_gradientn, scale_fill_gradientn
from plotnine.scales.scale_discrete import scale_discrete

from .palettes import bs5_pal, flatui_pal, gsea_pal, npg_pal


# NPG scales (discrete, no variation)
@dataclass
class scale_color_npg(scale_discrete):
    """
    NPG journal color scale

    Parameters
    ----------
    palette : str
        Palette name. Currently only "nrc" is available.
    alpha : float
        Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "nrc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette, alpha):
        super().__post_init__()
        self.palette = npg_pal(palette, alpha)


@dataclass
class scale_fill_npg(scale_discrete):
    """
    NPG journal fill scale

    Parameters
    ----------
    palette : str
        Palette name. Currently only "nrc" is available.
    alpha : float
        Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "nrc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette, alpha):
        super().__post_init__()
        self.palette = npg_pal(palette, alpha)


# FlatUI scales (discrete with 3 variations)
@dataclass
class scale_color_flatui(scale_discrete):
    """
    Flat UI color scale

    Parameters
    ----------
    palette : str
        Palette name: "default", "flattastic", or "aussie".
    alpha : float
        Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette, alpha):
        super().__post_init__()
        self.palette = flatui_pal(palette, alpha)


@dataclass
class scale_fill_flatui(scale_discrete):
    """
    Flat UI fill scale

    Parameters
    ----------
    palette : str
        Palette name: "default", "flattastic", or "aussie".
    alpha : float
        Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette, alpha):
        super().__post_init__()
        self.palette = flatui_pal(palette, alpha)


# GSEA scales (continuous diverging)
def scale_color_gsea(palette="default", alpha=1.0, reverse=False, **kwargs):
    """
    GSEA GenePattern color scale (continuous/diverging)

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.
    **kwargs
        Additional arguments passed to plotnine.scale_color_gradientn.
    """
    colors = gsea_pal(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_gsea(palette="default", alpha=1.0, reverse=False, **kwargs):
    """
    GSEA GenePattern fill scale (continuous/diverging)

    Parameters
    ----------
    palette : str
        Palette name. Currently only "default" is available.
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.
    **kwargs
        Additional arguments passed to plotnine.scale_fill_gradientn.
    """
    colors = gsea_pal(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


# BS5 scales (continuous sequential)
def scale_color_bs5(palette="blue", alpha=1.0, reverse=False, **kwargs):
    """
    Bootstrap 5 color scale (continuous/sequential)

    Parameters
    ----------
    palette : str
        Palette name: "blue", "indigo", "purple", "pink", "red",
        "orange", "yellow", "green", "teal", "cyan", or "gray".
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.
    **kwargs
        Additional arguments passed to plotnine.scale_color_gradientn.
    """
    colors = bs5_pal(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_bs5(palette="blue", alpha=1.0, reverse=False, **kwargs):
    """
    Bootstrap 5 fill scale (continuous/sequential)

    Parameters
    ----------
    palette : str
        Palette name: "blue", "indigo", "purple", "pink", "red",
        "orange", "yellow", "green", "teal", "cyan", or "gray".
    alpha : float
        Transparency level, between 0 and 1.
    reverse : bool
        Whether to reverse the color order.
    **kwargs
        Additional arguments passed to plotnine.scale_fill_gradientn.
    """
    colors = bs5_pal(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


# Aliases for British spelling
scale_colour_npg = scale_color_npg
scale_colour_flatui = scale_color_flatui
scale_colour_gsea = scale_color_gsea
scale_colour_bs5 = scale_color_bs5
