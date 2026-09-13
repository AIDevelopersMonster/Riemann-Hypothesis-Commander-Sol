# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 26

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total projection. This note closes the first host size left open by `PLANAR_65_TERMINAL_TAIL_16_24.md`.

The key point is that at order `26` a 5-regular planar support needs exactly seven added edges to become a triangulation. Seven is the first value above the automatic `Delta(F)<=6` range, but the only bad seven-edge configuration is a star, and a local face re-triangulation destroys that star.

---

## 1. External existence input

We use one classical existence fact.

Hasheminezhad, McKay and Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations* (JGAA 15(3), 2011), enumerate connected simple planar 5-regular graphs by order and connectivity. At order `26` their table contains, in particular, 5-connected examples.

Fix one such 5-connected plane graph and call it

\[
H_{26}.
\]

Then

\[
|V(H_{26})|=26,
\qquad
|E(H_{26})|=65.
\]

Because the graph is 5-connected, every face boundary is a simple cycle.

A maximal planar graph on the same vertex set has

\[
3\cdot26-6=72
\]

edges. Therefore any face-by-face triangulation of `H_26` adds exactly

\[
\boxed{72-65=7}
\]

edges.

---

## 2. Seven-diagonal star-escape lemma

### Lemma T11.60 — seven-edge triangulation augmentation can avoid degree seven

Let `H` be a 3-connected simple plane graph whose faces can be triangulated by adding exactly seven edges in total. Then there exists a triangulation `T` of `H` on the same vertex set such that the added-edge graph

\[
F:=E(T)\setminus E(H)
\]

satisfies

\[
\boxed{|F|=7,
\qquad
\Delta(F)\le6.}
\]

### Proof

Start with any face-by-face triangulation. If `Delta(F)<=6`, there is nothing to prove.

Assume instead

\[
\Delta(F)=7.
\]

Since `F` has exactly seven simple edges, all seven must be incident with one vertex `x`. Thus `F` is a seven-edge star centered at `x`.

Every nontriangular face of `H` must contain `x`: otherwise that face contributes at least one triangulation diagonal not incident with `x`, contradicting the star assumption.

Let a nontriangular face `C` require

\[
k(C)=|C|-3
\]

diagonals.

### Case A: at least two nontriangular faces

Then every such face satisfies

\[
1\le k(C)\le6
\]

because the total over all nontriangular faces is seven.

Choose one such face `C`. On its boundary, let `y` be a neighbor of `x`. Re-triangulate `C` by a fan centered at `y`.

Because `xy` is already a boundary edge of `H`, none of the new diagonals of this fan is incident with `x`. The new fan contributes exactly `k(C)` added edges at `y`, hence at most six.

Outside `C`, the vertex `x` keeps only

\[
7-k(C)\le6
\]

added incidences. Before the re-triangulation every added edge was incident with `x`, and `xy` is an original edge, so `y` had no added incidence outside `C`. All other vertices receive at most one fan diagonal from `C`.

Thus the modified added-edge graph has maximum degree at most six.

### Case B: exactly one nontriangular face

Then that face requires all seven diagonals, so it is a decagon.

Triangulate the decagon by a zig-zag triangulation whose diagonal graph is a path. In particular every boundary vertex is incident with at most two added diagonals.

Hence

\[
\Delta(F)\le2<6.
\]

This closes both cases. QED.

---

## 3. The `B_O=0` endpoint at order 26

Apply T11.60 to `H_26`. We obtain a triangulation `T_26` with added-edge graph `F` satisfying

\[
|F|=7,
\qquad
\Delta(F)\le6.
\]

For the state

\[
\Xi=(6,5),
\]

color every edge of `H_26` by the capacity-five channel and every edge of `F` by the capacity-six channel.

Both channel constraints are respected:

\[
\Delta(H_{26})=5,
\qquad
\Delta(F)\le6.
\]

All triangulation edges are used, so the boundary is

\[
B_O
=5\cdot26-2\cdot65
=0,
\]

and

\[
B_A
=6\cdot26-2\cdot7
=142.
\]

Thus

\[
\boxed{(142,0)}
\]

is attainable.

Equivalently, since `5n+12=142`, the terminal `B_O=0` point lies on the universal minimum-total line.

---

## 4. The `B_O=2` endpoint at order 26

Let

\[
S:=\{v:d_F(v)=6\}.
\]

Since `F` has seven edges,

\[
\sum_v d_F(v)=14,
\]

so

\[
\boxed{|S|\le2.}
\]

The 5-regular graph `H_26` has `65` edges. At most

\[
5|S|\le10
\]

of them are incident with `S`. Therefore there exists an edge

\[
e\in E(H_{26})
\]

whose two endpoints lie outside `S`.

Recolor `e` from the capacity-five channel to the capacity-six channel.

Then

\[
\Delta(F\cup\{e\})\le6
\]

because both endpoints of `e` had `F`-degree at most five, while

\[
\Delta(H_{26}-e)\le5.
\]

Hence the recolored network is feasible and has

\[
B_O=2,
\qquad
B_A=140.
\]

So the second terminal point is

\[
\boxed{(140,2).}
\]

### Theorem T11.61 — terminal-pair closure at order 26

For the planar orbit-total state `(6,5)` on `26` vertices, both terminal minimum-total points

\[
\boxed{(140,2),
\qquad
(142,0)}
\]

are attainable.

---

## 5. Exact full order-26 Pareto front

The universal planar inequalities for `(6,5)` are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5n+12.
\]

At `n=26`, the minimum-total line is

\[
B_A+B_O=142.
\]

T11.57 in `PLANAR_65_TERMINAL_TAIL_16_24.md` applies to every even `n>=16` and supplies every parity-compatible point on this line with

\[
B_O\ge4.
\]

T11.61 supplies the two missing levels `B_O=2,0`.

Therefore every allowed even lattice point on the minimum-total line is attained.

### Theorem T11.62 — exact planar `(6,5)` front at order 26

\[
\boxed{
\mathcal R^\Xi_{Pl,26}(6,5)
=
\{(12+2t,130-2t):0\le t\le65\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,26}(6,5;X,Y)
=
\sum_{t=0}^{65}X^{12+2t}Y^{130-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by one of these points, so no additional Pareto point exists. QED.

---

## 6. Updated exact range

Combining T11.56, T11.59 and T11.62, the full planar `(6,5)` Pareto front is now exact for every even host size

\[
\boxed{4\le n\le26.}
\]

The next unsolved order is

\[
\boxed{n=28.}
\]

There the triangulation complement of a 5-regular support has eight edges. The new hostile target is to prove that an eight-edge face-triangulation complement can always be chosen with maximum degree at most six, or to exhibit a genuine order-28 obstruction.

The seven-edge case shows that mere concentration around one vertex is not an obstruction: a local re-triangulation removes the star.