---
title: "The Cup That Asks Its Own Questions"
subtitle: "Anonymous Probes, the Exact Predecessor of a Prime, and Recursive Rigidity"
author: "Malachevsky, A.A."
date: "2026"
lang: en-US
geometry: margin=2.2cm
fontsize: 11pt
header-includes:
  - |
    \usepackage{amsmath,amssymb,amsthm}
  - |
    \usepackage{setspace}
  - |
    \onehalfspacing
  - |
    \usepackage{float}
  - |
    \floatplacement{figure}{H}
  - |
    \usepackage[font=small,labelfont=bf,labelformat=empty]{caption}
---

**HATTER-SOL-03 · preprint v0.9.1 · 2026**  
**ORCID:** 0009-0008-6009-3196  
**Joint research line:** Commander Sol / Hatter Sol

> "And what if nobody asks the questions anymore?"  
> "Then we shall have to teach the cup to ask them itself."

# Abstract

In HATTER-SOL-02, rigidity of the multiplicative world was recovered by an infinite family of explicitly named modular and quadratic probes. The present paper asks the next question: can that external infinite menu be replaced by one finite internal mechanism that generates the required distinguishers by itself?

We first prove a negative boundary: no finite tuple of parameters in the pure multiplicative monoid $(\mathbb N_{>0},\times)$ can individualize all primes. We then examine anonymous probe networks and emphasize a classical contrast: after external indexing is erased, a rich family of questions can become highly homogeneous again.

The positive mechanism is built on recursion through $p-1$. For the binary relation

$$
S_{\mathbb P}(n,p)\iff p\in\mathbb P\text{ and }p=n+1,
$$

we prove

$$
\boxed{\operatorname{Aut}(\mathbb N_{>0},\times,S_{\mathbb P})=\{\mathrm{id}\}}.
$$

Thus rigidity does not require full addition: it is enough to know the exact predecessor of every prime. Over the multiplicative carrier, this relation is first-order interdefinable with the binary query relation $J(a,p)$ - "is $a$ a prime power dividing $p-1$?" - and with the relation $H(a,p)$ of maximal exact prime powers in the factorization of $p-1$.

We then isolate the weaker layer

$$
R_{\mathbb P}(r,p)\iff r=\operatorname{rad}(p-1),
$$

which is equivalent to the directed support graph $q\mid p-1$. Its full rigidity remains an open frontier of our analysis. Finally, for a fixed ladder of threshold queries we introduce the gap profile and prove that the residual uncertainty is exactly the size of the corresponding gaps; filling a gap of size $g$ adaptively costs exactly $\lceil\log_2 g\rceil$ binary queries in the worst case.

The central conclusion can be summarized as

$$
\boxed{
\text{self-generated individuality}
=
\text{a canonical anchor}
+
\text{internal generation of questions}
+
\text{resolving power}.}
$$

**Keywords:** prime numbers; automorphisms; Skolem arithmetic; prime chains; Pratt trees; rigidity; prime predecessor; binary queries; threshold ladders; structural information.

# 1. After the second cup

The first paper in the series separated pure multiplication from full arithmetic [1]. The second [2] established a finer law: no finite family of binary quadratic probes can individualize all primes, yet an infinite separating family can be arbitrarily sparse and still make the structure rigid.

This naturally raises a new question:

> Can we stop listing the questions by hand and instead give the structure a finite mechanism that generates its own distinguishers?

This is a different type of problem. External information is replaced by internal generation.

# 2. Pure multiplication cannot start from a finite seed

Let

$$
\mathcal M=(\mathbb N_{>0},\times)
$$

and fix a finite tuple of parameters

$$
\bar a=(a_1,\ldots,a_k).
$$

For a prime $p$, define its valuation vector

$$
\nu_{\bar a}(p)=(v_p(a_1),\ldots,v_p(a_k)).
$$

For $s\in\mathbb N^k$, put

$$
C_s=\{p\in\mathbb P:\nu_{\bar a}(p)=s\}.
$$

## Theorem 2.1 - exact stabilizer of a finite seed

Two primes $p,q$ lie in the same orbit of the pointwise stabilizer of $\bar a$ if and only if

$$
\boxed{\nu_{\bar a}(p)=\nu_{\bar a}(q)}.
$$

More precisely,

$$
\boxed{
\operatorname{Aut}(\mathcal M/\bar a)
\cong
\prod_{C_s\ne\varnothing}\operatorname{Sym}(C_s).}
$$

