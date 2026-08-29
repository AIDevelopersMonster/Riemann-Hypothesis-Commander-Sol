# FCOA Passport Automation Plan — Archived

**Original version:** P0.1  
**Closure status:** **PARTIALLY IMPLEMENTED / DEFERRED**  
**Branch closed:** 2026-08-29

## 1. Historical objective

The planned tool was a dependency-light exact finite auditor that would take an explicitly defined partial operation and emit a reproducible structural passport plus a diff against a predecessor.

The tool was always evidence infrastructure, not a proof engine. Exhaustive finite checks support and attack formulas; they do not replace theorem proofs.

## 2. What was actually implemented

The branch delivered `passport_enumerator.py`, which independently computes for the G3/G4 benchmark family:

- active-sort definedness automorphisms;
- base permutations extendable to full-operation automorphisms;
- exact small-case group orders for `N=3,4,5,6`;
- finite VRI checks without substituting claimed closed forms.

It also enforced two central conventions:

- represent a partial operation by **defined cells only**;
- treat `UNDEF` as absence of a key, never as an operation value.

This implementation was sufficient to close the concrete verifier gap that motivated the lab.

## 3. Frozen target architecture

If a future tooling branch revives the general auditor, the intended modules remain:

### A — Cell inventory
- defined-cell count and families;
- base-valued versus terminal-valued cells;
- output fiber sizes;
- predecessor delta.

### B — Commutation
Enumerate the exact ordered-pair locus and count.

### C — Association Spectrum
Enumerate base triples and classify `EQ/NEQ/LEFT/RIGHT/NONE`; assert checksum `(N+1)^3`.

### D — Translation profiles
For each base element emit left/right domain and value-fiber fingerprints and compare them across branches.

### E — Active-sort definedness automorphisms
Construct

`D={(x,y): star(x,y) is defined}`

and test candidate permutations directly.

### F — Full-operation automorphisms
Test whether definedness automorphisms transport the actual value-fiber partition bijectively, keeping inherited/named values distinct from anonymous outputs.

### G — Output orbits
Compute active-element, output and cell orbits from the enumerated full group.

### H — Erasure tests and VRI
Compute active definedness symmetry, projected full-operation symmetry and their finite index where applicable.

### I — Branch diff
Compare machine passports field-by-field and emit changed coordinates plus explicit zero deltas.

## 4. Regression matrix retained

A revived implementation should continue to require:

- `N=3,4,5,6` for every polynomial formula;
- preferably `N=3..10` for inexpensive spectrum/commutation checks;
- automorphism enumeration on at least `N=3,4,5`, with structural pruning rather than formula substitution.

Benchmark acceptance cases remain M0/G2/G3/G4 as recorded in `BRANCH_DIFFS.md` and `ENUMERATION_REPORT_P1.md`.

## 5. Machine-readable schema — deferred

The planned stable JSON-like output included:

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

This general serialization was **not needed** to close the mathematical work and was therefore not completed.

## 6. Closure classification

The following are **DEFERRED / NON-BLOCKING**:

1. universal machine-readable passport serialization;
2. generalized Carrier-Erasure and Value-Erasure executables;
3. automatic diff generation for arbitrary future FCOA branches.

They are not defects in the closed branch. They are optional future infrastructure and should be started under a new tooling scope if needed.

## 7. Canonical mathematical successor

The mathematical discoveries that emerged from the audit branch were promoted and published separately:

Zenodo DOI `10.5281/zenodo.22160014`.

This archived plan must not be read as a list of outstanding requirements for that publication or for closure of this branch.
