# RH-SOL-03 · REALZERO — matched direct-vs-smooth comparison

Status: descriptive comparison completed after the frozen REALZERO holdout verdict.

This comparison cannot alter the already-recorded confirmatory result in `HOLDOUT_RESULTS.md`.

## Purpose

Compare, on the same winding-area series and the same 1000-loop blocks:

1. direct irregular-time Lomb-Scargle evaluation at actual zero-pair midpoint times;
2. the earlier smooth blockwise loop-index-to-physical-frequency conversion.

The target dictionary and block structure are matched.

## Calibration range: loops 1..20000

### m=2..13

- direct score: `3.897458739496102`;
- direct best shift: `0.0`;
- smooth score: `2.6204433563730083`;
- smooth best shift: `0.000250000000000028`.

The direct score is `1.48733` times the smooth score, about `48.73%` larger.

### m=2..11

- direct score: `4.041270022452432`;
- direct best shift: `0.0`;
- smooth score: `2.7432552434667516`;
- smooth best shift: `0.000250000000000028`.

The direct score is `1.47317` times the smooth score, about `47.32%` larger.

## Frozen holdout range: loops 20001..40000

### m=2..13

- direct score: `3.4659735801364495`;
- direct best shift: `0.0`;
- smooth score: `3.1991792178957454`;
- smooth best shift: `0.0`.

The direct score is `1.08339` times the smooth score, about `8.34%` larger.

### m=2..11

- direct score: `3.6056592132518253`;
- direct best shift: `0.0`;
- smooth score: `3.3172901581153993`;
- smooth best shift: `0.0`.

The direct score is `1.08693` times the smooth score, about `8.69%` larger.

## Interpretation

The matched comparison gives no evidence that the earlier smooth time conversion is required to create or sharpen the `log(m)` alignment.

On both disjoint ranges the direct actual-time estimator gives the larger exact-target score. On the frozen holdout both estimators place the common-shift optimum exactly at zero; on calibration the smooth method has only a single grid-step offset of `+0.00025`, while direct actual-time remains exactly zero.

The size of the direct-over-smooth score advantage is not stable with height: it is about 47–49% on loops 1..20000 and about 8–9% on loops 20001..40000. This descriptive change should not be promoted to a new rate law without a separate preregistered study.

## Strongest defensible conclusion

> Direct use of the actual zero ordinates is at least as effective as the earlier smooth blockwise time conversion for locating the declared `log(m)` comb over the tested first 40,000 loops, and is stronger by the present normalized score on both tested ranges.

Therefore smooth time warping is best viewed as an approximation/convenience in the earlier pipeline rather than a necessary source of the observed frequency alignment.

## Guardrails

- Scores from the two estimators are normalized within their own spectral constructions; the ratio is descriptive, not a universal effect-size scale.
- The comparison does not establish why the comb exists.
- It does not test geometry-preserving surrogates or phase-randomized controls.
- Those causal/falsification questions are handed to RH-SOL-04 FIREWALL.
