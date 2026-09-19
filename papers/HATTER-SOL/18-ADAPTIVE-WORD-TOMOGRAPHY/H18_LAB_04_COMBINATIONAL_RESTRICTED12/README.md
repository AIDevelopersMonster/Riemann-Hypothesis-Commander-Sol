# H18-LAB-04 · Combinational restricted-12

Purpose: compare synchronous architectures with synchronous architectures.

H17-LAB-02 used registered inputs, one wide combinational mathematical core,
and registered outputs. H18-LAB-03 instead reused one word engine and one
classifier across up to 42 RTL cycles. LAB-04 compiles the exact H18-11
restricted-12 adaptive strategy back into combinational hardware.

Architecture:

\[
\text{registered inputs}
\rightarrow
\text{parallel 12-query shared word-DAG}
\rightarrow
\text{305-node compiled decision DAG}
\rightarrow
\text{registered result}.
\]

The fault input is the identity of one persistently unavailable query, not a
temporal pulse. This is the static/circuit form of the same known-query-erasure
model.

Generated structure:

- 12 supported query labels;
- 19 shared prefix-DAG permutation compositions;
- maximum word-DAG composition depth 3;
- 305 exact H18-11 decision nodes;
- maximum adaptive query depth including one erasure: 5;
- target wrapper latency: one registered result cycle.

## Exact local regression

Run:

\`\`\`powershell
.\tools\run_regression.ps1
\`\`\`

The regression checks all 197 simultaneous-conjugacy pair states against all
13 static fault identities:

- no erasure;
- each of the 12 supported query labels erased.

Total:

\[
197\times13=2561
\]

registered transactions.

Expected marker:

\`\`\`text
PASS H18-LAB-04 comb: 197 states x 13 erasure identities = 2561 runs; one registered result cycle
\`\`\`

## Cyclone IV C6

Target:

\`\`\`text
EP4CE22F17C6
\`\`\`

Run:

\`\`\`powershell
.\tools\run_quartus13_cycloneiv_c6.ps1
.\tools\run_worst_path_cycloneiv_c6.ps1
\`\`\`

The same 100 MHz reference SDC and Slow 1200 mV / 85 C TimeQuest corner are
used as in H17-LAB-02 and H18-LAB-03.

## Comparison boundary

The primary comparison is:

\[
H17\text{-LAB-02 fixed robust8 combinational}
\quad\text{vs}\quad
H18\text{-LAB-04 adaptive restricted12 compiled combinational}.
\]

Both use a one-result-cycle registered wrapper.

This experiment does not claim that combinational compilation is the optimal
H18 hardware implementation. It measures one exact point on the
area/latency tradeoff.
