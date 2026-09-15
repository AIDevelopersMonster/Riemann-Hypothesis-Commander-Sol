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

- the positivity/convergence obstruction at the natural boundary is closed exactly: every Cayley graph attached to a generating pair has diameter at most `10`, and Schur orthogonality gives a uniform spectral estimate

  \[
  \sup_{\theta,\phi}\|H_{A,B}(\theta,\phi)\|<4-\frac1{120}.
  \]

- a stronger typewise tensor-gap certificate over `Q(sqrt(5))` reduces the 38 pair-orbits to the same 14 Mahler types and proves rational tensor Cayley gaps

  \[
  \gamma>\frac34,\frac32,\frac38,1,\frac54,\frac35,\frac15,
  \frac9{10},\frac45,\frac3{10},\frac12,\frac34,\frac23,\frac45.
  \]

- using those typewise gaps, exact determinant Laurent polynomials in `Q(sqrt(5))`, outward-rounded interval arithmetic, and a rigorous trapezoidal aliasing bound, the natural boundary itself is now closed:

  \[
  \boxed{
  M_{5A}(4)<M_{3A}(4)<M_{5B}(4).
  }
  \]

  More strongly, every one of the four `5A` Mahler types lies below every one of the six `3A` types, and every `3A` type lies below every one of the four `5B` types.

Relevant theorem layers and certificates:

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

## Current barrier

The endpoint `mu=4` is no longer an open problem: both positivity and strict class ordering are now certified.

The large-parameter regime is also closed for

\[
\mu\ge\frac{23}{5}.
\]

The only remaining scalar-parameter gap in the A5 laboratory is therefore the compact open strip

\[
\boxed{4<\mu<\frac{23}{5}}.
\]

Numerical scans across that strip show the same ordering with no crossing, but this remains diagnostic until a compact-parameter interval certificate or an analytic no-crossing theorem is completed.

The next strike is now sharply defined:

1. certify the Mahler differences on the compact parameter strip `4 < mu < 23/5`, preferably by intervalizing the exact determinant polynomials in `mu` and reusing the typewise tensor gaps; then
2. once the all-`mu >= 4` A5 ordering is closed, move the main line to `PSL(2,7)` and test whether a single irreducible channel still separates the relevant commutator/Frobenius classes.
