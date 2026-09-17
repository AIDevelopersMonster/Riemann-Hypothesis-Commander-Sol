# HATTER-SOL-14 · Exact Equivariance-to-Cayley Reduction

**Status:** exact theorem layer

Let

\[
\Gamma_k=(\mathbb Z/(2^k-1)\mathbb Z)^\times/\langle 2\rangle
\]

act regularly on the set `X_k` of prime ideals above `2` in
`K_k=Q(zeta_{2^k-1})`. Choose one base vertex `x_0` and identify

\[
X_k\cong\Gamma_k,\qquad g\leftrightarrow g x_0.
\]

A simple undirected graph `C` on `X_k` is called equivariant when the regular `Gamma_k` action preserves adjacency.

## Theorem H14.1

Every simple undirected `Gamma_k`-equivariant graph on `X_k` is uniquely of the form

\[
\operatorname{Cay}(\Gamma_k,S)
\]

for a subset `S` satisfying

\[
1\notin S,\qquad S=S^{-1}.
\]

It is connected exactly when

\[
\langle S\rangle=\Gamma_k.
\]

### Proof

Let `1` denote the vertex corresponding to `x_0` and define

\[
S=\{s\in\Gamma_k:\{1,s\}\in E(C)\}.
\]

Simplicity gives `1 notin S`. Since the graph is undirected, `{1,s}` is an edge iff `{s,1}` is an edge. Translating the latter by `s^{-1}` gives `{1,s^{-1}}`, so `S=S^{-1}`.

Now for arbitrary `g,h`, equivariance under translation by `g^{-1}` gives

\[
\{g,h\}\in E(C)
\iff
\{1,g^{-1}h\}\in E(C)
\iff
g^{-1}h\in S.
\]

Thus `C=Cay(Gamma_k,S)`. The neighbor set of `1` recovers `S`, giving uniqueness.

Finally, a vertex `g` is reachable from `1` precisely when `g` is a product of elements of `S`; hence the connected component of `1` is `<S>`. Therefore `C` is connected iff `<S>=Gamma_k`. QED.

## Corollary H14.2 — exact boundary law

If `C=Cay(Gamma_k,S)` is connected and every vertex has H13 capacity `k`, then `C` is `|S|`-regular and

\[
\boxed{B_f(C)=n_k(k-|S|)},
\qquad n_k=|\Gamma_k|=\frac{\varphi(2^k-1)}{k}.
\]

Hence complete port-budget exhaustion in the equivariant class is equivalent to the existence of an inverse-closed generating set of exact cardinality `k`.

## Claim boundary

The Cayley classification is a standard consequence of a regular group action (Sabidussi-type viewpoint). H14 novelty cannot rest on H14.1 alone; it must come from arithmetic restrictions on the connection sets, genus cost, or equivariant homology.