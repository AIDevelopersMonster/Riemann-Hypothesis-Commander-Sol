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
wrapped by input/output registers, passes a real vendor synthesis, fitting,
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

The 134 top-level pins consume 87% of the selected package pins. Quartus emits
Critical Warning 169085 because no physical pin locations are assigned. This is
expected for the board-free benchmark and is not evidence of a logic failure.

## TimeQuest result

The reference SDC asks for a 10 ns / 100 MHz clock. H17-LAB-02 does not meet
that one-cycle target.

At the sign-off-relevant slow 1200 mV, 85 C corner:

[
oxed{F_{max}=24.52 mathrm{MHz}}
]

with

[
oxed{	ext{setup slack}=-30.782 mathrm{ns}}
]

and positive hold slack

[
oxed{	ext{hold slack}=+0.343 mathrm{ns}}.
]

The worst reported setup path is

[
b_q[14]ightarrow repaired_signature[11]
]

with reported data delay

[
oxed{41.082 mathrm{ns}}.
]

Thus the natural one-cycle period of the fully combinational H17-LAB-02 core on
this Cyclone IV E target is about

[
1/24.52 mathrm{MHz}approx 40.8 mathrm{ns}.
]

Other reported corners are consistent with the same interpretation:

- slow 1200 mV, 0 C: Fmax 27.24 MHz, setup slack -26.712 ns, hold +0.299 ns;
- fast 1200 mV, 0 C: setup slack -13.435 ns, hold +0.178 ns.

The critical paths terminate in `repaired_signature`, so the dominant path is
the intended mathematical chain from registered raw input through word
construction, conjugacy-class logic and ROM-free repair to the registered
fingerprint result.

## Constraint caveat

TimeQuest warns that no clock uncertainty assignment is present and that the
design is not fully constrained for external setup/hold requirements.

That warning matters for absolute sign-off precision, but it does not invalidate
the internal same-clock register-to-register Fmax comparison used here. A later
physical-target run should add derived clock uncertainty and real I/O timing.

## Interpretation

The experiment separates two different questions that were previously being
conflated.

### RTL simulation

The modular LAB-02 event-driven Icarus simulation can be impractically slow,
even on a single vector.

### Hardware synthesis

Quartus successfully synthesized, fitted, assembled and timing-analyzed the same
architecture in about 9.8 minutes.

Therefore

[
oxed{	ext{slow event-driven RTL simulation}
eq	ext{unsynthesizable hardware}}
]

for H17-LAB-02.

The fully combinational architecture is valid, but on this target it occupies
88% of the device and its unpipelined one-cycle Fmax is about 24.5 MHz.

This makes H17-LAB-02 a useful high-parallelism endpoint rather than a universal
implementation optimum. Pipeline cuts or a hybrid sequential/combinational
architecture are the natural next hardware comparisons.
