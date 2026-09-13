# HATTER-SOL-11 · Planar Low-Tail `b`-Matching Theorem

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Scope.** Throughout,

\[
\Omega=(a;\{b,c\})\longmapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total two-channel projection. The results below are statements about this `Xi` response model only.

This note begins with the requested case `(6,2)` and then closes the whole low-tail range `q<=4` on the bounded-degree triangulation family already used in `PLANAR_UNIT_TAIL_THEOREM.md`.

---

## 1. Curvature repair on a fixed triangulation

Let `T` be a simple planar triangulation on `n>=4` vertices. Put

\[
\delta_T(v):=6-d_T(v).
\]

Euler gives

\[
\boxed{\sum_v\delta_T(v)=12.}
\]

Consider the orbit-total state

\[
\Xi=(6,q),
\qquad q>=1,
\]

and insist that all triangulation edges are used, with an oblique subgraph `H` and axial complement `T-H`.

The channel constraints are

\[
d_H(v)\le q
\]

and

\[
d_T(v)-d_H(v)\le6.
\]

Hence full-support feasibility is equivalent to

\[
\boxed{
(d_T(v)-6)_+\le d_H(v)\le q
\quad\text{for every }v.
}
\]

So the secondary channel is exactly a degree-constrained subgraph, i.e. a `b`-matching / factor problem with lower demand

\[
\ell_T(v):=(d_T(v)-6)_+.
\]

### Theorem T11.47 — curvature–`b`-matching bridge

A triangulation `T` supports a full-edge realization of `(6,q)` iff it has a spanning subgraph `H` satisfying

\[
\boxed{
\ell_T(v)\le d_H(v)\le q
\quad\forall v.
}
\]

For every such `H`, with `t=|E(H)|`, the boundary is

\[
\boxed{
B_A=12+2t,
\qquad
B_O=nq-2t.
}
\]

### Proof

The degree inequalities above are exactly the two channel-capacity constraints.

Moreover

\[
B_A
=6n-2|E(T-H)|
=6n-2(3n-6-t)
=12+2t,
\]

while

\[
B_O=nq-2t.
\]

QED.

Thus the curvature defect controls **where** the secondary channel must be placed, while its edge count controls **where on the minimum-total Pareto line** the response lies.

---

## 2. The requested `(6,2)` local rule

Set `q=2`.

The bridge becomes

\[
(d_T(v)-6)_+\le d_H(v)\le2.
\]

Therefore:

- vertices of degree at most `6` need no repair;
- a degree-`7` vertex needs at least one secondary-channel incidence;
- a degree-`8` vertex needs exactly two;
- a vertex of degree at least `9` makes full-support `(6,2)` impossible.

Hence the fixed-triangulation problem is a genuine degree-constrained `2`-matching problem.

This is the precise generalization of the matching-cover rule for `(6,1)`.

---

## 3. Factor-rich bounded-degree triangulations

We reuse the triangulations `T_n` from `PLANAR_UNIT_TAIL_THEOREM.md`.

For every even `n=2m>=6`, start with the `m`-antiprism on

\[
u_0,\ldots,u_{m-1},
\qquad
v_0,\ldots,v_{m-1}
\]

and triangulate its two polygonal cap faces by zig-zag diagonals so that every final degree is at most six.

The added diagonals do not remove any antiprism edge. Consequently `T_n` contains the following spanning regular subgraphs:

### Degree 1

The rung matching

\[
R_1:=\{u_i v_i:0\le i<m\}
\]

is `1`-regular.

### Degree 2

The union of the two rim cycles

\[
R_2:=C_m[u_0,\ldots,u_{m-1}]\sqcup C_m[v_0,\ldots,v_{m-1}]
\]

is `2`-regular.

### Degree 3

Add the rung matching to the two rim cycles:

\[
R_3:=R_2\cup R_1.
\]

This is the prism graph `C_m\square K_2`, hence `3`-regular.

### Degree 4

The whole antiprism skeleton

\[
R_4
\]

is `4`-regular.

For the exceptional host `n=4`, take `T_4=K_4`, which contains spanning regular subgraphs of degrees `1,2,3`.

### Lemma T11.48 — low-tail spanning-factor ladder

For every even `n>=4`, `T_n` contains a spanning `q`-regular subgraph for

\[
q=1,2,3,
\]

and for every even `n>=6` it also contains one for

\[
q=4.
\]

---

## 4. Exact response for `(6,2)` on every even host

Fix even

\[
n>=4.
\]

Every planar realization of node capacity `(6,2)` satisfies

\[
B_A\ge12
\]

because the axial subgraph is planar, and

\[
B_A+B_O\ge2n+12
\]

because total capacity is `8n` while a planar support has at most `3n-6` edges.

Take `T_n` and its spanning `2`-regular subgraph `R_2` from T11.48.

For any integer

\[
0\le t\le n,
\]
choose any `t` edges of `R_2`, color them oblique, and color every other edge of `T_n` axial.

Because `R_2` has maximum degree two, the oblique channel is feasible. Because `Delta(T_n)<=6`, deleting oblique edges leaves an axial graph of degree at most six.

The boundary is

\[
\boxed{
(B_A,B_O)=(12+2t,2n-2t).
}
\]

### Theorem T11.49 — exact all-even planar front for `(6,2)`

For every even `n>=4`,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(6,2)
=
\{(12+2t,2n-2t):0\le t\le n\}.
}
\]

