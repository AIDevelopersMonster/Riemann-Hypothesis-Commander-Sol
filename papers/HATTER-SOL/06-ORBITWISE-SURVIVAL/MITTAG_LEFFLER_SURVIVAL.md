# HATTER-SOL-06 · Mittag-Leffler Survival and Infinite Attrition

## 0. Purpose

The preceding strikes identified two mechanisms behind global survival:

1. finite-fiber compactness (FFC), hence a finitely branching extension tree;
2. eventual bi-finite image control (EBFI), hence precompactness in the permutation topology.

There is a third mechanism, independent of both: **eventual stabilization of the restriction images** in the inverse system of finite-height extension sets.

This is the classical Mittag-Leffler principle for inverse systems of sets. In the present problem it gives a sharp statement:

\[
\boxed{
\text{arbitrarily deep finite survival}
+
\text{Mittag-Leffler stabilization}
\Longrightarrow
\text{global survival}.}
\]

Consequently, genuine noncompact death must exhibit not only coordinate escape, but also **infinite attrition at a fixed finite Pratt height**: deeper and deeper arithmetic constraints must keep killing previously viable partial automorphisms forever.

---

# 1. Cone-localized extension system

Fix a seed

\[
\tau\in G_m
\]

and its generated causal cone

\[
C=C^+(\operatorname{supp}\tau).
\]

For \(n\ge m\), let

\[
T_n=T_n^C(\tau)
\]

be the set of cone-localized extensions of \(\tau\) to \(P_{\le n}\):

\[
T_n
=
\left\{
 g\in G_n:
 g|_{P_{\le m}}=\tau,
\quad
 g(p)=p\text{ for }p\in P_{\le n}\setminus C
\right\}.
\]

For

\[
m\le n\le N,
\]
write

\[
r_n^N:T_N\to T_n
\]

for restriction.

The global cone-localized extensions are precisely the inverse limit

\[
\varprojlim T_n.
\]

We assume throughout this note that

\[
T_n\ne\varnothing
\qquad\text{for every }n\ge m,
\]

so the seed survives to every prescribed finite Pratt height.

---

# 2. Survivor images at a fixed height

For fixed \(n\) and \(N\ge n\), define

\[
A_{N,n}
=
\operatorname{im}(r_n^N)
\subseteq T_n.
\]

Thus \(A_{N,n}\) consists of the height-\(n\) partial automorphisms that survive at least to height \(N\).

As \(N\) increases, these form a descending chain:

\[
T_n=A_{n,n}
\supseteq
A_{n+1,n}
\supseteq
A_{n+2,n}
\supseteq\cdots.
\]

Define the arbitrarily-deep survivor set

\[
A_{\infty,n}
=
\bigcap_{N\ge n}A_{N,n}.
\]

A node \(g\in T_n\) belongs to \(A_{\infty,n}\) exactly when it has descendants at arbitrarily large finite heights.

This does **not** by itself mean that \(g\) lies on an infinite compatible branch.

---

# 3. Mittag-Leffler stabilization

## Definition 3.1

The inverse system \((T_n,r_n^{n+1})\) satisfies the **Mittag-Leffler condition at height \(n\)** if there exists

\[
N(n)\ge n
\]

such that

\[
A_{N,n}=A_{N(n),n}
\qquad
\text{for every }N\ge N(n).
\]

Equivalently, the descending survivor-image chain at height \(n\) eventually stabilizes.

The system satisfies **ML** if this holds for every finite height \(n\ge m\).

When ML holds, write the stable image as

\[
S_n=A_{N(n),n}=A_{\infty,n}.
\]

---

# 4. Mittag-Leffler survival theorem

## Theorem 4.1

Assume

\[
T_n\ne\varnothing
\qquad(n\ge m)
\]

and that the inverse system satisfies ML. Then

\[
\boxed{
\varprojlim T_n\ne\varnothing.
}
\]

Hence the seed \(\tau\) has a global cone-localized automorphism extension.

### Proof

First, every stable image \(S_n\) is nonempty. Indeed, choose \(N\ge N(n)\). Since \(T_N\ne\varnothing\), its restriction image

