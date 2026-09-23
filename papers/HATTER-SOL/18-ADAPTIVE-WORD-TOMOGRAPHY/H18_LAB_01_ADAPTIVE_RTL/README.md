# H18-LAB-01 · Adaptive one-erasure RTL

This laboratory is the first hardware realization of H18 adaptive word tomography.

Pipeline:

\[
(A,B)
\rightarrow
\text{PSL membership}
\rightarrow
\text{adaptive word controller}
\rightarrow
\text{shared word engine}
\rightarrow
\text{single class engine}
\rightarrow
\text{orbit ID / REJECT}.
\]

Fault contract:

- at most one query may return ERASED;
- the erased query is not retried;
- the controller must still identify the generating H17 orbit or return REJECT.

Exact H18-06 bound:

\[
4\text{ successful class answers}+1\text{ possible erased attempt}.
\]

## Generate

From this directory:

\`\`\`powershell
py -3 .\tools\generate_h18_adaptive_rtl.py --out-dir generated
\`\`\`

The generator imports the exact H18-06 certificate and emits:

- \`generated/h18_adaptive_strategy.json\`
- \`generated/h18_adaptive_vectors.txt\`
- \`generated/h18_adaptive_erasure_core.sv\`
- \`generated/tb_h18_adaptive_erasure.sv\`
- \`generated/H18_ADAPTIVE_STRATEGY_SUMMARY.md\`

H17 closure-aware membership/classifier RTL is generated separately by the existing H17 tool.

## Frozen first RTL result

CI run \`35428529384\`:

\[
\boxed{985/985\ \mathrm{PASS}}
\]

over 197 orbit states and five fault schedules per state.

Observed:

- max query attempts: 5;
- max RTL wait: 32 cycles.

Generic hierarchy-expanded Yosys cells:

- H17-LAB-03: 13,547;
- H18-LAB-01: 17,205.

So the first hardwired adaptive controller is 27.00% larger in generic cells despite using fewer observations.

See:

- \`../H18_07_ADAPTIVE_RTL_HARDWARE_COST.md\`
- \`.github/workflows/h18-adaptive-rtl.yml\`

## Boundary

This is board-independent RTL and generic synthesis.

It is **not** yet:

- FPGA LUT/FF/BRAM utilization;
- Fmax/timing closure;
- physical latency;
- board power;
- measured FPGA fault tolerance.

The next architecture should compress the 424-node control program rather than hardwire its full decode logic.
