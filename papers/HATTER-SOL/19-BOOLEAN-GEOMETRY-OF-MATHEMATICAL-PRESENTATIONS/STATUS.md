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


## H19-04 · compiler forgetting — CLOSED

All three E0 RTL variants pass the same exhaustive 2561-transaction functional
contract.

Under Yosys 0.33

\[
\texttt{proc}\to\texttt{flatten}\to\texttt{opt}
\]

the total cell counts are:

\[
\boxed{
DIRECT12=4919,\qquad
PREFIX19=4919,\qquad
NIELSEN12=5230.
}
\]

Under the further generic Boolean mapping

\[
\texttt{techmap}\to\texttt{opt}
\]

the counts become:

\[
\boxed{
DIRECT12=63719,\qquad
PREFIX19=63719,\qquad
NIELSEN12=72867.
}
\]

DIRECT12 and PREFIX19 have identical reported Boolean-cell histograms despite
the source-level exact difference

\[
24\to19
\]

permutation-composition nodes.

Thus this flow gives the first controlled compiler-forgetting witness:

\[
\boxed{
\text{different source presentation}
\to
\text{same measured optimized Boolean cell histogram}.
}
\]

NIELSEN12 remains distinct and is approximately 14.36% larger than
DIRECT12/PREFIX19 at the post-techmap generic-cell layer.

Claim boundary: this is compiler-relative evidence, not equality of minimum
Boolean circuit complexity.

Detailed record:

- \`H19_04_COMPILER_FORGETTING_RESULT.md\`.

## H19-05 · presentation-preserving compiler discipline — NEXT

Construct a second flow in which declared observer-factorization operations are
explicit module instances with preservation boundaries.

Compare

\[
\Pi_{\rm open}
\quad\text{versus}\quad
\Pi_{\rm preserve}.
\]

The key question is now:

\[
\boxed{
\text{How much hardware difference is hidden by semantic optimization?}
}
\]


## H19-05 · presentation preservation — CLOSED FIRST FAMILY

Two preservation attempts are now distinguished.

### Weak wire preservation

\`(* keep *)\` on intermediate wires did not preserve the source factorization
at the optimized Boolean-cell histogram level.

### Module preservation

Retained mathematical primitive modules preserve the declared factorization.

DIRECT12:

\[
24\,compose+2\,inverse.
\]

PREFIX19:

\[
19\,compose+2\,inverse.
\]

Native NIELSEN12:

\[
21\text{ elementary Nielsen moves}
+
6\text{ direct commutator compositions}
+
2\text{ shared base inversions}.
\]

All three variants pass the common 2561-transaction E0 regression.

The DIRECT12/PREFIX19 pair gives a strict finite compiler-kernel separation:

\[
\ker_{\rm module}
\subsetneq
\ker_{\rm open}
\]

at the declared observables.

Native Nielsen module evidence:

\[
\boxed{\texttt{run 35488601863}}.
\]

## H19-06 · compiler survival tower — ACTIVE

Current survival evidence:

\[
\text{source}
\to
\text{proc/opt}
\to
\text{techmap}.
\]

Next exact measurement:

\[
\boxed{\text{ABC generic logic image}}
\]

for DIRECT12, PREFIX19 and NIELSEN12 under one frozen open flow.

Only after this stage will the first E0 family move to matched Quartus targets.


## H19-LAB-01 · matched Cyclone-V E0 physical family — READY

A parameterized Quartus II 13.1 laboratory has been added for

\[
DIRECT12,\qquad PREFIX19,\qquad NIELSEN12
\]

on the frozen target

\[
\boxed{\texttt{5CEFA7F23C6}}.
\]

All variants use the same:

- generated 305-node decision DAG;
- static persistent-erasure interface;
- registered one-cycle shell;
- 100 MHz reference SDC;
- Slow 1100 mV / 85 C worst-path protocol.

Runner:

\[
\boxed{
\texttt{H19\_LAB\_01\_E0\_CYCLONEV/tools/run\_all\_cyclonev\_a7.ps1}
}
\]

The laboratory is intentionally single-technology first.  No second FPGA
family will be added until the first physical presentation-survival result is
understood.


## H19-07 · non-monotone presentation survival — CLOSED FIRST EXAMPLE

Matched Yosys 0.33 \`abc -fast\` run:

\[
\boxed{\texttt{35489140510}}.
\]

Cell totals:

\[
\boxed{
DIRECT12=60374,\quad
PREFIX19=60383,\quad
NIELSEN12=68406.
}
\]

This is the first H19 re-separation result.

DIRECT12 and PREFIX19 were indistinguishable by complete reported cell
histogram after both

\[
\texttt{proc/opt}
\]

and

\[
\texttt{techmap},
\]

but become distinguishable after \`abc -fast\`.

Therefore presentation survival is not assumed monotone along the compiler
tower:

\[
\boxed{
\text{visible}
\to
\text{hidden}
\to
\text{hidden}
\to
\text{visible}.
}
\]

The source ordering also reverses at this compiler-relative scalar:

\[
19<24
\]

composition nodes for PREFIX19 versus DIRECT12, but

\[
60383>60374
\]

ABC-fast cells.

Detailed record:

- \`H19_07_NONMONOTONE_PRESENTATION_SURVIVAL.md\`.

Next physical gate:

- H19-LAB-01 on 5CEFA7F23C6.
