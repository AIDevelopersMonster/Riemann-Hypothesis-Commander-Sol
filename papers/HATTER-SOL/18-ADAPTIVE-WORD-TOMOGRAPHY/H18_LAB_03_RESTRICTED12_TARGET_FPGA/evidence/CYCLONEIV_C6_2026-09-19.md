# H18-LAB-03 — Cyclone IV E C6 physical evidence

Date: 19 September 2026.

Target:

- Quartus II 13.1 Web Edition
- Cyclone IV E EP4CE22F17C6
- 100 MHz SDC reference clock
- Slow 1200 mV / 85 C sign-off corner

## Functional prerequisite

Before target compilation, the exact restricted-12 RTL passed Altera ModelSim:

\[
197\times 5=985/985
\]

with:

- maximum query attempts: 5;
- maximum RTL transaction latency: 42 cycles.

## Place-and-route

Quartus full compilation completed successfully.

Resource result:

- 5,227 / 22,320 logic elements = 23%;
- 5,200 combinational functions;
- 211 dedicated logic registers;
- 68 / 154 package pins;
- 0 inferred memory bits.

The zero-memory result is important: Quartus reports that
\`class_next_rom\` is not inferred as RAM because its read is asynchronous,
while \`word_desc_rom\` is too small for RAM inference. Therefore the current
18,425-bit explicit microprogram is not physically mapped as block RAM in this
implementation.

Fitter routing:

- estimated average interconnect usage: 4%;
- estimated peak interconnect usage: 28%;
- Auto Fit was used and fitter optimizations were skipped to reduce compile
  time.

## Timing

Slow 1200 mV / 85 C:

\[
F_{\max}=41.28\ {\rm MHz}.
\]

At the 100 MHz analysis reference:

- setup slack: -14.227 ns;
- setup TNS: -254.485 ns;
- hold slack: +0.345 ns.

Detailed worst path:

- from \`class_perm[15]\`;
- to \`next_node_q[5]\`;
- data delay: 24.510 ns;
- 42 logic levels;
- cell delay: 10.525 ns;
- routing delay: 13.799 ns.

Thus the dominant path crosses the class observer and the asynchronous
class-transition decode. This is the principal current timing boundary.

## Direct H17-LAB-02 comparison on the same target

H17-LAB-02, EP4CE22F17C6:

- 19,540 logic elements = 88%;
- 132 registers;
- Fmax 24.52 MHz;
- worst data delay 41.082 ns;
- 65 logic levels;
- one registered result cycle after input acceptance.

H18-LAB-03, EP4CE22F17C6:

- 5,227 logic elements = 23%;
- 211 registers;
- Fmax 41.28 MHz;
- worst data delay 24.510 ns;
- 42 logic levels;
- worst verified RTL transaction: 42 cycles.

Interpretation:

- H18-LAB-03 uses about 3.74 times fewer logic elements than H17-LAB-02;
- H18-LAB-03 Fmax is about 1.68 times higher;
- nevertheless H18-LAB-03 worst-case transaction latency is roughly
  42 / 41.28 MHz = 1.02 us, whereas H17-LAB-02's one-cycle registered result
  is roughly 1 / 24.52 MHz = 40.8 ns.

Therefore the current adaptive microcoded architecture is an area/Fmax winner
but a latency loser against the wide H17-LAB-02 combinational architecture.

This is not a theorem about adaptive tomography in general. It is an
implementation result for the present sequential reuse architecture.

## Mathematical-to-hardware interpretation

The large area reduction is mainly produced by architectural reuse of one word
engine and one classifier. The Nielsen 50-to-12 query-language compression is
real but by itself only reduced the explicit microprogram payload from 19,057
to 18,425 bits, because the six-way transition table remains dominant.

The next hardware question is therefore not merely whether the alphabet can be
reduced below 12. More consequential targets are:

1. factor the six-way transition program using Nielsen/Higman symmetry;
2. register the classifier/transition boundary;
3. test synchronous block-RAM transition storage;
4. explore partially parallel H18 implementations to move along the
   area/latency Pareto frontier.

No power or minimum achievable latency claim is made.
