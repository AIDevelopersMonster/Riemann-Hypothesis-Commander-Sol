# HATTER-SOL-15 · Inter-World Projective Incidence Code

**Status:** exact theorem layer.

Continue with

\[
V=A/pA\cong\mathbb F_p^r,
\qquad
\mathcal W=\mathbb P(V^*)
\]

as in the projective tomography layer. Every world is a hyperplane `H<V`.

For a nonzero projective class `[a] in P(V)`, define its binary world-signature

\[
 c_a(H):=
 \begin{cases}
 0,&a\in H,\\
 1,&a\notin H.
 \end{cases}
\]

Thus `c_a(H)=0` means the split rational prime has identity Frobenius in world `H`, while `c_a(H)=1` means nontrivial rotation Frobenius.

The code length is

\[
\boxed{N=|\mathcal W|=\frac{p^r-1}{p-1}.}
\]

## Theorem H15.27 — constant weight

Every nonzero projective class has codeword weight

\[
\boxed{w(c_a)=p^{r-1}.}
\]

### Proof

The zero positions are precisely the hyperplanes containing `<a>`, of which there are

\[
\frac{p^{r-1}-1}{p-1}.
\]

Subtracting from `N` gives `p^{r-1}`. QED.

## Theorem H15.28 — exact pairwise distance

Let `[a] != [b]` be distinct projective points. Then

\[
\boxed{d_H(c_a,c_b)=2p^{r-2}.}
\]

### Proof

The two codewords differ exactly at hyperplanes containing one of `<a>`, `<b>` but not the other.

The number of hyperplanes containing `<a>` is

\[
N_0=\frac{p^{r-1}-1}{p-1}.
\]

Because `[a]!=[b]`, the span `<a,b>` has dimension two. Hyperplanes containing both correspond to hyperplanes of `V/<a,b>`, so their number is

\[
N_{00}=\frac{p^{r-2}-1}{p-1}
\]

for `r>=2` (and the theorem is vacuous for `r=1`).

Hence hyperplanes containing `a` but not `b` number

\[
N_0-N_{00}=p^{r-2},
\]

and symmetrically the same number contain `b` but not `a`. Therefore

\[
d_H(c_a,c_b)=2p^{r-2}.
\]

QED.

## Corollary H15.29 — exact correction radius

The projective world-signature code has minimum distance

\[
\boxed{d_{min}=2p^{r-2}.}
\]

Hence nearest-neighbor decoding uniquely corrects any pattern of at most

\[
\boxed{t=p^{r-2}-1}
\]

adversarially corrupted world-bits.

It detects every pattern of fewer than `2p^{r-2}` corruptions.

## Corollary H15.30 — relative robustness

For large `r`, the relative distance is

\[
\delta_r
=
\frac{2p^{r-2}}{(p^r-1)/(p-1)}
\longrightarrow
\boxed{\frac{2(p-1)}{p^2}}.
\]

Thus increasing the class-group rank grows the number of worlds while preserving a positive asymptotic separation between different projective ideal classes.

## Interpretation

A single world gives one coarse splitting bit. The entire ensemble gives a redundant incidence word. Therefore the inter-world family acts as a finite-geometric error-correcting layer:

\[
\boxed{
[\mathfrak q]\bmod pA
\to
\text{projective class}
\to
\text{splitting word across worlds}
\to
\text{robust recoverability}.
}
\]

This is distinct from the intra-world wheel diagnostics: there the redundancy lives in cycles of one carrier; here it lives across different arithmetic worlds.

## Claim discipline

The code is the binary incidence/complement code of projective points against hyperplanes, a classical finite-geometric object. H15 does not claim invention of projective incidence codes. The arithmetic content is that coarse Frobenius splitting signatures of the dihedral class-field ensemble realize this code exactly.