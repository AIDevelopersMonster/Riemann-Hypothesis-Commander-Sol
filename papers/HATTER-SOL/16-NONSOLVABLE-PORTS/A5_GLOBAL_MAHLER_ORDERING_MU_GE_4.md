# HATTER-SOL-16 · Global A5 Mahler ordering for all mu >= 4

## Status

**Closed theorem layer.**

This note closes the final scalar-parameter gap in the A5 laboratory.

For a generating pair `(A,B)` in `A5`, let

\[
H_{A,B}(\theta,\phi)=
 e^{i\theta}\rho_3(A)+e^{-i\theta}\rho_3(A)^{-1}
 +e^{i\phi}\rho_3(B)+e^{-i\phi}\rho_3(B)^{-1}
\]

for one fixed real three-dimensional irreducible representation `rho_3`, and define

\[
M_{A,B}(\mu)=\frac1{(2\pi)^2}\int_{\mathbb T^2}
\log\det(\mu I-H_{A,B}(\theta,\phi))\,d\theta\,d\phi,
\qquad \mu\ge4.
\]

The generating commutator `[A,B]` lies only in `3A`, `5A`, or `5B`.

---

## Theorem 16.F · global nonsolvable Mahler class ordering

For every generating pair `(A,B)` in `A5` and every real parameter

\[
\mu\ge4,
\]

the scalar determinant/Mahler observer satisfies

\[
\boxed{
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu).
}
\]

More strongly, for every fixed `mu >= 4`, every one of the four `5A` Mahler types lies below every one of the six `3A` types, and every `3A` type lies below every one of the four `5B` types.

Thus a single three-dimensional scalar determinant observer separates the three possible generating-commutator classes of the smallest nonsolvable simple group throughout the complete natural parameter range.

---

## Proof architecture

The theorem is the union of two independently certified parameter regimes.

### 1. Large and intermediate parameter range

The exact moment/interval certificate

`certificates/a5_mahler_separation_mu_23_over_5_certificate.py`

proves

\[
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
\qquad
\text{for all }\mu\ge\frac{23}{5}.
\]

### 2. Compact strip

The certificate

`certificates/a5_global_mahler_mu_ge_4_certificate.py`

closes

\[
4\le\mu\le\frac{23}{5}.
\]

It reuses the exact determinant construction and the typewise tensor-gap bounds from the audited boundary certificate.

---

## Normalized monotone observer

The compact-strip proof becomes finite after removing the universal first terms of the logarithmic expansion.

Torus balancing gives vanishing odd moments, and the exact second moment is

\[
S_2=\langle\operatorname{Tr}H^2\rangle=12
\]

for every generating pair. Hence

\[
M(\mu)
=3\log\mu-\frac6{\mu^2}
-\sum_{m\ge2}\frac{S_{2m}}{2m\mu^{2m}}.
\]

Define

\[
\boxed{
G(\mu):=M(\mu)-3\log\mu+\frac6{\mu^2}.
}
\]

Since `H(theta,phi)` is Hermitian,

\[
S_{2m}=\left\langle\operatorname{Tr}H^{2m}\right\rangle\ge0.
\]

Therefore

\[
G'(\mu)
=
\sum_{m\ge2}\frac{S_{2m}}{\mu^{2m+1}}
\ge0.
\]

So `G` is monotone nondecreasing for every one of the fourteen exact Mahler types.

This monotonicity is the key device that turns point certificates into certificates for whole parameter intervals.

---

## Finite slab chain

The compact interval is divided into the 60 rational slabs

\[
\left[4+\frac{k}{100},\;4+\frac{k+1}{100}\right],
\qquad k=0,\dots,59.
\]

At every rational node the script constructs the exact Laurent determinant polynomial over

\[
\mathbf Q(\sqrt5)
\]

and evaluates the periodic trapezoidal average with outward-rounded interval arithmetic.

For each Mahler type the previously certified tensor gap `gamma` implies

\[
\frac{\|H\|}{4}<q_\gamma:=\sqrt{1-\frac\gamma6}.
\]

At parameter `mu >= 4` the logarithmic Fourier ratio is therefore

\[
r_\gamma(\mu)=\frac{4q_\gamma}{\mu}<1,
\]

and the same support argument as in the boundary theorem gives the rigorous aliasing enclosure

\[
\boxed{
|G(\mu)-T_M^{\rm norm}(\mu)|
\le
\frac{6r_\gamma(\mu)^M}{M(1-r_\gamma(\mu))}.
}
\]

For a slab `[a,b]`, monotonicity gives

\[
G_X(\mu)\le G_X(b),
\qquad
G_Y(\mu)\ge G_Y(a).
\]

Thus the two finite endpoint inequalities

\[
G_{5A}(b)<G_{3A}(a),
\qquad
G_{3A}(b)<G_{5B}(a)
\]

imply the desired strict ordering throughout the entire slab.

The certificate checks these inequalities for every relevant pair of the fourteen Mahler types and for all sixty slabs.

---

## Certified margins

The smallest certified slab margin for the first inequality occurs near the upper endpoint of the compact strip and is approximately

\[
\boxed{1.1253\times10^{-2}}.
\]

The tighter second inequality has its smallest certified slab margin in the first slab adjacent to `mu=4`, approximately

\[
\boxed{1.6184\times10^{-3}}.
\]

These numbers are diagnostics extracted from outward-rounded certified intervals; the theorem itself is the strict interval separation asserted by the script.

---

## Consequence for the H15 question

HATTER-SOL-15 obtained global separation in the prime-dihedral laboratory from a scalar first-harmonic dominance theorem.

The A5 theorem shows that the final phenomenon survives in a nonsolvable simple group even though the proof mechanism changes:

\[
\boxed{
\text{higher-dimensional irrep}
\to
\text{commutator trace at length 4}
\to
\text{tensor spectral gap}
\to
\text{monotone normalized determinant observer}
\to
\text{global Mahler class separation}.
}
\]

Thus literal first-harmonic dominance is not required for the first nonsolvable extension. The more robust invariant is a class-sensitive low-order representation trace together with enough spectral control to propagate determinant separation across the parameter range.

---

## Reproducibility

The global result uses the following certificate chain:

- `certificates/a5_generating_pair_commutator_certificate.py`
- `certificates/a5_type_tensor_gap_certificate.py`
- `certificates/a5_boundary_mahler_mu4_interval_certificate.py`
- `certificates/a5_mahler_separation_mu_23_over_5_certificate.py`
- `certificates/a5_global_mahler_mu_ge_4_certificate.py`

The compact-strip script terminates with

`PASS: M(5A)<M(3A)<M(5B) on every slab 4<=mu<=23/5`

and combines this with the previous large-parameter theorem.

---

## A5 laboratory status

The principal A5 scalar-observer problem is now closed for the full natural range `mu >= 4`.

The next main HATTER-SOL-16 strike is therefore `PSL(2,7)`: determine whether a single irreducible determinant channel still separates the relevant commutator classes or whether the first genuinely vector-valued tomography layer appears.