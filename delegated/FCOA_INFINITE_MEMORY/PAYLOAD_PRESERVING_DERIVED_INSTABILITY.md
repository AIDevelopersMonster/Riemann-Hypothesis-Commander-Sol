# Payload-Preserving Derived Instability — Linear Primitive Cost from Stable Self-Coordinates

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint; publication hardening still required  
**Scope:** infinite fixed-carrier branch; no finite-G4 status change

## 1. Target

The previous directed-subdivision benchmark proved that derived instability exists, but it consumed a quadratic number of witness-only roles relative to the ordered source spine.

The stricter target is:

> keep every carrier element as a full generic payload point; introduce no witness-only sort or dedicated pair-witness population; require every primitive relation to have bounded atomic ladder depth; nevertheless FO-recover a full order of type \(\omega\), with no FO recovery of ordinary addition or multiplication.

This note gives a positive construction with **linear primitive incidence cost**.

---

## 2. The self-coordinate carrier

Start with the pure discrete order

\[
I=(\mathbb N,<).
\]

Consider the two-dimensional payload universe

\[
U=\mathbb N^2.
\]

No element of \(U\) is assigned a witness-only role. Every pair

\[
u=(i,j)
\]

is itself a generic payload point.

We use three primitive binary relations on \(U\).

### First-coordinate projection

\[
\boxed{
P_1((i,j),(k,\ell))
\iff
k=\ell=i.
}
\]

Thus every point has exactly one \(P_1\)-target, namely its diagonal first-coordinate representative

\[
d_i=(i,i).
\]

### Second-coordinate projection

\[
\boxed{
P_2((i,j),(k,\ell))
\iff
k=\ell=j.
}
\]

Thus every point has exactly one \(P_2\)-target

\[
d_j=(j,j).
\]

### Upper-triangle marker

To keep the primitive signature binary, use only diagonal loops:

\[
\boxed{
M((i,j),(k,\ell))
\iff
(i,j)=(k,\ell)
\text{ and } i<j.
}
\]

So \(M(x,x)\) is precisely the unary condition “first coordinate < second coordinate”.

All three relations are defined from equality and the pure external order on the two coordinates. No addition, multiplication, divisibility, BIT, pairing arithmetic, square root, prime predicate, or other numerical operation is used in the source description.

---

## 3. Primitive atomic relations are half-graph-free

### Theorem PP-1

Each primitive binary relation

\[
P_1,\quad P_2,\quad M
\]

has atomic half-graph depth strictly below 2.

### Proof

For \(P_1\) and \(P_2\), every left argument has exactly one outgoing target. A length-2 half-graph would require one left point to hit two distinct right points. Impossible.

For \(M\), every edge is a loop. A length-2 half-graph requires off-diagonal incidence among four distinct row/column roles, which cannot occur.

Thus no primitive relation itself carries the order property. \(\square\)

This is stronger than merely bounded degree: the projections have large inverse fibres, yet remain atomically stable.

---

## 4. The diagonal is internally definable

A point is diagonal exactly when its first-coordinate projection is itself:

\[
\boxed{
D(x):=P_1(x,x).
}
\]

Equivalently one may use \(P_2(x,x)\).

Thus

\[
D(U)=\{d_0,d_1,d_2,\ldots\}.
\]

---

## 5. Derived order on the diagonal

Define

\[
\boxed{
\operatorname{DLess}(a,b):=
D(a)\wedge D(b)\wedge
\exists w\bigl(
M(w,w)\wedge P_1(w,a)\wedge P_2(w,b)
\bigr).
}
\]

If

\[
a=d_i,
\qquad b=d_j,
\]

then the unique point having those two projections is

\[
w=(i,j).
\]

Hence

\[
M(w,w)
\iff
i<j.
\]

Therefore:

### Theorem PP-2 — diagonal derived order

\[
\boxed{
\operatorname{DLess}(d_i,d_j)
\iff
i<j.
}
\]

Thus the order property appears only after an existential composition of three atomic-stable primitive relations.

This is genuine **derived instability**.

---

## 6. Coordinate representatives of every payload point

For every \(x\in U\), there are unique diagonal points \(r(x),c(x)\) such that

\[
P_1(x,r(x)),
\qquad
P_2(x,c(x)).
\]

These are FO-recoverable by the primitive projection relations.

Using \(\operatorname{DLess}\), define the diagonal non-strict order

\[
a\le_D b
\iff
a=b\vee\operatorname{DLess}(a,b).
\]

---

## 7. A definable order of type omega on the whole carrier

For \(x=(i,j)\), define its diagonal max-key

\[
\mu(x)=d_{\max(i,j)}.
\]

The graph of \(\mu\) is FO-definable: \(\mu(x)=k\) iff \(k\) is one of the two coordinate representatives and the other is \(\le_D k\).

Now order all payload points by:

1. increasing max-key;
2. inside one max-shell, increasing first coordinate;
3. if first coordinates agree, increasing second coordinate.

