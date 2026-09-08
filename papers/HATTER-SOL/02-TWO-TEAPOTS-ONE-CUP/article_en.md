---
title: "Two Teapots, One Cup: 'Who Are You?' Among the Primes"
subtitle: "Reflections on Structural Reducts, Binary Probes, and the Return of Individuality"
author:
  - "Malachevsky, A.A."
date: "2026"
lang: en-US
geometry: margin=2.25cm
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
    \usepackage[font=small,labelfont=bf]{caption}
---

**HATTER-SOL-02 · preprint v0.9.1 · 2026**  
**ORCID:** 0009-0008-6009-3196  
**Joint research line:** Commander Sol / Hatter Sol

> *"Who are you?" asked the Caterpillar.*  
> *For Alice this was a difficult question. For a prime number it can be difficult too, once almost all of arithmetic has been forgotten.*

# Abstract

The first paper in the HATTER-SOL series contrasted two extremes. In the purely multiplicative world of the positive integers, all primes are free atoms of one structural type and may be permuted arbitrarily. In full natural-number arithmetic, this freedom disappears. The present paper investigates the intermediate region: what happens if we restore not all of addition, but only carefully dosed fragments of additive information?

For a finite set of prime moduli $F$, we expand the multiplicative monoid by congruence relations $E_p(x,y)\iff x\equiv y\pmod p$. Primes outside $F$ are classified by vectors of multiplicative orders, and the number of prime automorphism orbits is

$$
\boxed{
|F|+\prod_{p\in F}\tau(p-1)
}.
$$

No finite family of such probes makes the structure rigid: infinitely large prime orbits remain outside $F$.

We then replace the full congruence information by the binary quadratic predicate

$$
Q_p(x)\iff p\nmid x\text{ and }\left(\frac{x}{p}\right)=1.
$$

For finite $F$ the number of prime orbits becomes

$$
\boxed{|F|+2^{|F|}},
$$

while rigidity for an arbitrary family $F$ is equivalent to injectivity of the full Legendre-signature map. There exist arbitrarily sparse infinite families of such binary probes that separate every pair of primes and thereby destroy all nontrivial automorphisms.

Finally, for any prescribed finite set $S$ of $N$ primes, the exact minimum number of quadratic binary probes needed to distinguish all elements of $S$ from one another is

$$
\boxed{\kappa_2(S)=\lceil\log_2N\rceil}.
$$

The central conclusion is that structural individuality depends not on the completeness of each observation, but on the global separating power of the family of observations.

**Keywords:** prime numbers; automorphisms; Skolem arithmetic; congruences; Legendre symbol; quadratic characters; reducts; structural information; rigidity; coding.

# 1. After the first cup

In HATTER-SOL-01 [11], the two teapots represented $+$ and $\times$, while the single cup represented the joint arithmetic world. The mathematical hinge was simple:

$$
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P),
$$

whereas restoring the additive skeleton makes the standard natural numbers rigid.

But this contrast is too abrupt. Between "multiplication only" and "full arithmetic" lies a large intermediate territory.

Can we restore not all of addition, but only a weak trace of it? One modulus? One binary question? How do the prime orbits change?

Here the image of two teapots ceases to be merely decorative. We do not have to pour the whole second teapot into the cup at once.

We may add the structure drop by drop.

# 2. "Who are you?"

In Chapter V of *Alice's Adventures in Wonderland*, the Caterpillar asks Alice the short question **"Who are you?"** Alice finds it difficult to answer because she has already changed several times. The theme of unstable identity has long been discussed in scholarship and museum interpretations of the Alice books [1,2].

We are not attributing a theory of prime automorphisms to Carroll. Here the scene is used as a modern mathematical allegory.

In our setting, the question "Who are you?" becomes:

> which properties of the given structure distinguish one element from all the others?

If an automorphism of the structure sends a prime $p$ to a prime $q$, then within that structure the two primes have not yet acquired full individuality.

For a structure $\mathcal R$ containing multiplication, define

$$
p\sim_{\mathcal R}q
\iff
\exists g\in\operatorname{Aut}(\mathcal R):g(p)=q.
$$

We call the equivalence classes the **prime-individuality orbits** of $\mathcal R$.

