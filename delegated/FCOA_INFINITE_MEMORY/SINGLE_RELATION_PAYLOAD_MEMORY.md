# Single-Relation Payload Memory — Minimal Primitive Signature at Dimension Two

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint  
**Scope:** infinite fixed-carrier branch; pure-order dimension-2 provenance

## 1. Target

`PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md` used three primitive binary relations

\[
P_1,\qquad P_2,\qquad M
\]

on the payload carrier

\[
U=\mathbb N^2
\]

to obtain:

- payload preservation;
- no witness-only population;
- bounded atomic ladder depth;
- \(\Theta(N)\) primitive incidence cost;
- FO recovery of a full order of type \(\omega\);
- no FO ordinary addition or multiplication.

The question is whether the primitive signature can be reduced from three binary traces to two, or even to one.

It can be reduced to **one**.

---

## 2. Carrier and notation

Let

\[
U=\mathbb N^2.
\]

Write

\[
d_i=(i,i)
\]

for the diagonal representative of coordinate \(i\).

Every point \((i,j)\) remains a generic payload peer.

No auxiliary sort or witness-only population is introduced.

---

## 3. One primitive binary relation

Define a single directed binary relation \(E\subseteq U^2\).

For

\[
x=(i,j),\qquad y=(k,\ell),
\]

set

\[
\boxed{
E(x,y)
\iff
\bigl(y=d_i\bigr)
\vee
\bigl(x=d_\ell\bigr)
\vee
\bigl(i<j\wedge y=d_j\bigr).
}
\]

Equivalently, \(E\) is the union of three edge types:

1. **first-coordinate projection**
   \[
   (i,j)\to d_i;
   \]
2. **reverse second-coordinate projection**
   \[
   d_j\to(i,j);
   \]
3. **upper-triangle marker edge**
   \[
   (i,j)\to d_j
   \qquad\text{when }i<j.
   \]

This one relation contains all the information previously stored separately in \(P_1,P_2,M\).

---

## 4. Diagonal points are FO-definable

A diagonal point has infinitely many outgoing edges because

\[
d_j\to(i,j)
\]

for every \(i\).

An off-diagonal point has at most two outgoing edges:

- always its first-coordinate projection \(d_i\);
- additionally \(d_j\) only if \(i<j\).

Hence the diagonal can be defined by the finite degree threshold

\[
\boxed{
D(x):=
\exists y_1y_2y_3\;
\Bigl(
\bigwedge_{p\ne q}y_p\ne y_q
\wedge
\bigwedge_{p=1}^3E(x,y_p)
\Bigr).
}
\]

Then

\[
D(U)=\{d_0,d_1,d_2,\ldots\}.
\]

---

## 5. Recovering the second-coordinate projection

For every payload point \(x=(i,j)\), the unique diagonal point with an edge **into** \(x\) is \(d_j\).

Thus define

\[
\boxed{
P_2^E(x,y):=D(y)\wedge E(y,x).
}
\]

Then

\[
P_2^E((i,j),d_k)
\iff
k=j.
\]

So the second-coordinate projection is FO-recovered from \(E\).

---

## 6. Recovering the first-coordinate projection

For an off-diagonal point \(x=(i,j)\), the first-coordinate representative \(d_i\) is the unique diagonal out-neighbor different from the second-coordinate representative \(d_j\).

For a diagonal point \(d_i\), both coordinates equal \(d_i\).

Define

\[
\boxed{
P_1^E(x,y):=
D(y)\wedge E(x,y)
\wedge
\Bigl(
(D(x)\wedge x=y)
\vee
(\neg D(x)\wedge\neg P_2^E(x,y))
\Bigr).
}
\]

Then

\[
P_1^E((i,j),d_k)
\iff
k=i.
\]

Hence the first-coordinate projection is also recovered.

---

## 7. Recovering the upper-triangle marker

For an off-diagonal point \(x=(i,j)\), the relation contains the extra edge

\[
x\to d_j
\]

exactly when

\[
i<j.
\]

Since \(d_j\) is already definable as the unique \(P_2^E\)-target, define

