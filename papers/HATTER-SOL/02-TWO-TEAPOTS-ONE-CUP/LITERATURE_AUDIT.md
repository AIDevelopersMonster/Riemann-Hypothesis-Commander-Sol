# HATTER-SOL-02 · Hostile Literature Audit

## Scope

This audit asks a narrow question: which parts of the current HATTER-SOL-02 mathematics are standard consequences of known theories, which are direct repackagings of known finite-monoid results, and which combinations remain plausible candidates for an original contribution?

The audit is deliberately conservative. Absence of a search hit is not evidence of novelty.

## 1. Standard background that must not be presented as new

The following ingredients are classical:

- the free commutative monoid structure of \((\mathbb N_{>0},\times)\) with primes as free generators;
- the resulting identification \(\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P)\);
- Dirichlet's theorem on primes in arithmetic progressions;
- CRT;
- quadratic reciprocity and prescribed finite Legendre-symbol patterns;
- automorphisms of finite cyclic groups and orbit classification by element order;
- general model-theoretic reduct/expansion monotonicity of automorphism groups;
- Skolem arithmetic as the first-order theory of the multiplicative natural numbers.

These are infrastructure only.

## 2. Important prior work that directly touches the composite-modulus layer

A targeted audit found recent work by Atalaye, Baker, and Marques on automorphism groups of multiplicative monoids of residue rings modulo prime powers and their products. Their results show that the finite quotient layer

\[
(\mathbb Z/m\mathbb Z,\cdot)
\]

has already been studied structurally, including the prime-power local factors and product decomposition.

Therefore the HATTER-SOL-02 composite-modulus discussion must not be advertised as the first classification of automorphisms of multiplicative residue monoids. Its role should instead be:

1. to use the known finite quotient automorphism structure as an input;
2. to lift that quotient symmetry back to the free multiplicative monoid of positive integers;
3. to classify the induced orbits of *prime generators*;
4. to interpret the support of the modulus versus prime-power depth as two different kinds of individuality information.

The support/depth interpretation and prime-orbit lift are the series-specific contribution candidate, not the finite quotient classification by itself.

## 3. Skolem arithmetic and definability

The literature on Skolem arithmetic establishes a mature model theory of \((\mathbb N_{>0},\times)\), including definability, decidability, and extensions. This means HATTER-SOL-02 should avoid broad claims such as "adding modular predicates to multiplication has not been studied."

The defensible narrower object is the **standard-model automorphism action on the prime generators under explicitly named modular or quadratic predicates**.

Targeted searches did not locate an exact theorem stated in the following form:

\[
\operatorname{Aut}(\mathbb N_{>0},\times,(E_p)_{p\in F})
\]

with an explicit prime-orbit formula

\[
|F|+\prod_{p\in F}\tau(p-1),
\]

nor the corresponding binary quadratic-predicate family with

\[
|F|+2^{|F|}
\]

prime orbits. This remains only a preliminary negative search result.

## 4. Quadratic one-bit probes

The arithmetic fact that finitely many Legendre symbols can be prescribed simultaneously is classical, by quadratic reciprocity + CRT + Dirichlet.

Likewise, the fact that quadratic characters separate square classes is classical.

What is potentially new in HATTER-SOL-02 is not either fact in isolation, but the packaging into an automorphism-rigidity statement for the standard multiplicative monoid:

\[
\mathcal Q_F=(\mathbb N_{>0},\times,(Q_p)_{p\in F}),
\]

with:

- exact finite prime-orbit decomposition;
- finite-family non-rigidity;
- exact rigidity criterion via injectivity of the Legendre-signature map;
- arbitrarily sparse infinite rigidifying families;
- comparison with full congruence predicates as a structural compression phenomenon.

No exact match for this package was located in the initial hostile search.

## 5. Exact finite coding law

For a prescribed finite set \(S\) of \(N\) primes, the theorem

\[
\kappa_2(S)=\lceil\log_2N\rceil
\]

uses only a counting lower bound plus the classical ability to prescribe Legendre-symbol patterns. The proof is elementary once the question is formulated.

Therefore this result should be presented as an exact coding theorem *inside the HATTER-SOL framework*, not as a deep new theorem of analytic number theory.

Its value is conceptual precision:

- \(k\) binary probes have capacity at most \(2^k\);
- prescribed Legendre patterns achieve that capacity exactly on any finite target set;
- finite observational separation must be distinguished from global automorphism individuality.

## 6. Current defensible novelty claim

The strongest publication-safe formulation at this stage is:

> We introduce a prime-individuality viewpoint for expansions of the standard multiplicative monoid and compute how selected modular and quadratic predicates split the prime-generator orbit. Within this framework we derive exact finite orbit counts, a finite-information barrier, sparse rigidifying families, a one-bit rigidity criterion, and an optimal finite quadratic coding law.

This is a **framework-and-theorem package claim**, not a claim that the arithmetic ingredients are new.

## 7. Claims to avoid

Do not claim:

- first study of automorphisms of \(\mathbb Z/n\mathbb Z\) under multiplication;
- first use of Legendre symbols to separate primes;
- first proof that prescribed quadratic patterns exist;
- first study of expansions of Skolem arithmetic;
- information-theoretic optimality in Shannon's sense for the entire infinite structure.

The phrase "one-bit probe" refers only to the binary output of each unary predicate on each query.

## 8. Publication threshold assessment

The branch has now crossed the mathematical threshold for a substantive preprint **provided** the final article keeps the novelty claims narrow and cites the finite-monoid and Skolem-arithmetic literature explicitly.

The strongest chain is:

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

The next step should be article assembly, not another theorem hunt.
