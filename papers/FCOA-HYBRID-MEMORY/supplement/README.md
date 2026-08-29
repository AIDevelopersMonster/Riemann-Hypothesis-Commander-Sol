# Supplement — finite classification verifier

`verify_minimal_classifications.py` is a dependency-free exhaustive verifier for the two computer-assisted propositions in Article A.

It checks:

1. unrestricted one-sorted binary partial operations with exactly one cell per operation under the strong VV/erasure conditions;
2. typed common-terminal JFS on three active points with exactly three tagged cells.

Expected results:

- one-sorted n=2: 0 labeled / 0 classes;
- one-sorted n=3: 0 labeled / 0 classes;
- one-sorted n=4: 24 labeled / 1 class;
- typed JFS-3: 48 labeled / 8 classes.

The script computes automorphism groups from the operation graphs directly and canonicalizes witnesses by the full carrier relabeling action. Operation symbols remain distinguished.

No external packages are required.