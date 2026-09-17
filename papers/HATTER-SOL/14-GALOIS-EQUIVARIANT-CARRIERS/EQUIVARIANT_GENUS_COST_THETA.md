# HATTER-SOL-14 · Equivariant Genus Cost Has the Same Asymptotic Order

**Status:** exact theorem layer

Fix `0<eta<=1`. Let

\[
\gamma_k^{\mathrm{Gal}}(\eta)
\]

be the minimum orientable genus among connected simple Galois-equivariant carriers on the prime ideals above `2` whose boundary satisfies

\[
B_f\le (1-\eta)n_k k,
\qquad
n_k=\frac{\varphi(2^k-1)}k.
\]

By the Cayley reduction, such carriers are `Cay(Gamma_k,S)` with inverse-closed generating sets `S`, and

\[
B_f=n_k(k-|S|).
\]

Thus exhausting at least an `eta` fraction requires `|S|>=eta k`.

## Lemma H14.7 — sublinear generator rank

Let

\[
r_k=\omega(2^k-1).
\]

Then

\[
\boxed{r_k=o(k).}
\]

### Proof

If an integer has `r` distinct prime divisors, it is at least the product of the first `r` primes, and hence at least `r!`. Therefore

\[
r_k!\le 2^k-1<2^k.
\]

For `r>=2`, at least `r/2` factors among `1,2,...,r` are at least `r/2`, so

\[
r!\ge (r/2)^{r/2}.
\]

Thus

\[
\frac{r_k}{2}\log(r_k/2)<k\log2.
\]

This implies `r_k=O(k/log k)`, hence `r_k=o(k)`. QED.

Since `d(Gamma_k)<=r_k`, an inverse-closed generating seed has size at most `2r_k=o(k)`.

## Lemma H14.8 — equivariant degree interpolation at linear scale

For every fixed `eta>0`, and all sufficiently large `k`, there exists an inverse-closed generating set `S_k` with

\[
\eta k\le |S_k|\le \eta k+2.
\]

### Proof

Start with an inverse-closed generating seed of size `o(k)`, so eventually its size is less than `eta k`. If necessary, adjust parity by adjoining one unused involution exactly as in Theorem H14.6. The complement is invariant under inversion and decomposes into orbits of sizes one and two. Since `n_k>k` for large `k`, there are enough unused elements to add inversion orbits until the first admissible cardinality at least `eta k` is reached. Orbit sizes are at most two, so the overshoot is at most two. QED.

## Theorem H14.9 — equivariant erasure cost

For every fixed `0<eta<=1`,

\[
\boxed{
\gamma_k^{\mathrm{Gal}}(\eta)=\Theta(n_k k).
}
\]

### Lower bound

Every equivariant carrier is in particular a connected simple carrier. Therefore the H13 surface bound applies:

\[
\gamma_k^{\mathrm{Gal}}(\eta)
\ge
\left(\frac{\eta}{12}-o(1)\right)n_k k.
\]

### Upper bound

Choose `S_k` from H14.8 and let

\[
C_k=\operatorname{Cay}(\Gamma_k,S_k).
\]

Then `C_k` is connected, simple, and Galois-equivariant, with degree

\[
d_k=|S_k|\le \eta k+2.
\]

Hence

\[
|E(C_k)|=\frac{n_kd_k}{2}.
\]

Any connected graph with `V` vertices and `E` edges embeds in an orientable surface of genus at most its cycle rank `E-V+1`: embed a spanning tree in the sphere and route each remaining edge through its own handle. Therefore

\[
\gamma(C_k)
\le
\frac{n_kd_k}{2}-n_k+1
\le
\frac{\eta}{2}n_k k+O(n_k).
\]

Thus

\[
\gamma_k^{\mathrm{Gal}}(\eta)=O(n_k k).
\]

Combining both bounds proves the theorem. QED.

## Consequence

Galois equivariance alone does not create a new asymptotic genus barrier:

\[
\boxed{
\gamma_k^{\mathrm{Gal}}(\eta)
\asymp
\gamma_k(\eta)
\asymp
n_k k.
}
\]

The exact constants may differ, but there is no divergent equivariant/unrestricted gap at the level of growth order.

## Programme consequence

Two natural scalar H14 hypotheses are now closed negatively:

1. symmetry does not forbid complete exhaustion for large `k`;
2. symmetry does not increase the asymptotic order of fixed-fraction genus cost.

The next serious target is therefore not scalar boundary/genus but **equivariant homological structure**, especially the `Z[Gamma_k]`-module carried by `H_1`.