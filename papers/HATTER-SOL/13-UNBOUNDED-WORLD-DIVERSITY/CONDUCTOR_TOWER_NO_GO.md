# HATTER-SOL-13 · CONDUCTOR-TOWER NO-GO

**Status:** exact theorem layer, revised after external mathematical review  
**Scope:** fixed imaginary quadratic field, varying orders, fixed rational integer.

## 1. Setup

Let `K` be an imaginary quadratic field with maximal order

\[
\mathcal O_K=\mathbb Z[\omega].
\]

For each positive conductor `f`, let

\[
\mathcal O_f=\mathbb Z+f\mathcal O_K=\mathbb Z[f\omega].
\]

Fix a positive rational integer `n`.

Define

\[
\operatorname{Div}_K(n)
=\{\alpha\in\mathcal O_K:\exists\beta\in\mathcal O_K,\ \alpha\beta=n\}.
\]

## 2. Finite ambient divisor set

### Lemma CT13.1

Modulo the finite unit group of `K`, the set `Div_K(n)` is finite.

### Proof

If `\alpha\beta=n`, then

\[
|N(\alpha)|\,|N(\beta)|=n^2.
\]

Hence `|N(\alpha)|<=n^2`. The norm form of an imaginary quadratic field is positive definite, so only finitely many algebraic integers have norm bounded by `n^2`. The unit group is finite. QED.

Every element divisor occurring in any order `O_f` belongs to this same finite ambient set.

## 3. Membership law

Write

\[
\alpha=a+b\omega,\qquad a,b\in\mathbb Z.
\]

Then

\[
\boxed{\alpha\in\mathcal O_f\iff f\mid b.}
\]

For a rational prime `p`, along

\[
\mathcal O_K\supset\mathcal O_p\supset\mathcal O_{p^2}\supset\cdots,
\]

a non-rational divisor `a+b\omega` survives exactly while

\[
r\le v_p(b).
\]

Rational divisors (`b=0`) survive at every level.

## 4. Divisor-poset stabilization

Let

\[
M_p(n;K)
=
\max\{v_p(b):a+b\omega\in\operatorname{Div}_K(n),\ b\ne0\},
\]

with `M_p=-1` if there is no non-rational divisor.

### Theorem CT13.2 — conductor-tower stabilization

For every fixed `n`, `K`, and rational prime `p`, all non-rational element divisors of `n` disappear from `O_{p^r}` once

\[
r>M_p(n;K).
\]

Consequently, beyond that level the element-divisor poset of `n` contains only rational integer divisors and is independent of `r`.

### Proof

The ambient divisor set is finite by CT13.1. For each non-rational divisor `a+b\omega`, membership in `O_{p^r}` is equivalent to `p^r|b` and therefore fails for `r>v_p(b)`. Taking the maximum over the finite ambient divisor set eliminates all non-rational divisors simultaneously. The remaining rational divisors lie in every order. QED.

### Corollary CT13.2a

Any invariant depending only on the finite element-divisor poset is eventually constant along a prime-power conductor tower.

This corollary replaces the earlier informal wording about a response being "determined functorially" by the divisor/interface poset.

## 5. Global finite diversity

### Corollary CT13.3

Across all conductors `f>=1` in one fixed imaginary quadratic field, a fixed rational integer `n` realizes only finitely many element-divisor posets.

### Proof

Every order-specific divisor set is a subset of the single finite ambient set `Div_K(n)`. Hence only finitely many subsets and induced finite posets can occur. QED.

Therefore every invariant that factors through this finite divisor-poset data takes only finitely many values as the conductor varies.

## 6. Independent quotient-ring saturation

If `\omega^2-T\omega+N=0` and `t=f\omega`, then

\[
t^2=fTt-f^2N.
\]

Hence

\[
\mathcal O_f/n\mathcal O_f
\cong
(\mathbb Z/n\mathbb Z)[t]/(t^2-fTt+f^2N).
\]

The ring structure depends only on `f mod n`. Any observer that factors through this quotient therefore also has only finitely many conductor responses.

## 7. Programme consequence

Varying the conductor inside one fixed imaginary quadratic field cannot produce unbounded fixed-`n` element-divisor diversity. The conductor candidate is closed negatively; field-degree growth is required to escape this finite ambient-divisor obstruction.