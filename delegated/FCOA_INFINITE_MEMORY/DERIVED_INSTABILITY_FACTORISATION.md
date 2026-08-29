# Derived Instability Factorisation — FO Order from Primitive Half-Graph-Free Incidence

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint + semantic-carrier caveat  
**Scope:** infinite fixed-carrier branch; primitive-vs-derived instability

## 1. Question

Can full FO order memory arise even when no primitive binary relation itself contains arbitrarily deep half-graphs?

The answer is **yes**.

In fact one primitive directed incidence relation can have no half-graph of length 2 while a fixed existential composition of two incidence steps defines an infinite linear order.

Thus primitive instability is not necessary for derived FO instability.

The price is different: the canonical construction reifies ordered pairs as witness roles, moving the quadratic order cost from primitive relation incidences into carrier-role multiplicity.

---

## 2. Directed subdivision construction

Let

\[
S=\{s_0,s_1,s_2,\ldots\}
\]

be source vertices.

For every pair

\[
i<j
\]

introduce one witness vertex

\[
w_{ij}.
\]

Let

\[
W=\{w_{ij}:i<j\},
\qquad
U=S\sqcup W.
\]

Use a single primitive binary relation \(E\), with exactly the edges

\[
\boxed{
E(s_i,w_{ij})
\quad\text{and}\quad
E(w_{ij},s_j)
\qquad(i<j).
}
\]

No other \(E\)-edges exist.

This is the directed one-subdivision of the strict order relation on the source spine.

---

## 3. Primitive relation has bounded ladder depth

### Theorem DI-1 — atomic half-graph exclusion

The primitive relation \(E(x,y)\) does not contain a half-graph of length 2.

### Proof

Suppose distinct

\[
a_0,a_1,b_0,b_1
\]

satisfied the length-2 half-graph pattern

\[
E(a_0,b_0),
\qquad
E(a_0,b_1),
\qquad
E(a_1,b_1),
\qquad
\neg E(a_1,b_0).
\]

Since \(a_0\) has two distinct outgoing neighbors, \(a_0\) must be a source vertex \(s_i\), because every witness has exactly one outgoing edge.

Therefore \(b_0,b_1\) are witness vertices. But every witness has exactly one incoming source. The two edges

\[
E(a_0,b_1)
\quad\text{and}\quad
E(a_1,b_1)
\]

then force

\[
a_1=a_0,
\]

contradicting distinctness. \(\square\)

Hence the atomic relation has uniformly trivial ladder complexity.

Yet the full structure will be unstable.

---

## 4. Source and witness roles are FO-definable

A witness is exactly an element with one incoming and one outgoing \(E\)-neighbor:

\[
\operatorname{Wit}(x):=
\exists p\exists q\Bigl(
E(p,x)\wedge E(x,q)
\wedge
\forall p'(E(p',x)\to p'=p)
\wedge
\forall q'(E(x,q')\to q'=q)
\Bigr).
\]

Every \(w_{ij}\) satisfies this.

Every source \(s_i\) has infinitely many outgoing edges, so no source satisfies it.

Thus

\[
\operatorname{Src}(x):=\neg\operatorname{Wit}(x)
\]

defines the source spine.

---

## 5. Derived order on the source spine

Define

\[
\boxed{
\operatorname{Less}_S(x,y):=
\operatorname{Src}(x)\wedge\operatorname{Src}(y)
\wedge
\exists w\bigl(
\operatorname{Wit}(w)
\wedge E(x,w)\wedge E(w,y)
\bigr).
}
\]

Then

\[
\operatorname{Less}_S(s_i,s_j)
\iff
i<j.
\]

Therefore a length-2 existential composition of an atomic half-graph-free relation already defines an infinite strict order.

### Corollary DI-1A — derived instability exists

The complete structure \((U,E)\) is unstable although the primitive atomic formula \(E(x,y)\) has bounded ladder depth.

The order property first appears in the derived formula

\[
\exists w\,(E(x,w)\wedge E(w,y)).
\]

This is the exact phenomenon sought under the name **derived instability**.

---

## 6. FO recovery of a full order on the entire universe

The source order alone is not yet an order of all vertices. We now define an order of type \(\omega\) on the whole universe using finite blocks.

For each \(j\), let

\[
B_j=
\{s_j,w_{0j},w_{1j},\ldots,w_{j-1,j}\}.
\]

Order the blocks by \(j\), and inside each block put

\[
s_j
\prec
w_{0j}
\prec
w_{1j}
\prec\cdots\prec
w_{j-1,j}.
\]

The resulting order has type \(\omega\).

### Definable block key

For a vertex \(v\), its block key is the source \(s_j\) defined by

