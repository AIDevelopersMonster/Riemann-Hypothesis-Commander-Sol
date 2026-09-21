# H20-EXT-LAB-10 · Extended-wheel falsification: include divisibility by 11

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Motivation

All strong C1 null models through LAB-09 condition on residue modulo

[
210=2cdot3cdot5cdot7.
]

A serious remaining explanation is therefore simple sieve structure from the
next prime divisor 11.

LAB-10 conditions on the extended wheel

[
oxed{
2310=2cdot3cdot5cdot7cdot11.
}
]

If C1 disappears, the correct interpretation is that the previous deficit was
largely a consequence of leaving divisibility by 11 unresolved.

## 2. Exact null partitions

For each declared local block size

[
Bin{65536,32768,16384},
]

partition inputs by

[
oxed{
(nmod2310,lfloor n/Bfloor).
}
]

Within each cell uniformly permute the exact finite prime/nonprime labels.

This preserves exactly:

- prime counts in every residue class modulo 2310;
- prime counts in every contiguous magnitude block of size B;
- their complete joint table.

## 3. Widths

[
W=17,18,19.
]

## 4. Observer

Unchanged:

[
L_W(4)
=
2^{-2W}
sum_{1le|S|le4}widehat f_W(S)^2.
]

The exact conditional expectation is computed analytically with the same
finite moment formula used in LAB-06 and LAB-07.

## 5. Frozen criterion

The extended-wheel C1 candidate survives only if

[
oxed{
L_W(4)_{m prime}
<
mathbb E[L_W(4)mid nmod2310,lfloor n/Bfloor]
}
]

for all nine combinations

[
Win{17,18,19},
qquad
Bin{65536,32768,16384}.
]

One nonnegative delta closes the claim that C1 survives explicit conditioning
on divisibility by 11.

No post-hoc block choice is allowed.

## 6. Interpretation

PASS would show that the finite low-degree deficit is not explained merely by
adding the next wheel prime 11 to the existing 2,3,5,7 sieve control.

FAIL would retain the earlier exact finite facts but materially weaken their
interpretation as a deeper prime-specific structure.

## 7. Required artifacts

- `lab10_extended_wheel.csv`;
- `H20_EXT_LAB10_REPORT.md`;
- self-test PASS record.

No RH claim and no publication claim are opened by this experiment alone.
