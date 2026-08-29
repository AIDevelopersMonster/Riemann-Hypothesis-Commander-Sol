# Sparse Marker Ladder — Polylogarithmic FO Order Memory without FO Arithmetic

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint; external unary-QE dependency explicitly isolated  
**Scope:** infinite fixed-carrier branch only

## 1. Why the previous N log N bound was not the final density frontier

The exponential nested-tail construction used

\[
R_{\rm tail}(Q_n,Q_m)\iff m\ge 2^n,
\]

so every active row stored an entire cofinal tail. This produced

\[
\Theta(N\log N)
\]

visible incidences on the initial window \([0,N]^2\).

That cost is optimal only inside the **D0L nested-tail** architecture.

The new observation is that FO order recovery by row inclusion does not require the rows to contain every point beyond a threshold. It only requires a strictly nested infinite family of row-neighborhoods. Sparse marker sets suffice.

This drops the visible incidence cost from almost linear-times-logarithmic to polylogarithmic.

---

## 2. Exponential marker ladder

Let

\[
G_\omega=\{Q_0,Q_1,Q_2,\ldots\}.
\]

Let the marker sequence be

\[
a_j=2^j.
\]

Define one binary relation

\[
\boxed{
R_1(Q_n,Q_m)
\iff
\exists j\ge n\;(m=a_j).
}
\]

Thus the row of \(Q_n\) is not the numerical tail after \(2^n\), but the sparse marker tail

\[
M_n=\{Q_{2^j}:j\ge n\}.
\]

Equivalently, with one terminal output \(\Omega\):

\[
Q_n\star Q_m=\Omega
\iff
R_1(Q_n,Q_m).
\]

Every row is infinite, but almost all of its targets lie far outside a fixed finite initial window.

---

## 3. FO recovery of the full carrier order

The marker rows satisfy

\[
M_0\supsetneq M_1\supsetneq M_2\supsetneq\cdots.
\]

Indeed,

\[
M_n\setminus M_{n+1}=\{Q_{2^n}\}.
\]

Therefore:

### Theorem ML-1 — marker-row inclusion theorem

The original carrier order is FO-definable from \(R_1\) alone by

\[
\boxed{
\operatorname{Less}(x,y):=
\forall z\,(R_1(y,z)\to R_1(x,z))
\wedge
\exists z\,(R_1(x,z)\wedge\neg R_1(y,z)).
}
\]

For all \(n,k\),

\[
\operatorname{Less}(Q_n,Q_k)
\iff
n<k.
\]

Thus one binary relation and one terminal output FO-recover the full strict order.

---

## 4. The marker map is internally recoverable

Once \(<\) is recovered, successor is FO-definable in the usual way.

The unique marker removed between two consecutive rows is also definable:

\[
\operatorname{Marker}(x,z):=
R_1(x,z)
\wedge
\exists y\bigl(
\operatorname{Succ}(x,y)
\wedge
\neg R_1(y,z)
\bigr).
\]

For \(x=Q_n\), the unique \(z\) satisfying this formula is

\[
z=Q_{2^n}.
\]

Hence the structure internally recovers the unary exponential marker map

\[
n\mapsto 2^n.
\]

This is expected and does not itself imply addition or multiplication.

---

## 5. Exact visible-incidence count

Let

\[
L=\lfloor\log_2N\rfloor.
\]

The marker columns visible in \([0,N]\) are precisely

\[
2^0,2^1,\ldots,2^L.
\]

The marker \(2^j\) belongs to exactly the rows

\[
0,1,\ldots,j.
\]

Therefore

\[
C_1(N)
=\sum_{j=0}^{L}(j+1)
=\frac{(L+1)(L+2)}2.
\]

Thus:

### Theorem ML-2 — polylogarithmic memory

\[
\boxed{
C_1(N)=\Theta((\log N)^2).
}
\]

In particular,

\[
C_1(N)=o(N^\varepsilon)
\]

for every fixed \(\varepsilon>0\).

This is vastly smaller than the \(\Theta(N\log N)\) dense-tail construction.

---

## 6. Why this does not contradict the Infinite Nonlocal Core theorem

The Sparse Memory Threshold concerned **global Gaifman nonlocality**, not the number of relation tuples visible inside the numerical window \([0,N]^2\).

For every source point \(Q_n\),

\[
\deg(Q_n)=\infty
\]

because it is related to every marker

\[
Q_{2^j},\qquad j\ge n.
\]

Hence

\[
H=G_\omega.
\]

The required infinite nonlocal core is fully present.

The low finite-window count occurs only because most edges from a small source point jump to very large marker targets.

Therefore:

\[
\boxed{
\text{global nonlocality}
\not\asymp
\text{initial-window incidence density}.
}
\]

This sharpens the earlier warning that raw tuple count is representation-dependent.

---

## 7. Source provenance

The marker sequence has the same certified one-letter D0L origin used in the previous audit:

\[
A\mapsto AA,
\qquad w=A.
\]

