"""
Demo of py-ggsci scales with plotnine

This script demonstrates how to use the py-ggsci color scales
with plotnine for creating publication-ready plots.
"""

import numpy as np
import pandas as pd
from plotnine import aes, geom_bar, geom_point, geom_tile, ggplot, labs, theme_minimal

from ggsci import scale_color_npg, scale_fill_bs5, scale_fill_flatui, scale_fill_gsea


def demo_npg_discrete():
    """Demo NPG discrete scale with scatter plot."""
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame(
        {
            "x": np.random.randn(100),
            "y": np.random.randn(100),
            "category": np.random.choice(["A", "B", "C", "D", "E"], 100),
        }
    )

    # Create plot
    plot = (
        ggplot(data, aes(x="x", y="y", color="category"))
        + geom_point(size=3, alpha=0.7)
        + scale_color_npg()
        + theme_minimal()
        + labs(
            title="NPG Color Scale Demo",
            subtitle="Nature Publishing Group inspired colors",
            x="X Value",
            y="Y Value",
        )
    )

    return plot


def demo_flatui_variations():
    """Demo FlatUI scale with its three variations."""
    # Create sample data
    np.random.seed(42)
    categories = ["A", "B", "C", "D", "E", "F"]
    values = np.random.randint(10, 100, len(categories))
    data = pd.DataFrame({"category": categories, "value": values})

    # Create and save three separate plots
    palettes = ["default", "flattastic", "aussie"]
    for palette in palettes:
        plot = (
            ggplot(data, aes(x="category", y="value", fill="category"))
            + geom_bar(stat="identity")
            + scale_fill_flatui(palette=palette)
            + theme_minimal()
            + labs(
                title=f"Flat UI Color Scale - {palette.title()}",
                x="Category",
                y="Value",
            )
        )
        plot.save(f"flatui_{palette}.png", dpi=150, width=8, height=6)
        print(f"Saved flatui_{palette}.png")

    # Return None since we've already saved the individual files
    return None


def demo_gsea_continuous():
    """Demo GSEA continuous diverging scale with heatmap."""
    # Create correlation matrix data
    np.random.seed(42)
    n_vars = 10
    corr_matrix = np.random.randn(n_vars, n_vars)
    corr_matrix = (corr_matrix + corr_matrix.T) / 2  # Make symmetric
    np.fill_diagonal(corr_matrix, 1)

    # Convert to long format for plotnine
    data = []
    for i in range(n_vars):
        for j in range(n_vars):
            data.append(
                {
                    "var1": f"V{i + 1}",
                    "var2": f"V{j + 1}",
                    "correlation": corr_matrix[i, j],
                }
            )

    data = pd.DataFrame(data)

    # Create heatmap
    plot = (
        ggplot(data, aes(x="var1", y="var2", fill="correlation"))
        + geom_tile()
        + scale_fill_gsea()
        + theme_minimal()
        + labs(
            title="GSEA Diverging Color Scale",
            subtitle="GSEA GenePattern inspired heatmap colors",
            x="Variable 1",
            y="Variable 2",
        )
    )

    return plot


def demo_bs5_sequential():
    """Demo BS5 continuous sequential scale."""
    # Create gradient data
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Convert to dataframe
    data = pd.DataFrame({"x": X.flatten(), "y": Y.flatten(), "z": Z.flatten()})

    # Create plot with different BS5 palettes
    plot = (
        ggplot(data.sample(5000), aes(x="x", y="y", fill="z"))
        + geom_tile()
        + scale_fill_bs5(palette="teal")
        + theme_minimal()
        + labs(
            title="Bootstrap 5 Sequential Color Scale",
            subtitle='Using the "teal" palette',
            x="X",
            y="Y",
            fill="Value",
        )
    )

    return plot


if __name__ == "__main__":
    print("Generating demo plots...")

    # Demo each scale type
    plots = {
        "npg_discrete": demo_npg_discrete(),
        "flatui_variations": demo_flatui_variations(),
        "gsea_continuous": demo_gsea_continuous(),
        "bs5_sequential": demo_bs5_sequential(),
    }

    # Save plots (requires plotnine to be properly configured)
    for name, plot in plots.items():
        if plot is not None:  # Skip None plots (like flatui_variations)
            try:
                plot.save(f"{name}.png", dpi=150, width=10, height=8)
                print(f"Saved {name}.png")
            except Exception as e:
                print(f"Could not save {name}.png: {e}")

    print("\nDemo complete!")
    print("\nYou can use these scales in your plotnine plots:")
    print("- scale_color_npg() / scale_fill_npg()")
    print("- scale_color_flatui() / scale_fill_flatui()")
    print("- scale_color_gsea() / scale_fill_gsea()")
    print("- scale_color_bs5() / scale_fill_bs5()")
