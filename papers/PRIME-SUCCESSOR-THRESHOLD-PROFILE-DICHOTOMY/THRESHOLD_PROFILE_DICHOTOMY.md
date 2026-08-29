# Theorem Checkpoint — Threshold-Profile Valuation Dichotomy

**Project:** Prime-Successor Algebra / Two Walls  
**Working title:** *Reflections on the Threshold-Profile Valuation Dichotomy with Commander Sol*  
**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Status:** new theorem checkpoint; first hostile audit passed  
**Date:** 2026-08-27

## 1. Family of structures

Let

\[
\kappa:\mathbb P\to\mathbb N_0
\]

be an arbitrary threshold profile on the rational primes. Define

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge \kappa(r),
\]

and

\[
\mathcal V_{\Delta,\kappa}
=
\Bigl(
(\mathbb N_{>0},\times,1),
(\mathbb Q,+,0),
U_\Delta,
B_\kappa
\Bigr),
\]

where

\[
U_\Delta(p,x)
\iff
\operatorname{Prime}(p)\land x=u_p,
\qquad
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Put

\[
P_+(\kappa)=\{r\in\mathbb P:\kappa(r)\ge1\}.
\]

The question is whether the logical phase is controlled by the numerical values of \(\kappa(r)\), or by the support of positive depth.

## 2. Main dichotomy

### Threshold-Profile Valuation Dichotomy Theorem

For every threshold profile \(\kappa:\mathbb P\to\mathbb N_0\):

### (A) Finite positive support

If

\[
|P_+(\kappa)|<\infty,
\]

then \(\mathcal V_{\Delta,\kappa}\) and the uniform zero-depth structure

\[
\mathcal V_{\Delta,0}
\]

are parameter-free interdefinable.

Consequently,

\[
<_{\mathbb P},\operatorname{Succ}_{\mathbb P}
\notin\operatorname{Def}(\mathcal V_{\Delta,\kappa}),
\]

and every fixed ternary isolator \(I\) satisfies

\[
\operatorname{GIR}(I)<\infty.
\]

### (B) Infinite positive support

If

\[
|P_+(\kappa)|=\infty,
\]

then there is one fixed ternary formula \(I_\kappa(p,q;r)\) such that

\[
\operatorname{GIR}(I_\kappa)=\infty.
\]

Moreover the source relation induced by \(I_\kappa\) uniformly codes every finite bipartite graph, and

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
\]

is undecidable.

Thus, inside this threshold-profile family,

\[
\boxed{
|P_+(\kappa)|<\infty
\iff
\forall I\;\operatorname{GIR}(I)<\infty.
}
\]

The transition is controlled by **finite versus infinite positive-depth support**, not by the magnitude, density, boundedness, or constancy of the positive thresholds.

## 3. Fixed source primes are definable from every threshold predicate

For a fixed ordinary prime \(\ell\), let \(\ell x\) denote the fixed additive scalar term in the target sort. Define

\[
\Theta_\ell(r)
:
\operatorname{Prime}(r)
\land
\exists x\,
\bigl(
\neg B_\kappa(r,x)
\land
B_\kappa(r,\ell x)
\bigr).
\]

Then

\[
\Theta_\ell(r)\iff r=\ell.
\]

Indeed, if \(r\ne\ell\), multiplication by \(\ell\) is an \(r\)-adic unit and cannot move a value across the threshold \(\kappa(r)\). If \(r=\ell\), choose \(x\) with

\[
v_\ell(x)=\kappa(\ell)-1.
\]

This works also when \(\kappa(\ell)=0\), using \(v_\ell(x)=-1\).

Hence every fixed standard prime can be named parameter-free in every \(\mathcal V_{\Delta,\kappa}\) by a formula using only a fixed target scalar.

## 4. Finite-support interdefinability

Assume

\[
P_+(\kappa)=\{\ell_1,\dots,\ell_t\}.
\]

Outside these finitely many primes,

\[
B_\kappa(r,x)=B_0(r,x).
\]

At a fixed exceptional prime \(\ell\) with \(k=\kappa(\ell)\ge1\),

\[
B_\kappa(\ell,x)
\iff
\exists y\,
\bigl(x=\ell^k y\land B_0(\ell,y)\bigr).
\]

Conversely,

\[
B_0(\ell,x)
\iff
B_\kappa(\ell,\ell^k x).
\]

Since each equality \(r=\ell_i\) is parameter-free definable by \(\Theta_{\ell_i}\), the finite case distinction gives parameter-free definitions of \(B_\kappa\) from \(B_0\) and of \(B_0\) from \(B_\kappa\).

