# RH-SOL-04 · FIREWALL-05 — permutation-rigidity map preregistration

Status: preregistered before inspection.
Branch: `agent/rh-sol-04-firewall`.

## Motivation

FIREWALL-04 and FIREWALL-04B preserved the exact blockwise area-value multiset but failed to achieve the preregistered high-fidelity Fourier-magnitude regime. Increasing IAAFT effort from one 200-iteration start to four 2000-iteration starts improved mismatch only moderately, while the statistical firewall remained strongly passed.

This raises a different structural question:

> How rapidly does the original blockwise Fourier magnitude spectrum deteriorate as the exact area multiset is moved away from its original order, and how does the exact-`log(m)` target score behave along that tradeoff?

The goal is not another significance test against a single null family. The goal is to map the geometry of the exact-multiset permutation space.

## Observable and blocks

Use exactly the same winding filled-area sequence and actual zero-pair midpoint times as FIREWALL-01..04B.

Analyze independently:

1. loops `1..20000`;
2. loops `20001..40000`.

Block size remains `1000` loops.

## Controlled partial-permutation family

For each 1000-loop block and each shuffle fraction

`f in {0.01, 0.02, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80, 1.00}`,

construct a random exact-multiset surrogate as follows:

1. choose exactly `k = round(f * 1000)` positions without replacement, with minimum `k=2`;
2. randomly permute the selected original indices among those positions;
3. reject and redraw only if the selected permutation is the identity;
4. leave all unselected positions fixed.

This preserves the exact blockwise multiset for every surrogate and gives direct control over how much of the ordering is allowed to move.

No optimization toward the Fourier spectrum or the `log(m)` score is performed.

## Replicates and seeds

For each range and each shuffle fraction:

- `B = 300` independent realizations;
- calibration seed base: `20260902`;
- holdout seed base: `20260903`.

A deterministic offset derived from the fraction index may be added to the base seed.

## Distance metrics

The permutation itself, not equality of floating-point area values, defines ordering distance.

For each block record:

1. **moved fraction**: fraction of indices `i` with `perm(i) != i`;
2. **normalized mean absolute displacement**:

`D_abs = mean_i |perm(i)-i| / (block_size-1)`;

3. **normalized RMS displacement**:

`D_rms = sqrt(mean_i (perm(i)-i)^2) / (block_size-1)`.

Aggregate each metric over the 20 blocks by mean.

## Spectral-fidelity metric

For each block use the FIREWALL-04 mismatch:

`E_spec = || |FFT(y_surr-mean)| - |FFT(y_orig-mean)| ||_2 / || |FFT(y_orig-mean)| ||_2`.

Aggregate over blocks by mean and maximum.

## Arithmetic target score

Use exactly the frozen FIREWALL target-only statistic:

- linear detrend against actual zero-pair midpoint time inside each block;
- exact targets `omega = log(m)`;
- primary `m=2..13`;
- sensitivity `m=2..11`;
- no target retuning or shift optimization.

## Required outputs at each shuffle fraction

Report distributions of:

- mean moved fraction;
- mean normalized absolute displacement;
- mean normalized RMS displacement;
- mean spectral mismatch;
- maximum-block spectral mismatch;
- primary exact-target score;
- sensitivity score.

For each quantity report at least median, q05, q95, minimum and maximum.

Also report correlations across all realizations between:

1. spectral mismatch and ordering distance;
2. exact-target score and spectral mismatch;
3. exact-target score and ordering distance.

## Predeclared rigidity diagnostics

Across all generated realizations, count how many satisfy each of the following:

- `E_spec_mean <= 0.05`;
- `E_spec_mean <= 0.10`;
- `E_spec_mean <= 0.05` AND mean moved fraction `>= 0.10`;
- `E_spec_mean <= 0.05` AND mean normalized absolute displacement `>= 0.02`.

These are feasibility diagnostics, not p-values.

## Interpretation

### Rigidity pattern

If low spectral mismatch occurs only when ordering distance is very small, then exact amplitude distribution plus near-exact Fourier magnitude constraints are empirically rigid around the original ordering under this controlled permutation family.

### Flexible pattern

If substantially displaced permutations with low spectral mismatch exist, then the failed IAAFT fidelity gate was primarily an algorithmic limitation rather than evidence of rigidity. Those low-mismatch, far-from-original permutations become the correct next surrogate family for a stronger firewall.

### Target-score behavior

If target score decays with ordering distance faster than spectral mismatch does, then the `log(m)` alignment contains information not captured by closeness of the loop-index power spectrum alone.

If target score remains high whenever spectral mismatch remains low, then the apparent arithmetic signal may be tightly coupled to the same ordering constraints that determine the Fourier magnitudes.

## Guardrails

1. This is a structural map, not a confirmatory hypothesis test with one scalar rejection threshold.
2. The partial-permutation family does not exhaust all exact-multiset permutations.
3. No claim of mathematical uniqueness or phase-retrieval theorem follows from finite sampling.
4. Results from both ranges must be reported, including any height-dependent weakening.
5. No Riemann-Hypothesis claim follows from any outcome.
