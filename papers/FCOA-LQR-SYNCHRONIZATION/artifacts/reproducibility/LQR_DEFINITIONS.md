# QGE3 LQR — Definitions and Exact Reformulation

**Branch:** `director/fcoa-rigidity-cost`  
**Phase:** post-publication research  
**Primary problem:** exact extremal synchronization number `L_q(r)`

## 1. Point-image constraint systems

Fix an anonymous alphabet

\[
O=\{0,\dots,q-1\},\qquad q\ge2,
\]

and `r` local full-support phases

\[
\pi_1,\dots,\pi_r\in S_O.
\]

A primitive synchronization constraint is

\[
[i,j;a]:\qquad \pi_i(a)=\pi_j(a),
\]

where `1<=i<j<=r` and `a in O`.

A finite family `S` of such constraints is **synchronizing** if every tuple satisfying all constraints is diagonal:

\[
\pi_1=\cdots=\pi_r.
\]

Define

\[
\boxed{
L_q(r)=\min\{|S|:S\text{ is synchronizing}\}.
}
\]

Global left composition

\[
\pi_i\mapsto \sigma\circ\pi_i
\qquad(\sigma\in S_q)
\]

preserves all primitive equality constraints. Hence in proofs one may normalize one phase, e.g. `pi_1=id`, without loss of generality.

---

## 2. Constraint graphs by source color

For each source color `a in O`, define a graph

\[
\Gamma_a(S)
\]

on vertex set `[r]` by

\[
\{i,j\}\in E(\Gamma_a)
\iff
[i,j;a]\in S.
\]

Only the connected components of `Gamma_a` matter: equality propagates along paths. Therefore any synchronizing system can be replaced, without changing its solution set and without increasing size, by one in which every `Gamma_a` is a forest.

For a reduced system write

\[
m_a=|E(\Gamma_a)|,
\qquad
c_a=\kappa(\Gamma_a)=r-m_a.
\]

Then

\[
|S|=\sum_{a\in O}m_a
=qr-\sum_{a\in O}c_a.
\]

---

## 3. Canonical quotient graph of a constraint system

For every `a`, let

\[
\mathcal B_a=\pi_0(\Gamma_a)
\]

be the set of connected components of `Gamma_a`.

Define a graph

\[
\boxed{H(S)}
\]

as follows.

Its vertices are pairs

\[
(a,B),\qquad a\in O,\quad B\in\mathcal B_a.
\]

For every phase index `i in [r]`, let `B_a(i)` denote the component of `Gamma_a` containing `i`. Join all `q` vertices

\[
(a,B_a(i)),\qquad a\in O,
\]

pairwise. Thus every index `i` contributes a `K_q` transversal, with duplicate graph edges suppressed.

There is a canonical proper `q`-coloring

\[
\chi_0(a,B)=a.
\]

The number of vertices is

\[
|V(H(S))|=\sum_a c_a=qr-|S|.
\]

---

## 4. Constraint systems are exactly a unique-coloring problem

### Theorem 4.1 — synchronization / unique-coloring equivalence

A constraint family `S` is synchronizing if and only if the canonical coloring `chi_0` of `H(S)` is the unique proper `q`-coloring up to a permutation of the `q` color names.

### Proof

Suppose `(pi_1,...,pi_r)` satisfies `S`. If `i,j` lie in one component `B` of `Gamma_a`, path propagation gives

\[
\pi_i(a)=\pi_j(a).
\]

Hence the value

\[
F(a,B):=\pi_i(a)\qquad(i\in B)
\]

is well-defined.

For each index `i`, the `q` vertices `(a,B_a(i))` form a clique. Their `F`-values are

\[
\pi_i(0),\dots,\pi_i(q-1),
\]

which are pairwise distinct because `pi_i` is a permutation. Thus `F` is a proper `q`-coloring of `H(S)`.

Conversely, let `F` be a proper `q`-coloring of `H(S)` using the `q` colors `O`. On the clique contributed by index `i`, the `q` vertices must receive all `q` colors exactly once. Therefore

\[
\pi_i(a):=F(a,B_a(i))
\]

defines a permutation `pi_i in S_q`. If `[i,j;a] in S`, then `i,j` lie in the same component of `Gamma_a`, so the corresponding vertex `(a,B)` is the same and

\[
\pi_i(a)=\pi_j(a).
\]

Hence proper `q`-colorings of `H(S)` are in bijection with satisfying phase tuples.

The diagonal tuples are exactly the colorings obtained from `chi_0` by one global permutation of the output colors. Therefore `S` is synchronizing exactly when `chi_0` is unique up to global color relabeling. \(\square\)

---

## 5. Consequences of the reformulation

The extremal problem may be written as

\[
\boxed{
L_q(r)=qr-\max |V(H(S))|,
}

where the maximum ranges over constraint quotients `H(S)` whose canonical `q`-coloring is unique.

This does **not** identify `L_q(r)` with the unrestricted extremal theory of uniquely colorable graphs: the graphs `H(S)` have special structure, namely they are obtained from `r` canonical `K_q` transversals by identifying vertices only inside the same source-color class.

The classical unique-colorability theory supplies necessary conditions and edge bounds, while the FCOA/LQR problem additionally imposes this transversal/partition realizability structure.

---

## 6. Cut interpretation

For a nonempty proper subset `X subset [r]`, let `Lab(X)` be the set of source colors appearing on constraints crossing the cut `(X,[r]\X)`.

If

\[
|Lab(X)|\le q-2,
\]

choose two colors `a,b` absent from the cut and let `sigma=(a b)`. Set

\[
\pi_i=\sigma\quad(i\in X),
\qquad
\pi_i=id\quad(i\notin X).
\]

Every internal constraint is satisfied, and every crossing constraint uses a color fixed by `sigma`. Hence this is a non-diagonal satisfying tuple.

Therefore every synchronizing system satisfies

\[
\boxed{
|Lab(X)|\ge q-1
\quad\text{for every nontrivial cut }X.
}
\]

Equivalently, for every pair of distinct source colors `a,b`,

\[
\boxed{
\Gamma_a\cup\Gamma_b\text{ is connected.}
}
\]

This pair-union connectivity condition is the first structural lower-bound engine for `L_q(r)`.

---

## 7. Scope firewall

1. `L_q(r)` is an abstract full-support phase synchronization number.
2. It is not the real FCOA operation-cell extension cost.
3. No multicolor `alpha_q` is defined here.
4. The published QGE3 theorem package remains frozen; this is post-publication continuation.
5. Classical unique-colorability results are used only as external graph-theoretic tools, not claimed as new.
