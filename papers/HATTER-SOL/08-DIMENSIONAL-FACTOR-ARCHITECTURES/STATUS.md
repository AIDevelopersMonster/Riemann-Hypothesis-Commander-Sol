# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED; repaired planar/3D theorem layer audited; RU/EN v0.9 PDF candidates assembled and visually QA-checked.**

## Audited theorem layer

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

For odd `q>=7`, the explicit outerplanar family is also planar and gives

\[
\boxed{
1\le\Delta_{planar}^{max}(2,q)
\le U_{Pl}(q)<q-2.
}
\]

## Proof-audit state

The obligations are closed and recorded in `PLANAR_PROOF_AUDIT.md`:

1. planar connectivity-recovery lemma rewritten at publication level;
2. four-incidence lemma rewritten as a local topological-disk argument;
3. repeated disjoint block reductions justified;
4. small cases and the exact threshold `q>=6` checked explicitly;
5. finite hostile-search regression support noted separately from proof.

## Retracted outerplanar claim

The attempted stronger outerplanar block-reduction theorem is **withdrawn**. A seven-vertex counterexample in `DIMENSIONAL_SEPARATION.md` shows that deleting three spokes and adding a missing edge may create a `K_{2,3}` subdivision. Therefore no universal stronger outerplanar suppression formula is currently claimed.

Safe outerplanar statements remain:

- the exact `q=3` value `Delta_outer^max(2,3)=1`;
- for odd `q>=3`, the explicit lower bound `Delta_outer^max(2,q)>=1`;
- the exact outerplanar extremal function for `q>3` is open.

## Literature audit state

`LITERATURE_AUDIT.md` records classical prior art on vertex splitting, constrained edge-splitting / splitting-off, planar edge splitting, plane-to-outerplane vertex splitting, and outerplanar degree realization.

No explicit equivalent was located for the HATTER-SOL planar free-boundary sensitivity bound under the arithmetic split `2q->(2,q)`. This remains a serious negative search, not an absolute priority guarantee.

## Illustration and PDF QA state

Canonical illustration folder:

`https://drive.google.com/drive/folders/1miJ-qqHMykpn_tQPfWCSKdowrQO5ct6g`

Illustrations `01.png`, `02.png`, `03.png`, and `05.png` passed publication use review as explanatory figures.

The originally generated `04.png` did **not** match the exact staircase values of

\[
U_{Pl}(q)=2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2)
\]

at several `q` values and is therefore **not approved for publication use**. A corrected programmatic figure `04_exact.png` was generated directly from the theorem formula and used in both v0.9 PDF candidates.

RU and EN publication candidates were rendered and visually inspected page-by-page:

- `HATTER-SOL-08_RU_v0.9_publication_candidate.pdf` — 12 pages;
- `HATTER-SOL-08_EN_v0.9_publication_candidate.pdf` — 12 pages.

No clipping, broken formulas, image overflow, or missing pages were found in the rendered QA pass.

## Manuscript state

Branch sources:

- `ARTICLE_RU_v0.8.md`
- `ARTICLE_EN_v0.8.md`
- `PLANAR_PROOF_AUDIT.md`
- `DIMENSIONAL_SEPARATION.md`
- `LITERATURE_AUDIT.md`
- `ILLUSTRATIONS.md`

Publication-layout v0.9 additionally incorporates:

- the HATTER-SOL-07 Zenodo citation `10.5281/zenodo.22724185`;
- verified DOI metadata for Jordán and Nagamochi–Eades;
- five figures, with Figure 5 rebuilt programmatically from the exact bound.

## Publication threshold

**Reached.**

HATTER-SOL-08 now contains a publication-ready mathematical core and visually QA-checked RU/EN PDF candidates.

## Next actions before Zenodo

1. decide final publication title/version (`v1.0` if no further theorem changes);
2. place the corrected `04_exact.png` and final RU/EN PDFs in the canonical Drive publication folder;
3. final metadata audit: author line, ORCID, DOI/date, bibliography, RU/EN consistency;
4. publish RU/EN package to Zenodo;
5. keep the outerplanar exact extremal problem open for a later paper rather than delaying HATTER-SOL-08.