\[
\operatorname{Key}(v,k):=
\operatorname{Src}(k)\wedge
\Bigl(v=k\vee(\operatorname{Wit}(v)\wedge E(v,k))\Bigr).
\]

For a witness \(w_{ij}\), its left/source coordinate is definable by

\[
\operatorname{Left}(w,p):=
\operatorname{Wit}(w)\wedge\operatorname{Src}(p)\wedge E(p,w).
\]

### Same-block order

If \(u,v\) have the same block key \(k\), define \(u\prec v\) when either:

1. \(u=k\) and \(v\) is a witness; or
2. both are witnesses and their left coordinates are ordered by \(\operatorname{Less}_S\).

Combining this with comparison of distinct block keys by \(\operatorname{Less}_S\) gives an FO formula

\[
\operatorname{Less}_U(u,v)
\]

defining the displayed order of type \(\omega\) on all of \(U\).

Hence, after identifying \((U,\prec)\) with the standard carrier

\[
Q_0<Q_1<Q_2<\cdots,
\]

the single primitive incidence relation \(E\) FO-recovers the full external carrier order.

---

## 7. Primitive incidence density is linear in the reified carrier

Enumerate \(U\) in the block order above.

Every witness contributes exactly two primitive \(E\)-edges, and when the witness appears both of its source endpoints already lie in the same or earlier block.

Let \(S(N)\) be the number of source vertices among the first \(N+1\) elements. Since the number of elements through block \(J\) is

\[
1+2+\cdots+(J+1)
=\frac{(J+1)(J+2)}2,
\]

we have

\[
S(N)=\Theta(\sqrt N).
\]

Therefore the number of witnesses is

\[
N+1-S(N)=N-O(\sqrt N),
\]

and the primitive edge count satisfies

\[
\boxed{
C_E(N)=2N+O(\sqrt N)=\Theta(N).
}
\]

Thus derived instability can coexist with **linear primitive incidence density** and an atomic relation of bounded ladder depth.

---

## 8. Where the quadratic cost went

For the first \(r\) source points

\[
s_0,\ldots,s_{r-1},
\]

the construction contains one distinct witness

\[
w_{ij}
\]

for every ordered pair \(i<j<r\).

Hence the carrier contains

\[
\binom r2
\]

pair-witness roles before those \(r\) source points are fully represented.

So the cost is not eliminated:

\[
\boxed{
\text{primitive edge cost relative to total carrier size: linear},
}
\]

but

\[
\boxed{
\text{carrier-role cost relative to source-order depth }r:
\Theta(r^2).
}
\]

This is the exact dual of the sparse-marker phenomenon:

- sparse markers kept the carrier roles but paid in witness escape;
- subdivision factorisation keeps witnesses local but pays in carrier reification.

---

## 9. Pure-order interpretation and source safety

The two-role structure has a clean finite-dimensional interpretation in the pure order \((\mathbb N,<)\):

- source \(s_j\) is represented by the one-coordinate code \(j\);
- witness \(w_{ij}\) is represented by the two-coordinate code \((i,j)\) with \(i<j\);
- the two atomic edge clauses are just coordinate equalities.

Thus the entire incidence structure is obtained from pure order by finite-dimensional reification of ordered pairs. No external-index addition, multiplication, divisibility, BIT, prime predicate, or numerical growth function is used.

This gives a strong source-safety benchmark:

\[
\boxed{
\text{the construction imports only order and tuple reification, not arithmetic}.}
\]

It lies outside the earlier Order-Only Quadratic Barrier because that theorem allowed only binary relations directly on the original one-dimensional carrier; it did not allow dimension-lifting pair witnesses and then collapsing the countable interpreted universe back to one carrier.

---

## 10. Addition does not become FO-definable

The finite-dimensional interpretation in pure discrete order also gives a clean arithmetic-leakage test.

The source point \(s_j\) is the first element of block \(B_j\). Its rank in the full order \(\prec\) is

\[
\operatorname{rk}(s_j)
=
1+2+\cdots+j
=
\frac{j(j+1)}2
\]

with rank \(0\) for \(s_0\).

Suppose ordinary addition with respect to the recovered full order were FO-definable in \((U,E)\).

Then the unary predicate

\[
\operatorname{Even}_U(x)
\iff
\exists y\,\operatorname{Add}(y,y,x)
\]

would be FO-definable.

Restrict it to source vertices. Under the pure-order interpretation this yields a unary definable subset of the source index order \((\mathbb N,<)\):

\[
X=\left\{j:rac{j(j+1)}2\text{ is even}\right\}.
\]

But

\[
X=\{j:j\equiv0\text{ or }3\pmod4\},
\]

