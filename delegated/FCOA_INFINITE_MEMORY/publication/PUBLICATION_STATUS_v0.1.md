# SOL-INFINITY Main Article — Publication Status

**Research phase:** CLOSED at the current theorem level.  
**Publication phase:** RELEASED.  
**Canonical Zenodo DOI:** [10.5281/zenodo.22151456](https://doi.org/10.5281/zenodo.22151456)  
**Release date:** 2026-08-29  
**Historical draft source:** `SOL_INFINITY_MAIN_EN_v0.1.tex`  
**Bibliography:** `sol_infinity_refs.bib`

> This file originated as the v0.1 pre-release audit. It is retained at the same path for branch continuity, but the status below reflects the completed Zenodo release. The frozen publication PDFs are not rebuilt merely to insert the DOI.

## Claim ceiling

The released article claims only the following package.

1. There exists a simple undirected graph on the payload carrier `N^2` which is:
   - symmetric;
   - irreflexive;
   - `C4`-free;
   - of atomic half-graph depth exactly `2`;
   - of linear primitive incidence cost in the natural max-shell order;
   - sufficient to FO-define a full order of type `omega` on all vertices.
2. Ordinary addition and multiplication in that recovered order are not FO-definable.
3. In the pure-order finite-dimensional provenance class, dimension `1` cannot combine the linear-cost primitive package with FO recovery of an `omega`-order; the explicit construction gives the matching dimension-`2` upper bound.
4. For any FO-definable `omega`-order on `N^d`, the definable one-coordinate diagonal spine occurs among the first `N` points with lower bound `Omega(N^(1/d))`; max-shell order attains `Theta(N^(1/d))`.
5. In dimension `2`, the exact diagonal-hub law is therefore `Theta(sqrt(N))`.

The publication does **not** claim:

- a classification of all finite-signature non-order sources;
- universal minimality of `Theta(N)` incidence over every provenance class;
- logarithmic lower bounds beyond fixed-dimensional pure-order interpretation;
- universal priority over every possible construction in the model-theory / sparse-graph literature.

## Mathematical audit

Cleared before release:

- graph construction and coordinate recovery;
- FO recovery of diagonal order;
- FO recovery of full max-shell `omega`-order;
- `C4`-free argument and atomic half-graph depth `2`;
- exact edge count on complete shell windows;
- parity pullback proof for nondefinability of ordinary addition;
- Robinson implication excluding ordinary multiplication;
- dimension-one quotient trivialization;
- pure-order binary tail dichotomy;
- bounded-degree form of the locality step used in the dimension-one barrier;
- finite-fibre box confinement;
- exact `N^(1/d)` diagonal-spine law.

## Source audit

Verified external anchors include:

- Galeotti--Lowe, *Order Types of Models of Fragments of Peano Arithmetic*, BSL 28(2), 2022, DOI `10.1017/bsl.2021.48`;
- Malliaris--Shelah, *Regularity Lemmas for Stable Graphs*, Trans. AMS 366(3), 2014, DOI `10.1090/S0002-9947-2013-05820-5`;
- Julia Robinson, *Definability and Decision Problems in Arithmetic*, JSL 14(2), 1949, DOI `10.2307/2266510`;
- Gajarsky et al., *First-Order Interpretations of Bounded Expansion Classes*, ICALP 2018, DOI `10.4230/LIPIcs.ICALP.2018.126`, as nearby structural-sparsity literature.

No exact predecessor of the complete theorem package was identified in the targeted related-work search. This is retained as a conservative literature statement, not as a universal priority claim.

## Release record

Canonical release metadata are recorded in:

`ZENODO_RELEASE_22151456.md`

Canonical DOI:

`10.5281/zenodo.22151456`

## Release status

`PUBLICATION_READY`

The research branch is closed at this theorem scope and the article is publicly released on Zenodo.