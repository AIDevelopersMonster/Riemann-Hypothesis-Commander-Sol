# Order-Only Quadratic Barrier

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Status:** theorem checkpoint  
**Scope:** binary finite-output infinite FCOA enrichments whose active domain/value geometry is compiled from the pure external discrete order, with only finitely many boundary parameters

## 1. Purpose

The Sparse Memory Threshold proved that FO recovery of the full order requires an infinite active nonlocal core. That still left open whether an admissible order-only FCOA layer could realize such a core with subquadratic cell density.

This note closes that question for a natural formalization of the branch prohibition against importing ordinary arithmetic on external indices.

The result is:

\[
\boxed{
\text{order-only binary finite-output compilation}
+\text{ FO recovery of full order}
\Longrightarrow
\Theta(N^2)\text{ active cells}.}
\]

Thus the complete comparison/domain constructions are asymptotically optimal inside the order-only binary class.

---

## 2. Admissible order-only compilation class

Let

\[
G_\omega=\{P_2,P_3,\ldots\}
\]

carry the external discrete order

\[
P_2<P_3<P_4<\cdots.
\]

An **order-only binary compilation** consists of finitely many binary relations

\[
R_1,\ldots,R_m\subseteq G_\omega^2
\]

such that every \(R_i(x,y)\) is first-order definable in the pure discrete order

\[
(G_\omega,<)
\]

with at most finitely many fixed boundary parameters.

For a partial-operation presentation with a finite terminal output alphabet, name the finitely many outputs temporarily and take as the \(R_i\)'s the domain/value-fiber traces

\[
R_j(x,y)\iff x\star y=\Omega_j.
\]

Naming outputs can only increase definability power, so any lower bound proved in this named expansion also applies to the anonymous-output presentation.

This class includes:

- successor/predecessor cells;
- every fixed finite-distance jump relation;
- finite boundary anchors;
- full orientation \(x<y\);
- finite value colorings whose fibers are defined using only order/equality and finitely many boundary points.

It excludes external use of addition, multiplication, squares, divisibility, BIT, prime predicates, or any other non-order geometry on the indices.

---

## 3. Tail Normal Form for binary order formulas

### Lemma Q-1 — bounded-distance/tail dichotomy

For every FO formula

\[
\varphi(x,y)
\]

in the language of the discrete order \((\mathbb N,<)\), with finitely many parameters allowed, there exist integers

\[
B,K<\infty
\]

and two truth values

\[
\epsilon_+,\epsilon_-\in\{0,1\}
\]

such that whenever

\[
x,y>B,
\qquad |x-y|>K,
\]

we have

\[
\varphi(x,y)=\epsilon_+
\quad\text{if }x<y,
\]

and

\[
\varphi(x,y)=\epsilon_-
\quad\text{if }y<x.
\]

### Proof

Expand the language by the least element and successor. The complete theory of the natural discrete order admits quantifier elimination in this standard expansion. Every fixed parameter is itself a finite successor iterate of the least element.

Hence \(\varphi\) is equivalent to a Boolean combination of finitely many atomic comparisons involving terms

\[
S^a(x),\quad S^b(y),\quad S^c(0).
\]

Let \(K\) exceed every successor-offset difference occurring in the quantifier-free formula, and let \(B\) exceed all named/term constants.

For \(x,y>B\) with \(|x-y|>K\):

- all equalities between a bounded successor iterate of \(x\) and one of \(y\) are false;
- every comparison of a bounded iterate of \(x\) with one of \(y\) is determined solely by whether \(x<y\) or \(y<x\);
- all comparisons with fixed initial constants have stabilized.

Therefore the Boolean combination has a fixed truth value on each of the two remote orientations. \(\square\)

### Literature boundary

Quantifier elimination for \((\mathbb N,<,S,0)\) is classical; e.g. Enderton, *A Mathematical Introduction to Logic*, Theorem 32A, and Marker, *Model Theory: An Introduction*, Exercise 3.4.4.

---

## 4. Density dichotomy for an order-definable binary relation

For

\[
[N]=\{0,1,\ldots,N\},
\]

write

\[
E_R(N)=|R\cap[N]^2|.
\]

### Theorem Q-2 — linear-or-quadratic tail dichotomy

Let \(R(x,y)\) be FO-definable in \((\mathbb N,<)\) with finitely many parameters. Then exactly one of the following asymptotic regimes occurs:

1. **local/finite-apex regime:**
   \[
   E_R(N)=O(N);
   \]
   after deleting a finite initial apex set, every \(R\)-edge has bounded order distance;

2. **global-tail regime:**
   \[
   E_R(N)=\Theta(N^2).
   \]

In particular, no such binary relation has genuinely intermediate density such as

\[
N^{3/2},\qquad N\log N,
\qquad\text{or more generally }\omega(N)\cap o(N^2).
\]

### Proof

Apply Lemma Q-1.

If

\[
\epsilon_+=\epsilon_-=0,
\]

then outside the finite boundary all relation pairs satisfy

