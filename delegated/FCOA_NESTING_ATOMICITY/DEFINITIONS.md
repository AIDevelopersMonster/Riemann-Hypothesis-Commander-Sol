# FCOA Nesting & Atomicity — Definitions

**Status:** hostile-audited definitions, repaired after `HOSTILE_AUDIT_01.md`  
**Branch:** `director/fcoa-nesting-atomicity`  
**Publication boundary:** does not revise Zenodo DOI `10.5281/zenodo.22129787`

## 1. Sandbox and typing

A **composition sandbox** is

\[
\mathfrak S=(X,\Omega,U),
\]

where `X` is the carrier, `Omega` is a declared family of allowed partial binary operations, and `U` is the declared class of trivial elements/results.

The branch passport must also declare the typing already present in the signature. In particular write

\[
X=A\sqcup T
\]

when there is an active argument part `A` and a terminal part `T`.

A terminal element is **not** an admissible factor merely because it lies in `X`; it becomes a factor only if some operation domain explicitly admits it as an argument. Conversely, once such admission is explicit, it must not be omitted from factor analysis merely because it was historically called terminal.

For every `omega in Omega`, let

\[
D_\omega\subseteq X\times X
\]

be its declared partial-operation domain. No associativity, commutativity, identity, cancellation, or closure property is presumed.

Atomicity may be *reported* on a chosen target sort, normally the active nontrivial set

\[
A^\circ=A\setminus U,
\]

but legal factors are drawn from the full signature domains.

## 2. Decomposition witnesses

For `x in X`, define

\[
\operatorname{Dec}_{\mathfrak S}(x)
=
\{(\omega,a,b):\omega\in\Omega,(a,b)\in D_\omega,\ \omega(a,b)=x\}.
\]

A witness is **left-nontrivial** if `a notin U`, **right-nontrivial** if `b notin U`, and **two-sided nontrivial** if both factors lie outside `U`.

Define

\[
\operatorname{Dec}^{L}_U(x)
=
\{(\omega,a,b)\in\operatorname{Dec}(x):a\notin U\},
\]

\[
\operatorname{Dec}^{R}_U(x)
=
\{(\omega,a,b)\in\operatorname{Dec}(x):b\notin U\},
\]

and

\[
\operatorname{Dec}^{LR}_U(x)
=
\{(\omega,a,b)\in\operatorname{Dec}(x):a,b\notin U\}.
\]

These are directional notions and need not agree.

## 3. Isolation, indecomposability, and atoms

An element `x` is **isolated** if it occurs in no allowed operation cell at all, neither as argument nor as result.

It is **indecomposable** if

\[
\operatorname{Dec}_{\mathfrak S}(x)=\varnothing.
\]

For a declared nontrivial atomicity target element `x`:

- `x` is **left-U-atomic** if `Dec^L_U(x)=emptyset`;
- `x` is **right-U-atomic** if `Dec^R_U(x)=emptyset`;
- `x` is a **bilateral U-atom**, or simply a **U-atom**, if

\[
\boxed{\operatorname{Dec}^{LR}_U(x)=\varnothing.}
\]

Thus a U-atom is not obtainable by one allowed cell whose two factors are both nontrivial relative to `U`.

Always

\[
\text{isolated}\Longrightarrow\text{indecomposable}\Longrightarrow U\text{-atom},
\]

with no converse in general.

## 4. Trivial-factor transport and the irreducibility firewall

A declaration `u in U` does not make `u` a unit.

For `y,z in X`, write

\[
y\to_U z
\]

if some `u in U`, some `omega in Omega`, and a legal cell satisfy either

\[
\omega(u,y)=z
\quad\text{or}\quad
\omega(y,u)=z.
\]

Let `leadsto_U` be its reflexive-transitive closure and define

\[
y\asymp_U z
\iff
 y\leadsto_U z\ \text{and}\ z\leadsto_U y.
\]

A decomposition `omega(a,b)=x` is **U-transport-inessential** if exactly one factor lies in `U` and the other factor is U-associated with `x`.

A nontrivial element `x` is **U-transport-irreducible** if every decomposition witness of `x` is U-transport-inessential.

The unqualified shorthand **U-irreducible** is not used unless the sandbox explicitly satisfies the following **U-coherence contract**:

