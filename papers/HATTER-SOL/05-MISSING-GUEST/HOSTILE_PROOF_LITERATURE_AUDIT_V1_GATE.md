# HATTER-SOL-05 · Final Hostile Proof + Literature Gate for v1.0

**Gate date:** 2026-09-11  
**Scope:** `papers/HATTER-SOL/05-MISSING-GUEST/` through commit `f720d3895770f78eb32340cd0bac959cec53a4c4`  
**Purpose:** audit the proof package after the forward-cone/causal-survival theorem and decide whether another research strike is needed before article assembly.

---

## 0. Gate verdict

The central question remains open:

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\},
\qquad
\Pi=(\mathbb P,D),\quad D(q,p)\iff q\mid p-1.
\]

HATTER-SOL-05 neither kills nor unconditionally extends the seed transposition

\[
\tau=(3\ 5).
\]

Nevertheless, the current package has crossed the publication threshold as a **structural boundary theorem package**.

The correct decision is

\[
\boxed{\text{NO ADDITIONAL RESEARCH STRIKE IS REQUIRED BEFORE v1.0.}}
\]

A short **proof-repair/editorial pass is required before the freeze**. After the repairs listed below, freeze v1.0 and assemble the article. Further attacks on exact orbitwise survival belong to the next research phase, not to the publication gate for HATTER-SOL-05.

---

## 1. Results surviving hostile proof checking

The following core statements survive.

### 1.1 Finite fixed-divisor escape

For every finite exact support \(S\ni2\), no finite set of fixed prime divisors covers the whole candidate family

\[
1+\prod_{q\in S}q^{e_q}.
\]

The generalized-Fermat spine

\[
A^{2^k}+1,
\qquad
A=\prod_{q\in S}q^{m_q},
\]

is pairwise coprime and gives a particularly clean strengthening: any fixed finite set of primes is avoided by all but finitely many terms of one fixed spine.

### 1.2 Cyclotomic dimension jump

If

\[
1+\prod_{i=1}^k q_i^{e_i}
\]

is prime, then

\[
\gcd(e_1,\ldots,e_k)=2^r.
\]

For \(k=1\) this collapses the exponent set to powers of two. For \(k\ge2\), the admissible exponent density is

\[
\frac{1}{\zeta(k)(1-2^{-k})}>0.
\]

The calculation is correct; the underlying factorization and Möbius inversion are classical ingredients.

### 1.3 The local \(3\)-versus-\(5\) sieve gap

For the first paired supports,

\[
\{2,3\}:\quad \frac{6}{\pi^2},
\qquad
\{2,5\}:\quad \frac{4}{\pi^2},
\]

so the first local admissibility ratio is exactly

\[
\frac32.
\]

The subgroup formula

\[
\delta_\ell(S)=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\
0,&-1\notin H_\ell(S)
\end{cases}
\]

is also correct.

### 1.4 Cardinality wall

If two exact fibers are both infinite, then both have cardinality \(\aleph_0\). Thus different local densities or different asymptotic constants cannot by themselves obstruct a multiplicity-tower extension. This is elementary but exactly the information-loss statement needed by the programme.

### 1.5 HFI survival theorem

Higher-Fiber Infinitude

\[
\mu(S)=\aleph_0
\qquad
(2\in S,\ S\neq\{2\})
\]

is sufficient for every permutation of the actually existing Fermat-prime layer to extend globally. No infinitude of Fermat primes is required. This is a genuine weakening of the older full-support infinitude formulation.

### 1.6 FFC compactness theorem

Under the all-finite exact-fiber condition, every Pratt-height truncation is finite. König's infinity lemma then implies:

\[
\tau\text{ survives every finite height}
\Longrightarrow
\tau\text{ survives globally}.
\]

Hence global death has a finite-height **structural obstruction family**. The theorem does not imply effective decidability of the required exact cardinalities.

### 1.7 Forward-cone density theorem

For every odd prime \(a\), the forward cone

\[
C^+(a)
\]

has relative prime density one.

The proof is valid: take primes \(q\equiv1\pmod a\); a prime outside the cone must avoid the class \(1\pmod q\) for every such \(q\). For a finite subset \(Q\), the prime-density upper bound is

\[
\prod_{q\in Q}\left(1-\frac1{q-1}\right),
\]

and this tends to zero because

\[
\sum_{q\equiv1\pmod a}\frac1q=\infty.
\]

In fact the proof gives the stronger observation that the **directed distance-\(\le2\) future of every odd prime already has relative prime density one**.

### 1.8 Causal survival theorem

The Cone-Fiber Infinitude condition for a first-layer seed \(g_1\), requiring countably infinite exact fibers only for supports meeting

