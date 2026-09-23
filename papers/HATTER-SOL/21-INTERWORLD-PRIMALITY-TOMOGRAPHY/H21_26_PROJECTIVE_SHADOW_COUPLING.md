# HATTER-SOL-21 · PROJECTIVE-SHADOW COUPLING DECOMPOSITION

Status: **EXACT DECOMPOSITION LAYER / ACTIVE PUBLICATION-GATE TEST**

## 1. Projective observer code

Fix a nonexceptional local world at prime \(p\).  Write the local phase as

\[
m=r+k e_p,
\]

with projective phase

\[
r\in\mathbf Z/e_p\mathbf Z
\]

and scalar-fiber phase

\[
k\in\mathbf Z/d_p\mathbf Z.
\]

For a fixed incoming character sign \(\sigma\), each of the two zero-bit
observer conditions is an affine level on the scalar ray through \(x^r\).

By H21-PG2, each bit is of exactly one of three projective types on that ray:

1. impossible: no scalar point on the ray satisfies the level;
2. forced: the observer level is zero and the whole scalar fiber satisfies it;
3. optional: the observer level is nonzero and exactly one scalar-fiber phase satisfies it.

Define:

\[
\boxed{
F_{W,p,\sigma}(r)
}
\]

as the two-bit mask of **forced** zero bits, and

\[
\boxed{
S_{W,p,\sigma}(r)
}
\]

as the two-bit mask of all **supported** zero bits, forced or optional.

Then for every scalar phase \(k\), the actual local zero mask \(Z\) satisfies

\[
\boxed{
F(r)\subseteq Z(r,k)\subseteq S(r).
}
\]

The pair

\[
\boxed{
P(r)=(F(r),S(r))
}
\]

is the projective observer code.

It depends only on the projective ray, not on the scalar-fiber coordinate.

## 2. Reciprocal projective stratum

For a semiprime \(pq\), define directional projective codes

\[
P_X=P_{W,p,\chi_q}(q\bmod e_p),
\]

\[
P_Y=P_{W,q,\chi_p}(p\bmod e_q).
\]

Inside a fixed quadratic-character stratum

\[
s\in\{++, +-, --\},
\]

define the orientation-invariant reciprocal projective stratum

\[
\boxed{
R=\{P_X,P_Y\}.
}
\]

Randomizing orientation inside the unordered pair makes the two conditional
directional marginals equal.

## Theorem H21-PS1 — projective-shadow coupling decomposition

Let \(K_s\) be the exact same-mask coupling inside character stratum \(s\).

For each reciprocal projective stratum \(R=\rho\), let

\[
K_{s,\rho}
\]

be the coupling computed after conditioning on \(R=\rho\), and let

\[
\pi_{s,\rho}(a)
\]

be the common conditional mask marginal.

Then

\[
\boxed{
K_s
=
\sum_\rho w_{\rho|s}K_{s,\rho}
-
\sum_a
\operatorname{Var}_{R|s}
\left(
\pi_{s,R}(a)
\right).
}
\]

Define

\[
K_{s,\mathrm{within-proj}}
=
\sum_\rho w_{\rho|s}K_{s,\rho}
\]

and

\[
\boxed{
H_{s,\mathrm{proj}}
=
\sum_a
\operatorname{Var}_{R|s}
\left(
\pi_{s,R}(a)
\right)
\ge0.
}
\]

Then

\[
\boxed{
K_s
=
K_{s,\mathrm{within-proj}}
-
H_{s,\mathrm{proj}}.
}
\]

### Proof

Apply the law of total covariance to the four same-mask indicators inside the
fixed character stratum, conditioning on the orientation-invariant projective
code pair \(R\).

The second total-covariance term is a variance because the two directional
conditional marginals are equal after orientation symmetrization.

Summing over the four diagonal mask indicators and using

\[
K=-\sum_a\operatorname{Cov}(\mathbf1_{X=a},\mathbf1_{Y=a})
\]

gives the identity. QED.

## 3. Support-only control

A coarser code keeps only

\[
S(r),
\]

forgetting whether a supported bit is forced or optional.

Applying the same theorem to the unordered pair

\[
\{S_X,S_Y\}
\]

gives

\[
\boxed{
K_s
=
K_{s,\mathrm{within-shadow}}
-
H_{s,\mathrm{shadow}}.
}
\]

Comparing

\[
H_{\mathrm{shadow}}
\]

with

\[
H_{\mathrm{proj}}
\]

measures the added explanatory value of distinguishing complete zero fibers
from one-point affine transversals.

## 4. Interpretation

Three outcomes are possible.

### Projective geometry dominates

If

\[
H_{s,\mathrm{proj}}
\approx |K_s|
\]

and the residual

\[
K_{s,\mathrm{within-proj}}
\]

is small, reciprocal coupling is largely explained before scalar-fiber
coordinates are inspected.

### Scalar fibers dominate

If

\[
H_{s,\mathrm{proj}}\ll |K_s|,
\]

then most coupling survives between pairs having the same reciprocal
projective observer code.

The remaining mechanism must lie in:

\[
k_p,\quad k_q,
\]

or in the partial-transversal graph

\[
k=k_c(r).
\]

### Support is insufficient but forced/optional matters

If

\[
H_{\mathrm{proj}}\gg H_{\mathrm{shadow}},
\]

the distinction between complete fibers and single-point transversals is an
essential geometric feature.

## 5. Publication significance

H21-PS1 itself is a total-covariance identity applied to an H21-specific
projective observer code; the probability identity is not novel.

The publication-relevant question is whether the exact algebraic
projective/scalar decomposition exposes a stable, nontrivial theorem about
reciprocal arithmetic sampling that is not already a repackaging of classical
Lucas/Frobenius machinery.

Accordingly, H21 publication remains gated on:

- broad validation of the projective/scalar mechanism;
- prior-art audit of subgroup/trace-incidence and Lucas/Frobenius literature;
- a theorem controlling reciprocal phase placement or a measured hardware
  advantage derived from the compression.