\[
A_{N,n}=S_n
\]

is nonempty.

We claim that the restriction map

\[
r_n^{n+1}:S_{n+1}\to S_n
\]

is surjective.

Take

\[
g_n\in S_n.
\]

Choose a height \(M\) so large that

\[
M\ge N(n),
\qquad
M\ge N(n+1).
\]

Because

\[
g_n\in S_n=A_{M,n},
\]

there exists

\[
g_M\in T_M
\]

with

\[
r_n^M(g_M)=g_n.
\]

Let

\[
g_{n+1}=r_{n+1}^M(g_M).
\]

Then

\[
g_{n+1}\in A_{M,n+1}=S_{n+1}
\]

and

\[
r_n^{n+1}(g_{n+1})=g_n.
\]

So the stable restriction maps are surjective.

Now choose any

\[
g_m\in S_m.
\]

Recursively choose

\[
g_{n+1}\in S_{n+1}
\]

lifting \(g_n\). This produces a compatible sequence

\[
(g_m,g_{m+1},g_{m+2},\ldots)
\in
\varprojlim T_n.
\]

Its union over Pratt height is a global cone-localized automorphism. \(\square\)

---

# 5. Infinite attrition is necessary for noncompact death

The contrapositive is immediate but important.

## Corollary 5.1 — fixed-height attrition theorem

Assume

\[
T_n\ne\varnothing
\qquad\forall n\ge m
\]

but

\[
\varprojlim T_n=\varnothing.
\]

Then ML fails at some finite height \(n\).

Equivalently, for some fixed \(n\), the chain

\[
A_{n,n}
\supseteq
A_{n+1,n}
\supseteq
A_{n+2,n}
\supseteq\cdots
\]

never stabilizes.

Hence there exist arbitrarily large heights

\[
N_1<N_2<N_3<\cdots
\]

with strict losses

\[
\boxed{
A_{N_{j+1},n}
\subsetneq
A_{N_j,n}.
}
\]

Thus global death after unbounded finite survival cannot be caused by a single late obstruction. At some already fixed finite Pratt height, deeper arithmetic must keep deleting viable partial automorphisms indefinitely.

We call this phenomenon **infinite attrition**.

---

# 6. Death-height spectrum at the attrition level

Fix a height \(n\) at which ML fails.

For

\[
g\in T_n,
\]
define its death height

\[
\delta(g)
=
\sup\{N\ge n:g\in A_{N,n}\}
\in
\{n,n+1,\ldots,\infty\}.
\]

Thus

- \(\delta(g)=N<\infty\) means \(g\) extends through height \(N\) but not arbitrarily farther;
- \(\delta(g)=\infty\) means \(g\in A_{\infty,n}\), so \(g\) survives to arbitrarily large finite heights.

If the chain \(A_{N,n}\) does not stabilize, then the finite values of \(\delta(g)\) are unbounded.

## Proposition 6.1

At every ML-failure height \(n\), there exists a sequence

\[
g_1,g_2,g_3,\dots\in T_n
\]

with finite death heights satisfying

\[
\delta(g_j)\to\infty.
\]

### Proof

Choose strict losses at heights

\[
N_1<N_2<\cdots.
\]

For each \(j\), take

\[
g_j\in A_{N_j,n}\setminus A_{N_{j+1},n}.
\]

Then

\[
N_j\le\delta(g_j)<N_{j+1},
\]

so \(\delta(g_j)\to\infty\). \(\square\)

This is the exact analogue, inside the actual extension system, of the countdown phenomenon from the explicit rank-\(\omega\) model.

---

# 7. Deep nodes and the bottleneck-node theorem

Call

\[
g\in T_n
\]

**deep** if

\[
g\in A_{\infty,n},
\]

i.e. if it has descendants at arbitrarily large finite heights.

The root seed is deep because all \(T_N\) are assumed nonempty.

## Theorem 7.1 — bottleneck node

If the seed survives to every finite height but has no global extension, then there exists a deep node

\[
g\in T_n
\]

such that **no child of \(g\)** in \(T_{n+1}\) is deep.

Consequently:

1. \(g\) has infinitely many children;
2. every child has finite death height;
3. the child death heights are unbounded.

### Proof

Suppose, to the contrary, that every deep node had at least one deep child. Starting from the deep seed, dependent choice would produce an infinite chain of deep nodes

\[
g_m\prec g_{m+1}\prec g_{m+2}\prec\cdots,
\]

which is a global branch, contradiction.

Therefore some deep node \(g\) has no deep child.

Because \(g\) is deep, for every \(N>n\) it has a descendant at height \(N\). The first step of such a descendant is a child of \(g\) whose death height is at least \(N\). Hence child death heights are unbounded.

If \(g\) had only finitely many children, the maximum of their finite death heights would be finite, contradicting that \(g\) is deep. Thus it has infinitely many children. \(\square\)

This localizes every noncompact-death scenario to a single finite-height node with an infinite cloud of one-step choices, each eventually killed, but with no uniform killing horizon.

---

# 8. One-step arithmetic meaning

Fix a bottleneck node

\[
g\in T_n.
\]

By the Multiplicity Tower Theorem, every child

\[
\widetilde g\in T_{n+1}
\]

is obtained by choosing, for every exact support \(S\) at level \(n\), a bijection

\[
\beta_S:X_S\to X_{gS}
\]

whenever the required multiplicities agree.

Thus the infinite child cloud of Theorem 7.1 does not come from changing the lower action: all children agree exactly on

\[
P_{\le n}.
\]

The noncompact choice occurs entirely in the new fiber bijections at layer

\[
L_{n+1}.
\]

Therefore genuine noncompact death has the following normal form:

\[
\boxed{
\begin{array}{c}
\text{a fixed lower automorphism }g,\\[2mm]
\text{infinitely many admissible next-layer fiber-bijection choices},\\[2mm]
\text{each killed by a finite future obstruction},\\[2mm]
\text{with killing heights unbounded.}
\end{array}
}
\]

This is considerably sharper than merely saying that some coordinate image escapes somewhere in the tower.

---

# 9. Correct branching-source dichotomy

An infinite number of children does **not** by itself force an infinite exact fiber.

The reason is that the next layer may contain infinitely many independent nontrivial finite fibers. Even if each individual fiber admits only finitely many permutations or bijections, choosing independently in infinitely many such coordinates can already produce infinitely many, and potentially continuum many, children.

Therefore the correct statement is the following.

## Proposition 9.1 — branching-source dichotomy

Fix a node

\[
g\in T_n.
\]

If every active next-layer exact fiber is finite and only finitely many active supports \(S\) satisfy

\[
\mu_n(S)\ge2,
\]

then \(g\) has only finitely many children in \(T_{n+1}\).

Consequently, if a bottleneck node has infinitely many children, then at least one of the following must occur:

1. some active exact fiber is infinite;
2. infinitely many active supports have multiplicity at least two.

### Proof

A child of \(g\) is obtained by choosing bijections

\[
\beta_S:X_S\to X_{gS}
\]

across the active support orbits. A fiber of cardinality \(0\) or \(1\) contributes no nontrivial choice. A finite fiber of cardinality \(k\ge2\) contributes only finitely many choices. If there are only finitely many such nontrivial finite coordinates and no infinite fiber, the product of all available choices is finite. \(\square\)

This is the exact correction to the tempting but false claim that infinite branching alone implies an infinite exact fiber.

Under full FFC, every Pratt truncation is finite; in particular there are only finitely many relevant supports at each step and all fibers are finite. Hence Proposition 9.1 recovers finite branching, and König compactness applies.

Outside FFC, noncompact branching can therefore enter in two distinct ways:

\[
\boxed{
\text{concentrated branching through an infinite fiber}
}
\]

or

\[
\boxed{
\text{diffuse branching through infinitely many nontrivial finite fibers}.}
\]

Both must remain in scope for HATTER-SOL-06.

---

# 10. Relation to EBFI

ML and EBFI are different sufficient mechanisms.

### ML

ML controls the **sets of partial automorphisms** that survive to deeper horizons:

\[
A_{N,n}\subseteq T_n.
\]

It allows these sets to be infinite, as long as their images eventually stabilize at each fixed height.

### EBFI

EBFI controls the **coordinate orbits of individual primes** under sufficiently deep partial automorphisms:

\[
I_H^\pm(p).
\]

It allows the survivor sets \(A_{N,n}\) to shrink forever, provided the whole family remains precompact in the permutation topology.

Thus neither condition is merely a restatement of the other.

But if unbounded finite survival ends in global death, then **both mechanisms must fail**:

\[
\boxed{
\text{noncompact death}
\Longrightarrow
\begin{cases}
\text{ML failure at some fixed finite height},\\
\text{EBFI failure for some prime coordinate}.
\end{cases}
}
\]

So a genuine counterexample must simultaneously exhibit:

1. **infinite attrition** of finite-height partial automorphisms; and
2. **eternal coordinate escape** in the permutation topology.

This dual signature is substantially more rigid than either symptom alone.

---

# 11. Application to the seed \((3\ 5)\)

Let

\[
\tau=(3\ 5).
\]

Suppose, hypothetically, that

\[
T_n^C(\tau)\ne\varnothing
\qquad\forall n,
\]

but no global automorphism extends \(\tau\).

Then there must exist a finite height \(n\) at which the survivor image sets

\[
A_{N,n}
=
\operatorname{im}
\left(
T_N^C(\tau)\to T_n^C(\tau)
\right)
\]

shrink strictly infinitely often.

Moreover there is a bottleneck partial automorphism

\[
g\in T_n^C(\tau)
\]

that itself survives to arbitrary finite depth, while every concrete choice of its next-layer fiber bijections eventually dies.

Hence the prime-specific problem can be sharpened again:

\[
\boxed{
\text{can deeper exact-support arithmetic keep deleting all next-layer choices forever,}
}
\]

with no finite uniform horizon at which the bottleneck is resolved?

If the answer is no, then noncompact death is impossible.

---

# 12. A new sufficient target: eventual survivor stabilization

To prove global survival of \((3\ 5)\) after establishing unbounded finite survival, it would therefore be enough to prove a statement weaker than EBFI:

> For every fixed finite Pratt height \(n\), there is a height \(N(n)\) such that a height-\(n\) cone-localized partial automorphism extends to all arbitrarily larger finite heights iff it already extends to height \(N(n)\).

In symbols:

\[
\boxed{
A_{N,n}=A_{N(n),n}
\qquad(N\ge N(n)).
}
\]

This is an **eventual finite-horizon decision principle** for survival at each fixed level.

It does not require exact fibers to be finite.

It does not require possible images of individual primes to become finite.

It requires only that deeper arithmetic eventually stop discovering new reasons to kill old finite-height partial automorphisms.

---

# 13. Research consequence

The search for compactness has now split into two genuinely different prime-specific targets:

### Target A — coordinate compactness

Prove EBFI, or at least eventual finiteness of the first escape channel

\[
J_H(7)=I_H^+(7)\cap X_{\{2,5\}}.
\]

### Target B — survivor stabilization

Prove ML at the first few fixed heights, beginning with the image of the seed extension set in

\[
T_2^C((3\ 5)).
\]

A proof of either mechanism at all heights rules out noncompact death.

A genuine noncompact counterexample must defeat both simultaneously.

---

# 14. Status

This strike establishes:

1. the exact Mittag-Leffler formulation of finite-height survival;
2. a rigorous ML survival theorem for the cone-localized extension system;
3. the fixed-height infinite-attrition obstruction forced by noncompact death;
4. a death-height spectrum with arbitrarily late finite deaths;
5. the bottleneck-node theorem;
6. localization of noncompact choice to next-layer fiber bijections over one fixed lower automorphism;
7. the corrected branching-source dichotomy: concentrated infinite-fiber branching or diffuse branching across infinitely many nontrivial finite fibers;
8. the dual necessary signature: ML failure plus EBFI failure.

No publication claim is made yet, but the structural package of HATTER-SOL-06 is now substantially stronger.

The next arithmetic strike should test **survivor stabilization at height 2** for the seed \((3\ 5)\), because this may be weaker than trying to bound the entire image set of \(7\).