After \(j\) parallel iterations,

\[
|\sigma^j(A)|=2^j.
\]

At stage \(j\), place a marker at the carrier point whose rank equals this intrinsic word length, and connect that marker to the order-initial stage set

\[
Q_0,\ldots,Q_j.
\]

The generation rule uses:

- the index-blind D0L duplication morphism;
- stage order only;
- no external-index addition, multiplication, divisibility, BIT, parity, prime predicate, or binary arithmetic operation.

Thus the base marker ladder passes the previously declared D0L-source gate.

---

## 8. Definability inside the pure-order exponential structure

Let

\[
e(x)=2^x.
\]

The relation \(R_1\) is FO-definable in

\[
\mathcal E=(\mathbb N,<,e)
\]

by

\[
\boxed{
R_1(n,m)
\iff
\exists j\,(n\le j\wedge e(j)=m).
}
\]

Therefore

\[
(G_\omega,R_1)
\]

is an FO reduct of \(\mathcal E\).

Any arithmetic relation FO-definable from \(R_1\) would therefore also be FO-definable in \(\mathcal E\).

---

## 9. External unary-QE input for (N,<,2^x)

Semenov's 1984 theorem proves decidability for a broad class of monotone order expansions and explicitly includes \(x\mapsto 2^x\) as effectively compatible with order.

For the exact pure-order exponential structure, Emil Jeřábek gave an explicit quantifier-elimination analysis of

\[
\operatorname{Th}(\mathbb N,0,S,<,2^x)
\]

in the language expanded by the floor-logarithm

\[
\ell(x)=\lfloor\log_2x\rfloor.
\]

The one-variable consequence used here is:

> every unary formula is equivalent to a Boolean combination of finitely many point equations and predicates of the form
> \[
> P(\ell^r(x)+c),
> \]
> where \(P(t)\) means that \(t\) is a power of two.

This branch reproduces the only consequence needed for arithmetic non-leakage below.

Literature anchors:

- A. L. Semenov, “Logical theories of one-place functions on the set of natural numbers”, *Math. USSR-Izv.* 22 (1984), 587–618, DOI `10.1070/IM1984v022n03ABEH001456`;
- E. Jeřábek, explicit QE theorem/proof outline for `Th(N,0,S,<,2^x)`, MathOverflow answer to “Models of arithmetic in a signature with exponentiation but not addition and multiplication”, 2018.

The second item is an expert mathematical source rather than a journal publication and remains a publication-hardening obligation if this result is promoted to a paper.

---

## 10. Parity is not FO-definable in (N,<,2^x)

### Lemma ML-3

The set

\[
2\mathbb N
\]

is not FO-definable in \(\mathcal E=(\mathbb N,<,2^x)\).

### Proof from the unary normal form

Suppose \(\varphi(x)\) is unary. By the external QE description, it is a Boolean combination of finitely many formulas

\[
x=\bar c
\]

and

\[
P(\ell^r(x)+c).
\]

Let \(C\) exceed the absolute value of every finite shift \(c\) occurring in the formula and all named constants.

Choose \(M\) large. Consider the long interior interval

\[
I_M=
[2^M+C+2,\,2^{M+1}-C-2].
\]

For every \(x\in I_M\):

1. no point equation \(x=\bar c\) holds;
2. for every shift \(|c|\le C\), \(x+c\) is strictly between consecutive powers \(2^M\) and \(2^{M+1}\), so \(P(x+c)\) is false;
3. \(\ell(x)=M\) is constant throughout \(I_M\), hence every predicate with at least one application of \(\ell\) has a fixed truth value throughout the interval.

Therefore \(\varphi\) is constant on \(I_M\).

For sufficiently large \(M\), the interval contains consecutive integers of opposite parity. Hence \(\varphi\) cannot define the even numbers. \(\square\)

---

## 11. Addition and multiplication do not leak

### Theorem ML-4 — no addition

Ordinary external-index addition is not FO-definable in \((G_\omega,R_1)\).

If addition were definable, then parity would be definable by

\[
\operatorname{Even}(x)
\iff
\exists y\,\operatorname{Add}(y,y,x).
\]

Because \(R_1\) is definable in \(\mathcal E\), this would make parity definable in \(\mathcal E\), contradicting Lemma ML-3. \(\square\)

Thus

\[
\boxed{R_1\not\Rightarrow_{\rm FO}+.}
\]

### Theorem ML-5 — no multiplication

The relation \(R_1\) already FO-defines the discrete order and hence successor.

Julia Robinson proved that addition of positive integers is first-order definable from multiplication and successor.

Therefore, if ordinary multiplication were FO-definable from \(R_1\), addition would also be FO-definable, contradicting ML-4. \(\square\)

Hence

\[
\boxed{
R_1\Rightarrow_{\rm FO}<,
\qquad
R_1\not\Rightarrow_{\rm FO}+,
\qquad
R_1\not\Rightarrow_{\rm FO}\times.
}
\]

