# Supervisor Acceptance — Value-Rigidity / Identity-Digraph Result

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Supervisor decision:** **ACCEPT WITH LOCAL PROOF REPAIR; UPSTREAM CANDIDATE**  
**Date:** 29 August 2026

## Accepted scientific core

The subordinate result is accepted as a valid contribution to the FCOA rigidity programme:

1. active-sort Value-Rigidity Index (VRI) separates definedness symmetry from additional symmetry destroyed by value fibers;
2. one anonymous terminal output gives no incremental value-rigidity (`VRI=1`);
3. two anonymous terminal outputs already permit maximal active-sort value-rigidity (`VRI=n!`);
4. minimizing the special value fiber in the complete two-output maximal-rigidity regime reduces exactly to the classical minimum-size identity-digraph problem;
5. the extremal deficit `delta(n)=n-m(n)` is controlled by pairwise nonisomorphic identity oriented-tree components;
6. the exact finite threshold formula, the second-order asymptotic refinement, and the partial-layer phase analysis are mathematically relevant to the rigidity-cost programme.

## Main theorem requested for upstream inclusion

Let `a_k` be the number of nonisomorphic identity oriented trees of order `k`, and define

\[
A_K=\sum_{j\le K}a_j,
\qquad
W_K=\sum_{j\le K}j a_j.
\]

Let `K` be the unique integer satisfying

\[
W_{K-1}\le n<W_K,
\]

and put

\[
q=\left\lfloor\frac{n-W_{K-1}}{K}\right\rfloor.
\]

Then for the minimum number `m(n)` of arcs in an identity digraph on `n` vertices,

\[
\boxed{
\delta(n):=n-m(n)=A_{K-1}+q,
}
\]

and hence

\[
\boxed{
m(n)=n-A_{K-1}-\left\lfloor\frac{n-W_{K-1}}{K}\right\rfloor.
}
\]

### Supervisor status

**Accepted as an upstream theorem in FCOA value-rigidity language, but not as a broad priority claim over classical graph theory.**

Harary–Robinson already established that the minimum-size identity-digraph problem is exactly determined and that `m(n)=n-delta(n)` with `delta(n)=Theta(n/log n)`. Harary–Jacobson explicitly connect the complete-graph orientation problem to minimum identity oriented forests. Therefore the FCOA main line must cite the classical extremal theorem and present the displayed formula as the explicit threshold realization used by the FCOA value-rigidity cost, unless a deeper historical audit establishes independent novelty for the exact threshold expression itself.

## Required proof repair in Theorem 6.1

The current construction says: if the leftover number of vertices is `r>0`, “replace one retained tree component by a longer directed path of a fresh order obtained by adding r vertices.” The idea is correct, but the choice of component must be specified to guarantee that the new path order is not already represented among the retained components.

Use the following explicit construction.

Let

\[
N_0=W_{K-1}+qK,
\qquad
s=n-N_0,
\qquad
0\le s<K.
\]

- If `s=0`, nothing is required.
- If `s>0` and `q>0`, choose one retained order-`K` identity oriented tree and replace it by a directed path of order `K+s`. Since `K+s>K`, this order was not previously used.
- If `s>0` and `q=0`, choose one retained identity oriented tree of order `K-1` (such a tree exists because the directed path is an identity oriented tree for every positive order) and replace it by a directed path of order `K-1+s`. This order is at least `K`, while all retained types have order below `K`, so it is fresh.

In either case the replacement increases both vertices and arcs by exactly `s`; therefore `n-|A|` is unchanged and pairwise nonisomorphism of connected components is preserved.

With this repair, the proof is accepted.

## Upstream inclusion rule

The theorem should be included in the main FCOA scientific synthesis under a section such as

**Exact Value-Rigidity Cost and the Identity-Digraph Bridge**

with the logical chain

\[
\text{two anonymous outputs}
\to
\text{maximal VRI}
\to
\text{minimum special fiber}
\to
m(n)
\to
\text{identity oriented-tree packing}.
\]

It should **not** be inserted into `FCOA Definition 1.0` as a foundational axiom or definition. It is a theorem about a concrete value-rigidity subclass.

## Relation to the director branch

This result is directly relevant to SOL-RIGIDITY because it gives an exact extremal cost for a strong rigidity target in the complete two-output regime. It complements, rather than replaces, the director branch results on:

- low-arity exact reducts;
- sparse component-phase cocycles;
- `lambda`, `mu`, `alpha` repair costs;
- actual cell-extension geometry.

The identity-digraph theorem concerns the cost of constructing a rigid value fiber from scratch; the sparse-phase line concerns the cost of repairing an already given anonymous layer. These are distinct cost problems and should remain separately named.

## Publication recommendation

The subordinate paper is worth publishing as a focused companion article, after:

1. applying the proof repair above;
2. tightening the classical/FCOA novelty boundary;
3. citing the published FCOA foundations and rigidity papers where appropriate;
4. keeping the second-order asymptotic and phase-oscillation claims, but subjecting them to an independent analytic-combinatorics audit before strong novelty language is used.

**Decision:** RESULT ACCEPTED. THEOREM 6.1 ACCEPTED WITH REPAIR. UPSTREAM INCLUSION APPROVED.