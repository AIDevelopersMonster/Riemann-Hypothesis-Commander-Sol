# HATTER-SOL-07 — continuity / handoff status

**Branch:** `research/hatter-sol-free-ports`  
**Path:** `papers/HATTER-SOL/07-FREE-PORT-FACTORIZATION/`  
**Status date:** 2026-09-12  
**Status:** active research; first nontrivial structural theorem obtained; publication threshold not yet declared.

## Core model

Treat a factor `m` as a capacity-`m` node. For a connected simple graph `G=(V,E)` with factor capacities `a_v>=2`, define free boundary

\[
B(G,\mathbf a)=\sum_v(a_v-\deg_G v)=\sum_v a_v-2|E|.
\]

For a tree,

\[
B(T,\mathbf a)=2+\sum_v(a_v-2).
\]

Hence the original chain quantity `F=\sum(a_i-2)` is exactly the tree free boundary after designating two global terminals as input/output.

## New result 1 — fixed-decomposition spectrum

For a fixed decomposition `\mathbf a=(a_1,...,a_k)`, let

\[
M_c(\mathbf a)=\max\{|E(G)|:\;G\text{ connected, simple, }\deg(v_i)\le a_i\}.
\]

Then

\[
\boxed{
\mathcal B(\mathbf a)
=\{\sum_i a_i-2e:\;k-1\le e\le M_c(\mathbf a)\}.
}
\]

So every fixed decomposition has a complete parity interval of boundary values. Any holes in the global integer spectrum must arise when the spectra of different multiplicative decompositions are united.

Proof: choose a maximum-edge admissible connected graph and a spanning tree inside it; adding arbitrary subsets of the extra edges realizes every intermediate edge count.

## New result 2 — refinement inversion theorem

The tree-only model has strict refinement monotonicity: replacing `ab` by `a,b` decreases tree free boundary by

\[
(ab-2)-[(a-2)+(b-2)]
=(a-1)(b-1)+1>0.
\]

But this monotonicity fails in the general connected-simple-network model.

For every odd `q>=3` and every `m>=2q`, define

\[
\mathbf A=(2q,2^m)
\]

meaning one capacity-`2q` node and `m` capacity-two nodes, and refine it to

\[
\mathbf A'=(q,2^{m+1}).
\]

Then

\[
\boxed{\lambda(\mathbf A)=0,\qquad \lambda(\mathbf A')=1,}
\]

where `\lambda` is minimum free boundary over connected simple capacity-respecting networks.

The coarse network is fully saturable by using the `2q` hub to close `q` disjoint paths of capacity-two vertices. The refined total capacity is odd, forcing boundary at least one; an explicit bouquet-of-triangles plus one tail realizes boundary exactly one.

See `REFINEMENT_INVERSION.md` for the full proof.

## Arithmetic corollary

For odd prime `q` and `m>=2q`, let

\[
n=q2^{m+1}.
\]

The full prime decomposition `(q,2^{m+1})` has minimum boundary one, whereas the coarser decomposition `(2q,2^m)` has minimum boundary zero.

Thus

\[
\boxed{\text{complete prime refinement need not minimize free boundary}.}
\]

The first explicit member obtained in the search is

\[
384=3\cdot2^7,
\]

with prime-resolution minimum `1`, while

\[
384=6\cdot2^6
\]

has a saturated boundary-zero realization.

Do not call `384` the globally smallest refinement-inversion integer unless a separate exhaustive proof is recorded.

## Conceptual hinge

The programme has moved beyond the chain identity. There is now a genuine competition:

\[
\boxed{
\text{multiplicative refinement}
\quad\text{vs}\quad
\text{topological closure / cycle capacity}.
}
\]

Refining a factor exposes more arithmetic structure, but it can destroy a parity or graphical condition required to saturate all ports. Hence "more factorized" no longer means "less free boundary" once topology is allowed to reorganize.

## Prior-art caution

There is classical literature encoding natural numbers by rooted trees through recursive prime factorization (Matula-Goebel numbers / Matula numbering), and a large classical theory of graphical degree sequences and bounded-degree graph realization. These must be discussed in a future literature audit. No priority claim is made yet for the broad idea "factorization represented by a graph".

The candidate novel object here is narrower: multiplicative decompositions as vertex-capacity multisets, free boundary under connected simple wiring, and behavior of that boundary under multiplicative refinement.

## Immediate next strike

1. Characterize when `\lambda(\mathbf a)=0` (full port saturation) in terms of graphical sequences dominated by the capacity vector.
2. Determine the exact effect of a one-step refinement `ab -> a,b` on `\lambda`: can the increase exceed `1`, or is refinement inversion universally parity-limited?
3. Determine the globally smallest `n` admitting refinement inversion, with a certified exhaustive search/proof.
4. Characterize global spectrum

\[
\mathcal B(n)=\bigcup_{\prod a_i=n}\mathcal B(\mathbf a)
\]

and decide which parity/arithmetic gaps can occur between decomposition spectra.
5. Separate what follows immediately from classical b-matching / graphical-sequence theorems from what is genuinely arithmetic in the factorization poset.

## Claim discipline

- The handshake identity, cycle-rank formula, graphical-sequence facts, Matula-Goebel encoding, and additive functions such as `sopfr` and `Omega` are classical or elementary and are not claimed as new.
- `m` ports for factor `m` is a chosen model, not a canonical interpretation of multiplication.
- The current theorem is structural inside this model; it is not a primality test or factorization algorithm.
- Publication gate remains open pending literature audit and at least one sharper characterization or extremal theorem.
