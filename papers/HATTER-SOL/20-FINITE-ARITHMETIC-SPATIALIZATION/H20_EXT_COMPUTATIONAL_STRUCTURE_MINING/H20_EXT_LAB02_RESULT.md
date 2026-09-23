# H20-EXT-LAB-02 · Wheel-conditioned continuation quotient

Status: **CLOSED NEGATIVE RESULT / LAB-01 PRIME-SPECIFIC CANDIDATE FALSIFIED**

Protocol frozen before execution in `H20_EXT_LAB02_PROTOCOL.md`.

## 1. Question

LAB-01 found a substantial continuation-quotient compression gap for the raw prime indicator relative to density-matched random and shuffled-prime baselines.

LAB-02 tested the predeclared falsification hypothesis:

[
oxed{
	ext{Is that gap still present after explicitly conditioning away}
atop
	ext{divisibility by small primes?}
}
]

The frozen wheels were

[
Min{2,6,30,210}.
]

For each admissible residue (rpmod M), the exact sequence

[
F_{W,M,r}(k)=mathbf 1[r+Mk	ext{ prime}]
]

was compared with fixed-count random and within-class shuffled baselines having exactly the same sequence length and number of ones.

Both MSB-first and LSB-first variable orders were measured.

## 2. Exact computation

The declared run was completed exhaustively for

[
W=8,ldots,16.
]

The code evaluated:

- every admissible residue class for each wheel;
- both bit orders;
- five predeclared random seeds;
- prime, squarefree and semiprime arithmetic families;
- exact three-terminal continuation quotients with explicit padding terminal.

Reference local artifact SHA-256 values:

- executed tool: `e74049050b9ee65601e945322dfff6d6051bc93a99546f64da4fccad85cfe0e1`;
- full CSV: `415495bf8e4ecf51bff8e02290b5a9b4bcd6033da547e7835279bcb18c27dc1a`;
- summary JSON: `ed52882051f7534091dce83b25523e82c24dc5190fee61d493bec99bc44d0ba7`;
- generated report: `3753d7af8ada63d2c50a11d27b919e09c1c2a1fbedb1b02c6b6a30bb362b25fd`.

The repository tool reproduces the full artifacts; CI stores the full CSV/JSON/Markdown as workflow artifacts.

## 3. Primary result

Define

[
ho_{W,M,sigma}
=
rac{sum_r N_{m prime}(W,M,r,sigma)}
{mathbb E[sum_r N_{m random}(W,M,r,sigma)]}.
]

A value substantially below one would indicate continuation compressibility beyond the fixed-count baseline after the declared wheel conditioning.

### Validation widths

| W | wheel | MSB rho | LSB rho |
|---:|---:|---:|---:|
| 13 | 30 | 0.9929 | 0.9737 |
| 14 | 30 | 0.9990 | 0.9889 |
| 15 | 30 | 1.0005 | 1.0014 |
| 13 | 210 | 1.0079 | 1.0010 |
| 14 | 210 | 1.0108 | 0.9941 |
| 15 | 210 | 1.0103 | 1.0087 |

### Extrapolation gate W=16

For (M=30):

[
ho_{16,30,MSB}=0.9952,
qquad
ho_{16,30,LSB}=0.9981.
]

For (M=210):

[
ho_{16,210,MSB}=1.0040,
qquad
ho_{16,210,LSB}=1.0017.
]

The shuffled-prime baselines give the same qualitative result:

[
ho^{m shuffled}_{16,30}
=
0.9969	ext{ (MSB)},quad0.9957	ext{ (LSB)},
]

[
ho^{m shuffled}_{16,210}
=
1.0049	ext{ (MSB)},quad0.9986	ext{ (LSB)}.
]

Thus the raw LAB-01 compression gap does not survive the stronger wheel conditioning.

## 4. Residue-class check

The aggregate cancellation is not hiding a universal prime advantage inside individual residue classes.

For (M=30), (W=16):

