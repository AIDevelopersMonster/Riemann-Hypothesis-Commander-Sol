# G4-A Generic FO Collapse — Exact Order-Wall Formulation

**Project:** FCOA Admissibility Geometry  
**Status:** main-line theorem candidate; to be audited together with `ARITHMETIC_LEAKAGE_BOUNDARY.md`  
**Scope:** post-publication, no new G5 cells

## 1. Purpose

The Arithmetic Leakage left wall can be stated more sharply than merely saying that canonical rank addition and multiplication are not uniformly definable.

For generic tuples, the entire first-order expressive power of G4-A is exactly the first-order expressive power of the recovered finite linear order.

This gives an exact classification of the G4-A generic FO layer.

## 2. Relationalized signature

To avoid any ambiguity about partial function symbols, relationalize the partial operation by a ternary graph

\[
T(x,y,z)
\iff
x\otimes_{4A}y=z.
\]

Let \(\mathfrak A_N^T\) be the resulting one-sorted relational structure containing

\[
P_0,P_1,P_2,\ldots,P_N,
\]

all

\[
E_i^\ast,E_i^\times
\qquad(2\le i\le N),
\]

and

\[
\Omega_+,\Omega_-.
\]

No constants or unary sort predicates are added to the target language.

## 3. Parameter-free finite-copy transduction from order

Put

\[
m=N-1
\]

and let

\[
L_m=([m],<)
\]

be the finite chain whose elements correspond externally to the generic points in increasing order.

Use seven fixed copy indices

\[
g,e_\ast,e_\times,b_0,b_1,w_+,w_-.
\]

The copy indices belong to the transduction mechanism; they are not symbols of the target language.

Let

\[
\operatorname{Min}(x)
\iff
\neg\exists y\,(y<x).
\]

The transduction universe consists of:

- \((g,x)\) for every \(x\in[m]\);
- \((e_\ast,x)\) for every \(x\in[m]\);
- \((e_\times,x)\) for every \(x\in[m]\);
- \((b_0,x),(b_1,x),(w_+,x),(w_-,x)\) only when \(\operatorname{Min}(x)\).

Because a finite nonempty chain has a unique minimum, the last four copies each contribute exactly one element.

Interpret

\[
(g,x)\leftrightarrow P_{x+2},
\]

metamathematically, with the understanding that \(x+2\) is only a description of the external identification and is not used by any target formula.

Similarly,

\[
(e_\ast,x)\leftrightarrow E_{x+2}^\ast,
\qquad
(e_\times,x)\leftrightarrow E_{x+2}^\times,
\]

while the four minimum-supported singleton copies represent

\[
P_0,P_1,\Omega_+,\Omega_-.
\]

The ternary graph \(T\) is defined by the following fixed copy cases:

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
(g,x)\otimes(g,y)=w_+
\qquad\text{iff }x<y,
\]

\[
(g,x)\otimes(g,y)=w_-
\qquad\text{iff }y<x,
\]

and

\[
b_1\otimes b_0=w_+.
\]

No other triple belongs to \(T\).

Every defining clause is first-order in \(( [m],< )\), the number of copies is fixed, and no parameter or size-dependent formula is used.

Hence:

### Theorem 3.1 — parameter-free order transduction

The family

\[
\{\mathfrak A_N^T:N\ge3\}
\]

is the image of the family of finite linear orders

\[
\{L_{N-1}:N\ge3\}
\]

under one fixed parameter-free finite-copy FO transduction.

In particular, every uniform target FO formula translates effectively to one uniform FO formula over finite linear orders.

## 4. Intrinsic recovery of the generic order

The converse direction uses only the target relation \(T\).

Define activity as an argument:

\[
\operatorname{Act}(x)
\iff
\exists y,z\,[T(x,y,z)\lor T(y,x,z)].
\]

Define the left-zero boundary point:

