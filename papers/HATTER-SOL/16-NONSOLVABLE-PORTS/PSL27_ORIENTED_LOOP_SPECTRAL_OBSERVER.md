# HATTER-SOL-16 · Oriented loop spectral observer in PSL(2,7)

## Status

**Closed theorem layer.**

The previous PSL(2,7) layer showed that the ordinary real scalar determinant/Mahler observer **collapses** the two order-seven commutator classes `7A` and `7B`, whereas the complex three-dimensional character separates them.

This note constructs the missing orientation-sensitive two-port spectral channel and proves that the lost bit already appears at the first possible closed-word length.

Let

\[
K=[A,B]=ABA^{-1}B^{-1}
\]

for a generating pair of `PSL(2,7)`, and let

\[
\rho_3:PSL(2,7)\to U(3)
\]

be one of the two conjugate irreducible three-dimensional representations, with character

\[
\chi_3=(3,-1,0,1,\alpha,\bar\alpha),
\qquad
\alpha=\frac{-1+i\sqrt7}{2}.
\]

## Orientation bit

Define

\[
\boxed{
Q_4(A,B)=
\frac{\operatorname{Tr}\rho_3(K)-\operatorname{Tr}\rho_3(K^{-1})}{i\sqrt7}.
}
\]

Then

\[
Q_4(A,B)=
\begin{cases}
0,&K\in3A\cup4A,\\
+1,&K\in7A,\\
-1,&K\in7B.
\end{cases}
\]

For a unitary representation,

\[
\chi_3(K^{-1})=\overline{\chi_3(K)},
\]

and substitution of the 3D character values proves the formula.

The complete generating-pair enumeration gives

\[
Q_4=0\text{ on }100\text{ generating-pair orbits},
\qquad
Q_4=+1\text{ on }7,
\qquad
Q_4=-1\text{ on }7.
\]

## Minimal closed-word depth

A torus-balanced word has zero total exponent in both generators. There is no nonempty freely reduced balanced word of length one, two or three. At length four the primitive commutator pair appears:

\[
ABA^{-1}B^{-1}=K,
\qquad
BAB^{-1}A^{-1}=K^{-1}.
\]

Hence

\[
\boxed{
\text{first closed non-Abelian information}=4,
\qquad
\text{first orientation-sensitive information}=4.
}
\]

## Non-Hermitian loop determinant

The same orientation is present in

\[
P_K(t)=\det(I-t\rho_3(K))
=1-\chi_3(K)t+\overline{\chi_3(K)}t^2-t^3.
\]

For the split order-seven classes, with

\[
R(t)=(1-t)\left(1+\frac32t+t^2\right),
\]

we have

\[
P_{7A}(t)=R(t)-i\frac{\sqrt7}{2}t(1+t),
\]

\[
P_{7B}(t)=R(t)+i\frac{\sqrt7}{2}t(1+t).
\]

For every real \(0<t<1\), \(R(t)>0\), so the determinant phases have opposite signs. Thus one signed spectral quadrature separates `7A` from `7B` at every fixed probe scale in that interval.

## Engineering consequence

A full vector-valued spectral system is not information-theoretically necessary for the split. One additional orientation-sensitive degree of freedom suffices:

\[
\boxed{
\text{unoriented scalar response}+Q_4
\Longrightarrow
\text{full generating-commutator class in }PSL(2,7).
}
\]

Equivalent finite-lab realizations are a complex trace channel, an `I/Q` pair, or the sign of the imaginary part of the local determinant.

## Structural interpretation

The exact hierarchy is

\[
\boxed{
\text{unoriented Mahler magnitude}
<
\text{oriented determinant phase}
\simeq
\text{complex 3D character/local factor}.
}
\]

The outer involution in `PGL(2,7)` exchanges `7A` and `7B` and complex-conjugates the 3D channel; `Q_4` is odd under this involution.

## Reproducibility

The certificate

`certificates/psl27_oriented_loop_spectral_observer_certificate.py`

verifies exactly the 114 pair orbits, commutator distribution, orientation values, pairwise distinct local determinant polynomials, opposite determinant-phase signs, and absence of shorter nontrivial balanced words.

This layer is final and is incorporated into the H16 publication manuscript.
