# Arithmetic Leakage Left Wall — Hostile Audit Reconciliation

**Project:** FCOA Admissibility Geometry  
**Targets:** `ARITHMETIC_LEAKAGE_BOUNDARY.md`, `G4A_GENERIC_FO_COLLAPSE.md`  
**Status after audit:** core left wall confirmed with two wording/formalism repairs  
**Scope:** uniform parameter-free first-order definability across the family unless explicitly stated otherwise

## 1. Executive verdict

The central left-wall theorem survives hostile audit.

The strongest correct statement is:

\[
\boxed{
FO(\text{G4-A on generic tuples})
=
FO(\text{finite linear order})
}
\]

in the **uniform family sense**.

Consequently the canonical truncated rank-addition and rank-multiplication graphs are not uniformly first-order definable in G4-A.

The audit found no hidden import of index arithmetic.

Two repairs are required:

1. formalize the source-to-target construction specifically as a **fixed deterministic parameter-free finite-copy FO transduction/copying interpretation**, rather than using `interpretation/transduction` interchangeably;
2. do not call `EqGap` the globally weakest or first possible non-order leakage. It is a canonical **full additive gateway**. Weaker non-order enrichments may exist between pure order and addition.

Neither repair changes the left-wall theorem.

## 2. Exact relational signature

Relationalize the partial G4-A operation by

\[
T(x,y,z)\iff x\otimes_{4A}y=z.
\]

The target language is exactly

\[
\{T\}.
\]

There are no named constants, no unary sort predicates, and no named outputs.

The one-sorted universe contains the base points, all indexed terminal outputs, and the two anonymous orientation outputs.

This relationalization is the signature in which the audit is carried out.

## 3. Fixed finite-copy order transduction — CONFIRMED WITH FORMALISM REPAIR

Let

\[
m=N-1,
\qquad
L_m=([m],<).
\]

Use seven fixed copy indices

\[
g,e_\ast,e_\times,b_0,b_1,w_+,w_-.
\]

The first three copies are present over every source element. The last four are restricted by the parameter-free source formula

\[
\operatorname{Min}(x)\iff\neg\exists y(y<x),
\]

so each contributes exactly one target element.

The operation graph is defined by finitely many fixed copy-cases using only equality and source order:

\[
b_0\otimes b_1=b_0,
\]

\[
b_0\otimes(g,x)=b_0,
\]

\[
(g,x)\otimes b_0=(e_\ast,x),
\]

\[
b_1\otimes(g,x)=(g,x),
\qquad
(g,x)\otimes b_1=(g,x),
\]

\[
(g,x)\otimes(g,x)=(e_\times,x),
\]

\[
(g,x)\otimes(g,y)=w_+\iff x<y,
\]

\[
(g,x)\otimes(g,y)=w_-\iff y<x,
\]

and

\[
b_1\otimes b_0=w_+.
\]

All other target triples are absent from \(T\).

This is a deterministic parameter-free 7-copy FO transduction (equivalently, a standard copying interpretation in a formalism allowing finitely many fixed copies). The copy indices are part of the interpretation mechanism, **not symbols in the target structure**.

Hence target anonymity is preserved: the resulting G4-A structure itself still has language \(\{T\}\).

Every target FO formula has an effective source FO translation obtained by a finite disjunction over copy assignments for its quantified variables.

Therefore the direction

\[
FO(\text{G4-A generic})\subseteq FO[<]
\]

is valid.

## 4. Intrinsic recovery of order — CONFIRMED

The following target formulas were checked directly against the exact G4-A cells.

Activity as an argument:

\[
\operatorname{Act}(x)
\iff
\exists y,z\,[T(x,y,z)\lor T(y,x,z)].
\]

The left-zero boundary point:

\[
B_0(x)
\iff
\operatorname{Act}(x)
\land
\exists y\,T(x,y,x)
\land
\forall y,z\,(T(x,y,z)\to z=x).
\]

