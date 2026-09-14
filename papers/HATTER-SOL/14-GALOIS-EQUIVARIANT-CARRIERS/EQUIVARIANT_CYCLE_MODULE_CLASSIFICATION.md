# HATTER-SOL-14 · Equivariant Cycle-Module Classification

**Status:** exact theorem layer

Let `Gamma` be a finite abelian group and let

\[
C=\operatorname{Cay}(\Gamma,S)
\]

be a connected simple undirected Cayley graph. Write the inverse-closed connection set uniquely as

\[
S=\bigsqcup_{j=1}^{p}\{s_j,s_j^{-1}\}\sqcup T,
\]

where every `s_j` has order greater than two and `T` is the set of involutions contained in `S`.

Let `n=|Gamma|`.

## Theorem H14.11 — rational cycle-module formula

In the rational representation ring of `Gamma`,

\[
\boxed{
[H_1(C;\mathbb Q)]
=(p-1)[\mathbb Q\Gamma]
+\sum_{\tau\in T}
[\operatorname{Ind}_{\langle\tau\rangle}^{\Gamma}\varepsilon_\tau]
+[\mathbf 1].
}
\]

Here `epsilon_tau` is the nontrivial one-dimensional representation of the order-two subgroup `<tau>`.

### Proof

The vertex-chain module is the regular module

\[
C_0(C;\mathbb Q)\cong\mathbb Q\Gamma.
\]

Each non-involutory inverse pair `{s,s^{-1}}` gives one free orbit of unoriented edges; after choosing orientations, its edge-chain module is one copy of `Q Gamma`.

For an involution `tau`, the corresponding edge orbit has stabilizer `<tau>`, and `tau` reverses the chosen orientation. Hence that orbit contributes

\[
\operatorname{Ind}_{\langle\tau\rangle}^{\Gamma}\varepsilon_\tau.
\]

Therefore

\[
C_1(C;\mathbb Q)
\cong
p\,\mathbb Q\Gamma
\oplus
\bigoplus_{\tau\in T}
\operatorname{Ind}_{\langle\tau\rangle}^{\Gamma}\varepsilon_\tau.
\]

Since `C` is connected, the cellular sequence gives

\[
0\to H_1(C;\mathbb Q)\to C_1\to C_0\to\mathbf 1\to0.
\]

Taking classes in the semisimple rational representation ring yields the formula. QED.

## Theorem H14.12 — exact character fingerprint

Let `chi_C` be the ordinary character of `H_1(C;Q)`. Then for every nonidentity element `g in Gamma`,

\[
\boxed{
\chi_C(g)=
\begin{cases}
1-n/2,& g\in T,\\
1,& g\notin T.
\end{cases}}
\]

At the identity,

\[
\boxed{
\chi_C(1)=n\left(p+\frac{|T|}{2}-1\right)+1
=|E(C)|-|V(C)|+1.
}
\]

### Proof

The regular character vanishes away from the identity. Because `Gamma` is abelian,

\[
\chi_{\operatorname{Ind}_{\langle\tau\rangle}^{\Gamma}\varepsilon_\tau}(g)
=
\begin{cases}
n/2,&g=1,\\
-n/2,&g=\tau,\\
0,&g\notin\{1,\tau\}.
\end{cases}
\]

Substitution in H14.11 gives the formulas. QED.

## Corollary H14.13 — complete classification at the equivariant-homology level

For connected simple undirected Cayley graphs on the same finite abelian group `Gamma`, the rational `Gamma`-module `H_1` determines, and is determined by,

1. the number `p` of non-involutory inverse-pair directions; and
2. the exact involution subset `T` used by the connection set.

Equivalently,

\[
\boxed{
H_1(\operatorname{Cay}(\Gamma,S);\mathbb Q)
\cong
H_1(\operatorname{Cay}(\Gamma,S');\mathbb Q)
}
\]

as `Q[Gamma]`-modules iff the two connection sets have the same `p` and the same involution subset `T`.

### Proof

The forward implication follows from H14.12: the character values at nonidentity involutions recover membership in `T` exactly. Once `T` is known, the identity value recovers `p`. Conversely, equal `p` and equal `T` give the same class in H14.11 and therefore the same semisimple rational module. QED.

## Consequence

The equivariant first homology is completely blind to **which** non-involutory inverse pairs occur, except for their number, but it remembers the involution directions exactly.

Thus the first positive H14 mechanism is now identified precisely:

\[
\boxed{
\text{equivariant homological memory}
=
\text{exact involution fingerprint}
+
\text{count of non-involutory directions}.
}
\]

This sharpens the `k=8` witness and gives the correct target for an infinite arithmetic family.