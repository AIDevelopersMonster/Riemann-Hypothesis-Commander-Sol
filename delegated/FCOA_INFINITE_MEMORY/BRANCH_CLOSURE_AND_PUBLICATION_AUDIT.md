# Branch Closure and Publication Audit — Infinite FCOA Memory

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-29  
**Document type:** publication audit / branch closure decision  
**Claim ceiling:** infinite-carrier/model-theoretic branch only; no promotion of finite G4 status

## 1. Original branch problem

The branch was tasked to determine what survives from finite successor/domain memory on the infinite carrier and to locate the exact first-order boundary between local directed memory and global order memory.

The required questions were:

1. whether full strict order is FO-definable from successor/definedness;
2. if not, a rigorous nondefinability proof;
3. separation of FO, FO+TC, MSO, computable recovery, parameters, and uniform finite-family definability;
4. identification of finite enrichments that cross the FO order boundary;
5. arithmetic-leakage analysis;
6. asymptotic invariants only when logically tied to recoverability.

## 2. Closure verdict

The core branch problem is **solved at the declared theorem scope**.

### Closed results

- Infinite G2 successor/domain memory uniformly recovers local successor but does not FO-define the full transitive order.
- The nondefinability result has independent EF/locality and quantifier-elimination style proofs.
- Finite parameters and finite unary/local enrichments do not repair the FO boundary.
- No single FO formula defines the full order uniformly across all finite directed paths.
- FO+TC and MSO recover reachability/order; computable reconstruction is separate and possible.
- Global order stored in operation-domain geometry crosses the FO boundary with one output.
- Complete comparison-value memory crosses the boundary with two value fibres if the domain is complete.
- Finite-apex locally finite active memory cannot FO-define the infinite order.
- In binary finite-output FCOA, a full FO order requires an infinite nonlocal core.
- Order-only one-dimensional binary compilations have a linear/quadratic density dichotomy; FO order forces a quadratic primitive relation.
- Primitive non-order nested-tail and sparse-marker geometries show that raw finite-window density is not a universal cost invariant.
- Nested-row order codes contain canonical half-graphs and obey the exact Ladder–Escape tradeoff.
- Derived instability exists: primitive relations can be ladder-shallow while FO composition recovers order.
- Payload-preserving derived instability exists with dimension-2 pure-order self-coordination.
- Dimension 1 is impossible for the linear-cost pure-order package; dimension 2 is exact.
- The primitive signature can be reduced to one binary relation / one one-output partial-operation layer.
- Directedness and loops are not essential: one symmetric irreflexive C4-free graph suffices.
- For dimension-2 pure-order provenance the infinite-degree diagonal hub count satisfies the exact law
  \[
  H(N)=\Theta(\sqrt N).
  \]
  More generally, fixed dimension \(d\) gives the exact diagonal-spine law
  \[
  H_d(N)=\Theta(N^{1/d}).
  \]

### Scope boundary

This is not a classification of every imaginable finite-signature enrichment over every possible non-order source. In particular, D0L/exponential-marker sources belong to a broader provenance class.

The original branch question is nevertheless closed in its intended form: the successor-to-global-order FO boundary is proved, explicit crossing mechanisms are identified, arithmetic leakage is separated, and the pure-order payload-preserving extremal architecture has exact minima/barriers.

## 3. Strongest publication nucleus

The strongest coherent paper is **not** the chronological collection of all branch notes. The publication nucleus should be the later exact architecture:

### Proposed paper nucleus

**Working title:**

> *First-Order Global Order from a Linear-Cost C4-Free Payload Graph: Exact Dimension and Nonlocal-Core Barriers*

Core theorem package:

1. construction of one simple symmetric irreflexive C4-free graph on a dimension-2 pure-order payload carrier;
2. exact atomic ladder depth 2;
3. FO recovery of a full order of type \(\omega\);
4. \(\Theta(N)\) primitive incidence cost;
5. nondefinability of ordinary addition and multiplication;
6. dimension-one impossibility under pure-order provenance;
7. exact dimension minimum \(2\);
8. exact hub-density law \(\Theta(\sqrt N)\) at dimension 2 and \(\Theta(N^{1/d})\) in fixed dimension \(d\).

This package is substantially cleaner and stronger than publishing the earlier nested-tail/sparse-marker sequence as the main article.

### Secondary companion material

The following belongs either in a shorter companion note or an appendix/related-work section:

- G2 successor nondefinability and finite-to-infinite transfer;
- Sparse Memory Threshold;
- Order-Only Quadratic Barrier;
- Ladder–Escape invariant;
- sparse-marker examples;
- directed subdivision benchmark.

These results motivate the final construction but should not overwhelm the main paper.

## 4. Novelty posture

The article must make conservative novelty claims.

Classical ingredients include:

- FO nondefinability of transitive reachability from successor;
- quantifier elimination/tail normal forms for discrete order;
- half-graphs and the model-theoretic order property;
- Ferrers/nested-neighborhood graph theory;
- finite-dimensional interpretations;
- C4-free/codegree-one graph observations;
- Julia Robinson's definability of addition from multiplication plus successor.

