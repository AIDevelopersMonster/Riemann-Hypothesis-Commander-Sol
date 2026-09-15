# HATTER-SOL-16 · PSL(2,7) orientation obstruction and minimal observer

## Status

**Closed theorem layer.**

The first PSL(2,7) computation showed that the scalar determinant/Mahler type sets of the two order-seven commutator classes coincide, even though the standard complex three-dimensional character separates those classes.

This note identifies the exact symmetry causing that collapse and determines a minimal observer that restores the lost orientation.

---

## 1. Outer automorphism exchanging the two order-seven classes

Realize

\[
G=PSL(2,7)
\]

in its faithful action on

\[
\mathbf P^1(\mathbf F_7).
\]

Let

\[
h=\begin{bmatrix}3&0\\0&1\end{bmatrix}
\]

viewed projectively.  Since `3` is a nonsquare modulo `7`, the projective transformation defined by `h` belongs to `PGL(2,7)` but not to `PSL(2,7)`.

Nevertheless conjugation by `h` normalizes `PSL(2,7)` and therefore defines an automorphism

\[
\alpha(g)=hgh^{-1}.
\]

Exact enumeration gives the class action

\[
\boxed{
1A\mapsto1A,
\quad2A\mapsto2A,
\quad3A\mapsto3A,
\quad4A\mapsto4A,
\quad7A\leftrightarrow7B.
}
\]

Because an inner automorphism preserves every conjugacy class, this class swap proves that \(\alpha\) is outer.

Thus the split pair `7A,7B` is an **orientation pair** for the nontrivial outer symmetry of `PSL(2,7)`.

---

## 2. Three-dimensional character and Galois orientation

For one of the complex irreducible three-dimensional representations, write

\[
\alpha_7=\frac{-1+i\sqrt7}{2},
\qquad
\bar\alpha_7=\frac{-1-i\sqrt7}{2}.
\]

Then

\[
\chi_3=(3,-1,0,1,\alpha_7,\bar\alpha_7)
\]

on

\[
1A,2A,3A,4A,7A,7B.
\]

The outer automorphism acts by complex conjugation:

\[
\boxed{
\chi_3(\alpha(g))=\overline{\chi_3(g)}.
}
\]

Hence the lost `7A/7B` label is exactly the sign of the imaginary part of the oriented three-dimensional character.

The conjugate irrep \(\bar\rho_3\) exchanges the two labels.

---

## 3. Local Artin polynomial remains fully separating

For the three-dimensional unitary representation,

\[
P_g(T)=\det(I-\rho_3(g)T)
\]

has the form

\[
\boxed{
P_g(T)
=
1-\chi_3(g)T+\overline{\chi_3(g)}T^2-T^3.
}
\]

The six resulting cubic polynomials are pairwise distinct.  Therefore

\[
[g]\longmapsto P_g(T)
\]

is injective on all six conjugacy classes of `PSL(2,7)`.

In particular,

\[
P_{7A}(T)\neq P_{7B}(T),
\]

although their real scalar Mahler quotients collapse.

Thus the Artin local factor retains the full orientation data lost by scalarization.

---

## 4. Minimal irreducible channel statement

The irreducible dimensions are

\[
1,3,3,6,7,8.
\]

Exact character-table verification shows:

- the two conjugate 3D rows each take six distinct values and individually separate all six classes;
- the 6D, 7D and 8D rows each take the same value on `7A` and `7B` and therefore fail to separate all classes;
- the trivial row is constant.

Therefore

\[
\boxed{
\text{dimension }3
\text{ is the minimal dimension of a single irreducible class-separating channel.}
}
\]

Moreover the only irreducible channels with that property are the conjugate pair

\[
\rho_3,\ \bar\rho_3.
\]

This is a stronger statement than merely observing that one complex trace happens to work.

---

## 5. Two real coordinates, and one calibrated real scalar

Write the three-dimensional character as two real coordinates

\[
I(g)=\Re\chi_3(g),
\qquad
Q(g)=\frac{2}{\sqrt7}\Im\chi_3(g).
\]

Then

\[
\begin{array}{c|rrrrrr}
[g] & 1A&2A&3A&4A&7A&7B\\
\hline
I & 3&-1&0&1&-\tfrac12&-\tfrac12\\
Q & 0&0&0&0&1&-1
\end{array}
\]

The coordinate `I` is the unoriented part.  The coordinate `Q` is exactly the orientation bit that scalar Mahler observation loses.

Thus the natural real observer is the two-component vector

\[
\boxed{(I,Q).}
\]

But a useful refinement appears: for this finite class set, even the single calibrated real scalar

\[
F(g)=I(g)+Q(g)
\]

is already injective, with values

\[
\boxed{
3,-1,0,1,\frac12,-\frac32
}
\]

on

\[
1A,2A,3A,4A,7A,7B.
\]

So **two real output wires are not information-theoretically necessary** once an oriented calibration is permitted.

What is necessary is not vector dimension per se, but retention of an orientation-sensitive channel.

---

## 6. Exact lower bound on outer-invariant scalar observers

Let \(F\) be any scalar class function satisfying

\[
F(\alpha(g))=F(g)
\]

for the outer automorphism above.  Since \(\alpha\) exchanges `7A` and `7B`, necessarily

\[
\boxed{F(7A)=F(7B).}
\]

Therefore no outer-invariant scalar class observer can distinguish the two order-seven classes.

This precisely explains the earlier Mahler collapse: once the construction quotients away the orientation transformed by \(\alpha\), the two split classes must merge.

The correct impossibility statement is therefore not

> “all scalar observers fail,”

which is false, but

> **every scalar observer invariant under the relevant outer/Galois orientation reversal fails to distinguish `7A` from `7B`.**

An oriented scalar such as `F=I+Q`, or the complex trace itself, escapes this obstruction.

---

## 7. Consequence for HATTER-SOL tomography

The PSL(2,7) laboratory therefore gives the first exact separation between two kinds of tomography:

\[
\boxed{
\text{unoriented scalar tomography}
<
\text{oriented representation tomography}.
}
\]

The minimal repair is not necessarily a large vector of channels.  It is enough to preserve one orientation-sensitive degree of freedom.

For arithmetic applications the natural object is already present:

\[
\boxed{
\det(I-\rho_3(\mathrm{Frob}_v)T)^{-1},
}
\]

whose complex coefficients retain the split Frobenius class.

For hardware, a natural real implementation is an `I/Q` pair, followed if desired by a calibrated scalar projection such as `I+Q`.

---

## Exact certificate

The finite proof is reproduced by

`certificates/psl27_outer_orientation_minimal_observer_certificate.py`.

It verifies exactly:

- the `PGL(2,7)` outer automorphism and its class swap;
- complex-conjugation of the 3D character under that automorphism;
- full six-class separation by the 3D Artin polynomial;
- the irreducible-character minimality statement;
- the real `I/Q` coordinates and injectivity of the scalar `F=I+Q`.

---

## Next barrier

The next question is no longer whether `PSL(2,7)` needs a vector observer.  The exact answer is subtler:

\[
\boxed{
\text{orientation-sensitive information is necessary, but one calibrated scalar can suffice.}
}
\]

The next strike should therefore test the actual **two-port spectral observer** rather than only the bare commutator trace:

1. construct an oriented/non-Hermitian determinant response that retains `Q`;
2. determine the lowest closed-word order at which its imaginary/orientation component appears;
3. decide whether a single physically measurable quadrature can recover the split `7A/7B` class over the complete set of 114 generating-pair orbits.
