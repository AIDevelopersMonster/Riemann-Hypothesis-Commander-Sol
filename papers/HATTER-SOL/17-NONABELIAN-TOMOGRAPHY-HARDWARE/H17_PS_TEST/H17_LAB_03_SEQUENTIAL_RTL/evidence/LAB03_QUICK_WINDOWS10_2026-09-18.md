# H17-LAB-03 · Windows 10 quick regression evidence · 2026-09-18

## Command

```powershell
.\tools\test_lab03.ps1 -Set quick
```

## Result

The complete H17-LAB-03 quick vector set passed:

```text
PASS H17-LAB-03 sequential RTL: 1796 vectors; max_wait_cycles=26
... $finish called at 443150000 (1ps)
LAB-03 quick ELAPSED: 4,682 seconds
```

PowerShell locale uses a comma decimal separator, so the measured wall-clock time is **4.682 s**.

## Progress consistency

The regression printed progress every 25 vectors and retained:

```text
max_wait_cycles=26
```

throughout the run.

## What was checked

For every quick vector the testbench compared the sequential LAB-03 outputs with the frozen LAB-01 golden-vector contract:

- status;
- raw 24-bit robust8 fingerprint;
- observed signature after the requested known erasure;
- repaired 24-bit fingerprint;
- fingerprint_valid consistency.

The legacy orbit_id field is intentionally ignored in the ROM-free LAB-03 mathematical core.

## Interpretation

This result demonstrates that the sequential/time-multiplexed architecture preserves the published H17 mathematical I/O contract on all **1,796 quick vectors** and removes the practical Icarus event-simulation barrier observed for the fully combinational LAB-02 implementation.

It does **not** establish target FPGA frequency, LUT/FF/BRAM utilization, power, or physical latency.

## Next gate

Run:

```powershell
.\tools\test_lab03.ps1 -Set full
```

to check all **29,911** frozen golden vectors.
