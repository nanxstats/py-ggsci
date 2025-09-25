"""
Plotnine scales for ggsci palettes.
"""

from dataclasses import InitVar, dataclass
from typing import Any

from plotnine.scales import scale_color_gradientn, scale_fill_gradientn
from plotnine.scales.scale_discrete import scale_discrete

from .palettes import (
    pal_aaas,
    pal_atlassian,
    pal_bmj,
    pal_bs5,
    pal_cosmic,
    pal_d3,
    pal_flatui,
    pal_frontiers,
    pal_futurama,
    pal_gsea,
    pal_igv,
    pal_iterm,
    pal_jama,
    pal_jco,
    pal_lancet,
    pal_locuszoom,
    pal_material,
    pal_nejm,
    pal_npg,
    pal_observable,
    pal_primer,
    pal_rickandmorty,
    pal_simpsons,
    pal_startrek,
    pal_tron,
    pal_tw3,
    pal_uchicago,
    pal_ucscgb,
)


@dataclass
class scale_color_npg(scale_discrete):
    """
    NPG journal color scale.

    Args:
        palette: Palette name. Currently only "nrc" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "nrc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_npg(palette, alpha))


@dataclass
class scale_fill_npg(scale_discrete):
    """
    NPG journal fill scale.

    Args:
        palette: Palette name. Currently only "nrc" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "nrc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_npg(palette, alpha))


@dataclass
class scale_color_aaas(scale_discrete):
    """
    AAAS journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_aaas(palette, alpha))


@dataclass
class scale_fill_aaas(scale_discrete):
    """
    AAAS journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_aaas(palette, alpha))


@dataclass
class scale_color_nejm(scale_discrete):
    """
    NEJM journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_nejm(palette, alpha))


@dataclass
class scale_fill_nejm(scale_discrete):
    """
    NEJM journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_nejm(palette, alpha))


@dataclass
class scale_color_lancet(scale_discrete):
    """
    Lancet journal color scale.

    Args:
        palette: Palette name. Currently only "lanonc" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "lanonc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_lancet(palette, alpha))


@dataclass
class scale_fill_lancet(scale_discrete):
    """
    Lancet journal fill scale.

    Args:
        palette: Palette name. Currently only "lanonc" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "lanonc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_lancet(palette, alpha))


@dataclass
class scale_color_jama(scale_discrete):
    """
    JAMA journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_jama(palette, alpha))


@dataclass
class scale_fill_jama(scale_discrete):
    """
    JAMA journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_jama(palette, alpha))


@dataclass
class scale_color_bmj(scale_discrete):
    """
    BMJ journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_bmj(palette, alpha))


@dataclass
class scale_fill_bmj(scale_discrete):
    """
    BMJ journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_bmj(palette, alpha))


@dataclass
class scale_color_jco(scale_discrete):
    """
    JCO journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_jco(palette, alpha))


@dataclass
class scale_fill_jco(scale_discrete):
    """
    JCO journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_jco(palette, alpha))


@dataclass
class scale_color_ucscgb(scale_discrete):
    """
    UCSC Genome Browser color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_ucscgb(palette, alpha))


@dataclass
class scale_fill_ucscgb(scale_discrete):
    """
    UCSC Genome Browser fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_ucscgb(palette, alpha))


@dataclass
class scale_color_d3(scale_discrete):
    """
    D3.js color scale.

    Args:
        palette: Palette name: "category10", "category20", "category20b", or "category20c".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "category10"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_d3(palette, alpha))


@dataclass
class scale_fill_d3(scale_discrete):
    """
    D3.js fill scale.

    Args:
        palette: Palette name: "category10", "category20", "category20b", or "category20c".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "category10"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_d3(palette, alpha))


@dataclass
class scale_color_observable(scale_discrete):
    """
    Observable color scale.

    Args:
        palette: Palette name. Currently only "observable10" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "observable10"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_observable(palette, alpha))


@dataclass
class scale_fill_observable(scale_discrete):
    """
    Observable fill scale.

    Args:
        palette: Palette name. Currently only "observable10" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "observable10"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_observable(palette, alpha))


@dataclass
class scale_color_primer(scale_discrete):
    """
    Primer design system color scale.

    Args:
        palette: Palette name. Currently only "mark17" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "mark17"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_primer(palette, alpha))


@dataclass
class scale_fill_primer(scale_discrete):
    """
    Primer design system fill scale.

    Args:
        palette: Palette name. Currently only "mark17" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "mark17"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_primer(palette, alpha))


@dataclass
class scale_color_atlassian(scale_discrete):
    """
    Atlassian design system color scale.

    Args:
        palette: Palette name. Currently only "categorical8" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "categorical8"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_atlassian(palette, alpha))


@dataclass
class scale_fill_atlassian(scale_discrete):
    """
    Atlassian design system fill scale.

    Args:
        palette: Palette name. Currently only "categorical8" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "categorical8"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_atlassian(palette, alpha))


