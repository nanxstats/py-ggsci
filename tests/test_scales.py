"""Tests for ggsci.scales (discrete classes, continuous functions, aliases)."""

from __future__ import annotations

import inspect
from collections.abc import Callable

import pytest
from plotnine.scales import scale_color_gradientn, scale_fill_gradientn

import ggsci.scales as sc


def _discrete_scale_classes() -> list[tuple[str, type]]:
    items: list[tuple[str, type]] = []
    for name, obj in sc.__dict__.items():
        if not isinstance(obj, type):
            continue
        if not issubclass(obj, sc.scale_discrete):
            continue
        # Skip the base class itself
        if name == "scale_discrete":
            continue
        items.append((name, obj))
    return items


def _continuous_scale_factories() -> list[tuple[str, Callable[..., object]]]:
    return [
        (name, obj)
        for name, obj in sc.__dict__.items()
        if name.startswith("scale_color_")
        and callable(obj)
        and not isinstance(obj, type)
        and "gradientn" in inspect.getsource(sc.__dict__[name]).lower()
    ] + [
        (name, obj)
        for name, obj in sc.__dict__.items()
        if name.startswith("scale_fill_")
        and callable(obj)
        and not isinstance(obj, type)
        and "gradientn" in inspect.getsource(sc.__dict__[name]).lower()
    ]


@pytest.mark.parametrize("name,cls", _discrete_scale_classes())
def test_discrete_scales_aesthetics_and_palette(name: str, cls: type):
    s = cls()
    if name.startswith("scale_color_") or name.startswith("scale_colour_"):
        assert s._aesthetics == ["color"]
    elif name.startswith("scale_fill_"):
        assert s._aesthetics == ["fill"]
    else:
        pytest.fail(f"Unexpected discrete scale name: {name}")

    # Palette is a callable taking n and returning list[str]
    colors = s.palette(3)
    assert isinstance(colors, list) and len(colors) == 3
    assert all(c.startswith("#") and len(c) == 7 for c in colors)

    # Alpha is applied via InitVar
    s_alpha = cls(alpha=0.6)
    out = s_alpha.palette(1)
    assert len(out) == 1 and out[0].startswith("#") and len(out[0]) == 9
    assert out[0][-2:] == f"{int(0.6 * 255):02x}"


@pytest.mark.parametrize("name,fn", _continuous_scale_factories())
def test_continuous_scale_return_types(name: str, fn: Callable[..., object]):
    obj = fn()
    if name.startswith("scale_color_"):
        assert isinstance(obj, scale_color_gradientn)
    else:
        assert isinstance(obj, scale_fill_gradientn)


def test_british_aliases_identity():
    # All scale_colour_* should be the same object as scale_color_*
    uk_names = [n for n in sc.__dict__ if n.startswith("scale_colour_")]
    for uk in uk_names:
        us = uk.replace("colour", "color")
        assert hasattr(sc, us)
        assert getattr(sc, uk) is getattr(sc, us)


def test_init_exports_alignment():
    # Importing from package root should expose the same objects
    import ggsci as pkg

    names = [
        # Sample a few across types to ensure import surface
        "scale_color_npg",
        "scale_fill_npg",
        "scale_colour_npg",
        "scale_color_gsea",
        "scale_fill_bs5",
        "pal_npg",
        "pal_gsea",
    ]
    for name in names:
        assert hasattr(pkg, name)
        # Identity with module definitions
        mod = (
            sc
            if name.startswith("scale_")
            else __import__("ggsci.palettes", fromlist=[name])
        )
        assert getattr(pkg, name) is getattr(mod, name)
