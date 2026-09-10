# HATTER-SOL-05 · Cyclotomic Dimension and Local Sieve Asymmetry

## 0. Purpose

The first HATTER-SOL-05 strike ruled out finite covering-congruence proofs of an empty exact-support fiber. The next question is whether the candidate family itself contains an algebraic collapse strong enough to make one support fundamentally thinner than another.

There is such a collapse, but only in one dimension.

For

\[
N_S(\mathbf e)=1+\prod_{q\in S}q^{e_q},
\qquad e_q\ge1,
\]

primality forces the common odd part of all exponents to disappear. For a singleton support this leaves only powers of two and recovers the classical Fermat sparsity. For two or more support primes, however, a positive-density set of exponent vectors survives.

This gives a sharp dimension jump between the Fermat layer and every higher exact-support family.

The same analysis also reveals a rigorous local-sieve asymmetry between the first two competing supports

\[
\{2,3\}
\quad\text{and}\quad
\{2,5\}.
\]

The asymmetry is real but, by itself, does not kill the transposition \((3\ 5)\), because the automorphism tower sees only the cardinality of each exact fiber, not the density of its parameterization.

---

# 1. Common-exponent factorization

Let

\[
S=\{q_1,\ldots,q_k\}
\]

be a finite set of primes containing \(2\), and let

\[
\mathbf e=(e_1,\ldots,e_k)\in\mathbb N_{>0}^k.
\]

Define

\[
N_S(\mathbf e)
=
1+q_1^{e_1}\cdots q_k^{e_k}.
\]

## Theorem 1.1 — cyclotomic common-divisor obstruction

If \(N_S(\mathbf e)\) is prime, then

\[
\boxed{
\gcd(e_1,\ldots,e_k)
\text{ is a power of }2.
}
\]

### Proof

Suppose that the gcd has an odd divisor \(d>1\). Then

\[
e_i=d f_i
\qquad(1\le i\le k)
\]

for positive integers \(f_i\). Put

\[
A=q_1^{f_1}\cdots q_k^{f_k}>1.
\]

Then

\[
N_S(\mathbf e)=A^d+1.
\]

Since \(d\) is odd,

\[
A^d+1
=(A+1)
(A^{d-1}-A^{d-2}+\cdots-A+1),
\]

with both factors greater than one. Hence \(N_S(\mathbf e)\) is composite. Contradiction. \(\square\)

### Remark

The theorem gives only a necessary condition. A vector whose gcd is a power of two may still yield a composite value.

---

# 2. Why the Fermat layer is qualitatively different

For the singleton support

\[
S=\{2\},
\]

the theorem says that a prime candidate

\[
2^a+1
\]

must satisfy

\[
\boxed{a=2^m.}
\]

Thus the original one-dimensional exponent line collapses to the powers of two. This is exactly the classical Fermat-number phenomenon.

If exponents are bounded by \(B\), the number of cyclotomically admissible singleton exponents is only

\[
\lfloor\log_2 B\rfloor+1
=
O(\log B).
\]

So their density inside \(\{1,\ldots,B\}\) is zero.

This explains structurally why the first fiber

\[
X_{\{2\}}
\]

is exceptionally sparse before any deeper primality question is asked.

---

# 3. Positive-density survival in dimension at least two

For \(k\ge2\), define

\[
\mathcal C_k(B)
=
\left\{
(e_1,\ldots,e_k)\in[1,B]^k:
\gcd(e_1,\ldots,e_k)
\text{ is a power of }2
\right\}.
\]

Equivalently, no odd prime divides all coordinates.

## Theorem 3.1 — cyclotomic dimension theorem

For every \(k\ge2\),

\[
\boxed{
\frac{|\mathcal C_k(B)|}{B^k}
\longrightarrow
\prod_{\ell\text{ odd prime}}
\left(1-\frac1{\ell^k}\right)
=
\frac1{\zeta(k)(1-2^{-k})}.
}
\]

In particular, for \(k=2\),

