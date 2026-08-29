# Reflections on the Support-Cardinality Valuation Wall with Commander Sol

## Finite Positive-Depth Perturbations versus Infinite Residual Graph Universality

**Alex Malachevsky**  
ORCID: 0009-0008-6009-3196  
Version 1.0 release candidate  
2026-08-27

## Abstract

We study a family of two-sorted first-order structures built from multiplicative positive integers, additive rationals, a Ramanujan-Delta bridge, and a uniformly indexed family of valuation-threshold predicates. For an arbitrary profile

\[
\kappa:\mathbb P\to\mathbb N_0,
\]

we write

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge \kappa(r),
\]

and

\[
P_+(\kappa)=\{r\in\mathbb P:\kappa(r)\ge1\}.
\]

The main result is a support-cardinality dichotomy. If \(P_+(\kappa)\) is finite, then the resulting structure is parameter-free interdefinable with the uniform zero-depth structure \(B_0\). Hence the formula-relative compression theorem from the preceding zero-depth paper transfers unchanged: ordinary prime order and prime successor remain parameter-free non-definable, and every fixed parameter-free grid isolator has finite Grid-Isolation Rank. If \(P_+(\kappa)\) is infinite, the behavior changes completely. The bridge exposes the residual condition

\[
r^{\kappa(r)}\mid \tau(p)^2-p^{11},
\]

and adelic open image for the Galois representation of \(\Delta\), together with Chebotarev, gives arbitrary finite EDGE/NONEDGE patterns simultaneously at arbitrary positive local depths. A single fixed ternary formula then has infinite Grid-Isolation Rank, all finite directed graphs are uniformly coded, and the complete first-order theory is undecidable.

Thus the phase transition is not controlled by whether the depth equals \(0\) or \(1\), nor by boundedness, density, or growth of the positive depths. It is controlled by one invariant only:

\[
\boxed{
|P_+(\kappa)|<\infty
\quad\Big|\quad
|P_+(\kappa)|=\infty.
}
\]

Equivalently, inside this threshold-profile family, the empty-parameter definability boundary over the zero-depth structure is exact:

\[
B_\kappa\in\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,0})
\iff
|P_+(\kappa)|<\infty.
\]

**Keywords:** Ramanujan tau function; modular forms; adelic Galois representations; valuations; model theory; definability; undecidability; Chebotarev; finite graph interpretation; Grid-Isolation Rank.

---

## 1. From a zero/one wall to a support-cardinality wall

The preceding stage of this programme isolated a sharp difference between two uniformly indexed valuation predicates. At depth zero,

