# Sharp one-step refinement bound

## 1. Setup

Let

\[
\mathbf c=(c_1,\ldots,c_k),\qquad c_i\ge2,
\]

and define

\[
\lambda(\mathbf c)
=
\min_G\sum_{i=1}^k(c_i-\deg_G v_i),
\]

where the minimum ranges over connected simple graphs on the labeled vertices with

\[
\deg_G(v_i)\le c_i.
\]

Equivalently, if

\[
M_c(\mathbf c)
=
\max_G |E(G)|
\]

over the same admissible connected graphs, then

\[
\lambda(\mathbf c)=\sum_i c_i-2M_c(\mathbf c).
\]

Suppose one factor-capacity

\[
c=ab,
\qquad a,b\ge2,
\]

is refined into the two capacities `a,b`. Write the refined vector as `\mathbf c'` and define

\[
\delta(a,b):=ab-a-b=(a-1)(b-1)-1\ge0.
\]

The total capacity drops by exactly `\delta(a,b)`:

\[
\sum \mathbf c' = \sum \mathbf c-\delta(a,b).
\]

---

## 2. Connectivity does not lower the maximum edge count

### Lemma 2.1

For every capacity vector `\mathbf c` with all `c_i\ge2`, the maximum number of edges among all simple graphs satisfying `\deg(v_i)\le c_i` is attained by a connected graph.

Hence the connectivity restriction can be omitted when computing `M_c(\mathbf c)`.

### Proof

Choose a maximum-edge feasible graph `H` having the minimum possible number of connected components.

Assume `H` is disconnected.

#### Case 1: `H` has an isolated vertex `z`

If another component contains a vertex `x` with unused capacity, then adding the edge `zx` increases the number of edges, contradicting maximality.

Therefore every vertex in every nontrivial component is saturated. Since every capacity is at least two, each such component has minimum degree at least two and hence contains a cycle edge `xy` that is not a bridge.

Delete `xy` and add `zx`. The edge count is unchanged. The old component remains connected because `xy` was not a bridge, and `z` joins it. All degree upper bounds remain satisfied. Thus the number of components decreases, contradicting the choice of `H`.

#### Case 2: there are no isolated vertices

If two different components contain vertices with unused capacity, an edge can be added between those two vertices, again contradicting maximality.

Thus at most one component contains any unsaturated vertex. In particular, one may choose a saturated component `C`; every vertex of `C` has degree at least two, so `C` contains a nonbridge edge.

If another component `D` contains an unsaturated vertex `z`, delete a nonbridge edge `xy` of `C` and add `xz`. Edge count is preserved, `C` remains connected, and `C` joins `D`.

If `D` is also saturated, choose nonbridge edges `xy` in `C` and `uv` in `D`, delete them, and add the two cross-edges `xu` and `yv`. Degrees are preserved exactly, both old components remain internally connected after deletion of the nonbridge edges, and the new cross-edges merge them.

In every case we obtain a maximum-edge feasible graph with fewer components, contradiction. Therefore a connected maximizer exists. `\square`

---

## 3. Universal one-step bound

### Theorem 3.1 — sharp refinement inversion bound

Let `\mathbf c'` be obtained from `\mathbf c` by the single multiplicative refinement

\[
ab\longmapsto a,b,
\qquad a,b\ge2.
\]

Then

