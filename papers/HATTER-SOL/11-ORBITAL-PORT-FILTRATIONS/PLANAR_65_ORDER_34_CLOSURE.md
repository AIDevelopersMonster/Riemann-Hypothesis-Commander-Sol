# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 34

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total projection. This note concerns only the `Xi` response model.

The previous note stopped at order `34` because an eleven-edge triangulation complement can contain a degree-seven vertex together with four off-center edges, while the earlier ear-off estimate allowed three new incidences on a repaired face. The obstruction disappears after strengthening the local polygon lemma from `3` to `2`.

---

## 1. External existence input

Hasheminezhad, McKay and Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations* (JGAA 15(3), 2011), Table 1, enumerate connected simple planar 5-regular graphs at order `34`, including `1,291,446` examples of vertex-connectivity `5`.

Fix one 5-connected plane 5-regular graph

\[
H_{34}.
\]

Then

\[
|V(H_{34})|=34,
\qquad
|E(H_{34})|=85.
\]

A triangulation on the same vertex set has

\[
3\cdot34-6=96
\]

edges, so a face-by-face triangulation adds exactly

\[
\boxed{11}
\]

edges.

Because `H_34` is 5-connected, it is 3-connected. Hence facial boundaries are simple cycles and two distinct facial cycles intersect in at most one vertex or one edge.

---

## 2. Strengthened local polygon lemma

### Lemma T11.72 — two-incidence ear-off triangulation

Let

\[
C=(x,y,w_1,\ldots,w_s,z)
\]

be a polygonal face of length at least four, where `y` and `z` are the two neighbors of `x` on the boundary.

Then `C` admits a triangulation such that

1. no added diagonal is incident with `x`;
2. every other boundary vertex is incident with at most **two** added diagonals of `C`.

### Proof

Add the diagonal

\[
yz,
\]

which cuts off the ear triangle `xyz`.

It remains to triangulate the polygon

\[
P=(y,w_1,\ldots,w_s,z)
\]

with `yz` as a boundary edge.

Triangulate `P` by the standard alternating zig-zag construction. Writing its cyclic vertices as

\[
p_0=y,p_1,\ldots,p_{m-1}=z,
\]

perform alternating ear cuts from the two ends:

\[
p_0p_{m-2},
\quad
p_1p_{m-2},
\quad
p_1p_{m-3},
\quad
p_2p_{m-3},
\quad\ldots
\]

until a triangle remains.

The diagonal graph of this zig-zag is a path. Hence every vertex of `P` is incident with at most two zig-zag diagonals; moreover `y=p_0` is incident with at most one and `z=p_{m-1}` with none.

After restoring the ear diagonal `yz`, the vertex `y` has at most two added incidences, `z` has at most one, and every other vertex has at most two. The vertex `x` has none. QED.

This improves the previous local bound `3` to the sharp uniform bound `2` needed at order `34`.

---

## 3. Uniqueness of an overloaded vertex with eleven added edges

Let `F` be any simple graph with eleven edges. For distinct vertices `u,v`,

\[
d_F(u)+d_F(v)\le |F|+1=12.
\]

Therefore two vertices cannot both have degree at least seven.

### Lemma T11.73

If

\[
|F|=11,
\]
then there is at most one vertex satisfying

\[
d_F(v)\ge7.
\]

---

## 4. Eleven-edge augmentation theorem

### Theorem T11.74 — eleven added edges can be balanced below degree seven

Let `H` be a 5-regular 3-connected plane graph whose faces require exactly eleven added edges to triangulate. Then there exists a triangulation `T` on the same vertex set such that the added-edge graph

\[
F:=E(T)\setminus E(H)
\]

satisfies

\[
\boxed{|F|=11,
\qquad
\Delta(F)\le6.}
\]

### Proof

Start from an arbitrary face-by-face triangulation. If `Delta(F)<=6`, stop.

Otherwise let `x` be the unique overloaded vertex from T11.73 and put

\[
d:=d_F(x)\in\{7,8,9,10,11\}.
\]

Let

\[
q:=11-d
\]

be the number of added edges not incident with `x`.

The vertex `x` has degree five in the original graph `H`, hence is incident with exactly five faces. For each incident face `C`, let

\[
k_C
\]

be the number of added diagonals in `C` incident with `x`. Then

\[
\sum_{C\ni x}k_C=d.
\]

A key observation is the following. If a boundary vertex `v\neq x` lies on a chosen face `C`, then no added edge from `x` lying in a different face can also meet `v`. Indeed, if `v` is adjacent to `x` in `H`, then `xv` is an original edge, not an added diagonal. If `v` is not adjacent to `x`, a second face containing both `x` and `v` would violate the face-intersection property of a 3-connected plane graph.

Hence, outside the face being repaired, such a vertex `v` can be incident only with the `q` off-center added edges.

We now treat the possible values of `d`.

### Case `d=7`

Here

\[
q=4.
\]

Choose any incident face with

\[
k_C\ge1.
\]

Apply T11.72 at `x`. The degree of `x` falls by at least one, hence to at most six.

Every other boundary vertex of `C` has outside added degree at most `4` and receives at most `2` new incidences from the repaired face. Thus

