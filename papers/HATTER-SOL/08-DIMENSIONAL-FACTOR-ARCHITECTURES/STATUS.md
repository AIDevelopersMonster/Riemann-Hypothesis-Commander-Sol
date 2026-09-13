# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-13  
**Status:** **v1.0 FROZEN · PUBLICATION-READY · ZENODO DEPOSIT PENDING**

## Final audited theorem layer

### 1. Exact 1D law

For `c=(c_1,...,c_k)`, `c_i>=2`, strict 1D forces a path:

\[
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1).
\]

For `ab->(a,b)`:

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Hence refinement inversion is impossible in strict 1D.

### 2. Exact dimensional sign reversal

For odd `q>=3`, `m>=2q`, and

\[
(2q,2^m)\to(q,2^{m+1}),
\]

the explicit HATTER-SOL-07 constructions are outerplanar and give

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\]

while strict 1D gives

\[
\Delta_{1D}=-q.
\]

For `q=3`:

\[
\boxed{
\Delta_{outer}^{max}(2,3)
=\Delta_{planar}^{max}(2,3)
=\Delta_{3D}^{max}(2,3)=1,
}
\]

and

\[
\boxed{\Delta_{1D}^{max}(2,3)=-3.}
\]

### 3. Audited planar suppression theorem

For the split

\[
2q\to(2,q),
\]

we have

\[
\boxed{
\Delta_{planar}^{max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

HATTER-SOL-07 gives the unrestricted / 3D exact value

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
U_{Pl}(q)=\frac{q-2}{2}+O(1).
\]

Thus planar architecture suppresses worst-case refinement inversion by an asymptotic factor of at least two relative to unrestricted/3D architecture.

## Hostile-audit correction retained

The attempted stronger outerplanar suppression theorem remains **withdrawn**. The seven-vertex counterexample in `DIMENSIONAL_SEPARATION.md` shows that deleting three spokes and adding a missing edge may create a `K_{2,3}` subdivision.

Safe outerplanar statements:

- exact `q=3` value `Delta_outer^max(2,3)=1`;
- for odd `q>=3`, explicit lower bound `Delta_outer^max(2,q)>=1`;
- exact outerplanar extremal function for `q>3` remains open.

## Proof and literature audit

Closed and recorded in `PLANAR_PROOF_AUDIT.md` / `LITERATURE_AUDIT.md`:

- planar connectivity recovery;
- four-incidence local topological-disk reduction;
- repeated-block justification;
- threshold `q>=6` and small cases;
- targeted prior-art search on vertex splitting, splitting-off, planar edge splitting, plane-to-outerplane splitting, and degree realization.

Bibliographic metadata was rechecked before v1.0. In particular, the Nagamochi–Eades entry now includes DOI `10.1023/A:1024470929537`.

## Final v1.0 artifacts

GitHub source:

- `ARTICLE_RU_v1.0.md`
- `ARTICLE_EN_v1.0.md`
- `ZENODO_METADATA_v1.0.md`

Final PDFs, each 12 pages and visually QA-checked:

- `HATTER-SOL-08_RU_v1.0.pdf`
- `HATTER-SOL-08_EN_v1.0.pdf`

Canonical five-figure set:

- `01.png` — dimensional ladder;
- `02.png` — sign reversal `6 -> 2 x 3`;
- `03.png` — planar four-block reduction;
- `04.png` — corrected exact planar/3D separation graph;
- `05.png` — complete-capacity dimensional staircase.

Publication Drive folder:

`https://drive.google.com/drive/folders/1ZnhcoqblWKr3mxioQ2zsza74cUU2ATCL`

It contains both v1.0 PDFs, `ZENODO_METADATA_HATTER-SOL-08_v1.0.md`, `SHA256SUMS_HATTER-SOL-08_v1.0.txt`, and `HATTER-SOL-08_v1.0_source-and-figures.zip`.

## Metadata freeze

- Author RU: **Малачевский А.А.**
- Author EN/Zenodo: **Malachevsky, A.A.**
- ORCID: `0009-0008-6009-3196`
- Version: `1.0`
- Publication date: `2026-09-13`
- Parent DOI: `10.5281/zenodo.22724185`
- HATTER-SOL-08 DOI: **pending Zenodo deposit**

## Next action

Publish the frozen v1.0 package to Zenodo. After Zenodo assigns the DOI, update `README.md`, this status file, and cross-link HATTER-SOL-07. No theorem/content change is planned before deposit.