\[
\boxed{
\frac{|\mathcal C_2(B)|}{B^2}
\longrightarrow
\frac8{\pi^2}.
}
\]

### Proof

The indicator that no odd prime divides the gcd is

\[
\sum_{\substack{d\mid\gcd(e_1,\ldots,e_k)\\ d\text{ odd}}}
\mu(d).
\]

Therefore

\[
|\mathcal C_k(B)|
=
\sum_{\substack{d\le B\\ d\text{ odd}}}
\mu(d)
\left\lfloor\frac Bd\right\rfloor^k.
\]

For \(k\ge2\), division by \(B^k\) and dominated convergence give

\[
\lim_{B\to\infty}
\frac{|\mathcal C_k(B)|}{B^k}
=
\sum_{d\text{ odd}}\frac{\mu(d)}{d^k}
=
\prod_{\ell\text{ odd prime}}
\left(1-\ell^{-k}\right).
\]

Using

\[
\zeta(k)^{-1}
=
(1-2^{-k})
\prod_{\ell\text{ odd prime}}
(1-\ell^{-k}),
\]

gives the stated formula. For \(k=2\),

\[
\frac1{\zeta(2)(1-2^{-2})}
=
\frac1{(\pi^2/6)(3/4)}
=
\frac8{\pi^2}.
\]

\(\square\)

---

# 4. The dimension jump

Combining Sections 2 and 3 gives:

## Corollary 4.1 — one support prime versus two or more

The universal algebraic factorization obstruction behaves in two radically different ways.

For one support prime:

\[
\boxed{
\text{cyclotomically admissible exponent density}=0.
}
\]

For every fixed \(k\ge2\):

\[
\boxed{
\text{cyclotomically admissible exponent density}
=
\frac1{\zeta(k)(1-2^{-k})}>0.
}
\]

Thus the transition

\[
|S|=1
\longrightarrow
|S|=2
\]

is a genuine arithmetic phase change in the candidate parameter space.

For HATTER-SOL-05 this matters because the first unresolved comparison

\[
X_{\{2,3\}}
\quad\text{vs.}\quad
X_{\{2,5\}}
\]

lives on the positive-density side of this boundary, unlike the Fermat fiber \(X_{\{2\}}\).

---

# 5. The first local sieve for \(\{2,5\}\)

Consider

\[
N_{2,5}(a,b)=1+2^a5^b,
\qquad a,b\ge1.
\]

Modulo \(3\),

\[
2\equiv-1,
\qquad
5\equiv-1.
\]

Hence

\[
N_{2,5}(a,b)
\equiv
1+(-1)^{a+b}\pmod3.
\]

If \(a+b\) is odd, then

\[
N_{2,5}(a,b)\equiv0\pmod3.
\]

Since \(N_{2,5}(a,b)>3\), the number is composite.

Therefore every prime value satisfies

\[
\boxed{a+b\equiv0\pmod2.}
\]

Among all positive exponent pairs this removes asymptotically one half.

Because the condition "gcd has no odd prime divisor" is asymptotically independent of parity, the density of pairs surviving both the cyclotomic obstruction and this forced mod-3 obstruction is

\[
\boxed{
\frac12\cdot\frac8{\pi^2}
=
\frac4{\pi^2}.
}
\]

---

# 6. The first local sieve for \(\{2,3\}\)

Now consider

\[
N_{2,3}(a,b)=1+2^a3^b.
\]

Modulo \(5\), note that

\[
3\equiv2^3\pmod5.
\]

Thus

\[
2^a3^b
\equiv
2^{a+3b}\pmod5.
\]

Since \(2^2\equiv-1\pmod5\), we have

\[
5\mid N_{2,3}(a,b)
\iff
 a+3b\equiv2\pmod4.
\]

Again the value is then greater than \(5\), so it is composite.

Exactly one quarter of exponent residue pairs modulo \(4\) satisfy this forbidden relation. Hence the mod-5 admissible fraction is \(3/4\).

The forbidden relation is invariant under common multiplication of \((a,b)\) by an odd integer, because

