# Ladder Escape Invariant — A Representation-Robust Cost for Infinite FO Order Memory

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Status:** theorem checkpoint  
**Scope:** infinite fixed-carrier branch; quantitative refinement for nested-neighborhood/Ferrers order codes

## 1. Motivation

The sparse marker construction showed that the raw count

\[
C_R(N)=|R\cap[0,N]^2|
\]

can be made extremely small while preserving FO recovery of the full order. The apparent paradox is resolved by observing that the relation does not eliminate comparison witnesses; it pushes them to very large carrier ranks.

Therefore the correct cost cannot be a one-variable density function alone. It must simultaneously measure:

1. **how many order distinctions have been resolved**;
2. **how far one must travel to find the witnesses that resolve them**;
3. **how many primitive incidences those witnesses necessarily carry**.

For the nested-row architecture this can be done exactly.

The resulting invariant is naturally connected with the classical **half-graph / ladder / order-property** pattern of model theory and with Ferrers/chain relations in graph theory.

---

## 2. Nested-row order codes are Ferrers relations

Let

\[
G_\omega=\{Q_0,Q_1,Q_2,\ldots\}
\]

and let \(R\subseteq G_\omega^2\). Write

\[
N_i=\{z:R(Q_i,z)\}
\]

for the row-neighborhood of \(Q_i\).

Assume

\[
\boxed{
N_0\supsetneq N_1\supsetneq N_2\supsetneq\cdots.
}
\]

Then the out-neighborhoods are linearly ordered by inclusion. In graph-theoretic language this is the characteristic Ferrers/chain condition. Ferrers digraphs are classically characterized by nested out-neighborhoods (equivalently nested in-neighborhoods).

The carrier order is FO-definable by

\[
Q_i<Q_j
\iff
N_j\subsetneq N_i.
\]

Thus every nested-row FCOA order code is a Ferrers-type order memory layer.

---

## 3. Canonical separators

For each adjacent pair define the difference layer

\[
D_i=N_i\setminus N_{i+1}.
\]

Strict nesting implies

\[
D_i\ne\varnothing.
\]

Because the recovered order has type \(\omega\), every nonempty subset has a least element. Define the **canonical separator**

\[
\boxed{
s_i=\min_{<}D_i.
}
\]

The map \(i\mapsto s_i\) is itself FO-definable from \(R\):

- \(<\) is defined by strict row inclusion;
- successor in the recovered order is FO-definable;
- \(s_i\) is the least point satisfying \(R(Q_i,s_i)\wedge\neg R(Q_{i+1},s_i)\).

Thus separator position is not an externally imposed bookkeeping choice once the order has been recovered.

---

## 4. Canonical Half-Graph Theorem

### Theorem LE-1 — strict nested rows force an infinite half-graph

For all \(i,j\in\mathbb N\),

\[
\boxed{
R(Q_i,s_j)
\iff
i\le j.
}
\]

### Proof

By definition,

\[
s_j\in N_j
\qquad\text{and}\qquad
s_j\notin N_{j+1}.
\]

If \(i\le j\), nestedness gives

\[
N_i\supseteq N_j,
\]

so

\[
s_j\in N_i.
\]

If \(i>j\), then

\[
N_i\subseteq N_{j+1},
\]

so

\[
s_j\notin N_i.
\]

Hence the displayed equivalence holds. \(\square\)

The bipartite incidence matrix between

\[
Q_0,Q_1,Q_2,\ldots
\]

and

\[
s_0,s_1,s_2,\ldots
\]

is therefore triangular. This is exactly the classical infinite half-graph (also called a ladder, up to the conventional choice of \(<\) versus \(\le\)).

---

## 5. Model-theoretic meaning: order property

A formula \(\varphi(x,y)\) has the order property if it realizes arbitrarily long finite patterns

\[
\varphi(a_i,b_j)
\iff
i<j.
\]

Half-graphs are the canonical graph-theoretic witnesses of this order property. A complete theory is stable exactly when no formula has the order property.

Therefore LE-1 yields:

### Corollary LE-1A

Every infinite nested-row order code is unstable already at the level of its primitive binary relation \(R\).

