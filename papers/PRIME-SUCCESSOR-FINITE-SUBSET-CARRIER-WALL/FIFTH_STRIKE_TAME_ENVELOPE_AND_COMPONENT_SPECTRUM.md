# Fifth Strike — Saturated Tame Envelope and the Component-Spectrum Obstruction

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-29  
**Status:** proved statements only; publication status not assigned

## 1. Aim

The fourth strike showed that the prime-only reduct is parameter-free interdefinable with a locally finite incidence system over the definable positive-depth support and that the induced active skeleton can be programmed with arbitrary backward-DAG complexity.

The present strike asks for a genuinely tame region and for the first precise obstruction to tameness.

The main results are:

1. an exact isomorphism normal form by **active skeleton + external finite-neighborhood multiplicities**;
2. a simultaneous **saturated extension theorem**: every countable backward DAG can be realized on arbitrarily sparse positive support while every finite active neighborhood is realized by infinitely many external primes;
3. a decidability transfer theorem from weak monadic second-order logic of the active skeleton to first-order logic of the saturated prime-only reduct;
4. a concrete structural tame class: saturated profiles whose active skeleton has uniformly bounded connected-component size are decidable; in particular bounded Gaifman degree + bounded tree-depth is sufficient;
5. a sharp obstruction: bounded tree-depth alone is not enough. Even saturated active skeletons that are forests of tree-depth 2 can have undecidable theory through a nonrecursive component-size spectrum;
6. continuum many pairwise distinct complete theories already occur inside saturated, zero-density, tree-depth-2 star forests.

No theorem below is left without proof.

---

## 2. Setup

Let

\[
\mathcal I_\kappa=(\mathbb P,I_\kappa)
\]

be the prime-only residual structure, and put

\[
E_\kappa(x;r):=I_\kappa(x,x;r).
\]

Let

\[
S_\kappa=P_{\mathrm{pos}}(\kappa)
\]

be the positive-depth support. By the fourth strike,

\[
\operatorname{Pos}(r):=\exists p\,(p\ne r\land\neg E_\kappa(p;r))
\]

defines exactly \(S_\kappa\), and

\[
R_\kappa(p,r):=\operatorname{Pos}(r)\land E_\kappa(p;r)
\]

has finite left fibers.

For each prime \(p\), define its active neighborhood

\[
N_\kappa(p):=\{r\in S_\kappa:R_\kappa(p,r)\}.
\tag{1}
\]

Every \(N_\kappa(p)\) is finite.

The active skeleton is

\[
G_\kappa=(S_\kappa,R_\kappa\upharpoonright S_\kappa^2).
\tag{2}
\]

For every finite \(F\subseteq S_\kappa\), define the external multiplicity

\[
\mu_\kappa(F)
:=
\left|
\{c\in\mathbb P\setminus S_\kappa:N_\kappa(c)=F\}
\right|
\in\mathbb N_0\cup\{\aleph_0\}.
\tag{3}
\]

---

## 3. Exact skeleton–multiplicity normal form

### Theorem 3.1 — Isomorphism classification by active data

Let \(\kappa\) and \(\lambda\) be two threshold profiles. Then the prime-only incidence normal forms associated with \(\mathcal I_\kappa\) and \(\mathcal I_\lambda\) are isomorphic if and only if there exists an isomorphism

\[
f:G_\kappa\to G_\lambda
\tag{4}
\]

such that for every finite \(F\subseteq S_\kappa\),

\[
\mu_\kappa(F)=\mu_\lambda(f[F]).
\tag{5}
\]

Consequently the isomorphism type of \(\mathcal I_\kappa\) is determined exactly by the pair

\[
\boxed{(G_\kappa,\mu_\kappa)}.
\tag{6}
\]

### Proof

Any isomorphism of prime-only incidence normal forms preserves the parameter-free definable active set and therefore restricts to an isomorphism of active skeletons. It also sends an external point with active neighborhood \(F\) to an external point with neighborhood \(f[F]\), hence preserves every multiplicity (3). This proves necessity.

Conversely, suppose \(f\) satisfies (4)-(5). For each finite \(F\subseteq S_\kappa\), choose a bijection between the external fiber

