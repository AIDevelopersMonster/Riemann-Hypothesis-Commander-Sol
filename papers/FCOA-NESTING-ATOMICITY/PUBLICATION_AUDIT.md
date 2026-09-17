# Publication Audit — FCOA Nesting & Atomicity

**Date:** 2026-08-28  
**Document type:** bilingual technical research note / Commander Sol “Reflections” article  
**Current release status:** `PUBLICATION_READY`

## Declared claim ceiling

The manuscript claims only results about typed partial-composition sandboxes, the induced nontrivial factor relation, sandbox-relative atomicity, nesting-minimal SCCs, well-founded rank as applied to that relation, and quotient behavior.

It does not claim unique factorization, universal existence of atomic factorizations, novelty of partial algebra/strong congruence/SCCs/ordinal rank/bounded morphisms/transfer homomorphisms, automatic arithmetic meaning for FCOA carrier labels, any revision of the published M0-G1-G2 checkpoint, or validation of neighboring G4 work.

## Resolved audit findings

| ID | Severity | Location | Problem | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|
| A01 | C1 | factor graph | graph initially too narrowly restricted | vertices use full nontrivial carrier `X\\U` | clarifies |
| A02 | C2 | nesting boundary | global acyclicity stated too strongly | replaced by exact minimal-SCC criterion | narrows |
| A03 | C2 | irreducibility terminology | `U` implicitly unit-like | `U`-transport-irreducible + explicit `U`-coherence | narrows |
| A04 | C0 | quotient-rank status | old exploratory source said preservation remained open | final bounded-morphism theorem is authoritative | clarifies |
| A05 | C2 | CPL terminology | could look like a new general morphism concept | identify with standard bounded/p-morphism back clause | narrows |
| A06 | C4 | partial-algebra background | source support required | Grätzer / Grätzer-Wenzel cited | none |
| A07 | C4 | ordinal rank | source support required | Jech cited | none |
| A08 | C4 | transfer analogy | source support required | Geroldinger-Halter-Koch cited | none |
| A09 | C5 | DOI | DOI was unavailable before deposit | Zenodo DOI assigned as `10.5281/zenodo.22140527` and inserted in archival metadata | none |
| A10 | C5 | final render | render audit initially outstanding | EN/RU PDFs compiled and visually inspected | none |
| A11 | C6 | §8 quotient convention | existential-representative semantics was stated in prose but not written as an explicit quotient-operation formula | add `bar omega(bar a,bar b)=bar z` iff a source witness exists; state result-class independence and explicitly retain existential domain semantics | none |
| A12 | C6 | §9 exact-rank proof | strongest proof was correct but compressed | write quotient-rank supremum explicitly; derive upper bound by back and lower bound by forth under the induction hypothesis | none |
| A13 | C5 | post-DOI archival build | DOI-bearing PDF had to be re-rendered and compared against the already audited pre-DOI v1.0 | recompile both manuscripts, preflight, render, and pixel-compare against pre-DOI v1.0 | none |

## Mathematical reread after supervisor repairs

- **Sandbox monotonicity: PASS.** Witness-set inclusion gives atom inclusion directly.
- **Atom versus nesting boundary: PASS.** Exact minimal-SCC criterion remains unchanged.
- **Well-founded factor rank: PASS.** Standard ordinal recursion applies; rank zero is exactly empty predecessor set.
- **`U`-coherence theorem: PASS.** Both coherence clauses remain explicit.
- **Pure erasure: PASS.** Operation cells and witness sets are literally unchanged.
- **Terminal value-fiber invariance: PASS with target-sort hypothesis.**
- **Quotient semantics: PASS after A11.** The manuscript explicitly fixes existential representative semantics. The compatibility/congruence hypothesis is used to make the result class independent of witnessing representatives; no total-definedness-across-all-representatives convention is silently imported.
- **Exact quotient witness criterion: PASS.** It is a literal unpacking of the displayed quotient convention.
- **Fiberwise universal criterion: PASS with triviality reflection.**
- **Unsafe quotient counterexamples: PASS.** Result-fiber contamination and triviality collapse remain distinct.
- **Bounded factor morphism theorem: PASS.** Forth/back are standard relational conditions; no novelty claim for them is made.
- **Exact rank preservation: PASS after A12.** The proof displays the quotient-rank supremum, derives `bar rho(q(x)) <= rho(x)` from back plus induction, derives `rho(x) <= bar rho(q(x))` from forth plus induction, and concludes equality. No theorem statement or assumption changed.

## Bibliography audit

Verified anchors:

1. George Grätzer, *Universal Algebra*, 2nd ed., Springer, 1979, DOI `10.1007/978-0-387-77487-9`.
2. George Grätzer and G. H. Wenzel, “On the Concept of Congruence Relation in Partial Algebras,” *Mathematica Scandinavica* 20 (1967), 275–280.
3. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press, 2001, DOI `10.1017/CBO9781107050884`.
4. Thomas Jech, *Set Theory: The Third Millennium Edition, Revised and Expanded*, Springer, 2003, DOI `10.1007/3-540-44761-X`.
5. Alfred Geroldinger and Franz Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Chapman & Hall/CRC, 2006, DOI `10.1201/9781420003208`.
6. Alex Malachevsky, upstream FCOA publication, Zenodo DOI `10.5281/zenodo.22129787`.

`BIBLIOGRAPHY_VERIFIED = yes`.

## Final v1.0 render audit

The final DOI-bearing archival build was performed with XeLaTeX on 2026-08-28.

- English v1.0: 8 pages; openable text PDF; no undefined references/citations; no overfull boxes; DOI printed on page 1.
- Russian v1.0: 9 pages; openable text PDF; Cyrillic and mathematical glyphs verified; no undefined references/citations; no overfull boxes; DOI printed on page 1.
- PDF preflight: both documents unencrypted, openable with PyMuPDF, non-scanned, no XFA.
- Representative pages inspected after DOI insertion: both first pages; §8 quotient semantics; §9 rank proof; final bibliography.
- Pixel comparison against the already audited pre-DOI v1.0 shows **only page 1 changed** in each language. Pages 2–8 EN and 2–9 RU are pixel-identical at the comparison resolution. Therefore the DOI insertion changed metadata/front matter only and did not modify the theorem/proof body.

## Metadata audit

- Author: Alex Malachevsky — fixed.
- ORCID: `0009-0008-6009-3196` — fixed.
- Publication date: `2026-08-28` — fixed.
- Version: `v1.0` — frozen.
- Zenodo DOI: **`10.5281/zenodo.22140527`** — assigned by deposit and recorded in the archival package.
- Upstream DOI: `10.5281/zenodo.22129787` — fixed and cited as preceding FCOA work.
- At finalization time, external search/resolver indexing of the newly assigned DOI had not yet propagated; no additional Zenodo metadata were inferred from that temporary absence.

## Final audit block

- unresolved blocking mathematical issues: **none**
- unresolved claim-discipline issues: **none**
- theorem statements changed by supervisor repairs: **no**
- proofs/exposition changed by supervisor repairs: **yes**
- claim set changed by supervisor repairs: **no**
- claim set changed by DOI insertion: **no**
- bibliography verified: **yes**
- metadata verified: **yes**
- source compiled: **yes**
- PDF visually inspected: **yes**
- archival DOI recorded: **yes — `10.5281/zenodo.22140527`**
- release status: **`PUBLICATION_READY`**

The v1.0 scientific, publication-hygiene, and archival gates are closed. DOI `10.5281/zenodo.22140527` is the frozen citation target for this version.