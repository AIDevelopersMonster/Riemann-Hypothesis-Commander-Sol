# HATTER-SOL-08 · Dimensional separation for `2q -> (2,q)`

**Status:** audited theorem layer. The earlier outerplanar block-reduction claim is retracted; the planar suppression theorem survives.  
**Date:** 2026-09-12.

## 1. Setup

For a graph class `C` and capacity vector `c`, define

\[
M_C(\mathbf c)=\max\{|E(G)|:\;G\in C,\ G\text{ connected},\ \deg(v_i)\le c_i\},
\]

and

\[
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c).
\]

For the split

\[
2q\longrightarrow(2,q),\qquad q\ge3,
\]

write

\[
\delta=q-2.
\]

The unrestricted / 3D theorem of HATTER-SOL-07 gives

\[
\boxed{\Delta_A^{\max}(2,q)=q-2=\delta.}
\]

Strict 1D gives

\[
\boxed{\Delta_P^{\max}(2,q)=-q.}
\]

The HATTER-SOL-07 cactus/bouquet construction is outerplanar and, for odd `q>=3`, gives an explicit ambient family with

\[
\Delta_O=\Delta_{Pl}=\Delta_A=+1.
\]

Thus the same arithmetic split already reverses sign between strict 1D and every richer class.

---

## 2. Hostile audit: retraction of the first outerplanar block lemma

The first draft claimed that for three consecutive neighbors `a,b,c` of a vertex `x` in an outerplane embedding, deleting the three spokes `xa,xb,xc` and adding any missing edge among `a,b,c` could always be done while preserving outerplanarity.

That statement is false.

### Explicit counterexample

Take the graph on vertices `0,1,2,3,4,5,6` with edge set

\[
\{05,06,12,16,23,26,34,45,46,56\}.
\]

It has an outerplane embedding with boundary order

\[
6,1,2,3,4,5,0
\]

and the rotation of the neighbors of `x=6` contains the consecutive triple

\[
(1,0,5).
\]

Among this triple the edge `05` is present while `10` and `15` are absent.

Delete the three spokes

\[
61,60,65.
\]

If we add `10`, the resulting graph contains three internally vertex-disjoint `(2,4)` paths

\[
2-3-4,
\qquad
2-6-4,
\qquad
2-1-0-5-4,
\]

hence a subdivision of `K_{2,3}` and is not outerplanar.

If instead we add `15`, the same obstruction occurs via

\[
2-3-4,
\qquad
2-6-4,
\qquad
2-1-5-4.
\]

Therefore `K_4`-freeness alone does not guarantee that a missing chord created by the local reduction is outerplanar-admissible.

### Consequence

The previously stated outerplanar bound

\[
2\left\lceil\frac{2(q-2)}3\right\rceil-(q-2)
\]

and the derived claim

\[
\Delta_O^{\max}(2,5)=1
\]

are **withdrawn**. They are not part of the proved theorem layer.

The safe outerplanar statements currently remain:

\[
\Delta_O^{\max}(2,q)\le q-2,
\]

from the general class-preserving split bound, and for odd `q>=3`,

\[
\Delta_O^{\max}(2,q)\ge1,
\]

from the explicit cactus/bouquet family. For `q=3`, these meet and give the exact value `1`.

---

## 3. Planar four-block lemma

The planar case is different because a local planar disk, rather than outer-face incidence, is enough.

Let `G` be a plane graph and let `x` be a vertex. Take four consecutive incidences around `x`, with neighbors

\[
a,b,c,d.
\]

If every pair among `a,b,c,d` were adjacent, then together with `x` they would span a `K_5`, impossible in a planar graph. Hence at least one pair `u,v` among the four is nonadjacent.

Delete all four spokes from `x` to this consecutive block. The deleted spokes free a topological disk sector around `x`. Draw the new edge `uv` inside a sufficiently small neighborhood of the union of the deleted arcs `ux` and `xv`, staying inside that freed sector. Because the four incidences were consecutive, all remaining incidences of `x` lie outside the sector; because the original drawing was planar, the thin neighborhoods of the deleted arcs contain no other edges except at their endpoints.

Thus the new edge can be inserted without crossing.

At each endpoint `u,v`, one deleted spoke is replaced by the new edge, so no degree outside `x` exceeds its previous value.

Hence the operation has

\[
\Delta\deg(x)=-4,
\qquad
\Delta|E|=-3,
\]

and preserves planarity and all degree upper bounds.

### Lemma 3.1

A consecutive block of four incidences at a plane vertex can be removed and one missing edge inserted so that the degree of the center drops by four while the edge count drops by only three.

Repeated operations on disjoint consecutive incidence blocks are supported in disjoint local sectors and therefore commute topologically.

For a requested degree reduction `r`, partition the removed incidences into blocks of four and a remainder. This yields an edge loss at most

\[
L_{Pl}(r)
=3\left\lfloor\frac r4\right\rfloor+(r\bmod4)
=\left\lceil\frac{3r}{4}\right\rceil.
\]

---

## 4. Planar refinement suppression theorem

Take a maximum-edge feasible planar graph for the coarse capacity vector and let `x` be the capacity-`2q` vertex with degree

\[
d\le2q.
\]

If `d<=q+2`, split `x` locally into capacities `2` and `q` by cutting the cyclic order into two contiguous incidence intervals; no edge need be lost.

If `d>q+2`, set

\[
r=d-(q+2).
\]

Then

\[
0<r\le q-2=\delta.
\]

