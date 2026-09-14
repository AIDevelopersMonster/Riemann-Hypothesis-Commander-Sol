# HATTER-SOL-13 · CONDUCTOR-TOWER NO-GO

**Status:** exact theorem layer  
**Scope:** fixed imaginary quadratic field, varying quadratic orders, fixed rational integer.

## 1. Setup

Let `K` be an imaginary quadratic field with maximal order

\[
\mathcal O_K=\mathbb Z[\omega].
\]

For each positive integer conductor `f`, let

\[
\mathcal O_f=\mathbb Z+f\mathcal O_K=\mathbb Z[f\omega].
\]

Fix a positive rational integer `n`.

We ask whether varying `f` can produce infinitely many genuinely different element-factorization/interface states of the same `n`.

## 2. Finite ambient divisor set

Define the ambient divisor set

\[
\operatorname{Div}_K(n)
=\{\alpha\in\mathcal O_K:\exists\beta\in\mathcal O_K,\ \alpha\beta=n\}.
\]

### Lemma CT13.1

Modulo the finite unit group of the imaginary quadratic field, `Div_K(n)` is finite.

### Proof

If `\alpha\beta=n`, then

\[
|N_{K/\mathbb Q}(\alpha)|\,|N_{K/\mathbb Q}(\beta)|=n^2.
\]

Hence `|N(\alpha)|` is a positive divisor of `n^2`. In an imaginary quadratic field the norm form is positive definite, so only finitely many algebraic integers have norm bounded by `n^2`. The unit group is finite. QED.

Every factor of `n` occurring in any suborder `\mathcal O_f` belongs to this same finite ambient set.

## 3. Membership in a conductor tower

Write an ambient divisor uniquely as

\[
\alpha=a+b\omega,
\qquad a,b\in\mathbb Z.
\]

Then

\[
\boxed{\alpha\in\mathcal O_f\iff f\mid b.}
\]

Therefore, for a prime `p`, along the tower

\[
\mathcal O_{p^0}\supset\mathcal O_{p^1}\supset\mathcal O_{p^2}\supset\cdots,
\]

a non-rational ambient divisor `a+b\omega` survives exactly through the levels

\[
k\le v_p(b).
\]

Rational divisors (`b=0`) survive at every level.

## 4. Eventual stabilization theorem

Let

\[
M_p(n;K)
=
\max\{v_p(b):a+b\omega\in\operatorname{Div}_K(n),\ b\ne0\},
\]

with `M_p=-1` if there is no non-rational divisor.

### Theorem CT13.2 — conductor-tower stabilization

For every fixed `n`, `K`, and rational prime `p`, all non-rational divisors of `n` disappear from `\mathcal O_{p^k}` once

\[
k>M_p(n;K).
\]

Consequently, beyond that level the element-factorization poset of `n` inside `\mathcal O_{p^k}` contains only rational integer divisors and is independent of `k`.

In particular any HATTER response that is determined functorially from the element-factorization/interface poset of `n` is eventually constant along the conductor tower.

### Proof

The ambient divisor set is finite by CT13.1. For each non-rational divisor `a+b\omega`, membership in `\mathcal O_{p^k}` is equivalent to `p^k|b`, hence fails for `k>v_p(b)`. Taking the maximum over the finite set eliminates all non-rational divisors simultaneously. The remaining possible factors are rational integers, which lie in every order. Therefore the factorization poset and every response constructed solely from it stabilize. QED.

## 5. Global finite-diversity corollary

### Corollary CT13.3

Across **all** conductors `f>=1` in one fixed imaginary quadratic field, a fixed rational integer `n` can realize only finitely many element-factorization patterns.

### Proof

Every order-specific factorization uses elements from the finite ambient divisor set `Div_K(n)`. Hence each order selects a sub-poset of one finite poset. Only finitely many such sub-posets exist. QED.

Thus

\[
\boxed{\sup_m D_m(n)<\infty}
\]

for every world family consisting only of quadratic orders inside one fixed imaginary quadratic field, whenever the HATTER response factors through the element-factorization poset.

## 6. Independent quotient-ring saturation

If `\omega` satisfies

\[
\omega^2-T\omega+N=0,
\]

and `t=f\omega`, then

\[
t^2=fTt-f^2N.
\]

Therefore

\[
\mathcal O_f/n\mathcal O_f
\cong
(\mathbb Z/n\mathbb Z)[t]/(t^2-fTt+f^2N).
\]

Its ring structure depends only on the residue class of `f mod n`. Hence any observer that factors through the finite quotient `\mathcal O_f/n\mathcal O_f` also has only finitely many conductor responses.

This gives a second, independent finite-diversity obstruction.

## 7. Programme consequence

Conductor variation inside a fixed imaginary quadratic field cannot realize the HATTER-SOL-13 primary target of unbounded fixed-number diversity.

The first candidate family is therefore **closed negatively**.

Next target: test whether varying the **field degree** can evade the finite ambient-divisor obstruction, since a fixed rational prime can then have factorization patterns with an unbounded number of prime ideals as degree grows.
