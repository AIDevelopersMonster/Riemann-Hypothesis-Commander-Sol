# Sixth Stage — Multiplicity Trace Transform and Finite-Projection Blindness

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; publication status not assigned

## 1. Aim

The previous stage separated the prime-only structure into two exact isomorphism-level channels

\[
(G_\kappa,\mu_\kappa),
\]

where \(G_\kappa\) is the active skeleton and \(\mu_\kappa\) records multiplicities of exact finite active neighborhoods of external points.

This stage freezes the active geometry and analyzes the multiplicity channel itself.

The conclusions proved here are:

1. for binary profiles, the multiplicity data is exactly a trace-counting transform of one fixed residual divisor hypergraph;
2. finite Chebotarev pattern realization forces every finite trace cylinder to have infinite total multiplicity on zero-density good supports;
3. nevertheless, that finite-projection information is model-theoretically insufficient: there are abstract locally finite prime-only normal forms with empty active skeleton and the same infinite finite-pattern extension behavior, one decidable and others with arbitrary graph complexity;
4. therefore the remaining arithmetic problem is global atomic trace control: which exact trace fibers can be zero, finite, or infinite.

No claim is made that the wild abstract multiplicity spectra constructed below are arithmetically realizable for the Ramanujan divisor system.

---

## 2. Binary profiles and the residual divisor hypergraph

Let

\[
N_p:=\tau(p)^2-p^{11}.
\tag{1}
\]

For every prime \(p\),

\[
N_p\ne0,
\tag{2}
\]

because equality would imply

\[
2v_p(\tau(p))=11,
\tag{3}
\]

which is impossible.

Hence

\[
D(p):=\{r\in\mathbb P:r\mid N_p\}
\tag{4}
\]

is finite.

Fix a binary profile determined by a support \(S\subseteq\mathbb P\):

\[
\kappa_S(r)=
\begin{cases}
1,&r\in S,\\
0,&r\notin S.
\end{cases}
\tag{5}
\]

For an external prime \(p\notin S\), define

\[
T_S(p):=\{r\in S:E_{\kappa_S}(p;r)\}.
\tag{6}
\]

### Theorem 2.1 — Exact Trace Formula

For every \(p\notin S\),

\[
\boxed{T_S(p)=D(p)\cap S.}
\tag{7}
\]

For active primes \(p,r\in S\) with \(p\ne r\),

\[
p\to_S r
\iff
r\in D(p)\cap S.
\tag{8}
\]

### Proof

If \(p\notin S\) and \(r\in S\), then \(p\ne r\) and \(\kappa_S(r)=1\), so

\[
E_{\kappa_S}(p;r)
\iff
r\mid \tau(p)^2-p^{11}
\iff
r\in D(p).
\tag{9}
\]

Intersecting with \(S\) gives (7). The same calculation gives (8) for distinct active primes. ∎

### Definition 2.2 — Residual divisor hypergraph

The fixed family

\[
\mathscr D_\Delta:=\{D(p):p\in\mathbb P\}
\tag{10}
\]

is the residual divisor hypergraph of \(\Delta\).

### Definition 2.3 — Trace multiplicity transform

For finite \(F\subseteq S\), put

\[
\mu_S(F)
:=
\left|
\{p\in\mathbb P\setminus S:D(p)\cap S=F\}
\right|.
\tag{11}
\]

Thus the multiplicity channel is exactly the fiber-counting transform

\[
S\longmapsto(F\mapsto\mu_S(F))
\tag{12}
\]

of the single arithmetic hypergraph \(\mathscr D_\Delta\).

---

## 3. Finite Chebotarev independence gives cylinder infinitude

Assume that \(S\) is contained outside the fixed finite exceptional marker set needed for depth-one finite-pattern realization and that \(S\) has Dirichlet density zero.

For finite disjoint \(A,B\subseteq S\), define

\[
\mathcal C(A,B)
:=
\{F\in\operatorname{Fin}(S):A\subseteq F,\ F\cap B=\varnothing\}.
\tag{13}
\]

### Theorem 3.1 — Cylinder Infinitude

For every finite disjoint \(A,B\subseteq S\),

\[
\boxed{
\sum_{F\in\mathcal C(A,B)}\mu_S(F)=\aleph_0.
}
\tag{14}
\]

### Proof

