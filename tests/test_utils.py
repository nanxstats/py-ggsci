"""Tests for ggsci.utils helpers."""

from __future__ import annotations

import pytest

from ggsci.utils import apply_alpha, hex_to_rgb, interpolate_colors, rgb_to_hex


def test_hex_to_rgb_and_back():
    # Basic round-trip for full intensity channels
    assert hex_to_rgb("#ffffff") == (255, 255, 255)
    assert hex_to_rgb("#000000") == (0, 0, 0)

    # to_hex returns lowercase, verify known mapping
    assert rgb_to_hex((1.0, 0.0, 0.0)) == "#ff0000"
    assert rgb_to_hex((0.0, 1.0, 0.0)) == "#00ff00"
    assert rgb_to_hex((0.0, 0.0, 1.0)) == "#0000ff"


@pytest.mark.parametrize(
    "colors,alpha,expected_suffix",
    [
        (
            [
                "#ffffff",
            ],
            0.5,
            "7f",
        ),
        (["#000000"], 1.0, "ff"),
        (["#abcdef"], 0.0 + 1e-9, "00"),
    ],
)
def test_apply_alpha(colors: list[str], alpha: float, expected_suffix: str):
    out = apply_alpha(colors, alpha)
    assert len(out) == len(colors)
    assert all(v.startswith("#") and len(v) == 9 for v in out)
    # Last two digits encode alpha
    assert out[0][-2:] == expected_suffix


def test_interpolate_colors_endpoints_and_sampling():
    # Interpolation across two endpoints keeps ends intact
    colors = interpolate_colors(["#ff0000", "#0000ff"], 5)
    assert len(colors) == 5
    assert colors[0] == "#ff0000"
    assert colors[-1] == "#0000ff"

    # When n <= len(colors), sample endpoints evenly
    base = ["#000000", "#111111", "#222222"]
    sampled = interpolate_colors(base, 2)
    assert sampled == [base[0], base[-1]]
