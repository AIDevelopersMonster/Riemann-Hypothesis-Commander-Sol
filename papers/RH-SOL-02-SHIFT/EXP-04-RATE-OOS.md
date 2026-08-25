# RH-SOL-02 · EXP-04 RATE-OOS — frozen out-of-sample prediction test

Status: preregistered out-of-sample validation.
Freeze date: 2026-08-24.
Training range already viewed: loops 1..20000.
New prediction range: loops 20001..40000.

## Purpose

EXP-03 RATE found that the relative translation-dependent variance

`F_res = residual_mean_square / (zero_mode_variance + residual_mean_square)`

is described substantially better over loops 1..20000 by an inverse power of `log(T/(2*pi))` than by the simpler fixed inverse-log laws, with a power law in T as the strongest competing two-parameter model.

EXP-04 is a clean out-of-sample test between the two strongest already-fitted models. No primary parameter is refit on loops 20001..40000.

## Frozen geometry and blocking

- loops: 20001..40000;
- 20 non-overlapping consecutive blocks of 1000 loops;
- zero source: LMFDB ordinates 20001..40001 inclusive;
- Argand sampling: 30 decimal digits, 60 uniform segments, non-adaptive;
- fill rule: winding;
- translation grid: q=16 midpoint grid;
- boundary tolerance: 1e-10;
- block height: median zero-pair midpoint `T = median((gamma_n+gamma_{n+1})/2)`;
- `x = log(T/(2*pi))`.

Only q=16 winding is generated because the RATE target is the already-frozen q=16 winding variance decomposition. No q or fill-rule selection occurs in EXP-04.

## Frozen competing models

### M1 — inverse log-power

Fit on loops 1..20000 in EXP-03:

`F1(T) = 0.21368139779723283 / [log(T/(2*pi))]^3.137757448939574`

Frozen parameters:

- A1 = 0.21368139779723283
- p = 3.137757448939574

### M2 — power in T/(2*pi)

Fit on loops 1..20000 in EXP-03:

`F2(T) = 0.014291857670165177 * (T/(2*pi))^(-0.48215823718583606)`

Frozen parameters:

- A2 = 0.014291857670165177
- alpha = 0.48215823718583606

## Primary scoring rule

For each of the 20 new blocks compute observed `F_res`, then both frozen predictions.

Primary error is log prediction error:

`e_j = log(F_pred_j) - log(F_obs)`.

Primary model score:

`RMSE_log = sqrt(mean(e_j^2))`.

The primary winner is the model with smaller `RMSE_log` over all 20 OOS blocks.

No fitting, intercept correction, scale correction, exponent correction, model averaging, or block deletion is permitted before the primary winner is recorded.

## Secondary descriptive scores

Report for both models:

- mean signed log error;
- MAE in log space;
- relative RMSE `sqrt(mean(((pred-obs)/obs)^2))`;
- median absolute relative error;
- number of blocks with smaller absolute log error than the competitor;
- cumulative log-SSE.

Also report the ratio

`RMSE_log(M2) / RMSE_log(M1)`.

Values above 1 favor M1.

## Prediction-shape diagnostics

Without refitting, report:

- observed first and last OOS `F_res`;
- predicted first and last values under both models;
- Pearson/Spearman trend of observed `F_res` versus `x` as descriptive continuity checks;
- residual mean square and zero-mode variance for each block.

## Post-primary exploratory analyses

Only after the frozen OOS score has been written may one perform any refit on loops 20001..40000 or loops 1..40000. Such fits must be labeled post-OOS exploratory and may not replace the frozen prediction score.

## Interpretation guardrails

1. EXP-04 tests finite-range predictive transfer, not an asymptotic theorem.
2. A win for M1 supports the empirical inverse-log-power description over the extended observed range; it does not prove that this is the true asymptotic law.
3. A win for M2 weakens the specific inverse-log-power interpretation but does not affect the independently confirmed EXP-01 zero-mode result.
4. A near-tie is a valid result and must be reported as such.
5. No Riemann-Hypothesis claim follows from either outcome.
