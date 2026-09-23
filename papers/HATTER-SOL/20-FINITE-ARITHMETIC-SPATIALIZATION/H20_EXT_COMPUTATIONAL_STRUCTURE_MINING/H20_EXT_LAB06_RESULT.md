# H20-EXT-LAB-06 · Exact conditional Walsh expectation result

Status: **C1 SURVIVES EXACT-EXPECTATION GATE**

Run: GitHub Actions `35580373007`.

## Self-test

The one-stratum second-moment formula was checked against explicit enumeration of a finite fixed-sign multiset.

[
oxed{	ext{SELFTEST PASS}}
]

## Frozen criterion

LAB-06 was frozen before execution with the requirement

[
L_W(4)_{m prime}
<
mathbb E[L_W(4)_{m stratified}]
]

for every

[
W=13,ldots,19.
]

The stratified ensemble uniformly permutes prime/nonprime sign labels independently inside every joint cell

[
(nmod210,lfloorlog_2 nfloor),
]

preserving exact finite prime counts in every such cell.

## Exact finite result

| W | observed low-4 | exact conditional expectation | delta = observed - expected |
|---:|---:|---:|---:|
| 13 | 0.0959908962250 | 0.100415605950 | -0.00442470972460 |
| 14 | 0.0748510360718 | 0.0786800574402 | -0.00382902136846 |
| 15 | 0.0590400993824 | 0.0620445816911 | -0.00300448230871 |
| 16 | 0.0481837540865 | 0.0500804878770 | -0.00189673379053 |
| 17 | 0.0403356489260 | 0.0414212566959 | -0.00108560776997 |
| 18 | 0.0341052222066 | 0.0348872719020 | -0.000782049695455 |
| 19 | 0.0295731101069 | 0.0299704792774 | -0.000397369170504 |

Therefore

[
oxed{
Delta_W^{m exact}<0
qquad
	ext{for every }W=13,ldots,19.
}
]

No random seeds enter this statement.

## Exact conditional expectation formula

For a stratum (G), let

[
m=|G|,
qquad
s=sum_{xin G}Y_x,
qquad
A_{G,S}=sum_{xin G}chi_S(x).
]

Then

[
mathbb E[Z_{G,S}]
=
rac{sA_{G,S}}m
]

and for (m>1)

[
operatorname{Var}(Z_{G,S})
=
rac{(m^2-s^2)(m^2-A_{G,S}^2)}
{m^2(m-1)}.
]

Independence between strata gives the exact coefficient-square expectation

[
mathbb E[widehat Y(S)^2]
=
left(
sum_Grac{s_GA_{G,S}}{m_G}
ight)^2
+
sum_G
rac{(m_G^2-s_G^2)(m_G^2-A_{G,S}^2)}
{m_G^2(m_G-1)}.
]

Summing over (1le |S|le4) gives the exact conditional expectation in the table.

## Interpretation

C1 is no longer merely a five-seed empirical observation.

The exact finite statement is now:

> On every tested width W=13..19, the exact prime indicator has less cumulative Walsh energy in degrees 1 through 4 than the exact conditional ensemble mean obtained by uniformly randomizing labels while preserving all prime counts by mod-210 residue and dyadic magnitude shell.

This is a reproducible finite arithmetic/Boolean discrepancy.

## Non-claim

This does not yet establish:

- an asymptotic inequality;
- statistical tail probability under the permutation ensemble;
- novelty relative to the Fourier-Walsh prime literature;
- a circuit lower bound;
- any RH implication.

## Next falsification gate

The dyadic-shell control is still coarse.

The next experiment must preserve prime counts simultaneously by:

[
nmod210
]

and substantially finer contiguous magnitude blocks.

If the deficit disappears under finer density preservation, C1 is explained by within-shell density variation and must be closed.

If it survives, the candidate becomes materially stronger.
