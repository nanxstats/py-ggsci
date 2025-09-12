# py-ggsci package design notes

## Overview

Python port of the R package ggsci providing color palettes for plotnine.

## Package structure

```
- src/ggsci/
  - __init__.py     # Main exports
  - data.py         # Color palette data (hex strings)
  - palettes.py     # Palette generation functions
  - scales.py       # Plotnine scale implementations
  - utils.py        # Color utilities (alpha, interpolation)
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

## Testing

- `tests/`: Unit tests using pytest

## Commands for development

```bash
# Run tests
uv run pytest
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

## Typing & docstring conventions

- Prefer generic ABCs for parameters: import from `collections.abc` (e.g., `Sequence[str]`, `Mapping[... ]`).
- Use built-in generics (PEP 585): `list[str]`, `tuple[int, ...]`; for unions use `A | B | None` with `None` last.
- Return types should be as general as reasonable (e.g., `Sequence[str]`), even if implementation returns a `list`.
- Use `TypeAlias` for repeated callable signatures (e.g., `PaletteFunc = Callable[[int], Sequence[str]]`).
- Discrete palette fns return a callable (`PaletteFunc`); continuous palette fns return `Sequence[str]` directly.
- Discrete scales: dataclass with `InitVar` fields; annotate `__post_init__(palette: str, alpha: float) -> None`; set palette via `setattr(self, "palette", pal_...(...))` to avoid mypy method-assign issues.
- Continuous scales: thin functions returning `scale_*_gradientn`; type `**kwargs: Any` and explicit return type (`scale_color_gradientn`/`scale_fill_gradientn`).
- Docstrings use indentation-based style with sections: summary line, `Args`, `Returns`, `Raises`. Do not repeat types in the docstring (they are in the signature).
- Do not edit `data.py` by hand; it is generated.
- Keep British spelling aliases (`scale_colour_*`) in sync with `scale_color_*`.
- Ensure `mypy .` passes before submitting changes.