**Proof.** The monoid $(\mathbb N_{>0},\times)$ is the free commutative monoid on the set of prime generators. Hence every automorphism is induced by a permutation of the primes. Such a permutation fixes every $a_i$ exactly when it preserves the exponent of each moved prime in every $a_i$, equivalently when it preserves $\nu_{\bar a}$. Therefore the allowed automorphisms are precisely the independent permutations inside the sets $C_s$. $\square$

Only finitely many primes occur in the factorizations of $a_1,\ldots,a_k$. Hence

$$
C_{\mathbf0}=\{p:v_p(a_i)=0\text{ for all }i\}
$$

is cofinite in $\mathbb P$ and therefore infinite.

## Corollary 2.2 - finite-seed barrier

For every finite tuple $\bar a$,

$$
\boxed{\operatorname{Aut}(\mathcal M/\bar a)\ne\{\mathrm{id}\}}.
$$

A cup containing only multiplication cannot manufacture infinitely many individual prime names from a finite start.

# 3. When the questions become anonymous

HATTER-SOL-02 used separately named predicates $Q_p$. The index $p$ was part of the structure: the question itself could not move together with the answer.

If the questions are made anonymous, the picture changes. On the primes $p\equiv1\pmod4$, consider the graph

$$
p\sim q\iff\left(\frac pq\right)=1.
$$

Quadratic reciprocity makes the relation symmetric. The mechanism behind homogeneity is concrete. Take two finite disjoint sets of already chosen vertices $U$ and $V$. For each $u\in U$, require the new prime to be a quadratic residue modulo $u$; for each $v\in V$, require it to be a nonresidue modulo $v$; also impose $p\equiv1\pmod4$. The Chinese remainder theorem assembles these local requirements into one reduced residue class, and Dirichlet's theorem gives infinitely many primes in that class. Thus every finite adjacency pattern is realized. This is exactly the extension property of the Rado graph, and this arithmetic realization is discussed by Cameron [3].

Erasing the index of the question is essential here. The structure no longer remembers *which externally fixed question* created a coordinate; it only sees finite patterns of relations among anonymous vertices. Since any such pattern can be extended by a new vertex, local distinctions are not pinned by external names and instead become raw material for further automorphisms. A rich anonymous network can therefore be not rigid but maximally homogeneous.

$$
\boxed{
\text{many questions without a canonical anchor}
\not\Rightarrow
\text{individuality}.}
$$

# 4. Descent through $p-1$

For a prime $p$, every prime divisor of $p-1$ is smaller than $p$. Thus the factorization of $p-1$ provides a natural well-founded descent.

For example,

$$
13-1=12=2^2\cdot3.
$$

If the exact maximal prime powers $4$ and $3$ are known, their product reconstructs $12$, and therefore $13$.

Define

$$
H(a,p)\iff
\begin{cases}
p\text{ is prime},\\
a=q^e\text{ for some prime }q,\\
q^e\parallel p-1.
\end{cases}
$$

and

$$
\mathcal H=(\mathbb N_{>0},\times,H).
$$

## Theorem 4.1 - exact-depth rigidity

$$
\boxed{\operatorname{Aut}(\mathcal H)=\{\mathrm{id}\}}.
$$

**Proof.** The prime $2$ is the unique prime with no nontrivial $H$-predecessor, so it is fixed. Assume by strong induction that all primes below $p$ are fixed. Every base $q$ occurring among the exact incoming prime powers of $p$ is smaller than $p$, hence $q$ and all of its powers are fixed. An automorphism must preserve the set

$$
\{q^{v_q(p-1)}:q\mid p-1\}.
$$

The product of these elements is exactly $p-1$. Therefore the image of $p$ has the same exact predecessor and must equal $p$. Strong induction fixes every prime, and unique factorization fixes the entire monoid. $\square$

Descent through the divisors of $p-1$ is classically related to prime chains and Pratt certificates [4,5]. Here it is used as a rigidity mechanism for an expansion of the multiplicative monoid.

# 5. The cup asks the same question again

Define

$$
J(a,p)\iff
\begin{cases}
p\text{ is prime},\\
a=q^k\text{ is a nontrivial prime power},\\
a\mid p-1.
\end{cases}
$$

Each individual answer is binary. But the multiplicative carrier can generate

$$
q,q^2,q^3,\ldots
$$

and repeat the same question:

$$
J(q,p)?,\qquad J(q^2,p)?,\qquad J(q^3,p)?,\ldots
$$

