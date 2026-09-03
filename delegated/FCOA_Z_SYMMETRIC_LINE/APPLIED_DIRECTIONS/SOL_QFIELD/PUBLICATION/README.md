# SOL-QFIELD publication package

**Status:** PUBLICATION PACKAGE QA-PASSED / DOI METADATA PENDING  
**Mathematical version:** 1.0  
**Manuscript date:** 2026-09-03

## Canonical authorship metadata

- **EN author:** Alex Malachevsky
- **RU author:** Алексей Малачевский
- **ORCID:** 0009-0008-6009-3196
- **AI collaboration:** Commander Sol / OpenAI GPT-5.6 Sol is disclosed as an AI research collaborator and is not part of the creator/author list for this release.

This follows the current repository convention in the root `README.md`: the human author is Alex Malachevsky, while Commander Sol is disclosed separately as an AI research collaborator; mathematical claims are attributed to the human author unless otherwise stated.

## Master manuscripts

- `PARIKH_COLLISIONS_FINITE_GROUP_HISTORIES_EN_v1_0.md` — English master article.
- `PARIKH_COLLISIONS_FINITE_GROUP_HISTORIES_RU_v1_0.md` — Russian companion article with matching theorem numbering.

The external publication bundle is generated from corrected release sources carrying the canonical author names above. The authorship change is metadata-only and does not modify the v1.0 mathematical content.

## Publication correction incorporated

The final manuscripts incorporate `SOL_QFIELD_PUBLICATION_AUDIT_v0_18.md`: FCOA root-comb endpoint reconvergence is exactly binary Parikh equivalence **at fixed history depth**. Across unequal depths, `L`-stutter produces additional reconvergences, so unrestricted carrier reconvergence is strictly coarser. The abstract finite-group theorems are unaffected.

## Robust headline theorem

For a monoid-surjective history morphism, Parikh collision is exactly the abelianization-fiber relation:

\[
g\sim_Pg'\iff g^{-1}g'\in[G,G].
\]

For finite `G`, the publication derives the complete-coset collision graph, the relative augmentation ideal

\[
J_P=I([G,G];G),
\]

the canonical collision tight frame with bound `|[G,G]|/2`, and the constructive witness bound

\[
B(h)\le |G|-1+2|G|(|[G,G]|-1)<2|G|^2.
\]

For `S3`:

\[
K_3\sqcup K_3,\qquad
J_P\cong M_2(\mathbb C),\qquad
S_P=\frac32I,\qquad
B_{S_3}^{universal}=5.
\]

## Claim discipline

The article does not claim priority for the Parikh/abelianization analogy, relative augmentation ideals, complete-graph tight frames, or standard `S3` representation theory. The literature search did not locate the exact combined formulation, which is recorded only as a negative bibliographic observation.

## Physical status

`QFT STATUS: ANALOGY ONLY`.

## QA completed

- EN DOCX: 13 pages, visually inspected.
- RU DOCX: 14 pages, visually inspected.
- DOCX accessibility audits: zero findings.
- EN/RU PDF preflight: PASS.
- LaTeX sources compile under XeLaTeX.
- `verify_parikh_collision_s3.py`: PASS on all 18 ordered noncommuting `S3` generator pairs.
- Release ZIP integrity manifest generated.

## Remaining release gate

Only Zenodo release metadata remains: reserve/assign the DOI, stamp the final DOI into release metadata if desired, publish to the Commander Sol Math community, and record the DOI back in GitHub. Mathematical content remains frozen at v1.0.