# FCOA QGE3 — Upstream Memo

**To:** Commander Sol, lead FCOA Rigidity Cost line  
**From:** delegated QGE3 assistant  
**Status:** theorem-level handoff

## 1. Strongest result

The expected sparse multicolor analogue

\[
\text{one connected comparison component}
\Longrightarrow
\text{one local }S_q\text{ phase}
\]

is false for every `q>=3`.

For `q=3` the failure is sharp already at

\[
\boxed{|G|=3,\qquad |D|=4.}
\]

A minimal witness is

\[
D=\{(0,1),(0,2),(1,0),(1,2)\},
\]

with

\[
c(0,1)=c(0,2)=0,
\quad c(1,0)=1,
\quad c(1,2)=2.
\]

The carrier involution `(0 1)` preserves `D` and the ternary equality reduct but maps two cells of source color `0` to different target colors. Hence no local color permutation exists on the unique connected comparison component.

No counterexample is possible with `|D|=3`, since surjectivity onto three colors then makes each color occur exactly once and every domain-preserving cell permutation automatically induces a color permutation.

---

## 2. Correct replacement object

For each comparison component `C`, contract all composability edges whose endpoint cells have equal terminal values. The resulting graph `H_T(C)` has:

- vertices = equality atoms;
- edges = forced inequalities between atoms;
- a proper coloring `kappa_C` induced by the original terminal fibers.

A ternary-reduct automorphism always induces an isomorphism of these quotient graphs and hence transports `kappa_C` to another proper coloring of the same abstract quotient.

Therefore the universally defined local datum is

\[
\boxed{
[\kappa_C^g]
\in \operatorname{Col}(H_T(C))/S_q,
}
\]

not an element of `S_q`.

A local permutation phase exists exactly when the transported coloring lies in the same color-relabeling orbit as the original coloring.

---

## 3. Sector where a nonabelian phase law is valid

If the quotient `H_T(C)` is color-rigid — in particular, uniquely colorable with the number of visible colors — every ternary-reduct automorphism induces a unique visible-support bijection

\[
\phi_{g,C}:O_C\to O_{gC}.
\]

These local phases satisfy the exact noncommutative composition law

\[
\boxed{
\phi_{gh,C}
=\phi_{g,hC}\circ\phi_{h,C}.
}
\]

Thus the correct phase structure is a groupoid of visible-support bijections. It reduces to an `S_q`-valued crossed law when every component sees the full alphabet.

---

## 4. Exact gluing obstruction

Assuming local phases exist on all components, define

\[
R_g=\bigcup_C\operatorname{graph}(\phi_{g,C})\subseteq O\times O.
\]

Then `g` is an automorphism of the full anonymous color layer if and only if

\[
\boxed{R_g\text{ is the graph of one permutation }\pi\in S_O.}
\]

Equivalently:

1. local maps agree on every shared source color;
2. different source colors never collide at the same target color across components.

This yields a complete two-stage exactness criterion for Model T:

\[
\boxed{
\text{local proper-coloring preservation}
+
\text{global phase gluing}.
}
\]

---

## 5. Relation to Article A and Article B

Article A's complete-domain arity transition is respected:

- binary ternary equality is exceptional;
- `q>=3` requires four-ary arbitrary-cell equality for universal exactness.

Article B's binary component cocycle is now explained structurally as the special case where each connected quotient has only one proper 2-coloring orbit. For `q>=3`, the obstruction appears before a group-valued cocycle exists.

No Article A/B claim is modified.

---

## 6. Literature boundary

The quotient invokes classical proper coloring and unique colorability. Gain graphs and multicolor switching provide nearby nonabelian language, but their group labels/switching operations are supplied as part of the structure. Here the permutation phase must be induced from anonymous equality data and can fail to exist.

Therefore any publication claim should be restricted to the FCOA anonymous sparse-operation reconstruction model.

---

## 7. Recommendation

\[
\boxed{\text{MERGE THEOREM INTO MAIN RIGIDITY THEORY}}
\]

The result is strong enough to close the delegated first theorem target: the naive `S_q` phase is disproved sharply and replaced by an exact proper-coloring transport theorem plus a gluing criterion.

A separate short publication is defensible after Commander Sol review, especially if paired with the complete-domain arity transition from Article A as motivation. A broader cost theory should not yet be forced: the natural synchronization unit is no longer one binary phase bit per component, so a multicolor analogue of `lambda` requires a separate optimization theory over proper-coloring orbit constraints.
