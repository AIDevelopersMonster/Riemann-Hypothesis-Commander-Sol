# FCOA-Z — Share/Split Selector Audit 0.2

**Date:** 2026-08-31  
**Status:** CORRECTED PROVED CORE / SUPERSEDES 0.1  
**Supersedes:** `SHARE_SPLIT_SELECTOR_AUDIT_0_1.md`  
**Uses:** `TERMINAL_COST_MEMORY_DUALITY_0_2.md`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Corrected selector statements

The hostile audit of `TERMINAL_COST_MEMORY_DUALITY_0_1.md` found a quantifier defect: a fixed finite window cannot constrain profile bits outside that window.

Accordingly, the cost and memory selectors must be stated globally by simultaneous optimization over all windows.

The remaining automorphism and reflection-faithfulness statements are unchanged.

---

## 2. Mirror-extension cost

### Theorem 2.1

Global `share` is the unique global profile satisfying

\[
C_N=0
\quad\text{for every }N\ge1.
\]

Equivalently, on each fixed window the all-share **visible restriction** is the unique finite-window cost minimizer.

Thus simultaneous all-window mirror-extension minimization selects

\[
\boxed{ZM0\text{-share}.}
\]

### Proof

Every terminal orbit appears at some finite depth. If all finite-window costs vanish, every profile bit must vanish. See `TERMINAL_COST_MEMORY_DUALITY_0_2.md`, Theorem 5.1. \(\square\)

---

## 3. Terminal branch memory

### Theorem 3.1

Global `split` is the unique global profile satisfying

\[
M_N=Q_N
\quad\text{for every }N\ge1.
\]

Equivalently, on each fixed window the all-split **visible restriction** is the unique finite-window memory maximizer.

Thus simultaneous all-window branch-memory maximization selects

\[
\boxed{ZM0\text{-split}.}
\]

### Proof

Every terminal orbit appears in some finite window. Simultaneous maximality forces every profile bit to one. See `TERMINAL_COST_MEMORY_DUALITY_0_2.md`, Theorem 5.2. \(\square\)

---

## 4. `otimes`-reduct automorphism rigidity

The audited signed-M0 transfer theorem gives

\[
\operatorname{Aut}(W_N,\otimes)_{split}
\cong S_{N-1}\wr C_2,
\]

\[
\operatorname{Aut}(W_N,\otimes)_{share}
\cong S_{N-1}\times C_2.
\]

For \(N\ge3\),

\[
2(N-1)!<2((N-1)!)^2.
\]

### Theorem 4.1

If rigidity is measured on the `otimes` reduct by smaller finite-window automorphism group, then every window \(N\ge3\) prefers

\[
\boxed{ZM0\text{-share}.}
\]

At \(N=2\) the two groups are both \(C_2\).

---

## 5. Full-operation automorphism rigidity

For either canonical lift and every \(N\ge2\),

\[
\operatorname{Aut}(W_N,\oplus,\otimes)\cong C_2.
\]

### Theorem 5.1 — Full-Rigidity Nonselector

Automorphism rigidity of the full signed-M0 operation structure does not distinguish `share` from `split`.

### Proof

The full automorphism groups coincide. \(\square\)

---

## 6. Faithful terminal reflection

For global `share`, terminal reflection fixes every active terminal output, so the induced \(C_2\)-action is trivial and nonfaithful.

For global `split`, the nonidentity reflection swaps each active terminal pair, hence acts nontrivially. Since the acting group is \(C_2\), the action is faithful.

### Theorem 6.1

Requiring faithful terminal reflection selects

\[
\boxed{ZM0\text{-split}.}
\]

among the two globally uniform lifts.

---

## 7. Corrected selector table

| Criterion | `share` | `split` | Outcome |
|---|---:|---:|---|
| simultaneous all-window extension cost | unique minimum | maximum | `share` |
| simultaneous all-window branch memory | minimum | unique maximum | `split` |
| `otimes` rigidity, \(N\ge3\) | more rigid | less rigid | `share` |
| full \((\oplus,\otimes)\) rigidity | \(C_2\) | \(C_2\) | tie |
| faithful terminal reflection | no | yes | `split` |

### Theorem 7.1 — Selector Conflict

The audited selector family has no unanimous winner:

- two criteria prefer `share`;
- two criteria prefer `split`;
- one criterion ties them.

### Scope

This does not prove that no future invariant can select a canonical lift. It proves that none can be presented as already selected by the current family of natural cost, memory, rigidity, and reflection-faithfulness principles without declaring which objective is privileged.

---

## 8. Publication consequence

After the 0.2 scope repair, the selector-conflict conclusion survives unchanged.

The correction strengthens publication discipline because it separates:

\[
\text{finite-window visible extremality}
\]

from

\[
\text{global simultaneous extremality}.
\]

No higher-dimensional construction is involved:

\[
\boxed{c_{coord}=0.}
\]
