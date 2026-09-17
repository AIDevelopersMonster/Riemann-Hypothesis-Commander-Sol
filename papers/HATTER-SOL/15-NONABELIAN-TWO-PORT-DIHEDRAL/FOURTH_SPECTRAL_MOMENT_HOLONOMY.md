# HATTER-SOL-15 · Fourth Spectral Moment Detects Square Holonomy

**Status:** exact theorem layer in the periodic square-lattice model.

Consider a finite periodic square lattice with an internal `n`-dimensional fibre. Let horizontal oriented edges carry a unitary/permutation matrix `A`, reverse horizontal edges carry `A^{-1}`, vertical edges carry `B`, and reverse vertical edges carry `B^{-1}`.

Let `H` be the corresponding Hermitian adjacency/transfer operator.

Define the elementary plaquette holonomy

\[
K=[A,B]=ABA^{-1}B^{-1}.
\]

## Theorem H15.43 — first holonomy-sensitive closed-walk length

Among local contractible closed walks on the square lattice, no walk of length `<4` encloses an elementary plaquette. At length `4`, the oriented plaquette walks appear and contribute the fibre traces

\[
\boxed{\operatorname{Tr}K}
\qquad\text{and}\qquad
\boxed{\operatorname{Tr}K^{-1}}.
\]

Consequently `Tr(H^4)` is the first local spectral moment that can distinguish the elementary commutator holonomy from the flat case through contractible square loops.

### Proof

`Tr(H^m)` is the sum over all closed length-`m` walks of the trace of the ordered product of their edge transport matrices.

For `m<4`, every contractible closed walk on the square lattice consists only of immediate backtracking/retracing and its transport reduces by adjacent cancellations such as `AA^{-1}` or `BB^{-1}`. Such contributions are independent of `[A,B]`.

At `m=4`, a positively oriented elementary square has transport

\[
ABA^{-1}B^{-1}=K,
\]

while the reverse orientation has transport `K^{-1}`. Hence the fourth moment contains `Tr K + Tr K^{-1}` for each plaquette, in addition to holonomy-independent backtracking terms. QED.

## Corollary H15.44 — permutation ports turn spectrum into a fixed-point observer

If `A,B` are permutation matrices, then

\[
\boxed{\operatorname{Tr}K=\#\operatorname{Fix}(K).}
\]

Thus the fourth spectral moment contains exactly the same elementary-square closure information as the fixed-point observer applied to the commutator permutation.

For a flat torus connection `K=I_n`,

\[
\operatorname{Tr}K=n.
\]

For the dihedral pair on `p` sectors,

\[
A=R,
\qquad B=S,
\qquad K=R^2,
\]

and `R^2` is a single `p`-cycle. Therefore

\[
\boxed{\operatorname{Tr}K=0.}
\]

So the flat and dihedral square laws are spectrally separated already in the fourth moment.

## Theorem H15.45 — higher moments recover commutator cycle data

Repeated elementary-square loops contribute

\[
\operatorname{Tr}(K^m)=\#\operatorname{Fix}(K^m)
\]

for permutation ports. Knowing these traces for `m=1,...,n` reconstructs the complete cycle type of `K` by Möbius inversion.

Therefore the family of spectral closed-walk moments contains enough information to reconstruct the same cycle data that determine the branched-cover genus

\[
g=1+\frac{n-c(K)}2.
\]

Safe synthesis:

\[
\boxed{
\text{spectral moments}
\to
\text{plaquette holonomy traces}
\to
\text{commutator cycle type}
\to
\text{topological closing cost}.
}
\]

## Claim boundary

The trace-of-powers/closed-walk correspondence and Wilson-loop sensitivity of magnetic or connection Laplacians are classical. H15 does not claim that general spectral principle as new. The H15-specific contribution is the exact identification of the dihedral arithmetic two-port commutator with the first square-loop spectral defect and its previously derived genus cost.