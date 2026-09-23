# HATTER-SOL-18 · H18-07
# First adaptive RTL realization and generic hardware-cost comparison

**Status:** CLOSED first engineering layer.

## 1. What was implemented

H18-06 gave an exact finite strategy for identify-or-REJECT tomography under one persistent known query erasure:

\[
4\text{ successful class answers}+1\text{ possible ERASED attempt}.
\]

H18-07 materializes that strategy as a sequential RTL processor.

The generated core:

- accepts packed H17 permutation inputs \(A,B\);
- checks raw membership in \(PSL(2,7)\);
- uses only freely reduced words of length at most four;
- reuses one permutation-composition datapath;
- reuses one member-class-only classifier;
- follows a hardwired adaptive decision controller;
- allows one query to be marked ERASED;
- never retries the erased query;
- returns one of 114 H17 orbit IDs or REJECT.

No FPGA vendor primitive or target device is used.

---

## 2. Materialized strategy size

The deterministic generator materializes the exact H18-06 strategy into:

\[
\boxed{424\text{ controller nodes}}
\]

consisting of:

- 308 query nodes;
- 114 orbit terminals;
- 1 REJECT terminal;
- 1 FAULT terminal.

Among the query nodes:

- 69 belong to the pre-erasure phase;
- 239 belong to post-erasure continuations.

The selected strategy uses 24 distinct word representatives, all with

\[
\boxed{|w|\le4}.
\]

This is the first machine-level size measurement of the exact adaptive program.

---

## 3. RTL regression

GitHub Actions run:

\[
\boxed{\texttt{35428529384}}
\]

completed successfully.

The generated SystemVerilog was compiled with Icarus and tested on every one of the 197 simultaneous-conjugacy pair-orbit representatives.

For each state the testbench ran five fault schedules:

1. no erasure;
2. erase attempt 1;
3. erase attempt 2;
4. erase attempt 3;
5. erase attempt 4.

Thus:

\[
197\times5=985
\]

RTL transactions were checked.

Exact observed result:

\[
\boxed{985/985\ \mathrm{PASS}}.
\]

Observed maxima:

\[
\boxed{\text{max attempts}=5},
\]

\[
\boxed{\text{max RTL wait}=32\text{ cycles}}.
\]

The 32-cycle value is an RTL-controller schedule measurement, not target-FPGA physical latency.

---

## 4. Generic Yosys comparison with H17-LAB-03

The same CI run synthesized both designs with Yosys 0.33 under a common technology-independent methodology.

The comparison uses hierarchy-expanded generic-cell counts.

| Metric | H17-LAB-03 fixed robust8 | H18-LAB-01 adaptive erasure | Delta |
|---|---:|---:|---:|
| generic cells | 13,547 | 17,205 | +3,658 (+27.00%) |
| sequential generic cells | 417 | 177 | -240 |
| mux-family cells | 2,439 | 1,855 | -584 |
| observed RTL max wait | 26 cycles | 32 cycles | +6 cycles |
| fixed/adaptive observations | 8 fixed probes | at most 5 attempts | -3 attempts |

The generic-cell result is the important surprise:

\[
\boxed{
\text{fewer observations did not produce a smaller first RTL implementation}.
}
\]

The first adaptive realization is about

\[
\boxed{27\%}
\]

larger in hierarchy-expanded generic Boolean cells than H17-LAB-03.

---

## 5. Why adaptive is larger in the first implementation

The datapath itself is highly shared: one word-composition path and one class engine.

The cost is instead concentrated in the hardwired controller.

The exact adaptive strategy contains 308 query nodes and a large number of class-dependent next-node transitions. Yosys turns this large symbolic switch network primarily into OR/AND decode logic.

Hierarchy-expanded dominant cell counts:

### H17-LAB-03

- ANDNOT: 4,488;
- OR: 2,921;
- MUX: 2,439.

### H18-LAB-01

- OR: 7,062;
- ANDNOT: 4,776;
- MUX: 1,855.

So H18 uses fewer mux cells and fewer sequential cells, but much more OR/decode logic.

This diagnoses the next engineering bottleneck precisely:

\[
\boxed{
\text{adaptive information gain is being paid for as hardwired control decode}.
}
\]

---

## 6. What is and is not being compared

The output contracts are different.

H17-LAB-03:

\[
(A,B)\mapsto\text{robust8 fingerprint/repaired fingerprint}.
\]

H18-LAB-01:

\[
(A,B)\mapsto\text{orbit ID or REJECT}
\]

through an adaptive path.

Therefore the 27% number is not a universal statement that adaptive tomography is more expensive. It is a measurement of these two current RTL realizations under one generic synthesis methodology.

No target-specific LUT, FF, BRAM, Fmax, power, place-and-route, or physical-board result is claimed.

---

## 7. The next optimization target

The result points to an obvious architectural repair.

The 424-node adaptive strategy should not necessarily be expanded into random combinational decode.

Three candidate representations are now worth comparing:

1. **microcoded ROM/BRAM controller**  
   store node records \((word,next_0,\ldots,next_5,erase\_next)\);

2. **factored decision DAG**  
   merge structurally equivalent subtrees beyond the current mathematical memoization and optimize encoding jointly with hardware cost;

3. **Nielsen/Higman symmetry quotient controller**  
   encode repeated transition patterns using the four \(\tau\)-components and word symmetries rather than individual hardwired nodes.

This creates the next engineering question:

\[
\boxed{
\text{can the 27\% controller overhead be compressed below H17-LAB-03?}
}
\]

The mathematical observation advantage is already exact:

\[
8_{\rm fixed}\to5_{\rm adaptive\ attempts}.
\]

H18-07 shows that turning that information advantage into an area advantage requires a better controller representation.

---

## 8. Reproducibility evidence

Workflow:

\[
\texttt{.github/workflows/h18-adaptive-rtl.yml}
\]

Successful run:

\[
\texttt{35428529384}
\]

Artifact:

\[
\texttt{h18-adaptive-rtl-evidence}
\]

Artifact ID:

\[
\texttt{10579876480}
\]

Artifact ZIP SHA-256:

\[
\boxed{
\texttt{91c14f80d847c8811e230821149fee692a45f349a561b1231108fefcb815dcab}
}
\]

The artifact contains the exact strategy JSON, strategy summary, Icarus regression log, both Yosys logs, and the generated comparison report.
