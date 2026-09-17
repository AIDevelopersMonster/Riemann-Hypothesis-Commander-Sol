# QGE3 LQR — Complement-Graph Reformulation for Pure Plane Families

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** structural continuation of the r=7 trade programme  
**Scope:** abstract pure defect-two synchronization

This note records the next reduction after `LQR_R7_TRADE_HIERARCHY.md`. It does not close `M_7`, but it replaces the higher-order resolution oracle by an ordinary edge-coloured graph problem with a very rigid set-complement geometry and records the current sharp test objects for the `15`-plane barrier.

---

## 1. Marked and unmarked blocks

Fix phase `0`. For every defect-two source partition

\[
P_a=\{A_a,U_a,V_a\},
\qquad 0\in A_a,
\]

write

\[
M_a=X\setminus A_a=U_a\sqcup V_a.
\]

The block `A_a` is fixed to target color `a` in every normalized quotient coloring. Hence all nontrivial freedom lies in the `2q` unmarked blocks

\[
\mathcal U=\{U_a,V_a:a\in[q]\}.
\]

Pairwise cut-space compatibility implies that the normalized cuts represented by all `U_a,V_a,M_a` are distinct.

---

## 2. Complement graph

Define an edge-coloured graph `K(F)` whose vertex set is the `2q` unmarked block occurrences. For every target color `a`, join two block vertices `B,C` by an edge of color `a` exactly when

\[
B\cap C=\varnothing,
\qquad
B\cup C=M_a.
\]

Equivalently,

\[
C=M_a\setminus B.
\]

### Lemma 2.1
Every color class of `K(F)` is a matching.

### Proof
For fixed `a` and fixed block `B`, its possible partner is uniquely determined as `M_a\setminus B`. Thus a block vertex is incident with at most one edge of color `a`. \(\square\)

The canonical pair `\{U_a,V_a\}` is an edge of color `a`, so the canonical resolution gives a rainbow perfect matching

\[
R_0=\{U_aV_a:a\in[q]\}.
\]

---

## 3. Rainbow Perfect-Matching Equivalence

### Theorem 3.1
For a pairwise compatible pure-plane family `F`, normalized quotient colorings are in bijection with rainbow perfect matchings of `K(F)` that use every target color exactly once.

Consequently,

\[
\boxed{
F\text{ is synchronizing}
\iff
R_0\text{ is the unique rainbow perfect matching using all }q\text{ colors}.
}
\]

### Proof
A normalized target class `a` already contains the fixed block `A_a`. Its two remaining blocks must therefore be a pair `B,C` disjoint from one another and from `A_a`, with

\[
B\sqcup C=X\setminus A_a=M_a.
\]

That is exactly an edge of color `a` in `K(F)`. Distinct target classes must use disjoint unmarked block occurrences, so the selected colored edges form a perfect matching on all `2q` block vertices. Since every target color occurs once, the matching is rainbow and uses every color.

Conversely, such a rainbow perfect matching supplies exactly two unmarked blocks to each fixed marked block `A_a`, giving a normalized resolution and hence a quotient coloring. \(\square\)

---

## 4. Alternating-cycle and 2-factor form

Let `R` be a noncanonical rainbow perfect matching. Then

\[
R_0\triangle R
\]

is a disjoint union of even alternating cycles in the ordinary graph `K(F)`.

Contract every canonical edge `U_aV_a` to the source color vertex `a`. The noncanonical edges of `R` become a 2-regular multigraph on the support colors. Their edge colors are the target colors, each used exactly once.

Thus every closed-support trade is equivalently a **port-labelled rainbow 2-factor**:

- every source contributes its two unmarked block ports exactly once;
- every target color labels exactly one chosen complement edge;
- the chosen noncanonical edges form degree two at each active source after canonical contraction.

This is the ordinary-graph counterpart of the Incidence–2-Factor Theorem.

---

## 5. Why degree-only and peeling criteria fail

The complement graph has two strong properties:

1. each color class is a matching;
2. an edge of color `a` is forced by the Boolean equation
   \[
   B\sqcup C=M_a.
   \]

Ordinary rainbow-matching degree conditions are nevertheless insufficient.

### Counterexample 5.1 — no peelable parent is necessary

There exists a synchronizing compatible six-plane family

```text
(56, 199, 268, 293, 133, 126)
```

for which every target color has exactly two complement decompositions: the canonical pair and one noncanonical pair. Hence every color class of `K(F)` has size exactly two, but the canonical rainbow perfect matching remains unique.

The six alternative complement edges are mutually incompatible at the block ports and do not form a rainbow perfect matching.

Therefore the tempting recursive statement

\[
\text{unique rainbow matching}\Rightarrow\text{some color has degree one}
\]

is false even inside the actual Boolean partition geometry.

Any proof of the `r=7` bound must therefore retain port incidence, not only color degrees.

---

