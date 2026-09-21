# H20-EXT-LAB-05 · Fresh hold-out for the residual low-degree Walsh deficit

Status: **PROTOCOL FROZEN BEFORE NEW WIDTHS ARE COMPUTED**

## 1. Candidate frozen after LAB-04

LAB-04 left exactly one narrower candidate worth testing:

[
oxed{
L_W(4)_{m prime}
<
L_W(4)_{m wheel210+dyadic shuffle}
}
]

where

[
L_W(4)=sum_{k=1}^{4}e_{W,k}.
]

The comparison uses the same exact sign encoding, FWHT, five seeds, and joint stratification by

[
(nmod210,lfloorlog_2 nfloor).
]

No other statistic is promoted in LAB-05.

## 2. Fresh ranges

The widths below have not been inspected in LAB-01--04.

### Validation

[
W=17,18.
]

### Extrapolation

[
W=19.
]

## 3. Frozen criterion

The candidate survives LAB-05 only if:

1. for W=17 and W=18, the prime low-4 mass is below **every** one of the five fixed-seed stratified baseline samples;
2. the mean delta remains negative;
3. W=19 does not reverse the sign.

If any validation width fails condition 1, the candidate is closed.

No threshold magnitude is fitted.

## 4. Computational constraint

Exact integer FWHT only.

The maximum truth table is

[
2^{19}=524288
]

entries, which is acceptable for this single focused CPU experiment.

No synthesis or graph mining is permitted.

## 5. Literature boundary

Even successful validation would remain adjacent to known work on Fourier-Walsh coefficients of von Mangoldt/primes and prescribed binary digits.

Success would justify only a targeted novelty audit and an attempt at an exact finite formulation explaining the degree-1--4 deficit.

No RH claim.
