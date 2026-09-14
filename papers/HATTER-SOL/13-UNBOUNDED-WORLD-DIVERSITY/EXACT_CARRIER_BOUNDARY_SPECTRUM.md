# HATTER-SOL-13 · Exact Carrier Boundary Spectrum

**Status:** exact theorem layer  
**Probe:** fixed rational integer `2`  
**World:** `K_k = Q(zeta_{2^k-1})`

Let

\[
g_k=\frac{\varphi(2^k-1)}{k},
\]

and use the residue-degree port lift from `RESIDUE_DEGREE_CARRIER_DICHOTOMY.md`. Every one of the `g_k` prime-ideal vertices above `2` has capacity `k`.

For a connected simple feasible carrier `G`,

\[
B_f(G)=g_k k-2|E(G)|,
\qquad
\deg_G(v)\le k.
\]

For all sufficiently large `k`, we have `g_k>k`, so the explicit connected simple `k`-regular circulant carrier `S_k` exists.

## 1. Hamiltonian backbone

The construction of `S_k` contains every edge

\[
\{x,x+1\},\qquad x\in\mathbb Z/g_k\mathbb Z.
\]

Hence it contains the Hamiltonian cycle

\[
0-1-2-\cdots-(g_k-1)-0.
\]

Delete the final edge `{g_k-1,0}`. The remaining graph is a Hamiltonian path `P_k` with

\[
|E(P_k)|=g_k-1.
\]

Because `P_k` is a subgraph of `S_k`, all local degree constraints remain satisfied.

## 2. Exact edge-count interpolation

Enumerate the edges of

\[
E(S_k)\setminus E(P_k)
\]

arbitrarily as

\[
e_1,\ldots,e_M.
\]

For `0<=j<=M`, define

\[
G_{k,j}:=P_k\cup\{e_1,\ldots,e_j\}.
\]

Every `G_{k,j}` is

1. simple, because it is a subgraph of `S_k`;
2. connected, because it contains `P_k`;
3. capacity-feasible, because every vertex degree is at most its degree `k` in `S_k`.

Moreover

\[
|E(G_{k,j})|=g_k-1+j.
\]

Since `S_k` is `k`-regular,

\[
|E(S_k)|=\frac{g_k k}{2}.
\]

Therefore every integer edge count

\[
\boxed{
g_k-1\le e\le\frac{g_k k}{2}}
\]

is realized by a connected simple capacity-feasible carrier.

## 3. Exact spectrum theorem

### Theorem C13.7 — complete connected boundary spectrum

For all sufficiently large `k`, the set of scalar residue-degree HATTER boundary values over all connected simple feasible carriers on the prime ideals above `2` is exactly

\[
\boxed{
\mathcal B_k
=
\{g_k k-2e:\ g_k-1\le e\le g_k k/2\}.
}
\]

Equivalently,

\[
\boxed{
\mathcal B_k
=
\{0,2,4,\ldots,g_k(k-2)+2\}.
}
\]

### Proof

For any connected carrier on `g_k` vertices,

\[
|E|\ge g_k-1.
\]

The capacity constraint gives

\[
2|E|=\sum_v\deg(v)\le g_k k,
\]

so

\[
|E|\le g_k k/2.
\]

Thus no boundary outside the displayed set is possible.

Section 2 constructs a feasible connected carrier for every integer edge count in the full interval. Substitution into

\[
B_f=g_k k-2|E|
\]

gives every even boundary from `g_k(k-2)+2` down to `0`. QED.

## 4. Spectrum size

The number of distinct connected-carrier boundary values in world `K_k` is therefore

\[
|\mathcal B_k|
=
\frac{g_k(k-2)+2}{2}+1.
\]

Hence

\[
\boxed{
|\mathcal B_k|
=\frac{g_k(k-2)}2+2.
}
\]

Since `g_k->infinity` and `k->infinity`,

\[
\boxed{|\mathcal B_k|\to\infty.}
\]

This is stronger than exhibiting one sparse and one saturated carrier: each single sufficiently large arithmetic world already supports an unboundedly growing finite interval of distinct carrier responses as `k` increases.

## 5. Exact interpolation interpretation

The two extreme theorems from `RESIDUE_DEGREE_CARRIER_DICHOTOMY.md` are the endpoints of one exact spectrum:

\[
\boxed{
P_k\quad\leadsto\quad B_{max}=g_k(k-2)+2,
}
\]

\[
\boxed{
S_k\quad\leadsto\quad B_{min}=0.
}
\]

Each additional internal edge lowers the boundary by exactly two ports.

Thus carrier memory loss in this model is not merely qualitative. It has a complete one-dimensional filtration indexed by edge count.

## 6. Claim boundary

This theorem is exact for the scalar residue-degree port lift and the class of connected simple feasible carriers.

It does not yet imply an exact spectrum for the richer HATTER-SOL-10 ideal typed frontier, nor any entropy or coding statement.
