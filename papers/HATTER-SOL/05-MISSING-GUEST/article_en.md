# Tea Parties in the Additive–Multiplicative World with Hatter Sol — V

## Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the \(3\leftrightarrow5\) Transposition

**Malachevsky, A.A.**  
ORCID: **0009-0008-6009-3196**

AI research collaborator: **Commander Sol · Hatter Sol**

---

## Abstract

We study the directed graph on the primes

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1,
\]

which records only the set of prime divisors of \(p-1\), forgetting their multiplicities. In the previous paper of the series, the automorphism problem for this graph was reduced to the exact predecessor fibers

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

The present paper studies the first nontrivial local symmetry

\[
\tau=(3\ 5),
\]

arising from

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

We prove: finite fixed-divisor escape for every exact-support candidate family; a cyclotomic dimension barrier for exponent vectors; a rigorous local sieve asymmetry between \(\{2,3\}\) and \(\{2,5\}\), including weighted asymptotics by numerical size; hereditary persistence of this asymmetry along exact-descendant chains; a cardinality wall showing why quantitative asymmetry disappears once both exact fibers are countably infinite; a finite-fiber compactness theorem turning global death of a seed symmetry into a finite obstruction tree under FFC; a density-one forward-cone theorem, strengthened to show that directed distance at most two already has relative prime density one; and a Causal Survival Theorem under Cone-Fiber Infinitude (CFI).

The central question

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}
\]

remains open. The main outcome is instead a sharp separation between two kinds of information: arithmetic asymmetry between the \(3\)- and \(5\)-branches exists and amplifies, but the multiplicity tower does not see it while the corresponding exact fibers remain infinite.

**Keywords:** automorphisms of prime graphs, Pratt graph, exact supports, S-units, Fermat primes, Pierpont primes, local sieve, infinite graphs.  
**MSC 2020:** 11A41, 11N13, 05C25, 05C63.

---

# 1. From the first cup to the fifth

In the purely multiplicative structure

\[
(\mathbb N_{>0},\times),
\]

the positive integers form the free commutative monoid on the set of primes. Hence

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

From the viewpoint of multiplication alone, prime labels are interchangeable.

For full arithmetic

\[
(\mathbb N,+,\times,0,1),
\]

the situation is opposite: every natural number is fixed, so the automorphism group is trivial.

The HATTER-SOL series asks where, between these two extremes, prime labels cease to be freely permutable.

HATTER-SOL-03 used a stronger predecessor structure that already forces rigidity. HATTER-SOL-04 weakened the retained information to

\[
D(q,p)\iff q\mid p-1.
\]

Only the support of the factorization of \(p-1\) remains; multiplicities are forgotten. This leads to the delicate question whether this radical predecessor information is already sufficient to destroy all prime-renaming symmetries.

---

# 2. Exact fibers and the multiplicity tower

For a prime \(p\), define

\[
\operatorname{Pred}(p)=\{q\in\mathbb P:q\mid p-1\}.
\]

For a finite set of primes \(S\ni2\), let

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Then \(p\in X_S\) exactly when there are positive exponents \((e_q)_{q\in S}\) such that

\[
p=1+\prod_{q\in S}q^{e_q}
\]

is prime. Thus prime values of shifted finite-prime semigroups are not an auxiliary topic here; they are the exact arithmetic content of the graph condition \(\operatorname{Pred}(p)=S\).

We use Pratt height

\[
h(2)=0,
\qquad
h(p)=1+\max_{q\mid p-1}h(q)
\quad(p>2),
\]

and write

\[
P_{\le n}=\{p:h(p)\le n\},
\qquad
L_n=\{p:h(p)=n\},
\]

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

The key extension mechanism from HATTER-SOL-04 may be stated as follows.

## Proposition 2.1 — fiber extension criterion

Let \(g\in G_n\). Then \(g\) extends to an element of \(G_{n+1}\) if and only if, for every exact support occurring at the next layer,

\[
\boxed{\mu(S)=\mu(gS).}
\]

### Proof

Any extension of \(g\) must send a vertex with predecessor set \(S\) to a vertex with predecessor set \(gS\). Thus it induces a bijection

\[
X_S\cap L_{n+1}\longrightarrow X_{gS}\cap L_{n+1},
\]