Equivalently,

\[
\boxed{
Z^{\Xi}_{Pl,n}(6,2;X,Y)
=
\sum_{t=0}^{n}X^{12+2t}Y^{2n-2t}.
}
\]

### Proof of exactness

Every feasible point satisfies

\[
B_A\ge12,
\qquad
B_O\ge0,
\qquad
B_A+B_O\ge2n+12,
\]

and both coordinates are even.

The construction realizes every parity-compatible point on the minimum-total line between `(12,2n)` and `(2n+12,0)`. Any feasible point above that line is componentwise dominated by one of these realized points. QED.

---

## 5. Swapped and pure members of the `(6,2)` fiber

By channel exchange,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(2,6)
=
\{(2n-2t,12+2t):0\le t\le n\}.
}
\]

For the pure state `(0,8)`, the planar edge ceiling gives

\[
B_O\ge8n-2(3n-6)=2n+12.
\]

Since `Delta(T_n)<=6<8`, the full triangulation is feasible in the pure channel and attains equality:

\[
\boxed{
Z^{\Xi}_{Pl,n}(0,8)=Y^{2n+12}.
}
\]

The two mixed fronts are unequal because their minimum `X` exponents are `12` and `0`, respectively. Each mixed front has more than one monomial, whereas the pure response is a singleton.

### Corollary T11.49a — permanent planar memory of `(6,2)`

For every even

\[
n>=4,
\]

\[
\boxed{
\nu^{\Xi}_{Pl,n}(6,2)=3.
}
\]

So `(6,2)` remains fully distinguishable at every even planar host size.

---

## 6. Exact low-tail theorem for `P>=6`

The same argument does not depend on the high channel being exactly six.

Let

\[
P>=6
\]

and let `q` be one of the spanning-factor degrees supplied by T11.48.

The universal planar lower bounds are

\[
\boxed{
B_A\ge n(P-6)+12
}
\]

and

\[
\boxed{
B_A+B_O\ge n(P+q-6)+12.
}
\]

Choose any `t` edges from a spanning `q`-regular subgraph `R_q` of `T_n`, color them oblique, and color all remaining triangulation edges axial.

Because any subset of `R_q` has maximum degree at most `q`, this is feasible for every

\[
0\le t\le\frac{nq}{2}.
\]

It gives

\[
\boxed{
B_A=n(P-6)+12+2t,
\qquad
B_O=nq-2t.
}
\]

### Theorem T11.50 — exact planar low-tail family

For every integer `P>=6`:

- for `q=1,2,3` and every even `n>=4`;
- for `q=4` and every even `n>=6`;

we have

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(P,q)
=
\left\{
\bigl(n(P-6)+12+2t,\ nq-2t\bigr):
0\le t\le\frac{nq}{2}
\right\}.
}
\]

The swapped state is obtained by exchanging coordinates, and the pure state satisfies

\[
\boxed{
Z^{\Xi}_{Pl,n}(0,P+q)
=
Y^{n(P+q-6)+12}.
}
\]

Hence all three canonical orbit-total members are pairwise distinct:

\[
\boxed{
\nu^{\Xi}_{Pl,n}(P,q)=3
}
\]

throughout this range.

### Proof

The construction realizes every parity-compatible point on the line

\[
B_A+B_O=n(P+q-6)+12
\]

between the coordinate floor

\[
B_A=n(P-6)+12
\]

and `B_O=0`.

The planar edge ceiling and the axial planar edge ceiling give exactly these two universal lower bounds. The same domination argument as in T11.49 proves that no point above the line can be Pareto-minimal.

For the swapped mixed state, the minimum `X` exponent is zero because the low-capacity channel can be saturated on `R_q`, while the original state's minimum `X` exponent is

\[
n(P-6)+12>0.
\]

The pure response is a singleton, whereas every mixed front contains at least two points. QED.

---

## 7. Structural consequence

The unit-tail theorem was not an isolated matching phenomenon.

The exact non-forgetting region now contains the whole strip

\[
\boxed{
P>=6,
\qquad
1\le q\le4
}
\]

subject only to the small-host condition `n>=6` for `q=4`.

The mechanism is:

\[
\boxed{
\text{Euler defect }12
+
\text{bounded-degree triangulation}
+
\text{spanning low-degree factor}
\Longrightarrow
\text{exact Pareto segment}.
}
\]

At high capacity `P>=6`, planar geometry therefore preserves the placement of the high-capacity orbit against every low tail through capacity four on these all-even host families.

---

## 8. Why `q=5` is the next genuine boundary

The proof of T11.50 needs a spanning `q`-regular planar subgraph inside a bounded-degree triangulation at every host size under consideration.

For `q<=4`, the antiprism skeleton supplies these factors uniformly.

At `q=5`, this uniform construction disappears. The icosahedron supplies a `5`-regular example at `n=12`, but there is no corresponding factor already built into the all-even antiprism family.

Thus the next unresolved question is not `(6,3)` or `(6,4)`; those are already closed here. It is

\[
\boxed{(6,5).}
\]

The correct hostile question is:

> for which even host sizes does there exist a bounded-degree planar triangulation containing a spanning `5`-regular subgraph, and when such a subgraph does not exist, what does the exact `(6,5)` Pareto front become?

That is the first place where the low-tail factor ladder stops being automatic.