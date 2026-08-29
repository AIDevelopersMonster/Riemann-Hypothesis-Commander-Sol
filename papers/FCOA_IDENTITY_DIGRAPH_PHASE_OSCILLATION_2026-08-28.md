# FCOA — Identity-Digraph Sparsity: phase oscillation and nonexistence of a universal constant term

**Date:** 2026-08-28  
**Status:** theorem-level deduction conditional only on the enumerative asymptotic `a_k ~ c lambda^k k^(-5/2)` recorded for identity oriented trees (OEIS A102755).  
**Novelty status:** **not claimed** pending dedicated prior-art audit.

## 1. Question

Let

`m(n)=min{|F| : F subset X_n^2\Delta, Stab_{S_n}(F)=1}`

and

`delta(n)=n-m(n)`.

The previous checkpoint established

`delta(n) = L n/[log n+(3/2)log log n+O(1)]`,

where

`L=log lambda`,

`lambda=5.249032491228170579164952216...`.

The question was whether the bounded term converges to a genuine constant:

`delta(n) = L n/[log n+(3/2)log log n+K_0+o(1)]`.

The answer is **no**. The bounded term has a nonvanishing phase oscillation caused by partial occupation of the last available tree-size layer.

## 2. Enumeration input

Let `a_k` be the number of nonisomorphic identity (asymmetric) oriented trees on `k` vertices. We use

`a_k ~ c lambda^k k^(-5/2)`

with

`lambda = 5.249032491228170579164952216...`,

`c = 0.17807103914078424643862998...`.

Set

`L=log lambda = 1.658043772235415321742334376...`.

## 3. Exact greedy packing coordinates

To maximize the positive deficit, one packs pairwise nonisomorphic identity oriented-tree components in increasing order of their sizes.

For a layer `K`, define

`A_{K-1}=sum_{j<K} a_j`

and

`R_{K-1}=sum_{j<K} (K-j)a_j`.

Choose `q` tree types of order `K`, `0<=q<=a_K`. Then the number of tree components is

`t_K(q)=A_{K-1}+q`,

while their total number of vertices is

`n_K(q)=sum_{j<K} j a_j + Kq`

and therefore exactly

`n_K(q)=K t_K(q)-R_{K-1}`.

Each such tree component contributes exactly `+1` to `n-|F|`. Conversely every positive unit of deficit in any identity digraph must come from a distinct identity oriented-tree weak component. Hence the cheapest-type packing is the relevant extremal knapsack.

At the exact orders `n_K(q)`, the resulting forest already has exactly that order, so no filling issue occurs.

## 4. The last layer is macroscopic

From the exponential tree asymptotic,

`A_{K-1}/a_K -> r`,

where

`r = sum_{d>=1} lambda^(-d) = 1/(lambda-1)`.

Likewise,

`R_{K-1}/a_K -> u`,

where

`u = sum_{d>=1} d lambda^(-d) = lambda/(lambda-1)^2`.

Numerically,

`r = 0.23534769434322515287...`,

`u = 0.29073623157589728549...`.

Thus the entire collection of all smaller tree types has size only about `r a_K`. A fraction of the current layer therefore remains visible at order one; it does not wash out asymptotically.

## 5. Phase parameter

Take any fixed `theta in [0,1]` and choose

`q_K=floor(theta a_K)`.

Put

`s(theta)=r+theta`.

Then

`t_K(q_K)/a_K -> s(theta)`

and

`R_{K-1}/t_K(q_K) -> beta(theta)=u/s(theta)`.

Since

`n_K(q_K)=K t_K(q_K)-R_{K-1}`,

we have

`n_K(q_K)/t_K(q_K)=K-beta(theta)+o(1)`.

On the other hand,

`log n_K(q_K)`

`= K L -(3/2)log K + log c + log s(theta)+o(1)`.

Also

`log K = log log n - log L + o(1)`.

## 6. Explicit phase law

Define the normalized bounded correction

`E(n)=L n/delta(n)-log n-(3/2)log log n`.

Along the subsequence `n=n_K(q_K)` with `q_K/a_K -> theta`,

`E(n) -> Phi(theta)`,

where

`Phi(theta) = -(3/2)log L - log c - log(r+theta) - L u/(r+theta)`.

Thus the bounded term is not a single constant but a continuous phase profile indexed by the fractional occupation of the last tree-size layer.

