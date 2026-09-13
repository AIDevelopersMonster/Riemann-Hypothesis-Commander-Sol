# HATTER-SOL-10 · Publication Audit v0.9

## Proposed title

**EN:** Ideal Factor Networks Beyond Unique Element Factorization  
**RU:** Идеальные факторные сети за пределами однозначной факторизации элементов

## Publication thesis

HATTER-SOL-10 extends the HATTER-SOL-09 typed factor-network model from principal/UFD element factorizations to arbitrary imaginary quadratic ideal factorizations. The core construction is not the classical ideal theory itself, but the chain

\[
\text{prime-ideal factorization}
\to
\text{minimal principalization witnesses}
\to
\text{finite witness-state sets}
\to
\text{residue fibers}
\to
\text{typed network optimization}
\to
\text{phase switching / residue-forced coexistence}.
\]

## 1. Closed theorem layers

### T10.1--T10.4 · Principalization cost and compatibility

For a nonzero integral ideal `I`,

\[
\delta(I)=\min_{0\ne\alpha\in I}\frac{|N(\alpha)|}{N(I)}.
\]

Closed results:

- `delta(I)` is a positive integer;
- `delta(I)=1` iff `I` is principal;
- `delta(I)` is the least norm of an integral ideal in the inverse ideal class;
- principal ideals exactly recover HATTER-SOL-09 witness states;
- conjugation compatibility holds.

### T10.5--T10.8 · Witness-adaptive ideal nodes

Minimal witness orbits modulo units are canonically identified with least-norm integral ideals in the inverse class.

Nonprincipal ideals can carry more than one typed witness state, including incomparable states.

Nodewise Pareto pruning is invalid: a locally dominated witness can be globally necessary for network feasibility.

Correct semantics: retain the full finite witness-state set and optimize witness selection jointly with the network.

### Interaction layer

Pure cross-edge interaction is separated from connectivity by an unconstrained utilization support function.

In the uniform one-channel model, the interaction law is exact and decomposes into:

- neighbor-space release;
- parity repair.

### T10.14--T10.16 · Witness switching and phase threshold

A nonprincipal ideal in `Q(sqrt(-15))` has two minimal witness states

\[
S=(3,2),\qquad T=(6,1).
\]

The locally optimal witness on `K_4` is `S`, while the globally optimal witness on `K_8` is `T` for weights `(1,2)`.

For two tradeoff states on even complete hosts, the exact transition threshold is

\[
c_*=P_s+Q_s+
\left(\frac{w_Q}{w_P}-1\right)(Q_s-Q_t).
\]

### T10.17--T10.18 · Purity theorem

On even complete hosts with a common finite witness-state set, strict heterogeneous mixed phases cannot outperform the best pure state.

The global optimum is the upper envelope

\[
\frac{k}{2}\max_X\phi_{k-1}(X).
\]

Mixed coexistence can occur only at an exact phase boundary, where graph parity can select allowed compositions.

### T10.19--T10.21 · Residue-enforced mixed phase

For a two-state ideal species with distinct companion ideals `J_S != J_T`, the residue ideal

\[
R_t=J_S^{k-t}J_T^t
\]

uniquely determines the composition count `t`.

Thus a fixed principalization residue can forbid both pure phases and force an interior mixed witness population.

Exact laboratory:

\[
q^8\subset Q(\sqrt{-15}),
\qquad R_4=(16),
\]

forces `S^4T^4` on `K_8`. The unconstrained value is `32`; the residue-constrained optimum is exactly `30`.

### Residue-refined response

Publication-safe status:

- residue labels should be principal integral ideals, not chosen generators;
- finite Pareto antichains are combined by Pareto-union and Pareto-filtered Minkowski sum;
- forgetting residue labels recovers the ordinary witness-adaptive response after global Pareto minimization;
- block-disjoint factor systems satisfy an exact residue convolution law;
- the fully interacting network is **not** multiplicative because cross-edges can improve the block baseline.

## 2. Hostile corrections already made

The following tempting claims were rejected during the branch:

