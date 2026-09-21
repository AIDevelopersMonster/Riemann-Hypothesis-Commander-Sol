# HATTER-SOL-21 · ZERO-MASK PHASE ENTROPY TARGET

Status: **NEXT WORLD-QUALITY STRIKE**

H21-LAB-08 rejects local clock length as a sufficient quality score.

The next candidate is the geometry of the phase partition itself.

## 1. Local phase distribution

For a fixed world \(W\) and prime \(p\), let

\[
\Lambda_{W,p}(q)=Z_{p\leftarrow q}(W)
\]

take values in

\[
\varnothing,\{0\},\{1\},\{0,1\}.
\]

Over a declared set of admissible prime phases, define probabilities

\[
\pi_{W,p}(z).
\]

The local zero-mask entropy is

\[
\boxed{
H_W(p)
=
-\sum_z\pi_{W,p}(z)\log_2\pi_{W,p}(z).
}
\]

A torsion-silent world has

\[
H_W(p)=0.
\]

But positive entropy alone may still be insufficient, because factor exposure
requires *cross-prime mismatch*.

## 2. Cross-prime asymmetry functional

For a prime pair \(p\ne q\), define

\[
A_W(p,q)
=
\mathbf 1[
\Lambda_{W,p}(q)
\ne
\Lambda_{W,q}(p)
].
\]

The exact semiprime factor-exposure rate is the mean of \(A_W\) over the
declared pair population.

A predictive world-quality model should approximate this pairwise quantity
from one-prime clock descriptors without explicitly scanning all semiprimes.

## 3. Candidate one-prime descriptors

For each world, measure distributions of:

- \(h_W(p)\);
- number of distinct zero masks realized by prime phases;
- local mask entropy \(H_W(p)\);
- maximum mask mass;
- split/inert-conditioned mask entropy;
- fraction of phases producing partial masks \(\{0\}\) or \(\{1\}\);
- fraction producing full-zero mask \(\{0,1\}\).

The strongest hypothesis is:

\[
\boxed{
\text{partial-mask richness, not clock length, predicts factor exposure}.
}
\]

This is natural because a factor appears only when coordinate zero patterns
differ across the two local sides.

## 4. Required negative controls

The lab must test:

- whether entropy ranking predicts the six measured exposure rankings;
- whether the ranking survives changing the prime range;
- whether \(D=5\) is correctly explained despite its smaller mean clock order;
- whether \(D=-3\) collapses to zero entropy;
- whether a high-entropy world can still be poor because the two directions
  are correlated.

## 5. Publication threshold

A correlation alone is not enough.

The serious target is an inequality or exact relation connecting

\[
H_W(p),\quad H_W(q)
\]

or a stronger one-prime descriptor to the pairwise asymmetry probability

\[
\Pr[A_W(p,q)=1].
\]

Until then the entropy layer remains a compiler heuristic.
