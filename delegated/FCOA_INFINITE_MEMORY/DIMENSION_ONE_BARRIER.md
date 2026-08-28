# Dimension-One Barrier — Exact Minimality of Two-Coordinate Self-Coordination

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint  
**Scope:** pure-order provenance; finite binary signature / finite-output traces; infinite fixed-carrier branch

## 1. Question

The payload-preserving construction in `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md` uses a dimension-2 interpretation in the pure discrete order and achieves simultaneously:

- every carrier point remains a payload peer;
- no witness-only population;
- every primitive binary relation has bounded atomic ladder depth;
- total primitive incidence cost \(\Theta(N)\);
- FO recovery of a full order of type \(\omega\);
- no FO recovery of ordinary addition or multiplication.

The remaining question was whether the interpretation dimension can be reduced from 2 to 1 while preserving the same properties.

Within the same **pure-order provenance class**, the answer is **no**.

The obstruction is stronger than bounded primitive ladder depth: any one-dimensional pure-order interpretation that FO-recovers an \(\omega\)-order must contain a primitive binary relation with quadratic initial-segment density.

---

## 2. One-dimensional pure-order interpretation

Let

\[
\mathcal O=(\mathbb N,<)
\]

be the source structure. Finite parameters are allowed.

A one-dimensional interpretation of a target relational structure consists of:

1. a unary definable domain \(D(x)\subseteq\mathbb N\);
2. a definable equivalence relation \(E(x,y)\) on \(D\);
3. for every target primitive binary relation \(R_i\), an \(E\)-invariant binary formula
   \[
   \widehat R_i(x,y)
   \]
   definable in \(\mathcal O\).

The target universe is

\[
D/E.
\]

We assume this quotient is infinite.

For finite-output FCOA layers, temporarily name the finite output set and replace every operation layer by its finitely many binary domain/value-fiber traces. Naming outputs only strengthens definability, so a lower bound here transfers back to anonymous outputs.

---

## 3. Unary tail rigidity of the pure discrete order

### Lemma D1-1 — finite/cofinite unary theorem

Every unary subset of \(\mathbb N\) first-order definable in \((\mathbb N,<)\) with finitely many parameters is finite or cofinite.

### Proof

Expand definitionaly by the least element \(0\) and successor \(S\). The complete theory of

\[
(\mathbb N,0,S,<)
\]

admits quantifier elimination. A unary formula is therefore equivalent to a Boolean combination of comparisons between finitely many bounded successor iterates of \(x\) and fixed parameter/constant terms. Beyond the largest such constant/offset, all those atoms have fixed truth values. Hence the unary formula is eventually constant. \(\square\)

Classical reference: Enderton, *A Mathematical Introduction to Logic*, 2nd ed., Theorem 32A; Marker, *Model Theory: An Introduction*, Exercise 3.4.4.

Consequently, if the interpreted domain \(D\) is infinite, then

\[
\boxed{D\text{ is cofinite}.}
\]

---

## 4. One-dimensional quotients cannot hide pair geometry

### Theorem D1-2 — eventual quotient trivialization

Let \(D/E\) be an infinite one-dimensional interpretation quotient in the pure discrete order. Then \(E\) is eventually equality: there exists \(B\) such that for all

\[
x,y>B,
\]

\[
E(x,y)\iff x=y.
\]

### Proof

Because the source order is a well-order, every nonempty \(E\)-class has a least element. Define the set of canonical representatives

\[
\operatorname{Rep}(x):=
D(x)\wedge
\forall y\bigl(D(y)\wedge E(y,x)\to \neg(y<x)\bigr).
\]

There is exactly one representative per \(E\)-class.

Since \(D/E\) is infinite, \(\operatorname{Rep}\) is infinite. By Lemma D1-1, \(\operatorname{Rep}\) is therefore cofinite.

Choose \(B\) beyond its finite complement. Then every \(x>B\) is the least member of its class. If distinct \(x,y>B\) were \(E\)-equivalent, the larger of the two would fail to be the least representative of that class, contradiction.

Hence distinct sufficiently large elements are never equivalent. Reflexivity gives equality. \(\square\)

### Consequence

A one-dimensional quotient over pure order cannot asymptotically simulate the pair universe

\[
\mathbb N^2.
\]

Any infinite quotient becomes, after finitely many exceptional points, an ordinary one-copy carrier with absolute equality.

This closes the most serious quotient loophole in the dimension comparison.

---

## 5. Tail normal form for every primitive relation

After replacing the interpreted quotient by its cofinite canonical representative set, every target primitive binary relation becomes an ordinary binary relation

\[
R_i^*(x,y)
\]

FO-definable in the pure discrete order.

By the already proved Tail Normal Form / Order-Only Quadratic Barrier, each such relation satisfies exactly one of two asymptotic regimes:

### local regime

\[
|R_i^*\cap[0,N]^2|=O(N),
\]

and outside a finite boundary every edge has bounded source-order distance;

### global-tail regime

\[
|R_i^*\cap[0,N]^2|=\Theta(N^2).
\]

There is no intermediate density.

---

## 6. A definable omega-order cannot distort rank substantially

