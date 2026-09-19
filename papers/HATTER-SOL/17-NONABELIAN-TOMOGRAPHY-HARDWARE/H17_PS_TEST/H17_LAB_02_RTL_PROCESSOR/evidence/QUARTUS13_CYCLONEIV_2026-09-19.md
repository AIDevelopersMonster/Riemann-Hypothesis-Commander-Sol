# H17-LAB-02 · Quartus II 13.1 Cyclone IV E evidence

**Date:** 2026-09-19  
**Branch:** `research/hatter-sol-17-lab02-romfree-rtl`  
**Tool:** Quartus II 13.1.0 Build 162 Web Edition, 64-bit  
**Target:** Cyclone IV E `EP4CE22F17C6`  
**Board:** none; technology-mapping benchmark only.

## Flow result

Quartus full compile completed successfully.

| Stage | Wall time | Peak memory reported |
|---|---:|---:|
| Analysis & Synthesis | 00:04:40 | 4724 MB |
| Fitter | 00:04:38 | 5128 MB |
| Assembler | 00:00:03 | 4616 MB |
| TimeQuest Timing Analyzer | 00:00:14 | 4828 MB |

Total wrapper-measured compile time:

[
589.939 mathrm{s}approx 9.83 mathrm{min}.
]

This establishes that the complete H17-LAB-02 combinational mathematical core,
wrapped by input/output registers, can pass a real vendor synthesis, fitting,
assembler and STA flow.

## Fitter utilization

Quartus reports:

[
oxed{19540/22320 = 88% 	ext{logic elements}}
]

with

- total combinational functions: 19,537 / 22,320 (88%);
- dedicated logic registers: 132 / 22,320 (<1%);
- total registers: 132;
- total memory bits: 0 / 608,256;
- PLLs: 0 / 4.

This confirms the expected architecture character: the cost is overwhelmingly
combinational logic, not state or RAM.

The 134 unconstrained top-level pins consume 87% of the selected package pins.
Quartus emits Critical Warning 169085 because no physical pin locations are
assigned. This is expected for the board-free benchmark and is not evidence of
a logic or timing failure.

## Interpretation

The result materially changes the interpretation of the earlier Windows/Icarus
smoke behavior.

A one-vector event-driven RTL simulation could take impractically long, while
Quartus successfully reduced, mapped, placed and routed the same architecture
in finite host time.

Therefore the simulation pathology must not be used as evidence that the
combinational architecture is unsynthesizable.

The remaining decisive measurement is the TimeQuest register-to-register setup
result for the 10 ns reference clock.

## Pending

Record from `h17_lab02_q13.sta.rpt`:

- setup slack;
- Fmax / Restricted Fmax if reported;
- worst register-to-register path endpoints;
- path delay / logic depth if available.
