# Author response to Review 01

**Manuscript:** *Reflections on Sparse Anonymous Phase Geometry with Commander Sol: Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation*  
**Review verdict:** ACCEPT WITH MINOR REVISIONS  
**Author decision:** accept the review as substantively strong, but not every optional recommendation is mathematically safe as stated.

## Accepted revisions

1. **Signed/gain graph distinction — ACCEPT.**  
   The manuscript will explicitly distinguish an active switching operation in signed/gain graphs from the passive component phase cocycle induced by a carrier automorphism preserving the anonymous equality reduct. This improves the novelty boundary and prevents an accidental identification of two different constructions.

2. **Minimal-counterexample constraints — ACCEPT.**  
   The last two constraints after Conjecture 14 will be merged into one statement: every optimal lambda-cell realization must create a deletion-symmetry ambiguity, equivalently a new bad automorphism moving the old domain.

3. **Interesting nontrivial regime — ACCEPT.**  
   A remark will be added after the sparse exactness criterion: the genuinely nontrivial case requires both disconnected Lambda(D) and nontrivial Aut(G;D,Q_D). Connected Lambda gives exactness immediately; trivial reduct automorphism group gives exactness vacuously.

4. **Self-contained status — ACCEPT.**  
   The introduction will state explicitly that Article B is mathematically self-contained. Article A is a conceptual and bibliographic foundation, not a prerequisite for following the proofs.

## Recommendations not accepted in their proposed form

5. **Computational-complexity paragraph — DEFER / REWRITE BEFORE ANY USE.**  
   The review suggests that computing mu(D) is polynomial via a spanning-tree reduction and that alpha is likely NP-hard. Neither statement has been proved in the manuscript. In particular, the one-cell touch sets naturally form a hypergraph and newly added cells can interact, so a naive minimum-spanning-tree claim for exact mu(D) is not currently justified. Likewise, “alpha is likely NP-hard” would be speculation without a reduction. The paper will not add unproved complexity claims. At most it may state that the algorithmic complexity of lambda, mu, and alpha is open.

6. **k-ary / Z_k generalization — REJECT AS STATED.**  
   For q>2 anonymous outputs, the natural phase freedom is not canonically additive in Z_k. Article A already shows that the multicolor problem is governed by local permutations of the anonymous alphabet and a q>=3 arity transition; the relevant discrepancy is generally S_q-valued rather than a Z_k difference. Therefore the suggested formula delta_g(p)=c(gp)-c(p) mod k is not a valid general anonymous-output model unless extra cyclic structure on the colors is imposed. The paper will not insert this statement. A future-work remark may instead point to sparse q>=3 layers and non-abelian S_q-valued phase transport.

## Publication decision

The review strengthens the manuscript but does not identify a flaw in any proved theorem. The required mathematical changes are minor and local. Conjecture 14 remains a conjecture. No theorem statement or proof architecture is withdrawn.

The review itself is retained in the repository because it records an external-style mathematical audit, the accepted corrections, and two recommendations deliberately rejected on mathematical grounds.
