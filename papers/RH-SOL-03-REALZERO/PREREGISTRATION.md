# RH-SOL-03 · REALZERO — preregistration

Status: preregistered before direct irregular-time spectral inspection.
Branch: `agent/rh-sol-03-realzero`.

## Core question

Does the Dirichlet `log m` comb survive when the temporal coordinate is taken directly from the actual Riemann-zero ordinates rather than inferred through a smooth local `dt/dn` conversion?

The target frequencies remain

`omega_m = log(m)` for integers `m >= 2`.

The point of REALZERO is to remove one potential source of structure: smooth time warping from loop index to physical height.

## Primary observable

Use the continuous filled area of each zeta Argand loop under the winding convention.

For loop `n` between consecutive zeros `gamma_n < gamma_{n+1}` define

`A_n = Area(D_n)`.

This choice is fixed because RH-SOL-02 SHIFT independently showed that the dominant scalar spectral signal is carried by the translation zero mode, numerically equivalent to continuous filled area at the tested q resolutions.

No lattice translation parameter enters the primary REALZERO test.

## Primary time coordinate

For each loop use the actual zero-pair midpoint

`t_n = (gamma_n + gamma_{n+1}) / 2`.

No Riemann-von Mangoldt inversion, local linear `dt/dn` mapping, polynomial time warp, spline, or fitted phase correction is allowed in the primary analysis.

## Primary spectral estimator

REALZERO uses direct irregular-time sinusoidal projection on the actual `t_n`.

Within each 1000-loop block:

1. fit and remove a linear trend in `A_n` as a function of the actual time coordinate `t_n`;
2. subtract the block time origin before trigonometric evaluation for numerical stability;
3. evaluate an irregular-time Lomb-Scargle / least-squares periodogram directly at angular frequencies on the fixed grid

   `omega = 0.40 .. 3.50` with step `0.0005`;

4. median-normalize the periodogram over the fixed omega grid;
5. transform normalized power by `log1p`;
6. average the resulting score across blocks at each omega.

This is a direct physical-frequency estimator: no conversion from loop-index frequency is used.

## Primary comb score

Use the pre-existing target dictionary

`m = 2..13`,

with target frequencies `log(m)`.

The primary comb score is the mean spectrum score at those 12 frequencies.

No target may be removed after inspection.

## Primary calibration / holdout split

- calibration: loops `1..20000`;
- frozen holdout: loops `20001..40000`.

The geometric data for the holdout already exist because they were generated for RH-SOL-02 RATE-OOS. However, the direct irregular-time REALZERO spectrum on these blocks has not been inspected at the time of this preregistration.

Calibration may be inspected first only to validate the implementation and verify that the estimator is numerically well behaved. Before holdout inspection, all scoring and null choices below are frozen.

## Null and alignment diagnostics

Primary target-alignment null:

- independent per-target uniform jitter;
- half-width: `0.20` rad/time-unit in omega;
- `B = 20000`;
- seed `20260825`.

Report:

- observed comb score;
- null median;
- null q95;
- null q99;
- empirical upper-tail p-value.

Also perform the same common-shift diagnostic used previously:

- shift range `[-0.25, +0.25]`;
- `2001` equally spaced shifts.

This common-shift scan is diagnostic, not a tuned replacement for the exact-target primary score.

## Primary success criterion

REALZERO is supported on a range if:

1. the exact-target comb score exceeds the jitter-null q99;
2. empirical `p <= 0.01`;
3. the best common shift has small absolute magnitude, reported without retargeting;
4. the qualitative target pattern is reproduced on the frozen holdout.

The holdout result is the decisive confirmation.

## Required comparison against smooth-warp spectrum

For the same area series and same blocks, compute the already-existing RH-SOL-02 smooth-warp spectrum only as a matched comparator.

Report:

- exact-target score under direct actual-time analysis;
- exact-target score under smooth warp;
- target-by-target peak locations or local maxima;
- best common shift under both methods.

The smooth-warp analysis is not permitted to alter the primary actual-time estimator.

## Nyquist / identifiability sensitivity

Because actual zero spacing changes with height, report the common conservative dictionary `m=2..11` as a predeclared sensitivity in addition to the primary `m=2..13` dictionary.

The primary result remains `m=2..13` for continuity with RH-SOL-01/02.

## Secondary observables

After the primary area result is frozen, the following may be examined as secondary checks:

- finite-q translation mean from q=16 winding;
- scalar count at selected translations if desired;
- translation residual summaries.

These cannot replace the primary area result.

## Interpretation guardrails

1. A positive REALZERO result means the comb survives removal of the smooth time warp; it does not prove that the comb is caused by individual primes or that the geometry is uniquely arithmetic.
2. A negative result would identify smooth time warping as an essential component of the earlier spectral recovery and would materially weaken the interpretation of RH-SOL-01/02.
3. The jitter null tests target-frequency alignment only; geometry-preserving and phase-randomized nulls belong to RH-SOL-04 FIREWALL.
4. No Riemann-Hypothesis claim follows from either outcome.
5. No post-holdout parameter tuning may be reclassified as confirmatory.
