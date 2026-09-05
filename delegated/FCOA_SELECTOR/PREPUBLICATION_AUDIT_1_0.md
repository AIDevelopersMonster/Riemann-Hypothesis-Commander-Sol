# SOL-SELECTOR — Prepublication Audit 1.0

**Date:** 2026-09-05  
**Target:** `ARTICLE_EN_v1_0.md`, `ARTICLE_RU_v1_0.md`  
**Status:** PASS WITH MINOR PRODUCTION TASKS

## 1. Theorem dependency chain

PASS.

The article follows the dependency order:

1. admissible objects and weak morphisms;
2. category closure;
3. optional-domain obstruction and initiality of `M0`;
4. ordered free full completion `F_to`;
5. commutative quotient `F_mix`;
6. relation-only quotient `B0`;
7. weak root anchor `BR`;
8. kernel-factorization order;
9. pure event quotient geometry;
10. span/gap incomparability;
11. exact meet/join;
12. reflection constraints on anchors;
13. uniqueness of `BR` as base-line anchor;
14. missing-join theorem;
15. weak/strong bifurcation.

No theorem is used before its required structural layer is introduced.

## 2. Proof coverage

PASS.

Every publication-level theorem/proposition in the main chain is followed by a proof. No unproved conjecture is formatted as a theorem.

## 3. Numbering

PASS.

Section-based numbering is monotone. Displayed equations used as reference landmarks are numbered. The two language versions follow the same mathematical order.

## 4. Scope discipline

PASS.

Mandatory restrictions are present:

- preservation-only partial-algebra morphisms are background, not novelty;
- G-set/unary congruence lattices are background;
- complete-lattice infrastructure is not claimed as new;
- span/gap/phase are called canonically generated structural invariants;
- no uniform parameter-free FO definability claim is made;
- `B0 -> BR` is explicitly scoped to the weak category;
- strong definedness reflection and primitive output typing are identified as bifurcation axioms;
- uniqueness of `BR` is stated only among reflection-compatible **base-line** anchors of `B0`.

## 5. Novelty wording

PASS.

The article claims novelty only for the combined FCOA-specific package:

```math
M_0 -> F_to -> F_mix -> B0 -> BR,
```

plus the explicit span/gap quotient geometry and the transition from the pure invariant-partition lattice to a core-anchored quotient poset with missing joins.

## 6. Arithmetic firewall

PASS.

The article does not define span/gap by importing primitive integer addition/subtraction. Coordinate expressions `i+j`, `|i-j|`, and parity are explicitly described as representations of structurally generated invariants.

## 7. Weak quotient convention

PASS.

The text explicitly states that equivalent representative tuples need compatible outputs when both are defined, while definedness itself need not be constant over equivalence classes. This is sufficient for the one-step terminal-event quotient layer used in the paper.

## 8. Anchoring hazard

PASS.

The article does not silently assume that anchoring a terminal event to an operation-active old point preserves terminality. Instead it treats the extra target definedness as legal in the weak category and explains why strong definedness reflection would prohibit the map.

## 9. Bibliography

PASS FOR CONTENT / PRODUCTION CHECK REMAINS.

Included background references:

1. Hoefnagel–Jacqmin (2024), partial algebras and weak matrix properties, DOI 10.1007/s10485-024-09790-z;
2. Vernikov (1997), congruences of G-sets;
3. Seif (2013), congruence lattices of intransitive G-sets and flat M-sets;
4. Burmeister (1986), monograph on partial algebras.

Before Zenodo release, verify final publisher metadata/ISBN/page formatting for the Burmeister monograph and normalize journal title typography in BibTeX/LaTeX.

## 10. Author metadata

PASS.

English form:

`Malachevsky, A.A.`

Russian form:

`Малачевский А.А.`

ORCID:

`0009-0008-6009-3196`

No DOI has yet been assigned to SOL-SELECTOR and none is fabricated in the manuscript.

## 11. Language parity

PASS.

EN and RU versions contain the same theorem nucleus, the same scope restrictions, the same bibliography, and the same next-level re-entry boundary.

## 12. Remaining production tasks

The mathematics is publication-ready. Remaining tasks are mechanical:

1. produce final LaTeX source from the English master;
2. compile and visually inspect PDF;
3. produce/compile Russian LaTeX or retain RU Markdown/HTML companion as desired;
4. verify bibliography metadata one final time;
5. freeze release files and checksum manifest;
6. after Zenodo deposition, insert the assigned DOI into repository metadata and article front matter.

## 13. Final verdict

```math
\boxed{
\text{SOL-SELECTOR v1.0: MATHEMATICAL PREPUBLICATION AUDIT PASSED.}
}
```

The branch may proceed to LaTeX/PDF production and Zenodo release preparation without another research cycle at the one-step selector level.
