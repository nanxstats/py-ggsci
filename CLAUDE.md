# py-ggsci package design notes

## Overview

Python port of the R package ggsci providing color palettes for plotnine.

## Package structure

```
src/ggsci/
├── __init__.py     # Main exports
├── data.py         # Color palette data (hex strings)
├── palettes.py     # Palette generation functions
├── scales.py       # Plotnine scale implementations
└── utils.py        # Color utilities (alpha, interpolation)
```

## Key design decisions

### 1. Pure Python data storage

- Color data stored directly in Python dict (not TOML)
- No runtime parsing overhead
- Better IDE support and type hints
- Follows mizani pattern

### 2. Two scale patterns

**Discrete scales**: Use `@dataclass` with `InitVar` and `__post_init__`

```python
@dataclass
class scale_color_npg(scale_discrete):
    palette: InitVar[str] = "nrc"
    alpha: InitVar[float] = 1.0

    def __post_init__(self, palette, alpha):
        super().__post_init__()
        self.palette = pal_npg(palette, alpha)
```

**Continuous scales**: Use functions that return `scale_*_gradientn`

```python
def scale_color_gsea(palette="default", alpha=1.0, reverse=False, **kwargs):
    colors = pal_gsea(palette, n=512, alpha=alpha, reverse=reverse)
    return scale_color_gradientn(colors=colors, **kwargs)
```

### 3. Palette function types

- **Discrete**: Return callable `(n: int) -> List[str]`
- **Continuous**: Return `List[str]` directly

## Critical implementation details

### Plotnine imports

```python
from plotnine.scales.scale_discrete import scale_discrete
from plotnine.scales import scale_color_gradientn, scale_fill_gradientn
```

### Alpha handling

- Discrete: Applied in palette function, returns RGBA hex
- Continuous: Applied during interpolation

### Aliases

```python
scale_colour_npg = scale_color_npg  # etc.
```

## Testing & demo

- `tests/`: Unit tests using pytest
- `examples/demo.py`: Visual demos with plot generation

## Commands for development

```bash
# Run tests
uv run python test.py

# Generate demo plots
uv run python examples/demo.py

# Check structure
find src/ -name "*.py"
```

## Import usage

```python
from ggsci import (
    scale_color_npg, scale_fill_npg,        # Discrete NPG
    scale_color_flatui,                     # Discrete FlatUI
    scale_color_gsea, scale_fill_gsea,      # Continuous diverging
    scale_color_bs5, scale_fill_bs5,        # Continuous sequential
    pal_npg, pal_flatui, pal_gsea, pal_bs5  # Palette functions
)
```

## Architecture benefits

- **Clean**: Flattened structure, no nested subdirs
- **Pythonic**: Follows plotnine/dataclass patterns
- **Performant**: No file parsing, direct data access
- **Extensible**: Clear patterns for adding new scales
- **Compatible**: Seamless plotnine integration