If $q\mid p-1$, then the last "yes" before the first "no" determines $v_q(p-1)$ exactly.

![Figure 1. One reusable binary question and an internally generated ladder of prime powers: repeated queries recover the exact exponent $v_q(p-1)$.](figure1_self_query.png){ width=95% }

# 6. The main structural turn: the exact predecessor of a prime

The adaptive picture is equivalent to an even simpler relation:

$$
S_{\mathbb P}(n,p)\iff p\in\mathbb P\text{ and }p=n+1.
$$

This is not the full successor relation on the natural numbers: it records the predecessor only when the successor is prime.

In $(\mathbb N_{>0},\times)$, the multiplicative identity, divisibility, primality, and the property of being a nontrivial power of some prime are first-order definable [6,7]. Denote the last property by $\operatorname{PPow}(a)$.

## Theorem 6.1 - first-order interdefinability

Over $(\mathbb N_{>0},\times)$, the relations

$$
H,\qquad J,\qquad S_{\mathbb P}
$$

are first-order interdefinable.

**Proof.** From $S_{\mathbb P}$ we obtain

$$
J(a,p)\iff
\operatorname{PPow}(a)\land
\exists n\bigl(S_{\mathbb P}(n,p)\land a\mid n\bigr).
$$

Conversely, $S_{\mathbb P}(n,p)$ is defined by

$$
\operatorname{Prime}(p)\land
\forall a\left(
\operatorname{PPow}(a)
\Rightarrow
(J(a,p)\leftrightarrow a\mid n)
\right).
$$

If this condition holds, then $n$ and $p-1$ have exactly the same nontrivial prime-power divisors. Hence, for every prime $q$, the maximal exponents $v_q(n)$ and $v_q(p-1)$ coincide, and therefore $n=p-1$ by unique factorization. When $p=2$, the relevant set of prime-power divisors is empty, which uniquely forces $n=1$.

Finally,

$$
H(a,p)\iff J(a,p)\land
\neg\exists b\bigl(J(b,p)\land a\mid b\land a\ne b\bigr),
$$

while $J$ is recovered from $H$ as the set of all prime powers dividing the corresponding maximal power. $\square$

## Theorem 6.2 - rigidity from the exact prime predecessor

For

$$
\mathcal S_{\mathbb P}=(\mathbb N_{>0},\times,S_{\mathbb P}),
$$

we have

$$
\boxed{\operatorname{Aut}(\mathcal S_{\mathbb P})=\{\mathrm{id}\}}.
$$

**Proof.** The element $1$ is fixed as the multiplicative identity, and $S_{\mathbb P}(1,2)$ fixes $2$. Assume by strong induction that all primes below $p$ are fixed. Every prime divisor of $p-1$ is smaller than $p$, hence fixed. A multiplicative automorphism fixing these prime generators fixes the element $p-1$ together with all of its exponents. From

$$
S_{\mathbb P}(p-1,p)
$$

we obtain after applying the automorphism

$$
S_{\mathbb P}(p-1,g(p)).
$$

A given integer $p-1$ has only one integer successor, so $g(p)=p$. The induction fixes every prime; unique factorization fixes the entire monoid. $\square$

Thus

$$
\boxed{
\text{multiplication}
+
\text{the exact predecessor of every prime}
\Longrightarrow
\text{full rigidity}.}
$$

The full successor relation together with multiplication is classically much stronger and allows addition to be defined [8]. Here we prove only rigidity for the relation restricted to prime outputs; definability of full addition does not follow from this result.

# 7. What can be erased: the radical predecessor

Let

$$
\operatorname{rad}(p-1)=\prod_{q\mid p-1}q.
$$

Define the directed support relation

$$
D(q,p)\iff q,p\in\mathbb P\text{ and }q\mid p-1
$$

and

$$
R_{\mathbb P}(r,p)\iff p\in\mathbb P\text{ and }r=\operatorname{rad}(p-1).
$$

## Lemma 7.1 - support and radical are interdefinable

Over $(\mathbb N_{>0},\times)$, the relations $D$ and $R_{\mathbb P}$ are first-order interdefinable.

**Proof.** From $D$, the integer $r$ is characterized as the unique squarefree positive integer whose prime divisors are exactly the primes $q$ satisfying $D(q,p)$. Conversely,

$$
D(q,p)\iff\operatorname{Prime}(q)\land
\exists r\bigl(R_{\mathbb P}(r,p)\land q\mid r\bigr).
$$

$\square$

The current intermediate frontier is

