# Changelog

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
