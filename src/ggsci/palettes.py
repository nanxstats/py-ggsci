"""
Palette generators for ggsci.

This module provides palette functions that either return a callable for
discrete palettes or a sequence of colors for continuous palettes.
"""

from collections.abc import Callable, Sequence
from typing import Final, TypeAlias

from .data import PALETTES
from .data_iterm import ITERM_PALETTES, PALETTES_ITERM
from .utils import apply_alpha, interpolate_colors

PaletteFunc: TypeAlias = Callable[[int], Sequence[str]]

ITERM_VARIANTS: Final[tuple[str, ...]] = ("normal", "bright")


def pal_npg(palette: str = "nrc", alpha: float = 1.0) -> PaletteFunc:
    """
    NPG journal color palette.

    Args:
        palette: Palette name. Currently only "nrc" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["npg"]:
        raise ValueError(f"Unknown NPG palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["npg"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_aaas(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    AAAS journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["aaas"]:
        raise ValueError(f"Unknown AAAS palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["aaas"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_nejm(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    NEJM journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["nejm"]:
        raise ValueError(f"Unknown NEJM palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["nejm"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_lancet(palette: str = "lanonc", alpha: float = 1.0) -> PaletteFunc:
    """
    Lancet journal color palette.

    Args:
        palette: Palette name. Currently only "lanonc" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["lancet"]:
        raise ValueError(f"Unknown Lancet palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["lancet"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_jama(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    JAMA journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["jama"]:
        raise ValueError(f"Unknown JAMA palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["jama"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_bmj(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    BMJ journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["bmj"]:
        raise ValueError(f"Unknown BMJ palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["bmj"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_jco(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    JCO journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["jco"]:
        raise ValueError(f"Unknown JCO palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["jco"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_ucscgb(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    UCSC Genome Browser color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["ucscgb"]:
        raise ValueError(f"Unknown UCSCGB palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["ucscgb"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_d3(palette: str = "category10", alpha: float = 1.0) -> PaletteFunc:
    """
    D3.js color palette.

    Args:
        palette: Palette name: "category10", "category20", "category20b", or "category20c".
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["d3"]:
        raise ValueError(f"Unknown D3 palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["d3"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_observable(palette: str = "observable10", alpha: float = 1.0) -> PaletteFunc:
    """
    Observable color palette.

    Args:
        palette: Palette name. Currently only "observable10" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["observable"]:
        raise ValueError(f"Unknown Observable palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["observable"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_primer(palette: str = "mark17", alpha: float = 1.0) -> PaletteFunc:
    """
    Primer design system color palette.

    Args:
        palette: Palette name. Currently only "mark17" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["primer"]:
        raise ValueError(f"Unknown Primer palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["primer"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_atlassian(palette: str = "categorical8", alpha: float = 1.0) -> PaletteFunc:
    """
    Atlassian design system color palette.

    Args:
        palette: Palette name. Currently only "categorical8" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["atlassian"]:
        raise ValueError(f"Unknown Atlassian palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["atlassian"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_iterm(
    palette: str = "Rose Pine",
    variant: str = "normal",
    alpha: float = 1.0,
) -> PaletteFunc:
    """
    iTerm color palette.

    Args:
        palette: Palette name. See `ITERM_PALETTES` for available options.
        variant: Palette variant. Either "normal" or "bright".
        alpha: Transparency level, between 0 and 1.

    Details:
        Preview all iTerm palettes: <https://nanx.me/ggsci-iterm/>.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name, variant, or alpha is invalid.
    """
    if palette not in ITERM_PALETTES:
        raise ValueError(f"Unknown iTerm palette: {palette}")

    if variant not in ITERM_VARIANTS:
        raise ValueError(f"Unknown iTerm variant: {variant}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES_ITERM[palette][variant]

    def palette_func(n: int) -> Sequence[str]:
        if n > len(colors):
            raise ValueError(
                f"Palette '{palette}' ({variant}) has only {len(colors)} colors, "
                f"but {n} were requested"
            )
        selected = colors[:n]
        if alpha < 1:
            return apply_alpha(selected, alpha)
        return selected

    return palette_func


def pal_locuszoom(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    LocusZoom color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["locuszoom"]:
        raise ValueError(f"Unknown LocusZoom palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["locuszoom"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_igv(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    IGV color palette.

    Args:
        palette: Palette name: "default" or "alternating".
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["igv"]:
        raise ValueError(f"Unknown IGV palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["igv"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_cosmic(palette: str = "hallmarks_dark", alpha: float = 1.0) -> PaletteFunc:
    """
    COSMIC color palette.

    Args:
        palette: Palette name: "hallmarks_dark", "hallmarks_light", or "signature_substitutions".
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["cosmic"]:
        raise ValueError(f"Unknown COSMIC palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["cosmic"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_uchicago(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    University of Chicago color palette.

    Args:
        palette: Palette name: "default", "light", or "dark".
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["uchicago"]:
        raise ValueError(f"Unknown UChicago palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["uchicago"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_startrek(palette: str = "uniform", alpha: float = 1.0) -> PaletteFunc:
    """
    Star Trek color palette.

    Args:
        palette: Palette name. Currently only "uniform" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["startrek"]:
        raise ValueError(f"Unknown Star Trek palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["startrek"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_tron(palette: str = "legacy", alpha: float = 1.0) -> PaletteFunc:
    """
    Tron Legacy color palette.

    Args:
        palette: Palette name. Currently only "legacy" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["tron"]:
        raise ValueError(f"Unknown Tron palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["tron"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_futurama(palette: str = "planetexpress", alpha: float = 1.0) -> PaletteFunc:
    """
    Futurama color palette.

    Args:
        palette: Palette name. Currently only "planetexpress" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["futurama"]:
        raise ValueError(f"Unknown Futurama palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["futurama"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_rickandmorty(palette: str = "schwifty", alpha: float = 1.0) -> PaletteFunc:
    """
    Rick and Morty color palette.

    Args:
        palette: Palette name. Currently only "schwifty" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["rickandmorty"]:
        raise ValueError(f"Unknown Rick and Morty palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["rickandmorty"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_simpsons(palette: str = "springfield", alpha: float = 1.0) -> PaletteFunc:
    """
    The Simpsons color palette.

    Args:
        palette: Palette name. Currently only "springfield" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["simpsons"]:
        raise ValueError(f"Unknown Simpsons palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["simpsons"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_flatui(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    Flat UI color palette.

    Args:
        palette: Palette name: "default", "flattastic", or "aussie".
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["flatui"]:
        raise ValueError(f"Unknown Flat UI palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["flatui"][palette]

    def palette_func(n: int) -> Sequence[str]:
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


def pal_frontiers(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    Frontiers journal color palette.

    Args:
        palette: Palette name. Currently only "default" is available.
        alpha: Transparency level, between 0 and 1.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
    """
    if palette not in PALETTES["frontiers"]:
        raise ValueError(f"Unknown Frontiers palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    colors = PALETTES["frontiers"][palette]

    def palette_func(n: int) -> Sequence[str]:
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
) -> Sequence[str]:
    """
    GSEA GenePattern color palette (continuous/diverging).

    Args:
        palette: Palette name. Currently only "default" is available.
        n: Number of colors to generate.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.

    Returns:
        A sequence of hex color codes.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
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
) -> Sequence[str]:
    """
    Bootstrap 5 color palette (continuous/sequential).

    Args:
        palette: Palette name: "blue", "indigo", "purple", "pink", "red",
            "orange", "yellow", "green", "teal", "cyan", or "gray".
        n: Number of colors to generate.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.

    Returns:
        A sequence of hex color codes.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
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
) -> Sequence[str]:
    """
    Material Design color palette (continuous/sequential).

    Args:
        palette: Palette name: "red", "pink", "purple", "deep-purple", "indigo",
            "blue", "light-blue", "cyan", "teal", "green", "light-green",
            "lime", "yellow", "amber", "orange", "deep-orange", "brown",
            "grey", or "blue-grey".
        n: Number of colors to generate.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.

    Returns:
        A sequence of hex color codes.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
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
) -> Sequence[str]:
    """
    Tailwind CSS 3 color palette (continuous/sequential).

    Args:
        palette: Palette name: "slate", "gray", "zinc", "neutral", "stone",
            "red", "orange", "amber", "yellow", "lime", "green", "emerald",
            "teal", "cyan", "sky", "blue", "indigo", "violet", "purple",
            "fuchsia", "pink", or "rose".
        n: Number of colors to generate.
        alpha: Transparency level, between 0 and 1.
        reverse: Whether to reverse the color order.

    Returns:
        A sequence of hex color codes.

    Raises:
        ValueError: If the palette name is unknown or alpha is invalid.
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
