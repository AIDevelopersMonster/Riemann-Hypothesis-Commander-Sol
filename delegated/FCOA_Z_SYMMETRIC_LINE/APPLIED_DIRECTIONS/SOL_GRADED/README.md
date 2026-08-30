# SOL-GRADED

**Status:** ACTIVE — exchange-selection phase complete  
**Date:** 2026-08-30  
**Scientific director:** Commander Sol  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`

## Current verdict

The completed FCOA-Z line canonically generates a `Z_2`-graded **linearized shadow** through the eigenspaces of its derived reflection involution. Raw positive/negative branches are not even/odd parity sectors, and abstract grading alone loses the rooted shift geometry.

The second phase now proves a sharper result about mixed-sector exchange:

- simultaneous reflection of ordered pairs and argument exchange are distinct involutions in general;
- they coincide exactly on the **mirror locus** `(x, nu x)`;
- therefore on mirror pairs, reflection equivariance itself becomes an exchange law;
- reflection-fixed outputs give symmetric/commutative mirror interaction;
- reflection-paired outputs give two-way-defined noncommutative mirror interaction;
- after linearization, output-even and output-odd components become exchange-symmetric and exchange-antisymmetric, respectively;
- two incompatible conservative `1D-CLOSED` mirror realizations exist, so the current FCOA-Z axioms do **not** select the super factor `(-1)^(pq)`.

Current applied classification:

`FORMAL EMBEDDING` — reflection-linearized subsystem plus proved mirror-exchange law.

Line-first verdict for super exchange-factor selection:

`UNDERDETERMINED`.

## Reports

- [`SOL_GRADED_REPORT_v0_1.md`](SOL_GRADED_REPORT_v0_1.md) — reflection-generated grading and strict non-equivalence to branch sign.
- [`SOL_GRADED_EXCHANGE_SELECTION_v0_2.md`](SOL_GRADED_EXCHANGE_SELECTION_v0_2.md) — pair-involution theorem, mirror-exchange theorem, two conservative mirror realizations, and exchange-factor underdetermination.

## Strongest new internal theorem

On the mirror mixed locus `y = nu x`, simultaneous reflection equals argument exchange. Hence geometry genuinely induces exchange behavior there. In the base-valued reflection-equivariant commutative case, the only possible mirror output is the root `P_0`.

## Next frontier

Test whether any conservative one-dimensional LC3 generator can induce a **nonzero bilinear law on reflection-homogeneous modes**

`V_1 x V_1 -> V_0`

from the original partial `oplus` itself, without defining a new bracket by hand.

If such a lift exists, test whether it forces the nontrivial exchange bit and satisfies graded Jacobi. If it cannot exist, prove the corresponding no-go theorem.

## Publication status

No standalone SOL-GRADED publication yet. The new mathematics is theorem-level and should be retained for a future applied comparison / line-completion paper, but the super-specific emergence claim should not be published before the bilinear-lift frontier is closed.
