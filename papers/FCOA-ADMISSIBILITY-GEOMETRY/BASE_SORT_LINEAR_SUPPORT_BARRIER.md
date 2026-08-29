# Base-Sort Linear Support Barrier for Exact AL1

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-29  
**Status:** central theorem; proof complete with internal hostile audit  
**Backend:** `FCOA_DEFINITION_1_0.md`, `FCOA_MORPHISMS_EQUIVALENCE_REPRESENTATION_1_0.md`  
**Companion upper bound:** `INTERNAL_DIGIT_SCAFFOLD_AND_DIMENSION_COLLAPSE.md`

---

## 1. Central question

After the internal digit construction, exact additive leakage can be obtained on the **same explicit `N`-element base carrier** with only

\[
\Theta(N)
\]

additional primitive support.

The remaining question was whether one could do better:

\[
\boxed{
\text{Can canonical truncated addition be uniformly FO-recovered with }o(N)
\text{ charged added support?}
}
\]

The answer is **no** in a broad base-sorted finite-signature model, even if the added relations are arbitrary, varied with `N`, and may encode global size-oracle bits.

The obstruction is not Presburger semilinearity. It is simpler and more robust:

> sublinear fixed-arity support leaves an arbitrarily long interval of the ordered carrier untouched by every added primitive tuple; inside that clean interval, bounded-rank first-order logic cannot compare two unbounded variable distances.

This gives a linear lower bound for exact AL1.

---

## 2. Model and cost convention

Let

\[
X_N=\{0,1,\ldots,N-1\}
\]

with the background linear order `<`.

Fix once and for all a finite relational signature

\[
\tau=\{R_1,\ldots,R_s\}
\]

of maximum arity

\[
r=\max_i\operatorname{arity}(R_i)<\infty.
\]

For every `N`, the interpretations

\[
R_{i,N}\subseteq X_N^{\operatorname{arity}(R_i)}
\]

may be chosen **arbitrarily** and may depend on `N` in any way.

The structure is

\[
\mathfrak A_N=(X_N,<,R_{1,N},\ldots,R_{s,N}).
\]

The added primitive tuple cost is

\[
S(N)=\sum_{i=1}^s |R_{i,N}|.
\]

The dense background order `<` is the already-available AL0 substrate and is not charged as new memory.

Fixed finitely many constant symbols or zero-ary size bits are allowed; they only add `O(1)` exceptional carrier points or global truth values and do not affect the theorem.

---

## 3. Active support

Define the active carrier support of the added relations by

\[
A_N=
\{x\in X_N:
 x\text{ occurs in some tuple of some }R_{i,N}
\}.
\]

Because arity is fixed,

\[
|A_N|\le rS(N).
\tag{3.1}
\]

If there are finitely many named constants, include their interpretations in `A_N`; this changes `|A_N|` by only `O(1)`.

A **clean interval** is a consecutive interval

\[
I\subseteq X_N
\]

with

\[
I\cap A_N=\varnothing.
\]

No true added primitive tuple contains any point of a clean interval.

---

## 4. Long clean intervals from sublinear support

### Lemma 4.1 — Clean-Gap Lemma

If

\[
|A_N|=a_N,
\]

then `X_N\setminus A_N` contains a clean interval of length at least

\[
\left\lfloor
\frac{N-a_N}{a_N+1}
\right\rfloor.
\tag{4.1}
\]

### Proof

The `a_N` active points cut the line into at most `a_N+1` consecutive components of inactive points. Their total length is `N-a_N`. One component therefore has at least the average length. `□`

### Corollary 4.2

If along some infinite subsequence

\[
\frac{S(N)}N\longrightarrow0,
\]

then the corresponding maximum clean-interval length tends to infinity.

This follows from (3.1) and (4.1).

---

## 5. FO indistinguishability inside one clean interval

We use only the standard finite Ehrenfeucht-Fraisse fact for linear orders.

For a quantifier rank `q`, let

\[
T_q=2^{q+1}.
\]

The exact numerical threshold is unimportant; any standard exponential EF threshold works.

### Lemma 5.1 — Clean-Interval Transfer

Fix `q`. Let `I` be a clean interval long enough to contain two increasing four-tuples

\[
\bar a=(a,b,c,d),
\qquad
\bar a'=(a',b',c',d')
\]

such that, relative to the two ends of `I`, every one of the five segments

- before the first marked point;
- between the first and second;
- between the second and third;
- between the third and fourth;
- after the fourth

has length at least `T_q` for both tuples.

Then the two pointed expanded structures