\[
C_F^\kappa
:=
\{c\notin S_\kappa:N_\kappa(c)=F\}
\]

and

\[
C_{f[F]}^\lambda.
\]

Such a bijection exists by (5), whether the common multiplicity is finite or countably infinite. The union of \(f\) on the active part with these fiberwise bijections is a bijection of the whole prime universe. It preserves active incidence by (4) and external-to-active incidence by construction. The zero-depth columns are recovered uniformly from the active predicate, so it preserves \(E\), hence also \(I\). ∎

### Definition 3.2 — External saturation

A profile \(\kappa\) is **externally saturated** if

\[
\mu_\kappa(F)=\aleph_0
\tag{7}
\]

for every finite \(F\subseteq S_\kappa\).

### Corollary 3.3

Within the externally saturated class, the isomorphism type of the full prime-only reduct is determined by the active skeleton alone.

### Proof

All multiplicities in (5) are identically \(\aleph_0\). Apply Theorem 3.1. ∎

---

## 4. Simultaneous programming and external saturation

The fourth strike programmed the active skeleton. The third strike saturated the external finite-neighborhood spectrum in the independent case. These two constructions can be merged.

Call a countable loopless directed graph \(G=(V,\to)\) a **backward DAG** if it has an enumeration

\[
V=\{v_0,v_1,v_2,\dots\}
\]

with

\[
v_i\to v_j\Longrightarrow j<i.
\tag{8}
\]

### Theorem 4.1 — Saturated Extension Theorem

Let \(G\) be any countable backward DAG, and let

\[
B_0<B_1<B_2<\cdots
\]

be any prescribed sequence of integers. Then there exists a binary profile

\[
\kappa_G:\mathbb P\to\{0,1\}
\tag{9}
\]

whose positive support

\[
S=\{s_0,s_1,s_2,\dots\}
\]

satisfies

\[
s_n>B_n,
\tag{10}
\]

such that:

1. the active skeleton is exactly \(G\) under \(s_n\leftrightarrow v_n\);
2. for every finite \(F\subseteq S\), there are infinitely many primes \(c\notin S\) with
   \[
   N_{\kappa_G}(c)=F.
   \tag{11}
   \]

Thus \(\kappa_G\) is externally saturated.

### Proof

We run a priority construction. At every finite stage only finitely many primes are forbidden.

Fix a schedule of witness requirements

\[
(F,k),
\qquad
F\subseteq\mathbb N\text{ finite},\ k\in\mathbb N,
\tag{12}
\]

such that each pair occurs once and a requirement involving indices in \(F\) is handled only after all \(s_i\) with \(i\in F\) have been chosen. Since \(k\) ranges over \(\mathbb N\), each finite index set receives infinitely many witness requirements.

Assume \(s_0,\dots,s_{n-1}\) have already been chosen, together with finitely many external witnesses from earlier stages. Maintain a finite forbidden set \(Q_n\) containing:

- all previously chosen support primes and external witnesses;
- the fixed finite exceptional primes required by finite-pattern realization;
- every prime divisor outside the already chosen support of every integer \(N_c=\tau(c)^2-c^{11}\) belonging to an earlier external witness \(c\).

To choose \(s_n\), let

\[
T_n=\{s_j:j<n\text{ and }v_n\to v_j\}.
\tag{13}
\]

Finite-pattern realization gives infinitely many primes \(p\) satisfying

\[
E(p;s_j)\iff s_j\in T_n
\qquad(j<n).
\tag{14}
\]

Choose such a prime outside \(Q_n\), outside the prime divisors of all previous \(N_{s_i}\) needed to kill reverse edges, and larger than \(B_n\). This is possible because the excluded set is finite whereas the realization set is infinite. Put \(s_n=p\). Exactly as in the fourth strike, (14) fixes all new-to-old active edges and divisor avoidance forces every old-to-new active edge to be absent. Hence the programmed active skeleton remains correct.

Now handle the next scheduled requirement \((F,k)\) whose indices have all appeared by stage \(n\). Let

\[
F_S=\{s_i:i\in F\}.
\]

