# HATTER-SOL-08 · Status

**Branch:** `research/hatter-sol-dimensional-factor-morphisms`  
**Path:** `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`  
**Status date:** 2026-09-12  
**Status:** **PUBLICATION THRESHOLD REACHED; hostile proof audit required before manuscript assembly.**

## Proven theorem layer

### 1. Exact 1D law

\[
\lambda_{1D}(\mathbf c)=\sum_i c_i-2(k-1),
\]

and for `ab->(a,b)`

\[
\boxed{
\lambda_{1D}(\mathbf c')-\lambda_{1D}(\mathbf c)
=-(ab-a-b+2)<0.
}
\]

Hence refinement inversion is impossible in strict 1D.

### 2. Complete-capacity dimensional staircase

For `c^(k)=(k-1,...,k-1)`:

\[
\lambda_{1D}=(k-1)(k-2),
\]

\[
\lambda_{outer}=(k-2)(k-3),
\]

\[
\lambda_{planar}=(k-3)(k-4),
\]

\[
\lambda_{3D}=0.
\]

This calibration family follows from classical extremal edge bounds and is not itself a novelty claim.

### 3. Class-preserving one-step bound

For `C in {outer, planar}`:

\[
\lambda_C(\ldots,a,b,\ldots)-\lambda_C(\ldots,ab,\ldots)
\le ab-a-b.
\]

### 4. Exact dimensional sign reversal

For odd `q>=3`, `m>=2q`, and

\[
(2q,2^m)\to(q,2^{m+1}),
\]

there are outerplanar realizations with

\[
\Delta_{outer}=\Delta_{planar}=\Delta_{3D}=+1,
\]

while strict 1D gives

\[
\Delta_{1D}=-q.
\]

For `q=3` this yields the exact special case

\[
\Delta_{outer}^{max}(2,3)
=\Delta_{planar}^{max}(2,3)
=\Delta_{3D}^{max}(2,3)=1.
\]

### 5. New dimensional suppression theorem for `2q -> (2,q)`

Let

\[
\delta=q-2.
\]

Using forbidden-clique block reduction at the split vertex, the current theorem layer gives

\[
\boxed{
\Delta_{outer}^{max}(2,q)
\le
U_O(q)
:=
2\left\lceil\frac{2(q-2)}{3}\right\rceil-(q-2).
}
\]

and

\[
\boxed{
\Delta_{planar}^{max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}{4}\right\rceil-(q-2).
}
\]

In contrast HATTER-SOL-07 gives the unrestricted / 3D exact value

\[
\boxed{
\Delta_{3D}^{max}(2,q)=q-2.
}
\]

Therefore:

- for every `q>=5`, outerplanar worst-case inversion is strictly smaller than the 3D/unrestricted value;
- for every `q>=6`, planar worst-case inversion is strictly smaller than the 3D/unrestricted value;
- asymptotically the upper-bound scales are approximately `q/3`, `q/2`, and `q` for outerplanar, planar, and unrestricted/3D classes.

This is the first infinite-family **dimensional suppression law** in the programme.

### 6. Exact new outerplanar value

For `q=5`, the explicit odd-`q` outerplanar inversion family gives the lower bound `1`, while the suppression theorem gives

\[
U_O(5)=1.
\]

Hence

\[
\boxed{
\Delta_{outer}^{max}(2,5)=1.
}
\]

while

\[
\boxed{
\Delta_{3D}^{max}(2,5)=3.
}
\]

Thus the split

\[
10\to2\cdot5
\]

has exact worst-case inversion amplitude `1` in the outerplanar class versus `3` in unrestricted/3D architecture.

See `DIMENSIONAL_SEPARATION.md` for the proof layer.

## Computational support

Exploratory MILP checks were used only as hostile-search support while forming the theorem. They are **not** part of the proof. In particular, circular-order MILP searches found outerplanar realizations consistent with the low-boundary constructions for tested `q=5,...,10` and did not supply any theorem claim by themselves.

## Prior-art boundary

Classical / not claimed as new:

- outerplanar edge bound `2n-3`;
- planar edge bound `3n-6`;
- Fary straight-line planarity;
- 3D straight-line graph drawings;
- vertex splitting / detachment / splitting-off;
- `K_4` exclusion in outerplanar graphs and `K_5` exclusion in planar graphs;
- outerplanar and planar degree-realization theory.

Candidate contribution:

> quantitative free-boundary sensitivity under the arithmetic split `ab -> (a,b)` across nested dimensional graph classes, including exact 1D monotonicity, sign reversal, and strict infinite-family suppression of the unrestricted sharp inversion amplitude.

## Mandatory proof-audit obligations before article assembly

1. Audit the local outerplanar block-reduction lemma in a fixed one-page embedding, especially the routing argument for the inserted missing chord after deleting three spokes.
2. Audit the planar four-neighbor block-reduction lemma inside the local disk around the split vertex.
3. Verify that repeated block reductions on disjoint consecutive incidence blocks commute without introducing crossings or parallel edges.
4. Re-audit the connectivity-recovery lemma for the outerplanar and planar capacity-constrained maxima.
5. Verify all ceiling identities and threshold claims (`q>=5`, `q>=6`).
6. Expand literature audit specifically for local splitting-off in outerplanar/planar classes and clique-exclusion based edge-preserving reductions.

No final PDF or Zenodo release until these six obligations are closed.

## Publication threshold

**Reached, conditionally on hostile audit.**

The branch now contains more than a research seed: it has an infinite-family strict separation theorem and an exact nontrivial outerplanar value `Delta_outer^max(2,5)=1` versus unrestricted value `3`. This is sufficient to begin publication assembly after the proof audit.
