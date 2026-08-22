# RH-SOL-02 · SHIFT

## Shifted-Lattice Spectroscopy of Riemann-Zeta Argand Loops

**Status:** Active research branch  
**Branch:** `agent/rh-sol-02-shift`  
**Parent publication:** RH-SOL-01 · LATTICE — DOI `10.5281/zenodo.22060296`

## Core question

Does the Dirichlet-frequency structure reported in RH-SOL-01 survive arbitrary translations of the sampling lattice, or is it tied to the special placement of the integer grid?

For the loop domain `D_n` and translation `delta = (dx,dy) in [0,1)^2`, define

`C_n(delta) = sum_{k in Z^2} 1_{D_n}(k + delta)`.

A tensor-valued version is

`I_delta(n,a,b) = 1_{D_n}((a,b) + delta)`.

## Interior convention

The primary convention for this branch is **non-zero winding number**, with boundary points excluded using an explicit numerical tolerance. Because self-intersecting Argand loops are possible, an **even-odd fill rule** is retained as a sensitivity control rather than silently identifying the two notions of interior.

## Exact translation identity

For any bounded measurable domain `D`,

`integral_[0,1)^2 C_D(delta) d delta = Area(D)`.

Thus translation-averaged lattice count has a theorem-level geometric baseline before any zeta-specific spectral claim is tested. See `THEORY.md`.

## Confirmatory design

- Stage A: calibration/reproduction on loops 1–10000. This is **not** an independent holdout because RH-SOL-01 used the same height range.
- Stage B: after freezing code and scoring rules, test the same hypotheses on a new height range, provisionally loops 10001–20000.

## Files

- `PREREGISTRATION.md` — hypotheses, fixed choices, success/failure criteria
- `THEORY.md` — translation averaging and Poisson/Parseval structure
- `RESULTS.md` — append-only record of positive and negative findings
- `analysis/` — article-specific analysis
- `figures/` — publication figures
- `manuscript/` — article sources
- `release/` — Zenodo/release metadata

Reusable code lives in `../../src/shifted_lattice.py`; the first CLI runner is `../../scripts/run_shift_scan.py`.
