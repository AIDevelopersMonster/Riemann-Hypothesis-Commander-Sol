# H17-LAB-03 · Windows 10 full regression evidence · 2026-09-18

## Command

```powershell
.\tools\test_lab03.ps1 -Set full
```

## Final result

```text
PASS H17-LAB-03 sequential RTL: 29911 vectors; max_wait_cycles=26
... $finish called at 8315830000 (1ps)
LAB-03 full ELAPSED: 91,984 seconds
```

PowerShell locale uses a comma decimal separator, so the wall-clock elapsed
time is **91.984 s**.

## Scope checked

For every frozen full-vector row the sequential processor was checked against
the LAB-01 golden contract for:

- status;
- raw robust8 fingerprint;
- observed signature after the requested known erasure;
- repaired robust8 fingerprint;
- fingerprint_valid consistency.

The legacy orbit_id column remains intentionally outside the ROM-free
mathematical output.

## Result

[
\boxed{29911/29911\ \text{PASS}}
]

and

[
\boxed{\max\_wait\_cycles=26}.
]

No target-FPGA Fmax, LUT/FF/BRAM count, power or physical latency is inferred
from this simulator result.

## Next gate

Generate and inspect a publication waveform for a representative generating
transaction, then perform generic synthesis of LAB-03.
