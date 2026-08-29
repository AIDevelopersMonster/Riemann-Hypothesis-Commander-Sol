# FCOA Foundation Citation Directive

**Issued:** 2026-08-29  
**Authority:** central FCOA scientific director  
**Applies to:** all central and delegated FCOA manuscripts, preprints, release packages, READMEs, citation metadata, and future branch publication instructions  
**Foundation version:** FCOA Definition 1.0  
**Foundation DOI:** PENDING ZENODO ASSIGNMENT

## Mandatory rule

Every paper that uses the FCOA framework must cite the canonical **FCOA Definition 1.0** article in **two places**:

1. **Abstract / Аннотация** — the abstract must explicitly state that the paper works in the Fixed-Carrier Oriented Algebra (FCOA) framework and must include the Foundation DOI once it is assigned.
2. **Bibliography / Литература** — the full Foundation article must appear as a bibliographic entry.

This applies even when the paper studies only one specialized reduct or extension such as rigidity cost, nesting, infinite memory, hybrid memory, branch passports, arithmetic leakage, admissibility geometry, or value-fiber geometry.

## Required abstract wording

### English template

> We work in the framework of Fixed-Carrier Oriented Algebra (FCOA), as fixed in the foundational Definition 1.0 article [Foundation DOI]. In this paper we study the following concrete FCOA reduct/extension: ...

The wording may be adapted for style, but the abstract must retain all three facts:

- this is an FCOA paper;
- the Foundation article is the source of the framework definition;
- the DOI is given explicitly.

### Russian template

> Работа выполнена в рамках ориентированной алгебры фиксированного носителя (Fixed-Carrier Oriented Algebra, FCOA), зафиксированной в базовой статье Definition 1.0 [Foundation DOI]. В настоящей работе исследуется следующий конкретный reduct/extension FCOA: ...

Формулировку можно стилистически менять, но в аннотации обязательно должны остаться три пункта:

- работа относится к FCOA;
- определение рамки берется из Foundation article;
- DOI Foundation article указан явно.

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

Until Zenodo assigns the DOI, use a placeholder only in working drafts:

> Malachevsky, A. *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*. Version 1.0, 2026. Zenodo. DOI: [FOUNDATION DOI PENDING].

After DOI assignment, placeholders are forbidden in release candidates.

Russian bibliographies may use the Russian title, but the DOI and version must be identical.

## Relationship to the earlier Admissibility Geometry paper

The existing paper

> Malachevsky, A. *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier*. Zenodo, 2026. DOI: `10.5281/zenodo.22129787`.

is **not replaced** by the Foundation article.

Citation roles are now separated:

- cite **FCOA Definition 1.0** for the meaning of the FCOA framework, its typed partial-algebra conventions, canonical carrier, M0 baseline, terminal outputs, arithmetic firewall, and carrier-erasure reduct;
- cite **Admissibility Geometry 10.5281/zenodo.22129787** when using the concrete `M0 -> G1 -> G2` theorem chain, Domain Compilation theorem, or associated audited invariants.

A paper may and often should cite both.

## Release gate

A new FCOA manuscript is **not publication-ready** if either of the following is missing:

- Foundation citation with DOI in the abstract;
- Foundation bibliographic entry.

The release audit must also check that the body identifies the exact FCOA object used rather than saying only “in FCOA”.

## Instructions to delegated directions

The scientific supervisors of:

- SOL-RIGIDITY;
- SOL-INFINITY;
- SOL-HYBRID;
- SOL-PASSPORT;
- SOL-NESTING;

must apply this directive to every new publication package and to any unpublished manuscript currently being prepared.

Already published archival versions are not silently rewritten. If they receive a new version/revision, the Foundation citation must be added in that revision.

## DOI propagation after Zenodo assignment

Immediately after the Foundation DOI is assigned, update:

1. `papers/FCOA-FOUNDATION-1.0/README.md`;
2. this directive;
3. the Foundation publication metadata/CITATION file;
4. the central FCOA README and state/publication index;
5. every queued central FCOA manuscript;
6. every queued delegated FCOA manuscript;
7. all branch publication instructions that contain citation requirements.

The DOI must be copied exactly and should use the persistent form `https://doi.org/<DOI>` in metadata where a URL is expected.
