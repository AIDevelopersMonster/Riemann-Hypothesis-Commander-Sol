# HATTER-SOL-02 · RESEARCH STATE

## Working title

**«Два чайника, одна чашка: редукции структуры и возвращение симметрии простых»**

English working title:

**“Two Teapots, One Cup: Structural Reducts and the Return of Prime Symmetry.”**

## Starting question

HATTER-SOL-01 established the elementary contrast

\[
\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P)
\]

versus the rigidity of additive / full natural arithmetic. HATTER-SOL-02 asks for an **intermediate theory**:

> If we begin with the multiplicative world and reveal only a controlled amount of additive information, how much prime symmetry disappears, and can that loss be measured exactly?

The central object is no longer merely the paired map \(\Omega(a,b)=(a+b,ab)\). That map remains the literary doorway. The mathematical core is the lattice of **reducts and expansions** of the multiplicative structure and the induced subgroup descent inside \(\operatorname{Sym}(\mathbb P)\).

## Basic invariant: prime individuality under a structure

For a structure \(\mathcal R\) on \(\mathbb N_{>0}\) whose automorphisms preserve primality, define

\[
G_{\mathcal R}=\operatorname{Aut}(\mathcal R),
\]

and on primes

\[
p\sim_{\mathcal R}q
\iff
\exists g\in G_{\mathcal R}: g(p)=q.
\]

The equivalence classes are the **prime-individuality orbits** of \(\mathcal R\).

- one orbit on \(\mathbb P\): maximal prime symmetry;
- singleton orbits: full prime individuality;
- intermediate orbit partitions: partial individuality.

If \(\mathcal S\) is an expansion of \(\mathcal R\), then

\[
\operatorname{Aut}(\mathcal S)\le \operatorname{Aut}(\mathcal R),
\]

so prime orbits can only split. This is the monotonicity principle for individuality under added structure.

## First decisive correction / refinement

Full multiplication is **not** needed to make the natural numbers rigid once addition is present. Already

\[
\operatorname{Aut}(\mathbb N,+)=\{\mathrm{id}\}.
\]

Likewise, standard order or successor already rigidify \(\mathbb N\). Therefore the interesting intermediate zone is not simply

\[
\times \to (+,\times),
\]

but structures that leak **partial additive information** without restoring the whole additive skeleton.

## First candidate family: prime-modulus congruence reducts

For a prime \(p\), let

\[
E_p(x,y)\iff x\equiv y\pmod p,
\]

and define

\[
\mathcal M_p=(\mathbb N_{>0},\times,E_p).
\]

For a finite set \(F\subset\mathbb P\), define

\[
\mathcal M_F=(\mathbb N_{>0},\times,(E_p)_{p\in F}).
\]

These structures inject genuine additive information (congruence classes) into the multiplicative world, but only at finite resolution.

## First theorem target

For one prime modulus \(p\), let

\[
C_r=\{q\in\mathbb P\setminus\{p\}:q\equiv r\pmod p\},\qquad r\in\mathbb F_p^\times.
\]

Expected exact structure:

\[
1\to \prod_{r\in\mathbb F_p^\times}\operatorname{Sym}(C_r)
\to \operatorname{Aut}(\mathcal M_p)
\to \operatorname{Aut}(\mathbb F_p^\times)
\to1.
\]

Since \(\mathbb F_p^\times\) is cyclic,

\[
\operatorname{Aut}(\mathbb F_p^\times)\cong(\mathbb Z/(p-1)\mathbb Z)^\times.
\]

The sequence should split noncanonically by choosing enumerations of the prime residue classes. Dirichlet's theorem guarantees that every \(C_r\) is infinite.

Consequences:

1. \(p\) is fixed by every automorphism of \(\mathcal M_p\);
2. every other prime still belongs to an infinite orbit;
3. one congruence relation creates exactly one named prime but leaves enormous residual prime symmetry.

## Finite-congruence barrier

For finite \(F\subset\mathbb P\), the expected generalization is

\[
\operatorname{Aut}(\mathcal M_F)
\cong
\left(
\prod_{\mathbf r\in\prod_{p\in F}\mathbb F_p^\times}
\operatorname{Sym}(C_{\mathbf r})
\right)
\rtimes
\prod_{p\in F}\operatorname{Aut}(\mathbb F_p^\times),
\]

noncanonically, where \(C_{\mathbf r}\) is the set of primes outside \(F\) with the residue vector \(\mathbf r\). CRT + Dirichlet imply every compatible residue-vector class contains infinitely many primes.

Hence:

\[
\boxed{
\text{no finite family of prime-modulus congruence relations can fully individuate the primes.}
}
\]

More sharply, the primes fixed pointwise by all automorphisms should be exactly the moduli in \(F\):

\[
\operatorname{Fix}_{\mathbb P}(\operatorname{Aut}(\mathcal M_F))=F.
\]

This is the current main theorem candidate for HATTER-SOL-02.

## Why this fits the series metaphor

- teapot \(\times\): all prime atoms interchangeable;
- a small pour from the additive teapot: a congruence relation \(E_p\);
- the cup: the expansion \(\mathcal M_p\);
- result: one prime becomes individually recognizable, while all remaining primes retain structured residual symmetry.

Thus the metaphor can be made exact: **amount/type of added structure corresponds to subgroup descent of the automorphism group.**

## Literature guard (preliminary)

Nearby standard areas found so far:

- free commutative monoid structure of \((\mathbb N_{>0},\times)\);
- Presburger arithmetic and reducts of arithmetic;
- automorphisms of nonstandard models of arithmetic;
- automorphism groups of multiplicative monoids modulo \(n\);
- general model-theoretic reduct/expansion formalism.

No exact literature match was found in the initial search for the specific structure \((\mathbb N_{>0},\times,\equiv_p)\) and its prime-orbit decomposition. This is **not yet a novelty claim**; a dedicated literature audit is required before publication.

## Immediate next strikes

1. Write and check the full proof of the one-modulus theorem.
2. Prove the finite-family theorem using CRT + Dirichlet.
3. Decide whether the semidirect-product splitting should be stated or only the exact sequence.
4. Define a useful quantitative individuality invariant on finite prime windows that does not depend on arbitrary truncation closure.
5. Investigate the infinite-family problem: characterize \(F\subseteq\mathbb P\) for which \(\mathcal M_F\) is rigid.
6. Test a single composite modulus \(m\): how many primes can one congruence relation \(\equiv_m\) individuate?

## Publication threshold

Not reached yet. HATTER-SOL-02 becomes publication-worthy if the finite-congruence theorem survives proof and literature audit, preferably together with either:

- an exact infinite-family rigidity criterion, or
- a nontrivial single-modulus classification / information-cost theorem.
