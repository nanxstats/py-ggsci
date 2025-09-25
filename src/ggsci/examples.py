"""
Example plots used in documentation and demos.
"""

from __future__ import annotations

from plotnine import (
    aes,
    element_blank,
    geom_bar,
    geom_point,
    geom_smooth,
    ggplot,
    position_dodge,
    theme,
    theme_minimal,
)
from plotnine.data import diamonds


def example_scatterplot() -> ggplot:
    """
    Create the scatter plot example used in documentation.

    Args:
        None.

    Returns:
        Plot configured for discrete color palette demonstrations.

    Raises:
        None.
    """
    large_diamonds = diamonds.loc[diamonds["carat"] >= 2.2]

    return (
        ggplot(large_diamonds, aes("table", "price", color="cut"))
        + geom_point(alpha=0.7)
        + geom_smooth(method="lm", alpha=0.05, size=1)
        + theme_minimal()
        + theme(
            axis_title_x=element_blank(),
            axis_title_y=element_blank(),
            panel_grid_minor=element_blank(),
        )
    )


def example_barplot() -> ggplot:
    """
    Create the bar plot example used in documentation.

    Args:
        None.

    Returns:
        Plot configured for discrete fill palette demonstrations.

    Raises:
        None.
    """
    return (
        ggplot(diamonds, aes("color", fill="cut"))
        + geom_bar(position=position_dodge())
        + theme_minimal()
        + theme(
            axis_title_x=element_blank(),
            axis_title_y=element_blank(),
            panel_grid_major_x=element_blank(),
            panel_grid_minor_y=element_blank(),
        )
    )