@dataclass
class scale_color_iterm(scale_discrete):
    """
    iTerm color scale.

    Args:
        palette: Palette name. See `ITERM_PALETTES` for available options.
        variant: Palette variant. Either "normal" or "bright".
        alpha: Transparency level, between 0 and 1.

    Details:
        Preview all iTerm palettes: <https://nanx.me/ggsci-iterm/>.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "Rose Pine"
    variant: InitVar[str] = "normal"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, variant: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_iterm(palette, variant, alpha))


@dataclass
class scale_fill_iterm(scale_discrete):
    """
    iTerm fill scale.

    Args:
        palette: Palette name. See `ITERM_PALETTES` for available options.
        variant: Palette variant. Either "normal" or "bright".
        alpha: Transparency level, between 0 and 1.

    Details:
        Preview all iTerm palettes: <https://nanx.me/ggsci-iterm/>.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "Rose Pine"
    variant: InitVar[str] = "normal"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, variant: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_iterm(palette, variant, alpha))


@dataclass
class scale_color_locuszoom(scale_discrete):
    """
    LocusZoom color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_locuszoom(palette, alpha))


@dataclass
class scale_fill_locuszoom(scale_discrete):
    """
    LocusZoom fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_locuszoom(palette, alpha))


@dataclass
class scale_color_igv(scale_discrete):
    """
    IGV color scale.

    Args:
        palette: Palette name: "default" or "alternating".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_igv(palette, alpha))


@dataclass
class scale_fill_igv(scale_discrete):
    """
    IGV fill scale.

    Args:
        palette: Palette name: "default" or "alternating".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_igv(palette, alpha))


@dataclass
class scale_color_cosmic(scale_discrete):
    """
    COSMIC color scale.

    Args:
        palette: Palette name: "hallmarks_dark", "hallmarks_light", or "signature_substitutions".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "hallmarks_dark"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_cosmic(palette, alpha))


@dataclass
class scale_fill_cosmic(scale_discrete):
    """
    COSMIC fill scale.

    Args:
        palette: Palette name: "hallmarks_dark", "hallmarks_light", or "signature_substitutions".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "hallmarks_dark"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_cosmic(palette, alpha))


@dataclass
class scale_color_uchicago(scale_discrete):
    """
    University of Chicago color scale.

    Args:
        palette: Palette name: "default", "light", or "dark".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_uchicago(palette, alpha))


@dataclass
class scale_fill_uchicago(scale_discrete):
    """
    University of Chicago fill scale.

    Args:
        palette: Palette name: "default", "light", or "dark".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_uchicago(palette, alpha))


@dataclass
class scale_color_startrek(scale_discrete):
    """
    Star Trek color scale.

    Args:
        palette: Palette name. Currently only "uniform" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "uniform"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_startrek(palette, alpha))


@dataclass
class scale_fill_startrek(scale_discrete):
    """
    Star Trek fill scale.

    Args:
        palette: Palette name. Currently only "uniform" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "uniform"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_startrek(palette, alpha))


@dataclass
class scale_color_tron(scale_discrete):
    """
    Tron Legacy color scale.

    Args:
        palette: Palette name. Currently only "legacy" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "legacy"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_tron(palette, alpha))


@dataclass
class scale_fill_tron(scale_discrete):
    """
    Tron Legacy fill scale.

    Args:
        palette: Palette name. Currently only "legacy" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "legacy"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_tron(palette, alpha))


@dataclass
class scale_color_futurama(scale_discrete):
    """
    Futurama color scale.

    Args:
        palette: Palette name. Currently only "planetexpress" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "planetexpress"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_futurama(palette, alpha))


@dataclass
class scale_fill_futurama(scale_discrete):
    """
    Futurama fill scale.

    Args:
        palette: Palette name. Currently only "planetexpress" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "planetexpress"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_futurama(palette, alpha))


@dataclass
class scale_color_rickandmorty(scale_discrete):
    """
    Rick and Morty color scale.

    Args:
        palette: Palette name. Currently only "schwifty" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "schwifty"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_rickandmorty(palette, alpha))


@dataclass
class scale_fill_rickandmorty(scale_discrete):
    """
    Rick and Morty fill scale.

    Args:
        palette: Palette name. Currently only "schwifty" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "schwifty"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_rickandmorty(palette, alpha))


@dataclass
class scale_color_simpsons(scale_discrete):
    """
    The Simpsons color scale.

    Args:
        palette: Palette name. Currently only "springfield" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "springfield"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_simpsons(palette, alpha))


@dataclass
class scale_fill_simpsons(scale_discrete):
    """
    The Simpsons fill scale.

    Args:
        palette: Palette name. Currently only "springfield" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "springfield"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_simpsons(palette, alpha))


@dataclass
class scale_color_flatui(scale_discrete):
    """
    Flat UI color scale.

    Args:
        palette: Palette name: "default", "flattastic", or "aussie".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_flatui(palette, alpha))


@dataclass
class scale_fill_flatui(scale_discrete):
    """
    Flat UI fill scale.

    Args:
        palette: Palette name: "default", "flattastic", or "aussie".
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_flatui(palette, alpha))


