# Publication Audit — FCOA Nesting & Atomicity

**Date:** 2026-08-28  
**Document type:** technical research note / Commander Sol “Reflections” article  
**Current release status:** `PUBLICATION_READY_PENDING_RENDER_AUDIT`

## Declared claim ceiling

The manuscript claims only results about typed partial-composition sandboxes, the induced nontrivial factor relation, sandbox-relative atomicity, nesting-minimal SCCs, well-founded rank as applied to that relation, and quotient behavior.

It does not claim:

- unique factorization;
- universal existence of atomic factorizations;
- novelty of partial algebra, strong congruence, SCCs, ordinal rank, bounded morphisms, or transfer homomorphisms;
- automatic arithmetic meaning for FCOA carrier labels;
- any revision of the published M0-G1-G2 checkpoint;
- validation of G4 or any other neighboring branch.

## Mandatory audit table

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| A01 | C1 | early factor-graph definition | graph was initially restricted to active elements although signature may admit other nontrivial factors | could make `atom = indegree zero` false | use full nontrivial carrier `X\\U` for graph vertices | clarifies |
| A02 | C2 | first boundary theorem | global acyclicity was presented too close to a necessary condition | cycles above the minimal layer are harmless | replace by exact minimal-SCC criterion | narrows |
| A03 | C2 | `U`-irreducible terminology | arbitrary `U` was implicitly unit-like | imports monoid assumptions | use `U`-transport-irreducible; require explicit `U`-coherence before shorthand irreducible | narrows |
| A04 | C0 | quotient rank status | older theorem package still said rank preservation was open after a later theorem closed it | internal contradiction | publication manuscript uses the later bounded-morphism theorem as authoritative; old exploratory file is non-publication source | clarifies |
| A05 | C2 | CPL terminology | internal name could be read as a new general lifting concept | condition is standard bounded-morphism back clause on the factor relation | identify it explicitly with bounded/p-morphism prior art | narrows |
| A06 | C4 | partial algebra quotient background | ordinary/strong congruence distinction needed primary support | prevents rediscovery claim | cite Grätzer and Grätzer--Wenzel | none |
| A07 | C4 | ordinal rank | recursion theorem needed source support | standard result must be attributed | cite Jech | none |
| A08 | C4 | transfer analogy | factorization lifting comparison needed source support | avoids vague analogy | cite Geroldinger--Halter-Koch | none |
| A09 | C5 | publication metadata | new DOI not yet assigned | cannot freeze archival metadata prematurely | leave DOI explicitly unassigned until Zenodo deposit | none |
| A10 | C5 | final PDF | source has not yet undergone final compile/render inspection in this publication cycle | C5 gate remains | compile LaTeX, inspect equation breaks, references, fonts, page layout | none |

## Mathematical reread

### Sandbox monotonicity

**PASS.** Witness-set inclusion gives the atom inclusion directly. No associativity or closure assumption is used.

### Atom versus nesting boundary

**PASS after repair.** An indegree-zero vertex is necessarily an edge-free singleton SCC with no incoming condensation edge. Conversely, every edge-free singleton minimal SCC is an atom. Non-singleton minimal SCCs and singleton self-loops contain no atoms.

The exact statement is therefore the minimal-SCC theorem, not a global-DAG equivalence.

### Well-founded factor rank

**PASS.** Standard ordinal recursion applies to the factor relation when well-founded. Rank zero equals empty predecessor set and therefore atomhood by definition.

### `U`-coherence theorem

**PASS with explicit hypotheses.** The implication atom => transport-irreducible uses both clauses: two-`U` decompositions must be excluded and every one-`U` cofactor must remain in the result's `U`-transport class. The converse is immediate.

### Pure erasure

**PASS.** Since operation cells and `U` are literally unchanged, every witness set is unchanged. This also preserves isolation under the branch definition of isolation.

### Terminal value-fiber invariance

**PASS with target-sort hypothesis.** Recoloring only terminal-result cells cannot alter decomposition witnesses whose result is in the chosen atomicity target sort.

### Exact quotient witness criterion

**PASS.** It is a direct unpacking of existential-representative quotient semantics.

### Fiberwise universal criterion

**PASS with triviality reflection.** The equality `q^{-1}(q(U))=U` ensures quotient nontriviality is equivalent to source nontriviality. Atomhood of a quotient result class is then equivalent to atomhood of every source result representative in that class.

### Unsafe quotient counterexamples

**PASS.** Two distinct mechanisms are retained:

1. result-fiber contamination destroys an atomic representative;
2. failure of triviality reflection can create an atom by collapsing a source nontrivial factor into the quotient trivial class.

### Bounded factor morphism theorem

**PASS after prior-art repair.** The internal CPL clause is exactly the standard relational back clause once the factor relation is extracted. Together with forward preservation, it makes the quotient map a bounded morphism of factor frames.

If the quotient had an infinite descending chain, repeated back-lifting would produce one in the source. Exact rank preservation follows by well-founded induction using forth for the lower inequality and back for the upper inequality.

No necessity theorem is claimed.

## Bibliography audit

Verified publication anchors:

1. George Grätzer, *Universal Algebra*, 2nd ed., Springer, 1979, DOI `10.1007/978-0-387-77487-9`.
2. George Grätzer and G. H. Wenzel, “On the Concept of Congruence Relation in Partial Algebras,” *Mathematica Scandinavica* 20 (1967), 275–280.
3. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press, 2001, DOI `10.1017/CBO9781107050884`.
4. Thomas Jech, *Set Theory: The Third Millennium Edition, Revised and Expanded*, Springer, 2003, DOI `10.1007/3-540-44761-X`.
5. Alfred Geroldinger and Franz Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Chapman & Hall/CRC, 2006, DOI `10.1201/9781420003208`.
6. Alex Malachevsky, upstream FCOA publication, Zenodo DOI `10.5281/zenodo.22129787`.

`BIBLIOGRAPHY_VERIFIED = yes` for these entries.

## Metadata audit

- Author name: Alex Malachevsky — fixed.
- ORCID: `0009-0008-6009-3196` — fixed.
- Manuscript date: 2026 — fixed at draft level.
- New Zenodo DOI: not assigned — correctly omitted.
- Upstream DOI: `10.5281/zenodo.22129787` — fixed and cited only as previous FCOA work.
- Licence: inherit repository/publication choice at release; do not invent a new licence in the manuscript.

`METADATA_VERIFIED = partial` pending final Zenodo record and version/date freeze.

## Final audit block

- unresolved blocking mathematical issues: **none**
- unresolved claim-discipline issues: **none**
- equations/theorems changed: **yes**, hostile-audit repairs incorporated
- claim set changed: **yes — narrowed and clarified, not expanded**
- bibliography verified: **yes**
- metadata verified: **partial**
- source compiled: **not yet in this release cycle**
- PDF visually inspected: **not yet**
- release status: **`PUBLICATION_READY_PENDING_RENDER_AUDIT`**

The remaining gate is formal rather than mathematical: compile the final LaTeX source, inspect the rendered PDF, freeze metadata/version/date, then assign the Zenodo DOI.