# HATTER-SOL-03 · Coarse Depth vs Adaptive Probes

## 0. Question

The previous strike isolated the directed support graph

\[
D(q,p)\iff q\mid p-1
\]

as the first unresolved layer between pure support and exact exponent depth.

A natural next attempt is to retain only one extra bit on every support edge, for example

\[
B(q,p)\iff q^2\mid p-1.
\]

Does this already restore the self-generated rigidity mechanism?

The answer splits into two different information architectures:

1. **static local labels:** a fixed finite number of bits is stored once on each edge;
2. **adaptive binary queries:** the structure can generate new candidate powers internally and ask the same yes/no question repeatedly.

These regimes behave very differently.

---

# 1. One static threshold bit does not restore predecessor extensionality

Consider the two relations

\[
D(q,p)\iff q\mid p-1
\]

and

\[
B(q,p)\iff q^2\mid p-1.
\]

The incoming \((D,B)\)-profile of a prime records, for each prime divisor \(q\mid p-1\), only whether

\[
v_q(p-1)=1
\quad\text{or}\quad
v_q(p-1)\ge2.
\]

Already

\[
5-1=2^2,
\qquad
17-1=2^4,
\]

so

\[
\operatorname{Pred}(5)=\operatorname{Pred}(17)=\{2\}
\]

and in both cases the unique incoming edge satisfies \(B(2,p)\).

Thus the static one-bit predecessor code is not injective.

The same collision persists for

\[
257-1=2^8,
\qquad
65537-1=2^{16}.
\]

Hence:

\[
\boxed{
\text{support + the single threshold }v_q\ge2
\text{ is not predecessor-extensional.}
}
\]

This does **not** prove that the full directed graph with this one-bit label has a nontrivial automorphism; future descendants may still distinguish the collided vertices. It proves that the clean well-founded induction used in the exact-depth theorem no longer works.

---

# 2. Arbitrary finite local edge labels

The same obstruction is not special to the threshold \(v_q\ge2\).

Let \(C\) be a finite alphabet. For every prime \(q\), let

\[
c_q:\mathbb N_{\ge1}\to C
\]

be an arbitrary local encoding of the exponent on an edge from \(q\).

For a prime \(p\), define the colored incoming code

\[
\operatorname{Code}_c(p)
=
\{(q,c_q(v_q(p-1))):q\mid p-1\}.
\]

Call the encoding **incoming-extensional** if

\[
\operatorname{Code}_c(p)=\operatorname{Code}_c(r)
\Longrightarrow
p=r.
\]

If \(|C|\le2^b\), think of this as at most \(b\) static bits per incoming edge.

---

# 3. Unconditional two-bit barrier from the five known Fermat primes

The five classical known Fermat primes are

\[
3=2^1+1,
\quad
5=2^2+1,
\quad
17=2^4+1,
\quad
257=2^8+1,
\quad
65537=2^{16}+1.
\]

All five have the same predecessor support \(\{2\}\).

Therefore an incoming code with an alphabet of size at most four can assign at most four different colored codes to these five vertices.

## Theorem 3.1

For every local exponent encoding with

\[
|C|\le4,
\]

the colored predecessor code is not incoming-extensional.

Equivalently, **no static local encoding with at most two bits per edge can make the predecessor code extensional.**

### Proof

For all five known Fermat primes the support is the singleton \(\{2\}\), so their code is determined by the single color

\[
c_2(e),
\qquad
e\in\{1,2,4,8,16\}.
\]

Five exponent values are mapped to at most four colors. Two receive the same color by the pigeonhole principle. \(\square\)

---

# 4. A deterministic three-bit barrier from \(2^a3^b+1\)

The same idea can be pushed one step further without relying on any unproved infinitude statement.

Consider primes of the form

\[
p=2^a3^b+1,
\qquad a,b\ge1.
\]

Every such prime has exact predecessor support

\[
\operatorname{Pred}(p)=\{2,3\}.
\]