The interpreted target may define an order

\[
\prec
\]

which is not literally the source order \(<\). We must therefore compare target initial-segment cost with source initial-segment cost.

### Lemma D1-3 — bounded rank distortion

Let \(\prec\) be an FO-definable strict linear order of type \(\omega\) on a cofinite subset of \((\mathbb N,<)\). Then there exist constants \(B,K\) such that for all sufficiently large \(x,y\):

\[
|x-y|>K
\quad\Longrightarrow\quad
(x\prec y\iff x<y).
\]

Consequently the \(\prec\)-rank of \(x\) differs from its source rank by at most a constant:

\[
\boxed{
\operatorname{rk}_{\prec}(x)=x+O(1).
}
\]

### Proof

Apply the binary Tail Normal Form to the formula \(x\prec y\). For sufficiently separated large \(x,y\), its truth depends only on whether \(x<y\) or \(y<x\).

Because \(\prec\) is a strict total order, exactly one of the two remote orientations must be selected.

If the selected remote orientation were reverse source order, then any sufficiently large point \(y\) would have infinitely many \(\prec\)-predecessors: every sufficiently large source point \(x>y+K\) would satisfy \(x\prec y\). That is impossible in an order of type \(\omega\), where each point has only finitely many predecessors.

Therefore the remote orientation agrees with \(<\).

For a large \(x\), every source point below \(x-K\) lies \(\prec\)-before \(x\), and every source point above \(x+K\) lies \(\prec\)-after \(x\). Only the finite boundary and the \(2K+1\) nearby points can change relative rank. Hence rank distortion is bounded. \(\square\)

### Density transfer

Therefore for every fixed binary relation \(R\),

\[
|R\cap[0,N]^2|=O(N)
\]

in source-order windows iff it is \(O(N)\) in \(\prec\)-windows, up to changing constants. The same holds for \(\Theta(N^2)\).

So the cost metric used by the payload-preserving construction is compatible with the one-dimensional source-order dichotomy.

---

## 7. Main no-go theorem

### Theorem D1-4 — Dimension-One Linear-Cost Barrier

Let \(\mathcal A\) be an infinite finite-signature structure obtained by a one-dimensional FO interpretation in pure discrete order \((\mathbb N,<)\), with finitely many parameters allowed and arbitrary definable quotient equality.

Assume \(\mathcal A\) FO-defines a strict linear order \(\prec\) of type \(\omega\) on its full interpreted carrier.

Then at least one primitive binary relation of \(\mathcal A\) has

