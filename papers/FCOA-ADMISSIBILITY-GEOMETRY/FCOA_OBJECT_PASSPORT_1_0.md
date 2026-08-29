# FCOA Object Passport 1.0

**Object:** Fixed-Carrier Oriented Algebra (FCOA)  
**Russian:** Ориентированная алгебра фиксированного носителя  
**Document role:** versioned mathematical passport of the object and accepted theorem programme  
**Status:** canonical working passport 1.0  
**Backend authorities:** `FCOA_DEFINITION_1_0.md`, `FCOA_FOUNDATIONAL_SPECIFICATION.md`, `FCOA_MORPHISMS_EQUIVALENCE_REPRESENTATION_1_0.md`  
**Rule:** this passport records what is fixed, what is known to exist, what is impossible in declared classes, and what remains open. It must not silently turn an extension theorem into an axiom of the base object.

---

## 1. Identity card

### Name

\[
\boxed{\text{FCOA = Fixed-Carrier Oriented Algebra}}
\]

### Mathematical habitat

Nearest standard setting:

\[
\boxed{
\text{typed / many-sorted partial algebra}
+
\text{oriented carrier presentation}
+
\text{FO relational reducts}.
}
\]

FCOA is not defined as a group, ring, semiring or field.

### Core purpose

FCOA is a laboratory for **structural memory**: how information about orientation, order, distance, addition and multiplication can be compiled into domains, values, sorts, incidence patterns and generated auxiliary structures of partial operations.

---

## 2. Canonical reference carrier

For the canonical natural line:

\[
B=\mathbb N_0=\{0,1,2,\ldots\}.
\]

Project notation:

\[
P_n\leftrightarrow n.
\]

The index `n` is external metalanguage unless the corresponding numerical relation is primitive or internally recovered.

### Arithmetic firewall

The carrier `N_0` does not automatically contain ordinary

\[
+_{\mathbb N},\qquad \times_{\mathbb N}.
\]

---

## 3. Canonical baseline object

The reference object is

\[
\mathfrak F_{M0}^{\omega}
=(\mathbb N_0;E^+,E^\ast,E^\times;\oplus,\otimes).
\]

Output families are disjoint tagged sorts and are terminal in the baseline.

### `oplus`

For `n>=1`:

\[
0\oplus n=n,
\]

\[
n\oplus0=n-1,
\]

\[
n\oplus n=E_n^+.
\]

All other base-base cells are `UNDEF`.

### `otimes`

For `n>=1`:

\[
0\otimes n=0.
\]

For `n>=2`:

\[
n\otimes0=E_n^\ast,
\]

\[
1\otimes n=n\otimes1=n,
\]

\[
n\otimes n=E_n^\times.
\]

All other base-base cells are `UNDEF`.

---

## 4. Structural type

| Field | Passport value |
|---|---|
| Active carrier | fixed, explicitly declared |
| Orientation | retained in construction presentation; erasable in operational reduct |
| Operations | partial, typed, fixed arity |
| Argument roles | positional / role-sensitive |
| Domain | structural information channel |
| Values | independent structural information channel |
| Output sorts | allowed; terminal in M0 |
| Ordinary commutativity | not assumed |
| Ordinary associativity | not assumed |
| Distributivity | not assumed |
| Global zero / one | not assumed |
| Inverses | not assumed |
| Closure on active sort | not assumed |
| Relationalization | canonical FO interface |

---

## 5. Erasure passport

Two presentations must be distinguished.

### Oriented presentation

\[
\mathfrak F^{\rm or}=(B,\preceq;\mathcal O;\Omega).
\]

### Carrier-erased operational reduct

\[
\mathfrak F^\circ=(B;\mathcal O;\Omega).
\]

The central memory question is always explicit:

> What survives after the external orientation or generator scaffold is erased?

No recovery result belongs in the passport unless the erasure regime is stated.

---

## 6. Status vocabulary

### `F` — fixed/proved

Accepted definition or theorem inside its stated scope.

### `W` — working