Formally, \(x\prec y\) iff either

\[
\mu(x)<_D\mu(y),
\]

or the max-keys agree and

\[
r(x)<_D r(y),
\]

or both max-key and first coordinate agree and

\[
c(x)<_D c(y).
\]

Every clause is first-order definable from \(P_1,P_2,M\).

### Theorem PP-3 — full payload order

The relation \(\prec\) is a strict linear order of type \(\omega\) on **all** of \(U\).

### Proof

For each \(m\), the shell

\[
S_m=\{(i,j):\max(i,j)=m\}
\]

has exactly

\[
2m+1
\]

elements. The order first lists the finite shell \(S_0\), then \(S_1\), and so on. Therefore every initial segment is finite and the whole order has type \(\omega\). \(\square\)

Consequently, after transporting the structure along the unique order isomorphism

\[
(U,\prec)\cong(\mathbb N,<),
\]

we obtain a structure on the original countable generic carrier

\[
G_\omega=\{Q_0,Q_1,Q_2,\ldots\}
\]

in which every point remains a peer payload point.

No witness-only sort exists.

---

## 8. Payload preservation is exact

The previous subdivision architecture distinguished:

- source payload points;
- separate pair-witness points.

Here there is only one carrier role:

\[
\boxed{\text{every }(i,j)\in U\text{ is a generic payload point}.}
\]

Some points with \(i<j\) participate as witnesses in the formula defining diagonal comparison, but this is not an exclusive role. The same point is simultaneously:

- a member of the full recovered order;
- an ordinary argument of \(P_1,P_2,M\);
- a payload peer with its own coordinate projections;
- potentially a comparison witness.

Thus the construction satisfies the strong **no dedicated witness-only population** condition.

---

## 9. Linear primitive incidence cost

Let

\[
W_m=\{(i,j):0\le i,j\le m\}.
\]

This is exactly the union of shells through \(m\), so

\[
|W_m|=(m+1)^2.
\]

Inside \(W_m\):

- \(P_1\) contributes exactly one edge per point;
- \(P_2\) contributes exactly one edge per point;
- \(M\) contributes one loop for every \(i<j\), namely
  \[
  \frac{m(m+1)}2
  \]
  loops.

Therefore the total primitive tuple count on complete shell windows is

\[
2(m+1)^2+\frac{m(m+1)}2.
\]

Hence:

### Theorem PP-4 — linear primitive cost

For the intrinsic first \(N\) payload points of the recovered order,

\[
\boxed{
C_{\rm prim}(N)=\Theta(N).
}
\]

Thus payload-preserving derived instability can recover full FO order with the information-theoretically minimal scale of primitive tuple growth up to constant factors.

The previous quadratic resolved-prefix law was specific to primitive half-graph/Ferrers encodings and does not extend to derived instability.

---

## 10. Why this does not contradict the local-finiteness barrier

Although each point has only one outgoing \(P_1\)-edge and one outgoing \(P_2\)-edge, the diagonal points have infinite inverse fibres.

For example,

\[
P_1^{-1}(d_i)=\{(i,j):j\in\mathbb N\}.
\]

Thus the Gaifman graph is not locally finite. In fact there are infinitely many infinite-degree active points.

Therefore the Infinite Nonlocal Core theorem is fully respected.

The construction crosses the locality barrier through **stable infinite fibres**, not through primitive half-graphs.

This is a new mechanism in the branch.

---

## 11. Source safety: pure-order dimension-2 interpretation

The entire primitive structure is first-order interpretable in the pure discrete order

\[
(\mathbb N,<)
\]

using dimension 2:

- domain: all pairs \((i,j)\);
- \(P_1\) and \(P_2\): coordinate equalities with diagonal representatives;
- \(M\): equality of the two payload arguments plus the coordinate comparison \(i<j\).

Therefore the source uses only:

\[
\boxed{
\text{pure order + finite-dimensional self-coordination}.}
\]

No arithmetic is imported.

This explains how the earlier one-dimensional Order-Only Quadratic Barrier is evaded: that theorem forbids subquadratic order recovery by binary relations **directly on a one-dimensional order-only carrier**. Here the source geometry has interpretation dimension 2, while still collapsing canonically to one countable payload carrier.

---

## 12. Ordinary addition does not leak

The source interpretation in pure order gives a direct non-leakage proof.

Assume ordinary addition with respect to the recovered full order \(\prec\) were FO-definable in

\[
(U;P_1,P_2,M).
\]

Then the parity predicate of the recovered rank would be FO-definable:

\[
\operatorname{Even}_\prec(x)
\iff
\exists y\,\operatorname{Add}_\prec(y,y,x).
\]

Now consider the definable coordinate line

\[
L=\{(0,m):m\in\mathbb N\}.
\]

The point \((0,m)\) is the first point of max-shell \(m\). The number of points in all earlier shells is

\[
1+3+5+\cdots+(2m-1)=m^2.
\]

