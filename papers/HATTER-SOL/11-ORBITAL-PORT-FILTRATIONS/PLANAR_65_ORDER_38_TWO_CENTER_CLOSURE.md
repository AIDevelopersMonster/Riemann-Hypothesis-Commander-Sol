# HATTER-SOL-11 · Exact `(6,5)` Closure at Planar Order 38

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total projection. This note concerns only the `Xi` response model.

Order `38` is the first place where a triangulation complement can contain two vertices above the capacity-six threshold. The new ingredient is therefore a genuine **two-center augmentation theorem**.

---

## 1. External existence input at order 38

For a planar 5-regular graph with `v` vertices,

\[
f=\frac{3v}{2}+2.
\]

At

\[
v=38
\]

this gives

\[
\boxed{f=59.}
\]

The known existence theorem for planar quintic graphs states that there are even 5-connected 5-regular planar graphs with `f` faces whenever

\[
f=20
\]

or

\[
f\ge26,
\qquad
f\equiv2\pmod3.
\]

Since

\[
59\ge26,
\qquad
59\equiv2\pmod3,
\]

there exists a 5-connected plane 5-regular graph

\[
H_{38}.
\]

We use only existence of one such support.

A bibliographic route for the existence result is the recursive theory of Hasheminezhad–McKay–Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations*, JGAA 15(3), 417–436 (2011), DOI `10.7155/jgaa.00232`; the face-order formulation is also quoted explicitly in later work on optimal beyond-planar graphs.

For `H_38`,

\[
|E(H_{38})|=\frac{5\cdot38}{2}=95.
\]

A triangulation on the same vertex set has

\[
3\cdot38-6=108
\]

edges. Hence a face-by-face triangulation adds exactly

\[
\boxed{13}
\]

edges.

Because `H_38` is 5-connected, it is 3-connected; in particular facial boundaries are simple cycles and two distinct facial cycles intersect in at most one vertex or one edge.

---

## 2. A two-protected polygon triangulation

The two-center case requires a local triangulation that protects two nonadjacent boundary vertices simultaneously.

### Lemma T11.82 — double-ear protection

Let `C` be a polygonal face and let `x,y` be two **nonadjacent** boundary vertices. Then `C` admits a triangulation such that

\[
\boxed{
 d_C^{\mathrm{add}}(x)=d_C^{\mathrm{add}}(y)=0
}
\]

and every other boundary vertex is incident with at most four added diagonals.

### Proof

If `C` is a quadrilateral, `x,y` are opposite vertices. Choose the other diagonal; then neither protected vertex is incident with an added edge.

Assume now that `|C|>=5`.

First cut off `x` as an ear: add the diagonal joining the two neighbors of `x`. Since `x` and `y` are nonadjacent, this ear diagonal is not incident with `y`.

Remove the ear vertex `x`. In the remaining polygon, cut off `y` as an ear in the same way. Finally triangulate the remaining polygon by a zig-zag triangulation whose diagonal graph has maximum degree at most two.

The protected vertices `x,y` receive no added diagonal. Any other vertex can be incident with at most the two ear diagonals and at most two zig-zag diagonals, hence with at most four added diagonals in total. QED.

---

## 3. Structure of overloads in a thirteen-edge graph

Let `F` be a simple graph with

\[
|E(F)|=13.
\]

Call a vertex **overloaded** if its degree in `F` is at least seven.

### Lemma T11.83 — at most two overload centers

`F` has at most two overloaded vertices.

If it has two, say `x,y`, then necessarily

\[
\boxed{
 d_F(x)=d_F(y)=7,
 \qquad
 xy\in E(F),
}
\]

and every edge of `F` is incident with at least one of `x,y`.

### Proof

Three overloaded vertices would have degree sum at least `21`. Among three vertices there are at most three internal edges, so the number of graph edges incident with at least one of them would be at least

\[
21-3=18>13,
\]

impossible.

Now suppose `x,y` are both overloaded. For any two vertices of a simple `13`-edge graph,

\[
d_F(x)+d_F(y)-\mathbf 1_{xy\in E(F)}\le13.
\]

Since the left degree sum is at least `14`, equality forces

\[
d_F(x)=d_F(y)=7
\]

and

\[
xy\in E(F).
\]

The same equality says that the union of the two incident edge sets has size exactly `13`; hence every edge is incident with `x` or `y`. QED.

---

## 4. The one-center case

Assume first that exactly one vertex `x` is overloaded. Put

\[
d:=d_F(x),
\qquad
q:=13-d.
\]

Thus `q` is the number of added edges not incident with `x`.

Because the original support is 5-regular, `x` is incident with exactly five faces. For an incident face `C`, let

\[
k_C
\]

