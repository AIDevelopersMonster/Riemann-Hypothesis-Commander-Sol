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

## Proved core package awaiting hostile audit

The following statements are proved in `SIGNED_M0_REFLECTION_TRANSFER_0_1.md` but are not yet promoted to branch-fixed status pending hostile audit.

### PZ7 — Minimal signed M0 reflection closure

For each declared involution on the terminal output sorts, the positive M0 table has a unique minimal simultaneous-reflection extension. The old positive cells are unchanged, their negative mirrors are forced, and no genuinely mixed-sign cell is opened.

### PZ8 — `oplus` becomes radial contraction, not signed addition

Right multiplication by the fixed origin is

\[
\rho(P_n^\sigma)=P_{n-1}^\sigma
\]

with the convention \(P_1^\sigma\mapsto P_0\). Thus it moves toward zero on both branches. It is not a global successor/predecessor on the signed line.

The old positional asymmetry survives:

\[
P_0\oplus x=x,
\qquad
x\oplus P_0=\rho(x)\ne x.
\]

### PZ9 — Legacy noncommutativity and partial nonassociativity survive

Signed reflection completion does not force the old operations to become commutative or associative.

### PZ10 — Two canonical mirror-output lifts

- `ZM0-share`: mirror cells share terminal output fibers;
- `ZM0-split`: mirror cells receive distinct outputs exchanged by reflection.

The base-domain extension is the same; only value-fiber geometry changes.

### PZ11 — Fiber choice changes rigidity

For symmetric finite windows and \(N\ge2\):

\[
\operatorname{Aut}(W_N,\otimes)_{split}\cong S_{N-1}\wr C_2,
\]

while

\[
\operatorname{Aut}(W_N,\otimes)_{share}\cong S_{N-1}\times C_2.
\]

For `oplus`, in either variant,

\[
\operatorname{Aut}(W_N,\oplus)\cong C_2.
\]

For both operations together,

\[
\operatorname{Aut}(W_N,\oplus,\otimes)\cong C_2.
\]

### PZ12 — Rooted radial memory without signed orientation

The signed `oplus` reduct remembers the root and radial depth but still admits the global branch reflection. This is distinct from full signed-coordinate recovery.

### PZ13 — Zero-reflection definability barrier

In a reflection-symmetric signed M0 operational reduct, parameter-free FO definitions must be invariant under simultaneous zero reflection.

Therefore standard signed order and standard integer multiplication are not parameter-free FO-definable there.

By contrast, the addition graph is reflection-invariant:

\[
x+y=z\implies(-x)+(-y)=-z.
\]

Hence zero reflection alone does not block signed addition.

A necessary condition for parameter-free recovery of ordinary signed multiplication is therefore that the operational/relational reduct break zero reflection somewhere, unless the target or equivalence notion is changed.

---

## Working / not yet fixed

### WZ1 — Hostile audit of signed M0 transfer

Audit `SIGNED_M0_REFLECTION_TRANSFER_0_1.md` for:

- hidden use of arithmetic sign laws;
- exact treatment of output-sort automorphisms;
- small-window exceptions;
- one-sorted versus typed-output differences;
- correctness of the shared/split rigidity groups;
- any implicit assumption that reflection-equivariance should be canonical rather than merely one admissible extension class.

### WZ2 — Reflection equivariance classes beyond minimal closure

Classify at least:

1. operations commuting with reflection;
2. operations conjugated to a distinct operation under reflection;
3. operations for which only domain geometry is reflection-compatible;
4. genuinely asymmetric signed operations.

### WZ3 — Mixed-sector generators

The genuinely new signed sectors are

\[
(+,-),\qquad(-,+).
\]

Need to find the weakest admissible coupling law that connects the branches without collapsing M0 to ordinary arithmetic.

### WZ4 — Signed output fibers as proto-transport channels

Need to determine whether shared or split output fibers are the better baseline for later multi-line transport. The finite automorphism calculation shows the choice is mathematically non-cosmetic.

---

## Open

### OZ1 — Signed carrier-erasure memory

After removing `P0`, `S`, `<`, `nu` in selected combinations, determine how much absolute coordinate/sign structure is recoverable from the partial operations alone.

### OZ2 — Signed AL ladder

Define and prove a correct integer-line analogue of

\[
AL0<AL1<AL2
\]

for the coordinate-rigid signed setting.

### OZ3 — Minimal reflection breaking for multiplication

Determine the weakest generated structural modification that destroys exactly enough zero-reflection symmetry to permit signed multiplication recovery, while keeping ordinary signed addition below it.

### OZ4 — Interacting-line extension

Only after the one-line signed theory stabilizes, permit selected output fibers to re-enter as transitions between distinct coordinate lines and classify commuting, twisted, noncommuting, and partial transport squares.

---

## Immediate next strike

\[
\boxed{
\text{Hostile-audit the signed M0 reflection package, then attack the mixed sectors }(+,-),(-,+).
}
\]

The first target is not to imitate ordinary sign arithmetic. It is to determine whether there exists a genuinely FCOA mixed-sign coupling whose composition geometry is new while the old positive-ray operation remains an exact substructure.