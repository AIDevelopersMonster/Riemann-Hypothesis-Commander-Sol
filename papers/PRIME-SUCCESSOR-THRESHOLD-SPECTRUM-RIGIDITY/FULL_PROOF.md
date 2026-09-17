# Full Proof — Threshold Spectrum Rigidity and Gauge Fixing

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/threshold-spectrum-rigidity`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-28  
**Status:** complete proof checkpoint

## 0. Purpose

This file supplies the complete proofs missing from the initial research checkpoint. Nothing below is assigned theorem status merely because it is plausible: every displayed theorem is proved in this file.

The central result is

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
=
\operatorname{Th}(\mathcal V_{\Delta,\lambda})
\iff
\kappa=\lambda.
\]

The proof is elementary once one identifies the correct calibration mechanism. In particular, the earlier two-prime Bezout construction is unnecessary: the single bridge value \(u_2=-23/32\) already parameter-free defines the target element \(1\).

A second theorem explains why the Ramanujan bridge matters. If the bridge is removed, the target additive sort has a rational-scaling gauge symmetry, and profiles differing at finitely many primes become isomorphic. The bridge fixes this gauge.

---

## 1. Language and structures

Let the source sort be

\[
S=(\mathbb N_{>0},\times,1),
\]

and the target sort be

\[
T=(\mathbb Q,+,0).
\]

For every profile

\[
\kappa:\mathbb P\to\mathbb N_0,
\]

define

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge\kappa(r).
\]

For the Ramanujan bridge put

\[
U_\Delta(p,x)
\iff
\operatorname{Prime}(p)\land x=u_p,
\]

where

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

The anchored threshold structure is

\[
\mathcal V_{\Delta,\kappa}
=
(S,T,U_\Delta,B_\kappa).
\]

The unanchored threshold structure is

\[
\mathcal W_\kappa
=
(S,T,B_\kappa).
\]

All anchored structures are considered in one common first-order language whose binary predicate symbol \(B\) is interpreted as \(B_\kappa\).

For a fixed positive integer \(n\), the expression \(nx\) is merely shorthand for the fixed target term

\[
\underbrace{x+\cdots+x}_{n\text{ times}}.
\]

No variable source-to-target scalar multiplication is present or used.

---

## 2. Fixed source primes are parameter-free definable

Recall that primality is first-order definable in \((\mathbb N_{>0},\times,1)\):

\[
\operatorname{Prime}(r)
:\iff
r\ne1\land
\forall a\forall b\,(r=ab\to(a=1\lor b=1)).
\]

Fix an ordinary standard prime \(\ell\). Define

\[
\Theta_\ell(r)
:\iff
\operatorname{Prime}(r)
\land
\exists x\,
\bigl(
\neg B(r,x)
\land
B(r,\ell x)
\bigr).
\]

### Lemma 2.1 — Fixed-prime calibration

In every threshold structure, anchored or unanchored,

\[
\Theta_\ell(r)
\iff
r=\ell.
\]

### Proof

Assume first that \(r\ne\ell\). Since \(\ell\) is an \(r\)-adic unit,

\[
v_r(\ell x)=v_r(x)
\]

for every nonzero rational \(x\), and the equality is also harmless at \(x=0\). Consequently

\[
B_\kappa(r,\ell x)
\iff
B_\kappa(r,x),
\]

so the conjunction

\[
\neg B(r,x)\land B(r,\ell x)
\]

is impossible.

Now let \(r=\ell\). Choose

\[
x=\ell^{\kappa(\ell)-1}\in\mathbb Q.
\]

This notation is valid also when \(\kappa(\ell)=0\), in which case \(x=\ell^{-1}\). Then

\[
v_\ell(x)=\kappa(\ell)-1<\kappa(\ell),
\]

while

\[
v_\ell(\ell x)=\kappa(\ell).
\]

Hence

\[
\neg B_\kappa(\ell,x)
\land
B_\kappa(\ell,\ell x)
\]

holds. Therefore \(\Theta_\ell\) defines exactly the source prime \(\ell\). ∎

### Consequence 2.2

Every fixed standard prime is parameter-free definable uniformly across the entire profile family. The defining formula depends on the chosen standard prime \(\ell\), but not on the unknown value \(\kappa(\ell)\).

---

## 3. One Ramanujan bridge value fixes the target scale

The Fourier expansion of the discriminant form begins

\[
\Delta(q)=q-24q^2+252q^3-1472q^4+4830q^5-\cdots,
\]

so

\[
\tau(2)=-24.
\]

Hence

\[
u_2
=
\frac{(-24)^2-2^{11}}{2^{11}}
=
\frac{576-2048}{2048}
=
-\frac{23}{32}.
\]

By Lemma 2.1, the source prime \(2\) is parameter-free definable by \(\Theta_2\). Therefore the bridge relation parameter-free defines the unique target value \(u_2\).

Define \(\operatorname{One}(z)\) by the first-order formula

\[
\exists r\exists x\,
\bigl(
\Theta_2(r)
\land
U_\Delta(r,x)
\land
23z+32x=0
\bigr).
\]

The equation uses only fixed repeated-addition terms.

### Lemma 3.1 — Uniform target-unit definability

For every threshold profile \(\kappa\),

\[
\mathcal V_{\Delta,\kappa}\models\operatorname{One}(z)
\iff
z=1.
\]

### Proof

The first two conjuncts force

\[
r=2,
\qquad
x=u_2=-\frac{23}{32}.
\]

The remaining equation is

\[
23z+32\left(-\frac{23}{32}\right)=0,
\]

hence

\[
23z-23=0.
\]

The additive group of \(\mathbb Q\) is torsion-free, so this equation has the unique solution

\[
z=1.
\]

Thus \(1\) is parameter-free definable by one formula independent of \(\kappa\). ∎

### Remark 3.2 — Proof simplification

An earlier checkpoint used both \(u_2\) and \(u_5\) and an explicit Bezout identity. That construction is correct but unnecessary. Because the target sort is divisible and torsion-free, the single nonzero rational bridge label \(u_2=-23/32\) already fixes the target scale.

---

## 4. Every fixed rational is parameter-free definable

Once \(1\) is definable in \((\mathbb Q,+,0)\), every fixed rational number becomes parameter-free definable.

Let

\[
q=\frac{a}{b}\in\mathbb Q,
\qquad
b>0,
\]

with fixed integers \(a,b\).

If \(a\ge0\), define \(q\) by

\[
bx=a\cdot1.
\]

If \(a<0\), equivalently define \(q\) by

\[
bx+(-a)\cdot1=0.
\]

The equation has a unique solution because \(\mathbb Q\) is divisible and torsion-free.

### Lemma 4.1 — Fixed-rational definability

For every fixed \(q\in\mathbb Q\), there is a parameter-free formula \(Q_q(x)\), independent of \(\kappa\), such that

\[
\mathcal V_{\Delta,\kappa}\models Q_q(x)
\iff
x=q.
\]

### Proof

Use Lemma 3.1 to define the unique target element \(1\), and then use one of the preceding fixed integer equations. Existence and uniqueness follow from divisibility and torsion-freeness of \((\mathbb Q,+,0)\). ∎

---

## 5. Fixed valuation probes

Fix a standard prime \(\ell\) and an integer \(t\in\mathbb Z\). Define

\[
q_{\ell,t}=\ell^t\in\mathbb Q.
\]

By Lemma 4.1, this rational is parameter-free definable. It satisfies

\[
v_\ell(q_{\ell,t})=t.
\]

For later syntactic use, let \(Q_{\ell,t}(x)\) be any fixed parameter-free formula defining \(q_{\ell,t}\).

No variable exponentiation is being introduced: \(\ell\) and \(t\) are fixed metamathematical indices of the formula.

---

## 6. A sentence detecting one exact threshold coordinate

Fix a standard prime \(\ell\) and \(m\in\mathbb N_0\). Define the parameter-free sentence

\[
\Sigma_{\ell,m}
\]

as

\[
\exists r\exists x\exists y\,
\Bigl(
\Theta_\ell(r)
\land
Q_{\ell,m}(x)
\land
Q_{\ell,m-1}(y)
\land
B(r,x)
\land
\neg B(r,y)
\Bigr).
\]

The case \(m=0\) uses the fixed rational \(\ell^{-1}\), which is definable by Lemma 4.1.

### Lemma 6.1 — Exact coordinate decoding

For every threshold profile \(\kappa\),

\[
\boxed{
\mathcal V_{\Delta,\kappa}\models\Sigma_{\ell,m}
\iff
\kappa(\ell)=m.
}
\]

### Proof

The first three conjuncts force

\[
r=\ell,
\qquad
x=\ell^m,
\qquad
y=\ell^{m-1}.
\]

Therefore

\[
B_\kappa(r,x)
\iff
m\ge\kappa(\ell),
\]

and

\[
\neg B_\kappa(r,y)
\iff
m-1<\kappa(\ell).
\]

Since \(\kappa(\ell)\) is an integer, the conjunction is equivalent to

\[
\kappa(\ell)=m.
\]

This includes \(m=0\): then the two inequalities read

\[
0\ge\kappa(\ell)
\quad\text{and}\quad
-1<\kappa(\ell),
\]

which, because \(\kappa(\ell)\in\mathbb N_0\), are equivalent to \(\kappa(\ell)=0\). ∎

---

## 7. Threshold Spectrum Rigidity

### Theorem 7.1 — Pointwise Threshold Recovery

For each fixed standard prime \(\ell\), the complete parameter-free first-order theory of \(\mathcal V_{\Delta,\kappa}\) determines the exact integer \(\kappa(\ell)\).

### Proof

Exactly one sentence in the family

\[
\{\Sigma_{\ell,m}:m\in\mathbb N_0\}
\]

is true, namely \(\Sigma_{\ell,\kappa(\ell)}\), by Lemma 6.1. ∎

### Theorem 7.2 — Threshold Spectrum Rigidity

For arbitrary profiles

\[
\kappa,\lambda:\mathbb P\to\mathbb N_0,
\]

we have

\[
\boxed{
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
=
\operatorname{Th}(\mathcal V_{\Delta,\lambda})
\iff
\kappa=\lambda.
}
\]

### Proof

If \(\kappa=\lambda\), the structures have identical interpretations of every symbol, so their theories are equal.

Conversely suppose \(\kappa\ne\lambda\). Choose a standard prime \(\ell\) such that

\[
\kappa(\ell)\ne\lambda(\ell).
\]

Put

\[
m=\kappa(\ell).
\]

By Lemma 6.1,

\[
\mathcal V_{\Delta,\kappa}\models\Sigma_{\ell,m},
\]

whereas

\[
\mathcal V_{\Delta,\lambda}\not\models\Sigma_{\ell,m}.
\]

Thus the complete theories differ. ∎

### Corollary 7.3

Different threshold profiles give non-elementarily-equivalent anchored structures and therefore, a fortiori, non-isomorphic anchored structures.

---

## 8. Continuum many complete theories at fixed support and depth alphabet

Enumerate the primes as

\[
\mathbb P=\{p_0,p_1,p_2,\dots\}.
\]

For every subset \(A\subseteq\mathbb N\), define

\[
\kappa_A(p_i)
=
\begin{cases}
1,&i\in A,\\
2,&i\notin A.
\end{cases}
\]

Then

\[
P_+(\kappa_A)=\mathbb P
\]

for every \(A\), and every threshold value lies in \(\{1,2\}\).

If \(A\ne A'\), then \(\kappa_A\ne\kappa_{A'}\), so Theorem 7.2 gives

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa_A})
\ne
\operatorname{Th}(\mathcal V_{\Delta,\kappa_{A'}}).
\]

There are \(2^{\aleph_0}\) subsets of \(\mathbb N\).

### Corollary 8.1 — Continuum spectrum in one macroscopic phase

There are exactly continuum many pairwise distinct complete theories among anchored threshold structures satisfying simultaneously

\[
P_+(\kappa)=\mathbb P
\]

and

\[
\kappa(r)\in\{1,2\}
\qquad(r\in\mathbb P).
\]

The lower bound is the construction above. The upper bound follows because the language is countable, hence there are at most continuum many complete theories in that language. ∎

By the published Support-Cardinality Valuation Wall theorem, every structure in this family lies in the same GIR-infinite, finite-graph-universal, undecidable macroscopic phase. Therefore the macroscopic phase does not determine the complete theory.

---

## 9. Effective information recovery

The pointwise proof gives more than cardinality.

Fix a computable enumeration

\[
p_0,p_1,p_2,\dots
\]

of the ordinary primes and again let

\[
\kappa_A(p_i)=1
\iff
i\in A,
\]

with value \(2\) otherwise.

The map

\[
i\longmapsto \ulcorner\Sigma_{p_i,1}\urcorner
\]

from \(i\) to a Gödel code of the corresponding sentence is computable: given the standard prime \(p_i\), the finite formulas \(\Theta_{p_i}\), \(Q_{p_i,1}\), and \(Q_{p_i,0}\) can be written down effectively.

Moreover

\[
i\in A
\iff
\Sigma_{p_i,1}
\in
\operatorname{Th}(\mathcal V_{\Delta,\kappa_A}).
\]

### Proposition 9.1 — Spectrum information lower bound

For every \(A\subseteq\mathbb N\),

\[
A\le_m
\operatorname{Th}(\mathcal V_{\Delta,\kappa_A}),
\]

where \(\le_m\) denotes many-one reducibility after fixing a standard effective coding of first-order sentences.

### Proof

Use the computable map

\[
i\mapsto\ulcorner\Sigma_{p_i,1}\urcorner.
\]

Its correctness is exactly Lemma 6.1. ∎

This is only a lower bound. No claim is made that the complete theory has exactly the Turing degree of \(A\).

---

## 10. Abstract scale-anchor principle

The preceding proof uses very little special arithmetic after the target scale has been fixed.

### Theorem 10.1 — Abstract Threshold Calibration

Consider any two-sorted structure with source \((\mathbb N_{>0},\times,1)\), target \((\mathbb Q,+,0)\), and a threshold predicate

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge\kappa(r).
\]

Assume additionally that the target element \(1\in\mathbb Q\) is parameter-free definable by a formula independent of \(\kappa\).

Then the complete theory determines \(\kappa\) pointwise, and two different profiles have different complete theories.

### Proof

Lemma 2.1 uses only \(B_\kappa\) and fixed integer scalar terms, so every fixed source prime \(\ell\) is parameter-free definable. Once target \(1\) is parameter-free definable, Lemmas 4.1, 5, and 6.1 apply verbatim. Hence each \(\kappa(\ell)\) is detected by the sentence \(\Sigma_{\ell,m}\). Theorem 7.2 follows. ∎

Thus the role of the Ramanujan bridge in Threshold Spectrum Rigidity is to provide a parameter-free **scale anchor**. The residual Galois machinery from the Support-Cardinality Wall is not needed for this rigidity theorem.

---

## 11. What happens without the bridge: a gauge symmetry

Remove \(U_\Delta\) and consider

\[
\mathcal W_\kappa
=
\bigl(
(\mathbb N_{>0},\times,1),
(\mathbb Q,+,0),
B_\kappa
\bigr).
\]

For a prime \(p\) and integer \(a\), write

\[
H_{p,a}
=
\{x\in\mathbb Q:v_p(x)\ge a\}.
\]

We first record two elementary facts.

### Lemma 11.1 — Automorphisms of the additive rationals

Every automorphism

\[
f:(\mathbb Q,+,0)\to(\mathbb Q,+,0)
\]

has the form

\[
f(x)=cx
\]

for a unique \(c\in\mathbb Q^\times\).

### Proof

Set \(c=f(1)\ne0\). For integers \(n\), additivity gives

\[
f(n)=nc.
\]

For a rational \(a/b\), the element \(f(a/b)\) is the unique solution \(y\) of

\[
by=ac,
\]

because \((\mathbb Q,+)\) is torsion-free and divisible. Hence

\[
f(a/b)=c(a/b).
\]

Uniqueness of \(c\) is immediate from \(c=f(1)\). ∎

### Lemma 11.2 — Different valuation places give different threshold subgroups

If \(p\ne q\) are primes and \(a,b\in\mathbb Z\), then

\[
H_{p,a}\ne H_{q,b}.
\]

### Proof

Take

\[
x=p^a q^{b-1}.
\]

Then

\[
v_p(x)=a,
\qquad
v_q(x)=b-1.
\]

Thus

\[
x\in H_{p,a}
\quad\text{but}\quad
x\notin H_{q,b}.
\]

So the subgroups are different. ∎

For the same prime, the chain is strict:

\[
H_{p,a+1}\subsetneq H_{p,a},
\]

since \(p^a\in H_{p,a}\setminus H_{p,a+1}\).

### Theorem 11.3 — Unanchored gauge classification up to isomorphism

For profiles \(\kappa,\lambda:\mathbb P\to\mathbb N_0\),

\[
\boxed{
\mathcal W_\kappa\cong\mathcal W_\lambda
\iff
\{p:\kappa(p)\ne\lambda(p)\}
\text{ is finite}.
}
\]

More precisely, every isomorphism has identity source action and target action

\[
x\mapsto cx
\]

for some \(c\in\mathbb Q^\times\), with

\[
\boxed{
\lambda(p)=\kappa(p)+v_p(c)
\qquad(p\in\mathbb P).
}
\]

### Proof

#### Necessity

Let

\[
F:\mathcal W_\kappa\to\mathcal W_\lambda
\]

be an isomorphism. Write its source and target components as \(F_S\) and \(F_T\).

By Lemma 11.1 there is \(c\in\mathbb Q^\times\) such that

\[
F_T(x)=cx.
\]

Let \(p\) be a source prime and put

\[
q=F_S(p).
\]

Because source isomorphisms preserve primality, \(q\) is prime. Preservation of \(B\) gives, for every \(x\in\mathbb Q\),

\[
v_p(x)\ge\kappa(p)
\iff
v_q(cx)\ge\lambda(q).
\]

Equivalently,

\[
x\in H_{p,\kappa(p)}
\iff
x\in H_{q,\lambda(q)-v_q(c)}.
\]

Hence

\[
H_{p,\kappa(p)}
=
H_{q,\lambda(q)-v_q(c)}.
\]

Lemma 11.2 forces

\[
q=p.
\]

Therefore every source prime is fixed by \(F_S\). Since every positive integer is a finite product of primes, \(F_S\) is the identity on the whole source sort.

We now have

\[
H_{p,\kappa(p)}
=
H_{p,\lambda(p)-v_p(c)}.
\]

Strictness of the \(p\)-adic threshold chain implies equality of the indices:

\[
\kappa(p)=\lambda(p)-v_p(c).
\]

Thus

\[
\lambda(p)=\kappa(p)+v_p(c).
\]

A nonzero rational has nonzero valuation at only finitely many primes. Hence \(\kappa\) and \(\lambda\) differ at only finitely many primes.

#### Sufficiency

Conversely suppose

\[
D=\{p:\kappa(p)\ne\lambda(p)\}
\]

is finite. Set

\[
c=
\prod_{p\in D}p^{\lambda(p)-\kappa(p)}
\in\mathbb Q^\times.
\]

Then for every prime \(p\),

\[
v_p(c)=\lambda(p)-\kappa(p).
\]

Define \(F_S\) to be the identity and

\[
F_T(x)=cx.
\]

For every prime \(p\) and rational \(x\),

\[
B_\lambda(p,cx)
\iff
v_p(x)+v_p(c)\ge\lambda(p)
\]

\[
\iff
v_p(x)+\lambda(p)-\kappa(p)\ge\lambda(p)
\]

\[
\iff
v_p(x)\ge\kappa(p)
\iff
B_\kappa(p,x).
\]

Thus \((F_S,F_T)\) is an isomorphism. ∎

### Corollary 11.4 — Finite profile changes are a gauge without an anchor

In the unanchored language, changing finitely many threshold values does not merely preserve a coarse phase: it yields an isomorphic structure.

---

## 12. The Ramanujan bridge fixes the gauge

The preceding theorem exposes the conceptual role of \(U_\Delta\).

Suppose an isomorphism between anchored structures had target component

\[
x\mapsto cx.
\]

Lemma 2.1 makes the source prime \(2\) parameter-free definable, so any isomorphism fixes it. The bridge must therefore send the unique label \(u_2\) to itself:

\[
cu_2=u_2.
\]

Since

\[
u_2=-\frac{23}{32}\ne0,
\]

we get

\[
c=1.
\]

Hence the rational-scaling gauge is completely removed.

### Proposition 12.1 — Bridge gauge fixing

The Ramanujan bridge kills every nontrivial rational scaling automorphism of the target sort compatible with the full anchored structure.

### Proof

As above, compatibility with the fixed bridge value \(u_2\ne0\) forces \(c=1\). ∎

This explains the contrast:

\[
\mathcal W_\kappa\cong\mathcal W_\lambda
\quad\text{for every finite profile difference},
\]

whereas in the anchored family

\[
\kappa\ne\lambda
\Longrightarrow
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
e
\operatorname{Th}(\mathcal V_{\Delta,\lambda}).
\]

The bridge does not merely transmit residual data. It also provides an absolute target scale.

---

## 13. Relation to the Support-Cardinality Wall

There is no contradiction between the following two established facts.

1. If \(P_+(\kappa)\) is finite, then \(\mathcal V_{\Delta,\kappa}\) is parameter-free interdefinable with \(\mathcal V_{\Delta,0}\).
2. If \(\kappa\ne0\), then \(\operatorname{Th}(\mathcal V_{\Delta,\kappa})\ne\operatorname{Th}(\mathcal V_{\Delta,0})\).

Interdefinability allows one predicate to be translated into a formula of the other structure. Equality of complete theories in the same literal language would require the original predicate symbol \(B\) itself to have the same first-order behavior. The calibration sentences \(\Sigma_{\ell,m}\) distinguish those interpretations.

Thus the two results live at different scales:

\[
\boxed{
\text{macroscopic phase}
=
\text{finite/infinite positive support}
}
\]

and

\[
\boxed{
\text{microscopic elementary spectrum}
=
\text{exact anchored profile }\kappa.
}
\]

---

## 14. What remains open

The present proofs close **theory-level pointwise recovery**. They do not solve **uniform internal profile reconstruction**.

For every fixed standard pair \((\ell,m)\), we have a sentence

\[
\Sigma_{\ell,m}
\]

detecting \(\kappa(\ell)=m\). This is a countable external family of formulas.

What is not proved is the existence of one internal formula with a variable prime argument and a variable numerical depth argument that reconstructs the whole graph of \(\kappa\). The language still contains no known variable source-to-target numerical transport map

\[
J(r,z)\iff z=r.
\]

That problem is logically distinct from Threshold Spectrum Rigidity and should be treated as a separate research front rather than smuggled into the theorem proved here.

---

## 15. Proof verdict

The central candidate from the initial checkpoint is now fully proved.

Proved in this file:

1. fixed-prime parameter-free definability;
2. one-prime target-scale calibration using \(u_2\);
3. parameter-free definability of every fixed rational;
4. exact threshold-coordinate sentences \(\Sigma_{\ell,m}\);
5. Pointwise Threshold Recovery;
6. Threshold Spectrum Rigidity;
7. continuum many distinct complete theories at fixed full support and thresholds \(\{1,2\}\);
8. a many-one lower bound recovering arbitrary subset information from the complete theory;
9. the abstract scale-anchor theorem;
10. exact isomorphism classification of the unanchored profile family;
11. bridge gauge fixing.

A separate hostile audit must still attempt to break these proofs before publication status is assigned.