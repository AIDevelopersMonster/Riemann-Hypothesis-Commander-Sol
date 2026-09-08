# LQR publication source map

This file records theorem provenance for the release candidate. The publication manuscript is self-contained; the delegated files below are development and audit sources.

| Manuscript result | Development source | Independent check |
|---|---|---|
| Definition of L_q(r) and forest reduction | QGE3/LQR_DEFINITIONS.md | verify_lqr.py |
| Synchronization / unique-coloring equivalence | QGE3/LQR_DEFINITIONS.md | quotient-coloring routines in verify_lqr.py |
| Pair-union connectivity and half-density bound | QGE3/LQR_LOWER_BOUNDS.md | small exact tables |
| Exact q=3 row | QGE3/LQR_CONSTRUCTIONS.md and LQR_LOWER_BOUNDS.md | exhaustive normalized checks in verify_lqr.py |
| Exact r=2 and r=3 columns | QGE3/LQR_CONSTRUCTIONS.md and LQR_LOWER_BOUNDS.md | small exhaustive checks |
| Exact r=4 column | QGE3/LQR_R4_THEOREM.md | exact partition search in verify_lqr.py |
| Universal binary-cut gadget | QGE3/LQR_BINARY_CUT_GADGET.md | agreement with solved r=2,3,4 cases |
| Cut-space lemmas and stabilization theorem | QGE3/LQR_STABILIZATION_THEOREM.md | verify_lqr_cutspace.py |
| Literature and novelty boundary | QGE3/LQR_PRIORITY_AUDIT.md and LITERATURE_NOTES.md | dedicated literature search |
| Final mathematical hostile audit | QGE3/LQR_HOSTILE_AUDIT.md | both verifier scripts |

## Frozen theorem chain

The release candidate treats the following chain as proved:

point-image constraints -> source-color constraint graphs -> transversal unique-coloring quotient -> pair-union connectivity -> phase component partitions -> normalized binary cut spaces -> pairwise trivial subspace intersections -> defect packing bound -> exact stabilization threshold.

## Explicitly open material

The manuscript does not claim a general exact solution in the pre-stabilization sector for r>=5, does not claim that every optimal subspace packing is synchronizing, and does not introduce a multicolor real-operation-cell repair invariant.
