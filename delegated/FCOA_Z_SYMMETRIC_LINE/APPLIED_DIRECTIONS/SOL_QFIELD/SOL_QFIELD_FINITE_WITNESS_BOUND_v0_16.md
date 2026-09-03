# SOL-QFIELD — Constructive Finite Witness Bound for Parikh Collisions

**Version:** 0.16  
**Date:** 2026-09-03  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** CONSTRUCTIVE FINITE-DEPTH THEOREM PROVED / GENERAL COLLISION THEOREM MADE EFFECTIVE  
**Depends on:** `SOL_QFIELD_PARIKH_ABELIANIZATION_v0_15.md`

---

## 1. Executive verdict

Version 0.15 proved that for a monoid-surjective history morphism

\[
h:\Sigma^*\twoheadrightarrow G
\]

into a group,

\[
g\sim_P g'
\iff
g^{-1}g'\in [G,G].
\]

For finite groups this existence theorem can be made completely constructive.

Let

\[
S=h(\Sigma)\subseteq G,
\qquad
H=[G,G].
\]

Let \(\delta_+(G,S)\) be the directed diameter of the positive Cayley digraph of \(G\) with respect to \(S\): every \(x\in G\) has a positive representative of length at most \(\delta_+\).

Let

\[
\mathcal C
=
\left\{
 x c_{ij}^{\pm1}x^{-1}:
 x\in G,\ i,j
\right\}
\]

where

\[
c_{ij}:=(g_i g_j)^{-1}(g_j g_i),
\qquad g_i=h(a_i).
\]

The set \(\mathcal C\) is a symmetric generating set of \(H\). Let

\[
\delta_H:=\operatorname{diam}\operatorname{Cay}(H,\mathcal C).
\]

