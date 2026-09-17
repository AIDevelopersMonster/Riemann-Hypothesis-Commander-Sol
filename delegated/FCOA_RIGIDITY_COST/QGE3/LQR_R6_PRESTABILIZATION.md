# QGE3 LQR — Exact Six-Phase Pre-Stabilization Law

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** post-publication continuation  
**Scope:** abstract full-support point-image synchronization only  
**Proof status:** analytic reduction plus two finite `S_6`-orbit classifications, independently verified by `verify_lqr_r6_prestabilization.py`

This note closes the complete `r=6` column of the LQR synchronization problem. It continues the exact `r=5` result in `LQR_R5_PRESTABILIZATION.md` and leaves the archived FCOA LQR publication unchanged.

---

## 1. Exact theorem

Let

\[
C_6(q):=5q-L_q(6)
\]

be the six-phase synchronization defect.

### Theorem 1.1 — exact six-phase law

For every `q>=2`,

\[
\boxed{
C_6(q)=
\begin{cases}
2q+1, & 2\le q\le5,\\[1mm]
12, & q=6,\\[1mm]
\min\left\{31,\ q+7,\ \left\lfloor\dfrac{q+31}{2}\right\rfloor\right\}, & q\ge7.
\end{cases}}
\]

Equivalently,

\[
\boxed{L_q(6)=5q-C_6(q).}
\]

In particular, the formerly open pre-stabilization sector `4<=q<31` is exact. The first values are

\[
\begin{array}{c|rrrrrrrrrrrrrr}
q&4&5&6&7&8&9&10&11&12&13&14&15&16&17\\ \hline
L_q(6)&11&14&18&21&25&29&33&37&41&45&49&53&57&61.
\end{array}
\]

For `18<=q<=30`,

\[
L_q(6)=5q-\left\lfloor\frac{q+31}{2}\right\rfloor,
\]

and at `q=31` this joins the already proved stabilization law

\[
L_q(6)=5q-31\qquad(q\ge31).
\]

The known small-alphabet theorems give `L_2(6)=5` and `L_3(6)=8`, agreeing with the displayed defect formula.

---

## 2. Defect reduction in `F_2^5`

For a reduced synchronizing system let `P_a` be the component partition of the six phases for source color `a`, and define

\[
d_a=|P_a|-1=\dim W(P_a).
\]

Then

\[
|S|=5q-\sum_a d_a,
\]

so

\[
C_6(q)=\max\sum_a d_a
\]

subject to synchronization.

The universal cut-space theorem places all `W(P_a)` in

\[
V=\mathbb F_2^5
\]

with pairwise trivial intersections. Hence

\[
\sum_a(2^{d_a}-1)\le31.
\]

The dimension inequality

\[
\dim(U\cap W)\ge \dim U+\dim W-5
\]

implies immediately:

- a defect-five color excludes every other positive defect;
- a defect-four color can coexist only with defect-one colors;
- at most one defect-three color may occur;
- a defect-three color can coexist only with defect-two and defect-one colors.

Packing alone is still not sufficient. Two new closed-support obstructions are required.

---

## 3. Closed-support persistence

We use the persistence lemma proved in `LQR_R5_PRESTABILIZATION.md`.

### Lemma 3.1 — closed-support persistence

If a subset `A` of source colors admits a non-diagonal satisfying phase tuple whose permutations are supported inside `A`, then adding arbitrary constraints on colors outside `A` cannot restore synchronization.

Indeed, extend every witness permutation by the identity outside `A`. Every external source color is then fixed by every phase, so all external equalities are automatically satisfied.

Thus any finite non-synchronizing core is a permanent obstruction in every larger alphabet.

---

## 4. Eight-plane obstruction

A defect-two color has a three-block partition and a two-dimensional cut space in `F_2^5`. Call it a **partition plane**.

There are

\[
S(6,3)=90
\]

partition planes.

### Lemma 4.1 — eight-plane obstruction

Every synchronizing six-phase system contains at most seven defect-two colors:

\[
\boxed{m_2\le7.}
\]

### Finite classification

Among the 90 partition planes there are exactly

\[
58\,800
\]

