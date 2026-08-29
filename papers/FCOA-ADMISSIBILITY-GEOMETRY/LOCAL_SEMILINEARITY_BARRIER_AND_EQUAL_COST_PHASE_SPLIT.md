# Local Semilinearity Barrier and the Equal-Cost AL1/AL2 Phase Split

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-29  
**Status:** central theorem package; internal hostile audit included  
**Backend:** `FCOA_DEFINITION_1_0.md`, `FCOA_MORPHISMS_EQUIVALENCE_REPRESENTATION_1_0.md`  
**Depends on:** `INTERNAL_DIGIT_SCAFFOLD_AND_DIMENSION_COLLAPSE.md`, `BASE_SORT_LINEAR_SUPPORT_BARRIER.md`

---

## 1. Problem

The previous two results establish that, on an explicit ordered base carrier,

\[
C_{AL1}^{\rm base}(N)=\Theta(N).
\]

This immediately raises the next question:

\[
\boxed{
\text{What separates exact AL1 from AL2 when both can live at total cost }\Theta(N)?
}
\]

A scalar support count cannot be the separator.

The answer inside the fixed-width coordinate-compilation class is a **qualitative local-law boundary**:

\[
\boxed{
\text{Presburger-definable coordinate kernel}
\quad\text{vs}\quad
\text{non-Presburger multiplicative coordinate law}.
}
\]

The target carrier can remain explicit, the signature finite, the total support linear, and the same coordinate infrastructure can be used on both sides. What changes is the logical strength of one local coordinate law.

---

## 2. Two-digit coordinate scaffold

Let

\[
X_N=\{0,\ldots,N-1\},
\qquad
b=\lceil\sqrt N\rceil,
\qquad
D=\{0,\ldots,b-1\}.
\]

For every target point

\[
x=hb+\ell,
\]

use the coordinate graphs

\[
H(x,h),
\qquad
L(x,\ell).
\]

The additive scaffold contains the digit add-with-carry graph

\[
S(a,d;c,r)
\iff
a+d=cb+r,
\]

where

\[
a,d,r\in D,
\qquad
c\in\{0,1\}.
\]

As proved in `INTERNAL_DIGIT_SCAFFOLD_AND_DIMENSION_COLLAPSE.md`, this gives exact AL1 with total support

\[
3N+O(\sqrt N).
\]

---

## 3. The multiplication-split law

Add one new local relation

\[
M(a,d;q,r)
\iff
ad=qb+r,
\]

with

\[
a,d,q,r\in D.
\]

For each ordered pair `(a,d)` there is exactly one quotient-remainder pair `(q,r)`, so

\[
|M|=b^2=N+O(\sqrt N).
\]

The extended scaffold is

\[
\mathcal D_N^\times
=(X_N,<,D,H,L,S,M).
\]

Its total primitive support is still

\[
\boxed{
C_\times(N)=4N+O(\sqrt N)=\Theta(N).
}
\]

Thus AL2, if recovered, appears at the same asymptotic total support scale as AL1.

---

## 4. Exact two-digit multiplication formula

Let

\[
x=h_xb+\ell_x,
\qquad
y=h_yb+\ell_y,
\qquad
z=h_zb+\ell_z.
\]

The product expands as

\[
xy
=
\ell_x\ell_y
+b(h_x\ell_y+\ell_xh_y)
+b^2h_xh_y.
\tag{4.1}
\]

For a product below `b^2`, the `b^2` coefficient must vanish.

Choose digits

\[
q_0,r_1,r_2,t.
\]

Require:

\[
M(\ell_x,\ell_y;q_0,\ell_z),
\tag{4.2}
\]

\[
M(h_x,\ell_y;0,r_1),
\tag{4.3}
\]

\[
M(\ell_x,h_y;0,r_2),
\tag{4.4}
\]

\[
h_x=0\ \vee\ h_y=0,
\tag{4.5}
\]

\[
S(q_0,r_1;0,t),
\tag{4.6}
\]

\[
S(t,r_2;0,h_z).
\tag{4.7}
\]

All zeros are expressed by the least-element formula in the background order.

### Theorem 4.1 — Exact two-digit multiplication

The fixed FO formula consisting of coordinate recovery plus (4.2)-(4.7) satisfies

\[
\boxed{
\operatorname{Mul}_{\mathcal D^\times}(x,y,z)
\iff
xy=z<N.
}
\]

### Proof

Equation (4.2) writes

\[
\ell_x\ell_y=q_0b+\ell_z.
\]

Equations (4.3) and (4.4) assert that both cross products are strictly below `b`, namely

\[
h_x\ell_y=r_1,
\qquad
\ell_xh_y=r_2.
\]

If either cross product had quotient at least one, its contribution after multiplication by `b` would already include a `b^2` term and the full product could not be below `b^2`.

Condition (4.5) is equivalent to

\[
h_xh_y=0,
\]

which removes the direct `b^2h_xh_y` term.

Finally (4.6)-(4.7), both with zero carry, state

\[
q_0+r_1+r_2=h_z<b.
\]

Substituting into (4.1) gives

\[
xy=h_zb+\ell_z=z.
\]

Conversely, if `xy=z<N<=b^2`, then no `b^2` contribution is possible. Hence `h_xh_y=0`, both cross-product quotients vanish, and the middle coefficient is below `b`. The unique quotient/remainder and carry witnesses satisfy (4.2)-(4.7).

If `xy` lies in `[N,b^2)`, the resulting digit pair has no target representative `z in X_N`, so the formula correctly rejects it.

`□`

Therefore

\[
\boxed{
\operatorname{FTR}(\mathcal D^\times)=2.
}
\]

---

## 5. The phase jump is not a support jump

The additive scaffold has

\[
C_+(N)=3N+O(\sqrt N),
\]

while the multiplicative extension has

\[
C_\times(N)=4N+O(\sqrt N).
\]

Hence

\[
\boxed{
C_+(N)=\Theta(N)=C_\times(N),
}
\]

but

\[
\boxed{
\operatorname{FTR}(\mathcal D)=1,
\qquad
\operatorname{FTR}(\mathcal D^\times)=2.
}
\]

Thus total support density cannot distinguish AL1 from AL2.

---

## 6. Local coordinate kernels

On the square subsequence

\[
N=b^2,
\]

the target carrier is exactly the Cartesian square

\[
X_{b^2}\cong D_b^2.
\]

Define the additive local kernel

\[
\mathcal K_b^+
=(D_b,<,S_b)
\]

and the multiplicative local kernel

\[
\mathcal K_b^\times
=(D_b,<,S_b,M_b).
\]

The entire target scaffold is uniformly dimension-2 FO-interpretable in its local kernel by representing

\[
x=hb+\ell
\]

as `(h,ell)`.

Conversely, the digit subset and its local laws are definable inside the target scaffold.

The key point is therefore not the physical target dimension but the logical class of the coordinate kernel.

---

## 7. Presburger-kernel barrier

Let

\[
\mathsf P_b=([b],<,+_{tr})
\]

be finite Presburger arithmetic.

### Definition 7.1 — Presburger-coordinate compilation

A fixed-width coordinate presentation on

\[
X_{b^k}\cong[b]^k
\]

is called **Presburger-coordinate** if, after replacing each target point by its `k` coordinates, every primitive relation of the presentation is uniformly FO-definable in

\[
\mathsf P_b.
\]

The coordinate width `k` is fixed independently of `b`.

### Theorem 7.2 — Local Semilinearity Barrier

No Presburger-coordinate compilation uniformly FO-defines canonical target multiplication on

\[
X_{b^k}.
\]

### Proof

Suppose a fixed target formula defines truncated multiplication on `X_{b^k}`.

By definition of Presburger-coordinate compilation, substitute the fixed coordinate interpretation of every primitive target relation. This yields one fixed FO formula over

\[
([b],<,+_{tr}).
\]

Now restrict each target argument to the definable coordinate axis

\[
A_b=\{(0,\ldots,0,a):a<b\}.
\]

On this axis, canonical target multiplication is exactly ordinary truncated digit multiplication:

\[
(0,\ldots,0,a)
\cdot
(0,\ldots,0,d)
=
(0,\ldots,0,r)
\iff
ad=r<b.
\]

Hence finite `TIMES` would be uniformly FO-definable in

\[
FO(<,PLUS),
\]

contradicting Troy Lee's finite-structure separation

\[
\boxed{
TIMES\notin FO(<,PLUS).
}
\]

Therefore target multiplication is impossible in every fixed-width Presburger-coordinate compilation. `□`

### Reference

Troy Lee, “Arithmetical Definability over Finite Structures,” *Mathematical Logic Quarterly* 49(4), 2003, 385-392, DOI `10.1002/malq.200310041`.

The result used here is the strict expressive separation of finite addition from finite multiplication in first-order logic with order.

---

## 8. The multiplication-split law is genuinely non-Presburger

### Corollary 8.1

The local relation

\[
M_b(a,d;q,r)
\iff
ad=qb+r
\]

is not uniformly FO-definable in

\[
([b],<,+_{tr}).
\]

### Proof

If `M_b` were Presburger-definable, then truncated multiplication would be definable by

\[
TIMES(a,d,r)
\iff
M_b(a,d;0,r).
\]

This contradicts Theorem 7.2 / Lee's separation. `□`

Therefore the AL1-to-AL2 transition in this scaffold is a genuine nondefinitional extension.

---

## 9. Exact separator inside the fixed-width coordinate class

Theorems 7.2 and 4.1 combine into the following statement.

### Theorem 9.1 — Equal-Cost Phase Split

Inside the fixed-width coordinate-compilation class:

1. if all local coordinate laws remain uniformly Presburger-definable, target multiplication is impossible;
2. one explicit non-Presburger local multiplication-split law suffices to recover target multiplication;
3. both the exact AL1 and AL2 presentations can have total support
   \[
   \Theta(N).
   \]

Hence the first robust separator in this class is not total tuple density but

\[
\boxed{
\text{local semilinearity / Presburger closure}
}
\]

versus

\[
\boxed{
\text{a genuinely non-Presburger local law}.
}
\]

This is a representation-class theorem, not a universal invariant of every conceivable FCOA presentation.

---

## 10. Fixed-width generalization

Let

\[
N=b^k
\]

for fixed

\[
k\ge2.
\]

Represent every target point by `k` base-`b` digits using `k` charged coordinate maps.

### Additive phase

With only the digit add-with-carry law `S`, fixed-length addition is obtained by unrolling the `k` carry steps in one fixed FO formula.

The total support is

\[
C_{+,k}(N)
=
kN+b^2+O(b)
=
\Theta(N).
\]

The Presburger-kernel barrier prevents multiplication, so the family is exact AL1.

### Multiplicative phase

Add the same multiplication-split table `M` on the digit carrier.

Each of the `k^2` elementary digit products is represented by one quotient/remainder pair. Since `k` is fixed, ordinary grade-school multiplication can be unrolled into a fixed finite FO formula:

1. use `M` for the finitely many elementary products;
2. regard each elementary product as a two-digit shifted partial word;
3. add the finitely many partial words sequentially with the fixed digit add-with-carry relation `S`;
4. require zero final overflow beyond the first `k` digits;
5. identify the resulting `k` output digits with the target point.

All intermediate words use only a number of digit variables depending on fixed `k`, not on `b`.

Thus canonical target multiplication is uniformly FO-definable.

The total support remains

\[
C_{\times,k}(N)
=
kN+2b^2+O(b)
=
\Theta(N).
\]

---

## 11. Marginal phase-upgrade cost

The coordinate infrastructure and additive law are already present in the AL1 scaffold. The only new primitive table needed for the AL2 extension is `M`.

Therefore the marginal primitive support is

\[
\Delta C_k(N)
=|M|
=b^2
=N^{2/k}.
\]

### Theorem 11.1 — Sublinear AL1-to-AL2 upgrade

For every fixed

\[
k>2,
\]

there exists an exact AL1 family of total cost `Theta(N)` with an AL2 extension whose additional primitive support is

\[
\boxed{
\Delta C_k(N)=\Theta(N^{2/k})=o(N).
}
\]

Yet both the before and after structures have total cost

\[
\Theta(N).
\]

### Corollary 11.2 — No universal polynomial marginal lower bound

For every

\[
\varepsilon>0,
\]

choose a fixed integer

\[
k>2/\varepsilon.
\]

Then

\[
\Delta C_k(N)
=O(N^\varepsilon).
\]

Hence across the union of fixed-width coordinate classes there is no universal exponent

\[
\delta>0
\]

such that every AL1-to-AL2 phase upgrade must cost

\[
\Omega(N^\delta)
\]

new primitive tuples.

This does not contradict the base-sort linear lower bound: that theorem concerns total memory required to build AL1 from the bare ordered carrier, not the marginal cost of upgrading an already factorized AL1 representation.

---

## 12. What resource changed?

The phase transition can now be factored as

\[
\boxed{
\begin{array}{c}
\text{same explicit target carrier},\\
\text{same coordinate maps},\\
\text{same fixed width},\\
\text{same }\Theta(N)\text{ total support scale},\\
\text{same FO query language},\\
\text{same additive carry law},
\end{array}
}
\]

with only one qualitative change:

\[
\boxed{
\text{Presburger local kernel}
\longrightarrow
\text{kernel containing a non-Presburger multiplicative split law}.
}
\]

Therefore the correct phase parameter is not merely how much memory is stored, but **what definability class the local law belongs to**.

---

## 13. Working invariant: Local-Law Class

For comparison purposes define the working presentation descriptor

\[
\operatorname{LLC}(\mathcal F)
\]

as the weakest declared logical/algebraic class in which all local coordinate laws of the chosen factorization are uniformly definable.

Examples:

\[
\operatorname{LLC}=\text{finite-state/regular},
\]

\[
\operatorname{LLC}=\text{Presburger},
\]

\[
\operatorname{LLC}=\text{multiplicative arithmetic}.
\]

For the present pair:

\[
\operatorname{LLC}(\mathcal D)=\text{Presburger},
\]

while

\[
\operatorname{LLC}(\mathcal D^\times)
\not\subseteq
\text{Presburger}.
\]

`LLC` is a working presentation descriptor, not yet a representation-invariant FCOA quantity.

---

## 14. Bounded-fiber recoding firewall

The semantic phase itself remains invariant under the backend's mutual-FO-interpretability notion.

Thus if two presentations are mutually uniformly FO-interpretable with the declared bounded-fiber/fixed-dimension controls, they cannot turn exact AL1 into AL2 or vice versa.

What may change under recoding is the chosen coordinate kernel and therefore the raw `LLC` descriptor.

Consequently:

\[
\boxed{
\text{FTR is semantic; LLC is explanatory/presentation-level.}
}
\]

This distinction must be preserved in any later minimality theorem.

---

## 15. Hostile audit

### 15.1 Does the two-digit multiplication formula miss an overflow channel?

No. There are exactly three possible sources of a `b^2` term:

1. `h_xh_y b^2`;
2. the quotient of `h_x ell_y` multiplied by `b`;
3. the quotient of `ell_x h_y` multiplied by `b`;
4. overflow from the middle-digit sum.

Conditions (4.3)-(4.7) force all four to vanish. The low product quotient `q_0` is correctly retained in the middle digit.

**PASS.**

### 15.2 Does non-square `N` cause false multiplication witnesses?

No. The coordinate map embeds `X_N` into the first `N` pairs of the `b x b` grid. A computed product in `[N,b^2)` has no target `z`, so the formula rejects it.

**PASS.**

### 15.3 Could `M` secretly be Presburger-definable because it returns quotient and remainder rather than the product itself?

No. The zero-quotient slice

\[
M(a,d;0,r)
\]

is exactly truncated digit multiplication `ad=r<b`. Therefore Presburger definability of `M` would imply Presburger definability of TIMES.

**PASS.**

### 15.4 Is the Local Semilinearity Barrier merely a restatement of Lee's theorem?

Its external logical anchor is Lee's separation, but the FCOA result is the transport theorem across fixed-width coordinate compilations: any target multiplication formula would pull back through the coordinate interpretation and contradict the local finite-arithmetic separation. The new content is the representation-level placement of the separator and its cost consequences.

**PASS.**

### 15.5 Does the fixed-`k` multiplication argument require unbounded iteration?

No. There are only `k^2` elementary digit products and a fixed finite number of additions of fixed-length words. Since `k` is fixed before the family varies, the entire grade-school circuit is unrolled into one finite FO formula.

**PASS.**

### 15.6 Do carries in the fixed-`k` multiplication require a growing-value sort?

No. The sequential-partial-word formulation avoids a single large column accumulator. Each step adds two `k`-digit words using the same binary digit carry law `S`; the intermediate result is another `k`-digit word, and overflow is a single carry bit that is required to vanish whenever the target product remains below `b^k`. A fixed sequence of such additions suffices because the number of partial words is fixed by `k`.

**PASS.**

### 15.7 Does the marginal `N^(2/k)` result violate the `Omega(N)` AL1 lower bound?

No. The `Omega(N)` theorem charges the total distributed memory needed to reach AL1 from the ordered base. The marginal theorem starts from an already-paid `Theta(N)` coordinate/additive scaffold and asks only for the extra memory needed to cross from AL1 to AL2.

**PASS.**

No fatal defect was found.

---

## 16. Scientific consequence

The equal-cost phase problem is now answered inside the fixed-width factorized model:

\[
\boxed{
\text{AL1 vs AL2 is not a density phase transition.}
}
\]

Instead:

\[
\boxed{
\text{AL1: Presburger local coordinate law}
}
\]

and

\[
\boxed{
\text{AL2: a genuinely non-Presburger local law becomes available.}
}
\]

The result also shows that the **marginal** price of crossing this semantic boundary can be arbitrarily small as a polynomial power of the total carrier size while the total representation remains linear.

---

## 17. Next frontier

The next question is no longer whether AL1 and AL2 can have the same asymptotic cost: they can.

The new hard frontier is:

\[
\boxed{
\text{Can the non-Presburger local-law jump itself be generated from a weaker provenance class}
}
\]

without directly installing a multiplication-split table?

More concretely:

1. can a fixed finite-state/local generator produce a non-Presburger kernel after bounded nesting;
2. can repeated FCOA composition generate the multiplicative split law without importing it as primitive data;
3. is there a representation-invariant version of local-law strength under bounded-fiber recodings;
4. can the marginal AL1-to-AL2 upgrade be made polylogarithmic or `O(1)` with one fixed finite signature and no arbitrary size oracle;
5. does every such stronger compression necessarily pay through growing coordinate depth, closure depth, or another explicitly chargeable channel?

This is now the genuine phase-boundary problem.

---

## 18. Status

\[
\boxed{\mathbf F:\ \Theta(N)\text{-cost exact AL2 scaffold exists.}}
\]

\[
\boxed{\mathbf F:\ \text{fixed-width Presburger-coordinate compilations cannot reach AL2.}}
\]

\[
\boxed{\mathbf F:\ M\text{ is a genuine non-Presburger local law and suffices for AL2.}}
\]

\[
\boxed{\mathbf F:\ \text{AL1 and AL2 can have the same total }\Theta(N)\text{ support scale.}}
\]

\[
\boxed{\mathbf F:\ \Delta C_k(N)=\Theta(N^{2/k})\text{ for the fixed-width AL1-to-AL2 upgrade.}}
\]

\[
\boxed{\mathbf W:\ \operatorname{LLC}\text{ as explanatory presentation terminology.}}
\]

\[
\boxed{\mathbf O:\ \text{representation-invariant local-law strength and generated non-Presburger escape.}}
\]

No numbered G5 family is opened by this note.