## 7. No universal K_0

If a constant `K_0` existed in

`delta(n)=L n/[log n+(3/2)log log n+K_0+o(1)]`,

then `E(n)` would converge to `K_0`.

But `Phi(theta)` is nonconstant. Indeed

`Phi'(theta) = [L u-(r+theta)]/(r+theta)^2`.

Its unique interior critical point is

`theta_* = L u-r = 0.24670570378438485015...`.

At the endpoints,

`Phi(0)=Phi(1)=0.36554578327397464521...`,

while

`Phi(theta_*)=0.69681541309816101230...`.

Hence two explicit subsequences have different limiting bounded corrections. Therefore

**there is no universal constant `K_0`.**

## 8. Oscillation theorem

### Phase-Oscillation Theorem

Assume

`a_k ~ c lambda^k k^(-5/2)`

for identity oriented trees. Let

`L=log lambda`,

`r=1/(lambda-1)`,

`u=lambda/(lambda-1)^2`.

Then the normalized second-order correction

`E(n)=L n/[n-m(n)]-log n-(3/2)log log n`

has nontrivial bounded phase oscillation. For every `theta in [0,1]`, there exists a subsequence along which

`E(n) -> Phi(theta)`

with

`Phi(theta)=-(3/2)log L-log c-log(r+theta)-L u/(r+theta)`.

In particular `E(n)` does not converge.

Moreover, under the standard cheapest-type packing characterization of minimum identity digraphs, the full accumulation interval is

`[Phi_min,Phi_max]`,

where

`Phi_min = 0.36554578327397464521...`,

`Phi_max = 0.69681541309816101230...`.

Thus

`liminf E(n)=Phi_min`,

`limsup E(n)=Phi_max`.

## 9. Endpoint consistency

The phase profile closes continuously from one layer to the next.

At `theta=1`,

`s(1)=lambda r`,

while at the next layer with `theta=0`, `s(0)=r`. The logarithmic shift is exactly compensated by the change in `beta=u/s`, giving

`Phi(1)=Phi(0)`.

So the effect is a genuine bounded lattice/partial-layer oscillation, not a discontinuity artifact of changing `K`.

## 10. Correct asymptotic statement

The strongest phase-free expansion remains

`delta(n)=L n/[log n+(3/2)log log n+O(1)]`,

or equivalently

`m(n)=n-L n/log n+(3/2)L n log log n/(log n)^2+O(n/(log n)^2)`.

The `O(1)` in the denominator cannot in general be replaced by a single constant plus `o(1)`.

A sharper form must retain the phase:

`delta(n)=L n/[log n+(3/2)log log n+Phi(theta_n)+o(1)]`,

where `theta_n` records the fractional occupation of the current extremal identity-tree layer (up to an asymptotically negligible exact-order filling error).

## 11. FCOA consequence

The sparsity frontier is now resolved through the bounded denominator scale:

1. `m(n)=n-Theta(n/log n)`;
2. exact leading coefficient `L=1.6580437722354153...`;
3. exact `+(3/2)L n log log n/(log n)^2` correction in `m(n)`;
4. no universal constant third term in the denominator;
5. instead, an explicit nonconstant phase profile `Phi` with oscillation amplitude

`Phi_max-Phi_min = 0.33126962982418636709...`.

This phase is caused by the discrete exponential growth of the number of available identity oriented-tree types and the macroscopic size of the final partially used layer.

## 12. Sources and scope

- Frank Harary and Robert W. Robinson, **Identity Digraphs of Minimum Size**, *Congressus Numerantium* 152 (2001), 139–147: classical minimum-size identity-digraph problem and `Theta(n/log n)` scale.
- Frank Harary and Michael S. Jacobson, **Destroying symmetry by orienting edges: complete graphs and complete bigraphs**, *Discussiones Mathematicae Graph Theory* 21 (2001), 149–158: relation to identity oriented forests/trees.
- OEIS **A102755**: number of asymmetric/identity oriented trees; records `A(x)=B(x)-B(x)^2` and `a_k ~ c lambda^k/k^(5/2)` with the constants used above.

The nonexistence proof is a deduction from the displayed enumerative asymptotic and the extremal cheapest-type packing structure. A separate literature audit is still required before any novelty claim for the explicit phase function itself.