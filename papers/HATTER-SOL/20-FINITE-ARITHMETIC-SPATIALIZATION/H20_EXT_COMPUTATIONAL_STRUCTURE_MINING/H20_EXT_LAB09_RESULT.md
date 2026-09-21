# H20-EXT-LAB-09 · Arithmetic-control specificity result

Status: **PASS / PRIME-SPECIFICITY SUPPORTED AGAINST DECLARED CONTROLS**

Run: GitHub Actions `35582460589`.

## Frozen criterion

For each W=17,18,19 define

[
R_{W,F}
=
rac{mathbb E[L_{W,F}(4)]-L_{W,F}(4)}
{mathbb E[L_{W,F}(4)]}.
]

Prime specificity was supported only if

[
R_{W,m prime}
>
R_{W,m squarefree},
qquad
R_{W,m prime}
>
R_{W,m semiprime}
]

at every width.

Each family is compared with its own exact null model preserving membership
counts jointly by

[
(nmod210,lfloor n/4096floor).
]

## Exact result

| W | family | observed | exact expectation | delta | normalized deficit R |
|---:|---|---:|---:|---:|---:|
| 17 | prime | 0.0403356489260 | 0.0413314797766 | -0.000995830851 | +0.0240938 |
| 17 | squarefree | 0.495484732091 | 0.182079219793 | +0.313405512298 | -1.72126 |
| 17 | semiprime | 0.101410760777 | 0.0832901424405 | +0.018120618337 | -0.217560 |
| 18 | prime | 0.0341052222066 | 0.0348420660751 | -0.000736843869 | +0.0211481 |
| 18 | squarefree | 0.494222164154 | 0.175450312602 | +0.318771851552 | -1.81688 |
| 18 | semiprime | 0.0929975605104 | 0.0765921816069 | +0.016405378903 | -0.214191 |
| 19 | prime | 0.0295731101069 | 0.0299468618387 | -0.000373751732 | +0.0124805 |
| 19 | squarefree | 0.493515702008 | 0.171268711175 | +0.322246990833 | -1.88153 |
| 19 | semiprime | 0.0863326930412 | 0.0715959439968 | +0.014736749044 | -0.205832 |

Thus the declared specificity criterion passes at all three widths.

## Interpretation

Under the same exact local arithmetic/density conditioning:

- PRIME shows a positive normalized **deficit**;
- SQUAREFREE shows a very large low-degree **excess**;
- SEMIPRIME also shows a low-degree **excess**.

Therefore C1 is not reproduced merely by choosing another familiar arithmetic
set with strong multiplicative structure.

This supports, but does not prove, a prime-specific interpretation.

## Non-claim

The control set is not exhaustive.

Other sifted sets, pseudoprimes, almost-primes of different orders, or custom
residue-constrained models could behave differently.

No asymptotic or novelty claim follows.
