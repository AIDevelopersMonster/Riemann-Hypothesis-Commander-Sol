# HATTER-SOL-16 · A5 results

## Current status

The principal scalar-observer problem in the first nonsolvable laboratory is now **closed for the full natural range `mu >= 4`**.

Closed facts:

- `A5` has 2280 ordered generating pairs and 38 simultaneous-conjugacy orbits;
- generating commutators occur only in classes `3A`, `5A`, `5B`, with pair counts `1080`, `600`, `600`;
- one real three-dimensional irreducible character separates all five conjugacy classes of `A5`;
- the fourth torus moment retains the H15 length-four mechanism beyond the dihedral case:

  \[
  \langle\operatorname{Tr}H_{\rho_3}^4\rangle
  =48+8\chi_3([A,B]);
  \]

- the same three-dimensional representation gives an exact Artin local-factor observer

  \[
  \det(I-\rho_3(g)T)=1-\chi_3(g)T+\chi_3(g)T^2-T^3,
  \]

  which is injective on all five conjugacy classes;
- for an `A5`-Galois extension, the corresponding unramified three-dimensional Artin local factor therefore determines the Frobenius conjugacy class;
- exact balanced moments through order 40 collapse the 38 generating-pair orbits to `6` moment types in class `3A`, `4` in `5A`, and `4` in `5B`;
- a typewise tensor-gap certificate over `Q(sqrt(5))` proves positive rational tensor gaps for all fourteen Mahler types, with minimum

  \[
  \gamma>\frac15;
  \]

- exact determinant Laurent polynomials, outward-rounded interval arithmetic, and the tensor-gap aliasing theorem prove the boundary ordering

  \[
  M_{5A}(4)<M_{3A}(4)<M_{5B}(4);
  \]

- the exact large-parameter certificate proves the same ordering for

  \[
  \mu\ge\frac{23}{5};
  \]

- the final compact-strip certificate introduces the normalized observer

  \[
  G(\mu)=M(\mu)-3\log\mu+\frac6{\mu^2}
  \]

  and uses

  \[
  G'(\mu)=\sum_{m\ge2}\frac{S_{2m}}{\mu^{2m+1}}\ge0
  \]

  together with 60 rational parameter slabs of width `1/100` to close

  \[
  4\le\mu\le\frac{23}{5}.
  \]

Therefore the global theorem is

\[
\boxed{
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
\qquad\text{for every generating pair and every }\mu\ge4.
}
\]

More strongly, at every fixed `mu >= 4`, all four `5A` Mahler types lie below all six `3A` types, which in turn lie below all four `5B` types.

The compact-strip certificate has positive certified slab margins throughout; the smallest diagnostic margins are approximately

\[
1.1253\times10^{-2}
\]

for the `5A < 3A` comparison and

\[
1.6184\times10^{-3}
\]

for `3A < 5B`.

## Theorem and certificate chain

- `certificates/a5_generating_pair_commutator_certificate.py`
- `A5_ARTIN_LOCAL_FACTOR_TOMOGRAPHY.md`
- `certificates/a5_mahler_separation_mu_21_over_4_certificate.py`
- `certificates/a5_mahler_separation_mu_23_over_5_certificate.py`
- `A5_MAHLER_SEPARATION_MU_23_OVER_5.md`
- `certificates/a5_uniform_spectral_gap_diameter_certificate.py`
- `A5_UNIFORM_BOUNDARY_SPECTRAL_GAP.md`
- `certificates/a5_type_tensor_gap_certificate.py`
- `certificates/a5_boundary_mahler_mu4_interval_certificate.py`
- `A5_BOUNDARY_MAHLER_ORDERING_MU4.md`
- `certificates/a5_global_mahler_mu_ge_4_certificate.py`
- `A5_GLOBAL_MAHLER_ORDERING_MU_GE_4.md`

## Interpretation

The A5 laboratory answers the first H16 universality question in a precise form.

The literal H15 first-harmonic argument does not survive unchanged. What survives is the deeper chain

\[
\boxed{
\text{higher-dimensional representation}
\to
\text{length-four commutator trace}
\to
\text{spectral gap}
\to
\text{global determinant/Mahler class separation}.
}
\]

The three-dimensional Artin local factor and the Mahler observer are controlled by the same representation-theoretic class information.

## Next main strike

The first nonsolvable laboratory is now sufficiently closed to move the main line to

\[
\boxed{PSL(2,7)}.
\]

The next question is whether one irreducible channel still separates the relevant commutator/Frobenius classes, or whether `PSL(2,7)` is the first point where genuinely vector-valued non-Abelian tomography becomes necessary.