\[
B_0(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge0,
\]

formula-relative tail symmetry survives and every fixed parameter-free source isolator has finite Grid-Isolation Rank. At depth one,

\[
B_1(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge1,
\]

the Ramanujan bridge exposes residual congruence data and produces a fixed isolator of infinite rank. The two results gave an exact expressive separation between \(B_0\) and \(B_1\).

The natural next question is whether depth one is exceptional. It is not.

The correct object is an arbitrary threshold profile

\[
\kappa:\mathbb P\to\mathbb N_0.
\]

One may allow \(\kappa\) to be irregular, sparse, unbounded, or non-computable. The threshold at one prime need bear no relation to the threshold at another. Surprisingly, none of these numerical features governs the logical transition. What matters is simply whether positive depth occurs at finitely or infinitely many prime places.

This paper proves that statement and makes the boundary exact.

The result should be read as a theorem about the expressive geometry of a specific mixed arithmetic structure, not as a statement about the Riemann hypothesis and not as a claim that ordinary prime order becomes definable on the amplifying side. Infinite graph universality is a strong form of expressive amplification, but orientation is a separate question.

---

## 2. The structure and the Ramanujan bridge

Let

\[
\Delta(z)=q\prod_{n\ge1}(1-q^n)^{24}
=\sum_{n\ge1}\tau(n)q^n
\]

be the Ramanujan discriminant form. For each prime \(p\), define the rational bridge label

\[
u_p
=
\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

We use two sorts:

\[
(\mathbb N_{>0},\times,1)
\]

and

\[
(\mathbb Q,+,0).
\]

The bridge relation is

\[
U_\Delta(p,x)
\iff
\operatorname{Prime}(p)\land x=u_p.
\]

For an arbitrary threshold profile \(\kappa:\mathbb P\to\mathbb N_0\), define

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge\kappa(r).
\]

The resulting two-sorted structure is

\[
\mathcal V_{\Delta,\kappa}
=
\Bigl(
(\mathbb N_{>0},\times,1),
(\mathbb Q,+,0),
U_\Delta,
B_\kappa
\Bigr).
\]

Finally set

\[
P_+(\kappa)
=
\{r\in\mathbb P:\kappa(r)\ge1\}.
\]

The main theorem will show that the cardinality type of \(P_+(\kappa)\) — finite or infinite — is the phase parameter.

### 2.1. The local bridge identity

If \(p\ne r\), then the denominator \(p^{11}\) is an \(r\)-adic unit. Hence

\[
v_r(u_p)
=
v_r\bigl(\tau(p)^2-p^{11}\bigr).
\]

Therefore, whenever \(r\in P_+(\kappa)\) and \(p\ne r\),

\[
B_\kappa(r,u_p)
\iff
r^{\kappa(r)}\mid \tau(p)^2-p^{11}.
\]

At depth zero the same condition is automatic for \(p\ne r\). At every positive depth it becomes a genuine congruence condition. This is the elementary source of the wall.

---

## 3. Grid-Isolation Rank

The rank used here measures whether one fixed ternary formula can isolate arbitrarily large coordinate grids.

### Definition 3.1. Grid-Isolation Rank

Let \(I(p,q;r)\) be a fixed parameter-free formula whose free variables lie in the source sort and are intended to range over primes. We say

\[
\operatorname{GIR}(I)\ge n
\]

if there exist primes

\[
p_1,\dots,p_n,
\qquad
q_1,\dots,q_n,
\qquad
r_{ij}\ (1\le i,j\le n),
\]

which may be chosen pairwise distinct, such that

\[
I(p_k,q_\ell;r_{ij})
\iff
(k,\ell)=(i,j).
\]

The Grid-Isolation Rank \(\operatorname{GIR}(I)\) is the supremum of such \(n\), possibly \(\infty\).

Finite GIR is a compression phenomenon: one fixed formula cannot create arbitrarily large independent coordinate addresses. Infinite GIR is an amplification phenomenon: the formula can isolate an arbitrarily large matrix of markers.

The zero-depth paper proves that every fixed parameter-free isolator in \(\mathcal V_{\Delta,0}\) has finite GIR. The present paper determines exactly which threshold profiles remain on that side of the wall.

---

## 4. Every fixed source prime is parameter-free definable

A small lemma will let us treat finitely many exceptional places without adding parameters.

### Lemma 4.1. Fixed-prime definability

For every fixed ordinary prime \(\ell\), define

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
\bigr),
\]

where \(\ell x\) is the fixed additive scalar term obtained by repeated addition.

Then

\[
\Theta_\ell(r)
\iff
r=\ell.
\]

### Proof

If \(r\ne\ell\), multiplication by \(\ell\) is an \(r\)-adic unit, so

\[
v_r(\ell x)=v_r(x).
\]

Thus \(x\) cannot cross the threshold \(\kappa(r)\) under multiplication by \(\ell\).

If \(r=\ell\), choose \(x\in\mathbb Q\) with

\[
v_\ell(x)=\kappa(\ell)-1.
\]

Then \(B_\kappa(\ell,x)\) fails while \(B_\kappa(\ell,\ell x)\) holds. When \(\kappa(\ell)=0\), take \(v_\ell(x)=-1\). ∎

This lemma is intentionally elementary, but it is structurally important. Any finite set of standard primes can be named without parameters inside every threshold-profile structure.

---

## 5. The safe side: finite positive support

Assume

\[
P_+(\kappa)
=
\{\ell_1,\dots,\ell_t\}
\]

is finite.

Outside this finite set,

\[
B_\kappa(r,x)=B_0(r,x).
\]

At one exceptional place \(\ell\), write

\[
k=\kappa(\ell)\ge1.
\]

Then

\[
B_\kappa(\ell,x)
\iff
\exists y\,
\bigl(
 x=\ell^k y
\land
 B_0(\ell,y)
\bigr).
\]

Conversely,

\[
B_0(\ell,x)
\iff
B_\kappa(\ell,\ell^k x).
\]

Because \(r=\ell_i\) is parameter-free definable by Lemma 4.1, a finite first-order case distinction over \(\ell_1,\dots,\ell_t\) yields both directions of definability.