so equality of cardinalities is necessary.

Conversely, if these cardinalities agree, choose compatible bijections between the corresponding fibers along every orbit of supports under \(g\). Together with the already prescribed action of \(g\) on \(P_{\le n}\), these bijections define an automorphism of \(P_{\le n+1}\). \(\square\)

The first nontrivial test symmetry is

\[
\tau=(3\ 5),
\]

because

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

---

# 3. A closed route: finite fixed-divisor coverings

A natural first attempt is to find an exact support \(S\) such that the entire family

\[
N_S(\mathbf e)=1+\prod_{q\in S}q^{e_q},
\qquad e_q\ge1,
\]

is covered by finitely many fixed prime divisors. This mechanism cannot work.

## Theorem 3.1 — finite fixed-divisor escape

Let \(S\ni2\) be finite and let \(T\) be any finite set of primes. Then there exist positive integers \(m_q\) \((q\in S)\) such that for every \(t\ge1\),

\[
\boxed{
\gcd\!\left(
1+\prod_{q\in S}q^{tm_q},
\prod_{\ell\in T}\ell
\right)=1.
}
\]

In particular, no finite collection of fixed prime divisors covers the entire exact-support candidate family.

### Proof

For \(q\in S\), put

\[
m_q=
\operatorname{lcm}_{\ell\in T\setminus S}
\operatorname{ord}_{\ell}(q),
\]

with the empty least common multiple interpreted as \(1\).

Fix \(\ell\in T\). If \(\ell\in S\), then

\[
1+\prod_{q\in S}q^{tm_q}\equiv1\pmod\ell.
\]

If \(\ell\notin S\), then for every \(q\in S\),

\[
q^{tm_q}\equiv1\pmod\ell,
\]

and therefore

\[
1+\prod_{q\in S}q^{tm_q}\equiv2\pmod\ell.
\]

The case \(\ell=2\notin S\) cannot occur because \(2\in S\). Hence no prime in \(T\) divides the constructed values. \(\square\)

The theorem does not prove \(X_S\neq\varnothing\). It proves the more precise negative statement that emptiness of \(X_S\), if it occurs, cannot be explained by a finite fixed-divisor cover.

---

# 4. The cyclotomic dimension barrier

Let

\[
S=\{q_1,\dots,q_k\},
\qquad
N_S(\mathbf e)=1+q_1^{e_1}\cdots q_k^{e_k}.
\]

## Theorem 4.1 — common odd exponent divisors are forbidden

If \(N_S(\mathbf e)\) is prime, then

\[
\boxed{\gcd(e_1,\ldots,e_k)\text{ is a power of }2.}
\]

### Proof

If an odd \(d>1\) divides all exponents, write \(e_i=df_i\). Then

\[
N_S(\mathbf e)=A^d+1,
\qquad
A=q_1^{f_1}\cdots q_k^{f_k}>1.
\]

For odd \(d\),

\[
A^d+1=(A+1)(A^{d-1}-A^{d-2}+\cdots-A+1),
\]

with both factors greater than one. Contradiction. \(\square\)

For \(S=\{2\}\), this forces

\[
e_1=2^m,
\]

which is the classical Fermat collapse.

For \(k\ge2\), define

\[
\mathcal C_k(B)
=
\{\mathbf e\in[1,B]^k:\gcd(\mathbf e)
\text{ has no odd prime divisor}\}.
\]

## Theorem 4.2 — dimension jump

For every \(k\ge2\),

\[
\boxed{
\frac{|\mathcal C_k(B)|}{B^k}
\longrightarrow
\frac1{\zeta(k)(1-2^{-k})}.
}
\]

In particular,

\[
\frac{|\mathcal C_2(B)|}{B^2}\longrightarrow\frac8{\pi^2}.
\]

### Proof

The indicator that no odd prime divides all coordinates equals

\[
\sum_{\substack{d\mid\gcd(e_1,\dots,e_k)\\d\text{ odd}}}\mu(d).
\]

Thus

\[
|\mathcal C_k(B)|
=
\sum_{\substack{d\le B\\d\text{ odd}}}
\mu(d)\left\lfloor\frac Bd\right\rfloor^k.
\]