\[
B_0(x)
\iff
\operatorname{Act}(x)
\land
\exists y\,T(x,y,x)
\land
\forall y,z\,(T(x,y,z)\to z=x).
\]

In G4-A this defines exactly \(P_0\).

Define

\[
B_1(x)
\iff
\operatorname{Act}(x)
\land
\neg B_0(x)
\land
\neg\exists z\,T(x,x,z).
\]

This defines exactly \(P_1\): terminal points are inactive, while every generic point has a diagonal product.

Define the generic sector by

\[
G(x)
\iff
\operatorname{Act}(x)
\land
\exists z\,T(x,x,z).
\]

This defines exactly \(G_N\).

Define the anchored positive-orientation output by

\[
W_+(w)
\iff
\exists b_0,b_1\,
[B_0(b_0)\land B_1(b_1)\land T(b_1,b_0,w)].
\]

This defines exactly \(\Omega_+\), without naming it.

Finally define

\[
x<_{G}y
\iff
G(x)\land G(y)
\land
\exists w\,[W_+(w)\land T(x,y,w)].
\]

Then \(<_G\) is exactly

\[
P_2<P_3<\cdots<P_N.
\]

Thus the generic finite order is uniformly parameter-free definable in the one-sorted relationalized G4-A family.

## 5. Generic FO Collapse Theorem

For each arity \(r\), let

\[
R_N\subseteq G_N^r
\]

be a family of relations, and identify generic tuples with tuples from \([N-1]^r\) through the external increasing correspondence.

### Theorem 5.1 — Generic FO Collapse

The following are equivalent:

1. there is one parameter-free FO formula in the G4-A relational signature \(\{T\}\) defining \(R_N\) for every \(N\ge3\);
2. there is one FO formula in the language \(\{<\}\) defining the corresponding relation on \([N-1]^r\) for every \(N\ge3\).

### Proof

`(1) => (2)` follows by translating the target formula through the fixed finite-copy FO transduction of Theorem 3.1 and restricting each free variable to the generic copy.

`(2) => (1)` follows by replacing every occurrence of the source order with the uniformly target-definable relation \(<_G\) from Section 4 and restricting variables to \(G\).

\(\square\)

Therefore:

\[
\boxed{
FO(\text{G4-A on generic tuples})
=
FO(\text{finite linear order}),
}
\]

in the uniform family sense.

This is the exact left-wall statement.

## 6. Direct finite-order obstruction by EF games

A standard Ehrenfeucht-Fraisse fact for finite linear orders is:

> For quantifier rank \(q\), sufficiently long finite linear orders of consecutive sizes are \(q\)-equivalent; one convenient standard bound is that any two finite chains of sizes at least \(2^q\) are indistinguishable by rank-\(q\) FO sentences.

Hence no single FO sentence in the language of order defines parity of the size of finite linear orders: for \(q\ge1\), the chains of sizes

\[
2^q
\quad\text{and}\quad
2^q+1
\]

have opposite parity but are rank-\(q\) equivalent.

This supplies the finite-model-theoretic obstruction used below without relying on informal statements that FO simply “cannot count.”

## 7. Consequences for canonical arithmetic graphs

Let rank be external only:

\[
\operatorname{rk}_N(P_{k+2})=k.
\]

### Addition

If truncated rank addition were uniformly FO-definable in G4-A, it would be uniformly FO-definable in finite order by Theorem 5.1.

Let \(M\) be the maximum generic point. Then

\[
\exists x\,\operatorname{Add}(x,x,M)
\]

holds exactly when

\[
N-2=m-1
\]

is even, equivalently when \(m\) is odd.

This would define parity of finite-chain size, contradiction.

Therefore

