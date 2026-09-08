# HATTER-SOL-02 · Congruence-Reduct Theorems

## 0. Setup

Let

\[
\mathbb N_{>0}=\{1,2,3,\ldots\},
\qquad
\mathbb P=\{2,3,5,\ldots\}.
\]

For every prime \(p\), write

\[
E_p(x,y)\iff x\equiv y\pmod p.
\]

For \(F\subseteq\mathbb P\), define the expansion of the multiplicative monoid

\[
\mathcal M_F=
(\mathbb N_{>0},\times,(E_p)_{p\in F}),
\]

where every \(E_p\) is a separately named binary relation.

For a structure \(\mathcal R\) containing multiplication, primes are definable as multiplicative atoms, so every automorphism acts on \(\mathbb P\). We call the orbits of this action the **prime-individuality orbits**.

The point of the family \(\mathcal M_F\) is that it adds a controlled amount of additive information (congruence data) to the purely multiplicative world.

---

# 1. The zero class is structurally visible

## Lemma 1.1

For fixed prime \(p\), the \(E_p\)-class of \(0\) inside \(\mathbb N_{>0}\), i.e. the set \(p\mathbb N_{>0}\), is definable in \(\mathcal M_{\{p\}}\) by

\[
Z_p(x)\iff \forall y\;E_p(xy,x).
\]

### Proof

If \(p\mid x\), then \(xy\equiv0\equiv x\pmod p\) for every \(y\), so \(Z_p(x)\) holds.

If \(p\nmid x\), choose \(y=p\). Then \(xy\equiv0\pmod p\), while \(x\not\equiv0\pmod p\), so \(E_p(xy,x)\) fails. Hence \(Z_p(x)\) is exactly the set of multiples of \(p\). \(\square\)

## Corollary 1.2

Every automorphism of \(\mathcal M_{\{p\}}\) fixes the prime \(p\).

### Proof

Primality is definable from multiplication as atomicity. Among the prime atoms, \(p\) is the unique one satisfying \(Z_p\). Therefore it is fixed. \(\square\)

For general \(F\), every \(p\in F\) is fixed individually because its own named relation \(E_p\) defines its zero class.

---

# 2. One-modulus theorem

Fix a prime \(p\). For every nonzero residue \(r\in\mathbb F_p^\times\), define

\[
C_r=
\{q\in\mathbb P\setminus\{p\}:q\equiv r\pmod p\}.
\]

By Dirichlet's theorem, every \(C_r\) is countably infinite.

## Theorem 2.1 — exact automorphism group for one congruence layer

There is a split exact sequence

\[
1\longrightarrow
\prod_{r\in\mathbb F_p^\times}\operatorname{Sym}(C_r)
\longrightarrow
\operatorname{Aut}(\mathcal M_{\{p\}})
\overset{\rho_p}{\longrightarrow}
\operatorname{Aut}(\mathbb F_p^\times)
\longrightarrow1.
\]

Consequently, noncanonically,

\[
\boxed{
\operatorname{Aut}(\mathcal M_{\{p\}})
\cong
\left(\prod_{r\in\mathbb F_p^\times}\operatorname{Sym}(C_r)\right)
\rtimes
\operatorname{Aut}(\mathbb F_p^\times).
}
\]

Since \(\mathbb F_p^\times\) is cyclic,

\[
\operatorname{Aut}(\mathbb F_p^\times)
\cong
(\mathbb Z/(p-1)\mathbb Z)^\times.
\]

### Proof

Let \(g\in\operatorname{Aut}(\mathcal M_{\{p\}})\). By Corollary 1.2, \(g(p)=p\). Hence \(g\) preserves divisibility by \(p\).

For \(r\in\mathbb F_p^\times\), choose any \(x\in\mathbb N_{>0}\) with \(x\equiv r\pmod p\), and define

\[
\alpha_g(r):=g(x)\pmod p.
\]

This is well-defined: if \(x\equiv y\pmod p\), then \(E_p(x,y)\), and preservation of \(E_p\) gives \(g(x)\equiv g(y)\pmod p\). Since \(g\) is bijective and preserves the zero class, \(\alpha_g\) is a bijection of \(\mathbb F_p^\times\).

Moreover, for nonzero residues \(r,s\), choose \(x\equiv r\), \(y\equiv s\). Then

