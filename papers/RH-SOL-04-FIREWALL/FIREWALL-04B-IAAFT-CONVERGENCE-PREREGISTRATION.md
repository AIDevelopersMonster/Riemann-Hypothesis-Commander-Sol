# RH-SOL-04 · FIREWALL-04B — IAAFT convergence stress test

Status: preregistered after FIREWALL-04 and before FIREWALL-04B surrogate inspection.
Branch: `agent/rh-sol-04-firewall`.

## Motivation

FIREWALL-04 passed its frozen target-score criterion, but its IAAFT surrogates retained the exact blockwise area-value multiset while matching the original blockwise Fourier magnitudes only approximately. The median realization-mean relative spectral mismatch was about 17% on both tested ranges.

FIREWALL-04B is a new convergence/fidelity stress test. It does not replace or retroactively modify FIREWALL-04.

## Core question

Can the exact `log(m)` target alignment still reject IAAFT surrogates when the joint preservation of:

1. the exact blockwise area-value multiset; and
2. the blockwise loop-index Fourier magnitude spectrum

is substantially tighter than in FIREWALL-04?

## Frozen target statistic

Use exactly the existing FIREWALL target-only score:

- linear detrend against actual zero-pair midpoint time within each 1000-loop block;
- exact target frequencies `omega=log(m)`;
- cosine/sine least-squares fit;
- `-log(1-R2+1e-15)` target score;
- mean over targets and blocks.

Primary dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

No frequency search, shift optimization, target deletion, or target-score-based surrogate selection is permitted.

## Stronger IAAFT construction

For every block and every surrogate realization:

1. preserve the exact sorted original area values;
2. preserve the target rFFT magnitudes of the mean-centered original sequence;
3. generate `4` independent random initial permutations;
4. run each start for exactly `2000` IAAFT iterations;
5. after each start, compute the final relative spectral-magnitude mismatch

   `E_spec = || |FFT(y_surr-mean)| - |FFT(y_orig-mean)| ||_2 / || |FFT(y_orig-mean)| ||_2`;

6. retain the start with the smallest `E_spec`.

Selection is based **only** on preservation fidelity. The `log(m)` target score is not computed or consulted during start selection.

Every retained surrogate preserves the exact area-value multiset by final rank projection.

## Surrogate count and seeds

Because the construction is substantially more expensive:

- `B=500` per range;
- starts per block: `4`;
- iterations per start: `2000`;
- calibration seed: `20260831`;
- holdout seed: `20260901`.

Finite-surrogate p-value floor: `1/(500+1) ≈ 0.001996`.

## Spectral-fidelity gate

Before any strong joint-preservation interpretation is allowed, the realized surrogate ensemble must satisfy:

- median realization-mean `E_spec <= 0.05`.

Also report:

- q95 realization-mean mismatch;
- maximum realization-mean mismatch;
- median maximum-block mismatch;
- maximum maximum-block mismatch;
- fraction of realizations with mean mismatch <= 0.05;
- fraction with mean mismatch <= 0.02.

### Interpretation of the gate

If median mean mismatch remains above `0.05`, FIREWALL-04B may still be reported as a surrogate test, but it cannot support the claim that distribution and second-order spectrum have been jointly preserved with high fidelity.

If the gate is passed and observed still exceeds q99 with `p<=0.01` on both ranges, then the stronger statement becomes supported:

> The exact blockwise area distribution together with a high-fidelity approximation to the blockwise second-order loop-index spectrum is insufficient to reproduce the observed exact-`log(m)` alignment under the tested IAAFT construction.

## Primary success criterion

For each range and dictionary:

- observed > surrogate q99;
- empirical p <= 0.01.

The statistical pass/fail and the preservation-fidelity gate are reported separately.

## Ranges

Run independently on:

1. loops `1..20000`;
2. loops `20001..40000`.

No changes are permitted between ranges.

## Guardrails

1. FIREWALL-04B is a new test, not a correction of FIREWALL-04.
2. Best-start selection uses spectral mismatch only, never the target score.
3. Exact joint preservation of an arbitrary non-Gaussian marginal and arbitrary Fourier magnitude spectrum is not guaranteed by finite-iteration IAAFT; fidelity is measured explicitly.
4. Passing the fidelity gate and target test still does not prove arithmetic causation.
5. No Riemann-Hypothesis claim follows.
