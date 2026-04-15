"""
Palette generators for ggsci.

This module provides palette functions that either return a callable for
discrete palettes or a sequence of colors for continuous palettes.
"""

import math
from collections.abc import Callable, Sequence
from functools import cache
from typing import Final, TypeAlias

import numpy as np

from .data import PALETTES
from .data_iterm import ITERM_PALETTES, PALETTES_ITERM
from .utils import apply_alpha, interpolate_colors

PaletteFunc: TypeAlias = Callable[[int], Sequence[str]]

ITERM_VARIANTS: Final[tuple[str, ...]] = ("normal", "bright")
GephiFilter: TypeAlias = tuple[float, float, float, float, float, float]


def _as_gephi_filter(values: Sequence[float]) -> GephiFilter:
    return (
        float(values[0]),
        float(values[1]),
        float(values[2]),
        float(values[3]),
        float(values[4]),
        float(values[5]),
    )


GEPHI_FILTERS: Final[dict[str, GephiFilter]] = {
    name: _as_gephi_filter(values) for name, values in PALETTES["gephi"].items()
}
#: Available Gephi generative palette identifiers.
GEPHI_PALETTES: Final[tuple[str, ...]] = tuple(GEPHI_FILTERS)


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
        palette: Palette name: "category10", "category20", "category20b",
            or "category20c".
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


@cache
def _gephi_color_samples(filter_values: GephiFilter) -> np.ndarray:
    grid = np.meshgrid(
        np.linspace(0, 1, 21),
        np.linspace(-1, 1, 21),
        np.linspace(-1, 1, 21),
        indexing="ij",
    )
    samples = np.stack(grid, axis=-1).reshape(-1, 3)
    valid = np.array(
        [_gephi_check_color(sample, filter_values) for sample in samples], dtype=bool
    )
    return samples[valid]


def _gephi_generate_palette_quality(colors_count: int) -> int:
    quality = 50

    if colors_count > 300:
        quality = 2
    elif colors_count > 200:
        quality = 5
    elif colors_count > 100:
        quality = 10
    elif colors_count > 50:
        quality = 25

    return quality


def _gephi_generate_palette(colors_count: int, filter_values: GephiFilter) -> list[str]:
    k_means = _gephi_generate_random_kmeans(colors_count, filter_values)
    color_samples = _gephi_color_samples(filter_values)
    quality = _gephi_generate_palette_quality(colors_count)
    samples_closest = np.zeros(len(color_samples), dtype=int)

    for _ in range(quality):
        min_distance = np.full(len(color_samples), np.inf)

        for index, k_mean in enumerate(k_means):
            distance = _gephi_distance_sq(color_samples, k_mean)
            update = distance < min_distance
            min_distance[update] = distance[update]
            samples_closest[update] = index

        free_color_samples = color_samples.copy()

        for index in range(len(k_means)):
            assigned = samples_closest == index
            if assigned.any():
                candidate_k_mean = color_samples[assigned].mean(axis=0)
            else:
                candidate_k_mean = np.zeros(3)

            if assigned.any() and _gephi_check_color(candidate_k_mean, filter_values):
                k_means[index] = candidate_k_mean
            elif len(free_color_samples):
                closest = _gephi_closest_sample(free_color_samples, candidate_k_mean)
                k_means[index] = free_color_samples[closest]
            else:
                closest = _gephi_closest_sample(color_samples, candidate_k_mean)
                k_means[index] = color_samples[closest]

            if len(free_color_samples):
                keep = ~np.all(free_color_samples == k_means[index], axis=1)
                free_color_samples = free_color_samples[keep]

    return [_gephi_lab_to_hex(color) for color in _gephi_sort_colors(k_means)]


def _gephi_generate_random_kmeans(
    colors_count: int, filter_values: GephiFilter
) -> np.ndarray:
    k_means = np.empty((colors_count, 3), dtype=float)

    for index in range(colors_count):
        lab = np.array(
            [
                np.random.random(),
                2 * np.random.random() - 1,
                2 * np.random.random() - 1,
            ]
        )
        while not _gephi_check_color(lab, filter_values):
            lab = np.array(
                [
                    np.random.random(),
                    2 * np.random.random() - 1,
                    2 * np.random.random() - 1,
                ]
            )
        k_means[index] = lab

    return k_means


def _gephi_closest_sample(samples: np.ndarray, target: np.ndarray) -> int:
    return int(np.argmin(_gephi_distance_sq(samples, target)))


def _gephi_distance_sq(samples: np.ndarray, target: np.ndarray) -> np.ndarray:
    delta = samples - target
    return np.sum(delta * delta, axis=1)