1. **Normalized ideal-lattice shape alone is enough.** False: it cannot recover varying HATTER-SOL-09 principal witness geometry.
2. **Nodewise Pareto pruning is safe.** False: explicit `Q(sqrt(-15))` counterexample.
3. **Class-group cost should be a third additive boundary coordinate.** Rejected: class charge is conserved and naive cancellation terms telescope.
4. **Joint witness/network optimization creates gain merely by reordering maxima.** False: finite maxima commute.
5. **Strict mixed phases should appear freely on complete hosts.** False: purity theorem.
6. **Residue-refined full response is multiplicative.** False in the interacting network; only the block-disjoint arithmetic/network baseline convolves exactly.

These corrections should be retained explicitly because they define the safe claim boundary.

## 3. Classical prior-art ingredients — do NOT claim novelty

The following are classical or independently established topics:

- unique prime-ideal factorization in Dedekind domains;
- ideal class groups and inverse classes;
- least-norm or normalized representatives of ideal classes;
- Minkowski bounds;
- correspondence with imaginary quadratic lattices / binary quadratic forms;
- principal ideals and fractional ideal groups;
- Pareto sets, Minkowski sums, and Pareto-filtered sums;
- graph degree constraints, matchings, and 1-factorizations of even complete graphs.

## 4. Candidate original contribution — conservative wording

The branch supports the following publication-safe originality claim:

> We introduce a witness-adaptive network construction that couples canonical prime-ideal factorization with minimal principalization witnesses, typed interface capacities, principalization-residue fibers, and Pareto network response. Within this framework we prove exact compatibility with the principal/UFD model, exhibit nonprincipal multistate nodes, derive witness-state switching thresholds, prove purity on even complete hosts, and show that arithmetic residue constraints can force mixed witness phases that are absent in the unconstrained network.

Do **not** claim that minimal ideal representatives, ideal-class geometry, Pareto sums, or graph factorizations are new individually.

## 5. Literature audit status

Targeted searches surfaced nearby but distinct material on:

- least-norm / normalized ideal representatives in imaginary quadratic fields;
- minimal-norm residue digit sets in imaginary quadratic arithmetic;
- nonunique factorization in commutative algebra and monoids;
- Pareto-filtered Minkowski sums and min-plus convolution.

No surfaced source matched the full chain

\[
\text{ideal principalization witnesses}
\to
\text{typed factor-network states}
\to
\text{residue-indexed network sectors}
\to
\text{witness phase transition / residue-forced coexistence}.
\]

This is an internal literature audit only, not independent confirmation of novelty.

## 6. Remaining publication obligations

### Mathematical

The theorem core is sufficiently closed for a conservative preprint. No additional structural theorem is mandatory before drafting.

Before v1.0, perform one consistency pass on:

1. residue terminology (`principal residue ideal` vs generator orbit);
2. exact scope of connected vs unconstrained utilization functions;
3. theorem numbering across files;
4. the use of `Q(sqrt(-15))` class-number facts and ideal identities;
5. whether every explicit edge-set example realizes the stated typed degrees.

### Literature / positioning

Add formal references for:

1. Dedekind ideal factorization / class groups;
2. Minkowski least-norm class representatives;
3. binary quadratic forms / imaginary quadratic ideal classes;
4. 1-factorization of `K_{2m}`;
5. modern Pareto-sum literature as terminology/computational context;
6. parent HATTER-SOL-09 DOI once published.

### Publication packaging

Required before Zenodo:

- English article v1.0;
- Russian article v1.0;
- bibliography and DOI audit;
- notation table;
- explicit novelty-boundary paragraph;
- theorem/proposition numbering audit;
- PDF visual QA;
- SHA256 manifest;
- Zenodo metadata;
- repository README/update with DOI after deposit.

## 7. Publication threshold decision

\[
\boxed{\text{MATHEMATICAL PUBLICATION THRESHOLD: CROSSED}}
\]

The branch now contains more than a speculative extension. It has a coherent sequence of definitions, no-go corrections, exact theorems, non-UFD examples, a general phase-transition law, a purity theorem, and a residue-enforced coexistence theorem.

Recommendation: **freeze structural research for HATTER-SOL-10 and move to preprint assembly/audit.**

Further ideas — especially orbital-port filtrations — remain future-branch material and should not be inserted into the current paper.