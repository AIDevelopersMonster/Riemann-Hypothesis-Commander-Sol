# QGE3 LQR — Plane Resolution Trades and the First r=7 Forbidden-Core Layers

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** post-publication continuation  
**Scope:** abstract LQR point-image synchronization; pure defect-two sector  
**Proof status:** general structural theorems plus finite `S_7` orbit classifications verified by `verify_lqr_plane_trades_r7.py`

This note replaces the naive idea that the next step after the exact `r=6` column should merely be a full `r=7` table. The correct object is a forbidden-core calculus for families of defect-two colors. The main new point is that pure-plane synchronization is exactly a **unique resolution problem** for a finite family of set partitions.

---

## 1. Pure plane families

Let the phase set be

\[
X=[r]=\{0,1,\dots,r-1\}.
\]

A defect-two source color `a` has a component partition

\[
P_a=\{B_{a,1},B_{a,2},B_{a,3}\}
\]

into exactly three nonempty blocks. Its cut space `W(P_a)` is a two-dimensional binary subspace, hence a partition plane.

Assume throughout this note that the family is **pairwise compatible**:

\[
W(P_a)\cap W(P_b)=\{0\}
\qquad(a\ne b).
\]

Equivalently,

\[
P_a\vee P_b=\mathbf 1.
\]

Let `q` be the number of source colors.

The quotient graph has one vertex `(a,B)` for each block `B in P_a`. Two vertices of different source colors are adjacent exactly when their phase supports intersect.

Thus a pure `q`-plane family has exactly `3q` quotient vertices.

---

## 2. Resolution–Trade Equivalence

### Theorem 2.1 — resolution form of a quotient coloring

For a pairwise compatible pure-plane family, proper `q`-colorings of the quotient graph, modulo global relabeling of the target colors, are in bijection with resolutions of the `3q` block-vertices into `q` triples

\[
\mathcal R=\{R_1,\dots,R_q\}
\]

such that the three phase-support blocks in every `R_j` form a set partition of `X`.

The canonical coloring corresponds to the canonical resolution

\[
R_a^{\rm can}=\{(a,B):B\in P_a\}.
\]

Consequently,

\[
\boxed{
\text{the pure-plane family is synchronizing}
\iff
\text{its canonical resolution is unique.}
}
\]

### Proof

For each phase `i`, the quotient vertices whose blocks contain `i` form a clique of size `q`, one vertex from every source color. Hence every proper `q`-coloring uses every target color exactly once on that phase clique.

Fix a target color `c`. The block-vertices colored `c` are pairwise nonadjacent, so their phase supports are pairwise disjoint. Since `c` occurs exactly once in every phase clique, those supports cover `X`. Thus every target color class is a set partition of `X`.

No target color class can contain one block. No target color class can contain exactly two blocks: if `B` and `C` covered `X`, then `C=X\\B`; the cut `(B,X\\B)` would be a common nontrivial coarsening of the two source partitions containing those blocks, contradicting pairwise compatibility. Therefore every target color class contains at least three block-vertices.

There are `q` target colors and exactly `3q` block-vertices, so every target color class contains exactly three blocks.

Conversely, any decomposition of all block-vertices into `q` triples whose supports partition `X` defines a proper `q`-coloring by assigning one target color to each triple. Blocks inside one triple are disjoint, while every phase sees exactly one block of every target color.

This gives the claimed bijection. \(\square\)

---

## 3. Noncanonical triples use three source colors

### Lemma 3.1

If one resolved triple contains two blocks of the same source partition `P_a`, then it is the canonical triple of source color `a`.

### Proof

Let two blocks be `B,C in P_a`; the third canonical block is

\[
D=X\\(B\cup C).
\]

Any triple containing `B` and `C` and partitioning `X` must use `D` as its third block. Pairwise compatibility forbids another source partition from containing `D` or its complement, because that would reproduce the cut defined by `D`. Hence the third block is the remaining block of `P_a`. \(\square\)

Therefore every genuinely noncanonical resolved triple uses exactly one block from each of three distinct source colors.

This makes every closed-support obstruction a finite **resolution trade**: some canonical source triples can be regrouped into the same number of noncanonical triples.

---

## 4. Normalized marked/unmarked formulation

Distinguish phase `0`. For every source partition `P_a`, let

- `A_a` be the block containing `0`;
- `U_a,V_a` be the other two blocks.

After deleting phase `0`, define the marked cut support

\[
M_a=X\\A_a
\]

and regard `U_a,V_a` as subsets of `X\\{0}`. Then

\[
U_a\cap V_a=\varnothing,
\qquad
U_a\cup V_a=M_a.
\]

