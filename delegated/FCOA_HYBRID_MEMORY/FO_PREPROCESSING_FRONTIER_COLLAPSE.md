# FCOA Hybrid Memory — FO Preprocessing Frontier Collapse

**Status:** standard-model no-go theorem  
**Scope:** fixed finite relational signature, static preprocessing structure, uniform FO query decoder

## 1. Standard database-style model

For each `N`, let `X_N` be an `N`-element target sector inside a finite relational structure `A_N` over one fixed finite signature of bounded arity.

The structure `A_N` is the preprocessed memory. Its storage size is

\[
S(A_N)=|A_N|+\sum_R |R^{A_N}|.
\]

A target relation such as order, truncated addition, or truncated multiplication is recovered by one fixed FO formula over `A_N`.

For phase `j in {0,1,2}` and quantifier-rank budget `q`, define

\[
\sigma_j(q)
=
\inf \limsup_{N\to\infty}
\frac{\log S(A_N)}{\log N},
\]

where the infimum ranges over presentations whose decoder has quantifier rank at most `q` and recovers the canonical AL-j benchmark on `X_N`.

Because the target sector itself contains `N` elements,

\[
\boxed{\sigma_j(q)\ge1}
\]

whenever the phase is realizable.

---

## 2. Why bit-level NC0 is not the right target model

If target elements are supplied to the decoder by their external binary names, a bounded-fan-in constant-depth Boolean circuit can inspect only constantly many input bits. Even comparing two arbitrary `log N`-bit names is therefore outside strict NC0.

This is incompatible with the FCOA semantics, where elements are anonymous and their order/arithmetic must be stored structurally.

The natural standard model is instead database-style FO query evaluation after preprocessing: query variables denote structure elements directly and formulas access preprocessed relations.

---

## 3. Linear-space AL0 with constant quantifier rank

Take

\[
N=b^2
\]

for clarity, with the usual rectangular adjustment for arbitrary `N`.

Use two auxiliary coordinate sets

\[
B=P=\{0,\ldots,b-1\}.
\]

Store for every target `x_{i,j}` its block and position coordinates by binary relations

\[
C_B(x_{i,j},i),
\qquad
C_P(x_{i,j},j).
\]

This uses `2N` tuples.

Store the complete strict orders on `B` and `P`. Each contains `Theta(b^2)=Theta(N)` tuples.

Then lexicographic target order is defined by one fixed FO formula:

\[
\begin{aligned}
x<y \iff \exists i,j,k,l\;(&C_B(x,i)\land C_P(x,j)\land
C_B(y,k)\land C_P(y,l)\\
&\land(i<_B k\lor(i=k\land j<_P l))).
\end{aligned}
\]

Thus for some absolute constant `Q_0`,

\[
\boxed{\sigma_0(q)=1\quad\text{for every }q\ge Q_0.}
\]

---

## 4. Linear-space AL1 with constant quantifier rank

Use a two-digit base-`b` representation of target values and store:

1. the two digit-coordinate relations of all targets: `Theta(N)` tuples;
2. the complete digit add-with-carry table on the `b`-element digit alphabet: `Theta(b^2)=Theta(N)` tuples;
3. the coordinate order needed for canonical target order: `Theta(N)` tuples.

A fixed school-addition FO formula quantifies the constant number of digit/carry witnesses and recovers exact truncated addition.

Therefore for some absolute constant `Q_1`,

\[
\boxed{\sigma_1(q)=1\quad\text{for every }q\ge Q_1.}
\]

This is the standard-relational restatement of the earlier linear digit/CRT constructions.

---

## 5. Linear-space AL2 with constant quantifier rank

In the same two-digit presentation, additionally store the complete digit multiply-and-split table

\[
P(a,b;h,r),
\]

with one row for every ordered pair of bottom digits. Its size is

\[
b^2=N.
\]

The fixed school-multiplication formula from the digit no-go theorem uses only a constant number of coordinate, product, and carry witnesses because the number of target digits is fixed.

Hence for some absolute constant `Q_2`,

\[
\boxed{\sigma_2(q)=1\quad\text{for every }q\ge Q_2.}
\]

Combining with the unavoidable target-size lower bound gives equality.

---

## 6. FO Preprocessing Collapse Theorem

### Theorem HM-FOPC

In the unrestricted static-preprocessing / uniform-FO-query model over a fixed finite bounded-arity relational signature, there are constants

\[
Q_0,Q_1,Q_2<\infty
\]

such that

\[
\boxed{
\sigma_0(q)=\sigma_1(q)=\sigma_2(q)=1
}
\]

for every

\[
q\ge \max(Q_0,Q_1,Q_2).
\]

Therefore ordinary FO query depth after unrestricted linear-size preprocessing does **not** yield an asymptotic space separation between order, addition, and multiplication.

