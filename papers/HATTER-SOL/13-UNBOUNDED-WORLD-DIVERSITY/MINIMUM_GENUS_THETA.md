# HATTER-SOL-13 · Minimum Genus Theorem

Set `n_k = phi(2^k-1)/k`. For a connected simple degree-feasible carrier define

\[
B_f(G)=n_k k-2|E(G)|.
\]

For fixed `0<eta<=1`, let `gamma_k(eta)` be the minimum orientable genus among carriers satisfying

\[
B_f(G)\le(1-\eta)n_k k.
\]

The previously proved surface-genus bound gives

\[
\gamma_k(\eta)
\ge
\frac{\eta}{12}n_k k-\frac{n_k}{2}+1.
\]

For the converse, choose

\[
m=\left\lceil\eta n_k k/2\right\rceil.
\]

For all sufficiently large `k`, the exact carrier-spectrum theorem supplies a connected simple feasible carrier with exactly `m` edges. Every connected graph with `n` vertices and `m` edges embeds in an orientable surface of genus at most `m-n+1`: embed a spanning tree in the sphere and route each of the remaining `m-n+1` edges through its own handle. Therefore

\[
\gamma_k(\eta)
\le
\frac{\eta}{2}n_k k-n_k+2.
\]

Hence, for every fixed `eta>0`,

\[
\boxed{\gamma_k(\eta)=\Theta(n_k k).}
\]

The growth order is sharp; the leading constant is not. The current bounds place it between `eta/12` and `eta/2`. Determining the optimal constant remains open.

This theorem applies only to the stated connected-simple residue-degree port model.