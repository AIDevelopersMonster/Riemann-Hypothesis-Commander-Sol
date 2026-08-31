# FCOA-Z — Share/Split Selector Audit 0.1

**Date:** 2026-08-31  
**Status:** PROVED CORE / HOSTILE AUDIT REQUIRED  
**Depends on:** `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`, `TERMINAL_COST_MEMORY_DUALITY_0_1.md`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Question

After terminal uniformity is imposed, two canonical signed-M0 terminal lifts remain:

\[
ZM0\text{-share},
\qquad
ZM0\text{-split}.
\]

The purpose of this note is to audit whether an already meaningful FCOA invariant uniquely selects one of them.

Four candidate selectors are tested:

1. minimal mirror-extension cost;
2. maximal terminal branch memory;
3. automorphism rigidity;
4. faithfulness of terminal reflection.

The outcome is not a hidden canonical winner. Different invariants select different endpoints, and full-operation automorphism rigidity ties them.

---

## 2. Cost selector

From `TERMINAL_COST_MEMORY_DUALITY_0_1.md`, for each finite signed window \(W_N\),

\[
C_N(share)=0,
\]

while

\[
C_N(split)=Q_N,
\]

where for \(N\ge2\),

\[
Q_N=3N-2.
\]

### Theorem 2.1

Minimal mirror-extension cost uniquely selects

\[
\boxed{ZM0\text{-share}.}
\]

### Proof

Every split terminal orbit requires one fresh reflected output, while a shared orbit requires none. Global `share` is the unique profile with zero added mirror outputs on every finite window. \(\square\)

---

## 3. Branch-memory selector

Let \(M_N\) count terminal-producing reflection orbits whose positive and negative source cells receive distinct terminal values.

Then

\[
M_N(share)=0,
\]

and

\[
M_N(split)=Q_N.
\]

### Theorem 3.1

Maximal terminal branch-memory uniquely selects

\[
\boxed{ZM0\text{-split}.}
\]

### Proof

A shared fiber erases branch distinction at its terminal value, while a split fiber preserves it. Global `split` separates every terminal-producing mirror orbit. \(\square\)

---

## 4. `otimes`-reduct rigidity selector

The audited signed-M0 transfer theorem gives, for \(N\ge2\):

\[
\operatorname{Aut}(W_N,\otimes)_{split}
\cong
S_{N-1}\wr C_2,
\tag{4.1}
\]

whereas

\[
\operatorname{Aut}(W_N,\otimes)_{share}
\cong
S_{N-1}\times C_2.
\tag{4.2}
\]

For \(N\ge3\),

\[
|S_{N-1}\times C_2|
=2(N-1)!,
\tag{4.3}
\]

while

\[
|S_{N-1}\wr C_2|
=2((N-1)!)^2.
\tag{4.4}
\]

Thus the shared lift has the smaller automorphism group once \(N\ge3\).

### Theorem 4.1

If rigidity is measured only on the signed `otimes` reduct by minimizing finite-window automorphism-group size, then for every \(N\ge3\) the selector chooses

\[
\boxed{ZM0\text{-share}.}
\]

### Proof

For \(N\ge3\), \((N-1)!>1\), hence

\[
2(N-1)!<2((N-1)!)^2.
\]

The group formulas (4.1)–(4.2) then give the claim. \(\square\)

### Boundary case

At \(N=2\), both groups are \(C_2\). Therefore the rigidity separation begins only at \(N\ge3\).

---

## 5. Full-operation rigidity tie

The same audited source proves that in either terminal lift,

\[
\operatorname{Aut}(W_N,\oplus,\otimes)
\cong C_2
\qquad(N\ge2).
\tag{5.1}
\]

### Theorem 5.1 — Full-Rigidity Nonselector

Finite-window automorphism rigidity of the **combined signed-M0 operation structure** does not distinguish global `share` from global `split`.

### Proof

Both variants have isomorphic full-operation automorphism group \(C_2\) for every \(N\ge2\). \(\square\)

### Interpretation

The cross-branch rigidity added by shared `otimes` fibers is already dominated by the much stronger radial rigidity supplied by `oplus`. Therefore it disappears as a distinguishing invariant when both operations are retained.

---

## 6. Faithfulness of terminal reflection

Let \(E_N\) be the active terminal output set in a nontrivial finite window, equipped with the involution \(\nu_E\).

The reflection group is

\[
C_2=\{1,r\}.
\]

### Shared case

For global `share`, every active terminal output is fixed:

\[
r\cdot e=e.
\]

Hence the action kernel is all of \(C_2\), and the action is not faithful.

### Split case

For global `split`, every terminal-producing orbit supplies a two-cycle:

\[
r\cdot e^+=e^-,
\qquad
r\cdot e^-=e^+.
\]

Since \(r\) acts nontrivially, the action of \(C_2\) is faithful.

### Theorem 6.1

Requiring the terminal reflection action to be faithful uniquely selects

\[
\boxed{ZM0\text{-split}.}
\]

among the two globally uniform canonical lifts.

### Proof

For an action of \(C_2\), faithfulness is equivalent to the nonidentity element acting nontrivially. It acts trivially on all terminal outputs in `share` and nontrivially in `split`. \(\square\)

---

## 7. Selector table

The audited selectors therefore behave as follows:

| Criterion | `share` | `split` | Selector outcome |
|---|---:|---:|---|
| mirror-extension cost | minimum | maximum | `share` |
| terminal branch memory | minimum | maximum | `split` |
| `otimes` automorphism rigidity, \(N\ge3\) | more rigid | less rigid | `share` |
| full \((\oplus,\otimes)\) automorphism rigidity | \(C_2\) | \(C_2\) | tie |
| faithful terminal reflection | no | yes | `split` |

Thus no unanimity exists among the already meaningful structural criteria.

---

## 8. Selector-Conflict Theorem

### Theorem 8.1

Within the two globally uniform canonical signed-M0 terminal lifts, the current family of audited intrinsic criteria does not produce a criterion-independent canonical choice.

More precisely:

1. two audited criteria uniquely select `share`;
2. two audited criteria uniquely select `split`;
3. one audited criterion ties the variants.

### Proof

Combine Theorems 2.1, 3.1, 4.1, 5.1, and 6.1. \(\square\)

### Scope

This theorem does **not** prove that no future invariant can canonically select one lift. It proves only that the present natural selector family is internally conflicting and that no selection can be attributed to the existing signed-M0 structure without specifying which invariant is privileged.

---

## 9. Stronger no-go statements already available

The selector audit sits above three exact no-go results:

1. current terminal-opacity axioms force neither global `share` nor global `split`;
2. pure equality coupling can force global uniformity but cannot break global complement symmetry;
3. full-operation automorphism rigidity does not break the tie.

Hence a future canonical selector must use information beyond all three mechanisms.

---

## 10. What would count as a genuine canonical selector?

A convincing selector should satisfy at least:

1. it is defined from existing or independently motivated FCOA structure, not from the words `share` or `split`;
2. it does not merely encode an arbitrary unary bit;
3. it remains meaningful on all sufficiently large finite windows or directly on the infinite structure;
4. its preference survives the presence of both legacy operations;
5. it introduces no hidden second coordinate.

The current audit shows:

- minimal extension violates no condition but chooses low memory;
- maximal memory chooses high cost;
- `otimes` rigidity is not stable after restoring `oplus`;
- terminal reflection faithfulness is stable but explicitly privileges retention of the reflection action in the output fiber.

Thus none is neutral with respect to the research objective.

---

## 11. Reconstruction interpretation

The choice between `share` and `split` is best viewed not as an ambiguity to be eliminated at all costs, but as a controlled resource decision:

\[
\boxed{
\text{share}=	ext{minimal extension / stronger value coupling},
}
\tag{11.1}
\]

\[
\boxed{
\text{split}=	ext{maximal branch memory / faithful terminal reflection}.
}
\tag{11.2}
\]

The exact cost-memory theorem quantifies the first tradeoff, and the automorphism audit quantifies part of the second.

---

## 12. Dimensional firewall

All selectors operate on terminal fibers over the already constructed signed line or on finite channel/output structure.

No second independently iterable coordinate is introduced.

Therefore

\[
\boxed{c_{coord}=0.}
\]

throughout.

---

## 13. Publication implication

The post-publication theorem package now contains:

1. terminal-profile classification with continuum fibre;
2. exact uniformity independence;
3. complete finite equality-coupling classification;
4. exact terminal cost-memory duality;
5. conflicting intrinsic selector audit.

This is now close to a publication-sized layer. Before publication promotion, the entire chain should receive one hostile audit and a focused prior-art review on:

- reduct/expansion fibres;
- reconstruction from reducts;
- finite constraint coupling;
- memory/cost tradeoffs in covers or extensions;
- faithful versus trivial involutive fibers.

No further mathematical expansion should be required unless the hostile audit exposes a missing theorem or false scope.

---

## 14. Next action

The next action is therefore **not** another speculative extension.

It is:

\[
\boxed{
\text{hostile-audit the complete post-publication terminal-reconstruction layer and decide publication readiness.}
}
\]

If the audit passes, prepare a separate RU/EN publication package. If it fails, repair only the failed theorem(s) before resuming research.