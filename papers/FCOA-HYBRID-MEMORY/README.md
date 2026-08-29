# FCOA Hybrid Memory — Article A

Publication companion for the release candidate:

**Alex Malachevsky, “Reflections on Hybrid Memory with Commander Sol: Minimal Joint Rigidity of Partial Operations.”**

Russian title:

**«Размышлизмы о гибридной памяти с Commander Sol: минимальная совместная жёсткость частичных операций».**

- Author: Alex Malachevsky
- ORCID: 0009-0008-6009-3196
- Version: 0.9.0-rc1
- Package date: 2026-08-29
- Intended resource type: Publication / Preprint
- License: CC BY 4.0
- Zenodo DOI: **pending reservation** — never substitute an invented DOI
- Repository: https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol

## Scope

Article A closes the finite **hybrid-memory / joint-rigidity** problem for partial operations. It studies structures in which neither operation reduct is rigid, but their joint reduct is:

\[
Aut(\star)\ne1,\qquad Aut(\diamond)\ne1,\qquad Aut(\star,\diamond)=1.
\]

The article separates three mechanisms:

1. **carrier-stabilizer transversality** — domains or independent value layers leave transverse residual carrier groups;
2. **joint fiber synchronization (JFS)** — a carrier symmetry survives both reducts but requires incompatible lifts on a shared terminal output sort;
3. **carrier–value selection (CVS)** — in a one-sorted partial algebra, operation values are themselves carrier points and act as selectors inside a residual orbit.

## Published theorem set in the release candidate

- sharp pure domain–domain cost: **2 cells**;
- typed Lift-Compatibility Theorem, including the non-surjective lift-set formulation;
- typed common-terminal genuine value-memory threshold: **3 tagged cells**, attained by JFS-3;
- smallest common-output active carrier: **2 active points**, with sharp cost **4 cells**;
- independent-output domain–value threshold: **4 = 1+3 cells**;
- independent-output separately value-sensitive value–value threshold: **6 = 3+3 cells**;
- unrestricted one-sorted absolute hybrid cell minimum: **2 cells**;
- one-sorted two-cell strong VV classification: no witnesses for n=2,3; for n=4, **24 labeled witnesses / 1 isomorphism class**;
- typed three-active-point, three-cell JFS classification: **48 labeled witnesses / 8 operation-preserving isomorphism classes**;
- scalable CVS selector ladder:
  \[
  S_{m+1}\to S_m\to\cdots\to S_2\to1.
  \]

Every non-enumerative theorem is proved in both language editions. The two finite classifications are accompanied by an exhaustive dependency-free verifier.

## Claim boundary

The article does **not** claim that stabilizer/equalizer/fiber-product ideas are new in abstract group theory. It does **not** claim that general symmetry breaking, distinguishing colorings, base size, or partial algebra are new subjects. The contribution is the exact partial-operation hybrid-memory formulation, the separation of output semantics, sharp thresholds, and the two value mechanisms JFS/CVS.

The article also does **not** infer order or arithmetic from finite rigidity. The later AL0/AL1/AL2, sparse-order, CRT, RTP and interpretation-invariance work belongs to **Article B / subsequent research** and is deliberately excluded from Article A.

## Package contents

- `article/FCOA_HYBRID_MEMORY_EN.tex` — canonical English source (inside the source bundle until final DOI build).
- `article/FCOA_HYBRID_MEMORY_RU.tex` — canonical Russian source (inside the source bundle until final DOI build).
- `release/FCOA_HYBRID_MEMORY_SOURCE_RC0.9.0.zip` — complete RC source/metadata bundle.
- `supplement/verify_minimal_classifications.py` — exhaustive verifier.
- `supplement/verification_output.txt` — expected verified output.
- `MATHEMATICAL_CORE.md` — theorem and proof ledger.
- `PUBLICATION_AUDIT.md` — publication-auditor report.
- `CITATION.cff` — citation metadata without fabricated DOI.
- `ZENODO_METADATA.json` — draft deposit metadata.
- `ZENODO_CHECKLIST.md` — final DOI/deposit procedure.
- `STATE.md` — continuity checkpoint.
- `WORKSPACE.md` — publication ownership boundary.
- `release/RELEASE_MANIFEST.md` — archival manifest and checksums.

The RC PDFs are generated publication artifacts. The final PDFs will be archived on Zenodo after DOI reservation and deterministic rebuild.

## Publication gate

Current gate: **REVIEWED_CLEAN — DOI reservation pending**.

Before publication, reserve the Zenodo DOI, replace the explicit “pending reservation” marker in both sources, rebuild both PDFs, rerun the verification script, render-check both PDFs, update `CITATION.cff`, `ZENODO_METADATA.json`, and the release manifest, then publish the Zenodo record.