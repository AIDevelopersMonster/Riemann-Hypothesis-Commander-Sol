# FCOA Hybrid Memory — Incidence Compiler Leakage Boundary

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem package candidate; internal proof complete modulo standard finite-model-theory locality calibration; hostile audit required  
**Scope:** fixed two-operation incidence compiler from `FIXED_TWO_OPERATION_INCIDENCE_COMPILATION.md`.

## 1. Question

The fixed-two-operation compiler sends a finite bipartite graph

\[
B=(L,R;E)
\]

to the one-sorted partial algebra

\[
\mathcal H(B)=(L\sqcup R\sqcup E;\oplus,\otimes)
\]

with

\[
e\oplus e=\ell(e),
\qquad
e\otimes e=r(e).
\]

The first leakage question is not whether `\mathcal H(B)` can be rigid. It can.

The correct question is:

> What first-order information does the compilation add beyond the input bipartite incidence structure?

The answer is essentially none: the compiler is logically transparent.

## 2. FO recovery of the input graph from the operation pair

Inside `\mathcal H(B)`, define

\[
E^\ast(x)\iff \operatorname{Def}(x\oplus x),
\]

\[
L^\ast(x)\iff \exists e\,(E^\ast(e)\land e\oplus e=x),
\]

\[
R^\ast(x)\iff \exists e\,(E^\ast(e)\land e\otimes e=x).
\]

Because the input graph has no isolated vertices, these formulas recover exactly the edge-elements, left vertices, and right vertices.

Incidence is then defined by

\[
I_L(e,x)\iff E^\ast(e)\land e\oplus e=x,
\]

\[
I_R(e,y)\iff E^\ast(e)\land e\otimes e=y.
\]

Thus the full incidence expansion of `B` is parameter-free FO interpretable in `\mathcal H(B)`.

## 3. FO construction of the operation pair from incidence

Conversely, start with the three-sorted incidence presentation

\[
\widehat B=(L,R,E;I_L,I_R),
\]

where every edge has exactly one left and one right incident endpoint.

The universe of `\mathcal H(B)` is simply the disjoint union of these three sorts. The two operation graphs are first-order definable by

\[
\operatorname{Graph}_\oplus(e,e,x)
\iff E(e)\land L(x)\land I_L(e,x),
\]

and

\[
\operatorname{Graph}_\otimes(e,e,y)
\iff E(e)\land R(y)\land I_R(e,y).
\]

All other triples are outside the operation graphs.

Therefore `\mathcal H(B)` is a definitional/finite-copy FO expansion of the bipartite incidence structure.

## 4. Leakage-Transparency Theorem

### Theorem HM-IL

For any uniformly presented family `\mathcal C` of finite bipartite graphs without isolated vertices, the compiled family

\[
\mathcal H(\mathcal C)=\{\mathcal H(B):B\in\mathcal C\}
\]

and the corresponding incidence family are mutually parameter-free first-order interpretable by fixed formulas.

Consequently any uniformly FO-definable relation or interpretation on one side transfers uniformly to the other, up to the fixed interpretation coordinates.

In particular:

\[
\boxed{
\text{the incidence compiler itself does not have an intrinsic AL level.}
}
\]

Its leakage level is inherited from the chosen input family.

## 5. Consequence: arbitrary bipartite inputs are unsafe by design

If the input class is the class of all finite bipartite graphs, then the compiled two-operation class inherits the full first-order complexity of finite bipartite graph logic.

This is not merely a heuristic warning. Classical finite model theory gives undecidability phenomena already on finite bipartite graphs. Therefore no global statement of the form

\[
\text{“two-operation incidence compilation is below AL0/AL1”}
\]

can be true for unrestricted inputs.

The compiler is a transport mechanism, not a safety mechanism.

## 6. Arithmetic can be compiled if it is present in the input skeleton

Because the compiler preserves the FO information of the input incidence structure, any graph family that uniformly encodes a linear order, EqGap/addition, or a stronger arithmetic structure transfers that information to the operation pair.

Thus the following are all possible **in principle**, depending on the chosen graph family:

\[
\text{below AL0},
\qquad
AL0,
\qquad
AL1,
\qquad
AL2.
\]

No jump is forced solely by the operation format

\[
e\oplus e=\ell(e),
\qquad e\otimes e=r(e).
\]

## 7. The explicit rigid-tree family is a different question

Let `T_m` be the rigid tree family from `FIXED_TWO_OPERATION_INCIDENCE_COMPILATION.md`:

- path `p_0-p_1-\cdots-p_m`;
- an extra path `p_1-q_1-q_2`;
- `m\ge4`.

