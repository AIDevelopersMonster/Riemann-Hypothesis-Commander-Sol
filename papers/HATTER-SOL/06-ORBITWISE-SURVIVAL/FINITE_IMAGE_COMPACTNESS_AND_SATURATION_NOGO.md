# HATTER-SOL-06 · Finite-Image Compactness and Prime Saturation No-Go

## 0. Purpose

The previous strike constructed an abstract exact-fiber graph with genuine noncompact death of obstruction rank \(\omega\). The natural next hope was that the actual prime graph might nevertheless enjoy a prime-specific future-type compactness principle.

This note shows that a naive compactness principle of that kind is impossible: the prime graph itself already has very strong finitely realizable but globally unrealized future types.

The correct replacement is an **equivariant finite-image compactness principle** for automorphism extensions. This yields a sharp theorem:

\[
\boxed{
\text{noncompact death forces eternal image escape for some vertex.}
}
\]

For the seed \((3\ 5)\), any genuinely noncompact obstruction must therefore manifest as an infinite family of distinct candidate images inside one exact prime fiber, surviving to arbitrarily large finite heights.

---

# 1. The prime graph has a strong finite incoming-pattern extension property

Work in

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

## Theorem 1.1 — finite incoming-pattern realization

Let \(A\) and \(B\) be disjoint finite sets of odd primes. Then there are infinitely many primes \(r\) such that

\[
D(a,r)\quad(a\in A),
\]

and

\[
\neg D(b,r)\quad(b\in B).
\]

Equivalently,

\[
A\subseteq\operatorname{Pred}(r),
\qquad
B\cap\operatorname{Pred}(r)=\varnothing.
\]

### Proof

Put

\[
M=\prod_{a\in A}a\prod_{b\in B}b.
\]

By the Chinese remainder theorem choose \(c\pmod M\) satisfying

\[
c\equiv1\pmod a
\qquad(a\in A),
\]

\[
c\equiv2\pmod b
\qquad(b\in B).
\]

Because every prime in \(A\cup B\) is odd, \(c\) is nonzero modulo every prime divisor of \(M\), hence

\[
\gcd(c,M)=1.
\]

Dirichlet's theorem gives infinitely many primes

\[
r\equiv c\pmod M.
\]

For \(a\in A\),

\[
r-1\equiv0\pmod a,
\]

while for \(b\in B\),

\[
r-1\equiv1\pmod b.
\]

Thus all required incidences and non-incidences hold. \(\square\)

The prime \(2\) is exceptional only because it is a predecessor of every odd prime; this is why the theorem is stated for odd prescribed primes.

---

# 2. A direct compactness failure in the prime graph

Enumerate the odd primes

\[
p_1,p_2,p_3,\dots.
\]

Consider the infinite family of requirements on a prime variable \(x\):

\[
D(p_i,x)
\qquad(i=1,2,3,\dots).
\]

Every finite subfamily is realizable: by Theorem 1.1, or directly by Dirichlet, there are infinitely many primes

\[
x\equiv1\pmod{p_1p_2\cdots p_N}.
\]

But the whole family is not realizable, because a fixed integer \(x-1\) has only finitely many prime divisors.

## Corollary 2.1 — naive future compactness fails

The prime graph has a countable family of future adjacency constraints such that every finite subfamily is realizable by a prime, while the full family is not.

Thus the implication

\[
\boxed{
\text{every finite future pattern is realizable}
\Longrightarrow
\text{the whole future type is realizable}
}
\]

is false already in the actual prime graph.

No abstract model-theoretic saturation argument can therefore supply the compactness needed for the automorphism problem.

---

# 3. Failure even inside an infinite exact fiber

The previous example allows the candidate prime to range over all primes. The failure is stronger.

Assume an exact fiber

\[
X_S
=
\{q\in\mathbb P:\operatorname{Pred}(q)=S\}
\]

is infinite. Enumerate it as

\[
X_S=\{q_1,q_2,q_3,\dots\}.
\]

For each \(i\), choose a prime \(r_i\) satisfying

\[
q_i\mid r_i-1.
\]

