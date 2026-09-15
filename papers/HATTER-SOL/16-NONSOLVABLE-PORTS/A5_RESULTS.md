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
- an exact rational interval certificate now proves

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

Relevant theorem layers and certificates:

- `certificates/a5_generating_pair_commutator_certificate.py`
- `A5_ARTIN_LOCAL_FACTOR_TOMOGRAPHY.md`
- `certificates/a5_mahler_separation_mu_21_over_4_certificate.py`
- `certificates/a5_mahler_separation_mu_23_over_5_certificate.py`
- `A5_MAHLER_SEPARATION_MU_23_OVER_5.md`

## Current barrier

Numerical quadrature at `mu=4` still shows the same strict class ordering across all 38 simultaneous-conjugacy representatives, but this is not yet a theorem.

The remaining obstruction is now sharply localized: the crude tail proof uses `||H|| <= 4`, so its geometric remainder degenerates at the natural boundary `mu=4`.

The next strike is to prove a uniform finite-lab spectral gap

\[
\sup_{\theta,\phi}\|H_{A,B}(\theta,\phi)\|<4
\]

for every generating pair, preferably with an exact common constant over the 38 orbit types. Once this gap is certified, the moment/tail argument can be rerun directly at `mu=4`.

Only after that boundary question is closed should the main line move to `PSL(2,7)`.