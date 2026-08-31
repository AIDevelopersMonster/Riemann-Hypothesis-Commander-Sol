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

- [`SOL_GRADED_REPORT_v0_1.md`](SOL_GRADED_REPORT_v0_1.md) — reflection-generated grading and strict non-equivalence to branch sign.
- [`SOL_GRADED_EXCHANGE_SELECTION_v0_2.md`](SOL_GRADED_EXCHANGE_SELECTION_v0_2.md) — pair-involution theorem, mirror-exchange theorem, two conservative mirror realizations, and exchange-factor underdetermination.
- [`SOL_GRADED_BILINEAR_LIFT_NO_GO_v0_3.md`](SOL_GRADED_BILINEAR_LIFT_NO_GO_v0_3.md) — canonical partial bilinearization, exact odd-odd domain theorem, typed-output closure obstruction, root-odd super-skew no-go, and final `1D-OBSTRUCTED` verdict.
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md) — category, strong embeddings, free linearization, completion dcpo, orbitwise completion, exchange loci, and functoriality.
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md) — `Xi` incompleteness, exchange chirality, and exact twisted one-orbit passport.
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md) — diagonal multi-orbit classification, double-coset interaction, minimal four-point stabilizer breaking, and Burnside enumeration.
- [`REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md`](REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md) — response to Review 1, novelty narrowing, weak-free degeneracy, strong-free nonexistence, and corrected universal-property target.
- [`REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md`](REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md) — initial RPM realization for required/protected/open reflection-admissibility schemas, term normal form, protected-strong universal maps, and finite construction theorem.

## Successor theory: RPM / RGPA

Set level:

`reflection-partial magma (RPM)` = partial binary operation plus an involution `nu` satisfying simultaneous-reflection equivariance

`mu(nu x, nu y) = nu mu(x,y)`

on an invariant partial domain.

Linear level:

`reflection-graded partial algebra (RGPA)` = vector space with involution `J`, invariant partial tensor domain, and linear product satisfying

`J m = m (J tensor J)`.

For `char K != 2`, the reflection eigenspaces generate the `Z_2` grading automatically wherever the product is defined.

### Foundations proved

1. RPMs form a category; strong embeddings preserve both defined and undefined legacy cells exactly.
2. Free linearization is a functor `K[-]: RPM -> RGPA_K`.
3. Conservative completions ordered by graph inclusion form a dcpo and complete meet-semilattice; arbitrary joins need not exist because conflicting output assignments are incompatible.
4. Reflection-compatible raw completion decomposes orbitwise under `R_2 = nu x nu`.
5. The geometric exchange locus is exactly the graph of the involution: `M_nu = Eq(R_2, swap) = {(x,nu x)}`.
6. Every defined mirror cell satisfies forced reflection-mediated exchange.
7. The larger algebraic exchange locus may contain additional off-mirror cells; its excess over the geometric locus is a structural invariant.
8. Exchange loci are functorial under RPM morphisms, exact under strong embeddings, and monotone under conservative completion.

### One-orbit and multi-orbit classification

The coarse profile

`Xi = (|E_geom|, |E_fix|, |E_split|, |E_excess|)`

is not complete. The exact one-orbit classifier for `O={p,R_2p}` is the twisted passport

`Pi_O(z) = [z]_(Gamma_O,star_p)`

with

`gamma star_p z = nu^(epsilon_p(gamma)) gamma z`.

For labelled unresolved reflection input-orbits `O_1,...,O_k`, with common input stabilizer `G` and local decoration spaces `Z_i`,

`Class(O_1,...,O_k) = G \ (product Z_i)`.

For two orbits, the forgetful map to individual passport classes has fiber

`H_1 \ G / H_2`.

Hence local passports factor independently over a given pair iff

`G = H_1 H_2`.

This yields the stabilizer-breaking interaction mechanism

`decoration -> stabilizer reduction -> refinement of later passport classes`.

A minimal nontrivial-reflection example occurs on four elements and carries the relational `SAME/OPPOSITE` phase. For finite `G`, labelled completion classes are counted exactly by Burnside's formula.

### Universal-property trichotomy

The post-Review-1 freeness problem is now closed at the first nontrivial level.

#### Weak free RPM over bare `Set`

Exists, but its multiplication domain is empty.

#### Strong free RPM over bare `Set`

Does not exist, already on one generator.

#### Schema-relative initial RPM

Let `A_0` be a base RPM and let a reflection-admissibility schema split candidate term pairs into:

- `R` — REQUIRED new cells;
- `P` — PROTECTED `UNDEF` cells;
- all remaining cells — OPEN.

Then there is a canonical initial realization

`F_(A_0)(S)`

whose carrier is the least closure of `A_0` under required formal products.

Its exact domain is

`D_S = D_0 union (R cap L_S^2)`.

Old base values are preserved, every legal required cell is defined, every protected cell remains undefined, and open cells are left undefined only in the initial realization and may be opened later.

For every schema realization `(A,j)` there is a unique RPM morphism

`j_hat : F_(A_0)(S) -> A`

extending `j`. Although this map need not be globally strong, it is automatically `P`-strong: protected pairs remain undefined after evaluation.

Every nonbase legal term has a unique binary-tree normal form. If `A_0` and explicit `R` are finite, then

`|L_S| <= |A_0| + |R|`,

and the fixed-point construction terminates after at most `|R|` strict growth stages.

This gives the universal object actually required by FCOA: exact legacy data, protected absence, controlled new cells, and an open frontier.

## Novelty status

The literature audit has narrowed what can responsibly be claimed.

Classical or standard neighboring machinery includes:

- general partial algebras and strong/closed homomorphisms;
- partial Horn / essentially algebraic free-model constructions;
- partial `*`-algebras;
- locality semigroups and related partial products;
- Chermak-style partial groups, generators/relations, and finite enumeration;
- diagonal group actions, double cosets, stabilizer chains, and Burnside enumeration.

Accordingly, the project does **not** claim novelty for those mechanisms themselves.

The current candidate distinctive package is narrower:

`covariant reflection + protected UNDEF + open completion frontier + reflection/exchange equalizer + reflection-compatible completion moduli`.

External priority for that exact package is still under audit.

## Publication status

The SOL-GRADED/SUSY question remains closed and should not be published as a SUSY model.

The successor RPM/RGPA theory now has sufficient internal mathematics for a standalone article, including a nontrivial universal-property layer. However standalone publication remains **not frozen** because the novelty/positioning audit is not finished.

The mathematical gap is now narrower than the bibliographic gap.

Before freezing publication, the programme should obtain:

1. a separation/comparison theorem against the closest involutive partial-algebra / binary-partial-group frameworks;
2. the next presentation theorem with equations and protected undefinedness;
3. a protection-safe quotient criterion preventing identifications from turning protected cells into defined cells.

## Next frontier

Priority next strike:

`PROTECTION-SAFE QUOTIENT / GENERATORS-AND-RELATIONS THEOREM`.

Extend a schema from

`(A_0,R,P)`

to

`(A_0,R,P,E)`,

where `E` is a reflection-stable family of equations between legal terms.

Exact target:

`Characterize when the partial congruence generated by E is protection-safe, and prove that the quotient of the initial term realization is initial among schema realizations satisfying E.`

This is the first place where ordinary term identification can collide with semantically protected `UNDEF`, so it is the next genuinely nontrivial universal-algebra barrier.