# RH-SOL-05 · POISSON — preregistration

Status: preregistered before inspection of POISSON-mode results.
Branch: `agent/rh-sol-05-poisson`.

## Core question

For each zeta Argand filled loop-domain `D_n`, define the translated lattice count on the translation torus

`C_n(delta) = sum_{k in Z^2} 1_{D_n}(k + delta)`,  `delta in T^2`.

RH-SOL-02 SHIFT established that the translation mean is essentially the filled area and that translation-dependent residual variance is small. RH-SOL-04 FIREWALL later showed that the scalar area exact-`log(m)` score survives within a broad second-order equivalence class.

RH-SOL-05 asks:

> What spatial Fourier modes of `C_n(delta)` carry the nonzero translation structure, and do low nonzero spatial modes contain temporal arithmetic information beyond the area / zero mode?

## Exact torus decomposition

For a bounded measurable filled domain `D` with indicator `1_D`, define Fourier transform convention

`hat{1_D}(ell) = integral_D exp(-2 pi i ell dot x) dx`,  `ell in Z^2`.

Then, in the standard Poisson-periodization sense,

`C_D(delta) = sum_{ell in Z^2} hat{1_D}(ell) exp(2 pi i ell dot delta)`.

In particular,

`hat C_D(0) = area(D)`.

Parseval gives

`integral_{T^2} |C_D(delta)-area(D)|^2 d delta = sum_{ell != 0} |hat{1_D}(ell)|^2`.

Thus translation variance is exactly the total nonzero spatial-mode energy for the continuous translation observable.

The discrete q x q midpoint translation grid measures aliased Fourier coefficients. Therefore q-stability is mandatory before interpreting any nonzero discrete mode as a resolved spatial mode.

## Data

Use the existing RH-SOL-02 EXP-01 winding-fill translation tensors if present locally:

- loops `1..10000`: `data/derived/rh-sol-02-exp01/calibration_1_10000.npz`;
- loops `10001..20000`: `data/derived/rh-sol-02-exp01-holdout/holdout_10001_20000.npz`.

Required arrays:

- `counts_winding_q8`;
- `counts_winding_q16`;
- `counts_winding_q32`;
- `area_winding`;
- `gamma0`, `gamma1`, `loops`.

If q8/q32 tensors are unavailable in a merged file, the experiment must stop rather than silently substitute another design.

## Spatial DFT convention

For each q x q midpoint-grid count map `C[j,i]`, compute

`F_q = fft2(C) / q^2`.

Because the grid uses midpoint shifts `((i+1/2)/q, (j+1/2)/q)`, DFT coefficients carry a deterministic midpoint phase factor. Magnitudes are unaffected. Primary mode-energy analyses use `|F_q|^2`, so no phase correction is needed there.

The DFT zero mode is the translation mean.

## Resolved mode set

Primary resolved modes are integer vectors

`ell=(a,b)` with `max(|a|,|b|) <= 3`, excluding `(0,0)`.

For q=8,16,32 these indices are representable without index collision, but q=8 may still contain unresolved alias contributions from higher true modes. Cross-q stability is therefore diagnostic rather than assumed.

## Cross-q aliasing diagnostic

For each resolved mode and each loop compare magnitude-squared coefficients across q:

- q8 vs q16;
- q16 vs q32.

Aggregate relative discrepancy using

`R_q1_q2(ell) = median_n |P_q1(n,ell)-P_q2(n,ell)| / (P_q2(n,ell)+eps)`

with `eps=1e-15`.

A mode is declared **q-stable** for primary low-mode interpretation if

`R_16_32 <= 0.10`.

q8 is secondary only.

No mode may be promoted or removed after temporal target-score inspection. Stability selection depends only on q16/q32 spatial agreement.

## Spatial shells

Using q32 coefficients, define per-loop energies:

- `E0 = |F(0,0)|^2`;
- `E1 = sum_{a^2+b^2=1} |F(a,b)|^2`;
- `E2 = sum_{a^2+b^2=2} |F(a,b)|^2`;
- `E4 = sum_{a^2+b^2=4} |F(a,b)|^2`;
- `Elow = sum_{0 < a^2+b^2 <= 4} |F(a,b)|^2`;
- `Enonzero_total = sum_{all DFT indices except zero} |F|^2`;
- `Ehigh = Enonzero_total - Elow`.

Because a discrete q-grid contains aliasing, `Enonzero_total` is a discrete-grid quantity. The low shells require q-stability checks before continuous-mode interpretation.

## Parseval / SHIFT consistency checks

For every loop and q verify numerically:

1. `F_q(0,0) == mean(C_q)` within floating precision;
2. `sum_{ell != 0} |F_q(ell)|^2 == variance(C_q)` within tolerance `1e-12` absolute plus `1e-10` relative;
3. q32 zero mode tracks `area_winding` with the already observed SHIFT-level small error.

Failure of (1) or (2) is an implementation error and stops the experiment.

## Temporal scoring

Use actual zero-pair midpoint time

`t_n = (gamma_n + gamma_{n+1})/2`.

For each scalar per-loop observable below, use exactly the FIREWALL target-only block statistic:

- blocks of 1000 loops;
- linear detrend observable vs actual `t` within block;
- exact targets `omega=log(m)`;
- OLS cosine/sine response;
- transform `R2 -> -log(1-R2+1e-15)`;
- average over targets and blocks.

Primary dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

Temporal observables:

1. `A = area_winding`;
2. `Z = Re F_q32(0,0)` translation mean;
3. `E1`;
4. `E1+E2`;
5. `Elow`;
6. `Ehigh`;
7. `Enonzero_total`;
8. `V = variance(C_q32)` as a direct SHIFT consistency observable.

These are declared before results.

## Incremental-information diagnostics

The primary scientific question is not whether low-mode energy alone has a comb, but whether it contributes temporal structure beyond area.

For each nonzero-mode scalar `X` in `{E1, E1+E2, Elow, Ehigh, Enonzero_total}` construct an area-residualized observable blockwise:

`X_perp = X - alpha - beta A`,

where `alpha,beta` are OLS fit inside each 1000-loop block using only that block.

Then score `X_perp` with the same exact-target statistic.

This is descriptive incremental-information analysis, not a causal decomposition.

## Frozen ranges

Calibration:

- loops `1..10000`.

Independent holdout:

- loops `10001..20000`.

No temporal threshold or mode set is tuned on calibration and changed for holdout.

## Primary success pattern

POISSON-01 supports a genuine nonzero-spatial arithmetic layer if all of the following occur:

1. at least one declared low shell is q-stable by the frozen q16/q32 rule;
2. its temporal target score is non-negligible on calibration and reproduces qualitatively on holdout;
3. its area-residualized score remains materially above zero on both ranges;
4. the result is not explainable solely by `Enonzero_total = variance(C)` identity without shell localization.

No hard p-value threshold is preregistered for this first decomposition stage; the main purpose is structural localization and cross-resolution validation.

## Negative / zero-mode outcome

If nonzero shell scores collapse after residualizing against area, then RH-SOL-05 should conclude that the tested low spatial modes add little temporal exact-target information beyond the scalar area layer, despite being real geometric degrees of freedom.

That is a scientifically valid stopping outcome.

## Guardrails

1. Continuous Poisson coefficients and discrete q-grid DFT coefficients are not identical without accounting for aliasing.
2. q-stability is required before interpreting a discrete coefficient as a resolved low spatial mode.
3. Shell energies lose Fourier phase information; phase-sensitive observables may be tested only in a later preregistered stage.
4. No Riemann-Hypothesis claim follows from any POISSON outcome.
