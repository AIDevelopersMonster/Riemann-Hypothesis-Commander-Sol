# FCOA QGE3 — Multicolor Cost Theory

**Branch:** `director/fcoa-rigidity-cost`  
**Status:** structural cost note  
**Scope:** abstract synchronization after local phase existence; no claim about exact real-cell extension cost

## 1. Why the binary cost cannot be copied verbatim

For binary sparse layers, a connected comparison component carries one bit of phase, and equality of one phase bit between two components synchronizes them.

For `q>=3`, two new phenomena intervene:

1. a local phase may not exist at all because Model T may transport the hidden proper coloring to an inequivalent coloring;
2. when local phases do exist, they are permutations or partial visible-support bijections, and one pointwise agreement need not determine the whole permutation.

Therefore a multicolor cost theory must separate:

\[
\boxed{
\text{local color-partition repair}
\quad\text{from}\quad
\text{inter-component phase synchronization}.
}
\]

Only the second layer is developed here.

---

## 2. Full-support phase sector

Assume every comparison component sees the full alphabet:

\[
O_C=O,
\qquad |O|=q,
\]

and every reduct automorphism under consideration is phase-admissible on every component.

Let

\[
\mathcal C(D)=\{C_1,\dots,C_r\}.
\]

For each such automorphism `g`, define its phase tuple

\[
\Phi_g
=(\phi_{g,C_1},\dots,\phi_{g,C_r})
\in S_q^r.
\]

Let

\[
\Sigma_q(D,c)
=
\{\Phi_g:g\in A_{\rm ph}\}
\subseteq S_q^r
\]

be the realized phase set.

The globally anonymous phases are exactly the diagonal tuples

\[
\Delta(S_q)
=
\{(\pi,\dots,\pi):\pi\in S_q\}.
\]

---

## 3. Primitive point-image synchronization constraints

For components `C_i,C_j` and a color `a in O`, define the abstract primitive constraint

\[
\boxed{
[i,j;a]:
\phi_{C_i}(a)=\phi_{C_j}(a).
}
\]

This constraint compares the image of one source color under two local phases.

It is deliberately abstract. It is **not** automatically identified with one new operation cell.

A finite set `S` of such constraints **synchronizes** the realized phase set when every tuple in `Sigma_q(D,c)` satisfying all constraints in `S` is diagonal.

Define the **multicolor phase-link number**

\[
\boxed{
\lambda_q^{\rm ph}(D,c)
=
\min\{|S|:S\text{ synchronizes }\Sigma_q(D,c)\}.
}
\]

This is the direct nonabelian full-support analogue of the fixed-domain binary phase-link optimization.

---

## 4. Basic bounds

### Proposition 4.1

\[
\boxed{
0\le\lambda_q^{\rm ph}(D,c)\le(q-1)(r-1).
}
\]

### Proof

The lower bound is immediate.

For the upper bound, choose a spanning tree on the `r` comparison components. For each tree edge `{i,j}`, impose agreement on any fixed `q-1` colors:

\[
\phi_i(a)=\phi_j(a)
\]

for those `q-1` values of `a`.

Two permutations of a `q`-element set that agree on `q-1` points agree on the remaining point as well. Hence every tree edge forces

\[
\phi_i=\phi_j.
\]

Connectivity of the tree forces all component phases equal. The number of constraints is `(q-1)(r-1)`. `square`

The bound need not be optimal because permutation bijectivity can make constraints on different component pairs interact.

---

## 5. Binary reduction

For `q=2`, agreement on one color forces agreement of the entire permutation in `S_2`. Therefore the spanning-tree upper bound becomes

\[
(r-1),
\]

recovering the familiar binary synchronization scale in the full independent-phase case.

Thus the factor `q-1` is the naive per-edge permutation-identification cost, but multicolor networks may beat this factor globally through cross-edge inference.

---

## 6. Realized-state optimization versus worst-case capacity

As in Article B, one must distinguish abstract phase capacity from actually realized carrier behavior.

### Realized cost

\[
\lambda_q^{\rm ph}(D,c)
\]

uses only phase tuples produced by actual carrier automorphisms.

### Worst-case full phase capacity

If all tuples in

\[
S_q^r
\]

are allowed abstractly, define

\[
L_q(r)
=
\min\{|S|:S\text{ forces every satisfying tuple in }S_q^r
\text{ to lie in }\Delta(S_q)\}.
\]

Then

\[
\boxed{
r-1\le L_q(r)\le(q-1)(r-1).}
\]

The lower bound follows because if the graph on component indices touched by constraints is disconnected, one connected block may be right-composed by a nontrivial permutation independently of another block while preserving all within-block constraints.

For `q=2`,

\[
L_2(r)=r-1.
\]

For `q>=3`, determining exact `L_q(r)` is a separate finite extremal synchronization problem. No closed formula is claimed here.

Small brute-force experiments already show that the spanning-tree `(q-1)(r-1)` construction need not be sharp for `q>=3`.

---

## 7. Partial-support sector

When `O_C` is a proper subset of `O`, the primitive local data are partial bijections

\[
\phi_C:O_C\to O_{gC}.
\]

The exact gluing criterion from `GLUING_CRITERION.md` has two defect types:

- source disagreement;
- target collision.

A synchronization constraint system must therefore control both repeated source colors and cross-support collisions. A single scalar analogue of the binary `lambda` is less canonical here.

For that reason no universal partial-support cost invariant is promoted in this checkpoint.

---

## 8. Local partition-repair cost

Before phase synchronization, Model T may fail locally because the proper-coloring partition of `H_T(C)` is not invariant under a reduct automorphism.

One can define an abstract **partition-repair problem**: add arbitrary-cell equality comparisons until every bad transported proper coloring is separated from the original color partition.

However turning these abstract comparisons into legal new FCOA operation cells changes the sparse domain itself and may create new carrier symmetries, exactly as in the binary extension problem.

Therefore this note does **not** define a real-cell multicolor `alpha_q` or assert any inequality between an abstract partition cost and a cell-extension cost.

---

## 9. Current safe hierarchy

The multicolor sparse branch now has the following cost architecture:

\[
\boxed{
\begin{array}{c}
\text{Model-T proper-coloring ambiguity}\\
\downarrow\\
\text{phase-admissible sector}\\
\downarrow\\
\text{visible-support local bijections}\\
\downarrow\\
\text{global gluing obstruction}\\
\downarrow\\
\lambda_q^{\rm ph}\text{ in the full-support sector}\\
\downarrow\\
\text{actual operation-cell repair: open.}
\end{array}}
\]

This is intentionally more cautious than copying the binary cost hierarchy.

---

## 10. Open extremal problem

A clean independent problem emerging from the theory is:

\[
\boxed{
L_q(r)=?
}
\]

for point-image constraints of the form

\[
\pi_i(a)=\pi_j(a)
\]

forcing an arbitrary tuple in `S_q^r` to be diagonal.

This is mathematically meaningful without FCOA cell-extension complications and may be worth separate study if an exact formula or asymptotic law is found.

It is not needed for the present transport theorem package.
