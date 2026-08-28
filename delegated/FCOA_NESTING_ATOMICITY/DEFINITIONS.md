# FCOA Nesting & Atomicity — Definitions

**Status:** exploratory delegated branch  
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

when there is an active argument part `A` and a terminal part `T`. An element of `T` is **not** an admissible factor unless some operation domain explicitly admits it as an argument.

For every `omega in Omega`, let

\[
D_\omega\subseteq X\times X
\]

be its declared partial-operation domain. No associativity, commutativity, identity, cancellation, or closure property is presumed.

Atomicity below is primary on the active nontrivial set

\[
A^\circ=A\setminus U.
\]

If a different result sort is to carry an atomicity notion, it must be declared explicitly in that sandbox passport.

## 2. Decomposition witnesses

For `x in X`, define the incoming decomposition set

\[
\operatorname{Dec}_{\mathfrak S}(x)
=
\{(\omega,a,b):\omega\in\Omega,(a,b)\in D_\omega,\ \omega(a,b)=x\}.
\]

A witness is **left-nontrivial** if `a notin U`, **right-nontrivial** if `b notin U`, and **two-sided nontrivial** if both factors lie outside `U`.

Define

\[
\operatorname{Dec}^{L}_U(x)=
\{(\omega,a,b)\in\operatorname{Dec}(x):a\notin U\},
\]

\[
\operatorname{Dec}^{R}_U(x)=
\{(\omega,a,b)\in\operatorname{Dec}(x):b\notin U\},
\]

and

\[
\operatorname{Dec}^{LR}_U(x)=
\{(\omega,a,b)\in\operatorname{Dec}(x):a,b\notin U\}.
\]

These are directional notions. In a noncommutative or merely partial sandbox they need not agree.

## 3. Isolation, indecomposability, and atoms

An element `x` is **isolated** if it occurs in no allowed operation cell at all: neither as an argument nor as a result.

It is **indecomposable** if

\[
\operatorname{Dec}_{\mathfrak S}(x)=\varnothing.
\]

For `x in A^circ`:

- `x` is **left-U-atomic** if `Dec^L_U(x)=emptyset`;
- `x` is **right-U-atomic** if `Dec^R_U(x)=emptyset`;
- `x` is a **bilateral U-atom**, or simply a **U-atom** in this branch, if

\[
\boxed{\operatorname{Dec}^{LR}_U(x)=\varnothing.}
\]

Thus a U-atom is not obtainable by one allowed cell whose two active factors are both nontrivial relative to `U`.

Immediate implications are

\[
\text{isolated}\Longrightarrow\text{indecomposable}\Longrightarrow U\text{-atom},
\]

while neither converse is automatic.

## 4. Trivial-factor transport and irreducibility

The chosen set `U` need not behave like a unit group. To avoid silently importing ordinary monoid theory, define its actual transport behavior from the sandbox.

For active elements `y,z in A`, write

\[
y\to_U z
\]

if some `u in U cap A` and some `omega in Omega` satisfy either

\[
\omega(u,y)=z
\quad\text{or}\quad
\omega(y,u)=z.
\]

Let `leadsto_U` be the reflexive-transitive closure of `to_U`, and define **U-association** by mutual reachability:

\[
y\asymp_U z
\iff
y\leadsto_U z\ \text{and}\ z\leadsto_U y.
\]

A decomposition `omega(a,b)=x`, with `x in A^circ`, is **U-inessential** if exactly one factor lies in `U`, the other lies outside `U`, and the non-U factor is U-associated with `x`.

An element `x in A^circ` is **U-irreducible** if every decomposition witness of `x` is U-inessential.

Hence

\[
U\text{-irreducible}\Longrightarrow U\text{-atom}.
\]

The converse requires additional unit-like behavior of `U`; it is not built into the definition.

This distinction is deliberate: `U` is a sandbox declaration, not automatically a set of algebraic units.

## 5. Nontrivial factor graph

Define the directed **nontrivial factor graph**

\[
\mathcal G_{\mathfrak S,U}
\]

on vertex set `A^circ` as follows. Every two-sided nontrivial witness

\[
\omega(a,b)=x
\]

contributes directed edges

\[
a\to x,\qquad b\to x.
\]

Write

\[
y\triangleleft x
\]

when there is such an edge. The raw relation `triangleleft` need not be transitive and need not be antisymmetric.

Its reflexive-transitive closure

\[
\preceq_{\mathfrak S,U}
\]

is always a preorder. The quotient by mutual reachability is therefore a poset of strongly connected nesting classes.

An element `x` is **nesting-minimal** if its strongly connected class is minimal in this quotient poset; equivalently,

\[
y\preceq x\Longrightarrow x\preceq y.
\]

A U-atom is exactly a vertex of indegree zero in the nontrivial factor graph. Nesting-minimality is weaker in the presence of cycles.

## 6. Sandbox automorphisms

A **sandbox automorphism** is a bijection of `X` preserving all declared sorts, the subset `U`, every operation domain, and every operation value:

\[
g(\omega(a,b))=\omega(g(a),g(b))
\]

whenever the left side is defined.

Anonymous terminal outputs may be permuted when the signature permits it. No external order or index naming is part of the sandbox unless explicitly retained.

## 7. Carrier-erasure convention

A **pure carrier erasure** for this branch is a forgetful reduct that deletes external names, labels, orders, or relations while leaving unchanged:

1. the carrier elements;
2. active/terminal typing;
3. `U`;
4. all allowed operation cells and their values.

Such an erasure cannot change decomposition witnesses and therefore cannot change U-atomicity.

More general quotients or identifications are not called pure erasure here; they require a separate composition-reflection test because they can create or destroy decomposition witnesses.

## 8. Operation-graph reconstruction

The nontrivial factor graph is reconstructible from the full labeled operation graph plus `U` without importing divisibility.

Equivalently, if all labeled left and right translations are retained,

\[
L_a^\omega(b)=\omega(a,b),\qquad
R_b^\omega(a)=\omega(a,b),
\]

then

\[
a\triangleleft x
\]

is recoverable by asking whether some nontrivial cofactor maps with `a` to `x` under an allowed translation.

Unlabeled translation-cardinality summaries are weaker and need not determine the atom classes.
