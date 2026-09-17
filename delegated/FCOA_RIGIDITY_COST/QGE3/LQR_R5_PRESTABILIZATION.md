# QGE3 LQR — Exact Five-Phase Pre-Stabilization Law

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** post-publication continuation  
**Scope:** abstract full-support point-image synchronization only

This note closes the complete `r=5` column of the LQR synchronization problem. It does not modify the archived FCOA LQR publication and does not introduce a real-cell multicolor `alpha_q`.

## 1. Exact theorem

Let

\[
C_5(q):=4q-L_q(5)
\]

be the five-phase synchronization defect.

### Theorem 1.1 — exact five-phase law

For every `q>=2`,

\[
\boxed{
L_q(5)=
\begin{cases}
4, & q=2,\\[2mm]
3q-3, & 3\le q\le 9,\\[2mm]
\left\lceil\dfrac{7q-15}{2}\right\rceil, & 10\le q\le 14,\\[3mm]
4q-15, & q\ge15.
\end{cases}}
\]

Equivalently, for `q>=3`,

\[
\boxed{
C_5(q)=
\min\left\{
15,\ q+3,\ \left\lfloor\frac{q+15}{2}\right\rfloor
\right\}.
}
\]

Thus the complete previously open pre-stabilization sector is

\[
\begin{array}{c|rrrrrrrrrrr}
q&4&5&6&7&8&9&10&11&12&13&14\\ \hline
L_q(5)&9&12&15&18&21&24&28&31&35&38&42.
\end{array}
\]

The value at `q=15` is `45`, agreeing with the already proved stabilization law `L_q(5)=4q-15` for `q>=15`.

---

## 2. Defect language

For a reduced synchronizing system, let `P_a` be the component partition of the five phase indices for source color `a`, and put

\[
d_a=|P_a|-1=\dim W(P_a).
\]

The forest reduction gives

\[
|S|=4q-\sum_a d_a.
\]

Hence minimizing the synchronization cost is equivalent to maximizing

\[
C=\sum_a d_a.
\]

Synchronization implies the pairwise cut-space condition

\[
W(P_a)\cap W(P_b)=\{0\}\qquad(a\ne b)
\]

inside

\[
V=\mathbb F_2^4.
\]

The large-alphabet theorem therefore supplies the Mersenne packing constraint

\[
\sum_a(2^{d_a}-1)\le15.
\]

For `r=5`, however, packing alone is not sufficient in the first four unknown alphabet sizes. The missing ingredient is a local support obstruction.

---

## 3. Closed-support persistence

### Lemma 3.1 — closed-support witness persistence

Let `A` be a subset of source colors. Suppose there exist permutations

\[
\rho_0,\dots,\rho_4\in S_A
\]

which are not all equal and satisfy every point-image equality belonging to colors in `A`. Then the full constraint system is not synchronizing, regardless of all constraints on colors outside `A`.

### Proof

Extend every `rho_i` to the full alphabet by the identity on the complement of `A`. For a source color outside `A`, all five extended permutations fix that color, so every equality on that color is automatically satisfied. The constraints on `A` remain satisfied by hypothesis. The extended phase tuple is still non-diagonal. Therefore it is a full non-synchronizing witness. \(\square\)

This is the key repair principle: an external color cannot repair a witness whose permutation support is already closed inside a smaller color set.

---

## 4. The four-plane obstruction

A defect-two color has a three-block partition and a two-dimensional cut space in `F_2^4`. Call such a color a **partition plane**.

### Lemma 4.1 — four-plane obstruction

A synchronizing five-phase system contains at most three defect-two colors:

\[
\boxed{m_2\le3.}
\]

### Finite classification behind the lemma

There are exactly

\[
S(5,3)=25
\]

three-block partitions of five phase indices. Among their pairwise-joining four-element families there are exactly `50` unordered compatible four-cores. Under the natural `S_5` action on phase indices these split into exactly two orbits, of sizes `30` and `20`.

Representatives may be taken as follows, where vertical bars separate blocks and the four rows are indexed by source colors `0,1,2,3`.

**Orbit A**

\[
\begin{array}{c|c}
0&01\mid23\mid4\\
1&02\mid14\mid3\\
2&03\mid1\mid24\\
3&04\mid13\mid2
\end{array}
\]

A non-diagonal satisfying phase tuple, written by point images on the four-color support, is

\[
\begin{array}{c|cccc}
&0&1&2&3\\ \hline
\rho_0&0&1&2&3\\
\rho_1&0&2&3&1\\
\rho_2&3&1&0&2\\
\rho_3&3&0&2&1\\
\rho_4&1&2&0&3
\end{array}
\]

**Orbit B**

\[
\begin{array}{c|c}
0&01\mid24\mid3\\
1&023\mid1\mid4\\
2&0\mid12\mid34\\
3&04\mid13\mid2
\end{array}
\]

A non-diagonal satisfying phase tuple is

\[
\begin{array}{c|cccc}
&0&1&2&3\\ \hline
\rho_0&0&1&2&3\\
\rho_1&0&1&3&2\\
\rho_2&2&1&3&0\\
\rho_3&3&1&0&2\\
\rho_4&2&1&0&3.
\end{array}
\]

