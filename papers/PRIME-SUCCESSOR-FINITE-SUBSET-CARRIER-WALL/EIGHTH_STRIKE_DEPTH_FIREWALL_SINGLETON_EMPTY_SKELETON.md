# Eighth Strike — Depth-Firewall Singleton under an Empty Active Skeleton

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; publication status not assigned

## 1. Question

The seventh strike proved that a genuine arithmetic singleton exact atom exists in the Ramanujan trace system, but not with a controlled empty active skeleton.

The sharp compatibility question was:

> Can finite exact multiplicity coexist with an empty active skeleton?

For the full threshold-profile family, the answer is **yes**. In fact every prescribed positive finite multiplicity can be realized at the empty exact trace, while the positive-depth support is infinite, its complement is infinite, and the active skeleton is empty.

The construction uses variable threshold depths as a one-way firewall.

The binary-depth version remains open and is explicitly separated at the end.

---

## 2. Setup

For every prime `p`, put

\[
N_p:=\tau(p)^2-p^{11}.
\tag{1}
\]

As before,

\[
N_p\ne0
\tag{2}
\]

because equality would imply

\[
2v_p(\tau(p))=11.
\tag{3}
\]

Let

\[
\kappa:\mathbb P\to\mathbb N_0
\tag{4}
\]

be a threshold profile, with positive support

\[
S_\kappa:=\{r:\kappa(r)>0\}.
\tag{5}
\]

For distinct primes `p,r`,

\[
E_\kappa(p;r)
\iff
v_r(N_p)\ge\kappa(r).
\tag{6}
\]

For an external prime `p notin S_kappa`, define the exact active trace

\[
T_\kappa(p)
:=
\{r\in S_\kappa:E_\kappa(p;r)\}.
\tag{7}
\]

For finite `F subset S_kappa`, let

\[
\mu_\kappa(F)
:=
\left|
\{p\notin S_\kappa:T_\kappa(p)=F\}
\right|.
\tag{8}
\]

The active skeleton is empty when

\[
E_\kappa(s;t)=\text{false}
\qquad
\text{for all distinct }s,t\in S_\kappa.
\tag{9}
\]

---

## 3. The depth-firewall rule

Fix a nonempty finite target set of source primes

\[
T\subseteq\mathbb P
\tag{10}
\]

and assume

\[
3\in T.
\tag{11}
\]

The elements of `T` will be the only external primes having empty active trace.

Enumerate the remaining primes as

\[
q_0,q_1,q_2,\dots
\quad=
\mathbb P\setminus T.
\tag{12}
\]

We construct a partial support

\[
S_0\subseteq S_1\subseteq\cdots
\tag{13}
\]

and threshold values on admitted markers.

Start with

\[
S_0=\varnothing.
\tag{14}
\]

At stage `n`, inspect `q_n`.

### Case A — already hit

If there exists `r in S_n` such that

\[
v_r(N_{q_n})\ge\kappa(r),
\tag{15}
\]

then leave `q_n` external:

\[
q_n\notin S_{n+1},
\qquad
S_{n+1}=S_n.
\tag{16}
\]

### Case B — currently unhit

If

\[
v_r(N_{q_n})<\kappa(r)
\qquad
\text{for every }r\in S_n,
\tag{17}
\]

then admit `q_n` into the positive support and define its depth by

\[
\boxed{
\kappa(q_n)
=
1+
\max
\left(
\{v_{q_n}(N_t):t\in T\}
\cup
\{v_{q_n}(N_s):s\in S_n\}
\right).
}
\tag{18}
\]

Then set

\[
S_{n+1}=S_n\cup\{q_n\}.
\tag{19}
\]

Finally set

\[
\kappa(t)=0
\qquad(t\in T).
\tag{20}
\]

Because all sets in the maximum (18) are finite and every `N_p` is nonzero, the depth is a finite positive integer.

---

## 4. Empty-skeleton theorem

### Theorem 4.1 — Depth Firewall

The support produced by the recursion satisfies

\[
\boxed{
E_\kappa(s;t)=\text{false}
\quad
(s\ne t,\ s,t\in S_\kappa).
}
\tag{21}
\]

Hence the active skeleton is empty.

### Proof

Suppose `q_n` is admitted at stage `n` and let `s in S_n` be an earlier active prime.

By the admission condition (17),