Since \(k\ge2\), division by \(B^k\) and dominated convergence yield

\[
\lim_{B\to\infty}\frac{|\mathcal C_k(B)|}{B^k}
=
\sum_{d\text{ odd}}\frac{\mu(d)}{d^k}
=
\prod_{\ell\text{ odd prime}}(1-\ell^{-k}).
\]

Using

\[
\zeta(k)^{-1}
=(1-2^{-k})
\prod_{\ell\text{ odd prime}}(1-\ell^{-k})
\]

gives the formula. \(\square\)

Hence the transition from \(|S|=1\) to \(|S|=2\) is a genuine structural threshold: the universal cyclotomic obstruction leaves a zero-density exponent set in dimension one, but a positive-density set in every fixed dimension \(k\ge2\).

---

# 5. First arithmetic asymmetry: \(\{2,3\}\) versus \(\{2,5\}\)

For

\[
1+2^a5^b,
\]

working modulo \(3\) gives \(2\equiv5\equiv-1\), hence

\[
3\mid1+2^a5^b
\iff
a+b\equiv1\pmod2.
\]

Thus one half of exponent classes survive this local sieve.

For

\[
1+2^a3^b,
\]

working modulo \(5\), with \(3\equiv2^3\), gives

\[
5\mid1+2^a3^b
\iff
a+3b\equiv2\pmod4.
\]

Exactly one quarter of the residue pairs are forbidden, so the survival proportion is \(3/4\).

Both local conditions are invariant under common multiplication of the exponent vector by an odd integer. They therefore combine directly with the odd Möbius inversion from Theorem 4.2. The surviving densities are

\[
\boxed{
\{2,3\}:\frac6{\pi^2},
\qquad
\{2,5\}:\frac4{\pi^2}.
}
\]

Their ratio is

\[
\boxed{\frac32.}
\]

This is a rigorous arithmetic asymmetry of the parameter spaces, independent of any probabilistic model for primality.

---

# 6. Counting by numerical size

Box density does not account for the different growth rates of \(3^b\) and \(5^b\). Put

\[
L=\log X.
\]

The inequality

\[
2^a q^b\le X
\]

is equivalent to

\[
a\log2+b\log q\le L.
\]

The corresponding exponent triangle has area

\[
\frac{L^2}{2\log2\log q}.
\]

## Theorem 6.1 — weighted first-sieve asymptotics

Let \(A_{23}(X)\) count exponent pairs \((a,b)\) such that \(2^a3^b\le X\), the gcd of \(a,b\) is a power of two, and the mod-5 compositeness class is removed. Then

\[
\boxed{
A_{23}(X)
=
\frac{3}{\pi^2\log2\log3}(\log X)^2
+O((\log X)\log\log X).
}
\]

Similarly,

\[
\boxed{
A_{25}(X)
=
\frac{2}{\pi^2\log2\log5}(\log X)^2
+O((\log X)\log\log X).
}
\]

Consequently,

\[
\boxed{
\frac{A_{23}(X)}{A_{25}(X)}
\longrightarrow
\frac{3\log5}{2\log3}
\approx2.197460281.
}
\]

### Proof

Write

\[
\alpha=\log2,
\qquad
\beta=\log q.
\]

For an odd common divisor \(d\mid a,b\), let \(a=du\), \(b=dv\). Then

\[
\alpha u+\beta v\le\frac Ld.
\]

The local residue restriction is invariant under odd common scaling. For a periodic set of residue classes of density \(r\), standard lattice counting in the weighted triangle gives

\[
N_d(L)
=
\frac{r}{2\alpha\beta}\frac{L^2}{d^2}
+O\!\left(\frac Ld+1\right).
\]

Möbius inversion over odd common divisors gives

\[
A(L)
=
\sum_{\substack{d\le cL\\d\text{ odd}}}\mu(d)N_d(L)
\]

for some constant \(c>0\). Therefore

\[
A(L)
=
\frac{rL^2}{2\alpha\beta}
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
+O(L\log L).
\]

The tail contributes only \(O(L)\) after multiplication by \(L^2\), and

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}=\frac8{\pi^2}.
\]

