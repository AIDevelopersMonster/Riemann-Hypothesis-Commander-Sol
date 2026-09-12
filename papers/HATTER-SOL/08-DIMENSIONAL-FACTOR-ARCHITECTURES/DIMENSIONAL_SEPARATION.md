# HATTER-SOL-08 · Dimensional separation for `2q -> (2,q)`

**Status:** proved theorem layer; publication-level candidate result.  
**Date:** 2026-09-12.

## 1. Setup

For a graph class `C` and a capacity vector `c`, define

\[
M_C(\mathbf c)=\max\{|E(G)|:\;G\in C,\ G\text{ connected},\ \deg(v_i)\le c_i\},
\]

and

\[
\lambda_C(\mathbf c)=\sum_i c_i-2M_C(\mathbf c).
\]

For the one-step split

\[
2q\longrightarrow(2,q),\qquad q\ge3,
\]

write

\[
\delta=q-2.
\]

The unrestricted / 3D theorem of HATTER-SOL-07 gives

\[
\Delta_A^{\max}(2,q)=q-2=\delta.
\]

The goal here is to show that outerplanar and planar architecture restrictions suppress this worst-case inversion by a factor bounded away from one.

---

## 2. Local block-reduction lemma: outerplanar case

Let `G` be an outerplanar graph and let `x` have degree `d`. Use a one-page (equivalently outerplane circular) embedding and cut the circular order at `x`, so the neighbors of `x` occur in a linear order

\[
y_1,\ldots,y_d.
\]

Consider three consecutive neighbors `a,b,c` in this order.

Because an outerplanar graph is `K_4`-free, the three edges

\[
ab,\quad bc,\quad ac
\]

cannot all be present: together with the spokes `xa,xb,xc` they would induce a `K_4` on `x,a,b,c`.

Choose one missing edge among the three.

- If `ab` is missing, delete `xa,xb,xc`, add `ab`.
- If `bc` is missing, delete `xa,xb,xc`, add `bc`.
- Otherwise `ab` and `bc` are present, hence `ac` is missing; delete `xa,xb,xc`, add `ac`.

In every case:

- the degree of `x` drops by `3`;
- the total edge count drops by only `2`;
- no degree outside `x` increases beyond its original value: the two endpoints of the new edge each lost their spoke to `x` first;
- outerplanarity is preserved.

For the last point, use the one-page order. The endpoints of the inserted edge lie inside one consecutive block of neighbors of `x`. Any pre-existing edge that crossed the inserted chord would already have crossed one of the deleted extreme spokes from `x`; edges from `x` to vertices inside the chosen block are deleted. Operations on disjoint consecutive blocks therefore remain noncrossing.

### Lemma 2.1

A consecutive block of three incidences at `x` can be removed while replacing one edge, so that

\[
\Delta\deg(x)=-3,
\qquad
\Delta|E|=-2,
\]

with outerplanarity and all other degree upper bounds preserved.

For a remainder of one or two incidences we simply delete them; hence reducing the degree of `x` by an arbitrary integer `r>=0` costs at most

\[
L_O(r)
=2\left\lfloor\frac r3\right\rfloor+(r\bmod3)
=\left\lceil\frac{2r}{3}\right\rceil
\]

edges.

---

## 3. Outerplanar refinement bound

Take a maximum-edge feasible outerplanar graph for the coarse capacity vector and let `x` be the vertex of capacity `2q`, with

\[
d=\deg(x)\le2q.
\]

If `d<=q+2`, split `x` directly into capacities `2` and `q` with no edge loss, assigning two consecutive incidences to the capacity-2 piece and the remaining incidences to the capacity-`q` piece.

If `d>q+2`, define

\[
r=d-(q+2).
\]

Then

\[
0<r\le q-2=\delta.
\]

Apply Lemma 2.1 to reduce the degree of `x` by `r`, losing at most

\[
\left\lceil\frac{2r}{3}\right\rceil
\]