\[
\boxed{
\lambda(\mathbf c')-\lambda(\mathbf c)
\le
ab-a-b.
}
\]

Moreover, the bound is sharp for every pair `a,b\ge2`.

### Proof of the upper bound

Let `G` be a maximum-edge feasible graph for `\mathbf c`; by Lemma 2.1 we may work without worrying about connectivity during the local construction.

Let `x` be the vertex of capacity `ab`, and put

\[
d=\deg_G(x)\le ab.
\]

Replace `x` by two new vertices `u,v` of capacities `a,b`.

Keep every edge not incident with `x`. Among the `d` old edges incident with `x`, retain

\[
\min\{d,a+b\}
\]

of them and distribute their distinct old endpoints between `u` and `v`, with at most `a` edges assigned to `u` and at most `b` to `v`.

This is always possible because the old neighbors of `x` are distinct and because the total available new external capacity is `a+b`.

Therefore the refined capacity vector admits a simple feasible graph with at least

\[
M_c(\mathbf c)-\max\{0,d-a-b\}
\]

edges. Since `d\le ab`,

\[
\max\{0,d-a-b\}
\le
ab-a-b
=\delta(a,b).
\]

By Lemma 2.1 a connected graph exists with the same maximum edge count, hence

\[
M_c(\mathbf c')
\ge
M_c(\mathbf c)-\delta(a,b).
\]

Using

\[
\sum\mathbf c'
=\sum\mathbf c-\delta(a,b),
\]

we obtain

\[
\begin{aligned}
\lambda(\mathbf c')
&=\sum\mathbf c'-2M_c(\mathbf c')\\
&\le
\sum\mathbf c-\delta
-2(M_c(\mathbf c)-\delta)\\
&=\lambda(\mathbf c)+\delta.
\end{aligned}
\]

Thus

\[
\lambda(\mathbf c')-\lambda(\mathbf c)
\le\delta(a,b).
\qquad\square
\]

---

## 4. Sharpness for every local split

### Theorem 4.1

For every `a,b\ge2`, put

\[
c=ab,
\qquad
\delta=c-a-b.
\]

There exists an ambient capacity vector for which the refinement `c\to(a,b)` increases the minimum free boundary by exactly `\delta`.

### Construction

Take the coarse vector consisting of `c+1` copies of `c`:

\[
\mathbf C=(\underbrace{c,\ldots,c}_{c+1}).
\]

The complete graph `K_{c+1}` has degree `c` at every vertex, so it saturates all ports:

\[
\boxed{\lambda(\mathbf C)=0.}
\]

Now refine one copy of `c`:

\[
\mathbf C'
=(a,b,\underbrace{c,\ldots,c}_{c\text{ copies}}).
\]

### Upper construction

On the `c` high-capacity vertices, form `K_c`. Each high vertex then has degree `c-1` and one unused port.

Because

\[
a+b\le ab=c
\]

for all `a,b\ge2`, choose disjoint sets of `a` and `b` high vertices. Join the `a`-vertex to the first set and the `b`-vertex to the second set.

The two low-capacity vertices are saturated. Exactly `a+b` high vertices gain their last edge and become saturated. The remaining

\[
c-a-b=\delta
\]

high vertices each retain exactly one free port. Therefore

\[
\lambda(\mathbf C')\le\delta.
\]

### Matching lower bound

Any admissible graph on `\mathbf C'` contains at most

\[
\binom c2
\]

edges among the `c` high-capacity vertices.

The total number of edges incident with at least one of the two refined vertices is at most `a+b`: if the edge between them is absent this is immediate from their degree capacities; if it is present, it consumes two degree units while contributing only one edge, so the bound is even smaller.

Hence

\[
|E(G)|\le\binom c2+a+b.
\]

Since the total capacity is

\[
c^2+a+b,
\]

we get

\[
\begin{aligned}
B(G)
&\ge c^2+a+b
-2\left(\binom c2+a+b\right)\\
&=c-a-b\\
&=\delta.
\end{aligned}
\]

Thus

\[
\boxed{
\lambda(\mathbf C')=\delta=ab-a-b.
}
\]

Therefore the bound of Theorem 3.1 is globally sharp for every pair `a,b\ge2`. `\square`

---

## 5. Exact worst-case inversion amplitude

Combining the two theorems gives the compact statement

\[
\boxed{
\sup_{\text{ambient decompositions}}
\Bigl(
\lambda(\ldots,a,b,\ldots)
-
\lambda(\ldots,ab,\ldots)
\Bigr)
=ab-a-b.
}
\]

So refinement inversion is not bounded by any universal constant.

Examples:

\[
4\to2\cdot2:\qquad \Delta\lambda_{\max}=0,
\]

\[
6\to2\cdot3:\qquad \Delta\lambda_{\max}=1,
\]

\[
8\to2\cdot4:\qquad \Delta\lambda_{\max}=2,
\]

\[
9\to3\cdot3:\qquad \Delta\lambda_{\max}=3,
\]

and the quantity grows without bound with `a,b`.

A particularly clean corollary is that the split

\[
4\to2\cdot2
\]

can never increase the minimum free boundary in the simple-network model, whereas every nontrivial split other than `2\cdot2` has ambient examples producing a strict inversion.

---

## 6. Iterated refinement corollary

Suppose `\mathbf d` is obtained from `\mathbf c` by a sequence of multiplicative refinements. Let

\[
S(\mathbf c)=\sum_i c_i.
\]

At each step the sharp one-step bound equals exactly the loss of total capacity at that step. Summing gives

\[
\boxed{
\lambda(\mathbf d)-\lambda(\mathbf c)
\le
S(\mathbf c)-S(\mathbf d).
}
\]

Equivalently,

\[
\boxed{
\lambda(\mathbf d)+S(\mathbf d)
\le
\lambda(\mathbf c)+S(\mathbf c).
}
\]

Thus although `\lambda` itself is not monotone under multiplicative refinement, the corrected quantity

\[
\lambda(\mathbf c)+S(\mathbf c)
\]

is refinement-nonincreasing.

This monotone is a consequence of the capacity-network model and should not be presented as a classical arithmetic invariant.

---

## 7. Status

This theorem replaces the earlier conjecture that one-step inversion might be bounded by one. That conjecture is false.

The exact sharp amplitude `ab-a-b` is now proved. Before publication, it still requires a literature audit against maximum degree-constrained subgraph / b-matching sensitivity and graph-detachment results.
