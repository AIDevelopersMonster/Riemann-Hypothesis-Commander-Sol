# H20-EXT-LAB-08 · Conditional permutation tail significance

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

LAB-06 and LAB-07 established that the observed prime low-degree Walsh energy

[
L_W(4)
=
2^{-2W}
sum_{1le |S|le4}widehat f_W(S)^2
]

lies below the **exact conditional expectation** under increasingly strong
prime-count preserving null ensembles.

LAB-08 asks a different question:

[
oxed{
	ext{How deep in the lower tail of the strongest conditioned ensemble is the observed prime value?}
}
]

No new statistic is introduced.

## 2. Frozen null ensemble

Use the strongest LAB-07 conditioning resolution:

[
oxed{
(nmod210, lfloor n/4096floor).
}
]

Inside every joint cell, uniformly choose the positions of the fixed number of
prime labels.

Thus each permutation sample preserves exactly:

- total prime count;
- prime count in every residue class modulo 210;
- prime count in every contiguous block of length 4096;
- the full joint table of both constraints.

## 3. Widths

[
W=17,18,19.
]

## 4. Sample size

For each width generate exactly

[
oxed{2048}
]

independent conditional permutation samples.

The pseudorandom generator and master seed are fixed in the implementation and
recorded in the report.

No additional samples may be added after seeing the result while retaining this
LAB-08 significance label.

## 5. Primary tail statistic

Let (L_W^{m obs}) be the exact prime value.

For the 2048 null samples define

[
K_W
=
#{j:L_{W,j}^{m null}le L_W^{m obs}}.
]

Use the finite-sample corrected lower-tail empirical probability

[
oxed{
widehat p_W
=
rac{K_W+1}{2049}.
}
]

Also report sample mean, sample standard deviation and

[
z_W
=
rac{L_W^{m obs}-overline L_W^{m null}}{s_W}.
]

The exact expectation from LAB-07 remains the reference mean; the Monte Carlo
mean is only a consistency check.

## 6. Frozen criterion

The significance gate passes only if, for **every** W=17,18,19,

[
oxed{
widehat p_Wle 0.001
}
]

which with 2048 samples requires

[
K_Wle1.
]

Additionally the Monte Carlo mean must agree with the LAB-07 exact expectation
within five sample standard errors.

Failure at one width closes the claim that C1 has strong conditional-tail
separation on the declared range.

## 7. Non-claim

A pass would establish only a strong **finite conditional randomization
significance** for the declared null model.

It would not prove:

- an asymptotic probability bound;
- independence of the result from the chosen null ensemble;
- novelty;
- a prime-number theorem;
- a circuit lower bound;
- any RH implication.

## 8. Required artifacts

- `lab08_tail_summary.csv`;
- `H20_EXT_LAB08_REPORT.md`;
- reproducible RNG seed;
- workflow PASS/FAIL record.
