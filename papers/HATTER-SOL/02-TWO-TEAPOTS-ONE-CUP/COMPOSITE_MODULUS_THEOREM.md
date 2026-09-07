# HATTER-SOL-02 · Composite-Modulus Classification

## 0. Setup

For an integer \(m\ge2\), define

\[
E_m(x,y)\iff x\equiv y\pmod m
\]

and

\[
\mathcal M_m=(\mathbb N_{>0},\times,E_m).
\]

Write the prime-power factorization

\[
m=\prod_{i=1}^k p_i^{a_i}.
\]

Let

\[
U_m=(\mathbb Z/m\mathbb Z)^\times.
\]

For every reduced residue \(r\in U_m\), put

\[
C_r=\{q\in\mathbb P:q\nmid m,\ q\equiv r\pmod m\}.
\]

By Dirichlet's theorem, every \(C_r\) is countably infinite.

The purpose of this note is to classify \(\operatorname{Aut}(\mathcal M_m)\), identify exactly which primes become individually fixed, and compute the number of prime-individuality orbits.

---

# 1. The finite quotient induced by \(E_m\)

Because \(E_m\) is a multiplicative congruence, every automorphism

\[
g\in\operatorname{Aut}(\mathcal M_m)
\]

induces an automorphism

\[
\bar g\in\operatorname{Aut}(\mathbb Z/m\mathbb Z,\cdot)
\]

of the finite multiplicative monoid of residue classes.

Primes are exactly the multiplicative atoms of \((\mathbb N_{>0},\times)\), hence \(g\) permutes \(\mathbb P\).

## Lemma 1.1 — every prime divisor of \(m\) is fixed individually

If \(p\mid m\) is prime, then every automorphism of \(\mathcal M_m\) fixes \(p\).

### Proof

The residue class \([p]_m\) is a nonunit in the finite quotient. Therefore \(g(p)\) must also be a prime divisor of \(m\).

For any residue \(a\pmod m\), the principal ideal

\[
[a]_m(\mathbb Z/m\mathbb Z)
\]

has cardinality

\[
\frac{m}{\gcd(a,m)}.
\]

Hence for a prime divisor \(p\mid m\),

\[
\bigl|[p]_m(\mathbb Z/m\mathbb Z)\bigr|=\frac mp.
\]

A monoid automorphism preserves the cardinality of principal ideals. If \(g(p)=q\) for another prime divisor \(q\mid m\), then

\[
\frac mp=\frac mq,
\]

so \(p=q\). \(\square\)

Thus

\[
\operatorname{supp}(m):=\{p\in\mathbb P:p\mid m\}
\]

is pointwise fixed.

---

# 2. Local congruence filtration on the unit group

For a prime power \(p^a\), define

\[
U_{p^a}=(\mathbb Z/p^a\mathbb Z)^\times
\]

and the congruence subgroups

\[
K_{p,k}
:=
\{u\in U_{p^a}:u\equiv1\pmod{p^k}\},
\qquad 1\le k\le a.
\]

Let

\[
H_{p^a}
:=
\{\alpha\in\operatorname{Aut}(U_{p^a}):
\alpha(K_{p,k})=K_{p,k}\text{ for all }k\}.
\]

These are exactly the unit-group automorphisms compatible with multiplication by powers of \(p\) in the monoid \(\mathbb Z/p^a\mathbb Z\).

## Lemma 2.1 — compatibility criterion

A group automorphism

\[
\alpha\in\operatorname{Aut}(U_{p^a})
\]

extends, while fixing the residue class of \(p\), to an automorphism of the multiplicative monoid \((\mathbb Z/p^a\mathbb Z,\cdot)\) if and only if \(\alpha\in H_{p^a}\).

### Proof

Every nonzero residue can be written as

\[
p^e u,
\qquad 0\le e<a,
\]

with \(u\in U_{p^a}\). The unit \(u\) is determined modulo \(p^{a-e}\):

