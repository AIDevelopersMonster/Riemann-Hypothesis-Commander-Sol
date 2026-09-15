# HATTER-SOL-16 · A5 Artin local-factor tomography

## Status

**Closed theorem layer.**  This is the first exact arithmetic bridge beyond the dihedral laboratory.

Let

\[
G=A_5
\]

and let \(\rho_3:G\to SO(3)\) be either of the two real irreducible three-dimensional representations.  Fix the class convention in which

\[
\chi_3=(3,-1,0,\varphi,\varphi'),
\qquad
\varphi=\frac{1+\sqrt5}{2},
\qquad
\varphi'=\frac{1-\sqrt5}{2},
\]

on the classes

\[
1A,\ 2A,\ 3A,\ 5A,\ 5B.
\]

The second three-dimensional irrep exchanges \(5A\) and \(5B\).

---

## Theorem 16.A · one three-dimensional local factor separates every A5 class

For every \(g\in A_5\),

\[
\boxed{
P_g(T):=\det(I-\rho_3(g)T)
 =1-\chi_3(g)T+\chi_3(g)T^2-T^3.
}
\]

Consequently the map

\[
[g]\longmapsto P_g(T)
\]

from conjugacy classes of \(A_5\) to cubic polynomials is injective.

### Proof

Every matrix \(\rho_3(g)\) lies in \(SO(3)\).  Hence its eigenvalues are

\[
1,\lambda,\lambda^{-1}
\]

for a root of unity \(\lambda\), and

\[
\chi_3(g)=1+\lambda+\lambda^{-1}.
\]

Therefore

\[
\begin{aligned}
P_g(T)
&=(1-T)(1-\lambda T)(1-\lambda^{-1}T)\\
&=(1-T)\left(1-(\lambda+\lambda^{-1})T+T^2\right)\\
&=(1-T)\left(1-(\chi_3(g)-1)T+T^2\right)\\
&=1-\chi_3(g)T+\chi_3(g)T^2-T^3.
\end{aligned}
\]

The five values

\[
3,\ -1,\ 0,\ \varphi,\ \varphi'
\]

are pairwise distinct, so the coefficient of \(T\) already recovers the conjugacy class.  ∎

---

## Explicit local-factor table

The five denominators are

\[
\begin{array}{c|c|c}
\text{class} & \chi_3(g) & P_g(T)\\
\hline
1A & 3 & (1-T)^3\\
2A & -1 & (1-T)(1+T)^2\\
3A & 0 & 1-T^3\\
5A & \varphi & 1-\varphi T+\varphi T^2-T^3\\
5B & \varphi' & 1-\varphi' T+\varphi' T^2-T^3
\end{array}
\]

Equivalently,

\[
P_{5A}(T)=(1-T)\left(1-\frac{\sqrt5-1}{2}T+T^2\right),
\]

and

\[
P_{5B}(T)=(1-T)\left(1+\frac{\sqrt5+1}{2}T+T^2\right).
\]

Thus the split pair of five-cycle classes, invisible to ordinary cycle type in the natural five-point permutation action, is separated by a single three-dimensional determinant channel.

---

## Corollary 16.B · generating-commutator local tomography

The complete enumeration already established in the H16 A5 certificate gives, for every generating pair \((A,B)\),

\[
[A,B]\in 3A\cup5A\cup5B.
\]

Hence the single polynomial

\[
\boxed{
\det\left(I-\rho_3([A,B])T\right)
}
\]

recovers the conjugacy class of the commutator of every generating pair in \(A_5\).

This is the first HATTER-SOL observer in a non-solvable simple group whose exact class-separation theorem needs no scalar cyclic coordinate.

---

## Corollary 16.C · Artin local-factor interpretation

Let \(E/F\) be a finite Galois extension with

\[
\operatorname{Gal}(E/F)\simeq A_5,
\]

and let \(v\) be an unramified finite place.  For the three-dimensional Artin representation \(\rho_3\), the unramified local factor is

\[
L_v(T,\rho_3)
=
\det\left(I-\rho_3(\operatorname{Frob}_v)T\right)^{-1}.
\]

Therefore this single local factor determines the conjugacy class of \(\operatorname{Frob}_v\) in \(A_5\).

This statement uses only the representation-theoretic definition of the Artin local factor.  It does **not** assume or assert automorphy of a general \(A_5\) Artin representation.

---

## Corollary 16.D · Chebotarev observer frequencies

For an \(A_5\)-extension, Chebotarev density gives the class frequencies

\[
\frac1{60},\quad \frac{15}{60}=\frac14,\quad
\frac{20}{60}=\frac13,\quad
\frac{12}{60}=\frac15,\quad
\frac{12}{60}=\frac15
\]

for

\[
1A,2A,3A,5A,5B
\]

respectively, among unramified Frobenius classes.

Thus the local determinant observer is not merely injective: in an arithmetic realization its five outputs have explicit asymptotic frequencies.

---

## Minimality inside the irreducible character table

The irreducible dimensions of \(A_5\) are

\[
1,3,3,4,5.
\]

The trivial character does not separate classes.  The four-dimensional and five-dimensional irreducible characters take equal values on \(5A\) and \(5B\), whereas each three-dimensional character separates them.  Therefore dimension three is the smallest dimension of a single irreducible complex representation whose trace, and hence its local determinant polynomial, separates all five conjugacy classes.

The two three-dimensional observers are Galois conjugates under

\[
\sqrt5\longmapsto-\sqrt5,
\]

which exchanges \(5A\leftrightarrow5B\).

---

## Relation to the H15 mechanism

The dihedral laboratory used scalar character channels.  The A5 laboratory now has the exact replacement

\[
\boxed{
\text{scalar Dirichlet value}
\quad\rightsquigarrow\quad
\det(I-\rho_3(g)T).
}
\]

Together with the previously closed fourth-moment identity

\[
\langle\operatorname{Tr}H_{\rho_3}^4\rangle
=48+8\chi_3([A,B]),
\]

this shows that the same three-dimensional character controls both

1. the first commutator-sensitive closed-word spectral moment, and
2. the Artin local factor.

That is the first exact spectral--arithmetic bridge of HATTER-SOL-16.

---

## Next barrier

Two independent questions now remain:

1. **Mahler boundary:** close the scalar determinant separation from the certified range \(\mu\ge21/4\) down to the natural boundary \(\mu=4\), or exhibit a crossing.
2. **Higher simple group:** repeat the trace/local-factor tomography test in \(PSL(2,7)\) and determine whether one irrep still suffices or a genuinely vector-valued observer first becomes necessary.