\[
\boxed{
\Theta(N^2)
}

incidences in the first \(N\) points of the recovered order.

Equivalently, if the total primitive binary incidence cost is

\[
O(N),
\]

then no FO formula can define a full \(\omega\)-order on the interpreted carrier.

### Proof

By D1-2, replace the quotient outside finitely many exceptional points by its cofinite canonical representative set with absolute equality.

Assume for contradiction that every primitive binary relation is subquadratic in recovered-order windows. By D1-3 the same is true in source-order windows.

By the order-only linear/quadratic dichotomy, every primitive relation is therefore in the local regime: after removing one common finite boundary, every primitive edge has uniformly bounded source-order distance.

Because the signature is finite, the union Gaifman graph of all primitive traces is locally finite after that finite apex set is removed.

The Finite-Apex Locality Barrier / Sparse Memory Threshold then says that no FO formula in this structure can define a strict linear order on the infinite residual carrier.

Contradiction. \(\square\)

---

## 8. Finite-output FCOA corollary

### Corollary D1-4A

Consider finitely many partial binary operation layers with finite terminal output alphabets, obtained by a one-dimensional pure-order interpretation as above.

If their operation structure FO-recovers a full carrier order of type \(\omega\), then the number of defined generic-generic cells among the first \(N\) recovered carrier points is

\[
\boxed{\Theta(N^2).}
\]

In particular a one-dimensional pure-order source cannot simultaneously have

\[
\Theta(N)
\]

primitive operation cost and FO full-order recovery.

### Proof

Name the finite outputs and pass to binary domain/value-fiber traces. If total operation definedness were \(O(N)\), every fiber would be \(O(N)\). D1-4 gives the contradiction. \(\square\)

---

## 9. Bounded primitive ladder depth is not the decisive obstruction

The user target also required every primitive relation to have bounded half-graph/ladder depth.

D1-4 is stronger in a different direction: it rules out the desired dimension-1 package **without using that assumption at all**.

Thus

\[
\boxed{
\text{dimension 1}
+\text{pure-order provenance}
+\text{linear primitive cost}
+\text{FO }\omega\text{-order}
}

is already inconsistent.

Adding bounded primitive ladder depth cannot rescue it.

Note that quadratic density alone does not force an atomic half-graph: for example a complete relation can be dense but ladder-shallow. Hence the correct one-dimensional obstruction is the density/locality theorem, not ladder depth by itself.

---

## 10. Arithmetic leakage requirement becomes vacuous at dimension 1

The target package also demanded nondefinability of ordinary \(+\) and \(\times\).

Within the pure-order one-dimensional linear-cost class, the package already fails earlier: FO full order cannot be recovered at all.

Therefore no separate arithmetic-leakage argument is needed for the no-go theorem.

If the linear-cost condition is dropped and a quadratic order-only relation is allowed, pure-order provenance still ensures that ordinary external-index addition and multiplication are not automatically introduced, but that is a different regime already covered by the dense order-only constructions.

---

## 11. Exact minimality of dimension 2

The dimension-2 construction from `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md` supplies the matching upper bound:

\[
\boxed{
\begin{array}{c|c}
\text{interpretation dimension} & \text{linear-cost payload-preserving derived FO order}\\
\hline
1 & \text{impossible under pure-order provenance}\\
2 & \text{possible}
\end{array}
}
\]

The dimension-2 structure has:

\[
\boxed{
C_{\rm prim}(N)=\Theta(N),
}
\]

no witness-only population, bounded atomic ladder depth in every primitive binary relation, FO recovery of a full \(\omega\)-order, and no FO ordinary addition or multiplication.

Hence:

### Theorem D1-5 — Exact Self-Coordination Dimension

Within the pure-order finite-signature provenance class,

\[
\boxed{
\operatorname{dim}_{\rm self}=2
}
\]

is the exact minimum interpretation dimension for the package

\[
\boxed{
\text{payload preservation}
+\Theta(N)\text{ primitive cost}
+\text{bounded primitive ladder depth}
+\text{FO full }\omega\text{-order}
+\text{no FO ordinary arithmetic}.
}
\]

The lower bound is D1-4; the upper bound is PP-7.

---

## 12. Why dimension 2 escapes the theorem

A one-dimensional pure-order relation has only two remote orientations. Quantifier elimination forces it eventually either to remain local or to occupy an entire remote orientation, producing the linear/quadratic dichotomy.

Dimension 2 introduces an internal Cartesian square. A payload point

\[
(i,j)
\]

can simultaneously project to two independent diagonal coordinates. The primitive relations need only store:

- first-coordinate projection;
- second-coordinate projection;
- a unary/loop upper-triangle bit.

The dense comparison geometry exists in **coordinate space**, but its materialization in primitive carrier tuples is linear because each pair \((i,j)\) is itself one payload point.

Thus the new resource is not hidden arithmetic; it is genuinely higher interpretation dimension.

---

## 13. Quotient loophole audit

A hostile reviewer might try to use a one-dimensional quotient to compress multiple source positions into interpreted pair-like states.

D1-2 closes exactly this route:

\[
\boxed{
\text{infinite 1D pure-order quotient}
\Longrightarrow
\text{eventual equality}.}
\]

The proof is elementary but important: canonical least representatives form an infinite unary definable set, hence a cofinite set. Therefore almost every source point must already be the unique representative of its class.

No asymptotic pair coding survives.

---

## 14. Scope boundary

The exact dimension-2 minimality theorem is relative to the chosen provenance base:

\[
\boxed{(\mathbb N,<)\text{ with finite parameters}.}
\]

It does **not** claim that every conceivable one-dimensional primitive non-order source is impossible.

For example, the earlier D0L/exponential marker constructions are not one-dimensional interpretations of pure order; they deliberately add a new primitive global skeleton. They therefore lie outside D1-5.

So the correct statement is:

> Dimension 2 is the exact minimum for **pure-order-derived, payload-preserving, linear-cost derived instability**.

A broader theorem allowing non-order primitive source mechanisms would require a separate source-class definition and cannot be inferred from D1-5.

---

## 15. Programme consequence

The current infinite-memory architecture now has an exact structural boundary:

\[
\boxed{
\begin{array}{c}
\text{dimension 1 pure-order source}\\
\Downarrow\\
\text{linear primitive memory stays local after finite apex removal}\\
\Downarrow\\
\text{no FO global order}
\end{array}
}
\]

whereas

\[
\boxed{
\begin{array}{c}
\text{dimension 2 pure-order self-coordination}\\
\Downarrow\\
\text{stable infinite coordinate fibres}\\
\Downarrow\\
\text{derived instability}\\
\Downarrow\\
\text{FO global order at }\Theta(N)\text{ primitive cost}.
\end{array}
}
\]

This identifies **interpretation dimension 2** as the first place where pure-order geometry can be folded into a linear-cost payload carrier without primitive half-graph memory.

---

## 16. Next frontier

The dimension question is closed for the pure-order provenance class.

The next genuinely open direction is no longer “1 or 2?” but one of the following:

1. **source-class extension:** characterize which non-order primitive one-dimensional sources can simulate the dimension-2 effect without leaking arithmetic;
2. **minimal signature:** can PP-7 be reduced from three primitive binary traces to two or even one while keeping dimension 2 and bounded atomic ladder depth;
3. **minimal nonlocality:** quantify the least infinite-fibre complexity needed for dimension-2 derived instability;
4. **finite approximation:** determine the exact finite \(N\) cost and rigidity behavior of finite square/self-coordinate truncations.

For the current pure-order interpretation framework, however, the structural minimum is now exact:

\[
\boxed{\operatorname{dim}_{\rm self}=2.}
\]