Such a prime exists by Dirichlet's theorem in the progression

\[
1\pmod{q_i}.
\]

Consider the future non-incidence requirements

\[
\neg D(y,r_i)
\qquad(i=1,2,3,\dots)
\]

with \(y\) restricted to \(X_S\).

## Theorem 3.1 — exact-fiber future-type failure

Every finite subfamily of these requirements is realized by some

\[
y\in X_S,
\]

but no \(y\in X_S\) realizes all of them.

### Proof

Fix \(N\). The set

\[
F_N
=
\bigcup_{i=1}^{N}\operatorname{Pred}(r_i)
\]

is finite, because each \(r_i-1\) has only finitely many prime divisors.

Since \(X_S\) is infinite, choose

\[
y\in X_S\setminus F_N.
\]

Then

\[
\neg D(y,r_i)
\qquad(1\le i\le N).
\]

Thus every finite subfamily is realizable.

On the other hand, any \(y\in X_S\) equals \(q_j\) for some \(j\), and by construction

\[
D(q_j,r_j).
\]

Hence no \(y\in X_S\) satisfies all requirements. \(\square\)

So even an infinite exact prime fiber is not countably compact with respect to fixed future parameters.

---

# 4. Why this does not itself kill an automorphism

Theorem 3.1 is a no-go result for the naive compactness strategy, not a killing theorem for \((3\ 5)\).

If

\[
y\in C
\]

lies in the causal cone of a seed, then every future neighbor \(r\) with

\[
D(y,r)
\]

also lies in \(C\), because the cone is forward closed.

Therefore the witnesses \(r_i\) used above are themselves movable under a cone-localized automorphism. They cannot be treated as fixed external parameters when testing whether one candidate image of \(y\) can replace another.

This is the key correction:

\[
\boxed{
\text{the relevant compactness problem is equivariant, not parameter-fixed.}
}
\]

A candidate image must match not only finitely many named future vertices, but a future configuration whose parameters are transported simultaneously by the same partial automorphism.

---

# 5. Deep image sets

Fix a seed

\[
\tau\in G_m,
\]

its generated causal cone

\[
C=C^+(\operatorname{supp}\tau),
\]

and the cone-localized extension sets

\[
\mathcal T_n^C(\tau).
\]

For a prime \(p\) and an integer

\[
H\ge h(p),
\]

define the **deep forward-image set**

\[
I_H^+(p)
=
\left\{
q:\exists n\ge H,\ \exists g_n\in\mathcal T_n^C(\tau),\ g_n(p)=q
\right\}.
\]

Similarly define the **deep inverse-image set**

\[
I_H^-(p)
=
\left\{
q:\exists n\ge H,\ \exists g_n\in\mathcal T_n^C(\tau),\ g_n^{-1}(p)=q
\right\}.
\]

These sets decrease with the horizon:

\[
I_{H+1}^{\pm}(p)\subseteq I_H^{\pm}(p).
\]

Outside the causal cone they are eventually singletons.

---

# 6. Eventual bi-finite image property

## Definition 6.1 — EBFI

We say that the seed \(\tau\) satisfies the **eventual bi-finite image property** if for every prime \(p\) there exists a horizon \(H(p)\) such that both

\[
I_{H(p)}^+(p)
\]

and

\[
I_{H(p)}^-(p)
\]

are finite.

The condition allows exact fibers themselves to be infinite. It asks only that sufficiently deep survival constraints reduce the possible image and preimage of each individual prime to finitely many candidates.

Thus EBFI is strictly about future arithmetic discrimination, not about finiteness of fibers.

---

# 7. Finite-image compactness theorem

## Theorem 7.1 — EBFI restores compactness

Assume:

1. cone-localized extensions of \(\tau\) exist to arbitrarily large finite Pratt heights;
2. EBFI holds.

Then \(\tau\) has a global cone-localized extension

\[
g\in\operatorname{Aut}(\Pi).
\]

### Proof

Choose heights

\[
n_1<n_2<n_3<\cdots\to\infty
\]

and

\[
g_k\in\mathcal T_{n_k}^C(\tau).
\]

Enumerate the primes

