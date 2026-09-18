# HATTER-SOL-17 · Final publication audit v1.0

**Date:** 2026-09-18  
**Decision:** READY FOR ZENODO as an exact finite-model / RTL / generic-synthesis preprint.  
**Not claimed:** measured target-FPGA implementation.

## Publication scope

H17 v1.0 is frozen as a theorem-to-RTL architecture study. The publication boundary ends before target-specific place-and-route, LUT/FF/BRAM/Fmax/power and physical-board measurements.

This resolves the v0.2 gate precisely: the threshold for a completed physical-FPGA article is not crossed, but the threshold for a clearly delimited architecture/RTL/generic-synthesis publication is crossed.

## Authoritative claims

1. Canonical PSL(2,7) model: 168 elements, 28,224 ordered pairs, 19,152 generating pairs, 9,072 non-generating pairs, 114 generating simultaneous-conjugacy orbits.
2. The H16 five-probe signature is injective but not one-known-erasure resilient.
3. The complete depth-at-most-four candidate family retains seven generating-orbit distance-one defects.
4. Depth five admits an eight-probe joint one-known-erasure family with both relevant distances equal to two.
5. Eight probes are minimal in the stated 51-coordinate candidate family according to the zero-gap MILP plus exact verification.
6. The structural class engine is exhaustively checked on all 40,320 permutations.
7. The shared word DAG reduces 26 compositions to 14 in the stated model, with maximum depth three.
8. ROM-free repair has worst-case decision-tree depth four for a known erased coordinate.
9. Closure-aware classification is correct under exact group operations.
10. Under the stated generic Yosys methodology the flat core changes 43,330 -> 24,730 cells and the ROM-free core 42,484 -> 23,937 cells.

## Required claim boundary

The publication does not claim target FPGA timing closure, physical-board validation, recovery of damaged A/B, unknown-error correction, arbitrary sensor recovery, universal hardware fault tolerance, cryptographic hardness, post-quantum security, PUF unclonability, or application superiority.

## Evidence labels

- THEOREM
- EXHAUSTIVE COMPUTATION
- RTL VERIFIED
- GENERIC SYNTHESIS
- TARGET SYNTHESIS
- MEASURED HARDWARE
- RESEARCH HYPOTHESIS

No TARGET SYNTHESIS or MEASURED HARDWARE label is used without evidence.

## Publication title

**RU:** HATTER-SOL-17: От неабелевых портов к вычислительному устройству — точная орбитальная томография, восстановление известного стирания и путь к FPGA

**EN:** HATTER-SOL-17: From Non-Abelian Ports to a Computing Device — Exact Orbit Tomography, Known-Erasure Recovery, and the Path to FPGA

## DOI rule

The article DOI is assigned by Zenodo at deposition and must not be pre-invented.

## After DOI reservation

Insert DOI into RU/EN sources and metadata, rebuild PDF/DOCX, regenerate SHA-256 manifest, perform visual QA, publish Zenodo record, then add ZENODO_PUBLICATION.md and update HATTER-SOL navigation.
