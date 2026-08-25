# RH-SOL-04 · FIREWALL — preregistration

Status: preregistered before surrogate inspection.
Branch: `agent/rh-sol-04-firewall`.

## Core question

REALZERO established that the `log(m)` comb survives direct irregular-time analysis on the actual zero ordinates. FIREWALL asks a stronger falsification question:

> Is the comb tied to the correct correspondence between zeta-loop geometry and the actual zero-time sequence, or can it be reproduced by controls that preserve substantial non-arithmetic structure while destroying that correspondence?

The primary observable remains winding filled area

`A_n = Area(D_n)`

and the primary time coordinate remains

`t_n = (gamma_n + gamma_{n+1}) / 2`.

The direct irregular-time spectral estimator and target dictionary are frozen from REALZERO.

## Primary observed statistic

Use the already-frozen REALZERO comb score on `m=2..13`:

`S_obs = mean score at omega=log(m), m=2..13`.

Also report the predeclared sensitivity `m=2..11`.

No target retuning is permitted.

## FIREWALL-01 — within-block circular-offset surrogate

For each 1000-loop block independently, circularly rotate the area sequence by a random non-zero offset while leaving the actual time sequence fixed.

This preserves exactly within each block:

- the multiset of area values;
- the loop-index cyclic autocorrelation structure;
- all adjacent differences up to the single wrap boundary;
- the block mean, variance and empirical distribution;
- the actual zero-time coordinates themselves.

It destroys the original pointwise assignment

`A_n <-> t_n`

and therefore destroys the original arithmetic phase relation except for accidental invariants.

Primary surrogate count:

- `B = 5000` realizations;
- random seed `20260825`;
- each block offset sampled uniformly from `1..999`.

For every surrogate compute the same direct irregular-time spectrum and the same exact-target comb score.

Report:

- observed score;
- surrogate median;
- surrogate q95;
- surrogate q99;
- empirical upper-tail p-value;
- maximum surrogate score.

Primary success criterion for FIREWALL-01:

`S_obs > surrogate q99` and empirical `p <= 0.01`.

## FIREWALL-02 — whole-block reassignment surrogate

Partition the range into the same consecutive 1000-loop blocks. Randomly permute whole area blocks among the fixed actual-time blocks, preserving the internal order of all 1000 areas inside each moved block.

This preserves:

- every complete 1000-loop area trajectory;
- all within-block shape, distribution and loop-index ordering;
- the collection of actual time blocks;
- the global collection of geometry blocks.

It destroys the correct height assignment of those geometry blocks.

Primary surrogate count:

- `B = 5000`;
- seed `20260826`;
- identity permutation excluded.

Score exactly as above.

Primary success criterion:

`S_obs > surrogate q99` and empirical `p <= 0.01`.

## Two ranges

Run the firewall independently on:

1. loops `1..20000`;
2. loops `20001..40000`.

The second range is the stronger replication because it was the frozen REALZERO holdout.

No surrogate family may be tuned on the first range and then silently redefined for the second.

## Interpretation matrix

### Case A — both surrogates fail strongly

If observed score exceeds q99 for both circular-offset and block-reassignment controls on both ranges, then the comb depends on more than the marginal geometry distribution, local cyclic autocorrelation, or the unordered collection of 1000-loop geometry blocks. The correct geometry-to-zero-time assignment carries essential information.

### Case B — circular offsets fail but block reassignment survives

Then fine local geometry-time phase matters, but coarse height placement may not.

### Case C — circular offsets survive but block reassignment fails

Then coarse height dependence matters more than local pointwise assignment.

### Case D — controls reproduce the comb

Then the present arithmetic interpretation is materially weakened and FIREWALL must identify which preserved non-arithmetic feature is sufficient.

## Secondary diagnostics

After primary scores are recorded, report:

- m=2..11 sensitivity;
- best common shift distribution for a smaller diagnostic subset if computationally feasible;
- score correlations with original block means/variances;
- observed versus surrogate target-local peak positions.

These cannot replace the primary exact-target statistic.

## Guardrails

1. These surrogates do not prove arithmetic causation even if they fail.
2. They test specific alternatives: assignment/order effects under strong preservation of area-series structure.
3. Full geometry-preserving controls at the polygon/Argand-loop level remain a later FIREWALL stage.
4. Phase-randomized surrogates preserving a chosen second-order spectrum will be a separate preregistered stage, not mixed into FIREWALL-01/02 after inspection.
5. No Riemann-Hypothesis claim follows from any outcome.
