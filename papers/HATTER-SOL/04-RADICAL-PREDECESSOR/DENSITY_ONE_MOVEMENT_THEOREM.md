# HATTER-SOL-04 · Density-One Movement Theorem

## 0. Motivation

The infinite-propagation theorem proved that every nontrivial automorphism of the directed prime graph moves infinitely many primes and reaches arbitrarily large Pratt height.

This note strengthens that dramatically:

\[
\boxed{
\text{every nontrivial automorphism moves asymptotically almost every prime.}
}
\]

More precisely, the set of fixed primes has relative natural density zero inside the primes, and therefore the moved set has relative density one.

The argument uses only:

- preservation of predecessor support under a fixed point;
- the positive-density asymmetric-successor set forced by one moved prime;
- the prime number theorem in arithmetic progressions for finitely many congruence constraints.

---

# 1. The graph and relative prime density

Let

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

For a set \(A\subseteq\mathbb P\), define its relative upper density in the primes by

\[
\overline d_{\mathbb P}(A)
=
\limsup_{X\to\infty}
\frac{|A\cap[2,X]|}{\pi(X)}.
\]

If the limit exists, write \(d_{\mathbb P}(A)\).

Let

\[
\operatorname{Fix}(g)=\{p:g(p)=p\},
\qquad
\operatorname{supp}(g)=\mathbb P\setminus\operatorname{Fix}(g).
\]

---

# 2. A first positive-density moved set

Assume \(g\ne\mathrm{id}\), and choose a moved prime

\[
g(x)=y\ne x.
\]

Since \(2\) is fixed, both \(x\) and \(y\) are odd.

If a prime \(p\) is fixed by \(g\), then

\[
D(x,p)
\iff
D(g(x),g(p))
=
D(y,p).
\]

Hence every prime in the symmetric difference

\[
N^+(x)\triangle N^+(y)
\]

is moved.

Here

\[
N^+(q)=\{p:q\mid p-1\}.
\]

For distinct odd primes \(x,y\), the relative density of this symmetric difference is

\[
\delta(x,y)
=
\frac1{x-1}
+
\frac1{y-1}
-
\frac{2}{(x-1)(y-1)}
>0.
\]

This follows from the prime number theorem in arithmetic progressions: the events

\[
x\mid p-1,
\qquad
y\mid p-1
\]

have relative prime densities \(1/(x-1)\), \(1/(y-1)\), and joint density \(1/((x-1)(y-1))\).

Therefore

\[
\operatorname{supp}(g)
\]

contains a positive-density set of primes.

Consequently,

\[
\sum_{q\in\operatorname{supp}(g)}\frac1q
=
\infty,
\]

and hence also

\[
\boxed{
\sum_{q\in\operatorname{supp}(g)}\frac1{q-1}
=
\infty.
}
\]

---

# 3. Fixed vertices must see every automorphism orbit uniformly

Let \(p\in\operatorname{Fix}(g)\).

Then

\[
\operatorname{Pred}(p)
=
\operatorname{Pred}(g(p))
=
g(\operatorname{Pred}(p)).
\]

Thus the finite set \(\operatorname{Pred}(p)\) is \(g\)-invariant.

Equivalently, for any two primes \(a,b\) lying in the same \(g\)-orbit,

\[
\boxed{
 a\mid p-1
 \iff
 b\mid p-1.
}
\]

So a fixed target prime cannot distinguish two moduli belonging to the same automorphism orbit.

This elementary observation is the key to the density theorem.

---

# 4. Weighted pairing lemma on moved orbits

Put

\[
w(q)=\frac1{q-1}.
\]

The moved set is partitioned into \(g\)-orbits, each of size at least two.

## Lemma 4.1

There exists a countable family of pairwise disjoint pairs

\[
\{a_1,b_1\},
\{a_2,b_2\},
\ldots
\]

such that:

1. \(a_j,b_j\) lie in the same \(g\)-orbit for every \(j\);
2. all primes appearing in different pairs are distinct;
3.
\[
\boxed{
\sum_{j\ge1}
\bigl(w(a_j)+w(b_j)\bigr)
=\infty.
}
\]

### Proof

Work orbit by orbit.

For an infinite orbit, pair all its vertices arbitrarily.

For a finite even orbit, pair all vertices.

For a finite odd orbit, leave unpaired a vertex of minimum weight and pair all others. Because every moved orbit has at least two vertices, the omitted weight is at most half the total weight of that orbit.

Hence the total weight captured by all selected pairs is at least one half of

\[
\sum_{q\in\operatorname{supp}(g)}w(q),
\]

which diverges. \(\square\)

---

# 5. The equality condition for one pair

Fix one selected pair \(\{a,b\}\).

A fixed prime \(p\) must satisfy

\[
[a\mid p-1]=[b\mid p-1].
\]

Among reduced residue classes modulo \(ab\), there are

\[
(a-2)(b-2)+1
\]

classes satisfying this equality:

- \((a-2)(b-2)\) classes where neither congruence is \(1\);
- one class where both are \(1\).

Therefore the relative density among primes of this equality condition is

\[
E(a,b)
=
\frac{(a-2)(b-2)+1}{(a-1)(b-1)}.
\]

Writing

\[
u=w(a)=\frac1{a-1},
\qquad
v=w(b)=\frac1{b-1},
\]

we have

\[
E(a,b)
=
1-u-v+2uv.
\]

Since \(a,b\ge3\),

\[
0<u,v\le\frac12.
\]

Thus