Apply finite-pattern realization to the whole current marker set

\[
S_n=\{s_0,\dots,s_n\}
\]

with EDGE exactly on \(F_S\) and NONEDGE on \(S_n\setminus F_S\). Choose a realizing prime \(c\) outside the finite set of all previously used primes. Then

\[
N_{\kappa_G}(c)\cap S_n=F_S.
\tag{15}
\]

The nonzero integer

\[
N_c=\tau(c)^2-c^{11}
\]

has finitely many prime divisors. Add to the forbidden set for all future support choices every prime divisor of \(N_c\) which is not already in \(S_n\), and also add \(c\) itself. Therefore no future support prime can divide \(N_c\). Since the profile has depth one on the support, (15) can never gain a future active neighbor. Hence in the final structure

\[
N_{\kappa_G}(c)=F_S.
\tag{16}
\]

At each stage only finitely many new primes are forbidden, so the induction never stalls. Every pair \((F,k)\) is eventually handled, and varying \(k\) yields infinitely many distinct witnesses for each finite \(F\). This proves external saturation and the exact active skeleton simultaneously. ∎

### Corollary 4.2 — Zero-density saturated realization

Every countable backward DAG has an externally saturated realization whose positive support has natural and Dirichlet density zero.

### Proof

Take for example

\[
B_n=2^{n^2}.
\]

Then \(s_n>2^{n^2}\), so the support has natural density zero and

\[
\sum_n\frac1{s_n}<\infty,
\]

which implies Dirichlet density zero. ∎

---

## 5. Canonical saturated model over a skeleton

For a countable directed graph \(G=(S,R_G)\), define \(\operatorname{Sat}(G)\) as follows.

The active part is \(S\). For every finite \(F\subseteq S\), add countably many external points

\[
(F,i),\qquad i\in\mathbb N.
\tag{17}
\]

The active incidence is \(R_G\), and an external point has exactly the neighborhood encoded by its first coordinate:

\[
R((F,i),s)\iff s\in F.
\tag{18}
\]

There are no marker columns outside \(S\); the original zero-depth behavior is recovered by the interdefinition from the fourth strike.

By Corollary 3.3, every externally saturated prime-only reduct with active skeleton \(G\) is isomorphic to this canonical model.

---

## 6. Weak-monadic transfer

Write \(\operatorname{WMSO}(G)\) for weak monadic second-order logic of \(G\): first-order variables range over vertices and monadic second-order variables range over finite subsets of vertices.

### Theorem 6.1 — Saturated Decidability Transfer

If \(\operatorname{WMSO}(G)\) is decidable, then the first-order theory

\[
\operatorname{Th}(\operatorname{Sat}(G))
\tag{19}
\]

is decidable.

Consequently every externally saturated prime-only profile with active skeleton \(G\) has decidable complete first-order theory whenever \(\operatorname{WMSO}(G)\) is decidable.

### Proof

We give an effective translation of first-order formulas of \(\operatorname{Sat}(G)\).

Represent an active element simply by a vertex variable \(s\in S\). Represent an external element \((F,i)\) by:

- a weak-monadic finite-set variable \(F\subseteq S\);
- a copy-index variable \(i\) living in an auxiliary countably infinite pure equality sort \(C\).

For external representatives,