\[
|x-y|\le K.
\]

There are only \(O(N)\) such pairs, plus \(O(N)\) pairs incident with the finite boundary.

If at least one of \(\epsilon_+,\epsilon_-\) is 1, then one whole orientation of all sufficiently remote pairs belongs to \(R\). That contributes a positive asymptotic fraction of all \(N^2\) ordered pairs. Hence

\[
E_R(N)=\Theta(N^2).
\]

\(\square\)

---

## 5. Quadratic Barrier for a finite binary order-only signature

### Theorem Q-3 — order-only quadratic barrier

Let

\[
\mathcal R=(G_\omega;R_1,\ldots,R_m)
\]

be a finite order-only binary compilation. If the full strict order \(<\) is FO-definable in \(\mathcal R\), then at least one basic relation \(R_i\) satisfies

\[
\boxed{E_{R_i}(N)=\Theta(N^2).}
\]

Consequently the union of basic interaction cells also has quadratic initial-segment density.

### Proof

Assume every \(R_i\) is subquadratic. By Theorem Q-2 every \(R_i\) is then in its local/finite-apex regime.

Because there are only finitely many relations, take a common finite boundary set and a common finite width \(K\). Outside that boundary, the Gaifman graph of the entire expansion has uniformly bounded degree.

Therefore the finite-apex trace is locally finite. By the Sparse Memory Threshold / Finite-Apex Locality Barrier, no FO formula in the expansion can define a strict linear order on the infinite carrier.

Contradiction. \(\square\)

---

## 6. Partial-operation corollary

### Corollary Q-3A — finite-output FCOA cell lower bound

Consider finitely many partial binary operation layers on \(G_\omega\), each with a finite terminal output alphabet. Suppose every domain/value-fiber rule is order-only in the sense of Section 2.

If the reduct of those operations FO-recovers the full strict carrier order, then the number of defined generic-generic operation cells in the first \(N\) carrier points is

\[
\boxed{\Theta(N^2).}
\]

### Proof

Name the finitely many output values. Every output fiber becomes one of finitely many binary order-definable relations. If the total number of defined cells were \(o(N^2)\), every fiber would be \(o(N^2)\). Theorem Q-3 would then forbid FO recovery of order. \(\square\)

This remains true whether the information is stored in definedness, in value fibers, or split among finitely many operation layers.

---

## 7. Existing constructions meet the lower bound

### G2∞

Successor memory has

\[
E(N)=\Theta(N).
\]

It lies in the local regime and cannot FO-recover transitive order.

### Complete order in the domain

\[
x\diamond y=\Omega\iff x<y
\]

has

\[
E(N)=\frac{N(N+1)}2+O(N)=\Theta(N^2).
\]

It meets the lower bound and recovers order immediately from definedness.

### Infinite complete two-value comparison

Every distinct pair is defined, so

\[
E(N)=N(N+1)+O(N)=\Theta(N^2).
\]

It also meets the lower bound.

Thus the known order-recovering mechanisms are not merely convenient dense examples: within order-only binary finite-output FCOA, their quadratic scale is asymptotically unavoidable.

---

## 8. Exact meaning of the hard prohibition

The theorem gives a mathematically testable interpretation of

> do not import \(+\) or \(\times\) on external indices.

A conservative admissibility class is:

\[
\boxed{
\text{new carrier interaction geometry must be FO-generated from the external discrete order alone, plus finitely many boundary parameters}.}
\]

Within this class, subquadratic FO global-order memory is impossible.

Therefore any proposed \(o(N^2)\) construction must necessarily introduce a primitive global geometry that is **not** definable from pure order. Such a geometry may or may not be arithmetic, but it requires a separate source/admissibility and Arithmetic Leakage audit.

---

## 9. Why this sharpens the Sparse Memory Threshold

The previous theorem said:

\[
\text{FO order}\Rightarrow\text{infinite nonlocal core}.
\]

The new theorem says more in the order-only class:

\[
\boxed{
\text{FO order}
\Rightarrow
\text{a quadratic long-range tail}.}
\]

So there are two distinct thresholds:

1. **general finite-signature binary threshold:** an infinite nonlocal core is necessary;
2. **order-only binary FCOA threshold:** quadratic pair density is necessary.

This identifies exactly where a genuinely sparse candidate would have to obtain its extra power: not from more clever local order compilation, but from a new non-order global skeleton.

---

## 10. Research consequence

The sparse-memory search is now split into two branches:

### Admissible order-only branch

Closed asymptotically:

\[
\boxed{\Theta(N^2)\text{ is optimal}.}
\]

### Primitive-global-skeleton branch

Still open:

> Is there a natural, non-arithmetic primitive global skeleton on the same carrier whose binary incidence is \(o(N^2)\), from which FO recovers the carrier order, while ordinary external-index addition and multiplication remain FO-undefinable?

Any candidate in this second branch must be audited both for **source safety** (it was not constructed by smuggling arithmetic into the external indices) and **leakage safety** (arithmetic is not internally recoverable afterwards).