Hence

\[
\operatorname{rk}_\prec(0,m)=m^2.
\]

Therefore

\[
\operatorname{Even}_\prec(0,m)
\iff
m\text{ is even}.
\]

But every unary set obtained by pulling an interpreted FO formula back to the coordinate parameter \(m\) is FO-definable in pure discrete order \((\mathbb N,<)\). By quantifier elimination for the discrete order, every such one-variable definable set is eventually constant (indeed finite or cofinite after parameters are fixed).

The even numbers are neither finite nor cofinite.

Contradiction.

### Theorem PP-5

\[
\boxed{
\operatorname{Add}_\prec
\text{ is not FO-definable from }P_1,P_2,M.
}
\]

---

## 13. Ordinary multiplication does not leak

The recovered order \(\prec\) defines its successor relation.

Julia Robinson proved that addition on the positive integers is first-order definable from multiplication together with successor.

Therefore FO-definability of ordinary multiplication relative to \(\prec\) would imply FO-definability of addition, contradicting PP-5.

### Theorem PP-6

\[
\boxed{
\operatorname{Mult}_\prec
\text{ is not FO-definable from }P_1,P_2,M.
}
\]

Reference: Julia Robinson, “Definability and decision problems in arithmetic”, *Journal of Symbolic Logic* 14 (1949), 98–114, DOI `10.2307/2266510`.

---

## 14. FCOA operation-layer realization

Each primitive binary relation can be compiled into one one-output partial operation layer.

For \(r\in\{1,2,M\}\), introduce a terminal output \(\Omega_r\) and define

\[
x\star_r y=\Omega_r
\iff
R_r(x,y).
\]

After tracing out the finite output set

\[
\{\Omega_1,\Omega_2,\Omega_M\},
\]

the active binary trace is exactly

\[
P_1,P_2,M.
\]

Thus the theorem can be realized inside a finite-output partial-operation presentation rather than only as an abstract relational benchmark.

No primitive operation layer contains an atomic half-graph of depth 2.

---

## 15. Main theorem

### Theorem PP-7 — Payload-Preserving Derived Instability

There exists a finite-signature, finite-output, same-countable-carrier FCOA-style structure such that:

\[
\boxed{
\begin{array}{l}
\text{every carrier point remains a generic payload peer};\\
\text{there is no witness-only population};\\
\text{every primitive binary trace has atomic half-graph depth }<2;\\
\text{the full carrier order of type }\omega\text{ is FO-definable};\\
C_{\rm prim}(N)=\Theta(N);\\
\text{ordinary }+\text{ is not FO-definable};\\
\text{ordinary }\times\text{ is not FO-definable}.
\end{array}
}
\]

Hence the quadratic semantic-cost barrier does **not** survive once derived instability and payload-preserving finite-dimensional self-coordination are allowed.

---

## 16. What cost remains

The construction destroys three previous candidate lower bounds simultaneously:

- primitive ladder depth need not grow;
- primitive incidence count need only be linear;
- no dedicated witness-role inflation is needed.

The remaining nontrivial resource is different:

\[
\boxed{
\text{self-coordination / interpretation dimension}.}
\]

The order is recovered because each payload point carries two coordinate projections and the upper-triangle marker compares those coordinates indirectly.

Thus the cost vector must now include at least

\[
\boxed{
(
\text{incidence},
\text{escape},
\text{role inflation},
\text{primitive ladder depth},
\text{interpretation dimension}
).
}
\]

For PP-7 the coordinates are approximately:

\[
\boxed{
(
\Theta(N),
\text{local},
0,
<2,
2
).
}
\]

---

## 17. Literature boundary

No novelty claim is made for:

- finite-dimensional interpretations;
- coordinate projections;
- coding an order relation through an upper-triangle subset of a Cartesian square;
- the classical nondefinability of parity in pure discrete order;
- Julia Robinson's multiplication-plus-successor definability of addition.

The FCOA-specific contribution is the placement of this elementary construction in the memory-boundary diagram and the exact conclusion:

\[
\boxed{
\text{payload preservation + stable primitive relations + linear primitive cost are compatible with derived FO global order without FO arithmetic}.}
\]

A relevant warning from pairing-function literature is that not every one-dimensional collapse is harmless: for the classical Cantor pairing function, adjoining natural order gives an undecidable theory. Therefore the pure-order interpretation/provenance proof above is essential; one must not replace it by an arbitrary arithmetic pairing map.

---

## 18. Next frontier

Payload-preserving derived instability is therefore **possible**.

The next genuine barrier is narrower:

> Can the interpretation dimension be reduced from 2 to 1 while retaining all of the following simultaneously: payload preservation, bounded primitive ladder depth, \(\Theta(N)\) primitive incidence, FO full order, and no FO ordinary arithmetic?

Equivalently:

> Is two-coordinate self-reification the minimal structural dimension required to manufacture global FO order from atomically stable finite-output memory?

This is now the natural next strike.