# FCOA Nesting & Atomicity

Publication-ready bilingual companion for:

**Alex Malachevsky, “Reflections on Sandbox Atomicity with Commander Sol: Composition Boundaries, Nesting Rank, and Quotient Safety.”**

Russian title:

**«Размышлизмы о sandbox-атомарности с Commander Sol: границы композиции, ранг вложенности и безопасные quotient-отождествления».**

- Author: Alex Malachevsky
- ORCID: `0009-0008-6009-3196`
- Status: **PUBLICATION_READY** after hostile audit, prior-art repair, bilingual compile, and PDF render inspection
- Date: `2026-08-28`
- DOI: **not assigned yet** — assign only at Zenodo deposit
- Branch: `director/fcoa-nesting-atomicity`
- Upstream FCOA checkpoint: `10.5281/zenodo.22129787`

## Canonical publication files

- `manuscript_en.tex` — final English manuscript.
- `manuscript_ru.tex` — final Russian manuscript with the same theorem package and claim ceiling.
- `references.bib` — verified bibliography / archival bibliography source.
- `PRIOR_ART_AUDIT.md` — novelty and terminology firewall.
- `PUBLICATION_AUDIT.md` — final mathematical, bibliography, metadata, compile, and render audit.
- `RELEASE_CHECKLIST.md` — Zenodo/GitHub release gates.

Interactive demonstrator:

- `../../demos/fcoa-nesting-atomicity/index.html`

The older `manuscript.tex` is a pre-bilingual publication draft and is not the canonical release source.

## Main theorem package

The paper fixes a typed composition sandbox

\[
\mathfrak S=(X,\Omega,U)
\]

and defines bilateral `U`-atomicity by absence of two-sided nontrivial incoming composition witnesses.

The induced factor relation satisfies

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

## Demonstration scope

The HTML demonstrator visualizes four finite witnesses:

1. a basic acyclic sandbox in which atoms are exactly indegree-zero factor vertices;
2. a minimal cyclic SCC with no atoms;
3. result-fiber contamination destroying an atom under quotient identification;
4. triviality collapse creating an atom when triviality reflection fails.

The demo illustrates the finite mechanisms proved in the paper; it is not used as evidence for the theorems.

## Claim boundary

The publication does **not** claim novelty for partial algebras or strong congruences, ordinary monoid atoms/irreducibles, SCC condensation, ordinal rank of well-founded relations, bounded/p-morphisms, or transfer homomorphisms.

The contribution is the assembled FCOA-specific partial-composition boundary analysis and the exact local/global/well-founded/quotient distinctions proved in the manuscripts.

Research-development source files remain under:

`delegated/FCOA_NESTING_ATOMICITY/`

The publication folder is the cleaned release surface; exploratory terminology that failed hostile audit should not be reintroduced into the final article.