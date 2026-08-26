# RH-SOL-04 · FIREWALL-05 — permutation-rigidity map results

Status: completed on both predeclared ranges.
Branch: `agent/rh-sol-04-firewall`.

## Purpose

FIREWALL-05 mapped the geometry of exact-multiset partial permutations rather than testing a single null family. For each 1000-loop block, controlled fractions of positions were randomly permuted while preserving the exact blockwise area-value multiset.

Measured jointly:

- ordering distance;
- relative blockwise Fourier-magnitude mismatch `E_spec`;
- frozen exact-`log(m)` target score.

Shuffle fractions:

`0.01, 0.02, 0.05, 0.10, 0.20, 0.40, 0.60, 0.80, 1.00`.

Replicates: `B=300` per fraction per range, giving `2700` realizations per range.

## Range 1: loops 1..20000

Observed target scores:

- `m=2..13`: `0.04463219422177026`;
- `m=2..11`: `0.05027641438222484`.

Global pooled correlations across all 2700 realizations:

- spectral mismatch vs moved fraction: `0.9486787270292777`;
- spectral mismatch vs normalized mean absolute displacement: `0.9486385077386993`;
- spectral mismatch vs normalized RMS displacement: `0.9925211845896847`;
- primary score vs spectral mismatch: `-0.9916921391197819`;
- primary score vs moved fraction: `-0.9711908825395297`;
- primary score vs normalized absolute displacement: `-0.9711330813588461`;
- sensitivity score vs spectral mismatch: `-0.9917238808068813`.

Feasibility counts:

- total realizations: `2700`;
- mean `E_spec <= 0.05`: `63`;
- mean `E_spec <= 0.10`: `424`;
- `E_spec <= 0.05` AND moved fraction `>= 0.10`: `0`;
- `E_spec <= 0.05` AND normalized mean absolute displacement `>= 0.02`: `0`.

## Range 2: loops 20001..40000

Observed target scores:

- `m=2..13`: `0.034228925875265076`;
- `m=2..11`: `0.03843732058522577`.

Global pooled correlations:

- spectral mismatch vs moved fraction: `0.9540734317054662`;
- spectral mismatch vs normalized mean absolute displacement: `0.9539851004719625`;
- spectral mismatch vs normalized RMS displacement: `0.9938018936993195`;
- primary score vs spectral mismatch: `-0.9936491297270885`;
- primary score vs moved fraction: `-0.9714379930979201`;
- primary score vs normalized absolute displacement: `-0.9713690367862208`;
- sensitivity score vs spectral mismatch: `-0.9936530360052007`.

Feasibility counts:

- total realizations: `2700`;
- mean `E_spec <= 0.05`: `117`;
- mean `E_spec <= 0.10`: `462`;
- `E_spec <= 0.05` AND moved fraction `>= 0.10`: `0`;
- `E_spec <= 0.05` AND normalized mean absolute displacement `>= 0.02`: `0`.

## Primary structural finding

Across both independent ranges, low Fourier-magnitude mismatch was observed only near the original ordering under the tested controlled-partial-permutation family.

Combining the two ranges gives `5400` sampled realizations. Among them:

- `180` realizations achieved mean `E_spec <= 0.05`;
- **none** simultaneously moved at least `10%` of positions on average;
- **none** simultaneously reached normalized mean absolute displacement `>= 0.02`.

This is a direct empirical rigidity pattern:

> within the sampled exact-multiset partial-permutation family, entering the `E_spec <= 5%` spectral-fidelity region forces the ordering to remain close to the original sequence.

The replication across loops `1..20000` and `20001..40000` is especially important: the same qualitative geometry appears on both ranges.

## Target-score geometry

The frozen exact-`log(m)` score falls almost monotonically with spectral degradation across the pooled map. The pooled correlations are approximately `-0.992` and `-0.994` for the primary score on the two ranges.

Likewise, spectral mismatch rises strongly with ordering displacement; the strongest pooled relation is with normalized RMS displacement, approximately `0.993` and `0.994`.

These are structural-map correlations, not independent inferential tests. Because shuffle fraction is deliberately varied across the experiment, pooled correlations are partly driven by the controlled intervention itself and must not be interpreted as unconfounded causal coefficients.

## What FIREWALL-05 establishes

It establishes a finite-sample empirical fact about the tested permutation family:

1. exact multiset preservation alone allows large reordering;
2. large reordering rapidly destroys Fourier-magnitude fidelity;
3. low Fourier mismatch appears only close to the original ordering;
4. exact-`log(m)` target strength decays in near lockstep with that spectral/order degradation.

This explains why FIREWALL-04/04B struggled to generate high-fidelity exact-multiset surrogates far from the original ordering: the difficulty is consistent with a genuinely narrow feasible region, not merely with an obviously weak optimizer.

## What it does not establish

Finite random sampling does not prove that no far-from-original permutation with `E_spec <= 0.05` exists. The partial-permutation family is also not an exhaustive search of the `1000!` permutation space.

Therefore FIREWALL-05 does not yet prove permutation uniqueness or a phase-retrieval theorem.

## Next experiment

The correct next step is not more random sampling and not more IAAFT iterations. It is a **constrained adversarial search**:

> explicitly maximize ordering distance subject to `E_spec <= 0.05`, while preserving the exact area multiset and never optimizing the `log(m)` target score.

If such an optimizer finds substantially displaced low-mismatch permutations, they become the strongest available joint-invariant surrogates for a new target-score firewall.

If repeated independent constrained searches fail and terminate near the original ordering, the evidence for permutation-spectral rigidity becomes materially stronger.

## Guardrails

1. Correlations pooled across designed shuffle fractions are descriptive map geometry, not independent causal estimates.
2. Zero feasibility counts are empirical non-observations, not mathematical impossibility proofs.
3. No Riemann-Hypothesis claim follows from this result.
