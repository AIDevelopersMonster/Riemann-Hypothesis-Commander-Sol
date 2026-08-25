# RH-SOL-02 · EXP-02 HEIGHT — post-confirmation exploratory height dependence

Status: exploratory, opened only after EXP-01 independent holdout completion.
Date opened: 2026-08-23.

## Question

How do the confirmed SHIFT observables evolve with zeta height over loops 1..20000?

The purpose is not to redefine or rescue EXP-01. EXP-01 is already frozen and independently confirmed. This experiment asks a new descriptive question about height dependence.

## Inputs

Two already-generated cubes are used without regenerating zeta loops:

- calibration: loops 1..10000;
- independent holdout: loops 10001..20000.

For comparability across the full range, the time proxy is the zero-pair midpoint

`(gamma_n + gamma_{n+1}) / 2`

for all blocks. The RH-SOL-01 legacy `t_near` table is not mixed into this height trend because it exists only for loops 1..10000.

## Blocking

Primary exploratory partition: 20 non-overlapping consecutive blocks of 1000 loops each.

This matches the frozen spectral block size used by EXP-01. No overlapping or adaptively chosen windows are used in the primary HEIGHT table.

## Primary geometry

Primary field remains the q=16 winding count cube for direct continuity with EXP-01.

For each block:

`C_n(delta) = Cbar_n + R_n(delta)`

where `Cbar_n` is the q=16 translation mean and `R_n(delta)` is the translation residual.

The continuous filled area `A_n` is also analyzed directly.

## Height coordinate

Each block records:

- loop start and stop;
- median zero-pair midpoint height `T_median`;
- mean zero-pair midpoint height `T_mean`;
- `log(T_median / (2*pi))`, for comparison with natural zeta asymptotic scales.

## Frozen-within-EXP-02 spectral settings

The spectral transformation is exactly the already-implemented EXP-01 pipeline:

- 1000-loop block;
- linear detrend;
- rFFT power;
- median normalization on loop frequency [0.01, 0.48];
- physical omega grid [0.40, 3.50], step 0.0005;
- targets `log(m)`, m=2..13;
- common-shift scan [-0.25, 0.25], 2001 points;
- independent target jitter +/-0.20;
- B=20000;
- seed base 20260822.

## Primary HEIGHT metrics

### 1. Robust normalized comb excess

For area and q=16 translation mean separately:

`E95 = (S_obs - median(S_null)) / (q95(S_null) - median(S_null))`.

Interpretation:

- `E95 = 1` means the observed score is one median-to-95%-null interval above the null median;
- this is a robust descriptive normalization, not a Gaussian z-score.

Also record raw score, null median/q95/q99 and empirical jitter p-value.

### 2. Frequency alignment

Record the best common target shift from the frozen scan.

Primary alignment magnitude:

`abs(best_common_shift)`.

A value near zero means the blockwise comb aligns closely with the predeclared `log(m)` targets.

### 3. Residual variance fraction

For q=16 winding:

`F_res = residual_mean_square / (zero_mode_variance + residual_mean_square)`.

Equivalently `F_res = 1 - F_zero` under this decomposition.

This measures how much of the scalar count-field variance is translation-dependent rather than carried by the translation zero mode.

### 4. Descriptive map summaries

For each block, compute without per-cell null testing:

- median q=16 count-map comb score;
- median q=16 residual-map comb score;
- q05/q95 residual-map comb score.

These summarize spatial translation heterogeneity without creating 20 x 256 new hypothesis tests.

## Trend summaries

Across the 20 blocks, report descriptive Pearson and Spearman associations with `log(T_median/(2*pi))` for:

- area E95;
- translation-mean E95;
- absolute area alignment shift;
- residual variance fraction;
- median residual-map comb score.

Also report ordinary least-squares slope versus `log(T_median/(2*pi))`.

These are exploratory trend summaries. Their nominal p-values, if reported by SciPy, are descriptive and are not promoted to confirmatory significance claims.

## Guardrails

1. Do not interpret the already-observed calibration-to-holdout raw score increase as evidence of height growth before the 20-block normalized analysis.
2. Do not change block boundaries after viewing the table.
3. Do not select a subset of blocks because it gives a cleaner trend.
4. Do not change jitter width, target set, omega grid or spectral normalization in the primary HEIGHT run.
5. Any alternative window size, overlapping windows, different normalization or regression model is a separately labeled sensitivity analysis.
6. EXP-02 cannot retroactively alter EXP-01 claims.
