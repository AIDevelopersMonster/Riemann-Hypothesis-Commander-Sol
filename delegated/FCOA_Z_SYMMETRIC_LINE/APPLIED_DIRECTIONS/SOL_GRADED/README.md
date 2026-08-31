# SOL-GRADED

**Status:** CLOSED AT CURRENT SUSY SCOPE — RGPA SUCCESSOR THEORY OPEN  
**Date:** 2026-08-31  
**Scientific director:** Commander Sol  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`

## Current verdict

The completed FCOA-Z line canonically generates a `Z_2`-graded **linearized shadow** through the eigenspaces of its derived reflection involution. Raw positive/negative branches are not even/odd parity sectors, and abstract grading alone loses the rooted shift geometry.

The exchange-selection phase proved:

- simultaneous reflection and argument exchange are distinct involutions in general;
- they coincide exactly on the **mirror locus** `(x, nu x)`;
- on mirror pairs, reflection equivariance itself becomes an exchange law;
- reflection-fixed outputs give symmetric/commutative mirror interaction;
- reflection-paired outputs give two-way-defined noncommutative mirror interaction;
- after linearization, output-even and output-odd components become exchange-symmetric and exchange-antisymmetric;
- two incompatible conservative `1D-CLOSED` mirror realizations exist, so the current FCOA-Z axioms do **not** select the super factor `(-1)^(pq)`.

The bilinear-lift phase closes the stronger SUSY emergence claim negatively:

- canonical free linearization of a partial FCOA operation is naturally a **partial** linear map on the span of defined basis tensors; `UNDEF` cannot be replaced by zero;
- for odd modes `a_n=e_n^+-e_n^-`, an LC3-conservative domain contains `a_n tensor a_m` only for `n=m` and only if both mirror orientations at depth `n` are opened;
- therefore no conservative mixed completion induces a total bilinear law on `V_1 x V_1`;
- even on an allowed odd square, inherited same-sign terminal outputs prevent a nonzero faithful value in the base-even carrier without projecting or identifying output sorts;
- independently, the old root asymmetry gives `oplus_tilde(e_0,a_n)=a_n` but `oplus_tilde(a_n,e_0)=a_{n-1}`, contradicting Lie-super graded skewness before any mixed-sector choice is made.

Hence the original partial `oplus` itself cannot be faithfully promoted to a Lie-super bracket by a one-dimensional conservative LC3 completion.

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

## Successor theory: RPM / RGPA

The mathematically correct object surviving the hostile SUSY audit has now been abstracted beyond FCOA.

Set level:

`reflection-partial magma (RPM)` = partial binary operation plus an involution `nu` satisfying simultaneous-reflection equivariance

`mu(nu x, nu y) = nu mu(x,y)`

on an invariant partial domain.

Linear level:

`reflection-graded partial algebra (RGPA)` = vector space with involution `J`, invariant partial tensor domain, and linear product satisfying

`J m = m (J tensor J)`.

For `char K != 2`, the reflection eigenspaces generate the `Z_2` grading automatically wherever the product is defined.

### Foundational theorems now proved

1. RPMs form a category; strong embeddings preserve both defined and undefined legacy cells exactly.
2. Free linearization is a functor `K[-]: RPM -> RGPA_K`.
3. Conservative completions ordered by graph inclusion form a dcpo and complete meet-semilattice; arbitrary joins need not exist because conflicting output assignments are incompatible.
4. Reflection-compatible completion decomposes orbitwise under `R_2 = nu x nu`: a two-point input orbit is determined by one output choice; a fixed input orbit can only take a reflection-fixed output.
5. The geometric exchange locus is exactly the graph of the involution:
   `M_nu = Eq(R_2, swap) = {(x,nu x)}`.
6. Every defined mirror cell satisfies forced reflection-mediated exchange.
7. The larger algebraic exchange locus may contain additional off-mirror cells; its excess over the geometric locus is a new structural invariant.
8. Exchange loci are functorial under RPM morphisms, exact under strong embeddings, and monotone under conservative completion.

This is enough to answer the successor question positively at the foundational level:

`YES — reflection-graded partial algebras form a coherent independent mathematical class with their own morphism, completion, and exchange-locus theory.`

This is a mathematical classification statement, not yet a priority/novelty claim against all literature.

## Publication status

The SOL-GRADED/SUSY question remains closed and should not be published as a SUSY model.

The new RPM/RGPA foundations are already theorem-level, but standalone publication is **not yet frozen**. Before claiming a new named theory in the literature, the next threshold requires:

- dedicated bibliography/terminology audit against partial magmas, locality semigroups/algebras, partial `*`-algebras, partial groups, and related involutive partial systems;
- at least one further representation/universal-property theorem;
- two non-FCOA examples with computed exchange profiles;
- one finite classification theorem.

## Next frontier

Classify finite conservative completions up to strong RPM isomorphism.

First target:

`Is reflection-orbit data + exchange profile Xi complete for minimal one-orbit extensions?`

If yes, this gives the first nontrivial classification theorem of the new theory. If not, the smallest counterexample identifies the next invariant.