\[
d(a+3b)\equiv2\pmod4
\iff
 a+3b\equiv2\pmod4
\qquad(d\text{ odd}).
\]

Therefore the Möbius count from Theorem 3.1 can be combined directly with the mod-5 restriction.

## Proposition 6.1

The density of exponent pairs surviving both the common-odd-divisor obstruction and the forced mod-5 obstruction is

\[
\boxed{
\frac34\cdot\frac8{\pi^2}
=
\frac6{\pi^2}.
}
\]

---

# 7. A rigorous local-sieve asymmetry

The two first exact-support competitors therefore have different first-order admissible exponent densities:

\[
\boxed{
\{2,3\}:\ \frac6{\pi^2}
}
\]

versus

\[
\boxed{
\{2,5\}:\ \frac4{\pi^2}.
}
\]

The ratio is

\[
\boxed{\frac32.}
\]

This is a genuine arithmetic asymmetry between the two parameter spaces.

It is already visible before using any probabilistic model for primality.

---

# 8. Counting by numerical size

The exponent box is not the natural arithmetic ordering. To count candidates below a numerical bound \(X\), put

\[
L=\log X.
\]

For \(q\in\{3,5\}\), the inequality

\[
2^a q^b\le X
\]

is

\[
a\log2+b\log q\le L.
\]

The number of positive lattice points in this triangle is

\[
\frac{L^2}{2\log2\log q}+O(L).
\]

Applying the cyclotomic and first local sieve densities gives the following admissible-candidate asymptotics.

## Theorem 8.1 — first-sieve candidate counts

Let \(A_{23}(X)\) count exponent pairs \((a,b)\) satisfying

\[
2^a3^b\le X,
\]

with gcd a power of two and with the mod-5 compositeness class removed. Then

\[
\boxed{
A_{23}(X)
\sim
\frac{3}{\pi^2\log2\log3}
(\log X)^2.
}
\]

Let \(A_{25}(X)\) count exponent pairs \((a,b)\) satisfying

\[
2^a5^b\le X,
\]

with gcd a power of two and with the mod-3 compositeness class removed. Then