\[
p^eu\equiv p^ev\pmod{p^a}
\iff
u v^{-1}\in K_{p,a-e}.
\]

Therefore the formula

\[
p^eu\mapsto p^e\alpha(u)
\]

is well-defined exactly when every \(K_{p,k}\) is preserved. The zero class is fixed automatically. \(\square\)

---

# 3. CRT decomposition and the global quotient group

By the Chinese remainder theorem,

\[
\mathbb Z/m\mathbb Z
\cong
\prod_{i=1}^k\mathbb Z/p_i^{a_i}\mathbb Z
\]

as multiplicative monoids, and

\[
U_m\cong\prod_{i=1}^kU_{p_i^{a_i}}.
\]

The crucial point is that the local unit factors cannot mix under an automorphism induced from \(\mathcal M_m\).

## Lemma 3.1 — local factors are preserved

Every automorphism of \(\mathcal M_m\) induces on \(U_m\) an automorphism belonging to

\[
H_m:=\prod_{i=1}^kH_{p_i^{a_i}}.
\]

### Proof

Each prime divisor \(p_i\) is fixed by Lemma 1.1. Consider the stabilizer in \(U_m\) of the residue class \([p_i^{a_i}]_m\):

\[
S_i
=
\{u\in U_m:
up_i^{a_i}\equiv p_i^{a_i}\pmod m\}.
\]

Under the CRT decomposition, this subgroup is exactly

\[
U_{p_i^{a_i}}\times\prod_{j\ne i}\{1\}.
\]

Because \([p_i^{a_i}]_m\) is fixed, its unit stabilizer is preserved, so each CRT unit factor is preserved separately.

More generally, the stabilizer of \([p_i^{a_i-k}]_m\) inside \(S_i\) is exactly the embedded subgroup \(K_{p_i,k}\). Since these powers of \(p_i\) are fixed, every \(K_{p_i,k}\) is preserved. Hence the induced unit action lies in \(H_m\). \(\square\)

---

# 4. Exact automorphism group for arbitrary \(m\)

## Theorem 4.1 — composite-modulus automorphism theorem

There is a split exact sequence

\[
1\longrightarrow
\prod_{r\in U_m}\operatorname{Sym}(C_r)
\longrightarrow
\operatorname{Aut}(\mathcal M_m)
\overset{\rho_m}{\longrightarrow}
H_m
\longrightarrow1.
\]

Consequently, noncanonically,

\[
\boxed{
\operatorname{Aut}(\mathcal M_m)
\cong
\left(\prod_{r\in U_m}\operatorname{Sym}(C_r)\right)
\rtimes H_m.
}
\]

### Proof

Every automorphism fixes each prime divisor of \(m\) and induces an element of \(H_m\) on \(U_m\), giving the homomorphism \(\rho_m\).

If \(g\in\ker\rho_m\), then every reduced prime residue class \(C_r\) is preserved setwise. Conversely, arbitrary independent permutations of the infinite sets \(C_r\), with every prime divisor of \(m\) fixed, extend uniquely by prime factorization to a multiplicative automorphism. Since the residue class of every prime factor is unchanged, \(E_m\) is preserved. Thus

\[
\ker\rho_m
\cong
\prod_{r\in U_m}\operatorname{Sym}(C_r).
\]

For surjectivity, take

\[
\alpha=(\alpha_i)_i\in H_m.
\]

It acts on the reduced residues \(U_m\). Since every \(C_r\) is countably infinite, choose bijections

\[
C_r\to C_{\alpha(r)}
\]

for all \(r\in U_m\), fix each prime divisor of \(m\), and extend the resulting prime permutation multiplicatively.

At every local factor \(p_i^{a_i}\), the valuation of an integer is unchanged, while its unit component is transformed by \(\alpha_i\). Lemma 2.1 guarantees that congruence modulo \(p_i^{a_i}\) is preserved. CRT then gives preservation of congruence modulo \(m\).

