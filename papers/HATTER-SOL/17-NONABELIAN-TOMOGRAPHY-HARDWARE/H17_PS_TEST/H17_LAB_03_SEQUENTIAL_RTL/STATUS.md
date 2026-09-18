# H17-LAB-03 · STATUS

Branch: `research/hatter-sol-17-lab03-sequential-rtl`

## Motivation

LAB-02 generation and compilation reproduce correctly on independent Windows
hosts, but Icarus execution of the fully combinational core is impractically
slow.  On the second host a one-vector smoke run accumulated about 17,841 CPU
seconds without completion.

This is treated as a reproducible simulator/event-graph barrier.

## Architecture

    A,B latch
      -> 2 x membership-only
      -> H17-07 14-operation DAG, 1 composition/cycle
      -> 1 x reusable member-class-only
      -> 8 x 3-bit class registers
      -> known erasure mask
      -> H17-06 ROM-free repair
      -> done

## Mathematical invariants preserved

- robust8 probe order unchanged;
- H17-07 DAG unchanged;
- closure theorem unchanged;
- class coding unchanged;
- known-erasure semantics unchanged;
- ROM-free repair unchanged;
- LAB-01 vector contract unchanged except legacy orbit_id remains intentionally
  outside the ROM-free mathematical output.

## First independent Windows smoke result

On 2026-09-18, a second Windows 10 host reproduced the LAB-03 path:

- closure-classifier generation: PASS;
- ROM-free repair generation: PASS;
- Icarus compile: PASS;
- one-vector simulation returned success;
- measured smoke wall-clock time: **0.081 s**.

The previous LAB-02 fully combinational one-vector run on the same host had
accumulated about **17,841 CPU seconds without completion**.

This is not treated as a formal hardware speedup comparison.  It establishes
that the architectural serialization removes the practical Icarus
event-simulation barrier.

The first wrapper used PowerShell `Measure-Command`, which suppressed the
testbench stdout.  Therefore the exact wait-cycle count was not visible in
that first run.  The wrapper is now changed to `Stopwatch`, preserving the
testbench PASS/progress output.

## Validation gates

- [x] generate closure classifiers deterministically;
- [x] generate ROM-free repair deterministically;
- [x] compile sequential LAB-03 with Icarus;
- [x] pass one-vector smoke;
- [x] record smoke wall-clock time: 0.081 s;
- [x] record exact wait-cycle count from visible testbench stdout: 26 cycles;
- [x] pass quick 1,796 vectors in 4.682 s;
- [x] pass full 29,911 vectors in 91.984 s;
- [ ] compare LAB-02 combinational and LAB-03 sequential outputs on a finite
      regression subset;
- [ ] synthesize LAB-03 generically and compare area with LAB-02;
- [ ] only then select candidate FPGA targets.

## Non-claim

The sequential clock used by the testbench is a simulation clock.  No target
Fmax or physical latency is claimed before target synthesis/place-and-route.


## Quick regression result

On the same independent Windows 10 host, the LAB-03 quick regression completed successfully on 2026-09-18.

Observed result:

- vectors: **1,796 / 1,796 PASS**;
- maximum observed transaction wait: **26 cycles**;
- simulator-reported final time: **443150000 ps**;
- PowerShell wall-clock elapsed time: **4.682 s**;
- no mismatches in status, raw signature, observed erased signature or repaired signature.

This closes the practical simulation gate that blocked LAB-02.  The result is an RTL-simulation result only; it is not a target-FPGA timing or throughput claim.

The next validation gate is the full **29,911-vector** regression.


## Full regression result

On 2026-09-18 the independent Windows 10 host completed the full frozen
LAB-01/LAB-03 regression:

- vectors: **29,911 / 29,911 PASS**;
- maximum observed transaction wait: **26 cycles**;
- simulator final time: **8315830000 ps**;
- wall-clock elapsed time: **91.984 s**;
- no mismatches in status, raw signature, observed erased signature,
  repaired signature or fingerprint_valid.

This closes the full pure-RTL equivalence gate for the frozen vector corpus.

The remaining pre-hardware tasks are:
1. archive a publication-quality waveform for one representative transaction;
2. generic-synthesize LAB-03 and compare area/latency with LAB-02;
3. then select candidate FPGA targets.
