# HATTER-SOL-16 · Oriented loop spectral observer in PSL(2,7)

## Status

**Closed theorem layer.**

The previous PSL(2,7) layer showed that the ordinary scalar determinant/Mahler observer identifies the two order-seven commutator classes `7A` and `7B`, whereas the complex three-dimensional character does not collapse them.

This note constructs the missing **orientation-sensitive two-port spectral channel** and proves that the lost bit already appears at the first possible closed-word length.

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

---

## Theorem 16.F · the orientation bit is a length-four commutator quadrature

Define

\[
\boxed{
Q_4(A,B)
:=
\frac{\operatorname{Tr}\rho_3(K)-\operatorname{Tr}\rho_3(K^{-1})}
{i\sqrt7}.
}
\]

Then, for every generating pair `(A,B)`,

\[
Q_4(A,B)=
\begin{cases}
0,&K\in3A\cup4A,\\
+1,&K\in7A,\\
-1,&K\in7B.
\end{cases}
\]

Hence a single real oriented loop channel exactly recovers the `7A/7B` orientation.

### Proof

For a unitary representation,

\[
\chi_3(K^{-1})=\overline{\chi_3(K)}.
\]

The character values on the generating-commutator classes are

\[
\chi_3(3A)=0,
\qquad
\chi_3(4A)=1,
\]

and

\[
\chi_3(7A)=\frac{-1+i\sqrt7}{2},
\qquad
\chi_3(7B)=\frac{-1-i\sqrt7}{2}.
\]

Substitution gives the stated values.  ∎

The complete generating-pair enumeration gives the exact orbit distribution

\[
Q_4=0\text{ on }100\text{ generating-pair orbits},
\qquad
Q_4=+1\text{ on }7,
\qquad
Q_4=-1\text{ on }7.
\]

---

## Theorem 16.G · order four is minimal among closed port words

Assign exponent increments

\[
A:(1,0),\quad A^{-1}:(-1,0),\quad
B:(0,1),\quad B^{-1}:(0,-1).
\]

A torus-closed word must have total exponent vector `(0,0)`.

There is no nonempty freely reduced balanced word of length `1`, `2`, or `3`.
At length `4`, the primitive reduced balanced words appear, including

\[
ABA^{-1}B^{-1}=K
\]

and the reverse orientation

\[
BAB^{-1}A^{-1}=K^{-1}.
\]

Therefore the imaginary orientation of the commutator cannot enter a closed two-port word observable before order four.

Thus the H15/H16 `length-four` phenomenon survives once again, but now in an antisymmetric rather than Hermitian scalar channel:

\[
\boxed{
\text{first closed non-Abelian information}=4,
\qquad
\text{first orientation-sensitive information}=4.
}
\]

---

## Non-Hermitian loop determinant

The same orientation is present in the local loop determinant

\[
\boxed{
P_K(t)=\det(I-t\rho_3(K)).
}
\]

For every class,

\[
P_K(t)
=1-\chi_3(K)t+\overline{\chi_3(K)}t^2-t^3.
\]

For the split order-seven classes, write

\[
R(t)=(1-t)\left(1+\frac32t+t^2\right).
\]

Then

\[
\boxed{
P_{7A}(t)
=R(t)-i\frac{\sqrt7}{2}t(1+t),
}
\]

and

\[
\boxed{
P_{7B}(t)
=R(t)+i\frac{\sqrt7}{2}t(1+t).
}
\]

For real

\[
0<t<1,
\]

we have

\[
R(t)>0,
\qquad
\frac{\sqrt7}{2}t(1+t)>0.
\]

Hence

\[
\arg P_{7A}(t)<0,
\qquad
\arg P_{7B}(t)>0,
\]

with equal magnitude and opposite sign.

So the two conjugacy classes are separated for **every** real probe scale `0<t<1` by the sign of a determinant phase.

This is a genuine spectral readout, not merely an abstract character-table label.

---

## Corollary · minimal oriented scalar hardware channel

The pair

\[
\left(\operatorname{Tr}\rho_3(K),
\operatorname{Tr}\rho_3(K^{-1})\right)
\]

is redundant.  Their antisymmetric combination

\[
Q_4
\]

already gives the missing orientation bit.

Consequently the minimal extension of the unoriented scalar Mahler architecture need not be a full vector-valued spectral system.  One additional signed quadrature suffices:

\[
\boxed{
\text{unoriented scalar response}
+
Q_4
\quad\Longrightarrow\quad
\text{full generating-commutator class in }PSL(2,7).
}
\]

Equivalently, one can measure the sign of

\[
\operatorname{Im}\det(I-t\rho_3(K))
\]

for any fixed `0<t<1`.

---

## Structural interpretation

The collapse found in the scalar Mahler observer was not a failure of the representation.  It was produced by taking an orientation-even scalarization.

The exact hierarchy is now

\[
\boxed{
\text{unoriented Mahler magnitude}
<
\text{oriented determinant phase}
\simeq
\text{complex 3D character/local factor}.
}
\]

The outer involution in `PGL(2,7)` exchanges

\[
7A\leftrightarrow7B
\]

and complex-conjugates the 3D channel.  The orientation observable `Q_4` is odd under this involution.

Thus HATTER-SOL-16 now has a concrete mechanism for retaining Galois/outer orientation at the two-port spectral level.

---

## Exact reproducibility

The finite certificate is

`certificates/psl27_oriented_loop_spectral_observer_certificate.py`.

It verifies exactly:

- 114 simultaneous-conjugacy orbits of generating pairs;
- the commutator distribution `36 x 3A`, `64 x 4A`, `7 x 7A`, `7 x 7B`;
- the orientation values `0,0,+1,-1`;
- pairwise distinct three-dimensional local determinant polynomials;
- the opposite determinant-phase sign on `7A` and `7B`;
- the absence of any nontrivial freely reduced balanced word of length below four.

The script terminates with

`PASS: all exact assertions succeeded`.

---

## Next barrier

The first PSL(2,7) orientation problem is now closed.  The next question is no longer whether the split order-seven classes can be recovered, but how much of the **generating-pair orbit itself** can be reconstructed from a bounded collection of short closed-word channels.

The next strike should therefore be:

\[
\boxed{
\text{minimal short-word signature for the 114 generating-pair orbits}.
}
\]

This is the direct bridge from class tomography to the zero-oracle pair/network tomography planned for HATTER-SOL-17.
