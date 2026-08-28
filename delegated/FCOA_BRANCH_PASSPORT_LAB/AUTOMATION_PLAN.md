# FCOA Passport Automation Plan

**Version:** P0.1

## 1. Objective

Build a dependency-light exact finite auditor that takes an explicitly defined partial operation and emits a reproducible structural passport plus a diff against a predecessor.

The tool is evidence infrastructure, not a proof engine. Exhaustive finite checks support and attack formulas; they do not replace theorem proofs.

## 2. Core representation

Represent a partial operation as a dictionary/map

`(x,y) -> value`

containing **defined cells only**. Absence of a key means `UNDEF`. Never insert an `UNDEF` sentinel into the value set used for fiber/orbit computations.

Keep metadata for:

- active/base elements;
- terminal outputs;
- named/fixed elements;
- sorts;
- inherited backbone versus branch-added cells.

## 3. Exact modules

### Module A — cell inventory

Emit:

- defined-cell count;
- cell families;
- base-valued versus terminal-valued cells;
- output fiber sizes;
- predecessor delta.

### Module B — commutation

Enumerate exact ordered-pair locus and count.

### Module C — Association Spectrum

Enumerate base triples and classify `EQ/NEQ/LEFT/RIGHT/NONE`; assert checksum `(N+1)^3`.

### Module D — translation profiles

For each base element emit left/right translation fingerprints:

- domain set/size;
- output equality partition;
- base/terminal output counts;
- exact map when requested.

Check injectivity of the base-indexed translation families.

### Module E — active-sort definedness automorphisms

Construct

`D = {(x,y): star(x,y) is defined}`

on the active sort and test candidate permutations directly.

For small carriers, enumerate all active-sort permutations subject only to explicitly fixed/sorted metadata. Do not seed the search from the claimed answer group.

### Module F — full-operation automorphisms

For small cases enumerate compatible permutations of active elements and anonymous outputs and test

`g(star(x,y)) = star(gx,gy)`

for every defined cell together with preservation of undefinedness.

Optimization: first enumerate active-sort definedness automorphisms, then compute the induced permutation of value fibers. This is an algorithmic implementation of the Fiber-Transport theorem, but the finite test should derive the stabilizer from the actual fiber partition rather than a target formula.

### Module G — output orbits

From the enumerated full automorphism group compute:

- output orbits;
- active-element orbits;
- cell orbits;
- internally distinguished singleton orbits.

### Module H — erasure tests and VRI

Compute active-sort definedness group and projected full-operation carrier group. If finite and nested, compute the index directly from enumerated group orders.

### Module I — branch diff

Compare two machine passports field-by-field and emit only changed coordinates plus explicit zero deltas for the mandatory invariant set.

## 4. Regression matrix

Mandatory:

- `N=3,4,5,6` for every polynomial formula;
- preferred `N=3..10` for cheap spectrum/commutation checks;
- automorphism enumeration may use a smaller range where factorial search becomes expensive, but must include `N=3,4,5` and use structural pruning rather than formula substitution.

## 5. Benchmark acceptance tests

The implementation must reproduce:

1. M0 multiplication `Aut ~= S_{N-1}`;
2. G2 rigidity and spectrum;
3. G3-S/G3-C same spectrum but different commutation;
4. G3-A active-definedness group `C2 x C2` and full-operation rigidity;
5. G4-C active-definedness order `(N-1)!` by enumeration for small `N`;
6. G4-A active-definedness order `2(N-1)!` by enumeration for small `N`;
7. G4-C full-operation carrier group order `2` and G4-A order `1` for small `N`;
8. `N=3` G4-C VRI `1`.

## 6. Machine-readable output

Target a stable JSON-like schema with fields:

- `branch`;
- `N`;
- `status`;
- `cells`;
- `commutation`;
- `association_spectrum`;
- `translations`;
- `aut_full`;
- `aut_definedness_active`;
- `aut_definedness_full_one_sorted`;
- `output_orbits`;
- `vri`;
- `recoverability_notes`;
- `evidence`.

Every computed field should carry evidence provenance such as `ENUM`, while formulas imported from notes remain `WORKING`/`PROVED` until independently compared.

## 7. Immediate implementation priority

First implementation target is the audit gap in G4: independent enumeration of active-sort definedness and full-operation carrier automorphisms for G3/G4 small cases. Only after this passes should the lab automate translation profiles and generalized branch serialization.
