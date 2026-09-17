# HATTER-SOL-11 · Closing the `(6,5)` Terminal Tail for `16<=n<=24`

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\mapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total two-channel projection. This note concerns only the `Xi` response model.

The previous capacity-five note reduced the large-host `(6,5)` problem to the last two minimum-total boundary levels `B_O=2,0`. Here those levels are closed for

\[
\boxed{n=16,18,20,22,24.}
\]

The proof has two independent pieces: a uniform bounded-degree triangulation that gives every level `B_O>=4`, and a 5-regular planar support whose triangulation complement gives the two terminal levels.

---

## 1. A rigorous `B_O>=4` segment

Let

\[
n=2m\ge16.
\]

Use the bounded-degree triangulation `T_n` from `PLANAR_UNIT_TAIL_THEOREM.md`: start with the `m`-antiprism and triangulate its two `m`-gonal cap faces by identical zig-zag triangulations. Then

\[
|E(T_n)|=3n-6,
\qquad
\Delta(T_n)\le6.
\]

In each cap, the added diagonal graph is a path on `m-2` vertices plus two isolated vertices. Hence exactly `m-4` vertices in that cap receive two added diagonals and therefore have degree six in `T_n`.

Choose the two cap triangulations with the same cyclic index pattern. Then a top vertex `u_i` has degree six iff the corresponding bottom vertex `v_i` has degree six.

Let `I` be this common index set, so

\[
|I|=m-4.
\]

The antiprism rung edges

\[
M_6:=\{u_i v_i:i\in I\}
\]

form a matching covering every degree-six vertex of `T_n` exactly once.

Define

\[
H_5:=T_n-M_6.
\]

Then

\[
\boxed{\Delta(H_5)\le5}
\]

and

\[
|E(H_5)|
=(3n-6)-(m-4)
=\frac{5n}{2}-2.
\]

### Theorem T11.57 — uniform residual-four support

For every even `n>=16`, the `(6,5)` response contains every minimum-total boundary point with

\[
B_O\ge4.
\]

Explicitly,

\[
\boxed{
(12+2t,5n-2t)
\in\mathcal R^\Xi_{Pl,n}(6,5)
\quad
0\le t\le\frac{5n}{2}-2.
}
\]

### Proof

Choose any `t` edges of `H_5` as the capacity-five channel and color every remaining edge of `T_n` by the capacity-six channel.

The oblique subgraph is a subgraph of `H_5`, so its maximum degree is at most five. The axial subgraph is a subgraph of `T_n`, so its maximum degree is at most six.

All `3n-6` triangulation edges are used. Thus

\[
B_A=6n-2(3n-6-t)=12+2t,
\]

\[
B_O=5n-2t.
\]

Every such point lies on the universal planar minimum-total line

\[
B_A+B_O=5n+12.
\]

Hence it is Pareto-minimal. QED.

This supplies a proof for the `B_O>=4` claim that was only summarized in the preceding note.

---

## 2. External existence input for the terminal levels

For each

\[
n\in\{16,18,20,22,24\},
\]
there exists a connected simple planar 5-regular graph `H_n`.

This is a classical existence fact and is also explicitly witnessed by Table 1 of:

Mahdieh Hasheminezhad, Brendan D. McKay, Tristan Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations*, Journal of Graph Algorithms and Applications 15(3), 417–436 (2011).

Their table gives positive counts at orders `16,18,20,22,24` (respectively `1,1,6,14,98` connected embedded isomorphism types in their enumeration).

No enumeration count is used in the proof below; only existence of one such graph at each stated order is used.

---

## 3. The `B_O=0` endpoint

Fix one of the five host sizes and let `H_n` be a connected simple planar 5-regular graph.

Then

\[
|E(H_n)|=\frac{5n}{2}.
\]

Extend a planar embedding of `H_n` to a maximal simple planar graph `T` on the same vertex set by adding edges until no further planar edge can be inserted.

Since a maximal simple planar graph on `n>=3` vertices has `3n-6` edges, the added-edge graph

\[
F:=E(T)\setminus E(H_n)
\]

has