\[
C^+(\operatorname{supp}g_1),
\]

is sufficient for a global extension fixing the complement of that cone pointwise.

After the lemma-scope correction in Section 2 below, the induction is valid. Thus

\[
\text{HFI}\Longrightarrow\text{CFI}(g_1)
\]

and CFI is a strictly weaker sufficient survival hypothesis.

---

## 2. Mandatory proof repairs before freeze

### Repair A — narrow the descendant no-go statement

The current research note states too broadly that no finite congruence strategy at finitely many descendant levels can kill \((3\ 5)\).

What is proved is the narrower statement:

> **Levelwise fixed-divisor-cover barrier.** For each individual exact-support candidate family, no finite fixed set of prime divisors covers that family. Therefore a killing certificate cannot consist merely of finitely many such levelwise fixed-divisor covers.

Cross-level correlated congruence constraints, or divisors depending on earlier chosen vertices, are not excluded.

### Repair B — correct single-witness language

At the immediate next level, when the image of the support is already forced, one mismatch

\[
\mu(S)\ne\mu(gS)
\]

kills that candidate extension.

At later heights the seed may have several extensions. Global finite-height death therefore generally requires a finite obstruction family/tree intersecting every surviving branch, not a single unqualified pair \(S,\tau S\).

### Repair C — finish the weighted lattice-point proof

The asymptotics

\[
A_{23}(X)
\sim
\frac{3}{\pi^2\log2\log3}(\log X)^2,
\]

\[
A_{25}(X)
\sim
\frac{2}{\pi^2\log2\log5}(\log X)^2
\]

are correct, but the research note presently gives only a proof sketch.

A complete proof is short. Put \(L=\log X\), \(\alpha=\log2\), \(\beta=\log q\). For each odd \(d\), impose \(d\mid a,b\), write \(a=du,b=dv\), and count the permitted periodic residue classes in

\[
\alpha u+\beta v\le L/d.
\]

For a fixed periodic class set of density \(r\), standard planar lattice counting gives uniformly

\[
N_d(L)=
\frac{r}{2\alpha\beta}\frac{L^2}{d^2}
+O\!\left(\frac{L}{d}+1\right).
\]

Möbius inversion over odd \(d\) yields

\[
\sum_{d\le O(L),\ d\text{ odd}}\mu(d)N_d(L)
=
\frac{rL^2}{2\alpha\beta}
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
+O(L\log L).
\]

Since

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}=\frac8{\pi^2},
\]

and \(r=3/4\) for \(\{2,3\}\), \(r=1/2\) for \(\{2,5\}\), the claimed constants follow with an explicit \(O(L\log L)=o(L^2)\) remainder.

### Repair D — scope the causal localization lemma correctly

The sentence

> if \(C\) is merely forward closed and \(S\cap C=\varnothing\), then every \(p\in X_S\) lies outside \(C\)

is false for an arbitrary forward-closed set: such a set may contain \(p\) as an initially inserted vertex.

The application needed for Theorem 7.1 is valid after the following correction:

> Let \(C=C^+(A)\) be the forward cone generated by \(A\subseteq P_{\le n}\). If \(p\in L_{n+1}\) and \(\operatorname{Pred}(p)=S\) with \(S\cap C=\varnothing\), then \(p\notin C\).

Indeed \(p\notin A\); any path from \(A\) to \(p\) would have positive length, and its penultimate vertex would be a predecessor of \(p\) lying in \(C\), contradiction.

The separate implication

\[
p\notin C\Longrightarrow\operatorname{Pred}(p)\cap C=\varnothing
\]

is valid for every forward-closed \(C\).

### Repair E — terminology

- The descendant pressure product \(\mathfrak P\) is an external bookkeeping functional, not a joint probability/density across levels and not a graph invariant.
- Under FFC, use **finite structural obstruction family/certificate**, not an algorithmic decidability claim.
- Replace “generator \((3\ 5)\)” by “transposition” or “element”.
- Do not call the mixed finite/infinite regime the only genuinely difficult regime; it is specifically the regime where noncompact extension-tree failure can occur.

---

## 3. Literature audit

### 3.1 Exact graph question and exact-support viewpoint

The exact digraph

\[
p\to q\iff p\mid q-1
\]

was explicitly asked about on MathOverflow in 2012 by David Feldman. Gjergji Zaimi's answer already observed the unique role of \(2\), identified the Fermat-prime first fiber, proposed stratifying primes by exact incoming sets, and explained that a strong infinitude conjecture for primes

\[
1+\prod p_i^{a_i}
\]

would create many automorphisms, while finite sufficiently distinguishing fibers could force rigidity.

