# HATTER-SOL-15 · Inter-World Projective Class-Group Tomography

**Status:** exact theorem layer.

Let `E/Q` be an imaginary quadratic field and let `p` be an odd prime. Put

\[
A=\operatorname{Cl}(E),
\qquad
V=A/pA,
\qquad
r=\dim_{\mathbb F_p}V.
\]

Assume `r>=1`. Let `M/E` be the unramified elementary abelian `p`-class field corresponding under class field theory to the subgroup `pA`. Then

\[
\operatorname{Gal}(M/E)\cong V.
\]

Complex conjugation acts on `A`, hence on `V`, by inversion, so

\[
\operatorname{Gal}(M/\mathbb Q)
\cong
V\rtimes C_2
\]

with the nontrivial element of `C_2` acting by `v -> -v`.

Every hyperplane `H<V` gives an index-`p` quotient `V/H\cong C_p`, hence an unramified cyclic extension `M^H/E` and a dihedral degree-`2p` Galois extension over `Q`. Let `K_H/Q` denote its degree-`p` reflection-fixed side field.

The set of such worlds is naturally

\[
\mathcal W_p(E)=\mathbb P(V^*)
\]

and has cardinality

\[
\boxed{N=\frac{p^r-1}{p-1}.}
\]

## Theorem H15.22 — coarse world signature of a split prime

Let `q` be a rational prime unramified in `M` and split in `E`:

\[
q\mathcal O_E=\mathfrak q\bar{\mathfrak q}.
\]

Let

\[
a=[\mathfrak q]\in A,
\qquad
\bar a=a\bmod pA\in V.
\]

For the world indexed by the hyperplane `H`, the Frobenius state of `q` in the degree-`p` field `K_H` is:

- **identity state** (splitting type `1^p`) iff `bar a in H`;
- **nontrivial rotation state** (splitting type `p`) iff `bar a notin H`.

### Proof

The Artin symbol of `mathfrak q` in `Gal(M/E)=V` is exactly its class modulo `pA`. Passing to the quotient `V/H` gives the Frobenius in the cyclic degree-`p` extension `M^H/E`. It is trivial exactly when `bar a in H`; otherwise it is a nonidentity element of the prime-order cyclic quotient. In the associated degree-`p` dihedral permutation action, identity has cycle type `1^p`, while every nontrivial rotation is a single `p`-cycle. QED.

## Theorem H15.23 — projective tomography

The complete coarse splitting signature of `q` across all worlds `H in W_p(E)` determines:

1. whether `bar a=0`;
2. if `bar a!=0`, the projective class

\[
\boxed{[\bar a]\in\mathbb P(V).}
\]

### Proof

If `bar a=0`, it lies in every hyperplane, so every world reports identity state.

If `bar a!=0`, the identity worlds are exactly the hyperplanes containing the one-dimensional subspace `<bar a>`. The family of all hyperplanes containing a projective point determines that point uniquely: the intersection of those hyperplanes is precisely `<bar a>`. QED.

Thus coarse splitting across an ensemble of dihedral worlds reconstructs projectivized `p`-class-group information.

## Corollary H15.24 — exact world counts

For `bar a!=0`, the number of identity worlds is

\[
\boxed{N_0=\frac{p^{r-1}-1}{p-1},}
\]

and the number of rotation worlds is

\[
\boxed{N_1=p^{r-1}.}
\]

If `bar a=0`, all `N` worlds are identity worlds.

### Proof

The annihilator of a nonzero vector is an `(r-1)`-dimensional subspace of `V^*`. Its projective points are the hyperplanes containing `bar a`, so there are `(p^{r-1}-1)/(p-1)` of them. Subtracting from `N` gives `p^{r-1}`. QED.

## Theorem H15.25 — inert primes are universal reflection states

If `q` is inert in `E/Q` and unramified in `M`, then every world in `W_p(E)` reports the reflection splitting type

\[
\boxed{1\,2^{(p-1)/2}.}
\]

### Proof

The unique prime `q O_E` above `q` is the principal ideal `(q)`. Hence its Artin class in every unramified class-field quotient is trivial. The rational Frobenius nevertheless maps to the nontrivial element of `Gal(E/Q)`, so its lift to each dihedral quotient is a reflection. QED.

In particular, when `2` is inert in `E`, the fixed prime `2` is a reflection-state anchor simultaneously in every dihedral `p`-world arising from `E`.

## Theorem H15.26 — ensemble trace projector

Let `tilde chi_H` be the centered degree-`p` permutation character of world `H`:

\[
\widetilde\chi_H=\chi_H-1.
\]

For a split unramified prime with class `bar a in V`,

\[
\boxed{
\sum_{H\in\mathcal W_p(E)}\widetilde\chi_H(\bar a)
=
\begin{cases}
p^r-1,&\bar a=0,\\
-1,&\bar a\ne0.
\end{cases}}
\]

For an inert unramified rational prime, the sum is `0`.

### Proof

An identity world contributes `p-1`; a nontrivial-rotation world contributes `-1`; a reflection world contributes `0`. Insert the counts from H15.24. For nonzero `bar a`,

\[
(p-1)N_0-N_1
=(p^{r-1}-1)-p^{r-1}
=-1.
\]

For `bar a=0`, all `N` worlds contribute `p-1`, giving `(p-1)N=p^r-1`. QED.

This is exactly the character of the augmentation of the regular representation of `V`.

## Claim discipline

The class-field correspondence, projective parametrization of index-`p` subgroups, and character orthogonality are classical. The H15 contribution is the synthesis that interprets the ensemble of dihedral side-field splitting states as a projective tomography device for the class of a prime ideal modulo `pA`.

No claim is made that the projective-incidence mechanism itself is new finite geometry.