\[
\alpha_g(rs)
\equiv g(xy)
=g(x)g(y)
\equiv \alpha_g(r)\alpha_g(s)\pmod p.
\]

Thus \(\alpha_g\in\operatorname{Aut}(\mathbb F_p^\times)\). This defines the homomorphism

\[
\rho_p:g\mapsto\alpha_g.
\]

If \(g\in\ker\rho_p\), then every prime residue class \(C_r\) is preserved setwise. Conversely, arbitrary independent permutations of the sets \(C_r\), with \(p\) fixed, extend uniquely by prime factorization to multiplicative automorphisms preserving \(E_p\). Hence

\[
\ker\rho_p
\cong
\prod_{r\in\mathbb F_p^\times}\operatorname{Sym}(C_r).
\]

To prove surjectivity, take \(\alpha\in\operatorname{Aut}(\mathbb F_p^\times)\). Since all \(C_r\) are countably infinite, choose bijections

\[
\beta_r:C_r\to C_{\alpha(r)}.
\]

Fix \(p\), map each prime \(q\in C_r\) by \(\beta_r\), and extend multiplicatively. For every \(x\) not divisible by \(p\), its residue is sent to \(\alpha(x\bmod p)\); multiples of \(p\) remain multiples of \(p\). Therefore equality of residues modulo \(p\) is preserved in both directions. Thus \(\rho_p\) is onto.

Finally, choose once and for all enumerations

\[
C_r=\{c_{r,1},c_{r,2},\ldots\}.
\]

For \(\alpha\in\operatorname{Aut}(\mathbb F_p^\times)\), define a lift by

\[
c_{r,n}\mapsto c_{\alpha(r),n},
\qquad p\mapsto p.
\]

These lifts form a subgroup isomorphic to \(\operatorname{Aut}(\mathbb F_p^\times)\), proving that the exact sequence splits. The splitting depends on the chosen enumerations, hence is noncanonical. \(\square\)

---

# 3. Exact prime-orbit classification for one modulus

For \(q\ne p\), let

\[
\operatorname{ord}_p(q)
\]

be the multiplicative order of \(q\bmod p\) in \(\mathbb F_p^\times\).

## Theorem 3.1

The prime-individuality orbits of \(\mathcal M_{\{p\}}\) are:

1. the singleton \(\{p\}\);
2. for every divisor \(d\mid p-1\), one infinite orbit
   \[
   \mathcal O_{p,d}
   =\{q\in\mathbb P\setminus\{p\}:\operatorname{ord}_p(q)=d\}.
   \]

Hence the number of prime orbits is

\[
\boxed{1+\tau(p-1)},
\]

where \(\tau(n)\) is the divisor-counting function.

### Proof

The kernel of \(\rho_p\) is transitive inside each residue class \(C_r\). The quotient group \(\operatorname{Aut}(\mathbb F_p^\times)\) moves residue classes according to automorphisms of the cyclic group \(\mathbb F_p^\times\).

