# RH-SOL-05 · POISSON-04_PHASE_SINGULARITY_OOS — preregistration

Status: frozen before analysis of fresh loops `20001..40000`.
Branch: `agent/rh-sol-05-poisson`.

## Question

POISSON-03B ZERO-SAFE suggested an exploratory pattern on already inspected loops `1..20000`:

`bottom10 phase-only target score > top10 > middle80`,

while q16/q32 pointwise phase stability improves with Fourier amplitude.

POISSON-04 asks whether that **phase-singularity amplification** pattern survives on a fully fresh OOS range.

## Fresh OOS range

Use only loops `20001..40000`, based on the pre-existing zero table

`data/zeros/lmfdb_zeta_zeros_20001_40001.csv`.

No loop in this range contributed to POISSON-01/01B/02/03/03B.

Build winding-only translation tensors at `q=16,32` using the same loop-construction defaults as the established SHIFT pipeline:

- `dps=30`;
- initial segments `60`;
- no adaptive resampling unless explicitly present in the frozen builder defaults;
- boundary tolerance `1e-10`.

## Frozen spatial modes

Use exactly

`(1,0), (0,1), (1,1), (1,-1)`.

Apply the same midpoint correction

`G_q(a,b) = F_q[a,b] * exp(-pi i (a+b)/q)`.

## Phase definition

For temporal phase-only analysis use q32 unit phasors

`U = G32 / |G32|`.

Rows are dropped only when at least one frozen q32 coefficient is exactly zero or non-finite, because phase is then mathematically undefined. The number dropped is reported.

No amplitude threshold is used to select temporal rows beyond the frozen amplitude strata below.

## Frozen amplitude stratification

For each loop define

`M_n = min_{ell in four frozen modes} |G32_n(ell)|`.

Using only the fresh OOS range, compute target-blind empirical quantiles of `M_n` and define:

- `bottom10`: lowest 10%;
- `middle80`: 10th–90th percentiles;
- `top10`: highest 10%.

The quantile construction uses no temporal target score.

## Frozen temporal statistic

For each stratum use the same complex Frobenius exact-target statistic as POISSON-03:

1. retain only rows with defined phase;
2. keep original 1000-loop block identity from the full OOS sequence;
3. blockwise residualize the four unit-phasor channels against `[1, area]`;
4. detrend against `[1,t]`;
5. project on exact temporal basis `[cos(log(m)t), sin(log(m)t)]`;
6. transform `R2 -> -log(1-R2+1e-15)`;
7. average over targets and blocks.

Primary target dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

## Confirmatory target-jitter null

For each of the three frozen strata separately generate `B=2000` independent jitter dictionaries

`omega_m^null = log(m) + eta_m`,

with independent

`eta_m ~ Uniform[-0.20,0.20]`.

Use fixed seeds:

- bottom10: `20261001`;
- middle80: `20261002`;
- top10: `20261003`.

Report null median, q95, q99, maximum and

`p_ge = (1 + count(null >= observed))/(B+1)`.

No frequency scan, common shift optimization, target deletion, or post-hoc mode selection is allowed.

## Frozen primary claim

The **phase-singularity amplification** pattern is confirmed if all hold on the fresh OOS range:

1. bottom10 q32 area-residualized phase-only exact score exceeds its jitter q99 and `p_ge <= 0.01`;
2. top10 also exceeds its jitter q99 and `p_ge <= 0.01`;
3. middle80 is reported independently regardless of pass/fail;
4. exact-score ordering is

   `bottom10 > top10 > middle80`;

5. bottom10/top10 amplification ratio is `>1` and bottom10/middle80 ratio is `>1`;
6. `m=2..11` sensitivity is directionally consistent with bottom10 remaining above middle80.

The ordering criterion is confirmatory because it was frozen from POISSON-03B before this OOS tensor is analyzed.

## q16/q32 phase-stability audit

Separately report, by the same amplitude strata, q16/q32 phase RMS error and circular coherence. This is descriptive and must not be conflated with temporal localization.

The expected exploratory direction is increasing phase stability with amplitude, but POISSON-04's primary claim concerns temporal phase-singularity amplification, not restoration of the failed global POISSON-03 phase-stability gate.

## Interpretation guardrails

1. POISSON-03 remains `statistical PASS / phase-stability FAIL` regardless of POISSON-04.
2. Confirmation would establish a finite-range OOS property of this geometric observable, not an asymptotic theorem.
3. Target-jitter tests exact-frequency localization against the frozen local-frequency null family, not every possible null model.
4. No Riemann-Hypothesis claim follows from either outcome.
