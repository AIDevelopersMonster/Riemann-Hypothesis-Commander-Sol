# H17-09 · Sequential RTL laboratory and publication waveform

**Status:** CLOSED at RTL-simulation level.  
**Date:** 2026-09-19.

## Why LAB-03 was introduced

LAB-02 is a fully combinational realization of the closure-aware robust8 processor. It compiles successfully, but its zero-delay event graph is impractically expensive in Icarus. On an independent Windows 10 host, one LAB-02 smoke vector accumulated about 17,841 CPU seconds without completing.

LAB-03 preserves the H17 mathematics but serializes the computation:

```text
A,B latch
 -> 2 x membership-only
 -> 14 H17-07 compositions, one per cycle
 -> 1 x reused member-class-only engine
 -> 8 x 3-bit fingerprint registers
 -> known erasure mask
 -> H17-06 ROM-free repair
 -> done
```

## Frozen regression results

```text
smoke: 1 vector PASS, 0.081 s wall-clock
quick: 1,796 / 1,796 PASS, max_wait_cycles=26, 4.682 s
full: 29,911 / 29,911 PASS, max_wait_cycles=26, 91.984 s
```

The testbench checks status, raw fingerprint, observed erased signature, repaired fingerprint and fingerprint_valid against the LAB-01 frozen golden-vector contract.

## Publication waveform

Representative vector:

```text
A        = 5e3b88
B        = 7ecc11
mode     = 1
raw      = 8d256a
observed = ed256a
repaired = 8d256a
status   = 2
wait     = 26 cycles
```

Expected figure path:

`figures/H17_LAB03_WAVEFORM_26_CYCLES.png`

The waveform shows:

1. start/busy handshake;
2. the 14-operation shared DAG through `op_idx`;
3. eight class captures through `probe_idx`;
4. stepwise construction of `raw_signature=8d256a`;
5. mode-1 masking to `observed_signature=ed256a`;
6. ROM-free reconstruction to `repaired_signature=8d256a`;
7. `fingerprint_valid=1`, `status=2`, and the final `done` pulse.

## Claim boundary

The measured 26 cycles are RTL transaction latency in the current FSM. They are not a measured FPGA frequency or physical latency. Target performance requires synthesis, place-and-route and timing analysis for a concrete device.