edges. Now `x` has degree at most `q+2` and can be detached into adjacent vertices of capacities `2` and `q` without further edge loss. The detachment preserves a one-page embedding by assigning two extreme incidences to the capacity-2 piece and the remaining consecutive block to the capacity-`q` piece.

The intermediate graph need not be connected. As established in the HATTER-SOL-08 connectivity lemma, for capacities at least two the maximum feasible outerplanar edge count is attained by a connected graph. Therefore

\[
M_O(\mathbf c')
\ge
M_O(\mathbf c)
-
\left\lceil\frac{2r}{3}\right\rceil.
\]

The total capacity drops by `delta`, hence

\[
\lambda_O(\mathbf c')-\lambda_O(\mathbf c)
\le
-\delta
+2\left\lceil\frac{2r}{3}\right\rceil
\le
-\delta
+2\left\lceil\frac{2\delta}{3}\right\rceil.
\]

### Theorem 3.1 — outerplanar suppression bound

For every ambient capacity vector,

\[
\boxed{
\lambda_O(\ldots,2,q,\ldots)
-
\lambda_O(\ldots,2q,\ldots)
\le
U_O(q),
}
\]

where

\[
\boxed{
U_O(q)
:=
2\left\lceil\frac{2(q-2)}{3}\right\rceil-(q-2).
}
\]

Equivalently,

\[
\boxed{
\Delta_O^{\max}(2,q)
\le U_O(q).
}
\]

Since

\[
U_O(q)<q-2
\]

for every `q>=5`, we obtain a strict infinite-family separation from the unrestricted / 3D value.

### Corollary 3.2 — strict outerplanar/3D separation

For every `q>=5`,

\[
\boxed{
\Delta_O^{\max}(2,q)
<
\Delta_A^{\max}(2,q)=q-2.
}
\]

Asymptotically,

\[
U_O(q)=\frac{q-2}{3}+O(1),
\]

so the worst possible outerplanar inversion is at most roughly one third of the unrestricted sharp amplitude.

---

## 4. Exact case `10 -> 2*5`

For odd `q`, the explicit cactus/bouquet family from HATTER-SOL-07 is already outerplanar and gives

\[
\Delta_O^{\max}(2,q)\ge1.
\]

For `q=5`, `delta=3`, and Theorem 3.1 gives

\[
U_O(5)
=2\left\lceil\frac{6}{3}\right\rceil-3
=1.
\]

Therefore the lower and upper bounds meet.

### Corollary 4.1

\[
\boxed{
\Delta_O^{\max}(2,5)=1.
}
\]

But unrestricted / 3D sharpness is

\[
\Delta_A^{\max}(2,5)=3.
\]

Hence the split

\[
10\to2\cdot5
\]

already exhibits an exact threefold dimensional suppression of worst-case refinement inversion:

\[
\boxed{
1\quad\text{(outerplanar)}
\qquad\text{vs}\qquad
3\quad\text{(3D/unrestricted)}.
}
\]

---

## 5. Planar block-reduction lemma

The same argument works in the planar class with blocks of four consecutive incidences.

Let `a,b,c,d` be four consecutive neighbors of `x` in the rotation around `x`. If every pair among these four neighbors were adjacent, then together with `x` they would form a `K_5`, impossible in a planar graph. Hence at least one pair `u,v` among the four is nonadjacent.

Delete all four spokes from `x` to the block and add the missing edge `uv`. The inserted edge is routed through the local disk formerly occupied by those four spokes. Thus:

\[
\Delta\deg(x)=-4,
\qquad
\Delta|E|=-3,
\]

while planarity and all other degree upper bounds are preserved.

For an arbitrary degree reduction `r`, partition into blocks of four plus a remainder. The edge loss is at most

\[
L_{Pl}(r)
=3\left\lfloor\frac r4\right\rfloor+(r\bmod4)
=\left\lceil\frac{3r}{4}\right\rceil.
\]

### Theorem 5.1 — planar suppression bound

For every ambient capacity vector,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
U_{Pl}(q),
}
\]

