# QGE3 LQR — Small Exact Tables

## 1. Theorem-controlled rows

The following values are exact by proof, not by computation.

### Binary row

\[
L_2(r)=r-1.
\]

| `r` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_2(r)` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

### Three-color row

\[
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil.
\]

| `r` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_3(r)` | 0 | 2 | 3 | 5 | 6 | 8 | 9 | 11 | 12 | 14 |

### Two-phase column

\[
L_q(2)=q-1.
\]

| `q` | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_q(2)` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

### Three-phase column

\[
L_q(3)=2q-3.
\]

| `q` | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `L_q(3)` | 2 | 3 | 5 | 7 | 9 | 11 | 13 |

For `q=2`, the binary formula gives `L_2(3)=2`, so the displayed `2q-3` formula is intended for `q>=3`.

---

## 2. Exhaustive / integer-optimization checks

Independent finite optimization was used as a hostile check of the first theorem-controlled values. A normalized search fixes `pi_1=id`; every non-diagonal tuple in `S_q^r` becomes a row, every primitive constraint becomes a binary column indicating whether it excludes that tuple, and minimum synchronization is a minimum hitting-set / 0-1 covering problem.

Verified optima:

| `q` | `r` | exact optimum found | theorem prediction | status |
|---:|---:|---:|---:|---|
| 3 | 2 | 2 | 2 | PASS |
| 3 | 3 | 3 | 3 | PASS |
| 3 | 4 | 5 | 5 | PASS |
| 3 | 5 | 6 | 6 | PASS |
| 3 | 6 | 8 | 8 | PASS |
| 4 | 2 | 3 | 3 | PASS |
| 4 | 3 | 5 | 5 | PASS |
| 5 | 2 | 4 | 4 | PASS |
| 5 | 3 | 7 | 7 | PASS |
| 6 | 2 | 5 | 5 | PASS |
| 6 | 3 | 9 | 9 | PASS |

These computations are checks only; the infinite formulas above have independent proofs.

---

## 3. First genuinely two-parameter cells

The region `q>=4, r>=4` is not yet classified in general.

Finite optimization gives the following additional exact small values:

| `q` | `r` | `L_q(r)` | basis |
|---:|---:|---:|---|
| 4 | 4 | 7 | exact 0-1 covering search |
| 5 | 4 | 9 | lower bound from pair-union geometry + explicit construction |
| 6 | 4 | 12 | finite partition search + explicit construction |
| 7 | 4 | 14 | finite partition search + explicit construction |

The `r=4` values beyond the theorem-controlled axes are recorded as finite exact data, not yet promoted to a general formula.

Observed sequence at `r=4` begins

\[
L_3(4)=5,\quad L_4(4)=7,\quad L_5(4)=9,\quad L_6(4)=12,\quad L_7(4)=14.
\]

This already shows that a naive universal formula `ceil(q(r-1)/2)` is false: for example

\[
\left\lceil\frac{4\cdot3}{2}\right\rceil=6<7=L_4(4).
\]

Thus the universal half-density lower bound is sharp on the entire `q=3` row but not in general.

---

## 4. Explicit optimal examples from finite search

Constraints are written as triples `(i,j,a)`.

### `L_4(4)=7`

One optimal system is

```text
(0,1,3)
(0,2,0)
(0,2,2)
(0,3,0)
(1,3,1)
(1,3,2)
(2,3,1)
```

### `L_5(3)=7`

A theorem construction can be written

```text
(0,1,0)
(0,2,1)
(1,2,2)
(0,1,3)
(0,2,3)
(0,1,4)
(0,2,4)
```

The last four constraints synchronize the two additional source colors across the three phases; the first three form the `S_3` triangle gadget.

---

## 5. Current interpretation

The small table supports three distinct regimes:

1. `q=2`: purely tree-like synchronization, cost `r-1`;
2. `q=3`: exact half-density law `ceil(3(r-1)/2)`;
3. `q>=4,r>=4`: additional partition/unique-colorability obstructions appear and the half-density lower bound can fail to be sharp.

The next finite-enumeration target is a complete exact table for `4<=q<=7` and `4<=r<=6`, preferably using the quotient-partition formulation rather than raw enumeration of `S_q^r`.
