# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** active processor implementation research.  
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

The complete cyclic trace family through primitive depth four contains 25 coordinates but still has `d_min=1` on the 114 generating orbits. Exactly seven orbit pairs are at distance one, and in every case the only separating depth-`<=4` coordinate is

`ABab = [A,B]`.

Therefore one-erasure exact orbit recovery is impossible at depth `<=4` even if all 25 coordinates are measured.

The exact-depth-five word `AABAb` separates all seven defect pairs, so

```text
minimum possible maximum primitive depth for one-erasure orbit recovery = 5
```

within the present cyclic-trace observer class. The complete 51-word family through depth five has `d_min=5`.

Certificate: `certificates/psl27_depth5_erasure_certificate.py`.

Detailed note: `docs/H17_03_DEPTH5_ONE_ERASURE.md`.

## Closed: H17-04 optimal joint one-erasure tomography

The correct robust objective is simultaneous

```text
d_gen/gen >= 2
d_gen/non >= 2
```

so that deletion of any one known coordinate preserves both canonical generating-orbit recovery and generating/non-generating admissibility.

The candidate family consists of all 51 cyclic trace coordinates of primitive depth `<=5`. The exact finite model has 114 generating orbits, 83 non-generating simultaneous-conjugacy orbits, and 66 distinct non-generating full signatures. These produce 13,965 binary covering constraints.

A zero-gap binary MILP gives the exact optimum

```text
minimum joint one-erasure probe count = 8
```

One optimal family is

```text
AAB
Abb
AAAB
Abbb
AABAb
AAbAb
ABABB
ABaBB
```

and direct finite verification gives

```text
d_gen/gen = 2
d_gen/non = 2
```

Among all eight-probe joint optima, at least four probes must have exact depth five. With exactly four depth-five probes, the minimum total primitive word length is 34. Thus an optimal depth profile is

```text
(3,3,4,4,5,5,5,5)
```

and the displayed family realizes it.

Certificate: `certificates/psl27_joint_one_erasure_code_certificate.py`.

Detailed note: `docs/H17_04_OPTIMAL_JOINT_ONE_ERASURE_CODE.md`.

## Closed: H16-backward-compatible robust minimum

If the original H16 five channels

```text
A, B, AB, Ab, ABab
```

must remain exposed, eight total probes are impossible. Exhaustive enumeration of all `C(46,3)=15,180` three-coordinate extensions proves this independently of MILP optimization.

A nine-channel joint one-erasure interface exists:

```text
A
B
AA
AB
Ab
ABB
Abb
ABab
ABaBB
```

with

```text
d_gen/gen = 2
d_gen/non = 2
```

Only one of the four added probes has depth five. Therefore

```text
minimum H16-frozen robust channel count = 9
```

This replaces the earlier provisional four-depth-five extension as the preferred backward-compatible architecture.

## Closed: H17-05 LUT-free structural group/class processor

The H16 HDL proof-of-concept accepted already classified probes. H17 now derives the class channels from raw 24-bit permutations without a 168-entry element/class LUT.

For an arbitrary 8-point permutation, five cross-ratio equalities test whether it is induced by a `PGL(2,7)` transformation. A quadratic-character orientation test on the image of `(0,1,infinity)` selects the `PSL(2,7)` subgroup.

Exhaustive enumeration gives exactly

```text
all S8 permutations checked = 40320
PGL(2,7) accepted           =   336
PSL(2,7) accepted           =   168
```

and the accepted 168 elements coincide exactly with the independent determinant-one matrix construction.

For a valid element, permutation order computes the classes

```text
order 1 -> 1A
order 2 -> 2A
order 3 -> 3A
order 4 -> 4A.
```

For order seven, the quadratic orientation of three successive points on the unique 7-cycle separates the two remaining classes exactly:

```text
7A -> +1 (24 elements)
7B -> -1 (24 elements).
```

Therefore both group membership and all six conjugacy classes are computed structurally from the raw permutation. No element lookup table is required before the final orbit decoder.

Certificate: `certificates/psl27_structural_class_engine_certificate.py`.

Detailed note: `docs/H17_05_LUT_FREE_STRUCTURAL_PROCESSOR.md`.

RTL generator: `tools/generate_psl27_structural_processor.py`.

