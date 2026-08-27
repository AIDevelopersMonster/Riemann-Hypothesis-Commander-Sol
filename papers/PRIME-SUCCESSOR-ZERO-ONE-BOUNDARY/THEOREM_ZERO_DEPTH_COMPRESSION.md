# Theorem Checkpoint — Uniform Zero-Depth Compression

**Project:** Prime-Successor Algebra / Two Walls  
**Paper:** *Reflections on the Exact Zero/One Valuation Boundary with Commander Sol*  
**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Status:** theorem-level proof checkpoint, hostile-audit repaired  
**Date:** 2026-08-27

## 1. Structure

We work in the two-sorted structure

\[
\mathcal V_{\Delta,0}
=
\Bigl(
(\mathbb N_{>0},\times,1),
(\mathbb Q,+,0),
U_\Delta,
B_0
\Bigr),
\]

where

\[
U_\Delta(p,x)
\iff
\operatorname{Prime}(p)\land x=u_p,
\qquad
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

and

\[
B_0(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge0.
\]

A prime \(p\ge5\) is **regular** if \(\tau(p)\ne0\). For regular \(p\),

\[
\operatorname{DenSupp}(u_p)=\{p\}.
\]

If \(\tau(p)=0\), then \(u_p=-1\); all zero primes form one exact defect class.

## 2. Statement

### Uniform Zero-Depth Compression Theorem

For every parameter-free first-order formula

\[
\Phi(p_1,\ldots,p_n)
\]

whose free source variables are restricted to prime atoms, there exist

- a finite set of source primes \(F_\Phi\), and
- a finite formula-relative coloring \(c_\Phi\) of the regular prime tail,

such that for every prime permutation \(\sigma\) satisfying

1. \(\sigma\) fixes \(F_\Phi\) pointwise;
2. \(c_\Phi(\sigma(p))=c_\Phi(p)\) on the regular tail;
3. the zero-prime defect class is preserved setwise;

we have

\[
\mathcal V_{\Delta,0}\models\Phi(\bar p)
\iff
\mathcal V_{\Delta,0}\models\Phi(\sigma\bar p).
\]

The theorem is formula-relative. It is **not** a global automorphism theorem on the target sort.

## 3. Private-denominator input

For a regular prime \(p\ge5\), write \(a=v_p(\tau(p))\). Deligne gives

\[
|\tau(p)|\le2p^{11/2}.
\]

Hence \(a\le5\), so

\[
v_p(u_p)=2a-11<0.
\]

For every \(r\ne p\), the denominator \(p^{11}\) is an \(r\)-adic unit and therefore

\[
v_r(u_p)\ge0.
\]

Thus

\[
\neg B_0(r,u_p)\iff r=p.
\]

An infinite regular reservoir follows from Ramanujan's congruence

\[
\tau(p)\equiv1+p^{11}\pmod{691}
\]

and Dirichlet's theorem applied to \(p\equiv1\pmod{691}\).

## 4. Quotient interpretation and audit repair

For a prime \(r\), put

\[
B_r=\{x\in\mathbb Q:v_r(x)\ge0\},
\qquad
G_r=\mathbb Q/B_r.
\]

Then

\[
G_r\cong C_{r^\infty},
\]

and

\[
B_0(r,x)\iff[x]_r=0\text{ in }G_r.
\]

Moreover

\[
\mathbb Q/\mathbb Z\cong\bigoplus_rC_{r^\infty}.
\]

It is false that one may globally transport \(C_{r^\infty}\) to \(C_{s^\infty}\) by an isomorphism when \(r\ne s\). Their element orders are powers of different primes. The proof therefore uses only finite-fragment transfer.

## 5. Finite closure and generic primes

For a fixed formula \(\Phi\), choose a finite syntactic closure \(\Delta_\Phi\) containing all atomic subformulas, all target integer-linear forms appearing in them, all compatibility forms \(a_jt_i-a_it_j\) needed for pinning arguments, and the finitely many forms generated in the one-variable witness induction.

Every relevant form in a new target witness \(y\) has the shape

\[
a y+t,
\]

where \(a\in\mathbb Z\) is fixed by the syntax and \(t\) is built from already matched target data.

Let \(E_\Phi\) contain every prime dividing any nonzero coefficient appearing in this closure, enlarged by the finitely many stationary places required later. A prime \(r\notin E_\Phi\) is generic.

## 6. Generic Local One-Witness Transfer Lemma

Let \(r,s\notin E_\Phi\). Suppose the already matched target tuple has the same \(\Delta_\Phi\)-linear zero/nonzero pattern in \(G_r\) and \(G_s\). If \(y\in G_r\) is a new witness, there is \(y'\in G_s\) preserving every local atom from the closure.

Every local atom containing \(y\) is

\[
a_i y+t_i=0
\quad\text{or}\quad
a_i y+t_i\ne0.
\]

Because \(r,s\notin E_\Phi\), every nonzero \(a_i\) is simultaneously an \(r\)-adic and \(s\)-adic unit. Hence multiplication by \(a_i\) is an automorphism of both Prüfer groups.

**Pinned case.** If a true equation with \(a_i\ne0\) exists, then

\[
y=-a_i^{-1}t_i.
\]

Two pins are compatible iff

\[
a_jt_i-a_it_j=0,
\]

and a pinned value satisfies a required negative atom iff the corresponding compatibility difference is nonzero. These forms are in the closure, so the same truth pattern holds at \(s\).

**Free case.** If no true nonzero-coefficient equation exists, every negative nonzero-coefficient atom forbids exactly one point of \(G_s\). Finitely many points cannot exhaust the infinite group \(C_{s^\infty}\). Choose outside them.

The reverse direction is identical.

## 7. Finite-support globalization

For one global target witness \(y\in\mathbb Q\), let \(L_1,\ldots,L_N\) be the finitely many forms from the closure containing \(y\). Define

\[
A(y)=\bigcup_j\operatorname{DenSupp}(L_j(y)).
\]

This set is finite. Local transfer is needed only for primes in \(A(y)\), together with the finite exceptional atlas \(E_\Phi\). Outside these places all relevant local classes are zero.

After transporting the finitely many generic local components, the primary decomposition

\[
\mathbb Q/\mathbb Z\cong\bigoplus_rC_{r^\infty}
\]

produces one element of \(\mathbb Q/\mathbb Z\), hence a rational lift \(y'_0\in\mathbb Q\). No infinite-support element is introduced.

## 8. Exact equations

Exact atoms in the new witness have the form

\[
a_i y+t_i=0
\quad\text{or}\quad
a_i y+t_i\ne0
\]

in \(\mathbb Q\).

### Exact pinned case

If one true equation has \(a_i\ne0\), then

\[
y=-t_i/a_i.
\]

Define \(y'=-t'_i/a_i\). Multiple exact pins are compatible iff

\[
a_jt_i-a_it_j=0,
\]

which is included in the closure. At generic places division by \(a_i\) is local multiplication by a unit. Places dividing \(a_i\) are exceptional and handled by the stationary atlas.

### Free exact case: Integer-Translation Lemma

If no true exact atom pins \(y\), start with a rational lift \(y'_0\) having the correct \(B_0\)-diagram and define

\[
y'_N=y'_0+N,
\qquad N\in\mathbb Z.
\]

For every prime \(r\), fixed integer \(a\), and old target term \(t\),

\[
B_0(r,a(y'_0+N)+t)
\iff
B_0(r,ay'_0+t).
\]

Indeed, the two arguments differ by the integer \(aN\), which is \(r\)-integral at every finite place. Each false exact equality with \(a\ne0\) forbids at most one integer \(N\). Since the closure is finite, choose \(N\) outside the finite forbidden set.

## 9. Bridge-incidence preservation

If \(y=u_p\) for a regular source prime \(p\), it is bridge-pinned and is transported to

\[
y'=u_{\sigma(p)}.
\]

If \(y=-1\), it is the common defect value and remains \(-1\).

If \(y\) is not a bridge value, integer translation preserves denominator support. A regular bridge value \(u_q\) has support exactly \(\{q\}\), so only finitely many \(q\) can possibly satisfy \(y'_0+N=u_q\). Each forbids at most one integer \(N\), and \(-1\) forbids at most one more. Add these values to the finite forbidden set.

Thus free witness transport preserves both positive and negative bridge incidences.

## 10. Exceptional atlas

When a moving place equals a prime \(\ell\in E_\Phi\), the uniform predicate becomes a fixed stationary predicate \(B_0(\ell,\cdot)\). Exact pinning may create finitely many fixed depth requirements \(v_\ell(x)\ge m\). These are precisely the finite multi-adic conditions covered by the published Stationary Locality theorem (DOI 10.5281/zenodo.22110465).

The exceptional atlas therefore contributes only a finite formula-relative color \(c_\Phi(p)\) on the regular source-prime tail.

## 11. Back-and-forth

A prime permutation \(\sigma\) extends to the multiplicative source automorphism

\[
\widehat\sigma\left(\prod_pp^{e_p}\right)
=
\prod_p\sigma(p)^{e_p}.
\]

For each target witness use the priority:

1. bridge-pinned;
2. exact-pinned;
3. free local transfer + rational lift + integer translation.

The back move uses \(\sigma^{-1}\). Induction on the finite syntactic closure proves the theorem.

## 12. Consequences

\[
<_{\mathbb P}\notin\operatorname{Def}(\mathcal V_{\Delta,0}),
\qquad
\operatorname{Succ}_{\mathbb P}\notin\operatorname{Def}(\mathcal V_{\Delta,0}).
\]

For every fixed isolator \(I(p,q;r)\),

\[
\operatorname{GIR}(I)<\infty.
\]

The published depth-one paper (DOI 10.5281/zenodo.22116714) gives a fixed isolator \(I_1\) with

\[
\operatorname{GIR}(I_1)=\infty.
\]

Hence

\[
B_1\notin\operatorname{Def}(\mathcal V_{\Delta,0}).
\]

## 13. Claim boundary

The checkpoint does **not** claim decidability of \(\operatorname{Th}(\mathcal V_{\Delta,0})\), NIP/stability/simplicity, global non-interpretability of arithmetic, a global target automorphism implementing arbitrary prime permutations, effective complexity bounds for \(\Phi\mapsto(F_\Phi,c_\Phi)\), or historical priority without specialist prior-art review.

## 14. Audit verdict

The initial naive coordinate-permutation proof was rejected. After replacing it by finite-fragment generic local transfer and separately auditing exact equations, finite support, bridge incidences, zero-prime defects, and the exceptional atlas, the theorem survives.

**Theorem checkpoint status: PASS for publication packaging.**
