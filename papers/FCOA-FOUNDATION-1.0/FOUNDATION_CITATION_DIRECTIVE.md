# FCOA Foundation Citation Directive

**Issued:** 2026-08-29  
**Authority:** central FCOA scientific director  
**Applies to:** all central and delegated FCOA manuscripts, preprints, release packages, READMEs, citation metadata, and future branch publication instructions  
**Foundation version:** FCOA Definition 1.0  
**Foundation DOI:** https://doi.org/10.5281/zenodo.22164246

## Mandatory rule

Every paper that uses the FCOA framework must cite the canonical **FCOA Definition 1.0** article in **two places**:

1. **Abstract / Аннотация** — the abstract must explicitly state that the paper works in the Fixed-Carrier Oriented Algebra (FCOA) framework and must explicitly include `https://doi.org/10.5281/zenodo.22164246`.
2. **Bibliography / Литература** — the full Foundation article must appear as a bibliographic entry with DOI `10.5281/zenodo.22164246`.

This applies even when the paper studies only one specialized reduct or extension such as rigidity cost, nesting, infinite memory, hybrid memory, branch passports, arithmetic leakage, admissibility geometry, or value-fiber geometry.

## Required abstract wording

### English template

> We work in the framework of Fixed-Carrier Oriented Algebra (FCOA), as fixed in the foundational Definition 1.0 article, https://doi.org/10.5281/zenodo.22164246. In this paper we study the following concrete FCOA reduct/extension: ...

The wording may be adapted for style, but the abstract must retain all three facts:

- this is an FCOA paper;
- the Foundation article is the source of the framework definition;
- the DOI `https://doi.org/10.5281/zenodo.22164246` is given explicitly.

### Russian template

> Работа выполнена в рамках ориентированной алгебры фиксированного носителя (Fixed-Carrier Oriented Algebra, FCOA), зафиксированной в базовой статье Definition 1.0, https://doi.org/10.5281/zenodo.22164246. В настоящей работе исследуется следующий конкретный reduct/extension FCOA: ...

Формулировку можно стилистически менять, но в аннотации обязательно должны остаться три пункта:

- работа относится к FCOA;
- определение рамки берется из Foundation article;
- DOI `https://doi.org/10.5281/zenodo.22164246` указан явно.

## Required framework paragraph in the body

Every paper must contain a short section or paragraph equivalent to:

**FCOA framework and concrete structure used in this paper**

and it must identify:

1. active carrier;
2. auxiliary/output sorts;
3. primitive signature actually used;
4. exact changes relative to canonical M0 or another explicitly cited baseline;
5. whether the external orientation is retained or erased;
6. the recovery notion used in the paper (finite reconstruction, computable recovery, FO definability, interpretation, etc.);
7. whether external arithmetic is used in generation or only in metamathematical verification.

## Bibliographic entry

### English

> Malachevsky, A. *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*. Version 1.0, 2026. Zenodo. DOI: 10.5281/zenodo.22164246. https://doi.org/10.5281/zenodo.22164246

### Russian

> Malachevsky, A. *Ориентированная алгебра фиксированного носителя (FCOA): определение, типизированные частичные операции, стирание ориентации и каноническая база M0*. Версия 1.0, 2026. Zenodo. DOI: 10.5281/zenodo.22164246. https://doi.org/10.5281/zenodo.22164246

Russian bibliographies may retain the English title if that is the journal style, but the DOI and version must be identical.

## Relationship to the earlier Admissibility Geometry paper

The existing paper

> Malachevsky, A. *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier*. Zenodo, 2026. DOI: `10.5281/zenodo.22129787`.

is **not replaced** by the Foundation article.

Citation roles are now separated:

- cite **FCOA Definition 1.0**, DOI `10.5281/zenodo.22164246`, for the meaning of the FCOA framework, its typed partial-algebra conventions, canonical carrier, M0 baseline, terminal outputs, arithmetic firewall, and carrier-erasure reduct;
- cite **Admissibility Geometry 10.5281/zenodo.22129787** when using the concrete `M0 -> G1 -> G2` theorem chain, Domain Compilation theorem, or associated audited invariants.

A paper may and often should cite both.

## Release gate

A new FCOA manuscript is **not publication-ready** if either of the following is missing:

- `https://doi.org/10.5281/zenodo.22164246` in the abstract/аннотация;
- the Foundation bibliographic entry with DOI `10.5281/zenodo.22164246`.

The release audit must also check that the body identifies the exact FCOA object used rather than saying only “in FCOA”.

## Instructions to delegated directions

The scientific supervisors of:

- SOL-RIGIDITY;
- SOL-INFINITY;
- SOL-HYBRID;
- SOL-PASSPORT;
- SOL-NESTING;

must apply this directive to every new publication package and to any unpublished manuscript currently being prepared.

**Do not rewrite already published archival versions merely to add this citation.** If an already published work receives a new version/revision, the Foundation citation becomes mandatory in that new version.

## Canonical DOI propagation

The canonical FCOA Foundation DOI is now fixed as:

`https://doi.org/10.5281/zenodo.22164246`

All central and delegated publication instructions must use this exact persistent URL. No placeholder Foundation DOI is permitted in any new release candidate.