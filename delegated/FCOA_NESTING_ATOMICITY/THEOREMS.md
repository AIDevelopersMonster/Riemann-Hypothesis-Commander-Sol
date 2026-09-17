# FCOA Nesting & Atomicity — Final Theorem Ledger

**Direction:** `FCOA — SOL-NESTING — Sandbox Atomicity & Composition Boundary`  
**Status:** mathematically closed; publication v1.0 archived at DOI `10.5281/zenodo.22140527`.  
**Authority:** this file supersedes earlier exploratory statements in this branch wherever they conflict with the final publication.

Nothing here revises the published M0-G1-G2 checkpoint.

## T1 — Atomicity monotonicity under sandbox restriction

For sandboxes on the same carrier, typing and trivial class, if every allowed cell of `S1` is also an allowed cell of `S2` with the same value, then

\[
\operatorname{Dec}^{LR}_{S_1,U}(x)\subseteq\operatorname{Dec}^{LR}_{S_2,U}(x)
\]

and therefore

\[
\boxed{\operatorname{Atom}(S_2,U)\subseteq\operatorname{Atom}(S_1,U).}
\]

Expanding admissible composition may destroy atoms but cannot create them.

## T2 — Automorphism invariance

Every sandbox automorphism preserves decomposition witness classes, isolation, indecomposability, directional and bilateral atomicity, the nontrivial factor relation, SCCs, nesting-minimal classes and, when defined, well-founded factor rank.

## T3 — Pure erasure invariance

If an erasure forgets only external labels/orders/relations while preserving carrier, typing, `U`, operation domains and operation values, then all decomposition witnesses are literally unchanged. Hence isolation, indecomposability, atomicity, factor relation, SCCs and well-founded rank are invariant.

## T4 — Terminal value-fiber invariance

If two sandboxes agree on all cells whose results lie in a chosen atomicity target sort, then repartitioning only terminal-output value fibers does not change the atom class on that target sort.

Thus terminal value-fiber rigidity and active-result atomicity are distinct structural coordinates.

## T5 — Local graph characterization

On `X\U`, define

\[
y\triangleleft x
\]

iff `y` occurs as one factor in a two-sided nontrivial decomposition witness with result `x`. Then

\[
\boxed{x\text{ is a bilateral }U\text{-atom}\iff\operatorname{indeg}_{\triangleleft}(x)=0.}
\]

## T6 — Exact local/global nesting boundary

Let `MinNest` be the union of minimal SCCs of the factor graph. Then

\[
\boxed{\operatorname{Atom}\subseteq\operatorname{MinNest}.}
\]

Moreover,

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
}
\]

Global acyclicity is sufficient but not necessary; cycles above the minimal SCC layer are harmless.

## T7 — Finite acyclic corollary

If the nontrivial factor graph is finite and acyclic, then atoms coincide with minimal elements of the induced nesting order.

## T8 — Well-founded ordinal factor rank

If `triangleleft` is well-founded, standard well-founded recursion gives

\[
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}.
\]

Then

\[
\boxed{x\text{ atomic}\iff\rho(x)=0}
\]

and every factor edge strictly raises rank.

The ordinal-rank construction itself is classical; the branch contribution is its application to the sandbox factor relation.

## T9 — U-coherence and transport irreducibility

For arbitrary `U`, atomicity need not coincide with a unit-style irreducibility notion. Under the explicit U-coherence contract:

1. no two-`U`-factor cell produces a nontrivial target;
2. every one-`U`-factor decomposition has its non-`U` cofactor in the same U-transport class as the result;

one has

\[
\boxed{U\text{-atom}\iff U\text{-transport-irreducible}.}
\]

## T10 — Side reversal

A side-reversing anti-automorphism exchanges left- and right-atomicity. At fixed points of the anti-automorphism, left- and right-atomicity coincide. No commutativity is imported.

## T11 — Explicit ordinary quotient convention

For the publication's existential-representative quotient semantics,

\[
\bar\omega(\bar a,\bar b)=\bar z
\]

iff there exist representatives `a,b,z` in the corresponding fibers such that

\[
\omega(a,b)=z.
\]

The congruence/compatibility condition guarantees independence of the resulting quotient class from the chosen witnessing representatives. It does not require every representative pair to lie in the source domain.

## T12 — Exact quotient witness criterion

Under T11, `q(x)` is non-atomic iff there exist `a,b,z` and an operation `omega` with

\[
q(z)=q(x),\qquad \omega(a,b)=z,
\qquad q(a),q(b)\notin\bar U.
\]

## T13 — Fiberwise universal atom criterion

If the quotient reflects triviality,

\[
q^{-1}(\bar U)=U,
\]

then

\[
\boxed{
q(x)\in\operatorname{Atom}(\bar{\mathfrak S},\bar U)
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Thus quotient atomhood is a universal property of the whole result fiber.

## T14 — Ordinary quotients can destroy well-foundedness

Ordinary congruence quotienting does not in general preserve acyclicity, well-foundedness or rank. For example,

\[
a\star b=c,\qquad c\star b=d
\]

is acyclic, while identifying `c\sim d` creates the quotient self-loop

\[
[c]\star[b]=[c].
\]

This is a failure theorem, not an open problem.

## T15 — Safe quotient theorem: bounded factor morphism

Assume:

1. the source factor relation is well-founded;
2. the quotient is operation-compatible;
3. triviality is reflected;
4. the induced map on nontrivial factor frames satisfies the standard bounded-morphism forth and back clauses:

\[
y\triangleleft x\Longrightarrow q(y)\bar\triangleleft q(x),
\]

and

\[
\bar y\bar\triangleleft q(x)
\Longrightarrow
\exists y\in q^{-1}(\bar y):y\triangleleft x
\]

for every nontrivial representative `x`.

Then the quotient factor relation is well-founded and

\[
\boxed{\bar\rho(q(x))=\rho(x)}
\]

for every `x\notin U`. Consequently,

\[
\boxed{x\text{ atomic}\iff q(x)\text{ atomic}.}
\]

This closes the old exploratory obligation that had been left open after the first ordinary-quotient counterexample. The bounded/p-morphism concept itself is standard and is not claimed as novel.

## T16 — Reconstruction from operation data

Given the typed full operation graph and `U`, the one-step factor relation is reconstructed by

\[
a\triangleleft x
\iff
\exists\omega\exists b\notin U
\bigl(\omega(a,b)=x\lor\omega(b,a)=x\bigr),
\]

with all cells legal in the signature and `a\notin U`.

Hence ordinary divisibility is unnecessary for reconstructing nesting.

If all labeled left/right partial translations are retained, the same relation is reconstructible from those translations. Coarse unlabeled statistics such as domain cardinalities or orbit sizes do not determine atom classes in general.

## Final synthesis

The branch theorem package is therefore

\[
\boxed{
\text{atom}=\text{local zero-incoming boundary}
\subseteq
\text{minimal SCC global boundary};
}
\]

\[
\boxed{
\text{well-founded atom}=\text{rank-zero boundary};
}
\]

and under safe quotienting,

\[
\boxed{
\text{triviality reflection + bounded factor morphism}
\Longrightarrow
\bar\rho\circ q=\rho.
}
\]

No unresolved theorem obligation remains from `ROLE_AND_PROMPT.md`. Any stronger question now belongs to a new FCOA direction rather than to silent extension of this closed branch.