A deterministic exhaustive check below \(10^{12}\) finds **77** such primes.

The accompanying verifier

`verify_coarse_depth_barrier.py`

uses only trial division by all primes up to \(10^6\); therefore every asserted primality below \(10^{12}\) is certified deterministically, not by a probable-prime test.

If \(|C|\le8\), a support-\(\{2,3\}\) vertex has at most

\[
|C|^2\le64
\]

possible colored incoming codes:

\[
(c_2(a),c_3(b)).
\]

Since there are 77 certified prime vertices of this form, two must collide.

## Theorem 4.1 — three-bit static local barrier

For every family of local exponent encodings

\[
c_q:\mathbb N_{\ge1}\to C
\]

with

\[
|C|\le8,
\]

the colored predecessor code is not incoming-extensional.

Equivalently:

\[
\boxed{
\text{three static bits per support edge are still insufficient}
\text{ for universal predecessor extensionality.}
}
\]

### Proof

Among the 77 certified primes \(2^a3^b+1<10^{12}\), every incoming support is exactly \(\{2,3\}\). Their codes lie in \(C^2\), which has at most \(64\) elements. Pigeonhole. \(\square\)

### Scope

This theorem concerns **local static exponent encodings**. It does not claim that every finite-language expansion with three bits is non-rigid; a more global relation may carry information not reducible to independent local edge colors.

---

# 5. Conditional unbounded barrier from Fermat primes

The same argument reveals why a universal finite-bit minimality theorem touches open arithmetic.

If there are infinitely many Fermat primes

\[
2^{2^n}+1,
\]

then there are infinitely many prime vertices whose predecessor support is exactly \(\{2\}\).

Hence any finite alphabet \(C\) would identify at least two of them at the incoming-code level.

Thus:

## Proposition 5.1

If infinitely many Fermat primes exist, then **no finite number of static local bits per edge can make the predecessor code incoming-extensional.**

This is conditional because infinitude of Fermat primes is unknown.

So the exact global finite-bit threshold cannot be settled by a naive counting argument without touching unresolved prime-distribution questions.

---

# 6. Adaptive binary probing

Static storage is not the only way a finite relation can carry depth.

Let \(J(a,p)\) be the binary relation

\[
J(a,p)
\iff
\begin{cases}
p\text{ is prime},\\
a=q^k\text{ for some prime }q\text{ and }k\ge1,\\
a\mid p-1.
\end{cases}
\]

Each evaluation of \(J\) is only a yes/no answer.

But the multiplicative carrier can generate the candidate questions

\[
q,\ q^2,\ q^3,\ldots
\]

internally.

For a fixed support edge \(q\to p\), the structure can ask

\[
J(q,p)?
\]

then

\[
J(q^2,p)?
\]

then

\[
J(q^3,p)?
\]

and so on, until the first failure.

The final successful exponent is exactly

\[
v_q(p-1).
\]

So the answer alphabet remains binary, but the number of internally generated queries is adaptive and unbounded.

---

# 7. Interdefinability with the exact-depth relation

Recall the exact-maximal-power relation

\[
H(a,p)
\iff
\begin{cases}
p\text{ prime},\\
a=q^e\text{ for some prime }q,\\
q^e\parallel p-1.
\end{cases}
\]

used in the exact-depth rigidity theorem.

## Theorem 7.1 — adaptive-threshold equivalence

Over the multiplicative monoid \((\mathbb N_{>0},\times)\), the relations \(J\) and \(H\) are first-order interdefinable.

### Proof

A nontrivial prime power is multiplicatively definable as an element having exactly one prime divisor.

From \(H\) to \(J\):

\[
J(a,p)
\iff
\exists b\,
\bigl(H(b,p)\land a\mid b\bigr),
\]

with \(a\) restricted to nontrivial prime powers. Indeed, \(H\) supplies the unique maximal \(q\)-power dividing \(p-1\), and every lower \(q\)-power divides it.

From \(J\) to \(H\):

