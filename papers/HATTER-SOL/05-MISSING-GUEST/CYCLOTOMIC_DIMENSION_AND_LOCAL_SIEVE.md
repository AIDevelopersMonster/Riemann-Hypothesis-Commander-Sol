# HATTER-SOL-05 · Cyclotomic Dimension and Local Sieve Asymmetry

## 0. Status

Canonical v1.0 source after hostile proof audit.

We study

\[
N_S(\mathbf e)=1+\prod_{q\in S}q^{e_q},\qquad e_q\ge1,
\]

for finite prime supports \(S\ni2\). The purpose is to separate three facts that must not be conflated:

1. a universal cyclotomic obstruction;
2. a rigorous local-sieve asymmetry between \(\{2,3\}\) and \(\{2,5\}\);
3. the still-open prime-value problem needed to turn parameter-space asymmetry into exact-fiber cardinality asymmetry.

---

# 1. Common-exponent obstruction

## Theorem 1.1

If

\[
N_S(\mathbf e)=1+q_1^{e_1}\cdots q_k^{e_k}
\]

is prime, then

\[
\boxed{\gcd(e_1,\ldots,e_k)\text{ is a power of }2.}
\]

### Proof

If an odd \(d>1\) divides all exponents, write \(e_i=df_i\) and

\[
A=q_1^{f_1}\cdots q_k^{f_k}>1.
\]

Then

\[
N_S(\mathbf e)=A^d+1=(A+1)(A^{d-1}-A^{d-2}+\cdots-A+1),
\]

with both factors greater than one. \(\square\)

For \(S=\{2\}\), this forces \(e_1=2^m\), recovering the classical Fermat sparsity.

---

# 2. Dimension jump

For \(k\ge2\), let

\[
\mathcal C_k(B)=\{\mathbf e\in[1,B]^k:\gcd(\mathbf e)\text{ has no odd prime divisor}\}.
\]

## Theorem 2.1

For every \(k\ge2\),

\[
\boxed{
\frac{|\mathcal C_k(B)|}{B^k}
\longrightarrow
\prod_{\ell\text{ odd prime}}(1-\ell^{-k})
=
\frac1{\zeta(k)(1-2^{-k})}.
}
\]

In particular,

\[
\boxed{\frac{|\mathcal C_2(B)|}{B^2}\to\frac8{\pi^2}.}
\]

### Proof

By Möbius inversion over odd common divisors,

\[
|\mathcal C_k(B)|
=
\sum_{\substack{d\le B\\d\text{ odd}}}
\mu(d)\left\lfloor\frac Bd\right\rfloor^k.
\]

After division by \(B^k\), dominated convergence gives

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^k}
=
\prod_{\ell\text{ odd prime}}(1-\ell^{-k})
=
\frac1{\zeta(k)(1-2^{-k})}.
\]

For \(k=2\), this equals \(8/\pi^2\). \(\square\)

Thus the universal common-exponent obstruction is density-zero in dimension one but leaves positive density in every fixed dimension \(k\ge2\).

---

# 3. First local sieve: \(\{2,5\}\)

Let

\[
N_{2,5}(a,b)=1+2^a5^b.
\]

Modulo \(3\),

\[
N_{2,5}(a,b)\equiv1+(-1)^{a+b}\pmod3.
\]

Hence every prime value must satisfy

\[
\boxed{a+b\equiv0\pmod2.}
\]

Exactly half of all exponent pairs survive this local obstruction. Since multiplication of \((a,b)\) by an odd common divisor preserves parity, Möbius inversion combines with the parity condition, giving total admissible exponent density

\[
\boxed{\frac12\cdot\frac8{\pi^2}=\frac4{\pi^2}.}
\]

---

# 4. First local sieve: \(\{2,3\}\)

Let

\[
N_{2,3}(a,b)=1+2^a3^b.
\]

Modulo \(5\), since \(3\equiv2^3\pmod5\),

\[
5\mid N_{2,3}(a,b)
\iff
 a+3b\equiv2\pmod4.
\]

Exactly one quarter of residue pairs modulo \(4\) are forbidden. The relation is preserved under multiplication of both exponents by an odd integer. Therefore the density surviving both the cyclotomic obstruction and the mod-5 obstruction is

\[
\boxed{\frac34\cdot\frac8{\pi^2}=\frac6{\pi^2}.}
\]

Hence the first local-sieve ratio is

\[
\boxed{
\frac{6/\pi^2}{4/\pi^2}=\frac32.
}
\]

This is a rigorous arithmetic asymmetry of exponent parameter spaces. It is not yet an exact-fiber cardinality asymmetry.

---

# 5. Counting by numerical size

Put

\[
L=\log X,\qquad \alpha=\log2,\qquad \beta=\log q.
\]

The unfiltered inequality

\[
2^a q^b\le X
\]

is

\[
\alpha a+\beta b\le L.
\]

Its positive lattice-point count is

\[
\frac{L^2}{2\alpha\beta}+O(L).
\]

We now give the full weighted proof that was only sketched in the earlier draft.

## Lemma 5.1 — periodic lattice count in a weighted triangle

Fix a periodic subset \(R\subset\mathbb Z_{>0}^2\) with period modulus \(m\), and suppose its density among residue classes modulo \(m\) is \(r\). Then

