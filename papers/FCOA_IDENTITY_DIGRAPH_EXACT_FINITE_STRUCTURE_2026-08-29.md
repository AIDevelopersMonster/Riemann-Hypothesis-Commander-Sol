# FCOA — Exact finite structure of the minimum identity-digraph size

**Date:** 2026-08-29  
**Status:** theorem-level finite formula and constructive algorithm.  
**Novelty status:** **not claimed** pending dedicated comparison with Harary–Robinson and subsequent literature.

## 1. Problem

For `X_n={1,...,n}`, define

`m(n)=min{|F| : F subset X_n^2\Delta, Stab_{S_n}(F)=1}`.

Write

`delta(n)=n-m(n)`.

Previous work reduced every positive unit of `delta(n)` to a distinct identity oriented-tree weak component.

Let

`a_k = number of nonisomorphic identity oriented trees of order k`.

Define cumulative counts

`A_K = sum_{j<=K} a_j`

and cumulative vertex weights

`W_K = sum_{j<=K} j a_j`.

## 2. Exact threshold theorem

Let `K` be the unique positive integer such that

`W_{K-1} <= n < W_K`.

Put

`q = floor((n-W_{K-1})/K)`.

Then

`0 <= q < a_K`.

### Exact theorem

For every `n>=1`,

`delta(n)=A_{K-1}+q`,

and therefore

`m(n)=n-A_{K-1}-floor((n-W_{K-1})/K)`.

Equivalently,

`m(n)=n-delta(n)`

with

`delta(n)=A_{K-1}+floor((n-W_{K-1})/K)`.

## 3. Proof: upper bound on the number of positive-deficit components

Let `D` be any identity digraph of order `n`, decomposed into weak components.

For a component with `v` vertices and `a` arcs, weak connectivity gives

`a>=v-1`.

Thus its contribution to `n-|F|` is at most `1`, with equality only when `a=v-1`, i.e. precisely when the component is an oriented tree.

Since the whole digraph is identity:

1. each weak component is itself identity;
2. no two weak components are isomorphic.

Therefore, if `delta(D)=n-|F(D)|=t>0`, the digraph contains at least `t` pairwise nonisomorphic identity oriented-tree components.

Among all choices of `t` distinct identity oriented trees, the minimum possible number of vertices is obtained by taking tree types in nondecreasing order of their order. Hence:

- all `a_j` types of orders `j<K` cost exactly `W_{K-1}` vertices and contribute `A_{K-1}` components;
- every additional component costs at least `K` vertices.

Thus no identity digraph of order `n<W_K` can have more than

`A_{K-1}+floor((n-W_{K-1})/K)`

positive-deficit components.

Hence

`delta(n) <= A_{K-1}+q`.

## 4. Proof: exact construction

Take:

1. every identity oriented-tree isomorphism type of order `<K`;
2. any `q` distinct identity oriented-tree types of order `K`.

This uses

`N_0=W_{K-1}+qK`

vertices and has

`t=A_{K-1}+q`

components, hence exactly

`N_0-t`

arcs.

Let

`r=n-N_0`, so `0<=r<K`.

If `r=0`, this forest already has exact order `n`.

If `r>0`, stretch one selected component without changing the number of components: replace one selected identity tree by a directed path on `r` additional vertices.

A directed path is identity. Choosing its new order so that it is not isomorphic to any other retained component preserves pairwise nonisomorphism and global identity. Since replacing one tree component by another tree component changes vertices and arcs by the same amount, the deficit remains exactly one for that component.

Hence exact order `n` is achieved with the same component count `t` and therefore with

`delta(n)>=t`.

Combined with the upper bound,

`delta(n)=t=A_{K-1}+q`.

## 5. Algorithmic consequence

Computing `m(n)` does **not** require a general subset-sum or knapsack search.

All items have the same value `1` (one unit of deficit), so the exact extremum is a threshold packing:

1. generate `a_1,a_2,...` until `W_K>n`;
2. identify the threshold order `K`;
3. compute

   `q=floor((n-W_{K-1})/K)`;

4. return

   `m(n)=n-A_{K-1}-q`.

The optimization itself is therefore `O(K)` once the counts `a_k` are known.

## 6. Internal generation of `a_k`

Let

`B(x)=sum_{n>=1} b_n x^n`

be the rooted identity-oriented-tree generating series satisfying

`B(x)=x exp(2 sum_{r>=1} (-1)^(r+1) B(x^r)/r)`.

Write

`H(x)=2 sum_{r>=1} (-1)^(r+1) B(x^r)/r`

and

`exp(H(x))=sum_{m>=0} e_m x^m`.

Since `B(x)=x exp(H(x))`,

`b_{m+1}=e_m`.

If

`s_m = m[x^m]H(x) = 2 sum_{d|m} (-1)^(m/d+1) d b_d`,

then the standard exponential-series recurrence gives

`m b_{m+1} = sum_{k=1}^m s_k b_{m-k+1}`.

Thus the rooted counts are generated recursively with exact integer arithmetic.

For unrooted identity oriented trees,

`A(x)=B(x)-B(x)^2`,

so

`a_n=b_n-sum_{i=1}^{n-1} b_i b_{n-i}`.

This yields the prefix

`1,1,1,4,10,37,135,522,2060,8430,35115,149286,...`,

matching OEIS A102755.

## 7. Exact finite examples

The autonomous calculator gives:

- `m(10)=6`, `delta(10)=4`;
- `m(1000)=846`, `delta(1000)=154`;
- `m(10^6)=911561`, `delta(10^6)=88439`;
- `m(10^12)=950477504026`, `delta(10^12)=49522495974`.

The threshold orders are tiny because the number of identity oriented-tree types grows exponentially:

- for `n=10^6`, `K=12`;
- for `n=10^12`, `K=21`;
- for a 50-digit input `n=10^50`, `K=75`.

Therefore exact evaluation is practical even for enormous integer `n`.

## 8. Constructive output versus numeric output

The formula determines `m(n)` exactly from the counts `a_k` alone.

To output an explicit extremal relation `F`, one additionally needs canonical representatives of the selected identity oriented-tree types. This is a separate generation/canonical-labeling problem.

For the scalar extremal value `m(n)`, no representative enumeration is necessary.

## 9. Implementation

The repository contains

`experiments/fcoa_identity_exact_m.py`

which:

- generates rooted and unrooted identity-oriented-tree counts internally;
- verifies a published prefix of A102755;
- computes the threshold formula exactly using arbitrary-precision integers;
- reports the symbolic optimal component recipe;
- includes a self-test.

Example:

`python experiments/fcoa_identity_exact_m.py --self-test`

and

`python experiments/fcoa_identity_exact_m.py 1000000000000`.

## 10. Consequence for the programme

The finite extremal problem is no longer merely asymptotic.

Once the enumerative sequence `a_k` is accepted, the exact value `m(n)` is governed by the cumulative staircase

`W_K=sum_{j<=K} j a_j`.

The only remaining genuinely harder computational problem is not the number `m(n)` itself, but the explicit generation of a canonical optimal rigid fiber `F` for a prescribed large `n`.