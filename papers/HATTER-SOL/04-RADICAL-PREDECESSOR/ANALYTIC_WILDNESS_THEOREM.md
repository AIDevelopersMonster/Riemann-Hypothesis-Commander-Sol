# HATTER-SOL-04 · Analytic Wildness Theorem

## 0. Purpose of the strike

The density-one movement theorem showed that a nonidentity automorphism of the directed prime graph, if one exists, must move asymptotically almost every prime.

A natural question remains: could such an automorphism nevertheless be "almost the identity" numerically, for example by exchanging nearby primes?

The answer is no.

This note proves that every automorphism which is asymptotically near the identity in prime rank — equivalently, asymptotically near the identity in numerical size — is actually the identity.

Thus a hypothetical nontrivial automorphism must be wild in two independent senses:

1. it moves a density-one set of prime vertices;
2. it makes macroscopic displacements in the ordered list of primes infinitely often.

---

# 1. Setup

Let

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Write the primes in increasing order as

\[
p_1=2<p_2=3<p_3=5<\cdots.
\]

Every permutation \(g\) of the primes induces a permutation \(\sigma_g\) of \(\mathbb N\) by

\[
g(p_n)=p_{\sigma_g(n)}.
\]

For a set \(A\subseteq\mathbb P\), its relative density in the primes is the natural density of its index set

\[
I(A)=\{n:p_n\in A\}.
\]

---

# 2. Near-identity permutations preserve natural density

## Lemma 2.1

Let \(\sigma\) be a permutation of \(\mathbb N\) such that

\[
\boxed{
\frac{\sigma(n)}{n}\to1.
}
\]

Then for every set \(A\subseteq\mathbb N\) having natural density \(d(A)\), the image \(\sigma(A)\) also has natural density and

\[
\boxed{
d(\sigma(A))=d(A).
}
\]

### Proof

Fix \(\varepsilon\in(0,1)\). There is \(N_0\) such that for every \(n\ge N_0\),

\[
(1-\varepsilon)n\le \sigma(n)\le(1+\varepsilon)n.
\]

Let

\[
A(X)=|A\cap[1,X]|,
\qquad
B(X)=|\sigma(A)\cap[1,X]|.
\]

If \(n\in A\), \(n\ge N_0\), and

\[
n\le \frac{X}{1+\varepsilon},
\]

then \(\sigma(n)\le X\). Hence

\[
A\!\left(\frac{X}{1+\varepsilon}\right)-O(1)
\le B(X).
\]

Conversely, if \(\sigma(n)\le X\) and \(n\ge N_0\), then

\[
(1-\varepsilon)n\le X,
\]

so

\[
n\le \frac{X}{1-\varepsilon}.
\]

Therefore

\[
B(X)
\le
A\!\left(\frac{X}{1-\varepsilon}\right)+O(1).
\]

Divide by \(X\) and let \(X\to\infty\). Since \(A(T)=d(A)T+o(T)\),

\[
\frac{d(A)}{1+\varepsilon}
\le
\liminf\frac{B(X)}X
\le
\limsup\frac{B(X)}X
\le
\frac{d(A)}{1-\varepsilon}.
\]

Finally let \(\varepsilon\downarrow0\). Thus \(B(X)/X\to d(A)\). \(\square\)

---

# 3. Successor neighborhoods have distinct prime densities

For a prime \(q\), define

\[
N^+(q)=\{p\in\mathbb P:q\mid p-1\}.
\]

By the prime number theorem in arithmetic progressions,

\[
\boxed{
d_{\mathbb P}(N^+(q))=\frac1{q-1}.
}
\]

These densities are pairwise distinct as \(q\) ranges over the primes.

If \(g\in\operatorname{Aut}(\Pi)\), then

\[
\boxed{
g(N^+(q))=N^+(g(q)).
}
\]

because

\[
D(q,p)
\iff
D(g(q),g(p)).
\]

This gives an external analytic coordinate for every prime vertex: the relative density of its outgoing neighborhood is exactly \(1/(q-1)\).

The coordinate is not graph-internal, because an arbitrary permutation of the prime set need not preserve natural density. But any sufficiently tame permutation does preserve it.

---

# 4. Prime-rank rigidity theorem

## Theorem 4.1 — near-identity rank rigidity

Let \(g\in\operatorname{Aut}(\Pi)\), and let

\[
g(p_n)=p_{\sigma_g(n)}.
\]

If

\[
\boxed{
\frac{\sigma_g(n)}n\to1,
}
\]

then

\[
\boxed{g=\mathrm{id}.}
\]

### Proof

By Lemma 2.1, \(g\) preserves relative prime density for every prime set having such a density.

Fix a prime \(q\). Since

\[
g(N^+(q))=N^+(g(q)),
\]

we obtain

\[
\frac1{q-1}
=
d_{\mathbb P}(N^+(q))
=
d_{\mathbb P}(N^+(g(q)))
=
\frac1{g(q)-1}.
\]

Hence

\[
g(q)=q.
\]

This holds for every prime \(q\), so \(g=\mathrm{id}\). \(\square\)

---

# 5. Numerical-size version

The prime number theorem gives

