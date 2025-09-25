"""Tests for ggsci.palette functions (discrete and continuous)."""

from __future__ import annotations

import inspect
from collections.abc import Callable

import pytest

from ggsci import palettes as pl
from ggsci.data import PALETTES
from ggsci.data_iterm import ITERM_PALETTES, PALETTES_ITERM


def _is_continuous_palette(func: Callable[..., object]) -> bool:
    sig = inspect.signature(func)
    return "n" in sig.parameters


def _alpha_hex(alpha: float) -> str:
    return f"{int(alpha * 255):02x}"


def _all_palette_functions() -> dict[str, Callable[..., object]]:
    return {name[4:]: getattr(pl, name) for name in dir(pl) if name.startswith("pal_")}


def _discrete_and_continuous() -> tuple[list[str], list[str]]:
    funcs = _all_palette_functions()
    discrete = [name for name, fn in funcs.items() if not _is_continuous_palette(fn)]
    continuous = [name for name, fn in funcs.items() if _is_continuous_palette(fn)]
    return sorted(discrete), sorted(continuous)


DISCRETE_NAMES, CONTINUOUS_NAMES = _discrete_and_continuous()


def _iter_discrete_palette_cases(
    name: str,
) -> list[tuple[str, list[str], dict[str, str]]]:
    if name == "iterm":
        cases: list[tuple[str, list[str], dict[str, str]]] = []
        for palette_key, variants in PALETTES_ITERM.items():
            for variant, colors in variants.items():
                cases.append((palette_key, list(colors), {"variant": variant}))
        return cases

    return [
        (palette_key, list(colors), {})
        for palette_key, colors in PALETTES[name].items()
    ]


@pytest.mark.parametrize("name", DISCRETE_NAMES)
def test_discrete_palette_happy_path_and_alpha(name: str):
    func: Callable[..., Callable[[int], list[str]]] = getattr(pl, f"pal_{name}")

    # Validate each available sub-palette for this family
    palette_iter = _iter_discrete_palette_cases(name)

    for palette_key, colors, extra_kwargs in palette_iter:
        # Happy path
        pal_fn = func(palette=palette_key, alpha=1.0, **extra_kwargs)
        n = min(3, len(colors))
        out = pal_fn(n)
        assert isinstance(out, list) and len(out) == n
        assert all(c.startswith("#") and len(c) == 7 for c in out)

        # Too many requested colors -> error
        with pytest.raises(ValueError):
            pal_fn(len(colors) + 1)

        # Alpha applied in discrete palette function
        pal_fn_a = func(palette=palette_key, alpha=0.6, **extra_kwargs)
        out_a = pal_fn_a(1)
        assert len(out_a) == 1 and out_a[0].startswith("#") and len(out_a[0]) == 9
        assert out_a[0][-2:] == _alpha_hex(0.6)


@pytest.mark.parametrize("name", DISCRETE_NAMES)
def test_discrete_palette_errors(name: str):
    func: Callable[..., Callable[[int], list[str]]] = getattr(pl, f"pal_{name}")

    with pytest.raises(ValueError):
        func(palette="__unknown__", alpha=1.0)

    if name == "iterm":
        first_palette = ITERM_PALETTES[0]
        with pytest.raises(ValueError):
            func(palette=first_palette, variant="__unknown__")

    for bad_alpha in (0.0, -0.1, 1.0 + 1e-9):
        with pytest.raises(ValueError):
            func(alpha=bad_alpha)


@pytest.mark.parametrize("name", CONTINUOUS_NAMES)
def test_continuous_palette_happy_path_reverse_alpha(name: str):
    func: Callable[..., list[str]] = getattr(pl, f"pal_{name}")

    # Exercise all palettes for the family (kept small n for speed)
    for palette_key in PALETTES[name].keys():
        # Forward
        out = func(palette=palette_key, n=7, alpha=1.0, reverse=False)
        assert isinstance(out, list) and len(out) == 7
        assert all(c.startswith("#") and len(c) == 7 for c in out)

        # Reverse
        out_r = func(palette=palette_key, n=7, alpha=1.0, reverse=True)
        assert out_r == out[::-1]

        # Alpha applied post-interpolation
        out_a = func(palette=palette_key, n=5, alpha=0.6, reverse=False)
        assert all(c.startswith("#") and len(c) == 9 for c in out_a)
        assert out_a[0][-2:] == _alpha_hex(0.6)


@pytest.mark.parametrize("name", CONTINUOUS_NAMES)
def test_continuous_palette_errors(name: str):
    func: Callable[..., list[str]] = getattr(pl, f"pal_{name}")

    with pytest.raises(ValueError):
        func(palette="__unknown__")

    for bad_alpha in (0.0, -0.1, 1.0 + 1e-9):
        with pytest.raises(ValueError):
            func(alpha=bad_alpha)