\[
p_1,p_2,p_3,\dots.
\]

By EBFI, after passing far enough along the sequence, the pairs

\[
\bigl(g_k(p_1),g_k^{-1}(p_1)\bigr)
\]

range over a finite set. Pass to an infinite subsequence on which this pair is constant.

Repeat for \(p_2\), then \(p_3\), and so on. A diagonal subsequence, still denoted \((g_k)\), has the property that for every fixed \(i\), both

\[
g_k(p_i)
\]

and

\[
g_k^{-1}(p_i)
\]

are eventually constant.

Define

\[
g(p_i)=\lim_k g_k(p_i),
\]

\[
h(p_i)=\lim_k g_k^{-1}(p_i).
\]

We claim that \(h=g^{-1}\). Fix \(p_i\) and put

\[
g(p_i)=p_j.
\]

For all sufficiently large \(k\),

\[
g_k(p_i)=p_j.
\]

Hence

\[
g_k^{-1}(p_j)=p_i
\]

for all sufficiently large \(k\). Passing to the stabilized inverse limit gives

\[
h(p_j)=p_i.
\]

Thus

\[
hg=\mathrm{id}.
\]

The symmetric argument gives

\[
gh=\mathrm{id}.
\]

So \(g\) is a bijection.

Now take any edge relation between two primes \(p_i,p_j\). For all sufficiently large \(k\), both vertices lie in the domain of \(g_k\), and their images have stabilized. Since every \(g_k\) is a graph automorphism of its truncation,

\[
D(p_i,p_j)
\iff
D(g_k(p_i),g_k(p_j)).
\]

Passing to the stabilized values yields

\[
D(p_i,p_j)
\iff
D(g(p_i),g(p_j)).
\]

Hence \(g\in\operatorname{Aut}(\Pi)\).

Every \(g_k\) extends \(\tau\) and fixes the complement of \(C\), so the same holds for \(g\). \(\square\)

---

# 8. Image-escape theorem

The contrapositive is the key structural result.

## Corollary 8.1 — noncompact death forces eternal image escape

Assume \(\tau\) extends to arbitrarily large finite heights but has no global cone-localized extension. Then EBFI fails.

Consequently there exists a prime \(p\) such that at least one of the two alternatives holds:

\[
\boxed{
|I_H^+(p)|=\infty
\quad\text{for every sufficiently large }H,
}
\]

or

\[
\boxed{
|I_H^-(p)|=\infty
\quad\text{for every sufficiently large }H.
}
\]

Because the sets \(I_H^{\pm}(p)\) are nested, once one direction becomes finite it remains finite. Hence failure of EBFI really does force one direction to remain infinite arbitrarily far into the finite-height tower.

This is the precise form of **eternal image escape**.

---

# 9. Minimal escape height

Suppose noncompact death occurs. Choose a prime \(p\) of minimal Pratt height for which eternal forward-image escape occurs; the inverse case is symmetric.

Let

\[
S=\operatorname{Pred}(p).
\]

Every element of \(S\) has smaller Pratt height. By minimality, its sufficiently deep image set is finite.

Since \(S\) itself is finite, there are only finitely many possible transported predecessor sets

\[
g_nS
\]

among sufficiently deep extensions.

On the other hand, \(p\) has infinitely many candidate images at every deep horizon. Partition those candidate images according to their transported predecessor set. One cell must remain infinite along arbitrarily large horizons.

Hence:

## Theorem 9.1 — escaping exact-fiber sequence

If noncompact death occurs, then after possibly passing to the inverse action there exist

- a prime \(p\);
- a finite exact support \(T\);
- distinct primes
  \[
  q_1,q_2,q_3,\dots\in X_T;
  \]
- heights
  \[
  H_1<H_2<H_3<\cdots\to\infty;
  \]

such that for every \(j\) there is a cone-localized extension

\[
g_j\in\mathcal T_{H_j}^C(\tau)
\]

with

\[
\boxed{g_j(p)=q_j.}
\]

Thus genuine noncompact death in the prime graph cannot remain an abstract tree pathology. It must produce an explicit arithmetic escape sequence of distinct primes in one exact fiber, each imitating the same source prime through a deeper finite future.

