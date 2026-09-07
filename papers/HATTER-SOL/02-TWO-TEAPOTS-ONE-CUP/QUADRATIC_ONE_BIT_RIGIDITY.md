# HATTER-SOL-02 · One-Bit Quadratic Rigidity

## 0. Why weaken the additive probe?

The congruence expansions

\[
(\mathbb N_{>0},\times,E_p),
\qquad
E_p(x,y)\iff x\equiv y\pmod p,
\]

carry much more information than is needed for the sparse-rigidity construction. The previous proof of sparse rigidity used only one invariant of the residue of a prime modulo \(p\): whether that residue is a square.

This note isolates that information and shows that a single **binary predicate per selected modulus** is enough.

---

# 1. The quadratic probe

For an odd prime \(p\), define the unary predicate

\[
Q_p(x)
\iff
p\nmid x
\text{ and }
\left(\frac{x}{p}\right)=1,
\]

where \((\frac{x}{p})\) is the Legendre symbol.

Thus \(Q_p(x)\) says that the residue of \(x\) modulo \(p\) is a nonzero quadratic residue.

For a set \(F\) of odd primes, define

\[
\mathcal Q_F
=
(\mathbb N_{>0},\times,(Q_p)_{p\in F}).
\]

The language now remembers only one bit of multiplicative-residue information per input and per selected modulus:

\[
Q_p(x)\in\{0,1\}.
\]

---

# 2. A single quadratic probe

For fixed odd prime \(p\), partition the primes other than \(p\) into

\[
R_p
=
\left\{q\in\mathbb P\setminus\{p\}:
\left(\frac qp\right)=1
\right\}
\]

and

\[
N_p
=
\left\{q\in\mathbb P\setminus\{p\}:
\left(\frac qp\right)=-1
\right\}.
\]

By Dirichlet's theorem, both sets are infinite.

## Lemma 2.1 — the modulus prime is definable from one bit

The prime \(p\) is the unique multiplicative atom \(q\) satisfying

\[
\neg Q_p(q^2).
\]

### Proof

If \(q=p\), then \(p\mid q^2\), so \(Q_p(q^2)\) is false.

If \(q\ne p\) is prime, then \(q^2\) is a nonzero square modulo \(p\), hence

\[
Q_p(q^2)
\]

is true. Therefore \(p\) is uniquely characterized among the atoms. \(\square\)

So every automorphism of \(\mathcal Q_{\{p\}}\) fixes \(p\).

## Theorem 2.2 — exact automorphism group of one quadratic probe

\[
\boxed{
\operatorname{Aut}(\mathcal Q_{\{p\}})
\cong
\operatorname{Sym}(R_p)
\times
\operatorname{Sym}(N_p).
}
\]

The prime-individuality orbits are exactly

\[
\{p\},\qquad R_p,\qquad N_p.
\]

Hence one quadratic bit creates exactly three prime orbits.

### Proof

Every automorphism fixes \(p\) by Lemma 2.1. For a prime \(q\ne p\), the truth value of \(Q_p(q)\) records precisely whether \(q\in R_p\) or \(q\in N_p\). Hence an automorphism must preserve these two sets.

Conversely, take arbitrary permutations

\[
\sigma_R\in\operatorname{Sym}(R_p),
\qquad
\sigma_N\in\operatorname{Sym}(N_p),
\]

fix \(p\), and extend the resulting prime permutation multiplicatively.

For any integer

\[
x=p^e\prod_{q\ne p}q^{v_q(x)},
\]

if \(e>0\), then both before and after the automorphism \(Q_p(x)\) is false.

If \(e=0\), then

\[
\left(\frac{x}{p}\right)
=
\prod_{q\ne p}
\left(\frac qp\right)^{v_q(x)}.
\]

The permutation preserves the sign \((\frac qp)\in\{\pm1\}\) of every prime factor, so the Legendre symbol of the product is unchanged. Therefore \(Q_p\) is preserved. \(\square\)

---

# 3. Finite families of one-bit probes

Let \(F\) be a finite set of odd primes. Every prime in \(F\) is fixed individually because its own predicate \(Q_p\) detects its square.

For \(q\notin F\), define the quadratic signature

\[
\chi_F(q)
=
\left(
\left(\frac qp\right)
\right)_{p\in F}
\in\{\pm1\}^{F}.
\]

For a sign vector

\[
\varepsilon=(\varepsilon_p)_{p\in F}\in\{\pm1\}^{F},
\]

put

