# H17-LAB-03 · Windows 10 smoke evidence · 2026-09-18

## Host-side command

From `H17_PS_TEST/H17_LAB_03_SEQUENTIAL_RTL`, the operator ran:

`./tools/test_smoke.ps1` in PowerShell.

## Observed transcript

```text
== H17-LAB-03 smoke: generate closure classifiers ==
PASS: emitted H17-08 closure-aware membership-only and member-class-only RTL
== H17-LAB-03 smoke: generate ROM-free repair ==
PASS: emitted ROM-free H17-06 repair processor
worst-case class-query depth = 4
decision nodes by erasure = [41, 41, 43, 43, 30, 39, 39, 30]
total depth-optimal internal nodes = 306
orbit fingerprint bits = 24; orbit ROM entries = 0
== H17-LAB-03 smoke: compile ==
== H17-LAB-03 smoke: run exactly one vector ==
SMOKE ELAPSED: 0,081 seconds
```

PowerShell locale prints the decimal separator as a comma; this is 0.081 s.

## Interpretation

The wrapper reached its final elapsed-time line without throwing after the `vvp` invocation. Therefore generation, compilation and the one-vector simulation returned success.

The first wrapper used PowerShell `Measure-Command`, which suppressed the testbench stdout, so this transcript does not expose the internal PASS line or the transaction wait-cycle count. The wrapper was subsequently changed to `System.Diagnostics.Stopwatch`, preserving simulator stdout.

## Comparison boundary

On the same Windows host, the earlier LAB-02 fully combinational smoke had accumulated approximately 17,841 CPU seconds without completing one vector.

This is **not** a target-FPGA speedup measurement and is **not** reported as a formal simulator benchmark ratio. It demonstrates that moving from the all-at-once combinational event graph to the sequential/time-multiplexed architecture removes the practical Icarus execution barrier.

## Next gate

Re-run the updated smoke wrapper once to expose the exact testbench `max_wait_cycles`, then execute the 1,796-vector quick regression.