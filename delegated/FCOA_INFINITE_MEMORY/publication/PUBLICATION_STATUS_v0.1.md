# SOL-INFINITY Main Article — Publication Status v0.1

**Research phase:** CLOSED at the current theorem level.  
**Publication phase:** ACTIVE.  
**Main manuscript:** `SOL_INFINITY_MAIN_EN_v0.1.tex`  
**Bibliography:** `sol_infinity_refs.bib`

## Claim ceiling

The main article claims only the following package.

1. There exists a simple undirected graph on the payload carrier `N^2` which is:
   - symmetric;
   - irreflexive;
   - `C4`-free;
   - of atomic half-graph depth exactly `2`;
   - of linear primitive incidence cost in the natural max-shell order;
   - sufficient to FO-define a full order of type `omega` on all vertices.
2. Ordinary addition and multiplication in that recovered order are not FO-definable.
3. In the pure-order finite-dimensional provenance class, dimension `1` cannot combine subquadratic primitive binary traces with FO recovery of an `omega`-order; the explicit construction gives the matching dimension-`2` upper bound for the linear-cost package.
4. For any FO-definable `omega`-order on `N^d`, the definable diagonal spine occurs among the first `N` points with lower bound `Omega(N^(1/d))`; max-shell order attains `Theta(N^(1/d))`.
5. In dimension `2`, the exact diagonal-hub law is therefore `Theta(sqrt(N))`.

The manuscript does **not** claim:

- a classification of all finite-signature non-order sources;
- universal minimality of `Theta(N)` incidence over every provenance class;
- logarithmic lower bounds beyond fixed-dimensional pure-order interpretation;
- priority over every construction in the model-theory / sparse-graph literature without further literature audit.

## Internal mathematical audit

### Cleared

- Graph construction and coordinate recovery.
- FO recovery of diagonal order.
- FO recovery of full max-shell `omega`-order.
- `C4`-free argument and atomic half-graph depth `2`.
- Exact edge count on complete shell windows.
- Parity pullback proof for nondefinability of ordinary addition.
- Robinson implication excluding ordinary multiplication.
- Dimension-one quotient trivialization.
- Pure-order binary linear/quadratic tail dichotomy.
- Finite-fibre box confinement.
- Exact `N^(1/d)` diagonal-spine law.

### Conservative repair queued for v0.2

The locality lemma in v0.1 is stated more generally than needed.  The dimension-one proof only requires the following narrower statement:

> after the order-tail dichotomy, all primitive binary relations have a **uniform bounded-distance tail**, hence the residual Gaifman graph has **uniformly bounded degree**; standard FO locality then prevents definition of a strict infinite order.

The v0.2 manuscript should state this bounded-degree version instead of the broader locally-finite formulation.

## Source audit

Verified external anchors:

- Galeotti--Löwe, *Order Types of Models of Fragments of Peano Arithmetic*, BSL 28(2), 2022, DOI `10.1017/bsl.2021.48`: contains a self-contained quantifier-elimination proof for the discrete order / successor theory used here.
- Malliaris--Shelah, *Regularity Lemmas for Stable Graphs*, Trans. AMS 366(3), 2014, DOI `10.1090/S0002-9947-2013-05820-5`: standard half-graph / instability connection.
- Julia Robinson, *Definability and Decision Problems in Arithmetic*, JSL 14(2), 1949, DOI `10.2307/2266510`: addition definable from multiplication plus successor on positive integers.
- Gajarsky et al., *First-Order Interpretations of Bounded Expansion Classes*, ICALP 2018, DOI `10.4230/LIPIcs.ICALP.2018.126`: nearby literature on first-order interpretations/transductions and structural sparsity; no exact match to the present theorem package was found in targeted searches.

The related-work search to date did **not** locate an exact predecessor combining all of:

`one simple C4-free graph + bounded atomic half-graph depth + linear incidence + FO full omega-order + exact dimension-one barrier + exact hub-density law`.

This is a targeted search result, not a universal priority claim.

## Publication audit findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| P1 | C1 | locality lemma | broader locally-finite statement than needed | invites an avoidable model-theoretic challenge | restrict to uniformly bounded-degree residual graph | narrows |
| P2 | C4 | related work | priority search not exhaustive | journal-level novelty statement would be premature | retain conservative wording; expand before journal submission | clarifies |
| P3 | C5 | manuscript | LaTeX not yet compiled/render-audited | cross-references/layout may contain defects | compile twice with BibTeX and visually inspect PDF | none |
| P4 | C5 | metadata | DOI/version/license not yet assigned | required for Zenodo release package | fill after final PDF freeze | none |

## Release status

`REVIEWABLE_DRAFT`

Research mathematics is publication-grade at the current claim ceiling, but the article is not yet release-ready until the v0.2 locality repair and final LaTeX/PDF render audit are complete.