which is infinite and co-infinite.

Quantifier elimination for the discrete natural order \((\mathbb N,0,S,<)\) implies every parameter-free unary definable subset is finite or cofinite. Therefore \(X\) is not definable.

Contradiction.

### Theorem DI-2

\[
\boxed{
\operatorname{Add}_{\prec}
\text{ is not FO-definable in }(U,E).
}
\]

Literature anchor for the quantifier-elimination fact: Enderton, *A Mathematical Introduction to Logic*, 2nd ed., Theorem 32A; see also Marker, *Model Theory: An Introduction*, Exercise 3.4.4.

---

## 11. Multiplication does not become FO-definable

The recovered discrete order \(\prec\) defines its successor relation.

Julia Robinson proved that addition on the positive integers is first-order definable from multiplication together with successor.

Therefore, if ordinary multiplication relative to \(\prec\) were FO-definable in \((U,E)\), ordinary addition would also be FO-definable, contradicting DI-2.

### Theorem DI-3

\[
\boxed{
\operatorname{Mult}_{\prec}
\text{ is not FO-definable in }(U,E).
}
\]

Reference: Julia Robinson, “Definability and decision problems in arithmetic”, *J. Symbolic Logic* 14 (1949), 98–114, DOI `10.2307/2266510`.

---

## 12. Exact result

The construction simultaneously satisfies:

\[
\boxed{
\begin{array}{l}
\text{one primitive binary relation};\\
\text{primitive half-graph depth }<2;\\
\text{FO full order on an }\omega\text{-carrier};\\
\Theta(N)\text{ primitive incidences in the intrinsic carrier window};\\
\text{no FO ordinary addition};\\
\text{no FO ordinary multiplication}.
\end{array}}
\]

Hence:

### Theorem DI-4 — Derived Instability Theorem

Primitive half-graph depth does **not** lower-bound the depth of FO-definable order after quantification/composition.

A uniformly half-graph-free atomic relation can generate an infinite order property after a fixed existential composition.

---

## 13. Semantic-carrier caveat

This result must not be confused with a payload-preserving enrichment of the original generic ray.

Although the total universe remains countably infinite and can be identified with the same abstract carrier \(Q_0,Q_1,\ldots\), most points acquire **pair-witness roles** rather than source-spine roles. Among the first \(N\) points only \(\Theta(\sqrt N)\) are source anchors.

Therefore there are two notions of “same carrier”:

1. **cardinal same-carrier:** no new cardinality/sort is added; the interpreted universe is collapsed back to \(\omega\);
2. **payload-preserving same-carrier:** every original generic point remains a peer payload point rather than being consumed as a memory witness.

DI-4 is a theorem for the first notion.

Its status for the stronger payload-preserving requirement remains open.

This distinction is mandatory for upstream use.

---

## 14. New memory-cost coordinates

The previous Ladder–Escape invariant was complete for primitive nested-row/Ferrers codes. DI-4 shows it is not universal once reification is allowed.

The correct cost vector must now include at least three coordinates:

\[
\boxed{
\text{primitive incidence cost},
\quad
\text{witness escape},
\quad
\text{carrier reification / role inflation}.
}
\]

The two compression mechanisms occupy complementary corners:

### Sparse markers

- carrier-role inflation: low;
- primitive incidence count in a fixed window: tiny;
- witness escape: huge;
- primitive relation already contains a ladder.

### Directed subdivision factorisation

- witness escape: local;
- primitive incidence density: linear;
- primitive ladder depth: bounded;
- carrier-role inflation relative to source depth: quadratic;
- instability appears only after FO composition.

Thus there is again no free compression; the cost moves between coordinates.

---

## 15. Literature positioning

No novelty claim is made for the classical facts that:

- half-graphs witness the model-theoretic order property;
- subdivisions/incidence structures can encode a relation through bounded-length paths;
- biclique/rectangle factorisations are standard combinatorial representations of binary relations.

The FCOA-specific point is the exact placement of this mechanism in the infinite-memory cost diagram:

\[
\boxed{
\text{primitive instability can be traded for quadratic witness-role reification while preserving FO order and avoiding FO arithmetic}.}
\]

---

## 16. Next frontier

The genuinely hard remaining form of the question is now:

> Can a payload-preserving finite-signature enrichment of the same generic carrier recover full order by derived instability while every primitive relation has uniformly bounded ladder depth, **without** quadratic witness-role inflation and without FO arithmetic leakage?

Equivalently: can the order-property half-graph be factorized compositionally at subquadratic total semantic cost when the carrier points are not allowed to be consumed as pair witnesses?

This is the correct next boundary.