The arithmetic phase can be precompiled into a linear-size finite relational data structure and decoded by one fixed FO formula.

---

## 7. Exact quantifier-free endpoint

The opposite endpoint `q=0` is also informative.

Assume a fixed finite relational signature with no function symbols and a quantifier-free decoder `phi(x,y)` for a strict total order on `X_N`.

Unary atoms provide only finitely many unary types. Hence some unary type contains `Omega(N)` target points.

Suppose the total number of stored relation tuples involving two or more target points were `o(N^2)`. Then among the `Omega(N^2)` ordered pairs `(x,y)` of distinct points of the large common unary type, one can choose a pair for which all non-equality atomic relations on `(x,y)` and `(y,x)` are false (and similarly for the finitely many fixed permutations of variables occurring in `phi`).

The quantifier-free atomic diagrams of `(x,y)` and `(y,x)` are then identical. Consequently

\[
\phi(x,y)\iff\phi(y,x),
\]

contradicting strict total order.

Therefore any quantifier-free relational presentation of an `N`-point strict total order requires

\[
\Omega(N^2)
\]

stored tuples. The direct order relation gives the matching upper bound.

Hence

\[
\boxed{\sigma_0(0)=2.}
\]

Since AL1 and AL2 include the canonical order benchmark,

\[
\boxed{\sigma_1(0)=\sigma_2(0)=2.}
\]

under the same convention.

---

## 8. The resulting frontier bracket

The standard FO-preprocessing model therefore has a genuine storage/query-depth tradeoff, but the currently proved endpoints are common to all three phases:

\[
\boxed{
\sigma_j(0)=2,
\qquad
\sigma_j(q)=1\text{ for all sufficiently large constant }q,
\qquad j=0,1,2.
}
\]

Thus the asymptotic exponent frontier drops from quadratic direct materialization to linear compressed preprocessing, but **does not distinguish the AL hierarchy at the endpoints**.

Possible differences can only live in the finite intermediate quantifier-rank window before the common linear plateau.

---

## 9. Relation to standard FO query-evaluation literature

This model is aligned with the standard database/FMT separation between preprocessing and query evaluation. Classical results show that on bounded-degree or bounded-expansion structures, fixed FO queries admit linear preprocessing and constant-delay enumeration.

Those results are algorithmic upper bounds on restricted input classes, not the storage lower bounds studied here. Nevertheless they confirm that “linear preprocessing + logically simple query phase” is a standard research architecture rather than an FCOA-specific invention.

The present theorem differs in that the preprocessing structure itself is designed as a memory representation of a target algebraic phase.

---

## 10. Why bounded-degree preprocessing is too restrictive

If the preprocessed structures are required to have uniformly bounded Gaifman degree, the earlier Gaifman-locality theorem blocks uniform order on an unbounded target sector altogether.

Hence bounded-degree FO preprocessing lies entirely below AL0 and cannot serve as a model separating AL0 from AL2.

The useful standard model must allow sparse but unbounded-degree coordinate/index nodes.

---

## 11. What remains open

The theorem rules out a broad strategy:

\[
\boxed{
\text{unrestricted linear preprocessing} + \text{bounded FO query rank}
}
\]

cannot yield a persistent asymptotic exponent separation once the quantifier-rank budget exceeds a fixed constant.

The remaining possible standard frontiers are finer:

1. exact values of `sigma_j(q)` for small/intermediate fixed `q`;
2. bounded-variable FO rather than quantifier rank alone;
3. guarded/immersive/local FO query decoders with an additional dependency-width restriction;
4. preprocessing restricted by width/tree-depth/degree growth rather than only total space;
5. multi-resource frontiers combining space, decoder rank, variables, and structural width.

---

## 12. Research consequence

The standard-model strike gives a clean diagnosis:

\[
\boxed{
\text{FO preprocessing space alone has the same asymptotic exponent for AL0, AL1, AL2.}
}
\]

So the phase distinction cannot be recovered merely by moving from FCOA-specific factor circuits to unrestricted standard FO query evaluation.

The next promising standard parameter is **decoder variable-width / guarded dependency width**, because the digit constructions pay for arithmetic by simultaneously coordinating several local witnesses, while pure order needs fewer interacting coordinates.

This moves the search from a one-dimensional space-vs-rank curve to a standard finite-variable / pebble-game setting where genuine lower-bound tools exist.

## 13. Literature calibration

Relevant standard interfaces include:

- Wojciech Kazana and Luc Segoufin, *First-order query evaluation on structures of bounded degree* (linear preprocessing and constant-delay query enumeration);
- Kazana and Segoufin, *First-order queries on classes of structures with bounded expansion*;
- Braunfeld, Nešetřil, Ossona de Mendez, Siebertz, *On first-order transductions of classes of graphs* for strongly local/immersive transduction normal forms.