- MSB per-class prime/random ratios range approximately from (0.9826) to (1.0032);
- LSB ratios range approximately from (0.9825) to (1.0107);
- no residue class is below (0.95).

At validation width (W=15):

- MSB mean ratio across the eight reduced residues is (1.0006);
- LSB mean ratio is (1.0014).

For (M=210), individual small finite classes fluctuate above and below one, but by (W=16):

- MSB mean ratio is approximately (1.0041);
- LSB mean ratio is approximately (1.0018).

Therefore there is no coherent across-residue compression signal of the type required by the frozen protocol.

## 5. Falsification decision

The LAB-02 protocol declared the LAB-01 candidate explained by small-modulus structure if, for (M=30) and (M=210), the prime/random ratio approached one within baseline variation across validation widths.

That condition is met.

Therefore:

[
oxed{
	ext{LAB-01 raw continuation-compressibility is not promoted}
atop
	ext{to a prime-specific structural invariant.}
}
]

More strongly, under the declared observer and baselines:

[
oxed{
	ext{conditioning on the }2,3,5,7	ext{ wheel removes the observed advantage}
atop
	ext{to baseline scale on }W=13,ldots,16.
}
]

This is the intended successful-negative outcome of the falsification experiment.

## 6. Observation

The raw prime indicator was substantially more continuation-compressible than density-matched random data.

After residue conditioning by increasingly strong primorial wheels, that advantage decays.

At wheels (30) and (210), the validation/extrapolation ratios are near one and alternate on both sides of one.

## 7. Exact finite statement

For the exact finite experiment defined in `H20_EXT_LAB02_PROTOCOL.md`, exhaustive computation on (W=8,ldots,16) shows that the wheel-conditioned prime continuation quotient is not consistently smaller than the fixed-count random/shuffled quotient for (M=30) or (M=210).

This is an exact statement about the generated finite data and declared seeds, not an asymptotic theorem.

## 8. Interpretation

The most economical interpretation is that the strong LAB-01 compression signal was largely generated by elementary residue exclusions associated with small prime divisors.

This does **not** prove that all finite structural information in the primes is explained by wheel structure.

It does show that this particular candidate observer failed the first serious prime-specific falsification gate.

Therefore the correct scientific action is to stop developing this candidate as though it were a new invariant.

## 9. Literature context

The negative conclusion is also consistent with a much stronger known automata-complexity background.

Shallit's 1996 automaticity work gave a quantitative lower bound for finite automata recognizing the prime characteristic sequence on finite ranges.

A 2025 result, *The automaticity of the set of primes*, substantially strengthened this direction, proving that prime automaticity is close to maximal up to a subexponential factor.

Hence state growth / finite-state complexity of the prime sequence is already a serious established topic. H20-EXT must not claim novelty from the mere growth or non-regularity of continuation states.

Our wheel-conditioned experiment remains useful because it tests a different finite residual/OBDD-style observer and, importantly, falsifies the simplest compressibility interpretation before publication.

## 10. Non-claim

LAB-02 does not prove:

- that primes contain no other computational structure;
- that every continuation observer is explained by congruence information;
- an OBDD lower bound;
- an asymptotic equivalence to random Boolean functions;
- a new theorem in automaticity;
- any statement about the Riemann Hypothesis.

## 11. Publication decision

[
oxed{	ext{PUBLICATION THRESHOLD NOT REACHED}}
]

No H20 paper extension is justified from LAB-01/LAB-02.

The evidence-first branch has nevertheless succeeded scientifically:

1. a measurable signal was found;
2. a stronger baseline/falsification experiment was frozen before execution;
3. the signal failed that test;
4. the candidate is therefore retired rather than renamed or overinterpreted.

## 12. Branch decision

The **continuation-compressibility candidate is CLOSED**.

H20-EXT itself should remain exploratory only if a genuinely different observer is selected.

The next observer must not be another cosmetic version of residual-state count or BDD size. It must test a distinct structural question.
