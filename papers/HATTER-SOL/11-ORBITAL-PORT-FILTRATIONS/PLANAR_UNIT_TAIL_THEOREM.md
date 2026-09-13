# HATTER-SOL-11 · Exact Planar Unit-Tail Theorem

**Scope:** orbit-total `Xi=(A,O)` model only.  
**Host:** even `n>=4`.

## 1. Euler defect at capacity six

For every simple planar graph on `n>=3` vertices,

\[
|E|\le 3n-6.
\]

Hence a single channel of uniform capacity `6` has boundary

\[
B_6=6n-2|E|\ge12.
\]

Thus uniform capacity six can never be fully saturated in finite planar geometry. The irreducible planar defect is at least `12`.

For a triangulation `T`, equality holds:

\[
\sum_v (6-d_T(v))=12.
\]

## 2. A bounded-degree triangulation with a perfect matching

### Lemma T11.44

For every even `n>=4` there exists a simple planar triangulation `T_n` with

\[
\Delta(T_n)\le6
\]

and a perfect matching.

### Proof

For `n=4`, use `K_4`.

For `n=2m>=6`, start from the `m`-antiprism graph. It has vertices

\[
u_0,...,u_{m-1},v_0,...,v_{m-1}
\]

and edges

\[
u_i u_{i+1},\quad v_i v_{i+1},\quad u_i v_i,\quad u_i v_{i-1}
\]

(indices modulo `m`). It is planar and 4-regular, with two `m`-gonal faces and all other faces triangular.

Triangulate each `m`-gon by a zig-zag triangulation in which each polygon vertex receives at most two new diagonals. Hence every final degree is at most six. The edges

\[
M=\{u_i v_i:0\le i<m\}
\]

form a perfect matching. QED.

## 3. Exact response for `(6,1)`

For any typed planar network with node capacity `(6,1)`,

\[
B_A+B_O\ge n+12
\]

because the total capacity is `7n` and the support has at most `3n-6` edges. Also

\[
B_A\ge12.
\]

Use `T_n` from T11.44. Choose any `t` edges of its perfect matching, color them `O`, and color every other triangulation edge `A`. Since `Delta(T_n)<=6`, the axial degree constraint is satisfied. The oblique edges form a matching, so the oblique capacity-one constraint is satisfied.

The boundary is

\[
(B_A,B_O)=(12+2t,n-2t),
\qquad 0\le t\le n/2.
\]

All these points lie on the minimum-total-boundary line.

### Theorem T11.45

For every even `n>=4`,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(6,1)
=
\{(12+2t,n-2t):0\le t\le n/2\}.
}
\]

Equivalently,

\[
\boxed{
Z^{\Xi}_{Pl,n}(6,1;X,Y)
=
\sum_{t=0}^{n/2}X^{12+2t}Y^{n-2t}.
}
\]

### Proof of exactness

Every feasible point satisfies

\[
B_A+B_O\ge n+12,
\qquad
B_A\ge12,
\qquad
B_O\ge0,
\]

and both coordinates are even. Hence every feasible point above the minimum-total line is componentwise dominated by one of the displayed points. QED.

## 4. Swapped and pure states

By channel exchange,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(1,6)
=
\{(n-2t,12+2t):0\le t\le n/2\}.
}
\]

For the pure state `(0,7)`, the planar edge bound gives

\[
B_O\ge n+12.
\]

The same triangulation `T_n` attains equality, so

\[
\boxed{Z^{\Xi}_{Pl,n}(0,7)=Y^{n+12}.}
\]

Therefore the three responses are pairwise distinct.

### Corollary T11.45a

For every even `n>=4`,

\[
\boxed{\nu^{\Xi}_{Pl,n}(6,1)=3.}
\]

Thus the `(6,1)` fiber remains fully distinguishable for every even planar host size.

## 5. Infinite unit-tail family

The same construction works for every `P>=6`.

The planar lower bounds are

\[
B_A\ge n(P-6)+12,
\]

and

\[
B_A+B_O\ge n(P-5)+12.
\]

Using `t` edges of the perfect matching for the unit channel gives

\[
B_A=n(P-6)+12+2t,
\qquad
B_O=n-2t.
\]

### Theorem T11.46 — exact planar unit-tail family

For every integer `P>=6` and every even `n>=4`,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(P,1)
=
\{(n(P-6)+12+2t,n-2t):0\le t\le n/2\}.
}
\]

The swapped state is obtained by exchanging coordinates, while

\[
\boxed{
Z^{\Xi}_{Pl,n}(0,P+1)
=
Y^{n(P-5)+12}.
}
\]

Hence

\[
\boxed{\nu^{\Xi}_{Pl,n}(P,1)=3\qquad(P>=6).}
\]

## 6. Structural interpretation

Below capacity six, the solved regular triangulations produce host thresholds `3,4,5`. At capacity six, regular saturation becomes impossible for every finite planar host. The controlling quantity changes from a host degree threshold to the Euler defect

\[
\boxed{12.}
\]

So the planar memory mechanism has a sharp transition:

\[
3,4,5\text{-threshold regime}
\quad\longrightarrow\quad
6\text{-capacity defect regime}.
\]

The next natural case is `(6,2)`, where the secondary channel is no longer a matching and can repair up to two incidences per vertex.