The tree is rigid because `p_1` is the unique degree-3 vertex and its three branches have pairwise distinct lengths

\[
1,
\quad2,
\quad m-1.
\]

The corresponding operation pair is rigid for every finite `m`.

However, this does **not** imply a uniform FO total order.

## 8. Gaifman-locality obstruction to uniform order

### Theorem HM-T0 — rigid-tree family stays below the order wall

There is no single parameter-free first-order formula

\[
\varphi(x,y)
\]

in the two-operation language that defines a strict total order on the growing principal branch of every compiled `T_m`.

### Proof sketch

The Gaifman graph of the compiled algebra is the incidence graph obtained by joining every edge-element to its left and right endpoint values. Its degree is uniformly bounded.

Fix a candidate formula `\varphi(x,y)`. By standard Gaifman locality for FO on bounded-degree structures, there is a finite radius `r` such that sufficiently separated tuples with the same local neighborhoods cannot be distinguished by `\varphi` except through finitely bounded global local-type counts.

Choose `m` large. On the long branch, choose two vertices `x,y`:

1. both farther than the locality radius from `p_1`, the far endpoint, and the short attached branch;
2. far from one another;
3. of the same bipartition/local parity type;
4. with isomorphic radius-`r` rooted neighborhoods.

Then the ordered tuples `(x,y)` and `(y,x)` have the same relevant local configuration. Hence

\[
\varphi(x,y)\iff\varphi(y,x).
\]

A strict total order must satisfy exactly one of these for distinct `x,y`, contradiction.

Therefore finite rigidity does not yield uniform FO order on this family. `□`

The only external ingredient is the classical locality theorem; the geometric choice of the two points is specific to this family.

## 9. Consequences for AL0 and AL1

The main-line convention defines AL0 by a uniformly FO-definable total order.

Hence the rigid-tree compiled family satisfies

\[
\boxed{
\text{rigid-tree incidence family is below AL0.}
}
\]

This also blocks any uniform canonical rank-addition relation on the long branch if that relation would uniformly recover its order in the usual way. In particular, a rank-addition graph with definable zero would give

\[
x\le y
\iff
\exists z\,\operatorname{Add}(x,z,y),
\]

contradicting HM-T0.

Accordingly no AL1 claim is available for the tree family.

## 10. Rigidity versus logical memory

The tree family gives an important calibration:

\[
\boxed{
\operatorname{Aut}(\mathcal H(T_m))=1
\quad\not\Rightarrow\quad
\text{uniform FO order recovery}.
}
\]

Every finite member is pointwise rigid, but a fixed FO formula cannot exploit arbitrarily long finite distances from the unique branching landmark.

This separates three notions that must not be conflated:

\[
\text{finite rigidity},
\qquad
\text{uniform FO role recovery},
\qquad
\text{uniform arithmetic recovery}.
\]

## 11. Exact leakage classification

The incidence compiler should no longer be assigned one blanket status `QUARANTINED`. The corrected classification is:

### Compiler as a schema

\[
\boxed{
\text{LEAKAGE-TRANSPARENT / input-relative}.
}
\]

It preserves the logical power of the chosen incidence family.

### Arbitrary bipartite input family

\[
\boxed{
\text{UNRESTRICTED / potentially beyond AL2 calibration.}
}
\]

No arithmetic firewall follows from the compiler itself.

### Explicit rigid-tree family

\[
\boxed{
\text{below AL0 despite finite rigidity.}
}
\]

The family carries unbounded combinatorial value-memory but no uniform FO total order.

## 12. Programmatic consequence for FCOA

This produces a clean research boundary:

\[
\boxed{
\text{value-memory capacity}
\ne
\text{arithmetic leakage level}.
}
\]

A fixed pair of operations can have factorially large rigidity amplification and even recover an unbounded rigid graph family while remaining below AL0, provided the recovered graph family itself has the appropriate locality obstruction.

Conversely, the same exact compiler can cross AL0/AL1/AL2 if the input skeleton carries those relations.

Therefore future hybrid branches must audit the **interpreted skeleton class**, not merely count operation cells, outputs, or automorphism collapse.

## 13. Strongest current conclusion

For the SOL-HYBRID programme the new chain is

\[
\boxed{
\text{minimal joint value memory}
\to
\text{scalable carrier-value selection}
\to
\text{fixed-two-operation incidence compilation}
\to
\text{leakage transparency}.
}
\]

The fixed-two-operation mechanism is expressive but neutral: it is a faithful carrier of whatever logical complexity is placed into the value-incidence skeleton.

This is the correct interface back to the main FCOA Arithmetic Leakage programme.
