# H17-LAB-03 · Windows 10 waveform evidence · 2026-09-19

## Command

```powershell
.\tools\make_waveform.ps1
```

## Observed result

```text
VCD info: dumpfile build/h17_lab03_waveform.vcd opened for output.
PASS H17-LAB-03 waveform: wait_cycles=26 raw=8d256a observed=ed256a repaired=8d256a
... $finish called at 330000 (1ps)

PASS: waveform VCD created:
...\build\h17_lab03_waveform.vcd
```

## Frozen publication transaction

- A = `5e3b88`
- B = `7ecc11`
- mode = `1`
- raw signature = `8d256a`
- observed signature = `ed256a`
- repaired signature = `8d256a`
- status = `2`
- measured wait = **26 cycles**

## Interpretation

The VCD is not only emitted; the waveform testbench self-checks the terminal
mathematical result before calling PASS.

The remaining waveform gate is visual inspection in GTKWave and saving a
publication-oriented trace view.
