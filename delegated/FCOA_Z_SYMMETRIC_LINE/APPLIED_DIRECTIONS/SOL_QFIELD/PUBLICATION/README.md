# SOL-QFIELD publication package

**Status:** ARTICLE MANUSCRIPTS ASSEMBLED / PROOF-PUBLICATION AUDIT NEXT  
**Date:** 2026-09-03

## Master manuscripts

- `PARIKH_COLLISIONS_FINITE_GROUP_HISTORIES_EN_v1_0.md` — English master article.
- `PARIKH_COLLISIONS_FINITE_GROUP_HISTORIES_RU_v1_0.md` — Russian companion article with matching theorem numbering.

## Publication correction incorporated

The final manuscripts incorporate `SOL_QFIELD_PUBLICATION_AUDIT_v0_18.md`: FCOA root-comb endpoint reconvergence is exactly binary Parikh equivalence **at fixed history depth**. Across unequal depths, `L`-stutter produces additional reconvergences, so unrestricted carrier reconvergence is strictly coarser. The abstract finite-group theorems are unaffected.

## Robust headline theorem

For a monoid-surjective morphism `h : Sigma* -> G`,

\[
g\sim_Pg'\iff g^{-1}g'\in[G,G].
\]

For finite `G`:

\[
\Gamma_P=\coprod_{G/[G,G]}K_{|[G,G]|},
\]

\[
J_P=\ker\bigl(\mathbb C[G]\to\mathbb C[G_{ab}]\bigr)=I([G,G];G),
\]

\[
S_P=\frac{|[G,G]|}{2}I,
\]

and

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

## Publication claim discipline

The manuscripts do not claim priority for the Parikh/abelianization analogy, relative augmentation ideals, complete-graph tight frames, or standard `S3` representation theory. The publication claim is the proved collision correspondence and the combined graph/algebra/frame/effective-history package. The literature search did not locate the exact combined formulation, but this is stated only as a negative bibliographic observation.

## Physical status

`QFT STATUS: ANALOGY ONLY`.

The paper does not claim a derivation of fermions, spin, Fock space, physical CAR/CCR fields, or scattering theory.

## Supplement

- `../verify_parikh_collision_s3.py` — exhaustive sharp-depth certificate for the `S3` two-letter case.

## Next publication gate

Before release: independent line-by-line proof reread, bibliography/DOI audit, typeset build, metadata consistency check, and repository freeze.