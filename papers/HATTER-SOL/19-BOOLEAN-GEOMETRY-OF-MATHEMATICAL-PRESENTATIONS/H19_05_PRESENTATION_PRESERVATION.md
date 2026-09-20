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


## 5. Module-preserving result — CLOSED for DIRECT12/PREFIX19

GitHub Actions run:

\[
\boxed{\texttt{35488321221}}.
\]

All three module-preserved variants pass the same exhaustive

\[
197\times13=2561
\]

transaction E0 regression.

With \`flatten\` removed and declared permutation primitives represented by
retained module instances, the H18 decision/controller shell is common and the
observer-factorization difference remains explicit.

### DIRECT12

Inside \`h18_r12_comb_core\`:

\[
\boxed{
24\ \texttt{h19\_compose\_perm}
+
2\ \texttt{h19\_inverse\_perm}
}
\]

with

\[
\boxed{1591\text{ core cells}}.
\]

### PREFIX19

Inside the same core:

\[
\boxed{
19\ \texttt{h19\_compose\_perm}
+
2\ \texttt{h19\_inverse\_perm}
}
\]

with

\[
\boxed{1586\text{ core cells}}.
\]

Therefore the exact source-level reduction

\[
24\to19
\]

survives one-for-one as five fewer retained primitive instances and five fewer
top-level core cells under \(\Pi_{\rm module}\):

\[
\boxed{
1591\to1586.
}
\]

This should be contrasted with \(\Pi_{\rm open}\), where both presentations
collapsed to

\[
4919
\]

post-proc cells and

\[
63719
\]

post-techmap generic Boolean cells with identical reported cell histograms.

Thus on this controlled pair:

\[
\boxed{
\ker_{cellhist}(C_{\Pi_{\rm module}})
\subsetneq
\ker_{cellhist}(C_{\Pi_{\rm open}})
}
\]

when restricted to the two-presentation family
\(\{DIRECT12,PREFIX19\}\).

Equivalently, the source distinction is invisible under the open cell-histogram
observable but visible under the module-preserving instance-profile observable.

## 6. NIELSEN12 caution

The first module experiment currently decomposes each Nielsen shear into
permutation \`compose\` and, for inverse shears, explicit \`inverse\` modules.
It therefore reports

\[
24\ \texttt{compose}
+
21\ \texttt{inverse}
\]

inside the NIELSEN12 core and 1610 core cells.

This is a valid hardware decomposition but **not yet the canonical
presentation-preserving Nielsen experiment**, because a Nielsen elementary move
is itself the declared mathematical primitive in that presentation.

The next refinement will represent elementary Nielsen moves as retained
primitive modules before comparing the Nielsen presentation against DIRECT12
and PREFIX19.


## 7. Native Nielsen primitive hierarchy — CLOSED

GitHub Actions run:

\[
\boxed{\texttt{35488601863}}
\]

replaces the decomposed compose/inverse surrogate for the primitive part of
NIELSEN12 by retained elementary Nielsen-move modules.

The exact native module profile inside the restricted-12 core is

\[
\boxed{
2\,I_A
+
1\,I_B
+
8\,N_A^{-}
+
2\,N_A^{+}
+
8\,N_B^{-}
}
\]

for a total of

\[
\boxed{21\text{ elementary Nielsen modules}}
\]

on the ten primitive observers.

This matches the source certificate exactly:

\[
\boxed{
18\text{ shear}+3\text{ inversion}=21\text{ moves}.
}
\]

The two non-primitive oriented commutator observers remain direct and contribute

\[
\boxed{6\ \texttt{h19\_compose\_perm}}
\]

instances.  Their inverse letters use the shared

\[
\boxed{2\ \texttt{h19\_inverse\_perm}}
\]

instances for \(A^{-1},B^{-1}\).

All 2561 E0 regression transactions pass.

The complete hierarchical Yosys design contains 6120 cells before flattening,
but this scalar is **not** compared directly with the DIRECT12/PREFIX19
primitive-instance counts as a mathematical cost because native Nielsen
modules and permutation-compose modules are heterogeneous objects.

The result closes the presentation-preserving source/RTL correspondence:

\[
\boxed{
\text{NIELSEN source programme}
\longleftrightarrow
\text{native retained Nielsen module hierarchy}.
}
\]

The next comparison must therefore use either a common lower-level Boolean
observable after releasing hierarchy, or a declared vector-valued primitive
cost model.  No arbitrary unit weight is assigned to unlike mathematical
primitives.