Finally, fixed enumerations of all \(C_r\) produce a coherent lift of \(H_m\), so the exact sequence splits noncanonically. \(\square\)

---

# 5. Local classification for odd prime powers

Assume \(p\) is odd. Then

\[
U_{p^a}
\]

is cyclic of order

\[
\varphi(p^a)=p^{a-1}(p-1).
\]

Every subgroup of a finite cyclic group is characteristic. Hence every congruence subgroup \(K_{p,k}\) is characteristic and therefore

\[
\boxed{
H_{p^a}=\operatorname{Aut}(U_{p^a}).
}
\]

Automorphisms of a finite cyclic group are transitive on elements of a given order. Therefore the \(H_{p^a}\)-orbits on \(U_{p^a}\) are indexed exactly by divisors of \(\varphi(p^a)\).

Since

\[
\tau(\varphi(p^a))
=
\tau(p^{a-1})\tau(p-1)
=
a\tau(p-1),
\]

we obtain:

## Theorem 5.1 — odd local orbit count

For odd prime \(p\), the number of local unit orbits is

\[
\boxed{
h(p^a)=a\tau(p-1).
}
\]

Two reduced residues \(u,v\pmod{p^a}\) are in the same local orbit exactly when

\[
\operatorname{ord}_{p^a}(u)
=
\operatorname{ord}_{p^a}(v).
\]

---

# 6. The 2-adic local factor

The prime \(2\) is exceptional because \(U_{2^a}\) stops being cyclic for \(a\ge3\).

For \(a\ge3\),

\[
U_{2^a}
\cong
C_2\times C_{2^{a-2}},
\]

with a standard decomposition

\[
u=(-1)^\varepsilon5^t.
\]

The subgroup

\[
K_{2,2}=\langle5\rangle
\]

is the cyclic index-two subgroup of units congruent to \(1\pmod4\). Preserving the full congruence filtration is equivalent to preserving \(K_{2,2}\), because all deeper \(K_{2,k}\) are the unique subgroups of the relevant orders inside \(K_{2,2}\).

## Theorem 6.1 — 2-adic compatible unit automorphisms

For \(a\ge3\), every element of \(H_{2^a}\) has the form

\[
5\mapsto5^c,
\qquad c\text{ odd},
\]

and

\[
-1\mapsto(-1)5^{\delta2^{a-3}},
\qquad \delta\in\{0,1\}.
\]

Hence

\[
H_{2^a}
\cong
(\mathbb Z/2^{a-2}\mathbb Z)^\times\times C_2
\]

for \(a\ge3\).

For \(a=1\), \(U_2\) is trivial. For \(a=2\), \(U_4\cong C_2\) and its automorphism group is trivial.

## Theorem 6.2 — 2-adic local orbit count

Let \(h(2^a)\) be the number of \(H_{2^a}\)-orbits on \(U_{2^a}\). Then

\[
\boxed{
 h(2^a)=
 \begin{cases}
 1,&a=1,\\
 2,&a=2,\\
 2a-3,&a\ge3.
 \end{cases}
}
\]

### Proof sketch

For \(a\ge3\), write \(N=2^{a-2}\) and \(u=(-1)^\varepsilon5^t\).

Inside \(K_{2,2}=\langle5\rangle\), the action is

\[
t\mapsto ct
\]

with \(c\) odd. Orbits are classified by the order of \(5^t\), giving \(a-1\) orbits.

Outside \(K_{2,2}\), the exponent transforms by

\[
t\mapsto ct+\delta N/2.
\]

This gives one orbit for each valuation stratum

\[
v_2(t)=0,1,\ldots,a-4,
\]

plus one final orbit containing both \(t=0\) and \(t=N/2\). Thus there are \(a-2\) outside orbits.

Total:

\[
(a-1)+(a-2)=2a-3.
\]

---

# 7. Exact prime-orbit count for arbitrary \(m\)

Define the local orbit factor

