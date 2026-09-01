# FCOA Hybrid Memory — CQ Variable-Width Separation: Base Cases

**Status:** CANONICAL FOR CONJUNCTIVE QUERIES  
**Model:** static relational preprocessing + one fixed conjunctive-query decoder  
**Important scope correction:** a single CQ is **not** the whole existential-positive finite-variable fragment. Existential-positive FO allows finite disjunctions of CQs. Pebble-game characterizations apply to the broader existential-positive fragment, not automatically to every lower bound proved here for one CQ.

## 1. Model

For each `N`, let `X_N` be an `N`-element target sector in a finite structure `A_N` over one fixed finite bounded-arity relational signature. Storage is

\[
S(A_N)=|A_N|+\sum_R |R^{A_N}|.
\]

A target relation is decoded by one fixed conjunctive query using at most `k` distinct variables total, free and existential.

Define

\[
\sigma_j^{CQ}(k)=\inf\limsup_{N\to\infty}\frac{\log S(A_N)}{\log N}
\]

for the canonical target benchmark of phase `j`.

## 2. Order at width 3

Build a balanced binary decomposition tree with target elements as leaves. Store

\[
L(x,w),\qquad R(y,w)
\]

when leaf `x` lies below the left child of `w` and leaf `y` below the right child. There are `O(N log N)=N^{1+o(1)}` tuples.

Then

\[
x<y\iff\exists w\,(L(x,w)\land R(y,w)).
\]

The least common ancestor witnesses the formula exactly for `x<y`. Therefore

\[
\boxed{\sigma_0^{CQ}(3)=1.}
\]

## 3. Order at width 2

A CQ with free variables `x,y` and no third variable must contain an atom involving both variables in order to orient pairs. That primitive relation must contain all `Theta(N^2)` ordered pairs satisfying `<`. Direct materialization matches the lower bound:

\[
\boxed{\sigma_0^{CQ}(2)=2.}
\]

## 4. Addition at width 3

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

There are `Theta(N^2)` valid triples. A three-variable CQ has no extra helper variable. If every atom uses at most two of `x,y,z`, then every atom must contain the corresponding projection of `Add_N`. The spurious triple `(1,1,3)` for `N>=4` belongs to all unary and pair projections but is not an addition triple. Hence some atom must involve all three free variables, and its primitive relation must contain all `Theta(N^2)` valid addition triples.

Thus

\[
\boxed{\sigma_1^{CQ}(3)=2.}
\]

If the AL2 benchmark includes canonical addition, the same lower bound applies:

\[
\boxed{\sigma_2^{CQ}(3)=2.}
\]

## 5. Base separation

Therefore

\[
\boxed{
\sigma_0^{CQ}(3)=1,
\qquad
\sigma_1^{CQ}(3)=\sigma_2^{CQ}(3)=2.
}
\]

This is a theorem about **single conjunctive queries**. It is not advertised as a lower bound for arbitrary existential-positive `FO^3`, full `FO^3`, formulas with disjunction, or formulas with negation.

## 6. Relation to the exact threshold

The later audited theorem `CQ8_EXACT_THRESHOLD.md` proves that near-linear exact addition requires total CQ width at least `9`, and a two-channel CRT CQ of width `9` attains it. The present file supplies the small-width base cases and the clean `k=3` space separation.

## 7. Literature calibration

Finite-variable logic and existential pebble games remain relevant background for the general research programme, but the publication claim here uses only elementary CQ arguments. No pebble-game theorem is needed for the proof above.