\[
v_s(N_{q_n})<\kappa(s),
\tag{22}
\]

so

\[
\neg E_\kappa(q_n;s).
\tag{23}
\]

In the reverse direction, (18) gives

\[
\kappa(q_n)>v_{q_n}(N_s),
\tag{24}
\]

hence

\[
\neg E_\kappa(s;q_n).
\tag{25}
\]

Thus every new active prime is nonadjacent in both directions to every previous active prime.

For future active primes the same argument applies at their own admission stage, so no active-active edge can ever appear. ∎

---

## 5. Target protection

### Lemma 5.1 — Every target has empty trace

For every `t in T`,

\[
\boxed{T_\kappa(t)=\varnothing.}
\tag{26}
\]

### Proof

Let `r in S_kappa`. At the stage when `r` was admitted, formula (18) imposed

\[
\kappa(r)>v_r(N_t)
\qquad(t\in T).
\tag{27}
\]

Therefore

\[
\neg E_\kappa(t;r)
\tag{28}
\]

for every active marker `r`. Hence the active trace of `t` is empty. ∎

---

## 6. Every non-target external source is hit

### Lemma 6.1

If

\[
p\notin T\cup S_\kappa,
\tag{29}
\]

then

\[
T_\kappa(p)\ne\varnothing.
\tag{30}
\]

### Proof

The prime `p` occurs as some `q_n`. Since it was not admitted into the support, Case A must have applied. Hence at that stage there existed `r in S_n` with

\[
v_r(N_p)\ge\kappa(r).
\tag{31}
\]

The depth `kappa(r)` is never changed later. Thus

\[
E_\kappa(p;r)
\tag{32}
\]

holds in the final structure, so `r in T_kappa(p)`. ∎

---

## 7. Exact finite multiplicity theorem

### Theorem 7.1 — Empty-Trace Finite Multiplicity Realization

Let `m>=1`. There exists a threshold profile `kappa_m` such that:

1. `S_{kappa_m}` is infinite;
2. `P \ S_{kappa_m}` is infinite;
3. the active skeleton on `S_{kappa_m}` is empty;
4. the exact empty trace has multiplicity exactly `m`:

\[
\boxed{
\mu_{\kappa_m}(\varnothing)=m.
}
\tag{33}
\]

Moreover the profile can be chosen computable.

### Proof

Choose any finite target set `T` of size `m` containing `3`, and perform the recursion of Section 3.

By Theorem 4.1 the active skeleton is empty. By Lemma 5.1 every target prime has empty active trace. By Lemma 6.1 every other external prime has nonempty active trace. Therefore

\[
\{p\notin S_\kappa:T_\kappa(p)=\varnothing\}=T,
\tag{34}
\]

which proves (33).

It remains to prove that the support is infinite.

Assume for contradiction that the final support is a finite set

\[
R=\{r_1,\dots,r_d\}.
\tag{35}
\]

Because `3 in T`,

\[
3\notin R.
\tag{36}
\]

For each `r_i`, let

\[
k_i:=\kappa(r_i)\ge1.
\tag{37}
\]

Consider the finite Galois extension obtained by adjoining the coordinates of the Galois representations attached to `Delta` modulo all `r_i^{k_i}`. Its identity conjugacy class is nonempty. By Chebotarev there are infinitely many rational primes `q` splitting completely in this finite extension.

For such a prime `q`, at every marker `r_i`,

\[
\rho_{\Delta,r_i^{k_i}}(\operatorname{Frob}_q)=I.
\tag{38}
\]

Hence

\[
\tau(q)\equiv2\pmod{r_i^{k_i}}
\tag{39}
\]

and, from the determinant,

\[
q^{11}\equiv1\pmod{r_i^{k_i}}.
\tag{40}
\]

Therefore

\[
N_q
=
\tau(q)^2-q^{11}
\equiv3
\pmod{r_i^{k_i}}.
\tag{41}
\]

Since `r_i != 3`, equation (41) implies

\[
v_{r_i}(N_q)=0<k_i.
\tag{42}
\]

Thus `q` is unhit by every marker in `R`. Choosing such a `q` outside the finite target set and after all existing support primes have appeared in the enumeration, Case B would admit it into the support, contradicting finiteness of `R`.

So the support is infinite.