### Theorem 5.1. Finite-support interdefinability

If \(P_+(\kappa)\) is finite, then

\[
\mathcal V_{\Delta,\kappa}
\equiv_{\emptyset\text{-def}}
\mathcal V_{\Delta,0}.
\]

That is, each structure is definable in the other without parameters, on the same underlying sorts.

### Corollary 5.2. Transfer of zero-depth compression

If \(P_+(\kappa)\) is finite, then the parameter-free consequences proved for \(\mathcal V_{\Delta,0}\) transfer to \(\mathcal V_{\Delta,\kappa}\). In particular,

\[
<_{\mathbb P}
\notin
\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,\kappa}),
\]

\[
\operatorname{Succ}_{\mathbb P}
\notin
\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,\kappa}),
\]

and for every fixed parameter-free ternary isolator \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

Thus finitely many positive-depth perturbations do not move the structure across the wall.

---

## 6. The amplifying side: residual incidence at arbitrary depth

Now assume

\[
|P_+(\kappa)|=\infty.
\]

Define, for distinct prime source variables \(p,r\),

\[
E_\kappa(p;r)
:
 p\ne r
\land
\exists x\,
\bigl(
U_\Delta(p,x)
\land
B_\kappa(r,x)
\bigr).
\]

By the local bridge identity,

\[
\boxed{
E_\kappa(p;r)
\iff
r^{\kappa(r)}\mid\tau(p)^2-p^{11}
}
\]

for \(r\in P_+(\kappa)\) and \(p\ne r\).

The important point is that \(E_\kappa\) is one fixed first-order formula of the language of the fixed structure \(\mathcal V_{\Delta,\kappa}\). The external function \(\kappa\) does not occur in the syntax.

---

## 7. Adelic independence at arbitrary finite levels

For each prime \(r\), let

\[
\rho_{\Delta,r}:G_\mathbb Q\to\operatorname{GL}_2(\mathbb Z_r)
\]

be the \(r\)-adic representation attached to \(\Delta\), normalized so that for primes \(p\ne r\),

\[
\operatorname{tr}\rho_{\Delta,r}(\operatorname{Frob}_p)
=
\tau(p),
\]

and

\[
\det\rho_{\Delta,r}(\operatorname{Frob}_p)
=
p^{11}.
\]

Let

\[
H=G_{\mathbb Q(\mu_\infty)}
=
\ker\chi,
\]

where \(\chi\) is the cyclotomic character. On \(H\), the determinant contribution is trivial, so the image lies in the product of the determinant-one local groups.

Loeffler's adelic open-image theorem for non-CM modular forms gives, after specialization to the level-one form \(\Delta\), an open adelic image in the relevant algebraic group. Intersecting with the cyclotomic kernel gives an open subgroup of

\[
\prod_r\operatorname{SL}_2(\mathbb Z_r).
\]

The following elementary profinite observation converts openness into the exact finite-level independence needed here.

### Lemma 7.1. Full factors outside a finite set

Let

\[
V\le\prod_r\operatorname{SL}_2(\mathbb Z_r)
\]

be open. Then there is a finite set of primes \(S\) such that

\[
\prod_{r\notin S}\operatorname{SL}_2(\mathbb Z_r)
\subseteq V.
\]

### Proof

A neighborhood basis at the identity in the product topology consists of subgroups

\[
\prod_rV_r
\]

with \(V_r=\operatorname{SL}_2(\mathbb Z_r)\) for all but finitely many \(r\). Since \(V\) is open and contains the identity, one such basic neighborhood lies inside \(V\). ∎

Applying Lemma 7.1 to the cyclotomic-kernel image yields a finite exceptional set \(S_\Delta\).

### Theorem 7.2. Arbitrary-depth finite residual independence

For every finite

\[
R\subseteq\mathbb P\setminus S_\Delta
\]

and every family of positive integers \(k_r\ge1\), the reduction map

\[
H
\longrightarrow
\prod_{r\in R}
\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z)
\]

is surjective.

### Proof

By Lemma 7.1, each finite tuple of local elements in the good factors can be prescribed independently inside the adelic image. Reduction

\[
\operatorname{SL}_2(\mathbb Z_r)
\to
\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z)
\]

is surjective. Combining the finitely many coordinates proves the claim. ∎

No bound on the numbers \(k_r\) is needed. Every application uses only finitely many finite levels.

