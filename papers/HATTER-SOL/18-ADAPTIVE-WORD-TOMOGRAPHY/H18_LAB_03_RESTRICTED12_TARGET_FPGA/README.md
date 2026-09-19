# H18-LAB-03 · Restricted-12 target FPGA

This laboratory is the first target-FPGA implementation of the H18-11
restricted 12-query adaptive controller.

It keeps the exact H18 one-persistent-erasure information contract:

\[
D_0=4,\qquad S_1=4,\qquad A_1=5.
\]

The supported query alphabet is:

\[
A,\ B,\ ABab,\ AbaB,\ ABB,\ Abb,\ AAb,\ AAAB,\ AAAb,\ Baa,\ aab,\ abb.
\]

## Frozen structural data

Exact H18-11 materialization:

- 305 nonterminal query nodes;
- 67 pre-erasure nodes;
- 238 post-erasure nodes;
- 12 distinct query labels;
- 9-bit node address;
- 4-bit query selector;
- explicit microprogram payload: 18,425 bits.

This is a representation count, not an FPGA RAM-block claim.

## Generated RTL

The generator:

\`\`\`text
tools/generate_h18_r12_rtl.py
\`\`\`

emits into \`generated_r12/\`:

- \`psl27_membership_only.sv\` and \`psl27_member_class_only.sv\`
  are generated separately by the H17 closure-classifier generator;
- \`h18_r12_microcoded_core.sv\`;
- \`tb_h18_r12_microcoded.sv\`;
- \`h18_r12_vectors.txt\`;
- four \`.mem\` microprogram images;
- \`h18_r12_program.json\`;
- \`H18_R12_PROGRAM_SUMMARY.md\`.

The same generated SystemVerilog core is used for generic synthesis and both
Quartus targets.

## 1. Local exact regression

From this laboratory directory:

\`\`\`powershell
.\tools\run_regression.ps1
\`\`\`

Expected behavioral conclusion:

\`\`\`text
PASS H18-LAB-03 restricted12: 197 states x 5 schedules = 985 runs
\`\`\`

The five schedules are:

- no erasure;
- erase attempted query 1;
- erase attempted query 2;
- erase attempted query 3;
- erase attempted query 4.

A fifth attempted query can occur only after the unique erasure has already
been consumed, so a second erasure on attempt 5 is outside the frozen fault
model.

## 1A. Verified local result

Altera ModelSim 10.1d has now completed the full regression:

\[
\boxed{197\times5=985/985\ \mathrm{PASS}}
\]

with observed maxima

\[
\boxed{\max\ attempts=5,\qquad \max\ RTL\ wait=42\ cycles}.
\]

This closes the SystemVerilog behavioral gate for H18-LAB-03.

The 42-cycle value is an RTL cycle count only. It is not a physical latency
claim until routed target \(F_{\max}\) is known.

Evidence:

\`\`\`text
evidence/MODELSIM_R12_2026-09-19.md
\`\`\`

## 2. Cyclone IV E C6 target

Target:

\`\`\`text
EP4CE22F17C6
\`\`\`

This is the direct device/speed-grade control against the H17 Cyclone-IV C6
measurement.

Run:

\`\`\`powershell
.\tools\run_quartus13_cycloneiv_c6.ps1
\`\`\`

Then obtain the detailed routed critical path:

\`\`\`powershell
.\tools\run_worst_path_cycloneiv_c6.ps1
\`\`\`

The SDC uses a 100 MHz reference clock only as an analysis target. 100 MHz is
not assumed to close timing.

## 3. Cyclone V E A7 target

Target:

\`\`\`text
5CEFA7F23C6
\`\`\`

Run:

\`\`\`powershell
.\tools\run_quartus13_cyclonev_a7.ps1
\`\`\`

Then:

\`\`\`powershell
.\tools\run_worst_path_cyclonev_a7.ps1
\`\`\`

The detailed TimeQuest script uses the slow 1100 mV / 85 C operating
condition, matching the earlier H17 Cyclone-V experiment.

## 4. What to record

For each target preserve:

- logic utilization (LE or ALM);
- registers;
- inferred memory bits / RAM blocks;
- inferred DSP blocks, if any;
- pin count;
- Fmax;
- worst setup and hold slack;
- detailed worst data path;
- logic levels;
- cell delay;
- routing delay;
- routing percentage;
- fitter routing usage and optimization notes.

The relevant comparison is not only H18-versus-H17 area. Record also:

\[
\text{cycles per transaction}\times\frac{1}{F_{\max}}
\]

because H18 is sequential and data-dependent.

## 5. Baselines

The principal comparisons are:

### H17-LAB-03 / H17 target evidence

Fixed robust8 architecture:

- 8 fixed observations;
- measured RTL transaction wait 26 cycles;
- Cyclone IV C6 and Cyclone V target evidence already recorded in H17.

### H18-08 baseline

Canonical 24-query microcoded representation:

- 308 query nodes;
- 19,057 explicit program bits;
- dual-RTL CI is a separate baseline gate.

### H18-LAB-03

Restricted-12 successor:

- 305 query nodes;
- 18,425 explicit program bits;
- at most 5 query attempts;
- exact target FPGA measurements pending.

## 6. Claim boundary

Before Quartus reports exist, the only claims are:

- exact finite adaptive correctness;
- exact 12-query restriction;
- generated SystemVerilog realization;
- CI regression/synthesis results when the workflow passes.

Do not claim target LUT/LE/ALM, RAM, DSP, Fmax, routed delay, power, or physical
latency until the corresponding Quartus report has been produced and archived.