unordered compatible eight-plane families. Under the natural action of `S_6` on the phase indices these split into exactly

\[
\boxed{88}
\]

orbits, with orbit-size distribution

\[
77\times720,
\qquad
7\times360,
\qquad
3\times240,
\qquad
1\times120.
\]

For one representative of every orbit, the canonical quotient graph has a proper coloring distinct from the canonical source coloring after fixing the first transversal. Hence every compatible eight-plane core is non-synchronizing.

By phase relabeling the same holds for every member of every orbit, and by Lemma 3.1 it remains an obstruction after arbitrary external colors are added. Therefore `m_2<=7`. \(\square\)

The exact enumeration, orbit reduction and alternative-coloring checks are reproduced by `verify_lqr_r6_prestabilization.py`.

---

## 5. Defect-three plus five-plane obstruction

There are

\[
S(6,4)=65
\]

defect-three partitions.

### Lemma 5.1 — `3+5 planes` obstruction

If a synchronizing system contains a defect-three color, then it contains at most four defect-two colors:

\[
\boxed{d_3>0\Longrightarrow m_2\le4.}
\]

### Finite classification

There are exactly

\[
75\,120
\]

compatible cores consisting of one defect-three partition and five partition planes. Under `S_6` they split into exactly

\[
\boxed{108}
\]

orbits, with orbit-size distribution

\[
101\times720,
\qquad
6\times360,
\qquad
1\times240.
\]

Every orbit representative admits a noncanonical proper coloring of its quotient graph after the standard first-transversal normalization. Hence every such six-color core carries a closed-support non-diagonal witness. Lemma 3.1 makes the obstruction permanent in every larger alphabet. \(\square\)

Again the full classification is independently reproduced by the verifier.

---

## 6. Universal six-phase defect bound

Let

\[
C=\sum_a d_a.
\]

We optimize by the largest occurring defect.

### Case A: defect five

A five-dimensional cut space is all of `F_2^5`, so no other positive defect is possible:

\[
C\le5.
\]

### Case B: defect four

Every other positive cut space must be a line. A four-space contains `15` nonzero vectors, leaving at most `16` available lines. Hence

\[
C\le4+\min\{q-1,16\}.
\]

### Case C: defect three

There is at most one defect-three color. Let `m` be the number of planes and `ell` the number of lines. Lemma 5.1 gives

\[
m\le4.
\]

The cut-vector budget and color budget are

\[
7+3m+\ell\le31,
\qquad
1+m+\ell\le q.
\]

Thus

\[
C=3+2m+\ell.
\]

For `q=4` the optimum is `9`; for `q=5` it is `11`; for `q=6` it is `12`. For `q>=7` this branch is dominated by the plane-line branch below.

### Case D: only planes and lines

Let `m` be the number of planes and `ell` the number of lines. Lemma 4.1 gives

\[
m\le7.
\]

The budgets are

\[
3m+\ell\le31,
\qquad
m+\ell\le q,
\]

and

\[
C=2m+\ell.
\]

For `q>=7`, optimizing over `0<=m<=7` gives

\[
\boxed{
C\le
\min\left\{
31,\ q+7,\ \left\lfloor\frac{q+31}{2}\right\rfloor
\right\}.
}
\]

Combining all four cases gives exactly the lower bound stated in Theorem 1.1.

The elementary integer optimization is also checked directly by the verifier.

---

## 7. Sharp constructions for `q=4,5,6`

The following partition families are synchronizing. Vertical bars separate blocks.

### `q=4`, defect `9`, cost `11`

\[
\begin{array}{c|c}
0&014\mid23\mid5\\
1&02\mid135\mid4\\
2&04\mid12\mid35\\
3&05\mid1\mid24\mid3
\end{array}
\]

### `q=5`, defect `11`, cost `14`

\[
\begin{array}{c|c}
0&012\mid3\mid45\\
1&01\mid24\mid35\\
2&035\mid12\mid4\\
3&04\mid13\mid25\\
4&0\mid15\mid2\mid34
\end{array}
\]

### `q=6`, defect `12`, cost `18`

