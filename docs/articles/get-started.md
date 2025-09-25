# Get started

ggsci for Python offers a collection of plotnine color palettes inspired by
scientific journals, data visualization libraries, science fiction movies,
and TV shows. Palettes are exposed as plotnine scales:

- `scale_color_palname()` / `scale_colour_palname()`
- `scale_fill_palname()`

This article mirrors the original R package vignette using plotnine.

```python
import numpy as np
import pandas as pd
from plotnine import *
from plotnine.data import diamonds, mtcars

from ggsci import *

LAST = None
```

```python exec="on" session="default"
# Imports shared by all chunks in this article
import base64
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotnine import (
    aes,
    element_blank,
    element_rect,
    geom_tile,
    ggplot,
    scale_fill_identity,
    scale_x_continuous,
    scale_y_continuous,
    theme,
    theme_bw,
    theme_dark,
    theme_void,
)
from plotnine.data import diamonds, mtcars
from plotnine.options import set_option

from ggsci import *

# Match the vignette's aspect ratio across figures
W_DEFAULT, H_DEFAULT = 10.6667, 3.3334
set_option("figure_size", (W_DEFAULT, H_DEFAULT))


# Helper to render any plotnine plot/composition as inline PNG
def render_png(
    obj, *, width: float | None = None, height: float | None = None, dpi: int = 150
) -> str:
    fig = obj.draw()
    try:
        if width and height:
            fig.set_size_inches(width, height, forward=True)
        buf = BytesIO()
        fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight")
        data = base64.b64encode(buf.getvalue()).decode("ascii")
        return f'<img src="data:image/png;base64,{data}" alt="plot" />'
    finally:
        plt.close(fig)


# A shared handle for the last-computed plot/composition
LAST = None
```

## Discrete color palettes

We will use reusable helpers that construct a scatter plot with a smoothed
curve and a side-by-side bar plot to demonstrate discrete palettes. The
examples below use the `diamonds` dataset and apply each palette to `color`
and `fill` scales respectively.

```python exec="on" source="above" session="default"
# Base plots shared for discrete palette demos
p1 = example_scatterplot()
p2 = example_barplot()
```

### NPG

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_npg()) | (p2 + scale_fill_npg())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### AAAS

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_aaas()) | (p2 + scale_fill_aaas())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### NEJM

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_nejm()) | (p2 + scale_fill_nejm())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Lancet

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_lancet()) | (p2 + scale_fill_lancet())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### JAMA

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_jama()) | (p2 + scale_fill_jama())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### BMJ

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_bmj()) | (p2 + scale_fill_bmj())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### JCO

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_jco()) | (p2 + scale_fill_jco())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### UCSCGB

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_ucscgb()) | (p2 + scale_fill_ucscgb())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### D3 (category10)

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_d3("category10")) | (p2 + scale_fill_d3("category10"))
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Observable 10

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_observable()) | (p2 + scale_fill_observable())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Primer

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_primer()) | (p2 + scale_fill_primer())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Atlassian

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_atlassian()) | (p2 + scale_fill_atlassian())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### iTerm

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_iterm("Rose Pine")) | (p2 + scale_fill_iterm("Rose Pine"))
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

You can preview these color palettes in ggsci on a dedicated microsite:
<https://nanx.me/ggsci-iterm/>. It renders example plots for all palettes
on a single page for fast visual comparison.

### LocusZoom

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_locuszoom()) | (p2 + scale_fill_locuszoom())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### IGV (chromosomes)

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_igv()) | (p2 + scale_fill_igv())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### COSMIC

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_cosmic("hallmarks_light")) | (p2 + scale_fill_cosmic("hallmarks_light"))
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_cosmic("hallmarks_dark")) | (p2 + scale_fill_cosmic("hallmarks_dark"))
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_cosmic("signature_substitutions")) | (p2 + scale_fill_cosmic("signature_substitutions"))
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### UChicago

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_uchicago()) | (p2 + scale_fill_uchicago())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Star Trek

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_startrek()) | (p2 + scale_fill_startrek())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Tron Legacy (use with dark theme)

