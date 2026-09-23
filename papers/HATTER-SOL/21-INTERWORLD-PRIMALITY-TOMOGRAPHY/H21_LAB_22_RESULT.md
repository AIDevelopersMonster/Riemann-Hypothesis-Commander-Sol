# HATTER-SOL-21 · H21-LAB-22 RESULT

Status: **EXPANDED BINARY-LIFT SIGNAL / STILL STATISTICALLY UNDERPOWERED**

Run:

\`35739633735\`

Range:

\[
pq<2^{20}.
\]

## 1. |D| <= 127

Eligible reciprocal binary-lift pairs:

\[
\boxed{914}.
\]

Groups with

\[
n\ge10:
\quad
\boxed{9}.
\]

Groups with

\[
n\ge20:
\quad
\boxed{0}.
\]

Across the retained groups,

\[
\boxed{
\operatorname{mean}|\operatorname{Cov}|
=
0.087295
}
\]

while the deterministic shifted control gives

\[
\boxed{
\operatorname{mean}|\operatorname{Cov}_{\rm control}|
=
0.022910.
}
\]

Maximum observed covariance magnitude:

\[
\boxed{0.173554}.
\]

The covariance sign is not universal:

- positive groups: 5;
- negative groups: 2;
- remaining retained groups have zero covariance at finite precision.

## 2. |D| <= 63

Eligible pairs:

\[
\boxed{691}.
\]

Groups with \(n\ge10\):

\[
\boxed{18}.
\]

Groups with \(n\ge20\):

\[
\boxed{1}.
\]

Mean absolute covariance:

\[
\boxed{0.070747}.
\]

Mean absolute shifted-control covariance:

\[
\boxed{0.009759}.
\]

Maximum observed covariance magnitude:

\[
\boxed{0.210000}.
\]

Again the sign is mixed:

- positive groups: 8;
- negative groups: 3.

## 3. Interpretation

The enlarged experiment produces a signal clearly larger than the deterministic
shift control on average.

However the decisive per-world/per-stratum sample sizes remain small.

Therefore H21 does **not** claim a reciprocal binary-lift law from LAB-22.

The correct statement is:

\[
\boxed{
\text{binary-lift dependence is a viable theorem target, but current finite
statistics are insufficient to identify its law.}
}
\]

The mixed signs also rule out a universal simple assertion such as

\[
\beta_p=\beta_q
\]

or

\[
\beta_p\ne\beta_q
\]

across all worlds.

## 4. Consequence

Further brute-force enlargement is not automatically the best next step.

Before spending substantially more compute, the programme should either:

1. derive a world-specific algebraic relation for the lift bits;
2. or move the publication effort toward the world-compiler / scheduling
   consequence that is already broad and reproducible.

## 5. Publication gate

LAB-22 does not cross the publication threshold.

It strengthens the case that a residual binary arithmetic dependence exists,
but does not supply a stable theorem or statistically mature universal law.