\[
(\mathfrak A_N;\bar a)
\quad\text{and}\quad
(\mathfrak A_N;\bar a')
\]

are `q`-equivalent whenever the corresponding marked points have the same order pattern.

Equivalently, every FO formula of quantifier rank at most `q` has the same truth value on `\bar a` and `\bar a'`.

### Proof

Play the `q`-round EF game between two copies of the **same** expanded structure, with the distinguished tuple interpreted as `\bar a` on one side and `\bar a'` on the other.

Outside `I`, Duplicator responds identically. The arbitrary added relations are then preserved exactly.

Inside `I`, no point participates in any true `R_i`-tuple. Hence every atomic formula involving an added relation and at least one inside point is false on both sides. The only nontrivial atomic information involving inside points is equality and order.

Duplicator therefore uses the ordinary `q`-round EF strategy for the two finite pointed linear intervals. Since all corresponding gaps are at least `T_q`, bounded-rank FO cannot distinguish their exact lengths. Order relations between an inside point and every outside point are also preserved, because every outside point lies entirely to the left or entirely to the right of `I`, and outside points are matched identically.

Thus the partial map remains an isomorphism for the full expanded signature throughout the game. `□`

### Remark 5.2

The lemma is insensitive to:

- arbitrary relations among active points outside `I`;
- arbitrary size dependence of those relations;
- finitely many zero-ary global bits;
- finitely many named constants.

All such information is the same for the two tuples inside the same carrier size.

---

## 6. EqGap cannot live on a long clean interval

For forward intervals define canonical equal-gap relation

\[
\operatorname{EqGap}_N(a,b;c,d)
\iff
b-a=d-c,
\qquad a\le b,\ c\le d.
\]

### Lemma 6.1 — Clean-gap contradiction

For every quantifier rank `q`, there is a constant `L(q)` such that no FO formula of rank at most `q` can define `EqGap_N` in a structure containing a clean interval of length at least `L(q)`.

### Proof

Let

\[
T=T_q.
\]

Inside a sufficiently long clean interval choose

\[
a<b<c<d<d'
\]

so that

\[
b-a=2T,
\]

\[
c-b=2T,
\]

\[
d-c=2T,
\]

\[
d'-c=2T+1,
\]

and both `a` and `d'` remain at least `T` away from the ends of the clean interval.

Then

\[
\operatorname{EqGap}_N(a,b;c,d)
\]

is true, while

\[
\operatorname{EqGap}_N(a,b;c,d')
\]

is false.

However, the two pointed four-tuples

\[
(a,b,c,d)
\quad\text{and}\quad
(a,b,c,d')
\]

satisfy the hypotheses of Lemma 5.1: all relevant order gaps are larger than the EF threshold. Hence they have the same `q`-type in the full expanded structure.

No rank-`q` formula can distinguish them. Contradiction. `□`

One may take, for example,

\[
L(q)=10T_q+10.
\]

No optimization of this constant is needed.

---

## 7. Addition uniformly defines EqGap

Let canonical truncated addition be

\[
\operatorname{Add}_N(x,y,z)
\iff
x+y=z<N.
\]

For forward intervals,

\[
\boxed{
\operatorname{EqGap}_N(a,b;c,d)
\iff
\exists u\,
\bigl(
\operatorname{Add}_N(a,u,b)
\land
\operatorname{Add}_N(c,u,d)
\bigr).
}
\tag{7.1}
\]

The witness is uniquely

\[
u=b-a=d-c<N.
\]

Thus any uniform FO definition of truncated addition yields a uniform FO definition of `EqGap` with only one additional existential quantifier.

---

## 8. Main theorem

### Theorem 8.1 — Base-Sort Linear Support Barrier

Let

\[
\mathfrak A_N=(X_N,<,R_{1,N},\ldots,R_{s,N})
\]

be any family in one fixed finite relational signature of bounded arity. The added relations may vary arbitrarily with `N`.

If canonical truncated addition is uniformly first-order definable in the family, then

\[
\boxed{
S(N)=\Omega(N).
}
\]

Equivalently, no family with

\[
S(N)=o(N)
\]

can uniformly FO-recover exact AL1.

### Proof

Suppose no linear lower bound holds. Then there is an infinite subsequence `N_k` with

\[
\frac{S(N_k)}{N_k}\to0.
\]

By Corollary 4.2, the structures `A_{N_k}` contain clean intervals whose lengths tend to infinity.

Assume a fixed FO formula `\varphi_+(x,y,z)` defines canonical truncated addition. By (7.1), a fixed FO formula `\varphi_{gap}(a,b,c,d)` then defines `EqGap`. Let `q` be its quantifier rank.

For sufficiently large `k`, the clean interval has length at least `L(q)`. Lemma 6.1 says no rank-`q` formula can define `EqGap` in that structure, contradiction.

Therefore such a sublinear subsequence cannot exist. Hence there are constants `c>0` and `N_0` such that

\[
S(N)\ge cN
\]

for all `N>=N_0`. `□`

---

## 9. Explicit quantitative version

The proof gives a formula-dependent constant.

Let `q` be the quantifier rank of the induced EqGap formula and let `L=L(q)` be the forbidden clean-gap length from Lemma 6.1.

If every clean gap has length `<L`, then

\[
N-|A_N|<L(|A_N|+1).
\]

Hence

\[
|A_N|>
\frac{N-L}{L+1}.
\]

Using `|A_N|<=rS(N)+O(1)`,

\[
S(N)
\ge
\frac{1}{r(L+1)}N-O(1).
\]

So the linear constant is determined by the fixed defining formula and maximum primitive arity.

---

## 10. Exact AL1 support scale in the broad base-sorted model

`INTERNAL_DIGIT_SCAFFOLD_AND_DIMENSION_COLLAPSE.md` supplies a finite-signature varied scaffold on the same explicit target carrier with

\[
S(N)=\Theta(N)
\]

and exact semantic phase

\[
\operatorname{FTR}=1.
\]

Combining that upper bound with Theorem 8.1 gives:

### Corollary 10.1 — Exact base-sorted AL1 cost

In the model

- explicit `N`-element ordered target carrier;
- fixed finite bounded-arity added signature;
- no growing auxiliary carrier;
- ordinary FO query language;
- all added primitive tuples charged;
- arbitrary `N`-dependent placement allowed;

we have

\[
\boxed{
C_{AL1}^{\mathrm{base}}(N)=\Theta(N).
}
\]

The upper construction may be exact AL1 rather than AL2, so the optimum is attained without multiplication leakage.

---

## 11. Relation to the Presburger Compression Barrier

There is no conflict with

\[
\Theta(N^2)
\]

from `PRESBURGER_COMPRESSION_BARRIER.md`.

The two theorems optimize over different representation classes:

\[
\boxed{
\begin{array}{c|c}
\text{class} & \text{minimum support for AL1}\\
\hline
\text{fixed unvaried base-sorted Presburger} & \Theta(N^2)\\
\text{arbitrary varied base-sorted finite signature} & \Theta(N)
\end{array}}
}
\]

Thus provenance restrictions create a genuine quadratic-versus-linear phase in representation cost.

The internal digit scaffold achieves the linear regime by using `N`-dependent coordinate factorization.

---

## 12. Relation to the One-Cell Oracle

A one-cell or zero-ary size oracle can encode an arbitrary global bit with `O(1)` support. Therefore no density-only lower bound can hold for **family-level sentence spectra**.

Theorem 8.1 shows a sharply different fact:

\[
\boxed{
O(1)\text{ global oracle leakage does not buy a variable-displacement relation such as EqGap/Add.}
}
\]

The proof is size-internal: both compared tuples live in the same structure `A_N`, so every global oracle bit has the same value on both and cannot distinguish the equal-gap tuple from the unequal-gap tuple.

This cleanly separates:

\[
\text{global size information}
\quad\text{from}\quad
\text{distributed variable-displacement memory}.
\]

---

## 13. FCOA partial-operation corollary

Relationalize every added partial operation by its graph.

Suppose:

- the base carrier is the explicit ordered `X_N`;
- there are only finitely many operation symbols of fixed arity;
- terminal output sorts have uniformly bounded total size, or are finitely many fixed named outputs;
- there is no growing auxiliary carrier;
- every defined operation cell / graph record is charged.

If the total number of added defined cells is `o(N)`, then only `o(N)` base elements can occur in those cells. A long clean base interval remains, and the same EF argument applies.

Hence:

### Corollary 13.1 — FCOA Linear Cell Barrier

Under the above typed base-carrier assumptions, uniform FO recovery of canonical truncated addition requires

\[
\boxed{
\Omega(N)
}

charged operation/incidence cells.

The statement is invariant under fixed constant-factor relational/incidence compilations allowed by the FCOA backend cost protocol.

---

## 14. What the theorem does not cover

The linear barrier is intentionally sharp in scope.

It does **not** automatically cover:

1. growing auxiliary sorts whose internal relations carry information;
2. interpretations that represent target elements by uncharged tuples over a smaller carrier;
3. signatures whose arity grows with `N`;
4. transitive closure, fixed-point, counting or stronger logics in the query language;
5. presentation models in which a total function/table is treated as a free algorithm rather than charged by its graph/cells;
6. compressed external programs whose description length, rather than materialized primitive support, is the chosen cost model.

Those are different resource models and must be analyzed separately.

---

## 15. Hostile audit

### 15.1 Could an arbitrary sparse relation outside the clean interval still distinguish positions inside it?

Only through FO order comparisons to outside points. In the EF game outside points are matched identically, and all points of the same clean interval have the same left/right orientation to every outside point. Exact interior distances beyond the fixed EF threshold remain invisible.

**PASS.**

### 15.2 Could a true primitive relation mix an inside point with an outside point?

No. By definition, every element occurring in any true added tuple belongs to `A_N`; a clean interval contains no such element.

**PASS.**

### 15.3 Could zero-ary size bits defeat the argument?

No. The two candidate tuples are evaluated in the same `N`, so all global bits agree. The distinction needed by EqGap is intra-structure.

**PASS.**

### 15.4 Could one named size-dependent landmark defeat the argument?

A fixed finite number of constants is inserted into `A_N`. It creates only finitely many extra cuts and cannot prevent a long clean interval under sublinear active support.

**PASS.**

### 15.5 Is EqGap really definable from truncated addition without overflow problems?

Yes. For each forward interval `a<=b`, the difference `u=b-a` satisfies `u<N`, and `Add(a,u,b)` is defined. Equal forward gaps share exactly this witness. No sum beyond the carrier is needed.

**PASS.**

### 15.6 Does `not o(N)` really imply `Omega(N)`?

The proof argues by the stronger negation of `Omega(N)`: if no eventual linear lower bound existed, one could choose an increasing subsequence with `S(N_k)/N_k -> 0`, contradicting the clean-gap argument. Hence the conclusion is genuinely `Omega(N)`.

**PASS.**

### 15.7 Does the internal digit upper bound fit the theorem's class?

Yes. It uses the same explicit target carrier, one fixed finite relational signature, no disjoint growing auxiliary sort, and charges both coordinate graphs and the digit table. Its total support is linear, exactly at the lower-bound scale.

**PASS.**

### 15.8 Does this contradict SOL-INFINITY's dimension-one barrier?

No. SOL-INFINITY concerns infinite global-order recovery from fixed-dimensional pure-order provenance. The present theorem concerns finite exact addition over an already ordered explicit carrier with arbitrary varied added relations. Different target, provenance and family semantics.

**PASS.**

No fatal defect was found.

---

## 16. Strategic consequence

The previous frontier question

\[
\text{“can exact AL1 be compressed below linear support?”}
\]

is now closed negatively in the broad explicit-base finite-signature FO model.

Together with the internal digit construction:

\[
\boxed{
\Theta(N)
\text{ is the exact added-memory scale for AL1 on an explicit ordered base carrier.}
}
\]

The next unresolved frontier is therefore no longer scalar support minimization inside this class.

The natural next questions are:

1. **Auxiliary-carrier tradeoff:** can total charged cost remain linear or become sublinear when target points are represented through a growing auxiliary carrier and every incidence is honestly charged?
2. **Provenance minimization at the linear floor:** among `Theta(N)` exact-AL1 mechanisms, what is the weakest generator class that attains the floor without a final-size numerical scaffold such as `ceil(sqrt N)`?
3. **Semantic phase at fixed linear cost:** what structural resource separates exact AL1 from AL2 when both admit `Theta(N)` representations?
4. **Representation invariants:** which parts of coordinate factorization survive bounded-fiber definitional/FO recodings?

The first scalar base-sort cost question is closed.

---

## 17. Status

\[
\boxed{\mathbf F:\ \text{Base-Sort Linear Support Barrier.}}
\]

\[
\boxed{\mathbf F:\ C_{AL1}^{\mathrm{base}}(N)=\Theta(N)\text{ in the declared model.}}
\]

\[
\boxed{\mathbf F:\ \text{one-cell/global size oracles cannot replace distributed AL1 memory.}}
\]

\[
\boxed{\mathbf O:\ \text{weakest provenance-safe mechanism attaining the linear floor.}}
\]

\[
\boxed{\mathbf O:\ \text{intrinsic AL1/AL2 separator at equal linear asymptotic cost.}}
\]

No new numbered G5 family is opened by this theorem.