$$
\boxed{
\operatorname{Aut}(\mathbb N_{>0},\times,R_{\mathbb P})
=\{\mathrm{id}\}\ ?}
$$

Local extensionality is already lost:

$$
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\},
$$

$$
\operatorname{Pred}(7)=\operatorname{Pred}(13)=\{2,3\}.
$$

But this does not produce a global automorphism: later vertices may distinguish primes that have identical local predecessor sets.

The graph $q\mid p-1$ appears classically in Jones [5]. After deleting $2$, forgetting directions and labels, the corresponding undirected graph on odd primes becomes the Rado graph [5].

# 8. Pratt height and equal-predecessor fibers

Set

$$
h(2)=0,
$$

and for an odd prime

$$
h(p)=1+\max_{q\mid p-1}h(q).
$$

This is the well-founded rank of the relation $D$, so every automorphism preserves $h$.

For finite $S\subset\mathbb P$, define

$$
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
$$

Every automorphism $g$ must satisfy

$$
\boxed{g(X_S)=X_{g(S)}},
\qquad
\boxed{\mu(S)=\mu(g(S))}.
$$

## Theorem 8.1 - rank-by-rank extension criterion

Let $g_n$ be an automorphism of the induced directed graph on the primes of height at most $n$. Then $g_n$ extends to level $n+1$ if and only if

$$
\boxed{\mu(S)=\mu(g_n(S))}
$$

for every predecessor set $S$ realized at level $n+1$.

**Proof.** Necessity follows from preservation of exact predecessor sets. For sufficiency, the vertices at level $n+1$ are partitioned into the disjoint fibers $X_S$, and there are no edges between vertices of one level because every edge strictly increases height. Therefore, whenever the cardinalities agree, we may independently choose bijections

$$
X_S\longrightarrow X_{g_n(S)}
$$

and obtain an extension of the automorphism. $\square$

The very first fiber is already tied to the Fermat primes:

$$
X_{\{2\}}=\{p:p-1=2^m\}.
$$

If $2^m+1$ is prime, then $m$ is a power of $2$. Hence $X_{\{2\}}$ consists exactly of the Fermat primes. The unknown existence of further Fermat primes does not decide the automorphism problem, but it shows that even an early layer is sensitive to open arithmetic.

# 9. Static depth and a reusable question are different resources

If each edge stores only one static bit,

$$
v_q(p-1)=1\quad\text{or}\quad v_q(p-1)\ge2,
$$

local extensionality is not restored:

$$
5-1=2^2,\qquad17-1=2^4.
$$

Both primes have the same support $\{2\}$ and the same stored bit.

More generally, let the exponent be encoded by a finite alphabet $C$. The five known Fermat primes

$$
3,5,17,257,65537
$$

all have support $\{2\}$. Hence any alphabet with $|C|\le4$ must identify at least two of these five vertices.

## Theorem 9.1 - two-bit local barrier

No local static encoding using at most two bits per edge makes the predecessor code extensional for all primes.

**Proof.** For the five primes above, the code is determined by a single symbol $c_2(e)$, and there are at most four such symbols. Apply the pigeonhole principle. $\square$

There is also an unconditional finite three-bit barrier. A deterministic enumeration of all

$$
p=2^a3^b+1<10^{12},\qquad a,b\ge1,
$$

with primality certified by trial division by every prime up to $10^6$ yields **77 primes**. Each of them has exact support $\{2,3\}$.

The cutoff $10^{12}$ is neither a theoretical constant nor claimed to be minimal. It is simply a finite window large enough to provide the required certificate: with three bits on each of two incoming edges there are at most $8^2=64$ local codes, so the pigeonhole argument only needs any $65$ primes with support $\{2,3\}$. The chosen window contains $77$, after which further search is unnecessary for this theorem. Primality certification in the window is deterministic because $\sqrt{10^{12}}=10^6$; trial division by all primes up to $10^6$ is sufficient for every candidate.

## Theorem 9.2 - three-bit local barrier

No local static exponent encoding by an alphabet $|C|\le8$ makes the predecessor code extensional for all primes.

**Proof.** For support $\{2,3\}$ there are at most

$$
|C|^2\le64
$$

possible colored codes, whereas the certified family contains $77$ primes. Two vertices must receive the same code. $\square$

The computation is reproduced by `verify_coarse_depth_barrier.py`; the SHA-256 digest of the list of triples $(a,b,p)$ is

