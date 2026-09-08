# RH-SOL-05 · POISSON-04B_MATCHED_NULL_CONTRAST — exploratory analysis plan

Status: frozen implementation plan for a **post-hoc exploratory diagnostic** on the already inspected POISSON-04 OOS tensor.

This analysis cannot alter the frozen POISSON-04 verdict. POISSON-04 remains **full confirmation FAIL** because the preregistered `top10` jitter-null criterion failed.

## Purpose

POISSON-04 exposed a large stratum-dependent baseline in the raw exact-target score. In particular, the independent jitter-null medians differed strongly between `bottom10`, `middle80`, and `top10`.

POISSON-04B asks a narrower methodological question:

> After forcing the **same jittered target dictionary** on all three amplitude strata in every Monte-Carlo draw, is the exact-frequency between-stratum contrast unusual relative to the matched-jitter contrast distribution?

This directly removes the confounding caused by comparing three raw scores against three separately fluctuating frequency dictionaries.

## Data

Use only the already built POISSON-04 tensor:

`data/derived/rh-sol-05-poisson-04-phase-singularity-oos/oos_20001_40000_q16_q32.npz`

Range must be exactly loops `20001..40000`.

No new zeta-loop reconstruction is required.

## Frozen spatial phase representation

Use exactly the same four q32 midpoint-corrected modes as POISSON-04:

- `(1,0)`;
- `(0,1)`;
- `(1,1)`;
- `(1,-1)`.

For each mode

`G_q(a,b) = F_q[a,b] * exp(-pi i (a+b)/q)`.

Temporal phase-only channels are

`U = G32 / |G32|`.

Rows are dropped only if any frozen q32 coefficient is zero or non-finite.

## Frozen amplitude strata

Repeat the exact POISSON-04 target-blind definition

`M_n = min |G32_n(ell)|`

over the four frozen modes, with empirical q10 and q90 on the full OOS range:

- `bottom10`: `M <= q10`;
- `middle80`: `q10 < M < q90`;
- `top10`: `M >= q90`.

No target score enters stratum construction.

## Temporal score

Repeat the POISSON-04 q32 area-residualized complex Frobenius statistic:

1. block identity is inherited from the original 20,000-loop sequence in consecutive 1000-loop blocks;
2. within each stratum and block, residualize the four unit-phasor channels against `[1, area]`;
3. detrend residuals against `[1,t]`;
4. project onto `[cos(omega t), sin(omega t)]`;
5. transform `R2 -> -log(1-R2+1e-15)`;
6. average over frequencies and available blocks.

Exact target dictionary:

`omega_m = log(m), m=2..13`.

## Matched-jitter design

Use `B=2000` by default and fixed seed `20261004`.

For Monte-Carlo draw `j`, generate one common vector

`eta_j,m ~ Uniform[-0.20,0.20]`

and define

`omega_j,m = log(m) + eta_j,m`.

**The identical `omega_j` vector is then scored on bottom10, middle80 and top10.**

Thus every draw yields a matched triple

`(Q_B^j, Q_M^j, Q_T^j)`.

## Contrasts

For both the exact dictionary and every matched-jitter draw compute:

- `Delta_BT = Q_bottom - Q_top`;
- `Delta_BM = Q_bottom - Q_middle`;
- `Delta_MT = Q_middle - Q_top`.

For each contrast report:

- observed exact contrast;
- matched-null mean and median;
- matched-null standard deviation;
- q01, q05, q95, q99;
- null minimum and maximum;
- empirical one-sided `p_ge = (1 + count(null >= observed))/(B+1)`;
- empirical lower-tail `p_le = (1 + count(null <= observed))/(B+1)`;
- standardized displacement `(observed - null_mean)/null_sd`.

Also report the matched-null correlation matrix of `(Q_B,Q_M,Q_T)` so that the degree of common-frequency cancellation is visible.

## Interpretation

POISSON-04B is exploratory because the OOS data and the baseline issue were already inspected before this analysis was designed.

Therefore:

- a small `p_ge` for `Delta_BT` or `Delta_BM` is evidence that the exact dictionary produces an unusually large low-amplitude advantage relative to **common local frequency perturbations**;
- a small `p_le` for `Delta_MT` is evidence that the exact dictionary reverses or suppresses the high-amplitude raw-score advantage relative to common jitter;
- these are diagnostic matched-null statements, not a new confirmatory theorem;
- no result from POISSON-04B can retroactively convert POISSON-04 to PASS.

## Guardrails

1. POISSON-03 remains `statistical PASS / phase-stability FAIL`.
2. POISSON-04 remains frozen full-confirmation FAIL.
3. POISSON-04B uses no frequency scan, target deletion, mode selection, or threshold optimization.
4. No asymptotic or RH claim follows.
