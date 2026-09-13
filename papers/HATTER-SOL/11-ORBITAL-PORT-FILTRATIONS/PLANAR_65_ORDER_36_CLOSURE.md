# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 36

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total projection. This note concerns only the `Xi` response model.

The previous note closed order `34` and identified the first new obstruction at order `36`: a degree-seven center may coexist with five off-center added edges, while the ordinary two-incidence ear-off estimate gives the borderline value `5+2=7`.

The obstruction is removable because the only dangerous off-center configuration is a five-edge star. In that case one protects its center during the local retriangulation.

---

## 1. External existence input

Hasheminezhad, McKay and Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations*, Journal of Graph Algorithms and Applications 15(3), 417–436 (2011), DOI `10.7155/jgaa.00232`, Table 1, enumerate connected simple planar 5-regular graphs up to order `36`.

At order `36` the table contains, in particular,

\[
\boxed{10,252,136}
\]

5-connected examples.

Fix one 5-connected plane 5-regular graph

\[
H_{36}.
\]

Then

\[
|V(H_{36})|=36,
\qquad
|E(H_{36})|=90.
\]

A triangulation on the same vertex set has

\[
3\cdot36-6=102
\]

edges. Thus triangulating all faces of `H_36` requires exactly

\[
\boxed{12}
\]

added edges.

Because `H_36` is 5-connected, it is 3-connected; hence every face boundary is a simple cycle and two distinct facial cycles intersect in at most one vertex or one edge.

---

## 2. Protected ear-off lemma

We need one refinement of T11.72 from `PLANAR_65_ORDER_34_CLOSURE.md`.

### Lemma T11.77 — protected ear-off retriangulation

Let `C` be a polygonal face, let `x` be a boundary vertex, and let `y!=x` be another boundary vertex.

Then `C` admits a triangulation such that

1. no added diagonal is incident with `x`;
2. at most one added diagonal is incident with `y`;
3. every other boundary vertex is incident with at most three added diagonals.

### Proof

Let `a,b` be the two neighbors of `x` on the boundary of `C`. Add the diagonal `ab`, cutting off the ear triangle `axb`. Thus no future diagonal need meet `x`.

The remaining polygon `P` has `ab` as a boundary edge and still contains `y`.

Choose a standard zig-zag triangulation of `P` in which `y` is an ear vertex of the zig-zag. Equivalently, cyclically label the polygon so that `y` is one of the two zero-degree ear vertices of the diagonal-path triangulation. Then no zig-zag diagonal is incident with `y`, while every vertex of `P` is incident with at most two zig-zag diagonals.

If `y` is one of `a,b`, it receives the ear diagonal `ab` and no other added diagonal, hence added degree one. If `y` is not `a` or `b`, it receives no added diagonal at all.

The vertices `a,b` receive the ear diagonal `ab` plus at most two zig-zag diagonals, so their added degree is at most three. Every other boundary vertex receives at most two. QED.

The only purpose of the weaker `3` bound on unprotected vertices is to gain the stronger `1` bound at the chosen protected vertex.

---

## 3. Uniqueness of an overloaded augmentation vertex

Let `F` be any simple graph with twelve edges. For distinct vertices `u,v`,

\[
d_F(u)+d_F(v)\le |F|+1=13.
\]

Hence two distinct vertices cannot both have degree at least seven.

### Lemma T11.78

If

\[
|F|=12,
\]
there is at most one vertex with

\[
d_F(v)\ge7.
\]

---

## 4. Twelve-edge augmentation theorem

### Theorem T11.79 — twelve added edges can be balanced below degree seven

Let `H` be a 5-regular 3-connected plane graph whose faces require exactly twelve added edges to triangulate. Then there exists a triangulation `T` on the same vertex set such that the added-edge graph

\[
F:=E(T)\setminus E(H)
\]

satisfies

\[
\boxed{|F|=12,
\qquad
\Delta(F)\le6.}
\]

### Proof

Start from an arbitrary face-by-face triangulation. If `Delta(F)<=6`, stop.

Otherwise let `x` be the unique overloaded vertex from T11.78, with

\[
d:=d_F(x)\in\{7,8,9,10,11,12\}.
\]

Let

\[
q:=12-d
\]

be the number of added edges not incident with `x`.

Since `H` is 5-regular, `x` is incident with exactly five faces. For each such face `C`, let `k_C` be the number of added diagonals of `C` incident with `x`. Then

\[
\sum_{C\ni x}k_C=d.
\]

As in the order-34 proof, if a vertex `v!=x` lies on a selected incident face `C`, then no added diagonal from `x` in another face can also meet `v`; this follows from the facial intersection property of a 3-connected plane graph.

We treat the possible values of `d`.

### Case `d=7`

Here

\[
q=5.
\]

Choose any incident face `C` with

\[
k_C\ge1.
\]

First suppose that every boundary vertex `v!=x` of `C` has outside off-center added degree at most four. Apply T11.72. The repaired face contributes at most two new incidences at such a vertex, hence

\[
d_F(v)\le4+2=6.
\]

The degree of `x` drops by at least one and is therefore at most six.

The only remaining possibility is that some boundary vertex `y` of `C` has outside off-center added degree five. Since there are only five off-center edges total, all five are incident with `y`; they form a five-edge star centered at `y`. Consequently every other vertex is incident with at most one off-center edge.

Apply the protected ear-off lemma T11.77 to `C`, protecting `y`. Then `x` receives no new diagonal from `C`, `y` receives at most one, and every other boundary vertex receives at most three.