1. no cell with both factors in `U` produces a nontrivial atomicity-target result;
2. every one-U-factor decomposition of a nontrivial atomicity-target result has its non-U cofactor U-associated with that result.

Under U-coherence,

\[
\boxed{
U\text{-atom}\iff U\text{-transport-irreducible}.
}
\]

An optional **trivial-realization axiom** may additionally require every nontrivial target element to admit at least one one-U-factor decomposition. That axiom is useful for comparison with ordinary units but is not part of abstract atomicity.

## 5. Nontrivial factor graph

Let

\[
N=X\setminus U.
\]

The directed **nontrivial factor graph**

\[
\mathcal G_{\mathfrak S,U}
\]

has vertex set `N`. Every two-sided nontrivial witness

\[
\omega(a,b)=x
\]

contributes the edges

\[
a\to x,\qquad b\to x.
\]

Write

\[
y\triangleleft x
\]

when such an edge exists.

The reflexive-transitive closure

\[
\preceq_{\mathfrak S,U}
\]

is a preorder. Its quotient by mutual reachability is the condensation poset of strongly connected nesting classes.

An element `x` is **nesting-minimal** if its SCC is minimal in that condensation poset.

A U-atom is exactly a vertex of indegree zero in this repaired graph. Every U-atom is nesting-minimal. The converse can fail only inside a minimal SCC carrying an internal edge.

## 6. Well-founded factor rank

If `triangleleft` is well-founded, define its canonical ordinal rank by

\[
\boxed{
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}.
}
\]

Then

\[
\boxed{x\text{ is a U-atom}\iff\rho(x)=0}
\]

for every declared atomicity-target element.

The ordinal rank construction for well-founded relations is classical; this branch only applies it to the sandbox factor relation.

## 7. Sandbox automorphisms and side reversal

A **sandbox automorphism** is a bijection preserving the declared sorts, `U`, every operation domain, and every operation value.

A **side-reversing anti-automorphism** is a bijection `rho` preserving sorts and `U` and satisfying

\[
\rho(\omega(a,b))=\omega(\rho(b),\rho(a))
\]

on every allowed cell. Such a map exchanges left- and right-atomicity.

Anonymous terminal outputs may be permuted when the signature permits it. No external order or index naming is part of the sandbox unless explicitly retained.

## 8. Pure carrier erasure

A **pure carrier erasure** deletes only external names, labels, orders, or relations while leaving unchanged:

1. carrier elements;
2. typing;
3. `U`;
4. all allowed operation cells and values.

Therefore it preserves literally every operation-incidence and decomposition witness. Consequently it preserves isolation, indecomposability, all atomicity notions, U-transport-irreducibility, the factor graph, SCCs, and any well-founded factor rank.

A quotient or identification of carrier points is not a pure erasure.

## 9. Quotient / carrier identification

Let

\[
q:X\twoheadrightarrow\bar X
\]

be a sort-respecting quotient map compatible with the partial operations, and let

\[
\bar U=q(U).
\]

The quotient may change atomicity because distinct result or factor fibers are identified.

Call the quotient **triviality-reflecting** if

\[
\boxed{q^{-1}(\bar U)=U.}
\]

Under this hypothesis, quotient factor classes are nontrivial exactly when their representatives are nontrivial.

For ordinary congruence quotients with existential representative semantics, one then has

\[
\boxed{
q(x)\text{ is a quotient U-atom}
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Thus atomicity is preserved pointwise exactly when atomhood is constant on each quotient result fiber.

Without triviality reflection, quotient identification may manufacture atoms by collapsing a formerly nontrivial factor into the trivial class.

Ordinary quotienting also need not preserve well-foundedness or factor rank; stronger definedness-saturated quotient hypotheses would be required for such a theorem.

## 10. Operation-graph reconstruction

The repaired nontrivial factor graph is reconstructible from the full labeled operation graph plus `U` without importing divisibility.

Equivalently, if labeled left and right translations are retained,

\[
L_a^\omega(b)=\omega(a,b),\qquad
R_b^\omega(a)=\omega(a,b),
\]

then the one-step relation `triangleleft` is recoverable by testing whether a nontrivial cofactor combines with `a` to produce the target.

Coarse unlabeled translation-cardinality summaries remain insufficient in general.