---

## 8. One pair of integral matrices works at every positive depth

The higher-depth argument becomes simpler than one might expect. No classification of projective order over \(\mathbb Z/r^k\mathbb Z\) is required.

Consider

\[
A=
\begin{pmatrix}
0&-1\\
1&1
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

Both lie in \(\operatorname{SL}_2(\mathbb Z)\). For \(A\),

\[
\operatorname{tr}(A)=1,
\qquad
\det(A)=1,
\]

and therefore

\[
\operatorname{tr}(A)^2-\det(A)=0.
\]

For the identity matrix \(J\),

\[
\operatorname{tr}(J)^2-\det(J)=4-1=3.
\]

Hence, for every prime \(r>3\) and every \(k\ge1\),

\[
\operatorname{tr}(A)^2
\equiv
\det(A)
\pmod{r^k},
\]

while

\[
\operatorname{tr}(J)^2
\not\equiv
\det(J)
\pmod{r^k}.
\]

Thus the same pair \(A,J\) supplies an exact EDGE/NONEDGE witness at every positive local depth.

This is the key reason the numerical size of \(\kappa(r)\) disappears from the phase diagram.

---

## 9. Finite pattern realization

Choose a finite marker set

\[
R
\subset
P_+(\kappa)
\setminus
(S_\Delta\cup\{2,3\}).
\]

Let \(T\subseteq R\) be arbitrary. For each \(r\in R\), prescribe the finite-level local matrix

\[
g_r=
\begin{cases}
A,&r\in T,\\
J,&r\notin T,
\end{cases}
\]

modulo \(r^{\kappa(r)}\).

By Theorem 7.2 there exists

\[
\sigma\in H
\]

with precisely these finite-level coordinates.

Let \(L/\mathbb Q\) be the finite Galois extension cut out by the combined residual representations modulo \(r^{\kappa(r)}\) for \(r\in R\). The image of \(\sigma\) determines a conjugacy class in \(\operatorname{Gal}(L/\mathbb Q)\). By Chebotarev, infinitely many rational primes \(p\) have Frobenius in that conjugacy class.

Trace and determinant are conjugacy invariants. Therefore the prescribed EDGE/NONEDGE values survive passage from the chosen element to its Frobenius class, and

\[
E_\kappa(p;r)
\iff
r\in T
\qquad(r\in R).
\]

### Theorem 9.1. Finite pattern realization

For every finite marker set

\[
R\subset
P_+(\kappa)
\setminus
(S_\Delta\cup\{2,3\})
\]

and every subset \(T\subseteq R\), there exist infinitely many source primes \(p\) such that

\[
E_\kappa(p;r)
\iff
r\in T
\]

for all \(r\in R\).

Only infinitude of \(P_+(\kappa)\) is used. Its natural density may be zero. The profile may be unbounded and non-computable.

---

## 10. Infinite Grid-Isolation Rank

Define the fixed ternary formula

\[
I_\kappa(p,q;r)
:=
E_\kappa(p;r)
\land
E_\kappa(q;r).
\]

Fix \(n\ge1\). Choose \(n^2\) distinct markers

\[
r_{ij}
\in
P_+(\kappa)
\setminus
(S_\Delta\cup\{2,3\}).
\]

For each row \(i\), finite pattern realization gives a prime \(p_i\) whose positive marker set is exactly

\[
\{r_{i1},\dots,r_{in}\}.
\]

For each column \(j\), choose a prime \(q_j\) whose positive marker set is exactly

\[
\{r_{1j},\dots,r_{nj}\}.
\]

Because each desired pattern is realized by infinitely many source primes, all \(p_i,q_j,r_{ij}\) may be chosen pairwise distinct.

Then

\[
I_\kappa(p_k,q_\ell;r_{ij})
\iff
(k,\ell)=(i,j).
\]

### Theorem 10.1. Infinite GIR

If \(P_+(\kappa)\) is infinite, then

\[
\boxed{
\operatorname{GIR}(I_\kappa)=\infty.
}
\]

This already separates every infinite-positive-support profile from the zero-depth structure.

---

## 11. Uniform coding of finite directed graphs

The same grid gives an effective interpretation of arbitrary finite directed graphs.

Divisibility is first-order definable in the multiplicative source sort:

\[
x\mid y
\iff
\exists z\;y=xz.
\]

For a source parameter \(a\), define the finite set

\[
D_a(x)
:
\operatorname{Prime}(x)\land x\mid a.
\]

For a source parameter \(\eta\), define

\[
R_\eta(x,y)
:=
\exists r\,
\bigl(
\operatorname{Prime}(r)
\land r\mid\eta
\land I_\kappa(x,y;r)
\bigr).
\]

Given an \(n\times n\) GIR grid, set

\[
a=\prod_i p_i,
\qquad
b=\prod_j q_j,
\qquad
\mu=\prod_i r_{ii}.
\]

Then \(R_\mu\) is a bijection from \(D_a\) to \(D_b\), sending \(p_i\) to \(q_i\).

For a directed graph

\[
G\subseteq[n]\times[n],
\]

put

\[
\nu_G
=
\prod_{(i,j)\in G}r_{ij}.
\]

Define on \(D_a\):

\[
G_{a,b,\mu,\nu}(x,z)
:=
\exists y\,
\bigl(
D_b(y)
\land R_\mu(z,y)
\land R_\nu(x,y)
\bigr).
\]

Then

\[
G_{a,b,\mu,\nu_G}(p_i,p_j)
\iff
(i,j)\in G.
\]

Thus every finite directed graph occurs inside the fixed structure using only four source parameters.

The converse needed for undecidability is equally important. If arbitrary source elements \(a,b,\mu,\nu\) satisfy the first-order condition that \(R_\mu\) is a bijection between the finite sets \(D_a\) and \(D_b\), then \(G_{a,b,\mu,\nu}\) is simply some binary relation on the finite set \(D_a\). It need not come from a canonical GIR grid for the reverse implication.

---

## 12. Undecidability by Trakhtenbrot

Let \(\varphi\) be a sentence in the language of one binary relation. Construct effectively a sentence \(\widehat\varphi\) in the language of \(\mathcal V_{\Delta,\kappa}\) as follows:

1. existentially quantify source variables \(a,b,\mu,\nu\);
2. require \(D_a\) to be nonempty;
3. require \(R_\mu\) to be a bijection from \(D_a\) onto \(D_b\);
4. relativize every graph-domain quantifier of \(\varphi\) to \(D_a\);
5. replace every graph atom \(R(x,z)\) by \(G_{a,b,\mu,\nu}(x,z)\).

This translation is mechanical. It does not inspect, compute, or mention the function \(\kappa\). The profile is already encoded by the single relation symbol \(B_\kappa\) of the fixed structure.

If \(\varphi\) has a finite nonempty model, choose a GIR grid of the same cardinality and encode the model by \(a,b,\mu,\nu\). Then \(\widehat\varphi\) holds.

Conversely, if \(\widehat\varphi\) holds, its witnesses define a finite nonempty set \(D_a\) and a binary relation \(G_{a,b,\mu,\nu}\) on that set satisfying \(\varphi\). Hence \(\varphi\) has a finite model.

Therefore

\[
\varphi\text{ is finitely satisfiable}
\iff
\mathcal V_{\Delta,\kappa}\models\widehat\varphi.
\]

Trakhtenbrot's theorem states that finite satisfiability for first-order structures with a binary relation is undecidable. We conclude:

### Theorem 12.1. Undecidability

If \(P_+(\kappa)\) is infinite, then

\[
\boxed{
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
\text{ is undecidable}.
}
\]

This remains true even when \(\kappa\) is non-computable. Computability of \(\kappa\) is not an input to the reduction.

---

## 13. The exact definability boundary over zero depth

The finite-support direction gives

\[
|P_+(\kappa)|<\infty
\Longrightarrow
B_\kappa
\in
\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,0}).
\]

