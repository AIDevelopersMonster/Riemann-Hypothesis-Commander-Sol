# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** active implementation research.  
**Date:** 16 September 2026.

## Closed: H17-01 canonical golden model

The deterministic `PSL(2,7)` golden model is fixed: 168 group elements, 114 simultaneous-conjugacy orbits of generating pairs, and 114 unique five-probe signatures. Canonical orbit IDs `0..113` are stable under Python hash/set iteration.

Source: `tools/generate_psl27_golden_model.py`.

## Closed mathematically: H17-02 admissibility law

A new exhaustive finite certificate strengthens the H16 handoff.

For all `168^2 = 28,224` ordered pairs `(A,B)`:

```text
generating ordered pairs        = 19,152
non-generating ordered pairs    =  9,072
generating signature image      =    114
non-generating signature image  =     66
intersection                    =      0
```

Therefore, for valid `PSL(2,7)` ports, the same 114-entry signature ROM is an exact generation-domain recognizer:

`signature_hit <=> <A,B> = PSL(2,7)`.

No separate subgroup-generation checker is required on this laboratory path.

Certificate: `certificates/psl27_signature_admissibility_certificate.py`.

## First erasure law

The exact five-probe signature has

```text
minimum generating-orbit signature distance = 1
minimum generating/non-generating distance  = 2
```

Hence one lost probe may destroy orbit reconstruction, but any one lost probe still preserves generating/non-generating separation.

Exact single-channel deletion statistics are recorded in:

`docs/H17_02_SIGNATURE_ADMISSIBILITY_AND_ERASURE.md`.

## New depth-4 barrier

The complete H16 cyclic trace family of all primitive words of depth at most four has 25 coordinates. Exhaustive comparison of the 114 orbit codewords gives

```text
minimum orbit-code distance = 1
number of distance-1 orbit pairs = 7
unique separating coordinate for all 7 pairs = ABab = [A,B]
```

Therefore exact one-erasure orbit recovery is impossible for **any** observer system restricted to the full depth-`<=4` cyclic-trace family. Redundancy at the same depth cannot repair the problem.

This converts the next strike into a sharp mathematical question: find the shortest depth `>4` probe family (or a different observer type) that raises orbit-code distance to at least two.

## End-to-end RTL generator added

`tools/generate_psl27_end_to_end.py`

It composes the existing H17 generators and emits:

```text
psl27_classify_perm.sv
psl27_five_probe_engine.sv
psl27_orbit_rom.sv
psl27_tomography_core.sv
tb_psl27_tomography_core.sv
psl27_114_orbit_signatures.csv
```

The end-to-end data path is

```text
A,B
 -> exact word engine
 -> oriented six-class channel
 -> 15-bit five-probe signature
 -> 114-entry ROM
 -> orbit_valid / canonical orbit_id
```

The generated testbench covers all 180 five-probe signatures realized by `PSL(2,7)^2`:

- 114 generating signatures must accept with the correct canonical orbit ID;
- one representative of each of the 66 non-generating signatures must reject.

## Verification boundary

The exact Python certificates pass. The current execution environment has no `iverilog`, `verilator`, or `yosys`, so the generated SystemVerilog has not yet crossed the external HDL-simulation/synthesis gate. That gate remains explicitly open.

## Next strike

Search primitive trace words beginning at depth five and determine the minimum additional probe cost needed to raise the 114-orbit code distance from `1` to at least `2`.

Priority order:

1. prove whether depth five already breaks all seven depth-4 defect pairs;
2. minimize the number of added probes over the original five-probe core;
3. if possible, raise distance to `3` for stronger erasure/error protection;
4. generate the redundant RTL interface and compare its word-depth/resource cost against the minimal core.

## Integer-to-port note

`6=2*3` naturally exposes two ordinary multiplicative ports in `Z`, whereas primes such as `17` or `53` require a chosen arithmetic extension/world before nontrivial decomposition ports appear. This remains a future H07/H10/H14 -> H17 frontend and is intentionally not mixed into the exact `PSL(2,7)` hardware theorem.