Therefore HATTER-SOL-05 must not claim priority for the exact-support viewpoint or the broad infinitude-versus-rigidity dichotomy.

Source: https://mathoverflow.net/questions/102907/automorphisms-of-a-certain-digraph-defined-on-the-set-of-primes-edited

### 3.2 Two-prime S-unit distribution

Languasco, Luca, Moree and Togbé study the distribution and gaps of numbers \(p^a q^b\). Their lattice-point count has the same logarithmic triangular scale used in HATTER-SOL-05, but they do not prove infinitude of prime values \(p^a q^b+1\).

Reference: A. Languasco, F. Luca, P. Moree, A. Togbé, *Sequences of integers generated by two fixed primes*, Abh. Math. Semin. Univ. Hambg. 95 (2025), 123–148, DOI 10.1007/s12188-025-00293-9.

### 3.3 Pierpont frontier

The first higher exact fiber \(X_{\{2,3\}}\) is a positive-exponent Pierpont-prime family. The infinitude of Pierpont primes remains open. Hence no local-density or heuristic calculation in HATTER-SOL-05 may be promoted to an infinitude theorem.

Relevant background includes Gleason's conjecture, Cox–Shurman, and OEIS A005109.

### 3.4 Recent S-unit irreducibility work

Michael Stoll and Samir Siksek, *Hilbert's Irreducibility for \(\mathbb G_m\)*, arXiv:2609.04551 (2026), describes reducible specializations over S-units. It is close enough to cite as current adjacent literature, but it does not prove infinitely many prime values of

\[
1+\prod q_i^{e_i}.
\]

It does not close the HATTER-SOL-05 frontier.

### 3.5 Forward-cone theorem

The density-one cone proof uses classical Dirichlet/PNT-in-AP, divergence of reciprocal primes in an arithmetic progression, and CRT. A targeted search did not reveal a source packaging the resulting distance-two density-one statement as an automorphism/Pratt-graph theorem. This is not proof of literature-wide novelty, so the publication should claim the theorem as a proved structural consequence in this programme without asserting priority over all prior literature.

---

## 4. Safe publication claims

After the repairs, HATTER-SOL-05 may safely claim the following package:

\[
\boxed{\text{finite fixed-divisor covers fail levelwise for every exact support};}
\]

\[
\boxed{|S|=1\to|S|\ge2\text{ is a genuine cyclotomic-admissibility dimension jump};}
\]

\[
\boxed{\{2,3\}\text{ and }\{2,5\}\text{ have a rigorous local }3/2\text{ sieve gap};}
\]

\[
\boxed{\text{quantitative local asymmetry is erased by the cardinality wall if both fibers are infinite};}
\]

\[
\boxed{\text{HFI forces global survival of every existing Fermat-layer permutation};}
\]

\[
\boxed{\text{FFC forces every global death to have a finite-height structural obstruction family};}
\]

\[
\boxed{d_{\mathbb P}(C^+(a))=1\text{ for every odd prime }a;}
\]

indeed the directed distance-\(\le2\) future already has density one; and

\[
\boxed{\text{CFI}(g_1)\Longrightarrow\text{global survival localized to the seed forward cone}.}
\]

---

## 5. Claims that remain forbidden

Do not claim:

- \(\operatorname{Aut}(\Pi)=\{\mathrm{id}\}\);
- unconditional non-rigidity of \(\Pi\);
- unconditional survival or death of \((3\ 5)\);
- infinitude of \(X_{\{2,3\}}\), \(X_{\{2,5\}}\), or all higher exact fibers;
- that unequal sieve densities imply unequal exact-fiber cardinalities;
- that every finite congruence strategy is impossible;
- that FFC gives an effective algorithm for deciding survival;
- priority for the 2012 exact-support architecture.

---

## 6. Final publication decision

The fifth note now has a coherent mathematical arc:

1. the radical-predecessor graph reduces prime-renaming survival to exact-support multiplicities;
2. the obvious local mechanisms do distinguish the \(3\)- and \(5\)-sides, but do not convert that difference into a graph-visible cardinality mismatch;
3. the cardinality wall explains the loss;
4. the all-infinite and all-finite regimes admit rigorous opposite structural theorems;
5. the forward cone identifies the exact causal region of a seed symmetry, shows that this region already has density one, and yields a strictly weaker conditional survival theorem.

That is enough for HATTER-SOL-05 v1.0.

\[
\boxed{\textbf{DECISION: REPAIR → FREEZE v1.0 → ASSEMBLE ARTICLE.}}
\]

Do not spend the fifth paper on another speculative attack. The orbitwise necessary-and-sufficient survival problem and direct arithmetic attacks on cone-intersecting finite/empty fibers are the correct continuation after the v1.0 article is frozen.
