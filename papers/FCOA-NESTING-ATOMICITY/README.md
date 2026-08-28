# FCOA Nesting & Atomicity

Publication-candidate companion for:

**Alex Malachevsky, “Reflections on Sandbox Atomicity with Commander Sol: Composition Boundaries, Nesting Rank, and Quotient Safety.”**

Russian working title:

**«Размышлизмы об атомарности в sandbox с Commander Sol: границы композиции, ранг вложенности и безопасные фактор-отображения».**

- Author: Alex Malachevsky
- ORCID: `0009-0008-6009-3196`
- Status: publication candidate after hostile audit and prior-art claim repair
- Date: 2026-08-28
- DOI: **not assigned yet**
- Branch: `director/fcoa-nesting-atomicity`
- Upstream FCOA checkpoint: `10.5281/zenodo.22129787`

## Main theorem package

The paper fixes a typed composition sandbox

\[
\mathfrak S=(X,\Omega,U)
\]

and defines bilateral `U`-atomicity by absence of two-sided nontrivial incoming composition witnesses.

The induced factor relation satisfies:

\[
\boxed{
\operatorname{Atom}(\mathfrak S,U)
\subseteq
\operatorname{MinNest}(\mathfrak S,U).
}
\]

Moreover,

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
}
\]

If the factor relation is well-founded, its classical ordinal rank obeys

\[
\boxed{x\text{ atomic}\iff\rho(x)=0.}
\]

For a triviality-reflecting ordinary quotient,

\[
\boxed{
q(x)\text{ atomic}
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Ordinary quotient identification can therefore destroy atomicity by result-fiber contamination; without triviality reflection it can also create atomicity by collapsing a formerly nontrivial factor into the quotient trivial class.

Finally, when the induced factor-frame map is a surjective bounded morphism (forth + back), the well-founded factor rank is preserved exactly:

\[
\boxed{\bar\rho(q(x))=\rho(x).}
\]

## Claim boundary

The publication does **not** claim novelty for:

- partial algebras or strong congruences;
- ordinary monoid atoms/irreducibles;
- SCC condensation;
- ordinal rank of well-founded relations;
- bounded/p-morphisms;
- transfer homomorphisms.

The contribution is the assembled FCOA-specific partial-composition boundary analysis and the exact finite/infinite/quotient distinctions proved in the manuscript.

## Files

- `manuscript.tex` — publication manuscript.
- `references.bib` — verified bibliography used by the manuscript.
- `PRIOR_ART_AUDIT.md` — novelty/terminology firewall.
- `PUBLICATION_AUDIT.md` — mathematical and release audit.
- `RELEASE_CHECKLIST.md` — final Zenodo/GitHub release gates.

Research-development source files remain under:

`delegated/FCOA_NESTING_ATOMICITY/`

The publication folder is the cleaned manuscript surface; exploratory terminology that failed hostile audit should not be reintroduced from older drafts.