Useful terminology or architecture not yet promoted to an invariant theorem.

### `O` — open

Mathematically unresolved or deliberately unchosen.

### `B` — saved branch

An archived but noncanonical research alternative.

### `UNDEF`

A cell is outside the domain of the current partial operation.

### `OUT`

A finite-truncation result belongs to the master rule but lies outside the present finite window.

---

## 7. Canonical finite baseline passport

For

\[
X_N=\{P_0,\ldots,P_N\},\qquad N\ge3,
\]

the accepted M0 invariants include:

### Addition reduct

\[
\operatorname{Aut}(X_N,\oplus)=1.
\]

### Multiplication reduct

With

\[
G_N=\{P_2,\ldots,P_N\},
\]

\[
\operatorname{Aut}(X_N,\otimes)\cong S_{N-1}.
\]

### Joint reduct

\[
\operatorname{Aut}(X_N,\oplus,\otimes)=1.
\]

### Generic interpretation

`oplus` is boundary/predecessor-rich; `otimes` is the symmetry-rich laboratory baseline.

---

## 8. Primary information channels

The programme has established that the following must be treated as separate channels.

1. **Domain geometry** — which cells are defined.
2. **Value geometry** — equality/fibre pattern among outputs.
3. **Output-sort architecture** — where results live.
4. **Anchors / boundary points** — distinguished positions that break residual symmetry.
5. **Argument roles** — left/right position.
6. **Nesting / recursion** — whether outputs re-enter or history is materialized.
7. **Auxiliary carriers / coordinates** — added or internal coordinate systems.
8. **Generator provenance** — how the primitive memory was produced.

This separation is an accepted methodological invariant of the programme.

---

## 9. Accepted memory ladder

The current semantic ladder is:

\[
AL0=FO[<],
\]

\[
AL\text{-}FS=FO[<,\text{ultimately periodic unary memory}],
\]

\[
AL1=\text{EqGap / truncated-addition gateway},
\]

\[
AL2=\text{addition + multiplication / full finite arithmetic benchmark}.
\]

Accepted strict separation:

\[
\boxed{AL0<AL\text{-}FS<AL1.}
\]

G4-A provides a canonical order-only benchmark with generic FO power exactly `FO[<]`.

---

## 10. G-family capability register

### M0 — baseline

Purpose: reference symmetry and boundary structure.

### G1 — external admissibility skeleton

External relation can destroy generic symmetry while erasing it restores the M0 symmetry.

### G2 — domain compilation

Directed adjacency can be compiled into operation definedness using one anonymous terminal output.

Accepted principle:

\[
\boxed{\text{external geometry}\to\text{domain placement}\to\text{internal structural memory}.}
\]

### G3 — domain/value separation

Same or similar definedness geometry can have different automorphism groups after value-fibre structure is imposed.

### G4 — bounded added-output rigidity amplification

A small number of added anonymous orientation outputs can induce factorial-scale rigidity relative to the M0 generic symmetry.

G4-A uniformly recovers a generic total order while its generic FO theory remains equivalent to finite linear order.

---

## 11. Fixed theorem: domain and value geometry are independent resources

For a typed fibre map

\[
c:D\to O
\]

with domain automorphism group `Gamma`, value fibres reduce the surviving automorphisms to the stabilizer of the fibre equivalence relation.

Programme-level accepted form:

\[
\boxed{
\operatorname{Aut}(\text{valued layer})
\cong
\operatorname{Stab}_{\Gamma}(\equiv_c)
}
\]

under the declared typed hypotheses.

This underlies the Value-Rigidity Index programme.

---

## 12. Fixed theorem: rigidity is not order memory

A finite reduct may be rigid,

\[
\operatorname{Aut}(\mathfrak A)=1,
\]

while there is no corresponding uniform FO theorem recovering a full order across the family.

Therefore:

\[
\boxed{
\text{rigidity}\neq\text{uniform FO order memory}.}
\]

---

## 13. Fixed theorem: regular primitive wall