Finite residual pattern realization gives a positive-Dirichlet-density set of primes \(p\) satisfying

\[
r\mid N_p\quad(r\in A),
\tag{15}
\]

and

\[
r\nmid N_p\quad(r\in B).
\tag{16}
\]

Removing the zero-density set \(S\) leaves infinitely many external source primes with this pattern.

For each such source prime,

\[
F_p=D(p)\cap S
\tag{17}
\]

is finite and belongs to \(\mathcal C(A,B)\). Every external source contributes to exactly one atomic multiplicity \(\mu_S(F_p)\). Hence the cardinal sum over the cylinder is countably infinite. ∎

### Corollary 3.2

On zero-density good supports, every finite Boolean trace cylinder has infinite total mass.

### Limitation

The theorem does not determine any individual value

\[
\mu_S(F).
\tag{18}
\]

The total infinite mass of a cylinder can be distributed among infinitely many exact traces in very different ways.

---

## 4. Abstract multiplicity models with the active skeleton fixed to empty

Let \(S\) be a countably infinite active set and let \(C\) be a countable external set. Assume:

- the active skeleton is empty;
- each external point \(c\in C\) has a finite neighborhood \(N(c)\subseteq S\).

For finite \(F\subseteq S\), let

\[
\mu(F):=|\{c\in C:N(c)=F\}|.
\tag{19}
\]

Recover the prime-only relation by

\[
E(p;r)
\iff
p\ne r\land(\neg\operatorname{Pos}(r)\lor R(p,r)),
\tag{20}
\]

and

\[
I(p,q;r)
\iff
E(p;r)\land E(q;r).
\tag{21}
\]

If \(\mu(\varnothing)=\aleph_0\), then \(\operatorname{Pos}\) is parameter-free definable from \(I\): every active column has an external nonneighbor, while every inactive column is a co-singleton.

---

## 5. A decidable frozen-skeleton point

### Theorem 5.1 — Saturated empty-skeleton decidability

Suppose

\[
\mu(F)=\aleph_0
\qquad
\text{for every finite }F\subseteq S.
\tag{22}
\]

Then the complete first-order theory of the resulting structure is decidable.

### Proof

Represent an external point by a pair

\[
(F,i),
\qquad
F\in\operatorname{Fin}(S),\ i\in\mathbb N,
\tag{23}
\]

with incidence

\[
R((F,i),s)\iff s\in F.
\tag{24}
\]

Translate first-order formulas into the weak monadic theory of the countably infinite pure equality set \(S\), together with an auxiliary countably infinite pure equality copy-index sort for \(i\).

External equality becomes

