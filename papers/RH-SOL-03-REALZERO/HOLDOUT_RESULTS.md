# RH-SOL-03 · REALZERO — frozen holdout results

Status: primary confirmatory test passed.
Holdout range: loops `20001..40000`.
Estimator and scoring were frozen in `CALIBRATION_FREEZE.md` before holdout inspection.

## Primary result: m=2..13

Direct irregular-time Lomb-Scargle spectrum on actual zero-pair midpoint times:

- observed exact-target comb score: `3.4659735801364495`;
- jitter-null median: `0.8207368636200278`;
- jitter-null q95: `1.1909605694450016`;
- jitter-null q99: `1.367251639628815`;
- empirical upper-tail p-value: `4.999750012499375e-05`;
- best common shift: `0.0`;
- best shifted score: `3.4659735801364495`.

The observed score is approximately `2.535` times the null q99.

## Predeclared conservative sensitivity: m=2..11

- observed exact-target comb score: `3.6056592132518253`;
- jitter-null median: `0.8029112191940885`;
- jitter-null q95: `1.219568681554937`;
- jitter-null q99: `1.4396563906942155`;
- empirical upper-tail p-value: `4.999750012499375e-05`;
- best common shift: `0.0`;
- best shifted score: `3.6056592132518253`.

The observed score is approximately `2.505` times the null q99.

## Calibration-to-holdout comparison

Calibration on loops `1..20000` gave:

- primary score `3.897458739496102`;
- primary best common shift `0.0`;
- m=2..11 score `4.041270022452432`;
- m=2..11 best common shift `0.0`.

The holdout exact-target score is about `11.1%` lower than calibration for m=2..13 and about `10.8%` lower for m=2..11, but remains far above the corresponding jitter-null q99 thresholds.

Crucially, the common-shift optimum remains exactly zero on both disjoint ranges and on both target dictionaries.

## Confirmatory verdict

All preregistered REALZERO success criteria are satisfied on the frozen holdout:

1. exact-target score exceeds null q99;
2. empirical `p <= 0.01`;
3. best common shift is zero on the declared scan;
4. the qualitative target pattern reproduces on the independent holdout;
5. the same conclusion holds under the predeclared m=2..11 sensitivity.

Therefore the primary REALZERO conclusion is supported:

> The Dirichlet `log(m)` comb in the continuous filled-area observable survives direct use of the actual Riemann-zero ordinates. The previously used smooth local time conversion is not required to place the dominant spectral structure at the declared `log(m)` frequencies over the tested first 40,000 loops.

## What this removes

RH-SOL-01/02 used a smooth blockwise conversion from loop-index frequency to physical frequency. REALZERO replaces that step with direct irregular-time sinusoidal projection on

`t_n = (gamma_n + gamma_{n+1}) / 2`.

The independent holdout therefore rules out the hypothesis that the observed frequency alignment is merely an artifact of that smooth `dt/dn` conversion.

## What this does not establish

- It does not prove the Riemann Hypothesis.
- It does not prove that the comb is uniquely caused by primes.
- It does not establish an asymptotic law.
- It does not replace geometry-preserving and phase-randomized nulls; those belong to RH-SOL-04 FIREWALL.
- The target-jitter null tests alignment with the declared frequency dictionary, not the full causal origin of the signal.

## Remaining required comparison

Before closing REALZERO, perform the preregistered matched comparison between:

1. direct actual-time irregular spectrum;
2. the earlier smooth blockwise time-warp spectrum;

on the same area series and the same blocks, reporting exact-target scores, best common shifts, and target-local peak locations.

This comparison is descriptive and cannot alter the already-recorded primary confirmatory result.
