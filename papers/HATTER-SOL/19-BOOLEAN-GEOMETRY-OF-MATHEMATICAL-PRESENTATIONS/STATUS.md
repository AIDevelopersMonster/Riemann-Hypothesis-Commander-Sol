# HATTER-SOL-19 · STATUS

Branch: \`research/hatter-sol-19-boolean-geometry\`

## Parent state

HATTER-SOL-18 is frozen and publication-ready.

Closed parent evidence includes:

- exact adaptive depth and one-erasure results;
- restricted-12 decision certificate;
- temporal H18-LAB-03 realization;
- spatial H18-LAB-04 realization;
- matched H17/H18 one-cycle FPGA controls;
- H18-12 hardware-image framework;
- H18-13 E0/E1 common-contract boundary.

## H19-01 · formal presentation model — OPENED

Target objects:

\[
M=(X,Y,Q,G,\lambda,\delta,\omega)
\]

for a finite adaptive presentation, with explicit observer labels, response
alphabets, decision DAG, terminal outputs, and encoded semantics.

The first formal distinction is:

\[
\boxed{
\text{query depth}
\neq
\text{Boolean circuit depth}
\neq
\text{transaction latency}.
}
\]

## H19-02 · temporal/spatial compiler theorem — OPENED

Target: exact construction-level formulas for the canonical compiled-DAG
discipline.

No unrestricted circuit lower bound is claimed.

## First controlled E0 family

Use the frozen H18 restricted-12 task and identical external input/fault/output
encoding.

Planned presentations:

1. **DIRECT12** — each word observer realized directly;
2. **PREFIX19** — shared 19-node word-prefix DAG from H18-LAB-04;
3. **NIELSEN12** — observers generated from an explicit Nielsen/SLP basis;
4. **FLAT** — semantics-preserving flattened Boolean control.

The first three are source-structured presentations.  FLAT is the semantic
control.

## H18 closure side branch

\`research/hatter-sol-18-m1-closure\`

Initial strike: test the certified minimum distance-two 9-query alphabet against
the full adaptive one-erasure depth-four contract before launching a global
9/10/11 alphabet search.
