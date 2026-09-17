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
