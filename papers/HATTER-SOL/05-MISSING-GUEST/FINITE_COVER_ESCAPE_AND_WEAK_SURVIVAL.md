# HATTER-SOL-05 · Finite-Cover Escape and a Weaker Survival Hypothesis

## 0. Purpose

HATTER-SOL-05 began with the strongest possible killing strategy for the first Fermat-layer transposition

\[
\tau=(3\ 5):
\]

find an exact predecessor support \(S\) such that

\[
\mu(S)=0,
\qquad
\mu(\tau S)>0,
\]

or conversely.

The first proposed route was a finite covering-congruence obstruction: prove that every number

\[
1+\prod_{q\in S}q^{e_q},
\qquad e_q\ge1,
\]

is divisible by one of finitely many auxiliary primes.

This note proves that **such a finite cover is impossible for every exact support \(S\ni2\)**.

The strike also improves the conditional non-rigidity theorem from HATTER-SOL-04: infinitude of the Fermat primes is not needed. It is enough to assume infinitude only for exact fibers above the Fermat layer.

---

# 1. Exact-support candidate family

Fix a finite set of primes

\[
S\subset\mathbb P,
\qquad 2\in S.
\]

For an exponent vector

\[
\mathbf e=(e_q)_{q\in S}
\in\mathbb N_{>0}^{S},
\]

put

\[
N_S(\mathbf e)
=
1+\prod_{q\in S}q^{e_q}.
\]

Then

\[
X_S
=
\{N_S(\mathbf e):N_S(\mathbf e)\text{ is prime}\}
\]

is exactly the prime fiber with predecessor support \(S\).

---

# 2. Finite-divisor escape theorem

## Theorem 2.1 — simultaneous escape from every finite prime set

Let \(S\) be a finite set of primes containing \(2\), and let \(T\) be any finite set of primes.

Then there exist positive integers

\[
m_q\ge1
\qquad(q\in S)
\]

such that for every positive integer \(t\),

\[
\boxed{
\gcd\!\left(
N_S((tm_q)_{q\in S}),
\prod_{\ell\in T}\ell
\right)=1.
}
\]

Thus a whole infinite ray of exponent vectors avoids every prime in \(T\) simultaneously.

### Proof

For \(q\in S\), define

\[
m_q
=
\operatorname{lcm}_{\ell\in T\setminus S}
\operatorname{ord}_{\ell}(q),
\]

with the empty least common multiple interpreted as \(1\).

This is well-defined because if \(\ell\notin S\), then \(\ell\ne q\), so \(q\) is invertible modulo \(\ell\).

Fix \(t\ge1\), and write

\[
M_t=
\prod_{q\in S}q^{tm_q}.
\]

Take \(\ell\in T\).

### Case 1: \(\ell\in S\)

Then \(\ell\mid M_t\), hence

\[
N_S((tm_q))
=1+M_t
\equiv1\pmod\ell.
\]

So \(\ell\nmid N_S((tm_q))\).

### Case 2: \(\ell\notin S\)

For every \(q\in S\), the exponent \(m_q\) is divisible by \(\operatorname{ord}_{\ell}(q)\). Therefore

\[
q^{tm_q}\equiv1\pmod\ell.
\]

Hence

\[
M_t\equiv1\pmod\ell
\]

and therefore

\[
N_S((tm_q))
\equiv2\pmod\ell.
\]

Because \(2\in S\), the case \(\ell=2\notin S\) cannot occur. Thus \(2\not\equiv0\pmod\ell\), and again \(\ell\nmid N_S((tm_q))\).

No prime in \(T\) divides the candidate. \(\square\)

---

# 3. Arbitrarily rough candidates

For an integer \(n>1\), let \(P^-(n)\) denote its least prime factor.

## Corollary 3.1

For every bound \(B\ge2\), there are infinitely many exponent vectors \(\mathbf e\) such that

\[
\boxed{
P^-(N_S(\mathbf e))>B.
}
\]

Here, if \(N_S(\mathbf e)\) itself is prime, then \(P^-(N_S(\mathbf e))=N_S(\mathbf e)\).

### Proof

Apply Theorem 2.1 with \(T\) equal to the set of all primes \(\ell\le B\). Along the resulting ray \(t=1,2,3,\ldots\), the values \(N_S\) are strictly increasing and have no prime divisor at most \(B\). \(\square\)