For the converse, assume \(P_+(\kappa)\) is infinite and suppose, toward a contradiction, that \(B_\kappa\) were parameter-free definable in \(\mathcal V_{\Delta,0}\).

Then \(E_\kappa\) and the fixed ternary isolator \(I_\kappa\) would also become parameter-free definable in \(\mathcal V_{\Delta,0}\). But the zero-depth compression theorem gives finite GIR for every fixed parameter-free isolator in that structure, while Theorem 10.1 gives

\[
\operatorname{GIR}(I_\kappa)=\infty.
\]

Contradiction.

### Theorem 13.1. Exact empty-parameter definability boundary

For every threshold profile \(\kappa\),

\[
\boxed{
B_\kappa
\in
\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,0})
\iff
|P_+(\kappa)|<\infty.
}
\]

The statement is deliberately about empty-parameter definability. No claim is made here about definability after naming arbitrary external parameters.

---

## 14. Main dichotomy

Combining the safe and amplifying sides gives the central theorem.

### Theorem 14.1. Support-Cardinality Valuation Wall

Let

\[
\kappa:\mathbb P\to\mathbb N_0
\]

be arbitrary.

If \(P_+(\kappa)\) is finite, then

\[
\mathcal V_{\Delta,\kappa}
\equiv_{\emptyset\text{-def}}
\mathcal V_{\Delta,0},
\]

