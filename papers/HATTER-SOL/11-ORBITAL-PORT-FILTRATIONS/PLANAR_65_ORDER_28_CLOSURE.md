# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 28

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total two-channel projection. This note concerns only the `Xi` response model.

The previous note closed the exact `(6,5)` front through order `26`. At order `28`, a 5-regular planar support needs exactly eight additional edges to become a triangulation. The only new issue is to show that the eight-edge triangulation complement can be chosen with maximum degree at most six.

---

## 1. External existence input

Hasheminezhad, McKay and Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations* (JGAA 15(3), 2011), Table 1, list connected simple planar 5-regular graphs of order `28` in every connectivity class from `1` through `5`, including `2954` examples of vertex-connectivity `5`.

Fix one 5-connected plane 5-regular graph and call it

\[
H_{28}.
\]

Then

\[
|V(H_{28})|=28,
\qquad
|E(H_{28})|=70.
\]

A triangulation on the same vertex set has

\[
3\cdot28-6=78
\]

edges, so a face-by-face triangulation of `H_28` adds exactly

\[
\boxed{8}
\]

edges.

Because `H_28` is 5-connected, in particular it is 3-connected; hence every face boundary is a simple cycle and distinct faces meet properly.

---

## 2. A local ear-off triangulation lemma

We need a local operation that removes all added incidences from a chosen boundary vertex without creating a new high-degree concentration.

### Lemma T11.63 — ear-off retriangulation of a polygon

Let `C` be a polygonal face of length at least four and let `x` be one of its boundary vertices. Then `C` admits a triangulation with the following properties:

1. no added diagonal is incident with `x`;
2. every other boundary vertex is incident with at most three added diagonals.

### Proof

Let `y,z` be the two neighbors of `x` on the boundary of `C`.

Add the diagonal `yz`, cutting off the ear triangle `xyz`. The remaining polygon does not contain `x` in its interior boundary cycle. Triangulate that remaining polygon by a zig-zag triangulation, whose diagonal graph has maximum degree at most two.

Thus `x` receives no diagonal. The vertices `y,z` receive the ear diagonal `yz` plus at most two zig-zag diagonals, hence at most three added incidences; every other vertex receives at most two. QED.

---

## 3. Eight-edge augmentation lemma

### Theorem T11.64 — an eight-edge augmentation can be chosen with `Delta<=6`

Let `H` be a 5-regular 3-connected plane graph such that triangulating all faces requires exactly eight added edges. Then there exists a triangulation `T` of `H` on the same vertex set for which the added-edge graph

\[
F:=E(T)\setminus E(H)
\]

satisfies

\[
\boxed{|F|=8,
\qquad
\Delta(F)\le6.}
\]

### Proof

Start with an arbitrary face-by-face triangulation and its eight-edge added graph `F`.

If

\[
\Delta(F)\le6,
\]
there is nothing to prove.

Assume instead that some vertex `x` has

\[
d_F(x)\ge7.
\]

Because `|F|=8`, at most one edge of `F` is not incident with `x`.

We distinguish two possibilities.

### Case A: `d_F(x)=7`

At least one face incident with `x` contains an added diagonal incident with `x`. Choose such a face `C` and retriangulate it using T11.63.

All added diagonals formerly incident with `x` inside `C` disappear, so the new added degree of `x` is at most

\[
7-1=6.
\]

Now consider another vertex `v` of `C`.

Outside `C`, at most two added edges can be incident with `v`: at most one edge `xv` because the graph is simple, and at most the unique added edge of `F` not incident with `x`.

Inside the new triangulation of `C`, T11.63 contributes at most three added incidences at `v`. Hence

\[
d_F(v)\le2+3=5.
\]

Vertices outside `C` are unchanged. Therefore the modified added-edge graph has maximum degree at most six.

### Case B: `d_F(x)=8`

All eight added edges are incident with `x`.

The vertex `x` has degree five in the original graph `H`, so it is incident with exactly five faces. The eight added incidences at `x` are distributed among those five faces. By the pigeonhole principle, some incident face `C` contains at least two added diagonals incident with `x`.

