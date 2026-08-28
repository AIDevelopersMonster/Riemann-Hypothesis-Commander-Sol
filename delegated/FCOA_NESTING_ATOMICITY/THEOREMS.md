# FCOA Nesting & Atomicity — Repaired Theorem Package

**Status:** hostile-audited with repairs.  
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

for every target element `x`. Hence

\[
\boxed{\operatorname{Atom}(\mathfrak S_2,U)
\subseteq
\operatorname{Atom}(\mathfrak S_1,U).}
\]

So enlarging admissible composition can only destroy atoms; restricting it can only create atoms.

## Theorem 2 — Automorphism invariance

Every sandbox automorphism preserves isolation, indecomposability, left/right/bilateral atomicity, U-transport-irreducibility, the repaired nontrivial factor graph, SCCs, and nesting-minimal classes.

### Proof

Every decomposition witness

\[
\omega(a,b)=x
\]

is transported bijectively to

\[
\omega(g(a),g(b))=g(x),
\]

while `U` and typing are preserved. Therefore every witness class and graph edge is transported equivariantly. `square`

## Theorem 3 — Pure carrier-erasure invariance

Under the pure carrier-erasure convention, every operation cell and every decomposition witness is literally unchanged. Consequently

\[
\boxed{
\text{isolation, indecomposability, atomicity, transport-irreducibility,}
\text{factor graph, SCCs and well-founded rank are invariant.}
}
\]

Losing an external order can therefore increase automorphism symmetry without changing composition-boundary atomicity.

## Theorem 4 — Terminal value-fiber invariance for active-result atomicity

Let two sandboxes have the same carrier, `U`, operation domains, and the same set of cells whose results lie in the chosen atomicity-target sort. They may differ only in how cells landing in terminal output sorts are partitioned among anonymous terminal values.

Then their atom classes on the target sort are identical.

### Proof

Atomhood of `x` depends only on two-sided nontrivial cells whose result is `x`. Repartitioning terminal-output fibers changes no such witness. `square`

Thus rigidity memory carried by terminal values is orthogonal to active-result atomicity under this hypothesis.

## Theorem 5 — Atom implies global nesting minimality

For every sandbox and every target element `x`:

\[
\boxed{x\text{ is a U-atom}\Longrightarrow x\text{ is nesting-minimal}.}
\]

### Proof

If `x` were not nesting-minimal, then in the condensation poset there would be a strictly lower SCC with a directed path into the SCC of `x`. The final edge entering the SCC of `x` is an incoming nontrivial factor edge into some element of that SCC. If `x` is a singleton SCC with no internal path back, this contradicts indegree zero immediately; more generally an atom cannot lie in a nontrivial SCC because strong connectivity gives it an incoming internal edge, and a self-loop also gives indegree. Therefore an atom lies in an edge-free singleton SCC with no incoming condensation edge, hence is nesting-minimal. `square`

## Theorem 6 — Exact minimal-SCC criterion

Let `MinNest` be the set of all elements lying in minimal SCCs of the nontrivial factor graph. Then

\[
\operatorname{Atom}\subseteq\operatorname{MinNest}.
\]

Moreover

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
}
\]

### Proof

A minimal SCC that is an edge-free singleton has no incoming edge from another SCC by minimality and no internal edge by hypothesis, so its unique vertex has indegree zero and is an atom.

Conversely, if a minimal SCC contains at least two vertices, strong connectivity gives every vertex an internal incoming edge. If it is a singleton with a self-loop, that loop is an incoming edge. Hence such a component contains no atoms. `square`

### Consequence

Global acyclicity is sufficient but not necessary for atom/minimal equality. Cycles strictly above the minimal condensation layer are harmless.

## Theorem 7 — Finite acyclic corollary

If the repaired nontrivial factor graph is finite and acyclic, then

\[
\boxed{x\text{ is a U-atom}\iff x\text{ is minimal in the nesting order}.}
\]

This is now a corollary of Theorem 6, not the sharp boundary theorem.

## Theorem 8 — Well-founded ordinal factor rank

Assume the one-step factor relation `triangleleft` on `X\U` is well-founded. Then there is a unique ordinal rank

\[
\boxed{
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}.
}
\]

For every declared target element,

\[
\boxed{x\text{ is a U-atom}\iff\rho(x)=0.}
\]

And every factor edge strictly raises rank:

\[
y\triangleleft x\Longrightarrow\rho(y)<\rho(x).
\]

### Proof

Existence and uniqueness of the ordinal recursion are the standard well-founded recursion theorem. Rank zero is equivalent to having no predecessors under `triangleleft`, which is exactly bilateral U-atomicity. `square`

### Claim boundary

