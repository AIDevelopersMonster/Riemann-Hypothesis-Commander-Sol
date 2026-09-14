# HATTER-SOL-15 · Pairwise Cocycle and Planar Diagnostics

**Status:** exact theorem layer, with standard group-synchronization machinery separated from the arithmetic specialization.

Let the fixed unramified rational prime `q` have `p` Galois branches

\[
P_i,\qquad i\in\mathbb F_p,
\]

with reflection involutions

\[
\tau_i=r^{2i}s.
\]

Define the relative transport between branches by

\[
\boxed{g_{ij}:=\tau_i\tau_j=r^{2(i-j)}\in C_p.}
\]

## Theorem H15.12 — exact branch cocycle

For all `i,j,k`,

\[
\boxed{g_{ij}g_{jk}=g_{ik}.}
\]

Equivalently,

\[
\boxed{g_{ij}g_{jk}g_{ki}=1.}
\]

### Proof

Directly,

\[
g_{ij}g_{jk}
=r^{2(i-j)}r^{2(j-k)}
=r^{2(i-k)}
=g_{ik}.
\]

The triangle-holonomy identity follows by multiplying by `g_{ki}`. QED.

This is the exact group-synchronization/cycle-consistency law for the branch transports. The general law is classical; the H15-specific point is that these ratios arise canonically from decomposition involutions of one fixed arithmetic prime.

## Theorem H15.13 — reconstruction on a connected transport graph

Let `H` be any connected graph on the `p` branches and suppose every oriented edge `(i,j)` carries its exact label `g_ij`.

Then the branch coordinates in `C_p` are reconstructible from the edge labels up to one common global left factor.

### Proof

Choose a root `0` and set its coordinate to the identity. For any vertex `i`, choose a path

\[
0=v_0,v_1,\ldots,v_m=i
\]

and define

\[
x_i:=g_{v_m v_{m-1}}\cdots g_{v_1v_0}.
\]

Cycle consistency makes this independent of path. Then

\[
g_{ij}=x_i x_j^{-1}.
\]

Changing the root coordinate multiplies all `x_i` by the same group element, which is the only ambiguity. QED.

## Corollary H15.14 — trees synchronize but cannot self-diagnose

A spanning tree with `p-1` relative transports is sufficient for coordinate reconstruction.

However, a tree has no cycles, so **every** assignment of edge labels is compatible with some set of vertex coordinates. Therefore no purely internal cycle-consistency observer on a tree can detect even one corrupted edge label.

Thus

\[
\boxed{\text{synchronization does not imply self-diagnosis}.}
\]

## Corollary H15.15 — one cycle detects but does not localize one edge error

On a simple cycle, the product of edge transports around the cycle must equal `1`.

If exactly one edge label is replaced by an incorrect value, the cycle holonomy becomes nontrivial, so the error is detected.

But every edge belongs to the same unique cycle, hence the syndrome does not identify which edge failed.

Thus a single cycle gives detection without localization.

## Theorem H15.16 — planar wheel localizes and repairs one corrupted transport

Assume `p>=5`. After an oriented two-branch synchronization has supplied a cyclic ordering of the branch set, build the wheel graph `W_p`:

- choose one branch as center;
- arrange the remaining `p-1` branches on a rim cycle;
- retain all `p-1` spokes and all `p-1` rim edges.

The wheel is planar and has

\[
V=p,
\qquad
E=2p-2,
\qquad
\beta_1=E-V+1=p-1,
\qquad
\gamma=0.
\]

For every triangular face `F`, let its diagnostic syndrome be the ordered product of edge transports around `F`.

If exactly one undirected edge label is corrupted, with the reverse orientation kept as its inverse, then:

1. every face not incident with that edge still has trivial holonomy;
2. every face incident with the corrupted edge has nontrivial holonomy;
3. the set of failed triangular faces identifies the corrupted edge uniquely;
4. once localized, the correct edge label is reconstructed from either incident triangle using the two correct labels on the other sides.

### Proof

A rim edge is incident with exactly one triangular face; therefore its syndrome is a unique singleton face.

A spoke is incident with exactly two adjacent triangular faces; different spokes determine different adjacent-face pairs when the rim length `p-1>=4`.

Hence the failed-face set uniquely distinguishes every edge: singleton syndromes are rim edges, adjacent-pair syndromes are spokes. The cocycle equation on an incident triangle then solves uniquely for the missing/corrupted label. QED.

## 5. Surface hierarchy

The same arithmetic world therefore admits the exact diagnostic ladder

\[
\boxed{
\begin{array}{c|c|c}
\text{transport carrier} & \text{capability} & \text{genus}\\
\hline
\text{tree} & \text{reconstruct only} & 0\\
\text{single cycle} & \text{detect one error} & 0\\
\text{wheel} & \text{localize + repair one error} & 0
\end{array}}
\]

The distinction is not genus. It is the amount and arrangement of cycle redundancy.

Safe conceptual statement:

\[
\boxed{\text{self-diagnostic memory can be carried by planar cycle redundancy rather than topological genus}.}
\]

## 6. Claim boundary and prior art

The abstract equivalence between pairwise group ratios, global synchronization up to gauge, and cycle consistency is standard in group-synchronization literature. H15 does not claim that general machinery as new.

The H15-specific synthesis is:

1. the vertices are prime branches of one fixed rational prime in a dihedral Galois world;
2. the edge ratios are products of arithmetic decomposition involutions;
3. two branches generate the internal cyclic frame;
4. a planar redundancy carrier already suffices for exact single-edge diagnosis and repair.

No physical communication, biological network, or quantum mechanism is asserted.