Thus even if \(X_S\) were empty, compositeness could not be explained by a bounded collection of small prime divisors.

---

# 4. No finite covering congruence can prove an exact fiber empty

## Corollary 4.1 — finite-cover no-go

There is no finite set of primes \(T\) such that every number

\[
N_S(\mathbf e)
=
1+\prod_{q\in S}q^{e_q}
\]

has a prime divisor in \(T\).

In particular, no standard finite covering-congruence argument with finitely many fixed prime divisors can prove

\[
X_S=\varnothing.
\]

### Interpretation

A Sierpiński-type one-parameter sequence can sometimes be covered by finitely many fixed divisors. Our exact-support family is different: **all support exponents remain free**. By synchronizing every exponent with the multiplicative orders modulo a proposed finite divisor set, the entire family escapes that cover.

This does not prove that \(X_S\ne\varnothing\). It proves something more precise about the difficulty:

\[
\boxed{
\text{if an exact fiber is empty, its compositeness mechanism must use unboundedly many prime divisors.}
}
\]

So Strike A from the initial HATTER-SOL-05 plan is closed in its naive finite-cover form.

---

# 5. Local admissibility of every exact support

Theorem 2.1 suggests a useful terminology.

## Definition 5.1

Call a support \(S\ni2\) **finitely divisor-admissible** if for every finite prime set \(T\) there exists an exponent vector \(\mathbf e\) such that

\[
\gcd(N_S(\mathbf e),\prod_{\ell\in T}\ell)=1.
\]

## Corollary 5.2

\[
\boxed{
\text{Every finite exact support }S\ni2\text{ is finitely divisor-admissible.}
}
\]

Hence there is no local obstruction of the finite fixed-divisor type distinguishing

\[
S
\quad\text{from}\quad
\tau S.
\]

Any arithmetic killing certificate for \((3\ 5)\) must be genuinely stronger.

---

# 6. Why this does not prove prime values

The escape theorem should not be confused with a prime-producing theorem.

It guarantees candidates with arbitrarily large least prime factor, but a sequence of such candidates may still be composite forever, with the prime divisors themselves drifting to infinity.

The classical one-parameter Sierpiński problem already illustrates the distinction between:

- compositeness explained by a finite covering;
- compositeness without any known finite covering.

For our multi-exponent family, finite covers are ruled out automatically, but primality remains a much deeper global question.

For the smallest higher support

\[
S=\{2,3\},
\]

the prime values are Pierpont primes of the form

\[
2^a3^b+1.
\]

Their infinitude is conjectured but not known. Therefore no argument in this note assumes that \(X_{\{2,3\}}\) is infinite.

---

# 7. Removing an unnecessary Fermat-prime assumption

HATTER-SOL-04 used the following deliberately strong hypothesis:

> every finite support \(S\ni2\) has \(\mu(S)=\aleph_0\).

That hypothesis includes

\[
S=\{2\},
\]

so it implies infinitely many Fermat primes.

For extending symmetries **above the first Pratt layer**, this is unnecessary.

## Hypothesis HFI — Higher-Fiber Infinitude

For every finite support \(S\) satisfying

\[
2\in S,
\qquad
S\ne\{2\},
\]

assume

\[
\boxed{
\mu(S)=\aleph_0.
}
\]

Equivalently: every exact predecessor fiber of Pratt height at least two is countably infinite.

HFI says nothing about whether there are finitely or infinitely many Fermat primes.

---

# 8. Higher-Fiber Survival Theorem

Let

\[
G_n=
\operatorname{Aut}(\Pi\upharpoonright P_{\le n})
\]

be the finite-height automorphism tower from HATTER-SOL-04.

## Theorem 8.1

Assume HFI. Then for every \(n\ge1\), the restriction map

\[
\rho_n:G_{n+1}\to G_n
\]

is surjective.

### Proof

Take \(g\in G_n\), with \(n\ge1\), and let \(S\) be the predecessor support of a vertex in \(L_{n+1}\).

Since

\[
\max_{q\in S}h(q)=n\ge1,
\]

there is an odd prime in \(S\). Also \(2\in S\), because every odd prime has even predecessor. Therefore

\[
S\ne\{2\}.
\]

The same is true for \(gS\). By HFI,

\[
\mu(S)=\aleph_0=
\mu(gS).
\]

Hence every \(g\in G_n\) lies in the extendable subgroup \(E_n\). By the multiplicity-tower theorem,