\[
\boxed{
A_{25}(X)
\sim
\frac{2}{\pi^2\log2\log5}
(\log X)^2.
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

### Proof sketch

The unfiltered lattice-point count follows from the area of the weighted exponent triangle. The odd-gcd condition is imposed by Möbius inversion over odd common divisors. The finite residue restrictions modulo \(4\) or \(2\) are periodic and have the densities computed above. Standard lattice-point estimates on dilates of a fixed rational-periodic decomposition give the claimed main terms; boundary contributions are \(o(L^2)\). \(\square\)

---

# 9. What the asymmetry does and does not prove

The asymmetry is mathematically real:

\[
\{2,3\}
\quad\text{has a larger first-sieve candidate space than}\quad
\{2,5\}.
\]

But this is **not yet a killing certificate** for the graph automorphism problem.

The multiplicity tower at this stage sees

\[
\mu(S)=|X_S|,
\]

not the asymptotic density of exponent vectors producing the candidates.

If both

\[
X_{\{2,3\}}
\quad\text{and}\quad
X_{\{2,5\}}
\]

are infinite, then their cardinalities are both \(\aleph_0\), regardless of very different counting laws.

Thus:

\[
\boxed{
\text{local sieve asymmetry}\not\Rightarrow
\text{fiber-cardinality asymmetry}.
}
\]

This distinction is essential.

---

# 10. Heuristic reading, kept separate from theorem

A naive random-prime heuristic would assign probability roughly

\[
\frac1{\log(2^a q^b)}
\]

to an admissible candidate. Since the number of admissible exponent pairs below \(X\) grows on the order of \((\log X)^2\), such a heuristic predicts an unbounded number of prime values for both supports.

This is only heuristic. It does not prove infinitude of Pierpont primes or of primes of the form

\[
2^a5^b+1.
\]

The current literature still treats infinitude of the Pierpont family

\[
2^a3^b+1
\]

as unproved.

Therefore no publication claim in HATTER-SOL-05 should convert this heuristic into a theorem.

---

# 11. Generalized Fermat spine inside every support

The cyclotomic theorem has another useful consequence.

Fix any positive vector \(\mathbf m=(m_q)_{q\in S}\) and put

\[
A=\prod_{q\in S}q^{m_q}.
\]

Consider the subsequence

\[
F_k(A)=A^{2^k}+1.
\]

Each term belongs to the original candidate family, with exponent vector

\[
2^k\mathbf m.
\]

## Proposition 11.1

If \(A\) is even, then the numbers

\[
F_0(A),F_1(A),F_2(A),\ldots
\]

are pairwise coprime.

Moreover, every prime divisor \(r\mid F_k(A)\) satisfies

\[
\boxed{
\operatorname{ord}_r(A)=2^{k+1}
}
\]

and hence

\[
\boxed{
r\equiv1\pmod{2^{k+1}}.}
\]

### Proof

If \(j<k\), then modulo \(F_j(A)\),

\[
A^{2^j}\equiv-1.
\]

Raising to the even power \(2^{k-j}\) gives

\[
A^{2^k}\equiv1,
\]

so

\[
F_k(A)\equiv2\pmod{F_j(A)}.
\]

All \(F_j(A)\) are odd because \(A\) is even, so their gcd is one.

If an odd prime \(r\mid A^{2^k}+1\), then

\[
A^{2^k}\equiv-1\pmod r,
\]

so the order divides \(2^{k+1}\) but not \(2^k\). Hence it equals \(2^{k+1}\), which divides \(r-1\). \(\square\)

## Corollary 11.2

Every exact-support candidate family contains an infinite pairwise-coprime subsequence.

In particular, even if an exact fiber were empty, the composite candidates along this spine would require infinitely many distinct prime divisors, and those divisors occur in congruence classes

\[
r\equiv1\pmod{2^{k+1}}
\]

of unbounded modulus.

This reinforces the finite-cover no-go theorem from the previous strike.

---

# 12. Structural conclusion

Two naive mechanisms for making a higher exact-support fiber small are now ruled out as explanations of a Fermat-like collapse:

1. **finite fixed-divisor coverings** fail for every support \(S\ni2\);
2. **common-exponent cyclotomic factorization** causes a density-zero collapse only when \(|S|=1\), whereas every dimension \(|S|\ge2\) retains a positive-density exponent set.

Thus the higher-fiber problem really is qualitatively different from the Fermat-prime problem.

The first pair \(\{2,3\}\) and \(\{2,5\}\) is locally asymmetric, but both remain two-dimensional after all currently controlled universal obstructions.

This makes the following boundary precise:

\[
\boxed{
\text{Fermat sparsity is structurally one-dimensional;}
}
\]

\[
\boxed{
\text{higher exact-support sparsity, if strong enough to kill symmetry, must come from deeper prime-value arithmetic.}
}
\]

---

# 13. Next strike

The next useful target is no longer ordinary local sieving.

We should ask whether the parameter-space asymmetry can be **amplified by exact descendants** into a graph-visible cardinality asymmetry.

Concretely, for

\[
p\in X_{\{2,3\}}
\quad\text{and}\quad
p'\in X_{\{2,5\}},
\]

compare higher fibers such as

\[
X_{\{2,3,p\}}
\quad\text{and}\quad
X_{\{2,5,p'\}}.
\]

The immediate question is whether some finite configuration of exact supports admits a provable nonexistence or finite-cardinality statement on one side but not the other.

If that also fails for structural reasons, the branch will have identified a much stronger no-go frontier and may itself cross the publication threshold even without killing \((3\ 5)\).

---

# Literature boundary

The common-exponent factorization \(A^d+1\) for odd \(d\) is classical. The Pierpont-prime family \(2^a3^b+1\) is classical and its infinitude remains unproved. The present note uses these facts to isolate a dimension transition and a local-sieve asymmetry specific to the HATTER-SOL-05 exact-support programme; it does not claim priority for the underlying cyclotomic identities or standard lattice-point/Möbius estimates.