Taking \(r=3/4\) for \(q=3\) and \(r=1/2\) for \(q=5\) yields the formulas. Since \(L=\log X\), the error term becomes \(O((\log X)\log\log X)\). \(\square\)

---

# 7. Local divisor density and exact descendants

Let \(\ell\notin S\) be prime and set

\[
H_\ell(S)
=
\langle q\bmod\ell:q\in S\rangle
\le(\mathbb Z/\ell\mathbb Z)^\times.
\]

## Theorem 7.1 — one-prime local divisor density

As exponent vectors range uniformly over large boxes, the density of vectors satisfying

\[
\ell\mid N_S(\mathbf e)
\]

is

\[
\boxed{
\delta_\ell(S)=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\[4pt]
0,&-1\notin H_\ell(S).
\end{cases}
}
\]

### Proof

Let

\[
M=\operatorname{lcm}_{q\in S}\operatorname{ord}_{\ell}(q).
\]

The residue of \(N_S(\mathbf e)\) modulo \(\ell\) depends only on \(\mathbf e\pmod M\). On the finite torus \((\mathbb Z/M\mathbb Z)^S\), the map

\[
\Phi(\mathbf e)=\prod_{q\in S}q^{e_q}\pmod\ell
\]

is a surjective homomorphism onto \(H_\ell(S)\), so all fibers have equal size. The divisibility condition is exactly \(\Phi(\mathbf e)=-1\). Hence the density is zero if \(-1\notin H_\ell(S)\), and otherwise it is \(1/|H_\ell(S)|\). \(\square\)

Since \(2\) generates both \((\mathbb Z/3\mathbb Z)^\times\) and \((\mathbb Z/5\mathbb Z)^\times\), every \(S\ni2\) satisfies

\[
3\notin S\Longrightarrow\delta_3(S)=\frac12,
\]

\[
5\notin S\Longrightarrow\delta_5(S)=\frac14.
\]

Call \(S\) **3-pure** if

\[
2,3\in S,
\qquad
5\notin S.
\]

If a partial automorphism extends \((3\ 5)\), the image of such a support is 5-pure. Hence the local survival ratio is

\[
\frac{1-\delta_5(S)}{1-\delta_3(gS)}
=
\frac{3/4}{1/2}
=
\boxed{\frac32}.
\]

If \(p\in X_S\) and

\[
S^+=S\cup\{p\},
\]

then 3-purity persists. Therefore the factor \(3/2\) reappears at each stage of such a descendant chain.

For external bookkeeping define

\[
\mathfrak P_5(\mathcal S)=\prod_{j=0}^{m}(1-\delta_5(S_j)),
\qquad
\mathfrak P_3(g\mathcal S)=\prod_{j=0}^{m}(1-\delta_3(gS_j)).
\]

Then

\[
\boxed{
\frac{\mathfrak P_5(\mathcal S)}{\mathfrak P_3(g\mathcal S)}
=
\left(\frac32\right)^{m+1}.
}
\]

The functional \(\mathfrak P\) is only external bookkeeping. It is not a joint probability across levels, not a proved joint density, and not a graph invariant.

---

# 8. The cardinality wall

The multiplicity tower records only

\[
\mu(S)=|X_S|.
\]

## Theorem 8.1 — quantitative asymmetry is invisible on infinite fibers

If \(X_S\) and \(X_T\) are both infinite, then

\[
\boxed{\mu(S)=\mu(T)=\aleph_0.}
\]

Thus differences in local sieve density, asymptotic constants, heuristic singular series, or growth laws do not by themselves obstruct extension across those two fibers.

### Proof

Every exact fiber is a subset of the countable set \(\mathbb P\). Hence every infinite exact fiber is countably infinite. Proposition 2.1 compares precisely these cardinalities. \(\square\)

Therefore any graph-visible obstruction must eventually become one of

\[
\boxed{\text{empty versus nonempty},}
\]

\[
\boxed{\text{finite versus infinite},}
\]

or

\[
\boxed{\text{different finite cardinalities}.}
\]

This is the **cardinality wall**.

---

# 9. The exact scope of the local no-go result

Theorem 3.1 does not justify the claim that every congruence mechanism across several descendant levels must fail. What is proved is narrower.

