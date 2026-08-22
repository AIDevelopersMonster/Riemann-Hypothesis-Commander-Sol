# Analysis inventory

The canonical v0.1.1 Zenodo package contains the downstream analysis code and selected derived tables used in RH-SOL-01.

## Core scripts

- `analyze_integer_lattice.py` — static lattice statistics, residual geometry controls and primary spectral analysis.
- `crossfit_mixing_dictionary.py` — even/odd cross-fit removal of the predeclared log-integer plus small-ratio frequency dictionary.
- `nyquist_fold_test.py` — local Nyquist/folding diagnostics.
- `theory_warp_check.py` — theory-only smooth Riemann-von Mangoldt warp checks.

## Selected derived tables

- `zeta_integer_analysis_summary.json`
- `zeta_integer_modq_static_tests_corrected.csv`
- `zeta_integer_vonmangoldt_robustness.csv`
- `zeta_integer_theory_log_comb.csv`
- `zeta_integer_crossfit_dictionary_reduction.csv`
- `zeta_integer_crossfit_residual_peaks.csv`
- `zeta_integer_nyquist_fold_summary.csv`
- `zeta_integer_nyquist_cusp_table.csv`

## Integrity / scope

The larger `full_analysis_archive.zip` is intentionally kept on Zenodo rather than copied into Git history. See `../REPRODUCIBILITY.md` for dataset counts, reference multiplicities and publication checksums.

The published analysis is downstream-reproducible from the archived intermediate data. A complete upstream generator from zero ordinates to loop boundaries and interior incidence tensors is a declared open reproducibility task for subsequent RH-SOL work.
