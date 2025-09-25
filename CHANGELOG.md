# Changelog

## py-ggsci 1.0.0

### New features

- Added `scale_color_primer()` and `scale_fill_primer()` for the
  Primer (GitHub) design system palette (#29).
- Added `scale_color_atlassian()` and `scale_fill_atlassian()` for the
  Atlassian Design System palette (#29).
- Added `scale_color_iterm()` and `scale_fill_iterm()`,
  providing over 400 new iTerm color palettes (#30).

### Improvements

- Introduced `example_scatterplot()` and `example_barplot()` to simplify
  documentation examples, reducing boilerplate and aligning the visual style
  with the R ggsci package examples (#28).

### Maintenance

- Refactored the logo generation script to use ImageMagick, removing the
  previous R and hexSticker dependency (#20).

## py-ggsci 0.4.1

### Documentation

- Add an initial code block to the Get Started article showing the
  essential imports required for the example plots (#17).

## py-ggsci 0.4.0

### Testing

- Add a parametrized, introspection-driven test suite covering utilities,
  palettes, and scales. Code coverage reaches 100% (#14).

## py-ggsci 0.3.0

### Improvements

- Refine type annotations and docstrings to follow best practices (#9).

### Documentation

- Add a [Get Started article](https://nanx.me/py-ggsci/articles/get-started/)
  mirroring the original R package vignette (#11).

### CI/CD

- Add GitHub Actions workflow for mypy type checks (#10).

## py-ggsci 0.2.0

### New features

- Port all color scales from the R package ggsci (#5).

### Improvements

- Relax minimum dependency versions to broaden compatibility (#3).
- Rename palette functions from `*_pal()` to `pal_*()` for consistency
  with the R package ggsci (#4).

### Documentation

- Add an API reference page for each palette to the MkDocs site (#6).

### Infrastructure

- Add scripts to retrieve and update color palette data (#2).

## py-ggsci 0.1.0

### New features

- Port four experimental color scales for plotnine from the R package ggsci.
  - Add palette functions for direct color access.
  - Support alpha transparency for all scales.
  - Reverse parameter for continuous scales.
  - British spelling aliases.