\[
d_F(v)\le4+2=6.
\]

All vertices outside `C` were already of degree at most six.

### Case `d=8`

Now

\[
q=3.
\]

Since eight incidences are distributed over five faces, some face has

\[
k_C\ge2.
\]

Repair that face. Then `x` drops to degree at most six, while every other affected vertex has degree at most

\[
3+2=5.
\]

### Case `d=9`

Here

\[
q=2.
\]

If some face has `k_C>=3`, repair that one face.

Otherwise every `k_C<=2`. Since five nonnegative integers bounded by two sum to nine, their multiset is

\[
\{2,2,2,2,1\}.
\]

Choose two nonconsecutive faces among the four faces of load two. Such a pair exists in the cyclic order of five incident faces.

Repair both faces. Nonconsecutive incident faces intersect only in `x`, so no other vertex receives new diagonals from both repairs. The degree of `x` drops by four, while every other affected vertex has total added degree at most

\[
2+2=4.
\]

### Case `d=10`

Now

\[
q=1.
\]

If some face has `k_C>=4`, repair that face.

Otherwise consider the five pairs of nonconsecutive incident faces. Each face appears in exactly two such pairs, so the sum of their pair-loads is

\[
2\sum_Ck_C=20.
\]

Their average load is four. Hence some nonconsecutive pair has combined load at least four.

Repair those two faces. The degree of `x` falls to at most six, and every other affected vertex has total added degree at most

\[
1+2=3.
\]

### Case `d=11`

Here

\[
q=0.
\]

If some face has `k_C>=5`, repair that face.

Otherwise the five nonconsecutive face-pairs have total pair-load

\[
2\sum_Ck_C=22,
\]

so their average is

\[
\frac{22}{5}>4.
\]

Therefore some nonconsecutive pair has combined load at least five.

Repair that pair. The degree of `x` decreases by at least five and is therefore at most six. Every other affected vertex receives at most two added incidences.

Thus all cases produce a triangulation with

\[
\Delta(F)\le6.
\]

QED.

---

## 5. The terminal `B_O=0` endpoint at order 34

Apply T11.74 to `H_34`. We obtain a triangulation `T_34` with added-edge graph `F` satisfying

\[
|F|=11,
\qquad
\Delta(F)\le6.
\]

For the orbit-total state

\[
\Xi=(6,5),
\]

color `H_34` by the capacity-five channel and `F` by the capacity-six channel.

Then

\[
B_O
=5\cdot34-2\cdot85
=0,
\]

while

\[
B_A
=6\cdot34-2\cdot11
=182.
\]

Hence

\[
\boxed{(182,0)}
\]

is attained.

---

## 6. The terminal `B_O=2` endpoint

Let

\[
S:=\{v:d_F(v)=6\}.
\]

Since

\[
\sum_vd_F(v)=22,
\]

we have

\[
\boxed{|S|\le3.}
\]

The support `H_34` is 5-regular with `85` edges. At most

\[
5|S|\le15
\]

of its edges are incident with `S`. Therefore an edge

\[
e\in E(H_{34})
\]

exists with both endpoints outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then

\[
\Delta(F\cup\{e\})\le6,
\qquad
\Delta(H_{34}-e)\le5.
\]

The resulting boundaries are

\[
B_O=2,
\qquad
B_A=180.
\]

Thus

\[
\boxed{(180,2)}
\]

is attained.

### Theorem T11.75 — terminal-pair closure at order 34

For the planar orbit-total state `(6,5)` on `34` vertices, both terminal minimum-total points

\[
\boxed{(180,2),
\qquad
(182,0)}
\]

are attainable.

---

## 7. Exact full order-34 Pareto front

The universal planar bounds are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5\cdot34+12=182.
\]

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` realizes every parity-compatible point on the minimum-total line with

\[
B_O\ge4
\]

for every even `n>=16`.

T11.75 supplies `B_O=2,0`.

Therefore every allowed even lattice point on the minimum-total line is attained.

### Theorem T11.76 — exact planar `(6,5)` front at order 34

\[
\boxed{
\mathcal R^\Xi_{Pl,34}(6,5)
=
\{(12+2t,170-2t):0\le t\le85\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,34}(6,5;X,Y)
=
\sum_{t=0}^{85}X^{12+2t}Y^{170-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by a displayed even lattice point. Hence the displayed segment is the complete Pareto front. QED.

---

## 8. Updated exact range

Combining the preceding theorem layers with T11.76, the full planar `(6,5)` Pareto front is now exact for every even host size

\[
\boxed{4\le n\le34.}
\]

The first unresolved order is now

\[
\boxed{n=36,}
\]

where a 5-regular support requires

\[
\frac{36}{2}-6=12
\]

added triangulation edges.

The strengthened two-incidence ear-off lemma solves all overload patterns through eleven edges. At twelve edges, the first unresolved pattern is a degree-seven center with five off-center edges: the crude local estimate becomes

\[
5+2=7.
\]

So order `36` is now the first genuine obstruction. The next hostile target is to use the geometry of the five off-center edges, rather than their total count, to choose a repair face whose boundary avoids every off-center degree-five concentration.