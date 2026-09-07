# HATTER-SOL-02 · Optimal Finite Quadratic Coding

## 0. Purpose

The one-bit predicates

\[
Q_p(x)
\iff
p\nmid x\text{ and }\left(\frac{x}{p}\right)=1
\]

produce only a binary answer at each selected modulus. For a finite set of target primes, this raises a precise coding question:

> How many quadratic probes are necessary and sufficient to give \(N\) prescribed primes pairwise distinct quadratic signatures?

This is a **finite observational-separation** problem. It must not be confused with global automorphism rigidity: with finitely many probes, every signature class still contains infinitely many primes outside the target set, so no target prime outside the probe set becomes globally fixed.

---

# 1. Finite quadratic signature complexity

Let

\[
S=\{q_1,\ldots,q_N\}\subset\mathbb P
\]

be a finite set of distinct primes.

For a finite set \(F\) of odd primes disjoint from \(S\), define

\[
\chi_F(q)
=
\left(\left(\frac qp\right)\right)_{p\in F}
\in\{\pm1\}^{F}.
\]

Define the **finite quadratic separation complexity**

\[
\kappa_2(S)
:=
\min\left\{|F|:
F\cap S=\varnothing,
\ \chi_F|_S\text{ is injective}
\right\}.
\]

For \(|S|=1\), set \(\kappa_2(S)=0\).

---

# 2. Prescribed Legendre-pattern lemma

## Lemma 2.1

Let

\[
S=\{q_1,\ldots,q_N\}
\]

be distinct primes and let

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_N)
\in\{\pm1\}^N.
\]

Then there exist infinitely many odd primes \(p\notin S\) such that

\[
\left(\frac{q_i}{p}\right)=\varepsilon_i
\qquad (1\le i\le N).
\]

Moreover, \(p\) may be required to exceed any prescribed bound.

### Proof

First handle the parity condition. If \(2\in S\), prescribe

\[
p\equiv
\begin{cases}
1\pmod 8,&\text{if the desired value of }(2/p)\text{ is }+1,\\
5\pmod 8,&\text{if the desired value of }(2/p)\text{ is }-1.
\end{cases}
\]

In either case \(p\equiv1\pmod4\), so quadratic reciprocity has no sign twist for the odd target primes:

\[
\left(\frac{q_i}{p}\right)
=
\left(\frac{p}{q_i}\right)
\qquad(q_i\text{ odd}).
\]

For each odd \(q_i\in S\), choose a nonzero residue

\[
a_i\pmod{q_i}
\]

with

\[
\left(\frac{a_i}{q_i}\right)=\varepsilon_i.
\]

By the Chinese remainder theorem, these local prescriptions, together with the chosen class modulo \(8\), determine a reduced residue class

\[
a\pmod M,
\qquad
M=8\prod_{q_i\in S,\ q_i\ne2}q_i.
\]

Every prime \(p\equiv a\pmod M\) has the required Legendre-symbol pattern. Dirichlet's theorem on primes in arithmetic progressions gives infinitely many such primes, hence arbitrarily large ones. \(\square\)

### Literature status

The ability to prescribe finite quadratic-character patterns is classical; it is an immediate quadratic-reciprocity + CRT + Dirichlet construction and belongs to the literature on prescribed Legendre symbols. The theorem below is the coding-theoretic application relevant to the HATTER-SOL framework, not a claim of a new reciprocity theorem.

---

# 3. Exact finite coding theorem

## Theorem 3.1 — optimal quadratic probe complexity

For every finite set \(S\) of \(N\ge1\) distinct primes,

\[
\boxed{
\kappa_2(S)=\lceil\log_2 N\rceil.
}
\]

The selected probe primes can furthermore be required to be arbitrarily large, subject to any prescribed finite lower bounds.

### Proof

Let

\[
k=|F|.
\]

A family of \(k\) binary quadratic probes gives at most

\[
2^k
\]

distinct signatures. Therefore injectivity on an \(N\)-element set requires

\[
2^k\ge N,
\]

so

\[
k\ge\lceil\log_2N\rceil.
\]

This proves the lower bound.

For the upper bound, put

\[
k=\lceil\log_2N\rceil.
\]

Choose \(N\) distinct codewords

\[
c_i=(c_{i1},\ldots,c_{ik})
\in\{\pm1\}^k,
\qquad 1\le i\le N.
\]

For each coordinate \(j\), apply Lemma 2.1 to the desired pattern

\[
(c_{1j},\ldots,c_{Nj}).
\]

Choose a fresh probe prime \(p_j\notin S\) realizing that pattern, and if desired choose it above any prescribed lower bound. Then

\[
\left(\frac{q_i}{p_j}\right)=c_{ij}
\]

for every \(i,j\). Hence

\[
\chi_F(q_i)=c_i,
\qquad
F=\{p_1,\ldots,p_k\},
\]

and the signatures on \(S\) are pairwise distinct. Thus

\[
\kappa_2(S)\le k.
\]

Together with the lower bound, equality follows. \(\square\)

---

# 4. What the theorem does and does not say

The theorem gives an exact coding law:

\[
N\text{ chosen primes}
\quad\longleftrightarrow\quad
\lceil\log_2N\rceil\text{ binary quadratic tests}
\]

for **pairwise distinction inside that finite target set**.

It does **not** say that those \(N\) primes become singleton automorphism orbits in the full structure. For finite \(F\), every sign vector is realized by infinitely many primes (CRT + Dirichlet), so each target prime still shares its full signature with infinitely many primes outside \(S\).

Thus two notions must remain distinct throughout publication:

1. **finite observational separation:** targets have distinct signatures among themselves;
2. **global structural individuality:** a target is fixed by every automorphism of the full infinite structure.

Finite binary probes achieve the first optimally, but never the second for outside primes.

---

# 5. From finite coding to sparse global rigidity

The exact finite law explains the infinite construction conceptually.

At a finite stage, \(k\) bits can distinguish at most \(2^k\) chosen targets. For countably many primes, no finite \(k\) can suffice globally. However, an infinite sequence of binary probes can assign a unique infinite signature to every prime.

Because each new probe prime may be chosen arbitrarily large, the sequence of probes can simultaneously be:

- pair-separating;
- arbitrarily sparse;
- of zero relative density among primes;
- chosen with convergent reciprocal sum.

Thus the finite coding theorem and sparse-rigidity theorem form two halves of one statement:

\[
\boxed{
\text{local binary capacity is logarithmic on finite targets,}
\quad
\text{while countably sparse capacity suffices globally.}
}
\]

---

# 6. Publication role

This theorem should replace vague language such as “a few bits of additive information identify many primes.” It gives an exact, falsifiable statement with a matching lower and upper bound.

The correct interpretation for the tea-party metaphor is:

- each quadratic probe is a **yes/no sip** from the second teapot;
- \(k\) such sips create a \(k\)-bit signature;
- exactly \(\lceil\log_2N\rceil\) carefully chosen sips suffice to distinguish \(N\) selected prime guests from one another;
- only an infinite separating menu can make every prime guest globally unique.
