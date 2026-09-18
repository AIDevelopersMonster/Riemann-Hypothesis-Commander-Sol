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

## Validation gates

- [ ] generate closure classifiers deterministically;
- [ ] generate ROM-free repair deterministically;
- [ ] compile sequential LAB-03 with Icarus;
- [ ] pass one-vector smoke;
- [ ] record smoke wall-clock time and wait-cycle count;
- [ ] pass quick 1,796 vectors;
- [ ] pass full 29,911 vectors;
- [ ] compare LAB-02 combinational and LAB-03 sequential outputs on a finite
      regression subset;
- [ ] synthesize LAB-03 generically and compare area with LAB-02;
- [ ] only then select candidate FPGA targets.

## Non-claim

The sequential clock used by the testbench is a simulation clock.  No target
Fmax or physical latency is claimed before target synthesis/place-and-route.
