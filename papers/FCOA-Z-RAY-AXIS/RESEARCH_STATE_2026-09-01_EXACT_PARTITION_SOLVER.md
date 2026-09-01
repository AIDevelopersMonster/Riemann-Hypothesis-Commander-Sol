# FCOA-Z Research State — Exact Partition-Only Solver Milestone

Date: 2026-09-01
Status: internal research checkpoint

## Closed in this checkpoint

The arbitrary partition-only prescribed-support problem

\[
d(\lambda)=\min\{|R|:\operatorname{Aut}(R)=K_\lambda\}
\]

is now solved as an exact finite optimization problem.

The new theorem package `PARTITION_ONLY_EXACT_TWIN_SOLVER.md` proves:

1. every proper overgroup of a partition stabilizer either contains a forbidden cross-block point transposition or is the single exceptional singleton-union macro-swap type;
2. exact recognition `Aut(R)=K_lambda` therefore reduces to finitely many representative forbidden symmetries;
3. every forbidden symmetry gives an OR-of-XOR constraint on orbital membership bits;
4. the exact minimum `d(lambda)` is the optimum of the resulting weighted Orbital XOR-Separation Program;
5. the number of variables is `O(k^2)`, where `k` is the number of distinct block sizes;
6. the exact FCOA value-support cost is

\[
\boxed{m_G(J_\lambda;S_\times)=t^2 d(\lambda).}
\]

The executable solver is:

`solve_partition_only_support.py`

The hostile finite verifier is:

`verify_partition_only_exact_solver.py`

The recognition theorem was independently checked by direct full `S_b` enumeration for every integer partition with `2 <= b <= 7` and every `K_lambda`-invariant orbital union; no discrepancy was found.

## Important correction to the previous frontier

The previous question was phrased as whether one could derive a closed formula for arbitrary `lambda` or else prove hardness.

A closed scalar formula is not necessary for mathematical closure of the invariant. We now have an exact canonical optimization formulation and an exact solver that does not call a graph-automorphism oracle.

Therefore the main structural problem

> what exactly is `d(lambda)` and how can it be computed from the partition type?

is closed in the finite exact sense.

## Remaining secondary frontier

What remains open is complexity classification of the compressed optimization problem:

1. polynomial-time solvability versus NP-hardness in the compressed partition input;
2. approximation guarantees if NP-hard;
3. additional closed formulas for distinguished infinite families.

This is a secondary optimization/complexity question, not a gap in the correctness of the prescribed-support theory.

## Literature boundary

The transposition-separation mechanism is closely related to classical point-determining / twin-free graphs and digraphs. Minimum Test Cover and discriminating-code problems are known NP-hard in general, but that fact alone does **not** establish NP-hardness of the present highly structured partition-orbital program.

Relevant classical boundary references include:

- D. P. Sumner, *Point determination in graphs*, Discrete Mathematics 5 (1973), 179–187, DOI `10.1016/0012-365X(73)90109-X`.
- R. C. Entringer and L. D. Gassman, *Line-critical point determining and point distinguishing graphs*, Discrete Mathematics 10 (1974), 43–55, DOI `10.1016/0012-365X(74)90019-3`.
- P. Hell and C. Hernández-Cruz, *Point determining digraphs, {0,1}-matrix partitions, and dualities in full homomorphisms*, Discrete Mathematics 338 (2015), 1755–1762, DOI `10.1016/j.disc.2014.12.001`.
- E. Charbit, I. Charon, G. Cohen, O. Hudry, *Discriminating codes in bipartite graphs*, Electronic Notes in Discrete Mathematics 26 (2006), 29–35, DOI `10.1016/j.endm.2006.08.005`.

No NP-hardness claim for `d(lambda)` is made at this stage.

## Publication readiness

The post-publication FCOA-Z branch now contains a coherent theorem chain:

- finite-state radial phase transport;
- terminal symmetry collapse;
- branching lift obstruction and coherence bit;
- value recovery and exact 9-cell binary compiler;
- prescribed-stabilizer support invariant;
- global wreath coherence formula;
- equal and unequal partition phase-coherence formulas;
- partition-only reduction and complement compression;
- exact arbitrary-partition recognition theorem and solver.

This is now substantial enough to justify beginning a dedicated follow-up paper assembly **after** one focused hostile literature audit on exact prescribed set stabilizers / relation groups and the new partition-overgroup dichotomy.

The branch should not yet be released to Zenodo before that audit and a proof-numbering/formalization pass.