# HATTER-SOL-11 · Exact Planar Capacity-Five Floor

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

This note closes the one-channel capacity-five extremal problem left open after the capacity-six barrier theorem and isolates the only exceptional even host size.

## 1. Definition

For even `n>=4`, define

\[
\mu_{Pl,n}(5)
:=
\min\{5n-2|E(G)|:\ G\text{ is connected, simple, planar, }\Delta(G)\le5\}.
\]

Equivalently, if

\[
M_5(n):=\max\{|E(G)|:\ G\text{ connected, simple, planar, }\Delta(G)\le5\},
\]

then

\[
\mu_{Pl,n}(5)=5n-2M_5(n).
\]

Two universal upper bounds are

\[
M_5(n)\le3n-6
\]

and

\[
M_5(n)\le\frac{5n}{2}.
\]

Hence

\[
M_5(n)\le\min\left(3n-6,\frac{5n}{2}\right).
\]

## 2. Small even hosts `4<=n<=12`

For `n<=12`, the planar edge ceiling is the active bound.

It is sharp for every even `n=4,6,8,10,12` with maximum degree at most five:

- `n=4`: `K_4`;
- `n=6`: the octahedral graph;
- `n=8`: the square antiprism with one diagonal inserted in each of its two square faces;
- `n=10`: the square antiprism capped by one new apex in each square face, each apex joined to the four vertices of that face (the gyroelongated square-bipyramid graph);
- `n=12`: the icosahedral graph.

Each construction is a planar triangulation with `3n-6` edges and maximum degree at most five. Therefore

\[
M_5(n)=3n-6
\]

and

\[
\boxed{\mu_{Pl,n}(5)=12-n}
\]

for even `4<=n<=12`.

Thus the values are

\[
8,6,4,2,0
\]

at host sizes

\[
4,6,8,10,12.
\]

## 3. The exceptional host `n=14`

A 5-regular simple planar graph on fourteen vertices does not exist. This is the exceptional degree-five/order-fourteen case in the classical classification of planar regular incidence sequences due to A. B. Owens.

Therefore

\[
M_5(14)\le34
\]

because `35` edges together with `Delta<=5` would force every vertex to have degree exactly five.

The bound `34` is attained explicitly.

Start with the hexagonal antiprism on twelve ring vertices. It is planar and 4-regular, with two hexagonal faces. Add one apex inside each hexagonal face and join it to all six vertices of that face. The resulting graph is a triangulation on fourteen vertices with

\[
36=3\cdot14-6
\]

edges. The twelve ring vertices have degree five and the two apices have degree six.

Delete one apex-to-ring edge at the top apex and one apex-to-ring edge at the bottom apex, choosing distinct ring endpoints. The graph remains connected and planar, now has `34` edges, and every degree is at most five.

Hence

\[
M_5(14)=34
\]

and

\[
\boxed{\mu_{Pl,14}(5)=2.}
\]

## 4. All even hosts `n>=16`

We use the classical regular-planar existence theorem: a simple planar 5-regular realization exists for every even order satisfying the Euler bound, except order fourteen. In particular, for every even

\[
n\ge16
\]

there exists a connected simple planar 5-regular graph.

Thus

\[
M_5(n)=\frac{5n}{2}
\]

and

\[
\boxed{\mu_{Pl,n}(5)=0}
\]

for every even `n>=16`.

A modern recursive-generation reference confirming the connected 5-regular planar class is:

Mahdieh Hasheminezhad, Brendan D. McKay, Tristan Reeves, *Recursive generation of simple planar 5-regular graphs and pentangulations*, Journal of Graph Algorithms and Applications 15(3), 417–436 (2011).

The classical regular-sequence source is:

A. B. Owens, *On the planarity of regular incidence sequences*, Journal of Combinatorial Theory, Series B 11(3), 201–212 (1971), DOI `10.1016/0095-8956(71)90030-X`.

## 5. Exact floor theorem

### Theorem T11.55 — exact planar capacity-five floor

For every even `n>=4`,