This is stronger than merely saying that a derived FO formula defines a linear order: the primitive memory relation itself contains an infinite ladder.

### General FO consequence

More broadly, **any** structure in which an infinite linear order is FO-definable has an unstable theory, because the defining order formula itself has the order property.

Hence the FO memory boundary has a classical stability-theoretic reformulation:

\[
\boxed{
\text{FO recovery of an infinite linear order}
\Longrightarrow
\text{order property / instability}.}
\]

For the canonical G2 successor reduct the earlier quantifier-elimination/locality analysis places the structure on the opposite side: no formula can realize unbounded half-graph order patterns. Thus the G2-to-global-order transition can be read as a **stable-to-unstable memory transition**.

---

## 6. Distinct separators cannot be reused

### Lemma LE-2

The canonical separators

\[
s_0,s_1,s_2,\ldots
\]

are pairwise distinct.

### Proof

If \(i<j\), then by LE-1

\[
R(Q_{i+1},s_j)
\]

because \(i+1\le j\), while

\[
\neg R(Q_{i+1},s_i)
\]

by definition of \(s_i\in N_i\setminus N_{i+1}\). Hence \(s_i\ne s_j\). \(\square\)

So one target element cannot certify two different adjacent row boundaries in a strict nested chain.

This is the first no-free-lunch principle hidden by finite-window sparsification.

---

## 7. Intrinsic quadratic witness cost

Suppose we want to resolve the order of the first \(r\) source points

\[
Q_0,\ldots,Q_{r-1}.
\]

The adjacent strict inclusions

\[
N_0\supsetneq N_1\supsetneq\cdots\supsetneq N_{r-1}
\]

require the distinct separators

\[
s_0,\ldots,s_{r-2}.
\]

By LE-1, the separator \(s_j\) is incident with exactly the first

\[
j+1
\]

source rows among this prefix.

Therefore the canonical witnessing substructure contains

\[
\sum_{j=0}^{r-2}(j+1)
=\frac{r(r-1)}2
\]

primitive incidences.

### Theorem LE-3 — quadratic resolved-prefix cost

Every strict nested-row order code requires at least

\[
\boxed{
\frac{r(r-1)}2
}
\]

primitive \(R\)-incidences in any witness set certifying all adjacent inclusions among the first \(r\) ordered source points.

The half-graph itself attains equality.

Thus:

\[
\boxed{
\text{quadratic cost reappears when cost is normalized by resolved order length, not ambient rank}.}
\]

This is the central repair of the misleading finite-window density invariant.

---

## 8. Escape profile

Let \(\operatorname{rk}(x)\) denote the rank of \(x\) in the FO-recovered order of type \(\omega\).

Define the **separator escape sequence**

\[
\boxed{
e(i)=\operatorname{rk}(s_i).}
\]

Define the **prefix escape cost**

\[
\boxed{
E(r)=\max_{0\le i<r-1} e(i)
}
\]

for \(r\ge2\).

Thus \(E(r)\) is the smallest carrier scale by which the canonical separators for the first \(r\) source points have all appeared.

Since \(<\) and the separator map are FO-definable from \(R\), and the order type \(\omega\) is rigid, the sequence \(e(i)\) and the profile \(E(r)\) are invariants of the isomorphism type of the nested-row structure. They do not depend on arbitrary relabeling.

This is the desired representation-robust version of “witness displacement.”

---

## 9. Resolution function

Define the dual **resolution profile**

\[
\boxed{
\rho(M)
=
\max\{r:E(r)\le M\}.
}
\]

Thus \(\rho(M)\) is the length of the largest initial source prefix whose adjacent row distinctions have all received canonical witnesses by carrier scale \(M\).

Equivalently, it measures the order depth resolved inside the first \(M\) ranks.

The functions \(E\) and \(\rho\) are generalized inverses.

---

## 10. Density–resolution law

Let

\[
C_R(M)=|R\cap[0,M]^2|
\]

where \([0,M]\) is understood intrinsically as the first \(M+1\) points of the recovered order.

### Theorem LE-4 — density–resolution inequality

For every \(M\),

\[
\boxed{
C_R(M)
\ge
\frac{\rho(M)(\rho(M)-1)}2.
}
\]

