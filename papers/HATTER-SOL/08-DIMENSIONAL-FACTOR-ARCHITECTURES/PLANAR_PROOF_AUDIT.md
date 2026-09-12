# HATTER-SOL-08 · Publication-level planar proof audit

**Date:** 2026-09-12  
**Scope:** planar connectivity recovery, four-block reduction, small-`q` thresholds, and separation statement.

## 1. Connectivity recovery for maximum-edge planar realizations

Let `c=(c_1,...,c_k)` with every `c_i>=2`. Consider all simple planar graphs on the labeled vertices with `deg(v_i)<=c_i`, not necessarily connected. Choose one with maximum edge count and, subject to that, minimum number of connected components.

We show it is connected.

If two distinct components contain unsaturated vertices `u,v`, place those components in disjoint disks and draw `uv` through the common exterior face. This preserves planarity and degree feasibility and increases the edge count, contradicting maximality. Hence at most one component contains an unsaturated vertex.

Every saturated nontrivial component has minimum degree at least two and therefore contains a cycle and a nonbridge edge.

Take a saturated component `C` and another component `D`.

### Case A: `D` contains an unsaturated vertex `z`

Choose a nonbridge edge `xy` of `C`. Re-embed `C` so a face incident to `xy` is the outer face, delete `xy`, and embed `D` with a face incident to `z` as outer. Draw `xz` through the exterior face.

- `C-xy` stays connected because `xy` was not a bridge;
- the number of edges is unchanged;
- `x` keeps its degree, `y` loses one, and `z` gains one while remaining within capacity;
- `C` and `D` merge into one component.

This contradicts minimality of the number of components.

### Case B: `D` is also saturated

Choose nonbridge edges `xy` in `C` and `uv` in `D`. Re-embed both components so these edges lie on their outer-face boundaries. Delete `xy` and `uv`, then place the two components disjointly in the plane and add `xu` and `yv` through the common exterior face, flipping one component if necessary so the two new arcs are noncrossing.

Degrees and edge count are preserved, both old components remain internally connected after deleting their nonbridge edges, and the two new edges merge them into one component. Again this contradicts minimality.

Thus a maximum-edge feasible planar graph can always be chosen connected.

### Lemma A

\[
\boxed{
\max\{|E(G)|:G\text{ planar},\deg(v_i)\le c_i\}
=
M_{Pl}(\mathbf c)
}
\]

when all `c_i>=2`, where `M_Pl` is defined with connectedness required.

This closes the connectivity-recovery obligation used in the planar refinement proof.

---

## 2. Publication-level four-incidence lemma

Let a plane graph `G` have a vertex `x`, and let four consecutive incidences around `x` go to distinct neighbors

\[
a,b,c,d.
\]

If every pair among `a,b,c,d` were adjacent, then `G` would contain `K_5` on `x,a,b,c,d`, impossible in a planar graph. Hence choose a nonadjacent pair `u,v` among the four.

Delete the four edges from `x` to this block.

Because the incidences are consecutive in the rotation at `x`, there is a closed topological disk `D` around the union of those four edge-arcs and a small neighborhood of `x` such that:

1. the interior of `D` meets no edge of the remaining graph;
2. `u` and `v` lie on the boundary-accessible ends of two deleted arcs inside `D`;
3. all surviving incidences at `x` leave outside the chosen sector.

Inside `D`, connect `u` to `v` by a simple arc following a thin neighborhood of the two deleted arcs and the now-empty neighborhood of `x`. This creates no crossing with the remaining drawing.

Since `uv` was chosen nonadjacent, the new graph remains simple.

At `u` and `v`, one deleted edge is replaced by one new edge, so their degrees do not increase; every other neighbor in the block loses one edge; `x` loses four incidences.

Hence the operation preserves simplicity, planarity, and all degree upper bounds while satisfying

\[
\Delta\deg(x)=-4,
\qquad
\Delta|E|=-3.
\]

For several disjoint consecutive four-blocks, choose pairwise disjoint local sectors. The operations commute topologically.

### Lemma B

To reduce the degree of `x` by `r>=0`, one can lose at most

\[
L_{Pl}(r)
=3\left\lfloor\frac r4\right\rfloor+(r\bmod4)
=\left\lceil\frac{3r}{4}\right\rceil
\]

edges while preserving planarity and all degree upper bounds.

---

## 3. Planar suppression theorem re-derived

For the split

\[
2q\to(2,q),\qquad q\ge3,
\]

let

\[
\delta=q-2.
\]

Take a maximum-edge connected feasible planar graph before refinement and let the capacity-`2q` vertex have degree `d`.

If `d<=q+2`, a local vertex split into contiguous incidence intervals of sizes at most `2` and `q` loses no edges.

If `d>q+2`, put

\[
r=d-(q+2)\le q-2=\delta.
\]

Lemma B reduces the degree to at most `q+2` at an edge loss of at most

\[
\left\lceil\frac{3r}{4}\right\rceil.
\]

Then perform the local planar vertex split. By Lemma A, connectedness can be restored without lowering the maximum feasible edge count.

Therefore

\[
M_{Pl}(\mathbf c')
\ge
M_{Pl}(\mathbf c)-\left\lceil\frac{3r}{4}\right\rceil.
\]

Since the total capacity decreases by `delta`, we get

\[
\boxed{
\lambda_{Pl}(\mathbf c')-\lambda_{Pl}(\mathbf c)
\le
-\delta+2\left\lceil\frac{3\delta}{4}\right\rceil.
}
\]

Equivalently,

\[
\boxed{
\Delta_{Pl}^{\max}(2,q)
\le
U_{Pl}(q)
:=2\left\lceil\frac{3(q-2)}4\right\rceil-(q-2).
}
\]

---

## 4. Small-`q` audit

Let `delta=q-2`.

- `q=3`: `delta=1`, `U_Pl=1`. The explicit outerplanar family attains `1`, so
  \[
  \Delta_{Pl}^{\max}(2,3)=1.
  \]
- `q=4`: `delta=2`, `U_Pl=2`; no strict planar/3D separation follows from this bound.
- `q=5`: `delta=3`, `U_Pl=3`; again no strict separation follows from this bound.
- `q=6`: `delta=4`, `U_Pl=2`; strict separation begins:
  \[
  \Delta_{Pl}^{\max}(2,6)\le2<4=\Delta_A^{\max}(2,6).
  \]
- `q=7`: `delta=5`, `U_Pl=3`, and the odd-`q` explicit family gives
  \[
  1\le\Delta_{Pl}^{\max}(2,7)\le3<5.
  \]

In general,

\[
U_{Pl}(q)<q-2
\iff
\left\lceil\frac{3(q-2)}4\right\rceil<q-2,
\]

which holds exactly for `q>=6`.

Asymptotically,

\[
U_{Pl}(q)=\frac{q-2}{2}+O(1).
\]

---

## 5. Hostile-search status

A finite regression search over connected planar graphs in the small graph atlas found no violation of the four-incidence operation. This is supporting evidence only and is not used in the proof.

The analogous hostile search for the attempted outerplanar three-block lemma found an explicit counterexample, so no stronger outerplanar suppression theorem is claimed.

## Audit conclusion

The planar theorem layer is publication-ready at the proof level, subject only to standard notation/bibliography editing. The outerplanar extremal function remains open except for the exact `q=3` point and the explicit positive lower-bound family for odd `q`.
