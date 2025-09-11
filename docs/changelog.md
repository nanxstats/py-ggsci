# Changelog

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
