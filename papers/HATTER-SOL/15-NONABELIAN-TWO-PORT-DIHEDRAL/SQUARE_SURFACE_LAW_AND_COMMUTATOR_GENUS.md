# HATTER-SOL-15 · Square Surface Law, Commutator Defect, and Genus Reconstruction

**Status:** exact theorem layer; square-tiled/origami and branched-cover machinery is classical, H15 contribution is the port/world/observer synthesis.

Let `A,B in S_n` be two labelled port permutations acting transitively on an `n`-sheet fibre.

A square fundamental polygon can impose different surface laws depending on how opposite sides are identified.

## 1. Torus law

For the oriented torus the boundary word is

\[
aba^{-1}b^{-1},
\]

so a flat permutation bundle over the closed torus requires

\[
\boxed{ABA^{-1}B^{-1}=I.}
\]

Define the square-loop defect

\[
\boxed{K_T(A,B):=[A,B]=ABA^{-1}B^{-1}.}
\]

Thus the same two ports are flat on the torus exactly when they commute.

## 2. Punctured torus and defect monodromy

If `K_T(A,B)` is nontrivial, the pair still gives a transitive monodromy representation of the once-punctured torus. The boundary loop around the puncture has monodromy `K_T(A,B)` up to inversion/orientation convention.

Filling the puncture produces a connected degree-`n` branched cover of the torus with a single branch value whose monodromy cycle structure is that of `K_T`.

Let

\[
c(K)=\text{number of cycles of }K\text{ on }\{1,\ldots,n\}.
\]

## Theorem H15.40 — exact genus cost of closing the torus defect

For the compact orientable branched cover obtained by filling the puncture,

\[
\boxed{g=1+\frac{n-c(K_T)}2.}
\]

### Proof

For a degree-`n` branched cover `X -> T^2`, Riemann-Hurwitz gives

\[
2g(X)-2
=n(2g(T^2)-2)+R.
\]

Since `g(T^2)=1`, the base term vanishes. A monodromy permutation with cycle lengths `e_1,...,e_c` contributes ramification

\[
R=\sum_{j=1}^c(e_j-1)=n-c(K_T).
\]

Hence

\[
2g-2=n-c(K_T),
\]

which gives the formula. Because every commutator permutation is even, `n-c(K_T)` is even, so the genus is integral. QED.

Thus the cycle deficit

\[
\boxed{n-c(K_T)}
\]

is the exact topological cost of absorbing square-loop noncommutativity into a compact orientable branched surface.

## 3. Dihedral specialization

Let

\[
A=R,\qquad B=S,
\]

where on `F_p`, with `p` an odd prime,

\[
R(i)=i+1,\qquad S(i)=-i.
\]

The dihedral relation is

\[
SRS^{-1}=R^{-1}.
\]

The torus defect is

\[
[R,S]
=RSR^{-1}S^{-1}
=R^2.
\]

Since `p` is odd, `R^2` is a single `p`-cycle. Therefore

\[
\boxed{c([R,S])=1}
\]

and

\[
\boxed{g=\frac{p+1}{2}.}
\]

So the same dihedral ports that live on a planar Schreier carrier acquire genus growing linearly in `p` if one insists on interpreting them as square side monodromies of an orientable torus and then closes the resulting puncture.

## 4. Klein-bottle law

The Klein bottle is also obtained from a square, but one pair of opposite sides is glued with reversed orientation. Its group law may be written

\[
aba^{-1}=b^{-1}.
\]

Choosing

\[
a=S,\qquad b=R,
\]

the dihedral relation gives exactly

\[
\boxed{SRS^{-1}=R^{-1}.}
\]

Hence the same port pair `(R,S)` is **flat for the Klein-bottle surface law** while it has nontrivial commutator defect for the torus law.

Safe synthesis:

\[
\boxed{\text{flatness is a relation between port algebra and surface law, not a property of the ports alone}.}
\]

The pair `(R,S)` is defective relative to the torus relation and exact relative to the Klein relation.

## 5. Observer reconstruction of the hidden genus

Let `K in S_n` be the square-loop monodromy. Define the repeated-loop closure observer

\[
F_m(K):=\operatorname{Tr}(P_K^m)=\#\operatorname{Fix}(K^m).
\]

If `c_d(K)` denotes the number of cycles of length `d`, then

\[
F_m(K)=\sum_{d\mid m} d\,c_d(K).
\]

By Möbius inversion,

\[
\boxed{
c_d(K)=\frac1d\sum_{e\mid d}\mu(d/e)F_e(K).
}
\]

Therefore the observer sequence `F_1,...,F_n` reconstructs the entire cycle type of `K`, and hence

\[
\boxed{
c(K)=\sum_{d=1}^n c_d(K),
\qquad
g=1+\frac{n-c(K)}2.
}
\]

Thus a purely local repeated square-loop observer can infer the genus required to close the global branched surface.

For the dihedral `p`-cycle defect `K=R^2`,

\[
F_m(K)=
\begin{cases}
0,&p\nmid m,\\
p,&p\mid m,
\end{cases}
\]

so the observer reconstructs one `p`-cycle and therefore `g=(p+1)/2`.

## 6. Relation to earlier H15 surface results

There is no contradiction with the earlier planar-carrier theorem.

- the **Schreier carrier graph** for two-port path-order memory can be planar / outerplanar;
- the **square-side monodromy realization** asks a different question: can the two port permutations satisfy the defining relation of a chosen closed surface?

For the torus, the answer is no unless the ports commute. Closing the resulting defect creates branching and a genus cost.

Hence H15 now distinguishes three notions:

\[
\boxed{
\text{graph embedding genus}
\neq
\text{surface-law flatness}
\neq
\text{branched-cover genus required to absorb holonomy}.
}
\]

## Prior-art boundary

Square-tiled surfaces/origamis are classically encoded by horizontal and vertical permutations, and commutator cycles encode ramification over the torus. Riemann-Hurwitz then gives genus from those cycles. The Klein-bottle presentation is classical. H15 does not claim these standalone facts as new.

The H15-specific synthesis is to interpret the same arithmetic two-port system under different surface laws and to promote repeated-loop fixed-point responses to an observer that reconstructs the topological cost of closing the defect.