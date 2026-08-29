# Upstream Addendum — Exact Dimension-2 Minimum

**Direction:** FCOA — SOL-INFINITY  
**Date:** 2026-08-28  
**Companion theorem:** `DIMENSION_ONE_BARRIER.md`  
**Upper-bound construction:** `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`

## New fixed result

Within the pure-order provenance class based on one-dimensional FO interpretations of `(N,<)` with finitely many parameters, including arbitrary definable quotient equality and finitely many binary finite-output traces, the package

- payload preservation;
- bounded primitive ladder depth;
- `Theta(N)` primitive cost;
- FO recovery of a full order of type `omega`;
- no FO ordinary `+` or `x`;

cannot be realized at interpretation dimension 1.

The obstruction is stronger than the primitive ladder condition.

### 1. Quotient loophole closes

For any infinite one-dimensional quotient `D/E`, canonical least representatives form an infinite unary definable subset of `(N,<)`. Unary definable sets in discrete pure order with finitely many parameters are finite or cofinite. Hence almost every source point is already a canonical representative, and `E` is eventually equality.

Therefore a 1D quotient cannot asymptotically simulate pair geometry.

### 2. Recovered omega-order has bounded rank distortion

Any FO-definable order of type `omega` on a cofinite subset of `(N,<)` must eventually have the same remote orientation as the source order. Otherwise large points would acquire infinitely many predecessors. By the binary tail normal form, only bounded-distance permutations remain possible, so recovered rank differs from source rank by `O(1)`.

Thus linear/quadratic density regimes transfer between source-order and recovered-order windows.

### 3. One-dimensional primitive relations obey the old dichotomy

After quotient trivialization, every primitive binary trace is directly FO-definable in pure order. Therefore each primitive relation has either `O(N)` local/finite-apex density or `Theta(N^2)` density.

If total primitive cost is linear, every primitive trace is in the local regime. Finite union plus finite-apex removal yields a locally finite residual Gaifman graph. The existing Sparse Memory Threshold then forbids any FO-defined infinite strict linear order.

Therefore:

`dimension 1 + pure-order provenance + Theta(N) primitive cost + FO omega-order` is impossible.

### 4. Matching upper bound

The dimension-2 self-coordinate construction already achieves the complete target package:

- every point remains a payload peer;
- no dedicated witness-only population;
- every primitive binary relation has atomic half-graph depth `<2`;
- primitive incidence cost is `Theta(N)`;
- full omega-order is FO-definable;
- ordinary addition and multiplication remain FO-undefinable.

Hence the structural minimum is exact:

`dim_self = 2`.

## Scope

This exact minimality theorem is relative to **pure-order provenance**. It does not rule out one-dimensional primitive non-order sources such as D0L/exponential/global skeletons, which are outside the 1D pure-order interpretation class.

## Recommendation

Treat the dimension question as closed for pure-order-derived payload-preserving memory. The next frontier should move to one of:

1. source-class extension beyond pure order;
2. reducing the dimension-2 signature from three primitive traces to two or one;
3. quantifying the least infinite-fibre complexity needed for derived instability;
4. finite truncation / exact finite-N cost and rigidity.