\[
p_n\sim n\log n.
\]

Consequently, if

\[
\frac{p_{\sigma(n)}}{p_n}\to1,
\]

then

\[
\frac{\sigma(n)}n\to1.
\]

Indeed, if the index ratio failed to approach \(1\), some subsequence would remain bounded away from \(1\) on one side, and the asymptotic \(p_n\sim n\log n\) would force the corresponding prime ratio to remain bounded away from \(1\).

Therefore:

## Corollary 5.1 — near-identity size rigidity

If \(g\in\operatorname{Aut}(\Pi)\) satisfies

\[
\boxed{
\frac{g(p)}p\to1
\qquad(p\to\infty\text{ through primes}),
}
\]

then

\[
\boxed{g=\mathrm{id}.}
\]

Equivalently, any automorphism with

\[
|g(p)-p|=o(p)
\]

is trivial.

---

# 6. Macroscopic displacement corollary

The contrapositive gives a useful unconditional constraint.

## Corollary 6.1

If \(g\ne\mathrm{id}\), then there exists \(\varepsilon>0\) and infinitely many indices \(n\) such that

\[
\boxed{
|\sigma_g(n)-n|\ge \varepsilon n.
}
\]

Likewise, there exists \(\delta>0\) and infinitely many primes \(p\) such that

\[
\boxed{
|g(p)-p|\ge \delta p.
}
\]

### Proof

If no such \(\varepsilon\) existed, then \(\sigma_g(n)/n\to1\), and Theorem 4.1 would give \(g=\mathrm{id}\).

The numerical statement follows from the prime number theorem. \(\square\)

Thus a hypothetical nontrivial automorphism cannot be built from adjacent swaps, uniformly bounded prime-rank displacement, or any perturbation that becomes relatively small at infinity.

---

# 7. Density-preserving rigidity

The proof contains a slightly more abstract theorem.

## Theorem 7.1

Suppose \(g\in\operatorname{Aut}(\Pi)\) has the property that for every prime \(q\),

\[
d_{\mathbb P}(g(N^+(q)))
=
d_{\mathbb P}(N^+(q)).
\]

Then

\[
\boxed{g=\mathrm{id}.}
\]

### Proof

Since

\[
g(N^+(q))=N^+(g(q)),
\]

we get

\[
\frac1{q-1}
=
\frac1{g(q)-1},
\]

so \(g(q)=q\) for every prime. \(\square\)

Thus nontrivial graph symmetry can exist only by distorting the external arithmetic density profile of outgoing neighborhoods.

---

# 8. Combined wildness law

Together with the previously proved density-one movement theorem, we obtain:

## Theorem 8.1 — combined wildness

If \(g\in\operatorname{Aut}(\Pi)\) is nontrivial, then simultaneously

\[
\boxed{
d_{\mathbb P}(\operatorname{supp}(g))=1,
}
\]

and

\[
\boxed{
\frac{\sigma_g(n)}n\not\to1.
}
\]

Hence there is no nontrivial automorphism in either of the two intuitive "small symmetry" regimes:

1. sparse movement;
2. asymptotically local movement.

A nonidentity automorphism, if it exists, must be both **ubiquitous** and **macroscopically displacing**.

---

# 9. Consequence for the Fermat swap

If the transposition

\[
3\leftrightarrow5
\]

extends to a global automorphism, then the resulting automorphism:

- moves a density-one subset of all primes;
- reaches arbitrarily large Pratt height;
- has infinitely branching moved future;
- and must displace prime rank by a positive proportion infinitely often.

Thus the phrase "swap \(3\) and \(5\)" is misleading at the global level. Any extension would be an enormous rearrangement of essentially the entire prime universe.

---

# 10. Did density-one movement contradict the multiplicity tower?

No direct contradiction emerges from density alone.

The multiplicity tower is purely combinatorial: it asks whether exact predecessor-fiber cardinalities are preserved under successive finite-height permutations. Natural density is external to the language of the graph, and a wild permutation is free to distort it.

This explains why the density-one theorem by itself cannot close the original automorphism problem.

However, the present theorem narrows the remaining possibility sharply:

\[
\boxed{
\text{any surviving inverse-limit branch must be analytically wild.}
}
\]

The next useful attack should therefore not try to derive a contradiction from density alone. It should ask whether multiplicity-tower compatibility can force **any form of asymptotic regularity**. If it can, Theorem 4.1 will immediately collapse the automorphism to the identity.

---

# 11. Publication status

At this point HATTER-SOL-04 contains a coherent unconditional theorem package:

1. exact multiplicity-tower recursion and inverse-limit description;
2. finite-future indistinguishability over equal-predecessor vertices;
3. infinite propagation and unbounded Pratt-height movement;
4. density-one movement for every nonidentity automorphism;
5. near-identity rank/size rigidity and macroscopic-displacement necessity;
6. conditional continuum-sized automorphism group under full support infinitude.

The original directed-prime automorphism problem remains unresolved. The branch should therefore be presented as a structural analysis of the problem, not as a solution of the 2012 question.

The package is now strong enough to justify a publication draft after one more hostile literature/proof audit, even if no final yes/no rigidity theorem is obtained.
