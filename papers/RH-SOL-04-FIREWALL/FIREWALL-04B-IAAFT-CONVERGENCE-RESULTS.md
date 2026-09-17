# RH-SOL-04 · FIREWALL-04B — IAAFT convergence stress-test results

Status: statistical firewall passed; preregistered spectral-fidelity gate failed on both ranges.
Branch: `agent/rh-sol-04-firewall`.

## Frozen construction

For each 1000-loop block and each surrogate realization:

- preserve the exact blockwise multiset of area values;
- run `4` independent IAAFT starts;
- run `2000` IAAFT iterations per start;
- select the start with the lowest Fourier-magnitude mismatch only;
- never use the `log(m)` target score for surrogate selection.

Surrogate count: `B=500` per range.

Preregistered fidelity gate:

`median mean spectral mismatch <= 0.05`.

Primary target dictionary: `m=2..13`.
Sensitivity: `m=2..11`.

## Range 1: loops 1..20000

### Primary m=2..13

- observed: `0.04463219422177026`;
- null median: `0.014031302612183057`;
- null q95: `0.015390431358528014`;
- null q99: `0.016275517456108727`;
- null maximum: `0.01692083789535796`;
- empirical p-value: `0.001996007984031936`.

Observed / q99 ≈ `2.7422`.
Observed / null maximum ≈ `2.6377`.

### Sensitivity m=2..11

- observed: `0.05027641438222484`;
- null q99: `0.01823613433101833`;
- null maximum: `0.018911226859285698`;
- empirical p-value: `0.001996007984031936`.

Observed / q99 ≈ `2.7560`.
Observed / null maximum ≈ `2.6586`.

### Spectral fidelity

- median mean mismatch: `0.1477398945595509`;
- q95 mean mismatch: `0.1562498481975109`;
- maximum mean mismatch: `0.16114153242840895`;
- median maximum-block mismatch: `0.20033579948204858`;
- maximum maximum-block mismatch: `0.23705805031781665`;
- fraction of realizations with mean mismatch <= 0.05: `0.0`;
- fraction with mean mismatch <= 0.02: `0.0`;
- fidelity gate: **FAIL**.

## Range 2: loops 20001..40000

### Primary m=2..13

- observed: `0.034228925875265076`;
- null median: `0.019778925823337713`;
- null q95: `0.021011570998667402`;
- null q99: `0.02160768188544763`;
- null maximum: `0.0222939108114169`;
- empirical p-value: `0.001996007984031936`.

Observed / q99 ≈ `1.5841`.
Observed / null maximum ≈ `1.5353`.

### Sensitivity m=2..11

- observed: `0.03843732058522577`;
- null q99: `0.023985326382414063`;
- null maximum: `0.024477914678105492`;
- empirical p-value: `0.001996007984031936`.

Observed / q99 ≈ `1.6025`.
Observed / null maximum ≈ `1.5703`.

### Spectral fidelity

- median mean mismatch: `0.12862451297769012`;
- q95 mean mismatch: `0.13640271924711717`;
- maximum mean mismatch: `0.14108556163101552`;
- median maximum-block mismatch: `0.20334791871709362`;
- maximum maximum-block mismatch: `0.2925899950171727`;
- fraction of realizations with mean mismatch <= 0.05: `0.0`;
- fraction with mean mismatch <= 0.02: `0.0`;
- fidelity gate: **FAIL**.

## Comparison with FIREWALL-04

Increasing IAAFT effort from one 200-iteration start to four 2000-iteration starts selected by spectral fidelity improves the median mean mismatch:

- loops 1..20000: `0.17711 -> 0.14774`, about a `16.6%` relative reduction;
- loops 20001..40000: `0.16785 -> 0.12862`, about a `23.4%` relative reduction.

The improvement is real but remains far from the preregistered 5% fidelity gate.

## Dual verdict

### Statistical verdict: PASS

On both ranges and both target dictionaries:

- observed exceeds surrogate q99;
- empirical p-value is below `0.01`;
- no generated surrogate reaches observed.

Thus the stronger, best-of-four, 2000-iteration IAAFT family still does not reproduce the exact-`log(m)` target score.

### Fidelity verdict: FAIL

The joint-invariant fidelity requirement fails decisively:

- median mean mismatch remains about `14.8%` and `12.9%`;
- zero of 500 realizations on either range reaches mean mismatch `<= 5%`;
- zero reaches `<= 2%`.

Therefore FIREWALL-04B does **not** license the statement that an exact amplitude distribution plus a faithfully preserved second-order spectrum is jointly insufficient.

## Scientific interpretation

The correct conclusion is narrower:

> Even after a substantial IAAFT convergence stress test, exact blockwise amplitude-distribution preservation combined with moderately close Fourier-magnitude preservation does not reproduce the observed exact-`log(m)` alignment. However, the surrogate family does not achieve the preregistered spectral fidelity required for a strong joint-invariant no-go claim.

This is not a failure of the statistical firewall. It is a failure of the surrogate generator to enter the intended high-fidelity joint-invariant regime.

## New structural question

Because the original sequence itself has both the exact multiset and the exact Fourier magnitude spectrum, the joint constraints are feasible in principle. The persistent inability of independent IAAFT starts to approach that intersection raises a different possibility:

> the intersection of exact amplitude-distribution and near-exact Fourier-magnitude constraints may be highly rigid, with only the original sequence and trivial/near-trivial rearrangements occupying the very-low-mismatch region.

If so, asking for an independent surrogate that is simultaneously far from the original ordering and extremely close in spectrum may itself be a constrained phase-retrieval / permutation-rigidity problem.

A further test should therefore map the tradeoff between:

1. spectral mismatch;
2. distance from the original sequence/order;
3. exact-`log(m)` target score;

rather than merely increasing IAAFT iterations.

## Guardrails

1. FIREWALL-04B passes its statistical criterion but fails its fidelity gate.
2. No exact joint distribution-plus-spectrum surrogate conclusion is claimed.
3. The next stage should test feasibility/rigidity of the joint constraints, not silently weaken the fidelity threshold.
4. No Riemann-Hypothesis claim follows from this result.
