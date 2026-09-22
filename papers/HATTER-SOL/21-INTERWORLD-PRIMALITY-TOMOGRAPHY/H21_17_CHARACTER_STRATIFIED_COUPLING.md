# HATTER-SOL-21 · CHARACTER-STRATIFIED COUPLING THEOREM

Status: **EXACT DECOMPOSITION THEOREM / ARITHMETIC COUPLING LAYER**

## 1. Setup

For a fixed quadratic world \(W=(B,C,\Delta)\), let

\[
X=L_W(p\leftarrow q),
\qquad
Y=L_W(q\leftarrow p)
\]

be the reciprocal zero masks after randomizing the orientation of an unordered
prime pair \(\{p,q\}\).

Let

\[
\chi_p=\left(\frac{\Delta}{p}\right),
\qquad
\chi_q=\left(\frac{\Delta}{q}\right).
\]

Define the orientation-invariant character stratum

\[
\boxed{
S=\{\chi_p,\chi_q\}
\in
\{++, +-, --\}.
}
\]

Because orientation is symmetrized, conditional on \(S=s\) the two directional
marginals are equal. Denote this common marginal by

\[
\pi_s(a)=\Pr[X=a\mid S=s]
=
\Pr[Y=a\mid S=s].
\]

Let

\[
w_s=\Pr[S=s].
\]

## 2. Conditional coupling

Inside stratum \(s\), define

\[
G_s
=
1-\sum_a\pi_s(a)^2,
\]

\[
Q_s
=
\Pr[X\ne Y\mid S=s],
\]

and

\[
\boxed{
K_s=Q_s-G_s.
}
\]

The unconditional coupling remains

\[
K=Q-G.
\]

## Theorem H21-CS1 — within-stratum minus heterogeneity

The total coupling decomposes exactly as

\[
\boxed{
K
=
\sum_s w_s K_s
-
\sum_a
\operatorname{Var}_{S}
\big(
\pi_S(a)
\big).
}
\]

Equivalently,

\[
\boxed{
K
=
K_{\rm within}
-
H_{\rm char},
}
\]

where

\[
K_{\rm within}
=
\sum_s w_s K_s
\]

and

\[
\boxed{
H_{\rm char}
=
\sum_a
\operatorname{Var}_{S}
\big(
\pi_S(a)
\big)
\ge0.
}
\]

### Proof

For each mask \(a\), define

\[
I_a=\mathbf 1_{\{X=a\}},
\qquad
J_a=\mathbf 1_{\{Y=a\}}.
\]

The law of total covariance gives

\[
\operatorname{Cov}(I_a,J_a)
=
\mathbb E[
\operatorname{Cov}(I_a,J_a\mid S)
]
+
\operatorname{Cov}(
\mathbb E[I_a\mid S],
\mathbb E[J_a\mid S]
).
\]

By orientation symmetry,

\[
\mathbb E[I_a\mid S=s]
=
\mathbb E[J_a\mid S=s]
=
\pi_s(a),
\]

so the second term is

\[
\operatorname{Var}_S(\pi_S(a)).
\]

Summing over masks and using

\[
K=-\sum_a\operatorname{Cov}(I_a,J_a)
\]

and

\[
K_s
=
-\sum_a
\operatorname{Cov}(I_a,J_a\mid S=s)
\]

gives the result. QED.

## Corollary H21-CS2 — arithmetic heterogeneity is always negative

The character-mixture contribution satisfies

\[
\boxed{
-H_{\rm char}\le0.
}
\]

Therefore variation of the local mask distributions between

\[
++,\quad+-,\quad--
\]

classes can only move the total coupling **downward** relative to the weighted
within-stratum coupling.

This supplies a universal mechanism for negative \(K\).

## Corollary H21-CS3 — condition for positive total coupling

If

\[
K>0,
\]

then necessarily

\[
\boxed{
K_{\rm within}>H_{\rm char}.
}
\]

Thus positive coupling requires genuine same-mask repulsion *inside* the
character strata strong enough to overcome the negative heterogeneity penalty.

## Corollary H21-CS4 — zero within-stratum coupling

If all character strata are conditionally independent at the mask level,

\[
K_s=0
\quad
\text{for all }s,
\]

then

\[
\boxed{
K=-H_{\rm char}\le0.
}
\]

Hence negative coupling may arise even when there is no reciprocal dependence
inside any fixed split/inert class.

It can be generated purely by mixing arithmetic populations with different
mask marginals.

## 3. Per-mask form

For each mask \(a\),

\[
c_a
=
\operatorname{Cov}(
\mathbf1_{X=a},
\mathbf1_{Y=a}
)
\]

decomposes as

\[
\boxed{
c_a
=
\sum_s w_s c_{a,s}
+
\operatorname{Var}_S(\pi_s(a)).
}
\]

Thus the observed self-mask attraction has two sources:

1. genuine reciprocal synchronization inside a character stratum;
2. population heterogeneity across split/inert strata.

The second source is always attractive.

## 4. Why this is arithmetic rather than arbitrary conditioning

The stratifier

\[
S=\{\chi_p,\chi_q\}
\]

is not chosen after seeing the mask.

It is intrinsic to the quadratic world and already enters the exact Lucas
zero conditions.

Hence \(H_{\rm char}\) measures how much of coupling is explained simply by
the split/inert geometry of the two prime factors.

The residual

\[
K_{\rm within}
\]

is the coupling that remains after controlling for quadratic-character type.

## 5. Compiler consequence

The world compiler can estimate coupling in layers:

\[
\boxed{
\text{pooled marginal}
\to
G
\to
\text{character-stratified marginals}
\to
H_{\rm char}
\to
K_{\rm within}
\to
K.
}
\]

If

\[
|K_{\rm within}|\ll H_{\rm char},
\]

then most coupling is explained without reciprocal pairwise training.

If \(K_{\rm within}\) remains large, deeper Lucas-clock synchronization is
required.

## 6. Next refinement

The same theorem applies to any orientation-invariant arithmetic stratum.

Possible refinements include

\[
S=(\{\chi_p,\chi_q\},\{p\bmod4,q\bmod4\}),
\]

or bins of

\[
\gcd(h_W(p),h_W(q)).
\]

Every refinement separates coupling into:

\[
\text{within-bin reciprocal dependence}
-
\text{between-bin marginal heterogeneity}.
\]

The scientific objective is to find the coarsest arithmetic stratifier that
explains most of \(K\).

## 7. Claim boundary

The law of total covariance is classical.

The H21-specific theorem is its application to the exact quadratic
split/inert stratification of the Lucas zero-mask factor observer.

The new empirical question is whether \(H_{\rm char}\) explains a substantial
fraction of the broad negative coupling observed in H21-LAB-11.
