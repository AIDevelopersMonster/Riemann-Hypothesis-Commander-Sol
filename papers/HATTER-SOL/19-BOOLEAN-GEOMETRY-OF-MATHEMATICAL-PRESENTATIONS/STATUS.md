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


## H19-03 · first E0 source-factorization dataset — CLOSED

Three exact source presentations of the same restricted-12 observer semantics
have now been certified before Boolean synthesis.

### DIRECT12

Independent direct evaluation of every observer word:

\[
\boxed{24\text{ permutation-composition nodes}}
\]

with maximum composition depth

\[
\boxed{3}.
\]

### PREFIX19

Global prefix sharing across the same 12 observers:

\[
\boxed{19\text{ shared composition nodes}}
\]

with the same maximum depth

\[
\boxed{3}.
\]

Thus source-level common-subexpression sharing gives the exact E0 reduction

\[
\boxed{24\to19}
\]

without increasing composition depth.

### NIELSEN12

The ten primitive observers use exact shortest elementary Nielsen programmes
from H18-11. Their aggregate source profile is:

\[
\boxed{
18\text{ shear}
+
3\text{ inverse}
}
\]

elementary Nielsen moves.

The two oriented commutator observers remain direct and require six
permutation compositions in this first mixed presentation.

Hence the exact source resource vector is

\[
\boxed{
(\text{swap}=0,\ \text{inverse}=3,\ \text{shear}=18,\
\text{direct commutator compositions}=6).
}
\]

The scalar mixed step count is 27, but it is **not** interpreted as a Boolean
gate-count or FPGA-area metric because the operation types are heterogeneous.

Shortest-program comparison on primitive words gives seven ties with direct
execution and three labels that require one additional elementary Nielsen move.

### Structural conclusion

\[
\boxed{
\text{semantic / algebraic compression}
\not\Rightarrow
\text{source-operation-count compression}.
}
\]

This is now an exact finite statement for the frozen restricted-12 observer
family.

GitHub Actions run \`35487642123\` verifies the NIELSEN12 source certificate.

## H19-04 · E0 RTL comparison — IN PROGRESS

A common generator now emits

- \`direct12\`,
- \`prefix19\`,
- \`nielsen12\`

with one identical 305-node H18 decision DAG, identical static-erasure
interface, identical input/output register shell, and identical 2561-vector
regression contract.

The immediate gate is:

\[
\boxed{
\text{source factorization}
\to
\text{generic Yosys Boolean image}
}
\]

before any FPGA-specific place-and-route comparison.