### Proof sketch

Take \(p\) of minimal escape height. For every predecessor \(s\in S\), choose a common horizon beyond which \(I_H^+(s)\) is finite. Therefore the image tuple of the finite set \(S\) has only finitely many possibilities in sufficiently deep extensions.

For arbitrarily large horizons the candidate image set of \(p\) is infinite. Partition it by the finitely many possible image tuples of \(S\). One tuple occurs with infinitely many candidate images for arbitrarily large horizons. Its image set is a fixed support \(T\). Choose successively distinct candidate images \(q_j\in X_T\) at strictly increasing horizons. \(\square\)

---

# 10. The new arithmetic target

Theorem 9.1 converts the noncompactness question into a concrete prime problem.

To rule out noncompact death for \((3\ 5)\), it is enough to prove the following kind of statement:

> For every source prime \(p\) in the causal cone and every exact target fiber \(X_T\) compatible with the lower action, there is a finite future horizon after which only finitely many \(q\in X_T\) can still serve as the image of \(p\).

Equivalently, one seeks a finite family of transported descendant multiplicity tests whose combined fingerprint has only finitely many matches in \(X_T\).

This is much weaker than proving that the fiber itself is finite.

It is also much weaker than CFI, which demanded that many fibers be infinite.

The new target is therefore a genuine middle principle:

\[
\boxed{
\text{infinite exact fibers may exist, but finite future data eventually reduce image ambiguity to a finite set.}
}
\]

---

# 11. Specialization to \(\tau=(3\ 5)\)

For

\[
\tau=(3\ 5),
\qquad
C_\tau=C^+(\{3,5\}),
\]

the seed images of \(2,3,5\) are already fixed.

The first possible image escape can therefore occur only above the seed layer.

At height two, the simplest moved pair of exact supports is

\[
\{2,3\}
\longleftrightarrow
\{2,5\}.
\]

Thus a first concrete test case is:

\[
p\in X_{\{2,3\}}
\]

and candidate images

\[
q\in X_{\{2,5\}}.
\]

For example,

\[
7,13\in X_{\{2,3\}},
\]

while

\[
11,41,101,401,641,\dots
\]

supply known elements of \(X_{\{2,5\}}\).

The next arithmetic strike should ask:

\[
\boxed{
\text{can one prove that only finitely many }q\in X_{\{2,5\}}
\text{ can imitate }7\text{ through arbitrarily deep finite extensions?}
}
\]

If yes, the first potential escape channel closes. Repeating this orbit by orbit would restore compactness without any need to prove global finiteness of the exact fibers.

---

# 12. What is now closed

Three tempting routes are now sharply separated.

### Route A — naive future-type compactness

Closed. Theorems 2.1 and 3.1 give explicit prime-graph counterexamples.

### Route B — abstract multiplicity-tower compactness

Closed. The explicit rank-\(\omega\) noncompact-death model from the previous strike is a counterexample.

### Route C — equivariant finite-image compactness

Still open and viable. Theorem 7.1 proves it would be sufficient, while Corollary 8.1 and Theorem 9.1 describe exactly what a counterexample must look like inside the prime graph.

---

# 13. Status

This strike establishes:

1. finite incoming-pattern realization in the actual prime graph by CRT + Dirichlet;
2. explicit failure of naive countable future compactness;
3. stronger future-type failure inside every infinite exact fiber;
4. the necessity of an equivariant, moving-parameter formulation;
5. the Eventual Bi-Finite Image property (EBFI);
6. an EBFI compactness theorem yielding a global automorphism from arbitrarily deep finite survival;
7. the eternal image-escape necessary condition for noncompact death;
8. extraction of an escaping sequence of distinct primes inside one exact fiber at a minimal escape height.

The next target is now highly concrete:

\[
\boxed{
\text{close the first image-escape channel }X_{\{2,3\}}\to X_{\{2,5\}}
\text{ for }p=7\text{ or exhibit an escaping sequence.}
}
\]

No publication claim is made yet. HATTER-SOL-06 remains active research.
