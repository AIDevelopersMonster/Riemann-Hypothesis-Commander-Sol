# RH-SOL-04 · FIREWALL-04 — IAAFT preregistration

Status: preregistered before IAAFT surrogate inspection.
Branch: `agent/rh-sol-04-firewall`.

## Core question

FIREWALL-03 showed that exact preservation of the blockwise loop-index Fourier magnitudes is insufficient once the original phase organization is destroyed.

FIREWALL-04 asks a stronger question:

> Is the exact `log(m)` alignment reproducible when each surrogate preserves the exact empirical distribution of area values within every 1000-loop block and simultaneously matches the original blockwise loop-index Fourier magnitude spectrum as closely as a frozen IAAFT iteration scheme permits?

This tests whether the combination of marginal distribution plus second-order spectral structure is sufficient without the original higher-order/phase organization.

## Observed statistic

Use exactly the frozen FIREWALL target-only score:

- detrend area linearly against actual zero-pair midpoint time inside each 1000-loop block;
- at each exact target `omega=log(m)`, fit cosine/sine by least squares;
- convert explained fraction `R2` to `-log(1-R2+1e-15)`;
- average over targets and blocks.

Primary dictionary: `m=2..13`.
Predeclared sensitivity: `m=2..11`.

No frequency search or common-shift optimization enters the primary test.

## IAAFT surrogate construction

For each 1000-loop area block independently:

1. save the exact sorted original area values;
2. save the original rFFT magnitudes of the mean-centered area sequence;
3. initialize from a random permutation of the original area values;
4. iterate the following two projections exactly `200` times:
   - spectral projection: replace current rFFT magnitudes by the original magnitudes while retaining current phases, then inverse transform;
   - amplitude projection: replace the resulting values by the exact original sorted area values according to rank order;
5. return the final rank-projected sequence.

Thus every final surrogate preserves the exact multiset of original area values in each block.

The Fourier magnitude spectrum is matched iteratively but need not be mathematically exact after the final amplitude projection. Therefore each generated surrogate must report its relative spectral-magnitude mismatch.

## Frozen convergence diagnostic

For each block surrogate define

`E_spec = || |FFT(y_surr-mean)| - |FFT(y_orig-mean)| ||_2 / || |FFT(y_orig-mean)| ||_2`.

For every realization aggregate across the 20 blocks by mean and maximum `E_spec`.

Report over all generated surrogates:

- median mean spectral mismatch;
- q95 mean mismatch;
- maximum mean mismatch;
- median maximum-block mismatch;
- maximum maximum-block mismatch.

No surrogate is deleted based on mismatch after viewing results. The frozen iteration count is `200` for all blocks and all ranges.

## Surrogate count and seeds

- `B=2000` per range;
- calibration-range seed: `20260829`;
- holdout-range seed: `20260830`.

The lower B relative to earlier firewall stages is chosen because IAAFT is substantially more expensive. The finite-surrogate p-value floor is therefore `1/(2000+1)`.

## Ranges

Run independently on:

1. loops `1..20000`;
2. loops `20001..40000`.

No tuning on the first range may alter the second-range construction.

## Primary success criterion

For each range and each target dictionary, FIREWALL-04 passes if:

- observed score exceeds surrogate q99; and
- empirical upper-tail `p <= 0.01`.

Also report surrogate maximum.

## Interpretation

If FIREWALL-04 passes on both ranges, then neither of the following, separately or jointly, is sufficient under the tested blockwise construction:

- the exact empirical distribution of area values;
- the blockwise loop-index second-order spectrum.

The surviving information must then reside in higher-order temporal organization, exact phase relations, nonlinear dependence on actual zero times, or structure not captured by these blockwise invariants.

If FIREWALL-04 fails, then the combination of distribution plus second-order spectrum is sufficient to reproduce the present target statistic, materially narrowing the claim.

## Guardrails

1. IAAFT surrogates preserve the exact amplitude distribution but only approximately preserve Fourier magnitudes after the final rank projection.
2. The mismatch is measured and reported rather than silently ignored.
3. Passing IAAFT does not prove arithmetic causation.
4. These are still scalar-area controls, not full polygon-level geometry controls.
5. Pure polygon transformations that preserve area cannot change the current primary scalar observable and therefore are not informative for this stage.
6. No Riemann-Hypothesis claim follows from any outcome.
