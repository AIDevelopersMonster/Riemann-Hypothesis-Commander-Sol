# HATTER-SOL-11 · PRIME 61 SAME-INTEGER WORLD TABLE

**Status:** partial exact theorem layer; unresolved cells are marked explicitly.

Take the fixed rational integer

\[
N=61^{23}.
\]

This choice is canonical for the present laboratory: in split worlds it produces 46 irreducible factor nodes, matching the current Gaussian `(6,5)` order-46 problem; in inert worlds it produces only 23 nodes. Hence this file implements the fixed-host / same-integer distinction from `WORLD_GEOMETRY_RESPONSE_CALCULUS.md`.

## 1. UFD world classification

Across the nine imaginary quadratic class-number-one worlds, `61` is split for discriminants

\[
-4,-3,-19,-163
\]

and inert for

\[
-8,-7,-11,-43,-67.
\]

The split-world folded states are

\[
\Pi_{-4}(61)=(6,5),\qquad
\Pi_{-3}(61)=(5,4),\qquad
\Pi_{-19}(61)=(7,1),\qquad
\Pi_{-163}(61)=(4,1).
\]

In the inert worlds the local state is `(61,0)`.

Therefore

\[
\kappa_R(61^{23})=
\begin{cases}
46,&61\text{ split in }R,\\
23,&61\text{ inert in }R.
\end{cases}
\]

## 2. Exact inert response

For an inert world the canonical network has 23 identical `(61,0)` nodes. A planar graph on 23 vertices has at most

\[
3\cdot23-6=63
\]

edges, and a planar triangulation attains this bound. The capacity 61 is nonbinding. Hence

\[
B_P=23\cdot61-2\cdot63=1277,
\qquad B_Q=0.
\]

### Theorem P61.1

For every inert class-number-one world

\[
\Delta\in\{-8,-7,-11,-43,-67\},
\]

\[
\boxed{
\mathcal R^{\Xi,\mathrm{can}}_{Pl,\Delta}(61^{23})=\{(1277,0)\}
}
\]

and

\[
\boxed{Z^{\Xi,\mathrm{can}}_{Pl,\Delta}=X^{1277}.}
\]

## 3. Exact `Delta=-19` response

Here the canonical split state is `(7,1)` on 46 nodes. By the established unit-tail theorem,

\[
\boxed{
\mathcal R^{\Xi,\mathrm{can}}_{Pl,-19}(61^{23})
=
\{(58+2t,46-2t):0\le t\le23\}.
}
\]

Thus

\[
\boxed{
Z^{\Xi,\mathrm{can}}_{Pl,-19}
=
\sum_{t=0}^{23}X^{58+2t}Y^{46-2t}.
}
\]

Every Pareto point has total boundary 104.

## 4. Exact `Delta=-163` closure

Here the canonical state is `(4,1)` on 46 nodes. The HATTER-SOL-11 support-existence input supplies a 5-connected 5-regular planar support of this order.

### Lemma P61.2

Every 5-edge-connected 5-regular graph has a perfect matching.

### Proof

For any vertex set `S`, let `C` be an odd component of `G-S`. Since

\[
5|C|=2|E(C)|+|\delta(C)|,
\]

the cut size `|delta(C)|` is odd. By 5-edge-connectivity it is at least 5. Therefore

\[
5\,o(G-S)
\le
\sum_C|\delta(C)|
\le
5|S|,
\]

so `o(G-S)<=|S|`. Tutte's theorem gives a perfect matching. QED.

A 5-connected 5-regular graph is 5-edge-connected because

\[
\kappa(G)\le\lambda(G)\le\delta(G)=5.
\]

Let `M` be a perfect matching in the 46-vertex planar support. Color `M` by `Q` and every remaining support edge by `P`. Then each vertex has Q-degree 1 and P-degree 4, so every port is saturated.

### Theorem P61.3

\[
\boxed{
\mathcal R^{\Xi,\mathrm{can}}_{Pl,-163}(61^{23})=\{(0,0)\},
\qquad
Z^{\Xi,\mathrm{can}}_{Pl,-163}=1.
}
\]

## 5. Exact status of the remaining split worlds

### Gaussian `Delta=-4`

The canonical state is `(6,5)` on 46 nodes. This is exactly the unresolved universal `r=17` balancing problem. Several local overload cases are closed, but no universal order-46 theorem has yet been proved. Therefore this canonical cell remains open.

### Eisenstein `Delta=-3`

The canonical state is `(5,4)` on 46 nodes. The antiprism construction gives the attained minimum-total segment

\[
\boxed{
(150-2t,2t),\qquad0\le t\le69.
}
\]

Its final point is `(12,138)`. The low-P tail

\[
B_P\in\{0,2,4,6,8,10\}
\]

remains unresolved, so the full Pareto front is not yet claimed.

## 6. Canonical same-integer table

| discriminant(s) | 61 | nodes for `61^23` | state | planar response |
|---|---:|---:|---:|---|
| `-4` | split | 46 | `(6,5)` | open: Gaussian `r=17` |
| `-3` | split | 46 | `(5,4)` | exact long segment; low-P tail open |
| `-19` | split | 46 | `(7,1)` | exact line, total boundary 104 |
| `-163` | split | 46 | `(4,1)` | exact `{(0,0)}` |
| `-8,-7,-11,-43,-67` | inert | 23 | `(61,0)` | exact `{(1277,0)}` |

## 7. Consequence

The same rational integer occupies sharply different regimes depending on arithmetic world:

- critical five-tail balancing;
- sub-six mixed threshold;
- unit-tail permanent-memory regime;
- full planar closure;
- inert rational-axis regime with a different canonical host size.

Therefore the Gaussian complement parameter `r` is a local chart coordinate, not an invariant of the integer.

## 8. Next targets

1. Close the Eisenstein `(5,4)` low-P tail at order 46.
2. Continue Gaussian `r=17`, next beginning with the unclosed one-center `(d,q)=(9,8)` case.
3. Build the first exact world-geometry rectangle using worlds whose planar cells are already closed, then evaluate the mixed response from `WORLD_GEOMETRY_RESPONSE_CALCULUS.md`.
