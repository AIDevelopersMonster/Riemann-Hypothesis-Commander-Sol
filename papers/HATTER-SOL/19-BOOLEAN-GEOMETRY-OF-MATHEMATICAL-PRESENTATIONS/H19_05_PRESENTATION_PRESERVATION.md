# H19-05 · Presentation-Preserving Compilation

Status: **OPEN / first weak control closed negative**

## 1. Weak preservation control

The first control marked declared word-factorization intermediates with Yosys

\`\`\`verilog
(* keep *)
\`\`\`

attributes while retaining the same flattened compilation flow.

For DIRECT12 and PREFIX19 this changed neither the post-proc cell count nor the
post-techmap Boolean cell histogram:

\[
4919 \leftrightarrow 4919,
\]

\[
63719 \leftrightarrow 63719.
\]

Therefore wire-level keep attributes do **not** define a sufficiently strong
presentation-preserving realization discipline for this experiment.

This is a useful negative result:

\[
\boxed{
\texttt{keep wire}
\not\Rightarrow
\text{preserved mathematical factorization}.
}
\]

The optimizer may retain named nets while still rewriting the logic that
computes them.

## 2. Stronger discipline

Define \(\Pi_{\rm module}\) by promoting each declared mathematical primitive
instance to a module boundary.

For the first H19 family:

- each permutation composition is one \`h19_compose_perm\` instance;
- each permutation inversion is one \`h19_inverse_perm\` instance;
- module hierarchy is retained through the presentation-sensitive measurement;
- the 12 class observers and 305-node decision DAG remain common across all
  variants;
- input/output/fault semantics remain E0-identical.

The structural instance count is then an exact compiler-visible reflection of
the source presentation before any optional hierarchy collapse.

## 3. Required comparison

Measure two flows.

### Open flow

\[
\Pi_{\rm open}:
\text{flatten}\to\text{opt}\to\text{techmap}.
\]

### Module-preserving flow

\[
\Pi_{\rm module}:
\text{preserve primitive instances}\to
\text{opt within modules}\to
\text{hierarchical stat}.
\]

A later third flow may flatten the already-measured module-preserving netlist
to ask how quickly the distinction disappears.

## 4. Claim boundary

The module boundary is a declared experimental discipline, not a claim that
mathematics has a unique hardware modularization.

Its purpose is precisely to make the comparison question well-posed:

\[
\boxed{
\text{what hardware image follows if the compiler is required to respect the
declared mathematical primitive boundaries?}
}
\]
