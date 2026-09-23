# H20-EXT-LAB-07 · Exact Walsh expectation under fine local-density preservation

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

LAB-06 established

[
L_W(4)_{m prime}
<
mathbb E[L_W(4)_{m mod210+dyadic}]
]

for every W=13..19.

The remaining obvious confound is density variation *inside* one dyadic shell.

LAB-07 replaces dyadic shells by substantially finer contiguous magnitude blocks.

## 2. Exact conditioning ensembles

For each selected block size

[
Bin{2^{14},2^{13},2^{12}}
=
{16384,8192,4096},
]

partition indices by the joint key

[
oxed{
(nmod210, lfloor n/Bfloor).
}
]

Within every joint cell uniformly permute the observed prime/nonprime sign labels.

Therefore each ensemble preserves exactly:

- total prime count;
- prime count in every residue class modulo 210;
- prime count in every contiguous block of length B;
- more strongly, prime count in every joint mod-210 x local-block cell.

No random seeds enter the primary expectation.

## 3. Observer

Use the same exact cumulative low-degree Walsh energy

[
L_W(4)
=
2^{-2W}
sum_{1le |S|le4}widehat f_W(S)^2.
]

The exact conditional expectation is evaluated using the LAB-06 finite moment formula.

## 4. Widths

Primary falsification widths:

[
W=17,18,19.
]

These are the fresh LAB-05 validation/extrapolation region and are large enough that every declared block size yields multiple magnitude blocks.

## 5. Frozen criterion

C1 survives LAB-07 only if

[
L_W(4)_{m prime}
<
mathbb E[L_W(4)mid B]
]

for **every**

[
Win{17,18,19}
]

and **every**

[
Bin{16384,8192,4096}.
]

Equivalently, every exact discrepancy

[
Delta_{W,B}
=
L_W(4)_{m prime}
-
mathbb E[L_W(4)mid B]
]

must remain strictly negative.

One nonnegative value closes C1 as a robust local-density-independent candidate.

No trend fitting or post-hoc block selection is allowed.

## 6. Interpretation

If the deficit disappears at finer blocks, the correct explanation is that LAB-06 was driven by residual magnitude-density variation.

If it survives all three resolutions, then the exact finite deficit is not explained by:

- density alone;
- residue counts modulo 210;
- dyadic shell counts;
- or prime-count variation on contiguous scales down to 4096.

That would materially strengthen C1.

## 7. Required artifacts

- `exact_localblock_expectation.csv`;
- `H20_EXT_LAB07_REPORT.md`;
- self-test PASS record.

No RH claim. No FPGA work. No symbolic fitting.
