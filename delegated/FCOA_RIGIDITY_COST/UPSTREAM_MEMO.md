# FCOA Rigidity Cost — Upstream Memo

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Audience:** main Commander Sol scientific director  
**Status:** local results proposed for upstream review; nothing here modifies M0–G4 automatically.

## Executive verdict

Eight results from this direction are strong enough for upstream review.

### U1. Rigidity cost is not successor-memory cost

For generic size `n=N-1`, exact directed rigidity minima through `n=7` are `(1,1,2,3,3,4)`, with

\[
\lceil(n-1)/2\rceil\le r_\to(n)\le n-2.
\]

G2 spends `n-1` cells to retain a chosen successor path, not merely to kill automorphisms.

### U2. Terminal Generic Layer Master Lemma

For `m` new off-diagonal generic cells with terminal outputs,

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=(4(N-1)+m,0,N^2+2N-2+m,N^2+N-2+m,N^3+N^2-4N+9-3m).
\]

Commutation has the exact reverse-cell equality correction. Hence Association Spectrum and commutation are coarse relative to terminal-fiber geometry.

### U3. Same G4-C coarse invariants, but rigidity instead of C2

The asymmetric non-self-converse tournament `T5={40,41,42,43,20,21,31,32,03,10}` gives a balanced complete two-anonymous-output zero-anchor layer with the same Association Spectrum and commutation as G4-C but generic group `1` instead of `C2`. Universal-source extension gives such a layer for every `n>=5`.

### U4. Minimal separator: cyclic-triangle defect

For tournament layers,

\[
\tau_3(T)=\#\{C_3\text{ induced triples}\}
\]

satisfies `tau3(G4-C)=0`, anonymous rigidity requires `tau3>=2`, and the U3 family attains exactly `2` for every `n>=5`.

### U5. Histograms versus abstract half-reconstruction

There is an explicit seven-vertex pair `S7/R7` with identical anonymous induced histograms at every proper order `k=3,4,5,6` but residual groups `C2` and `1`. Classically, finite tournaments are `(<=7)`-half-reconstructible, with 7 optimal for the stronger subset-indexed abstract hemimorphism data model.

### U6. Tournament specialization: exact ternary betweenness

For tournament-type opposite fibers,

\[
B_\star(x,y,z)\iff x\star y=y\star z=x\star z
\]

is carrier-exact:

\[
\operatorname{Aut}(B_T)=\operatorname{Aut}^{\pm}(T).
\]

Full proof and the factorial failure of the weaker C3-hypergraph are in `BETWEENNESS_REDUCT.md`.

### U7. Universal binary ternary phase reduct

For every complete off-diagonal layer with exactly two anonymous terminal outputs,

\[
Q_\star(x,y,z)\iff x\star y=y\star z
\]

is carrier-exact:

\[
\operatorname{Aut}(Q_\star)=\operatorname{Aut}^{\pm}(c).
\]

The proof uses a binary discrepancy bit on ordered cells and connectivity of the composable-cell graph. Tournament and balanced assumptions are unnecessary. Full proof is in `UNIVERSAL_TERNARY_PHASE_REDUCT.md`.

### U8. Multicolor arity phase transition

The binary theorem is sharp in alphabet size. For `q>=3`, ternary anonymous equality information is no longer universally exact.

#### Explicit q=3 lower-bound witness

Use the symmetric complete layer on vertices `0,1,2,3,4`, so opposite ordered cells have the same color. On the ten unordered edges in lexicographic order

\[
01,02,03,04,12,13,14,23,24,34,
\]

use colors

\[
\boxed{0,0,0,1,0,0,2,1,0,0.}
\]

Thus

\[
C_0=\{01,02,03,12,13,24,34\},\quad
C_1=\{04,23\},\quad
C_2=\{14\}.
\]

The carrier permutation

\[
g=(0\ 1)
\]

preserves the **entire labeled anonymous equality pattern on every subset of at most three vertices**, but it is not induced by one global color permutation: edge `04` forces colors `1` and `2` to exchange, while fixed edge `23` forces color `1` to remain fixed.

Exact finite audit gives

\[
\boxed{
|\operatorname{Aut}^{an}(c)|=2,
\qquad
|\operatorname{Aut}(R_{\le3}^{eq}(c))|=4.
}
\]

So even the maximal ternary local equality passport is not stabilizer-complete at `q=3`. The witness extends to every fixed `q>3` by adding fixed vertices carrying fresh colors.

#### Universal q-color upper bound

For arbitrary finite `q`, define the four-ary relation

\[
\boxed{
E_\star(x,y,u,v)\iff x\star y=u\star v.
}
\]

This is the equality partition of all ordered cells. By the Fiber-Transport principle,

\[
\boxed{
\operatorname{Aut}(E_\star)=\operatorname{Aut}^{an}(c)
}
\]

for every surjective q-color layer.

Therefore, in the class of reducts determined by anonymous equality patterns on bounded-size carrier subsets,

\[
\boxed{
q=2:\ k_{exact}=3,
\qquad
q\ge3:\ k_{exact}=4.
}
\]

This is an exact **arity phase transition**. Two colors are exceptional because local inequality determines the unique opposite phase. With three or more colors, locally compatible color permutations can disagree on colors not jointly witnessed; a fourth carrier variable is needed to compare disjoint cells directly.

Full theorem, witness, proof and scope firewall are in `MULTICOLOR_ARITY_THRESHOLD.md`.

## Current structural hierarchy

\[
\boxed{
\begin{array}{rcl}
q=2 &:& \text{ternary phase propagation is exact},\\
q\ge3 &:& \text{ternary local equality has gauge freedom},\\
q\ge3 &:& \text{four-ary arbitrary-cell equality is exact}.
\end{array}}
\]

This is independent of tournament geometry and balancedness.

## Recommendation

Recommend upstream hostile audit of U8 together with U7. The q=3 lower-bound witness should be independently re-enumerated before publication-level use; the four-ary upper bound is immediate from the equality partition/Fiber-Transport argument.

Do not edit G4 from this subordinate branch.

The remaining major boundary is now **sparse/partial domains**: classify exactly when local equality propagation on the defined-cell incidence graph is sufficient, and how the required arity/cost changes when that graph disconnects.