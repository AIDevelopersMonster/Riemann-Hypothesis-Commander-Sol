# HATTER-SOL-17 · Publication assembly v1.1

**Date:** 2026-09-19  
**Series DOI:** 10.5281/zenodo.17996774  
**ORCID:** 0009-0008-6009-3196  
**Article DOI:** **10.5281/zenodo.22832502**

## Why v1.1

Version 1.1 supersedes the pre-LAB-03 publication assembly.

The mathematical H17-01..H17-08 layers are unchanged.  The new material is the
completed sequential RTL laboratory H17-LAB-03 and its publication waveform.

## New v1.1 evidence

Independent Windows 10 RTL simulation:

- smoke: 1 vector PASS, 0.081 s wall-clock;
- quick: 1,796 / 1,796 PASS, max_wait_cycles = 26, 4.682 s;
- full: 29,911 / 29,911 PASS, max_wait_cycles = 26, 91.984 s;
- dedicated waveform transaction:
  raw 8d256a -> observed ed256a -> repaired 8d256a,
  status=2, wait_cycles=26.

The current FSM therefore has a measured RTL transaction latency of 26 cycles
on the frozen valid-path transaction used by the regression.  This is not an
FPGA Fmax or physical-latency claim.

## Figure required before final PDF build

Place the GTKWave screenshot at exactly:

`papers/HATTER-SOL/17-NONABELIAN-TOMOGRAPHY-HARDWARE/figures/H17_LAB03_WAVEFORM_26_CYCLES.png`

The RU v1.1 Markdown already references this relative path.

## Authoritative v1.1 text

- `HATTER_SOL_17_RU_v1.1.md`
- EN v1.1 must carry the same LAB-03 section and claim boundary before the final
  Zenodo byte package is regenerated.

## Final publication boundary

H17 v1.1 claims:

- exact finite mathematics;
- exhaustive finite certificates;
- RTL equivalence on 29,911 frozen vectors;
- publication waveform;
- generic technology-independent synthesis for the closure-aware LAB-02 class
  of designs.

H17 v1.1 still does not claim:

- target FPGA LUT/FF/BRAM/DSP utilization;
- timing closure or Fmax;
- measured board power or latency;
- physical distributed-probe fault tolerance.

## Next engineering gate

1. generic-synthesize LAB-03 under the same methodology as LAB-02;
2. compare area/latency tradeoff;
3. choose candidate FPGA family/part;
4. map/place/route and run STA;
5. only then define the physical board experiment.