Thus

\[
d_F(y)\le5+1=6,
\]

while every other affected vertex has degree at most

\[
1+3=4.
\]

So the repaired augmentation has maximum degree at most six.

### Case `d=8`

Now

\[
q=4.
\]

Some incident face has `k_C>=2`. Apply T11.72 to that face. Then `x` loses at least two incidences, and every other affected vertex has degree at most

\[
4+2=6.
\]

### Case `d=9`

Here

\[
q=3.
\]

If some face has `k_C>=3`, repair that face.

Otherwise all `k_C<=2`, and because they sum to nine their multiset is

\[
\{2,2,2,2,1\}.
\]

Choose two nonconsecutive faces among the four load-two faces and repair both. Their facial cycles intersect only in `x`, so no other vertex receives local diagonals from both repairs. The degree of `x` falls by four, and every other affected vertex has degree at most

\[
3+2=5.
\]

### Case `d=10`

Now

\[
q=2.
\]

If some face has load at least four, repair it.

Otherwise the five nonconsecutive face-pairs have total pair-load

\[
2d=20,
\]

so one such pair has combined load at least four. Repair that nonconsecutive pair. The degree of `x` falls to at most six, and every other affected vertex has degree at most

\[
2+2=4.
\]

### Case `d=11`

Here

\[
q=1.
\]

If one face has load at least five, repair it.

Otherwise the average load of a nonconsecutive face-pair is

\[
\frac{2d}{5}=\frac{22}{5}>4,
\]

so some nonconsecutive pair has combined load at least five. Repair that pair. The degree of `x` drops to at most six, and all other affected vertices remain at degree at most three.

### Case `d=12`

Now

\[
q=0.
\]

If one face has load at least six, repair it and finish.

Assume every face has load at most five. Choose the three incident faces of largest load. Their total load is at least

\[
\left\lceil\frac{3\cdot12}{5}\right\rceil=8,
\]

and in particular at least six.

Repair all three faces using T11.72. Then the degree of `x` decreases by at least six.

A vertex other than `x` can lie on at most two faces incident with `x`: if it is a neighbor of `x`, these are exactly the two faces adjacent to the edge joining them; if it is not a neighbor, 3-connectivity allows at most one common face. Hence any other vertex receives at most

\[
2+2=4
\]

new local incidences from the three repairs. Since `q=0`, no outside added edge remains to increase this value.

Thus every case yields

\[
\Delta(F)\le6.
\]

QED.

---

## 5. Terminal endpoints at order 36

Apply T11.79 to `H_36`. We obtain a triangulation `T_36` with added-edge graph `F` satisfying

\[
|F|=12,
\qquad
\Delta(F)\le6.
\]

For the orbit-total state

\[
\Xi=(6,5),
\]

color the original 5-regular support `H_36` by the capacity-five channel and `F` by the capacity-six channel.

Then

\[
B_O
=5\cdot36-2\cdot90
=0,
\]

and

\[
B_A
=6\cdot36-2\cdot12
=192.
\]

Hence

\[
\boxed{(192,0)}
\]

is attainable.

Now let

\[
S:=\{v:d_F(v)=6\}.
\]

Since

\[
\sum_vd_F(v)=24,
\]

we have

\[
|S|\le4.
\]

The support `H_36` has ninety edges. At most

\[
5|S|\le20
\]

of them are incident with `S`, so there exists an edge `e` of `H_36` whose endpoints both lie outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then

\[
\Delta(F\cup\{e\})\le6,
\qquad
\Delta(H_{36}-e)\le5.
\]

The resulting boundary is

\[
\boxed{(190,2)}.
\]

### Theorem T11.80 — terminal-pair closure at order 36

For the planar orbit-total state `(6,5)` on `36` vertices, both terminal minimum-total points

\[
\boxed{(190,2),
\qquad
(192,0)}
\]

are attainable.

---

## 6. Exact full order-36 Pareto front

For `(6,5)` on `n=36`, the universal planar inequalities are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5\cdot36+12=192.
\]

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` realizes every parity-compatible point on the minimum-total line with

\[
B_O\ge4
\]

for every even `n>=16`.

T11.80 supplies the final two levels `B_O=2,0`.

Therefore every allowed even lattice point on the minimum-total line is attained.

### Theorem T11.81 — exact planar `(6,5)` front at order 36

\[
\boxed{
\mathcal R^\Xi_{Pl,36}(6,5)
=
\{(12+2t,180-2t):0\le t\le90\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,36}(6,5;X,Y)
=
\sum_{t=0}^{90}X^{12+2t}Y^{180-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by one of these displayed points. Hence the displayed segment is the complete Pareto front. QED.

---

## 7. Updated exact range and the next obstruction

Combining all preceding theorem layers with T11.81, the full planar `(6,5)` Pareto front is now exact for every even host size

\[
\boxed{4\le n\le36.}
\]

The next first unresolved order is

\[
\boxed{n=38.}
\]

A 5-regular support there requires thirteen added triangulation edges.

At thirteen edges, the uniqueness lemma fails for the first time: two degree-seven vertices are combinatorially possible, necessarily in the extremal pattern

\[
d_F(x)=d_F(y)=7,
\qquad
xy\in E(F),
\]

with every added edge incident with at least one of `x,y`.

Thus order `38` is a genuinely different problem. The next hostile target is no longer a one-center repair theorem; it is a **two-center augmentation theorem**.