\[
H(a,p)
\iff
J(a,p)
\land
\neg\exists b\,
\bigl(J(b,p)\land a\mid b\land a\ne b\bigr).
\]

Among the prime powers with fixed base \(q\), this selects the unique maximal divisor of \(p-1\). Since divisibility is definable from multiplication by

\[
a\mid b\iff\exists c\;(ac=b),
\]

the definitions use no extra arithmetic operation. \(\square\)

## Corollary 7.2 — adaptive one-bit rigidity

Let

\[
\mathcal J
=(\mathbb N_{>0},\times,J).
\]

Then

\[
\boxed{
\operatorname{Aut}(\mathcal J)=\{\mathrm{id}\}.
}
\]

### Proof

By Theorem 7.1, \(H\) is definable in \(\mathcal J\). The exact-depth structure \((\mathbb N_{>0},\times,H)\) is rigid, so every automorphism of \(\mathcal J\) is the identity. \(\square\)

---

# 8. Static bits versus a reusable binary question

The distinction can now be stated precisely.

A static local label gives, once and for all,

\[
c_q(v_q(p-1))\in C.
\]

With a finite alphabet, different exponents may collapse permanently.

The adaptive relation \(J\), by contrast, uses only the binary alphabet

\[
\{0,1\}
\]

but can be applied repeatedly to a sequence of multiplicatively generated candidates.

Thus:

\[
\boxed{
\text{one bit stored once}
\not\Rightarrow
\text{predecessor extensionality},
}
\]

while

\[
\boxed{
\text{one reusable binary query}
+
\text{self-generated powers}
\Longrightarrow
\text{exact depth}
\Longrightarrow
\text{rigidity}.
}
\]

This is the sharpest form so far of the phrase **"teach the cup to ask questions itself."**

The cup does not need a large answer alphabet. It needs the ability to generate the next question from the previous one.

---

# 9. A recursive-query law

HATTER-SOL-02 established

\[
\text{individuality}=\text{sufficient separation}.
\]

The present strike adds a computational/structural refinement:

\[
\boxed{
\text{self-generated individuality}
=
\text{a finite query rule}
+
\text{internal generation of new queries}
+
\text{well-founded termination}.}
\]

For \(J\), the query chain for a fixed \((q,p)\) is

\[
q,q^2,\ldots,q^{v_q(p-1)},q^{v_q(p-1)+1},
\]

and the first `no` ends the search.

The mechanism is finite in language, binary in each answer, but unbounded in adaptive depth.

---

# 10. Publication significance

The current HATTER-SOL-03 theorem spine is now stronger than a simple rigidity statement:

\[
\boxed{
\begin{array}{c}
\text{pure multiplication + finite seeds: impossible}\\
\downarrow\\
\text{anonymous/unanchored probes: symmetry may return}\\
\downarrow\\
\text{directed support only: exact global status unresolved}\\
\downarrow\\
\text{static coarse depth: local extensionality fails}\\
\downarrow\\
\text{adaptive binary prime-power queries: exact depth recovered}\\
\downarrow\\
\text{self-generated rigidity.}
\end{array}
}
\]

The key new contrast is **static information versus interactive information** inside a fixed finite relational language.

---

# 11. Next strike

The next minimality question is now sharper than "how many bits?":

\[
\boxed{
\text{How weak can the internally generated query family be and still recover exact depth?}
}
\]

Candidate weakenings:

1. allow only the squaring chain
   \[
   q,q^2,q^4,q^8,\ldots;
   \]
   this locates the exponent only to dyadic intervals;
2. add one parity-type query and ask whether dyadic search + one extra bit recovers \(v_q(p-1)\);
3. restrict queries to a fixed sparse multiplicative ladder and determine the exact resolution law;
4. seek a single relation whose allowed queries are generated by one unary operation rather than arbitrary multiplication.

The likely minimality invariant is no longer a raw number of bits. It is the **growth/resolution capacity of the self-generated query ladder**.