The robust8 generator instantiates `psl27_structural_classify` for `A`, `B`, and all eight observer words.

## Closed mathematically: H17-06 ROM-free erasure repair

The 24-bit robust8 signature itself is a canonical fingerprint of the 114 generating simultaneous-conjugacy orbits relative to the fixed ordered observer family. The integer `orbit_id=0..113` is therefore optional external naming metadata rather than a necessary mathematical output.

For each known erased coordinate, exact dynamic programming optimizes a decision tree over the seven surviving class coordinates. Leaves output either the missing generating class or `NON`.

For every erasure position the exact minimum worst-case decision depth is

```text
4 class queries.
```

Among depth-optimal trees, internal-node counts are

```text
AAB    41
Abb    41
AAAB   43
Abbb   43
AABAb  30
AAbAb  39
ABABB  39
ABaBB  30
```

for 306 internal nodes before synthesis/factoring across erasure modes.

Thus H17 has a ROM-free mathematical core:

```text
raw A,B
 -> structural PSL membership
 -> permutation word arithmetic
 -> structural class computation
 -> robust8 signature
 -> depth-4 erasure repair/admissibility tree
 -> 24-bit canonical orbit fingerprint
```

No element ROM and no 114-orbit ROM are required in this core.

Certificate: `certificates/psl27_erasure_repair_tree_certificate.py`.

Generator: `tools/generate_psl27_romfree_repair.py`.

Detailed note: `docs/H17_06_ROM_FREE_ERASURE_REPAIR.md`.

The generated adversarial repair test overwrites the erased three-bit coordinate with `3'b111`, so the repair logic cannot recover by reading the supposedly missing value.

## Independent HDL simulation status

GitHub Actions workflow `HATTER-SOL-17 HDL` has crossed the first external simulation gate with Icarus Verilog 12.0.

The following jobs have passed independently on GitHub-hosted Ubuntu runners:

```text
structural-classifier : PASS
robust8               : PASS
```

The structural-classifier simulation checks all 168 valid `PSL(2,7)` elements plus invalid witnesses.

The robust8 simulation checks

```text
114 * 8 = 912 generating one-erasure states
 66 * 8 = 528 non-generating one-erasure states
```

and reports

```text
PASS: robust8 checked 114*8 generating and 66*8 non-generating erasure states
```

The new `romfree-repair` CI job is now part of the workflow and is the next HDL gate. Until that job completes successfully, H17-06 is recorded as mathematically closed and RTL-generated, but not yet externally simulated.

No synthesis timing/resource/board claim is made yet.

## Exact observer tiers now fixed

H17 now has four hardware targets:

1. **5-channel baseline** — minimal exact orbit/admissibility decoder, no erasure tolerance;
2. **8-channel robust flat-ID decoder** — globally minimal one-erasure observer with historical `orbit_id` ROM;
3. **8-channel robust ROM-free fingerprint processor** — preferred mathematical processor core;
4. **9-channel H16-compatible robust core** — preferred migration target if the original H16 channels must remain exposed.

## Arithmetic two-port frontend seed

For composite `n`, define

```text
D2(n) = {(a,b): a >= b >= 2, ab = n}.
```

The restored H07/H11 maximal-first protocol inspects the pair with largest first factor first, equivalently

```text
MF2(n) = (n / p_min(n), p_min(n)).
```

Examples:

```text
52: D2 = {(26,2),(13,4)} -> maximal-first (26,2)
 9: D2 = {(3,3)}        -> maximal-first (3,3)
 6: D2 = {(3,2)}        -> maximal-first (3,2)
```

The full factor family remains present; maximal-first is an experimental selection protocol, not a canonical orbit theorem.

Seed: `docs/INTEGER_TWO_PORT_MAXIMAL_FIRST_FRONTEND_SEED.md`.

## Next strike

1. cross the independent HDL simulation gate for `romfree-repair`;
2. synthesize the structural classifier, flat robust8 decoder, and ROM-free repair design with Yosys;
3. compare logic cells, mux/decode structure, critical combinational depth proxies, and inferred memories;
4. generate the nine-channel H16-compatible structural variant;
5. only after synthesis choose the preferred FPGA architecture and pipeline/register placement;
6. then move to vendor FPGA timing closure and physical-board verification.