Then every colliding pair \(g\sim_P g'\) admits Parikh-equivalent witnesses of common length at most

\[
\boxed{
B(h)
\le
\delta_+
+
\delta_H(2\delta_++2).
}
\]

Since for finite \(G\)

\[
\delta_+\le |G|-1,
\qquad
\delta_H\le |H|-1,
\]

one obtains the explicit group-size bound

\[
\boxed{
B(h)
\le
|G|-1+2|G|(|[G,G]|-1).
}
\]

In particular,

\[
\boxed{
B(h)<2|G|^2.
}
\]

Thus the general Parikh-collision theorem is not merely existential: for every finite history quotient, all collision classes are witnessed at a uniformly bounded finite depth that is at worst quadratic in the group order.

The bound is intentionally conservative. For \(S_3\), the sharp universal depth is \(5\), while the general theorem gives a much larger number. The point of v0.16 is universality and constructivity, not sharpness.

---

## 2. Positive word diameter

Let

\[
S=\{g_i:h(a_i)=g_i\}.
\]

Because \(G\) is finite and the letter images generate \(G\) as a group, they generate \(G\) as a monoid. Hence the directed Cayley graph

\[
\operatorname{Cay}^+(G,S)
\]

is strongly connected.

Define

\[
\delta_+
:=
\max_{x\in G}\ell_+(x),
\]

where \(\ell_+(x)\) is the shortest length of a positive word representing \(x\).

### Lemma 2.1

\[
\boxed{
\delta_+\le |G|-1.
}
\]

### Proof

A shortest directed path from the identity to any vertex cannot repeat a vertex. Therefore it has at most \(|G|-1\) edges. \(\square\)

---

## 3. Basic Parikh commutator seeds

For letters \(a_i,a_j\), the two words

\[
a_i a_j,
\qquad
a_j a_i
\]

have the same Parikh vector.

Put

\[
\alpha_{ij}:=g_i g_j,
\qquad
\beta_{ij}:=g_j g_i,
\]

and

\[
c_{ij}:=\alpha_{ij}^{-1}\beta_{ij}.
\]

The normal closure of all \(c_{ij}\) is exactly \(H=[G,G]\).

The first task is to produce short **normalized** Parikh witnesses for conjugates of \(c_{ij}\).

---

## 4. Lemma A — short normalized conjugate witness

### Lemma 4.1

For every \(x\in G\), every pair \(i,j\), and either sign \(\varepsilon\in\{\pm1\}\), there exist Parikh-equivalent words \(U,V\) with

\[
h(U)=e,
\qquad
h(V)=x c_{ij}^{\varepsilon}x^{-1},
\]

and

\[
\boxed{
|U|=|V|\le 2\delta_++2.
}
\]

### Proof

First take \(\varepsilon=+1\).

Choose a positive word \(y\) with

\[
h(y)=x^{-1},
\qquad
|y|\le\delta_+.
\]

Choose a positive word \(z\) with

\[
h(z)=x\alpha_{ij}^{-1},
\qquad
|z|\le\delta_+.
\]

Set

\[
U:=z\,a_i a_j\,y,
\qquad
V:=z\,a_j a_i\,y.
\]

They have the same Parikh vector, because they differ only by swapping the adjacent letters \(a_i,a_j\).

Their images are

\[
h(U)
=x\alpha_{ij}^{-1}\alpha_{ij}x^{-1}
=e,
\]

and

\[
h(V)
=x\alpha_{ij}^{-1}\beta_{ij}x^{-1}
=xc_{ij}x^{-1}.
\]

Moreover

\[
|U|=|V|\le\delta_++2+\delta_+.
\]

For \(\varepsilon=-1\), interchange the two seed words and use \(\beta_{ij}^{-1}\) in the same construction. \(\square\)

---

## 5. Normal commutator generating set

Define

\[
\mathcal C
:=
\left\{
xc_{ij}^{\pm1}x^{-1}:
 x\in G,\ i,j
\right\}.
\]

Then \(\mathcal C\) is symmetric and generates \(H=[G,G]\).

Let

\[
\delta_H
:=
\operatorname{diam}\operatorname{Cay}(H,\mathcal C).
\]

Because this is a connected undirected Cayley graph on \(|H|\) vertices,

\[
\boxed{
\delta_H\le |H|-1.
}
\]

Thus every \(d\in H\) admits a factorization

\[
d=d_1d_2\cdots d_t,
\qquad
d_r\in\mathcal C,
\qquad
t\le\delta_H.
\]

---

## 6. Lemma B — short normalized witness for every derived element

### Lemma 6.1

For every \(d\in H\), there exist Parikh-equivalent words \(U_d,V_d\) such that

\[
h(U_d)=e,
\qquad
h(V_d)=d,
\]

and

\[
\boxed{
|U_d|=|V_d|
\le
\delta_H(2\delta_++2).
}
\]

### Proof

Write

\[
d=d_1\cdots d_t,
\qquad t\le\delta_H,
\]

with \(d_r\in\mathcal C\).

By Lemma 4.1, for each \(d_r\) choose Parikh-equivalent normalized witnesses

\[
U_r\equiv_PV_r,
\qquad
h(U_r)=e,
\qquad
h(V_r)=d_r,
\]

with length at most \(2\delta_++2\).

Now concatenate:

\[
U_d:=U_1U_2\cdots U_t,
\qquad
V_d:=V_1V_2\cdots V_t.
\]

Parikh equivalence is additive under concatenation, so

\[
U_d\equiv_PV_d.
\]

Also

\[
h(U_d)=e,
\qquad
h(V_d)=d_1\cdots d_t=d.
\]

The claimed length bound follows. \(\square\)

---

## 7. Theorem A — constructive collision-depth bound

### Theorem 7.1

Let \(G\) be finite and

\[
h:\Sigma^*\twoheadrightarrow G
\]

be a monoid-surjective history morphism.

For every pair

\[
g\sim_Pg',
\]

there exist Parikh-equivalent words \(W,W'\) with

\[
h(W)=g,
\qquad
h(W')=g',
\]

and

\[
\boxed{
|W|=|W'|
\le
\delta_+
+
\delta_H(2\delta_++2).
}
\]

### Proof

By v0.15,

\[
d:=g^{-1}g'\in H.
\]

Choose normalized witnesses \(U_d,V_d\) from Lemma 6.1.

Choose a positive word \(p\) with

\[
h(p)=g,
\qquad
|p|\le\delta_+.
\]

Set

\[
W:=pU_d,
\qquad
W':=pV_d.
\]

Then

\[
W\equiv_PW',
\]

and

\[
h(W)=g,
\qquad
h(W')=gd=g'.
\]

The length bound follows. \(\square\)

---

## 8. Corollary — explicit finite-group bound

Let

\[
n:=|G|,
\qquad
d:=|[G,G]|.
\]

Using

\[
\delta_+\le n-1,
\qquad
\delta_H\le d-1,
\]

Theorem 7.1 gives

\[
\begin{aligned}
B(h)
&\le
(n-1)+(d-1)(2(n-1)+2)\\
&=
(n-1)+2n(d-1).
\end{aligned}
\]

Therefore

\[
\boxed{
B(h)
\le
|G|-1+2|G|(|[G,G]|-1).
}
\]

Since \(|[G,G]|\le|G|\),

\[
\boxed{
B(h)
\le
2|G|^2-|G|-1
<2|G|^2.
}
\]

This is a universal bound depending only on the finite target group order.

---

## 9. Algorithmic extraction of witnesses

The proof is constructive when the finite multiplication table of \(G\) and the letter images are known.

### Input

- finite group \(G\);
- alphabet images \(S=h(\Sigma)\);
- two elements \(g,g'\in G\) with equal abelianization image.

### Procedure

1. Run breadth-first search in the positive Cayley digraph to store one shortest positive word for every element of \(G\).
2. Form all basic elements
   \[
   c_{ij}=(g_ig_j)^{-1}(g_jg_i).
   \]
3. Form the symmetric normal generating set \(\mathcal C\) of \(H=[G,G]\).
4. Run breadth-first search in \(\operatorname{Cay}(H,\mathcal C)\) to express
   \[
   d=g^{-1}g'
   \]
   as a product of at most \(\delta_H\) conjugate basic commutators.
5. Replace each factor by the two Parikh-equivalent words from Lemma 4.1.
6. Concatenate those normalized witnesses.
7. Prefix the stored positive representative of \(g\).

The output is an explicit Parikh-equivalent witness pair for the collision \(g\sim_Pg'\).

---

## 10. Relation to the sharp \(S_3\) certificate

For

\[
G=S_3,
\qquad
|G|=6,
\qquad
|[G,G]|=3,
\]

the coarse size-only bound gives

\[
B(h)\le5+12\cdot2=29.
\]

The exact exhaustive result of v0.14 is dramatically sharper:

\[
\boxed{B_{S_3}^{\rm universal}=5.}
\]

Thus v0.16 must not replace the sharp \(S_3\) certificate. Its role is different:

\[
\boxed{
\text{v0.14: sharp special-case depth}
\qquad
\text{v0.16: general constructive finite-depth theorem}.
}
\]

---

## 11. Hostile audit

### 11.1 The quadratic bound is not claimed sharp

The proof deliberately uses only elementary diameter bounds. Better estimates can be inserted immediately if the positive Cayley diameter or the commutator Cayley diameter is known.

### 11.2 Monoid-surjectivity remains essential

The proof repeatedly requires positive words for arbitrary inverses and contextual group elements. For finite groups generated by the letter images this is automatic; for arbitrary infinite groups it is not.

### 11.3 The theorem does not imply bounded FCOA carrier depth independent of the quotient

The bound grows with the chosen finite history quotient. It therefore establishes finite witness depth **for each fixed quotient**, not a universal constant across all finite quotients.

### 11.4 The theorem is purely combinatorial/group-theoretic

No physical time, propagation length, or quantum evolution should be inferred from history-word length.

---

## 12. Literature positioning

Two background facts are standard:

1. the Parikh map is the free-monoid analogue of abelianization; Ciobanu–Garreta explicitly use this analogy in *Group Equations With Abelian Predicates*, IMRN 2024;
2. positive word length in a finite generated group is directed distance in its Cayley digraph, a standard viewpoint in the literature on directed Cayley diameter.

The present theorem uses only the elementary finite bound \(\delta_+\le|G|-1\), so no deep diameter estimate is required.

The exact constructive combination

\[
\text{Parikh collision}
\to
\text{normal commutator factorization}
\to
\text{uniform witness-depth bound}
\]

remains subject to bibliographic novelty audit.

---

## 13. Publication assessment

The robust theorem chain is now:

\[
\boxed{
\begin{aligned}
\text{Parikh collisions}
&\iff
\text{abelianization fibers}\\
&\Downarrow\\
\Gamma_P
&=
\coprod K_{|[G,G]|}\\
&\Downarrow\\
J_P
&=
I([G,G];G)\\
&\Downarrow\\
\text{canonical tight collision frame}\\
&\Downarrow\\
\text{finite constructive witnesses with }B(h)<2|G|^2.
\end{aligned}
}
\]

This is now a self-contained general finite-group package.

Status:

\[
\boxed{
\texttt{PUBLICATION CORE STRONG — EFFECTIVE GENERAL THEOREM ADDED}.
}
\]

The next publication-critical strike should be a **deep novelty audit of Theorem 9.1 from v0.15 and Theorem 7.1 here**. If no direct prior formulation is found, assemble the article immediately. If they are known, the FCOA-specific root-comb specialization plus canonical relative-augmentation/frame consequences remain the candidate contribution.
