# Seventh Strike — A Genuine Singleton Exact Trace Atom

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; publication status not assigned

## 1. Question

The previous stage reduced the multiplicity channel for a binary support `S` to

\[
\mu_S(F)=\left|\{p\notin S:D(p)\cap S=F\}\right|,
\]

where

\[
D(p)=\{r:r\mid \tau(p)^2-p^{11}\}.
\]

The immediate problem was whether a nonzero exact atom can be finite, and in particular whether one can realize

\[
\mu_S(F)=1.
\]

The answer is **yes in the actual Ramanujan prime-only structure**, even with both the support and its complement infinite.

This refutes the unrestricted statement that every nonzero exact atom must be infinite.

---

## 2. Hecke identification of the residual integer

For every prime `p`, the Hecke recurrence gives

\[
\tau(p^2)=\tau(p)^2-p^{11}.
\tag{1}
\]

Hence

\[
\boxed{D(p)=\operatorname{PrimeDiv}(\tau(p^2)).}
\tag{2}
\]

Thus the residual divisor hypergraph used throughout this branch is exactly the prime-divisor hypergraph of the square-prime Fourier coefficients `tau(p^2)`.

This connects the branch directly with the literature on prime factors of Fourier coefficients of Hecke eigenforms.

---

## 3. The mod-3 separator

We use the standard congruence of Swinnerton-Dyer quoted, for example, in Bennett–Gherga–Patel–Siksek:

for `n ≡ 1 (mod 3)`,

\[
\tau(n)\equiv n^{-610}\sigma_{1231}(n)\pmod{3^6}.
\tag{3}
\]

Only reduction modulo `3` is needed here.

### Lemma 3.1

If `q` is a prime with

\[
q\equiv1\pmod3,
\]

then

\[
3\mid \tau(q^2).
\tag{4}
\]

### Proof

Since `q ≡ 1 (mod 3)`, equation (3) gives

\[
\tau(q)
\equiv
q^{-610}(1+q^{1231})
\equiv
1\cdot(1+1)
\equiv2
\pmod3.
\tag{5}
\]

Using (1),

\[
\tau(q^2)
=
\tau(q)^2-q^{11}
\equiv
2^2-1^{11}
\equiv
4-1
\equiv0
\pmod3.
\tag{6}
\]

Therefore `3 | tau(q^2)`. ∎

---

## 4. The target prime `2`

The exact square-prime coefficient at `2` is

\[
\tau(4)
=
\tau(2)^2-2^{11}
=
(-24)^2-2048
=-1472
=-2^6\cdot23.
\tag{7}
\]

Therefore

\[
D(2)=\{2,23\}.
\tag{8}
\]

---

## 5. The support

Define

\[
S_*
:=
\{3\}
\cup
\{r\in\mathbb P:r\equiv2\pmod3,\ r\ne2\}.
\tag{9}
\]

Then both `S_*` and its complement are infinite. In fact

\[
\mathbb P\setminus S_*
=
\{2\}
\cup
\{q\in\mathbb P:q\equiv1\pmod3\}.
\tag{10}
\]

Let `kappa_*` be the binary profile

\[
\kappa_*(r)=1\iff r\in S_*.
\tag{11}
\]

For an external prime `p`, its exact active trace is

\[
T_*(p):=D(p)\cap S_*.
\tag{12}
\]

---

## 6. Singleton Atom Theorem

### Theorem 6.1 — Genuine finite atom

For the support `S_*` defined in (9),

\[
\boxed{\mu_{S_*}(\{23\})=1.}
\tag{13}
\]

The unique external source prime realizing the exact trace `{23}` is `p=2`.

### Proof

First consider `p=2`. By (8),

\[
D(2)=\{2,23\}.
\]

Now `2 notin S_*`, while

\[
23\equiv2\pmod3
\]

and `23 != 2`, so `23 in S_*`. Hence

\[
T_*(2)=D(2)\cap S_*=\{23\}.
\tag{14}
\]

Thus

\[
\mu_{S_*}(\{23\})\ge1.
\tag{15}
\]

Now let `q` be any other external prime. By (10), necessarily

\[
q\equiv1\pmod3.
\tag{16}
\]

Lemma 3.1 gives

\[
3\mid\tau(q^2),
\]