The publishable claim is the **specific extremal synthesis and exact barrier package**, not any of those ingredients individually:

\[
\boxed{
\text{one simple C4-free relation}
+\Theta(N)\text{ primitive cost}
+\text{payload preservation}
+\text{FO global order}
+\neg\text{FO arithmetic}
}
\]

together with the exact pure-order lower bounds on interpretation dimension and hub density.

A full related-work search is still required before claiming priority for this exact combination.

## 5. Publication audit findings

| ID | Severity | Location | Problem | Why it matters | Minimal repair | Claim-set effect |
|---|---|---|---|---|---|---|
| PA-01 | C2 | `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`, PP-4 prose | Calls \(\Theta(N)\) “information-theoretically minimal” without a proved universal \(\Omega(N)\) theorem for the whole class | Overstates the proven lower bound | Delete “information-theoretically minimal” and state only “linear primitive incidence cost” | narrows |
| PA-02 | C4 | corpus-wide related-work positioning | No exhaustive literature search yet for the exact combination “C4-free simple graph + FO interpreted \(\omega\)-order + dimension/hub optimality” | Priority/novelty cannot be asserted safely | Add targeted MathSciNet/zbMATH/Google Scholar/arXiv search and cite nearest results | none |
| PA-03 | C4 | QE references | Current notes cite standard textbook QE facts but bibliography has not been normalized and primary/standard-source locations have not been checked consistently | Publication requires reliable theorem provenance | Verify exact editions/theorem numbers or give a short self-contained tail-normal-form proof and cite standard references only as background | none |
| PA-04 | C2 | some chronological notes | Phrases such as “new mechanism” or “exact universal cost” occasionally exceed the theorem's provenance scope | Could imply universality beyond pure-order/fixed-dimensional class | Restrict every exact-minimum statement to the declared provenance class | clarifies |
| PA-05 | C3 | corpus architecture | Chronological discovery notes duplicate and supersede earlier candidate invariants | A paper assembled directly from them would be diffuse and internally repetitive | Write a fresh theorem-first manuscript; use old notes only as source material | none |
| PA-06 | C5 | publication package | No unified manuscript, theorem numbering, bibliography, metadata, DOI record, compiled PDF, or visual render audit yet | Release artifact does not yet exist | Build clean RU/EN or EN manuscript, compile, render, inspect | none |
| PA-07 | C1 | `HUB_DENSITY_BARRIER.md`, general-dimension statement | The \(\Theta(N^{1/d})\) statement is proved for the definable one-coordinate diagonal spine under fixed-dimensional pure-order provenance, not for arbitrary infinite nonlocal cores | Without this hypothesis, the statement can be misread as universal | State “diagonal-spine hub law” in theorem title/hypotheses and avoid universal-core wording | clarifies |

## 6. Mathematical status after audit

No C0 mathematical error has been identified in the final theorem nucleus.

The hub-density proof closes the last unresolved quantitative parameter of the dimension-2 pure-order architecture:

\[
\boxed{
H(N)=\Theta(\sqrt N).
}
\]

The lower bound follows from finite-fibre confinement under discrete-order quantifier elimination: for any FO-definable \(\omega\)-order on \(\mathbb N^2\), the finite predecessor fibre of \((m,m)\) lies in a box \([0,m+K]^2\), hence the rank of the \(m\)-th diagonal hub is \(O(m^2)\). The max-shell construction attains the matching upper bound.

The exact dimension-2 construction has also been computationally sanity-checked on finite truncations for the claimed C4-freeness; the publication proof remains the combinatorial codegree proof, not the computation.

## 7. Is there enough for publication?

**Yes.** There is now enough for a focused mathematical article/preprint.

The publishable contribution is not “FCOA” terminology by itself and not the classical successor boundary. It is the compact extremal theorem package around derived instability in a one-relation C4-free payload graph plus exact pure-order dimension and hub-density barriers.

A reasonable publication sequence is:

1. **Main paper:** undirected one-relation construction + dimension-one barrier + hub-density barrier + arithmetic non-leakage.
2. **Optional companion note:** successor/G2 boundary, sparse-memory threshold, Ladder–Escape and sparse-marker history.

The main paper can stand on its own without the companion note.

## 8. Release decision

Unresolved blocking issues:

- related-work/priority search for the exact theorem package;
- removal of the unsupported “information-theoretically minimal” wording;
- normalization of QE references or replacement by self-contained lemmas;
- creation and render-audit of the final manuscript.

Equations/theorems changed in this audit: none; one theorem scope must be clarified in the eventual manuscript (`HD-4`).

Claim set changed: **yes, narrowed conservatively** (remove universal/minimal wording not proved outside the declared class).

Bibliography verified: **partial**.

Metadata verified: **no**.

Source compiled: **not supplied**.

PDF visually inspected: **not supplied**.

**Release status:** `BLOCKED_SOURCE_SUPPORT`

This status does **not** mean the mathematics is unpublishable. It means the theorem nucleus is strong enough to draft now, but publication should not be released until the source/priority audit and final manuscript/render checks are completed.