# HATTER-SOL-21 · EVEN-DISCRIMINANT WORLD COLLAPSE TO EULER-JACOBI

Status: **EXACT RUNTIME COMPILATION THEOREM**

## 1. Canonical even-discriminant world

For a canonical fundamental discriminant

\[
D\equiv0\pmod4,
\]

H21 uses

\[
B=0,
\qquad
C=D/4.
\]

The quadratic algebra is

\[
A_n=(\mathbf Z/n\mathbf Z)[x]/(x^2-C).
\]

Assume \(n\) is odd and

\[
\gcd(n,C)=1.
\]

## Theorem H21-EJ1 — exact scalar collapse

For every odd \(n\),

\[
\boxed{
x^n=C^{(n-1)/2}x
}
\]

inside \(A_n\).

The conjugation is

\[
\tau(x)=-x.
\]

Moreover,

\[
\left(\frac Dn\right)
=
\left(\frac{4C}{n}\right)
=
\left(\frac Cn\right).
\]

Therefore the H21 expected prime-law response is

\[
\left(\frac Cn\right)x,
\]

and the complete quadratic defect is

\[
\boxed{
\delta_W(n)
=
\left(
0,\,
C^{(n-1)/2}
-
\left(\frac Cn\right)
\right)
\pmod n.
}
\]

### Proof

Because \(n\) is odd,

\[
x^n=x(x^2)^{(n-1)/2}
=
C^{(n-1)/2}x.
\]

The Jacobi identity follows because \(4\) is a square modulo every odd
denominator coprime to \(C\). QED.

## Corollary H21-EJ2 — exact Euler-Jacobi equivalence

The quadratic world passes its Frobenius equality iff

\[
\boxed{
C^{(n-1)/2}
\equiv
\left(\frac Cn\right)
\pmod n.
}
\]

This is exactly the Euler-Jacobi congruence underlying the
Solovay-Strassen probable-prime test with base \(C\).

Thus canonical \(B=0\) worlds are not genuinely two-dimensional quadratic
observers.

They are scalar Euler-Jacobi observers embedded in a quadratic algebra.

## Corollary H21-EJ3 — factor observer equivalence

The constant defect coordinate is identically zero.

The only nontrivial factor projection is

\[
\boxed{
g=
\gcd\left(
n,\,
C^{(n-1)/2}
-
\left(\frac Cn\right)
\right).
}
\]

Whenever

\[
1<g<n,
\]

the quadratic H21 observer and the scalar Euler-Jacobi observer expose exactly
the same factor.

No quadratic-algebra multiplication is required.

## 2. Runtime compiler rule

A world descriptor can be compiled by its presentation:

### \(B=0\)

Emit a scalar Euler-Jacobi observer:

1. precheck \(\gcd(n,C)\);
2. compute Jacobi \((C/n)\);
3. compute
   \[
   C^{(n-1)/2}\bmod n;
   \]
4. gcd the scalar defect.

### \(B\ne0\)

Retain the genuine quadratic Frobenius observer.

Hence the runtime world compiler has an exact architecture split:

\[
\boxed{
B=0
\Rightarrow
\text{scalar Euler core},
}
\]

\[
\boxed{
B\ne0
\Rightarrow
\text{quadratic algebra core}.
}
\]

## 3. Relation to projective collapse

H21-PG1 found

\[
e_p\le2
\]

for canonical \(B=0\) worlds.

H21-EJ1 explains why:

\[
x^2=C
\]

is already scalar, so the projective orbit has at most two rays.

The projective collapse and Euler-Jacobi collapse are the same structural fact
seen locally and globally.

## 4. Hardware significance

Unlike the factor-conditioned quantities \(e_p,d_p\), the condition \(B=0\)
is known directly from the world descriptor at runtime.

Therefore this reduction is directly implementable.

A heterogeneous H21 engine may route:

- \(B=0\) worlds to a scalar modular-exponentiation datapath;
- \(B\ne0\) worlds to the full quadratic datapath.

This is a legitimate target for FPGA area/latency/energy comparison.

## 5. Claim boundary

Euler's criterion and Solovay-Strassen are classical.

H21 does not claim a new primality test here.

The H21 contribution is the exact compiler identification that a whole
canonical world class collapses to the scalar test, allowing a mixed
world-runtime architecture without changing observer semantics.
