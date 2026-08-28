# Publication Audit — FCOA Nesting & Atomicity

**Date:** 2026-08-28  
**Document type:** bilingual technical research note / Commander Sol “Reflections” article  
**Current release status:** `PUBLICATION_READY`

## Declared claim ceiling

The manuscript claims only results about typed partial-composition sandboxes, the induced nontrivial factor relation, sandbox-relative atomicity, nesting-minimal SCCs, well-founded rank as applied to that relation, and quotient behavior.

It does not claim unique factorization, universal existence of atomic factorizations, novelty of partial algebra/strong congruence/SCCs/ordinal rank/bounded morphisms/transfer homomorphisms, automatic arithmetic meaning for FCOA carrier labels, any revision of the published M0-G1-G2 checkpoint, or validation of neighboring G4 work.

## Resolved audit findings

| ID | Severity | Problem | Repair | Claim-set effect |
|---|---|---|---|---|
| A01 | C1 | factor graph initially too narrowly restricted | vertices use full nontrivial carrier `X\\U` | clarifies |
| A02 | C2 | global acyclicity stated too strongly | replaced by exact minimal-SCC criterion | narrows |
| A03 | C2 | `U`-irreducible implicitly unit-like | replaced by `U`-transport-irreducible + explicit `U`-coherence | narrows |
| A04 | C0 | old exploratory file said quotient rank preservation remained open | final publication uses later bounded-morphism theorem as authoritative | clarifies |
| A05 | C2 | CPL could look like a new general morphism concept | identified explicitly with standard bounded/p-morphism back clause | narrows |
| A06 | C4 | partial-algebra background needed support | Grätzer / Grätzer-Wenzel cited | none |
| A07 | C4 | ordinal rank needed attribution | Jech cited | none |
| A08 | C4 | transfer analogy needed support | Geroldinger-Halter-Koch cited | none |
| A09 | C5 | new DOI not assigned | DOI intentionally remains unassigned until Zenodo deposit | none |
| A10 | C5 | final render audit outstanding | both EN/RU PDFs compiled and visually inspected on 2026-08-28 | none |

## Mathematical reread

- **Sandbox monotonicity: PASS.** Witness-set inclusion gives atom inclusion directly.
- **Atom versus nesting boundary: PASS after repair.** The exact statement is the minimal-SCC theorem; global DAG is only a sufficient special case.
- **Well-founded factor rank: PASS.** Standard ordinal recursion applies and rank zero is exactly empty predecessor set.
- **`U`-coherence theorem: PASS with explicit hypotheses.** Both coherence clauses are used.
- **Pure erasure: PASS.** Operation cells and witness sets are literally unchanged.
- **Terminal value-fiber invariance: PASS with target-sort hypothesis.**
- **Exact quotient witness criterion: PASS.** Direct unpacking of existential representative semantics.
- **Fiberwise universal criterion: PASS with triviality reflection.**
- **Unsafe quotient counterexamples: PASS.** Result-fiber contamination and triviality collapse are distinct mechanisms.
- **Bounded factor morphism theorem: PASS after prior-art repair.** Forth gives one rank inequality; back gives the other by well-founded induction. No necessity theorem is claimed.

## Bibliography audit

Verified anchors:

1. George Grätzer, *Universal Algebra*, 2nd ed., Springer, 1979, DOI `10.1007/978-0-387-77487-9`.
2. George Grätzer and G. H. Wenzel, “On the Concept of Congruence Relation in Partial Algebras,” *Mathematica Scandinavica* 20 (1967), 275–280.
3. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press, 2001, DOI `10.1017/CBO9781107050884`.
4. Thomas Jech, *Set Theory: The Third Millennium Edition, Revised and Expanded*, Springer, 2003, DOI `10.1007/3-540-44761-X`.
5. Alfred Geroldinger and Franz Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Chapman & Hall/CRC, 2006, DOI `10.1201/9781420003208`.
6. Alex Malachevsky, upstream FCOA publication, Zenodo DOI `10.5281/zenodo.22129787`.

`BIBLIOGRAPHY_VERIFIED = yes`.

## Render audit

Final local publication build performed with XeLaTeX on 2026-08-28.

- English manuscript: 8 pages; openable; text PDF; no undefined references; no clipping observed in rendered inspection.
- Russian manuscript: 8 pages; Cyrillic and mathematical glyphs verified; no undefined references; the long minimal-SCC formula was explicitly reflowed and visually inspected.
- PDF preflight: both documents unencrypted, openable with PyMuPDF, non-scanned, no XFA.
- Representative pages inspected: title/abstract, central SCC theorem, bounded-morphism/rank theorem, final bibliography.

## Metadata audit

- Author: Alex Malachevsky — fixed.
- ORCID: `0009-0008-6009-3196` — fixed.
- Manuscript date: `2026-08-28` — fixed.
- New Zenodo DOI: **not assigned yet by design**; to be inserted only after deposit reservation/creation.
- Upstream DOI: `10.5281/zenodo.22129787` — fixed and cited as preceding FCOA work.
- Licence: use the repository/publication choice at deposit; no new licence is invented inside the manuscript.

## Final audit block

- unresolved blocking mathematical issues: **none**
- unresolved claim-discipline issues: **none**
- equations/theorems changed: **yes**, hostile-audit repairs incorporated
- claim set changed: **yes — narrowed and clarified, not expanded**
- bibliography verified: **yes**
- source compiled: **yes**
- PDF visually inspected: **yes**
- metadata verified: **yes except DOI field that is created by the deposit action itself**
- release status: **`PUBLICATION_READY`**

The scientific and rendering gates are closed. The next archival action is Zenodo deposit / DOI assignment, followed by insertion of that DOI into the repository publication metadata.