\[
\operatorname{im}(\rho_n)=E_n=G_n.
\]

Thus \(\rho_n\) is surjective. \(\square\)

---

# 9. The Fermat swap survives under HFI

## Corollary 9.1

Assume HFI. Then **every permutation of the actually existing Fermat primes** extends to a global automorphism of \(\Pi\).

In particular,

\[
\boxed{
3\leftrightarrow5
\text{ extends globally under HFI.}
}
\]

### Proof

The first Pratt layer is

\[
L_1=X_{\{2\}},
\]

so

\[
G_1=\operatorname{Sym}(L_1).
\]

Choose any \(g_1\in G_1\). Theorem 8.1 makes every restriction map above level one surjective, so recursively choose

\[
g_2,g_3,\ldots
\]

with

\[
\rho_n(g_{n+1})=g_n.
\]

The inverse-limit theorem gives a global automorphism. \(\square\)

### Key improvement

No infinitude of Fermat primes is assumed.

Even if the currently known Fermat primes were all of them, HFI would still force the transposition

\[
(3\ 5)
\]

to survive globally.

---

# 10. Continuum many automorphisms under HFI

## Corollary 10.1

Assume HFI. Then

\[
\boxed{
|\operatorname{Aut}(\Pi)|=2^{\aleph_0}.
}
\]

### Proof

HFI implies that

\[
X_{\{2,3\}}
\]

is countably infinite. Therefore the kernel of

\[
G_2\to G_1
\]

contains

\[
\operatorname{Sym}(X_{\{2,3\}}),
\]

which has cardinality \(2^{\aleph_0}\).

By Theorem 8.1, every element of \(G_2\) extends through all higher levels, hence globally. Thus

\[
|\operatorname{Aut}(\Pi)|\ge2^{\aleph_0}.
\]

Since the prime graph is countable, its full permutation group has cardinality at most \(2^{\aleph_0}\). \(\square\)

---

# 11. The new dichotomy

The fifth-paper problem is now sharper than at its start.

A naive empty-fiber proof by finite covering congruences is impossible:

\[
\boxed{
\text{every exact support escapes every finite fixed divisor set}.}
\]

At the opposite extreme, one does not need the very strong Full Support Infinitude hypothesis from HATTER-SOL-04. It is enough that all higher fibers be infinite:

\[
\boxed{
\text{HFI}\Longrightarrow
(3\ 5)\text{ survives globally and }|\operatorname{Aut}(\Pi)|=2^{\aleph_0}.
}
\]

Thus the real arithmetic battleground is now the family

\[
S\ni2,
\qquad |S|\ge2,
\]

beginning with

\[
S=\{2,3\}
\quad\text{and}\quad
S=\{2,5\}.
\]

---

# 12. Next strike

The next attack should no longer search for a finite covering of all exponent vectors.

Instead we should study the **exact-support prime-value spectrum** itself:

\[
\mathcal E_S
=
\{\mathbf e\in\mathbb N_{>0}^{S}:N_S(\mathbf e)\text{ is prime}\}.
\]

The immediate target pair is

\[
\mathcal E_{\{2,3\}}
\quad\text{versus}\quad
\mathcal E_{\{2,5\}}.
\]

Useful questions are:

1. can one prove infinitude of one family from a theorem weaker than full Pierpont infinitude?
2. can one prove a graph-relevant cardinality asymmetry without determining either family completely?
3. can higher exact-support descendants amplify a weaker arithmetic asymmetry into a finite-height killing certificate?
4. is there a structural theorem showing that every nonempty higher fiber must be infinite under a standard prime-value conjecture?

The finite-cover route is now closed rigorously; the research must move to genuinely global prime-value arithmetic.

---

# Literature boundary

The proof of Theorem 2.1 is elementary and is not presented as a claim of literature-wide priority. Its role is to identify a no-go mechanism specific to the multi-exponent exact-support family.

For comparison, Sierpiński-type sequences \(k2^n+1\) are classical examples where finite covering congruences can force compositeness for every \(n\). The distinction here is that all exponents of all support primes are allowed to vary and can therefore be synchronized with multiplicative orders modulo any proposed finite divisor set.

The smallest higher fiber \(X_{\{2,3\}}\) belongs to the classical Pierpont-prime setting; infinitude of Pierpont primes remains conjectural.
