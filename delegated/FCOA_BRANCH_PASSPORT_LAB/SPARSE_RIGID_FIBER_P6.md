# Sparse Rigid Fiber Extremality — P6

**Laboratory:** FCOA — SOL-PASSPORT  
**Problem:** determine the minimum number of special cells needed for a rigid two-output fiber inside a maximally symmetric off-diagonal domain  
**Parameter:**

`m(n) = min{|F| : F subset {(i,j): i!=j}, Stab_{S_n}(F)=1}`.

Equivalently, `m(n)` is the minimum number of arcs in a loopless directed graph on `n` labeled vertices with trivial automorphism group.

## 1. Immediate consequences

A directed Hamilton path gives

`m(n) <= n-1`.

A naive incidence argument gives only

`m(n) >= ceil((n-1)/2)`,

because at most one vertex may be isolated and each arc touches at most two vertices.

That bound is far from sharp.

## 2. Weak-component decomposition

Let `F` be rigid and decompose its underlying weak graph into nontrivial weak components

`C_1,...,C_c`

plus possibly one isolated vertex.

Rigidity forces two conditions:

1. every `C_i` is itself rigid;
2. no two `C_i` are isomorphic as directed graphs.

Otherwise an internal component automorphism or a swap of two isomorphic components would give a nontrivial automorphism of `F`.

If `v_i` and `e_i` denote the number of vertices and arcs of `C_i`, weak connectivity gives

`e_i >= v_i-1`.

Hence, with `t in {0,1}` isolated vertices,

`|F| = sum e_i >= (n-t)-c >= n-1-c`.

Thus saving arcs below the Hamilton-path value is equivalent to packing many pairwise nonisomorphic rigid weak components.

## 3. Upper bound construction: save Omega(n/log n) arcs

There are exponentially many pairwise nonisomorphic rigid oriented trees of linear size.

An explicit family is obtained from a directed spine

`p_0 -> p_1 -> ... -> p_k`

and one pendant leaf `q_i` attached to each spine point `p_i`. For each bit `b_i`, orient the pendant edge as either

`p_i -> q_i`

or

`q_i -> p_i`.

The underlying degree pattern preserves the spine set; the directed spine fixes every spine vertex pointwise; then every pendant leaf is fixed. Hence every such oriented tree is rigid.

Different bit strings give nonisomorphic directed trees because the directed spine has no nontrivial automorphism and the pendant-edge directions recover the bit string position by position.

For `k+1` bits this gives

`2^(k+1)`

pairwise nonisomorphic rigid oriented trees, each on

`2k+2`

vertices and exactly

`2k+1 = (2k+2)-1`

arcs.

Choose

`c = floor(a n/log n)`

for a sufficiently small absolute constant `a>0`, and choose `k=Theta(log n)` so that at least `c` distinct trees of the above family are available and their total number of vertices is at most, say, `n/2`.

Use `c` distinct rigid tree components and put all remaining vertices into one additional directed path component of a different order (or leave one isolated vertex when necessary). All components are rigid and pairwise nonisomorphic.

The resulting union is rigid and has

`n - Theta(n/log n)`

arcs.

Therefore

`m(n) <= n - Omega(n/log n)`.

## 4. Lower bound: no linear-fraction saving

We prove

`m(n) >= n - O(n/log n)`.

If `m(n) >= n`, there is nothing to prove. So consider a rigid `F` with `m<n` arcs.

Using the notation above, define the excess of a component by

`r_i = e_i-(v_i-1) >= 0`.

Then

`R = sum r_i = m - (n-t-c)`.

Since `m<n` and `t<=1`,

`R < c+1`.

Therefore fewer than about half of the components can have excess at least `2`; more precisely, all but at most `R/2` components have `r_i in {0,1}`. Hence at least `(c-O(1))/2` components are directed trees or weakly connected one-excess digraphs.

For each order `s`, the number of isomorphism types of such low-excess directed components is at most exponential in `s`:

`N_s <= A^s`

for some absolute constant `A`.

Reason:

- for excess `0`, the underlying weak graph is a tree; the number of unlabeled trees grows exponentially, and each tree has at most `2^(s-1)` orientations;
- for excess `1`, the underlying weak graph is a tree or unicyclic graph with one additional directed choice; unlabeled unicyclic graphs are also exponentially numerous, and orientations contribute only another exponential factor.

Thus the total number of available low-excess component types on fewer than `L` vertices is at most `A'^{L}` for some constant `A'>1`.

Because our low-excess components must be pairwise nonisomorphic, if there are `k=Theta(c)` of them then a positive fraction must have order at least

`Omega(log k)`.

Consequently

`n >= Omega(k log k) = Omega(c log c)`.

Hence

`c = O(n/log n)`.

Returning to the component edge bound,

`m >= n-1-c`,

we obtain

`m(n) >= n - O(n/log n)`.

## 5. Asymptotic theorem

Combining the two bounds:

`m(n) = n - Theta(n/log n)`.

Therefore:

- `m(n)=o(n)` is impossible;
- `m(n)=O(log n)` is impossible;
- in fact `m(n)/n -> 1`;
- the directed-path construction with `n-1` special cells is asymptotically optimal in its leading linear term;
- one can nevertheless save `Theta(n/log n)` cells by decomposing the rigid fiber into many pairwise nonisomorphic rigid components.

## 6. Consequence for two-output maximal VRI

In P5, maximal VRI `n!` was obtained by taking `Omega_+` on a rigid fiber `F` and `Omega_-` on its complement inside the complete off-diagonal domain.

P6 therefore gives the asymptotically optimal sparsity of the small distinguished fiber needed by that mechanism:

`|F|_min = n - Theta(n/log n)`.

So maximal value-rigidity with two outputs cannot be carried by a sublinear number of specially colored cells in this exact complete-domain / rigid-fiber model.

## 7. Prior-art discipline

The general extremal theory of asymmetric undirected graphs is classical; work going back to Erdos-Renyi and Quintas studies minimum and maximum edge counts of asymmetric graphs. The present parameter is the loopless directed/oriented-fiber version used by the FCOA passport laboratory.

No novelty claim is made here without a dedicated prior-art audit for sparse asymmetric digraphs and oriented graphs.