Pairwise compatibility means that all cut points

\[
U_a,\ V_a,\ M_a
\]

are globally distinct.

Normalize the phase-0 transversal of a quotient coloring to the canonical target labels. Then the block `A_a` is forced to keep target color `a`. The only remaining freedom is to assign to every marked set `M_a` an unordered pair of unmarked blocks whose disjoint union equals `M_a`.

### Theorem 4.1 — complement-pair form

A normalized alternative coloring exists if and only if the `2q` unmarked blocks can be repartitioned into `q` pairs

\[
\{X_a,Y_a\}_{a=1}^q
\]

such that

\[
X_a\cap Y_a=\varnothing,
\qquad
X_a\cup Y_a=M_a
\]

for every marked block `M_a`, with at least one pair different from the canonical pair `\{U_a,V_a\}`.

Thus the pure-plane obstruction problem is a finite **rainbow complement-matching / resolution-trade problem**.

This is the structural reformulation needed for a general forbidden-core theory.

---

## 5. Three-color obstruction theorem

For a closed-support core on exactly three source colors, normalize one phase permutation to the identity and write the phase witness as

\[
\rho_i\in S_3.
\]

For a source color `a`, its partition groups phases according to the value `\rho_i(a)`.

### Theorem 5.1 — five-permutation criterion

A non-diagonal three-color witness produces three pairwise compatible partition planes if and only if the set of distinct phase permutations

\[
D=\{\rho_i:i\in X\}\subseteq S_3
\]

contains at least five elements:

\[
\boxed{|D|\ge5.}
\]

Conversely, every obstructing compatible three-plane core has such a witness.

### Proof

Fix two source colors `a!=b`. Build the bipartite graph whose left vertices are the three possible values of `\rho_i(a)`, whose right vertices are the three possible values of `\rho_i(b)`, and whose phase `i` contributes the edge

\[
(\rho_i(a),\rho_i(b)).
\]

Because `\rho_i` is a permutation, the two values are distinct. Hence the six possible ordered pairs are exactly the six edges of

\[
K_{3,3}\setminus M,
\]

where `M` is a perfect matching. This graph is a six-cycle. Moreover `S_3` maps bijectively to those six edges.

The two source partitions have connected join exactly when this six-vertex bipartite graph is connected. A connected graph on six vertices needs at least five distinct edges; any five edges of a six-cycle form a spanning path, and all six form the cycle. Therefore compatibility is equivalent to `|D|>=5`.

The same set `D` works for every pair of source colors. With at least five permutations, every coordinate attains all three target values, so all three source partitions indeed have exactly three blocks. \(\square\)

This theorem gives a direct permutation model for every minimal three-plane trade.

---

## 6. Complete `r=7` three-plane classification

For seven phases there are

\[
S(7,3)=301
\]

partition planes.

There are exactly

\[
\boxed{2\,614\,570}
\]

unordered pairwise compatible three-plane families.

Under the natural action of `S_7` on the phase indices they split into

\[
\boxed{786}
\]

orbits.

Exactly

\[
\boxed{6}
\]

orbits are obstructing; the remaining

\[
\boxed{780}
\]

are synchronizing.

The six obstructing orbit sizes are

\[
420,\ 280,\ 1260,\ 630,\ 210,\ 420,
\]

so the six orbit types contain exactly

\[
\boxed{3\,220}
\]

concrete bad triples.

One set of canonical representatives, using the verifier's plane indices, is

```text
(2, 9, 21)      orbit 420
(2, 10, 19)     orbit 280
(2, 47, 59)     orbit 1260
(12, 42, 77)    orbit 630
(12, 43, 75)    orbit 210
(15, 40, 78)    orbit 420
```

For every representative the alternative resolution is a `3 x 3` trade: the three canonical source rows and the three alternative target columns both partition the seven phases.

---

## 7. Complete minimal four-plane layer for `r=7`

A four-plane obstruction is **minimal** if every one of its three-plane subfamilies is synchronizing.

Because obstruction persists under alphabet extension, every synchronizing family must avoid all minimal obstruction cores.

Starting from the 780 synchronizing three-plane orbit representatives, extend by one compatible partition plane, reject every four-family containing one of the six bad three-core types, and test the remaining four-family for a noncanonical resolution.

This exhaustive finite classification gives:

\[
\boxed{25}
\]

minimal obstructing four-plane `S_7`-orbits.

Their orbit-size distribution is

\[
\boxed{
13\times2520
+5\times1260
+5\times630
+1\times840
+1\times210.
}
\]

Hence the minimal bad four-core layer contains exactly

\[
\boxed{43\,260}
\]

concrete four-plane cores.