\[
C_\varepsilon
=
\{q\in\mathbb P\setminus F:
\chi_F(q)=\varepsilon\}.
\]

## Lemma 3.1 — every quadratic signature is infinite

Every \(C_\varepsilon\) is infinite.

### Proof

For each \(p\in F\), choose a nonzero residue \(a_p\pmod p\) with

\[
\left(\frac{a_p}{p}\right)=\varepsilon_p.
\]

By CRT there is a reduced residue class

\[
a\pmod M,
\qquad
M=\prod_{p\in F}p,
\]

realizing all chosen signs. Dirichlet's theorem gives infinitely many primes

\[
q\equiv a\pmod M.
\]

All such primes lie in \(C_\varepsilon\). \(\square\)

## Theorem 3.2 — exact finite one-bit decomposition

For finite \(F\) of odd primes,

\[
\boxed{
\operatorname{Aut}(\mathcal Q_F)
\cong
\prod_{\varepsilon\in\{\pm1\}^{F}}
\operatorname{Sym}(C_\varepsilon).
}
\]

All primes in \(F\) are fixed individually, and the primes outside \(F\) split into exactly

\[
2^{|F|}
\]

infinite orbits.

Therefore

\[
\boxed{
\#\bigl(\mathbb P/\operatorname{Aut}(\mathcal Q_F)\bigr)
=
|F|+2^{|F|}.
}
\]

### Proof

Every named predicate \(Q_p\) fixes its own modulus prime \(p\). For a prime \(q\notin F\), the tuple of truth values \((Q_p(q))_{p\in F}\) is exactly its quadratic signature.

Hence every automorphism preserves each cell \(C_\varepsilon\) setwise.

Conversely, arbitrary independent permutations of the cells, fixing every prime in \(F\), extend multiplicatively. Since the Legendre-symbol sign of every prime factor at every selected modulus is preserved, all predicates \(Q_p\) are preserved on all integers. \(\square\)

## Corollary 3.3 — finite one-bit barrier

For every finite \(F\),

\[
\operatorname{Aut}(\mathcal Q_F)\ne\{\mathrm{id}\}.
\]

Indeed every outside prime orbit is infinite.

Thus finitely many binary probes cannot rigidify the multiplicative world.

---

# 4. Sparse one-bit rigidity

The finite barrier is sharp in the same sense as for full congruence relations: an arbitrarily sparse infinite family of one-bit probes can force complete rigidity.

## Lemma 4.1 — pair separator

For any two distinct primes \(q\ne r\), there exist infinitely many odd primes \(p\notin\{q,r\}\) such that

\[
\left(\frac qp\right)
\ne
\left(\frac rp\right).
\]

### Proof

Equivalently,

\[
\left(\frac{qr}{p}\right)=-1.
\]

Since \(qr\) is not a square, the corresponding quadratic Dirichlet character is nontrivial. There exists a reduced residue class on which it has value \(-1\), and Dirichlet's theorem supplies infinitely many primes in that class. \(\square\)

## Theorem 4.2 — arbitrarily sparse one-bit rigidity

Let

\[
B_1<B_2<B_3<\cdots,
\qquad
B_n\to\infty,
\]

be any prescribed growth schedule. Then there exists a set of odd primes

\[
F=\{p_1,p_2,p_3,\ldots\}
\]

with

\[
p_n>B_n
\]

for every \(n\), such that

\[
\boxed{
\operatorname{Aut}(\mathcal Q_F)=\{\mathrm{id}\}.
}
\]

### Proof

Enumerate all unordered pairs of distinct primes:

\[
\{q_1,r_1\},\{q_2,r_2\},\ldots
\]

Inductively use Lemma 4.1 to choose a fresh odd prime \(p_n>B_n\), distinct from \(q_n,r_n\), such that

\[
\left(\frac{q_n}{p_n}\right)
\ne
\left(\frac{r_n}{p_n}\right).
\]

Let

\[
F=\{p_n:n\ge1\}.
\]

Every \(p_n\in F\) is fixed by its own predicate \(Q_{p_n}\).

Suppose an automorphism sends a prime \(q\) to a distinct prime \(r\). Their pair appears as \(\{q_n,r_n\}\) for some \(n\). But the predicate \(Q_{p_n}\) gives opposite truth values on \(q\) and \(r\), contradicting preservation of the named predicate.

Thus every prime is fixed. A multiplicative automorphism is determined by its action on primes, so the automorphism is the identity. \(\square\)

Because the separators can be chosen arbitrarily large, the rigidity set \(F\) may be made as sparse as desired. In particular, one can require

