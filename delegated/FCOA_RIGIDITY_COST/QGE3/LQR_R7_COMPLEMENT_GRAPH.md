# QGE3 LQR — Complement-Graph Reformulation for Pure Plane Families

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** structural continuation of the r=7 trade programme  
**Scope:** abstract pure defect-two synchronization

This note records the next reduction after `LQR_R7_TRADE_HIERARCHY.md`. It does not close `M_7`, but it replaces the higher-order resolution oracle by an ordinary edge-coloured graph problem with a very rigid set-complement geometry.

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

## 5. Why ordinary rainbow-matching theory is not enough

The complement graph has two strong properties:

1. each color class is a matching;
2. an edge of color `a` is not arbitrary: it is forced by the set equation
   \[
   B\sqcup C=M_a.
   \]

It is tempting to conjecture that a unique rainbow perfect matching in an edge-coloured graph with matching color classes must have a singleton color class. This is false already on six vertices. For example, with canonical edges

\[
01,\quad23,\quad45
\]

one may take the three color classes

\[
\{01,24\},\qquad
\{23,04\},\qquad
\{45,02\}.
\]

They are pairwise edge-disjoint matchings, every color class has size two, and the canonical rainbow perfect matching is unique.

Therefore any proof of the `r=7` bound must use the Boolean set-complement geometry, not only abstract proper edge-colouring/rainbow-matching arguments.

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

A direct random search through compatible fifteen-plane packings found many non-synchronizing families and, among the sampled packings, examples with as few as 51 noncanonical complement edges. This number is search evidence only; no extremal lower bound on `E(F)` is claimed here.

The next structural target is therefore:

\[
\boxed{
\text{derive an extremal complement-energy or rainbow-2-factor criterion from }
|\mathcal C|=30,\ |\mathcal P|=15,
\text{ and only 18 unused cuts.}
}
\]

Such a criterion would attack `M_7` without enumerating higher trade cores.

---

## 7. Relation to known matching theory

The terminology “uniquely restricted matching” is standard for ordinary graphs: a matching is uniquely restricted when it is the unique perfect matching on its saturated vertices. The alternating-cycle characterization belongs to the graph case (Golumbic–Hirst–Lewenstein, 2001).

For uniform hypergraphs, Bal–Dudek–Yilma determined the maximum number of edges in a hypergraph with a unique perfect matching (Discrete Mathematics 311 (2011), 2577–2580, DOI `10.1016/j.disc.2011.07.016`). Their general extremal bound is much too coarse for the present sparse Boolean-partition geometry, but it confirms that the unique-perfect-matching viewpoint is standard and should be separated from the programme-specific complement structure.

The programme-specific object is the rigid combination of:

- partition-realizable cut planes;
- pairwise cut-disjointness;
- fixed marked blocks;
- complement edge equations `B sqcup C = M_a`;
- uniqueness of the all-colors rainbow perfect matching.

---

## 8. Current status

This reduction does not change the rigorous numerical status

\[
14\le M_7\le21.
\]

No synchronizing 15-plane family has been found, but no infeasibility certificate has yet been obtained.

The next proof attack should be on the complement-energy/rainbow-2-factor side, not on a full enumeration of minimal support seven and above.