Therefore

\[
\mathcal V_{\Delta,\kappa}
\quad\text{and}\quad
\mathcal V_{\Delta,0}
\]

are parameter-free interdefinable whenever \(P_+(\kappa)\) is finite.

The Uniform Zero-Depth Compression Theorem (Zenodo DOI 10.5281/zenodo.22131827) then transfers immediately: ordinary prime order and prime successor are not definable, and every fixed GIR is finite.

## 5. Positive-depth incidence on an infinite marker set

Now assume \(P_+(\kappa)\) is infinite.

For distinct primes \(p,r\) with \(r\in P_+(\kappa)\), define

\[
E_\kappa(p;r)
:
 p\ne r
\land
\exists x\,
\bigl(U_\Delta(p,x)\land B_\kappa(r,x)\bigr).
\]

Because \(r\ne p\), the denominator \(p^{11}\) is an \(r\)-adic unit, hence

\[
v_r(u_p)
=
v_r\bigl(\tau(p)^2-p^{11}\bigr).
\]

Therefore

\[
\boxed{
E_\kappa(p;r)
\iff
r^{\kappa(r)}\mid \tau(p)^2-p^{11}.
}
\]

The zero-depth case is qualitatively different: when \(\kappa(r)=0\), the same condition is automatic for \(r\ne p\). Positive depth opens a genuine residual congruence condition.

## 6. Arbitrary finite-level residual independence

Let

\[
\rho_{\Delta,r}:G_{\mathbb Q}\to\operatorname{GL}_2(\mathbb Z_r)
\]

be the Deligne representation in the normalization

\[
\operatorname{tr}\rho_{\Delta,r}(\operatorname{Frob}_p)=\tau(p),
\qquad
\det\rho_{\Delta,r}(\operatorname{Frob}_p)=p^{11}
\]

for \(p\ne r\).

Let

\[
H=G_{\mathbb Q(\mu_\infty)}.
\]

On \(H\), the cyclotomic determinant is trivial, so the adelic image lies in the product of \(\operatorname{SL}_2(\mathbb Z_r)\).

The adelic open-image theorem for non-CM modular forms, specialized to \(\Delta\), gives a finite exceptional set \(S_\Delta\) such that the image of \(H\) contains the full local factor at every prime outside \(S_\Delta\). Equivalently:

### Arbitrary-Depth Finite Residual Independence Lemma

For every finite

\[
R\subset\mathbb P\setminus S_\Delta
\]

and every choice of positive integers \(k_r\ge1\), the reduction map

\[
H\longrightarrow
\prod_{r\in R}
\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z)
\]

is surjective.

This is the exact strengthening of the mod-\(r\) independence used in the depth-one paper. It follows because an open subgroup of the profinite product contains all full local factors outside a finite set, and reduction of each full \(\operatorname{SL}_2(\mathbb Z_r)\) factor modulo \(r^{k_r}\) is surjective.

Reference: David Loeffler, *Images of adelic Galois representations for modular forms*, Glasgow Math. J. 59 (2017), 11–25, DOI 10.1017/S0017089516000367, arXiv:1411.1789.

## 7. One integral cubic witness works at every depth

Use the two integral matrices