```python exec="on" session="default" source="above"
LAST = (p1 + theme_dark() + scale_color_tron()) | (p2 + theme_dark() + scale_fill_tron())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Futurama

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_futurama()) | (p2 + scale_fill_futurama())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Rick and Morty

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_rickandmorty()) | (p2 + scale_fill_rickandmorty())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### The Simpsons

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_simpsons()) | (p2 + scale_fill_simpsons())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Flat UI

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_flatui()) | (p2 + scale_fill_flatui())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

### Frontiers

```python exec="on" session="default" source="above"
LAST = (p1 + scale_color_frontiers()) | (p2 + scale_fill_frontiers())
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

## Continuous color palettes

There are two types of continuous palettes: diverging and sequential.
We demonstrate with a correlation heatmap and a small random matrix.

```python exec="on" source="above" session="default"
# Correlation matrix for diverging palettes (numeric columns only)
cor = mtcars.select_dtypes(include=[np.number]).corr()
cor_melt = (
    cor.stack()
    .reset_index()
    .rename(columns={"level_0": "Var1", "level_1": "Var2", 0: "value"})
)

p3 = (
    ggplot(cor_melt, aes("Var1", "Var2", fill="value"))
    + geom_tile(color="black", size=0.3)
    + theme_void()
)

# Random upper-triangular matrix for sequential palettes
np.random.seed(42)
k = 6
x = np.eye(k)
iu = np.triu_indices(k, 1)
x[iu] = np.random.uniform(0, 1, size=len(iu[0]))
x_melt = (
    pd.DataFrame(x)
    .stack()
    .reset_index()
    .rename(columns={"level_0": "Var1", "level_1": "Var2", 0: "value"})
)

p4 = (
    ggplot(x_melt, aes("Var1", "Var2", fill="value"))
    + geom_tile(color="black", size=0.3)
    + scale_x_continuous(expand=(0, 0))
    + scale_y_continuous(expand=(0, 0))
    + theme_bw()
    + theme(
        legend_position="none",
        plot_background=element_rect(fill="white"),
        panel_background=element_rect(fill="white"),
        axis_title_x=element_blank(),
        axis_title_y=element_blank(),
        axis_text_x=element_blank(),
        axis_text_y=element_blank(),
        axis_ticks=element_blank(),
        axis_line=element_blank(),
        panel_border=element_blank(),
        panel_grid_major=element_blank(),
        panel_grid_minor=element_blank(),
    )
)

# Placeholder panel to pad compositions to equal column counts
def blank_panel():
    # Build a grid matching p4's tile layout, but with white tiles (no fill mapping)
    try:
        df = x_melt[["Var1", "Var2"]].copy()
    except NameError:
        # Fallback to a 6x6 grid if x_melt is not yet defined
        k = 6
        df = pd.DataFrame(
            [(i, j) for i in range(k) for j in range(k)], columns=["Var1", "Var2"]
        )
    return (
        ggplot(df, aes("Var1", "Var2"))
        + geom_tile(fill="white", color="black", size=0.3)
        + scale_x_continuous(expand=(0, 0))
        + scale_y_continuous(expand=(0, 0))
        + theme_bw()
        + theme(
            legend_position="none",
            plot_background=element_rect(fill="white"),
            panel_background=element_rect(fill="white"),
            axis_title_x=element_blank(),
            axis_title_y=element_blank(),
            axis_text_x=element_blank(),
            axis_text_y=element_blank(),
            axis_ticks=element_blank(),
            axis_line=element_blank(),
            panel_border=element_blank(),
            panel_grid_major=element_blank(),
            panel_grid_minor=element_blank(),
        )
    )
```

### GSEA (diverging)

```python exec="on" session="default" source="above"
LAST = (p3 + scale_fill_gsea()) | (p3 + scale_fill_gsea(reverse=True))
```

```python exec="on" session="default" html="true"
print(render_png(LAST, width=W_DEFAULT, height=4.0))
```

### Bootstrap 5 (sequential)

```python exec="on" session="default" source="above"
row1 = (
    (p4 + scale_fill_bs5("blue"))
    | (p4 + scale_fill_bs5("indigo"))
    | (p4 + scale_fill_bs5("purple"))
    | (p4 + scale_fill_bs5("pink"))
    | (p4 + scale_fill_bs5("red"))
    | (p4 + scale_fill_bs5("orange"))
    | (p4 + scale_fill_bs5("yellow"))
    | (p4 + scale_fill_bs5("green"))
)
row2 = (
    (p4 + scale_fill_bs5("teal"))
    | (p4 + scale_fill_bs5("cyan"))
    | (p4 + scale_fill_bs5("gray"))
    | blank_panel()
    | blank_panel()
    | blank_panel()
    | blank_panel()
    | blank_panel()
)
LAST = row1 / row2
```

