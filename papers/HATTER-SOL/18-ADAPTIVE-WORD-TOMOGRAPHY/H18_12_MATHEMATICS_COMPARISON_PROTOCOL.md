# H18-12 · Protocol for Comparing Different Mathematics in Hardware

Status: **DRAFT METHOD**

This protocol is intended for comparisons where two mathematical descriptions,
algorithms, algebraic factorizations, or observer systems are claimed to solve
the same abstract finite problem.

The purpose is to measure differences caused by the **mathematical
presentation**, rather than accidentally measuring different interfaces,
different fault contracts, different pipelines, or different FPGA targets.

---

## 1. Declare the abstract task before the implementations

Write the common task as either

\[
\Phi:X\to Y
\]

or a correctness relation

\[
\mathcal R\subseteq X\times F\times Y.
\]

Do not begin with HDL modules.

For every pair of models \(M_1,M_2\), classify the comparison:

- **E0 exact**: identical abstract map after fixed encodings;
- **E1 contract-equivalent**: same abstract correctness relation, different
  internal protocols / fault alphabets;
- **E2 related only**: not a direct complexity comparison.

Only E0 supports an unqualified "same function" claim.

---

## 2. Freeze interface encodings

The following must be identical or explicitly translated:

- input object encoding;
- output encoding;
- validity convention;
- reject/fault convention;
- clock/reset/start/done convention;
- registered input/output boundary.

If encodings differ, measure and report the translation cost separately.

---

## 3. Freeze the realization discipline

Declare a discipline \(\Pi\) before comparing mathematics.

Examples:

### One-cycle spatial discipline

\[
\text{input register}
\to
\text{combinational mathematical core}
\to
\text{output register}.
\]

This is the H17-LAB-02 versus H18-LAB-04 discipline.

### Sequential reusable discipline

One shared arithmetic/observer engine with registered state transitions.

This is the H18-LAB-03 style.

Do not compare one-cycle and 42-cycle designs and attribute the full difference
to mathematics.  That is an architecture comparison.

---

## 4. Preserve enough structure for the mathematics to remain observable

A presentation comparison requires a declared translation from mathematical
primitives to RTL/Boolean primitives.

Record:

- algebraic primitive library;
- common-subexpression sharing rule;
- whether decision-DAG sharing is preserved;
- whether algebraic identities may rewrite across primitive boundaries;
- whether ROM tables may replace explicit logic;
- whether all branches are spatialized or time-multiplexed.

An unrestricted truth-table optimizer can erase the distinction between two
presentations of the same function.

Therefore both the original mathematical representation and the post-synthesis
netlist must be retained.

---

## 5. Freeze the technology stack

For a matched FPGA comparison, hold fixed:

- exact FPGA device;
- package;
- speed grade;
- tool and version;
- synthesis / fitter settings;
- seed policy;
- clock constraints;
- operating corner;
- I/O policy;
- hard-block inference policy.

If one item changes, that is a technology-effect experiment and must be labeled
as such.

---

## 6. Verify semantics independently before measuring cost

Every implementation must pass an independent correctness gate.

Preferred hierarchy:

1. exact mathematical certificate;
2. exhaustive finite-state or vector regression when feasible;
3. independent RTL simulator;
4. synthesis sanity;
5. place-and-route;
6. optional post-fit timing simulation where supported.

A smaller/faster circuit that has not passed the same semantic gate is not a
valid competitor.

---

## 7. Record three layers of complexity

### Layer A — mathematical structure

Examples:

- number of primitive algebraic operations;
- straight-line program length;
- algebraic depth;
- decision/query depth;
- number of states/nodes;
- number of distinct observers;
- branch factor;
- explicit program/storage bits.

### Layer B — Boolean / mapped structure

Examples:

- generic Boolean cells;
- mux count;
- LUT/LE/ALM count;
- register count;
- inferred RAM;
- DSP/hard-block usage;
- mapped logic depth.

### Layer C — physical structure

Examples:

- routed critical-path delay;
- cell/routing decomposition;
- Fmax;
- congestion/interconnect use;
- transaction cycles;
- physical transaction latency.

The purpose is to detect where a mathematical transformation gains or loses
leverage.

---

## 8. Use a vector comparison first

For matched successful implementations report

\[
\mathbf r(M_2:M_1)=
\left(
\frac{A_2}{A_1},
\frac{d_2}{d_1},
\frac{F_2}{F_1},
\frac{N_2}{N_1},
\frac{T_2}{T_1},
\frac{M_2^{\rm mem}}{M_1^{\rm mem}},
\ldots
\right).
\]

Do not collapse this to a single "winner".

Use Pareto dominance.

Application-specific scalarizations such as \(AT\) or \(AT^2\) may be added
after the vector is shown.

