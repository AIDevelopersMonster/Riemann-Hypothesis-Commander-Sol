# FCOA Nesting & Atomicity — First Theorem Package

**Status:** exploratory theorem package for delegated review.  
Nothing here revises the published M0-G1-G2 checkpoint.

## Theorem 1 — Atomicity monotonicity under sandbox restriction

Let

\[
\mathfrak S_1=(X,\Omega_1,U),\qquad
\mathfrak S_2=(X,\Omega_2,U)
\]

have the same carrier, typing and trivial class, and suppose every allowed cell of `S1` is also an allowed cell of `S2`, with the same value. Then

\[
\operatorname{Dec}^{LR}_{\mathfrak S_1,U}(x)
\subseteq
\operatorname{Dec}^{LR}_{\mathfrak S_2,U}(x)
\]

for every active `x`. Hence

\[
\boxed{\operatorname{Atom}(\mathfrak S_2,U)
\subseteq
\operatorname{Atom}(\mathfrak S_1,U).}
\]

So enlarging the admissible composition family can only destroy atoms; restricting the family can only create atoms.

### Proof

Immediate from inclusion of the two-sided nontrivial decomposition witness sets. `square`

This is the precise sense in which atomicity is sandbox-relative.

## Theorem 2 — Automorphism invariance

Every sandbox automorphism preserves the left-, right-, and bilateral atomic classes, indecomposability, the nontrivial factor graph, and nesting-minimal strongly connected classes.

### Proof

An automorphism bijectively transports each witness

\[
\omega(a,b)=x
\]

to

\[
\omega(g(a),g(b))=g(x),
\]

while preserving membership in `U` and active/terminal sorts. Thus every witness class and every graph edge is transported equivariantly. `square`

## Theorem 3 — Pure carrier-erasure invariance

Under the pure carrier-erasure convention of `DEFINITIONS.md`, all decomposition witness sets remain literally unchanged. Consequently isolation may change only if erased external relations were counted as incidence data, but

\[
\boxed{
\text{indecomposability, left/right/bilateral U-atomicity, U-irreducibility,
and the nontrivial factor graph are invariant.}
}
\]

In particular, losing an external order does not by itself change atomicity when the operation cells remain fixed.

## Theorem 4 — Value-fiber invariance for active-result atomicity

Let two sandboxes have the same active carrier `A`, the same `U`, the same operation domains on active arguments, and the same set of active-result cells. They may differ only by how cells whose results lie in terminal sorts are partitioned among anonymous terminal output values.

Then their atomic classes inside `A` are identical.

### Proof

Atomicity of `x in A` depends only on cells whose result equals `x`. Recoloring or repartitioning cells landing in terminal sorts creates no new witness with active result `x` and destroys none. `square`

### FCOA consequence

G3-style changes of anonymous terminal value fibers can alter automorphism groups, commutation behavior, and Value-Rigidity Index while leaving active-result atomicity unchanged, provided the active-result cells themselves are not modified.

This formally separates **rigidity memory** from **composition-boundary atomicity**.

## Theorem 5 — Atoms versus nesting-minimality in acyclic sandboxes

Assume the nontrivial factor graph `G_{S,U}` is finite and acyclic. Then for every active nontrivial element `x`:

\[
\boxed{
x\text{ is a U-atom}
\iff
x\text{ is minimal in }\preceq_{\mathfrak S,U}.}
\]

### Proof

A U-atom has indegree zero. In a finite DAG, a vertex has no strict predecessor in the transitive closure iff it has indegree zero. Conversely, if `x` has a two-sided nontrivial decomposition witness, one factor contributes an incoming edge from a distinct predecessor because acyclicity excludes a self-loop or directed return path. Thus `x` is not minimal. `square`

### Boundary

Acyclicity is essential. In cyclic sandboxes a strongly connected class may be minimal while every member has an incoming nontrivial decomposition edge.

## Theorem 6 — Cycle obstruction to elementwise minimality

Suppose a strongly connected component `C` of the nontrivial factor graph is minimal in the condensation DAG and contains at least one edge. Then every element of `C` is nesting-minimal in the preorder quotient, but at least one element of `C` is not a U-atom; if every vertex of `C` has internal indegree at least one, no element of `C` is a U-atom.

Thus

\[
\boxed{\text{minimal nesting class}\not\Rightarrow\text{atomic element}.}
\]

The obstruction is cyclic composition, not arithmetic divisibility.

## Theorem 7 — Left/right coincidence under reversal symmetry

Let a sandbox admit an involutive automorphism `rho` of the signature satisfying

\[
\rho(\omega(a,b))=\omega(\rho(b),\rho(a))
\]

for every allowed cell, and suppose `rho(U)=U`.

Then

\[
x\text{ left-U-atomic}
\iff
\rho(x)\text{ right-U-atomic}.
\]

If `rho(x)=x`, left- and right-U-atomicity coincide at `x`.

This is a sufficient symmetry criterion; no commutativity is assumed.

## Theorem 8 — Full operation graph reconstruction of the nesting relation

Given the typed full operation graph, the set `U`, and the distinction between active and terminal sorts, the nontrivial factor relation `triangleleft` is first-order recoverable in the natural incidence language:

`a triangleleft x` iff there exist an allowed operation label `omega` and an active `b notin U` such that either `omega(a,b)=x` or `omega(b,a)=x`, with `a notin U`.

Therefore ordinary divisibility is unnecessary for reconstructing the one-step nesting boundary.

## Theorem 9 — Translation reconstruction under labeled profiles

If the sandbox retains all labeled partial left and right translations, then the same relation is reconstructible from those translations:

\[
a\triangleleft x
\iff
\exists\omega\exists b\notin U
\bigl(L_a^\omega(b)=x\lor R_a^\omega(b)=x\bigr).
\]

However, coarse unlabeled summaries such as translation-domain cardinalities or orbit sizes need not determine atomicity. Separation examples are recorded in `SEPARATION_EXAMPLES.md`.

## Working synthesis

The theorem package supports a sharpened version of the branch thesis:

\[
\boxed{
\text{A U-atom is an indegree-zero point of the nontrivial admissible-composition graph.}
}
\]

When that graph is finite and acyclic, this is exactly a minimal boundary point of the induced nesting order. With cycles, the correct global boundary object is a minimal strongly connected nesting class rather than necessarily an atomic element.

Hence "atomicity is a boundary state" is true only after specifying whether the intended boundary is local witness-boundary or global preorder-boundary.