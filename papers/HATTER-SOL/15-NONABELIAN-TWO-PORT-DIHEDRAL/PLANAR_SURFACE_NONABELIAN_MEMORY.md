# HATTER-SOL-15 · Non-Abelian Two-Port Memory on a Planar Carrier

**Status:** exact theorem layer

Let the dihedral two-port sector set be

\[
X=\mathbb F_p,
\qquad
R(i)=i+1,
\qquad
S(i)=-i,
\]

for an odd prime `p`.

Forget orientations and port labels, discard the fixed `S`-loop at `0`, and merge duplicate edges. Let `U_p` be the resulting simple undirected graph.

## Structure of `U_p`

The `R`-edges form the cycle

\[
C_p=(0,1,2,\ldots,p-1,0).
\]

The nontrivial `S`-edges are

\[
\{i,p-i\},
\qquad
1\le i\le (p-1)/2.
\]

For `i=(p-1)/2`, this edge is already a cycle edge, since

\[
p-i=i+1.
\]

Thus the genuinely new chords are

\[
\{i,p-i\},
\qquad
1\le i\le (p-3)/2.
\]

## Theorem H15.9 — outerplanarity

For every odd prime `p`, the underlying simple carrier `U_p` is outerplanar. In particular,

\[
\boxed{\gamma(U_p)=0.}
\]

### Proof

Place the vertices `0,1,...,p-1` in cyclic order on a circle and draw the cycle edges on the boundary. For

\[
1\le i<j\le(p-3)/2,
\]

the chord endpoints occur in the cyclic order

\[
i<j<p-j<p-i.
\]

Hence the chords `{i,p-i}` and `{j,p-j}` are nested rather than alternating, so they do not cross. All vertices remain on the outer boundary. Therefore this drawing is outerplanar. QED.

## Corollary H15.10 — topology does not cause the path-order memory

The same marked carrier supports the noncommuting port actions

\[
RS\ne SR
\]

and the exact sector-addressing/observer phenomena of H15.1-H15.8, while its underlying unmarked simple graph has genus zero.

Therefore the new H15 memory layer cannot be attributed to ordinary graph genus:

\[
\boxed{
\text{non-abelian path-order memory}
\not\Rightarrow
\text{topological complexity of the underlying surface}.
}
\]

The relevant structure is the marked Schreier action (edge labels/directions and word order), not the unmarked embedding genus.

## Comparison with H13-H14

H13 quantified a topological cost for erasing scalar port budget in unrestricted carriers. H14 showed that equivariant homology can retain arithmetic marking even when the abstract graph is fixed. H15 now exhibits a stronger separation of mechanism:

\[
\boxed{
\text{planar abstract carrier}
+
\text{non-abelian marked action}
\Longrightarrow
\text{path-order structural memory}.
}
\]

Thus genus, equivariant homology, and non-abelian word-order memory are genuinely distinct layers.