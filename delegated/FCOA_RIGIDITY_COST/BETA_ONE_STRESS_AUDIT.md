# FCOA Rigidity Cost — Beta-One Anchored-Recognizable Stress Audit

**Status:** exploratory computational evidence; not an exhaustive theorem.

## Target

Test the strengthened mechanism

\[
\beta=1
\quad\Longrightarrow?\quad
\text{there exists an anchored-recognizable beta-killing one-cell repair}.
\]

By `ANCHORED_RECOGNIZABLE_REPAIR.md`, such a repair is automatically exact.

## Search space

Carrier size:

\[
|G|=6.
\]

A fresh optimized C++ verifier sampled

\[
\boxed{1,000,000}
\]

random surjective sparse binary layers with domain sizes between 4 and 15 cells.

For each sampled layer it computed directly:

1. the uncolored domain automorphism group;
2. the ternary equality reduct automorphism group;
3. the full anonymous binary group;
4. the old bad automorphisms;
5. every missing one-cell extension and both binary colors;
6. whether the extension kills every old bad automorphism (`beta=1` witness);
7. whether the extension is exact;
8. whether the new cell is anchored to an old incidence component;
9. whether every automorphism of the enlarged uncolored domain fixes the unique new cell, equivalently preserves the old domain.

## Result

Among the one million sampled layers,

\[
\boxed{19,408}
\]

were nonexact and possessed at least one one-cell old-obstruction repair, hence had `beta=1` in the sampled direct test.

Every one of these 19,408 layers possessed an exact one-cell repair.

More strongly, no layer was found for which exact one-cell repair existed but **all** beta-killing cells failed the anchored-recognizable criterion.

Thus the search found no counterexample to

\[
\boxed{
\beta=1
\Longrightarrow
\exists\text{ anchored-recognizable beta-minimizer}
}
\]

on this large random six-carrier sample.

## Interpretation

This strengthens the earlier targeted evidence in two ways:

- it is not biased toward the known unsafe witness;
- it explicitly checks the structural sufficient mechanism, not merely equality `alpha=beta`.

Together with the exhaustive five-carrier result, the evidence now supports the possibility that the beta-one case admits a direct geometric theorem.

## What remains open

The audit is random, not exhaustive. It does not establish the six-carrier `|D|<=8` frontier theorem and does not prove the general beta-one implication.

The next theoretical target is therefore the **Beta-One Escape Theorem**:

> If a sparse binary layer has `beta=1`, then some beta-killing cell is both anchored and outside the one-cell replacement obstruction, or else a replacement-boundary cell admits an exact coloring by positive-rank affine avoidance.

A proof would establish

\[
\boxed{\beta=1\Longrightarrow\alpha=1}
\]

in full generality and remove the dominant class from the global Safe-Minimizer problem.

## Claim firewall

1. 1,000,000 is the number of sampled layers, not the number of isomorphism classes.
2. The result is evidence, not an exhaustive theorem.
3. No positive eta witness was found.
4. The global conjecture `alpha=beta` remains open.
