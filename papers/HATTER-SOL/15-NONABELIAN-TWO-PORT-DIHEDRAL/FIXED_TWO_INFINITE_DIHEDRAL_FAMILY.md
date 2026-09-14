# HATTER-SOL-15 · Infinite Dihedral Worlds for the Fixed Prime 2

**Status:** exact arithmetic theorem layer

## External input

Meng Fai Lim proved that for every squarefree odd integer `n>1`, and in particular for every odd prime `p`, there exist infinitely many squarefree negative integers

\[
d\equiv5\pmod8
\]

such that the imaginary quadratic field

\[
E=\mathbb Q(\sqrt d)
\]

has class group containing an element of order `p` (indeed his theorem gives the stronger simultaneous divisibility condition on the discriminant and class number).

The congruence `d=5 mod 8` implies that the rational prime `2` is inert in `E/Q`.

Reference: Meng Fai Lim, *On the divisibility of the class numbers and discriminants of imaginary quadratic fields*, arXiv:1601.05180, Theorem 1.1.

## Theorem H15.8 — fixed-prime-2 infinite dihedral realization

For every odd prime `p`, there exist infinitely many Galois extensions

\[
L/\mathbb Q
\]

with

\[
\operatorname{Gal}(L/\mathbb Q)\cong D_{2p}=C_p\rtimes C_2
\]

such that the rational prime `2` is unramified and has decomposition group of order `2`, necessarily a reflection subgroup.

### Proof

Choose one of Lim's imaginary quadratic fields

\[
E=\mathbb Q(\sqrt d),\qquad d\equiv5\pmod8,
\]

whose class group has an element of order `p`.

Because the finite abelian group `Cl(E)` has `p`-torsion, it has a quotient

\[
Cl(E)\twoheadrightarrow C_p.
\]

By global class field theory this quotient corresponds to an everywhere-unramified cyclic extension

\[
L/E,
\qquad
\operatorname{Gal}(L/E)\cong C_p.
\]

For an imaginary quadratic field, complex conjugation acts on the ideal class group by inversion. Therefore the kernel of the quotient is stable under conjugation, so `L/Q` is Galois, and conjugation acts on `Gal(L/E)=C_p` by inversion. Hence

\[
\operatorname{Gal}(L/\mathbb Q)
\cong C_p\rtimes_{-1} C_2
\cong D_{2p}.
\]

Since `d=5 mod 8`, the prime `2` is inert in `E/Q`; thus

\[
(2)=\mathfrak q
\]

is a single prime ideal of `E`. It is principal, so its ideal class is trivial. Under the Artin map for the unramified extension `L/E`, its Frobenius is therefore trivial. Hence `q` splits completely in `L/E`.

Consequently, at any prime `P` of `L` above `2`, the residue degree over `E` is `1`, while the residue degree of `q/2` in `E/Q` is `2`. Therefore

\[
f(P/2)=2.
\]

The whole tower is unramified at `2`, so the decomposition group in `L/Q` has order `2`. It maps nontrivially to `Gal(E/Q)=C_2`, and therefore is one of the reflection subgroups of `D_{2p}`. QED.

## Corollary H15.9 — fixed 2 in the degree-p side field

Let `D<=D_{2p}` be the reflection decomposition group of a chosen prime `P|2`, and let

\[
K=L^D,
\qquad [K:\mathbb Q]=p.
\]

The action of a reflection on the `p` cosets `D\backslash D_{2p}` has cycle type

\[
\boxed{1\,2^{(p-1)/2}}.
\]

Therefore the factorization of the fixed rational prime `2` in `K` is

\[
\boxed{
2\mathcal O_K
=
\mathfrak p_0
\prod_{j=1}^{(p-1)/2}\mathfrak p_j,
}
\]

with

\[
f(\mathfrak p_0/2)=1,
\qquad
f(\mathfrak p_j/2)=2\quad(1\le j\le(p-1)/2).
\]

Thus for every odd prime `p` there are infinitely many degree-`p` non-Galois arithmetic worlds in which the **same fixed prime 2** realizes the H15 reflection port pattern.

## Corollary H15.10 — fixed local Euler factor at 2

For every field `K` in H15.9, the unramified local Euler factor of the Dedekind zeta function at `2` is

\[
\boxed{
\zeta_{K,2}(s)
=
(1-2^{-s})^{-1}
(1-2^{-2s})^{-(p-1)/2}.
}
\]

Hence the two-port reflection state has a literal fixed-prime analytic signature.

## Programme meaning

H15 no longer studies only a variable Chebotarev prime moving through one world. It now has the complementary H07-style regime:

\[
\boxed{
\text{hold the number }2\text{ fixed and vary the arithmetic world}.}
\]

Across infinitely many non-abelian worlds of every odd prime degree, the same prime `2` acquires the same reflection-type sector pattern appropriate to that degree.

This gives a rigorous realization of the programme slogan:

\[
\boxed{
\text{a fixed number can expose different structural port geometries when the arithmetic world changes}.}
\]

No claim about the Riemann hypothesis is made. The zeta connection here is through an exact local Euler factor and the associated global Dedekind/Artin-Hecke factorization.