# Support-Cardinality Valuation Wall — version 1.1

**Title:** *Reflections on the Support-Cardinality Valuation Wall with Commander Sol: Finite Positive-Depth Perturbations versus Infinite Residual Graph Universality*  
**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Version:** 1.1 release candidate  
**Date:** 2026-08-28

Version 1.1 is a proof-complete revision of the published version 1.0.

Previous published version: **10.5281/zenodo.22135379**.  
Version 1.1 DOI: **pending assignment**.

## What changed

The mathematical claim boundary is unchanged. The revision expands the proof layer:

- every named theorem, lemma, and corollary now carries a proof;
- all displayed mathematical formulas are numbered consecutively **(1)–(68)** in both language versions;
- the open-adelic-image → arbitrary finite-depth residual-surjectivity step is written out;
- the finite graph interpretation is formalized with an explicit first-order bijection condition;
- both directions of the Trakhtenbrot reduction are proved;
- a proof-dependency map and a strict claim boundary are included;
- the notation `P_pos(kappa)` is used in publication binaries to avoid a known LibreOffice/OMML rendering defect affecting a subscript-plus glyph. This is only a typographic notation change from `P_+(kappa)`.

## Main theorem

For an arbitrary threshold profile `kappa:P->N_0`, put

`P_pos(kappa)={r in P : kappa(r)>=1}`.

Then:

- finite `P_pos(kappa)` gives parameter-free interdefinability with the zero-depth structure and finite GIR for every fixed parameter-free ternary isolator;
- infinite `P_pos(kappa)` gives one fixed isolator of infinite GIR, uniform finite directed graph coding, and undecidability of the complete first-order theory.

The exact parameter-free definability boundary is

`B_kappa in Def_pf(V_{Delta,0})` iff `P_pos(kappa)` is finite.

## Quality status

- Mathematical proof-completeness audit: **PASS**.
- Equation-number synchronization EN/RU: **PASS**, 68/68.
- DOCX visual QA: **PASS**, EN 15 pages, RU 16 pages.
- PDF render QA: **PASS**, EN 15 pages, RU 16 pages.
- DOI gate: **OPEN** — only version 1.1 DOI insertion and checksum regeneration remain after DOI assignment.

---

## Proof audit snapshot

Both EN and RU manuscripts contain **22 named results**. Every one is followed by a proof:

1. Lemma 2.1 — Local bridge identity.
2. Lemma 4.1 — Fixed-prime definability.
3. Lemma 5.1 — Local threshold translation.
4. Theorem 5.2 — Finite-support interdefinability.
5. Corollary 5.3 — Transfer of zero-depth compression.
6. Lemma 6.1 — Residual meaning of the incidence formula.
7. Lemma 7.1 — Full local factors outside a finite set.
8. Lemma 7.2 — Reduction at one local factor.
9. Theorem 7.3 — Arbitrary-depth finite residual independence.
10. Lemma 8.1 — Uniform matrix witnesses.
11. Theorem 9.1 — Finite pattern realization.
12. Theorem 10.1 — Infinite GIR on infinite positive support.
13. Lemma 11.1 — Graph realization.
14. Lemma 11.2 — Every admissible parameter tuple defines a finite graph.
15. Theorem 12.1 — Effective finite-model reduction.
16. Theorem 12.2 — Undecidability.
17. Corollary 12.3 — Noncomputable profiles are included.
18. Theorem 13.1 — Exact empty-parameter boundary.
19. Theorem 14.1 — Support-Cardinality Valuation Wall.
20. Corollary 15.1 — Every fixed positive depth is amplifying.
21. Corollary 15.2 — Arbitrarily sparse positive support still amplifies.
22. Corollary 15.3 — Unbounded positive depths create no further phase.

## External mathematical inputs

The following results are used as cited inputs and are not presented as new theorems of v1.1:

- the previously published Uniform Zero-Depth Compression theorem;
- Loeffler's adelic open-image theorem for non-CM modular forms;
- Chebotarev's density theorem;
- Trakhtenbrot's theorem on finite satisfiability.

The v1.1 manuscript proves the nontrivial specialization/reduction steps required to connect these inputs to the Support-Cardinality theorem.

## Adversarial points checked

- **Finite-support translation:** both directions are explicit and use only fixed scalar multiplication and parameter-free definitions of the finitely many exceptional primes.
- **Local reduction:** the proof of `SL_2(Z_r) -> SL_2(Z/r^k Z)` now uses invertibility of the reduction and the adjugate to justify existence of an r-adic-unit cofactor before determinant correction.
- **Open image -> independence:** the product-topology argument explicitly supplies full factors outside a finite set before reducing to arbitrary finite levels.
- **Chebotarev:** applied only to the finite Galois quotient cut out by the chosen finite residual levels; trace and determinant are conjugacy invariants.
- **Graph coding:** the forward and reverse total-unique matching conditions are first-order; no canonical GIR origin is assumed in the reverse direction.
- **Noncomputable profiles:** the effective sentence translation never queries `kappa`; profile values occur only in the metamathematical existence proof.
- **Definability boundary:** explicitly restricted to parameter-free definability.

## Formula audit

- EN displayed formulas: **68**.
- RU displayed formulas: **68**.
- Numbering range: **(1)–(68)** with no gaps.
- Every displayed formula has a number.
- Cross-references resolve to existing equation numbers.

## Publication verdict

The proof layer requested for version 1.1 is complete. The release remains DOI-gated: a new version-specific DOI has not yet been assigned.
