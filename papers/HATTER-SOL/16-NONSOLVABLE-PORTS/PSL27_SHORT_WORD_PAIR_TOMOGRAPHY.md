# HATTER-SOL-16 · Short-word tomography of generating-pair orbits in PSL(2,7)

## Status

**Closed theorem layer.**  The 114 simultaneous-conjugacy orbits of generating pairs are now exactly reconstructible from a finite short-word trace signature.

Let

\[
G=PSL(2,7),
\qquad
\rho_3:G\to U(3)
\]

be the oriented three-dimensional irreducible representation used in the preceding PSL(2,7) layers.  Since its character is injective on the six conjugacy classes, recording

\[
\operatorname{Tr}\rho_3(w(A,B))
\]

is equivalent to recording the conjugacy class of the word value \(w(A,B)\).

The exact finite certificate is

`certificates/psl27_pair_tomography_short_word_certificate.py`.

---

## Theorem 16.F · unrestricted trace depth four is necessary and sufficient

Take all cyclically reduced words in the alphabet

\[
A,A^{-1},B,B^{-1}
\]

up to cyclic rotation and inversion.

The cumulative number of distinct signatures on the 114 generating-pair orbits is

\[
\boxed{
24,\ 107,\ 107,\ 114
}
\]

for maximal word lengths

\[
1,2,3,4
\]

respectively.

Hence

\[
\boxed{
\text{trace depth }4\text{ is necessary and sufficient.}
}
\]

Depth 3 cannot reconstruct all pair orbits, while depth 4 reconstructs every orbit.

---

## A five-probe complete signature

Among the complete depth-at-most-four family, the following five words already suffice:

\[
\boxed{
A,\quad B,\quad AB,\quad AB^{-1},\quad ABA^{-1}B^{-1}.
}
\]

Thus the map

\[
[(A,B)]_{\mathrm{sim.conj}}
\longmapsto
\Bigl(
[ A ],[ B ],[ AB ],[ AB^{-1} ],[ [A,B] ]
\Bigr)
\]

is injective on the 114 generating-pair orbits, where brackets on the right denote conjugacy class, or equivalently the oriented three-dimensional trace value.

The certificate also exhaustively checks all subsets of the full depth-at-most-four candidate family and proves:

\[
\boxed{
\text{no signature using at most four such probes separates all 114 orbits.}
}
\]

Therefore, inside this complete short-word probe family, five channels are minimal.

This gives a particularly compact zero-oracle tomography primitive:

\[
\boxed{
(A,B,AB,AB^{-1},[A,B]).
}
\]

It uses two one-port reads, two mixed two-letter reads, and one oriented commutator read.

---

## Theorem 16.G · closed-loop-only tomography has exact depth fourteen

For a stricter observer, require every probe word to be torus-balanced:

\[
\exp_A(w)=0,
\qquad
\exp_B(w)=0.
\]

These are closed-loop probes in the abelianized port lattice and do not use the open words \(A,B,AB,AB^{-1}\).

For cumulative balanced word lengths

\[
4,6,8,10,12,14
\]

the exact numbers of distinguished generating-pair orbits are

\[
\boxed{
4,\ 22,\ 98,\ 110,\ 112,\ 114.
}
\]

The numbers of new cyclic balanced words at those lengths are

\[
\boxed{
1,\ 2,\ 14,\ 76,\ 505,\ 3386.
}
\]

Consequently

\[
\boxed{
\text{balanced closed-loop trace depth }14\text{ is necessary and sufficient.}
}
\]

In particular, every balanced trace probe of length at most 12, even when all such probes are used simultaneously, leaves two nontrivial collisions among the 114 pair orbits.

---

## An explicit eight-probe balanced signature

The following eight cyclically reduced balanced words already separate all 114 orbits:

```text
AABBaabb
AAABAbabbaBaaB
AAbABaBBBabbab
AABBAbababaB
AAAABabaBabbaB
AABabaBAAbaBab
ABBAbaBBabbb
ABABABaBabbabb
```

Here lower-case letters denote inverses:

\[
a=A^{-1},\qquad b=B^{-1}.
\]

Their lengths are

\[
8,14,14,12,14,14,12,14.
\]

Each has zero exponent sum in both generators, so this is a genuine closed-loop-only finite tomography scheme.

No minimality claim is made here for the number eight; only its sufficiency is certified.  The depth-14 lower bound, however, is exact for the complete balanced word family.

---

## Structural consequence

The commutator class alone has only four values on generating pairs:

\[
3A,4A,7A,7B,
\]

so it cannot identify 114 pair orbits.

The present theorem quantifies exactly how much extra non-Abelian word information is required:

\[
\boxed{
\begin{array}{c|c}
\text{observer model} & \text{exact reconstruction depth}\\
\hline
\text{general oriented trace words} & 4\\
\text{balanced closed-loop trace words} & 14
\end{array}
}
\]

Thus there is a real information cost for insisting on closed-loop-only access.

This is the direct bridge from HATTER-SOL-16 to HATTER-SOL-17: zero-oracle pair tomography is possible with a very small mixed-word signature, while a pure closed-loop interface remains possible but requires deeper word memory.

---

## H17 hardware interpretation

The five-probe signature is particularly suitable for a finite-state port processor.  It requires evaluation of only

\[
A,\ B,\ AB,\ AB^{-1},\ [A,B]
\]

followed by one class/representation readout for each result.

The deepest word is the commutator, of length four.  Hence the complete generating-pair orbit can be reconstructed with primitive port-word depth four and five observer channels.

A loop-only implementation can instead use the certified eight balanced probes above, with maximal word depth fourteen.

This gives two explicit engineering points on the depth-versus-interface tradeoff that HATTER-SOL-17 is meant to study.
