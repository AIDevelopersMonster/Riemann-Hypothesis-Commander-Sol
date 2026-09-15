# HATTER-SOL-16 · A5 results

Current closed facts:

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
- an exact rational interval certificate proves

  \[
  \boxed{
  M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
  \quad\text{for every generating pair and every }\mu\ge 23/5.
  }
  \]

This improves the first crude threshold `mu >= 58`, and the intermediate `mu >= 21/4`, to

\[
\boxed{\mu\ge 4.6}.
\]

- the former positivity/convergence obstruction at the natural boundary is now closed exactly: every Cayley graph attached to a generating pair has diameter at most `10`, and Schur orthogonality then gives the uniform spectral estimate

  \[
  \boxed{
  \sup_{\theta,\phi}\|H_{A,B}(\theta,\phi)\|
  <4-\frac1{120}.
  }
  \]

  Therefore

  \[
  4I-H_{A,B}(\theta,\phi)\succeq \frac1{120}I
  \]

  and the logarithmic trace series converges absolutely and uniformly already at `mu=4`.

Relevant theorem layers and certificates:

- `certificates/a5_generating_pair_commutator_certificate.py`
- `A5_ARTIN_LOCAL_FACTOR_TOMOGRAPHY.md`
- `certificates/a5_mahler_separation_mu_21_over_4_certificate.py`
- `certificates/a5_mahler_separation_mu_23_over_5_certificate.py`
- `A5_MAHLER_SEPARATION_MU_23_OVER_5.md`
- `certificates/a5_uniform_spectral_gap_diameter_certificate.py`
- `A5_UNIFORM_BOUNDARY_SPECTRAL_GAP.md`

## Current barrier

The boundary `mu=4` is no longer singular: the determinant is uniformly positive and the moment expansion converges there.

What remains is strictly narrower. Numerical quadrature at `mu=4` over all 38 simultaneous-conjugacy representatives gives separated bands approximately

\[
M_{5A}\in[3.5817,3.6082],\qquad
M_{3A}\in[3.6322,3.6508],\qquad
M_{5B}\in[3.6552,3.6641],
\]

so the large-`mu` ordering appears to persist all the way to the natural boundary. These decimals are diagnostic only, not a theorem.

The remaining theorem obligation is now the **class-ordering gap** on

\[
4\le\mu<23/5,
\]

especially the small `5B-3A` boundary gap. The exact diameter bound `1/120` is sufficient for uniform convergence but too coarse, by itself, to make the old order-40 geometric tail smaller than that gap.

The next strike is therefore to obtain either:

1. sharper orbit-wise spectral radii and a certified higher-moment tail; or
2. a direct interval certificate for the Mahler difference on the compact box `mu in [4,23/5]`, `(theta,phi) in T^2`.

Once this class-ordering gap is closed, the A5 laboratory will have a complete boundary theorem and the main line can move to `PSL(2,7)`.