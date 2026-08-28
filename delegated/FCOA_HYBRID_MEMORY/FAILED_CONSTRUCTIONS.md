# FCOA Hybrid Memory — Failed / Rejected Constructions

## 1. One rigid reduct plus spectator

Any pair with

\[
\operatorname{Aut}(\oplus)=1
\quad\text{or}\quad
\operatorname{Aut}(\otimes)=1
\]

is rejected as a hybrid-memory witness even if the joint reduct is rigid. This excludes directly reusing M0 addition, G3-A, or G4-A as one side of the pair.

Reason: the target is information present only jointly, not rigidity inherited from one reduct.

## 2. Carrier size two

Rejected by theorem HM-0. On two active points the unique nontrivial permutation is the transposition. Therefore two nonrigid reducts necessarily share it and cannot be jointly rigid.

## 3. Empty operation on one side

If one operation has no defined cells and no other structure on its outputs, its active automorphism group is the full symmetric group. The joint automorphism group then contains the automorphism group of the other reduct. Hence the pair cannot become rigid while the other reduct remains nonrigid.

This proves the one-defined-cell-per-operation lower bound for DD-3.

## 4. Same residual involution twice

If both reducts have the same residual `C_2` subgroup, then

\[
\operatorname{Aut}(\oplus,\otimes)=C_2,
\]

not `1`. Equal group sizes are irrelevant; subgroup position matters.

This is the basic false positive the branch must avoid.

## 5. Anonymous two-value partition with equal fiber sizes on three diagonal cells

Impossible because three is odd. This is useful: the `1+2` fiber-size asymmetry in DV-3/VV-3 automatically prevents swapping the two anonymous outputs.

For even carriers, equal-size two-fiber colorings require a separate output-swap audit; one cannot assume that a two-coloring fixes either fiber individually.

## 6. Treating finite rigidity as arithmetic leakage

Rejected inference:

\[
\operatorname{Aut}(M_n)=1
\quad\Rightarrow\quad
\text{uniform external order/arithmetic is definable.}
\]

This is false as a general research step. Rigidity is a finite orbit statement; uniform family definability is stronger and must be proved separately.

## 7. Copying G4 orientation coloring into both operations

Rejected as the first witness because it imports too much order-like geometry and obscures the genuinely hybrid mechanism. The three-point diagonal witnesses are strictly weaker, cleaner, and safer with respect to the Arithmetic Leakage firewall.

## 8. Unqualified HRI scalar

The provisional scalar

\[
\frac{|Aut(\oplus)||Aut(\otimes)|}{|Aut(\oplus,\otimes)|}
\]

is not adopted as a theorem-level invariant. It loses subgroup-position information: distinct subgroup configurations can have the same three cardinalities. The subgroup-intersection profile is primary.
