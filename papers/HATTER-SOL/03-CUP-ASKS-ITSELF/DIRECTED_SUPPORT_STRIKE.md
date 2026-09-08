# HATTER-SOL-03 · Directed-Support Strike

## 0. Target

The current frontier is the directed prime graph

\[
\Pi_D=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

The question is whether erasing the exact exponent depth from the labelled \(p-1\) structure still leaves enough information to force rigidity:

\[
\boxed{\operatorname{Aut}(\Pi_D)=1\ ?}
\]

This note records what can be proved unconditionally, where the elementary induction stops, and what arithmetic data control any further extension of a putative symmetry.

---

# 1. Finite seeds in pure multiplication cannot self-generate rigidity

Let

\[
\mathcal M=(\mathbb N_{>0},\times)
\]

and let

\[
\bar a=(a_1,\ldots,a_k)
\]

be a finite tuple of parameters.

For a prime \(p\), define the valuation signature

\[
\nu_{\bar a}(p)
=
(v_p(a_1),\ldots,v_p(a_k))\in\mathbb N^k.
\]

For a signature \(s\in\mathbb N^k\), put

\[
C_s=\{p\in\mathbb P:\nu_{\bar a}(p)=s\}.
\]

## Theorem 1.1 — exact finite-seed stabilizer

The pointwise stabilizer of \(\bar a\) is

\[
\boxed{
\operatorname{Aut}(\mathcal M/\bar a)
\cong
\prod_s\operatorname{Sym}(C_s),
}
\]

where the product runs over nonempty valuation-signature fibers.

Equivalently,

\[
\boxed{
p\sim_{\bar a}q
\iff
\nu_{\bar a}(p)=\nu_{\bar a}(q).}
\]

### Proof

Every automorphism of \(\mathcal M\) is induced by a permutation of the prime generators. Such a permutation fixes every \(a_i\) exactly when it preserves the exponent of each moved prime in every \(a_i\), i.e. exactly when it preserves \(\nu_{\bar a}\). Thus arbitrary independent permutations inside each fiber \(C_s\) are allowed, and no permutation between different fibers is allowed. \(\square\)

## Corollary 1.2 — finite-seed barrier

Only finitely many primes occur in the support of the tuple \(\bar a\). Hence

\[
C_{\mathbf 0}
=
\{p:v_p(a_i)=0\text{ for all }i\}
\]

is cofinite in \(\mathbb P\), in particular infinite. Therefore

\[
\boxed{
\operatorname{Aut}(\mathcal M/\bar a)\ne1
}
\]

for every finite tuple \(\bar a\).

So pure multiplication plus finitely many multiplicative seeds cannot generate complete individuality of the primes.

---

# 2. The labelled \(p-1\) graph is rigid

For primes \(q,p\), put an arc

\[
q\to p
\iff
q\mid p-1,
\]

and label that arc by

\[
\lambda(q,p)=v_q(p-1).
\]

This is the natural labelled prime-chain graph already used in the literature on prime chains and in Jones's graph \(\Pi\).

Call the labelled graph \(\Pi_\lambda\).

## Theorem 2.1 — exact-depth rigidity

\[
\boxed{
\operatorname{Aut}(\Pi_\lambda)=\{\mathrm{id}\}.
}
\]

### Proof

We use strong induction on the ordinary numerical value of the prime.

The prime \(2\) is the unique vertex with no incoming arc, so it is fixed.

Assume every prime \(q<p\) is fixed. Every incoming neighbour of \(p\) is a prime divisor of \(p-1\), hence is less than \(p\), and is therefore fixed by the induction hypothesis. A label-preserving automorphism must send \(p\) to a prime \(p'\) having exactly the same labelled predecessor data:

\[
\{(q,v_q(p-1)):q\mid p-1\}
=
\{(q,v_q(p'-1)):q\mid p'-1\}.
\]

Taking the product of the corresponding prime powers gives

\[
p-1
=
\prod_{q\mid p-1}q^{v_q(p-1)}
=
\prod_{q\mid p'-1}q^{v_q(p'-1)}
=
p'-1.
\]

Hence \(p'=p\). By induction every prime is fixed. \(\square\)

## Interpretation

Exact exponent depth makes the predecessor relation **extensional**: the labelled incoming data reconstruct the vertex.

This gives a clean mechanism:

\[
\boxed{
\text{well-founded descent}
+
\text{extensional predecessor code}
\Longrightarrow
\text{rigidity}.
}
\]

The finite-language relation

\[
H(a,p)
\iff
\bigl(a=q^{v_q(p-1)}\text{ for some prime }q\mid p-1\bigr)
\]

is just a compression of the same exact-depth information into one binary relation on the multiplicative carrier. Therefore

\[
\operatorname{Aut}(\mathbb N_{>0},\times,H)=1.
\]

---

# 3. Erasing depth destroys local extensionality immediately

Now forget the labels and keep only

\[
D(q,p)\iff q\mid p-1.
\]

Write

\[
\operatorname{Pred}(p)
=
\{q\in\mathbb P:q\mid p-1\}.
\]

The predecessor map is not injective:

\[
\operatorname{Pred}(3)
=
\operatorname{Pred}(5)
=
\{2\},
\]

and

\[
\operatorname{Pred}(7)
=
\operatorname{Pred}(13)
=
\{2,3\}.
\]

Thus the exact induction from Theorem 2.1 cannot survive the erasure of the exponent labels.

This does **not** prove that \(\Pi_D\) has a nontrivial global automorphism. Future incidence may still distinguish locally identical vertices.

That distinction is the new barrier.

---

# 4. Pratt height is graph-theoretic and must be preserved

Define the Pratt height recursively by

\[
h(2)=0,
\]

and for odd prime \(p\),

\[
h(p)=1+\max_{q\mid p-1}h(q).
\]

Because every predecessor \(q\) is smaller than \(p\), this is finite.

## Lemma 4.1

Every automorphism of \(\Pi_D\) preserves \(h\).

### Proof

The function \(h\) is exactly the well-founded rank of the directed predecessor relation. Relation automorphisms preserve well-founded rank. \(\square\)

Hence any possible automorphism must act level by level through the Pratt hierarchy.

---

# 5. Exact predecessor fibers

For a finite set \(S\subset\mathbb P\), define

\[
X_S
=
\{p\in\mathbb P:\operatorname{Pred}(p)=S\}
\]

and its multiplicity

\[
\mu(S)=|X_S|
\in
\{0,1,2,\ldots,\aleph_0\}.
\]

Every vertex in \(X_S\) has height

\[
1+\max_{q\in S}h(q).
\]

An automorphism \(g\) necessarily satisfies

\[
\boxed{
g(X_S)=X_{g(S)}}
\]

and therefore

\[
\boxed{
\mu(S)=\mu(g(S)).
}
\]

for every finite predecessor set \(S\).

This multiplicity spectrum is the arithmetic fingerprint that remains after exponent depth has been erased.

---

# 6. Rank-by-rank extension criterion

Let

\[
P_{\le n}=\{p\in\mathbb P:h(p)\le n\}.
\]

Suppose \(g_n\) is an automorphism of the induced directed graph on \(P_{\le n}\).

For every finite set \(S\subseteq P_{\le n}\) with

\[
\max_{q\in S}h(q)=n,
\]

the fiber \(X_S\) lies in level \(n+1\).

## Theorem 6.1 — support-extension criterion

The automorphism \(g_n\) extends to an automorphism of the graph on \(P_{\le n+1}\) if and only if

\[
\boxed{
\mu(S)=\mu(g_n(S))
}
\]

for every predecessor set \(S\) occurring at level \(n+1\).

Whenever this condition holds, the extensions are obtained by choosing arbitrary bijections

\[
X_S\longrightarrow X_{g_n(S)}
\]

independently over all such fibers.

### Proof

Necessity follows from preservation of exact predecessor sets.

For sufficiency, the level \(n+1\) vertices are partitioned into the fibers \(X_S\), and there are no arcs between vertices of the same level because every arc strictly increases Pratt height. Hence arbitrary fiberwise bijections compatible with the already defined action on the predecessors preserve all arcs whose endpoints lie in \(P_{\le n+1}\). \(\square\)

Therefore the full automorphism group of \(\Pi_D\) is the inverse limit of this rank-by-rank extension process.

This is an exact reduction of the support-only rigidity problem to the arithmetic multiplicity spectrum \(\mu(S)\).

---

# 7. The first fiber already touches the Fermat-prime problem

Consider

\[
X_{\{2\}}
=
\{p:\operatorname{Pred}(p)=\{2\}\}.
\]

The condition says

\[
p-1=2^m
\]

for some \(m\ge1\). If \(2^m+1\) is prime, then \(m\) must be a power of \(2\), so these are exactly the Fermat primes:

\[
3,5,17,257,65537,\ldots
\]

Thus

\[
\boxed{
\mu(\{2\})
=
\#\{\text{Fermat primes}\}.
}
\]

Only five Fermat primes are currently known, and it is unknown whether any further Fermat primes exist.

This does not itself decide \(\operatorname{Aut}(\Pi_D)\), but it shows that even the first nontrivial predecessor fiber carries unresolved arithmetic information.

An exact classification of the support-only automorphism group therefore cannot be treated as a routine graph-theoretic corollary of the labelled case.

---

# 8. Relation to known prime-chain and Rado results

The directed graph

\[
q\to p\iff q\mid p-1
\]

is classical in prime-chain / Pratt-tree work.

Jones proves that every finite acyclic labelled directed graph occurs as an induced finite prime graph of this type. He also proves that after deleting \(2\), forgetting all labels and forgetting orientation, the resulting graph on odd primes is the Rado graph.

That Rado theorem establishes enormous symmetry for the **undirected shadow**, but it does not settle the automorphism group of the full directed support graph \(\Pi_D\).

The reason is exactly the finite-past structure exposed above: every prime has a finite exact predecessor set, and a global automorphism must preserve the entire rank-by-rank multiplicity spectrum.

---

# 9. What the strike resolves

The current hierarchy is now rigorous:

\[
\boxed{
\text{pure multiplication + finite seeds}
\Longrightarrow
\text{non-rigid}
}
\]

\[
\boxed{
\text{directed support only }D(q,p)
\Longrightarrow
\text{rigidity presently unresolved by this method}
}
\]

\[
\boxed{
\text{directed support + exact exponent depth}
\Longrightarrow
\text{rigid}
}
\]

and the exact reason the middle case is hard is no longer vague:

\[
\boxed{
\text{depth erasure}
\Longrightarrow
\text{loss of extensionality}
\Longrightarrow
\text{dependence on exact shifted-smooth-prime fiber multiplicities}.}
\]

---

# 10. New conceptual law for HATTER-SOL-03

HATTER-SOL-02 ended with

\[
\text{individuality}=\text{sufficiency of separation}.
\]

The third paper now refines this:

\[
\boxed{
\text{self-generated rigidity}
=
\text{well-founded separation}
+
\text{enough extensionality to anchor the recursion}.}
\]

If the questions are anonymous and the predecessor code is not extensional, symmetry can survive or return.

If the recursive predecessor data reconstruct each vertex, the cup can indeed "ask the questions itself".

---

# 11. Next strike

The next useful target is no longer to guess whether \(\Pi_D\) is rigid.

Instead:

1. seek a **strictly weaker-than-exact-depth label** that restores extensionality and hence rigidity;
2. quantify the minimum depth information required to distinguish the first collisions
   \[
   3\leftrightarrow5,
   \qquad
   7\leftrightarrow13;
   \]
3. test finite coarse labelings such as
   \[
   v_q(p-1)=1\quad\text{vs}\quad v_q(p-1)\ge2,
   \]
   and determine whether they still admit unavoidable predecessor collisions;
4. perform a hostile literature audit for automorphisms of the full directed prime-chain graph itself. No exact result on \(\operatorname{Aut}(\Pi_D)\) was located in the current targeted search.

The publication threshold for HATTER-SOL-03 is now close: the branch already has a finite-seed impossibility theorem, an anonymous-probe symmetry warning, an exact-depth rigidity theorem, and a precise reduction of the support-only case to an arithmetic multiplicity spectrum. One more nontrivial minimality theorem would make the article substantially stronger.
