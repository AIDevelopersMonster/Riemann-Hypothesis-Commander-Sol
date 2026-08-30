# FCOA-Z — Branch State

**Branch:** `director/fcoa-z-symmetric-line`  
**Date:** 2026-08-30  
**Research status:** ACTIVE

---

## Fixed inside this branch

### FZ0 — Symmetric signed completion

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

as a pointed oriented-line structure only. Binary addition and multiplication are not imported.

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
\qquad
\operatorname{Aut}(B^{\pm};<)\cong\mathbb Z,
\]

\[
\operatorname{Aut}(B^{\pm};A)\cong D_\infty,
\qquad
\operatorname{Aut}(B^{\pm};P_0,A)\cong C_2.
\]

### FZ5 — Coherent symmetric finite windows

\[
W_N=\{P_0\}\cup\{P_n^+,P_n^-:1\le n\le N\}
\]

are literal restrictions of one infinite signed line. No wrap-around.

### FZ6 — Signature arithmetic firewall

Signed completion introduces no primitive binary addition or multiplication.

### FZ7 — Minimal signed M0 reflection closure

For each chosen involution on the terminal output sorts, the positive M0 table has a unique minimal simultaneous-reflection extension. Positive cells are unchanged, negative mirror cells are forced, and genuinely mixed-sign cells remain unopened.

### FZ8 — `oplus` becomes radial contraction, not signed addition

Right multiplication by the fixed origin is the rooted contraction

\[
\rho(P_n^\sigma)=
\begin{cases}
P_0,&n=1,\\
P_{n-1}^\sigma,&n\ge2,
\end{cases}
\]

so the operation moves toward zero on both branches rather than acting as global successor/predecessor.

The old positional asymmetry survives:

\[
P_0\oplus x=x,
\qquad
x\oplus P_0=\rho(x)\ne x.
\]

### FZ9 — Legacy noncommutativity and partial-association asymmetry survive

Reflection completion does not force commutativity or associativity. Here “nonassociative” refers to the declared FCOA partial-association diagnostic, where one bracketing may be defined and the other undefined.

### FZ10 — Two canonical mirror-output lifts

- `ZM0-share`: mirror cells share terminal output fibers;
- `ZM0-split`: mirror cells receive distinct outputs exchanged by reflection.

The reflected base domain is identical; only value-fiber geometry differs.

### FZ11 — Fiber choice changes rigidity

For exact finite typed restrictions containing only active output elements and \(N\ge2\):

\[
\operatorname{Aut}(W_N,\otimes)_{split}\cong S_{N-1}\wr C_2,
\]

\[
\operatorname{Aut}(W_N,\otimes)_{share}\cong S_{N-1}\times C_2.
\]

For signed `oplus`, in either variant,

\[
\operatorname{Aut}(W_N,\oplus)\cong C_2,
\]

and for both operations together,

\[
\operatorname{Aut}(W_N,\oplus,\otimes)\cong C_2.
\]

If an ambient infinite output sort is retained inside a finite presentation, unused-output permutation kernels must be appended separately.

### FZ12 — Exact commutation counts

On \(W_N\):

\[
|Comm_{\oplus}|=2N,
\]

and for \(N\ge2\),

\[
|Comm_{\otimes}|=6(N-1).
\]

These counts are independent of shared versus split mirror fibers.

### FZ13 — Rooted radial memory without signed orientation

The signed `oplus` reduct remembers the origin and radial depth but still admits global branch reflection. This is weaker than full signed-coordinate recovery.

### FZ14 — Zero-reflection definability barrier

In any exact reflection-symmetric signed M0 operational reduct, parameter-free FO definitions on the base sort must be reflection invariant.

Hence standard signed order and ordinary integer multiplication are not parameter-free FO-definable there.

By contrast,

\[
x+y=z\Longrightarrow(-x)+(-y)=-z,
\]

so reflection supplies no corresponding obstruction to addition.

Therefore a necessary condition for parameter-free recovery of ordinary signed multiplication is that some generated structure break zero reflection, unless the recovered target/equivalence notion is changed.

---

## Audit status

`SIGNED_M0_REFLECTION_TRANSFER_0_1.md` was hostile-audited in

`HOSTILE_AUDIT_SIGNED_M0_TRANSFER_0_1.md`.

Verdict:

