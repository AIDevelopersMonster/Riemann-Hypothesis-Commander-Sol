# HATTER-SOL-11 · Orbital Forgetting-Map Fibers

Status: central theorem layer.

## Setup

Let

\[
f_\Delta:\Omega_\Delta(\alpha)\to\Pi_\Delta(\alpha)=(P,Q)
\]

be the canonical map from symmetry-resolved geodesic usage to the published HATTER-SOL typed pair.

The goal is to classify every fiber of this map.

## Generic even discriminants

For `Delta<-4`, `Delta==0 mod 4`, the natural direction orbits are axial and transverse. The published pair already keeps those labels:

\[
\Pi_\Delta(L+WF)=(|L|,|W|).
\]

Hence the forgetting map is injective.

## Gaussian world

At `Delta=-4`, the unit `i` exchanges the two directions, so the canonical orbital datum is the unordered pair `{|L|,|W|}`. The published pair is its decreasing sort. Hence the map is injective after quotienting by the natural symmetry.

## Generic odd discriminants

For `Delta<-3`, `Delta==1 mod 4`, the natural orbit partition is

\[
A=\{[1]\},\qquad O=\{[F],[\bar F]\}.
\]

If the unique geodesic triple is `(x,y,z)`, define

\[
\Omega_\Delta(\alpha)=(|x|;\{|y|,|z|\}),
\]

with the first entry axial and the last two an unordered oblique pair.

The published pair is obtained by sorting `|x|,|y|,|z|` and dropping the zero.

### Theorem T11.21 — exact generic-odd fiber sizes

For fixed `P>=Q>=0`:

\[
|f_\Delta^{-1}(P,Q)|=
\begin{cases}
1,&P=Q=0,\\
2,&P>0,\ Q=0,\\
2,&P=Q>0,\\
3,&P>Q>0.
\end{cases}
\]

### Proof

Every shortest representation uses at most two of the three undirected directions, so one geodesic count is zero.

If `P>Q>0`, there are exactly three symmetry-distinct placements:

\[
(P;\{Q,0\}),\qquad
(Q;\{P,0\}),\qquad
(0;\{P,Q\}).
\]

All three occur, respectively for

\[
P+QF,\qquad Q+PF,\qquad Q-(P+Q)F.
\]

No fourth placement exists because conjugation already identifies the two oblique slots.

If `P=Q=r>0`, the first two signatures coincide, leaving

\[
(r;\{r,0\}),\qquad (0;\{r,r\}).
\]

If `Q=0<P`, the two possibilities are

\[
(P;\{0,0\}),\qquad (0;\{P,0\}),
\]

realized by `P` and `PF`.

The zero element gives the unique zero signature. QED.

## Eisenstein world

At `Delta=-3`, extra units act transitively on all three directions. The canonical orbital datum is only the unordered magnitude multiset `{P,Q,0}`, which is exactly recovered from the published pair. Hence the map is injective.

## Global consequence

The published `(P,Q)` fold loses canonical direction-orbit placement information **only in generic odd discriminant worlds**. There the maximal fiber size is exactly three.

Thus the static orbital question is now sharply resolved:

\[
\boxed{
\text{canonical orbital refinement exists, and its forgetting fibers are completely classified.}
}
\]

## Norm resolves the generic-odd ambiguity

For `q=(1+|Delta|)/4>1`, the three interior signatures have norms

\[
N_I=P^2+PQ+qQ^2,
\]

\[
N_{II}=Q^2+PQ+qP^2,
\]

\[
N_{III}=q(P^2+Q^2)+(2q-1)PQ.
\]

For `P>Q>0`,

\[
N_I<N_{II}<N_{III}.
\]

Boundary and diagonal fiber types likewise have distinct norms. Therefore `(N_Delta,Pi_Delta)` still determines the orbital signature, in agreement with T11.4.

## Next target

The next nontrivial question is operational:

> can two members of the same generic-odd `(P,Q)` fiber have different network behavior when the network sees the natural axial/oblique labels before folding?

This is the correct next attack. The maximal-first rule from `MAXIMAL_FIRST_GEOMETRY_PROBE.md` may be used as a search probe, but full orbital-network optimization remains the primary object.