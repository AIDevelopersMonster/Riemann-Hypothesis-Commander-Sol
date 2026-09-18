# H17-LAB-02 · STATUS

Branch: research/hatter-sol-17-lab02-romfree-rtl

## Goal

Turn the closed H17-06/H17-07/H17-08 mathematics into a board-independent
pure-RTL mathematical processor and compare it against the H17-LAB-01 golden
vector contract before choosing any FPGA family or vendor toolchain.

## Architecture frozen for this laboratory

    A,B
     -> 2 x structural PSL(2,7) membership-only
     -> inverse A,B
     -> H17-07 shared 14-compose / depth-3 word DAG
     -> 8 x member-class-only conjugacy classifier
     -> 24-bit robust8 raw fingerprint
     -> known erasure marker 111
     -> H17-06 depth-4 ROM-free decision tree
     -> repaired 24-bit canonical orbit fingerprint

No board wrapper, UART, Vivado, Quartus, Gowin, FPGA part or pin map belongs to
the mathematical core.

## Current implementation

- rtl/h17_lab02_core.sv — pure combinational mathematical top.
- tb/tb_h17_lab02_vectors.sv — direct golden-vector test.
- tools/test_lab02.ps1 — deterministic Windows/PowerShell generation,
  compile and test path.
- Existing audited H17 generators provide the closure-aware structural
  frontend and ROM-free repair network.

## Validation gates

- [ ] generate closure-aware RTL deterministically;
- [ ] generate ROM-free repair RTL deterministically;
- [ ] compile LAB-02 with Icarus SystemVerilog;
- [ ] pass H17-LAB-01 quick vectors (1,796);
- [ ] pass H17-LAB-01 full vectors (29,911);
- [ ] add direct LAB-01 vs LAB-02 equivalence testbench;
- [ ] record waveform showing raw -> erased -> repaired fingerprint;
- [ ] only after all pure-RTL gates: compare candidate hardware targets.

No hardware target has been selected.
