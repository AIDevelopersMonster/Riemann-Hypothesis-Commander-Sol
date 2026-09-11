# HATTER-SOL-05 · RESEARCH STATE

## Working title

**«Кого нет за столом? Пустые волокна, спектр точных опор и выживание перестановки 3↔5»**

English:

**“Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the 3↔5 Swap.”**

## Core structure

\[
\Pi=(\mathbb P,D),\qquad D(q,p)\iff q\mid p-1.
\]

Exact predecessor fibers:

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Primary seed symmetry:

\[
\tau=(3\ 5),
\qquad
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

The central unresolved problem remains

\[
\boxed{\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}.}
\]

HATTER-SOL-05 does not claim to solve this yes/no problem.

## What is now proved

1. **Finite fixed-divisor escape.** No exact-support candidate family can be covered by a fixed finite set of prime divisors.

2. **Cyclotomic dimension barrier.** If \(1+\prod q_i^{e_i}\) is prime, then \(\gcd(e_1,\ldots,e_k)\) is a power of two. The singleton case collapses to Fermat-type exponents; every fixed dimension \(k\ge2\) retains positive admissible density
   \[
   \frac1{\zeta(k)(1-2^{-k})}.
   \]

3. **Local sieve asymmetry.** For the first paired supports,
   \[
   \{2,3\}:\frac6{\pi^2},
   \qquad
   \{2,5\}:\frac4{\pi^2},
   \]
   giving exact first-sieve ratio \(3/2\).

4. **Weighted numerical asymptotics.** With a complete Möbius/lattice proof,
   \[
   A_{23}(X)
   =\frac{3}{\pi^2\log2\log3}(\log X)^2+O((\log X)\log\log X),
   \]
   \[
   A_{25}(X)
   =\frac{2}{\pi^2\log2\log5}(\log X)^2+O((\log X)\log\log X).
   \]

5. **Hereditary descendant gap.** The \(3/2\) local survival ratio persists along 3-pure exact-descendant chains.

6. **Cardinality wall.** Quantitative asymptotic differences become invisible to the multiplicity tower once paired exact fibers are both infinite, because both cardinalities equal \(\aleph_0\).

7. **Finite-fiber compactness.** Under FFC, survival to every finite Pratt height is equivalent to global survival. Global death therefore occurs at a finite height and is represented by a finite structural obstruction family/tree.

8. **Density-one forward cone.** For every odd prime \(a\),
   \[
   d_{\mathbb P}(C^+(a))=1.
   \]
   In fact the directed future at distance at most two already has relative prime density one.

9. **Causal survival.** Under CFI\((g_1)\), a first-layer seed permutation extends globally and may be chosen to fix every prime outside its generated forward cone.

## Correct obstruction language

At the immediate next level, a single mismatch

\[
\mu(S)\ne\mu(\tau S)
\]

can kill the seed transposition.

At later levels this is generally insufficient as a universal formulation because previous extension choices branch. The correct object is a finite obstruction family/tree blocking all surviving partial extensions.

## Hostile-audit repairs completed

The following publication-gate repairs are now incorporated into canonical source notes:

- generated-cone scope correction for the causal localization lemma;
- explicit distance-two density-one corollary;
- full weighted asymptotic proof replacing the earlier sketch;
- descendant no-go theorem narrowed to levelwise finite fixed-divisor covers;
- \(\mathfrak P\) explicitly identified as external bookkeeping, not a joint density or graph invariant;
- finite certificate explicitly identified as structural, not algorithmic;
- terminology corrected from “generator” to “transposition/element”;
- continuity bridge corrected from a universal single-witness formulation to obstruction-tree language.

## Literature boundary

The 2012 MathOverflow discussion by David Feldman and Gjergji Zaimi already recognized this directed prime graph and exact incoming-predecessor classes as central to the automorphism problem. HATTER-SOL-05 therefore does not claim priority for the exact-support architecture itself or for the broad idea that large fibers favor symmetry while distinguishing finite fibers may enforce rigidity.

Classical analytic and combinatorial ingredients are credited as such. The publication contribution is the assembled theorem package and its precise interaction with the multiplicity tower.

## Publication threshold

\[
\boxed{\textbf{REACHED.}}
\]

Decision after hostile proof/literature audit:

\[
\boxed{\textbf{REPAIR}\to\textbf{FREEZE v1.0}\to\textbf{ASSEMBLE ARTICLE}.}
\]

The repair pass has now been executed on the core canonical notes. No additional research strike is required before assembling the fifth article.

## Next research target after v1.0

Do not delay HATTER-SOL-05 for this.

Open HATTER-SOL-06 around the sharper question:

\[
\boxed{
\text{replace cone-wide CFI by the minimal orbitwise support condition actually required for survival.}
}
\]

A second possible strike is an arithmetic attack inside the causal cone: find an exact support meeting \(C_\tau\) whose fiber can be proved empty or finite.