\[
(F,i)=(F',j)
\iff
F=F'\land i=j,
\tag{25}
\]

and incidence becomes (24).

For finitely many weak-monadic set variables, the pure set \(S\) splits into finitely many Boolean membership cells. A formula of fixed quantifier rank requires only finitely many witnesses from each cell, so the weak monadic theory of an infinite pure equality set is decidable by finite membership-type analysis. The copy-index sort is also pure equality and is decided by finite equality patterns.

Therefore every first-order sentence is effectively reduced to a decidable finite type calculation. ∎

---

## 6. Multiplicity memory alone can encode arbitrary graph complexity abstractly

Let \(H=(S,\sim_H)\) be any countable simple graph on the active set. Define

\[
\mu_H(F)=\aleph_0
\qquad\text{if }|F|\ne2,
\tag{26}
\]

and for distinct \(x,y\in S\),

\[
\mu_H(\{x,y\})=
\begin{cases}
1,&x\sim_Hy,\\
0,&x\not\sim_Hy.
\end{cases}
\tag{27}
\]

Let \(\mathfrak M_H\) be the corresponding empty-active-skeleton structure.

Define \(\operatorname{ExactPair}(c;x,y)\) by

\[
\neg\operatorname{Pos}(c)
\land
\operatorname{Pos}(x)
\land
\operatorname{Pos}(y)
\land x\ne y
\land R(c,x)
\land R(c,y)
\land
\forall z\bigl(
\operatorname{Pos}(z)\land R(c,z)
\to(z=x\lor z=y)
\bigr).
\tag{28}
\]

### Theorem 6.1 — Multiplicity-Only Graph Interpretation

The formula

\[
\operatorname{Adj}_H(x,y)
:\iff
\exists!c\,\operatorname{ExactPair}(c;x,y)
\tag{29}
\]

defines exactly the edge relation of \(H\). Hence \(H\) is parameter-free first-order interpretable in \(\mathfrak M_H\).

### Proof

For distinct active \(x,y\), the number of external points satisfying (28) is exactly \(\mu_H(\{x,y\})\). By (27), this number is one exactly for graph edges and zero otherwise. ∎

### Corollary 6.2 — Undecidable multiplicity-only models

There exist empty-active-skeleton abstract prime-only normal forms with undecidable complete theory.

### Proof

Choose a nonrecursive set \(A\subseteq\mathbb N\). Let \(H_A\) be the disjoint union of one clique \(K_{n+3}\) for every \(n\in A\), together with countably infinitely many isolated vertices.

For every \(n\), there is an effective graph sentence \(\chi_n\) saying that a connected component is exactly \(K_{n+3}\). Thus

\[
H_A\models\chi_n
\iff
n\in A.
\tag{30}
\]

Theorem 6.1 effectively translates \(\chi_n\) to a prime-only sentence \(\widehat\chi_n\), giving

\[
\mathfrak M_{H_A}\models\widehat\chi_n
\iff
n\in A.
\tag{31}
\]

Therefore

\[
A\le_m\operatorname{Th}(\mathfrak M_{H_A}),
\tag{32}
\]

so the complete theory is undecidable. ∎

---

## 7. The abstract wild models satisfy the same finite cylinder richness

### Theorem 7.1 — Cylinder-Rich Multiplicity Universality

For every countable graph \(H\), the multiplicity function \(\mu_H\) satisfies

\[
\sum_{F\in\mathcal C(A,B)}\mu_H(F)=\aleph_0
\tag{33}
\]

for every finite disjoint \(A,B\subseteq S\).

### Proof

Since \(S\) is infinite, choose a finite

\[
F\supseteq A,
\qquad
F\cap B=\varnothing,
\qquad
|F|\ge3.
\tag{34}
\]

Then \(\mu_H(F)=\aleph_0\) by (26), so the entire cylinder sum is \(\aleph_0\). ∎

### Theorem 7.2 — Finite-Projection Blindness

There exist two countable abstract prime-only normal forms with all of the following properties in common:

1. the active skeleton is empty;
2. every external neighborhood is finite;
3. every finite EDGE/NONEDGE pattern on active markers is realized by infinitely many external points;

but one has decidable complete theory and the other has undecidable complete theory.

### Proof

Take the saturated model of Theorem 5.1 for the decidable structure and \(\mathfrak M_{H_A}\) from Corollary 6.2 for the undecidable structure. The common finite-pattern property is immediate in the saturated model and follows from Theorem 7.1 in \(\mathfrak M_{H_A}\). ∎

### Consequence 7.3

Finite-pattern extension data of the type supplied by Chebotarev cannot by itself classify the multiplicity channel.

---

## 8. Continuum many theories with the active skeleton frozen abstractly

### Corollary 8.1

There are

\[
\boxed{2^{\aleph_0}}
\tag{35}

pairwise distinct complete theories of countable abstract prime-only normal forms such that:

- the active skeleton is empty;
- every external neighborhood is finite;
- every finite trace cylinder has infinite multiplicity.

### Proof

For each \(A\subseteq\mathbb N\), form \(H_A\) as above and then \(\mathfrak M_{H_A}\). If \(A\ne B\), choose \(n\in A\triangle B\). The translated sentence \(\widehat\chi_n\) holds in exactly one of the two structures, so their complete theories differ. There are \(2^{\aleph_0}\) choices of \(A\). ∎

---

## 9. Arithmetic versus abstract multiplicity memory

For actual binary Ramanujan profiles, the multiplicities must have the special form

\[
\boxed{
\mu_S(F)
=
\left|
\{p\notin S:D(p)\cap S=F\}
\right|.
}
\tag{36}
\]

Finite Chebotarev independence controls only finite projections

\[
D(p)\cap R
\qquad(R\subseteq S\text{ finite}),
\tag{37}
\]

whereas an exact atom requires simultaneous control on the whole support:

\[
D(p)\cap S=F.
\tag{38}
\]

Thus the difference between finite pattern realization and exact multiplicity is the difference between finite local conditions and an infinite avoidance condition.

---

## 10. Global Trace Atom Control

For finite \(F\subseteq S\), call

\[
\operatorname{Atom}_S(F):=\mu_S(F)
\tag{39}
\]

the exact trace atom.

Earlier priority constructions prove that one extreme is arithmetically realizable: there are arbitrarily sparse independent supports with

\[
\operatorname{Atom}_S(F)=\aleph_0
\qquad
\text{for every finite }F\subseteq S.
\tag{40}
\]

The unresolved issue is upper control of individual atoms while the active skeleton is kept fixed.

### Open Problem 10.1 — Finite atom problem

Does there exist an infinite good independent support \(S\) and finite \(F\subseteq S\) such that

\[
0<\mu_S(F)<\aleph_0?
\tag{41}
\]

### Open Problem 10.2 — Zero-atom programming

Can one construct an infinite good independent support \(S\) for which selected finite sets \(F\subseteq S\) satisfy

\[
\mu_S(F)=0
\tag{42}
\]

while other selected finite sets have positive or infinite multiplicity?

### Open Problem 10.3 — Arithmetic multiplicity universality

Can the relation

\[
M_S(x,y)
:\iff
\mu_S(\{x,y\})=1
\tag{43}
\]

or another fixed finite-multiplicity relation interpret an undecidable graph while the active skeleton remains empty?

A positive answer would prove that multiplicity memory alone is arithmetically wild. A negative answer would reveal a new rigidity of the residual divisor hypergraph.

---

## 11. Why exact upper control is a divisor-coverage problem

Suppose a source prime \(p\) has current trace

\[
D(p)\cap S_n=F
\tag{44}
\]

on a finite partial support \(S_n\).

To ensure that its final exact trace is not \(F\), some future support prime must belong to

\[
D(p)\setminus F.
\tag{45}
\]

If the active skeleton is required to remain empty, a newly admitted support prime \(r\) must also preserve both directional nonincidences against every earlier active prime \(s\):

\[
r\notin D(s),
\tag{46}
\]

and

\[
s\notin D(r).
\tag{47}
\]

Previously selected exact-neighborhood witnesses impose additional finite avoidance requirements.

Finite-pattern Chebotarev gives freedom to choose source primes with prescribed behavior at chosen markers. It does not provide freedom to choose a prime divisor of one already fixed integer \(N_p\) while simultaneously imposing new source-side residual conditions on that divisor.

This is a qualitatively different number-theoretic problem and marks the limit of the current finite-pattern machinery.

---

## 12. Revised two-channel picture

The branch now separates into two complexity channels.

### Channel A — Active-skeleton memory

Already established:

- arbitrary backward DAGs are programmable;
- undecidability may occur with bounded regular-positive GIR;
- tree-depth 2 already supports nonrecursive component spectra;
- saturated profiles inherit decidability from suitable weak-monadic tameness of the skeleton.

### Channel B — Exact multiplicity memory

Established here abstractly:

- even with the active skeleton empty, exact multiplicity atoms can interpret arbitrary graph complexity;
- finite-cylinder richness does not prevent this;
- complete saturation gives a decidable point.

For the actual Ramanujan structure, Channel B is reduced exactly to the trace transform (36), and its realizability range remains open.

The new frontier is therefore

\[
\boxed{
\textbf{Global Trace Atom Control / Residual Divisor Coverage Frontier}.
}
\tag{48}
\]

---

## 13. Audit

The following points were checked.

1. \(D(p)\) is finite because \(N_p\ne0\).
2. The exact trace formula is stated for external \(p\), so no diagonal exception is lost.
3. Cylinder infinitude uses density zero of the support to ensure infinitely many pattern realizers remain external.
4. Cylinder infinitude is only a cylinder-sum statement; no individual atom is claimed infinite.
5. In the abstract graph interpretation, active and external points are separated by the definable active predicate.
6. Larger exact neighborhoods do not create false pair edges because ExactPair universally excludes additional active neighbors.
7. The abstract wild models still realize every finite partial pattern infinitely often.
8. No arithmetic realization of the wild abstract multiplicity spectrum is claimed.
9. The remaining exact-atom problem requires control of prime divisors of fixed integers \(N_p\), which is not supplied by the existing source-prime Chebotarev construction.

**Audit verdict:** the proved statements are internally consistent. Arithmetic multiplicity universality remains open and requires genuinely new input beyond finite-pattern Chebotarev realization.