This defines exactly \(P_0\).

The other loopless active boundary point:

\[
B_1(x)
\iff
\operatorname{Act}(x)
\land
\neg B_0(x)
\land
\neg\exists z\,T(x,x,z).
\]

This defines exactly \(P_1\).

The generic sector:

\[
G(x)
\iff
\operatorname{Act}(x)
\land
\exists z\,T(x,x,z).
\]

This defines exactly \(G_N\).

The anchored positive output:

\[
W_+(w)
\iff
\exists b_0,b_1\,[B_0(b_0)\land B_1(b_1)\land T(b_1,b_0,w)].
\]

This defines exactly \(\Omega_+\), without naming it.

Finally

\[
x<_Gy
\iff
G(x)\land G(y)
\land
\exists w\,[W_+(w)\land T(x,y,w)]
\]

recovers exactly

\[
P_2<P_3<\cdots<P_N.
\]

Hence

\[
FO[<]\subseteq FO(\text{G4-A generic}).
\]

## 5. Generic FO Collapse Theorem — CONFIRMED

For every fixed arity \(r\), let

\[
R_N\subseteq G_N^r.
\]

Then the following are equivalent:

1. one parameter-free FO formula in \(\{T\}\) defines \(R_N\) for every \(N\ge3\);
2. one FO formula in \(\{<\}\) defines the corresponding relation under the increasing generic-order identification for every \(N\ge3\).

The first direction is the formula pullback through the fixed 7-copy transduction. The second direction substitutes the internally definable generic order \(<_G\) and relativizes all source variables to \(G\).

Thus:

\[
\boxed{
FO(\text{G4-A on generic tuples})
=
FO(\text{finite linear order})
}
\]

uniformly across the family.

This statement must **not** be confused with definability inside one fixed finite \(N\). For a fixed finite chain, positional relations can be defined by size-dependent formulas. The theorem concerns one formula working for all \(N\).

## 6. Finite parity obstruction — CONFIRMED

The exact classical fact needed is:

> Cardinality parity is not first-order definable on the class of finite linear orders in the language \(\{<\}\).

This follows either from the standard Ehrenfeucht-Fraisse analysis of long finite chains or from the McNaughton-Papert/Schützenberger characterization of FO[<] unary languages as star-free/aperiodic languages; the unary even-length language is not aperiodic.

No exact numerical EF threshold is needed for the theorem. It is sufficient that for every quantifier rank \(q\) there are sufficiently long consecutive finite chains of opposite parity that are \(q\)-equivalent.

This wording avoids making the proof depend on a particular non-optimal bound.

## 7. No uniform truncated rank addition — CONFIRMED

Externally only, let the generic ranks be

\[
0,1,\ldots,m-1.
\]

Assume a single G4-A FO formula uniformly defines

\[
\operatorname{Add}(x,y,z)
\iff
\operatorname{rk}(z)=\operatorname{rk}(x)+\operatorname{rk}(y)<m.
\]

By Generic FO Collapse it would define the same graph uniformly in finite linear order.

Let \(M\) be the maximum element. Then

\[
\exists x\,\operatorname{Add}(x,x,M)
\]

holds iff

\[
m-1
\]

is even, equivalently iff \(m\) is odd.

This uniformly defines parity of chain cardinality, contradiction.

Therefore