\[
h(p^a)=
\begin{cases}
a\tau(p-1),&p\text{ odd},\\
1,&p=2,\ a=1,\\
2,&p=2,\ a=2,\\
2a-3,&p=2,\ a\ge3.
\end{cases}
\]

Let

\[
\omega(m)=\#\{p:p\mid m\}
\]

be the number of distinct prime divisors.

## Theorem 7.1 — composite-modulus prime orbit formula

The number of prime-individuality orbits of \(\mathcal M_m\) is exactly

\[
\boxed{
\mathfrak O(m)
=
\omega(m)
+
\prod_{p^a\parallel m}h(p^a).
}
\]

The first \(\omega(m)\) orbits are the singleton prime divisors of \(m\). Every other orbit is infinite.

### Proof

The prime divisors of \(m\) are fixed individually by Lemma 1.1.

Every prime \(q\nmid m\) belongs to one reduced residue cell \(C_r\). The kernel in Theorem 4.1 is transitive inside each \(C_r\), while the quotient \(H_m\) moves residue classes according to the direct product of the local actions. Therefore outside prime orbits are in bijection with \(H_m\)-orbits on \(U_m\).

Because both the unit group and the quotient action decompose as direct products over prime powers, the number of global unit orbits is the product of the local orbit counts \(h(p^a)\). Every such orbit contains at least one reduced residue class, and every reduced residue class contains infinitely many primes by Dirichlet. \(\square\)

---

# 8. Support versus depth

The arbitrary-modulus theorem reveals two distinct information channels inside a single congruence relation \(E_m\).

## Theorem 8.1 — support controls fixed primes

\[
\boxed{
\operatorname{Fix}_{\mathbb P}
(\operatorname{Aut}(\mathcal M_m))
=
\{p\in\mathbb P:p\mid m\}.
}
\]

### Proof

Every prime divisor is fixed by Lemma 1.1. If \(q\nmid m\), then \(q\in C_r\) for some reduced residue \(r\), and \(C_r\) is infinite. A transposition of \(q\) with another prime in \(C_r\) lies in the kernel of \(\rho_m\), so \(q\) is not fixed by all automorphisms. \(\square\)

Thus replacing \(p\) by \(p^a\) does **not** create a new individually fixed prime. It only increases resolution among the outside primes.

This motivates the terminology:

- **support information:** the radical
  \[
  \operatorname{rad}(m)=\prod_{p\mid m}p,
  \]
  which determines which prime atoms are fixed;
- **depth information:** the exponents \(a=v_p(m)\), which refine the orbit structure of the remaining primes.

For odd \(p\), increasing the depth from \(p^a\) to \(p^{a+1}\) changes the local unit-orbit count from

\[
a\tau(p-1)
\]

to

\[
(a+1)\tau(p-1),
\]

without fixing any new prime.

---

# 9. Squarefree moduli recover the finite-family theorem

If \(m\) is squarefree,

\[
m=\prod_{p\in F}p,
\]

then

\[
h(p)=\tau(p-1)
\]

for odd \(p\), while \(h(2)=1=\tau(1)\). Therefore

\[
\boxed{
\mathfrak O(m)
=|F|+
\prod_{p\in F}\tau(p-1),
}
\]

exactly reproducing the finite-family formula from the separately named relations \((E_p)_{p\in F}\) at the level of prime automorphism orbits.

This is important conceptually: **one composite congruence relation can carry the same prime-orbit fragmentation as many prime-modulus layers.**

---

# 10. Exact modular cost of fixing prescribed primes

Let \(S\subset\mathbb P\) be finite.

## Corollary 10.1

A single congruence relation \(E_m\) fixes every prime in \(S\) if and only if

\[
\prod_{p\in S}p\mid m.
\]

Hence the smallest possible modulus that fixes every prime of \(S\) is

\[
\boxed{
m_{\min}(S)=\prod_{p\in S}p.}
\]

If only the number \(|S|=k\) matters, the smallest modulus capable of fixing \(k\) distinct primes is the primorial

