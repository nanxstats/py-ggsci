from collections.abc import Mapping, Sequence
from typing import cast

from plotnine.data import diamonds
from plotnine.geoms import geom_bar, geom_point, geom_smooth
from plotnine.ggplot import ggplot

from ggsci import example_barplot, example_scatterplot


def test_example_scatterplot_configuration() -> None:
    plot = example_scatterplot()

    assert isinstance(plot, ggplot)
    assert len(plot.layers) == 2
    assert plot.mapping["color"] == "cut"
    assert plot.mapping["x"] == "table"
    assert plot.mapping["y"] == "price"

    data = cast(Mapping[str, Sequence[float]], plot.data)
    carat = cast(Sequence[float], data["carat"])
    assert all(value >= 2.2 for value in carat)
    assert isinstance(plot.layers[0].geom, geom_point)
    assert isinstance(plot.layers[1].geom, geom_smooth)


def test_example_barplot_configuration() -> None:
    plot = example_barplot()

    assert isinstance(plot, ggplot)
    assert plot.data is diamonds
    assert plot.mapping["x"] == "color"
    assert plot.mapping["fill"] == "cut"
    assert len(plot.layers) == 1
    assert isinstance(plot.layers[0].geom, geom_bar)