ordinary prime order and prime successor are not parameter-free definable, and every fixed parameter-free ternary isolator has finite GIR.

If \(P_+(\kappa)\) is infinite, then one fixed parameter-free ternary formula has infinite GIR, every finite directed graph is uniformly coded, and the complete first-order theory is undecidable.

Consequently,

\[
\boxed{
|P_+(\kappa)|<\infty
\iff
\forall I\;\operatorname{GIR}(I)<\infty,
}
\]

where \(I\) ranges over fixed parameter-free ternary source formulas of the fixed threshold-profile structure.

The wall is therefore a **support-cardinality wall**.

---

## 15. Constant-depth and sparse-depth corollaries

### Corollary 15.1. Every positive constant depth is amplifying

For a fixed \(m\ge1\), let

\[
\kappa(r)=m
\]

for every prime \(r\). Then

\[
P_+(\kappa)=\mathbb P,
\]

so

\[
\exists I_m
\quad
\operatorname{GIR}(I_m)=\infty,
\]

and

\[
\operatorname{Th}(\mathcal V_{\Delta,m})
\]

is undecidable.

Thus depth one is not exceptional. Every fixed positive valuation depth lies on the amplifying side.

### Corollary 15.2. Arbitrarily sparse positive support still amplifies

Let \(S\subseteq\mathbb P\) be any infinite set, even of natural density zero, and let \(\kappa(r)\ge1\) on \(S\) and \(\kappa(r)=0\) outside \(S\). Then the theory is still on the amplifying side.

The proof never invokes density, regular spacing, or computability of \(S\).

### Corollary 15.3. Unbounded depths do not create a further phase

The values \(\kappa(r)\) may tend to infinity arbitrarily fast on \(P_+(\kappa)\). Every finite pattern uses only finitely many finite moduli, and the integral pair \(A,J\) works at all levels. Hence unbounded positive depth remains in the same right-hand phase.

---

## 16. Why the wall sits exactly here

The theorem can be summarized conceptually in three steps.

First, a finite number of deeper places is harmless because every fixed standard prime can be named and each deeper threshold can be compiled into finitely many zero-depth formulas. Finite positive support is therefore only a finite definitional perturbation of \(B_0\).

Second, one positive-depth place already exposes a nontrivial residual condition, but finitely many such places still give only finitely many stationary channels. There is no arbitrarily large moving marker reservoir.

Third, infinitely many positive-depth places provide infinitely many movable residual channels. Adelic independence lets finitely many of them be prescribed simultaneously, and Chebotarev turns those local prescriptions into infinitely many source primes. The GIR grid then converts residual independence into finite graph universality.

So the transition is not

\[
0\to1
\]

as a numerical jump. It is

\[
\text{finite support}
\to
\text{infinite support}
\]

as a logical-combinatorial jump.

---

## 17. Relation to nearby work

The number-theoretic engine is classical-modern rather than model-theoretic: the Galois representations attached to modular forms, adelic open image, and Chebotarev supply simultaneous finite residual control. Loeffler proves adelic openness for non-CM modular forms, which is the decisive structural input used here.

On the logic side, Trakhtenbrot supplies the undecidability endpoint once all finite graphs can be uniformly coded.

There is also contemporary work connecting the Ramanujan tau function directly to undecidable first-order theories. Karimov, Nieuwveld, and Ouaknine show undecidability for a structure containing the function \(n\mapsto|\tau(n)|\), using a different mechanism based on richness or quasi-randomness of the sequence. That structure, language, and coding mechanism are not the ones studied here. The present theorem uses prime-indexed valuation thresholds, a two-sorted bridge to \(\mathbb Q\), adelic residual independence, and a finite-versus-infinite support classification.

