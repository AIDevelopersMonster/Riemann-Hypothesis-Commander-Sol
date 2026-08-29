# Sixth Strike — Pure Multiplicity Memory with Empty Active Skeleton

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; arithmetic realization problem remains open; no publication status assigned

## 1. Question

The fifth strike gave the exact isomorphism invariant

\[
(G_\kappa,\mu_\kappa),
\]

where \(G_\kappa\) is the active skeleton and \(\mu_\kappa(F)\) records the number of external primes whose active neighborhood is exactly the finite set \(F\).

We now freeze the geometric layer completely:

\[
G_\kappa=\varnothing.
\tag{1}
\]

The question is whether the second layer alone can carry undecidability.

This strike separates two issues which must not be conflated:

1. **abstract model-theoretic multiplicity memory** — what arbitrary multiplicity functions can do once the active skeleton is empty;
2. **Ramanujan arithmetic realization** — which of those multiplicity functions actually arise from threshold profiles \(\kappa\) through the divisibility sets of \(\tau(p)^2-p^{11}\).

The abstract question has a complete positive answer: multiplicity alone can encode a nonrecursive set even when every finite neighborhood exists and the only values of the multiplicity function are \(1\) and \(2\).

The arithmetic realization of such upper-controlled multiplicity spectra is not proved here and is isolated as the next genuine barrier.

---

## 2. Empty-skeleton multiplicity models

Let \(S\) be a countably infinite pure set. Let

\[
\operatorname{Fin}(S)
\]

be the set of finite subsets of \(S\).

Fix a function

\[
\mu:\operatorname{Fin}(S)
\to
\mathbb N_0\cup\{\aleph_0\}.
\tag{2}
\]

Define the one-sorted incidence structure

\[
\mathfrak M_\mu
\tag{3}
\]

as follows.

Its universe is the disjoint union

\[
S
\sqcup
\coprod_{F\in\operatorname{Fin}(S)} C_F,
\tag{4}
\]

where

\[
|C_F|=\mu(F).
\tag{5}
\]

Elements of \(S\) are called **active**, and elements of \(C_F\) are **external copies of the finite neighborhood \(F\)**.

The only nontrivial incidence relation is

\[
R(c,s)
\iff
c\in C_F\text{ and }s\in F.
\tag{6}
\]

There is no active-active incidence:

\[
R(s,t)=\text{false}
\qquad(s,t\in S).
\tag{7}
\]

This is the canonical abstract normal form of an empty active skeleton together with multiplicity data.

---

## 3. The multiplicity quotient

For external points define

\[
c\sim d
\iff
\forall s\in S\,
\bigl(R(c,s)\leftrightarrow R(d,s)\bigr).
\tag{8}
\]

The \(\sim\)-class of an external point is exactly one fiber \(C_F\).

Let

\[
\mathcal F_\mu
=
\{F\in\operatorname{Fin}(S):\mu(F)>0\}.
\tag{9}
\]

On the quotient sort of external \(\sim\)-classes define membership

\[
M(s,[c])
\iff
R(c,s),
\tag{10}
\]

and for each integer \(m\ge1\) define

\[
P_{\ge m}([c])
\iff
\text{the class }[c]\text{ has at least }m\text{ representatives}.
\tag{11}
\]

Equivalently, if \([c]\) corresponds to \(F\), then

\[
P_{\ge m}(F)
\iff
\mu(F)\ge m.
\tag{12}
\]

Call the resulting two-sorted quotient structure

\[
\mathfrak Q_\mu
=
\bigl(
S,
\mathcal F_\mu,
M,
(P_{\ge m})_{m\ge1}
\bigr).
\tag{13}
\]

### Theorem 3.1 — Exact first-order complexity reduction

The complete first-order theories of \(\mathfrak M_\mu\) and \(\mathfrak Q_\mu\) are effectively Turing-equivalent:

\[
\boxed{
\operatorname{Th}(\mathfrak M_\mu)
\equiv_T
\operatorname{Th}(\mathfrak Q_\mu).
}
\tag{14}
\]

