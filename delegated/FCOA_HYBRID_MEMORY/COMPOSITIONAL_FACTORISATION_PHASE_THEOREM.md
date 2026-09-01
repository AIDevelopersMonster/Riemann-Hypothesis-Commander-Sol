# FCOA Hybrid Memory — Compositional Factorisation Phase Theorem

**Status:** QUARANTINED AFTER PUBLICATION AUDIT  
**Severity:** C0 for the former AL0 lower bound  
**Article B:** EXCLUDED FROM CANONICAL THEOREM CHAIN

## Audit finding

The former proposition `HM-CF-ORD-LOW` was not proved under the stated resource measure. The quantity `M_bot` counts only bottom-level records, while target/factorisation attachments are allowed to have total size `Theta(N)` and are not charged to `M_bot`.

The old proof argued that two bottom symbols untouched by bottom records could be swapped and that the swap would extend to an automorphism of the entire presentation. This implication does not follow: target/factorisation attachments may distinguish the two bottom symbols even when the bottom induced structure does not.

Therefore the following former claims are withdrawn:

- `HM-CF-ORD-LOW`;
- `M_bot(AL0)=Theta(N^{1/f^d})`;
- the derived exact factor-of-two separation between AL0 and pair-complete transport;
- `HM-CFPT` as a theorem under CF1--CF5 alone.

## What survives

The following material remains valid as construction/normal-form analysis:

1. the definitions of bounded-depth/bounded-fan-in factorisation are usable as exploratory vocabulary;
2. the explicit AL0 upper construction using a bottom chain is an upper bound for that construction;
3. if a primitive bottom binary law on an `s`-element alphabet is required by hypothesis to be represented extensionally, with no lower factorisation or intensional shortcut, its complete table has `Theta(s^2)` rows;
4. the standard-model bridge to bounded-depth factor DAGs and extensional CSP-style tables remains useful as motivation.

These observations do **not** imply an intrinsic AL0/AL1/AL2 lower-bound hierarchy.

## Reinstatement condition

A lower-bound theorem could be restored only after adding and justifying a genuinely global symmetry/equivariance hypothesis ensuring that permutations of bottom symbols preserving bottom records extend through all target/factorisation attachments. No such hypothesis is part of the current Article B claim set.

## Canonical replacement

The publication-grade resource separation is now the **CQ variable-width theorem** in `CQ8_EXACT_THRESHOLD.md`, where the storage measure counts the whole preprocessing structure and the lower bound does not ignore target attachments.