## Theorem 9.1 — levelwise finite fixed-divisor-cover barrier

At any fixed exact-support level, emptiness of the candidate family cannot be proved by a finite collection of fixed prime divisors covering all exponent vectors. The same statement applies independently at each level of any finite collection of levels.

### Proof

For a single fixed support, this is exactly Theorem 3.1. Given finitely many levels, apply Theorem 3.1 separately to every fixed support encountered there. Each candidate family admits an infinite ray of exponent vectors escaping every proposed finite set of fixed divisors at that level. Hence a mechanism consisting only of finitely many levelwise fixed-divisor covers cannot eliminate all these candidate families. \(\square\)

This theorem says nothing about variable divisors, correlated cross-level congruence constraints, other inter-level arithmetic mechanisms, or deeper prime-value results capable of proving finiteness or emptiness of an exact fiber.

---

# 10. Finite-fiber compactness

Consider the structural regime

\[
\boxed{\text{FFC}:\quad \mu(S)<\infty
\text{ for every finite }S\ni2.}
\]

FFC is not asserted as an arithmetic fact; it is a conditional regime in which the logic of global extension can be analyzed exactly.

## Lemma 10.1 — Pratt truncations are finite under FFC

Under FFC, every \(P_{\le n}\) is finite.

### Proof

Induct on \(n\). The base case is \(P_{\le0}=\{2\}\). Suppose \(P_{\le n}\) is finite. Every vertex of \(L_{n+1}\) has an exact support \(S\subseteq P_{\le n}\), with at least one predecessor of height \(n\). Only finitely many such supports are possible, and FFC makes each corresponding \(X_S\) finite. Hence \(L_{n+1}\) is finite. \(\square\)

In particular every \(G_n\) is finite.

For a seed \(\tau\in G_m\), let

\[
T_n(\tau)=\{g\in G_n:g|_{P_{\le m}}=\tau\}.
\]

## Theorem 10.2 — finite-fiber compactness theorem

Under FFC, the following are equivalent:

1. \(\tau\) extends to a global automorphism of \(\Pi\);
2. \(\tau\) extends to every finite Pratt height;
3. \(T_n(\tau)\ne\varnothing\) for every \(n\ge m\).

### Proof

The implications \((1)\Rightarrow(2)\Rightarrow(3)\) are immediate. Assume (3). The sets \(T_n(\tau)\) form the levels of an extension tree, where a node at level \(n+1\) is joined to its restriction at level \(n\). By Lemma 10.1 every level is finite, hence the tree is finitely branching. König's infinity lemma yields an infinite compatible branch

\[
g_m,g_{m+1},g_{m+2},\dots.
\]

Their union defines a global automorphism of \(\Pi\). \(\square\)

## Corollary 10.3 — finite obstruction tree

If, under FFC, a seed symmetry \(\tau\) has no global extension, then there is a least height \(N\) for which \(T_N(\tau)=\varnothing\). For every

\[
g\in T_{N-1}(\tau),
\]

there exists a support \(S_g\) such that

\[
\boxed{\mu(S_g)\ne\mu(gS_g).}
\]

Since \(T_{N-1}(\tau)\) is finite, this produces a finite obstruction family/tree.

### Proof

Minimality of \(N\) gives \(T_{N-1}(\tau)\ne\varnothing\). Each \(g\in T_{N-1}(\tau)\) fails to extend one more level, so Proposition 2.1 yields at least one support with unequal multiplicities. There are only finitely many such \(g\). \(\square\)

This is a structural finite certificate, not an algorithmic decidability theorem: no algorithm for computing all \(\mu(S)\) is supplied.

At the immediate next level, a single mismatch may suffice; at later heights, one generally needs the full finite obstruction tree.

---

# 11. Density-one forward cones

For \(A\subseteq\mathbb P\), define \(C^+(A)\) to be the smallest set containing \(A\) and closed forward under \(D\):

\[
q\in C^+(A),\quad q\mid p-1
\Longrightarrow
p\in C^+(A).
\]

For a set of primes \(B\), when the limit exists, define relative prime density by

\[
d_{\mathbb P}(B)
=
\lim_{x\to\infty}
\frac{|B\cap[2,x]|}{\pi(x)}.
\]