so by (2),

\[
3\in D(q).
\tag{17}
\]

Since `3 in S_*`,

\[
3\in T_*(q).
\tag{18}
\]

But

\[
3\notin\{23\}.
\]

Therefore

\[
T_*(q)\ne\{23\}.
\tag{19}
\]

No external prime other than `2` realizes the target trace. Hence

\[
\mu_{S_*}(\{23\})=1.
\]

∎

---

## 7. Immediate consequences

### Corollary 7.1

The unrestricted multiplicity statement

\[
\mu_S(F)>0\Longrightarrow \mu_S(F)=\aleph_0
\]

is false for actual Ramanujan binary profiles.

### Proof

Take `(S,F)=(S_*,{23})` and apply Theorem 6.1. ∎

### Corollary 7.2

Finite-pattern Chebotarev richness and the existence of finite exact atoms are compatible.

The obstruction is that exact atoms impose a global condition on the whole support, while Chebotarev controls only finitely many coordinates at a time.

---

## 8. What was really solved

The finite-atom problem has two versions.

### Version A — unrestricted active skeleton

Solved positively by Theorem 6.1:

\[
\boxed{\exists S,F\quad \mu_S(F)=1.}
\tag{20}
\]

The support and complement can both be infinite.

### Version B — frozen/independent active skeleton

Still open:

> Can one realize `mu_S(F)=1` while the active skeleton on `S` is empty (or belongs to another fixed tame class)?

The present construction does not satisfy that extra restriction. Its purpose is to show that **arithmetic exact atoms themselves are not forced to be 0 or infinity**.

Thus the remaining difficulty is no longer the existence of finite arithmetic atoms. It is the simultaneous compatibility of finite atom control with active-skeleton constraints.

---

## 9. New interpretation of the barrier

Before this strike, two possibilities remained:

1. a hidden arithmetic 0/infinity law for exact trace fibers;
2. finite atoms exist, but may be difficult to reconcile with skeleton control.

Theorem 6.1 eliminates the first possibility.

Therefore the genuine remaining frontier is

\[
\boxed{\textbf{Atom–Skeleton Compatibility}.}
\tag{21}
\]

More explicitly:

- exact multiplicity can already be finite in the true Ramanujan structure;
- the hard problem is to prescribe exact multiplicity **and** preserve a chosen tame active skeleton.

The sharp next question is:

> Does there exist an infinite independent support `S` and finite `F subset S` with `mu_S(F)=1`?

A negative answer would be a rigidity theorem specific to independent supports, not a universal 0/infinity theorem.

---

## 10. Literature connection

The identity (1) shows that the quantity driving the residual incidence is `tau(p^2)`. Bennett, Gherga, Patel and Siksek, *Odd values of the Ramanujan tau function*, Math. Ann. 382 (2022), 203–238, DOI 10.1007/s00208-021-02241-3, study prime factors of `tau(p^m)` and in particular prove effective lower bounds for the largest prime factor of `tau(p^m)` for fixed `m >= 2` when `tau(p) != 0`.

That external input is not needed for Theorem 6.1, which uses only the Hecke recurrence, the explicit value at `2`, and the mod-3 congruence. It does, however, show that the residual divisor hypergraph of this branch sits inside an already-developed arithmetic theory of prime factors of Fourier coefficients.

---

## 11. Hostile audit

1. **Is the target prime accidentally active?** No: `2 notin S_*` by definition.
2. **Is `23` really active?** Yes: `23 ≡ 2 (mod 3)` and `23 != 2`.
3. **Could another external prime fail to be `1 mod 3`?** No. The prime `3` is active, and every prime other than `2,3` is `1` or `2 mod 3`; all `2 mod 3` primes except `2` are active.
4. **Does every external `q ≡ 1 mod 3` really acquire marker `3`?** Yes, by Lemma 3.1.
5. **Could `3` also occur in the target trace of `2`?** No, because `tau(4)=-2^6*23`.
6. **Is Lehmer's conjecture used?** No.
7. **Is adelic open image used?** No.
8. **Is Chebotarev used?** No.
9. **Does the proof claim empty active skeleton?** No; that stronger constrained problem is explicitly left open.

**Audit verdict:** PASS for the stated singleton-atom theorem.