\[
\begin{array}{c|c}
0&0125\mid34\\
1&015\mid23\mid4\\
2&01\mid24\mid35\\
3&02\mid134\mid5\\
4&03\mid1\mid2\mid45\\
5&0\mid14\mid235
\end{array}
\]

For each family the normalized canonical quotient coloring is unique. The verifier checks this by exact backtracking.

---

## 8. Seven-plane kernel for `7<=q<=17`

The following seven partition planes form a synchronizing kernel:

\[
\begin{array}{c|c}
0&013\mid25\mid4\\
1&025\mid14\mid3\\
2&02\mid15\mid34\\
3&0\mid123\mid45\\
4&04\mid12\mid35\\
5&03\mid145\mid2\\
6&05\mid13\mid24.
\end{array}
\]

Their seven cut spaces occupy `21` nonzero vectors of `F_2^5`. The ten uncovered normalized cut vectors are

\[
1,6,11,14,16,19,21,22,28,30.
\]

For each such vector, add its corresponding bipartition as one defect-one source color. Adding these ten lines in the displayed order gives synchronizing families for every

\[
q=7,8,\dots,17.
\]

At stage `q` the defect is

\[
C=q+7,
\]

which attains the lower bound.

Every prefix is independently verified by exact unique-coloring search.

---

## 9. Plane splitting for `17<=q<=31`

At `q=17`, the seven-plane kernel plus the ten complementary lines partitions all `31` nonzero cut vectors.

A partition plane contains exactly three nonzero cut vectors. Replace one plane color by the three corresponding line colors. This changes

\[
q\mapsto q+2,
\qquad
C\mapsto C+1.
\]

For the seven kernel planes, successive splittings use the cut triples

\[
\{8,18,26\},
\{4,9,13\},
\{12,17,29\},
\{7,24,31\},
\{3,20,23\},
\{2,25,27\},
\{5,10,15\}.
\]

After each split the resulting quotient coloring remains unique. Hence we obtain sharp synchronizing families for

\[
q=19,21,23,25,27,29,31
\]

with

\[
C=25,26,27,28,29,30,31,
\]

respectively.

For every even

\[
q=18,20,\dots,30,
\]

append one connected source color to the preceding odd construction. After normalizing phase zero to the identity, a connected new color is fixed by every phase, so the old alphabet is invariant and the preceding synchronizing system applies. Thus the defect is unchanged and equals

\[
\left\lfloor\frac{q+31}{2}\right\rfloor.
\]

At `q=31` the completely split family is precisely the full binary-cut line gadget, so the construction joins the established stabilization theorem.

This proves sharpness for every `q>=2`. \(\square\)

---

## 10. Structural consequence

The exact `r=5` and `r=6` columns now display the same first forbidden-core pattern:

\[
\boxed{
\begin{array}{c|c|c}
r & \text{maximum synchronizing number of defect-2 colors} & \text{first forbidden pure-plane core}\\ \hline
5&3&4\\
6&7&8
\end{array}}
\]

That is,

\[
3=2^{5-3}-1,
\qquad
7=2^{6-3}-1.
\]

This motivates the next target.

### Plane-Core Conjecture

For every `r>=5`, a synchronizing LQR system contains at most

\[
\boxed{2^{r-3}-1}
\]

defect-two colors. Equivalently, every compatible family of

\[
2^{r-3}
\]

partition planes carries a closed-support non-diagonal witness.

The `r=5` and `r=6` theorems prove the first two nontrivial cases.

A second hierarchy is suggested by Lemma 5.1: the presence of a higher-dimensional defect space can lower the admissible plane count further. Determining these mixed forbidden-core thresholds is the natural route to a general pre-stabilization calculus.

---

## 11. Scope and novelty firewall

1. The theorem concerns the abstract LQR point-image synchronization number, not real FCOA operation-cell extension cost.
2. No multicolor real-cell invariant `alpha_q` is defined here.
3. Binary subspace packing, vector-space partitions and set-partition enumeration are classical tools and are not claimed as new.
4. The computer-assisted portion is finite and explicit: 88 pure eight-plane `S_6` orbits and 108 mixed `d_3+5-plane` orbits.
5. The programme-specific contribution is the closed-support obstruction calculus and the resulting exact six-phase synchronization law.
