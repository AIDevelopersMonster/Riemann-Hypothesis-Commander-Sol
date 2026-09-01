# Article B — Canonical Theorem Dependency Graph

**Status:** PUBLICATION CANON

## A. Definitions

`ARTICLE_B_CANONICAL_DEFINITIONS.md`

establishes the target sector, canonical benchmark relations, whole-structure storage measure, FO model, CQ model, and width conventions.

All Article B theorem statements depend on this layer.

## B. Construction layer: linear preprocessing is possible

### B1. Canonical order

A two-coordinate target representation with complete coordinate orders gives canonical target order with `Theta(N)` storage and a fixed FO decoder.

### B2. Canonical addition

`AL1_LINEAR_COST_CRT.md` gives an explicit two-modulus CRT construction. With `p,q=Theta(sqrt N)` and `pq>2N`, target residue maps plus complete modular addition tables have `Theta(N)` total records and recover exact truncated addition.

### B3. Canonical multiplication

`AL2_LINEAR_COST_CRT.md` gives an explicit four-modulus direct CRT construction with linear storage. Independently, the digit-table construction in the FO preprocessing theorem gives a linear-size constant-FO realization.

These yield the upper-bound side of:

### HM-FOPC

`FO_PREPROCESSING_FRONTIER_COLLAPSE.md`:

\[
\boxed{\sigma_0(q)=\sigma_1(q)=\sigma_2(q)=1}
\]

for all sufficiently large fixed FO rank `q`.

The lower bound is only the unavoidable target-size bound `S(A_N)>=N`.

## C. Why earlier scalar invariants fail

This is explanatory, not the positive theorem spine.

- `RESOLUTION_TRANSPORT_PHASE_BOUNDARY.md`: direct-CRT resolution is a normal-form resource, not intrinsic.
- `RTP_INTERPRETATION_NO_GO.md`: unrestricted interpretation can collapse direct resolution profiles.
- `LINEAR_INTERPRETATION_RESOURCE_THEORY.md`: BF1 is compositional but does not restore a storage-exponent hierarchy.
- `TARGET_HOSTING_AND_RADIX_NO_GO.md`: endpoint-based internal memory and every fixed positive internal-memory exponent fail as universal separators.
- `COMPOSITIONAL_FACTORISATION_PHASE_THEOREM.md`: quarantined; former AL0 lower bound ignored target/factorisation attachments.
- `BOUNDED_DEPTH_RESOURCE_SEPARATION.md`: quarantined; sparse successor does not FO-define total order and the AL0 symmetry lower bound was incomplete.

These failures motivate counting the whole preprocessing structure and restricting decoder coordination by CQ variable width.

## D. CQ base separation

`EXISTENTIAL_PEBBLE_WIDTH_SEPARATION.md` (renamed in content to CQ base cases) proves:

\[
\boxed{\sigma_0^{CQ}(3)=1}
\]

via a dyadic/LCA witness representation of order, and

\[
\boxed{\sigma_1^{CQ}(3)=\sigma_2^{CQ}(3)=2}
\]

for the canonical benchmark convention.

The addition lower bound uses the pair-projection obstruction: a width-3 CQ has no helper variable, and pairwise atoms alone accept a spurious tuple, so a three-free-variable primitive atom must materialize `Theta(N^2)` addition triples.

## E. Quantitative intermediate result

`CQ6_MIXED_HELPER_ENTROPY_CLOSURE.md` proves the stronger width-6 storage lower bound

\[
\boxed{\sigma_1^{CQ}(6)\ge7/6.}
\]

This theorem is not needed for the final threshold, but it shows a quantitative gap above exponent one.

## F. Exact near-linear width theorem

`CQ8_EXACT_THRESHOLD.md` contains the repaired hostile-audited proof.

Dependencies:

1. canonical `Add_N` benchmark;
2. no-free-pair observation: a primitive atom containing two free arithmetic variables costs `Theta(N^2)`;
3. Latin-box lemma: fixing all helpers makes the free-variable answer a Cartesian box, and any such box inside addition has size one;
4. deterministic witness selection;
5. entropy bounds from relation cardinalities;
6. conditioning away zero-normalized-entropy helpers;
7. unique information-color lemma for positive helpers;
8. singleton colored-component obstruction.

These imply at least two disjoint positive helpers for each of `X,Y,Z`, hence at least six helper variables:

\[
h\ge6.
\]

With three free variables:

\[
\boxed{k\ge9.}
\]

The two-channel CRT CQ uses exactly six residue helpers, so

\[
\boxed{k_+=9.}
\]

Since the canonical AL2 benchmark includes addition and truncated multiplication has only `Theta(N log N)` true triples,

\[
\boxed{k_{AL2}=9.}
\]

## G. Final publication theorem spine

The recommended Article B order is:

1. Definitions and benchmark hierarchy.
2. Linear preprocessing constructions for order/addition/multiplication.
3. HM-FOPC: unrestricted fixed-rank FO collapses all total-storage exponents to one.
4. Brief failed-invariant audit: why presentation-specific scalar resources do not survive.
5. CQ preprocessing model.
6. Width-3 base separation.
7. Optional width-6 quantitative lower bound.
8. Positive-core entropy lemmas.
9. HM-CQ-EXACT: exact threshold `k_+=9`.
10. Corollary `k_{AL2}=9` under the canonical benchmark convention.
11. Claim ceiling and open problems: exact exponents at widths 6--8; extension to UCQ/existential-positive/full FO.

No CF/BD/RTP lower bound is a dependency of the final theorem.