Use Lemma 3.1 to reduce the degree of `x` by `r`, at an edge cost of at most

\[
\left\lceil\frac{3r}{4}\right\rceil.
\]

Now split `x` into capacities `2` and `q` using contiguous incidence blocks.

The produced graph may be disconnected. The previously established planar connectivity-recovery lemma shows that for capacities at least two, the maximum feasible planar edge count is attained by a connected graph. Therefore

\[
M_{Pl}(\mathbf c')
\ge
M_{Pl}(\mathbf c)
-
\left\lceil\frac{3r}{4}\right\rceil.
\]

Since total capacity decreases by `delta=q-2`,

\[
\lambda_{Pl}(\mathbf c')-\lambda_{Pl}(\mathbf c)
\le
-\delta
+2\left\lceil\frac{3r}{4}\right\rceil
\le
-\delta
+2\left\lceil\frac{3\delta}{4}\right\rceil.
\]

### Theorem 4.1 — planar suppression

For every ambient capacity vector,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

For `q>=6`,

\[
\boxed{U_{Pl}(q)<q-2,}
\]

whereas HATTER-SOL-07 gives

\[
\Delta_A^{\max}(2,q)=q-2.
\]

Therefore:

### Corollary 4.2 — infinite planar/3D separation

For every `q>=6`,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
<
\Delta_A^{\max}(2,q).
}
\]

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1),
\]

so the planar worst-case inversion amplitude is at most approximately one half of the unrestricted / 3D sharp amplitude.

For every odd `q>=7`, the explicit outerplanar inversion family is also planar and supplies

\[
\boxed{
1\le\Delta_{Pl}^{\max}(2,q)
\le U_{Pl}(q)<q-2.
}
\]

Thus the planar class still admits genuine positive refinement inversion, but it cannot realize the unrestricted sharp amplitude on this infinite family.

---

## 5. Exact special case `6 -> 2*3`

For `q=3`, the general class-preserving one-step bound gives

\[
\Delta_O^{\max}(2,3),\Delta_{Pl}^{\max}(2,3)\le1.
\]

The explicit outerplanar family attains `+1`. Hence

\[
\boxed{
\Delta_O^{\max}(2,3)
=
\Delta_{Pl}^{\max}(2,3)
=
\Delta_A^{\max}(2,3)
=1.
}
\]

Strict 1D instead gives

\[
\boxed{\Delta_P^{\max}(2,3)=-3.}
\]

This remains the first exact sign-reversal point of the dimensional programme.

---

## 6. Audited dimension ladder

For the split `2q -> (2,q)`:

### strict 1D

\[
\boxed{\Delta_P^{\max}(2,q)=-q.}
\]

### outerplanar / circular

Safe bounds only:

\[
\boxed{
1\le\Delta_O^{\max}(2,q)\le q-2
\quad\text{for odd }q\ge3.
}
\]

Exact at `q=3`; otherwise open.

### planar 2D

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

For odd `q>=7`, the value is positive but strictly below `q-2`.

### unrestricted / 3D

\[
\boxed{\Delta_A^{\max}(2,q)=q-2.}
\]

The rigorously established dimensional phenomenon is therefore:

- strict 1D forces negative response;
- outerplanar and planar classes already permit positive response;
- planar geometry suppresses the worst possible amplitude by an asymptotic factor of at least two relative to unrestricted/3D;
- the exact outerplanar extremal function remains open.

---

## 7. Hostile computational check

A finite check over all connected planar graphs in the NetworkX graph atlas up to seven vertices found no violation of the planar four-block operation: for every tested plane rotation, deleting any four consecutive spokes and adding a missing edge among their endpoints preserved planarity.

This computation is **not** used as a proof; it is only regression support for Lemma 3.1.

The same style of finite hostile search is what exposed the outerplanar counterexample in Section 2.

---

## 8. Literature boundary

Classical ingredients, not novelty claims:

- planar graphs exclude `K_5`;
- outerplanar graphs exclude `K_4` and `K_{2,3}` minors;
- plane vertex splitting requires partitioning the cyclic order of incident edges into contiguous intervals;
- vertex splitting / detachment / splitting-off are classical operations;
- outerplanar and planar degree-realization problems have substantial prior literature.

Relevant references:

- A. Bar-Noy, T. Böhnlein, D. Peleg, Y. Ran, D. Rawitz, *Approximate realizations for outerplanaric degree sequences*, Journal of Computer and System Sciences 148 (2025), 103588, DOI `10.1016/j.jcss.2024.103588`.
- M. Gronemann, M. Nöllenburg, A. Villedieu, *Splitting Plane Graphs to Outerplanarity*, JGAA 28(3) (2024), 31–48, DOI `10.7155/jgaa.v28i3.2970`.

The candidate contribution remains narrower: **quantitative free-boundary response to the arithmetic split `2q -> (2,q)` across nested architecture classes**. The hostile audit also establishes a useful negative result: forbidden-clique counting alone is insufficient to transfer the planar local-reduction argument to outerplanarity.

---

## 9. Next proof obligations

1. Search for a correct outerplanar replacement theorem using induced-cycle / `K_{2,3}` structure rather than `K_4`-freeness alone.
2. Determine whether the planar upper bound `U_Pl(q)` is sharp on an infinite family.
3. Determine exact values for small planar `q>=4`.
4. Extend the audited planar argument from `2q -> (2,q)` to general `ab -> (a,b)`.
5. Keep the outerplanar problem open until a class-preserving local operation is actually proved.