\[
\boxed{
U^E(x):=
\neg D(x)
\wedge
\exists y\bigl(P_2^E(x,y)\wedge E(x,y)\bigr).
}
\]

Then

\[
U^E(i,j)
\iff
i<j.
\]

If one wants the old loop marker relation, define

\[
M^E(x,y):=x=y\wedge U^E(x).
\]

Thus the original triple

\[
(P_1,P_2,M)
\]

is FO-definable from the single primitive relation \(E\).

Conversely, \(E\) is FO-definable from \((P_1,P_2,M)\) by taking the union of the first projection, the reverse second projection, and the marked second-projection edge.

Therefore:

### Theorem SR-1 — interdefinability

\[
\boxed{
(U;E)
\quad\text{and}\quad
(U;P_1,P_2,M)
\text{ are FO-interdefinable}.}
\]

---

## 8. Full order recovery transfers immediately

Because the three-relation payload structure is FO-definable from \(E\), every derived construction from `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md` transfers.

In particular:

1. the diagonal order is defined by
   \[
   d_i<d_j
   \iff
   \exists w\bigl(U^E(w)\wedge P_1^E(w,d_i)\wedge P_2^E(w,d_j)\bigr);
   \]
2. each payload point FO-recovers its two diagonal coordinates;
3. the max-shell key is FO-definable;
4. the shell-lexicographic order \(\prec\) of type \(\omega\) on all payload points is FO-definable.

Hence:

### Theorem SR-2 — one relation recovers the full payload order

\[
\boxed{
(U;E)\Rightarrow_{\rm FO}(U,\prec)\cong(\mathbb N,<).
}
\]

The instability is still derived: it is absent from the primitive relation as an unbounded ladder and appears only after FO composition.

---

## 9. Atomic ladder depth remains uniformly bounded

The primitive relation \(E\) is not itself a half-graph carrier of unbounded depth.

### Theorem SR-3 — atomic ladder depth at most two

There is no \(E\)-half-graph of depth \(3\).

### Proof

Assume distinct left vertices

\[
a_0,a_1,a_2
\]

and distinct right vertices

\[
b_0,b_1,b_2
\]

satisfy

\[
E(a_i,b_j)
\iff i\le j.
\]

Then \(a_0\) must hit three distinct right vertices. Therefore \(a_0\) must be diagonal, because every off-diagonal point has out-degree at most two.

Let

\[
a_0=d_t.
\]

Its out-neighborhood is exactly the second-coordinate column

\[
C_t=\{(q,t):q\in\mathbb N\}.
\]

Now \(a_1\) must hit both \(b_1\) and \(b_2\), so these two distinct vertices lie in

\[
N_E(a_0)\cap N_E(a_1).
\]

If \(a_1\) is diagonal and distinct from \(a_0\), then its column neighborhood is disjoint from \(C_t\), impossible.

If \(a_1\) is off-diagonal, all of its out-neighbors are diagonal points, while \(C_t\) contains exactly one diagonal point, namely \(d_t\). Hence

\[
|N_E(a_0)\cap N_E(a_1)|\le1,
\]

again impossible because it would have to contain distinct \(b_1,b_2\).

Contradiction. \(\square\)

Depth \(2\) does occur, so the exact atomic ladder depth is two under the usual convention.

Therefore

\[
\boxed{
\lambda_E^{\rm atomic}=2<\infty.
}
\]

---

## 10. Primitive incidence cost remains linear

Take the complete shell window

\[
W_m=\{(i,j):0\le i,j\le m\},
\qquad |W_m|=(m+1)^2.
\]

Inside \(W_m\):

1. first-projection edges contribute
   \[
   (m+1)^2;
   \]
2. reverse second-projection edges contribute
   \[
   (m+1)^2;
   \]
3. the diagonal self-edges have been counted in both families, so subtract
   \[
   m+1;
   \]
4. upper-triangle marker edges contribute
   \[
   \frac{m(m+1)}2.
   \]

Thus

\[
|E\cap W_m^2|
=
2(m+1)^2-(m+1)+\frac{m(m+1)}2.
\]

Hence:

### Theorem SR-4 — linear one-relation cost