Under multiplication alone there is only one such orbit:

$$
\mathbb P.
$$

![Figure 1. "Who are you?" - a modern mathematical allegory of prime individuality. Original illustration for the HATTER-SOL series.](caterpillar_who_are_you.png){ width=82% }

# 3. The first drop: one congruence modulo $p$

Let $p$ be prime. Introduce

$$
E_p(x,y)
\iff
x\equiv y\pmod p
$$

and the structure

$$
\mathcal M_p=(\mathbb N_{>0},\times,E_p).
$$

We have not restored addition as an operation. We have only allowed one additive question: do two integers lie in the same residue class modulo $p$?

Even this weak information is enough to make $p$ definable among the primes.

## Lemma 3.1

The positive multiples of $p$ are defined by

$$
Z_p(x)\iff\forall y\;E_p(xy,x).
$$

**Proof.** If $p\mid x$, then $xy\equiv x\equiv0\pmod p$ for every $y$. If $p\nmid x$, take $y=p$: then $xy\equiv0\pmod p$, while $x\not\equiv0\pmod p$. $\square$

Intuitively, $Z_p$ is a local "black hole" modulo $p$: once an element lies in the zero class, multiplying by any $y$ leaves it in that same class. No nonzero class has this property.

Among the multiplicative atoms, exactly one prime lies in $Z_p$, namely $p$. Hence every automorphism of $\mathcal M_p$ fixes $p$.

# 4. One modulus: exact orbit classification

For $q\ne p$, the residue $q\bmod p$ lies in the cyclic group

$$
\mathbb F_p^\times.
$$

An automorphism of the structure may change the specific nonzero residue, but it must preserve its multiplicative type. This leads to the invariant

$$
\operatorname{ord}_p(q).
$$

## Theorem 4.1

For primes $q,r\ne p$,

$$
q\sim_{\mathcal M_p}r
\iff
\operatorname{ord}_p(q)=\operatorname{ord}_p(r).
$$

Consequently, the number of prime orbits is

$$
\boxed{1+\tau(p-1)}.
$$

Here $\tau(n)$ denotes the number of positive divisors of $n$.

**Proof.** Every automorphism of $\mathcal M_p$ induces an automorphism of the group $\mathbb F_p^\times$. Automorphisms of a finite cyclic group preserve element order, so the condition is necessary.

Conversely, if two nonzero residues have the same order, an automorphism of the cyclic group $\mathbb F_p^\times$ sends one to the other. For every residue class choose a bijection between the infinite sets of primes in the source and target classes; infinitude follows from Dirichlet's theorem. The resulting permutation of primes, fixing $p$, extends multiplicatively to all positive integers and preserves $E_p$. $\square$

Examples:

$$
p=2\Rightarrow2\text{ orbits},
\qquad
p=3\Rightarrow3,
\qquad
p=5\Rightarrow4.
$$

A single weak additive probe already fragments the giant orbit $\mathbb P$, but it does not destroy the remaining symmetry.

# 5. Several moduli: the fragmentation law

Let $F\subset\mathbb P$ be finite and consider

$$
\mathcal M_F
=(\mathbb N_{>0},\times,(E_p)_{p\in F}).
$$

Every $p\in F$ is fixed by its own relation $E_p$. For a prime $q\notin F$, define the **order signature**

$$
\mathbf d_F(q)
=
(\operatorname{ord}_p(q))_{p\in F}.
$$

## Theorem 5.1

For $q,r\notin F$,

$$
q\sim_{\mathcal M_F}r
\iff
\mathbf d_F(q)=\mathbf d_F(r).
$$

Every admissible divisor vector is realized by infinitely many primes, and therefore

$$
\boxed{
\mathfrak O(F)
=|F|+
\prod_{p\in F}\tau(p-1).
}
$$

**Proof.** For each $p\in F$, an automorphism induces an automorphism of $\mathbb F_p^\times$, hence preserves the corresponding multiplicative order. This proves necessity.

Conversely, take two primes with the same order signature. In each coordinate there is an automorphism of $\mathbb F_p^\times$ carrying the residue of the first prime to that of the second. These coordinate automorphisms act independently. The Chinese remainder theorem assembles the required residue vectors modulo $\prod_{p\in F}p$, while Dirichlet's theorem supplies infinitely many primes in every admissible reduced residue class. After choosing bijections between corresponding cells, the permutation of primes again extends multiplicatively. $\square$

# 6. The finite barrier

The formula immediately reveals the first genuine boundary.

## Corollary 6.1

For finite $F$,

$$
\boxed{
\operatorname{Fix}_{\mathbb P}
(\operatorname{Aut}(\mathcal M_F))=F.
}
$$

and

$$
\operatorname{Aut}(\mathcal M_F)\ne\{\mathrm{id}\}.
$$

**Proof.** The primes in $F$ are fixed. Any $q\notin F$ lies in an admissible residue-vector cell containing infinitely many primes by the Chinese remainder theorem and Dirichlet's theorem. A transposition of two primes within one cell preserves all named relations. $\square$

Thus finitely many modular probes cannot fully individualize the infinite set of primes.

# 7. One composite modulus: support and depth

Instead of several relations, we may use a single one:

$$
E_m(x,y)
\iff x\equiv y\pmod m.
$$

If

$$
m=\prod p^{a_p},
$$

then two different kinds of information appear.

The **support**

$$
\operatorname{supp}(m)=\{p:p\mid m\}
$$

determines which prime atoms become individually fixed.

The **depth** - the exponents $a_p$ - refines the distinction among the remaining residue types without adding new fixed primes.

In the language of the series:

$$
\boxed{\text{support answers "whom have we named?"}}
$$

while

$$
\boxed{\text{depth answers "how finely do we distinguish the rest?"}}
$$

Here an important boundary of novelty must be drawn. Automorphism groups of the finite multiplicative monoids $(\mathbb Z/p^e\mathbb Z,\cdot)$ and of their direct products have already been studied by Atalaye, Baker, and Marques [3,4]. We therefore use the finite quotient layer as known input rather than claiming a new classification. Our concern is its lift to the prime-generator orbits of the standard free multiplicative monoid.

A simple depth example is the passage from $m=3$ to $m=9$. In both cases the support is the same: the prime $3$ is fixed, and no new prime receives an individual name. But modulo $3$, the unit group has possible element orders $1$ and $2$, so the external primes form two types; together with $\{3\}$ there are three prime orbits. Modulo $9$, the unit group is cyclic of order $6$, with possible orders $1,2,3,6$: there are now four external types and five prime orbits in total. The support has not changed, but the depth $3\to9$ has increased the resolution of the observation.

# 8. The Caterpillar changes the question: only yes or no

The full relation $E_p$ distinguishes all residue classes modulo $p$. For symmetry breaking, this is more information than we need.

For an odd prime $p$, introduce the much weaker unary predicate

$$
Q_p(x)
\iff
p\nmid x
\text{ and }
\left(\frac{x}{p}\right)=1.
$$

It asks only one question:

> is $x$ a nonzero quadratic residue modulo $p$?

Each query has a binary answer:

$$
Q_p(x)\in\{0,1\}.
$$

This is the precise sense in which we call $Q_p$ a **binary probe**. It is not a statement about the total Shannon information contained in the infinite predicate.

# 9. One binary question creates three prime types

Define

$$
R_p=\left\{q\ne p:\left(\frac qp\right)=1\right\},
\qquad
N_p=\left\{q\ne p:\left(\frac qp\right)=-1\right\}.
$$

## Lemma 9.1

The prime $p$ is the unique multiplicative atom $q$ satisfying

$$
\neg Q_p(q^2).
$$

**Proof.** If $q=p$, then $q^2$ is divisible by $p$, so $Q_p(q^2)$ is false. If $q\ne p$, then $q^2$ is a nonzero quadratic residue modulo $p$. $\square$

## Theorem 9.2

$$
\boxed{
\operatorname{Aut}(\mathcal Q_{\{p\}})
\cong
\operatorname{Sym}(R_p)\times\operatorname{Sym}(N_p),
}
$$

where

$$
\mathcal Q_{\{p\}}
=(\mathbb N_{>0},\times,Q_p).
$$

Hence there are exactly three prime orbits:

$$
\boxed{\{p\},\ R_p,\ N_p.}
$$

**Proof.** Every automorphism fixes $p$ and preserves the truth value of $Q_p(q)$, so it preserves $R_p$ and $N_p$. Conversely, arbitrary independent permutations of these two sets, fixing $p$, extend multiplicatively. For every integer, the Legendre symbol of the product is the product of the Legendre symbols of its prime factors, so $Q_p$ is preserved. $\square$

One question still does not tell the Caterpillar who the prime is, but it already turns one orbit into three.

# 10. Several binary questions create a signature

For a finite set of odd primes $F$, define

$$
\chi_F(q)
=
\left(
\left(\frac qp\right)
\right)_{p\in F}
\in\{\pm1\}^{F},
\qquad q\notin F.
$$

This is the **quadratic signature** of the prime $q$ relative to the chosen probes.

## Theorem 10.1

In the structure

$$
\mathcal Q_F
=(\mathbb N_{>0},\times,(Q_p)_{p\in F}),
$$

every $p\in F$ is a singleton orbit, while two external primes lie in the same orbit exactly when their signatures $\chi_F$ agree.

All $2^{|F|}$ sign vectors are realized by infinitely many primes. Therefore

$$
\boxed{
\#(\mathbb P/\operatorname{Aut}(\mathcal Q_F))
=|F|+2^{|F|}.
}
$$

**Proof.** Each named predicate fixes its own modulus. On external primes, the family $(Q_p)$ records precisely the sign vector, so automorphisms cannot mix different signatures. Conversely, arbitrary permutations within a fixed signature class extend multiplicatively and preserve every $Q_p$. The realization of every sign vector follows from the Chinese remainder theorem, quadratic reciprocity, and Dirichlet's theorem. $\square$

As before, finite $F$ leaves every external orbit infinite.

# 11. The exact cost of finite recognition

Let

$$
S=\{q_1,\ldots,q_N\}\subset\mathbb P
$$

be prescribed in advance.

We want to choose prime moduli outside $S$ so that the elements of $S$ receive pairwise distinct quadratic signatures.

Let $\kappa_2(S)$ denote the minimum number of probes required.

## Lemma 11.1 - realizing a prescribed column of signs

For any finite set of distinct primes $q_1,\ldots,q_N$ and any vector

$$
(\varepsilon_1,\ldots,\varepsilon_N)\in\{\pm1\}^N,
$$

there exist arbitrarily large odd primes $p\notin S$ such that

$$
\left(\frac{q_i}{p}\right)=\varepsilon_i
\qquad(1\le i\le N).
$$

**Proof.** For each odd $q_i$, choose a residue $a_i\pmod{q_i}$ with the prescribed Legendre symbol. Require $p\equiv1\pmod4$, so quadratic reciprocity introduces no sign. If $2\in S$, instead impose $p\equiv1\pmod8$ when $(2/p)=+1$ is required and $p\equiv5\pmod8$ when $(2/p)=-1$ is required; both choices are $1\pmod4$. The Chinese remainder theorem combines these local requirements into a single reduced residue class, and Dirichlet's theorem supplies infinitely many primes in that class. $\square$

## Theorem 11.2 - optimal finite quadratic coding

For every finite set $S$ of $N\ge1$ primes,

$$
\boxed{
\kappa_2(S)=\lceil\log_2N\rceil.
}
$$

**Proof.** With $k$ binary probes there are at most $2^k$ possible signatures, so necessarily

$$
2^k\ge N,
$$

and therefore

$$
k\ge\lceil\log_2N\rceil.
$$

For the reverse bound, take

$$
k=\lceil\log_2N\rceil
$$

and assign the $N$ selected primes distinct codewords in $\{\pm1\}^k$. For each coordinate, apply Lemma 11.1 and choose a prime modulus realizing the required column of signs. The resulting full signatures of the selected primes are precisely the chosen codewords. $\square$

The lower and upper bounds match, so the estimate is exact.

A distinction is essential here. We have learned to separate the $N$ selected primes **from one another**. They have not yet become singleton orbits in the infinite prime world: every finite signature class contains infinitely many other primes.

# 12. An infinite menu and full individuality

Now let $F$ be an arbitrary set of odd prime moduli. The full signature map is

$$
\chi_F:
\mathbb P\setminus F
\to
\{\pm1\}^{F}.
$$

## Theorem 12.1 - rigidity criterion

$$
\boxed{
\operatorname{Aut}(\mathcal Q_F)=\{\mathrm{id}\}
\iff
\chi_F\text{ is injective on }\mathbb P\setminus F.
}
$$

**Proof.** If two external primes have the same signature, their transposition preserves every $Q_p$ and extends multiplicatively, so the structure is not rigid. If $\chi_F$ is injective, every external prime is determined by its full signature, while every $p\in F$ is fixed by its own predicate. Hence every prime generator is fixed, and therefore the entire free commutative monoid is fixed. $\square$

# 13. Sparse rigidity

The criterion becomes a constructive theorem.

## Theorem 13.1

Let

$$
B_1<B_2<\cdots,
\qquad B_n\to\infty.
$$

There exists a sequence of odd prime moduli

$$
F=\{p_1,p_2,\ldots\}
$$

such that $p_n>B_n$ for every $n$ and

$$
\boxed{
\operatorname{Aut}(\mathcal Q_F)=\{\mathrm{id}\}.
}
$$

In particular, $F$ may be chosen to have zero relative density among the primes and to satisfy

$$
\sum_{p\in F}\frac1p<\infty.
$$

**Proof.** Enumerate all unordered pairs of distinct primes:

$$
\{q_1,r_1\},\{q_2,r_2\},\ldots
$$

For each pair $q_n\ne r_n$, there exist infinitely many odd primes $p$ such that

$$
\left(\frac{q_n}{p}\right)\ne\left(\frac{r_n}{p}\right).
$$

This is a special case of Lemma 11.1. Choose a fresh $p_n>B_n$, distinct from the pair and from all previously selected probes. Then every pair of primes is separated in at least one coordinate of the full signature, so $\chi_F$ is injective. Theorem 12.1 gives rigidity. Since the growth of $B_n$ is arbitrary, one may simultaneously impose the desired sparsity conditions. $\square$

This is where the initial intuition changes.

Full individuality does not require a dense reconstruction of addition.

It requires a correctly distributed capacity to separate pairs.

# 14. What do we mean by information?

The phrase "binary probe" can be misleading if taken too literally.

The predicate $Q_p$ returns one binary answer to one query:

$$
Q_p(x)\in\{0,1\}.
$$

But an infinite predicate, and the named modulus $p$ itself, contain much more descriptive information. Our results are therefore not estimates of the total structure in Shannon's sense.

Their exact content is instead:

$$
\boxed{
\text{locally binary observations}
+
\text{global pair separation}
\Longrightarrow
\text{full structural individuality}.}
$$

# 15. What is known, and what is being claimed here

Skolem arithmetic - the arithmetic of the natural numbers with multiplication but without addition - is classical [5-8]. The general programme of expanding it by additional relations is also not new.

The Chinese remainder theorem, Dirichlet's theorem, quadratic reciprocity, and prescribed finite Legendre-symbol patterns are classical. Stronger quantitative questions about prescribed Legendre symbols have been studied, for example, by Hanson, Vaughan, and Zhang [9].

Recent work of Atalaye, Baker, and Marques studies finite multiplicative monoids of residue rings [3,4].

The contribution of the present paper is therefore stated more narrowly:

> We study explicit expansions of the standard multiplicative monoid from the viewpoint of prime individuality and compute how modular and quadratic probes fragment the orbit of its free prime generators. Within this framework we obtain exact finite orbit counts, a finite-information barrier, sparse rigidity, a rigidity criterion for binary probes, and an optimal finite quadratic coding law.

This is a claim about a specific framework-and-theorem package, not about novelty of the classical arithmetic ingredients.

A targeted hostile literature search did not locate an exact prior formulation of the whole package in this form. That is a negative search result, not a proof of priority.

# 16. Returning to Alice

We may now read the Caterpillar's question once more.

> Who are you?

One binary question gives Alice one bit of an answer.

Several questions create a signature.

For a company of $N$ guests, exactly

$$
\lceil\log_2N\rceil
$$

carefully chosen binary questions are enough to make all answers distinct.

But for infinitely many guests, no finite menu of questions can suffice.

And yet the infinite menu may be almost empty: the questions may become sparser and sparser, provided that each new question separates at least one pair that was still indistinguishable.

This is not an interpretation of Carroll's hidden intention. It is our mathematical game with his question.

But the game turns out to be exact.

![Figure 2. Two teapots, one cup, and binary signatures: from symmetry to individuality. Original illustration for the HATTER-SOL series.](two_teapots_one_cup.png){ width=82% }

# 17. After the second cup

In the first paper we asked what happens if we refuse to choose between addition and multiplication too early.

The second paper gives a more concrete answer: we do not have to pour the entire additive teapot into the arithmetic cup.

Sometimes one modular drop is enough to create new individuality.

Sometimes a binary probe is enough to split an orbit.

But finitely many drops leave infinite orbit classes. Full rigidity requires an infinite separating family - although that family may be arbitrarily sparse.

The conclusion of the second paper can therefore be written as

$$
\boxed{
\text{individuality}
\neq
\text{completeness of description};
\qquad
\text{individuality}
=
\text{sufficiency of separation}.}
$$

# 18. To be continued

The next problem of the series changes character.

So far the probes have been supplied externally: we explicitly named a modulus or a quadratic predicate.

The next question is:

> **Can a finite natural mechanism generate an adequately rich separating family by itself?**

If so, the third paper will no longer be about how much information we add by hand, but about how a structure may generate its own distinguishers.

> The Hatter looked at the Caterpillar and asked:  
> "And what if nobody asks the questions anymore?"  
> "Then," she replied, "we shall have to teach the cup to ask them itself."

$$
\boxed{\text{To be continued.}}
$$

# References

1. Carroll, L. *Alice's Adventures in Wonderland.* Macmillan, 1865. Chapter V.
2. Texas A&M University, Cushing Memorial Library. *"Who in the world am I? Ah, that's the great puzzle!": The Faces of Alice in Wonderland.* Exhibition materials, 2018.
3. Atalaye, J.; Baker, L.; Marques, S. *On the automorphism group of the monoid of the integers modulo a prime power.* arXiv:2408.06278, 2024, revised version.
4. Atalaye, J.; Baker, L.; Marques, S. *Automorphism groups of direct products of multiplicative monoids of certain rings.* arXiv:2605.06119, 2026.
5. Mostowski, A. *On direct products of theories.* Journal of Symbolic Logic 17(1), 1-31 (1952). DOI: 10.2307/2267454.
6. Bès, A.; Richard, D. *Undecidable Extensions of Skolem Arithmetic.* Journal of Symbolic Logic 63(2), 379-401 (1998). DOI: 10.2307/2586837.
7. Stonestrom, A. *Some model theory of Th(N,·).* Mathematical Logic Quarterly 68(3), 288-303 (2022). DOI: 10.1002/malq.202100049.
8. Kamiński, Ł. *Definable sets in Skolem arithmetic.* arXiv:2510.02062, 2025.
9. Hanson, B.; Vaughan, R. C.; Zhang, R. *The least number with prescribed Legendre symbols and representation by binary quadratic forms of small discriminant.* Journal of Number Theory 179, 3-16 (2017). DOI: 10.1016/j.jnt.2017.03.004.
10. Abeles, F. F. *Mathematics: Logic and Lewis Carroll.* Nature 527, 302-303 (2015). DOI: 10.1038/527302a.
11. Malachevsky, A.A. *A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations / Чаепитие в аддитивно-мультипликативном мире с Шляпником Sol: числовая ось, наблюдатель и две операции.* HATTER-SOL-01, Zenodo, 2026. DOI: [10.5281/zenodo.22639237](https://doi.org/10.5281/zenodo.22639237).

**HATTER-SOL series materials and updates on GitHub:** [GitHub · papers/HATTER-SOL](https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL)

# Manuscript status

The theorem package has been assembled and included with proofs. A separate hostile literature audit has already narrowed the novelty claims concerning finite multiplicative residue monoids. This version is intended as the English research preprint of the HATTER-SOL series; before Zenodo release, only the ordinary proof reread, bibliographic preflight, and final bilingual packaging remain.