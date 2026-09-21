# H20-EXT-LAB-03 · Exact Walsh degree-spectrum after wheel-preserving randomization

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Why a new observer is justified

LAB-01/LAB-02 closed the continuation-quotient candidate:

- raw prime data showed a compressibility gap;
- conditioning on wheels (30) and (210) removed that gap to baseline scale.

Therefore LAB-03 does **not** reuse residual-state count, BDD size, quotient-node count, or another cosmetic variant of the same object.

The new observer is the exact Walsh/Fourier degree-energy profile of the finite prime indicator on the Boolean cube.

## 2. Exact Boolean function

For width (W), define

[
P_W(x)=mathbf 1[x	ext{ prime}],
qquad xin{0,ldots,2^W-1}.
]

Use the sign encoding

[
f_W(x)=(-1)^{P_W(x)}in{+1,-1}.
]

The unnormalized Walsh transform is

[
widehat f_W(S)
=
sum_{xin{0,1}^W}
f_W(x)(-1)^{Scdot x}.
]

All coefficients are exact integers.

## 3. Primary invariant

For degree (k), define exact degree energy

[
E_{W,k}
=
sum_{|S|=k}widehat f_W(S)^2.
]

Parseval gives

[
sum_{k=0}^{W}E_{W,k}=2^{2W}.
]

Hence the normalized degree-energy vector

[
e_{W,k}=rac{E_{W,k}}{2^{2W}}
]

is an exact rational probability distribution over Walsh degree.

The primary object is the complete vector

[
oxed{
mathbf e_W=(e_{W,0},ldots,e_{W,W}).
}
]

This is invariant under permutation of input-bit labels, unlike the LAB-01 continuation quotient.

## 4. Secondary diagnostics

Record:

- degree-energy centroid
  [
  mu_W=sum_k k e_{W,k};
  ]
- variance of the degree-energy distribution;
- maximum nonconstant degree-energy coordinate;
- degree at which that maximum occurs;
- cumulative low-degree mass
  [
  L_W(d)=sum_{k=1}^{d}e_{W,k}
  ]
  for (d=1,2,3,4);
- spectral entropy of the degree-energy distribution.

The DC term (e_{W,0}) is reported but excluded from prime-structure interpretation because it is determined by density.

## 5. Baselines

All baselines use exactly (2^W) Boolean values.

### B1 · global fixed-count random

Randomize the positions of ones while preserving exactly (pi(2^W-1)) ones.

### B2 · global shuffled-prime

Shuffle the prime indicator globally, preserving the same number of ones.

### B3 · wheel-30 preserving shuffle

Partition indices by residue modulo 30.

Within each residue class independently, shuffle the prime labels.

This preserves exactly:

- sequence length;
- total prime count;
- prime count in every residue class mod 30.

### B4 · wheel-210 preserving shuffle

Partition indices by residue modulo 210 and independently shuffle prime labels inside every residue class.

This preserves the full finite residue-count profile modulo

[
210=2cdot3cdot5cdot7.
]

Fixed seeds:

[
1729,quad271828,quad314159,quad1618033,quad5772157.
]

The wheel-preserving baselines are the primary falsification controls.

## 6. Width split

Frozen before execution:

### Discovery

[
W=6,ldots,11.
]

### Validation

[
W=12,13,14.
]

### Extrapolation gate

[
W=15,16.
]

No spectral law may be altered after seeing validation widths and retain the label "validated".

## 7. Distance statistic

For each baseline sample (b), compare the nonconstant normalized degree vectors using total variation distance

[
D_{m TV}
=
rac12
sum_{k=1}^{W}
|e_{W,k}^{m prime}-e_{W,k}^{b}|.
]

Also record the same distance after renormalizing nonconstant mass to one, so density/DC effects cannot dominate:

[
widetilde e_{W,k}
=
rac{e_{W,k}}{sum_{j=1}^{W}e_{W,j}},
]

[
widetilde D_{m TV}
=
rac12
sum_{k=1}^{W}
|widetilde e_{W,k}^{m prime}
-widetilde e_{W,k}^{b}|.
]

The second quantity is the primary structural distance.

## 8. Falsification criterion

A prime-specific spectral candidate survives only if, against the **wheel-210 preserving baseline**:

1. a predeclared low-degree or full-profile statistic remains outside the five-seed baseline spread on all validation widths;
2. the direction of the effect is consistent on (W=12,13,14);
3. the extrapolation widths (W=15,16) do not reverse it;
4. the effect is not solely the DC/density term;
5. the same conclusion is supported by exact degree energies, not only a plotted curve.

If the prime spectrum lies at baseline scale after wheel-preserving randomization, the spectral candidate is closed.

## 9. No post-hoc fitting

LAB-03 does not fit a recurrence, power law, symbolic regression formula, or asymptotic exponent.

Its only task is to determine whether a nontrivial spectral signal remains after stronger controls.

## 10. Required artifacts

- `walsh_degree_spectrum.csv`;
- `walsh_degree_summary.json`;
- `H20_EXT_LAB03_REPORT.md`.

The computation must use an exact integer fast Walsh-Hadamard transform.

No FPGA synthesis is involved.

## 11. Claim boundary

Even a positive LAB-03 result would not establish novelty.

A surviving spectral feature would next require targeted comparison with:

- Fourier analysis of Boolean functions;
- arithmetic Boolean functions;
- spectral analyses of prime indicators;
- pseudorandomness/uniformity results for primes in residue classes.

No RH claim is permitted.
