# FCOA Hybrid Memory — Bounded-Depth Resource Separation

**Status:** QUARANTINED AFTER PUBLICATION AUDIT  
**Article B:** EXCLUDED FROM CANONICAL THEOREM CHAIN

## Audit finding

The former `HM-BDRS` package mixed a useful explicit radix construction with an unjustified AL0 lower bound.

Two independent problems were identified.

### 1. Successor-chain problem

The old AL0 upper-bound prose said that a directed successor chain on a growing bottom alphabet "gives the bottom digit order uniformly" and then used that order in a fixed FO lexicographic comparison. In plain first-order logic, transitive closure of an unbounded successor chain is not uniformly definable. Thus a sparse successor relation by itself is not a valid primitive replacement for the full bottom order in the stated FO model.

### 2. Target-attachment symmetry problem

The old AL0 lower bound counted only `M_bot` and argued that bottom symbols untouched by bottom records remained exchangeable. Target-to-digit/factorisation attachments were not charged to `M_bot`; they may distinguish those symbols and prevent the proposed swap from extending to an automorphism of the whole presentation.

Therefore the following former claims are withdrawn:

- `M_bot(AL0)=Theta(N^{1/2^d})` in the stated FO model;
- the exact factor-of-two exponent relation between AL0 and AL1/AL2;
- `HM-BDRS` as a publication theorem.

## What survives

The explicit arithmetic-table observations remain valid **inside a stipulated extensional radix normal form**:

- with `k` fixed bottom digits of alphabet size `s≈N^{1/k}`, a complete add-with-carry table has `Theta(s^2)` rows;
- a complete multiply-and-split table also has `Theta(s^2)` rows;
- fixed-width school arithmetic is recoverable by a fixed formula once the required bottom relations are supplied as primitives.

These are construction/description-size statements, not intrinsic phase lower bounds.

## Canonical replacement

Article B uses unrestricted whole-structure preprocessing cost and the CQ variable-width frontier instead. See `FO_PREPROCESSING_FRONTIER_COLLAPSE.md` and `CQ8_EXACT_THRESHOLD.md`.