`46511dd48a6ddb3b952150082d8472982ec25b22d52e1565e6f46f015cfd12ee`.

These theorems rule out **local static extensionality**; they do not prove non-rigidity for every possible global finite expansion.

# 10. Query ladders and their gap profile

Fix an increasing unbounded set of threshold exponents

$$
A=\{a_0<a_1<a_2<\cdots\}\subseteq\mathbb N_{\ge1},
\qquad a_0=1.
$$

For depth $e\ge1$, the query at threshold $a$ returns

$$
T_a(e)=\mathbf1[a\le e].
$$

The full answer signature is

$$
\sigma_A(e)=(T_a(e))_{a\in A}.
$$

For consecutive $a_j<a_{j+1}$ define

$$
g_j=a_{j+1}-a_j,
\qquad
I_j=[a_j,a_{j+1}-1]\cap\mathbb N.
$$

## Theorem 10.1 - gap law

For $e,f\ge1$,

$$
\boxed{
\sigma_A(e)=\sigma_A(f)
\iff
\text{$e$ and $f$ lie in the same cell }I_j.}
$$

**Proof.** Inside one cell, every allowed threshold is either at most both values or greater than both values. If $e<f$ lie in different cells, there is an allowed threshold $a$ with $e<a\le f$, which separates them. $\square$

## Corollary 10.2 - exact completeness of a threshold ladder

Exact recovery of every depth from $\sigma_A$ alone is possible if and only if

$$
\boxed{A=\mathbb N_{\ge1}}.
$$

Thus the full ladder

$$
q,q^2,q^3,\ldots
$$

is not only sufficient; among fixed threshold families it is necessary. Adaptive choice restricted to the same threshold set $A$ does not help, because two values in one cell answer every admissible query identically.

# 11. Exact cost of filling a gap

Once the cell $I_j$ is known, suppose new thresholds inside it are allowed. There remain $g_j$ possible depths.

## Theorem 11.1 - adaptive refinement cost

The minimum worst-case number of additional binary threshold queries is

$$
\boxed{\lceil\log_2 g_j\rceil}.
$$

**Proof.** With $k$ binary answers there are at most $2^k$ transcripts, giving the lower bound. The upper bound is achieved by ordinary binary search on the finite ordered interval $I_j$. $\square$

# 12. The dyadic ladder: room and chair

For

$$
A_{\mathrm{dyad}}=\{1,2,4,8,16,\ldots\},
$$

if

$$
2^n\le e<2^{n+1},
$$

then the ladder determines only the interval

$$
[2^n,2^{n+1}-1],
$$

which has size $2^n$. Therefore, after locating the interval, exactly

$$
\boxed{n}
$$

additional adaptive binary queries are required.

![Figure 2. "Room and chair": dyadic thresholds identify only the cell, while additional questions inside the cell produce exact identification.](figure2_rooms_chairs.png){ width=95% }

# 13. Every depth really occurs on prime targets

## Lemma 13.1 - realization of every exact depth

For every prime $q$ and every $e\ge1$, there are infinitely many primes $p$ such that

$$
\boxed{v_q(p-1)=e}.
$$

**Proof.** Consider the arithmetic progression

$$
p\equiv1+q^e\pmod{q^{e+1}}.
$$

The residue class $1+q^e$ is coprime to $q^{e+1}$, so Dirichlet's theorem gives infinitely many primes in this progression. For every such $p$,

$$
q^e\mid p-1,
\qquad
q^{e+1}\nmid p-1.
$$

Hence $v_q(p-1)=e$. $\square$

Thus every gap of every fixed threshold ladder is realized by genuine prime targets, infinitely often.

# 14. There are two kinds of sparsity

HATTER-SOL-02 showed that a global separating family of probes can be arbitrarily sparse and still enforce rigidity.

For a local threshold ladder, the situation is different.

## Corollary 14.1

If the gaps between consecutive elements of $A$ are bounded by $G$, then the lower density of $A$ is at least $1/G$. Hence a threshold set of natural density zero must have unbounded gaps.

Therefore

$$
\boxed{
\text{zero density of a local threshold ladder}
\Longrightarrow
\text{unbounded residual uncertainty}.}
$$

No fixed finite number of additional **static** bits can distinguish all values inside gaps of unbounded size.

Global sparsity and local sparsity are therefore fundamentally different resources.

# 15. What is known, and what is claimed here

