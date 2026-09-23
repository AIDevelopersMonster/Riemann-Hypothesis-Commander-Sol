# HATTER-SOL-21 · H21-LAB-09 RESULT

Status: **CI REPRODUCED / DIVERSITY SCORE POSITIVE HEURISTIC**

Run:

\`35662904006\`

Ranges:

\[
pq<2^{17},\quad
pq<2^{18},\quad
pq<2^{19}
\]

for distinct odd semiprimes.

## 1. Exact decomposition

For every world and every tested range,

\[
\boxed{
Q_{\rm asym}(W)=G_W+K_W
}
\]

holds exactly to floating-point reporting precision.

Maximum measured identity error:

\[
\boxed{0}.
\]

Here

\[
G_W
=
1-\sum_z\pi_W(z)^2
\]

is the one-direction mask diversity benchmark and

\[
K_W
=
Q_{\rm asym}(W)-G_W
\]

is the cross-direction coupling correction.

## 2. Range 2^19

| world | exposure | Shannon H | Gini G | coupling K | K/G |
|---|---:|---:|---:|---:|---:|
| D-7 | 37.690682% | 1.237096 | 0.471954 | -0.095047 | -0.201391 |
| D+5 | 33.044780% | 0.996529 | 0.331927 | -0.001480 | -0.004458 |
| D-3 | 0% | 0 | 0 | 0 | 0 |
| D-11 | 25.934788% | 0.791602 | 0.263428 | -0.004080 | -0.015490 |
| D+13 | 17.968226% | 0.575655 | 0.169520 | +0.010162 | +0.059945 |
| D-19 | 29.085937% | 0.852198 | 0.280363 | +0.010496 | +0.037438 |

## 3. Stable six-world ranking

On all three tested ranges,

\[
2^{17},\ 2^{18},\ 2^{19},
\]

the world ranking by

\[
Q_{\rm asym}
\]

is exactly reproduced by both:

\[
\boxed{\text{Shannon entropy}}
\]

and

\[
\boxed{\text{Gini diversity}}.
\]

The descriptive six-world Spearman correlation is

\[
\boxed{\rho=1.0}
\]

for both metrics on every tested range.

The order is

\[
\boxed{
D=-7
>
D=5
>
D=-19
>
D=-11
>
D=13
>
D=-3.
}
\]

This is a strong finite heuristic result, not a theorem.

## 4. Local per-prime entropy is much weaker

Mean entropy computed separately at each prime clock performs much worse:

\[
\rho\approx0.486.
\]

Therefore the useful one-direction summary is the **pooled directional mask
distribution across the declared prime-pair population**, not the simple mean
of local clock entropies.

This is an important distinction for the world compiler.

## 5. Partial-mask fraction is useful but not exact

The pooled partial-mask fraction

\[
\Pr[Z=\{0\}\text{ or }\{1\}]
\]

has descriptive Spearman

\[
\rho\approx0.943
\]

against exposure on all tested ranges.

Thus partial-mask richness captures much of world quality, but loses enough
information to mis-rank at least one pair of worlds.

## 6. Coupling mechanism differs by world

The correction

\[
K_W
\]

is not uniformly negligible.

For \(D=-7\),

\[
K_W\approx-0.095
\]

at \(2^{19}\), about

\[
-20.1\%
\]

of its Gini benchmark.

Thus the two directional masks are more often equal than independent pooled
marginals would predict.

For \(D=13\) and \(D=-19\),

\[
K_W>0,
\]

so paired arithmetic slightly **increases** mismatch probability.

Therefore two worlds with similar one-direction diversity can still differ
through cross-prime coupling.

## 7. Compiler consequence

The first inexpensive quality filter can now be:

\[
\boxed{
Q_{\rm cheap}(W)=G_W
}
\]

or equivalently pooled Shannon entropy as a ranking heuristic.

Then apply the coupling correction only to surviving candidates:

\[
\boxed{
Q_{\rm exact}(W)=G_W+K_W.
}
\]

This gives a two-stage compiler:

\[
\text{candidate worlds}
\to
\text{torsion rejection}
\to
\text{cheap pooled diversity ranking}
\to
\text{pairwise coupling refinement}
\to
\text{hardware schedule}.
\]

## 8. Strong negative caution

There are only six worlds in this experiment.

Perfect rank correlation across three ranges does **not** establish a general
law connecting entropy or Gini diversity to factor exposure.

The next required experiment is a broad scan over many admissible quadratic
worlds \((B,C,\Delta)\), with torsion/degenerate cases identified separately.

Only then can the diversity score be judged as a real pre-screening criterion.

## 9. Publication status

\[
\boxed{\text{NOT YET}}
\]

The exact decomposition is elementary probability; the six-world ranking is
an empirical heuristic.

Publication threshold requires either:

- a theorem bounding \(Q_{\rm asym}\) from one-direction diversity and
  arithmetic coupling descriptors;
- or a broad world-family study showing a stable compiler law beyond the six
  hand-selected worlds.
