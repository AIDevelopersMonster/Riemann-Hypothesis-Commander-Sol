# H20-EXT-LAB-12 · Conditioning-resolution crossover hold-out

Status: **PROTOCOL FROZEN BEFORE FRESH WIDTHS**

## 1. Observation motivating the test

At W=19 under mod-30030 conditioning:

- one magnitude block gives positive discrepancy;
- two magnitude blocks give negative discrepancy;
- four magnitude blocks remain negative.

This is a sign reversal under refinement of the conditioning partition.

## 2. Fresh widths

The new hold-out widths are

[
oxed{W=20,21}.
]

They have not been inspected in H20-EXT.

## 3. Frozen conditioning hierarchy

For each W compute exact expectations under:

### one block

[
B=2^W;
]

### two equal blocks

[
B=2^{W-1};
]

### four equal blocks

[
B=2^{W-2}.
]

All models condition on residue modulo

[
30030.
]

## 4. Frozen crossover candidate

The W=19 pattern is promoted to a candidate only if on **both** fresh widths

[
oxed{
Delta_{W,1 block}ge0
}
]

while

[
oxed{
Delta_{W,2 blocks}<0,
qquad
Delta_{W,4 blocks}<0.
}
]

If either width fails this three-sign pattern, the crossover is classified as
a finite W=19 event rather than a validated cross-width law.

## 5. No rescue rule

If the pattern fails, no alternative block count or threshold will be selected
from W=20,21 in the same validation layer.

## 6. Scientific meaning

PASS would identify a reproducible **conditioning-resolution sign crossover**
for the exact low-degree Walsh discrepancy.

FAIL would strengthen the negative conclusion that no stable law has yet been
found beyond the finite C1 statements.

## 7. Required artifacts

- `lab12_crossover.csv`;
- `H20_EXT_LAB12_REPORT.md`;
- self-test PASS record.

No RH claim.
