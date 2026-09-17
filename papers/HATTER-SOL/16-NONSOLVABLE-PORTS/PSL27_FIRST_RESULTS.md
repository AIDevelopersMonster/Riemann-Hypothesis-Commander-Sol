# HATTER-SOL-16 · First exact PSL(2,7) results

## Status

The second nonsolvable laboratory is now active.  The exact finite certificate is

`certificates/psl27_generating_pair_and_scalar_collapse_certificate.py`.

It constructs

\[
G=PSL(2,7)
\]

as the faithful Möbius action on

\[
\mathbf P^1(\mathbf F_7),
\]

so \(|G|=168\).

---

## 1. Conjugacy classes

The six conjugacy classes have sizes

\[
\boxed{
1,\ 21,\ 56,\ 42,\ 24,\ 24
}
\]

for

\[
1A,\ 2A,\ 3A,\ 4A,\ 7A,\ 7B.
\]

The two order-seven classes are distinct although they have the same cycle type in the natural 8-point action.

---

## 2. Generating pairs

Complete exact enumeration gives

\[
\boxed{19152}
\]

ordered generating pairs.

Under simultaneous conjugacy every generating pair has orbit size 168, so there are exactly

\[
\boxed{114}
\]

generating-pair orbits.

Their commutator classes are distributed as

\[
\boxed{
36\times 3A,
\qquad
64\times 4A,
\qquad
7\times 7A,
\qquad
7\times 7B.
}
\]

Equivalently, on ordered generating pairs the counts are

\[
6048,\ 10752,\ 1176,\ 1176.
\]

In particular, a generating-pair commutator never lies in `1A` or `2A`.

---

## 3. A single three-dimensional character still separates every group class

For the standard complex three-dimensional irreducible representation let

\[
\alpha=\frac{-1+i\sqrt7}{2},
\qquad
\bar\alpha=\frac{-1-i\sqrt7}{2}.
\]

Its character row is

\[
\boxed{
\chi_3=(3,-1,0,1,\alpha,\bar\alpha)
}
\]

on

\[
1A,2A,3A,4A,7A,7B.
\]

These six values are pairwise distinct.  Therefore the complex trace

\[
\operatorname{Tr}\rho_3(g)
\]

by itself recovers the full conjugacy class of every element of `PSL(2,7)`.

Thus the exact Artin/local-factor class tomography observed in `A5` survives at the trace level in the next simple group.

---

## 4. The new phenomenon: scalar Mahler observation loses the orientation of the order-seven split

For every generating-pair orbit the certificate constructs exactly the Laurent polynomial

\[
D_{A,B}(z,w;4)
=
\det\bigl(4I-H_{A,B}(z,w)\bigr)
\]

with coefficients in

\[
\mathbf Q(i\sqrt7).
\]

After quotienting by torus substitutions preserving scalar Mahler measure,

\[
(z,w)\mapsto(z^{-1},w),
\quad
(z,w)\mapsto(z,w^{-1}),
\quad
(z,w)\mapsto(w,z),
\]

the 114 generating-pair orbits collapse to

\[
\boxed{
6\text{ types in }3A,
\quad
12\text{ types in }4A,
\quad
3\text{ types in }7A,
\quad
3\text{ types in }7B.
}
\]

But the decisive fact is

\[
\boxed{
\mathcal T_{7A}=\mathcal T_{7B}.
}
\]

The exact determinant/Mahler type sets of the two order-seven commutator classes are identical.

Therefore a scalar determinant/Mahler observer built from this one three-dimensional irrep cannot distinguish `7A` from `7B`, despite the fact that the **complex trace** does distinguish them.

This is the first genuine observer collapse in HATTER-SOL-16.

---

## 5. Interpretation

The `A5` laboratory allowed one real 3D channel to do all of the following at once:

\[
\text{commutator class}
\to
\text{trace}
\to
\text{local factor}
\to
\text{scalar determinant/Mahler class separation}.
\]

In `PSL(2,7)` this chain breaks:

\[
\boxed{
\text{complex trace separates }7A,7B,
\quad
\text{scalar Mahler data does not.}
}
\]

The lost information is exactly the Galois-conjugate imaginary orientation

\[
\alpha\leftrightarrow\bar\alpha.
\]

This is strong evidence that the next universal object is not a single real scalar Mahler response but a **complex/oriented or vector-valued representation observer**.

---

## 6. Artin bridge

For an unramified Frobenius class in a `PSL(2,7)`-Galois realization, the three-dimensional Artin local factor

\[
L_v(T,\rho_3)
=
\det\left(I-\rho_3(\operatorname{Frob}_v)T\right)^{-1}
\]

retains the full complex character information and therefore distinguishes the two order-seven classes.

Hence the arithmetic local factor is strictly finer than the scalar Mahler quotient encountered above.

No automorphy claim is made here.

---

## 7. Immediate next strike

The next question is now sharper than expected:

> What is the smallest observer extension that restores the lost `7A/7B` orientation?

Candidates, in increasing order of cost:

1. retain an oriented complex trace channel instead of taking only a real scalar log-determinant;
2. use the conjugate pair \((\rho_3,\bar\rho_3)\) as a two-component observer;
3. test whether another single irreducible representation already restores scalar separation;
4. determine whether the two order-seven classes remain collapsed after all conjugation-invariant scalar determinant observables, which would establish a genuine lower bound on scalar tomography.

This is now the main PSL(2,7) theorem problem.
