# H20-EXT-LAB-08 · Conditional permutation tail significance result

Status: **PASS / STRONG FINITE CONDITIONAL-TAIL SEPARATION**

Successful run: GitHub Actions `35582246654`.

The preceding run `35582180457` failed at C++ compilation before scientific execution and contains no data.

## Frozen null model

The null ensemble preserves exact label counts jointly by

[
(nmod210,lfloor n/4096floor).
]

For every width exactly 2048 independent conditional permutations were generated from the frozen master seed

[
	exttt{0x48A7C20E5D1B9F31}.
]

## Frozen criterion

For every W=17,18,19:

[
widehat p_W=rac{K_W+1}{2049}le0.001,
]

and the sampled mean had to agree with the exact LAB-07 expectation within five standard errors.

## Result

| W | observed | exact expectation | MC mean | sample SD | K <= observed | corrected p-hat | z |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 0.0403356489260 | 0.0413314797766 | 0.0413260877049 | 0.000161734417 | 0 | 0.000488043 | -6.12386 |
| 18 | 0.0341052222066 | 0.0348420660751 | 0.0348414964274 | 0.0000863786301 | 0 | 0.000488043 | -8.52380 |
| 19 | 0.0295731101069 | 0.0299468618387 | 0.0299473730826 | 0.0000455946712 | 0 | 0.000488043 | -8.20848 |

Thus

[
oxed{
K_{17}=K_{18}=K_{19}=0.
}
]

All mean-consistency checks also pass.

## Interpretation

The exact prime low-4 Walsh energy is not merely below the conditioned ensemble mean.

Under the strongest declared local-density conditioned null model, the observed value lies far into the lower empirical permutation tail on all three widths.

The standardized sample separations are approximately 6.1, 8.5 and 8.2 standard deviations.

The corrected empirical tail probability is limited by the frozen sample count:

[
widehat p=rac1{2049}approx4.88	imes10^{-4}.
]

This is a finite randomization statement, not a Gaussian tail probability.

## Non-claim

The z values are descriptive standardized separations and are not converted into normal-theory p-values.

LAB-08 does not prove an asymptotic concentration theorem, novelty, or any RH statement.
