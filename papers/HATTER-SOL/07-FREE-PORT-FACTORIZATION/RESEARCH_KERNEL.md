# Research kernel — free-port factorization

## 1. Basic chain model

For an integer node of capacity `m>=2`, reserve one port for input and one for output. Define

\[
f(m)=m-2.
\]

For an ordered factorization

\[
\mathbf a=(a_1,\ldots,a_k),\qquad a_i\ge2,\qquad \prod_i a_i=n,
\]

define

\[
F(\mathbf a)=\sum_{i=1}^k(a_i-2).
\]

A refinement step replaces one factor `ab` by `a,b` with `a,b>=2`.

## 2. Strict refinement monotonicity

For a single refinement,

\[
\Delta(a,b)
:=F(\ldots,ab,\ldots)-F(\ldots,a,b,\ldots)
=ab-a-b+2
=(a-1)(b-1)+1>0.
\]

Hence `F` strictly decreases along every proper multiplicative refinement.

### Corollary

For fixed `n>=2`, the one-node decomposition `(n)` uniquely maximizes `F`, while complete prime factorizations minimize it.

For

\[
n=\prod_{j=1}^r p_j
\]

with multiplicity,

\[
F_{\min}(n)=\sum_j(p_j-2).
\]

## 3. Organization cost

For a decomposition `\mathbf a` define

\[
C_n(\mathbf a):=(n-2)-F(\mathbf a).
\]

Then `C_n` is strictly increasing under proper refinement.

At prime resolution,

\[
C_{\max}(n)
=(n-2)-\sum_j(p_j-2).
\]

Interpretive label only: “organization cost”. This is not currently claimed as a new arithmetic invariant.

## 4. First generalization: arbitrary connected wiring

The chain convention spends exactly two ports per node, but a graph model should instead assign each factor-node `v` a capacity `a_v` and use one port for each incident internal edge.

For a finite graph `G=(V,E)` with node capacities `a_v`, define total free boundary

\[
B(G,\mathbf a)
:=\sum_{v\in V}(a_v-\deg_G v).
\]

Therefore

\[
\boxed{B(G,\mathbf a)=\sum_{v\in V}a_v-2|E|.}
\]

This is the first topology-independent balance identity.

If `G` is connected with `k=|V|`, then `|E|>=k-1`, hence

\[
B(G,\mathbf a)\le \sum_v a_v-2(k-1),
\]

with equality exactly for trees.

Thus among connected simple wirings on a fixed factor multiset, trees maximize free boundary; each extra cycle consumes two additional free ports.

This is mathematically elementary, but it is the correct general backbone for the model.

## 5. New research hinge

The chain formula alone collapses to standard additive functions. The promising object is the pair

\[
(\text{multiplicative refinement},\ \text{wiring topology}).
\]

Questions:

1. For fixed `n`, what boundary values are realizable over all multiplicative decompositions and connected wirings?
2. Is the realizable boundary spectrum an interval, or can it have arithmetic gaps?
3. What changes if each factor-node must remain locally connected after refinement?
4. Can one define a refinement operation preserving selected external terminals and obtain a nontrivial minimal-cost theorem?
5. For prime-resolution nodes `p_j`, what graph topologies maximize/minimize boundary under degree constraints `deg(v)<=p_j`?
6. Do small primes (`2`, `3`) create graph-theoretic bottlenecks that reflect multiplicative structure in a genuinely useful way?

## 6. Immediate observation about 2

A prime node `2` has capacity two. In a chain interior it has zero free ports. In a general connected graph it cannot have degree greater than two, so at prime resolution every factor `2` is forced to be a path/cycle-type vertex rather than a branching vertex.

Thus the 2-adic valuation `v_2(n)` constrains the number of degree-at-most-two vertices available in every prime-factor network for `n`.

Whether this leads to a useful invariant is open.

## 7. Immediate observation about 3

A prime node `3` supports at most ternary incidence. In a tree, a degree-three `3`-node has no boundary port; degree two leaves one; degree one leaves two.

Hence the multiset of prime factors controls the possible degree sequence of any capacity-respecting factor tree.

This turns prime factorization into a degree-capacity budget.

## 8. Candidate next theorem

Characterize when a multiset of factor capacities `a_1,...,a_k` admits a connected tree using **all ports internally**, i.e.

\[
\deg(v_i)=a_i
\]

for every node.

For a tree this requires

\[
\sum_i a_i=2(k-1).
\]

Since every `a_i>=2`, the left side is at least `2k`, while the right side is `2k-2`, so it is impossible.

Therefore every finite connected factor tree with capacities at least two necessarily has at least two free boundary ports.

More strongly,

\[
B(T,\mathbf a)=\sum_i(a_i-2)+2.
\]

This shows that the earlier chain quantity `F=\sum(a_i-2)` differs from actual tree boundary by a universal `+2`: the chain's designated global input/output are precisely those two ports.

That identifies the chain model as a tree boundary model with two distinguished terminals.

## 9. Publication gate

Not reached. Current results are a clean formalization and a small structural kernel. Continue research until there is a theorem about realizability, extremality, or rigidity that is not merely degree-sum bookkeeping or a restatement of known additive arithmetic functions.