The ordinal-rank theorem for well-founded relations is classical. The branch claim is only its application to the admissible-composition factor relation.

## Theorem 9 — U-coherence collapses atom and transport-irreducible

Assume the U-coherence contract:

1. no two-U-factor cell produces a nontrivial target result;
2. every one-U-factor decomposition of a nontrivial target `x` has its non-U cofactor U-associated with `x`.

Then

\[
\boxed{
x\text{ is a U-atom}
\iff
x\text{ is U-transport-irreducible}.}
\]

### Proof

If `x` is an atom, every decomposition has at least one U-factor. Clause 1 excludes both factors lying in U, so exactly one lies in U; Clause 2 makes that witness transport-inessential. Thus `x` is transport-irreducible.

Conversely, a transport-irreducible element has only witnesses with exactly one U-factor, so it has no two-sided nontrivial witness and is atomic. `square`

This theorem replaces the earlier unconditional use of the word irreducible.

## Theorem 10 — Side-reversal exchanges directional atomicity

Let `rho` be a side-reversing anti-automorphism satisfying

\[
\rho(\omega(a,b))=\omega(\rho(b),\rho(a)),
\qquad \rho(U)=U.
\]

Then

\[
\boxed{x\text{ left-U-atomic}\iff\rho(x)\text{ right-U-atomic}.}
\]

If `rho(x)=x`, left- and right-U-atomicity coincide at `x`.

No commutativity is assumed.

## Theorem 11 — Exact quotient atom criterion

Let

\[
q:X\twoheadrightarrow\bar X
\]

be a sort-respecting ordinary congruence quotient of the partial operations, interpreted by existential representatives, and let

\[
\bar U=q(U).
\]

Then for any `x`:

\[
q(x)\text{ is non-atomic}
\]

iff there exist representatives `a,b,z` and an operation `omega` such that

\[
q(z)=q(x),\qquad \omega(a,b)=z,
\]

and both quotient factor classes are nontrivial:

\[
q(a),q(b)\notin\bar U.
\]

This is the exact witness-lifting description for quotient atomicity.

## Theorem 12 — Fiberwise universal criterion under triviality reflection

Assume additionally that the quotient is triviality-reflecting:

\[
\boxed{q^{-1}(\bar U)=U.}
\]

Then

\[
\boxed{
q(x)\in\operatorname{Atom}(\bar{\mathfrak S},\bar U)
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

### Proof

By triviality reflection,

\[
q(a)\notin\bar U\iff a\notin U.
\]

Thus a quotient two-sided nontrivial witness for `q(x)` exists exactly when some representative result `z` in the fiber of `x` has an original two-sided nontrivial witness. Negating gives the formula. `square`

### Consequences

Under triviality reflection:

- quotienting cannot create an atom from a composite representative;
- quotienting can destroy an atom if its result fiber also contains a composite representative;
- pointwise atomhood is preserved iff atomhood is constant on quotient fibers.

Without triviality reflection, a quotient may create atoms by collapsing a formerly nontrivial factor into `bar U`.

## Theorem 13 — Ordinary quotients do not preserve well-foundedness

There is no general theorem saying an ordinary congruence quotient preserves the factor DAG or ordinal rank.

Counterexample: with `U=emptyset`, take

\[
a\star b=c,
\qquad
c\star b=d.
\]

The original factor graph is acyclic. Identifying `c sim d` yields

\[
[c]\star[b]=[c],
\]

so the quotient graph contains a self-loop and is not well-founded.

Hence rank preservation requires a stronger quotient contract and remains open in this branch.

## Theorem 14 — Full operation-graph reconstruction

Given the typed full operation graph and `U`, the repaired one-step relation is recoverable by

\[
a\triangleleft x
\iff
\exists\omega\exists b\notin U
\bigl(\omega(a,b)=x\lor\omega(b,a)=x\bigr),
\]

with `a notin U` and all cells required to be legal in the signature.

Ordinary divisibility is unnecessary.

## Theorem 15 — Labeled translation reconstruction

If all labeled left/right partial translations are retained, then `triangleleft` is reconstructible from them. Coarse unlabeled statistics such as domain cardinalities or orbit sizes do not determine atom classes in general.

## Repaired synthesis

The hostile audit replaces the first slogan by the exact hierarchy

\[
\boxed{
\text{U-atom}
=
\text{zero-incoming local composition boundary}
\subseteq
\text{minimal condensation boundary}.
}
\]

Equality holds exactly when every minimal SCC is an edge-free singleton.

When the factor relation is well-founded, the same local boundary is rank zero of the canonical ordinal factor rank.

Under quotient identification, atomhood is not invariant; with triviality reflection it becomes a fiberwise universal property.