Direct substitution shows that every row is a permutation and that every block equality is satisfied. Phase relabeling and source-color relabeling transport these witnesses over the full two orbits. Lemma 3.1 then extends either four-color witness by the identity to every larger alphabet. Hence no synchronizing system can contain four compatible defect-two colors. \(\square\)

The exhaustive orbit count and both explicit witnesses are independently checked by `verify_lqr_r5_prestabilization.py`.

---

## 5. Universal five-phase defect cap

We now combine the cut-space packing with Lemma 4.1.

### Case 1: a defect-four color occurs

Then its cut space is all of `F_2^4`, so every other positive-defect cut space would intersect it nontrivially. Hence

\[
C\le4.
\]

### Case 2: a defect-three color occurs

If `U` has dimension `3` and `W` has dimension at least `2` in `F_2^4`, then

\[
\dim(U\cap W)\ge3+2-4=1.
\]

Therefore pairwise trivial intersection forces every other positive defect to be at most one. A three-dimensional space uses seven nonzero cut vectors, leaving at most eight lines. Thus

\[
C\le3+\min\{q-1,8\}.
\]

This never exceeds the bound obtained below for `q>=3`.

### Case 3: every positive defect is one or two

Let `m` be the number of defect-two colors and `ell` the number of defect-one colors. Lemma 4.1 gives

\[
m\le3.
\]

Pairwise disjoint nonzero cut spaces give

\[
3m+\ell\le15,
\]

while the alphabet size gives

\[
m+\ell\le q.
\]

The total defect is

\[
C=2m+\ell.
\]

For fixed `m`,

\[
C\le2m+\min\{q-m,15-3m\}.
\]

Maximizing over `m=0,1,2,3` yields

\[
\boxed{
C\le
\min\left\{
15,\ q+3,\ \left\lfloor\frac{q+15}{2}\right\rfloor
\right\}
\qquad(q\ge3).
}
\]

Consequently

\[
L_q(5)\ge
4q-
\min\left\{
15,\ q+3,\ \left\lfloor\frac{q+15}{2}\right\rfloor
\right\}.
\]

This is the required strengthening of the pure packing bound in the small pre-stabilization range.

---

## 6. Sharp constructions

The bound is attained for every `q>=3`.

For `q=3`, the previously proved theorem gives

\[
L_3(5)=6,
\]

so `C_5(3)=6`.

For `4<=q<=14`, the following explicit partition families attain the target defect. A one-block partition `01234` denotes a connected color of defect zero. Any spanning forest within each displayed block realizes the partition with exactly `4-d_a` primitive constraints.

| q | C_5(q) | Component partitions |
|---:|---:|---|
|4|7|`01|23|4`; `02|14|3`; `0|12|34`; `013|24`|
|5|8|q=4 family; `024|13`|
|6|9|`01|23|4`; `02|14|3`; `0|12|34`; `013|24`; `024|13`; `0134|2`|
|7|10|q=6 family; `0234|1`|
|8|11|`01|23|4`; `02|14|3`; `03|1|24`; `012|34`; `024|13`; `034|12`; `04|123`; `0134|2`|
|9|12|q=8 family; `0|1234`|
|10|12|q=9 family; `01234`|
|11|13|`01|23|4`; `02|14|3`; `012|34`; `013|24`; `024|13`; `034|12`; `03|124`; `04|123`; `0134|2`; `0234|1`; `0|1234`|
|12|13|q=11 family; `01234`|
|13|14|`01|23|4`; `012|34`; `013|24`; `023|14`; `024|13`; `02|134`; `034|12`; `03|124`; `04|123`; `0124|3`; `0134|2`; `0234|1`; `0|1234`|
|14|14|q=13 family; `01234`|

For every listed family, after fixing the first transversal of the canonical quotient graph to colors `0,...,q-1`, repeated singleton-domain propagation forces every remaining quotient vertex to its canonical color. This gives a compact deterministic certificate of unique `q`-colorability and therefore of synchronization. The verifier checks every certificate independently.

At `q=15`, the universal binary-cut gadget gives defect `15` and cost `45`. For every `q>15`, append connected colors; the defect remains `15`, giving cost `4q-15`.

The lower and upper bounds coincide, proving Theorem 1.1. \(\square\)

---

## 7. Structural interpretation

The five-phase result isolates the first genuine pre-stabilization obstruction.

Pure cut-space packing predicts too much defect for `q=4,5,6,7`. The failure is not caused by shortage of binary cuts. It is caused by a **closed four-color permutation witness** carried by every compatible four-plane core. External source colors cannot repair this witness because it extends by the identity.

Thus the correct hierarchy at `r=5` is

\[
\text{packing capacity}
\quad+\quad
\text{closed-support forbidden cores}
\quad=\quad
\text{exact synchronization defect}.
\]

This suggests the next general problem for `r>=6`: classify minimal partition-subspace families that are packing-compatible but carry a closed-support non-diagonal permutation witness.

---

## 8. Scope firewall

1. This theorem concerns the abstract LQR point-image synchronization number only.
2. It does not yet define a multicolor real-cell repair invariant for FCOA operation-cell extensions.
3. The finite orbit classification is explicitly computer-verified and separated from the analytic dimension/packing argument.
4. No novelty claim is made for binary subspace packing, finite vector-space partitions, or set-partition enumeration themselves.
5. The new programme-specific content is the closed-support persistence mechanism, the four-plane obstruction, and the resulting exact `r=5` LQR law.
