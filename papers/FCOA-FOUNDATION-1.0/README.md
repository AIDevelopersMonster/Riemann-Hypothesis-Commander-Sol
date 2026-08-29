# FCOA Foundation 1.0

**Publication status:** READY FOR ZENODO DEPOSIT  
**Version:** 1.0.0  
**Date:** 2026-08-29  
**Creator:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Foundation DOI:** pending Zenodo assignment

## English title

**Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline**

## Russian title

**Ориентированная алгебра фиксированного носителя (FCOA): определение, типизированные частичные операции, стирание ориентации и каноническая база M0**

## Role in the publication series

This is the normative **FCOA Definition 1.0** publication. It separates:

1. `FCOA` — the class/framework;
2. `M0` — the canonical typed partial-algebra baseline;
3. `G1/G2/G3/G4`, nesting, rigidity, infinite-memory and arithmetic-leakage systems — concrete extensions or reducts used by later papers.

The existing publication

**Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier**, DOI `10.5281/zenodo.22129787`,

remains the theorem paper for the concrete `M0 -> G1 -> G2` chain. The present foundation has a different role: it is the canonical source for the meaning of FCOA itself.

## Core definition

The natural formal envelope is

\[
\boxed{\text{many-sorted partial algebra} + \text{oriented carrier presentation} + \text{carrier-erasure reduct}.}
\]

An oriented FCOA presentation is

\[
\mathfrak F^{\mathrm{or}}=(B,\preceq;O_1,\ldots,O_t;\Omega),
\]

with partial operation symbols such as

\[
\omega:B\times B\rightharpoonup B\sqcup O_1\sqcup\cdots\sqcup O_t.
\]

The carrier-erased operational reduct is

\[
\mathfrak F^\circ=(B;O_1,\ldots,O_t;\Omega).
\]

The canonical line uses `B = N_0`, written structurally as `P_0,P_1,...`, but ordinary natural addition and multiplication are not part of the FCOA signature unless separately introduced or internally recovered.

FCOA is **not a semigroup by definition**: totality, closure on one sort, associativity, commutativity, distributivity, inverses, cancellation and neutral elements are not assumed.

## Canonical backend documents

The publication is distilled from the already maintained main-line specifications:

- `../FCOA-ADMISSIBILITY-GEOMETRY/FCOA_DEFINITION_1_0.md`
- `../FCOA-ADMISSIBILITY-GEOMETRY/FCOA_FOUNDATIONAL_SPECIFICATION.md`

These backend documents remain useful for the research programme, but the Zenodo foundation is the citable archival Definition 1.0.

## Mandatory citation rule after DOI assignment

Every FCOA publication — central or delegated — must:

1. mention the Foundation article and its DOI in the **abstract** whenever the paper uses the FCOA framework;
2. include the Foundation article as a full entry in the **bibliography/references**;
3. include a short section or paragraph titled `FCOA framework and concrete structure used in this paper` (or a direct equivalent), specifying carrier, sorts, primitive signature, changes relative to M0, erasure convention, and recovery notion;
4. cite the older Admissibility Geometry DOI separately only when its specific M0/G1/G2 theorems are used.

The exact branch-wide directive is stored in `FOUNDATION_CITATION_DIRECTIVE.md`.

## Deposit package

The Zenodo upload package consists of bilingual PDF and DOCX manuscripts plus source Markdown and metadata. The DOI field is intentionally left pending until Zenodo assigns the record DOI. Immediately after assignment, the DOI must be inserted here, in the citation directive, the FCOA main README/CITATION metadata, and all queued FCOA manuscripts.