---

## 9. Treat NO-FIT as a censored but meaningful observation

If one design does not fit:

- record post-map estimated area;
- record target capacity;
- record fitter failure;
- do not report routed Fmax;
- move both models to a common larger target for timing comparison if needed.

The no-fit boundary itself is a valid density result.

Current H17/H18 example:

\[
H17\text{-LAB-02 on EP4CE22F17C6}: \text{FIT at }19540\text{ LE},
\]

\[
H18\text{-LAB-04 on EP4CE22F17C6}: \text{NO FIT at }26332>22320.
\]

This establishes a same-target density difference but not a same-target timing
ratio.

---

## 10. Separate mathematics, architecture, and technology by paired controls

Use at least the following controls where possible.

### Mathematics control

Same \(\Theta\), same \(\Pi\), different \(M\).

Example:

\[
H17\text{-LAB-02}
\quad\text{vs}\quad
H18\text{-LAB-04}
\]

on the same EP4CE115F29C7.

### Architecture control

Same \(M\), same \(\Theta\), different \(\Pi\).

Example:

\[
H18\text{-LAB-03 sequential}
\quad\text{vs}\quad
H18\text{-LAB-04 spatialized}.
\]

### Technology control

Same \(M\), same \(\Pi\), different \(\Theta\).

Example:

H17-LAB-02 on different Cyclone-IV capacities/speed grades.

This triangulation is the minimum practical defense against attributing every
hardware difference to mathematics.

---

## 11. H17/H18 preliminary prediction before the matched 115K run

The following is a **registered prediction**, not evidence.

### Area

The 22K mapping estimate gives

\[
\frac{26332}{19540}\approx1.35.
\]

Therefore the current fully spatialized H18 presentation is expected to remain
larger in mapped logic than H17-LAB-02 on the matched 115K C7 target, unless
the larger-device mapper finds qualitatively different sharing.

The 1.35 ratio is not predicted as an invariant.

### Timing

No directional timing prediction is frozen.

There are competing effects:

- H18's shared word-prefix DAG has maximum composition depth three;
- all 12 observers are spatialized;
- the compiled adaptive decision structure adds a chain of control selection;
- routing on the much larger device may alter the balance.

Therefore H18-LAB-04 could be faster or slower than H17-LAB-02 despite its
larger area.

This uncertainty is exactly why the matched physical experiment is required.

### Expected interpretation

If H18 is larger but faster, the two presentations occupy different points on
an area-delay Pareto frontier.

If H18 is larger and slower, the current full spatialization is dominated by
H17 for the one-cycle discipline.

If H18 is smaller and/or faster than the 22K estimate suggested, the larger
device has exposed an important technology-mapping interaction and the
technology-relative nature of the ordering becomes central.

---

## 12. Comparing genuinely different mathematics beyond H17/H18

For a future family

\[
M_1,M_2,\ldots,M_k
\]

that solve one finite task, the recommended experiment is:

1. prove/verify common semantics;
2. publish each mathematical factorization explicitly;
3. choose one common realization discipline;
4. generate one HDL artifact per presentation;
5. run the same exact regression;
6. synthesize all with one frozen \(\Theta\);
7. archive pre-map, post-map, fit, and timing reports;
8. build the Pareto set;
9. repeat on at least one second technology stack;
10. distinguish stable ordering from technology-specific ordering.

A stable cross-technology ordering is substantially stronger evidence of a
presentation-level complexity difference than a single-FPGA result.

---

## 13. What this method does and does not measure

It **does** measure:

- the cost of a declared mathematical presentation under a reproducible
  realization discipline and technology;
- relative area/depth/latency induced by alternative mathematical
  factorizations;
- where semantic compression survives or disappears in hardware.

It **does not automatically measure**:

- absolute circuit complexity;
- minimum possible FPGA area;
- minimum possible latency;
- mathematical elegance;
- information-theoretic optimality;
- technology-independent superiority.

Those require separate proofs.

---

## 14. Publication language

Preferred:

> Under a fixed one-cycle realization discipline and matched FPGA/tool flow,
> presentation \(M_2\) maps to X times the logic area and Y times the routed
> latency of presentation \(M_1\).

Avoid:

> \(M_2\) is X times mathematically more complex.

The first is an experimental theorem about a specified map.

The second is undefined without a complexity model.

---

## 15. Current HATTER objective

Use H17/H18 as the first controlled dataset, then deliberately construct
additional mathematically equivalent finite presentations.

The long-term target is to determine which mathematical transformations have
predictable physical leverage and which do not:

\[
\boxed{
\Delta(\text{mathematics})
\longmapsto
\Delta(\text{Boolean structure})
\longmapsto
\Delta(\text{physical structure}).
}
\]
