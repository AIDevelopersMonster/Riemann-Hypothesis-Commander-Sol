# FCOA-Z — Ray to Axis / Local Law Differentiation

## Work

**English:** Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears

**Russian:** Размышлизмы о том, как луч становится осью: И почему старые операции после появления второго направления обнаруживают новые локальные законы

**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Series:** Commander Sol / FCOA-Z  
**Version:** 1.1  
**Publication date:** 2026-08-30  
**Zenodo DOI:** 10.5281/zenodo.22171473  
**Persistent URL:** https://doi.org/10.5281/zenodo.22171473

The English and Russian PDFs are parallel language versions of one theorem package.

## Direct FCOA predecessors

1. *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier* — DOI `10.5281/zenodo.22129787`.
2. *Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers* — DOI `10.5281/zenodo.22160014`.

Programme progression:

`domain geometry / recoverable structural memory -> value-rigidity / sparse rigid fibers -> reversible carrier / local-law differentiation`

## Theorem nucleus

Starting from a rooted discrete ray with one-sided successor and a legacy role-sensitive partial FCOA operation, the paper proves:

- the minimal reversible completion is a unique bi-infinite pointed orbit;
- the completed orbit carries a unique derived reflection about the root;
- a reflection-equivariant legacy-preserving extension radializes the legacy predecessor-like right-zero action into punctured contraction toward the root;
- noncommutativity survives;
- a second legacy operation exhibits a distinct absorber/transverse-port geometry;
- after the full nonnegative legacy substructure and output reflection involution are fixed, every remaining independent binary base choice is localized to opposite-sign sectors.

The published paper does **not** claim canonical mixed-sign values, recovery of ordinary signed addition/multiplication, forced global commutativity/associativity, or a physical-space model.

## Post-publication research continuation

The mixed-sector frontier identified by the publication has now been advanced through four internal theorem packages.

### 1. Mixed Radial Cancellation Generator

See [`MIXED_RADIAL_CANCELLATION_GENERATOR.md`](MIXED_RADIAL_CANCELLATION_GENERATOR.md).

A single non-tabular rule is imposed: for opposite-sign inputs, contract both arguments synchronously toward the root until the first inherited zero-port boundary is reached, then evaluate through the already-existing FCOA boundary cell.

Consequences proved there:

- existence and uniqueness relative to the radial-cancellation axiom;
- reflection compatibility;
- exact mixed-domain/output formula;
- adjacent-output noncommutation: swapping arguments changes the output by exactly one radial edge whenever depths are unequal;
- an exact root-right association phase law;
- realization of all five FCOA association statuses `EQ / NEQ / LEFT / RIGHT / NONE` without a hand-written triple table.

The cancellation mechanism itself has classical relatives, especially bicyclic shift/inverse-shift normal forms. The FCOA-Z claim is restricted to the interaction between that reduction and the inherited asymmetric zero ports.

### 2. Classification of Inward-Covariant Mixed Generators

See [`MIXED_GENERATOR_CLASSIFICATION.md`](MIXED_GENERATOR_CLASSIFICATION.md).

The mixed-sector classification is exact inside the inward-covariant class:

\[
F=\beta\circ N,
\]

where `N` is the unique first-boundary radial normal form and `beta` is the boundary trace. Therefore every inward-covariant mixed extension is completely determined by its reachable zero-port boundary values.

If the inherited FCOA boundary is preserved, `beta` is fixed, hence the mixed extension is unique. The candidate five-axiom package compresses to three essential ingredients:

1. signed FCOA-Z carrier with radial contraction;
2. simultaneous inward covariance;
3. inherited zero-port boundary preservation.

Within this class, boundary locality, uniqueness, and reflection compatibility are consequences rather than additional axioms.

### 3. Finite-State Mixed Transport / First Memory Threshold

See [`MIXED_FINITE_STATE_TRANSPORT.md`](MIXED_FINITE_STATE_TRANSPORT.md).

Weakening exact inward covariance by allowing output transport reveals a sharp hierarchy. A phase clock

