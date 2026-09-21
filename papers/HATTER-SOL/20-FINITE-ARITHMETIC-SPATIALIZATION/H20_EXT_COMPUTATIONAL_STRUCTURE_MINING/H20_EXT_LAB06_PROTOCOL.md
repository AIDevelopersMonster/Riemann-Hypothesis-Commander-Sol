# H20-EXT-LAB-06 · Exact conditional expectation of low-degree Walsh energy

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

LAB-05 independently validated the finite candidate

[
L_W(4)_{m prime}
<
L_W(4)_{m sampled stratified shuffle}
]

on fresh widths W=17,18 and extrapolation W=19.

The remaining weakness is that the baseline was represented by five random seeds.

LAB-06 removes the sampling layer.

## 2. Randomization ensemble

Fix width W.

Partition the Boolean cube indices by

[
G=(nmod210,lfloorlog_2 nfloor),
]

with a special shell for n=0.

Inside each stratum G, uniformly permute the observed prime/nonprime sign labels while preserving the exact label multiset in G.

Different strata are randomized independently.

Thus the ensemble preserves exactly the full finite table of prime counts by joint mod-210 residue and dyadic magnitude shell.

## 3. Exact one-stratum moment formula

Use sign labels

[
Y_xin{+1,-1}.
]

For one stratum G define

[
m=|G|,
qquad
s=sum_{xin G}Y_x.
]

For a Walsh character

[
chi_S(x)=(-1)^{Scdot x}
]

define

[
A=sum_{xin G}chi_S(x).
]

Under a uniform permutation of the fixed sign multiset inside G,

[
mathbb E[Y_x]=rac{s}{m}.
]

For distinct x,y in G,

[
mathbb E[Y_xY_y]
=
rac{s^2-m}{m(m-1)}.
]

Hence for

[
Z_{G,S}
=
sum_{xin G}Y_xchi_S(x),
]

[
mathbb E[Z_{G,S}]
=
rac{sA}{m},
]

and, for m>1,

[
oxed{
operatorname{Var}(Z_{G,S})
=
rac{(m^2-s^2)(m^2-A^2)}
{m^2(m-1)}.
}
]

For m=1 the variance is zero.

Because strata are independent,

[
widehat Y(S)=sum_G Z_{G,S}
]

has

[
oxed{
mathbb E[widehat Y(S)^2]
=
left(
sum_G rac{s_GA_{G,S}}{m_G}
ight)^2
+
sum_G
rac{(m_G^2-s_G^2)(m_G^2-A_{G,S}^2)}
{m_G^2(m_G-1)}.
}
]

This is the exact finite conditional expectation for one Walsh coefficient square.

## 4. Exact expected degree energies

Define

[
mathbb E[E_{W,k}]
=
sum_{|S|=k}
mathbb E[widehat Y(S)^2].
]

LAB-06 computes k=1,2,3,4 exactly from the combinatorial moment formula.

The cumulative expected low-degree mass is

[
mathbb E[L_W(4)]
=
rac{
sum_{k=1}^{4}mathbb E[E_{W,k}]
}{2^{2W}}.
]

The observed prime value uses the exact deterministic prime sign function.

## 5. Frozen widths

Compute:

[
W=13,14,15,16,17,18,19.
]

These widths include:

- the LAB-04 residual range;
- the LAB-05 fresh validation range;
- the LAB-05 extrapolation width.

No new statistic is selected after execution.

## 6. Frozen criterion

C1 survives replacement of Monte Carlo by the exact ensemble mean only if

[
oxed{
L_W(4)_{m prime}
<
mathbb E[L_W(4)_{m stratified}]
}
]

for every

[
W=13,ldots,19.
]

If the sign reverses at any width, C1 is closed.

The primary reported discrepancy is

[
Delta_W^{m exact}
=
L_W(4)_{m prime}
-
mathbb E[L_W(4)_{m stratified}].
]

No fitted trend is part of LAB-06.

## 7. Numerical representation

All combinatorial inputs m,s,A and the observed Walsh coefficient squares are exact integers.

The expectation formula is rational.

The implementation may evaluate the final rational sums in extended precision, but must report enough digits that the sign of the discrepancy is separated from numerical roundoff by many orders of magnitude.

A brute-force self-test on small strata must verify the moment formula against explicit enumeration.

## 8. Required artifacts

- `exact_stratified_expectation.csv`;
- `H20_EXT_LAB06_REPORT.md`;
- self-test PASS record.

## 9. Interpretation boundary

If C1 survives, the valid statement becomes:

> for W=13..19, the observed cumulative Walsh energy on degrees 1..4 of the exact finite prime indicator lies below the exact conditional expectation under uniform within-stratum permutation preserving all prime counts by mod-210 residue and dyadic shell.

This is substantially stronger than a five-seed empirical comparison.

It is still not an asymptotic theorem or a novelty claim.

No RH interpretation is permitted.
