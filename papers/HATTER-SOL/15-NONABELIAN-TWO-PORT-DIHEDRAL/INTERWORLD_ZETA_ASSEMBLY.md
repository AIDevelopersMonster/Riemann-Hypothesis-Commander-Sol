# HATTER-SOL-15 · Inter-World Zeta Assembly

**Status:** exact theorem layer; Artin factorization is classical, H15 contribution is the world-assembly interpretation.

Let `E/Q` be imaginary quadratic, let

\[
V=\operatorname{Cl}(E)/p\operatorname{Cl}(E)\cong\mathbb F_p^r,
\]

and let `M/E` be the elementary abelian unramified `p`-class extension with

\[
\operatorname{Gal}(M/E)\cong V.
\]

Complex conjugation acts by inversion, so

\[
G_*:=\operatorname{Gal}(M/\mathbb Q)\cong V\rtimes C_2.
\]

Let `K_*=M^{C_2}` be the degree-`p^r` reflection-fixed side field.

For each hyperplane `H<V`, let `M^H/E` be the corresponding cyclic degree-`p` extension and let `K_H/Q` be its degree-`p` reflection-fixed side field. The set of worlds is

\[
\mathcal W=\mathbb P(V^*).
\]

## Theorem H15.31 — representation assembly

Let `V_{0,H}` be the centered permutation representation of the world `K_H`, and let `V_{0,*}` be the centered permutation representation of the large world `K_*`.

Then

\[
\boxed{
\bigoplus_{H\in\mathcal W}V_{0,H}
\cong
V_{0,*}
}
\]

as complex representations of `G_*` after inflating each quotient-world representation along `G_* -> (V/H)\rtimes C_2`.

### Proof

The permutation representation of `G_*` on the `p^r` cosets of `C_2` restricts to the regular representation of `V`. Hence

\[
V_{0,*}|_V
\cong
\mathbb C[V]\ominus\mathbf1,
\]

which is the direct sum of all nontrivial characters of `V`, each once.

For a hyperplane `H`, the centered degree-`p` world representation restricts to the augmentation representation of `V/H`. Inflated to `V`, it is the direct sum of the `p-1` nontrivial characters whose kernel is exactly `H`.

Every nontrivial character of `V` has a unique kernel hyperplane. Therefore the sets of nontrivial characters contributed by distinct `H` are disjoint and partition all nontrivial characters of `V`. Compatibility with inversion by `C_2` preserves the decomposition under the full generalized-dihedral action. QED.

Dimension check:

\[
\sum_H\dim V_{0,H}
=\frac{p^r-1}{p-1}(p-1)
=p^r-1
=\dim V_{0,*}.
\]

## Theorem H15.32 — zeta assembly identity

Artin formalism gives

\[
L(s,V_{0,H})=\frac{\zeta_{K_H}(s)}{\zeta(s)},
\qquad
L(s,V_{0,*})=\frac{\zeta_{K_*}(s)}{\zeta(s)}.
\]

By H15.31 and multiplicativity of Artin `L`-functions under direct sum,

\[
\boxed{
\prod_{H\in\mathcal W}
\frac{\zeta_{K_H}(s)}{\zeta(s)}
=
\frac{\zeta_{K_*}(s)}{\zeta(s)}.
}
\]

Equivalently,

\[
\boxed{
\prod_{H\in\mathcal W}\zeta_{K_H}(s)
=
\zeta_{K_*}(s)\,\zeta(s)^{N-1},
\qquad
N=\frac{p^r-1}{p-1}.
}
\]

This identity holds first in the absolute-convergence half-plane and then meromorphically by analytic continuation.

## Corollary H15.33 — observer-signal assembly

Let

\[
\widetilde\Psi_H(x)=\psi_{K_H}(x)-\psi(x),
\qquad
\widetilde\Psi_*(x)=\psi_{K_*}(x)-\psi(x).
\]

Then the logarithmic-derivative identity yields

\[
\boxed{
\sum_{H\in\mathcal W}\widetilde\Psi_H(x)
=
\widetilde\Psi_*(x)
}
\]

at the level of prime-power coefficients, and therefore exactly for the cumulative Chebyshev sums with the same ramified-prime conventions.

Thus the centered observer signals of all degree-`p` worlds assemble without overlap or deficit into the centered signal of the degree-`p^r` world.

## Interpretation

The ensemble is not merely a list of parallel arithmetic worlds. It is a resolution of one larger generalized-dihedral world into projective one-dimensional quotient directions:

\[
\boxed{
\text{many }p\text{-sector worlds}
\longleftrightarrow
\text{one }p^r\text{-sector world}.
}
\]

At three levels simultaneously:

1. nontrivial characters partition by kernel hyperplane;
2. centered observer traces add;
3. relative zeta functions multiply.

This is the global analytic companion to the projective tomography theorem.

## Claim discipline

Artin formalism, character decomposition, and zeta relations from representation identities are classical. H15 does not claim a new general Brauer relation. The H15-specific synthesis is that the complete family of dihedral class-field worlds indexed by `P(V*)` furnishes an exact projective resolution of the generalized-dihedral large-world observer and zeta signal.