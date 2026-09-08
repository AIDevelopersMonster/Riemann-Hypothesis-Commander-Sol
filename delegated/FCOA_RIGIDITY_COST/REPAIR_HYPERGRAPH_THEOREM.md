# FCOA Rigidity Cost — Repair Hypergraph Audit

**Status:** corrected post-publication research note. The initially proposed singleton-factorization theorem is FALSE in general.

## 1. Setup

Let

\[
B_{\rm old}=A_Q(D,c)\setminus A_{\rm an}(D,c).
\]

For a colored candidate cell `u=(e,b)`, define the singleton kill set

\[
K(u)=\{g\in B_{\rm old}:g\notin\operatorname{Aut}(G;D\cup\{e\},Q_{D\cup\{e\}})\}.
\]

The tempting claim was that a multi-cell extension kills an old bad automorphism iff one selected singleton kills it. This is not correct.

## 2. Exact failure mechanism

An old automorphism `g` preserves `D` setwise. For a singleton extension `D union {e}`, if `g(e) != e`, then `g` cannot preserve that singleton domain and is therefore killed.

But for a multi-cell extension `E`, the same `g` may permute the new cells among themselves:

\[
gE=E.
\]

For example, if `e` is not fixed and

\[
E=\{e,g(e)\},
\]

the singleton `e` kills `g`, and the singleton `g(e)` kills `g`, while the two-cell domain may restore `g` by allowing the two new cells to be exchanged. If the new colors and induced ternary equality data are compatible with that exchange, `g` survives the combined extension.

Thus the implication

\[
\bigl(\exists u\in U:\ u\text{ kills }g\bigr)
\Longrightarrow
U\text{ kills }g
\]

is false in general.

Likewise, survival of the full extension does not imply survival of every singleton extension.

## 3. Safe one-way statement

The following implication is valid:

> If an old automorphism `g` survives every selected singleton extension, then it survives their union.

Indeed singleton survival forces every new ordered cell to be fixed individually by `g`; all old/new comparison data are then preserved in the union, and comparisons between fixed new cells are fixed as well.

Equivalently, by contrapositive:

\[
\boxed{
U\text{ kills }g
\Longrightarrow
\exists u\in U\text{ that kills }g\text{ as a singleton}.
}
\]

The converse is false because several new cells can form a nontrivial `g`-orbit.

## 4. Consequence for beta

Therefore `beta` is **not** in general the transversal number of the singleton kill-set hypergraph.

Every genuine beta-repair must select singleton candidates whose kill sets cover `B_old`, so the singleton cover number gives only a lower bound:

\[
\boxed{
\tau_{\rm sing}(D,c)\le\beta(D,c).
}
\]

The gap measures an old-symmetry **orbit restoration** phenomenon: cells that individually break an old automorphism can collectively restore it by completing a compatible orbit.

This is logically distinct from the later `eta=alpha-beta` phenomenon, where a repair killing all old bad automorphisms creates a genuinely new bad automorphism that did not preserve the old domain.

Hence there are now two possible extension overheads:

1. **old-orbit restoration:** singleton hits do not compose monotonically, producing `beta > tau_sing`;
2. **new-symmetry creation:** a genuine beta-repair is not exact, potentially producing `alpha > beta`.

## 5. Correct exchange object

A correct combinatorial model for beta must retain the action of each old bad automorphism on the whole selected new-cell set.

For `g in B_old`, an extension `(E,b)` kills `g` exactly when at least one of the following occurs:

1. `gE != E`; or
2. `gE=E` but the colored/ternary data on `D union E` are not preserved by `g`.

Thus beta is an **orbit-sensitive repair problem**, not an ordinary hitting-set problem.

The appropriate next object is an orbit-repair system whose constraints are imposed on complete `g`-orbits of missing cells together with their binary color patterns.

## 6. Impact on the Safe-Minimizer programme

This correction does not affect the definitions of `alpha`, `beta`, or `eta`, nor the exhaustive evidence `eta=0` already obtained by direct automorphism computation.

It does invalidate the proposed shortcut through an ordinary repair hypergraph and any matroid-style exchange inference based on that shortcut.

The stronger conjecture

\[
\boxed{\alpha=\beta}
\]

remains open.

The proof programme must now distinguish two levels:

\[
\text{orbit-sensitive destruction of old bad symmetries}
\quad\to\quad
\beta,
\]

followed by

\[
\text{avoidance of newly created bad symmetries}
\quad\to\quad
\alpha.
\]

## 7. Claim firewall

1. No singleton-factorization equivalence is claimed.
2. No exact ordinary-hypergraph formula for beta is claimed.
3. `tau_sing <= beta` is the safe general relation.
4. The finite `eta=0` audits remain valid because they computed beta from actual multi-cell extensions, not from this rejected shortcut.
5. The next target is an orbit-sensitive repair formalism and a Safe-Minimizer theorem inside that formalism.