\[
\boxed{\text{PASS WITH TWO SCOPE CLARIFICATIONS}.}
\]

No defect was found in the theorem nucleus. The two clarifications concern active-output versus ambient-output finite presentations and terminology for partial association.

---

## Working / not yet fixed

### WZ1 — Reflection-equivariance classes beyond minimal closure

Classify:

1. operations commuting with reflection;
2. operations conjugated to a distinct operation under reflection;
3. operations whose domain alone is reflection-compatible;
4. genuinely asymmetric signed operations.

### WZ2 — Mixed-sector generators — DELIBERATELY OPEN

The genuinely new signed sectors are

\[
(+,-),\qquad(-,+).
\]

No canonical value law is currently selected for them.

In particular, the programme does **not** currently impose

\[
P_{-3}\oplus P_1=P_{-2}
\]

or any other ordinary signed-addition rule on the legacy operation.

The default minimal signed M0 therefore keeps genuinely mixed cells `UNDEF`, while the *extension problem* remains `OPEN`.

This is a deliberate research hold, not a claim that the two branches should remain permanently non-interacting.

### WZ2a — Candidate interaction mechanism: directed displacement

The leading future candidate is interaction by shifting one argument relative to the other along the rigid line.

Schematically, future rules may depend on a directed displacement parameter rather than only on branch labels:

\[
(P_i^+,P_j^-)
\longmapsto
\text{a value determined by a controlled shift of }i\text{ or }j,
\]

and independently

\[
(P_i^-,P_j^+)
\longmapsto
\text{a value determined by the opposite or role-sensitive shift}.
\]

Candidate families to test later include:

- equal-radius bridges \((P_n^+,P_n^-)\);
- fixed-offset bridges \((P_n^+,P_{n+k}^-)\);
- variable-offset families generated by repeated successor/predecessor motion;
- role-asymmetric laws in which shifting the first variable is not equivalent to shifting the second;
- output-channel rules in which crossing the origin sends the result to a transverse fiber instead of a base point.

None of these is canonical yet.

### WZ2b — Selection criterion for a future mixed law

A future mixed-sector rule will be accepted only if it is derived from a clear generator principle and passes all of the following tests:

1. exact preservation of the old positive M0 substructure;
2. no hidden import of ordinary signed addition or multiplication;
3. explicit treatment of argument order;
4. explicit reflection behavior: preserved, twisted, or deliberately broken;
5. coherent restriction to symmetric finite windows;
6. measured effect on automorphism, commutation and association diagnostics;
7. arithmetic-leakage audit (`order`, `EqSignedGap`, `Add`, `Mul`);
8. output-sort accounting if the interaction leaves the base line.

### WZ3 — Signed output fibers as proto-transport channels

Determine whether `ZM0-share`, `ZM0-split`, or a third fiber organization is the correct baseline for eventual inter-line transport.

---

## Open

### OZ1 — Signed carrier-erasure memory

After selected erasures of `P0`, `S`, `<`, and `nu`, determine how much absolute coordinate/sign structure the operations alone recover.

### OZ2 — Signed AL ladder

Define and prove the integer-line analogue of

\[
AL0<AL1<AL2
\]

for the coordinate-rigid signed setting.

### OZ3 — Minimal reflection breaking for multiplication

Find the weakest generated modification that destroys exactly enough zero-reflection symmetry to permit signed multiplication recovery while keeping the addition boundary distinct.

### OZ4 — Interacting-line extension

After the one-line signed theory stabilizes, permit selected output fibers to re-enter as transitions between distinct coordinate lines and classify commuting, twisted, noncommuting, and partial transport squares.

---

## Current research hold

\[
\boxed{
\text{Do not freeze a mixed-sign value law yet.}
}
\]

The working expectation is that permanent separation of the two branches is unlikely to be the final theory. Their eventual interaction will probably be expressed through **directed displacement / variable shifting** along the rigid coordinate line, possibly with different laws for the first and second argument and with possible transverse-output events when trajectories cross or meet the origin.

For now this remains an explicitly named open problem rather than a hidden convention.

---

## Immediate next strike

Do not choose the mixed-sector formula yet. First classify the admissible **generator forms for directed displacement coupling** and determine which ones preserve genuinely FCOA behavior before testing any one of them as the canonical signed extension.