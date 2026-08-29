# FCOA — Identity-Digraph Sparsity: exact second-order asymptotics

**Date:** 2026-08-28  
**Status:** theorem-level deduction from classical identity-digraph structure plus the enumerative asymptotics of identity oriented trees.  
**Novelty status:** **not claimed**. The minimum-size identity-digraph problem is classical (Harary–Robinson). The asymptotic expansion below should be treated as a derived consequence until a dedicated prior-art search establishes whether this precise expansion has appeared before.

## 1. Problem

Let `X_n={1,...,n}` and let `F` be a loopless directed relation,

`F subset X_n^2 \ Delta`.

Define

`m(n)=min{|F| : Stab_{S_n}(F)=1}`.

Equivalently, `m(n)` is the minimum number of arcs in an identity (asymmetric) loopless digraph of order `n`.

Write

`delta(n)=n-m(n)`.

Harary and Robinson established the classical scale

`m(n)=n-delta(n)`, with `delta(n)=Theta(n/log n)`.

The goal here is to determine the leading constant and the next logarithmic correction.

## 2. Why identity oriented trees control the positive deficit

Let `D` be any identity digraph and decompose it into weakly connected components `C_i`. Put

- `v_i=|V(C_i)|`,
- `a_i=|A(C_i)|`.

Because the underlying simple graph of every weak component is connected,

`a_i >= v_i-1`.

Hence

`v_i-a_i <= 1`.

Moreover, equality `v_i-a_i=1` holds if and only if `a_i=v_i-1`. Then the underlying simple graph has exactly `v_i-1` edges and is a tree, while no antiparallel pair can occur (a digon would consume an extra arc). Thus precisely the components contributing `+1` to `n-|F|` are **oriented trees**.

Since the whole digraph is identity:

1. every weak component is itself identity;
2. no two weak components are isomorphic.

Therefore every positive unit of `delta(n)` requires one distinct identity oriented-tree component. Components with cycles, digons, or any other excess arcs contribute at most zero to the deficit and cannot improve its leading packing efficiency.

Thus the asymptotics of `delta(n)` reduce to the maximum number of pairwise nonisomorphic identity oriented trees that can be packed into `n` vertices, up to a negligible exact-order filling error.

## 3. Enumeration input

Let

`a_k = number of nonisomorphic identity (asymmetric) oriented trees on k vertices`.

OEIS A102755 records

`1,1,1,4,10,37,135,522,2060,...`

and the generating-function relation

`A(x)=B(x)-B(x)^2`,

where `B(x)` is the rooted identity-oriented-tree series corresponding to A005753.

For the rooted series,

`B(x)=x product_{j>=1}(1+x^j)^(2 b_j)`

and equivalently

`B(x)=x exp(2 sum_{r>=1} (-1)^(r+1) B(x^r)/r)`.

The unrooted identity oriented-tree sequence has the asymptotic

`a_k ~ c lambda^k k^(-5/2)`,

with

`lambda = 5.249032491228170579164952216...`

and

`c = 0.17807103914078424643862998...`.

Only `lambda` and the exponent `5/2` are needed for the first two terms of `m(n)`.

## 4. Cheapest-type packing

To maximize the number of distinct identity oriented-tree components under a vertex budget, use tree types in increasing order of their order.

Define cumulative type count and cumulative vertex weight

`N_K = sum_{k<=K} a_k`,

`W_K = sum_{k<=K} k a_k`.

Since `lambda>1`, these sums are geometrically dominated by their top layer. From

`a_k ~ c lambda^k k^(-5/2)`

we obtain

`N_K ~ (lambda/(lambda-1)) c lambda^K K^(-5/2)`

and

`W_K = N_K (K+O(1))`

(in fact `W_K/N_K = K-1/(lambda-1)+o(1)`).

Thus at the packing threshold,

`t = N_K` components use

`n = W_K = t(K+O(1))`

vertices, while

`log n = K log lambda - (3/2) log K + O(1)`.

The exponent is `3/2`, not `5/2`, because multiplying the component count by its typical order `K` changes `K^(-5/2)` to `K^(-3/2)` in total vertex weight.