be the number of added diagonals of `C` incident with `x`. Then

\[
\sum_{C\ni x}k_C=d.
\]

We use T11.72 from `PLANAR_65_ORDER_34_CLOSURE.md`: an incident face can be ear-off retriangulated at `x` so that `x` receives no new diagonal and every other boundary vertex receives at most two.

We also use T11.77 from `PLANAR_65_ORDER_36_CLOSURE.md`: a chosen second boundary vertex may be protected so that it receives at most one new diagonal.

### Case `d=7`, so `q=6`

Let `Q` be the six-edge subgraph formed by added edges not incident with `x`.

If

\[
\Delta(Q)\le4,
\]
choose any incident face with `k_C>=1` and apply T11.72. The degree of `x` falls to at most six, while every other affected vertex has degree at most

\[
4+2=6.
\]

Suppose next that

\[
\Delta(Q)=5.
\]
Let `y` be a degree-five vertex of `Q`. Five of the six off-center edges are incident with `y`, so every other vertex has `Q`-degree at most two.

Choose any face `C` with `k_C>=1`. If `y` is not on `C`, apply T11.72. If `y` lies on `C`, apply the protected ear-off T11.77 with protected vertex `y`. Then

\[
d(y)\le5+1=6,
\]

and every other affected vertex has degree at most

\[
2+3=5.
\]

Finally suppose

\[
\Delta(Q)=6.
\]
Then all six off-center edges form a star centered at some vertex `y`.

If there is a loaded face `C` of `x` not containing `y`, apply T11.72 there. Every affected noncentral vertex has outside `Q`-degree at most one, so no overload is created.

It remains only to consider the situation in which **every** loaded face of `x` contains `y`.

Two vertices in a 3-connected plane graph lie on at most two common faces. Since the total `x`-load is seven, one common face `C` satisfies

\[
\boxed{k_C\ge4.}
\]

Now ear off the face at `y`, not at `x`. Thus `y` receives no new diagonal from `C`, while every other boundary vertex, including `x`, receives at most two.

The new degree of `x` is therefore at most

\[
7-k_C+2\le5.
\]

The star center `y` remains at degree at most six. Every other boundary vertex has no old added incidence outside `C` from either center, by the facial intersection property, and therefore remains safely below six.

So the case `d=7` is closed.

### Case `d=8`, so `q=5`

Some incident face has

\[
k_C\ge2.
\]

If the five off-center edges have maximum degree at most four, apply T11.72.

If instead they form a five-edge star centered at `y`, then either `y` is outside the chosen face, in which case T11.72 is safe, or `y` lies on the face, in which case T11.77 gives

\[
d(y)\le5+1=6.
\]

The center `x` loses at least two incidences and falls to degree at most six.

### Case `d=9`, so `q=4`

If some incident face has

\[
k_C\ge3,
\]
repair that face with T11.72.

Otherwise the five face-loads are

\[
\{2,2,2,2,1\}.
\]

Choose two nonconsecutive load-two faces and repair both. Their facial cycles intersect only at `x`, so every other vertex is affected by at most one repair. Hence every other affected vertex has degree at most

\[
4+2=6,
\]

while `x` loses four incidences.

### Case `d=10`, so `q=3`

If one face has load at least four, repair it.

Otherwise consider the five pairs of nonconsecutive incident faces. Each face occurs in exactly two such pairs, so the sum of all five pair-loads is

\[
2d=20.
\]

Thus some nonconsecutive pair has combined load at least four. Repair that pair. Every other affected vertex has degree at most

\[
3+2=5.
\]

### Case `d=11`, so `q=2`

The same nonconsecutive-pair averaging gives a pair of combined load at least

\[
\left\lceil\frac{22}{5}\right\rceil=5.
\]

Repair that pair unless a single face already has load at least five. In either event `x` falls to degree at most six and every other affected vertex remains at degree at most four.

### Case `d=12`, so `q=1`

Take the three incident faces of largest load. Their total load is at least

\[
\left\lceil\frac{3\cdot12}{5}\right\rceil=8.
\]

Repair all three. A vertex other than `x` lies on at most two faces incident with `x`, so it receives at most four new local incidences. Including the unique off-center edge gives degree at most five.

The center loses at least eight incidences.

### Case `d=13`, so `q=0`

Again repair the three most heavily loaded incident faces. Their total load is at least

\[
\left\lceil\frac{3\cdot13}{5}\right\rceil=8.
\]

Thus `x` falls from degree thirteen to degree at most five. Every other vertex receives at most four new incidences.

Hence every one-center configuration admits a retriangulation with maximum added degree at most six.

---

## 5. The genuine two-center case

Assume now that `F` has two overloaded vertices `x,y`.

