# HATTER-SOL-14 · Integral Equivariant Homology Separation

**Status:** exact corollary of the rational separation theorem

Let `C_{k,1}` and `C_{k,2}` be the infinite family of same-abstract-graph Galois-equivariant carriers constructed for all sufficiently large

\[
k\equiv15\pmod{30}.
\]

The rational theorem proves

\[
H_1(C_{k,1};\mathbb Q)
\not\cong
H_1(C_{k,2};\mathbb Q)
\]

as `Q[Gamma_k]`-modules.

## Corollary H14.15 — integral separation

For the same infinite family,

\[
\boxed{
H_1(C_{k,1};\mathbb Z)
\not\cong
H_1(C_{k,2};\mathbb Z)
}
\]

as `Z[Gamma_k]`-modules.

### Proof

Suppose an isomorphism of `Z[Gamma_k]`-modules existed. Tensoring it over `Z` with `Q` would give an isomorphism

\[
H_1(C_{k,1};\mathbb Z)\otimes\mathbb Q
\cong
H_1(C_{k,2};\mathbb Z)\otimes\mathbb Q
\]

as `Q[Gamma_k]`-modules. Since graph homology is torsion-free in degree one,

\[
H_1(C;\mathbb Z)\otimes\mathbb Q
\cong
H_1(C;\mathbb Q).
\]

This contradicts the rational character separation theorem. QED.

## Consequence

The additional structural memory is not merely an artifact of rational representation theory. The same abstract graph can carry genuinely different **integral arithmetic actions on its cycle lattice**.

Thus the H14 hierarchy strengthens to

\[
\boxed{
\text{abstract graph}
<
\text{equivariant integral cycle lattice}.
}
\]

The ordinary abstract homology groups remain identical because the graphs themselves are isomorphic; the distinction lies entirely in the retained arithmetic group action.