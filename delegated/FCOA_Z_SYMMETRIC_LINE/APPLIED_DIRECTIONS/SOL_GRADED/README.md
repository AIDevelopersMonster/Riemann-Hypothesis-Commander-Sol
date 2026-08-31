# SOL-GRADED

**Status:** CLOSED AT CURRENT SUSY SCOPE — RGPA SUCCESSOR THEORY OPEN  
**Date:** 2026-08-31  
**Scientific director:** Commander Sol  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`

## Current verdict

The completed FCOA-Z line canonically generates a `Z_2`-graded linearized shadow through the eigenspaces of its derived reflection involution. Raw positive/negative branches are not even/odd parity sectors, and abstract grading alone loses the rooted shift geometry.

The SUSY/Lie-super route is closed negatively at the faithful-operation level:

- simultaneous reflection and argument exchange coincide exactly on the mirror locus `(x, nu x)`;
- reflection equivariance therefore induces a local exchange law there;
- the current FCOA-Z axioms do not select the super factor `(-1)^(pq)`;
- canonical free linearization preserves partiality, so `UNDEF` cannot be replaced by zero;
- no conservative mixed completion induces a total bilinear law on `V_1 x V_1`;
- inherited terminal outputs obstruct a nonzero faithful odd-odd base-even value;
- the old left-root/right-root role asymmetry contradicts Lie-super graded skewness independently of the mixed sector.

Hence the original partial `oplus` cannot be faithfully promoted to a Lie-super bracket by a one-dimensional conservative LC3 completion.

Current applied classification:

`FORMAL EMBEDDING` — reflection-linearized subsystem plus proved mirror-exchange law.

Line-first verdict for faithful Lie-superbracket emergence:

`1D-OBSTRUCTED`.

Direct identification of the FCOA operation with a Lie-super bracket:

`REJECT`.

## Reports

- [`SOL_GRADED_REPORT_v0_1.md`](SOL_GRADED_REPORT_v0_1.md)
- [`SOL_GRADED_EXCHANGE_SELECTION_v0_2.md`](SOL_GRADED_EXCHANGE_SELECTION_v0_2.md)
- [`SOL_GRADED_BILINEAR_LIFT_NO_GO_v0_3.md`](SOL_GRADED_BILINEAR_LIFT_NO_GO_v0_3.md)
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md)
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md)
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md)
- [`REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md`](REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md)
- [`REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md`](REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md)
- [`PROTECTION_SAFE_QUOTIENT_PRESENTATIONS_v0_5.md`](PROTECTION_SAFE_QUOTIENT_PRESENTATIONS_v0_5.md)

## Successor theory: RPM / RGPA

Set level:

`reflection-partial magma (RPM)` = partial binary operation plus an involution `nu` satisfying simultaneous-reflection equivariance

`mu(nu x, nu y) = nu mu(x,y)`

on an invariant partial domain.

Linear level:

`reflection-graded partial algebra (RGPA)` = vector space with involution `J`, invariant partial tensor domain, and linear product satisfying

`J m = m (J tensor J)`.

For `char K != 2`, the reflection eigenspaces generate the `Z_2` grading automatically wherever the product is defined.

### Classification and completion results

1. RPMs form a category; strong embeddings preserve defined and undefined legacy cells exactly.
2. Free linearization is a functor `K[-]: RPM -> RGPA_K`.
3. Conservative completions form a dcpo / complete meet-semilattice under graph inclusion.
4. The geometric exchange locus is `M_nu = Eq(R_2,swap) = {(x,nu x)}`.
5. `Xi` is incomplete; the exact one-orbit classifier is the twisted passport `Pi_O(z)`.
6. Multi-orbit labelled completions are diagonal quotients `G \ product Z_i`.
7. Two-orbit interaction fibers are double-coset spaces `H_1 \ G / H_2`; factorization holds iff `G=H_1H_2`.
8. Finite labelled completion classes are counted by Burnside's formula.

### Universal-property results

The freeness problem now has an exact trichotomy.

- Weak free RPM over bare `Set`: exists, but its product domain is empty.
- Strong free RPM over bare `Set`: does not exist.
- Relative initial RPM over a reflection-admissibility schema `(A_0,R,P)`: exists and is nontrivial.

The schema semantics are:

- `R` — REQUIRED cells;
- `P` — PROTECTED `UNDEF` cells;
- remaining cells — OPEN.

The initial carrier is the least closure under required formal products. Every nonbase legal term has a unique tree normal form. For finite explicit `R`, the construction terminates and satisfies `|L_S| <= |A_0|+|R|`.

### Protected generators-and-relations theorem

The presentation layer is now established.

A protected RPM presentation has the form

`< A_0 ; R | E ; P >`,

where `E` is a reflection-stable family of equations between legal terms.

Let

`theta_E = Cg_RPM(E)`

be the least RPM congruence containing the equations. Quotient multiplication is defined existentially on classes, so equations may activate previously undefined source pairs.

There are two independent requirements.

1. **Base separation**

`theta_E cap (A_0 x A_0) = Delta_(A_0)`.

2. **Protection safety**

For every `(p,q) in P`, there is no defined `(x,y) in D_F` with

`p theta_E x` and `q theta_E y`.

Equivalently, no protected pair becomes quotient-defined.

The main dichotomy is exact:

- if `theta_E` is base-separating and protection-safe, then
  `F(A_0,R,P)/theta_E`
  is the initial realization satisfying `E`;
- if either condition fails, then **no admissible realization exists at all**.

Failure is monotone: a larger congruence cannot repair a base collapse or protected-cell activation.

Thus equational identification may activate OPEN cells, but it may never activate PROTECTED cells.

For finite term carriers, `theta_E` is computable by finite saturation under reflection and operation coherence, followed by base/protection collision tests. This gives a decision procedure for finite protected presentations.

## Novelty status

The literature audit continues to constrain claims.

Classical/standard neighboring machinery includes general partial algebras, strong homomorphisms, partial Horn / essentially algebraic free constructions, partial `*`-algebras, locality semigroups, partial groups, diagonal actions, double cosets, stabilizer chains, and Burnside enumeration.

The current candidate distinctive package is narrower:

`covariant reflection + REQUIRED/PROTECTED/OPEN semantics + protected quotient consistency + reflection/exchange equalizer + reflection-compatible completion moduli`.

External priority for this exact package is not yet frozen.

## Publication status

The SOL-GRADED/SUSY question remains closed and should not be published as a SUSY model.

The successor RPM/RGPA programme now has enough internal mathematics for a standalone paper, including finite moduli, relative initial objects, and a protected generators-and-relations theory.

Publication remains **not frozen** only because the external novelty/separation question is still unresolved.

The next publication-critical step is no longer another internal theorem of the same type. It is a hostile comparison/separation theorem against the closest existing frameworks.

## Next frontier

Priority next strike:

`SEPARATION THEOREM AGAINST PARTIAL HORN / ESSENTIALLY ALGEBRAIC / BINARY PARTIAL GROUP FRAMEWORKS`.

Exact target:

1. determine whether REQUIRED/PROTECTED/OPEN protected presentations can be encoded faithfully as models of an existing essentially algebraic or partial-Horn theory with negative relational data;
2. determine whether the RPM reflection law is a genuine specialization/reduct of known involutive partial magma / binary partial group structures;
3. if equivalence exists, identify precisely which RPM results are instances of known general theorems;
4. if equivalence fails, prove a structural separation theorem exhibiting a property expressible/preserved in RPM protected-completion semantics but not captured by the nearest standard framework without enrichment.

This is now the decisive novelty barrier.