Equivalently, for every \(r\ge2\),

\[
\boxed{
C_R(E(r))
\ge
\frac{r(r-1)}2.
}
\]

### Proof

If \(E(r)\le M\), then the first \(r-1\) canonical separators all lie in the first \(M+1\) target points. The first \(r\) source points also lie there once \(M\ge r-1\), which follows automatically for all nondegenerate large prefixes and can be enforced by replacing \(E(r)\) with \(\max(E(r),r-1)\).

LE-1 then places an \(r\)-row triangular half-graph inside the window. Its primitive incidence count is exactly \(r(r-1)/2\). \(\square\)

Hence

\[
\boxed{
\rho(M)
\le
\frac{1+\sqrt{1+8C_R(M)}}2
=O(\sqrt{C_R(M)}).
}
\]

A sparse window can resolve only a correspondingly short prefix unless the witnesses are allowed to escape beyond that window.

---

## 11. Sparse Marker Ladder is extremal

For a strictly increasing marker sequence

\[
a_0<a_1<a_2<\cdots
\]

define

\[
R_a(Q_n,Q_m)
\iff
\exists j\ge n\;(m=a_j).
\]

Then

\[
N_n\setminus N_{n+1}=\{Q_{a_n}\},
\]

so

\[
\boxed{s_n=Q_{a_n},\qquad e(n)=a_n.}
\]

At the exact scale

\[
M=a_{r-2},
\]

the only marker columns visible are

\[
a_0,\ldots,a_{r-2}.
\]

Their incidences with the first \(r\) rows form precisely the triangular half-graph and no redundant columns are present. Therefore

\[
\boxed{
C_{R_a}(E(r))
=
\frac{r(r-1)}2.
}
\]

Thus the sparse marker ladder **saturates the universal nested-row lower bound exactly**.

It is not cheating the intrinsic cost. It is an optimal compression that removes every redundant witness and pays solely by moving the indispensable separators farther out.

---

## 12. Dense tails versus sparse markers

For the dense threshold relation

\[
R_f(n,m)\iff m\ge f(n),
\]

we have

\[
N_n\setminus N_{n+1}
=
[f(n),f(n+1)-1].
\]

Hence the canonical separator is

\[
s_n=f(n).
\]

The escape profile is essentially the same as for the corresponding sparse-marker code using marker sequence \(a_n=f(n)\).

But the dense tail retains every point between thresholds and after them, producing many columns with duplicate or redundant cut patterns.

Therefore:

\[
\boxed{
\text{dense tail and sparse marker have comparable escape cost, but sparse marker is incidence-optimal}.}
\]

This explains precisely why the earlier \(N\log N\) dense-tail bound collapsed to \((\log N)^2\) after marker sparsification.

---

## 13. Examples

### Exponential marker ladder

\[
a_n=2^n.
\]

Then

\[
E(r)=2^{r-2}
\]

up to the indexing convention, and

\[
\rho(M)=\Theta(\log M).
\]

Therefore

\[
C(M)=\Theta((\log M)^2),
\]

which saturates LE-4.

### Fixed-height exponential cascade

If

\[
a_n=E_k(n)
\]

with fixed \(k\)-fold iterated exponentiation, then

\[
\rho(M)=\Theta(\log^{(k)}M)
\]

and

\[
C(M)=\Theta((\log^{(k)}M)^2).
\]

Again LE-4 is saturated.

So every gain in visible density is paid for exactly by a corresponding deterioration of the escape profile.

---

## 14. Ladder profile as the deeper invariant

The classical terminology suggests an even more intrinsic formulation.

For a binary relation \(R\) and an intrinsic initial segment \([0,M]\), define the **half-graph depth**

\[
\lambda_R(M)
\]

as the largest \(r\) for which there exist

\[
a_0,\ldots,a_{r-1},
\qquad
b_0,\ldots,b_{r-1}
\in[0,M]
\]

with

\[
R(a_i,b_j)
\iff
i\le j.
\]

For nested-row codes, the canonical separators give

\[
\lambda_R(M)\ge \rho(M)-1,
\]

and in sparse marker ladders these quantities agree up to the indexing convention.

