# Release Checklist — FCOA Nesting & Atomicity

## Mathematical freeze

- [x] Sandbox definition fixed.
- [x] Active/terminal typing rule fixed.
- [x] Bilateral `U`-atom definition fixed.
- [x] Factor relation uses the full nontrivial carrier `X\U`.
- [x] Sandbox monotonicity proved.
- [x] Atom => nesting-minimal proved.
- [x] Exact minimal-SCC criterion proved.
- [x] Well-founded factor-rank theorem stated with classical-source attribution.
- [x] `U`-irreducibility repaired to transport-irreducibility + coherence contract.
- [x] Pure erasure invariance proved.
- [x] Terminal value-fiber invariance proved under target-sort hypothesis.
- [x] Exact ordinary quotient witness criterion proved.
- [x] Fiberwise universal atom criterion proved under triviality reflection.
- [x] Counterexample: quotient destroys an atom by result-fiber contamination.
- [x] Counterexample: quotient creates an atom when triviality reflection fails.
- [x] Bounded factor-morphism well-foundedness theorem proved.
- [x] Exact factor-rank preservation under forth/back proved.
- [x] Atomicity preservation corollary proved.

## Prior-art / claim firewall

- [x] Partial algebra / strong congruence background cited.
- [x] Well-founded ordinal rank explicitly marked classical.
- [x] CPL identified with bounded-morphism back clause on the factor relation.
- [x] Transfer homomorphisms cited only as stronger factorization-lifting analogy.
- [x] No priority claim for SCCs, graph condensation, bounded morphisms, ordinal ranks, or partial-algebra quotients.
- [x] Classical primes presented only as one sandbox example.
- [x] Unique factorization explicitly excluded from the claim set.
- [x] G4 and neighboring branches excluded from the theorem dependencies.

## Bibliography

- [x] Grätzer — *Universal Algebra*.
- [x] Grätzer–Wenzel — partial-algebra congruence paper.
- [x] Blackburn–de Rijke–Venema — bounded morphisms.
- [x] Jech — well-founded ordinal rank background.
- [x] Geroldinger–Halter-Koch — transfer principles.
- [x] Upstream FCOA DOI `10.5281/zenodo.22129787`.

## Manuscript hygiene

- [x] Theorems numbered by section.
- [x] Display equations numbered where referenced.
- [x] Proofs supplied for every new theorem used in the main claim chain.
- [x] Counterexamples written explicitly.
- [x] Claim boundary included in abstract/introduction/conclusion.
- [x] AI research-assistant role described without listing an AI as a legal author identity.
- [ ] Final LaTeX compile.
- [ ] Resolve all compile warnings / undefined references.
- [ ] Visual PDF inspection page by page.
- [ ] Verify bibliography layout and DOI rendering.

## Metadata freeze before Zenodo

- [x] Author: Alex Malachevsky.
- [x] ORCID: `0009-0008-6009-3196`.
- [x] English title fixed at draft level.
- [x] Russian working title fixed at draft level.
- [ ] Final publication date.
- [ ] Version (`v1.0` recommended after render audit).
- [ ] New Zenodo DOI.
- [ ] Final licence choice / inherited repository licence check.
- [ ] Branch/tag/commit freeze recorded in release notes.

## Recommended Zenodo package

At final freeze include:

1. final PDF;
2. `manuscript.tex`;
3. `references.bib`;
4. optional source ZIP;
5. concise `README.md`;
6. publication audit / claim-boundary note if desired;
7. link to the GitHub branch or immutable release tag.

## Current gate

\[
\boxed{\texttt{PUBLICATION\_READY\_PENDING\_RENDER\_AUDIT}}
\]

No mathematical or claim-discipline blocker remains. The only remaining blocking gate is formal compilation/render verification plus final Zenodo metadata assignment.