\[
\boxed{
\mu_{Pl,n}(5)=
\begin{cases}
12-n,&4\le n\le12,\\
2,&n=14,\\
0,&n\ge16.
\end{cases}}
\]

Equivalently,

\[
\boxed{
M_5(n)=
\begin{cases}
3n-6,&4\le n\le12,\\
34,&n=14,\\
5n/2,&n\ge16,
\end{cases}}
\]

for even `n`.

The host-size sequence of capacity-five defects is therefore

\[
\boxed{
8,6,4,2,0,2,0,0,0,\ldots
}
\]

for

\[
n=4,6,8,10,12,14,16,18,20,\ldots
\]

The return from `0` to `2` at `n=14` is the unique regular-planar anomaly in this range.

## 6. Exact consequence for the `(6,5)` rank swap

For the mixed state

\[
\Xi_I=(6,5),
\]

the minimum axial boundary is

\[
\boxed{\min B_A=12}
\]

for every even host, by the capacity-six theorem.

For the swapped state

\[
\Xi_{II}=(5,6),
\]

the minimum axial boundary is exactly the one-channel floor above, because a graph attaining `mu_{Pl,n}(5)` may be used with no edges in the second channel:

\[
\boxed{\min B_A=\mu_{Pl,n}(5).}
\]

Hence the exact minimum-exponent separation is

\[
\boxed{
12-\mu_{Pl,n}(5)=
\begin{cases}
n,&4\le n\le12,\\
10,&n=14,\\
12,&n\ge16.
\end{cases}}
\]

So the order-fourteen anomaly is visible directly in the orbital response as a temporary reduction of the rank-swap gap from `12` to `10`.

## 7. Exact `(6,5)` Pareto front through `n=14`

For every even

\[
4\le n\le14,
\]
we can choose a triangulation `T_n` with `Delta(T_n)<=6` that contains a maximum-edge capacity-five subgraph `H_5`:

- for `n<=12`, take the degree-at-most-five triangulations from Section 2 and let `H_5=T_n`;
- for `n=14`, take the capped hexagonal antiprism triangulation and let `H_5` be the graph obtained by deleting the two apex edges used in Section 3.

Let

\[
M_5(n)=|E(H_5)|.
\]

For any integer

\[
0\le t\le M_5(n),
\]
choose any `t` edges of `H_5` for the capacity-five channel and color every remaining edge of `T_n` by the capacity-six channel.

The two channel constraints are satisfied because

\[
\Delta(H_5)\le5,
\qquad
\Delta(T_n)\le6.
\]

The boundary vector is

\[
\boxed{
(B_A,B_O)=(12+2t,\ 5n-2t).
}
\]

Every point lies on the global minimum-total line

\[
B_A+B_O=5n+12.
\]

The coordinate floors are `B_A>=12` and `B_O>=mu_{Pl,n}(5)`, so the usual parity-and-domination argument proves exactness.

### Theorem T11.56 — exact small-host `(6,5)` front

For every even `4<=n<=14`,

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(6,5)
=
\{(12+2t,5n-2t):0\le t\le M_5(n)\}.
}
\]

Equivalently,

\[
\boxed{
Z^{\Xi}_{Pl,n}(6,5;X,Y)
=
\sum_{t=0}^{M_5(n)}X^{12+2t}Y^{5n-2t}.
}
\]

Thus the full Pareto front is now exact through the exceptional order fourteen.

## 8. What remains for `n>=16`

For even `n>=16`, the one-channel floor is already zero, but an exact full `(6,5)` front requires a **joint extension theorem**: one must understand how a 5-regular planar channel can coexist with enough disjoint capacity-six edges while preserving planarity of the combined support.

The bounded-degree antiprism triangulations already give a minimum-total Pareto segment down to a capacity-five residual at most `4`. Therefore any still-unresolved part of the front is confined to the terminal even boundary levels

\[
\boxed{B_O\in\{0,2\}}
\]

once the improved degree-six-vertex matching construction is used.

So after T11.55–T11.56, the infinite-host `(6,5)` problem has been reduced from an unrestricted planar optimization problem to a two-level terminal-tail question.