Targeted literature searches performed for this release found nearby results on adelic Galois images, logical undecidability from rich sequences, and classical product/locality methods, but no exact theorem matching the threshold-profile support-cardinality dichotomy formulated above. This is a literature-audit observation, not a historical-priority claim.

---

## 18. Claim boundary

The theorem proves a strong expressive dichotomy, but several statements are intentionally not made.

We do **not** claim that ordinary prime order or prime successor becomes definable when \(P_+(\kappa)\) is infinite. Infinite GIR and finite-graph universality show expressive amplification and undecidability, not orientation.

We do **not** claim that all infinite-positive-support profiles are mutually interdefinable.

We do **not** claim that \(B_0\) is definable from every infinite-positive-support profile.

We do **not** claim stability, NIP, simplicity, or another global model-theoretic classification.

We do **not** claim an effective bound for the finite adelic exceptional set \(S_\Delta\) in the formulation used here.

We do **not** claim historical priority beyond the targeted literature audit.

Finally, none of the results depends on Lehmer's conjecture. Possible primes with \(\tau(p)=0\) do not affect the residual pattern construction.

---

## 19. Conclusion

The zero/one valuation boundary was only the first visible slice of a larger phase transition.

For the threshold-profile structures

\[
\mathcal V_{\Delta,\kappa},
\]

the safe side consists exactly of profiles with finitely many positive-depth places. Those structures are parameter-free interdefinable with zero depth and inherit formula-relative compression.

The amplifying side begins as soon as positive depth occurs at infinitely many prime places. It does not matter how sparse those places are, how large the depths are, or whether the profile is computable. Adelic residual independence and Chebotarev convert that infinite support into arbitrary finite Boolean patterns, infinite Grid-Isolation Rank, uniform finite-graph coding, and undecidability.

The phase diagram is therefore

\[
\boxed{
\begin{array}{c}
|P_+(\kappa)|<\infty\\[1mm]
\mathcal V_{\Delta,\kappa}
\equiv_{\emptyset\text{-def}}
\mathcal V_{\Delta,0}\\[1mm]
\forall I\;\operatorname{GIR}(I)<\infty
\end{array}
\quad\Bigg|\quad
\begin{array}{c}
|P_+(\kappa)|=\infty\\[1mm]
\exists I_\kappa\;\operatorname{GIR}(I_\kappa)=\infty\\[1mm]
\text{finite graph universality}\\[1mm]
\operatorname{Th}(\mathcal V_{\Delta,\kappa})\text{ undecidable}
\end{array}
}
\]

The wall is a wall of support cardinality.

---

## References

1. Deligne, P. *La conjecture de Weil. I*. Publications Mathématiques de l'IHÉS **43** (1974), 273-307.
2. Loeffler, D. *Images of adelic Galois representations for modular forms*. Glasgow Mathematical Journal **59** (2017), no. 1, 11-25. DOI: 10.1017/S0017089516000367. arXiv:1411.1789.
3. Ribet, K. A. *On l-adic representations attached to modular forms*. Inventiones Mathematicae **28** (1975), 245-275.
4. Ribet, K. A. *On l-adic representations attached to modular forms. II*. Glasgow Mathematical Journal **27** (1985), 185-194.
5. Trakhtenbrot, B. A. *The impossibility of an algorithm for the decision problem on finite classes*. Doklady Akademii Nauk SSSR **70** (1950), 569-572.
6. Kirst, D.; Larchey-Wendling, D. *Trakhtenbrot's Theorem in Coq: A Constructive Approach to Finite Model Theory*. IJCAR 2020; arXiv:2004.07390.
7. Karimov, T.; Nieuwveld, J.; Ouaknine, J. *Rich sequences and decidability of logical theories*. Submitted, 2026.
8. Malachevsky, A. *Reflections on Finite Stationary Locality with Commander Sol*. Zenodo, 2026. DOI: 10.5281/zenodo.22110465.
9. Malachevsky, A. *Reflections on a One-Step Valuation Jump with Commander Sol: From Private Denominator Support to Residual-Cubic Grid Amplification*. Zenodo, 2026. DOI: 10.5281/zenodo.22116714.
10. Malachevsky, A. *Reflections on the Exact Zero/One Valuation Boundary with Commander Sol: Uniform Zero-Depth Compression versus Residual-Cubic Grid Amplification*. Zenodo, 2026. DOI: 10.5281/zenodo.22131827.
