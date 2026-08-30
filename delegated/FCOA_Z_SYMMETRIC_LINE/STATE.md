# FCOA-Z — Branch State

**Branch:** `director/fcoa-z-symmetric-line`  
**Date:** 2026-08-30  
**Research status:** ACTIVE

---

## Fixed inside this branch

The following statements have complete proofs in `SIGNED_COMPLETION_FOUNDATION_0_1.md`.

### FZ0 — Symmetric signed completion

The rooted ray admits the explicit two-branch completion

\[
B^{\pm}=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\]

with successor/predecessor crossing the origin.

### FZ1 — Canonical pointed-line identification

\[
(B^{\pm};P_0,S,P,<,\nu)
\cong
(\mathbb Z;0,s,p,<,-)
\]

as a pointed oriented-line structure.

This does **not** import binary `+` or `times` into the FCOA signature.

### FZ2 — Unique zero reflection

The unique origin-fixing map satisfying

\[
\nu S=P\nu
\]

is the signed reflection exchanging the two branches.

### FZ3 — Coordinate rigidity

\[
\operatorname{Aut}(B^{\pm};P_0,S)=1.
\]

### FZ4 — Exact base erasure symmetries

\[
\operatorname{Aut}(B^{\pm};S)\cong\mathbb Z,
\]

\[
\operatorname{Aut}(B^{\pm};<)\cong\mathbb Z,
\]

\[
\operatorname{Aut}(B^{\pm};A)\cong D_\infty,
\]

\[
\operatorname{Aut}(B^{\pm};P_0,A)\cong C_2.
\]

### FZ5 — Coherent symmetric finite windows

\[
W_N=\{P_0\}\cup\{P_n^+,P_n^-:1\le n\le N\}
\]

are literal restrictions of one infinite signed line. No wrap-around is allowed.

### FZ6 — Signature arithmetic firewall

The signed completion introduces no primitive binary addition or multiplication. This is only a signature statement; logical non-definability must be proved separately where needed.

---

## Working / not yet fixed

### WZ1 — Signed transfer of legacy M0 operations

Need to construct and hostile-audit extensions of

\[
\oplus,\qquad\otimes
\]

from the original nonnegative ray to the signed carrier.

Required constraints:

- old positive-sector cells unchanged;
- no imported arithmetic sign rules;
- argument roles remain positional;
- noncommutativity/nonassociativity remain admissible;
- mixed-sign sectors are not guessed by analogy.

### WZ2 — Reflection equivariance classes

Need to distinguish at least:

1. operations commuting with reflection;
2. operations conjugated to a distinct operation under reflection;
3. operations for which only domain geometry is reflection-compatible;
4. genuinely asymmetric signed operations.

### WZ3 — Signed output fibers

Candidate scheme:

\[
E_n^{\alpha,+},\qquad E_n^{\alpha,-}.
\]

Need to decide whether reflection preserves channel label \(\alpha\), permutes channel labels, or fails to extend to a channel symmetry.

---

## Open

### OZ1 — Mixed-sector law

Classify possible cells in

\[
(+,-),\qquad(-,+)
\]

without importing ordinary signed arithmetic.

### OZ2 — Signed carrier-erasure memory

After removing `P0`, `S`, `<`, `nu` in selected combinations, determine how much absolute coordinate/sign structure is recoverable from the partial operations alone.

### OZ3 — Signed AL ladder

Define and prove a correct integer-line analogue of

\[
AL0<AL1<AL2
\]

for the coordinate-rigid signed setting.

### OZ4 — Output fibers as future transport channels

Terminal output sorts remain baseline. A later extension may permit selected fibers to re-enter as morphisms/transport between distinct coordinate lines. This is explicitly postponed until the one-line signed theory is stable.

---

## Immediate next strike

\[
\boxed{
\text{Construct the weakest reflection-compatible signed extension of M0}
}
\]

subject to exact preservation of the original positive sector and no arithmetic sign-law import.

The audit must answer whether reflection should act:

- on carrier points only;
- on carrier and output indices;
- on output channel labels as well;
- or whether the original M0 directional asymmetry obstructs full reflection equivariance.
