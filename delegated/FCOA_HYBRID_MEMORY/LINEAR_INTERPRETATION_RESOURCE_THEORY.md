# FCOA Hybrid Memory — Linear Interpretation Resource Theory

**Status:** PARTLY CANONICAL, PARTLY SUPERSEDED  
**Article B:** definitions/no-go background only; former `M_int` hypothesis withdrawn

## 1. BF1 definition

A BF1 interpretation is a uniform parameter-free FO interpretation with:

1. interpretation dimension `1`;
2. interpreted domain a definable subset of the source (or a fixed finite disjoint union of such sectors);
3. quotient fibers bounded by a fixed constant;
4. linearly faithful output size.

This is retained as useful vocabulary for discussing recodings that do not use tuple-power universe expansion.

## 2. Composition

### Theorem HM-LIRT-COMP

BF1 interpretations are closed under composition.

### Proof

If `I:A->B` and `J:B->C` have quotient-fiber bounds `K_I,K_J`, substituting the dimension-one definitions of `I` into those of `J` still yields a dimension-one interpretation. Each output representative has at most `K_J` representatives in `B`, each of which has at most `K_I` representatives in `A`, so the composite fiber bound is at most `K_I K_J`. Linear size faithfulness composes by transitivity of `Theta`. `square`

## 3. What BF1 does not buy

BF1 alone does not force a superlinear arithmetic wall. A linear-size digit presentation can explicitly materialize `Theta(N)` table-entry points and `Theta(N)` incidence records while keeping the total universe and record count linear.

Thus banning tuple-power interpretations does not separate AL0, AL1 and AL2 by total storage exponent.

## 4. Superseded internal-memory hypothesis

An earlier version proposed endpoint-based target-independent internal memory `M_int` as the next candidate separator and asked whether

\[
AL0:M_{int}=o(N),\qquad AL2:M_{int}=Omega(N).
\]

That hypothesis is **false**. `TARGET_HOSTING_AND_RADIX_NO_GO.md` gives two countermechanisms:

1. target hosting can move an auxiliary lookup law onto target-indexed records and make endpoint-based `M_int=0`;
2. fixed but arbitrarily wide radix factorisation gives, for every `epsilon>0`, presentations with `M_int=O(N^epsilon)` while total storage remains `Theta(N)`.

Therefore `M_int` is not part of Article B's positive invariant set.

## 5. Publication use

Article B may use BF1 composition and the failure of interpretation dimension/internal-memory scalars as part of the **no-go sequence** motivating the final standard model. It must not present endpoint-based internal-law memory as a surviving conjectural invariant.

The canonical positive separation is instead the CQ variable-width theorem, which counts the whole preprocessing structure.