```python exec="on" session="default" html="true"
print(render_png(LAST, width=W_DEFAULT, height=2.6))
```

### Material Design (sequential)

```python exec="on" session="default" source="above"
row1 = (
    (p4 + scale_fill_material("red"))
    | (p4 + scale_fill_material("pink"))
    | (p4 + scale_fill_material("purple"))
    | (p4 + scale_fill_material("deep-purple"))
    | (p4 + scale_fill_material("indigo"))
    | (p4 + scale_fill_material("blue"))
    | (p4 + scale_fill_material("light-blue"))
    | (p4 + scale_fill_material("cyan"))
)
row2 = (
    (p4 + scale_fill_material("teal"))
    | (p4 + scale_fill_material("green"))
    | (p4 + scale_fill_material("light-green"))
    | (p4 + scale_fill_material("lime"))
    | (p4 + scale_fill_material("yellow"))
    | (p4 + scale_fill_material("amber"))
    | (p4 + scale_fill_material("orange"))
    | (p4 + scale_fill_material("deep-orange"))
)
row3 = (
    (p4 + scale_fill_material("brown"))
    | (p4 + scale_fill_material("grey"))
    | (p4 + scale_fill_material("blue-grey"))
    | blank_panel()
    | blank_panel()
    | blank_panel()
    | blank_panel()
    | blank_panel()
)
LAST = row1 / row2 / row3
```

```python exec="on" session="default" html="true"
print(render_png(LAST, width=W_DEFAULT, height=3.8))
```

### Tailwind CSS 3 (sequential)

```python exec="on" session="default" source="above"
row1 = (
    (p4 + scale_fill_tw3("slate"))
    | (p4 + scale_fill_tw3("gray"))
    | (p4 + scale_fill_tw3("zinc"))
    | (p4 + scale_fill_tw3("neutral"))
    | (p4 + scale_fill_tw3("stone"))
    | (p4 + scale_fill_tw3("red"))
    | (p4 + scale_fill_tw3("orange"))
    | (p4 + scale_fill_tw3("amber"))
)
row2 = (
    (p4 + scale_fill_tw3("yellow"))
    | (p4 + scale_fill_tw3("lime"))
    | (p4 + scale_fill_tw3("green"))
    | (p4 + scale_fill_tw3("emerald"))
    | (p4 + scale_fill_tw3("teal"))
    | (p4 + scale_fill_tw3("cyan"))
    | (p4 + scale_fill_tw3("sky"))
    | (p4 + scale_fill_tw3("blue"))
)
row3 = (
    (p4 + scale_fill_tw3("indigo"))
    | (p4 + scale_fill_tw3("violet"))
    | (p4 + scale_fill_tw3("purple"))
    | (p4 + scale_fill_tw3("fuchsia"))
    | (p4 + scale_fill_tw3("pink"))
    | (p4 + scale_fill_tw3("rose"))
    | blank_panel()
    | blank_panel()
)
LAST = row1 / row2 / row3
```

```python exec="on" session="default" html="true"
print(render_png(LAST, width=W_DEFAULT, height=3.8))
```

## Use palette functions outside plotnine

You can use palette generator functions to get hex color codes directly for
other plotting systems.

```python exec="on" source="above" session="default"
mypal = pal_observable("observable10", alpha=0.7)(10)
df_cols = pd.DataFrame({"x": range(len(mypal)), "fill": mypal})
LAST = (
    ggplot(df_cols, aes("x", 1, fill="fill"))
    + geom_tile(width=1, height=1)
    + scale_fill_identity(guide=None)
    + theme_void()
)
```

```python exec="on" session="default" html="true"
print(render_png(LAST))
```

## Discussion

Some palettes may not be optimal for specific needs such as color-blind safety,
photocopy safety, or print-friendliness. Consider alternatives like
ColorBrewer or viridis when these constraints apply. Palettes in ggsci are for
research and demonstration purposes only.
