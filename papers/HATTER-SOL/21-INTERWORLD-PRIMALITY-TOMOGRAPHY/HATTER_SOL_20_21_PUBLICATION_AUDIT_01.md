# HATTER-SOL 20–21 · PUBLICATION AUDIT 01

Status: **MANUSCRIPT v0.1 AUDITED / CLAIM SET FROZEN**

Date: 2026-09-22

## 1. Audit object

Audited draft:

\[
\texttt{HATTER\_SOL\_20\_21\_MANUSCRIPT\_DRAFT.md}
\]

Claim matrix:

\[
\texttt{HATTER\_SOL\_20\_21\_CLAIM\_MATRIX.md}
\]

Publication decision:

\[
\texttt{PUBLICATION\_DECISION.md}
\]

The audit checks:

- mathematical dependency;
- empirical/theorem separation;
- hardware claim discipline;
- novelty boundaries;
- reproducibility;
- H20/H21 narrative coherence.

## 2. Central claim survives audit

The manuscript's central claim is acceptable in the following bounded form:

> Equivalent finite arithmetic presentations can produce measurably different
> physical FPGA realizations under matched flows; for the declared H21
> quadratic-world family, the algebraic condition \(B=0\) gives an exact
> semantics-preserving lowering to a scalar Euler-Jacobi datapath, and the
> resulting matched implementation has a substantial measured advantage on the
> tested Cyclone V target.

This claim is supported by two logically distinct layers:

### H20 empirical precursor

\[
D_W\equiv B_W\equiv L_W
\]

under formal semantic equivalence, while synthesis/P&R observers separate the
presentations.

### H21 constructive theorem + implementation

\[
B=0
\Rightarrow
x^n=C^{(n-1)/2}x
\]

and therefore the generic quadratic observer can be lowered exactly to a scalar
observer with the same factor-gcd semantics.

## 3. Classical ingredients that must remain explicitly non-novel

The manuscript must continue to label the following as classical:

- Euler's criterion;
- Jacobi symbols;
- Solovay-Strassen / Euler-Jacobi probable-prime testing;
- Lucas probable-prime machinery;
- Frobenius probable-prime machinery;
- hardware specialization / partial evaluation;
- standard SAT equivalence checking;
- standard FPGA synthesis / place-and-route metrics.

No sentence may imply that H20–H21 introduces these ingredients.

## 4. H20 claim discipline

### Allowed

- formal equivalence for \(W=4,\dots,10\);
- structural separation under the declared Yosys/ABC flow;
- two-vendor resource-class separation;
- backend-dependent finite-width BALANCED/LINEAR crossover;
- vector-valued physical observer conclusion.

### Not allowed

- asymptotic circuit-complexity claims;
- universal crossover widths;
- global circuit optimality;
- prime-specific invariant claims from H20-EXT;
- statements implying H20 proved a number-theoretic theorem.

H20-EXT must remain a negative/falsification note.

## 5. H21 claim discipline

### Exact theorem layer

The following may be called exact results:

\[
x^n=C^{(n-1)/2}x
\]

for canonical \(B=0\) worlds, and the induced defect/gcd equivalence.

The theorem is algebraically elementary but operationally decisive because the
compiler predicate \(B=0\) is available directly from the descriptor.

### Implementation layer

LAB-27 and LAB-28 are measurements, not theorems.

The device-specific result is:

\[
215\text{ vs }328\ \mathrm{ALMs},
\]

\[
251\text{ vs }455\ \mathrm{registers},
\]

\[
157.33\text{ vs }123.20\ \mathrm{MHz},
\]

\[
9.5852\times
\]

quadratic/scalar ALM-latency ratio in the declared matched architecture.

The phrase "9.5852x improvement" must always carry a device/architecture
qualifier nearby.

## 6. Timing limitation

LAB-28 is suitable for an internal clock-domain comparison, not board-level
sign-off.

The manuscript must preserve the limitation that:

- exact pins were not assigned;
- full external I/O constraints were not supplied;
- no power/energy claim is made;
- Fmax is used comparatively within the matched flow.

This does not invalidate the core-comparison result.

## 7. H20–H21 narrative audit

The combined numbering is justified.

H20 is not a missing paper number and is not being retroactively upgraded.

Its function in the combined paper is:

\[
\boxed{
\text{empirical discovery that presentation remains physically observable}.
}
\]

H21 then supplies:

\[
\boxed{
\text{an exact rule for choosing an equivalent presentation from algebraic
structure}.
}
\]

This is a coherent technical dependency, not merely historical packaging.

## 8. Novelty wording

Use:

> Our targeted literature audit did not identify a direct analogue of the
> complete descriptor-to-specialization-to-matched-FPGA chain.

Do not use:

- first;
- unprecedented;
- unique;
- novel primality test;
- optimal architecture.

The novelty claim belongs to the **composition and validated compiler chain**,
not to the classical arithmetic primitives.

## 9. Reproducibility gate

Before archival release, freeze:

1. exact repository commit;
2. H20 generated RTL and formal scripts;
3. H20 Cyclone V and Gowin reports;
4. H21 LAB-27 RTL and CI artifacts;
5. H21 LAB-28 Quartus reports;
6. compiler/tool versions;
7. command lines used for the decisive laboratories.

No numerical table should survive into the final paper unless its source file
is in the frozen bundle.

## 10. Remaining editorial blockers

The scientific claim set has no blocking contradiction.

Remaining pre-release items are editorial/reproducibility items:

- author list and affiliations;
- final repository commit hash;
- final bibliography formatting;
- figure generation;
- final PDF typography;
- independent reviewer pass.

## 11. Audit decision

\[
\boxed{\text{SCIENTIFIC CLAIM SET: PASS}}
\]

\[
\boxed{\text{MANUSCRIPT v0.1: READY FOR PUBLICATION HARDENING}}
\]

The manuscript should now be edited conservatively rather than expanded with
new exploratory H21 results.
