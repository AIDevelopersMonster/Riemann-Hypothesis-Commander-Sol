# H20-EXT-C1 · Exact finite low-degree Walsh deficit

Status: **FINITE RESULT LAYER / NOVELTY UNRESOLVED / NOT YET PUBLICATION-READY**

## Definition

For fixed width W define the prime sign function

[
f_W(x)=(-1)^{mathbf 1[x	ext{ prime}]},
qquad
0le x<2^W.
]

Let

[
widehat f_W(S)
=
sum_{xin{0,1}^W}f_W(x)(-1)^{Scdot x}.
]

Define cumulative normalized Walsh energy through degree four:

[
oxed{
L_W(4)
=
2^{-2W}
sum_{1le |S|le4}
widehat f_W(S)^2.
}
]

For a finite partition (mathcal G) of the input cube, let (mathfrak R_{mathcal G}) be the ensemble obtained by independently uniformly permuting the fixed prime/nonprime sign labels inside every block (Ginmathcal G).

## Lemma C1.1 · exact conditional coefficient-square expectation

For one block G let

[
m_G=|G|,
qquad
s_G=sum_{xin G}f_W(x),
qquad
A_{G,S}=sum_{xin G}(-1)^{Scdot x}.
]

Then

[
mathbb E_{mathfrak R_{mathcal G}}
[widehat f(S)^2]
=
left(
sum_Grac{s_GA_{G,S}}{m_G}
ight)^2
+
sum_{G:m_G>1}
rac{(m_G^2-s_G^2)(m_G^2-A_{G,S}^2)}
{m_G^2(m_G-1)}.
]

This follows from the exact first and second moments of sampling without replacement inside each block.

The identity is elementary finite combinatorics; no novelty is claimed for the abstract formula.

## Corollary C1.2 · exact expected low-degree energy

[
oxed{
mathbb E_{mathfrak R_{mathcal G}}[L_W(4)]
=
2^{-2W}
sum_{1le|S|le4}
mathbb E[widehat f(S)^2].
}
]

Therefore the comparison with the prime indicator requires no Monte Carlo sampling.

## Proposition C1.3 · dyadic-shell conditioned deficit

Let

[
mathcal G_W^{m dyad}
=
{x:
(xmod210,lfloorlog_2xfloor)
	ext{ fixed}},
]

with a special block for x=0.

Exact computation gives

[
oxed{
L_W(4)
<
mathbb E_{mathfrak R_{mathcal G_W^{m dyad}}}[L_W(4)]
}
]

for every

[
W=13,ldots,19.
]

## Proposition C1.4 · fine local-density conditioned deficit

For block size B define

[
mathcal G_{W,B}^{m local}
=
{x:
(xmod210,lfloor x/Bfloor)
	ext{ fixed}}.
]

Exact computation gives

[
oxed{
L_W(4)
<
mathbb E_{mathfrak R_{mathcal G_{W,B}^{m local}}}[L_W(4)]
}
]

for every

[
Win{17,18,19}
]

and

[
Bin{16384,8192,4096}.
]

## Scientific status

These propositions are exact finite computational statements with reproducible certificates.

They are stronger than the earlier sampled observation because:

1. the baseline expectation is exact;
2. the hypothesis was frozen before fresh hold-out widths were computed;
3. the sign survives several increasingly strong conditioning partitions;
4. the observer is invariant under permutation of bit labels at the level of degree aggregation.

## Non-claim

No asymptotic statement

[
L_W(4)-mathbb E[L_W(4)]<0
quad(W	oinfty)
]

has been proved.

No novelty claim is made until the targeted literature audit is completed.

No relation to RH is asserted.
