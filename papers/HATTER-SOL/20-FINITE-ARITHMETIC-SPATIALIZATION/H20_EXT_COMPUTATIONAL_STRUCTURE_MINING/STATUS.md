# H20-EXT · Computational Structure Mining · STATUS

Branch: `research/hatter-sol-20-computational-structure-mining`

Parent H20 physical layer: **CLOSED**

Publication status: **NOT YET**

## Completed experiments

### LAB-01 · continuation quotient census

Raw prime continuation quotients appeared substantially smaller than density-matched random/shuffled baselines.

Result: **candidate opened, not promoted**.

### LAB-02 · wheel-conditioned continuation quotient

Conditioning by wheels 30 and 210 removed the LAB-01 compression advantage to baseline scale.

Result:

[
oxed{	ext{continuation-compressibility candidate CLOSED by falsification}.}
]

### LAB-03 · exact Walsh degree spectrum

Against mod-210 preserving shuffles, a low-degree spectral signature survived the first validation range.

Result: **candidate required stronger density control**.

### LAB-04 · wheel-210 + dyadic-density preserving Walsh baseline

The degree-1--2 excess reversed and was falsified.

A narrower cumulative degree-1--4 deficit remained.

Because this narrower hypothesis was isolated after seeing LAB-04 data, it was not allowed to inherit the existing validation.

### LAB-05 · fresh hold-out

The isolated low-4 deficit was frozen before computing new widths.

Fresh validation:

[
W=17,18.
]

Extrapolation:

[
W=19.
]

All five fixed-seed stratified baselines had larger cumulative degree-1--4 Walsh mass than the prime indicator at both validation widths and at W=19.

Result:

[
oxed{	ext{C1 empirical candidate OPEN}.}
]

## C1

[
oxed{
L_W(4)_{m prime}
<
L_W(4)_{m wheel210+dyadic stratified shuffle}
}
]

on the current frozen finite samples, with independent validation at W=17,18.

## Literature caution

Fourier-Walsh analysis of primes/von Mangoldt under binary expansion is established literature, especially Bourgain's work on prescribed binary digits and Boolean functions.

C1 is therefore **not** called new.

Current classification:

- exact finite computation: yes;
- discovery/validation discipline: yes;
- strong baseline: yes;
- fresh hold-out: yes;
- exact stochastic-baseline expectation: not yet;
- theorem: no;
- novelty audit: incomplete;
- representation-transport result beyond semantic invariance: no;
- publication threshold: not reached;
- RH claims: none.

## Next scientific target

Derive and compute the exact expected cumulative degree-1--4 Walsh energy under uniform random permutation of prime labels independently inside each

[
(nmod210,lfloorlog_2 nfloor)
]

stratum.

This replaces five sampled baselines with an exact combinatorial expectation.

If C1 disappears against that exact expectation, close it.

If it persists, formulate the exact finite discrepancy and begin a targeted theorem/prior-art audit.
