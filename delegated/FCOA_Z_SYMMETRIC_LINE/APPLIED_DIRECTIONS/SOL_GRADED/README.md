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
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md) — extraction of the surviving mathematics into a general theory of reflection-partial magmas / reflection-graded partial algebras, including categories, strong embeddings, free linearization, completion dcpo, orbitwise completion, exchange loci, and functoriality.
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md) — first finite classification theorem: `Xi` is incomplete already on two reflected points; exact one-orbit isomorphism classes are twisted stabilizer orbits of the chosen output.
- [`REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md`](REFLECTION_GRADED_PARTIAL_ALGEBRAS_MULTI_ORBIT_INTERACTION_v0_3.md) — two-orbit diagonal classification, sequential stabilizer theorem, double-coset interaction obstruction, minimal four-point stabilizer-breaking example, general labelled multi-orbit classification, and Burnside enumeration.

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

### One-orbit classification

The coarse exchange profile

`Xi = (|E_geom|, |E_fix|, |E_split|, |E_excess|)`

is not complete. The failure already occurs on `A={x,bar x}`.

The exact one-orbit classifier for a two-point unresolved input orbit `O={p,R_2p}` is the twisted passport

`Pi_O(z) = [z]_(Gamma_O,star_p)`

with

`gamma star_p z = nu^(epsilon_p(gamma)) gamma z`.

Two one-orbit completions are isomorphic over the fixed base iff their passports agree.

### Multi-orbit interaction theorem

For labelled unresolved reflection input-orbits `O_1,...,O_k`, let

`G = intersection Gamma_(O_i)`

be their common input stabilizer and let `Z_i` be the admissible decoration space with its local twisted action `star_i`.

Then the exact labelled completion moduli are

`Class(O_1,...,O_k) = G \ (product Z_i)`

under the single diagonal carrier action.

For two orbits, the forgetful map to the product of individual passport spaces has fiber

`H_1 \ G / H_2`,

where `H_i` is the twisted stabilizer of the chosen local decoration.

Hence local passports factor independently over that pair iff

`G = H_1 H_2`.

This identifies the first genuine interaction mechanism of the completion theory:

`decoration -> stabilizer breaking -> refinement of later passport classes`.

A minimal nontrivial-reflection example occurs on four elements. Two joint completions have the same local one-orbit passports, the same `Xi`, the same anchoring data, and the same output reflection orbits, but differ by a relative reflection-phase bit `SAME/OPPOSITE` and are not isomorphic.

For finite `G`, the number of labelled `k`-orbit completion classes is exactly

`N = (1/|G|) sum_(gamma in G) product_i |Fix_(Z_i)(gamma)|`.

Thus RPM/RGPA now has a genuine finite completion/moduli theory, not just definitions and local invariants.

## Publication status

The SOL-GRADED/SUSY question remains closed and should not be published as a SUSY model.

The successor RPM/RGPA mathematics has now crossed the internal structural threshold for a standalone mathematical theory note:

- category and strong embeddings;
- free linearization;
- completion dcpo;
- exchange-locus theory;
- exact one-orbit classification;
- exact multi-orbit diagonal classification;
- double-coset interaction theorem;
- minimal stabilizer-breaking example;
- Burnside enumeration formula.

The remaining blocker is now primarily **bibliographic novelty and terminology**, not absence of theorem structure.

Before freezing a standalone publication, perform a dedicated hostile literature audit against partial magmas, locality semigroups/algebras, partial `*`-algebras, partial groups, involutive partial systems, partial actions/groupoids, and existing equivariant partial-algebra/completion theories. If no exact prior framework subsumes the simultaneous-reflection + exchange-equalizer + twisted-completion-moduli package, publication threshold is reached.

## Next frontier

Priority next strike:

`UNIVERSAL PROPERTY / FREE RPM-RGPA CONSTRUCTION`.

Characterize the free RPM generated by a reflected set with a prescribed protected domain, and determine the exact universal property of free linearization `K[-]` relative to maps into RGPAs.

In parallel, a literature/novelty audit is now mandatory before naming/priority claims are frozen.