Primary reference for the implication `multiplication + successor => addition`:

Julia Robinson, “Definability and decision problems in arithmetic”, *J. Symbolic Logic* 14 (1949), 98–114, DOI `10.2307/2266510`.

---

## 12. Fixed-depth exponential marker cascades

The same logic yields a hierarchy far below \((\log N)^2\).

Let

\[
E_1(n)=2^n,
\qquad
E_{k+1}(n)=2^{E_k(n)}
\]

for a fixed integer \(k\ge1\).

Define

\[
\boxed{
R_k(Q_n,Q_m)
\iff
\exists j\ge n\;(m=E_k(j)).
}
\]

For every fixed \(k\), the marker map \(E_k\) is FO-definable in \((\mathbb N,<,2^x)\) by a finite chain of applications of the unary exponential function. Hence each \(R_k\) is an FO reduct of the same arithmetic-safe ambient structure \(\mathcal E\).

Therefore ML-4 and ML-5 transfer immediately:

\[
\boxed{
R_k\Rightarrow_{\rm FO}<,
\qquad
R_k\not\Rightarrow_{\rm FO}+,
\qquad
R_k\not\Rightarrow_{\rm FO}\times.
}
\]

---

## 13. Density of the fixed-depth cascade

Let

\[
J_k(N)=\max\{j:E_k(j)\le N\}.
\]

Then, up to additive constants,

\[
J_k(N)=\log_2^{(k)}N,
\]

where \(\log^{(k)}\) denotes \(k\)-fold iterated binary logarithm.

Each visible marker \(E_k(j)\) is incident with exactly \(j+1\) source rows. Hence

\[
C_k(N)
=\sum_{j=0}^{J_k(N)}(j+1)
=\frac{(J_k(N)+1)(J_k(N)+2)}2.
\]

Thus:

### Theorem ML-6 — iterated-log compression

For every fixed \(k\ge1\),

\[
\boxed{
C_k(N)
=\Theta\left((\log^{(k)}N)^2\right).
}
\]

Consequently, for every fixed \(k\), there is a finite-signature same-carrier skeleton with arithmetic-safe FO order recovery whose visible initial-window memory is only the square of a \(k\)-fold iterated logarithm.

This destroys every proposed universal lower bound of the forms

\[
N^\varepsilon,
\qquad
(\log N)^c,
\qquad
\log N,
\]

when the source class allows arbitrarily large but fixed cascade depth.

More precisely, no bound expressed by any **fixed finite level** of the iterated-log hierarchy can be universal across the whole finite-depth cascade family.

---

## 14. Provenance of the cascade family

For \(k=1\), source safety is the already audited D0L duplication source.

For fixed \(k>1\), use a **finite-depth D0L cascade**:

1. the first duplication layer runs for \(j\) stages and outputs a unary word of length \(2^j\);
2. its output word serves only as a unary clock for the next fixed duplication layer;
3. repeat for exactly \(k\) layers, where \(k\) is fixed in the finite construction and does not depend on \(j\).

No layer queries numerical addition, multiplication, divisibility, parity, BIT, or an index predicate. Each layer performs the same symbol-duplication primitive and consumes a unary stage clock.

This source formalism is not computationally universal at fixed depth; its growth is bounded by a tower of exponentials of fixed height depending on the finite source description.

Branch status:

- \(k=1\): **source PASS under D0L gate**;
- fixed \(k>1\): **source PASS under the declared finite-depth D0L-cascade gate**, subject to independent hostile audit if promoted beyond this branch.

---

## 15. Consequence for the programme invariant

The previous density ladder

\[
N^2
\to
N^{3/2}
\to
N\log N
\]

was not approaching a true general lower bound.

Sparse marker geometry changes the scale entirely:

\[
\boxed{
N^2
\to
N\log N
\to
(\log N)^2
\to
(\log\log N)^2
\to
\cdots
}
\]

while preserving all three properties:

\[
\boxed{
\text{same carrier},
\qquad
\text{FO full order},
\qquad
\text{no FO }+\text{ or }\times.
}
\]

Therefore the robust memory invariant is not finite-window tuple density.

The invariant that survived every compression is:

\[
\boxed{
\text{an infinite nonlocal core with a globally nested comparison code}.}
\]

---

## 16. New frontier

There are now two distinct questions.

### Logical/density frontier

Can a **single fixed** source-safe finite description achieve a marker inverse as slow as \(\log^*N\), or even slower, while preserving the non-leakage proof?

### Invariant frontier

What quantity measures global FO memory in a way invariant under moving witnesses arbitrarily far out in the carrier?

Initial-window cell count no longer does.

Candidates for the next invariant include:

- growth of the first separating witness for the first \(n\) rows;
- witness displacement / escape rate;
- rank of the nested-neighborhood chain;
- definable comparison depth versus witness scale.

The sparse marker ladder therefore does more than improve a bound: it forces a change in what “memory cost” should mean on an infinite carrier.