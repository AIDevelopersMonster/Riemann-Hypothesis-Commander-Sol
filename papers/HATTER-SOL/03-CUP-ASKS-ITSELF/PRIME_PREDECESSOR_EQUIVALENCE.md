# HATTER-SOL-03 · Prime-Predecessor Equivalence

## 0. Why this note matters

The literature audit revealed a cleaner interpretation of the positive rigidity mechanism.

The adaptive binary relation

\[
J(a,p)
\iff
\begin{cases}
p\text{ is prime},\\
a=q^k\text{ is a nontrivial prime power},\\
a\mid p-1,
\end{cases}
\]

is not merely a convenient way to query valuation depth.

Over the multiplicative monoid it is first-order equivalent to the **prime-restricted predecessor relation**

\[
S_{\mathbb P}(n,p)
\iff
p\in\mathbb P\text{ and }p=n+1.
\]

This gives a much sharper answer to the HATTER-SOL-03 question:

\[
\boxed{
\text{one finite binary relation carrying the exact predecessor of each prime is enough for rigidity.}
}
\]

The query-ladder picture remains useful, but it is one presentation of a simpler relational core.

---

# 1. Multiplicative preliminaries

In

\[
\mathcal M=(\mathbb N_{>0},\times)
\]

divisibility is first-order definable by

\[
a\mid b
\iff
\exists c\;(ac=b).
\]

The constant \(1\) is definable as the multiplicative identity.

Primality is definable by

\[
\operatorname{Prime}(p)
\iff
p\ne1
\land
\forall d\,(d\mid p\Rightarrow d=1\lor d=p).
\]

A nontrivial prime power is definable by requiring that all of its nontrivial prime divisors are equal. We denote this predicate by

\[
\operatorname{PPow}(a).
\]

---

# 2. From prime predecessor to adaptive power queries

Assume \(S_{\mathbb P}\) is given.

Then

\[
\boxed{
J(a,p)
\iff
\operatorname{PPow}(a)
\land
\exists n\,
\bigl(S_{\mathbb P}(n,p)\land a\mid n\bigr).
}
\]

Indeed, \(S_{\mathbb P}(n,p)\) says exactly that \(n=p-1\), so the right-hand side says precisely that the prime power \(a\) divides \(p-1\).

Thus

\[
J\le_{\mathrm{def}}S_{\mathbb P}.
\]

---

# 3. From adaptive power queries to prime predecessor

Now assume \(J\) is given.

Define

\[
\Phi(n,p)
\]

to mean

\[
\operatorname{Prime}(p)
\land
\forall a\,
\bigl(
\operatorname{PPow}(a)
\Rightarrow
(J(a,p)\leftrightarrow a\mid n)
\bigr).
\]

## Theorem 3.1 — prime-predecessor recovery

For positive integers \(n,p\),

\[
\boxed{
\Phi(n,p)
\iff
S_{\mathbb P}(n,p).
}
\]

### Proof

If \(S_{\mathbb P}(n,p)\), then \(n=p-1\), so by definition \(J(a,p)\) holds exactly for the nontrivial prime powers dividing \(n\). Hence \(\Phi(n,p)\).

Conversely, suppose \(\Phi(n,p)\). Then \(n\) and \(p-1\) have exactly the same nontrivial prime-power divisors.

For every prime \(q\), the largest \(k\) such that \(q^k\mid n\) is therefore the same as the largest \(k\) such that \(q^k\mid p-1\). Hence

\[
v_q(n)=v_q(p-1)
\]

for every prime \(q\). By unique factorization,

\[
n=p-1.
\]

The case \(p=2\) is included: \(J(-,2)\) has no nontrivial prime-power witness, forcing \(n=1\). Therefore \(S_{\mathbb P}(n,p)\). \(\square\)

Thus

\[
S_{\mathbb P}\le_{\mathrm{def}}J.
\]

Combining Sections 2 and 3:

## Corollary 3.2

Over \((\mathbb N_{>0},\times)\),

\[
\boxed{
J\equiv_{\mathrm{def}}S_{\mathbb P}.
}
\]

---

# 4. Equivalence with the maximal exact-power relation

Recall

\[
H(a,p)
\iff
\begin{cases}
p\text{ prime},\\
a=q^e\text{ for some prime }q,\\
q^e\parallel p-1.
\end{cases}
\]

From \(J\), the maximal exact power is definable by

\[
H(a,p)
\iff
J(a,p)
\land
\neg\exists b\,
\bigl(
J(b,p)
\land a\mid b
\land a\ne b
\bigr).
\]

Because \(a\) and \(b\) are prime powers and \(a\mid b\), they have the same prime base.

Conversely,

\[
J(a,p)
\iff
\operatorname{PPow}(a)
\land
\exists b\,
\bigl(H(b,p)\land a\mid b\bigr).
\]

Hence

