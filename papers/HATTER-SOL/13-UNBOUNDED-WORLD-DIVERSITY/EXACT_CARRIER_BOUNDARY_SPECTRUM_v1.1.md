# HATTER-SOL-13 · Exact Carrier Boundary Spectrum v1.1

**Status:** exact theorem layer, referee-corrected.

Set

\[
n_k:=\frac{\varphi(2^k-1)}{k}.
\]

Each prime-ideal vertex above `2` has capacity `k`, and

\[
B_f(G)=n_k k-2|E(G)|,
\qquad \deg_G(v)\le k.
\]

## Explicit threshold

For odd `m`, `phi(m)>=sqrt(m)`, hence

\[
n_k\ge\frac{\sqrt{2^k-1}}{k}.
\]

At `k=17`, `2^17-1>17^4`; and for `k>=6`,

\[
2k^4+1>(k+1)^4.
\]

Induction gives `2^k-1>k^4` for every `k>=17`, so

\[
\boxed{n_k>k\quad(k\ge17).}
\]

Also `n_k k=phi(2^k-1)` is even. Therefore a connected simple `k`-regular circulant carrier `S_k` exists for every `k>=17`.

## Hamiltonian interpolation

The step-1 edges of `S_k` form a Hamiltonian cycle. Choose that cycle as a subgraph and delete one cycle edge. The resulting **cycle subgraph** is a Hamiltonian path `P_k` with `n_k-1` edges; the remaining chords of `S_k` are not part of `P_k` yet.

Add the edges of `S_k\setminus P_k` one at a time. Every intermediate graph remains simple, connected, and degree-feasible. Hence every edge count

\[
\boxed{n_k-1\le e\le\frac{n_k k}{2}}
\]

is realized.

## Theorem C13.7 v1.1

For every `k>=17`, the complete scalar boundary spectrum over connected simple feasible carriers is

\[
\boxed{
\mathcal B_k
=
\{0,2,4,\ldots,n_k(k-2)+2\}.
}
\]

Indeed, connectivity forces `|E|>=n_k-1`, while degree feasibility gives `2|E|<=n_k k`; the construction above realizes every integer edge count between these extremes.

Consequently

\[
\boxed{|\mathcal B_k|=\frac{n_k(k-2)}2+2\to\infty.}
\]

## Claim boundary

This theorem is exact for the chosen residue-degree port model and connected simple carriers. The graph carrier is additional model structure, not an intrinsic arithmetic invariant. No Galois-equivariance, entropy, coding, or payload claim is imposed.