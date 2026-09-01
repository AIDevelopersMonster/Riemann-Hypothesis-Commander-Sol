# Article B — Publication Audit Ledger

**Audit date:** 2026-09-01  
**Status:** MATHEMATICAL CORE CONDITIONALLY READY; MANUSCRIPT ASSEMBLY STILL REQUIRED

Severity scale: `C0` fatal, `C1` major, `C2` moderate, `C3` minor.

## Executive verdict

Article B has a coherent publishable mathematical core after quarantine of several exploratory claims. The canonical result is not the old CF/RTP resource hierarchy. It is the standard relational preprocessing story:

\[
\boxed{\text{unrestricted fixed-rank FO preprocessing collapses to linear storage}}
\]

but

\[
\boxed{\text{near-linear exact addition by one CQ has exact variable-width threshold }9.}
\]

The Article B theorem spine is recorded in `ARTICLE_B_THEOREM_DEPENDENCY_GRAPH.md`.

## Findings

### C0-01 — CF AL0 lower bound invalid under stated cost measure — FIXED BY QUARANTINE

File: `COMPOSITIONAL_FACTORISATION_PHASE_THEOREM.md`.

Former proof counted only bottom records and assumed two bottom symbols untouched there remained globally exchangeable. Uncounted target/factorisation attachments can distinguish them. `HM-CF-ORD-LOW` and derived `HM-CFPT` were withdrawn.

### C0-02 — bounded-depth AL0 order package used successor as if FO transitive closure were available — FIXED BY QUARANTINE

File: `BOUNDED_DEPTH_RESOURCE_SEPARATION.md`.

A growing successor chain does not by itself give a uniformly FO-definable total order. The same file also inherited the target-attachment symmetry issue. `HM-BDRS` was withdrawn from the publication theorem chain.

### C1-01 — AL0/AL1/AL2 definitions were implicit and model-dependent — FIXED

Created `ARTICLE_B_CANONICAL_DEFINITIONS.md`.

Article B now uses canonical target-sector benchmarks:

\[
B_0=([N],<),\quad
B_1=([N],<,Add_N),\quad
B_2=([N],<,Add_N,Mul_N).
\]

Target recovery is explicitly distinguished from arithmetic interpretability on another quotient/sector.

### C1-02 — RTP profile was presented too strongly — FIXED

File: `RESOLUTION_TRANSPORT_PHASE_BOUNDARY.md`.

The AM--GM/direct-defect calculation survives only in the flat complete-table direct-CRT normal form. `rho(AL2)=2` is not intrinsic because digit/radix factorisation collapses direct resolution. RTP is now historical calibration only.

### C1-03 — endpoint-based internal-law memory was superseded but still looked live — FIXED

File: `LINEAR_INTERPRETATION_RESOURCE_THEORY.md`.

BF1 composition survives. The proposed `M_int` separator is explicitly withdrawn because of target hosting and arbitrarily wide fixed radix factorisation.

### C1-04 — single CQ conflated with existential-positive finite-variable FO — FIXED

File: `EXISTENTIAL_PEBBLE_WIDTH_SEPARATION.md`.

A single CQ is primitive-positive. Existential-positive FO permits finite disjunctions of CQs. The theorem is now stated only for one CQ; pebble-game language is background, not a proof dependency.

### C1-05 — CQ width-9 file contained an internal tool citation token and insufficient benchmark scoping — FIXED

File: `CQ8_EXACT_THRESHOLD.md`.

The internal citation token was removed. The target benchmark, storage model, CQ-only scope, repaired positive-core proof, and AL2 benchmark convention are now explicit.

### C1-06 — FO preprocessing file included an unaudited quantifier-free endpoint — FIXED BY QUARANTINE

File: `FO_PREPROCESSING_FRONTIER_COLLAPSE.md`.

The publication theorem now contains only the audited eventual-linear result HM-FOPC. The former `sigma_j(0)=2` endpoint is explicitly excluded pending a separate proof audit.

### C2-01 — direct CRT four-channel minimality needed constant-sensitive wording — FIXED IN CANONICAL INTERPRETATION

Exponent counting gives `k>=4` in the equal-scale direct-CRT template. At `k=4`, exactness depends on choosing sufficiently large constant multiples of `sqrt N`; one must not derive sufficiency from the exponent inequality alone. The RTP quarantine file records this.

### C2-02 — Article B had no single theorem dependency graph — FIXED

Created `ARTICLE_B_THEOREM_DEPENDENCY_GRAPH.md`.

### C2-03 — historical exploratory files can still contain obsolete statements — OPEN BUT CONTAINED

Not every research notebook in the branch has been rewritten. The canonical definitions, audit ledger, dependency graph, and explicit quarantine stubs now determine publication status. Before release, the final manuscript must cite only canonical files or clearly label historical no-go material.

### C2-04 — CQ positive-core theorem deserves one more independent proof pass in manuscript form — OPEN

The repaired width-9 proof survived the current hostile audit, but because it is the principal novel theorem, the final LaTeX manuscript should restate every entropy/conditioning lemma with explicit probability distributions and asymptotic quantifiers. This is a manuscript-hardening task, not a known mathematical contradiction.

### C2-05 — prior-art novelty search must be finalized — OPEN

Current calibration includes entropy bounds for CQs with FDs, factorised representations, finite-variable logic, and database preprocessing. Before Zenodo release, run a focused literature search for lower bounds specifically on representing finite group/quasigroup operation graphs by bounded-variable conjunctive queries with preprocessing. Novelty should be stated conservatively unless no direct predecessor is found.

### C3-01 — notation normalization — OPEN

Final manuscript must use one notation consistently for `Add_N`, `Mul_N`, `sigma_j^{CQ}(k)`, `k_+`, target sector, and storage. Avoid switching among `Cost`, `M`, `M_tot`, and `S` unless models are explicitly separated.

### C3-02 — references/DOIs — OPEN

Final bibliography must verify titles, author names, years, DOI strings, and current 2026 references. No internal search/tool citation markers may appear in source.

## Canonical theorem set after audit

Publication-positive:

1. explicit linear-size CRT addition construction;
2. explicit linear-size multiplication constructions;
3. `HM-FOPC`: eventual linear storage exponent for AL0/AL1/AL2 under unrestricted fixed-rank FO preprocessing;
4. CQ width-3 order/addition separation;
5. quantitative `CQ^6` lower bound `sigma_1^{CQ}(6)>=7/6` (optional, subject to manuscript restatement);
6. `HM-CQ-EXACT`: exact near-linear addition width `k_+=9`;
7. AL2 width corollary `k_{AL2}=9` under the canonical benchmark convention;
8. BF1 composition and the documented no-go sequence as background.

Excluded/quarantined as positive theorems:

- `HM-BDRS`;
- `HM-CFPT` and `HM-CF-ORD-LOW`;
- RTP as intrinsic;
- endpoint-based `M_int` separation;
- quantifier-free `sigma_j(0)=2` endpoint until separately audited;
- any statement identifying one CQ with the entire existential-positive fragment.

## Publication decision

**Do not release Article B yet.**

The mathematical architecture is now coherent enough to begin final manuscript assembly, but publication requires:

1. a fresh English/Russian manuscript built only from the canonical theorem graph;
2. one final hostile proof reread of HM-CQ-EXACT in manuscript notation;
3. focused prior-art/novelty search;
4. bibliography/DOI audit;
5. formula/theorem numbering audit;
6. source/PDF render verification;
7. release metadata and checksum freeze.

No new mathematical branch is required before manuscript assembly unless the final proof reread finds another defect.