@dataclass
class scale_color_frontiers(scale_discrete):
    """
    Frontiers journal color scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["color"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_frontiers(palette, alpha))


@dataclass
class scale_fill_frontiers(scale_discrete):
    """
    Frontiers journal fill scale.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
    """

    _aesthetics = ["fill"]

    palette: InitVar[str] = "default"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette: str, alpha: float) -> None:
        super().__post_init__()
        setattr(self, "palette", pal_frontiers(palette, alpha))


def scale_color_gsea(
    palette: str = "default",
    *,
    alpha: float = 1.0,
    reverse: bool = False,
    **kwargs: Any,
) -> scale_color_gradientn:
    """
    GSEA GenePattern color scale (continuous/diverging).

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_color_gradientn.
    """
    colors = pal_gsea(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_gsea(
    palette: str = "default",
    *,
    alpha: float = 1.0,
    reverse: bool = False,
    **kwargs: Any,
) -> scale_fill_gradientn:
    """
    GSEA GenePattern fill scale (continuous/diverging).

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_fill_gradientn.
    """
    colors = pal_gsea(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


def scale_color_bs5(
    palette: str = "blue", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_color_gradientn:
    """
    Bootstrap 5 color scale (continuous/sequential).

    Args:
        palette: Palette name: "blue", "indigo", "purple", "pink", "red",
            "orange", "yellow", "green", "teal", "cyan", or "gray".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_color_gradientn.
    """
    colors = pal_bs5(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_bs5(
    palette: str = "blue", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_fill_gradientn:
    """
    Bootstrap 5 fill scale (continuous/sequential).

    Args:
        palette: Palette name: "blue", "indigo", "purple", "pink", "red",
            "orange", "yellow", "green", "teal", "cyan", or "gray".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_fill_gradientn.
    """
    colors = pal_bs5(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


def scale_color_material(
    palette: str = "red", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_color_gradientn:
    """
    Material Design color scale (continuous/sequential).

    Args:
        palette: Palette name: "red", "pink", "purple", "deep-purple", "indigo",
            "blue", "light-blue", "cyan", "teal", "green", "light-green",
            "lime", "yellow", "amber", "orange", "deep-orange", "brown",
            "grey", or "blue-grey".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_color_gradientn.
    """
    colors = pal_material(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_material(
    palette: str = "red", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_fill_gradientn:
    """
    Material Design fill scale (continuous/sequential).

    Args:
        palette: Palette name: "red", "pink", "purple", "deep-purple", "indigo",
            "blue", "light-blue", "cyan", "teal", "green", "light-green",
            "lime", "yellow", "amber", "orange", "deep-orange", "brown",
            "grey", or "blue-grey".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_fill_gradientn.
    """
    colors = pal_material(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


def scale_color_tw3(
    palette: str = "blue", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_color_gradientn:
    """
    Tailwind CSS 3 color scale (continuous/sequential).

    Args:
        palette: Palette name: "slate", "gray", "zinc", "neutral", "stone",
            "red", "orange", "amber", "yellow", "lime", "green", "emerald",
            "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
            "fuchsia", "pink", or "rose".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_color_gradientn.
    """
    colors = pal_tw3(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)


def scale_fill_tw3(
    palette: str = "blue", *, alpha: float = 1.0, reverse: bool = False, **kwargs: Any
) -> scale_fill_gradientn:
    """
    Tailwind CSS 3 fill scale (continuous/sequential).

    Args:
        palette: Palette name: "slate", "gray", "zinc", "neutral", "stone",
            "red", "orange", "amber", "yellow", "lime", "green", "emerald",
            "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
            "fuchsia", "pink", or "rose".
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.
        **kwargs: Additional keyword arguments forwarded to plotnine.scale_fill_gradientn.
    """
    colors = pal_tw3(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_fill_gradientn(colors=colors, **kwargs)


# Aliases for British spelling
scale_colour_npg = scale_color_npg
scale_colour_aaas = scale_color_aaas
scale_colour_nejm = scale_color_nejm
scale_colour_lancet = scale_color_lancet
scale_colour_jama = scale_color_jama
scale_colour_bmj = scale_color_bmj
scale_colour_jco = scale_color_jco
scale_colour_ucscgb = scale_color_ucscgb
scale_colour_d3 = scale_color_d3
scale_colour_observable = scale_color_observable
scale_colour_primer = scale_color_primer
scale_colour_atlassian = scale_color_atlassian
scale_colour_iterm = scale_color_iterm
scale_colour_locuszoom = scale_color_locuszoom
scale_colour_igv = scale_color_igv
scale_colour_cosmic = scale_color_cosmic
scale_colour_uchicago = scale_color_uchicago
scale_colour_startrek = scale_color_startrek
scale_colour_tron = scale_color_tron
scale_colour_futurama = scale_color_futurama
scale_colour_rickandmorty = scale_color_rickandmorty
scale_colour_simpsons = scale_color_simpsons
scale_colour_flatui = scale_color_flatui
scale_colour_frontiers = scale_color_frontiers
scale_colour_gsea = scale_color_gsea
scale_colour_bs5 = scale_color_bs5
scale_colour_material = scale_color_material
scale_colour_tw3 = scale_color_tw3
