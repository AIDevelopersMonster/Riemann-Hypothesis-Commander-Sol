# H20-EXT-LAB-07 · Exact local-density Walsh result

Status: **C1 SURVIVES FINE LOCAL-DENSITY FALSIFICATION**

Run: GitHub Actions `35580640541`.

Two earlier runs failed before execution because of a C++ include error. They are technical failures only and contain no scientific data. The successful run is the one cited above.

## Frozen criterion

Before execution, LAB-07 required

[
L_W(4)_{m prime}
<
mathbb E[L_W(4)mid B]
]

for every

[
Win{17,18,19}
]

and every local block size

[
Bin{16384,8192,4096}.
]

The conditioning ensemble preserves exact prime counts jointly by

[
(nmod210,lfloor n/Bfloor).
]

One nonnegative delta would have closed C1.

## Exact result

| W | block size | observed | exact expectation | delta |
|---:|---:|---:|---:|---:|
| 17 | 16384 | 0.0403356489260 | 0.0412408706386 | -0.000905221712598 |
| 17 | 8192 | 0.0403356489260 | 0.0413220169187 | -0.000986367992717 |
| 17 | 4096 | 0.0403356489260 | 0.0413314797766 | -0.000995830850641 |
| 18 | 16384 | 0.0341052222066 | 0.0348144274523 | -0.000709205245753 |
| 18 | 8192 | 0.0341052222066 | 0.0348476895431 | -0.000742467336514 |
| 18 | 4096 | 0.0341052222066 | 0.0348420660751 | -0.000736843868577 |
| 19 | 16384 | 0.0295731101069 | 0.0299447209476 | -0.000371610840725 |
| 19 | 8192 | 0.0295731101069 | 0.0299549275597 | -0.000381817452832 |
| 19 | 4096 | 0.0295731101069 | 0.0299468618387 | -0.000373751731784 |

Hence

[
oxed{
Delta_{W,B}<0
}
]

for all nine predeclared tests.

## Exact finite statement

For W=17,18,19 and local block sizes 16384,8192,4096, the exact prime indicator on ({0,ldots,2^W-1}) has lower cumulative Walsh energy in degrees 1 through 4 than the exact conditional expectation under uniform independent permutations preserving the complete table of prime counts by joint mod-210 residue and local magnitude block.

No random seeds are involved.

## Interpretation

The observed deficit is not explained by:

- global prime density;
- oddness;
- residue exclusions modulo 2,3,5,7;
- exact counts modulo 210;
- coarse dyadic magnitude variation;
- or exact local prime-count variation on contiguous scales down to 4096.

This materially strengthens C1.

## Non-claim

The result does not establish:

- an asymptotic inequality;
- exact tail probability under the permutation ensemble;
- novelty;
- a circuit-complexity theorem;
- any RH implication.
