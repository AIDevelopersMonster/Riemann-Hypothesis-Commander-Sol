# Hostile Audit Prompt — Arithmetic Leakage Left Wall after G4-A

Use this prompt with an independent reviewer. The reviewer should derive the conclusions independently and must not assume the candidate note is correct.

---

You are performing a hostile audit of the proposed **Arithmetic Leakage Boundary** for the FCOA G4-A family.

Your job is not to improve the exposition. Your job is to find any logical gap, hidden strengthening of the signature, invalid finite-model-theory inference, incorrect interpretation/transduction claim, or accidental import of index arithmetic.

Do not assume any requested conclusion. Classify every principal claim as `CONFIRMED`, `REPAIRED`, or `REFUTED`.

## 1. Exact G4-A structure

For every \(N\ge3\), let

\[
X_N=\{P_0,P_1,P_2,\dots,P_N\},
\qquad
G_N=\{P_2,\dots,P_N\}.
\]

All indices are external construction labels only.

The partial multiplication has the M0 cells

\[
P_0\otimes P_i=P_0
\qquad(1\le i\le N),
\]

\[
P_i\otimes P_0=E_i^\ast
\qquad(2\le i\le N),
\]

\[
P_1\otimes P_i=P_i,
\qquad
P_i\otimes P_1=P_i
\qquad(2\le i\le N),
\]

\[
P_i\otimes P_i=E_i^\times
\qquad(2\le i\le N).
\]

For every distinct generic pair add

\[
P_i\otimes P_j=
\begin{cases}
\Omega_+,&i<j,\\
\Omega_-,&i>j,
\end{cases}
\qquad 2\le i,j\le N,\ i\ne j.
\]

Finally add the anchor

\[
P_1\otimes P_0=\Omega_+.
\]

All unspecified cells are UNDEF. Every \(E_i^\ast,E_i^\times,\Omega_+,\Omega_-\) is terminal: no further multiplication with a terminal output as an argument is defined.

The \(E\)-subscripts are bookkeeping labels, not named constants. \(\Omega_+,\Omega_-\) are anonymous terminal outputs; the anchor is supposed to make \(\Omega_+\) internally recoverable rather than named by the language.

The previously audited G4 result may be used only as a structural fact if you independently verify the exact consequence you need:

- the generic order is intended to be internally recoverable in G4-A;
- no internal addition or multiplication on external indices is explicitly part of the signature.

## 2. External comparison relations

For metamathematical comparison only, define

\[
\operatorname{rk}_N(P_{k+2})=k,
\qquad 0\le k<N-1.
\]

This rank map is **not** in the FCOA language.

Define external truncated rank graphs

\[
\operatorname{Add}_N(x,y,z)
\iff
\operatorname{rk}_N(z)=\operatorname{rk}_N(x)+\operatorname{rk}_N(y)<N-1,
\]

\[
\operatorname{Mul}_N(x,y,z)
\iff
\operatorname{rk}_N(z)=\operatorname{rk}_N(x)\operatorname{rk}_N(y)<N-1.
\]

The question is whether a **single parameter-free first-order formula in the exact G4-A signature** defines either graph uniformly for all \(N\).

## 3. Audit the order-reduction claim

Independently determine whether the full G4-A family is uniformly reducible to finite linear orders by a fixed finite-copy FO interpretation/transduction.

The intended construction uses:

- one copy for generic points;
- one copy for \(E_i^\ast\);
- one copy for \(E_i^\times\);
- finitely many fixed boundary/output tags representing \(P_0,P_1,\Omega_+,\Omega_-\);
- only equality, copy-tags and the finite linear order to define the graph of the partial operation.

Audit all formal details:

1. Is a fixed finite-copy FO transduction genuinely sufficient to create the required tagged copies and fixed singleton tags?
2. If standard FO interpretations do not permit literal new singleton constants, give a formally correct coding/transduction variant instead of silently assuming them.
3. Does the construction preserve the fact that \(\Omega_+\) is not named in the target language?
4. Is the operation graph uniformly definable from order for every \(N\ge3\)?
5. Does a uniform FO-definable relation in the G4-A structures necessarily pull back to a uniform FO-definable relation on the source finite orders?
6. Are there any hidden parameters, variable copy numbers, or size-dependent formulas?

Give a precise theorem statement in the formalism you regard as correct: FO interpretation, finite-copy interpretation, FO transduction, or another standard notion. Do not blur these notions.

## 4. Audit the finite order wall

Independently test the claim that neither \(\operatorname{Add}_N\) nor \(\operatorname{Mul}_N\) is uniformly parameter-free FO-definable in G4-A.

### Addition test

If uniform truncated rank addition were definable, examine the sentence based on the maximum element \(M\):

\[
\exists x\,\operatorname{Add}(x,x,M).
\]

Determine exactly which finite chain cardinalities it recognizes and whether this really contradicts a standard FO inexpressibility theorem for finite linear orders.

### Multiplication test

If uniform truncated rank multiplication were definable, examine a uniformly order-definable element of rank \(2\), call it \(T\), and the sentence

\[
\exists x\,\operatorname{Mul}(T,x,M).
\]

Check:

- all small-chain exceptions;
- whether rank \(2\) is uniformly definable where required;
- whether finite exceptional cardinalities can legitimately be patched by FO sentences;
- whether the parity contradiction is valid.

### Classical theorem discipline

Do not merely say "FO cannot count parity." State the exact classical fact needed and the precise class of finite structures/language to which it applies.

If parity is the wrong separating property, replace the argument with a correct EF-game, star-free-language, locality, or other standard proof.

## 5. Successor and betweenness

Audit the expressive-power statements concerning successor.

On each finite total order, check that

\[
\operatorname{Succ}(x,y)
\iff
x<y\land\neg\exists z(x<z<y)
\]

is uniform FO.

Then decide whether the following inference is valid:

> If uniform rank addition/multiplication were FO-definable from the pure successor reduct, then it would also be FO-definable from order, because successor itself is FO-definable from order.

Separately audit the infinite statement that pure successor on \(\mathbb N\) does not FO-define the full transitive order. Do not conflate finite uniform definability with definability in the single infinite structure.

## 6. Audit the infinite G4-A analogue

Let \(G_\infty=P_2<P_3<\cdots\) and define the same G4-A operation on all generic pairs, with the same boundary and terminal-output pattern.

Audit the proposed chain of reasoning:

1. the infinite G4-A structure is FO interpretable/transducible in \((\mathbb N,<)\);
2. its first-order theory is therefore decidable;
3. consequently it cannot parameter-free FO interpret \((\mathbb N,+,\times)\).

Check every qualification:

- Is decidability preserved under the chosen interpretation/transduction formalism?
- Is "parameter-free" essential here?
- Would interpretation with finitely many definable or named parameters change the conclusion?
- Is the undecidability fact needed merely undecidability of \(\operatorname{Th}(\mathbb N,+,\times)\), or a stronger noncomputability statement?
- Does the exact one-sorted terminal-output structure create any hidden complication?

Also audit the claim that the pure successor structure gives the same no-full-arithmetic obstruction by decidability.

## 7. Audit the equal-gap gateway

Externally define the directed equal-gap relation on forward intervals:

\[
\operatorname{EqGap}_N(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c),
\]

with \(a\le b\) and \(c\le d\).

Let \(0_G\) be the least generic point.

Independently test both directions of the proposed interdefinability:

\[
\operatorname{Add}(x,y,z)
\ ?\iff ?\ 
\operatorname{EqGap}(0_G,y;x,z),
\]

and

\[
\operatorname{EqGap}(a,b;c,d)
\ ?\iff ?\ 
\exists s\,[\operatorname{Add}(a,s,b)\land\operatorname{Add}(c,s,d)].
\]

Check carefully:

- forward-interval conditions;
- truncation at the end of the finite chain;
- whether the witness \(s\) always exists as an element of the same generic sector;
- whether the least generic point is uniformly parameter-free definable in G4-A;
- whether this gives genuine FO interdefinability of the **families**, not only a metamathematical numerical identity.

If correct, decide whether non-definability of Add immediately yields non-definability of EqGap in G4-A.

## 8. Audit the leakage-level terminology

The proposed programme levels are:

- `AL0`: exact order, hence successor/betweenness, but no uniform canonical rank addition or multiplication;
- `AL1`: variable equal-gap / truncated rank addition becomes uniformly definable;
- `AL2`: multiplication-level structure or another uniform interpretation of full first-order arithmetic.

Audit whether these levels are logically coherent.

In particular:

1. Is `AL1` genuinely Presburger-like, or does finite truncation require more cautious wording?
2. Is multiplication plus order really enough for full arithmetic in the exact classical sense being invoked?
3. State the correct classical theorem and signature for definability of addition from multiplication plus order/successor, or flag the claim if the citation is too loose.
4. Does AL2 need to be defined semantically as "uniformly interprets full arithmetic" rather than syntactically by the presence of a multiplication graph?

Treat terminology as working terminology; do not infer novelty.

## 9. Arithmetic-import firewall

Look specifically for hidden arithmetic import.

The candidate boundary note uses ranks only externally to state comparison relations. Determine whether any proof step illegitimately treats rank addition, rank multiplication, numerical distance, or the external labels \(i,j\) as internally available before it has been defined.

Distinguish:

\[
\text{external metamathematical definition}
\quad\text{vs}\quad
\text{internal FO definability}.
\]

This distinction is central to the audit.

## 10. Required final verdict

End with a compact table containing at least these claims:

1. G4-A uniform reduction to finite linear order;
2. no uniform FO truncated rank addition;
3. no uniform FO truncated rank multiplication;
4. successor/betweenness add no expressive strength over already recovered finite order;
5. infinite G4-A does not FO interpret full arithmetic;
6. EqGap and truncated addition are uniformly interdefinable over ordered generic sectors;
7. EqGap is not uniformly FO-definable in G4-A;
8. AL0/AL1/AL2 ladder is mathematically coherent after any necessary repairs;
9. classical literature calibration is correctly stated.

For each use exactly one status:

- `CONFIRMED`
- `REPAIRED`
- `REFUTED`

Then state:

- every repair needed in the theorem statements;
- every small-case exception;
- the weakest formally correct version of the left-wall theorem that survives;
- whether the main line is justified in treating variable equal-gap geometry as the first natural target beyond G4-A.

Do not propose a new G5 construction until the left wall has been settled.
