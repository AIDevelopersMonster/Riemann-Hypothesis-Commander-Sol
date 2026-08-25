# RH-SOL-04 · FIREWALL — primary assignment-surrogate results

Status: FIREWALL-01 and FIREWALL-02 completed on both predeclared ranges.
Branch: `agent/rh-sol-04-firewall`.

## Scope

Primary statistic: target-only sinusoidal explained-variance score on the exact frequencies `log(m)`.

Primary dictionary: `m=2..13`.
Predeclared sensitivity: `m=2..11`.
Surrogate count: `B=5000` for each family and each range.

Two surrogate families were frozen before inspection:

1. **FIREWALL-01 — within-block circular offsets**: independently rotate each 1000-loop area sequence by a random non-zero offset while keeping the actual zero-time block fixed.
2. **FIREWALL-02 — whole-block reassignment**: randomly reassign complete 1000-loop area trajectories among the fixed actual zero-time blocks while preserving the internal order of each area block.

## Range 1: loops 1..20000

### Primary m=2..13

#### Circular offsets

- observed: `0.044632194221770234`;
- null median: `0.015062928944469447`;
- null q95: `0.01899126466839227`;
- null q99: `0.020544493727716755`;
- null maximum: `0.023394564728844387`;
- empirical p-value: `0.0001999600079984003`.

Observed / q99 = `2.17247`.
Observed / null max = `1.90780`.

#### Whole-block reassignment

- observed: `0.044632194221770234`;
- null median: `0.003628263564204511`;
- null q95: `0.008075010454157861`;
- null q99: `0.010375153917726022`;
- null maximum: `0.015070052350478074`;
- empirical p-value: `0.0001999600079984003`.

Observed / q99 = `4.30183`.
Observed / null max = `2.96165`.

### Sensitivity m=2..11

Circular offsets:

- observed: `0.050276414382224834`;
- q99: `0.023090564607193012`;
- null maximum: `0.026173792692876174`;
- empirical p-value: `0.0001999600079984003`.

Whole-block reassignment:

- observed: `0.050276414382224834`;
- q99: `0.011463226100153549`;
- null maximum: `0.016871353561674504`;
- empirical p-value: `0.0001999600079984003`.

Both sensitivity controls reproduce the primary conclusion.

## Range 2: loops 20001..40000

This range was the frozen REALZERO holdout and is the stronger replication range for FIREWALL.

### Primary m=2..13

#### Circular offsets

- observed: `0.03422892587526507`;
- null median: `0.021260733510338782`;
- null q95: `0.02354029164615983`;
- null q99: `0.024416928036339932`;
- null maximum: `0.02674435072080597`;
- empirical p-value: `0.0001999600079984003`.

Observed / q99 = `1.40185`.
Observed / null max = `1.27986`.

#### Whole-block reassignment

- observed: `0.03422892587526507`;
- null median: `0.0036932970630888613`;
- null q95: `0.007170820456932399`;
- null q99: `0.009064969161070573`;
- null maximum: `0.012960993793906422`;
- empirical p-value: `0.0001999600079984003`.

Observed / q99 = `3.77596`.
Observed / null max = `2.64092`.

### Sensitivity m=2..11

Circular offsets:

- observed: `0.038437320585225754`;
- q99: `0.02717437441528342`;
- null maximum: `0.029761740415248133`;
- empirical p-value: `0.0001999600079984003`.

Whole-block reassignment:

- observed: `0.03843732058522576`;
- q99: `0.010069436968783974`;
- null maximum: `0.014592926564699007`;
- empirical p-value: `0.0001999600079984003`.

Again both sensitivity controls reproduce the primary conclusion.

## Primary verdict

All preregistered FIREWALL-01/02 tests pass on both disjoint ranges and on both target dictionaries.

In all eight observed-versus-surrogate comparisons:

- observed exceeds surrogate q99;
- empirical p-value is at the finite-surrogate floor `1/(5000+1)`;
- no generated surrogate reaches the observed score.

Therefore the present `log(m)` alignment cannot be reproduced merely by preserving:

- the within-block multiset of area values;
- cyclic loop-index autocorrelation under a common circular offset;
- block mean/variance/distribution;
- the internal 1000-loop geometry trajectory;
- or the unordered collection of full geometry blocks,

while destroying the correct geometry-to-zero-time assignment in the two tested ways.

The correct assignment carries information relevant to the exact-target score.

## Height-dependent nuance

The circular-offset firewall is visibly less separated from observed on loops `20001..40000` than on loops `1..20000`:

- primary observed/q99 falls from about `2.17` to about `1.40`;
- primary observed/null-max falls from about `1.91` to about `1.28`.

The firewall still passes decisively at the tested surrogate resolution, but this narrowing is a real descriptive feature and should be preserved rather than hidden.

No rate law is inferred from two ranges.

The whole-block reassignment firewall remains much more strongly separated on both ranges.

## Implementation audit

After the primary run and before further FIREWALL stages, `scripts/firewall_assignment_surrogates.py` was reread.

The implementation matches the preregistered design:

- observed and surrogates use exactly the same target-only score;
- each circular surrogate uses an independently sampled non-zero offset in each block;
- the zero-offset observed state is not sampled as a circular surrogate;
- whole-block reassignment uses random permutations and excludes the identity permutation;
- targets remain exactly `log(m)`, with no shift scan or post-view retargeting;
- primary and m=2..11 sensitivity differ only by the declared target subset.

No implementation defect requiring reinterpretation of FIREWALL-01/02 was identified.

## Scientific interpretation

The strongest defensible statement is:

> The exact `log(m)` target alignment in zeta-loop filled area depends on the correct geometry-to-zero-time correspondence more strongly than can be explained by the two tested surrogate families, even when substantial area-series structure is preserved.

This is stronger than REALZERO because it tests a class of preserved-structure counterfactuals rather than merely changing the spectral estimator.

## Guardrails

1. Failure of these surrogates does not prove arithmetic causation.
2. Circular offsets preserve only a restricted phase transformation of the loop-index spectrum; they do not independently randomize all Fourier phases.
3. Whole-block reassignment strongly changes the height assignment and therefore tests a coarser alternative.
4. A separate phase-randomized surrogate preserving the full blockwise second-order loop-index spectrum is required next.
5. Polygon-level geometry-preserving controls remain a later FIREWALL stage.
6. No Riemann-Hypothesis claim follows from this result.