\[
\varepsilon:\mathbb N_0\to\mathbb Z_2,\qquad \varepsilon(0)=0,
\]

gives

\[
F_\varepsilon(z)=\nu^{\varepsilon(k(z))}\beta(N(z)),
\]

where `k(z)` is cancellation depth.

Main results:

- unrestricted phase clocks give `2^{aleph_0}` distinct reflection-equivariant mixed operations with the same inherited boundary and mixed domain;
- the old mixed commutation status and both root-association phase diagrams are blind to this phase freedom;
- a new value-phase invariant `Pi_F` recovers the hidden phase exactly;
- the rooted radial carrier has automorphism group exactly `{id, nu} ~= C_2`;
- therefore the unique nontrivial homogeneous geometric transport is reflection;
- the first finite-state memory threshold is two states = one bit, giving the parity clock `epsilon(k)=k mod 2`;
- finite-state unary phase clocks are exactly the ultimately periodic phase sequences.

This produces the hierarchy

`rigid normal form -> one-bit geometric phase -> finite-state phase hierarchy -> continuum phase freedom`.

### 4. Phase Locality: Collapse and Non-Collapse

See [`PHASE_LOCALITY_COLLAPSE_THEOREMS.md`](PHASE_LOCALITY_COLLAPSE_THEOREMS.md).

The next question was which local identities actually force the hidden phase hierarchy to collapse. The answer depends not on locality alone but on **persistent branching**.

Main results:

- a finite forbidden-pattern rule need not imply finite-state behavior; forbidding only `11` already permits continuum many phase clocks, including continuum many aperiodic clocks;
- a finite-type local rule forces every phase clock to be ultimately periodic iff every reachable recurrent component of its finite block graph is a simple directed cycle;
- every deterministic bounded-window recurrence forces ultimate periodicity, hence collapses `M_infty -> M_FS`;
- exact `r`-step inward covariance forces eventual period dividing `r`;
- twisted one-step covariance `F(z)=nu F(Cz)` uniquely selects the parity phase;
- reversible one-bit dynamics gives only zero phase or parity phase.

The conceptual boundary is therefore

\[
\boxed{\text{local admissibility} \neq \text{local determinism}.}
\]

Persistent local choice is the first source of unbounded mixed memory.

## Current state of the branch

The original post-publication questions are now answered at four successive levels:

1. **Does a natural non-tabular mixed generator exist?** — yes.
2. **Is it canonical under exact inward covariance?** — yes; `F = beta o N` and legacy boundary fixes `beta`.
3. **What is the first degree of freedom beyond exact covariance?** — one cancellation-depth `Z_2` phase bit.
4. **When does local phase information remain bounded?** — deterministic finite-window laws force finite state; merely local admissibility can retain continuum aperiodic freedom.

## Active frontier

The scalar `Z_2` phase branch is now substantially classified. The mathematically distinct next strike is to return to the second legacy operation `otimes`, whose right-zero boundary values may leave the base carrier and enter terminal fibers.

The key question is:

\[
\boxed{\text{what is the output-transport symmetry group of the terminal }E^*\text{-fibers?}}
\]

If that group is larger than `C_2`, the first mixed-memory law for `otimes` may be a genuinely group-valued cocycle rather than a single reflection bit. A non-Abelian terminal-fiber symmetry would open an even stronger branch: noncommuting transport phases generated by carrier interaction.

A secondary independent frontier remains the replacement of the two-ray axis by rooted trees, where branch information survives radial cancellation.

## Archival notes

The supplied 15-page v1.1 manuscripts are preserved as the article body. The Zenodo publication PDFs add two unnumbered front-matter pages for author/ORCID, programme context, direct FCOA predecessor citations, notation clarification, and AI-assistance disclosure. Reference 1 was corrected from `C-method*` to the published title `C*-method`. No theorem, proof, equation number, or claim boundary was otherwise changed.

See `PREPUBLICATION_AUDIT.md`, `RELATED_FCOA_WORKS.md`, `zenodo_metadata.json`, and `CITATION.cff` for the release record.