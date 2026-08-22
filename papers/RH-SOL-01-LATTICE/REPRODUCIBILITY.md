# Reproducibility record

## Canonical publication

Zenodo DOI: https://doi.org/10.5281/zenodo.22060296

Published version: `v0.1.1`  
Publication date: `2026-08-22`

The Zenodo deposit is the canonical immutable release. GitHub mirrors the research context and selected human-readable/source materials.

## Dataset scope reported in the article

- 10,000 consecutive critical-line Argand loops.
- 115,642 total integer-point incidences.
- 6,248 loops with at least one interior lattice point.
- 3,752 loops with no interior lattice point.
- Cartesian grid support: `x = -5..16`, `y = -12..13`.
- 572 grid cells, of which 463 are occupied at least once.
- Binary tensor shape: `10000 x 26 x 22`.

Reference multiplicities used as integrity checks:

- `M(1,0) = 5848`
- `M(1,1) = 3781`
- `M(1,-1) = 3796`
- `M(2,0) = 3436`
- `M(2,1) = 2823`
- `M(2,-1) = 2854`
- `M(3,2) = 1469`

## Deposited analysis package

The v0.1.1 Zenodo package contains:

- `paper.pdf`
- `paper.tex`
- `references.bib`
- `demo.html`
- selected derived CSV/JSON tables
- `code/analyze_integer_lattice.py`
- `code/crossfit_mixing_dictionary.py`
- `code/nyquist_fold_test.py`
- `code/theory_warp_check.py`
- publication figures
- `REPORT_RU.md`
- `NYQUIST_RIEMANN_SIEGEL_NOTE_RU.md`
- `AI_ASSISTANCE.md`
- `MANIFEST.sha256`
- `full_analysis_archive.zip`

## Publication artifact checksums

SHA-256 values from the locally retained v0.1.1 publication package:

- `paper.pdf` — `a981d95e654347e4b1cf6a52f3201686fdf35b442fb5bf72db4621dab9d13deb`
- `demo.html` — `40769ac18e390769acfaa649b7abc3daa5d2ee449970ff23a967f8cb5f153c43`
- `paper.tex` — `ed4f90a19af5762286d0a588a8922068505e23c7157502c627e178cea78b43b2`
- `references.bib` — `a7d2723917b2a02cbd6aa6a7e53fdb0afe5158e236c553e457e52bc4dc90c5a3`

## Current reproducibility boundary

The archived scripts reproduce the reported downstream analyses from the deposited intermediate datasets. The published version does **not** yet package a complete single-command upstream pipeline from a public zero table through high-precision zeta evaluation, loop tracing, interior classification and generation of `I(n,a,b)`.

This limitation is preserved explicitly rather than hidden. RH-SOL-02/03/04 are designed to close it by formalizing the interior convention, testing actual-zero timing, adding shifted grids and introducing stronger null models.

## Reproducibility rule for later work

A later result must record at minimum: source zero list, precision, loop-sampling rule, interior/fill convention, boundary tolerance, lattice spacing and shift, software commit, random seeds where applicable, and checksums of derived data.