Within a fixed finite-copy presentation whose primitive relation/operation graphs are position-regular, FO closure remains position-regular.

Consequently neither EqGap nor truncated addition is uniformly FO-definable in that class.

Conceptual form:

\[
\boxed{
\text{regular local primitives}+FO
\not\Rightarrow
\text{variable displacement memory}.}
\]

This yields the Closure-Placement Principle: unbounded synchronized history must appear in a primitive graph, an unbounded closure semantics, or a materialized auxiliary structure.

---

## 14. Fixed theorem: finite-state wall

Prefix-consistent deterministic finite-state unary generation can leave pure `FO[<]` (for example by parity phase), but finitely many such ultimately periodic memories do not recover EqGap or addition.

Thus:

\[
\boxed{
\text{finite phase memory}<\text{variable displacement memory}.}
\]

---

## 15. Fixed theorem: Presburger compression barrier

For a fixed finite family of unvaried base-sorted Presburger-definable numerical predicates, uniform FO recovery of truncated addition requires total primitive support

\[
\boxed{\Omega(N^2).}
\]

The bound is sharp because the truncated addition graph itself has `Theta(N^2)` support.

Scope firewall: this theorem does not cover varied size-dependent scaffolds, growing auxiliary sorts, BIT-like histories, or non-Presburger generated memory.

---

## 16. Fixed theorem: internal digit exact-AL1 scaffold

There exists a varied deterministic size-dependent scaffold on the explicit `N`-element carrier with:

\[
\boxed{\Theta(N)\text{ charged primitive support}}
\]

that uniformly FO-defines truncated addition but not multiplication.

The target itself remains dimension `1`, while two internal coordinate maps expose a latent two-coordinate factorization.

Consequently:

\[
\boxed{
\text{target FO interpretation dimension alone does not control additive compression.}
}
\]

Working presentation parameter:

\[
\operatorname{CFW}=\text{Coordinate Factorization Width}.
\]

For the two-digit scaffold,

\[
\operatorname{CFW}=2.
\]

---

# 17. SOL-INFINITY — accepted object capability

**Status:** `F` within the exact published provenance scope.  
**Publication:** DOI `10.5281/zenodo.22151456`.  
**Director acceptance:** `SOL_INFINITY_DIRECTOR_ACCEPTANCE_2026-08-29.md`.

This result is recorded as an **existence/capability theorem for an FCOA extension**, not as a property of the M0 baseline.

### 17.1 Carrier and primitive layer

There exists a payload-preserving structure on

\[
U=\mathbb N^2
\]

with one simple symmetric irreflexive graph relation `G`.

Equivalently, introducing one terminal output `Omega`, it gives one commutative partial binary operation

\[
\boxed{x\star y=\Omega\iff G(x,y).}
\]

### 17.2 Primitive geometry

The accepted construction satisfies:

\[
G\text{ is }C_4\text{-free},
\]

\[
\boxed{\text{atomic half-graph depth}(G)=2.}
\]

### 17.3 Cost

In the FO-recovered max-shell order, the first `N` payload vertices induce only

\[
\boxed{\Theta(N)}
\]

primitive graph incidences.

### 17.4 Global order memory

Despite the primitive shallowness and linear incidence cost,

\[
\boxed{(U,G)\Rightarrow_{FO}(U,\prec)\cong(\mathbb N,<).}
\]

Thus a full order of type `omega` may emerge from FO composition even when the atomic primitive relation itself has bounded ladder depth.

### 17.5 Arithmetic leakage

Relative to the recovered order `prec`, ordinary rank addition and multiplication are not FO-definable:

\[
\boxed{+_{\prec}\notin FO(U,G),}
\]

\[
\boxed{\times_{\prec}\notin FO(U,G).}
\]

Hence the infinite order-memory construction remains strictly below ordinary FO arithmetic.

### 17.6 Exact dimension barrier in pure-order provenance

Within the class of fixed-dimensional FO interpretations in pure discrete order `(N,<)` with finitely many fixed parameters:

\[
\boxed{
\dim=1
\text{ cannot combine linear primitive binary cost with FO full }\omega\text{-order}
}
\]

while the explicit construction has dimension `2`.

Therefore, in this exact provenance class,

\[
\boxed{\dim_{\rm self}=2.}
\]

This is **not** a universal dimension theorem for arbitrary FCOA sources.

### 17.7 Exact diagonal-hub law

For a pure-order-definable `omega`-order on `N^d`, the definable diagonal spine must occur among the first `N` positions at rate

\[
\Omega(N^{1/d}).
\]

Max-shell order attains

\[
\Theta(N^{1/d}).
\]

Hence in dimension `2`:

\[
\boxed{H_2(N)=\Theta(\sqrt N).}
\]

### 17.8 Meaning for the FCOA passport

SOL-INFINITY establishes that none of the following is necessary for global order memory:

- primitive directionality;
- loops;
- multiple primitive binary relations;
- multiple operation layers;
- multiple output values;
- unbounded atomic half-graph depth;
- superlinear primitive incidence cost.

Inside the published construction the surviving structural resource is two-coordinate self-organization with a definable nonlocal diagonal spine.

---

## 18. Publication/capability ledger

| Result family | Status | Passport interpretation |
|---|---|---|
| M0/G1/G2 admissibility geometry | published/core | canonical finite baseline + domain compilation |
| G3/G4 value rigidity | accepted research core | value fibres are an independent memory channel |
| G4-A generic FO collapse | fixed | order without addition/multiplication |
| U1 finite-state wall | fixed | finite phase memory below EqGap |
| Regular-Primitive Barrier | fixed | local regular primitives cannot generate EqGap in static FO |
| Presburger Compression Barrier | fixed | quadratic exact-AL1 floor in unvaried base-sorted Presburger class |
| Internal digit scaffold | fixed theorem candidate after internal audit | linear exact AL1 in varied internal-coordinate model |
| SOL-INFINITY | published / director accepted | linear-cost shallow primitive relation can FO-generate infinite order without arithmetic |
| SOL-NESTING | published / closed | atomicity/nesting branch, separate semantic axis |
| Value-Rigidity / identity-digraph manuscript | publication-ready at prior audit | separate finite rigidity package |

---

## 19. Resource passport

No scalar `cost` is accepted as a universal invariant.

Every serious comparison should expose a vector containing at least:

\[
\boxed{
(
S_N,
A_N,
Q_N,
d,
k,
\alpha,
\eta,
\lambda
)
}
\]

where:

- `S_N` — primitive support/cell count;
- `A_N` — growing auxiliary-carrier size;
- `Q_N` — cross-carrier/coordinate incidence support;
- `d` — interpretation dimension;
- `k` — number of growing coordinate/channel sorts;
- `alpha` — output-alphabet growth;
- `eta` — provenance/generator class;
- `lambda` — semantic leakage level.

When relevant also record anchors, arity, finite-state complexity, nesting depth, closure semantics, witness escape, carrier-role inflation and coordinate factorization width.

---

## 20. Equivalence passport

The phrase “same FCOA” is incomplete unless the comparison level is stated.

Accepted levels:

1. literal typed isomorphism;
2. definitional equivalence;
3. mutual uniform FO interpretability;
4. same recovered target (`<`, Add, Mul, etc.);
5. same semantic phase/leakage level.

Resource lower bounds may transfer only across the equivalence level for which invariance has actually been proved.

---

## 21. Provenance passport

Every extension theorem must declare one of the following or a finer class:

- U0 / FO-definitional;
- local finite-state generated;
- closure/recursion generated;
- explicit numerical scaffold;
- varied size-dependent scaffold;
- arbitrary size oracle.

Arbitrary size-oracle constructions are valid negative benchmarks but are forbidden as evidence for intrinsic minimality unless oracle cost itself is being studied.

---

## 22. Current open frontier

The current main-line frontier after the internal digit result is:

\[
\boxed{
\text{Is }\Theta(N)\text{ the true exact-AL1 floor}
}
\]