\[
|F|
=3n-6-\frac{5n}{2}
=\frac n2-6.
\]

For

\[
n=16,18,20,22,24
\]
this number is

\[
2,3,4,5,6,
\]
respectively. Therefore

\[
\boxed{\Delta(F)\le |F|\le6.}
\]

Color `H_n` by the capacity-five channel and `F` by the capacity-six channel. Both channel bounds are respected and the full support is the triangulation `T`.

Thus

\[
\boxed{B_O=0}
\]

is attainable. The corresponding axial boundary is

\[
B_A
=6n-2|F|
=5n+12.
\]

So the terminal point is

\[
\boxed{(5n+12,0).}
\]

---

## 4. The `B_O=2` endpoint

We now recolor one edge of `H_n` from the capacity-five channel to the capacity-six channel.

If

\[
|F|\le5,
\]
then `Delta(F)<=5`, so **any** edge `e` of `H_n` can be added to the axial channel without exceeding axial degree six.

The only delicate case is

\[
n=24,
\qquad
|F|=6.
\]

If `Delta(F)<=5`, again any `e` works.

Suppose instead some vertex `x` has

\[
d_F(x)=6.
\]

There cannot be two such vertices. Indeed, if both `x` and `y` had degree six in a simple six-edge graph `F`, every edge of `F` would have to be incident with both `x` and `y`, which is impossible in a simple graph.

Since `H_24` is 5-regular and has sixty edges, it has an edge `e` not incident with `x`. For each endpoint of such an edge,

\[
d_F\le5,
\]

so

\[
\Delta(F\cup\{e\})\le6.
\]

Color `H_n-e` oblique and `F\cup\{e\}` axial. Then

\[
\boxed{B_O=2}
\]

and

\[
\boxed{B_A=5n+10.}
\]

### Theorem T11.58 — terminal-pair closure through order 24

For every

\[
n\in\{16,18,20,22,24\},
\]
both terminal points

\[
\boxed{(5n+10,2),\qquad(5n+12,0)}
\]

belong to the exact planar `(6,5)` Pareto front.

---

## 5. Exact full fronts for five new host sizes

The universal planar bounds for state `(6,5)` are

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge5n+12.
\]

Both coordinates are even because `n` is even.

T11.57 realizes every parity-compatible point on the minimum-total line with `B_O>=4`. T11.58 supplies the only two missing points, `B_O=2` and `B_O=0`.

Therefore the entire allowed minimum-total segment is attained.

### Theorem T11.59 — exact `(6,5)` front for `16<=n<=24`

For

\[
n\in\{16,18,20,22,24\},
\]

\[
\boxed{
\mathcal R^\Xi_{Pl,n}(6,5)
=
\left\{
(12+2t,5n-2t):
0\le t\le\frac{5n}{2}
\right\}.
}
\]

Equivalently,

\[
\boxed{
Z^\Xi_{Pl,n}(6,5;X,Y)
=
\sum_{t=0}^{5n/2}X^{12+2t}Y^{5n-2t}.
}
\]

### Proof of exactness

All displayed points are constructed above.

Any feasible point above the line

\[
B_A+B_O=5n+12
\]

is componentwise dominated by one of the displayed even lattice points, using the coordinate floors `B_A>=12`, `B_O>=0`. Hence no further Pareto point exists. QED.

---

## 6. Updated frontier

Combining T11.56 from `PLANAR_CAPACITY_FIVE_FLOOR.md` with T11.59, the full `(6,5)` Pareto polynomial is now exact for every even host size

\[
\boxed{4\le n\le24.}
\]

The remaining infinite-host problem begins at

\[
\boxed{n=26.}
\]

At `n=26`, a 5-regular planar graph needs only

\[
\frac{26}{2}-6=7
\]

additional edges to become a triangulation. Thus the obstruction is already extremely local: one must choose a triangulation augmentation whose added-edge graph has maximum degree at most six.

The next hostile target is therefore:

> prove or refute that every required 5-regular support can be chosen so that its seven-edge triangulation complement is not a seven-edge star.

A positive answer closes the `B_O=0` endpoint at order 26; a one-edge recoloring audit would then address `B_O=2`.