More precisely:

1. \(\mathfrak Q_\mu\) is interpretable in \(\mathfrak M_\mu^{\mathrm{eq}}\);
2. every first-order sentence of \(\mathfrak M_\mu\) can be translated effectively to a sentence of \(\mathfrak Q_\mu\), using only finitely many predicates \(P_{\ge m}\).

### Proof

The first direction is immediate from the definable equivalence relation (8). Membership (10) is well defined on equivalence classes, and (11) is first-order definable by asking for \(m\) distinct external representatives in the same \(\sim\)-class. Hence the quotient structure is interpretable in imaginaries.

For the converse, consider a first-order formula of \(\mathfrak M_\mu\) involving at most \(k\) element variables. Split each quantified variable into the two cases “active” and “external.” An active variable becomes a variable of the \(S\)-sort of \(\mathfrak Q_\mu\). An external variable contributes:

- a quotient-class variable \(F\in\mathcal F_\mu\);
- equality information telling whether two external variables are the same representative inside a common fiber.

Incidence with active points is exactly quotient membership (10). If two external variables belong to distinct quotient classes, they are automatically distinct. If \(j\) distinct representatives of one quotient class are required, the condition is exactly

\[
P_{\ge j}(F).
\tag{15}
\]

Because the original formula has only \(k\) variables, no multiplicity threshold beyond \(k\) can be required. Thus the equality pattern of external representatives can be eliminated by a finite disjunction over partitions of the finitely many external variables, with the necessary fiber-size conditions expressed by predicates \(P_{\ge j}\), \(j\le k\).

This gives an effective translation to \(\mathfrak Q_\mu\). ∎

### Consequence 3.2

When the active skeleton is empty, **all first-order complexity is concentrated in the family of finite subsets that occur and in their multiplicities**. No residual active geometry remains.

---

## 4. Multiplicity alone can encode a nonrecursive set

The cleanest separation is obtained by keeping the quotient geometry completely fixed.

Let

\[
A\subseteq\mathbb N
\tag{16}
\]

be arbitrary. Define

\[
\mu_A(F)
=
\begin{cases}
2,&|F|\in A,\\
1,&|F|\notin A.
\end{cases}
\tag{17}
\]

Thus:

- **every** finite subset \(F\subseteq S\) occurs;
- the family of realized neighborhoods is always exactly \(\operatorname{Fin}(S)\), independently of \(A\);
- the active skeleton is always empty;
- the only variation is whether a given finite-neighborhood class has one or two external copies.

For each \(n\in\mathbb N\), let \(\operatorname{Deg}_n(x)\) be the first-order formula saying that \(x\) is external and has exactly \(n\) active neighbors. Explicitly, it asserts that there exist distinct active elements

\[
s_1,\dots,s_n
\]

such that

\[
R(x,s_i)
\qquad(1\le i\le n)
\tag{18}
\]

and

\[
\forall s
\bigl(
S(s)\land R(x,s)
\to
(s=s_1\lor\cdots\lor s=s_n)
\bigr).
\tag{19}
\]

Define the sentence

\[
\Theta_n
:\iff
\exists x\exists y
\bigl(
 x\ne y
\land
x\sim y
\land
\operatorname{Deg}_n(x)
\bigr).
\tag{20}
\]

### Theorem 4.1 — Pure Multiplicity Undecidability

For every \(A\subseteq\mathbb N\),

\[
\boxed{
\mathfrak M_{\mu_A}\models\Theta_n
\iff
n\in A.
}
\tag{21}
\]

Consequently, if \(A\) is nonrecursive, then

\[
\boxed{
\operatorname{Th}(\mathfrak M_{\mu_A})
\text{ is undecidable}.
}
\tag{22}
\]

### Proof

Fix \(n\).

If \(n\in A\), every finite set \(F\subseteq S\) of size \(n\) has

\[
\mu_A(F)=2.
\]

Choose one such \(F\) and its two distinct external copies \(x,y\in C_F\). Then \(x\sim y\), both have exactly \(n\) active neighbors, and \(\Theta_n\) holds.