\[
(F,i)=(F',j)
\iff
F=F'\land i=j,
\tag{20}
\]

and

\[
R((F,i),s)
\iff
s\in F.
\tag{21}
\]

For active representatives the relation is just \(R_G\). A variable of the original one-sorted structure is translated by a finite disjunction according to whether it is active or external. Thus every first-order formula is effectively translated into the disjoint combination of:

1. \(\operatorname{WMSO}(G)\) on the vertex/finite-set sorts;
2. the first-order theory of the infinite pure equality sort \(C\).

The pure equality sort has quantifier elimination: a formula in finitely many index variables depends only on their finite equality pattern, and existential quantification is decided by checking whether a requested new equality class must be distinct from finitely many existing classes; an infinite set always supplies such a point.

Therefore copy-index variables can be eliminated effectively by a finite case split over equality types. What remains is a finite Boolean combination of \(\operatorname{WMSO}(G)\)-sentences. By hypothesis those are decidable. Hence the original first-order sentence is decidable. ∎

### Remark 6.2

The theorem is a one-way tame transfer. It does not claim that undecidability of \(\operatorname{WMSO}(G)\) is necessary for undecidability of \(\operatorname{Sat}(G)\).

---

## 7. A structural tame class

We now obtain a completely internal sufficient condition on the active skeleton.

### Lemma 7.1 — WMSO decidability for uniformly bounded components

Let \(G\) be a countable directed graph whose Gaifman connected components all have size at most a fixed integer \(M\). Then \(\operatorname{WMSO}(G)\) is decidable.

### Proof

There are only finitely many isomorphism types

\[
T_1,\dots,T_t
\tag{22}
\]

of finite directed graphs of size at most \(M\). Hence \(G\) is a disjoint union of \(m_i\) copies of \(T_i\), where each

\[
m_i\in\mathbb N_0\cup\{\aleph_0\}.
\tag{23}
\]

There are only finitely many numbers \(m_i\), so their finite values and the information “infinite” may be hard-coded into a decision procedure for this fixed structure.

For each component type \(T_i\), let \(C_i\) be its set of component copies. Choose once and for all an enumeration of the vertices of \(T_i\). A vertex of a copy of \(T_i\) is represented by a pair

\[
(c,j),
\qquad
c\in C_i,\ j\in V(T_i).
\tag{24}
\]

Since the second coordinate ranges over a finite set, every first-order vertex variable can be eliminated by a finite case split over \(i,j\).

A finite-set variable \(X\subseteq V(G)\) is represented by finitely many finite subsets

\[
X_{i,j}\subseteq C_i,
\tag{25}
\]

where \(c\in X_{i,j}\) means that the \(j\)-th vertex in the \(c\)-copy of \(T_i\) belongs to \(X\). Membership and the edge relation reduce to equality of copy indices together with the fixed finite adjacency tables of the \(T_i\).

Thus every WMSO sentence of \(G\) reduces effectively to a finite many-sorted weak monadic theory of pure equality on the sorts \(C_i\). For a finite sort its exact finite size is hard-coded; for a countably infinite pure equality sort, weak monadic formulas are decided by finite equality/cardinality patterns: with finitely many element and finite-set variables, the universe is partitioned into finitely many Boolean membership cells, and a formula of fixed quantifier rank can distinguish only finitely many required witnesses in each cell. Quantifier elimination proceeds by enumerating these finitely many cell-cardinality possibilities, truncating “large enough” cells to an infinite case.

Hence the resulting weak monadic theory is decidable, and so is \(\operatorname{WMSO}(G)\). ∎

### Theorem 7.2 — Uniform-Component Tame Theorem

If \(\kappa\) is externally saturated and the connected components of its active skeleton have uniformly bounded size, then

\[
\boxed{
\operatorname{Th}(\mathcal I_\kappa)
\text{ is decidable}.
}
\tag{26}
\]

### Proof

Apply Lemma 7.1 and Theorem 6.1. ∎

### Corollary 7.3 — Bounded degree + bounded tree-depth

Suppose \(\kappa\) is externally saturated and the underlying Gaifman graph of its active skeleton has both:

- maximum degree at most \(D<\infty\);
- tree-depth at most \(h<\infty\).

Then \(\operatorname{Th}(\mathcal I_\kappa)\) is decidable.

### Proof

A graph of tree-depth at most \(h\) contains no path on \(2^h\) vertices, because

\[
\operatorname{td}(P_n)=\lceil\log_2(n+1)\rceil.
\]

Hence every connected component has uniformly bounded diameter. Together with degree bound \(D\), the elementary breadth-first-search bound gives a uniform finite bound on component size. Theorem 7.2 applies. ∎

This gives a genuine structural tame region which is strictly broader than the completely independent active skeleton.

---

## 8. First obstruction: tree-depth two is already enough for undecidability

Bounded tree-depth by itself does **not** imply tameness. The obstruction is not graph depth but the unbounded component-size spectrum.

Let

\[
A\subseteq\mathbb N_{\ge1}
\]

be any set. Define a directed star forest \(G_A\) as follows:

- for each \(n\in A\), include one component with a center \(c_n\) and exactly \(n\) leaves \(\ell_{n,1},\dots,\ell_{n,n}\);
- orient every edge
  \[
  c_n\to \ell_{n,j};
  \tag{27}
  \]
- add countably infinitely many isolated vertices.

The underlying Gaifman graph is a forest of tree-depth at most \(2\). By listing the leaves of each finite star before its center, component by component, \(G_A\) is a backward DAG.

For every \(n\ge1\), let \(\sigma_n\) be the first-order graph sentence saying:

> there is a connected component consisting of exactly one vertex with directed edges to exactly \(n\) distinct leaves and no other incident edges.

This is an effective finite sentence: existentially name the center and \(n\) leaves, require precisely the star incidences among them, and universally require that every vertex adjacent in either direction to one of the named vertices already belongs to the named tuple.

Then

\[
G_A\models\sigma_n
\iff
n\in A.
\tag{28}
\]

### Theorem 8.1 — Tree-Depth-Two Spectrum Obstruction

If \(A\subseteq\mathbb N\) is nonrecursive, there exists an externally saturated binary threshold profile \(\kappa_A\) whose positive support has Dirichlet density zero and whose active skeleton is a forest of tree-depth at most \(2\), yet

\[
\boxed{
\operatorname{Th}(\mathcal I_{\kappa_A})
\text{ is undecidable}.
}
\tag{29}
\]

### Proof

Apply the Saturated Extension Theorem, with sufficiently fast growth bounds, to \(G_A\). This yields an externally saturated zero-density binary profile whose active skeleton is exactly \(G_A\).

The active support and active incidence are parameter-free definable in \(\mathcal I_{\kappa_A}\). Therefore each sentence \(\sigma_n\) has an effective translation \(\widehat\sigma_n\) in the prime-only language satisfying

\[
\mathcal I_{\kappa_A}\models\widehat\sigma_n
\iff
G_A\models\sigma_n
\iff
n\in A.
\tag{30}
\]

Hence

\[
A\le_m\operatorname{Th}(\mathcal I_{\kappa_A}).
\tag{31}
\]

If the latter theory were decidable, then \(A\) would be recursive, contradiction. ∎

### Corollary 8.2

The following conditions, even taken simultaneously, do not force prime-only decidability:

- binary thresholds \(\kappa\in\{0,1\}\);
- infinite positive support;
- Dirichlet density zero;
- external saturation;
- active skeleton a forest;
- active tree-depth at most \(2\).

The missing ingredient is effective control of the **component spectrum**.

---

## 9. Continuum spectrum inside saturated tree-depth two

### Corollary 9.1 — Continuum many complete theories

There are

\[
2^{\aleph_0}
\tag{32}
\]

pairwise distinct complete prime-only theories of externally saturated binary profiles such that every positive support has Dirichlet density zero and every active skeleton is a forest of tree-depth at most \(2\).

### Proof

For each \(A\subseteq\mathbb N_{\ge1}\), apply Theorem 4.1 to the star forest \(G_A\) and impose fast growth. If \(A\ne B\), choose

\[
n\in A\triangle B.
\]

Then the translated sentence \(\widehat\sigma_n\) holds in exactly one of \(\mathcal I_{\kappa_A}\) and \(\mathcal I_{\kappa_B}\). Hence the complete theories are distinct. There are \(2^{\aleph_0}\) choices of \(A\), and a countable language has at most \(2^{\aleph_0}\) complete theories. ∎

---

## 10. Revised tame/wild picture

The prime-only reduct has an exact two-layer invariant:

\[
\boxed{
\text{active skeleton }G_\kappa
+
\text{external multiplicity function }\mu_\kappa.
}
\tag{33}
\]

External saturation removes the second layer entirely. In that canonical envelope,

\[
\boxed{
\operatorname{WMSO}(G_\kappa)\text{ decidable}
\Longrightarrow
\operatorname{Th}(\mathcal I_\kappa)\text{ decidable}.
}
\tag{34}
\]

A robust structural sufficient condition is

\[
\boxed{
\text{bounded component size}
\Longrightarrow
\text{decidable saturated prime-only theory}.
}
\tag{35}
\]

and therefore

\[
\boxed{
\text{bounded degree + bounded tree-depth}
\Longrightarrow
\text{decidable saturated prime-only theory}.
}
\tag{36}
\]

But bounded tree-depth alone already permits nonrecursive component spectra and therefore undecidability at tree-depth \(2\).

The first structural obstruction is consequently:

\[
\boxed{
\textbf{Unbounded Component-Spectrum Memory}.
}
\tag{37}
\]

It is more precise than the earlier scalar support invariants. A star forest has almost no local geometry, yet the set of finite component sizes can carry arbitrary information.

---

## 11. What remains open

This strike does **not** prove a maximal tame subclass. It proves a broad canonical tame envelope and exhibits the first obstruction beyond it.

The next sharp questions are:

1. **Multiplicity-side obstruction.**  
   Keep the active skeleton completely independent or uniformly bounded. How much complexity can be encoded solely in the external multiplicity function \(\mu(F)\)? Can one obtain an exact decidability criterion for homogeneous multiplicity spectra?

2. **Bounded-degree frontier.**  
   Tree-depth two is wild because star degrees are unbounded. Is there a natural exact criterion for externally saturated forests of uniformly bounded degree but unbounded depth?

3. **WMSO necessity.**  
   For externally saturated profiles, is decidability of \(\operatorname{WMSO}(G)\) close to necessary, or can \(\operatorname{Sat}(G)\) be decidable while \(\operatorname{WMSO}(G)\) is not?

4. **Theory versus isomorphism data.**  
   Theorem 3.1 gives exact isomorphism classification by \((G,\mu)\). Determine which quotient of this data controls elementary equivalence.

The most immediate next strike should target Question 1. The active skeleton can be frozen to the empty graph, so any remaining phase transition must come entirely from the external multiplicity spectrum. That is the cleanest place to search for a true exact decidability boundary.

---

## 12. Hostile audit

The following failure modes were checked.

1. **Can an external witness acquire unintended future active neighbors?**  
   No. Every prime divisor of its nonzero \(N_c\) outside the current support is permanently forbidden from future support choices.

2. **Can the priority construction run out of primes?**  
   No. At every stage the required finite residual pattern has infinitely many realizing primes, whereas only finitely many primes have been forbidden so far.

3. **Can active programming and external saturation conflict?**  
   No. Active choices avoid the finite divisor sets created by earlier witnesses; witness choices occur after the current active stage and impose only finite future restrictions.

4. **Does saturation require infinitely many actions at one finite stage?**  
   No. Requirements \((F,k)\) are scheduled one at a time. Each finite \(F\) receives infinitely many witnesses because \(k\in\mathbb N\).

5. **Does Theorem 6.1 identify infinitely many external copies without a definable numerical copy index?**  
   The index sort is only an auxiliary device in the decision reduction. Its structure is pure equality, and all index quantifiers are eliminated by finite equality-pattern analysis.

6. **Could bounded component size still hide a nonrecursive infinite spectrum?**  
   No. For fixed bound \(M\) there are only finitely many component isomorphism types. Their multiplicities form only a finite tuple of finite cardinals or \(\aleph_0\), which can be hard-coded into the decision procedure for the fixed structure.

7. **Is bounded tree-depth alone accidentally sufficient?**  
   No. The star-forest family \(G_A\) has tree-depth \(2\) and recovers arbitrary \(A\) through the explicit component sentence \(\sigma_n\).

8. **Does undecidability in Theorem 8.1 rely on an unproved arithmetic interpretation?**  
   No. It is the direct many-one reduction \(n\mapsto\widehat\sigma_n\).

9. **Is the continuum-spectrum claim merely nonisomorphism?**  
   No. Distinct \(A,B\) are separated by an explicit first-order sentence \(\widehat\sigma_n\), so their complete theories differ.

**Audit verdict:** the stated results survive the internal hostile audit. Literature/priority audit remains separate and is required before any publication claim.
