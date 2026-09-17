# Prior-Art and Claim Audit — FCOA Nesting & Atomicity

**Date:** 2026-08-28  
**Branch:** `director/fcoa-nesting-atomicity`  
**Status:** publication hardening

## 1. Audit conclusion

The mathematical core survives the prior-art audit, but the novelty boundary must be stated conservatively.

The paper must **not** claim novelty for:

1. partial algebras, partial operations, ordinary/strong congruences, or quotient partial algebras;
2. atoms/irreducibles in ordinary monoids or classical factorization theory;
3. ordinal rank of a well-founded binary relation;
4. bounded morphisms / p-morphisms and their forth/back clauses;
5. transfer homomorphisms or factorization lifting in monoid theory;
6. strongly connected components or condensation DAGs.

The publishable contribution is instead the assembled FCOA-specific theory obtained after fixing a typed partial-composition sandbox and a declared trivial class `U`:

- a directional decomposition language for arbitrary partial noncommutative sandboxes;
- the nontrivial factor relation extracted directly from allowed operation cells;
- the exact minimal-SCC criterion separating local atoms from global nesting boundary;
- terminal-value-fiber invariance of active-result atomicity, separating atomicity from FCOA rigidity memory;
- exact quotient atom criterion under ordinary existential quotient semantics;
- the fiberwise universal criterion under triviality reflection;
- explicit counterexamples showing that ordinary quotient identification can both destroy and create atomhood;
- application of a standard bounded-morphism back condition to the factor frame to give a transparent sufficient contract for exact preservation of well-founded factor rank and atomhood.

No claim of priority is made for the standard ingredients separately.

## 2. Partial algebra and quotient background

George Grätzer's *Universal Algebra*, Chapter 2, treats partial algebras, homomorphisms, congruences, strong congruences, and quotient partial algebras. Grätzer and Wenzel (1967) explicitly distinguish ordinary congruences from strong congruences for partial algebras.

Therefore the manuscript uses the established terminology `ordinary congruence` and `strong congruence` where applicable. The FCOA quotient counterexamples are not presented as discovering the distinction between weak and strong partial-algebra quotients.

### Citation anchors

- G. Grätzer, *Universal Algebra*, 2nd ed., Springer, 1979; DOI `10.1007/978-0-387-77487-9`.
- G. Grätzer and G. H. Wenzel, “On the Concept of Congruence Relation in Partial Algebras,” *Mathematica Scandinavica* 20 (1967), 275–280.

## 3. Well-founded rank

The recursion

\[
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}
\]

for a well-founded relation is standard set theory. The manuscript therefore labels the existence/uniqueness of ordinal rank as classical background and claims only the branch-specific identification

\[
x\text{ is a }U\text{-atom}\iff \rho(x)=0
\]

for the factor relation induced by the sandbox.

Reference anchor:

- Thomas Jech, *Set Theory: The Third Millennium Edition, Revised and Expanded*, Springer, 2003; DOI `10.1007/3-540-44761-X`.

## 4. Bounded morphisms and the CPL repair

The branch originally introduced `Coherent Predecessor Lifting (CPL)` as a quotient condition. Prior-art review shows that, after passing from the partial operations to the binary factor relation, CPL is exactly the standard **back condition** of a bounded morphism / p-morphism of relational frames. Forward factor preservation supplies the corresponding forth condition.

Accordingly:

- `CPL` may remain an internal mnemonic;
- the publication must call the standard object a **bounded morphism of factor frames**;
- no novelty claim is made for the morphism notion itself.

Reference anchor:

- Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge University Press, 2001; DOI `10.1017/CBO9781107050884`, especially the treatment of bounded morphisms in the early model/frame chapters.

The exact rank-preservation proof is retained because it gives a short explicit application of the standard forth/back clauses to this factor relation.

## 5. Transfer-homomorphism comparison

Classical factorization theory contains a stronger lifting paradigm. A transfer homomorphism of monoids requires, among other things, lifting factorizations of an image element to factorizations of the source element up to associates. This is stronger and richer than the one-step relational predecessor lifting used here.

The paper therefore says only that factor-frame bounded morphisms are **analogous in purpose** to transfer principles: both prevent factor structure from being fabricated by mapping, but they live at different levels.

Reference anchor:

- Alfred Geroldinger and Franz Halter-Koch, *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory*, Chapman & Hall/CRC, 2006; DOI `10.1201/9781420003208`, Section 3.2 on transfer principles.

## 6. Atom / irreducible terminology

In ordinary cancellative monoids with genuine units, `atom` and `irreducible` are standard closely related notions. The present sandbox permits partiality, multiple operations, typing, noncommutativity, terminal outputs, and an arbitrary declared class `U`; hence the manuscript does **not** import the ordinary monoid definition as universal.

The publication uses:

- `U-atom` for absence of a two-sided nontrivial incoming composition witness;
- `U-transport-irreducible` for the stricter one-`U` transport condition;
- `U-irreducible` only after an explicit `U`-coherence contract is imposed.

This is presented as a definition tailored to the sandbox setting, not as a redefinition of classical monoid irreducibility.

## 7. Novelty wording permitted in the manuscript

Safe formulations:

- “We introduce the following sandbox-relative terminology for this FCOA analysis.”
- “The main theorem identifies the exact graph-theoretic boundary between local atomicity and global nesting minimality.”
- “We give explicit quotient counterexamples and a factor-frame formulation that separates unsafe carrier identification from a standard bounded-morphism safety regime.”
- “The novelty claim concerns the assembled partial-composition boundary analysis, not the standard constituent theories.”

Avoid:

- “new theory of bounded morphisms”;
- “new definition of irreducible element” without qualification;
- “first ordinal rank for factorization”;
- “new quotient theory for partial algebras”;
- “generalization of unique factorization”;
- “primes are universally characterized by FCOA.”

## 8. Publication assessment

`PRIOR_ART_STATUS = PASS_WITH_CLAIM_NARROWING`.

No known source found in this audit duplicates the complete FCOA package as stated, but this is **not** a priority proof. The manuscript is suitable for Zenodo as a mathematically self-contained research note / “Reflections” article provided the conservative claim boundary above is preserved.