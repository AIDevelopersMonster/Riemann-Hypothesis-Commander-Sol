# RH-SOL-05 · POISSON-04C_AMPLITUDE_DECILE_BOUNDARY — exploratory analysis plan

Status: **post-hoc exploratory diagnostic** on the already inspected POISSON-04 OOS tensor.

POISSON-03 remains `statistical PASS / phase-stability FAIL`.
POISSON-04 remains frozen **full confirmation FAIL**.
POISSON-04B remains exploratory.

## Motivation

POISSON-04B showed:

- bottom10 versus top10 matched contrast is extreme;
- bottom10 versus middle80 matched contrast is ordinary;
- middle80 versus top10 matched contrast is extreme;
- bottom10 and middle80 carry nearly equal exact-target excess over matched local-jitter baselines;
- top10 carries almost no exact-target excess.

This suggests a **regime boundary near the high-amplitude end**, rather than a monotone `lower amplitude => stronger specificity` law.

POISSON-04C maps the amplitude dependence at decile resolution and searches for a single low/high split with an explicit max-over-splits null correction.

## Data

Use only

`data/derived/rh-sol-05-poisson-04-phase-singularity-oos/oos_20001_40000_q16_q32.npz`

with exact range loops `20001..40000`.

No zeta-loop reconstruction is performed.

## Spatial representation

Use the same four frozen q32 midpoint-corrected modes:

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

For each loop define

`M_n = min_ell |G32_n(ell)|`.

Temporal channels are unit phasors `G32/|G32|`. Rows are discarded only where at least one frozen q32 coefficient is zero or non-finite.

## Amplitude deciles

Construct empirical q10, q20, ..., q90 of `M_n` over all 20,000 loops and define ten target-blind strata `D1,...,D10` in increasing amplitude order.

No temporal score enters the decile construction.

## Temporal statistic

For every decile use exactly the POISSON-04/04B q32 area-residualized complex Frobenius target statistic:

1. preserve original consecutive 1000-loop block identity;
2. within each decile/block residualize the four unit-phasor channels against `[1, area]`;
3. detrend against `[1,t]`;
4. project onto `[cos(omega t), sin(omega t)]`;
5. transform `R2 -> -log(1-R2+1e-15)`;
6. average over exact frequencies `omega=log(m), m=2..13` and available blocks.

## Common matched-jitter null

Use `B=2000`, seed `20261005`.

For Monte-Carlo draw `j`, draw one common 12-vector

`eta_j,m ~ Uniform[-0.20,0.20]`

and use

`omega_j,m = log(m)+eta_j,m`

for **all ten deciles**.

Thus each draw produces a matched vector

`Q^j = (Q_D1^j,...,Q_D10^j)`.

For each decile report:

- exact score;
- matched-null mean and median;
- exact-minus-null-mean excess;
- matched-null sd;
- q95, q99, max;
- empirical upper-tail p-value;
- standardized exact displacement from its null mean.

The decile profile is descriptive/exploratory.

## Boundary scan

For each split `k=1,...,9`, define

`C_k = mean(Q_D1,...,Q_Dk) - mean(Q_D{k+1},...,Q_D10)`.

The same contrast is computed on every common-jitter draw.

For each split report:

- exact `C_k`;
- null mean/sd;
- standardized displacement

`Z_k = (C_k_exact - mean(C_k_null))/sd(C_k_null)`.

A positive `Z_k` means the exact dictionary unusually favors the lower-amplitude side of that split relative to common local-frequency perturbations.

## Max-over-splits correction

Because nine split points are inspected, do not select the largest `Z_k` and quote its unadjusted tail probability.

Instead compute

`T_exact = max_k Z_k`.

For each null draw `j`, compute standardized split deviations using the same per-split null mean/sd,

`Z_k^j = (C_k^j - mean(C_k_null))/sd(C_k_null)`,

and

`T_j = max_k Z_k^j`.

Report

`p_max = (1 + count(T_j >= T_exact))/(B+1)`.

This is an exploratory family-wise correction for the scan over the nine candidate boundaries.

Also report the maximizing split `k*`, but interpret it only as a candidate transition location on already inspected data.

## Secondary profile summaries

Report:

- correlation matrix of the ten matched-null decile scores;
- Spearman correlation between decile rank and exact-minus-null-mean excess, descriptive only;
- adjacent exact-minus-null-mean differences, descriptive only.

## Interpretation guardrails

1. This is not a confirmatory fresh-data test.
2. A small `p_max` would show that **some amplitude split** is unusually aligned with exact Dirichlet frequencies under the tested common-jitter family; it would not establish a universal amplitude phase transition.
3. The candidate split must be tested later on genuinely fresh data before being promoted.
4. No asymptotic or Riemann-Hypothesis claim follows.