Automorphisms of a finite cyclic group preserve element order and are transitive on the set of elements of any fixed order \(d\mid p-1\). Therefore two primes \(q,q'\ne p\) lie in the same \(\operatorname{Aut}(\mathcal M_{\{p\}})\)-orbit exactly when

\[
\operatorname{ord}_p(q)=\operatorname{ord}_p(q').
\]

For each divisor \(d\mid p-1\), choose a residue \(r\in\mathbb F_p^\times\) of order \(d\). Dirichlet's theorem gives infinitely many primes in the class \(r\pmod p\), so every orbit \(\mathcal O_{p,d}\) is infinite. \(\square\)

### Examples

- \(p=2\): \(1+\tau(1)=2\) prime orbits: \(\{2\}\) and all odd primes.
- \(p=3\): \(1+\tau(2)=3\) prime orbits: \(\{3\}\), primes \(\equiv1\pmod3\), and primes \(\equiv2\pmod3\).
- \(p=5\): \(1+\tau(4)=4\) prime orbits: \(\{5\}\), and the three order types \(1,2,4\) in \(\mathbb F_5^\times\).

This is the first exact quantitative law of the series: **one additive congruence layer fragments the single multiplicative prime orbit into exactly \(1+\tau(p-1)\) orbits.**

---

# 4. Finite-family theorem

Let \(F\subset\mathbb P\) be finite. Put

\[
R_F:=\prod_{p\in F}\mathbb F_p^\times.
\]

For a residue vector

\[
\mathbf r=(r_p)_{p\in F}\in R_F,
\]

define

\[
C_{\mathbf r}
=
\{q\in\mathbb P\setminus F:
q\equiv r_p\pmod p\text{ for every }p\in F\}.
\]

By the Chinese remainder theorem, \(\mathbf r\) determines a reduced residue class modulo

\[
M_F:=\prod_{p\in F}p.
\]

Dirichlet's theorem therefore implies that every \(C_{\mathbf r}\) is infinite.

Define

\[
A_F:=\prod_{p\in F}\operatorname{Aut}(\mathbb F_p^\times).
\]

It acts coordinatewise on \(R_F\).

## Theorem 4.1 — finite congruence decomposition

There is a split exact sequence

\[
1\to
\prod_{\mathbf r\in R_F}\operatorname{Sym}(C_{\mathbf r})
\to
\operatorname{Aut}(\mathcal M_F)
\to
A_F
\to1.
\]

Consequently, noncanonically,

\[
\boxed{
\operatorname{Aut}(\mathcal M_F)
\cong
\left(
\prod_{\mathbf r\in R_F}\operatorname{Sym}(C_{\mathbf r})
\right)
\rtimes
\prod_{p\in F}\operatorname{Aut}(\mathbb F_p^\times).
}
\]

### Proof

For each \(p\in F\), Lemma 1.1 applied to the named relation \(E_p\) defines the zero class modulo \(p\), and hence fixes the unique prime \(p\). Thus every element of \(F\) is fixed individually.

An automorphism \(g\) therefore induces, for each \(p\in F\), a group automorphism

\[
\alpha_{g,p}\in\operatorname{Aut}(\mathbb F_p^\times)
\]

by the same argument as in Theorem 2.1. This yields

\[
\rho_F:\operatorname{Aut}(\mathcal M_F)\to A_F.
\]

The kernel consists exactly of independent permutations of each residue-vector cell \(C_{\mathbf r}\).

For surjectivity, take \(\boldsymbol\alpha=(\alpha_p)_{p\in F}\in A_F\). It sends

\[
\mathbf r\mapsto\boldsymbol\alpha(\mathbf r)
=(\alpha_p(r_p))_{p\in F}.
\]

Every source and target cell is countably infinite, so choose bijections

\[
C_{\mathbf r}\to C_{\boldsymbol\alpha(\mathbf r)}
\]

and extend the resulting prime permutation multiplicatively, fixing all primes in \(F\). The residue of every integer modulo every \(p\in F\) is transformed by \(\alpha_p\), hence every \(E_p\) is preserved.

A simultaneous choice of enumerations of the cells gives a group-theoretic splitting exactly as in the one-modulus case. \(\square\)

---

# 5. Exact prime-orbit count for finite \(F\)

For \(q\notin F\), define its **order signature**

\[
\mathbf d_F(q)
:=
(\operatorname{ord}_p(q))_{p\in F}.
\]

Each coordinate \(\operatorname{ord}_p(q)\) is a divisor of \(p-1\).

## Theorem 5.1 — order-signature classification

For primes \(q,q'\notin F\),

\[
q\sim_{\mathcal M_F}q'
\iff
\mathbf d_F(q)=\mathbf d_F(q').
\]

Every possible divisor vector

\[
(d_p)_{p\in F},
\qquad d_p\mid p-1,
\]

is realized by infinitely many primes.

Therefore the prime-individuality orbit count is exactly

\[
\boxed{
\mathfrak O(F)
:=
\#(\mathbb P/\operatorname{Aut}(\mathcal M_F))
=
|F|+\prod_{p\in F}\tau(p-1).
}
\]

The \(|F|\) first orbits are the fixed singleton primes in \(F\); all remaining orbits are infinite.

### Proof

The kernel of \(\rho_F\) is transitive within each residue-vector cell. The quotient \(A_F\) acts independently in each cyclic group \(\mathbb F_p^\times\), and its orbits in that coordinate are exactly the sets of elements of fixed multiplicative order. Therefore residue vectors are in the same \(A_F\)-orbit exactly when their coordinatewise order vectors agree.

Conversely, choose for every \(p\in F\) a residue \(r_p\in\mathbb F_p^\times\) of prescribed order \(d_p\mid p-1\). The Chinese remainder theorem combines the \(r_p\) into a reduced residue class modulo \(M_F\), and Dirichlet's theorem supplies infinitely many primes in that class. \(\square\)

## Corollary 5.2 — exact fragmentation increment

If \(s\notin F\) is prime, then

\[
\mathfrak O(F\cup\{s\})
-
\mathfrak O(F)
=
1+
\left(\tau(s-1)-1\right)
\prod_{p\in F}\tau(p-1).
\]

Thus a new congruence layer does two things at once:

1. it extracts \(s\) from an infinite orbit and makes it a singleton;
2. it splits every previous outside-orbit according to multiplicative order modulo \(s\).

This is an exact **symmetry-fragmentation law**.

---

# 6. Finite-congruence barrier

## Corollary 6.1

For every finite \(F\subset\mathbb P\),

\[
\operatorname{Fix}_{\mathbb P}
(\operatorname{Aut}(\mathcal M_F))
=F.
\]

### Proof

Every \(p\in F\) is fixed by its named zero class. If \(q\notin F\), then \(q\) lies in some cell \(C_{\mathbf r}\), and that cell is infinite. A transposition of \(q\) with another prime in the same cell belongs to the kernel of \(\rho_F\), so \(q\) is not fixed by all automorphisms. \(\square\)

## Corollary 6.2 — finite-information obstruction

No finite family of prime-modulus congruence relations can rigidify the multiplicative monoid:

\[
\boxed{
F\text{ finite}
\implies
\operatorname{Aut}(\mathcal M_F)\ne\{\mathrm{id}\}.
}
\]

In fact every non-singleton prime orbit outside \(F\) is infinite.

This is the finite-congruence barrier promised in the initial HATTER-SOL-02 programme.

---

# 7. A sparse infinite family can nevertheless force complete rigidity

The finite barrier raises the natural question: does one need *all* congruence relations to recover full individuality? No.

We first isolate the separator needed for the construction.

## Lemma 7.1 — quadratic separator

For any two distinct primes \(q\ne r\), there exist infinitely many odd primes \(p\notin\{q,r\}\) such that

\[
\left(\frac qp\right)
\ne
\left(\frac rp\right),
\]

where \((\frac{\cdot}{p})\) is the Legendre symbol.

### Proof sketch

Since \(qr\) is not a rational square, the associated quadratic Dirichlet character is nontrivial. Hence there exists a reduced residue class on which the character takes value \(-1\), and Dirichlet's theorem gives infinitely many primes in that class. For such \(p\),

\[
\left(\frac{qr}{p}\right)=-1,
\]

so the two Legendre symbols differ. Equivalently, this follows from the splitting law for primes in the quadratic field \(\mathbb Q(\sqrt{qr})\). \(\square\)

The square subgroup

\[
(\mathbb F_p^\times)^2
\]

is characteristic in \(\mathbb F_p^\times\). Therefore every automorphism of \(\mathbb F_p^\times\) preserves quadratic residuacity.

## Theorem 7.2 — arbitrarily sparse rigidity

Let

\[
B_1<B_2<B_3<\cdots
\]

be any prescribed sequence of positive real numbers tending to infinity. Then there exists an infinite set of primes

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
\operatorname{Aut}(\mathcal M_F)=\{\mathrm{id}\}.
}
\]

In particular, one may require simultaneously that \(F\) have relative density zero inside the primes and that

\[
\sum_{p\in F}\frac1p<\infty.
\]

### Proof

Enumerate all unordered pairs of distinct primes:

\[
\{q_1,r_1\},\{q_2,r_2\},\ldots
\]

Inductively, having chosen \(p_1,\ldots,p_{n-1}\), use Lemma 7.1 to choose a new odd prime \(p_n\), distinct from \(q_n,r_n\) and all previous choices, such that

\[
p_n>B_n
\]

and

\[
\left(\frac{q_n}{p_n}\right)
\ne
\left(\frac{r_n}{p_n}\right).
\]

Let \(F=\{p_n:n\ge1\}\).

Take \(g\in\operatorname{Aut}(\mathcal M_F)\). Every \(p\in F\) is fixed individually by its named relation \(E_p\).

Suppose two distinct primes \(q,r\notin F\) satisfy \(g(q)=r\). Their unordered pair occurs as \(\{q_n,r_n\}\) for some \(n\). The automorphism \(g\) induces

\[
\alpha_{p_n}\in\operatorname{Aut}(\mathbb F_{p_n}^\times).
\]

But every such \(\alpha_{p_n}\) preserves the characteristic subgroup of squares. Hence it preserves the Legendre-symbol partition into quadratic residues and nonresidues. This contradicts the construction of \(p_n\), for which \(q\) and \(r\) have opposite quadratic character modulo \(p_n\).

Thus no two distinct primes can be interchanged. Every prime is fixed by \(g\), and since a multiplicative automorphism of \(\mathbb N_{>0}\) is determined by its action on primes, \(g=\mathrm{id}\).

Since the separating prime for each pair may be chosen arbitrarily large, the growth constraint \(p_n>B_n\) is free. Taking, for example, \(B_n=2^{n+1}\) gives

\[
\sum_n\frac1{p_n}<\frac12
\]

and

\[
\#\{p\in F:p\le x\}=O(\log x),
\]

so \(F\) has relative density zero among all primes. \(\square\)

## Interpretation

Finite congruence information can never rigidify the multiplicative world, yet full rigidity does not require anything remotely like *all* additive information. A countable family of extremely sparse modular probes can separate every pair of primes.

Thus there is no density threshold of the form

\[
\text{“many congruences are required for rigidity”.}
\]

What matters is **separation power**, not density.

---

# 8. Main conceptual synthesis

The results above turn the tea-party metaphor into an exact hierarchy.

### Pure multiplicative teapot

\[
(\mathbb N_{>0},\times):
\qquad
\mathbb P\text{ is one orbit.}
\]

### One modular drop from the additive teapot

\[
\mathcal M_{\{p\}}:
\qquad
1+\tau(p-1)\text{ prime orbits.}
\]

### Finitely many drops

\[
\mathcal M_F:
\qquad
\mathfrak O(F)=|F|+\prod_{p\in F}\tau(p-1),
\]

but infinitely many primes remain in infinite orbits.

### An arbitrarily sparse infinite recipe

There exist \(F\) as thin as prescribed for which

\[
\mathcal M_F\text{ is completely rigid.}
\]

This gives the second article a precise mathematical arc:

\[
\boxed{
\text{symmetry}
\to
\text{fragmentation}
\to
\text{finite-information barrier}
\to
\text{sparse rigidity}.
}
\]

---

# 9. Literature status

The ingredients are classical:

- unique factorization / free commutative monoid structure of positive integers;
- Dirichlet's theorem in arithmetic progressions;
- CRT;
- automorphisms of finite cyclic groups;
- quadratic characters and quadratic reciprocity / splitting in quadratic fields;
- general reduct-expansion and automorphism-group monotonicity.

Nearby model-theoretic literature includes work on Skolem arithmetic, notably the structure and definability theory of \(\operatorname{Th}(\mathbb N_{>0},\times)\). A first targeted search did **not** locate this exact congruence-expansion family, the semidirect-product calculation, the order-signature orbit formula, or the sparse-rigidity packaging. This remains a preliminary negative search result, not a novelty claim.

Before publication, perform a dedicated literature audit under the languages:

- Skolem arithmetic expansions by congruences;
- graded / coloured free commutative monoids;
- automorphism groups of free commutative monoids with finite quotient colourings;
- reducts/expansions of arithmetic by modular equivalence relations.

---

# 10. Next research targets

1. **Composite-modulus theorem.** Classify \(\operatorname{Aut}(\mathbb N_{>0},\times,E_m)\) for arbitrary composite \(m\). This should reveal how a single relation can encode several prime divisors and zero-divisor strata.
2. **Rigidity criterion for arbitrary infinite \(F\).** Find necessary/sufficient conditions in terms of the family of order/character signatures.
3. **Minimal separating language.** Replace full congruence equivalence \(E_p\) by weaker unary predicates such as quadratic residuacity and determine whether sparse rigidity survives.
4. **Information invariant.** Formalize a structure-dependent prime individuality profile beyond raw orbit count.
5. **Hostile literature audit.** Required before any novelty statement or Zenodo freeze.