## Theorem 11.1 — every odd prime has a density-one forward cone

For every odd prime \(a\),

\[
\boxed{d_{\mathbb P}(C^+(a))=1.}
\]

### Proof

Let

\[
N^+(a)=\{q\in\mathbb P:q\equiv1\pmod a\}.
\]

Take a finite \(Q\subset N^+(a)\) and put

\[
M=\prod_{q\in Q}q.
\]

If \(p\notin C^+(a)\), then for every \(q\in Q\),

\[
p\not\equiv1\pmod q,
\]

otherwise there would be a path \(a\to q\to p\).

Among reduced residue classes modulo \(q\), exactly one of the \(q-1\) classes is forbidden. By the Chinese remainder theorem, the proportion of reduced classes modulo \(M\) that survive all exclusions is

\[
\prod_{q\in Q}\left(1-\frac1{q-1}\right).
\]

The prime number theorem in arithmetic progressions therefore gives

\[
\overline d_{\mathbb P}(\mathbb P\setminus C^+(a))
\le
\prod_{q\in Q}\left(1-\frac1{q-1}\right).
\]

Classically,

\[
\sum_{\substack{q\in\mathbb P\\q\equiv1\pmod a}}\frac1q=\infty.
\]

Hence

\[
\sum_{q\in N^+(a)}\frac1{q-1}=\infty,
\]

so, as \(Q\) exhausts finite subsets of \(N^+(a)\),

\[
\prod_{q\in Q}\left(1-\frac1{q-1}\right)\longrightarrow0.
\]

Thus the complement has relative upper prime density zero, and the cone has density one. \(\square\)

## Corollary 11.2 — two directed steps already suffice

Let \(C^+_{\le2}(a)\) be the set of primes reachable from \(a\) by a directed path of length at most two. Then

\[
\boxed{d_{\mathbb P}(C^+_{\le2}(a))=1.}
\]

### Proof

The proof of Theorem 11.1 uses only paths

\[
a\to q\to p.
\]

Therefore the same upper-density estimate already applies to the complement of \(C^+_{\le2}(a)\). \(\square\)

Thus almost the entire prime universe lies in the arithmetic future of one odd prime after only two layers of the relation \(q\mid p-1\).

---

# 12. Causal localization

The next lemma requires a **generated** forward cone; arbitrary forward-closedness is not sufficient.

## Lemma 12.1 — generated-cone localization

Let

\[
A\subseteq P_{\le n},
\qquad
C=C^+(A),
\]

and let \(g_n\in G_n\) fix every vertex of \(P_{\le n}\setminus C\). Let \(S\subseteq P_{\le n}\) be an exact support for next-layer vertices, and assume

\[
S\cap C=\varnothing.
\]

Then

\[
\boxed{g_nS=S,}
\]

and every \(p\in X_S\cap L_{n+1}\) lies outside \(C\).

### Proof

Every element of \(S\) lies outside \(C\), so it is fixed by \(g_n\); hence \(g_nS=S\).

Now take \(p\in X_S\cap L_{n+1}\). Since \(A\subseteq P_{\le n}\), we have \(p\notin A\). If \(p\in C=C^+(A)\), there is a positive-length path from \(A\) to \(p\). Its last edge is \(q\to p\) for some \(q\in C\), and then \(q\in\operatorname{Pred}(p)=S\), contradicting \(S\cap C=\varnothing\). \(\square\)

Separately, for every forward-closed \(C\), one always has

\[
\boxed{p\notin C\Longrightarrow\operatorname{Pred}(p)\cap C=\varnothing.}
\]

The converse fails for an arbitrary forward-closed set, because a vertex may have been inserted as a seed. This scope correction is essential.

---

# 13. Cone-Fiber Infinitude

Let \(g_1\in G_1\), and set

\[
M_1=\operatorname{supp}(g_1),
\qquad
C=C^+(M_1).
\]

## Definition 13.1 — CFI\((g_1)\)

We say that **Cone-Fiber Infinitude** holds for \(g_1\) if

\[
\boxed{\mu(S)=\aleph_0}
\]

for every finite exact support \(S\) satisfying

\[
S\cap C\ne\varnothing.
\]

No condition is imposed on supports disjoint from \(C\).