\[
\boxed{
H\equiv_{\mathrm{def}}J\equiv_{\mathrm{def}}S_{\mathbb P}
}
\]

over the multiplicative monoid.

This is the clean relational core of the positive mechanism.

---

# 5. Rigidity from the prime-predecessor relation

Let

\[
\mathcal S_{\mathbb P}
=
(\mathbb N_{>0},\times,S_{\mathbb P}).
\]

## Theorem 5.1 — prime-predecessor rigidity

\[
\boxed{
\operatorname{Aut}(\mathcal S_{\mathbb P})
=
\{\mathrm{id}\}.
}
\]

### Proof

The prime \(2\) is fixed because

\[
S_{\mathbb P}(1,2),
\]

and \(1\) is fixed by every multiplicative automorphism.

Assume by strong induction that every prime \(q<p\) is fixed.

All prime divisors of \(p-1\) are less than \(p\), so every such prime is fixed. Since a multiplicative automorphism fixing a prime \(q\) fixes every power \(q^e\), unique factorization implies that the integer \(p-1\) itself is fixed.

Now

\[
S_{\mathbb P}(p-1,p).
\]

If \(g\) is an automorphism, preservation of the relation gives

\[
S_{\mathbb P}(p-1,g(p)).
\]

But for a fixed predecessor integer \(p-1\), there is at most one successor integer, namely \(p\). Hence

\[
g(p)=p.
\]

By strong induction every prime is fixed, and unique factorization then fixes every positive integer. \(\square\)

By definitional equivalence, the same rigidity theorem holds for \((\mathbb N_{>0},\times,J)\) and \((\mathbb N_{>0},\times,H)\).

---

# 6. The support-only relation is the radical predecessor

Now consider only

\[
D(q,p)
\iff
q,p\in\mathbb P
\text{ and }
q\mid p-1.
\]

Over the full multiplicative carrier, \(D\) is first-order equivalent to the relation

\[
R_{\mathbb P}(r,p)
\iff
p\in\mathbb P
\text{ and }
r=\operatorname{rad}(p-1).
\]

Indeed, from \(D\) define \(r\) as the unique squarefree positive integer whose prime divisors are exactly the \(D\)-predecessors of \(p\). Conversely,

\[
D(q,p)
\iff
\operatorname{Prime}(q)
\land
\exists r\,
(R_{\mathbb P}(r,p)\land q\mid r).
\]

Thus the unresolved directed-support problem can be rewritten as:

\[
\boxed{
\operatorname{Aut}
(\mathbb N_{>0},\times,R_{\mathbb P})
=1\ ?
}
\]

where

\[
R_{\mathbb P}(r,p)
\iff
r=\operatorname{rad}(p-1).
\]

This is a much cleaner formulation of the frontier.

---

# 7. Exact predecessor versus radical predecessor

The minimality problem now has a canonical form:

\[
\boxed{
\begin{array}{ccc}
S_{\mathbb P}(n,p): n=p-1
&\Longrightarrow&
\text{rigid},\\[4pt]
\downarrow\text{ erase multiplicities}&&\\[-2pt]
R_{\mathbb P}(r,p): r=\operatorname{rad}(p-1)
&\Longrightarrow&
\text{rigidity unresolved.}
\end{array}
}
\]

The query-ladder gap theorem explains exactly what is lost locally when one tries to reconstruct the exact predecessor from threshold information. But at the full relational level the positive mechanism is simply the exact prime predecessor.

This distinction is essential for the final article:

- **threshold minimality** concerns one particular query architecture;
- **relational minimality** asks how much of \(p-1\) can be erased while preserving global rigidity.

These are not the same problem.

---

# 8. Relation to classical successor results

The full successor relation

\[
S(n,m)\iff m=n+1
\]

added to multiplication is classically much stronger: Julia Robinson's definability identities recover addition, so full arithmetic becomes definable.

Our relation

\[
S_{\mathbb P}(n,p)
\]

is only the graph of successor **when the output is prime**.

The current work proves rigidity of this restricted expansion, but does **not** prove:

- definability of full successor;
- definability of addition;
- undecidability of the complete theory;
- interdefinability with full arithmetic.

Those stronger claims must not be inferred merely from rigidity.

---

# 9. New central formulation for HATTER-SOL-03

The article can now state its positive result without any implementation metaphor:

\[
\boxed{
\text{exact prime predecessor}
+
\text{multiplication}
\Longrightarrow
\text{rigidity}.
}
\]

The self-questioning interpretation then explains *how* exact predecessor information can be presented through a single reusable binary probe:

\[
q,\ q^2,\ q^3,\ldots
\]

until the first failure.

So the literary phrase

> "teach the cup to ask the questions itself"

has two mathematically equivalent readings:

1. the cup knows the exact predecessor \(p-1\) of each prime;
2. the cup can recover that predecessor by repeatedly asking prime-power divisibility questions.

The first is the cleaner structural statement. The second is the cleaner information-flow statement.
