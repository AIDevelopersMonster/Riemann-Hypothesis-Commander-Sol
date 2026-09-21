# H20-EXT-LAB-11 · Final practical wheel gate result

Status: **FAIL / ROBUST-WHEEL C1 VERSION CLOSED**

Run: GitHub Actions `35582796620`.

## Frozen criterion

Every declared mod-30030 discrepancy had to remain strictly negative.

## Exact result

| W | modulus | block size | delta |
|---:|---:|---:|---:|
| 17 | 30030 | 131072 | -0.0000331005920 |
| 18 | 30030 | 262144 | -0.0000598629644 |
| 19 | 30030 | 524288 | **+0.000129799949** |
| 19 | 30030 | 262144 | -0.0000560438122 |
| 19 | 30030 | 131072 | -0.000138099987 |

Therefore

[
oxed{	ext{CRITERION PASS = FALSE}.}
]

The failure is scientific, not technical.

## Consequence

The statement

> prime low-degree Walsh energy remains below exact conditioned expectation
> under every reasonable wheel refinement through mod 30030

is false on the tested range.

The robust-wheel interpretation of C1 is therefore closed.

## Conditioning-resolution crossover at W=19

A narrower exact phenomenon appears:

[
mathbb E_{m mod30030, 1 block}[L_{19}(4)]
<
L_{19}^{m prime}(4)
<
mathbb E_{m mod30030, 2 blocks}[L_{19}(4)].
]

Numerically,

[
0.0294433101580
<
0.0295731101069
<
0.0296291539191.
]

Thus adding a single magnitude split changes the discrepancy sign.

With four blocks the deficit becomes larger in magnitude:

[
Delta=-0.000138099987.
]

## Interpretation

C1 is not a null-model-independent invariant.

Its sign depends on the resolution of the conditioning partition once the wheel
is strengthened to include 13.

This is exactly the kind of observer/null-model dependence that the H19/H20
framework requires us to expose rather than hide.

## Non-claim

The W=19 crossover alone is not promoted to a cross-width law.

A fresh hold-out is required before any recurrence or phase-boundary language
is used.
