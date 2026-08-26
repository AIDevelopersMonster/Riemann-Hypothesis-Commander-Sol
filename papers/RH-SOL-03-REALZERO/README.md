# RH SOL 03-REALZERO · REALZERO

## Dirichlet Frequencies without Smooth Time: Spectral Tests on the Actual Riemann Zeros

**Status:** Active research branch  
**Branch:** `agent/rh-sol-03-realzero`

## Core question

Does the Dirichlet `log m` comb survive when the temporal coordinate is taken directly from the actual Riemann-zero ordinates, rather than recovered through a smooth local conversion from loop index to physical height?

Primary loop time:

`t_n = (gamma_n + gamma_{n+1}) / 2`.

Primary observable:

continuous winding-filled Argand-loop area.

Primary spectrum:

direct irregular-time Lomb-Scargle / least-squares sinusoidal projection at physical angular frequencies, with no `dt/dn` warp.

## Design

- calibration: loops 1..20000;
- frozen holdout: loops 20001..40000;
- primary targets: `omega = log(m)`, `m=2..13`;
- predeclared Nyquist sensitivity: `m=2..11`;
- 1000-loop blocks;
- independent target-jitter diagnostic null, B=20000.

The holdout runner refuses to execute until `CALIBRATION_FREEZE.md` exists.

## Files

- `PREREGISTRATION.md` — frozen hypotheses, estimator and scoring rules
- `analysis/` — machine-readable output and spectra
- `figures/` — publication figures
- `manuscript/` — article sources
- `release/` — release notes and Zenodo metadata

Reusable analysis code:

- `../../scripts/realzero_irregular_spectrum.py`
- `../../scripts/run_rh_sol_03_realzero.ps1`
