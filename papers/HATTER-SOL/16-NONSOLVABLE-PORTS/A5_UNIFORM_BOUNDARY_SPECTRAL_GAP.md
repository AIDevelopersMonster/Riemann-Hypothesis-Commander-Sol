# HATTER-SOL-16 · Uniform boundary spectral gap in the 3D A5 observer

## Status

**Closed theorem layer.**  This closes the positivity/convergence obstruction at the natural boundary `mu=4`.  It does **not** by itself prove the class ordering of the Mahler values on the whole interval `4 <= mu < 23/5`; that remains a separate separation problem.

Let `rho:A5 -> SO(3)` be either irreducible real three-dimensional representation and let `(A,B)` be any ordered generating pair of `A5`.  Put

\[
H_{A,B}(\theta,\phi)
=e^{i\theta}\rho(A)+e^{-i\theta}\rho(A)^{-1}
+e^{i\phi}\rho(B)+e^{-i\phi}\rho(B)^{-1}.
\]

The matrix is Hermitian.

---

## Theorem 16.E · uniform gap from the Cayley diameter

For every generating pair `(A,B)` and every `(theta,phi)`, every eigenvalue `lambda` of `H_{A,B}(theta,phi)` satisfies

\[
\boxed{ |\lambda| < 4-\frac1{120}. }
\]

In particular

\[
\boxed{
4I-H_{A,B}(\theta,\phi)\succeq \frac1{120}I
}
\]

uniformly over all 2280 ordered generating pairs and the full two-torus.

### Proof

Write

\[
U=\rho(A),\qquad V=\rho(B),
\]

and suppose first that a unit vector `x` satisfies

\[
\langle Hx,x\rangle\ge 4-\delta.
\]

Since

\[
\langle Hx,x\rangle
=2\Re\bigl(e^{i\theta}\langle Ux,x\rangle\bigr)
+2\Re\bigl(e^{i\phi}\langle Vx,x\rangle\bigr)
\]

and each real part is at most `1`, the two deficits have nonnegative sum at most `delta/2`.  Hence

\[
\|e^{i\theta}Ux-x\|\le \sqrt\delta,
\qquad
\|e^{i\phi}Vx-x\|\le \sqrt\delta.
\]

The same estimates hold for the inverse generators with the inverse phases.

Let `g` be represented by a word of length `ell` in `A^{+/-1},B^{+/-1}`.  Multiplying the corresponding phase factors and telescoping gives a unit scalar `zeta_g` such that

\[
\|\zeta_g\rho(g)x-x\|\le \ell\sqrt\delta.
\]

Therefore

\[
|\langle \rho(g)x,x\rangle|
\ge 1-\frac{\ell^2\delta}{2}.
\]

The exact finite certificate

`certificates/a5_uniform_spectral_gap_diameter_certificate.py`

checks all 38 simultaneous-conjugacy classes of generating pairs and proves that every associated Cayley graph has diameter at most `10`.  Hence every `g in A5` may be chosen with `ell <= 10`, so

\[
|\langle \rho(g)x,x\rangle|
\ge 1-50\delta.
\]

Now use Schur orthogonality for the irreducible three-dimensional representation:

\[
\frac1{|A_5|}\sum_{g\in A_5}
|\langle \rho(g)x,x\rangle|^2
=\frac13.
\]

Thus, whenever `1-50 delta >= 0`,

\[
\frac13\ge (1-50\delta)^2,
\]

so

\[
\delta\ge \frac{1-1/\sqrt3}{50}.
\]

Finally

\[
\frac1{\sqrt3}<\frac7{12}
\]

because `48<49`, and therefore

\[
\frac{1-1/\sqrt3}{50}>
\frac{1-7/12}{50}=
\frac1{120}.
\]

Hence no eigenvalue can lie in `(4-1/120,4]`.

For the lower edge observe

\[
-H_{A,B}(\theta,\phi)
=H_{A,B}(\theta+\pi,\phi+\pi).
\]

Applying the same upper-edge estimate after shifting both phases by `pi` gives the symmetric lower bound.  This proves

\[
|\lambda|<4-\frac1{120}.
\]

∎

---

## Corollary 16.F · the boundary Mahler observer is uniformly regular

At `mu=4`,

\[
L_{A,B}(\theta,\phi;4)=4I-H_{A,B}(\theta,\phi)
\]

is uniformly positive definite, with

\[
\lambda_{\min}(L_{A,B})>\frac1{120}.
\]

Consequently

\[
M_{A,B}(4)=\frac1{(2\pi)^2}
\iint \log\det(4I-H_{A,B})\,d\theta\,d\phi
\]

is finite for every generating pair.

Moreover the logarithmic trace series is absolutely and uniformly convergent at the boundary, because

\[
\left\|\frac{H_{A,B}(\theta,\phi)}4\right\|
<\frac{479}{480}<1.
\]

Thus

\[
\boxed{
M_{A,B}(4)
=3\log4-
\sum_{n\ge1}
\frac{1}{n4^n}
\left\langle\operatorname{Tr}H_{A,B}^n\right\rangle.
}
\]

No limiting interpretation `mu downarrow 4` is needed: the series itself converges at `mu=4`.

---

## What this closes — and what it does not

The previous `mu >= 23/5` theorem used the crude universal norm bound `||H|| <= 4`; its geometric tail estimate therefore became singular at `mu=4`.

The present theorem removes that obstruction completely:

\[
\boxed{
\text{the A5 three-dimensional observer has a genuine uniform spectral gap at }\mu=4.
}
\]

However, the explicit rational gap `1/120` is intentionally coarse.  Inserted blindly into the old order-40 tail estimate it is not yet strong enough to certify the small numerical separation between the `3A` and `5B` Mahler bands at `mu=4`.

So the remaining barrier is now sharply identified:

> prove the **class-ordering gap**, not the positivity gap.

Numerical reconnaissance on all 38 simultaneous-conjugacy representatives gives at `mu=4` the bands

\[
M_{5A}\approx 3.5817\ldots\text{ to }3.6082\ldots,
\]

\[
M_{3A}\approx 3.6322\ldots\text{ to }3.6508\ldots,
\]

\[
M_{5B}\approx 3.6552\ldots\text{ to }3.6641\ldots,
\]

so the ordering suggested by the large-`mu` theorem persists numerically:

\[
M_{5A}<M_{3A}<M_{5B}.
\]

These decimal bands are **diagnostic only**, not part of the theorem.

---

## Next strike

The next exact task is to replace the coarse diameter gap by a sharper orbit-wise spectral bound, or to combine the now-convergent boundary series with a certified interval quadrature / higher-moment tail so that the smallest `5B-3A` boundary gap is proved positive.