To show the complement is infinite, note that an infinite support contains a marker `r` outside the finite exceptional set for the previously established finite-pattern theorem. For that fixed marker and fixed positive depth `kappa(r)`, finite-pattern realization supplies infinitely many primes `p` with

\[
E_\kappa(p;r).
\tag{43}
\]

No distinct active prime can satisfy (43), because the active skeleton is empty. Hence these primes are external, so the complement is infinite.

Finally the construction is computable: at each stage one computes the finite integer values `N_p`, checks finitely many divisibility/valuation inequalities, and evaluates the finite maximum (18). Thus both support membership and threshold values are recursively determined. ∎

---

## 8. Singleton corollary

### Corollary 8.1 — Singleton under empty active skeleton

There exists a computable threshold profile `kappa` with infinite positive support and infinite complement such that

\[
\boxed{
\text{active skeleton is empty}
\quad\text{and}\quad
\mu_\kappa(\varnothing)=1.
}
\tag{44}
\]

### Proof

Take

\[
T=\{3\}
\tag{45}
\]

in Theorem 7.1. The unique external source with empty active trace is `3`. ∎

---

## 9. What mechanism solved the compatibility problem?

At depth one, adding a new marker `q` can create an old-to-new active edge whenever

\[
q\mid N_s
\tag{46}
\]

for some previously chosen active source `s`. This was the reverse-divisor obstruction encountered in the binary branch.

Variable depth removes it completely: after deciding to admit `q`, choose

\[
\kappa(q)>\max_{s\in S_n}v_q(N_s).
\tag{47}
\]

Then no old active source reaches the new marker.

At the same time, admitting `q` only when it has no edge to any old marker guarantees the other direction.

Thus variable threshold depth acts as a **one-way firewall** which turns a difficult directed-kernel problem into a greedy recursion.

---

## 10. Consequences for the branch

The following statement is now proved in the actual arithmetic structure:

\[
\boxed{
\text{finite exact multiplicity and empty active geometry are compatible.}
}
\tag{48}
\]

Indeed every positive finite multiplicity occurs at the empty atom.

Therefore the previous alternative

> perhaps empty active geometry forces every nonzero exact atom to be infinite

is false for the full threshold-profile family.

The multiplicity channel is genuinely independent of active-skeleton complexity once variable depths are available.

---

## 11. Claim boundary: the binary problem survives

The construction crucially uses the freedom to raise `kappa(q)` in (18).

It does **not** solve the binary support problem

\[
\kappa(r)\in\{0,1\}.
\tag{49}
\]

For binary profiles, the reverse-divisor obstruction cannot be removed by increasing the new marker depth. Thus the following remains open:

> Does there exist an infinite binary support `S` with empty active skeleton and a finite exact atom, for example `mu_S(F)=1`?

The correct frontier has therefore split into two regimes:

\[
\boxed{
\begin{array}{ccl}
\text{variable depth} &:& \text{singleton + empty skeleton exists},\\
\text{binary depth} &:& \text{open reverse-divisor problem}.
\end{array}
}
\tag{50}
\]

---

## 12. Hostile audit

1. **Can a newly admitted active prime point to an old marker?**  
   No; Case B requires all such incidences to be false before admission.

2. **Can an old active prime point to the new marker?**  
   No; its valuation is strictly below the newly chosen threshold by (18).

3. **Can a target acquire a future active neighbor?**  
   No; every newly chosen threshold is strictly above all target valuations at that prime.

4. **Can a non-target external source remain empty-trace?**  
   No; it is external only because Case A found an already existing active edge.

5. **Can the support stop after finitely many markers?**  
   No; complete splitting in the finite compositum gives infinitely many all-nonedge source primes because marker `3` is excluded from the support.

6. **Why is marker `3` excluded?**  
   It is placed in the target set `T`. This is essential for the simple identity-Frobenius infinitude argument, since `N_q congruent 3` modulo a marker `3` would not be a nonedge.

7. **Could the complement be only the finite target set?**  
   No; any good active marker has infinitely many source primes incident to it by finite-pattern realization, and those sources cannot be active because the active skeleton is empty.

8. **Is the construction nonconstructive?**  
   No. The recursive profile itself is computable. Chebotarev is used only to prove that the recursively generated support cannot terminate and that the external complement is infinite.

9. **Does this prove the binary case?**  
   No. The binary case is explicitly left open.

**Audit verdict:** PASS for the stated variable-depth finite-multiplicity realization theorem.
