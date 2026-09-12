# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED; repaired planar/3D theorem layer audited; RU/EN v0.8 manuscripts assembled.**

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
=
\Delta_{planar}^{max}(2,3)
=
\Delta_{3D}^{max}(2,3)=1,
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

The following obligations are closed and recorded in `PLANAR_PROOF_AUDIT.md`:

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

`LITERATURE_AUDIT.md` now records classical prior art on:

- vertex splitting and detachment;
- constrained edge-splitting / splitting-off (Jordán);
- planar edge splitting (Nagamochi–Eades);
- plane-to-outerplane vertex splitting (Gronemann–Nöllenburg–Villedieu);
- outerplanar degree realization (Bar-Noy et al.).

No explicit equivalent was located for the HATTER-SOL planar free-boundary sensitivity bound under the arithmetic split `2q->(2,q)`. This is a serious negative search, not an absolute priority guarantee.

## Manuscript state

Assembled in this branch:

- `ARTICLE_RU_v0.8.md`
- `ARTICLE_EN_v0.8.md`
- `PLANAR_PROOF_AUDIT.md`
- `DIMENSIONAL_SEPARATION.md`
- `LITERATURE_AUDIT.md`

The RU and EN manuscripts are synchronized around the same audited theorem set. The retracted outerplanar formula does not appear as a theorem.

## Publication threshold

**Reached.**

HATTER-SOL-08 now contains a publication-ready mathematical core:

- exact 1D monotonicity;
- explicit dimension-dependent sign reversal;
- infinite-family strict planar-versus-3D separation;
- an audited negative result showing why the naive outerplanar analogue fails.

## Next actions before Zenodo

1. final RU/EN notation and bibliography audit;
2. add or design publication figures for the dimensional ladder and the four-block planar reduction;
3. produce native document/PDF candidates and perform visual QA;
4. assign final title/version and Zenodo metadata;
5. keep the outerplanar exact extremal problem open for a later paper rather than delaying HATTER-SOL-08.