\[
\boxed{p_k\#=2\cdot3\cdot5\cdots p_k.}
\]

Thus symbol-count alone is a bad measure of additive information: **one relation symbol \(E_m\) can individually fix arbitrarily many primes, because the modulus itself carries unbounded payload.**

A meaningful information-cost invariant must therefore charge the complexity of \(m\), for example through \(\log m\), not merely count relation symbols.

---

# 11. Examples

## \(m=4\)

\[
\omega(4)=1,
\qquad h(4)=2,
\]

so

\[
\mathfrak O(4)=3.
\]

The prime \(2\) is fixed; odd primes split into the two residue types \(1\) and \(3\pmod4\).

## \(m=8\)

\[
\omega(8)=1,
\qquad h(8)=3,
\]

so

\[
\mathfrak O(8)=4.
\]

The prime \(2\) is fixed; the outside primes occupy three infinite symmetry types.

## \(m=9\)

\[
\omega(9)=1,
\qquad h(9)=2\tau(2)=4,
\]

so

\[
\mathfrak O(9)=5.
\]

The prime \(3\) is fixed; the remaining prime orbits are classified by multiplicative order modulo \(9\), whose possible values are the four divisors of \(6\).

## \(m=15\)

\[
\omega(15)=2,
\qquad h(3)h(5)=2\cdot3=6,
\]

hence

\[
\mathfrak O(15)=8.
\]

The primes \(3\) and \(5\) are individually fixed; all other primes split into six infinite orbit types.

## \(m=12=2^2\cdot3\)

\[
\omega(12)=2,
\qquad h(4)h(3)=2\cdot2=4,
\]

so

\[
\mathfrak O(12)=6.
\]

---

# 12. Conceptual consequence for HATTER-SOL-02

The composite-modulus analysis sharpens the series metaphor into a two-axis law.

A congruence layer has:

1. **support** — which prime atoms are explicitly captured by the modulus;
2. **depth** — how finely the remaining unit-prime world is resolved.

The support controls pointwise individuality:

\[
\operatorname{Fix}_{\mathbb P}=\operatorname{supp}(m),
\]

while depth controls residual fragmentation through

\[
\mathfrak O(m)-\omega(m)
=
\prod_{p^a\parallel m}h(p^a).
\]

So one can now distinguish two ways of “pouring more additive structure into the cup”:

- add a **new prime factor** to the modulus: a new prime becomes individually fixed;
- increase an **existing prime exponent**: no new prime is fixed, but the unresolved outside world is split more finely.

This is a stronger and cleaner framework than merely counting how many congruence predicates have been added.

---

# 13. Literature guard

A targeted search found standard material on congruences, CRT, free commutative monoids, Skolem arithmetic, and multiplicative monoids modulo \(n\), but no direct match for the exact lifted automorphism-group classification of

\[
(\mathbb N_{>0},\times,E_m)
\]

with prime-individuality orbit counts and the support/depth interpretation.

This remains a preliminary negative search result, **not yet a novelty claim**. Before publication, the literature audit should explicitly include:

- automorphisms of the multiplicative semigroup \(\mathbb Z/n\mathbb Z\);
- congruence expansions of Skolem arithmetic;
- coloured/free commutative monoids and kernel-preserving automorphisms;
- automorphism groups of finite commutative monoids and monogenic local factors.

---

# 14. Next strike

The next mathematically sharp target is no longer composite \(m\); that classification is now essentially complete.

The strongest open continuation is:

\[
\boxed{
\text{How weak can the additive probe be and still force sparse rigidity?}
}
\]

In particular, replace the full equivalence relation \(E_p\) by only a unary quadratic-character bit on primes / units, and determine whether an arbitrarily sparse family of such one-bit probes still makes the multiplicative world rigid.

If yes, the series obtains an actual **information-compression theorem for arithmetic individuality**: full congruence classes are unnecessary; one binary character per selected modulus may suffice.
