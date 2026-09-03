# Parikh Collisions, Abelianization, and Canonical Tight Frames from Finite Group Histories

**Alexey Ivanov and Commander Sol**  
**SOL-QFIELD / FCOA-Z research programme**  
**Version 1.0 — 3 September 2026**

## Abstract

Let \(\Sigma\) be a finite alphabet and let
\[
h:\Sigma^*\twoheadrightarrow G
\]
be a surjective monoid morphism into a group. Two elements \(g,g'\in G\) are called *Parikh-colliding* if they admit preimages with the same Parikh vector. We prove that this relation is exactly the fiber relation of group abelianization:
\[
\boxed{g\sim_P g'\iff g^{-1}g'\in [G,G].}
\]
For finite \(G\), the collision graph is therefore a disjoint union of complete graphs, one on each coset of the derived subgroup. After complex linearization, the span of all collision residues is the relative augmentation ideal
\[
J_P=\ker\bigl(\mathbb C[G]\to\mathbb C[G_{\rm ab}]\bigr)=I([G,G];G).
\]
The normalized edge differences of the collision graph form a canonical unit-norm tight frame for \(J_P\) with frame bound \(|[G,G]|/2\). We also give a constructive finite-depth theorem: every collision in a finite target group admits Parikh-equivalent witnesses of common length
\[
B(h)\le |G|-1+2|G|(|[G,G]|-1)<2|G|^2.
\]
For \(G=S_3\), the collision graph is \(K_3\sqcup K_3\), the collision ideal is the standard block \(M_2(\mathbb C)\), the canonical frame bound is \(3/2\), and a separate exhaustive certificate gives the sharp universal witness depth \(5\) for noncommuting two-letter generating pairs. We finally explain how the theorem arises from fixed-depth reconvergence in the FCOA root-comb system. The physical interpretation remains deliberately limited: the construction supplies an abstract finite history algebra, not a derivation of fermionic quantum field theory.

**Keywords:** Parikh map; abelianization; finite groups; derived subgroup; relative augmentation ideal; tight frames; Cayley diameter; group languages; FCOA; history algebra.

---

## 1. Introduction

The Parikh map forgets the order of letters in a word while retaining their multiplicities. Group abelianization forgets the order of multiplication while retaining the image modulo the derived subgroup. The resemblance is classical, and modern work on equations with abelian predicates makes this analogy explicit. The purpose of this paper is not to claim that analogy as new. Instead, we isolate a concrete collision relation induced by a monoid morphism into a group and show that it is *exactly* the abelianization-fiber relation.

This elementary theorem becomes useful because several consequences follow canonically and with almost no additional choices. For finite groups:

\[
\text{Parikh collisions}
\Longrightarrow
\text{complete coset collision graph}
\Longrightarrow
\text{relative augmentation ideal}
\Longrightarrow
\text{tight collision frame}
\Longrightarrow
\text{finite constructive witness bound}.
\]

The theorem first emerged in a study of finite internal history memories for the FCOA-Z signed-line system. In that application, root-comb histories of a fixed depth reconverge exactly according to their binary Parikh vector. The smallest reversible noncommutative history group is \(S_3\), and this special case produces the two-triangle collision graph \(K_3\sqcup K_3\) and the standard \(M_2\)-block. The abstract theorem, however, is independent of FCOA and is stated first.

The paper is organized as follows. Section 2 fixes notation. Section 3 proves the Parikh–Abelianization Collision Theorem. Section 4 classifies the finite collision graph. Section 5 identifies the canonical collision ideal. Section 6 proves the tight-frame theorem. Section 7 gives an effective finite witness bound. Section 8 treats \(S_3\), including the sharp depth-five certificate. Section 9 specializes the construction to fixed-depth FCOA root-comb histories. Section 10 records a conditional Clifford/CAR coordinatization in the Coxeter realization. Section 11 states the physical limits of the analogy. Section 12 positions the result relative to neighboring literature.

---

## 2. Preliminaries

Let
\[
\Sigma=\{a_1,\dots,a_r\}
\]
be a finite alphabet and let
\[
\Psi:\Sigma^*\to\mathbb N^r
\]
be the Parikh map,
\[
\Psi(w)=\bigl(|w|_{a_1},\dots,|w|_{a_r}\bigr).
\]
We write
\[
u\equiv_P v
\]
when \(\Psi(u)=\Psi(v)\).

Let
\[
h:\Sigma^*\twoheadrightarrow G
\tag{2.1}
\]
be a surjective monoid morphism into a group \(G\), and write
\[
g_i:=h(a_i).
\tag{2.2}
\]

### Definition 2.1 — Parikh collision

For \(g,g'\in G\), define
\[
g\sim_P g'
\tag{2.3}
\]
if there exist \(u,v\in\Sigma^*\) such that
\[
\Psi(u)=\Psi(v),\qquad h(u)=g,\qquad h(v)=g'.
\tag{2.4}
\]

Define the collision-difference set
\[
D_h:=\{h(u)^{-1}h(v):u\equiv_P v\}.
\tag{2.5}
\]

Let
\[
G':=[G,G]
\tag{2.6}
\]
denote the derived subgroup and
\[
\pi:G\to G_{\rm ab}:=G/G'
\tag{2.7}
\]
the abelianization map.

---

## 3. The Parikh–Abelianization Collision Theorem

### Lemma 3.1

Every collision difference lies in the derived subgroup:
\[
D_h\subseteq G'.
\tag{3.1}
\]

### Proof

In \(G_{\rm ab}\), the elements \(\pi(g_i)\) commute. Hence for every word \(w\),
\[
\pi(h(w))
=
\prod_{i=1}^r \pi(g_i)^{|w|_{a_i}},
\tag{3.2}
\]
which depends only on \(\Psi(w)\). If \(u\equiv_P v\), then \(\pi(h(u))=\pi(h(v))\), so
\[
\pi(h(u)^{-1}h(v))=e.
\]
Thus \(h(u)^{-1}h(v)\in\ker\pi=G'\). ∎

### Lemma 3.2 — normalized collision witnesses

For each \(d\in D_h\), there exist \(u_d\equiv_P v_d\) with
\[
h(u_d)=e,\qquad h(v_d)=d.
\tag{3.3}
\]

### Proof

Choose \(u\equiv_P v\) with \(d=h(u)^{-1}h(v)\). By surjectivity, choose \(z\in\Sigma^*\) with \(h(z)=h(u)^{-1}\). Then
\[
zu\equiv_P zv,\qquad h(zu)=e,\qquad h(zv)=d.
\]
∎

### Lemma 3.3

The set \(D_h\) is a normal subgroup of \(G\).

### Proof

The identity belongs to \(D_h\), and swapping a witness pair gives inverses. For multiplication, let \(d_1,d_2\in D_h\), and choose normalized witnesses
\[
u_i\equiv_P v_i,\qquad h(u_i)=e,\qquad h(v_i)=d_i.
\]
Then
\[
u_1u_2\equiv_P v_1v_2,
\]
and the corresponding images are \(e\) and \(d_1d_2\). Hence \(d_1d_2\in D_h\).

For normality, let \(d\in D_h\) have normalized witnesses \(u\equiv_P v\), with images \(e,d\). For arbitrary \(x\in G\), choose positive words \(r,s\) with
\[
h(r)=x,\qquad h(s)=x^{-1}.
\]
Then
\[
rus\equiv_P rvs
\]
and the images are \(e\) and \(xdx^{-1}\). Hence \(xdx^{-1}\in D_h\). ∎

### Lemma 3.4

The derived subgroup \(G'\) is contained in \(D_h\).

### Proof

For each pair of letters \(a_i,a_j\), the words \(a_i a_j\) and \(a_j a_i\) are Parikh-equivalent. Therefore
\[
(g_i g_j)^{-1}(g_jg_i)\in D_h.
\tag{3.4}
\]
Let \(N\) be the normal closure of all these elements. In \(G/N\), the images of every pair \(g_i,g_j\) commute. Since the \(g_i\) generate \(G\), the quotient \(G/N\) is abelian. Thus \(G'\subseteq N\). Conversely, each generator in (3.4) belongs to \(G'\), so \(N\subseteq G'\). Hence \(N=G'\). By Lemma 3.3, \(D_h\) is normal and contains every generator (3.4), so \(G'\subseteq D_h\). ∎

### Theorem 3.5 — Parikh–Abelianization Collision Theorem

Let \(h:\Sigma^*\twoheadrightarrow G\) be a surjective monoid morphism into a group. Then
\[
\boxed{D_h=[G,G].}
\tag{3.5}
\]
Consequently, for \(g,g'\in G\),
\[
\boxed{
g\sim_P g'\iff g^{-1}g'\in[G,G].
}
\tag{3.6}
\]
Equivalently,
\[
\boxed{
g\sim_Pg'\iff \pi(g)=\pi(g')\text{ in }G_{\rm ab}.}
\tag{3.7}
\]

### Proof

Lemmas 3.1 and 3.4 give \(D_h=G'\). If \(g\sim_Pg'\), then \(g^{-1}g'\in D_h=G'\). Conversely, suppose \(d=g^{-1}g'\in G'=D_h\). By Lemma 3.2, choose normalized witnesses \(u\equiv_P v\) with images \(e,d\). Choose \(z\) with \(h(z)=g\). Then
\[
zu\equiv_P zv,\qquad h(zu)=g,\qquad h(zv)=gd=g'.
\]
Thus \(g\sim_Pg'\). ∎

### Corollary 3.6

The collision quotient is canonically the abelianization:
\[
\boxed{G/\!\sim_P\cong G_{\rm ab}.}
\tag{3.8}
\]

### Remark 3.7

Monoid surjectivity is essential in the proof because normalized witnesses and conjugation transport require positive words representing inverses. For finite groups, if the letter images generate \(G\) as a group, monoid surjectivity follows automatically because every inverse is a positive power.

---

## 4. Finite collision graphs

Assume from now on that \(G\) is finite. Put
\[
H:=G'=[G,G],\qquad d:=|H|,\qquad m:=|G/H|.
\tag{4.1}
\]

Define the simple collision graph \(\Gamma_P\) with vertex set \(G\), joining distinct \(g,g'\) iff \(g\sim_Pg'\).

### Theorem 4.1 — collision graph decomposition

\[
\boxed{
\Gamma_P=\coprod_{G/H} K_d.
}
\tag{4.2}
\]

### Proof

By Theorem 3.5, two distinct vertices collide exactly when they lie in the same coset of \(H\). Every coset has \(d\) elements, and there are \(m\) cosets. ∎

Thus the collision graph is determined by the abelianization partition alone.

---

## 5. The canonical collision ideal

Let
\[
A:=\mathbb C[G]
\tag{5.1}
\]
be the complex group algebra, and let
\[
\bar\pi:A\to \mathbb C[G/H]
\tag{5.2}
\]
be the algebra homomorphism induced by the quotient map \(G\to G/H\).

Define the collision-residue span
\[
J_P:=\operatorname{span}_{\mathbb C}\{g-g':g\sim_Pg'\}.
\tag{5.3}
\]

### Theorem 5.1 — canonical relative augmentation sector

\[
\boxed{
J_P=\ker\bar\pi=I(H;G),
}
\tag{5.4}
\]
where \(I(H;G)\) is the relative augmentation ideal associated with \(H=[G,G]\).

### Proof

If \(g\sim_Pg'\), then \(gH=g'H\), so \(\bar\pi(g-g')=0\); hence \(J_P\subseteq\ker\bar\pi\).

Conversely, write
\[
x=\sum_{g\in G}c_gg\in\ker\bar\pi.
\]
For each coset \(C\in G/H\), the coefficient sum satisfies
\[
\sum_{g\in C}c_g=0.
\tag{5.5}
\]
The zero-sum subspace on \(C\) is spanned by differences \(g-g'\) with \(g,g'\in C\). By Theorem 3.5 all such pairs collide. Therefore \(x\in J_P\). ∎

Define
\[
e_H:=\frac1{|H|}\sum_{h\in H}h.
\tag{5.6}
\]
Since \(H\trianglelefteq G\), \(e_H\) is a central self-adjoint idempotent.

### Corollary 5.2

\[
\boxed{J_P=A(1-e_H)=(1-e_H)A.}
\tag{5.7}
\]
Moreover
\[
Ae_H\cong \mathbb C[G/H],
\tag{5.8}
\]
and therefore
\[
\boxed{
\mathbb C[G]=Ae_H\oplus A(1-e_H).
}
\tag{5.9}
\]

This gives a canonical decomposition into an abelianization-visible sector and an order-sensitive collision sector.

---

## 6. Canonical tight frame of collision residues

Equip \(\mathbb C[G]\) with the coefficient inner product for which the group basis is orthonormal:
\[
\left\langle \sum_g a_gg,\sum_g b_gg\right\rangle
=
\sum_g \overline{a_g}b_g.
\tag{6.1}
\]
For every unordered collision edge \(\{g,g'\}\), define
\[
r_{g,g'}:=\frac{g-g'}{\sqrt2}.
\tag{6.2}
\]
Each such vector has norm one.

### Theorem 6.1 — universal tight collision frame

The family
\[
\mathcal R_P
=
\left\{\frac{g-g'}{\sqrt2}:\{g,g'\}\in E(\Gamma_P)\right\}
\tag{6.3}
\]
is a unit-norm tight frame for \(J_P\) with frame operator
\[
\boxed{
S_P=\frac d2 I_{J_P},
\qquad d=|[G,G]|.
}
\tag{6.4}
\]
Equivalently, for every \(x\in J_P\),
\[
\boxed{
\sum_{r\in\mathcal R_P}\langle x,r\rangle r
=
\frac d2 x.
}
\tag{6.5}
\]

### Proof

Fix a coset \(C=\{g_1,\dots,g_d\}\). Its edge vectors are
\[
r_{ij}=\frac{g_i-g_j}{\sqrt2}.
\]
Their frame operator is one half of the complete-graph Laplacian:
\[
\sum_{i<j}|r_{ij}\rangle\langle r_{ij}|=\frac12L(K_d).
\tag{6.6}
\]
Since
\[
L(K_d)=dI-J,
\tag{6.7}
\]
its restriction to the zero-sum subspace
\[
W_C:=\left\{\sum_{g\in C}c_gg:\sum_{g\in C}c_g=0\right\}
\tag{6.8}
\]
is \(dI\). Hence the normalized edge vectors form a tight frame on \(W_C\) with bound \(d/2\).

Different cosets are orthogonal in the coefficient inner product, and
\[
J_P=\bigoplus_{C\in G/H}W_C.
\tag{6.9}
\]
Taking the union of the coset edge frames gives (6.4)–(6.5). ∎

### Corollary 6.2 — reconstruction

For every \(x\in J_P\),
\[
\boxed{
x=\frac2d\sum_{r\in\mathcal R_P}\langle x,r\rangle r.}
\tag{6.10}
\]

### Corollary 6.3 — dimension and redundancy

\[
\dim_{\mathbb C}J_P
=|G|-|G_{\rm ab}|
=m(d-1),
\tag{6.11}
\]
while the number of unoriented frame vectors is
\[
N=m\binom d2=\frac{|G|(d-1)}2.
\tag{6.12}
\]
Hence
\[
\frac{N}{\dim J_P}=\frac d2,
\tag{6.13}
\]
matching the unit-norm tight-frame bound.

---

## 7. Effective finite witness depth

Theorem 3.5 is existential. For finite groups, it can be made constructive.

Let
\[
S=h(\Sigma)\subseteq G.
\]
Define the positive word length \(\ell_+(x)\) of \(x\in G\) as the length of the shortest positive word in \(\Sigma^*\) mapping to \(x\), and let
\[
\delta_+:=\max_{x\in G}\ell_+(x).
\tag{7.1}
\]
Because the positive Cayley digraph is strongly connected,
\[
\delta_+\le |G|-1.
\tag{7.2}
\]

For letters \(a_i,a_j\), define
\[
\alpha_{ij}:=g_ig_j,\qquad
\beta_{ij}:=g_jg_i,\qquad
c_{ij}:=\alpha_{ij}^{-1}\beta_{ij}.
\tag{7.3}
\]
Let
\[
\mathcal C:=\{xc_{ij}^{\pm1}x^{-1}:x\in G,\ i,j\}.
\tag{7.4}
\]
This is a symmetric generating set of \(H=[G,G]\). Let
\[
\delta_H:=\operatorname{diam}\operatorname{Cay}(H,\mathcal C).
\tag{7.5}
\]
Then
\[
\delta_H\le |H|-1.
\tag{7.6}
\]

### Lemma 7.1 — short normalized conjugate witnesses

For every \(x\in G\), every pair \(i,j\), and \(\varepsilon\in\{\pm1\}\), there exist Parikh-equivalent words \(U,V\) satisfying
\[
h(U)=e,\qquad h(V)=xc_{ij}^{\varepsilon}x^{-1},
\]
and
\[
\boxed{|U|=|V|\le 2\delta_++2.}
\tag{7.7}
\]

### Proof

Take first \(\varepsilon=1\). Choose positive words \(y,z\) with
\[
h(y)=x^{-1},\qquad h(z)=x\alpha_{ij}^{-1},
\]
and lengths at most \(\delta_+\). Set
\[
U=za_ia_jy,\qquad V=za_ja_iy.
\]
The words have the same Parikh vector. Their images are
\[
h(U)=x\alpha_{ij}^{-1}\alpha_{ij}x^{-1}=e,
\]
\[
h(V)=x\alpha_{ij}^{-1}\beta_{ij}x^{-1}=xc_{ij}x^{-1}.
\]
The common length is at most \(2\delta_++2\). The case \(\varepsilon=-1\) follows by exchanging the two seed words and using \(\beta_{ij}^{-1}\). ∎

### Lemma 7.2

For every \(d\in H\), there exist normalized Parikh-equivalent witnesses \(U_d,V_d\) with
\[
h(U_d)=e,\qquad h(V_d)=d,
\]
and
\[
\boxed{|U_d|=|V_d|\le \delta_H(2\delta_++2).}
\tag{7.8}
\]

### Proof

Write \(d=d_1\cdots d_t\) with \(d_k\in\mathcal C\) and \(t\le\delta_H\). Choose normalized witnesses for each factor from Lemma 7.1 and concatenate the identity-side words and the factor-side words. Parikh vectors add under concatenation, while the images multiply to \(e\) and \(d\). ∎

### Theorem 7.3 — constructive collision-depth bound

For every collision \(g\sim_Pg'\), there exist Parikh-equivalent witnesses \(W,W'\) with
\[
h(W)=g,\qquad h(W')=g'
\]
and
\[
\boxed{
|W|=|W'|
\le
\delta_++\delta_H(2\delta_++2).
}
\tag{7.9}
\]
Consequently,
\[
\boxed{
B(h)
\le
|G|-1+2|G|(|[G,G]|-1)
<2|G|^2.
}
\tag{7.10}
\]

### Proof

Put \(d=g^{-1}g'\in H\). Choose normalized witnesses \(U_d,V_d\) from Lemma 7.2. Choose a positive word \(p\) representing \(g\) with \(|p|\le\delta_+\). Then
\[
W=pU_d,\qquad W'=pV_d
\]
have the same Parikh vector and map to \(g\) and \(g'\). Substituting (7.2) and (7.6) into (7.9) gives (7.10). ∎

### Remark 7.4

The quadratic bound is deliberately coarse. It is universal and constructive, not sharp. Any better bounds on \(\delta_+\) or \(\delta_H\) improve (7.9) immediately.

---

## 8. The \(S_3\) case

Let \(G=S_3\). Then
\[
G'=A_3\cong C_3,
\qquad
|G'|=3,
\qquad
|G/G'|=2.
\tag{8.1}
\]
Hence Theorem 4.1 gives
\[
\boxed{\Gamma_P=K_3\sqcup K_3.}
\tag{8.2}
\]
The two components are the even and odd cosets.

The central averaging idempotent is
\[
e_{A_3}=\frac13(e+a+a^2),
\tag{8.3}
\]
where \(a=(123)\). Thus
\[
1-e_{A_3}=\frac13(2e-a-a^2).
\tag{8.4}
\]
This is exactly the central projector onto the standard irreducible block of \(\mathbb C[S_3]\). Therefore
\[
\boxed{
J_P=\mathbb C[S_3](1-e_{A_3})\cong M_2(\mathbb C).
}
\tag{8.5}
\]

The frame theorem gives six unoriented normalized edge differences spanning a four-dimensional complex collision sector, with
\[
\boxed{S_P=\frac32I.}
\tag{8.6}
\]
Before complexification, the corresponding real Wedderburn block is
\[
J_P^{\mathbb R}\cong M_2(\mathbb R).
\tag{8.7}
\]
In the standard real representation, the even coset gives one equilateral \(A_2\) edge frame, the transposition coset gives a second, and the two planes are orthogonal.

### Sharp two-letter depth

A separate exhaustive verifier checks all 18 ordered noncommuting pairs \((p,q)\in S_3^2\). Grouping binary words by exact Parikh vector, every same-parity collision edge appears by depth at most five, and depth five is necessary for the six ordered transposition/transposition generating pairs. Thus
\[
\boxed{B_{S_3}^{\rm universal}=5.}
\tag{8.8}
\]
For the remaining twelve ordered noncommuting pairs, depth four suffices.

This sharp certificate complements, rather than follows from, the coarse general bound (7.10).

---

## 9. Fixed-depth FCOA root-comb specialization

We now explain the origin of the construction in the FCOA-Z signed-line model.

Let
\[
X=\{x_k:k\in\mathbb Z\}
\]
with root \(x_0\), and define the radial contraction
\[
\rho(x_k)=x_{k-\operatorname{sgn}(k)}
\qquad(k\ne0).
\tag{9.1}
\]
The two root-comb events are
\[
L:x\mapsto x_0\oplus x=x,
\qquad
R:x\mapsto x\oplus x_0=\rho(x).
\tag{9.2}
\]
For a history word \(w\in\{L,R\}^*\), as long as the trajectory remains away from the root,
\[
\boxed{F_w(x_k)=\rho^{|w|_R}(x_k).}
\tag{9.3}
\]

### Proposition 9.1 — fixed-depth Parikh fibers

Fix a history depth \(m\). For safe words \(w,w'\in\{L,R\}^m\),
\[
F_w(x_k)=F_{w'}(x_k)
\iff
|w|_R=|w'|_R
\iff
\Psi(w)=\Psi(w').
\tag{9.4}
\]

### Proof

By (9.3), endpoint equality at fixed starting point is equivalent to equality of the number of \(R\)-steps in the safe range. Since \(|w|=|w'|=m\), equality of \(|w|_R\) also implies equality of \(|w|_L=m-|w|_R\). Thus the complete binary Parikh vectors agree. ∎

For
\[
W_{m,r}:=\{w\in\{L,R\}^m:|w|_R=r\},
\tag{9.5}
\]
all histories in \(W_{m,r}\) reconverge and \(W_{m,r}\) is precisely the Parikh fiber \((m-r,r)\).

### Important scope qualification

Across histories of different lengths, FCOA carrier reconvergence is strictly coarser than Parikh equivalence because inserting an \(L\)-event may leave the carrier endpoint unchanged. For example, \(L\) and \(LL\) have the same carrier action away from the root but different Parikh vectors. Therefore the abstract theorem of Sections 3–7 applies canonically to the **fixed-depth Parikh collision sector**, not to every unrestricted cross-depth carrier reconvergence.

This correction does not affect any finite-group theorem above.

### Minimal reversible memory

The shortest order-sensitive pair is \(LR\) versus \(RL\). A reversible history memory that distinguishes these routes requires noncommuting generator images. Every group of order below six is abelian, while \(S_3\) is nonabelian. Hence six is the smallest possible order of a reversible noncommutative history group, and \(S_3\) realizes the minimum.

The FCOA application therefore yields the chain
\[
\boxed{
\text{fixed-depth root-comb reconvergence}
\to
\text{binary Parikh fibers}
\to
S_3\text{ minimal reversible history}
\to
K_3\sqcup K_3
\to
M_2(\mathbb C).
}
\tag{9.6}
\]
All of this remains a finite internal history fiber over the original one-dimensional carrier.

---

## 10. Conditional Clifford and one-mode CAR coordinates

The collision ideal in the \(S_3\) case is canonical, but a preferred Pauli or Clifford basis is not.

If one imposes the additional involutive/Coxeter realization
\[
h(L)^2=h(R)^2=e,
\tag{10.1}
\]
with distinct noncommuting transpositions, then particular depth-two and depth-three route residues may be normalized to elements \(Q_x,Q_y\in J_P\) satisfying
\[
Q_x^2=Q_y^2=e_{\rm std},
\qquad
\{Q_x,Q_y\}=0.
\tag{10.2}
\]
Thus they generate
\[
\mathrm{Cl}_2(\mathbb C)\cong M_2(\mathbb C).
\tag{10.3}
\]
Setting
\[
c=\frac12(Q_x+iQ_y),
\qquad
c^*=\frac12(Q_x-iQ_y),
\tag{10.4}
\]
gives the algebraic one-mode CAR relations
\[
c^2=(c^*)^2=0,
\qquad
cc^*+c^*c=e_{\rm std}.
\tag{10.5}
\]

However, cardinality minimality alone does not force both history generators to be transpositions. Mixed generating pairs of orders \((3,2)\) or \((2,3)\) are also valid minimal \(S_3\) histories, and the direct primitive residues need not anticommute. Therefore (10.2)–(10.5) are **conditional coordinates inside the canonical collision sector**, not generator-independent theorems.

The robust object is
\[
\boxed{J_P=I([S_3,S_3];S_3)\cong M_2(\mathbb C),}
\tag{10.6}
\]
not a distinguished Pauli basis.

---

## 11. Limits of the physical analogy

The route-history construction was motivated by questions involving exchange constraints and annihilation channels, but the mathematics obtained here does not constitute a quantum-field-theoretic derivation.

The construction does **not** provide:

- a physical Hilbert or Fock space;
- Lorentz or Poincaré covariance;
- local quantum fields;
- a Hamiltonian or physical time evolution;
- an S-matrix;
- scattering amplitudes or cross sections;
- conservation laws;
- gauge structure;
- a Born-rule measurement postulate;
- physical CAR/CCR field relations.

Accordingly, the presence of an \(M_2(\mathbb C)\) block, Clifford coordinates, or one-mode algebraic CAR in a special realization must not be identified with the derivation of spin, fermions, or particle–antiparticle annihilation.

The physical verdict is therefore:
\[
\boxed{\text{QFT interpretation: analogy only}.}
\tag{11.1}
\]

---

## 12. Literature positioning

The components surrounding the main theorem are established mathematics.

The Parikh map and commutative closure are standard in formal-language theory. Hoffmann studied the commutative closure of group languages and state-complexity bounds, and later regularity of commutative closures of shuffle languages over group languages. More recently, Becher, Lew Deveali, and Mollo Cunningham gave automata constructions for regular commutative closures. Ciobanu and Garreta explicitly use group abelianization as the group-level analogue of Parikh-type abelian information in their study of equations with abelian predicates. Relative augmentation ideals are classical objects in group-ring theory; García-Lucas provides a modern use of such ideals in the modular isomorphism problem. Finally, the tight-frame calculation in Section 6 is the standard complete-graph Laplacian identity applied to the zero-sum subspace.

The contribution claimed here is therefore not the discovery of Parikh maps, abelianization, relative augmentation ideals, complete-graph frames, or the representation theory of \(S_3\). We instead isolate and prove the induced collision correspondence (3.6) and derive from it a coherent package of graph, group-algebra, frame-theoretic, effective finite-depth, and FCOA-history consequences.

In the literature consulted during preparation, we did not locate this exact combined formulation. This is a bibliographic observation, not a priority claim.

---

## 13. Conclusions and open problems

The main theorem identifies a simple but rigid quotient principle:
\[
\boxed{
\text{order erasure by Parikh equivalence}
\quad\Longleftrightarrow\quad
\text{order erasure by group abelianization}.
}
\]
Once this relation is transported to a finite target group, the remaining structure is canonical:
\[
\boxed{
\begin{aligned}
\Gamma_P&=\coprod_{G/[G,G]}K_{|[G,G]|},\\
J_P&=I([G,G];G),\\
S_P&=\frac{|[G,G]|}{2}I,\\
B(h)&<2|G|^2.
\end{aligned}}
\tag{13.1}
\]
For \(S_3\), this reduces to
\[
\boxed{
K_3\sqcup K_3,\qquad
J_P\cong M_2(\mathbb C),\qquad
S_P=\frac32I,\qquad
B^{\rm universal}_{S_3}=5.
}
\tag{13.2}
\]

Three natural problems remain.

1. Determine sharper general bounds for the minimal Parikh witness depth in terms of intrinsic invariants of \((G,S)\).
2. Classify when the canonical collision ideal \(I([G,G];G)\) is simple, a single matrix block, or admits distinguished geometric frames beyond the complete-coset edge frame.
3. Extend the fixed-depth history interpretation to broader reconvergence systems where endpoint fibers are governed by partially commutative or weighted Parikh data.

These are mathematical extensions of the present framework. They are not required for the validity of the results proved here.

---

## References

1. V. Becher, S. Lew Deveali, and I. Mollo Cunningham, “Automata for the commutative closure of regular languages,” *Journal of Computer and System Sciences* **158** (2026), 103762. DOI: `10.1016/j.jcss.2026.103762`.
2. L. Ciobanu and A. Garreta, “Group Equations With Abelian Predicates,” *International Mathematics Research Notices* **2024**(5) (2024), 4119–4159. DOI: `10.1093/imrn/rnad179`.
3. D. García-Lucas, “The Modular Isomorphism Problem and Abelian Direct Factors,” *Mediterranean Journal of Mathematics* **21** (2024), Article 18. DOI: `10.1007/s00009-023-02557-1`.
4. S. Hoffmann, “State Complexity Bounds for the Commutative Closure of Group Languages,” in *Descriptional Complexity of Formal Systems — DCFS 2020*, LNCS **12442** (2020), 64–77. DOI: `10.1007/978-3-030-62536-8_6`.
5. S. Hoffmann, “The Commutative Closure of Shuffle Languages over Group Languages is Regular,” in *Implementation and Application of Automata — CIAA 2021*, LNCS, pp. 53–64 (2021). DOI: `10.1007/978-3-030-79121-6_5`.
6. FCOA-Z v1.1, research programme record, DOI: `10.5281/zenodo.22169264`.
7. Supplementary computational certificate: `verify_parikh_collision_s3.py`, SOL-QFIELD repository branch `director/fcoa-z-symmetric-line`.

---

## Reproducibility statement

The general theorems are proved analytically and do not depend on computation. The supplementary \(S_3\) script performs an exhaustive finite verification of the sharp universal depth-five statement across all ordered noncommuting generator pairs. The script is a regression certificate, not a substitute for the structural proof of the collision theorem.

## Research-status statement

The robust theorem chain in this article supersedes earlier exploratory formulations in which a Clifford pair was temporarily treated as generator-independent. The publication version incorporates the later canonicity correction: the collision ideal and collision frame are canonical; Clifford/CAR coordinates require an additional involutive/Coxeter choice.