## 6. Additive/complement energy

For a pure-plane family define

\[
\mathcal C=\{U_a,V_a:a\in[q]\},
\qquad
\mathcal P=\{M_a:a\in[q]\}.
\]

The number of edges in the complement graph is exactly

\[
E(F)=
\#\left\{
\{B,C\}\subset\mathcal C:
B\cap C=\varnothing,
\ B\cup C\in\mathcal P
\right\}.
\]

The `q` canonical pairs contribute `q`; all other contributions measure noncanonical complement energy.

For `r=7,q=15`, the 45 normalized cuts

\[
\mathcal C\sqcup\mathcal P
\]

are distinct elements of the 63 nonzero vectors of `F_2^6`. Hence only 18 normalized cuts are unused.

---

## 7. A near-extremal fifteen-plane test object

A local search over compatible fifteen-plane packings produced the family

```text
(0, 42, 73, 78, 145, 148, 149, 166, 186, 198, 224, 236, 271, 275, 288)
```

with exactly **one** noncanonical rainbow perfect matching.

Its target-color complement degrees are

```text
1, 4, 6, 4, 5, 5, 4, 5, 5, 4, 5, 7, 4, 5, 2
```

so it has `66` complement edges in total, of which `51` are noncanonical.

The unique noncanonical trade has support exactly five, on source colors

\[
\{1,8,11,12,13\},
\]

and the symmetric difference with the canonical matching is one alternating cycle of length ten.

This object is important for proof design:

- a `15`-plane obstruction need not have many alternative resolutions;
- an argument based on lower-bounding the number of trades cannot be robust;
- if the `45-of-63` lemma is true, it is close to sharp at the level of matching multiplicity.

No one-swap neighbor of this family found in the exact compatibility neighborhood is synchronizing; the best one-swap alternatives still have at least three noncanonical rainbow matchings. This is search evidence only.

---

## 8. The 45-of-63 Complement Lemma target

The strongest clean statement currently under attack is:

### Conjectural Complement Lemma
Let

\[
|\mathcal C|=30,
\qquad
|\mathcal P|=15,
\qquad
\mathcal C\cap\mathcal P=\varnothing,
\]

where the 45 sets are distinct nonempty subsets of a six-element ground set and are partitioned into 15 canonical triples

\[
U_a,\ V_a,\ M_a=U_a\sqcup V_a.
\]

Assume the corresponding fifteen partition planes are pairwise cut-compatible. Then the canonical rainbow perfect matching in the complement graph is not unique.

If true, this gives

\[
M_7\le14.
\]

Together with the known synchronizing fourteen-plane construction it would imply

\[
\boxed{M_7=14}.
\]

The six-color counterexample above shows that any proof must exploit the density `45/63` and cannot be a purely local unique-matching theorem.

---

## 9. Exact-search frontier

A separate exact depth-first search is being used as an independent route to the same statement.

The search:

1. works directly on the 301 partition planes;
2. branches only through pairwise compatible families;
3. invokes the exact rainbow-resolution oracle after every augmentation;
4. prunes immediately when a partial family is already non-synchronizing, using obstruction persistence;
5. fixes the first plane to one of the four `S_7` block-size orbit representatives
   \[
   (1,1,5),\ (1,2,4),\ (1,3,3),\ (2,2,3);
   \]
6. applies canonical augmentation under the stabilizer of the first plane.

The current symmetry-reduced run has reached synchronizing partial families of size `13` in the first orbit `(1,1,5)`, but has not yet exhausted that orbit. Therefore it is **not** an infeasibility certificate and does not change the rigorous status of `M_7`.

The exact search is retained as a certification route; analytic work continues in parallel.

---

## 10. Relation to known unique-perfect-matching theory

Bal–Dudek–Yilma proved the exact maximum number of edges in a general `k`-uniform hypergraph with a unique perfect matching. For `k=3`, their theorem allows many more edges than occur in the present complement hypergraph, so their global edge bound does not settle the `15`-plane question.

Their proof is nevertheless conceptually relevant: a noncanonical complement edge in the present model intersects exactly three canonical matching edges — its target-color vertex and the two source block-pairs from which its block endpoints come. Thus every LQR trade is a highly restricted covering of canonical matching edges in the sense of general unique-perfect-matching theory.

The missing ingredient is the additional Boolean condition

\[
B\sqcup C=M_a,
\]

plus the 45-of-63 density constraint.

---

## 11. Current rigorous status

The reductions and searches in this note do not change

\[
\boxed{14\le M_7\le21.}
\]

No synchronizing fifteen-plane family has been found. No complete analytic proof or exhaustive infeasibility certificate has yet been obtained.

The next productive attack should target a **dense Boolean port-cycle lemma**: show that every compatible `45`-state canonical system on six Boolean coordinates forces a port-compatible rainbow alternating cycle, rather than merely forcing many complement edges.