where

\[
\boxed{
U_{Pl}(q)
:=
2\left\lceil\frac{3(q-2)}{4}\right\rceil-(q-2).
}
\]

For every `q>=6`,

\[
U_{Pl}(q)<q-2,
\]

and hence

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
<
\Delta_A^{\max}(2,q)=q-2.
}
\]

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1).
\]

Thus planarity allows more inversion than outerplanarity in the upper-bound scale, but still suppresses the unrestricted sharp amplitude by a factor asymptotically at least two.

---

## 6. Dimension ladder for the split `2q -> (2,q)`

The current rigorous picture is now:

### strict 1D

\[
\boxed{
\Delta_P^{\max}(2,q)=-q.
}
\]

Refinement always improves the 1D boundary; inversion is impossible.

### outerplanar / circular

\[
\boxed{
\Delta_O^{\max}(2,q)
\le
2\left\lceil\frac{2(q-2)}{3}\right\rceil-(q-2).
}
\]

For odd `q`, the explicit inversion family gives the lower bound `>=1`; for even `q`, the same family gives a zero-change realization after saturating the even hub and subdividing cycles, so `Delta_O^max(2,q)>=0`.

### planar 2D

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
2\left\lceil\frac{3(q-2)}{4}\right\rceil-(q-2).
}
\]

### unrestricted / 3D

\[
\boxed{
\Delta_A^{\max}(2,q)=q-2.
}
\]

The scale therefore changes from

\[
-q
\quad\longrightarrow\quad
O(q/3)
\quad\longrightarrow\quad
O(q/2)
\quad\longrightarrow\quad
q-2.
\]

This is the first genuine **dimensional suppression law** in the HATTER-SOL programme.

---

## 7. Literature boundary

The proof uses classical facts that are not novelty claims:

- outerplanar graphs are one-page embeddable and exclude `K_4` (indeed exclude `K_4` and `K_{2,3}` minors);
- planar graphs exclude `K_5`;
- vertex splitting / detachment and splitting-off are classical graph operations;
- outerplanar and planar degree-sequence realization have substantial prior literature and remain incompletely characterized in general.

Relevant modern degree-realization references include:

- A. Bar-Noy, T. Böhnlein, D. Peleg, Y. Ran, D. Rawitz, *On Key Parameters Affecting the Realizability of Degree Sequences*, MFCS 2024, DOI `10.4230/LIPIcs.MFCS.2024.1`.
- A. Bar-Noy, T. Böhnlein, D. Peleg, Y. Ran, D. Rawitz, *Approximate realizations for outerplanaric degree sequences*, Journal of Computer and System Sciences 148 (2025), 103588, DOI `10.1016/j.jcss.2024.103588`.
- M. Gronemann, M. Nöllenburg, A. Villedieu, *Splitting Plane Graphs to Outerplanarity*, JGAA 28(3) (2024), 31–48, DOI `10.7155/jgaa.v28i3.2970`.

The claim here is not that splitting itself is new. The candidate new statement is the **quantitative arithmetic-refinement sensitivity law across dimensional graph classes**, with the forbidden-clique size controlling how much of the HATTER-SOL-07 unrestricted inversion amplitude can survive.

---

## 8. Next proof obligations

1. Determine whether the outerplanar upper bound `U_O(q)` is sharp for infinitely many `q`.
2. Determine whether the planar upper bound `U_Pl(q)` is sharp for infinitely many `q`.
3. Close the exact outerplanar values for `q=4,6,7,...`.
4. Investigate the general split `ab -> (a,b)`: identify the correct local excess-degree parameter and whether clique-exclusion yields a comparable suppression law.
5. Abstract the block argument to classes with bounded clique number / bounded page number without overclaiming closure properties.