The earlier Higher-Fiber Infinitude hypothesis (HFI) required infinitude for all higher exact fibers. Thus, for a first-layer seed,

\[
\text{HFI}\Longrightarrow\text{CFI}(g_1).
\]

CFI is a more local sufficient condition tied to the causal future of the particular seed symmetry.

---

# 14. Causal Survival Theorem

## Theorem 14.1

Let \(g_1\in G_1\), and put

\[
C=C^+(\operatorname{supp}(g_1)).
\]

If CFI\((g_1)\) holds, then \(g_1\) extends to a global automorphism

\[
g\in\operatorname{Aut}(\Pi)
\]

such that

\[
\boxed{g(p)=p\qquad(p\notin C).}
\]

### Proof

Construct compatible \(g_n\in G_n\) inductively, maintaining

\[
g_n(p)=p
\qquad(p\in P_{\le n}\setminus C).
\]

The base case is immediate from the definition of the support of \(g_1\).

Assume \(g_n\) has been constructed, and consider an exact support \(S\subseteq P_{\le n}\) for the next layer.

If \(S\cap C=\varnothing\), apply Lemma 12.1 with \(A=\operatorname{supp}(g_1)\). Then \(g_nS=S\), and the whole next-layer fiber lies outside \(C\); fix it pointwise.

If \(S\cap C\ne\varnothing\), then \(g_n\) preserves \(C\cap P_{\le n}\) setwise, because it fixes the complement of \(C\) pointwise. Hence

\[
g_nS\cap C\ne\varnothing.
\]

CFI gives

\[
\mu(S)=\aleph_0=\mu(g_nS).
\]

By Proposition 2.1, choose compatible bijections between the relevant fibers. Every vertex \(p\in X_S\) with \(S\cap C\ne\varnothing\) lies in \(C\): if \(q\in S\cap C\), then \(q\to p\), and forward-closedness forces \(p\in C\). Thus no new moved vertex appears outside \(C\).

Induction gives a compatible inverse-limit sequence, hence a global automorphism fixing every prime outside \(C\). \(\square\)

For

\[
\tau=(3\ 5),
\qquad
C_\tau=C^+(\{3,5\}),
\]

we obtain

\[
\boxed{
\text{CFI}(\tau)
\Longrightarrow
(3\ 5)\text{ survives globally}.}
\]

Moreover,

\[
d_{\mathbb P}(C_\tau)=1,
\]

because \(C^+(3)\subseteq C_\tau\) already has relative prime density one.

---

# 15. What is now known about \(3\leftrightarrow5\)

The fifth paper does not answer the global automorphism question with a yes or a no. It does, however, change the shape of the problem.

First, arithmetic distinguishes the \(3\)- and \(5\)-branches already at the first two-dimensional exact supports. The local factor \(3/2\) persists along descendant chains, while numerical-size counting yields the limiting ratio

\[
\frac{3\log5}{2\log3}>2.
\]

Second, this quantitative asymmetry is not itself an obstruction to an automorphism: if the two exact fibers being compared are infinite, both cardinalities equal \(\aleph_0\).

Third, under FFC every global death of the seed symmetry must occur at finite height and has a finite obstruction tree.

Fourth, conditional survival does not require infinitude of all higher fibers; it is enough to impose infinitude on fibers whose supports meet the causal cone of the seed permutation.

Thus

\[
\boxed{
\text{arithmetic asymmetry may be strong while remaining graph-invisible}.}
\]

To kill the transposition, a quantitative difference must eventually become a cardinality difference between exact fibers.

---

# 16. Literature boundary

The directed graph

\[
p\to q\iff p\mid q-1
\]

was explicitly posed by David Feldman on MathOverflow in 2012 [1]. Gjergji Zaimi's answer already observed the special role of \(2\), identified the primes with exact predecessor set \(\{2\}\) as Fermat primes, stratified vertices by exact predecessor sets, and connected the sizes of these classes to possible automorphisms. Accordingly, the present work does not claim priority for the exact-fiber architecture itself or for the broad principle that fiber sizes constrain automorphisms.

