# HATTER-SOL-16 · A5 Artin local-factor tomography

## Status

**Closed theorem layer.** This is the first exact arithmetic bridge beyond the dihedral laboratory.

Let

\[
G=A_5
\]

and let \(\rho_3:G\to SO(3)\) be either real irreducible three-dimensional representation. Fix the class convention

\[
\chi_3=(3,-1,0,\varphi,\varphi'),
\qquad
\varphi=\frac{1+\sqrt5}{2},
\qquad
\varphi'=\frac{1-\sqrt5}{2},
\]

on

\[
1A,2A,3A,5A,5B.
\]

The other 3D irrep exchanges \(5A\) and \(5B\).

## Theorem · one 3D local factor separates every A5 class

For every \(g\in A_5\),

\[
\boxed{
P_g(T):=\det(I-\rho_3(g)T)
=1-\chi_3(g)T+\chi_3(g)T^2-T^3.
}
\]

Indeed every \(\rho_3(g)\in SO(3)\) has eigenvalues \(1,\lambda,\lambda^{-1}\), hence

\[
P_g(T)=(1-T)(1-\lambda T)(1-\lambda^{-1}T)
=1-\chi_3(g)T+\chi_3(g)T^2-T^3.
\]

The five character values are pairwise distinct, so the coefficient of \(T\) already recovers the conjugacy class.

The explicit denominators are

\[
\begin{array}{c|c|c}
\text{class} & \chi_3(g) & P_g(T)\\
\hline
1A & 3 & (1-T)^3\\
2A & -1 & (1-T)(1+T)^2\\
3A & 0 & 1-T^3\\
5A & \varphi & 1-\varphi T+\varphi T^2-T^3\\
5B & \varphi' & 1-\varphi' T+\varphi'T^2-T^3.
\end{array}
\]

For a generating pair \((A,B)\), exact enumeration gives

\[
[A,B]\in3A\cup5A\cup5B,
\]

so one polynomial \(\det(I-\rho_3([A,B])T)\) recovers the commutator class.

## Artin interpretation

Let \(E/F\) be a finite Galois extension with

\[
\operatorname{Gal}(E/F)\simeq A_5,
\]

and let \(v\) be unramified. Then

\[
L_v(T,\rho_3)
=\det(I-\rho_3(\operatorname{Frob}_v)T)^{-1}
\]

determines the Frobenius conjugacy class. This is only the representation-theoretic Artin local factor; no general automorphy claim is made.

By Chebotarev, the class frequencies in an \(A_5\)-extension are

\[
\frac1{60},\quad\frac14,\quad\frac13,\quad\frac15,\quad\frac15
\]

for \(1A,2A,3A,5A,5B\), respectively.

## Minimality inside the irreducible character table

The irreducible dimensions are

\[
1,3,3,4,5.
\]

The 4D and 5D irreducible characters take equal values on \(5A\) and \(5B\), while each 3D character separates them. Hence dimension three is the smallest dimension of a single irreducible representation whose trace, and therefore its local determinant polynomial, separates all five classes.

## Correct spectral bridge

For the two-port Hermitian operator used in H16, the universal balanced fourth torus moment is

\[
\boxed{
S_4=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}),
\qquad K=[A,B].
}
\]

For the real 3D \(A_5\) irrep this becomes

\[
\boxed{
S_4=84+8\chi_3(K).
}
\]

Thus the same 3D character controls both the first commutator-sensitive closed-word spectral moment and the Artin local factor.

The previously recorded provisional constant `48+8 chi_3(K)` is superseded by the corrected identity above.

## Final H16 status

The former Mahler-boundary question is no longer open. The exact certificate chain now proves

\[
\boxed{
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
\qquad\forall\mu\ge4.
}
\]

The higher simple-group step is also complete in `PSL(2,7)` and is incorporated into the final H16 publication manuscript.
