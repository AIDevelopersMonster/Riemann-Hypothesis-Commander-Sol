# HATTER-SOL-08 · Dimensional Factor Architectures

**Final title:** *From a Line to Space: Dimensional Suppression of Factor-Architecture Sensitivity*  
**Series:** HATTER-SOL · Arithmetic Tea Party  
**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Version:** `v1.0`  
**Publication date:** `2026-09-13`  
**Status:** **FROZEN FOR ZENODO DEPOSIT**  
**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** `0009-0008-6009-3196`  
**Parent work:** HATTER-SOL-07 — https://doi.org/10.5281/zenodo.22724185  
**HATTER-SOL-08 DOI:** pending Zenodo deposit

## Main result

HATTER-SOL-08 asks how the free-boundary response to arithmetic refinement changes when factor-capacity networks are restricted to increasingly rich architecture classes:

\[
\text{strict 1D}
\subset
\text{outerplanar}
\subset
\text{planar 2D}
\subset
\text{unrestricted / 3D}.
\]

For a capacity vector `c` and graph class `C`,

\[
M_C(\mathbf c)
=
\max\{|E(G)|:G\in C,\ G\text{ connected},\ \deg(v_i)\le c_i\},
\]

\[
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c).
\]

### Exact 1D law

For `ab -> (a,b)`,

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

So refinement inversion is impossible in strict 1D.

### Architecture-dependent sign reversal

For odd `q>=3`, the explicit family

\[
(2q,2^m)\to(q,2^{m+1})
\]

has

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\qquad
\Delta_{1D}=-q.
\]

Thus the same arithmetic refinement changes sign purely because the admissible architecture class changes.

### Planar suppression theorem

For

\[
2q\to(2,q),
\]

\[
\boxed{
\Delta_{planar}^{max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

The unrestricted / 3D result inherited from HATTER-SOL-07 is

\[
\boxed{
\Delta_{3D}^{max}(2,q)=q-2.
}
\]

Hence for every `q>=6`,

\[
\boxed{
\Delta_{planar}^{max}(2,q)
<
\Delta_{3D}^{max}(2,q).
}
\]

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1),
\]

so planar geometry suppresses worst-case refinement inversion by an asymptotic factor of at least two relative to unrestricted/3D architecture.

## Hostile-audit correction

An attempted stronger outerplanar theorem was rejected after hostile audit. A seven-vertex counterexample shows that the naive three-spoke reduction can create a `K_{2,3}` subdivision. The withdrawn outerplanar formula is not part of v1.0.

This leaves the exact outerplanar extremal function for `q>3` as an explicit open problem.

## Final publication package

GitHub sources:

- `ARTICLE_EN_v1.0.md`
- `ARTICLE_RU_v1.0.md`
- `ZENODO_METADATA_v1.0.md`
- `PLANAR_PROOF_AUDIT.md`
- `DIMENSIONAL_SEPARATION.md`
- `LITERATURE_AUDIT.md`

Publication Drive folder:

https://drive.google.com/drive/folders/1ZnhcoqblWKr3mxioQ2zsza74cUU2ATCL

Contents include:

- `HATTER-SOL-08_EN_v1.0.pdf` — 12 pages;
- `HATTER-SOL-08_RU_v1.0.pdf` — 12 pages;
- `ZENODO_METADATA_HATTER-SOL-08_v1.0.md`;
- `SHA256SUMS_HATTER-SOL-08_v1.0.txt`;
- `HATTER-SOL-08_v1.0_source-and-figures.zip`.

Both PDFs passed final visual QA after the exact separation graph was rebuilt directly from the theorem formula. The canonical corrected graph is `04.png`.

## Bibliographic note

The final bibliography includes:

- HATTER-SOL-07: DOI `10.5281/zenodo.22724185`;
- Jordán: DOI `10.1137/S0895480199364483`;
- Nagamochi–Eades: DOI `10.1023/A:1024470929537`;
- Gronemann–Nöllenburg–Villedieu: DOI `10.7155/jgaa.v28i3.2970`;
- Bar-Noy et al.: DOI `10.1016/j.jcss.2024.103588`;
- Korte–Vygen: DOI `10.1007/978-3-662-56039-6`.

## Deposit discipline

No theorem/content change is planned before Zenodo deposit. After Zenodo assigns the HATTER-SOL-08 DOI, update this README, `STATUS.md`, and the HATTER-SOL-07 cross-link.
