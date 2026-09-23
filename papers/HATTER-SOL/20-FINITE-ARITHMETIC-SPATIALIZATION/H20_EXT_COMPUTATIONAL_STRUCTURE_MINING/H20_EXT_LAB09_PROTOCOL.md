# H20-EXT-LAB-09 · Arithmetic-control specificity gate

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

C1 is now an exact finite and strongly tail-separated statement for the prime indicator.

LAB-09 asks whether the same low-degree deficit is generic to other familiar arithmetic sets.

The comparison uses each arithmetic family against its **own** exact locally conditioned null ensemble.

## 2. Arithmetic families

Evaluate:

- PRIME;
- SQUAREFREE;
- SEMIPRIME, where semiprime means exactly two prime factors counted with multiplicity.

ODD is not used as a primary control because mod-210 conditioning already determines parity residue information exactly.

## 3. Common observer

For each family F define sign labels

[
f_{W,F}(x)=(-1)^{mathbf 1[xin F]}.
]

Compute

[
L_{W,F}(4)
=
2^{-2W}
sum_{1le|S|le4}widehat f_{W,F}(S)^2.
]

## 4. Common exact null model

For each family independently preserve exact membership counts in every joint cell

[
oxed{
(nmod210,lfloor n/4096floor).
}
]

Use the exact LAB-06/LAB-07 conditional expectation formula.

No random seeds enter LAB-09.

## 5. Widths

[
W=17,18,19.
]

## 6. Primary normalized deficit

Define

[
R_{W,F}
=
rac{
mathbb E[L_{W,F}(4)]-L_{W,F}(4)
}{
mathbb E[L_{W,F}(4)]
}.
]

Positive R means a low-degree deficit relative to the exact conditioned null mean.

## 7. Frozen specificity criterion

C1 receives **prime-specificity support** only if, at every W=17,18,19,

[
oxed{
R_{W,m prime}
>
R_{W,m squarefree}
}
]

and

[
oxed{
R_{W,m prime}
>
R_{W,m semiprime}.
}
]

Failure does **not** invalidate the exact prime C1 inequality.

It invalidates the stronger interpretation that the observed effect is unusually prime-specific relative to these arithmetic controls.

## 8. Required artifacts

- `lab09_arithmetic_controls.csv`;
- `H20_EXT_LAB09_REPORT.md`;
- exact self-test PASS record.

No post-hoc control family selection is allowed inside LAB-09.