Languasco, Luca, Moree and Togbé [2] study the distribution and gaps of two-prime S-units \(p^a q^b\), including the natural triangular scale of order \((\log X)^2/(2\log p\log q)\). Their work does not settle infinitude of prime values \(1+p^a q^b\), which in the case \(p=2,q=3\) already contains the classical Pierpont-prime problem.

Stoll and Siksek [3] study irreducibility and reducible specializations over S-unit groups. Their results concern a different problem and do not supply finiteness or infinitude criteria for prime values

\[
1+\prod q_i^{e_i}.
\]

Classical ingredients used here include factorization of \(A^d+1\) for odd \(d\), Fermat and Pierpont prime background, the prime number theorem in arithmetic progressions and divergence of reciprocal primes in reduced progressions [4], the Chinese remainder theorem, Möbius inversion, periodic lattice counting, and König's infinity lemma [5].

The publication claim is limited to the proved structural package inside the HATTER-SOL multiplicity-tower programme: the levelwise finite-cover barrier, the cyclotomic dimension jump, hereditary local asymmetry and the cardinality wall, finite-fiber compactness, density-one forward cones, and the conditional CFI survival theorem. No literature-wide priority is claimed for the classical analytic or combinatorial ingredients.

---

# 17. Open questions

The first open direction is **unconditional killing**: find an exact support in the causal cone for which one can prove

\[
\mu(S)<\infty
\quad\text{or}\quad
\mu(S)=0,
\]

and turn this into a finite obstruction tree blocking all extensions of \((3\ 5)\).

The second is **minimal orbitwise survival**. CFI is still stronger than necessary: a particular extension may actually visit only part of the support-orbit space. The natural next question is

\[
\boxed{
\text{what is the exact orbitwise necessary-and-sufficient survival criterion?}
}
\]

This is the natural HATTER-SOL-06 problem.

The third is the **mixed finite/infinite regime**. FFC controls the all-finite case, while CFI gives a sufficient condition in an essentially infinite-fiber regime. Between them lies the mixed world in which some fibers are finite and others infinite; this is where genuinely noncompact branching may occur.

---

# 18. Conclusion

We began with the smallest symmetry surviving the first radical layer,

\[
3\leftrightarrow5,
\]

and encountered two different worlds of information.

The exponent spaces distinguish \(3\) from \(5\) quickly and persistently: the first local sieve gives the ratio \(3/2\), weighted counting strengthens the discrepancy to

\[
\frac{3\log5}{2\log3},
\]

and exact descendants preserve the local imbalance.

But the radical-predecessor graph asks not how many candidate exponent vectors survive; it asks how many actual prime vertices exist. If both sides contain countably infinitely many exact primes, all quantitative arithmetic collapses to the same cardinal value

\[
\aleph_0.
\]

Thus the fifth cup finds not a missing guest but a seating rule:

\[
\boxed{
\text{symmetry dies only when arithmetic difference becomes exact-fiber cardinality difference}.}
\]

And causal geometry adds one further surprise: the arithmetic future of any odd prime already has relative prime density one after at most two directed steps.

The next cup should therefore ask not “is there asymmetry?”, but “what is the smallest part of the multiplicity tower that must see it?”

**To be continued.**

---

# References

1. Feldman, D. *Automorphisms of a certain digraph defined on the set of primes?* MathOverflow, question 102907, 23 July 2012; answer by Gjergji Zaimi, 23 July 2012.
2. Languasco, A.; Luca, F.; Moree, P.; Togbé, A. *Sequences of integers generated by two fixed primes.* Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **95** (2025), 123–148. DOI: 10.1007/s12188-025-00293-9.
3. Stoll, M.; Siksek, S. *Hilbert's Irreducibility for \(\mathbb G_m\).* arXiv:2609.04551, 2026.
4. Davenport, H. *Multiplicative Number Theory.* 3rd ed., revised by H. L. Montgomery. Graduate Texts in Mathematics 74. Springer, 2000.
5. Diestel, R. *Graph Theory.* 5th ed. Graduate Texts in Mathematics 173. Springer, 2017. DOI: 10.1007/978-3-662-53622-3.
6. Cox, D. A.; Shurman, J. *Geometry and Number Theory on Clovers.* The American Mathematical Monthly **112** (2005), 682–704. DOI: 10.1080/00029890.2005.11920241.