\[
\boxed{
\operatorname{Add}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

### Multiplication

For chains of size at least three, the point of rank \(2\) is uniformly FO-definable from order. Let it be \(T_2\), and let \(M\) be maximum.

Then

\[
\exists x\,\operatorname{Mul}(T_2,x,M)
\]

holds exactly when \(m-1\) is even. For the only family case without a rank-2 point, \(m=2\), the sentence is false and \(m\) is even, so no exceptional repair is needed beyond defining the rank-2 witness by an existential formula.

Hence uniform truncated multiplication would again define finite-chain parity, contradiction.

Therefore

\[
\boxed{
\operatorname{Mul}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

## 8. What this theorem does and does not say

The collapse theorem is stronger than the two arithmetic corollaries: **every** uniform relation on generic tuples available in G4-A is already FO-definable from finite order.

It follows, for example, that no fixed-rank parity predicate can be uniformly recovered in G4-A if that predicate is not FO-definable in finite order.

However, this does **not** prove that equal-gap geometry is the globally weakest possible extension beyond G4-A. There are weaker non-order-definable enrichments, for example modular/counting predicates, which need not recover full addition.

Therefore the correct strategic statement is:

\[
\boxed{
\text{EqGap is a canonical gateway to full additive leakage, not a proved minimal leakage relation.}
}
\]

This distinction must be preserved in the Arithmetic Leakage programme.

## 9. Additive gateway remains exact

For forward intervals define externally

\[
\operatorname{EqGap}_N(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c).
\]

Let \(0_G\) be the least generic element, uniformly definable from \(<_G\).

Then

\[
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_G,y;x,z).
\]

Conversely,

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,
[
\operatorname{Add}(a,s,b)
\land
\operatorname{Add}(c,s,d)
],
\]

for forward intervals. The witness \(s\) represents their common nonnegative gap and always lies in the same generic sector because any gap occurring inside an \(m\)-element chain is at most \(m-1\).

Thus EqGap and truncated rank addition are uniformly FO-interdefinable once either is supplied.

Combining this with Section 7:

\[
\boxed{
\operatorname{EqGap}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

## 10. Refined leakage map

The exact collapse theorem suggests distinguishing two questions:

1. **first departure from the order wall** — any relation not uniformly FO-definable from finite order;
2. **first full additive gateway** — a relation interdefinable with truncated rank addition, such as EqGap.

Accordingly, do not use `AL1` to mean “the first conceivable non-order relation.”

A safe working map is:

- **AL0 — Order wall:** generic FO power is exactly FO of linear order;
- **AL-MOD / intermediate counting leakage:** optional intermediate zone for modular or other non-order-definable information that does not yet recover addition;
- **AL1 — Additive gateway:** EqGap / truncated rank addition becomes uniformly definable;
- **AL2 — Full-arithmetic gateway:** an enrichment reaches a uniform interpretation of full first-order arithmetic, or an equivalent audited criterion.

The intermediate zone is included to avoid a false minimality claim.

## 11. Infinite analogue

The same seven-copy parameter-free transduction works over

\[
(\mathbb N,<),
\]

using the unique minimum to create the four singleton copies.

Hence the infinite G4-A analogue is FO interpretable in a decidable structure, so its first-order theory is decidable.

It therefore cannot parameter-free FO interpret

\[
(\mathbb N,+,\times),
\]

whose complete first-order theory is undecidable.

This is an infinite order-wall calibration, separate from the finite uniform-family theorem above.

## 12. Classical calibration

The finite parity obstruction is standard finite model theory / Ehrenfeucht-Fraisse theory for linear orders.

For the infinite arithmetic comparison:

- Presburger arithmetic \((\mathbb N,+)\), equivalently with order added, has decidable first-order theory, so variable multiplication is not FO-definable there;
- Julia Robinson proved that addition of positive integers is arithmetically definable from multiplication together with successor. Since successor is definable from order on \(\mathbb N\), this calibrates the infinite structure with multiplication plus order at full first-order arithmetic strength.

These are classical calibration results, not FCOA novelty claims.

## 13. Status

\[
\boxed{
\mathbf W:\ \text{Generic FO Collapse and Arithmetic Leakage left wall; hostile audit pending.}
}
\]

No new operation cells have been added.