Canonical representatives are:

```text
(2, 9, 15, 18)
(2, 9, 18, 19)
(2, 9, 40, 70)
(2, 9, 56, 78)
(2, 10, 38, 69)
(2, 10, 39, 70)
(2, 10, 54, 78)
(2, 10, 55, 79)
(2, 14, 40, 77)
(2, 14, 40, 88)
(2, 14, 56, 65)
(2, 14, 56, 87)
(2, 14, 59, 68)
(2, 15, 55, 88)
(2, 15, 57, 68)
(2, 47, 53, 56)
(2, 47, 53, 57)
(12, 33, 75, 83)
(12, 33, 151, 245)
(12, 34, 77, 82)
(12, 34, 150, 245)
(12, 42, 62, 75)
(15, 40, 60, 70)
(15, 40, 143, 241)
(15, 40, 144, 242)
```

The verifier reproduces the full extension count, the minimality test, orbit canonicalization and the distribution above.

---

## 8. A synchronizing fourteen-plane `r=7` family

The following fourteen partition planes form a synchronizing family. They are listed by verifier index and partition:

```text
136 : 024 | 1 | 356
237 : 03 | 14 | 256
268 : 06 | 135 | 24
105 : 023 | 15 | 46
160 : 035 | 124 | 6
284 : 05 | 146 | 23
 88 : 01 | 26 | 345
 68 : 014 | 25 | 36
118 : 02 | 134 | 56
211 : 056 | 12 | 34
168 : 036 | 125 | 4
 83 : 015 | 2 | 346
  8 : 01246 | 3 | 5
191 : 0 | 1236 | 45
```

Its normalized quotient coloring is unique. Therefore, if

\[
M_r:=\max\{m_2:\text{a synchronizing pure defect-two family exists on }r\text{ phases}\},
\]

then

\[
\boxed{M_7\ge14.}
\]

This particular fourteen-plane family has exactly one further partition plane compatible with all fourteen; adding that plane makes the family non-synchronizing. This proves only maximality of this explicit construction, not the global equality `M_7=14`.

---

## 9. What happened to the first Plane-Core Conjecture?

The `r=5` and `r=6` exact columns gave

\[
M_5=3,
\qquad
M_6=7,
\]

which suggested

\[
M_r\stackrel{?}{\le}2^{r-3}-1.
\]

For `r=7` this predicts

\[
M_7\le15.
\]

The present work does **not** prove this inequality and does **not** prove that `15` is attainable. An extensive symmetry-aware cutting-plane search has not produced a synchronizing fifteen-plane family, but solver exhaustion is not a mathematical certificate.

Accordingly the correct status is

\[
\boxed{14\le M_7\le21}
\]

from the explicit construction and the raw cut-space packing bound, with the sharper conjectural upper bound `15` still open.

The important change is conceptual: the quantity `M_r` is now an extremal **unique-resolution** invariant, and the correct general attack is to classify minimal resolution trades rather than to count planes alone.

---

## 10. Higher-order cores are genuinely necessary

Using all 3,220 bad triples and all 43,260 minimal bad quadruples as forbidden subfamilies, the exact set-packing problem on the 301 `r=7` planes still admits a compatible family of size

\[
\boxed{17}.
\]

Such a family is nevertheless non-synchronizing, so its obstruction has support at least five after the already classified local cores are removed.

Therefore the `r=7` theory cannot close at the three- and four-color layers:

\[
\boxed{
\text{genuinely higher-order resolution trades are unavoidable.}
}
\]

This is a structural result, not merely a search inconvenience.

---

## 11. Revised programme

The next barrier is now precise.

1. Define the **resolution-trade hypergraph** whose vertices are compatible partition planes and whose hyperedges are minimal closed-support obstruction cores.
2. For `r=7`, classify the minimal five-core layer, then continue only as far as required to decide whether `M_7=14` or `15`.
3. In parallel, seek an abstract theorem bounding the size of a uniquely resolvable compatible family without enumerating all core layers.
4. Use the `S_3` five-permutation theorem as the first exact local model for a general permutation-support calculus.

The target is no longer a naive `r=7` table. It is an extremal theory of unique resolutions of partition-plane packings.

---

## 12. Scope firewall

1. This note concerns abstract LQR synchronization only.
2. No real-cell multicolor repair invariant is introduced.
3. The Resolution–Trade Equivalence is an exact reformulation of quotient-coloring uniqueness; it does not rely on probabilistic evidence.
4. The `r=7` orbit counts are finite computer-assisted classifications reproduced by the accompanying verifier.
5. The status of a synchronizing fifteen-plane `r=7` family remains open in this note.
