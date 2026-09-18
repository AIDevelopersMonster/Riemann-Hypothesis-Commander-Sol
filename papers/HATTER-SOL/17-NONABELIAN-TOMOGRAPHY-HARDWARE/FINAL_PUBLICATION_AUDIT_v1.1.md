# HATTER-SOL-17 · Final publication audit v1.1

**Date:** 2026-09-19  
**Decision:** READY AFTER FIGURE INSERTION AND BILINGUAL REBUILD.  
**DOI:** 10.5281/zenodo.22832502.

## New publication-level result

H17-LAB-03 closes the pure-RTL execution gate for the frozen golden corpus:

```text
smoke  : 1 vector PASS
quick  : 1,796 / 1,796 PASS
full   : 29,911 / 29,911 PASS
latency: max_wait_cycles = 26
```

Full regression wall-clock on the independent Windows 10 host was 91.984 s.

The dedicated waveform test also passed:

```text
raw      = 8d256a
observed = ed256a
repaired = 8d256a
status   = 2
wait     = 26 cycles
```

## Interpretation

LAB-03 validates a sequential/time-multiplexed realization of the H17
mathematics.  The full frozen vector contract is preserved while one
member-class engine is reused in time.

The 26-cycle result is an RTL state-machine latency.  It is not a physical
FPGA time measurement.

## Figure gate

The final article must include:

`figures/H17_LAB03_WAVEFORM_26_CYCLES.png`

with the publication caption explaining:

- 14 shared compositions;
- 8 sequential class captures;
- raw fingerprint construction;
- mode-1 erasure;
- ROM-free repair;
- fingerprint_valid/status/done;
- simulation-time versus target-hardware timing boundary.

## Remaining release work

- add the PNG under the frozen filename;
- synchronize EN v1.1 with RU v1.1;
- rebuild RU/EN DOCX and PDF;
- visually inspect the figure in both PDFs;
- regenerate SHA-256 manifest and Zenodo ZIP;
- publish DOI 10.5281/zenodo.22832502.
