# RH-SOL-05 · POISSON-05_AMPLITUDE_70_30_OOS — preregistration

Status: **frozen before acquisition or analysis of any zeta-loop data beyond index 40000**.

## Background

POISSON-04C, performed post hoc on loops `20001..40000`, found a strongly non-monotone amplitude profile and selected the empirical split

`D1..D7 | D8..D10`

as the strongest aggregate low/high boundary after max-over-nine-splits correction.

Because that boundary was discovered on already inspected data, POISSON-04C is exploratory only.

POISSON-05 is the independent confirmatory test.

## Fresh range

Use the next contiguous range of exactly 20,000 loops:

`40001..60000`.

A zero table must provide indices `40001..60001` before any loop tensor is built.

No loop with index `<=40000` may enter the primary analysis.

## Loop and translation construction

Use the same established winding-only pipeline as POISSON-04:

- `dps=30`;
- initial segments `60`;
- no adaptive resampling unless it is part of the frozen builder default;
- boundary tolerance `1e-10`;
- q-grid resolutions `q=16,32`;
- primary spatial analysis on q32;
- q16 retained only for descriptive stability audit.

## Frozen spatial modes

Use exactly

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

For each q,

`G_q(a,b) = F_q[a,b] * exp(-pi i (a+b)/q)`.

## Phase-only representation

For temporal analysis use

`U = G32 / |G32|`.

Rows are dropped only if at least one frozen q32 coefficient is exactly zero or non-finite. The dropped count is reported separately for each group.

## Frozen amplitude coordinate

For each loop define

`M_n = min_ell |G32_n(ell)|`

over the four frozen modes.

The split is defined by **empirical amplitude rank within the fresh 20,000-loop range**, not by the numerical q70 value seen in POISSON-04C.

This prevents a height-dependent change in absolute amplitude scale from turning the test into a threshold-transfer artifact.

## Frozen 70/30 partition

Compute the empirical 70th percentile `q70` of `M_n` on the fresh range and define exactly two target-blind groups:

- `lower70`: `M_n <= q70`;
- `upper30`: `M_n > q70`.

No decile scan, no alternate split, and no optimization of the boundary are allowed in the primary analysis.

## Temporal statistic

Use exactly the q32 area-residualized complex Frobenius score used in POISSON-04/04B/04C:

1. preserve original consecutive 1000-loop block identity;
2. within each group and block residualize the four unit-phasor channels against `[1, area]`;
3. detrend residuals against `[1,t]`;
4. project on `[cos(omega t), sin(omega t)]`;
5. transform `R2 -> -log(1-R2+1e-15)`;
6. average over exact targets and available blocks.

Primary dictionary:

`omega_m = log(m), m=2..13`.

Sensitivity dictionary:

`m=2..11`.

## Matched-jitter null

Use `B=5000` and fixed seed `20261006`.

For each Monte-Carlo draw generate one common jitter vector

`eta_m ~ Uniform[-0.20,0.20]`

and apply the identical perturbed dictionary

`omega_m^null = log(m) + eta_m`

to both `lower70` and `upper30`.

For every draw compute

`Delta_70_30 = Q_lower70 - Q_upper30`.

## Frozen primary success criterion

Let

`Delta_exact = Q_lower70(exact log m) - Q_upper30(exact log m)`.

The 70/30 amplitude-regime result is confirmed if all hold:

1. `Delta_exact > 0`;
2. `Delta_exact` exceeds the matched-null q99;
3. empirical upper-tail `p_ge <= 0.01`;
4. the `m=2..11` sensitivity contrast is also positive;
5. lower70 exact score itself exceeds its own matched-jitter q99 with `p<=0.01`.

Upper30 is not required to be null-like; the primary claim is a **relative exact-frequency specificity advantage** for lower70 versus upper30 under a common frequency perturbation.

## Secondary diagnostics

Report but do not use for primary success:

- q16/q32 phase RMS and coherence in lower70 and upper30;
- top10 exact specificity using empirical q90;
- decile profile D1..D10;
- absolute fresh q70 amplitude value;
- exact-minus-null-mean excess in each group.

No secondary result may replace a failed primary criterion.

## Interpretation guardrails

A PASS would establish only the following finite-range OOS statement:

> On fresh loops `40001..60000`, the lower 70% of the empirical frozen-mode amplitude distribution exhibits a greater exact-Dirichlet-frequency phase-only specificity than the upper 30% under the frozen common local-frequency jitter family.

It would not establish:

- a universal 70/30 law;
- an absolute amplitude threshold;
- an asymptotic phase transition;
- a causal prime-decoding theorem;
- the Riemann Hypothesis.

A FAIL is equally informative and leaves POISSON-04C as an exploratory finite-range structure only.