once:

- every target element remains explicitly represented;
- all coordinate/incidence maps are charged;
- arbitrary oracular size dependence is forbidden;
- provenance is explicitly constrained;
- multiplication must remain FO-undefinable.

The earlier candidate frontier “interpretation dimension `1` versus `2`” is no longer accepted as a stand-alone invariant because internal coordinate factorization can achieve linear exact AL1 while the target representation itself remains dimension `1`.

A second open problem is whether a useful coordinate-factorization statistic can be normalized under bounded-fibre recodings or whether it is only presentation-level.

---

## 23. Foundational open fields

The object passport deliberately leaves the following unresolved:

1. whether generic off-diagonal `oplus` should ever receive a canonical law beyond M0;
2. whether generic off-diagonal `otimes` should ever receive a canonical completion;
3. the final axioms of a nested-output FCOA subclass;
4. whether orientation belongs to the most abstract object or only to generator provenance;
5. the preferred category of FCOA morphisms;
6. the intrinsic representation-equivalence notion for resource complexity;
7. whether Coordinate Factorization Width can be made interpretation-invariant;
8. the broadest provenance-safe class in which exact AL1 has a linear lower bound.

---

## 24. Passport revision rule

This document is not a chronological notebook.

A new theorem enters the passport only if one of the following happens:

- it changes the definition of the object;
- it proves a new invariant of the baseline;
- it proves a capability of some declared FCOA subclass;
- it proves an impossibility/lower bound in a declared representation class;
- it changes the accepted resource vector or equivalence language;
- it closes or opens a principal phase boundary.

Every entry must carry its scope.

If a future result contradicts a passport item, the item is not silently edited away: the passport version is incremented and the revision states which scope or theorem failed.

---

## 25. Why a passport is different from a classification

A classification asks primarily:

> To which known class does this object belong, or which objects are equivalent/isomorphic?

A passport asks a different operational question:

> What is this object, how is it presented, which invariants are known, what can it encode, what can it not encode, under which equivalence/provenance assumptions, how expensive are its representations, what has been published, and which fields remain unknown?

Thus classification is one field of the passport, not a replacement for it.

For FCOA the distinction is essential because the same recovered semantic target may be realized by presentations with radically different domains, output fibres, auxiliary carriers, provenance and resource costs.

---

## 26. One-page current passport summary

\[
\boxed{
\begin{array}{ll}
\text{Name} & \text{Fixed-Carrier Oriented Algebra (FCOA)}\\
\text{Base type} & \text{typed partial algebra with oriented presentation}\\
\text{Canonical carrier} & \mathbb N_0\\
\text{Canonical baseline} & \mathfrak F_{M0}^{\omega}\\
\text{Core channels} & \text{domain, value fibres, sorts, anchors, roles, nesting, coordinates}\\
\text{Baseline arithmetic} & +,\times\text{ absent unless recovered}\\
\text{Order capability} & \text{yes, including sparse/derived mechanisms}\\
\text{Finite order-only benchmark} & G4\text{-A}: FO[<]\\
\text{Intermediate layer} & AL0<AL\text{-}FS<AL1\\
\text{Presburger AL1 floor} & \Theta(N^2)\text{ in fixed unvaried base-sorted class}\\
\text{Varied internal AL1} & \Theta(N)\text{ exact AL1 exists}\\
\text{Infinite sparse order} & \Theta(N)\text{ primitive graph cost exists}\\
\text{SOL-INFINITY primitive} & 1\ C_4\text{-free undirected relation, ladder depth }2\\
\text{SOL-INFINITY arithmetic} & \neg FO(+),\ \neg FO(\times)\\
\text{Pure-order infinite dimension} & 2\text{ exact for the published linear-cost order package}\\
\text{Pure-order hub law} & \Theta(N^{1/d})\text{ diagonal spine; }\Theta(\sqrt N)\text{ at }d=2\\
\text{Current frontier} & \text{linear lower bound for provenance-safe exact AL1}
\end{array}
}
\]