If \(n\notin A\), every finite set \(F\) of size \(n\) has

\[
\mu_A(F)=1.
\]

Hence no two distinct external points with exactly \(n\) active neighbors can belong to the same \(\sim\)-class. Therefore \(\Theta_n\) fails.

Thus (21) holds. The map

\[
n\mapsto\Theta_n
\]

is effective, so

\[
A\le_m\operatorname{Th}(\mathfrak M_{\mu_A}).
\tag{23}
\]

If the complete theory were decidable, \(A\) would be recursive. ∎

### Conceptual conclusion

This proves the desired separation in the strongest elementary form:

\[
\boxed{
\text{geometry fixed}
+
\text{all finite neighborhoods realized}
+
\mu(F)\in\{1,2\}
}
\]

can already carry undecidability.

The wildness is therefore genuinely **multiplicity memory**, not hidden geometry.

---

## 5. Continuum many theories with identical empty geometry

### Corollary 5.1 — Continuum multiplicity spectrum

There are

\[
\boxed{2^{\aleph_0}}
\tag{24}

pairwise distinct complete first-order theories of empty-skeleton multiplicity models in which:

1. the active set is a countably infinite pure set;
2. every finite active subset occurs as an external neighborhood;
3. every neighborhood multiplicity is either \(1\) or \(2\).

### Proof

For each \(A\subseteq\mathbb N\), take \(\mathfrak M_{\mu_A}\). If \(A\ne B\), choose

\[
n\in A\triangle B.
\]

By Theorem 4.1, \(\Theta_n\) holds in exactly one of the two structures, so their complete theories differ. There are \(2^{\aleph_0}\) subsets of \(\mathbb N\), while a countable language has at most \(2^{\aleph_0}\) complete theories. ∎

---

## 6. A stronger graph-coding variant

Multiplicity support can encode not only a unary set but an arbitrary countable graph.

Let

\[
H=(S,E_H)
\tag{25}
\]

be a countable simple graph on the same active set. Define

\[
\nu_H(F)
=
\begin{cases}
1,&F=\{u,v\}\text{ with }u\ne v\text{ and }\{u,v\}\in E_H,\\
0,&|F|=2\text{ and }\{u,v\}\notin E_H,\\
0,&\text{otherwise}.
\end{cases}
\tag{26}
\]

Then adjacency is interpreted by

\[
\operatorname{Adj}_H(u,v)
\iff
u_H(\{u,v\})>0.
\tag{27}
\]

In the incidence structure this becomes

\[
\exists x
\bigl(
R(x,u)\land R(x,v)
\land
\forall s\,(S(s)\land R(x,s)\to(s=u\lor s=v))
\bigr).
\tag{28}
\]

Hence arbitrary graph theory can be placed entirely in the multiplicity support while the active skeleton remains empty.

This variant is not needed for Theorem 4.1 but shows that multiplicity memory is not merely unary-memory capable.

---

## 7. What the arithmetic Ramanujan reduct allows

Return now to an actual threshold profile \(\kappa\) with empty active skeleton.

For each source prime \(p\), define

\[
N_p=\tau(p)^2-p^{11}.
\tag{29}
\]

If \(\kappa\) is binary, then for an external prime \(p\notin S_\kappa\),

\[
N_\kappa(p)
=
S_\kappa\cap\operatorname{PrimeDiv}(N_p).
\tag{30}
\]

Since \(N_p\ne0\), this neighborhood is finite.

Thus an arithmetic multiplicity function has the special form

\[
\mu_\kappa(F)
=
\left|
\left\{
 p\notin S_\kappa:
 S_\kappa\cap\operatorname{PrimeDiv}(N_p)=F
\right\}
\right|.
\tag{31}
\]

For higher thresholds, the same statement is replaced by the valuation condition

\[
r\in N_\kappa(p)
\iff
v_r(N_p)\ge\kappa(r).
\tag{32}
\]

This is a severe global realization constraint absent from the abstract models of Sections 2–6.

---

## 8. What is easy arithmetically: lower multiplicity control

The earlier saturated-extension construction proves that with empty active skeleton one can force

\[
\mu_\kappa(F)=\aleph_0
\tag{33}
\]

for every finite \(F\subseteq S_\kappa\), while keeping the support arbitrarily sparse.

The reason is one-sided. Given a finite \(F\), finite-pattern realization supplies infinitely many candidate source primes. Once one witness \(p\) is chosen, its exact neighborhood can be protected by permanently forbidding every prime divisor of \(N_p\) outside the current support from entering the future support.

Thus **existence and arbitrary finite lower bounds are easy to protect**.

---

## 9. What is hard arithmetically: upper multiplicity control

To realize the abstract model \(\mu_A\) from (17), one would need not only to produce one or two protected witnesses for each finite \(F\), but also to ensure that **every other rational prime** fails to have final neighborhood \(F\).

That is an upper-bound problem.

For an unwanted prime \(p\), changing its final neighborhood requires either:

1. placing some additional divisor of \(N_p\) into the support; or
2. changing a threshold at an already active marker so that the divisibility status of \(p\) changes.

Neither operation is uniformly available while preserving an empty active skeleton and already protected witnesses.

In particular, the finite-pattern/Chebotarev theorem controls congruence behavior on a prescribed finite set of markers, but it does **not** provide a fresh prime divisor of a fixed integer \(N_p\). Therefore the previous local independence machinery does not solve the global capping problem.

### Definition 9.1 — Upper Multiplicity Control Problem

Given an empty active skeleton and a finite set \(F\subseteq S\), determine whether one can force

\[
\mu_\kappa(F)\le m
\tag{34}
\]

for a prescribed finite \(m\), while retaining prescribed exact neighborhoods elsewhere.

This is the first unresolved step needed to realize the pure multiplicity models of Theorem 4.1 inside the Ramanujan threshold family.

---

## 10. A necessary trace-density condition

Although exact arithmetic realizability remains open, one universal necessary condition is immediate from finite-pattern realization.

Let

\[
\mathcal R_\kappa
=
\{F\in\operatorname{Fin}(S_\kappa):\mu_\kappa(F)>0\}
\tag{35}
\]

be the realized-neighborhood family.

### Proposition 10.1 — Cylinder density of realized neighborhoods

Assume the active markers under consideration lie outside the fixed finite exceptional set for residual pattern realization. For every finite

\[
R\subseteq S_\kappa
\tag{36}
\]

and every

\[
T\subseteq R,
\tag{37}
\]

there exists some realized finite neighborhood

\[
F\in\mathcal R_\kappa
\tag{38}
\]

such that

\[
F\cap R=T.
\tag{39}
\]

### Proof

Finite-pattern realization supplies a source prime \(p\) whose incidence with the finite marker set \(R\) is exactly \(T\). Its full active neighborhood \(F=N_\kappa(p)\) is finite by local finiteness, and by construction satisfies (39). If the chosen source happens to lie in the support, choose instead one of the infinitely many realizing primes outside the finite set \(R\); the realization theorem supplies infinitely many choices. ∎

Thus \(\mathcal R_\kappa\) is dense in the finite-cylinder topology on finite subsets.

### Remark 10.2

The abstract family in Theorem 4.1 realizes **every** finite subset, so it satisfies this necessary trace-density condition maximally. Therefore Proposition 10.1 does not rule out arithmetic realization of the \(1/2\)-multiplicity models.

---

## 11. Exact separation achieved at the model-theoretic level

The results can now be organized cleanly.

### Geometric memory

The active skeleton

\[
G_\kappa
\tag{40}
\]

can itself encode arbitrary backward-DAG complexity, as proved in the fourth strike.

### Multiplicity memory

Even when

\[
G=\varnothing
\tag{41}
\]

and the quotient family of finite neighborhoods is fixed to all of \(\operatorname{Fin}(S)\), the multiplicity function alone can encode a nonrecursive set through

\[
\mu_A(F)\in\{1,2\}.
\tag{42}
\]

Therefore:

\[
\boxed{
\text{geometric memory and multiplicity memory are logically independent sources of wildness.}
}
\tag{43}
\]

This is a theorem about the exact locally finite normal-form class.

For the original Ramanujan threshold family, only the geometric side is currently known to be arithmetically programmable with full upper control. The multiplicity side is known to admit arbitrary lower saturation, but finite upper control is open.

---

## 12. New frontier

The next problem is no longer whether multiplicity can in principle cause undecidability. It can.

The next problem is the arithmetic realization question:

> **Ramanujan Multiplicity Realization Problem.**  
> Does there exist a threshold profile \(\kappa\) with empty active skeleton such that the induced multiplicity quotient \(\mathfrak Q_{\mu_\kappa}\) has undecidable theory?

A particularly sharp target is:

\[
\boxed{
G_\kappa=\varnothing,
\qquad
\operatorname{Th}(\mathcal I_\kappa)\text{ undecidable}.
}
\tag{44}
\]

A still sharper finite-cap target is to realize, for some nonrecursive \(A\subseteq\mathbb N\),

\[
\mu_\kappa(F)
=
\begin{cases}
2,&|F|\in A,\\
1,&|F|\notin A.
\end{cases}
\tag{45}
\]

or any weaker first-order coding of \(A\) using only multiplicity thresholds.

The obstruction is now precisely named:

\[
\boxed{
\textbf{Upper Multiplicity Control Barrier}.
}
\tag{46}
\]

---

## 13. Claim boundary

This checkpoint proves:

- exact reduction of empty-skeleton first-order complexity to finite-neighborhood multiplicity data;
- pure multiplicity undecidability in the abstract locally finite normal-form class;
- continuum many complete theories with identical empty geometry and only multiplicities \(1\) or \(2\);
- a necessary trace-density condition for actual arithmetic profiles;
- identification of finite upper multiplicity control as the missing arithmetic step.

It does **not** prove:

- existence of an actual Ramanujan threshold profile with empty active skeleton and undecidable prime-only theory;
- realization of arbitrary multiplicity functions by threshold profiles;
- finite upper control of \(\mu_\kappa(F)\);
- that trace-density is sufficient for arithmetic realizability;
- an exact elementary-equivalence criterion for all multiplicity functions.

---

## 14. Hostile audit

1. **Is the undecidability secretly coming from active geometry?**  
   No. The active skeleton is identically empty in every \(\mathfrak M_{\mu_A}\).

2. **Is the realized-neighborhood family changing with \(A\)?**  
   No. Every finite subset of \(S\) is realized for every \(A\). Only multiplicity changes from one copy to two copies.

3. **Does the reduction require naming a finite subset parameter?**  
   No. \(\Theta_n\) merely asks for two distinct twins with exactly \(n\) active neighbors; the finite neighborhood is existentially quantified.

4. **Can \(\Theta_n\) accidentally hold through two different neighborhoods of size \(n\)?**  
   No. The formula includes \(x\sim y\), requiring equality of the entire active neighborhood.

5. **Is multiplicity larger than two needed?**  
   No. The whole reduction uses only the values \(1\) and \(2\).

6. **Does Theorem 3.1 need infinitely many multiplicity predicates in one translated formula?**  
   No. A formula with \(k\) variables needs only \(P_{\ge j}\) for \(j\le k\).

7. **Was abstract realizability confused with arithmetic realizability?**  
   No. Sections 7–13 explicitly separate the two questions.

8. **Does Chebotarev already solve upper multiplicity control?**  
   No. It gives infinitely many realizers of finite coordinate patterns; it does not provide a mechanism for eliminating all unwanted exact full-neighborhood realizers.

9. **Does the abstract \(1/2\)-multiplicity family violate the known cylinder-density constraint?**  
   No. It realizes every finite subset and therefore satisfies cylinder density maximally.

**Audit verdict:** the abstract multiplicity-memory theorems are proved. The Ramanujan arithmetic realization question remains genuinely open and is not promoted to theorem.