\[
2uv\le\min(u,v)\le\frac{u+v}{2},
\]

so

\[
1-E(a,b)
=u+v-2uv
\ge
\frac{u+v}{2}.
\]

Hence

\[
\boxed{
E(a,b)
\le
\exp\left(-\frac{u+v}{2}\right).
}
\]

---

# 6. Density-One Movement Theorem

## Theorem 6.1

Let \(g\in\operatorname{Aut}(\Pi)\). If \(g\ne\mathrm{id}\), then

\[
\boxed{
 d_{\mathbb P}(\operatorname{Fix}(g))=0
}
\]

and therefore

\[
\boxed{
 d_{\mathbb P}(\operatorname{supp}(g))=1.
}
\]

In words: every nontrivial automorphism moves asymptotically almost every prime.

### Proof

Take the disjoint pairs

\[
\{a_j,b_j\}
\]

from Lemma 4.1.

For \(N\ge1\), let \(C_N\) be the set of primes \(p\) satisfying

\[
[a_j\mid p-1]=[b_j\mid p-1]
\qquad
(1\le j\le N).
\]

Every fixed prime, except possibly the finitely many moduli themselves, lies in every \(C_N\). Thus

\[
\operatorname{Fix}(g)
\subseteq^* C_N
\]

for all \(N\), where \(\subseteq^*\) means containment up to finitely many exceptions.

Because all pair moduli are distinct, the Chinese remainder theorem makes these congruence conditions independent at the finite level. By the prime number theorem in arithmetic progressions,

\[
 d_{\mathbb P}(C_N)
=
\prod_{j=1}^N E(a_j,b_j).
\]

Using the estimate above,

\[
 d_{\mathbb P}(C_N)
\le
\exp\left(
-\frac12
\sum_{j=1}^N
\bigl(w(a_j)+w(b_j)\bigr)
\right).
\]

The exponent tends to \(-\infty\) by Lemma 4.1. Therefore

\[
 d_{\mathbb P}(C_N)\to0.
\]

Since \(\operatorname{Fix}(g)\subseteq^*C_N\) for every \(N\),

\[
\overline d_{\mathbb P}(\operatorname{Fix}(g))
\le
 d_{\mathbb P}(C_N)
\]

for every \(N\). Letting \(N\to\infty\) gives

\[
\overline d_{\mathbb P}(\operatorname{Fix}(g))=0.
\]

Thus the relative prime density of the fixed set exists and equals zero, while its complement has density one. \(\square\)

---

# 7. Localized version inside every arithmetic progression

The theorem can be strengthened.

## Corollary 7.1

Fix any reduced residue class

\[
r\pmod m,
\qquad
\gcd(r,m)=1.
\]

If \(g\ne\mathrm{id}\), then among primes in this progression, the proportion fixed by \(g\) tends to zero.

Equivalently, the moved primes have relative density one inside every reduced arithmetic progression.

### Proof sketch

Discard the finitely many selected pairs containing a prime divisor of \(m\). The remaining paired weight still diverges.

For every finite collection of the remaining pairs, the equality constraints are independent of the fixed residue condition modulo \(m\) by CRT. The same product estimate therefore applies inside the progression. \(\square\)

So nontrivial movement is not concentrated in a few congruence classes: it is asymptotically ubiquitous across all reduced progressions.

---

# 8. Specialization to the Fermat swap

Suppose a global automorphism extends

\[
3\leftrightarrow5.
\]

The first propagation step already forces movement on the symmetric difference

\[
N^+(3)\triangle N^+(5).
\]

Its relative density among primes is

\[
\frac1{2}
+
\frac1{4}
-
\frac{2}{8}
=
\frac12.
\]

Thus at least half of all primes are moved before any recursive propagation is used.

The density-one theorem then upgrades this to

\[
\boxed{
\text{a global }(3\ 5)\text{ automorphism would move density }1\text{ of all primes}.}
\]

In particular, the fixed primes would form a zero-density exceptional set.

---

# 9. Conceptual consequence

The previous results gave:

\[
\text{finite future patterns are too flexible to distinguish equal-predecessor vertices},
\]

and

\[
\text{one moved vertex forces infinitely many moved successors of unbounded height}.
\]

The present theorem strengthens the second statement to

\[
\boxed{
\text{nontrivial symmetry, if it exists, is almost everywhere movement}.}
\]

So there is no middle regime in which a nontrivial automorphism merely rearranges a sparse exceptional family of primes.

Either

\[
\operatorname{Aut}(\Pi)=1,
\]

or every nonidentity element acts globally on a density-one subset of the prime vertices.

---

# 10. What this does not prove

Relative density is an external arithmetic statistic, not part of the language of the directed graph.

Therefore an automorphism is not required *a priori* to preserve the natural density of arbitrary vertex sets.

So the density-one theorem does **not** itself imply rigidity.

Its role is different: it gives a strong unconditional structural constraint on any hypothetical nontrivial automorphism.

---

# 11. Next research question

The new theorem suggests a sharper target:

> Can a density-one moved set be reconciled with the multiplicity-tower compatibility conditions at every Pratt height?

A contradiction would prove rigidity.

If no contradiction can be found, then HATTER-SOL-04 already has a meaningful unconditional theorem package:

1. exact multiplicity-tower recursion;
2. finite-future indistinguishability;
3. infinite propagation to unbounded height;
4. density-one movement of every nontrivial automorphism;
5. conditional large-automorphism theorem under full support infinitude.

This is now close to an article-level structural package even if the original 2012 automorphism problem remains unresolved.
