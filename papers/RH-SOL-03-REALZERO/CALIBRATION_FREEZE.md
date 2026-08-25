# RH-SOL-03 · REALZERO — calibration freeze

Status: calibration inspected and estimator frozen before REALZERO holdout inspection.
Freeze date: 2026-08-25.
Branch: `agent/rh-sol-03-realzero`.

## Scope

Calibration range only:

- loops `1..20000`;
- 20 consecutive blocks of 1000 loops;
- observable: winding filled area `A_n = Area(D_n)`;
- physical time coordinate: actual zero-pair midpoint
  `t_n = (gamma_n + gamma_{n+1}) / 2`;
- direct irregular-time Lomb-Scargle / least-squares spectrum;
- omega grid: `0.40..3.50`, step `0.0005`;
- no `dt/dn` conversion;
- no Riemann-von Mangoldt inversion;
- no polynomial, spline, phase, or frequency warp;
- primary target dictionary: `log(m)`, `m=2..13`;
- predeclared conservative sensitivity: `m=2..11`;
- target-jitter null: independent uniform `+/-0.20`, `B=20000`;
- primary seed: `20260825`;
- common-shift diagnostic: `[-0.25,+0.25]`, 2001 points.

No scoring, null, block, target, or alignment parameter is changed after calibration inspection.

## Calibration result — primary m=2..13

Observed exact-target comb score:

`3.897458739496102`

Jitter null:

- median: `0.8489534914335335`;
- q95: `1.2628204059388057`;
- q99: `1.4598759255330063`;
- empirical upper-tail p-value: `4.999750012499375e-05`.

Common-shift diagnostic:

- best shift: `0.0`;
- best shifted score: `3.897458739496102`.

Thus the exact predeclared target locations themselves maximize the common-shift scan on the calibration range.

## Calibration result — Nyquist-safe sensitivity m=2..11

Observed exact-target comb score:

`4.041270022452432`

Jitter null:

- median: `0.8272575150665223`;
- q95: `1.29034818195257`;
- q99: `1.5220835678441076`;
- empirical upper-tail p-value: `4.999750012499375e-05`.

Common-shift diagnostic:

- best shift: `0.0`;
- best shifted score: `4.041270022452432`.

The conservative dictionary therefore gives the same qualitative result.

## Calibration verdict

Calibration passes the preregistered within-range REALZERO criteria:

1. exact-target comb score exceeds jitter-null q99;
2. empirical `p <= 0.01`;
3. best common shift has zero magnitude on the declared scan;
4. the result survives restriction from `m=2..13` to `m=2..11`.

The decisive criterion remains reproduction on the frozen holdout loops `20001..40000`.

## Implementation audit before holdout

The frozen implementation in `scripts/realzero_irregular_spectrum.py` was re-read after calibration and before holdout inspection.

The implementation:

- detrends area against actual time inside each 1000-loop block;
- subtracts only a block time origin before trigonometric evaluation, which changes phase origin but not physical frequencies;
- passes the declared angular-frequency grid directly to `scipy.signal.lombscargle`;
- uses no loop-index FFT and no local slope `dt/dn`;
- median-normalizes periodogram power over the fixed omega grid and then applies `log1p`;
- averages block scores at fixed physical omega.

No implementation defect requiring a calibration-stage change was identified. Therefore the estimator is frozen unchanged for holdout.

## Frozen interpretation before holdout

The calibration result supports the statement:

> The `log(m)` comb is visible in the continuous filled-area observable when the spectrum is evaluated directly on the actual zero-pair midpoint times, without a smooth time warp; on loops 1..20000 the best common frequency shift is exactly zero for both the full and conservative target dictionaries.

This statement is calibration-only. It is not yet the confirmatory REALZERO conclusion.

## Holdout rule

The next and only confirmatory step is to apply exactly the frozen estimator to loops `20001..40000` with no tuning or refitting.

The holdout result must be reported regardless of outcome.

No post-holdout modification may be reclassified as confirmatory.

## Guardrails

- Calibration and holdout share the same mathematical observable and scoring rule but disjoint loop ranges.
- The holdout geometry was generated earlier for RATE-OOS, but the direct REALZERO irregular-time spectrum was not inspected before this freeze.
- The jitter null measures target-frequency alignment only and is not a full geometry-preserving null.
- The required matched comparison with the earlier smooth-warp spectrum remains a secondary/comparative analysis and cannot modify the primary REALZERO result.
- No Riemann-Hypothesis claim follows from the calibration or holdout result.
