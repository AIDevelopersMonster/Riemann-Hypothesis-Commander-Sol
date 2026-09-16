# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** active implementation research.  
**Date:** 16 September 2026.

## Closed: H17-01 canonical golden model

The deterministic `PSL(2,7)` golden model is fixed: 168 group elements, 114 simultaneous-conjugacy orbits of generating pairs, and 114 unique five-probe signatures. Canonical orbit IDs `0..113` are stable under Python hash/set iteration.

Source: `tools/generate_psl27_golden_model.py`.

## Closed mathematically: H17-02 admissibility law

For all `168^2 = 28,224` ordered pairs `(A,B)`:

```text
generating ordered pairs        = 19,152
non-generating ordered pairs    =  9,072
generating signature image      =    114
non-generating signature image  =     66
intersection                    =      0
```

Therefore, for valid `PSL(2,7)` ports, the H16 five-probe 114-entry ROM is simultaneously an exact generation-domain recognizer and an orbit decoder:

`signature_hit <=> <A,B> = PSL(2,7)`.

Certificate: `certificates/psl27_signature_admissibility_certificate.py`.

## Closed: H17-03 minimum depth for one-erasure orbit recovery

The complete cyclic trace family through primitive depth four contains 25 coordinates but still has

```text
d_min = 1
```

on the 114 generating orbits. Exactly seven orbit pairs are at distance one, and in every case the only separating depth-`<=4` coordinate is

`ABab = [A,B]`.

Therefore one-erasure exact orbit recovery is impossible at depth `<=4` even if every one of the 25 available coordinates is measured.

At exact depth five, the single word

`AABAb`

separates all seven defect pairs. Hence the 25-word depth-`<=4` family plus `AABAb` has distance two. Thus

```text
minimum possible maximum primitive depth for one-erasure orbit recovery = 5
```

within the present cyclic-trace observer class.

Moreover the complete 51-word family through depth five has

```text
d_min = 5.
```

Certificate: `certificates/psl27_depth5_erasure_certificate.py`.

Detailed note: `docs/H17_03_DEPTH5_ONE_ERASURE.md`.

## Backward-compatible erasure architecture

If the original H16 five probes

```text
A, B, AB, Ab, ABab
```

must remain present, exhaustive search proves that one, two, or three exact-depth-five additions never reach distance two. Four additions suffice. One exact extension is

```text
AAABB
AAAbb
AABab
ABBaB
```

Therefore the minimum backward-compatible depth-five one-erasure interface has nine probes.

## Globally redesigned depth-five orbit code

A binary MILP over all 51 cyclic words of depth `<=5`, with one distance-`>=2` constraint for every unordered pair of the 114 generating orbits, returns an optimum of eight probes with zero MIP gap and dual bound eight; the same model constrained to at most seven probes is infeasible.

Among eight-probe solutions, the minimum number of exact-depth-five probes is four. A minimum-total-word-length solution is

```text
AAB
ABB
AAAb
Abbb
AABAb
AAbAb
ABaBB
AbAbb
```

with total primitive word length 34.

This cardinality-eight optimum is recorded as **solver-certified** rather than promoted beyond what the optimization certificate itself supports.

## New separation: orbit recovery is not admissibility

The globally optimized eight-probe orbit code has distance two on the 114 generating orbits, but its generating signature image intersects the non-generating image in two signatures.

Therefore the following are distinct hardware objectives:

1. generating-orbit recovery distance;
2. generating/non-generating admissibility separation.

The original five-probe H16 code has the second property exceptionally cleanly; a redesigned erasure code must not silently discard it.

The next mathematical optimization target is therefore a joint code satisfying at least

```text
d_gen/gen >= 2
S_gen intersection S_non = empty
```

and preferably

```text
d_gen/non >= 2
```

so that both exact orbit recovery and generation admissibility survive any one probe erasure.

A first full joint MILP attempt exceeded the current execution window and is explicitly not treated as a result.

## End-to-end RTL generator

`tools/generate_psl27_end_to_end.py`

Data path:

```text
A,B
 -> exact word engine
 -> oriented six-class channel
 -> 15-bit five-probe signature
 -> 114-entry ROM
 -> orbit_valid / canonical orbit_id
```

The generated testbench covers the 114 generating and 66 non-generating five-probe signature states. External HDL simulation/synthesis remains an open gate because this execution environment has no `iverilog`, `verilator`, or `yosys`.

## Arithmetic two-port frontend seed

The integer-side idea has been restored from H07/H11 without conflating it with the `PSL(2,7)` theorem.

For composite `n`, define the two-factor family

```text
D2(n) = {(a,b): a >= b >= 2, ab = n}.
```

The historical H11 maximal-first protocol inspects the lexicographically largest pair first. Equivalently,

```text
MF2(n) = (n / p_min(n), p_min(n)),
```

where `p_min(n)` is the smallest prime divisor.

Examples:

```text
52: D2 = {(26,2),(13,4)} -> maximal-first (26,2)
 9: D2 = {(3,3)}        -> maximal-first (3,3)
 6: D2 = {(3,2)}        -> maximal-first (3,2)
```

The full family remains mathematically present; maximal-first is an experimental selection rule, not a canonical orbit law.

Seed: `docs/INTEGER_TWO_PORT_MAXIMAL_FIRST_FRONTEND_SEED.md`.

## Next strike

1. solve the joint depth-`<=5` optimization with both orbit-erasure and generation-admissibility constraints;
2. determine the exact minimum probe count for one-erasure-safe admissible tomography;
3. generate the corresponding redundant RTL interface;
4. only then compare hardware resource/latency cost against the five-probe minimal core and the nine-probe backward-compatible code.