## 5. Inversion

Put

`L = log lambda`.

From

`log n = L K - (3/2) log K + O(1)`

we obtain

`L K = log n + (3/2) log log n + O(1)`,

hence

`K = [log n + (3/2) log log n + O(1)]/L`.

Since `t=n/(K+O(1))`, this gives

`delta(n) = n-m(n)`

with

`delta(n) = L n / [log n + (3/2) log log n + O(1)]`.

All logarithms here are natural.

Expanding the denominator,

`delta(n) = L n/log n - (3/2)L n log log n/(log n)^2 + O(n/(log n)^2)`.

Therefore

`m(n) = n - L n/log n + (3/2)L n log log n/(log n)^2 + O(n/(log n)^2)`.

Numerically,

`L = log(5.249032491228170579...) = 1.6580437722354153...`,

and

`(3/2)L = 2.487065658353123...`.

## 6. Main theorem

### Second-order Identity-Digraph Sparsity Theorem

For the loopless directed-relation problem

`m(n)=min{|F| : F subset X_n^2\Delta, Stab_{S_n}(F)=1}`,

let

`lambda=5.249032491228170579164952216...`

be the exponential growth constant of identity oriented trees. Then

`n-m(n) = (log lambda)n/[log n+(3/2)log log n+O(1)]`.

Equivalently,

`m(n)=n-(log lambda)n/log n+(3/2)(log lambda)n log log n/(log n)^2+O(n/(log n)^2)`.

In particular,

`n-m(n) ~ C n/log n`

with the exact coefficient

`C=log lambda=1.6580437722354153...`.

## 7. Exact-order filling does not change the expansion

The greedy packing argument naturally produces a vertex budget `<=n`. At the final threshold, after taking all cheaper types and a suitable number from the next order, the unused budget is `O(K)=O(log n)`.

For exact order `n`, reserve directed-path tree types as fillers. Excluding at most one path type per relevant order costs only `O(log n)` components. A leftover of order `O(log n)` can then be filled by a reserved identity directed path (or, after combining with one omitted component, by a path of a fresh larger order). This changes the component count by at most `O(log n)`, which is

`o(n/(log n)^2)`.

Therefore the exact-order requirement is absorbed by the displayed remainder term.

## 8. Relation to the classical literature

- Frank Harary and Robert W. Robinson, **Identity Digraphs of Minimum Size**, *Congressus Numerantium* 152 (2001), 139–147: the minimum-size identity-digraph problem is classical and `m(n)=n-Theta(n/log n)` is not a novelty claim of FCOA.
- Frank Harary and Michael S. Jacobson, **Destroying symmetry by orienting edges: complete graphs and complete bigraphs**, *Discussiones Mathematicae Graph Theory* 21 (2001), 149–158: connects minimum symmetry-destroying orientations of complete graphs to identity oriented forests.
- OEIS **A102755**: number of asymmetric/identity oriented trees; records `A(x)=B(x)-B(x)^2` and `a_k ~ c lambda^k/k^(5/2)` with `lambda=5.249032491228170579...`.
- OEIS **A005753**: rooted identity-oriented-tree counterpart; records the product/exponential generating equation and the same exponential growth constant.

## 9. FCOA consequence

The sparse rigid fiber problem is now sharpened from

`m(n)=n-Theta(n/log n)`

to an explicit second-order expansion. In the two-output maximum-VRI construction, a fully rigid value fiber cannot be substantially sparser than the directed-path `n-1` construction in its leading linear term; the optimal saving is

`1.658043772... n/log n`

to first correction, with a forced positive `n log log n/(log n)^2` correction in `m(n)`.

The next unresolved refinement is the **constant term inside the denominator**:

`n-m(n) = L n/[log n+(3/2)log log n + K_0 + o(1)]`.

Determining `K_0` requires the amplitude `c`, the geometric-tail correction `1/(lambda-1)`, and a careful treatment of the discrete partial-layer / exact-order packing oscillation. It is not automatically guaranteed that a single constant `K_0` exists without bounded periodic or lattice fluctuations.