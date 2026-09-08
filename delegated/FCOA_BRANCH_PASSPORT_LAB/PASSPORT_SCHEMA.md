# FCOA Branch Passport Schema

**Laboratory:** FCOA — SOL-PASSPORT — Invariant Lab & Branch Diff Auditor  
**Schema version:** P0.1  
**Scope:** structural passports for FCOA partial-operation branches  
**Governance:** methods/audit infrastructure only; no silent promotion of research candidates

## 1. Purpose

A branch passport is a compact, falsifiable record of the structure carried by one FCOA branch. It must distinguish operation domain, operation values, external relations, carrier sorting, and terminal-output geometry. A single invariant such as `|Aut|` is never sufficient.

The passport is valid only when every field below is either:

- **PROVED** — established by an explicit proof in the branch sources;
- **ENUM** — independently obtained by exhaustive finite enumeration for the stated values of `N`;
- **REGRESSION** — a closed formula merely checked against an independently enumerated quantity;
- **WORKING** — a research candidate not yet hostile-audited;
- **OPEN** — not yet computed or not yet justified.

A function that simply returns the claimed closed form is not an `ENUM` check of that invariant.

## 2. Universe and sorting conventions

For each branch record separately:

1. base/active carrier `X_N`;
2. generic sector `G_N`;
3. terminal outputs already present in the backbone;
4. new terminal outputs introduced by the branch;
5. whether the presentation is typed/many-sorted or one-sorted;
6. whether terminal outputs may be permuted anonymously, are named, or are fixed by sort.

`UNDEF` is absence of an operation cell. It is never an operation value and must never be counted as an output fiber.

## 3. Mandatory passport

### A. Identification

- Branch name and predecessor.
- Mathematical status: published/fixed, hostile-audited, working candidate.
- Source files and verifier files.
- Exact range of `N`.

### B. Carrier and signature

- Exact carrier decomposition.
- Exact partial-operation signature.
- External relations/constants/sorts, if any.
- Base outputs versus terminal outputs.
- Explicit `UNDEF` convention.

### C. Operation table delta

Record every defined cell family. For an extension branch, give both:

- inherited cell families;
- new/removed/retagged cell families.

For each family record its cardinality as a function of `N`.

### D. Symmetry passport

Record separately:

1. `Aut(star)` of the full operation;
2. projected carrier action `pi_X Aut(star)` when terminal outputs are present;
3. `Aut(D_star | X_N)` of the active/base definedness reduct;
4. full one-sorted `Aut(D_star)` if terminal outputs remain in the same universe after value erasure;
5. stabilizers obtained by fixing distinguished boundary roles;
6. generators and their action on output fibers;
7. group order for `N=3,4,5`.

Never substitute a base-sort group for a full one-sorted group or conversely.

### E. Commutation passport

Record the exact locus

`Comm_star = {(x,y): x star y and y star x are both defined and equal}`

and its cardinality. If two branches have the same count but different loci, record the locus difference as well.

### F. Association Spectrum

On base triples `(X_N)^3`, record

`(EQ, NEQ, LEFT, RIGHT, NONE)`

with definitions:

- `EQ`: both bracketings defined and equal;
- `NEQ`: both defined and unequal;
- `LEFT`: only left bracketing defined;
- `RIGHT`: only right bracketing defined;
- `NONE`: neither defined.

Mandatory checksum:

`EQ + NEQ + LEFT + RIGHT + NONE = (N+1)^3`.

For every polynomial formula, compare against explicit enumeration for at least `N=3,4,5,6`; preferred regression range is `N=3..10`.

### G. Translation profiles

For every base point `x`, record the left and right partial translations

`L_x(y)=x star y`, `R_x(y)=y star x`.

At minimum record:

- domain size;
- multiset of output-fiber sizes;
- number of base outputs versus terminal outputs;
- injectivity of the maps `x -> L_x` and `x -> R_x` on the base sort;
- which profiles change from the predecessor.

### H. Terminal-output geometry

For every terminal output or output orbit record:

- number and shape of preimage cells;
- whether it is internally distinguishable;
- orbit under `Aut(star)`;
- orbit under the definedness group after value erasure;
- small-case collisions, especially `N=3`.

### I. Erasure tests

**Carrier-Erasure.** State exactly what remains when external carrier labels/order/auxiliary relations are forgotten, subject to the chosen signature.

**Value-Erasure.** Replace operation values by definedness and compute the active-sort and, where applicable, full one-sorted groups.

If the full operation is more rigid than the active-sort definedness reduct, record

`VRI(star) = [Aut(D_star | X_N) : pi_X Aut(star)]`

when the index is finite and the scope is unambiguous.

### J. Recoverability

For each structural subset/relation (`P_0`, `P_1`, `G_N`, adjacency, orientation, boundary roles, etc.) classify recovery as:

- uniformly definable from the reduct;
- finitely/contextually recoverable only;
- recoverable only up to an automorphism/orbit;
- not recovered.

Give the actual defining predicate or the obstruction, not only a prose claim.

### K. Arithmetic Leakage

Record only structural information actually imported or recovered. Distinguish:

- external carrier order/orientation;
- adjacency/successor;
- full finite order;
- arithmetic operations on external indices.

Importing an external order coloring is not by itself reconstruction of ordinary arithmetic.

### L. Small cases and exhaustive totals

Mandatory exact passports for `N=3,4,5`; include `N=6` in regression checks. Record every exceptional coincidence, including group coincidences such as `S_2 = C_2`.

### M. False extrapolations

Each passport must contain at least one section listing natural statements that the branch does **not** justify. Where possible give a smallest counterexample.

## 4. Branch diff record

For `B -> B'`, do not repeat both passports. Record only:

- added/removed/retagged cell families;
- domain change;
- value-fiber partition change;
- `Aut(star)` change;
- `Aut(D_star | X_N)` change;
- full one-sorted definedness change;
- commutation locus/count delta;
- Association Spectrum delta;
- translation-profile delta;
- output-orbit delta;
- recoverability delta;
- VRI delta;
- Arithmetic Leakage delta;
- status/evidence delta.

A zero delta is scientifically meaningful and should be written explicitly.

## 5. Passport acceptance rule

A branch is **passport-complete** only if:

1. all mandatory fields are filled or explicitly marked `OPEN`;
2. every formula has proof provenance and, where finite enumeration is feasible, independent regression evidence;
3. `UNDEF` is never modeled as a value;
4. base-sort and full-carrier claims are separated;
5. `N=3` has been checked explicitly;
6. no `WORKING` claim is silently reported as fixed.

This schema is stricter than the current branch notes by design: its purpose is to make cross-branch comparison reproducible and hostile-audit ready.