\[
\boxed{
\operatorname{Add}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

## 8. No uniform truncated rank multiplication — CONFIRMED

Assume a single formula uniformly defines

\[
\operatorname{Mul}(x,y,z)
\iff
\operatorname{rk}(z)=\operatorname{rk}(x)\operatorname{rk}(y)<m.
\]

For \(m\ge3\), the rank-2 element is uniformly order-definable as the second successor of the minimum. Let it be \(T_2\), and let \(M\) be maximum.

Then

\[
\exists x\,\operatorname{Mul}(T_2,x,M)
\]

holds iff \(m-1\) is even, hence iff \(m\) is odd.

For the only family size lacking rank 2, namely \(m=2\), the existential sentence is false and \(m\) is even, so the same parity classification is obtained without any problematic exception.

Thus uniform multiplication would again define parity.

Therefore

\[
\boxed{
\operatorname{Mul}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

## 9. Successor and betweenness — CONFIRMED / SIDE CLAIM TRIMMED

Once \(<_G\) is available,

\[
\operatorname{Succ}(x,y)
\iff
x<_Gy\land\neg\exists z\,(x<_Gz\land z<_Gy)
\]

is uniformly FO-definable, and betweenness is likewise definable.

Hence adding successor or betweenness as named relations to the already ordered G4-A generic sector does not increase FO expressive power.

Also, if canonical rank addition or multiplication were uniformly definable from the pure successor reduct of the finite family, substituting the above order-definition of successor would make them definable from order, contradicting Sections 7-8.

The separate infinite statement that pure successor does not FO-define transitive order is classical but is not needed for the left-wall theorem and should not carry any proof burden in the main argument.

## 10. Infinite G4-A left wall — CONFIRMED

The same fixed 7-copy parameter-free construction works over

\[
(\mathbb N,<).
\]

Therefore every first-order sentence of the infinite G4-A structure effectively translates to a sentence of \((\mathbb N,<)\).

Since the first-order theory of \((\mathbb N,<)\) is decidable, the first-order theory of the infinite G4-A structure is decidable.

Hence it cannot first-order interpret

\[
(\mathbb N,+,\times),
\]

because such an interpretation would reduce true first-order arithmetic to a decidable theory.

The parameter-free statement is therefore confirmed.

In fact, in this exact infinite G4-A structure every individual element is parameter-free definable: boundary points and \(\Omega_+\) are defined structurally; the generic points are obtained by finite successor distance from the least generic point; the indexed terminal outputs are then their unique operation outputs; \(\Omega_-\) is the common reverse-orientation generic output. Thus allowing finitely many fixed element parameters does not evade the decidability obstruction.

## 11. EqGap / addition interdefinability — CONFIRMED

For forward intervals define externally

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c),
\]

with

\[
a\le b,
\qquad c\le d.
\]

Let \(0_G\) be the uniformly definable least generic point.

Then

\[
\boxed{
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_G,y;x,z).
}
\]

Conversely,

\[
\boxed{
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,[
\operatorname{Add}(a,s,b)
\land
\operatorname{Add}(c,s,d)
]
}
\]

for forward intervals.

The common gap is between \(0\) and \(m-1\), so its representing element \(s\) always exists inside the same generic sector. Truncation therefore causes no missing witness.

Thus EqGap and truncated rank addition are uniformly FO-interdefinable over the ordered generic family.

By Section 7:

\[
\boxed{
\operatorname{EqGap}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

## 12. Minimality claim — REPAIRED

The stronger claim

\[
\text{“EqGap is the first/weakest possible departure from the order wall”}
\]

is not established and should not be used.

There can be enrichments not definable in FO[<] that are still strictly weaker than full addition, for example suitable modular/counting information.

The correct statement is:

\[
\boxed{
\text{EqGap is a canonical gateway to full additive leakage.}
}
\]

Accordingly the safe programme map is:

- `AL0` — exact order wall: generic uniform FO power is exactly FO[<];
- optional intermediate non-order/counting zone (`AL-MOD` as working notation);
- `AL1` — additive gateway: EqGap / truncated rank addition;
- `AL2` — full-arithmetic gateway: a uniform interpretation of full first-order arithmetic, or an independently audited equivalent criterion.

`AL-MOD` is only a placeholder for possible intermediate strength and is not asserted to be a single canonical level.

## 13. Classical arithmetic calibration — CONFIRMED WITH SCOPE DISCIPLINE

Classical calibration used by the programme is sound when kept in the infinite standard-natural-number setting:

- Presburger arithmetic with addition is decidable, so variable multiplication is not first-order definable there;
- Julia Robinson's 1949 result defines addition of positive integers from multiplication together with successor;
- successor is definable from order on the standard natural-number chain.

Therefore multiplication together with order reaches full first-order arithmetic strength on the standard infinite natural numbers.

This calibration is not needed to prove the finite G4-A collapse and should not be silently transferred to arbitrary finite FCOA carriers.

## 14. Arithmetic-import firewall — CONFIRMED

All rank expressions in the left-wall argument occur only in the metalanguage to specify external comparison relations.

No proof step assumes that rank, numerical difference, addition, multiplication, or the external labels \(i,j\) are already internally available in G4-A.

The only internally recovered generic structure used by the collapse theorem is the total order \(<_G\).

Thus there is no hidden arithmetic import in the proof.

## 15. Final verdict table

| Claim | Verdict | Audit result |
|---|---|---|
| Fixed finite-copy reduction of G4-A to finite order | REPAIRED | Correct as a deterministic parameter-free 7-copy FO transduction/copying interpretation; avoid blurring interpretation formalisms. |
| Intrinsic recovery of \(P_0,P_1,G_N,\Omega_+,<_G\) | CONFIRMED | Exact in the one-sorted relational graph signature. |
| Generic FO Collapse | CONFIRMED | Uniform generic FO relations are exactly uniform FO[<] relations. |
| No uniform truncated rank addition | CONFIRMED | Would define parity of finite-chain size. |
| No uniform truncated rank multiplication | CONFIRMED | Rank-2-times-variable test defines the same parity; \(m=2\) is harmless. |
| Successor/betweenness add no FO power once order is recovered | CONFIRMED | Both are definable from order. |
| Infinite G4-A cannot FO-interpret full arithmetic | CONFIRMED | Decidability transfer from \((\mathbb N,<)\). |
| EqGap and truncated addition are uniformly interdefinable | CONFIRMED | Forward-interval and truncation checks pass. |
| EqGap is not uniformly FO-definable in G4-A | CONFIRMED | Follows immediately from Add non-definability. |
| EqGap is globally weakest non-order leakage | REFUTED | Not proved; weaker modular/counting enrichments may intervene. |
| EqGap is a canonical full-additive gateway | CONFIRMED | Exact interdefinability with truncated addition. |
| AL0/AL1/AL2 programme | REPAIRED | Insert/allow an intermediate non-order zone; define AL2 semantically by full-arithmetic interpretation. |
| Classical Presburger/Robinson calibration | CONFIRMED | Keep the standard infinite-arithmetic scope explicit. |

## 16. Fixed left-wall theorem

The hostile-audited theorem is therefore:

### G4-A Generic Order-Wall Theorem

For the one-sorted relationalized G4-A family \(\{\mathfrak A_N^T:N\ge3\}\), and every fixed arity \(r\), a family of relations

\[
R_N\subseteq G_N^r
\]

is uniformly parameter-free first-order definable in G4-A iff its increasing-order transport to \([N-1]^r\) is uniformly first-order definable in the language of finite linear order.

Consequently neither canonical truncated rank addition nor canonical truncated rank multiplication nor directed equal-gap geometry is uniformly first-order definable in G4-A.

The exact generic order, successor and betweenness are uniformly definable.

The infinite G4-A analogue has decidable first-order theory and cannot first-order interpret full standard arithmetic.

Thus G4-A is an exact **order wall** for the present uniform FO programme.

## 17. Next admissible main-line question

The left wall is now sufficiently sharp to move forward, but the target must be stated correctly.

There are two distinct optimization problems:

\[
\boxed{
\text{What is the cheapest FCOA mechanism that leaves }FO[<]?
}
\]

and

\[
\boxed{
\text{What is the cheapest FCOA mechanism that reaches EqGap / additive leakage?}
}
\]

These questions need not have the same answer.

No arbitrary G5 operation table is authorized merely by branch numbering.