By T11.83,

\[
d_F(x)=d_F(y)=7,
\qquad
xy\in E(F),
\]

and every added edge is incident with `x` or `y`.

Because `xy` is an **added** edge rather than an edge of the original support, `x,y` are nonadjacent in the original plane graph. Therefore they lie together on a unique nontriangular face `C`, namely the face containing the added diagonal `xy`.

Retriangulate `C` using the double-ear lemma T11.82.

Both centers receive zero diagonals from the new triangulation of `C`. Each loses at least the old diagonal `xy`, so

\[
d_F(x)\le6,
\qquad
 d_F(y)\le6.
\]

Now let `v` be another boundary vertex of `C`. Every old added edge was incident with `x` or `y`. No added edge `xv` or `yv` can lie in another face: if the endpoints are adjacent in the original graph, that edge is original rather than added; if they are nonadjacent, a second common face would violate the facial intersection property.

Hence `v` has no old added incidence outside `C`. The double-ear retriangulation gives it added degree at most four.

Vertices outside `C` are unchanged and were not overloaded.

Thus the two-center configuration also reduces to

\[
\Delta(F)\le6.
\]

---

## 6. Thirteen-edge augmentation theorem

Combining the one-center and two-center analyses gives the new local theorem.

### Theorem T11.84 — thirteen-edge augmentation theorem

Let `H` be a 5-regular 3-connected plane graph whose faces require exactly thirteen added edges to triangulate. Then there exists a triangulation `T` on the same vertex set such that

\[
F:=E(T)\setminus E(H)
\]

satisfies

\[
\boxed{
|F|=13,
\qquad
\Delta(F)\le6.
}
\]

No computation is used in the proof; the only external input is existence of the planar 5-regular support.

---

## 7. Terminal endpoints at order 38

Apply T11.84 to `H_38`. We obtain a triangulation `T_38` with added-edge graph `F` satisfying

\[
|F|=13,
\qquad
\Delta(F)\le6.
\]

For the orbit-total state

\[
\Xi=(6,5),
\]

color the original 5-regular support `H_38` by the capacity-five channel and the added graph `F` by the capacity-six channel.

Then

\[
B_O
=5\cdot38-2\cdot95
=0,
\]

and

\[
B_A
=6\cdot38-2\cdot13
=202.
\]

Hence

\[
\boxed{(202,0)}
\]

is attainable.

For the `B_O=2` endpoint, let

\[
S:=\{v:d_F(v)=6\}.
\]

Since

\[
\sum_vd_F(v)=26,
\]

we have

\[
|S|\le4.
\]

The 5-regular support `H_38` has `95` edges, while at most

\[
5|S|\le20
\]

support edges are incident with `S`. Hence there exists an edge `e` of `H_38` whose endpoints both lie outside `S`.

Move `e` from the capacity-five channel to the capacity-six channel. Then

\[
\Delta(F\cup\{e\})\le6,
\qquad
\Delta(H_{38}-e)\le5.
\]

This gives

\[
\boxed{(200,2)}.
\]

### Theorem T11.85 — terminal-pair closure at order 38

For the planar orbit-total state `(6,5)` on `38` vertices, both terminal minimum-total points

\[
\boxed{(200,2),
\qquad
(202,0)}
\]

are attainable.

---

## 8. Exact full order-38 Pareto front

The universal planar inequalities are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5\cdot38+12=202.
\]

T11.57 from `PLANAR_65_TERMINAL_TAIL_16_24.md` realizes every parity-compatible point on the minimum-total line with

\[
B_O\ge4
\]

for every even `n>=16`.

T11.85 supplies `B_O=2,0`.

Therefore every allowed even lattice point on the minimum-total line is attained.

### Theorem T11.86 — exact planar `(6,5)` front at order 38

\[
\boxed{
\mathcal R^\Xi_{Pl,38}(6,5)
=
\{(12+2t,190-2t):0\le t\le95\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,38}(6,5;X,Y)
=
\sum_{t=0}^{95}X^{12+2t}Y^{190-2t}.
}
\]

Any feasible point above the minimum-total line is componentwise dominated by one of the displayed even lattice points. Hence the displayed segment is the complete Pareto front. QED.

---

## 9. Updated exact range and next target

Combining all preceding layers with T11.86, the full planar `(6,5)` Pareto front is now exact for every even host size

\[
\boxed{4\le n\le38.}
\]

At order `40`, the complement contains

\[
\frac{40}{2}-6=14
\]

added edges.

Two degree-seven centers are then no longer forced into the rigid equality pattern of T11.83: they may coexist without exhausting all added edges. Thus the next problem is a **non-extremal two-center repair theorem** rather than the rigid order-38 configuration.