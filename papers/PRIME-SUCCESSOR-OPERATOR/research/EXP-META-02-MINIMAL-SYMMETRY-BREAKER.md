# EXP-META-02 — Minimal Symmetry Breaker without Magnitude

Status: open research problem.
Depends on: EXP-META-01 Equivariant Off-Diagonal No-Go.

## Objective

Find a mathematically natural additional datum `Omega` for the multiplicative operator system

`A = C*_lambda(N_{>0})` acting on `H = l^2(N_{>0})`

such that all of the following hold:

1. `Omega` breaks the full prime-permutation symmetry:

   `Stab_P(Omega) = {id}`.

2. `Omega` is not an arbitrary labeling of the primes.

3. `Omega` does not simply import ordinary magnitude, prime index, `nextPrime`, or the global prime order.

4. A uniform local/spectral/operator relation built from `Omega` and the multiplicative shifts can potentially recover standard prime successor.

The core question is:

> What is the weakest natural source of prime-coordinate asymmetry that is not already ordinary magnitude?

## Why this is the correct next question

EXP-META-01 shows that uniform valuation-local operators, the unlabeled divisibility/multiplicative graph, and any functorial operator built only from that graph preserve the full action of `Sym(P)`.

Therefore non-diagonality by itself is irrelevant. A successful operator must contain genuinely new symmetry-breaking information.

## Candidate families to audit

Every candidate below must pass the same four tests: stabilizer, naturality, magnitude audit, successor locality.

### A. Arithmetic local data not obviously equivalent to magnitude

Examples to test only as candidates, not assumptions:

- residue-class interaction data;
- local congruence incidence patterns;
- p-adic interaction profiles that compare distinct primes without ordering them numerically;
- multiplicative characters or character families;
- valuation-coupling operators depending on relations among prime coordinates rather than on a uniform single-coordinate rule.

Warning: any construction depending only on isomorphism-invariant structure of the free commutative monoid remains prime symmetric unless some additional arithmetic datum distinguishes the coordinates.

### B. Dynamical data

Search for a distinguished dynamics whose generator is not merely `log N`:

- transfer operators;
- KMS-type structures;
- modular flows;
- arithmetic dynamical systems;
- naturally selected states or equilibrium structures.

Audit whether the symmetry is broken intrinsically or only because numerical magnitude was inserted into the Hamiltonian.

### C. Representation-theoretic / character data

Ask whether a natural family of representations or characters can distinguish prime generators in a canonical but non-magnitude way.

The target is not mere point separation. The family must induce standard orientation through one uniform invariant relation.

### D. Geometric or spectral data imported from zeta-related structures

Potentially relevant only if the construction is independent enough to avoid circularity:

- zeta/Dirichlet spectral data;
- geometric invariants of associated complex or adelic structures;
- spectral projections, resonances, or transition amplitudes tied to a canonical arithmetic object.

Any use of absolute frequency `log p` must be classified as magnitude import unless the orientation is extracted from scale-free internal relations.

## Required audit for each candidate

### Test 1 — Prime stabilizer

Compute or bound

`Stab_P(Omega)`.

If nontrivial, the candidate cannot recover standard successor by an intrinsic invariant rule.

### Test 2 — Label leakage

Determine whether `Omega` is equivalent to choosing arbitrary distinct labels on the prime set.

A trivial stabilizer is necessary but not sufficient.

### Test 3 — Magnitude leakage

Determine whether ordinary order on all naturals is recoverable from `(A,H,Omega)` by a direct or cumulative mechanism.

Where possible, strengthen this to a definability audit:

- is `<` recoverable?
- is `+` recoverable?

A positive answer may place the candidate on the full-magnitude side of the corridor.

### Test 4 — Successor locality

Seek one invariant relation

`Phi(L_p,L_q,Omega)`

such that the induced directed graph on the prime generators is exactly

`2 -> 3 -> 5 -> 7 -> ...`.

Merely producing a rigid total labeling is not sufficient.

## Preferred success modes

Rank candidates by strength:

- Level A: breaks some prime symmetry;
- Level B: trivial prime stabilizer;
- Level C: canonical/natural trivial stabilizer;
- Level D: produces a scale-free orientation of the prime atoms;
- Level E: yields local prime successor without recovering full magnitude.

Only Level E would solve the Prime-Successor Operator Problem as currently posed.

## No-Go target

A valuable alternative outcome is a theorem of the form:

> Every natural datum in a specified operator-algebraic class that breaks `Sym(P)` either is equivalent to arbitrary prime labeling or recovers ordinary magnitude/full arithmetic.

Such a theorem would close that entire operator corridor and justify moving to a genuinely richer arithmetic/geometric category.

## Immediate next task

Before proposing numerical experiments, classify candidate symmetry breakers by source of asymmetry:

1. externally labeled;
2. magnitude-derived;
3. cumulative-order-derived;
4. representation/dynamics-derived;
5. genuinely relational and scale-free.

Only class 5 is a serious candidate for the minimal operator corridor.
