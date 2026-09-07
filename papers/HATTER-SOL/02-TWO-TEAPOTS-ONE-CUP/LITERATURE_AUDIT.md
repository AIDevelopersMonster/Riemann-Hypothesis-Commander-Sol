# HATTER-SOL-02 · Hostile Literature Audit

## Scope

This audit asks a narrow question: which parts of the current HATTER-SOL-02 mathematics are standard consequences of known theories, which are direct repackagings of known finite-monoid results, and which combinations remain plausible candidates for an original contribution?

The audit is deliberately conservative. Absence of a search hit is not evidence of novelty.

## 1. Standard background that must not be presented as new

The following ingredients are classical:

- the free commutative monoid structure of \((\mathbb N_{>0},\times)\) with primes as free generators;
- the resulting identification \(\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P)\);
- Dirichlet's theorem on primes in arithmetic progressions;
- the Chinese remainder theorem;
- quadratic reciprocity, the supplementary laws, and finite prescribed Legendre-symbol patterns;
- automorphisms of finite cyclic groups and orbit classification by element order;
- general reduct/expansion monotonicity of automorphism groups;
- Skolem arithmetic as the first-order theory of the multiplicative natural numbers.

These are infrastructure only.

### Core Skolem-arithmetic references

- Andrzej Mostowski, **On direct products of theories**, *Journal of Symbolic Logic* 17(1), 1-31 (1952), DOI **10.2307/2267454**.
- Alexis Bès; Denis Richard, **Undecidable Extensions of Skolem Arithmetic**, *Journal of Symbolic Logic* 63(2), 379-401 (1998), DOI **10.2307/2586837**.
- Atticus Stonestrom, **Some model theory of Th(N,·)**, *Mathematical Logic Quarterly* 68(3), 288-303 (2022), DOI **10.1002/malq.202100049**.
- Łukasz Kamiński, **Definable sets in Skolem arithmetic**, arXiv:**2510.02062** (2025).

Consequences for claims:

1. `Aut(N_{>0}, x) ~= Sym(P)` is elementary free-commutative-monoid structure, not a new theorem.
2. The programme "add a relation to Skolem arithmetic and study what changes" is classical.
3. Any originality claim must concern the specific modular/quadratic probes, the explicit action on prime generators, exact orbit formulae, separation laws, or their synthesis.

## 2. Important prior work directly touching the composite-modulus layer

Recent work by Joseph Atalaye, Liam Baker, and Sophie Marques directly studies automorphism groups of finite multiplicative residue monoids.

- J. Atalaye; L. Baker; S. Marques, **On the automorphism group of the monoid of the integers modulo a prime power**, arXiv:**2408.06278** (2024, revised version). The paper determines automorphism groups of unit groups and multiplicative monoids modulo prime powers, including the exceptional 2-adic structure.
- J. Atalaye; L. Baker; S. Marques, **Automorphism groups of direct products of multiplicative monoids of certain rings**, arXiv:**2605.06119** (2026). The paper proves factorwise rigidity under its hypotheses and deduces that the multiplicative monoid modulo \(n\) is controlled by its prime-power components.

Therefore HATTER-SOL-02 must **not** advertise the finite quotient

\[
(\mathbb Z/m\mathbb Z,\cdot)
\]

as a newly classified object.

Its role in our article is instead:

1. a known finite quotient induced by the relation \(E_m\);
2. an input whose symmetry is lifted back to the free multiplicative monoid of positive integers;
3. a device for describing the induced orbits of the **prime generators**;
4. a source of the support/depth distinction: prime support determines which prime atoms are fixed, whereas prime-power depth refines the unresolved outside orbits.

The support/depth interpretation and prime-orbit lift are the series-specific contribution candidates, not the finite quotient classification itself.

## 3. Quadratic characters and prescribed Legendre patterns

The arithmetic facts behind the one-bit probes are classical.

For finitely many target primes \(q_i\), one can prescribe the signs

\[
\left(\frac{q_i}{p}\right)\in\{\pm1\}
\]

simultaneously by choosing \(p\) in a suitable reduced residue class. A direct construction uses quadratic reciprocity, CRT, and Dirichlet's theorem.

A quantitatively much stronger nearby problem is studied in:

- Brandon Hanson; Robert C. Vaughan; Ruixiang Zhang, **The least number with prescribed Legendre symbols and representation by binary quadratic forms of small discriminant**, *Journal of Number Theory* 179, 3-16 (2017), DOI **10.1016/j.jnt.2017.03.004**, arXiv:**1605.05584**.

Consequences for claims:

- the prescribed-pattern lemma itself is classical;
- the existence of primes separating two prescribed primes by a quadratic character is classical;
- the exact coding statement \(\kappa_2(S)=\lceil\log_2|S|\rceil\) should be presented as an elementary optimal coding theorem **inside the HATTER-SOL framework**, obtained from a counting lower bound plus the classical pattern-realization lemma.

## 4. Quadratic one-bit probes: the narrower structural package

For

\[
Q_p(x)\iff p\nmid x\text{ and }\left(\frac{x}{p}\right)=1,
\]

consider

\[
\mathcal Q_F=(\mathbb N_{>0},\times,(Q_p)_{p\in F}).
\]

A targeted literature search did not locate an exact source packaging the following standard-model automorphism statements together:

- exact finite prime-orbit decomposition for \(\mathcal Q_F\);
- the finite-family non-rigidity barrier;
- the exact rigidity criterion via injectivity of the Legendre-signature map;
- arbitrarily sparse infinite rigidifying families;
- comparison with full congruence predicates as a structural-compression phenomenon.

This remains a negative targeted-search result only, not proof of priority.

## 5. Exact finite coding law

For a prescribed finite set \(S\) of \(N\) primes, define \(\kappa_2(S)\) as the minimum number of odd probe primes, disjoint from \(S\), whose Legendre-signature vectors distinguish the elements of \(S\) from one another.

The current theorem is

\[
\kappa_2(S)=\lceil\log_2N\rceil.
\]

The lower bound is the binary-capacity bound \(2^k\ge N\). The upper bound comes from assigning distinct binary codewords to the \(N\) targets and realizing each coordinate as a prescribed Legendre-symbol pattern.

Publication wording must distinguish:

1. **finite observational separation**: the targets have distinct signatures among themselves;
2. **global automorphism individuality**: a target is a singleton orbit among all primes.

Finite probes achieve the first optimally but, for targets outside the probe set, never the second: each finite signature is shared by infinitely many primes.

## 6. Alice / Caterpillar boundary

The literary frame is also kept explicit.

- Lewis Carroll, **Alice's Adventures in Wonderland** (1865), Chapter V: the Caterpillar asks Alice, **"Who are you?"**; Alice replies that she hardly knows at present because she has changed several times.
- Texas A&M Cushing Memorial Library's 2018 exhibition **"Who in the world am I? Ah, that's the great puzzle!: The Faces of Alice in Wonderland"** explicitly foregrounds mutable identity in the Alice tradition.
- Francine F. Abeles, **Mathematics: Logic and Lewis Carroll**, *Nature* 527, 302-303 (2015), DOI **10.1038/527302a**, surveys Carroll's mathematical and logical legacy.

Consequences:

- the Caterpillar scene is a legitimate literary frame for identity;
- the connection between "Who are you?" and automorphism orbits is **our modern mathematical allegory**, not a claim about Carroll's hidden intention;
- generated illustrations are contemporary original artwork and must not be treated as Carroll/Tenniel illustrations;
- text invented inside generated art is not evidence and must not be cited as a Carroll quotation.

## 7. Current defensible contribution claim

The strongest publication-safe formulation is:

> We introduce a prime-individuality viewpoint for explicit expansions of the standard multiplicative monoid and compute how selected modular and quadratic predicates split the automorphism orbit of its prime generators. Within this framework we obtain exact finite orbit counts, a finite-information barrier, sparse rigidifying families, a one-bit rigidity criterion, and an optimal finite quadratic coding law. The arithmetic ingredients and the surrounding theories are classical; the contribution claimed here is the explicit orbit/separation framework and this theorem package.

This is a framework-and-theorem-package claim, not a claim that the ingredients are new.

## 8. Claims to avoid

Do not claim:

- first study of automorphisms of \(\mathbb Z/n\mathbb Z\) under multiplication;
- first use of Legendre symbols to separate primes;
- first proof that prescribed quadratic patterns exist;
- first study of expansions of Skolem arithmetic;
- Shannon-optimality for the entire infinite structure;
- that Carroll intended an automorphism-theoretic reading of Alice.

The phrase **one-bit probe** refers only to the binary output of each predicate on each query.

## 9. Publication threshold assessment

The branch has crossed the mathematical threshold for a substantive preprint, provided that the final article keeps the claims narrow and includes proofs rather than only theorem summaries.

The strongest chain is

\[
\text{pure prime symmetry}
\to
\text{exact finite fragmentation}
\to
\text{support/depth}
\to
\text{finite barrier}
\to
\text{sparse rigidity}
\to
\text{one-bit rigidity}
\to
\text{optimal finite coding}.
\]

The next step is article assembly and proof preflight, not another theorem hunt.