This parameter is directly tied to the model-theoretic order property:

\[
\boxed{
R\text{ has the order property}
\iff
\sup_M\lambda_R(M)=\infty
}
\]

when the recovered order exhausts the carrier by finite initial segments.

Thus the hierarchy is:

\[
\boxed{
\text{order property / unbounded ladder depth}
\quad\text{(qualitative memory)}
}
\]

plus

\[
\boxed{
\lambda_R(M)\text{ or }E(r)
\quad\text{(quantitative rate at which that memory becomes visible)}.
}
\]

---

## 15. Stability-theoretic reinterpretation of the FCOA boundary

The infinite programme can now be restated in a classical model-theoretic coordinate.

### G2 local successor memory

The successor structure has quantifier elimination into bounded successor comparisons. It cannot realize arbitrarily large order-property ladders. Hence the local-memory reduct lies on the stable side of the boundary.

### FO global-order memory

Any enrichment defining the full infinite linear order is necessarily unstable because the defining order formula has the order property.

### Primitive nested-row memory

The relation itself contains the half-graph canonically, so instability is primitive rather than only derived.

Thus the transition can be summarized as

\[
\boxed{
\text{local successor memory}
\longrightarrow
\text{global FO order memory}
}
\]

corresponding to

\[
\boxed{
\text{no order property}
\longrightarrow
\text{order property / instability}.
}
\]

This is a stronger conceptual invariant than automorphism rigidity and a more representation-robust one than raw tuple density.

---

## 16. What has now been proved

For the nested-neighborhood/Ferrers order-code architecture:

1. strict row inclusion automatically creates an infinite half-graph;
2. canonical separating witnesses are definable and pairwise distinct;
3. resolving the first \(r\) ordered rows requires an intrinsic triangular witness pattern with
   \[
   r(r-1)/2
   \]
   primitive incidences;
4. finite-window density and witness escape obey the exact tradeoff
   \[
   C_R(E(r))\ge r(r-1)/2;
   \]
5. sparse marker ladders attain equality and are therefore optimally compressed within this architecture;
6. their tiny values of \(C_R(N)\) come entirely from enormous witness displacement, not from eliminating the underlying quadratic resolved-prefix incidence cost.

---

## 17. New programme invariant

The branch should therefore stop treating

\[
C_R(N)
\]

alone as “memory cost.”

For nested-row codes the natural invariant is the **Ladder–Escape profile**

\[
\boxed{
\mathcal L_R=(E_R(r),\rho_R(M),\lambda_R(M)).
}
\]

A compact two-coordinate version is

\[
\boxed{
\text{resolved order depth}
\quad\text{versus}\quad
\text{witness scale}.}
\]

Primitive incidence count is then constrained by the universal triangular law.

This profile survives every sparse-marker compression considered so far and exposes exactly where the apparent savings are paid.

---

## 18. Literature positioning

The underlying notions are classical and no novelty claim is made for them:

- half-graphs/ladders are canonical combinatorial encodings of total order;
- the order property characterizes instability in classical stability theory;
- Ferrers/chain relations are characterized by nested neighborhoods.

The FCOA-specific result is the identification of these notions as the correct repair of the failed finite-window density invariant and the exact triangular escape-cost law for the nested-row memory architecture.

Relevant literature anchors include:

- standard stability theory: formula order property and half-graph witnesses;
- M. Sokołowski, *Bounds on half graph orders in powers of sparse graphs*, arXiv:2103.06218;
- Ferrers digraph literature characterizing the class by linearly nested neighborhoods.

---

## 19. Next frontier

The remaining hard question is no longer how sparse a **nested-row** code can look; that architecture is quantitatively understood.

The next question is:

> Can a fundamentally different primitive finite-signature architecture FO-recover the full order while avoiding a primitive half-graph in every basic relation and achieving a better intrinsic resolved-prefix witness cost than \(\Theta(r^2)\)?

Any such structure would still be unstable at the level of some FO formula, because a definable infinite order forces the order property. The challenge is whether the order property can be generated compositionally from primitive relations whose own ladder profiles remain shallow.

That is now the natural boundary between **primitive instability** and **derived instability** in infinite FCOA memory.