def _gephi_sort_colors(colors: np.ndarray) -> np.ndarray:
    if len(colors) <= 1:
        return colors

    remaining = list(range(len(colors)))
    sorted_indices = [remaining.pop(0)]

    while remaining:
        candidate_colors = colors[remaining]
        current_colors = colors[sorted_indices]
        distances = np.min(
            np.sum(
                (candidate_colors[:, None, :] - current_colors[None, :, :]) ** 2,
                axis=2,
            ),
            axis=1,
        )
        next_index = int(np.argmax(distances))
        sorted_indices.append(remaining.pop(next_index))

    return colors[sorted_indices]


def _gephi_check_color(lab: np.ndarray, filter_values: GephiFilter) -> bool:
    rgb = _gephi_lab_to_rgb(lab)
    hue, chroma, luminance = _gephi_lab_to_hcl(lab)
    hmin, hmax, cmin, cmax, lmin, lmax = filter_values

    hue_ok = hmin <= hue <= hmax if hmin < hmax else hue >= hmin or hue <= hmax

    return bool(
        not np.isnan(rgb).any()
        and np.all(rgb >= 0)
        and np.all(rgb < 256)
        and hue_ok
        and cmin <= chroma <= cmax
        and lmin <= luminance <= lmax
    )


def _gephi_lab_to_hex(lab: np.ndarray) -> str:
    red, green, blue = (int(value) for value in _gephi_lab_to_rgb(lab))
    return f"#{red:02X}{green:02X}{blue:02X}"


def _gephi_lab_to_rgb(lab: np.ndarray) -> np.ndarray:
    return _gephi_xyz_to_rgb(_gephi_lab_to_xyz(lab))


def _gephi_lab_to_xyz(lab: np.ndarray) -> np.ndarray:
    sl = (lab[0] + 0.16) / 1.16
    illuminant = np.array([0.96421, 1.0, 0.82519])
    y_value = illuminant[1] * _gephi_finv(sl)
    x_value = illuminant[0] * _gephi_finv(sl + (lab[1] / 5))
    z_value = illuminant[2] * _gephi_finv(sl - (lab[2] / 2))
    return np.array([x_value, y_value, z_value])


def _gephi_xyz_to_rgb(xyz: np.ndarray) -> np.ndarray:
    red_linear = 3.2406 * xyz[0] - 1.5372 * xyz[1] - 0.4986 * xyz[2]
    green_linear = -0.9689 * xyz[0] + 1.8758 * xyz[1] + 0.0415 * xyz[2]
    blue_linear = 0.0557 * xyz[0] - 0.204 * xyz[1] + 1.057 * xyz[2]

    if (
        min(red_linear, green_linear, blue_linear) < -0.001
        or max(red_linear, green_linear, blue_linear) > 1.001
    ):
        red_linear = min(max(red_linear, 0), 1)
        green_linear = min(max(green_linear, 0), 1)
        blue_linear = min(max(blue_linear, 0), 1)

    return np.array(
        [
            round(255 * _gephi_correct1(red_linear)),
            round(255 * _gephi_correct1(green_linear)),
            round(255 * _gephi_correct1(blue_linear)),
        ],
        dtype=float,
    )


def _gephi_lab_to_hcl(lab: np.ndarray) -> tuple[float, float, float]:
    luminance = (lab[0] - 0.09) / 0.61
    radius = math.sqrt(lab[1] ** 2 + lab[2] ** 2)
    chroma = radius / (luminance * 0.311 + 0.125)
    angle = math.atan2(lab[1], lab[2])
    hue = ((math.tau / 6 - angle) / math.tau) * 360

    if hue < 0:
        hue += 360

    return hue, chroma, luminance


def _gephi_finv(value: float) -> float:
    threshold = 6 / 29
    if value > threshold:
        return value**3
    return 3 * threshold**2 * (value - (4 / 29))


def _gephi_correct1(channel: float) -> float:
    alpha = 0.055
    if channel <= 0.0031308:
        return 12.92 * channel
    return (1 + alpha) * channel ** (1 / 2.4) - alpha


def pal_gephi(palette: str = "default", alpha: float = 1.0) -> PaletteFunc:
    """
    Gephi generative color palette.

    Args:
        palette: Palette name. See `GEPHI_PALETTES` for available options.
        alpha: Transparency level, between 0 and 1.

    Details:
        Uses NumPy's global random state directly. Call `numpy.random.seed()`
        before generating colors or drawing a plot to get reproducible output.

    Returns:
        A callable that takes n and returns a color sequence.

    Raises:
        ValueError: If the palette name, alpha, or requested size is invalid.
    """
    if palette not in GEPHI_PALETTES:
        raise ValueError(f"Unknown Gephi palette: {palette}")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    filter_values = GEPHI_FILTERS[palette]

    def palette_func(n: int) -> Sequence[str]:
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if n == 0:
            return []

        colors = _gephi_generate_palette(n, filter_values)
        if alpha < 1:
            return apply_alpha(colors, alpha)
        return colors

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
        palette: Palette name: "hallmarks_dark", "hallmarks_light",
            or "signature_substitutions".
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
