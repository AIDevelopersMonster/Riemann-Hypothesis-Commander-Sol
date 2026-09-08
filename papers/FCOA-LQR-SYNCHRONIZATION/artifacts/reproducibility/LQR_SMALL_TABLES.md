# QGE3 LQR — Small Exact Tables

## 1. Theorem-controlled rows and columns

The following values are exact by proof, not by computation.

### Binary row

\[
L_2(r)=r-1.
\]

### Three-color row

\[
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil.
\]

### Two-phase column

\[
L_q(2)=q-1.
\]

### Three-phase column

\[
L_q(3)=2q-3\qquad(q\ge3).
\]

### Four-phase column

By `LQR_R4_THEOREM.md`, for every `q>=2`,

\[
\boxed{
L_q(4)=
\begin{cases}
3, & q=2,\\
2q-1, & 3\le q\le5,\\
12, & q=6,\\
3q-7, & q\ge7.
\end{cases}
}
\]

Hence:

| `q` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_q(4)` | 3 | 5 | 7 | 9 | 12 | 14 | 17 | 20 | 23 | 26 | 29 |

The formerly computational values `L_4(4)=7`, `L_5(4)=9`, `L_6(4)=12`, `L_7(4)=14` are now theorem-controlled.

---

## 2. Finite verification role

The verifier is retained as a hostile check, not as a proof engine for the infinite formulas.

It checks:

1. the optimal `q=3` constructions for small `r` by normalized enumeration of phase tuples;
2. the exact `r=3` constructions for small `q`;
3. the old general three-active-color upper bound;
4. the exact `r=4` partition search in the feasible finite range;
5. the explicit seven-cut construction for `q=7` and its connected-color extensions for larger `q`.

---

## 3. Exact frontier after the second strike

Exact theorem-controlled regions now include:

\[
L_2(r),\qquad L_3(r),\qquad L_q(2),\qquad L_q(3),\qquad L_q(4).
\]

Therefore the genuinely open two-parameter regime has moved to

\[
\boxed{q\ge4,\qquad r\ge5.}
\]

The next natural questions are:

- exact `L_4(r)` for general `r`;
- exact `L_q(5)` for general `q`;
- asymptotic defect from the naive spanning-tree cost at fixed `r` and `q->infinity`;
- partition-lattice constructions generalizing the seven-cut `F_2^3` gadget.

---

## 4. Interpretation of the four-phase sequence

The exact sequence

\[
L_q(4)=5,7,9,12,14,17,20,\dots
\]

for `q=3,4,5,6,7,8,9,...` has a structural explanation.

For four phase indices every reduced source-color graph determines a partition of rank `m in {0,1,2,3}`. Pair-union connectivity implies:

- at most one rank-one color;
- with one rank-one color, at most four rank-two colors;
- without rank-one colors, at most seven rank-two colors;
- the seven rank-two partitions are pairwise compatible and form the optimal seven-cut gadget.

Thus the exceptional value at `q=6` is a genuine transition point between the `1+rank-two` architecture and the complete seven-cut architecture.