Pure multiplicative arithmetic and its expansions are classical [6,7]. Factorization of $p-1$, prime chains, and Pratt certificates are classical as well [4,5]. Arithmetic realizations of the Rado graph through quadratic residues and through a heavily forgotten version of the graph $q\mid p-1$ are known [3,5]. The full successor relation together with multiplication is substantially stronger and defines addition [8].

The claim of this paper is therefore narrow:

> We study self-generated structural individuality of primes in expansions of the standard multiplicative monoid. Within this framework we obtain: the exact finite-seed barrier; rigidity after adding the exact predecessor of every prime; first-order interdefinability of this relation with adaptive prime-power queries and with maximal exact prime powers; the radical predecessor as a natural intermediate frontier; a rank-by-rank extension criterion through multiplicities of equal-predecessor fibers; static two-bit and three-bit local barriers; the exact gap law for threshold ladders; and the adaptive cost of filling a gap.

This is a claim about a framework-and-theorem package, not about novelty of the classical arithmetic ingredients.

A targeted literature search did not locate a ready-made formulation of the whole package and did not settle the automorphism problem for the full directed graph that retains only predecessor support. Failure to find a source is not a proof of priority.

# 16. Answer to the question of the second paper

Can a finite mechanism generate a sufficiently rich family of questions by itself?

**Yes.** But not every mechanism can.

Three ingredients are needed:

1. **a canonical anchor** - for example, well-founded descent to $2$;
2. **internal generation of new questions**;
3. **resolving power** sufficient to split the remaining gaps.

In the cleanest structural form, it is enough to add

$$
S_{\mathbb P}(n,p)\iff p=n+1\text{ and }p\text{ is prime}.
$$

The cup does not need to know all of addition. It is enough for it to know **what stands immediately before every prime**.

# 17. After the third cup

In the first paper, two teapots helped us separate $+$ from $\times$.

In the second, we learned to add fragments of additive information drop by drop.

In the third, it turns out that the drops need not all be listed in advance. The structure can generate its own questions - provided it can create new distinctions wherever the old questions leave a gap.

$$
\boxed{
\text{individuality}\ne\text{the number of questions};
}
$$

$$
\boxed{
\text{self-generated individuality}
=
\text{anchor}+\text{recursion}+\text{resolving power}.}
$$

One particularly sharp question remains:

$$
\boxed{
\operatorname{rad}(p-1)
\text{ already sufficient for global rigidity,}
\text{ or are multiplicities genuinely necessary?}}
$$

This is the natural doorway to the next research strike.

# References

1. Malachevsky, A.A. *A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations / Чаепитие в аддитивно-мультипликативном мире с Шляпником Sol: числовая ось, наблюдатель и две операции.* HATTER-SOL-01, Zenodo, 2026. DOI: 10.5281/zenodo.22639237.
2. Malachevsky, A.A. *Two Teapots, One Cup: “Who Are You?” Among the Primes / Два чайника, одна чашка: «Кто ты?» среди простых.* HATTER-SOL-02, Zenodo, 2026. DOI: 10.5281/zenodo.22656414.
3. Cameron, P. J. *The Random Graph Revisited.* In: *European Congress of Mathematics, Barcelona, July 10-14, 2000, Vol. I*, Progress in Mathematics 201, Birkhäuser, 2001, pp. 267-274. DOI: 10.1007/978-3-0348-8268-2_15.
4. Pratt, V. R. *Every Prime Has a Succinct Certificate.* SIAM Journal on Computing 4(3), 214-220 (1975). DOI: 10.1137/0204018.
5. Jones, G. A. *Regular embeddings of complete bipartite graphs: classification and enumeration.* Proceedings of the London Mathematical Society 101(2), 427-453 (2010). DOI: 10.1112/plms/pdp061.
6. Mostowski, A. *On direct products of theories.* Journal of Symbolic Logic 17(1), 1-31 (1952). DOI: 10.2307/2267454.
7. Stonestrom, A. *Some model theory of Th(N,·).* Mathematical Logic Quarterly 68(3), 288-303 (2022). DOI: 10.1002/malq.202100049.
8. Robinson, J. *Definability and decision problems in arithmetic.* Journal of Symbolic Logic 14(2), 98-114 (1949). DOI: 10.2307/2266510.
9. Bès, A.; Richard, D. *Undecidable Extensions of Skolem Arithmetic.* Journal of Symbolic Logic 63(2), 379-401 (1998). DOI: 10.2307/2586837.
10. Carroll, L. *Alice's Adventures in Wonderland.* Macmillan, 1865.

**HATTER-SOL series materials and updates:**  
https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL