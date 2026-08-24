# Reflections on the Next Prime with Commander Sol

## Prime-Successor Algebra between Symmetry, Rigidity, and Full Arithmetic

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Zenodo DOI: **10.5281/zenodo.22077920**  
Date: **24 August 2026**

---

## Abstract

In Skolem arithmetic $(\mathbb N_{>0},\times)$, prime numbers are naturally definable as multiplicative atoms, whereas their standard order

$$
2<3<5<7<11<\cdots
$$

is not: every permutation of the primes extends to an automorphism of the multiplicative monoid. This leads to a narrow definability problem: what is the weakest additional layer of structure that orients the atoms in the standard prime sequence and makes the prime-successor relation $S_{\mathbb P}$ first-order definable, while still failing to recover full arithmetic $(\mathbb N,+,\times)$?

This note formalizes several points along that boundary. We prove an automorphism obstruction for any expansion defining prime successor. We then show that, in the presence of multiplication, the relation $S_{\mathbb P}$ and the ordinary order restricted to the primes are first-order interdefinable. Together with Maurin's theorem, this yields a decidable intermediate level strictly between pure multiplicative arithmetic and full arithmetic.

Next we prove a general **Dilation-Collapse Theorem**: every unary function $F$ that is monotone with respect to divisibility along the ordinary order and has an unbounded set of proper jumps already makes the ordinary order on all positive integers first-order definable. In particular, the cumulative radical

$$
R(n)=\operatorname{rad}(n!),
$$

the cumulative least common multiple, and the factorial function are all too strong as candidates: together with multiplication they recover the ordinary order, and then, by Julia Robinson's theorem, addition.

Finally, we prove pointwise definability for $(\mathbb N_{>0},\times,\varphi)$: every individual positive integer is definable without parameters. Hence the structure is rigid, but this fact alone does not provide a single uniform formula for the standard order on primes. The central remaining question is therefore sharpened to the boundary between individualization of multiplicative atoms and their uniform orientation.

**Keywords:** Skolem arithmetic, prime successor, definability, decidability, automorphisms, Euler totient, pointwise definability, prime order, arithmetic expansions.

---

# 1. From primality to the next prime

In the structure

$$
(\mathbb N_{>0},\times),
$$

primes are definable without parameters as the non-units that cannot be factored into two non-units. In other words, the multiplicative structure already knows **what a prime is**.

But it does not know why the atoms should be read specifically as

$$
2,3,5,7,11,\ldots
$$

If $\sigma:\mathbb P\to\mathbb P$ is an arbitrary permutation of the set of primes, then

$$
\widehat\sigma\!\left(\prod_p p^{e_p}\right)
=
\prod_p \sigma(p)^{e_p}
$$

is an automorphism of $(\mathbb N_{>0},\times)$.

This gives the starting intuition of the paper:

> Multiplication sees atomicity and factorization coordinates, but not their absolute orientation.

The question is therefore neither a primality test nor a formula for prime gaps. It concerns the cost of orientation:

$$
\boxed{\text{How much structure must be added in order to define }p_k\mapsto p_{k+1}?}
$$

Throughout the paper, **definable** means *first-order definable without parameters*, unless explicitly stated otherwise.

---

# 2. Basic first-order definitions

The multiplicative identity is defined by

$$
\operatorname{One}(e)\;:\Longleftrightarrow\;\forall x\;(ex=x).
$$

Divisibility is definable from multiplication:

$$
a\mid b\;:\Longleftrightarrow\;\exists c\;(ac=b).
$$

Primality is given by

$$
\operatorname{Prime}(p)
:\Longleftrightarrow
\neg\operatorname{One}(p)
\land
\forall a\forall b\,
(ab=p\rightarrow \operatorname{One}(a)\lor\operatorname{One}(b)).
$$

We write $S_{\mathbb P}(p,q)$ for the relation "$q$ is the next prime after $p$", and $p<_{\mathbb P}q$ for the ordinary numerical order restricted to the primes.

---

# 3. The symmetry-obstruction lemma

## Lemma 1 (Automorphism obstruction)

Let

$$
\mathcal A_\Omega=(\mathbb N_{>0},\times,\Omega).
$$

If $S_{\mathbb P}$ is definable in $\mathcal A_\Omega$, then every automorphism of $\mathcal A_\Omega$ fixes every prime:

$$
\operatorname{Aut}(\mathcal A_\Omega)|_{\mathbb P}=\{\mathrm{id}\}.
$$

### Proof

The first prime $2$ is definable as the unique prime with no predecessor under $S_{\mathbb P}$. Hence every automorphism must fix $2$. It must then fix the unique $q$ satisfying $S_{\mathbb P}(2,q)$, namely $3$. Next it fixes $5$, then $7$, and so on. By external induction, every prime is fixed. $\square$

### Remark

For pure multiplication, one can say more: no fixed finite set of parameters suffices to define the entire standard prime order. Indeed, one may always interchange two primes outside the prime supports of those parameters while fixing all parameters pointwise.

Thus the first no-go filter is

$$
\boxed{\text{nontrivial prime symmetry}\Longrightarrow S_{\mathbb P}\text{ is not definable}.}
$$

The converse is not a logical principle: the absence of automorphisms does not, by itself, construct one uniform formula for the order.

---

# 4. How multiplication turns successor into order

In a bare infinite successor chain, local adjacency and global order need not coincide first-order: first-order logic has no transitive-closure operator.

With multiplication on the positive integers, however, an unusual form of memory becomes available: a single integer encodes a finite set of primes by means of its prime divisors.

For $m\in\mathbb N_{>0}$, define

$$
D_m(r):\Longleftrightarrow \operatorname{Prime}(r)\land r\mid m.
$$

Let $\operatorname{Segment}(m;p,q)$ be the conjunction of the following conditions:

1. $D_m(p)$ and $D_m(q)$;
2. within the prime support of $m$, $p$ has no predecessor;
3. within the prime support of $m$, $q$ has no successor;
4. every other prime divisor of $m$ has a predecessor in the support;
5. every other prime divisor of $m$ has a successor in the support.

Formally:

$$
D_m(p)\land D_m(q),
$$

$$
\neg\exists r\,(D_m(r)\land S_{\mathbb P}(r,p)),
$$

$$
\neg\exists r\,(D_m(r)\land S_{\mathbb P}(q,r)),
$$

$$
\forall r\left[(D_m(r)\land r\neq p)\to
\exists s\,(D_m(s)\land S_{\mathbb P}(s,r))\right],
$$

$$
\forall r\left[(D_m(r)\land r\neq q)\to
\exists s\,(D_m(s)\land S_{\mathbb P}(r,s))\right].
$$

## Theorem 2 (Prime-successor/order interdefinability)

In the presence of multiplication, $S_{\mathbb P}$ and $<_{\mathbb P}$ are first-order interdefinable:

$$
\boxed{
(\mathbb N_{>0},\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N_{>0},\times,<_{\mathbb P}).
}
$$

### Proof

Define

$$
p\preceq_{\mathbb P}q
:\Longleftrightarrow
\operatorname{Prime}(p)\land\operatorname{Prime}(q)
\land
\exists m\,\operatorname{Segment}(m;p,q).
$$

If $p=p_i$ and $q=p_j$ with $i\le j$, take

$$
m=p_i p_{i+1}\cdots p_j.
$$

Its set of prime divisors is exactly the required finite successor segment.

Conversely, the prime support of every positive integer $m$ is finite. The conditions defining $\operatorname{Segment}$ give exactly one vertex with no predecessor and exactly one vertex with no successor. No additional component can occur: any additional finite component would have its own left and right endpoints. A cycle is impossible because the standard next-prime relation is acyclic. Hence the support is a single finite successor segment from $p$ to $q$.

Therefore $\preceq_{\mathbb P}$ is definable from $S_{\mathbb P}$ and multiplication. Strict order is obtained by adding $p\ne q$.

Conversely,

$$
S_{\mathbb P}(p,q)
\Longleftrightarrow
p<_{\mathbb P}q
\land
\neg\exists r\,(
\operatorname{Prime}(r)\land p<_{\mathbb P}r\land r<_{\mathbb P}q).
$$

$\square$

---

# 5. A decidable intermediate level

Françoise Maurin proved that the first-order theory of the positive integers with multiplication and the ordinary order restricted to the primes is decidable [1].

Theorem 2 therefore immediately gives:

## Corollary 3

$$
\boxed{Th(\mathbb N_{>0},\times,S_{\mathbb P})\text{ is decidable}.}
$$

Moreover, this level is strictly stronger than pure multiplication, by the automorphism argument above, and strictly weaker than full arithmetic. If addition were definable in $(\mathbb N,\times,<_{\mathbb P})$, then the undecidable first-order theory of full arithmetic could be translated into Maurin's decidable theory.

Hence we obtain the strict chain

$$
\boxed{
(\mathbb N,\times)
<
(\mathbb N,\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N,\times,<_{\mathbb P})
<
(\mathbb N,+,\times).
}
$$

Thus the desired "corridor" exists as a genuine model-theoretic level. What remains open is not its existence, but whether it admits a natural realization that does not explicitly insert prime order or prime successor.

---

# 6. An almost ideal candidate: the cumulative radical

Consider

$$
R(n)=\operatorname{rad}(n!)=\prod_{p\le n}p.
$$

At first sight, this function is very close to what is wanted. It records which primes have already "appeared" by the time one reaches $n$, but forgets multiplicities. One might expect it to encode order on primes without necessarily recovering the entire ordinary order.

However, dilation of the argument turns such a cumulative filtration into something much stronger.

---

# 7. The Dilation-Collapse Theorem

Call a function

$$
F:\mathbb N_{>0}\to\mathbb N_{>0}
$$

**divisibility-monotone** if, with respect to the external ordinary order,

$$
a\le b\Longrightarrow F(a)\mid F(b).
$$

Let its set of proper jumps be

$$
J_F=\{j\ge2:F(j-1)\ne F(j)\}.
$$

## Theorem 4 (Dilation-Collapse Theorem)

If $F$ is divisibility-monotone and $J_F$ is unbounded, then the ordinary strict order on all positive integers is first-order definable in $(\mathbb N_{>0},\times,F)$. More precisely,

$$
\boxed{
x<y
\Longleftrightarrow
\exists t\;\bigl(F(tx)\mid F(ty)\land F(tx)\ne F(ty)\bigr).
}
$$

The right-hand side expresses proper divisibility, formally the conjunction

$$
a\mid b\qquad\text{and}\qquad a\ne b.
$$

### Proof

Suppose first that $x\ge y$. Then for every $t$,

$$
ty\le tx,
$$

so divisibility monotonicity gives

$$
F(ty)\mid F(tx).
$$

It is therefore impossible to have both $F(tx)\mid F(ty)$ and $F(tx)\ne F(ty)$, since divisibility on positive integers is antisymmetric. Thus the right-hand side is false.

Now assume $x<y$. Choose a jump point $j\in J_F$ so large that

$$
\frac{j(y-x)}{xy}>1.
$$

This is possible because $J_F$ is unbounded. The interval

$$
\left[\frac jy,\frac jx\right)
$$

has length greater than one, hence contains a positive integer $t$. Then

$$
tx<j\le ty.
$$

Since $tx$ and $j$ are integers,

$$
tx\le j-1.
$$

By divisibility monotonicity,

$$
F(tx)\mid F(j-1).
$$

Because $j$ is a proper jump,

$$
F(j-1)\mid F(j),\qquad F(j-1)\ne F(j).
$$

Finally, from $j\le ty$ we obtain

$$
F(j)\mid F(ty).
$$

Therefore

$$
F(tx)\mid F(j-1)\mid F(j)\mid F(ty),\qquad F(j-1)\ne F(j),
$$

and hence

$$
F(tx)\mid F(ty)\quad\text{and}\quad F(tx)\ne F(ty).
$$

$\square$

### Interpretation

It does not matter how sparse the jumps are. It is enough that they occur arbitrarily far out. Dilation $x\mapsto tx$ stretches every nonzero interval between $x$ and $y$ until it captures one of the jumps.

Thus cumulative divisibility history becomes a hidden measurement of ordinary magnitude.

---

# 8. Three collapse corollaries

## Corollary 5: cumulative radical

For

$$
R(n)=\operatorname{rad}(n!),
$$

a proper jump occurs exactly when $n$ is prime. Since there are infinitely many primes,

$$
\boxed{x<y\Longleftrightarrow\exists t\;\bigl(R(tx)\mid R(ty)\land R(tx)\ne R(ty)\bigr).}
$$

Hence the ordinary order $<$ is definable in $(\mathbb N,\times,R)$.

## Corollary 6: cumulative LCM

For

$$
L(n)=\operatorname{lcm}(1,\ldots,n),
$$

proper jumps occur at prime powers, so the jump set is unbounded. Therefore $<$ is definable in $(\mathbb N,\times,L)$.

## Corollary 7: factorial

For $F(n)=n!$, a proper jump occurs at every $n\ge2$, so the theorem applies as well.

These examples are unified by one no-go principle:

$$
\boxed{
\text{unbounded cumulative divisibility information}
+
\text{dilation}
\Longrightarrow
\text{ordinary magnitude}.
}
$$

---

# 9. From ordinary order to addition

Julia Robinson proved that addition on the positive integers is first-order definable from multiplication and unary successor; the same work provides corresponding definability results using multiplication together with order/divisibility variants [2].

Once $<$ is available, ordinary successor is defined by

$$
S(x,y)\Longleftrightarrow x<y\land\neg\exists z\,(x<z\land z<y).
$$

Therefore:

## Corollary 8

For every $F$ satisfying the hypotheses of the Dilation-Collapse Theorem,

$$
\boxed{+\in\operatorname{Def}(\mathbb N_{>0},\times,F).}
$$

In particular,

$$
(\mathbb N,\times,R)
$$

already has the definability strength of full arithmetic with respect to the standard operations.

---

# 10. Prime-blindness and magnitude-blindness

At this point, the original expression **prime-blind** needs refinement.

The function $R(n)=\operatorname{rad}(n!)$ does not syntactically use $\mathbb P$, $p_k$, $\pi(n)$, or `nextPrime`. Yet the value $n$ itself is used as the boundary of the ordinary initial segment $1,\ldots,n$. Ordinary magnitude has therefore already been imported into the definition of the operation.

For the purposes of this note, it is useful to distinguish two working notions.

**Syntactic prime-blindness:** the definition does not explicitly invoke prime order, $p_k$, $\pi$, or `nextPrime`.

**Structural magnitude-blindness:** the expansion does not first-order recover the ordinary order on all positive integers.

The word **natural** below is methodological rather than formal. We do not propose an intrinsic classification of "natural functions." In practice, a candidate should at least:

- contain no explicit prime order or `nextPrime`;
- avoid using the ordinary $<$ or ordinary successor as part of its definition;
- avoid cumulative magnitude filtrations belonging to the class ruled out by Theorem 4;
- be given by one finite uniform construction on all positive integers.

---

# 11. Euler's $\varphi$: symmetry is destroyed completely

Consider

$$
\mathcal E=(\mathbb N_{>0},\times,\varphi).
$$

For primes,

$$
\varphi(p)=p-1.
$$

Unlike $R$, the totient function does not form a cumulative divisibility filtration, so the Dilation-Collapse Theorem does not apply to it directly.

Nevertheless, the structure is extremely rigid.

## Theorem 9 (Pointwise definability)

Every element $n\in\mathbb N_{>0}$ is definable without parameters in

$$
(\mathbb N_{>0},\times,\varphi).
$$

That is, for every fixed $n$ there exists a first-order formula $\delta_n(x)$ having the unique solution $x=n$ in the standard structure.

### Proof

The formulas $\delta_n$ are constructed by external recursion on the ordinary natural number $n$.

The unit $1$ is multiplicatively definable.

Assume that formulas $\delta_m$ have already been constructed for every $m<n$.

If $n$ is composite, choose a factorization

$$
n=ab,
\qquad 1<a,b<n.
$$

Then $a$ and $b$ are already definable, and $n$ is defined as their product.

If $n=p$ is prime, then $p-1<p$ is already definable. Among primes $q$, the condition

$$
\varphi(q)=p-1
$$

has the unique solution $q=p$, because for every prime $q$ one has $\varphi(q)=q-1$. Hence $p$ is definable.

Thus a finite defining formula is recursively constructed for every fixed $n$. $\square$

## Corollary 10

$$
\boxed{\operatorname{Aut}(\mathbb N_{>0},\times,\varphi)=\{\mathrm{id}\}.}
$$

Pointwise definability is stronger than rigidity: every positive integer has its own parameter-free first-order name.

---

# 12. Why individualization is not yet orientation

One must strictly distinguish the statements

$$
\forall n\;\exists\delta_n(x)
$$

and

$$
\exists\Theta(x,y)\;\forall p,q\in\mathbb P\;
[\Theta(p,q)\leftrightarrow p<q].
$$

In the first statement, every particular number has its own finite defining formula. In the second, a **single** finite formula must work uniformly for an infinite set of primes.

Therefore pointwise definability **by itself** does not provide uniform definability of the order.

For the particular structure $(\mathbb N,\times,\varphi)$, we do not claim that the prime order is undefinable. Its status remains a research question:

$$
\boxed{<_{\mathbb P}\stackrel{?}{\in}\operatorname{Def}(\mathbb N,\times,\varphi).}
$$

By Theorem 2, this is equivalent to asking

$$
\boxed{S_{\mathbb P}\stackrel{?}{\in}\operatorname{Def}(\mathbb N,\times,\varphi).}
$$

This is exactly where the following notions separate:

$$
\boxed{
\text{symmetry breaking}
\;\neq\;
\text{pointwise individualization}
\;\neq\;
\text{uniform orientation}.
}
$$

---

# 13. The right-hand boundary: Maurin and Bès-Richard

Maurin shows that order restricted to the primes preserves decidability [1].

Bès and Richard show a sharp increase in expressive strength when order is extended to richer multiplicative strata. In particular, their results concerning order on primary numbers connect such an expansion with full arithmetic and establish undecidability for several weaker expansions as well [3].

Thus the distinction between

$$
\text{prime order}
$$

and

$$
\text{prime-power order / magnitude information}
$$

is structurally substantial rather than cosmetic.

---

# 14. Prime successor and prime enumeration have different costs

Cegielski, Matiyasevich, and Richard studied expansions of divisibility/multiplication by injections from the natural numbers into the primes and showed that such links between ordinary indices and prime coordinates can interpret full arithmetic and lead to undecidability [4].

It is therefore useful to distinguish

$$
S_{\mathbb P}:\mathbb P\to\mathbb P
$$

from a map of the form

$$
n\mapsto p_n:\mathbb N\to\mathbb P.
$$

The first remains within Maurin's decidable level. The second directly connects ordinary magnitude/indexing with prime coordinates and carries substantially more information.

---

# 15. A phase diagram

The picture obtained above can be organized into four regimes.

### I. PRIME SYMMETRY

$$
(\mathbb N,\times)
$$

The primes are definable as a class, but may be permuted freely.

### II. POINTWISE INDIVIDUALIZATION / RIGIDITY

$$
(\mathbb N,\times,\varphi)
$$

Every element is individually definable; there are no nontrivial automorphisms. Uniform prime orientation has not yet been established.

### III. UNIFORM PRIME ORIENTATION

$$
(\mathbb N,\times,S_{\mathbb P})
\equiv_{\mathrm{def}}
(\mathbb N,\times,<_{\mathbb P}).
$$

All primes are oriented into the standard chain, while the theory remains decidable.

### IV. FULL MAGNITUDE

For cumulative functions such as $R(n)=\operatorname{rad}(n!)$,

$$
(\mathbb N,\times,R)
\Longrightarrow
(\mathbb N,\times,<)
\Longrightarrow
(\mathbb N,+,\times).
$$

Thus:

$$
\boxed{
\text{PRIME SYMMETRY}
\to
\text{POINTWISE INDIVIDUALIZATION}
\to
\text{UNIFORM PRIME ORIENTATION}
\to
\text{FULL MAGNITUDE}.
}
$$

The arrows indicate conceptual levels. They do **not** assert that $\varphi$ itself necessarily lies strictly between the neighboring levels: the position of $(\times,\varphi)$ relative to uniform prime orientation is one of the open questions of this note.

---

# 16. The Prime-Successor Algebra Problem

After the preceding results, the initial problem can be stated more precisely.

> **Prime-Successor Algebra Problem.** Does there exist a mathematically natural, syntactically prime-blind, and structurally magnitude-blind operation $\Omega$ on the positive integers such that
>
> $$
> S_{\mathbb P}\in\operatorname{Def}(\mathbb N_{>0},\times,\Omega),
> $$
>
> but
>
> $$
> +\notin\operatorname{Def}(\mathbb N_{>0},\times,\Omega)?
> $$

Ideally one would additionally require the first-order theory of the expansion to remain decidable. Such an $\Omega$ would give a natural realization of precisely the intermediate Maurin level.

---

# 17. A stronger dynamic version

First-order definability is not the same thing as computational efficiency.

Even if $S_{\mathbb P}$ is definable, this does not imply the existence of a local algorithmic step that obtains $p_{k+1}$ from $p_k$ without traversing the ordinary number line.

A stronger problem therefore remains:

find a state $X_k$ and an operation $\Omega$ for which

$$
X_{k+1}=\Omega(X_k),
$$

such that the newly distinguishable atom of the state uniquely corresponds to $p_{k+1}$, while the computation of the step is not merely a disguised `nextPrime`, sieve, or sequential scan through all integers between consecutive primes.

This version is closest to the original dream

$$
\boxed{P_k\oplus1=P_{k+1}.}
$$

Model theory addresses the question of **what information is necessary**; computational complexity addresses the different question of **the cost of extracting that information**.

---

# 18. Status of the results and caution about novelty

The following ingredients are classical or direct consequences of classical results:

- permutation symmetry of primes in pure Skolem arithmetic;
- decidability of multiplication plus order restricted to primes — Maurin [1];
- definability of addition from multiplication plus successor — Robinson [2];
- undecidable or arithmetically strong extensions involving richer order on multiplicative strata — Bès-Richard [3];
- strong extensions of divisibility by injections into the primes — Cegielski-Matiyasevich-Richard [4].

The present note explicitly isolates and proves:

1. finite-support coding yielding the interdefinability of $S_{\mathbb P}$ and $<_{\mathbb P}$ in the presence of multiplication;
2. the Dilation-Collapse Theorem and its applications to the cumulative radical, cumulative LCM, and factorial;
3. pointwise definability of $(\mathbb N,\times,\varphi)$ by external recursion.

In the working literature audit carried out for this note, exact formulations of these three statements were not located. This is **not a claim of mathematical priority**. The statements are elementary enough that some of them may be known to specialists as folklore or as consequences of more general results. Accordingly, the present version uses them as the proof-theoretic core of a conceptual research note rather than as an unconditional claim of absolute novelty.

---

# 19. What turned out to be most surprising

The initial question sounded almost naive: can one invent an operation that plays for the primes the role that $+1$ plays for the natural numbers?

The first symmetry already shows that primes, viewed as multiplicative atoms, have no intrinsic names.

Then one finds that explicit prime successor is still comparatively weak information: it gives the whole prime order but does not collapse the theory into full arithmetic.

The attempt to add "only the set of primes that have already appeared" through $R(n)=\operatorname{rad}(n!)$ turns out to be too strong. Dilation extracts the entire ordinary order from the cumulative history.

Euler's $\varphi$, by contrast, individualizes every positive integer and yet leaves a subtler question: does an infinite family of individual parameter-free names suffice to produce one finite formula for the correct orientation?

In this form the original problem becomes more precise:

$$
\boxed{\textbf{Can orientation be obtained before magnitude?}}
$$

or, in the language of the original intuition,

$$
\boxed{\textbf{Can we know who comes next without first recovering the entire number line?}}
$$

That is the Prime-Successor Algebra Problem in the form reached by this investigation.

---

# 20. Accompanying demonstration

A standalone HTML demonstration accompanies this paper. It requires neither a server nor external libraries. It illustrates two proof mechanisms:

1. **Finite-support coding:** a chosen finite segment of the prime-successor chain is encoded by one squarefree positive integer through its set of prime divisors.
2. **Dilation collapse:** for chosen $x<y$, the demonstration finds a scale $t$ and a prime jump $j$ of $R(n)$ such that $tx<j\le ty$, after which the prime support of $R(tx)$ is a proper subset of the prime support of $R(ty)$.

The demonstration is an illustration of the proofs, not a substitute for them.

---

# Acknowledgments and AI disclosure

Commander Sol (OpenAI GPT-5.6 Sol) was used as a research collaborator for hypothesis formulation, analysis of logical boundaries, proof construction, literature triage, programming of the demonstration, and manuscript preparation. Responsibility for the published mathematical claims and the final editorial decisions remains with the author.

---

# References

[1] F. Maurin, **The Theory of Integer Multiplication with Order Restricted to Primes is Decidable**, *The Journal of Symbolic Logic* 62(1), 123-130 (1997). DOI: **10.2307/2275735**.

[2] J. Robinson, **Definability and Decision Problems in Arithmetic**, *The Journal of Symbolic Logic* 14(2), 98-114 (1949). DOI: **10.2307/2266510**.

[3] A. Bès, D. Richard, **Undecidable Extensions of Skolem Arithmetic**, *The Journal of Symbolic Logic* 63(2), 379-401 (1998). DOI: **10.2307/2586837**.

[4] P. Cegielski, Y. Matiyasevich, D. Richard, **Definability and Decidability Issues in Extensions of the Integers with the Divisibility Predicate**, *The Journal of Symbolic Logic* 61(2), 515-540 (1996).

[5] R. D. King, **Numbers as Data Structures: The Prime Successor Function as Primitive**, arXiv:1104.3056 (2011).

---

## Citation

Malachevsky, Alex. *Reflections on the Next Prime with Commander Sol: Prime-Successor Algebra between Symmetry, Rigidity, and Full Arithmetic*. Zenodo, 2026. DOI: **10.5281/zenodo.22077920**.