\[
A=
\begin{pmatrix}
0&-1\\
1&1
\end{pmatrix},
\qquad
I=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

They satisfy exactly over \(\mathbb Z\):

\[
\det A=1,
\qquad
\operatorname{tr}(A)=1,
\qquad
A^3=-I,
\]

so

\[
\operatorname{tr}(A)^2-\det(A)=0.
\]

For the identity matrix,

\[
\operatorname{tr}(I)^2-\det(I)=4-1=3.
\]

Hence for every prime \(r>3\) and every depth \(k\ge1\),

\[
\operatorname{tr}(A)^2\equiv\det(A)\pmod{r^k},
\]

whereas

\[
\operatorname{tr}(I)^2\not\equiv\det(I)\pmod{r^k}.
\]

Thus the same two integer matrices provide EDGE/NONEDGE witnesses simultaneously at all positive valuation depths. No projective-order classification over \(\mathbb Z/r^k\mathbb Z\) is needed.

## 8. Finite Pattern Realization at variable depth

Choose a finite marker set

\[
R\subset
P_+(\kappa)\setminus(S_\Delta\cup\{2,3\}).
\]

For an arbitrary subset \(T\subseteq R\), prescribe the coordinate

\[
g_r=
\begin{cases}
A,&r\in T,\\
I,&r\notin T
\end{cases}
\]

modulo \(r^{\kappa(r)}\).

By Arbitrary-Depth Finite Residual Independence, there exists

\[
\sigma\in H
\]

with these prescribed coordinates.

Let \(L/\mathbb Q\) be the finite Galois extension cut out by the combined representations modulo \(r^{\kappa(r)}\) for \(r\in R\). The image of \(\sigma\) is an element of \(\operatorname{Gal}(L/\mathbb Q)\). By Chebotarev, infinitely many rational primes \(p\notin R\) have Frobenius conjugacy class equal to that element.

Trace and determinant are conjugacy invariants. Hence, for such \(p\),

\[
E_\kappa(p;r)
\iff
r\in T
\qquad(r\in R).
\]

Therefore every finite Boolean pattern on positive-depth marker primes is realized by infinitely many source primes.

## 9. Infinite GIR

Define the fixed isolator

\[
I_\kappa(p,q;r)
:=
E_\kappa(p;r)\land E_\kappa(q;r).
\]

For any \(n\ge1\), choose \(n^2\) distinct marker primes

\[
r_{ij}
\in
P_+(\kappa)\setminus(S_\Delta\cup\{2,3\}).
\]

For every row \(i\), use finite pattern realization to choose a prime \(p_i\) whose positive pattern on the marker grid is exactly

\[
\{r_{i1},\dots,r_{in}\}.
\]

For every column \(j\), choose a prime \(q_j\) whose positive pattern is exactly

\[
\{r_{1j},\dots,r_{nj}\}.
\]

The realization sets are infinite, so all row primes, column primes, and markers can be chosen pairwise distinct.

Then

\[
I_\kappa(p_k,q_\ell;r_{ij})
\iff
(k,\ell)=(i,j).
\]

Therefore

\[
\boxed{
\operatorname{GIR}(I_\kappa)=\infty.
}
\]

This requires only infinitely many positive-depth places. Their density may be zero, and the values \(\kappa(r)\) may be unbounded.

## 10. Uniform finite graph coding

Divisibility is definable in the source sort:

\[
x\mid y
\iff
\exists z\;y=xz.
\]

For a source integer \(a\), let

\[
D_a(x):=\operatorname{Prime}(x)\land x\mid a.
\]

For a source integer \(\nu\), define

\[
R_\nu(x,y)
:=
\exists r\,
\bigl(
\operatorname{Prime}(r)
\land r\mid\nu
\land I_\kappa(x,y;r)
\bigr).
\]

Given an \(n\times n\) marker grid, let

\[
a=\prod_i p_i,
\qquad
b=\prod_j q_j,
\]

and choose

\[
\mu=\prod_i r_{ii}.
\]

Then \(R_\mu\) is a bijection between the finite prime supports \(D_a\) and \(D_b\).

For any finite directed graph \(G\subseteq[n]\times[n]\), put

\[
\nu_G
=
\prod_{(i,j)\in G}r_{ij}.
\]

The relation

\[
G_{a,b,\mu,\nu}(x,z)
:=
\exists y\,
\bigl(
D_b(y)
\land R_\mu(z,y)
\land R_\nu(x,y)
\bigr)
\]

interprets \(G\) on \(D_a\).

Conversely, every tuple \((a,b,\mu,\nu)\) for which \(R_\mu\) is a bijection between \(D_a\) and \(D_b\) determines a finite graph on the finite set \(D_a\).

Therefore the standard effective relativization of a sentence in one binary-relation language reduces finite satisfiability to truth in \(\mathcal V_{\Delta,\kappa}\). By Trakhtenbrot's theorem,

\[
\boxed{
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
\text{ is undecidable}
}
\]

whenever \(P_+(\kappa)\) is infinite.

The same reduction already lives in the source expansion

\[
(\mathbb N_{>0},\times,1,E_\kappa),
\]

so the target additive sort is not used after the residual incidence has been exposed.

## 11. Exact definability boundary over the zero-depth structure

The finite-support direction already showed

\[
|P_+(\kappa)|<\infty
\Longrightarrow
B_\kappa\in\operatorname{Def}(\mathcal V_{\Delta,0}).
\]

For the converse, assume \(P_+(\kappa)\) is infinite and suppose \(B_\kappa\) were definable in \(\mathcal V_{\Delta,0}\). Then the fixed source relation \(E_\kappa\), and hence the fixed isolator \(I_\kappa\), would also be definable in \(\mathcal V_{\Delta,0}\).

But the Uniform Zero-Depth Compression Theorem gives

\[
\forall I\quad\operatorname{GIR}(I)<\infty
\]

for every fixed formula in \(\mathcal V_{\Delta,0}\), whereas Section 9 gives

\[
\operatorname{GIR}(I_\kappa)=\infty.
\]

Contradiction. Thus

\[
\boxed{
B_\kappa\in\operatorname{Def}(\mathcal V_{\Delta,0})
\iff
|P_+(\kappa)|<\infty.
}
\]

This strengthens the previously proved special case \(B_1\notin\operatorname{Def}(\mathcal V_{\Delta,0})\).

## 12. Constant-depth corollary

For every fixed \(m\ge1\), take

\[
\kappa(r)=m
\qquad\text{for all primes }r.
\]

Then

\[
P_+(\kappa)=\mathbb P,
\]

so

\[
\boxed{
\forall m\ge1:
\quad
\exists I_m\;\operatorname{GIR}(I_m)=\infty,
\qquad
\operatorname{Th}(\mathcal V_{\Delta,m})\text{ undecidable}.
}
\]

Thus depth one is not an isolated accident. **Every fixed positive valuation depth lies on the same right-hand side of the GIR wall.**

## 13. Phase diagram

The earlier sequence

\[
B_0\quad|\quad B_1
\]

now becomes the complete threshold-profile phase diagram

\[
\boxed{
\begin{array}{c}
|P_+(\kappa)|<\infty\\[2mm]
\mathcal V_{\Delta,\kappa}\equiv_{\mathrm{def}}\mathcal V_{\Delta,0}\\[1mm]
\forall I\;\operatorname{GIR}(I)<\infty
\end{array}
\quad\Bigg|\quad
\begin{array}{c}
|P_+(\kappa)|=\infty\\[2mm]
\exists I_\kappa\;\operatorname{GIR}(I_\kappa)=\infty\\[1mm]
\operatorname{Th}(\mathcal V_{\Delta,\kappa})\text{ undecidable}
\end{array}
}
\]

The wall is therefore a **support-cardinality wall**.

## 14. Hostile-audit checklist

The first hostile audit specifically checked the following failure modes.

1. **Variable depths.** No uniform bound on \(\kappa(r)\) is used. Every finite grid sees only finitely many finite moduli \(r^{\kappa(r)}\).
2. **Adelic independence.** The argument needs full local factors outside a finite set, not merely independent mod-\(r\) images. This is supplied by the open adelic image and basic profinite topology.
3. **Chebotarev versus the cyclotomic kernel.** Chebotarev is applied to the image of one \(\sigma\in H\) in the finite Galois quotient cut out by the chosen finite-level representations; no Frobenius element is required to lie in \(H\) itself.
4. **Conjugacy.** Only trace and determinant are read from Frobenius, so passage to a conjugacy class is harmless.
5. **Higher-level cubic classification.** None is assumed. The integral matrix \(A\) gives an exact zero of \(\operatorname{tr}^2-\det\) at every level; the identity gives the fixed nonzero value \(3\).
6. **Small marker primes.** Markers \(2,3\) are excluded.
7. **Zero primes of \(\tau\).** Pattern-realizing primes have trace \(1\) or \(2\) modulo at least one marker prime, so they cannot satisfy \(\tau(p)=0\).
8. **Sparse positive support.** Only infinitude is used; no density hypothesis appears.
9. **Effective undecidability reduction.** The translated graph sentence uses \(B_\kappa\) only through one fixed formula; it does not need to compute the values \(\kappa(r)\).
10. **Safe side.** Finite positive support is handled by explicit parameter-free interdefinability with \(B_0\), not by an unproved extension of zero-depth compression.

## 15. Claim boundary

This checkpoint does **not** claim:

- that ordinary prime order or prime successor is definable when \(P_+(\kappa)\) is infinite;
- that all positive profiles are mutually interdefinable;
- that \(B_0\) is definable from every infinite positive profile;
- NIP, stability, simplicity, or any other global classification of the positive-profile theories;
- minimality of the finite exceptional adelic set;
- historical priority without a dedicated specialist literature audit.

The result isolates a stronger phenomenon than the earlier zero/one statement: infinite residual graph universality can appear on an arbitrarily sparse set of positively deep places, while any finite positive-depth perturbation remains definitionally equivalent to zero depth.

## 16. Current verdict

**Theorem checkpoint: PASS after first hostile audit.**

Next required step before publication: a second adversarial audit focused on the exact open-image-to-arbitrary-level surjectivity step and on the parameter-free finite-graph interpretation.