For the intrinsic first \(N\) points of the recovered payload order,

\[
\boxed{
C_E(N)=\Theta(N).
}
\]

Thus compressing three primitive relations to one does not change the asymptotic memory scale.

---

## 11. Arithmetic non-leakage transfers by interdefinability

By SR-1, the one-relation structure is FO-interdefinable with the previously audited dimension-2 payload structure.

Therefore the nondefinability proofs transfer exactly:

\[
\boxed{
E\not\Rightarrow_{\rm FO}+,
\qquad
E\not\Rightarrow_{\rm FO}\times.
}
\]

More explicitly, the structure has the same dimension-2 interpretation in pure discrete order. If ordinary addition in the recovered payload order were definable, restricting parity to the definable coordinate line would define the even numbers in pure \((\mathbb N,<)\), impossible by discrete-order quantifier elimination. Multiplication would then imply addition via Julia Robinson once recovered successor is available.

No new arithmetic source is introduced by the signature compression.

---

## 12. FCOA one-operation realization

Introduce one terminal output \(\Omega\) and one partial binary operation

\[
\boxed{
x\star y=\Omega
\iff E(x,y).
}
\]

The generic-generic domain trace of this single operation is exactly \(E\).

Therefore the whole payload-preserving derived-instability mechanism can be realized with:

\[
\boxed{
1\text{ partial binary operation layer}
+1\text{ terminal output}.}
\]

No value-fiber multiplicity is needed.

---

## 13. Exact primitive-signature minimum

Zero primitive binary traces cannot define an infinite linear order on a pure payload set: with only equality and finitely many named constants/unary finite boundary data, the infinite residual set has the full symmetric group as automorphisms, so no strict linear order is definable.

One primitive binary trace suffices by SR-2.

Hence:

### Theorem SR-5 — exact binary signature minimum

Within the dimension-2 pure-order payload-preserving class,

\[
\boxed{
\#\text{primitive binary traces}_{\min}=1.
}
\]

In the partial-operation presentation,

\[
\boxed{
\#\text{operation layers}_{\min}=1,
\qquad
|O|_{\min}=1.
}
\]

This is an exact minimum.

---

## 14. Combined exact boundary

Together with `DIMENSION_ONE_BARRIER.md`, the current package is now sharp in two independent structural coordinates:

\[
\boxed{
\operatorname{dim}_{\rm self}=2
}
\]

and

\[
\boxed{
\#\text{primitive binary traces}=1.
}
\]

The resulting extremal package is:

\[
\boxed{
\begin{array}{l}
\text{interpretation dimension }2;\\
\text{one primitive binary relation};\\
\text{one one-output partial-operation layer};\\
\text{all carrier points are payload peers};\\
\text{no witness-only population};\\
\text{atomic ladder depth }2;\\
\Theta(N)\text{ primitive incidence cost};\\
\text{FO full order of type }\omega;\\
\text{no FO ordinary }+;\\
\text{no FO ordinary }\times.
\end{array}}
\]

---

## 15. What resource remains nontrivial

After this compression, none of the following is still a candidate irreducible cost:

- number of primitive relations;
- number of operation layers;
- number of terminal outputs;
- primitive ladder depth;
- asymptotic primitive incidence above linear;
- witness-only role inflation.

The surviving structural resource is the same one isolated by the dimension barrier:

\[
\boxed{
\text{two-coordinate self-coordination with stable infinite fibres}.}
\]

The one relation \(E\) packages those fibres using directionality.

---

## 16. Next frontier

The signature question is now closed inside the current provenance class.

The next genuine minimization questions are finer:

1. can directionality be removed, i.e. can an **undirected/symmetric single relation** achieve the same package;
2. can the one-output partial operation be required to satisfy an algebraic law such as commutativity without restoring a primitive half-graph or arithmetic leakage;
3. can the infinite inverse fibres be weakened while retaining dimension-2 derived instability;
4. what is the exact finite-truncation cost and rigidity profile of the single-relation construction.

The cleanest next strike is the first:

\[
\boxed{
\text{is directedness itself essential?}
}
\]