\[
\sum_{p\in F}\frac1p<\infty
\]

and zero relative density among all primes.

---

# 5. Information compression relative to full congruence data

For a full congruence predicate \(E_p\), one modulus produces

\[
1+\tau(p-1)
\]

prime orbits.

For the quadratic one-bit predicate \(Q_p\), one modulus always produces exactly

\[
3
\]

prime orbits:

\[
\{p\},\ R_p,\ N_p.
\]

So \(Q_p\) retains dramatically less local information.

Nevertheless, at the global infinite level both languages admit arbitrarily sparse rigidifying families:

\[
(\mathbb N_{>0},\times,(E_p)_{p\in F})
\quad\text{can be rigid},
\]

and already

\[
\boxed{
(\mathbb N_{>0},\times,(Q_p)_{p\in F})
\quad\text{can be rigid}.
}
\]

Hence full residue information is unnecessary for complete arithmetic individuality.

The essential resource is not local resolution but **pair-separation capacity**.

---

# 6. Separation criterion for arbitrary families

For any set \(F\) of odd primes, define the quadratic signature map on primes outside \(F\):

\[
\chi_F:
\mathbb P\setminus F
\to
\{\pm1\}^{F},
\qquad
q\mapsto
\left(\left(\frac qp\right)\right)_{p\in F}.
\]

## Theorem 6.1 — exact rigidity criterion

\[
\boxed{
\operatorname{Aut}(\mathcal Q_F)=\{\mathrm{id}\}
\iff
\chi_F\text{ is injective on }\mathbb P\setminus F.
}
\]

### Proof

If \(\chi_F\) is not injective, choose distinct primes \(q,r\notin F\) with identical signatures. The transposition \(q\leftrightarrow r\), fixing every other prime, extends multiplicatively and preserves every \(Q_p\), so the structure is not rigid.

If \(\chi_F\) is injective, every prime in \(F\) is fixed by its own predicate, while every prime outside \(F\) is uniquely determined by its full truth-value signature. Hence every automorphism fixes every prime and is the identity. \(\square\)

This gives a complete characterization of rigidity for the one-bit family.

---

# 7. Conceptual law

The HATTER-SOL-02 hierarchy can now be sharpened:

### Pure multiplication

\[
\mathbb P\text{ is one orbit.}
\]

### One quadratic bit

\[
\mathbb P
\rightsquigarrow
\{p\}\sqcup R_p\sqcup N_p.
\]

### Finitely many bits

\[
|F|+2^{|F|}
\]

prime orbits, with every outside orbit infinite.

### Sparse infinite bits

If the signatures separate all prime pairs,

\[
\operatorname{Aut}(\mathcal Q_F)=\{\mathrm{id}\}.
\]

Thus the amount of *local* information per modulus can be reduced to one bit without losing the possibility of *global* rigidity.

This is the first genuine information-compression law of the series:

\[
\boxed{
\text{one-bit local probes}
+\text{sparse global separation}
\Longrightarrow
\text{complete prime individuality}.
}
\]

---

# 8. Important limitation of the phrase “one bit”

The expression “one-bit probe” refers to the **output alphabet of each predicate on each input**:

\[
Q_p(x)\in\{0,1\}.
\]

It does not mean that an entire infinite predicate \(Q_p\) contains only one bit of description-theoretic information. The modulus \(p\) itself is named, and the predicate is available on every integer.

Therefore publication language should distinguish carefully between:

- one-bit **observation per query**;
- finite/infinite **language size**;
- description cost of the selected moduli;
- total information content of an infinite relational structure.

The theorem is a structural compression result, not a Shannon-bit count of the whole theory.

---

# 9. Publication significance

Together with the congruence and composite-modulus theorems, the one-bit result gives HATTER-SOL-02 a complete mathematical progression:

\[
\boxed{
\begin{array}{c}
\text{pure multiplicative symmetry}\\
\downarrow\\
\text{finite exact fragmentation by congruences}\\
\downarrow\\
\text{support/depth law for composite moduli}\\
\downarrow\\
\text{finite-information barrier}\\
\downarrow\\
\text{arbitrarily sparse rigidity}\\
\downarrow\\
\text{one-bit sparse rigidity and exact separation criterion.}
\end{array}
}
\]

At this point the mathematical threshold for a substantive second paper is close to being met. The remaining mandatory step is a hostile literature audit, especially around expansions of Skolem arithmetic, quadratic-character predicates, and coloured free commutative monoids.