Retriangulate `C` using T11.63. Then the new added degree of `x` is at most

\[
8-2=6.
\]

Before the retriangulation there was no added edge not incident with `x`. Thus any other vertex of `C` has outside added degree at most one, coming from a possible edge to `x`. T11.63 contributes at most three new incidences inside `C`, so its total added degree is at most four.

Again all vertices outside `C` are unchanged, and the resulting added graph has maximum degree at most six.

This proves the theorem. QED.

---

## 4. The `B_O=0` endpoint at order 28

Apply T11.64 to the 5-connected 5-regular support `H_28`.

We obtain a triangulation `T_28` with added-edge graph `F` satisfying

\[
|F|=8,
\qquad
\Delta(F)\le6.
\]

For the orbit-total state

\[
\Xi=(6,5),
\]

color `H_28` by the capacity-five channel and `F` by the capacity-six channel.

Both degree bounds are respected:

\[
\Delta(H_{28})=5,
\qquad
\Delta(F)\le6.
\]

Therefore

\[
B_O
=5\cdot28-2\cdot70
=0,
\]

and

\[
B_A
=6\cdot28-2\cdot8
=152.
\]

Thus the terminal point

\[
\boxed{(152,0)}
\]

is attainable.

---

## 5. The `B_O=2` endpoint at order 28

Let

\[
S:=\{v:d_F(v)=6\}.
\]

Since `F` has eight edges,

\[
\sum_vd_F(v)=16,
\]

and therefore

\[
\boxed{|S|\le2.}
\]

The graph `H_28` is 5-regular and has seventy edges. At most

\[
5|S|\le10
\]

of its edges are incident with `S`. Hence there exists an edge

\[
e\in E(H_{28})
\]

whose endpoints both lie outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel.

At both endpoints of `e`, the previous `F`-degree was at most five, so

\[
\Delta(F\cup\{e\})\le6.
\]

Meanwhile

\[
\Delta(H_{28}-e)\le5.
\]

Thus the recolored network is feasible and has

\[
B_O=2,
\qquad
B_A=150.
\]

Therefore

\[
\boxed{(150,2)}
\]

is attainable.

### Theorem T11.65 — terminal-pair closure at order 28

For the planar orbit-total state `(6,5)` on `28` vertices, both terminal minimum-total points

\[
\boxed{(150,2),
\qquad
(152,0)}
\]

are attainable.

---

## 6. Exact full order-28 Pareto front

For `(6,5)` on `n=28`, the universal planar bounds are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5\cdot28+12=152.
\]

Both boundary coordinates are even.

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` applies to every even `n>=16` and realizes every parity-compatible point on the minimum-total line with

\[
B_O\ge4.
\]

T11.65 supplies the remaining two levels `B_O=2,0`.

Hence every allowed even lattice point on the minimum-total line is attained.

### Theorem T11.66 — exact planar `(6,5)` front at order 28

\[
\boxed{
\mathcal R^\Xi_{Pl,28}(6,5)
=
\{(12+2t,140-2t):0\le t\le70\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,28}(6,5;X,Y)
=
\sum_{t=0}^{70}X^{12+2t}Y^{140-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by one of these points, so there are no additional Pareto-minimal responses. QED.

---

## 7. Updated exact range and next hostile target

Combining T11.56, T11.59, T11.62 and T11.66, the full planar `(6,5)` Pareto front is now exact for every even host size

\[
\boxed{4\le n\le28.}
\]

The next first unresolved order is

\[
\boxed{n=30.}
\]

A 5-regular support there needs

\[
\frac{30}{2}-6=9
\]

added triangulation edges.

The order-28 proof shows that one highly concentrated vertex is still removable by local retriangulation when at most one added edge lies away from it. At nine edges, a degree-seven obstruction may coexist with two off-center edges, so the next task is to strengthen T11.63 into a controlled multi-face retriangulation lemma or find a genuine order-30 counterexample.