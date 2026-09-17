# HATTER-SOL-16 · Exact A5 boundary Mahler ordering at mu = 4

## Status

**Closed theorem layer.**

This note closes the natural boundary point `mu = 4` for the scalar determinant observer attached to the real three-dimensional irreducible representation of `A5`.

For a generating pair `(A,B)` define

\[
H_{A,B}(\theta,\phi)=
 e^{i\theta}\rho_3(A)+e^{-i\theta}\rho_3(A)^{-1}
 +e^{i\phi}\rho_3(B)+e^{-i\phi}\rho_3(B)^{-1}
\]

and

\[
M_{A,B}(4)=\frac1{(2\pi)^2}\int_{0}^{2\pi}\int_{0}^{2\pi}
\log\det\bigl(4I-H_{A,B}(\theta,\phi)\bigr)\,d\theta\,d\phi.
\]

The 38 simultaneous-conjugacy orbits of generating pairs collapse, under the determinant-polynomial symmetries used below, to exactly 14 Mahler types:

\[
4\text{ types in }5A,\qquad 6\text{ types in }3A,\qquad 4\text{ types in }5B.
\]

---

## Theorem 16.E · strict class ordering at the spectral boundary

For every generating pair `(A,B)` in `A5`, with commutator

\[
K=[A,B],
\]

the boundary Mahler observer satisfies the strict ordering

\[
\boxed{
M_{5A}(4)<M_{3A}(4)<M_{5B}(4).
}
\]

More precisely, every one of the four `5A` Mahler types is strictly below every one of the six `3A` types, and every `3A` type is strictly below every one of the four `5B` types.

This is an exact computer-assisted theorem with a finite interval certificate; it is not inferred from floating-point quadrature.

---

## Exact determinant polynomial

For each generating-pair representative the determinant

\[
D_{A,B}(z,w;4)=\det\bigl(4I-H_{A,B}(z,w)\bigr)
\]

is computed exactly as a Laurent polynomial with coefficients in

\[
\mathbf Q(\sqrt5).
\]

The certificate obtains this polynomial from the Newton identity

\[
\det(\mu I-H)
=
\mu^3-\mu^2\operatorname{Tr}H
+\frac{\mu}{2}\bigl((\operatorname{Tr}H)^2-\operatorname{Tr}H^2\bigr)
-\frac16\bigl((\operatorname{Tr}H)^3-3\operatorname{Tr}H\operatorname{Tr}H^2+2\operatorname{Tr}H^3\bigr),
\]

with `mu = 4`, and evaluates the character coefficients exactly in the quadratic field.

After quotienting by the torus symmetries

\[
(z,w)\mapsto(z^{-1},w),\quad
(z,w)\mapsto(z,w^{-1}),\quad
(z,w)\mapsto(w,z),
\]

the 38 pair-orbits reduce to 14 determinant/Mahler types.

---

## Typewise tensor spectral gaps

The boundary quadrature is certified using a stronger, type-dependent version of the tensor-gap argument.

For each of the 14 Mahler types consider the tensor Cayley Laplacian on

\[
\rho_3\otimes\rho_3:
\]

\[
\mathcal L_{A,B}
=
4I-ho(A)\otimes\rho(A)-\rho(A)^{-1}\otimes\rho(A)^{-1}
-ho(B)\otimes\rho(B)-\rho(B)^{-1}\otimes\rho(B)^{-1}.
\]

On the orthogonal complement of the invariant tensor `vec(I)`, exact Sylvester-criterion calculations over `Q(sqrt(5))` certify the following rational lower bounds for the 14 types:

\[
\gamma>
\frac34,\ \frac32,\ \frac38,\ 1,\ \frac54,\ \frac35,\ \frac15,
\frac9{10},\ \frac45,\ \frac3{10},\ \frac12,\ \frac34,\ \frac23,\ \frac45.
\]

The minimum is

\[
\boxed{\gamma>\frac15}.
\]

The exact certificate is

`certificates/a5_type_tensor_gap_certificate.py`.

For a type with tensor gap `gamma`, the phase-optimized spectral radius obeys

\[
\frac{\|H_{A,B}(\theta,\phi)\|}{4}
<
q_\gamma:=\sqrt{1-\frac{\gamma}{6}}<1.
\]

This is the key input that makes the boundary logarithm analytic in a full annulus and gives an explicit Fourier-aliasing bound.

---

## Certified torus quadrature

For each exact determinant polynomial the certificate evaluates the periodic trapezoidal rule using outward-rounded interval arithmetic (`mpmath.iv`).

The type-dependent grids use

\[
M\in\{96,128,160,240\}.
\]

If `T_M` is the two-dimensional `M x M` trapezoidal average of `log D`, the tensor spectral gap yields the rigorous aliasing estimate

\[
\boxed{
|M_{A,B}(4)-T_M|
\le
\frac{6q_\gamma^M}{M(1-q_\gamma)}.
}
\]

Each numerical interval is therefore the sum of

1. an outward-rounded interval evaluation of the finite trapezoidal average, and
2. the exact analytic aliasing enclosure above.

The resulting 14 certified intervals are pairwise separated according to the class ordering.

In particular, the difficult `5A` type with the weakest tensor gap is still enclosed below the lowest `3A` enclosure, and the highest `3A` enclosure remains below the lowest `5B` enclosure.

---

## Why this is stronger than the earlier boundary positivity theorem

The previous uniform spectral-gap theorem proved only

\[
4I-H_{A,B}(\theta,\phi)>0
\]

uniformly for every generating pair, so the boundary Mahler integral was well-defined and its logarithmic series converged.

The present theorem proves the **relative ordering of the complete scalar observer** across the three possible generating-commutator classes.

Thus the class-sensitive scalar determinant observer survives at the natural spectral boundary in the first nonsolvable simple laboratory.

---

## Relation to HATTER-SOL-15

In the prime-dihedral case HATTER-SOL-15 obtained class/tomography separation from a positive first-harmonic dominance theorem.

The `A5` result shows that the same final phenomenon survives, but by a different mechanism:

\[
\boxed{
\text{higher-dimensional irrep}
\to
\text{length-four commutator trace}
\to
\text{tensor spectral gap}
\to
\text{certified determinant/Mahler separation}.
}
\]

So the H15 scalar first-harmonic proof is not the universal object.  The more robust structure appears to be representation-theoretic closed-word information plus a spectral-gap-controlled determinant observer.

---

## Exact reproducibility

The proof is split between two machine-checkable scripts:

- `certificates/a5_type_tensor_gap_certificate.py` — exact algebraic tensor-gap proof over `Q(sqrt(5))`;
- `certificates/a5_boundary_mahler_mu4_interval_certificate.py` — exact determinant construction plus outward-rounded interval quadrature and analytic aliasing bounds.

The boundary certificate terminates with

`PASS: rigorous interval + aliasing certificate closes mu=4 ordering`.

---

## Remaining global parameter question

Two parameter ranges are now rigorous:

\[
\mu=4
\]

and

\[
\mu\ge\frac{23}{5}.
\]

The open strip is

\[
\boxed{4<\mu<\frac{23}{5}}.
\]

Numerical scans show the same ordering throughout this strip, but this note does **not** promote that numerical observation to a theorem.  A compact-parameter interval certificate or an analytic no-crossing argument is still required before claiming the ordering for every `mu >= 4`.
