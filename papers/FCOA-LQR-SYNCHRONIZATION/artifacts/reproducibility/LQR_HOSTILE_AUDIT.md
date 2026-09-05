# QGE3 LQR — Hostile Proof Audit

**Branch:** `director/fcoa-rigidity-cost`  
**Audit target:** `LQR_STABILIZATION_THEOREM.md`, `LQR_BINARY_CUT_GADGET.md`, `LQR_R4_THEOREM.md`  
**Verdict:** PASS WITH ONE PRESENTATION REPAIR

## 1. Executive verdict

The general stabilization theorem survives hostile review:

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1)
\quad\text{for }q\ge2^{r-1}-1.
}
\]

The proof also correctly shows that the threshold is exact.

No mathematical counterexample was found in the following critical steps:

1. forest reduction;
2. defect identity `d_a=|P_a|-1`;
3. cut-space realization `W(P)`;
4. dimension identity `dim W(P)=|P|-1`;
5. lattice identity `W(P) cap W(Q)=W(P vee Q)`;
6. conversion of pair-union connectivity into pairwise trivial subspace intersection;
7. nonzero-vector packing inequality;
8. equality analysis forcing every positive defect to equal one;
9. binary-cut upper-bound construction;
10. exact threshold `q_0(r)=2^(r-1)-1`.

A new independent verifier `verify_lqr_cutspace.py` was added and reproduces the structural identities through `r=6` and the exact weighted partition-packing capacity for all `q<=15` at `r=5`.

---

## 2. Forest reduction

For a fixed source color `a`, constraints only impose equality of the values `pi_i(a)` along connected components of `Gamma_a`.

Replacing each connected component by any spanning tree preserves exactly the same propagated equalities. Hence an optimal synchronizing system may be assumed colorwise acyclic.

PASS.

---

## 3. Defect bookkeeping

If the forest `Gamma_a` has `c_a` connected components on `r` phase vertices, then

\[
|E(\Gamma_a)|=r-c_a.
\]

Relative to the connected cost `r-1`, the saving is

\[
d_a=(r-1)-(r-c_a)=c_a-1.
\]

Therefore

\[
|S|=(r-1)q-\sum_a d_a.
\]

PASS.

---

## 4. Cut-space construction

Fix phase `0`. A normalized binary cut is represented by a vector

\[
x=(x_1,\dots,x_{r-1})\in\mathbb F_2^{r-1}
\]

with `x_0=0`.

For a phase partition `P`, define `W(P)` as the binary vectors constant on every block of `P`.

If `P` has `c` blocks, the block containing phase `0` is forced to bit zero and the other `c-1` blocks are independent. Therefore

\[
|W(P)|=2^{c-1},
\qquad
\dim W(P)=c-1.
\]

Thus

\[
\dim W(P_a)=d_a.
\]

PASS.

---

## 5. Partition join versus subspace intersection

A vector is constant on every block of both `P` and `Q` if and only if it is constant on every block of the equivalence relation generated jointly by `P` and `Q`. Hence

\[
\boxed{W(P)\cap W(Q)=W(P\vee Q).}
\]

The pair-union theorem gives

\[
P_a\vee P_b=\mathbf 1
\]

for every two source colors in a synchronizing system, so

\[
W(P_a)\cap W(P_b)=W(\mathbf 1)=\{0\}.
\]

PASS.

The identity was independently exhaustively checked for every pair of set partitions through `r=6`:

- `r=2`: Bell number 2;
- `r=3`: Bell number 5;
- `r=4`: Bell number 15;
- `r=5`: Bell number 52;
- `r=6`: Bell number 203.

---

## 6. Packing inequality

A `d_a`-dimensional binary subspace has `2^{d_a}-1` nonzero vectors. Pairwise trivial intersection makes these nonzero sets disjoint. Since the ambient space contains `2^{r-1}-1` nonzero vectors,

\[
\boxed{
\sum_a(2^{d_a}-1)\le2^{r-1}-1.
}
\]

Using

\[
d\le2^d-1
\]

for every integer `d>=0` gives

\[
\sum_a d_a\le2^{r-1}-1.
\]

Therefore

\[
L_q(r)\ge(r-1)q-(2^{r-1}-1).
\]

PASS.

Important novelty firewall: the nonzero-vector counting bound itself is standard finite-geometry packing logic. The programme-specific result is the canonical LQR-to-cut-space reduction and its exact matching with the LQR construction.

---

## 7. Equality and exact threshold

If equality holds in the linear lower bound, then

\[
\sum_a d_a=2^{r-1}-1.
\]

But

\[
\sum_a d_a
\le
\sum_a(2^{d_a}-1)
\le
2^{r-1}-1.
\]

Hence equality holds termwise in `d_a <= 2^{d_a}-1` for every color. The only nonnegative integer solutions are

\[
d_a\in\{0,1\}.
\]

Every positive-defect color therefore contributes exactly one nonzero vector, and obtaining total defect `2^{r-1}-1` requires at least that many positive-defect colors. Thus

\[
q\ge2^{r-1}-1.
\]

For smaller `q`, equality in the lower bound is impossible.

PASS.

---

## 8. Binary-cut upper bound

The active colors are the nonzero vectors

\[
V=\mathbb F_2^{r-1}\setminus\{0\}.
\]

For source color `v`, the phase partition is the bipartition induced by the bits of `v`, with phase `0` on the zero side. Each such color costs `r-2` constraints.

The recovery proof in `LQR_BINARY_CUT_GADGET.md` is valid:

- phase `i` fixes every color with `v_i=0`;
- hence it preserves the complementary set `A_i={v:v_i=1}`;
- comparison with phase `j` on colors in `A_i cap A_j` makes phase `i` preserve each of those intersections;
- their membership bits recover all coordinates other than `i`;
- phase `i` therefore fixes every vector in `A_i` individually.

Hence every normalized phase is the identity.

PASS.

---

## 9. Independent finite checks

The new verifier `verify_lqr_cutspace.py` passed the following tests.

### Partition/subspace identities

All partitions through `r=6` satisfy

\[
|W(P)|=2^{|P|-1}
\]

and every pair satisfies

\[
W(P)\cap W(Q)=W(P\vee Q).
\]

### r=5 weighted partition packing

Exact maximum total defect under pairwise joining was independently obtained as:

| q | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| max defect | 4 | 4 | 6 | 8 | 10 | 10 | 11 | 11 | 12 | 12 | 13 | 13 | 14 | 14 | 15 |

At `q=15`, equality in the Mersenne cap occurs only through fifteen one-dimensional cut spaces, agreeing with the exact-threshold theorem.

These computations are hostile checks, not dependencies of the proof.

---

## 10. One presentation repair

`LQR_R4_THEOREM.md` Section 5 gives a concrete five-constraint `q=3` system and says it is already optimal because `L_3(4)=5`. Optimal cardinality alone does not prove that this particular five-constraint realization synchronizes.

The realization has been independently exhaustively checked and is synchronizing, and it is equivalent to an already proved optimal three-color gadget after relabeling. The publication version should explicitly state one of those two facts, rather than infer synchronization merely from the cardinality theorem.

This is a proof-presentation repair only. It does not alter any theorem or numerical value.

---

## 11. Final audit verdict

\[
\boxed{\text{STABILIZATION THEOREM: PASS}}
\]

\[
\boxed{\text{EXACT THRESHOLD: PASS}}
\]

\[
\boxed{\text{BINARY-CUT CONSTRUCTION: PASS}}
\]

\[
\boxed{\text{R4 PACKAGE: PASS WITH ONE PRESENTATION REPAIR}}
\]

No theorem-level defect was found.
