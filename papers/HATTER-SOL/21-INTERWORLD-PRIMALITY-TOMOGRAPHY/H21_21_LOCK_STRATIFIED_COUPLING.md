# HATTER-SOL-21 · LOCK-STRATIFIED COUPLING THEOREM

Status: **EXACT DECOMPOSITION LAYER**

Fix a quadratic-character stratum

\[
s\in\{++, +-, --\}.
\]

Let the orientation-invariant shared-clock class be

\[
L\in\{T,+,-,0\},
\]

where

\[
T:\ g\le2,
\]

\[
+:\ g>2,\ pq\equiv1\pmod g,
\]

\[
-:\ g>2,\ pq\equiv-1\pmod g,
\]

and

\[
0:\ g>2,\ pq\not\equiv\pm1\pmod g.
\]

For every lock class, let

\[
\pi_{s,\ell}(a)
=
\Pr[X=a\mid s,L=\ell].
\]

Let

\[
K_{s,\ell}
\]

be the coupling computed inside that class.

## Theorem H21-LS1

For every fixed character stratum,

\[
\boxed{
K_s
=
\sum_\ell w_{\ell|s}K_{s,\ell}
-
\sum_a
\operatorname{Var}_{L|s}
\big(
\pi_{s,L}(a)
\big).
}
\]

Define

\[
K_{s,\mathrm{within-lock}}
=
\sum_\ell w_{\ell|s}K_{s,\ell},
\]

and

\[
H_{s,\mathrm{lock}}
=
\sum_a
\operatorname{Var}_{L|s}
\big(
\pi_{s,L}(a)
\big)
\ge0.
\]

Then

\[
\boxed{
K_s
=
K_{s,\mathrm{within-lock}}
-
H_{s,\mathrm{lock}}.
}
\]

### Proof

Apply the law of total covariance inside the fixed character stratum, using
the lock class \(L\) as the conditioning variable.

Because \(L\) is orientation-invariant, the two conditional directional
marginals are equal.

Summing the four diagonal indicator covariances gives the result exactly.

## Consequence

If

\[
H_{s,\mathrm{lock}}
\]

accounts for most of \(|K_s|\), then simple shared-clock lock classes explain
the residual coupling.

If instead

\[
|K_{s,\mathrm{within-lock}}|
\]

remains large, then the mechanism lies inside the detailed phase-set incidence
even after both character type and coarse clock lock have been fixed.

This theorem therefore supplies a clean stopping test for the coarse clock
hypothesis.