\[
\#\{(u,v)\in R:\alpha u+\beta v\le Y\}
=
\frac{r}{2\alpha\beta}Y^2+O(Y+1),
\]

where the implied constant depends only on \(\alpha,\beta,m\).

### Proof

Decompose the integer lattice into the finitely many residue classes modulo \(m\). Each residue class contributes the area of a translated lattice of covolume \(m^2\) inside the triangle, plus an \(O(Y+1)\) boundary error. Summing over the \(r m^2\) allowed classes gives the stated main term. \(\square\)

## Theorem 5.2 — first-sieve candidate counts

Let \(A_{23}(X)\) count positive pairs \((a,b)\) such that

\[
2^a3^b\le X,
\]

\(\gcd(a,b)\) is a power of two, and the mod-5 compositeness class is excluded. Then

\[
\boxed{
A_{23}(X)
=
\frac{3}{\pi^2\log2\log3}(\log X)^2
+O((\log X)\log\log X).
}
\]

Let \(A_{25}(X)\) be defined analogously for \(2^a5^b\), with the mod-3 class excluded. Then

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

For an odd integer \(d\), impose \(d\mid a,b\) and write

\[
a=du,\qquad b=dv.
\]

Then

\[
\alpha u+\beta v\le\frac Ld.
\]

Because \(d\) is odd, the relevant local residue restriction is unchanged under multiplication by \(d\). Thus Lemma 5.1 gives

\[
N_d(L)
=
\frac{r}{2\alpha\beta}\frac{L^2}{d^2}
+O\left(\frac Ld+1\right),
\]

where

\[
r=\frac34\quad\text{for }\{2,3\},
\qquad
r=\frac12\quad\text{for }\{2,5\}.
\]

Möbius inversion over odd common divisors yields

\[
A(L)=
\sum_{\substack{d\le cL\\d\text{ odd}}}
\mu(d)N_d(L),
\]

for a fixed positive constant \(c\) depending only on the weights. Hence

\[
A(L)
=
\frac{rL^2}{2\alpha\beta}
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
+O\left(L\sum_{d\le cL}\frac1d+L\right).
\]

The error is \(O(L\log L)\), and

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
=
\prod_{\ell\text{ odd prime}}(1-\ell^{-2})
=
\frac8{\pi^2}.
\]

Therefore

\[
A(L)
=
\frac{4r}{\pi^2\alpha\beta}L^2+O(L\log L).
\]

For \(q=3\), \(r=3/4\), giving

\[
\frac{3}{\pi^2\log2\log3}L^2.
\]

For \(q=5\), \(r=1/2\), giving

\[
\frac{2}{\pi^2\log2\log5}L^2.
\]

Since \(L=\log X\), the theorem follows. \(\square\)

---

# 6. What the asymmetry proves — and does not prove

The candidate parameter space for \(\{2,3\}\) is rigorously larger, at the first controlled sieve level, than the corresponding space for \(\{2,5\}\). But the multiplicity tower records only

\[
\mu(S)=|X_S|.
\]

If both exact fibers are infinite, then both cardinalities equal \(\aleph_0\). Therefore

\[
\boxed{
\text{local-sieve asymmetry}\not\Rightarrow
\text{fiber-cardinality asymmetry}.
}
\]

In particular, the theorem above does not prove infinitude of Pierpont primes \(2^a3^b+1\), nor of primes \(2^a5^b+1\).

---

# 7. Generalized Fermat spine

Fix positive exponents \((m_q)_{q\in S}\) and put

\[
A=\prod_{q\in S}q^{m_q}.
\]

Since \(2\in S\), \(A\) is even. Consider

\[
F_k(A)=A^{2^k}+1.
\]

## Proposition 7.1

The numbers \(F_k(A)\) are pairwise coprime. Every prime divisor \(r\mid F_k(A)\) satisfies

\[
\boxed{\operatorname{ord}_r(A)=2^{k+1}}
\]

and therefore

\[
\boxed{r\equiv1\pmod{2^{k+1}}.}
\]

### Proof

If \(j<k\), then modulo \(F_j(A)\),

\[
A^{2^j}\equiv-1,
\]

so after raising to the even power \(2^{k-j}\),

\[
A^{2^k}\equiv1,
\qquad
F_k(A)\equiv2\pmod{F_j(A)}.
\]

Both numbers are odd, hence coprime. If \(r\mid A^{2^k}+1\), then \(A^{2^k}\equiv-1\pmod r\), so the multiplicative order of \(A\) modulo \(r\) is exactly \(2^{k+1}\), which divides \(r-1\). \(\square\)

Thus every exact-support candidate family contains an infinite pairwise-coprime generalized-Fermat spine. In particular, no finite set of fixed prime divisors can cover all candidates along that spine.

---

# 8. Publication boundary

The rigorous conclusions are:

- singleton support has a genuine cyclotomic density collapse;
- every fixed support dimension \(k\ge2\) retains positive cyclotomic admissible density;
- the \(\{2,3\}\) and \(\{2,5\}\) first local sieves differ by the exact factor \(3/2\);
- numerical-size weighted counts have the explicit constants proved above;
- none of this alone settles the exact-fiber cardinalities.

The common factorization, Pierpont family, Möbius inversion, lattice counting, and generalized Fermat identities are classical ingredients. HATTER-SOL-05 uses them only as rigorously delimited components of the exact-support automorphism programme; no literature-wide priority is claimed for the classical ingredients.
