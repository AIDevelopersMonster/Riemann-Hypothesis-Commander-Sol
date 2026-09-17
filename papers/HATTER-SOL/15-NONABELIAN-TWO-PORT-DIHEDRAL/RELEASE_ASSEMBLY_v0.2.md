# HATTER-SOL-15 · Release Assembly v0.2

**Date:** 2026-09-15  
**Branch:** `research/hatter-sol-nonabelian-two-port-dihedral`  
**Publication source:** audited H15.137–H15.139 proof layer + `PUBLICATION_AUDIT_v0.2.md`.

## Status

The RU/EN publication candidates have been rebuilt from the audited proof, with synchronized section/theorem/equation structure and the v0.1 publication defects removed.

Release PDFs were generated with XeLaTeX and visually checked page-by-page after rendering to PNG. The English candidate is 11 pages; the Russian candidate is 12 pages.

The publication structure is synchronized:

1. Dihedral two-port setup and commutator square.
2. Topological/Fourier signatures.
3. Object-dependent curvature and arithmetic worlds.
4. What the unlabelled invariant spectrum forgets.
5. Primitive Mahler observer.
6. Mahler–Dirichlet–Gauss transform and Gram spectrum.
7. Universal first-harmonic dominance.
8. All-prime linear tomography.
9. Secondary motivic/regulator branch.
10. Observer hierarchy and non-Abelian information.
11. Prior art and claim boundary.
12. Conclusion.
13. Appendix A: exact certificate and reproducibility.
14. Appendix B: proof dependency map.

The theorem numbering is synchronized across RU/EN:

- Theorem 3.1 — square curvature is twice the world coordinate.
- Corollary 3.2 — flatness/splitting equivalence.
- Theorem 3.3 — projective curvature tomography.
- Proposition 4.1 — spectral blindness of the unlabelled full operator.
- Theorem 5.1 — positive Mahler harmonic expansion.
- Theorem 6.1 — Mahler–Dirichlet–Gauss bridge.
- Theorem 7.1 — universal first-harmonic dominance.
- Theorem 8.1 — nonvanishing of every nontrivial even character mode.
- Corollary 8.2 — full linear reaction tomography for every odd-prime world.

## Corrected publication proof

Only the audited far-tail estimate is used:

\[
\sum_{m\ge8}\frac{y^m}{m^2}<\frac1{15}y^8,
\qquad
0<y\le\frac{400}{441}.
\]

The high-`m` control is explicitly stated as a one-sided lower bound, not as an absolute-value estimate.

The final theorem remains

\[
\boxed{
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4).
}
\]

and consequently, for every odd prime `p`, every nontrivial even Dirichlet character `chi mod p`, and every `mu>=4`,

\[
\widehat f_\mu(\chi)\ne0.
\]

For `p=3`, the centered signless reaction space is zero-dimensional; for `p>=5`, the statement is nontrivial.

## Independent exact-certificate reproduction

A separate reproduction script was run using exact `fractions.Fraction` arithmetic only. All assertions passed.

Recorded output:

```text
PASS: all exact assertions succeeded
near_lower = 0.035403115821673055
near_margin_sq = 6.819542469761168e-05
series_bound = 0.06661764484578646 < 0.06666666666666667
far_endpoint_squared_ratio = 5.012771695274961
global_H_min = 3.513888888888889
```

The floating-point numbers above are display-only summaries of exact rational inequalities; no floating-point value is used in an assertion.

## SHA-256 values of assembled artifacts

```text
certificate reproduction script
9c405932cb0da49bc14268bf1a55c1d88eab5839baff69cdc6feac838ee2ee7d

English PDF
c4e837c393ecc2e72702e72144b0e1eff3a5165bb5ae25df6d7a0272ab0855d7

Russian PDF
7f20242e9735d4d0b941c54c6c09e5e080ff488fa02dacfb0e1c6acaa74d8ccf

English XeLaTeX source
ddbf81b85aeeca75d4cbd5792319feb70836e10fd8caaf73f24d393f1bab35e6

Russian XeLaTeX source
5719dafd861a22208b8453ab1f2bd12c18268db44c6ef61a784ecdd9baab3a8c
```

## Bibliography/claim audit

The selected bibliography was normalized according to `PUBLICATION_AUDIT_v0.2.md`. The manuscript uses conservative novelty language only: the exact first-harmonic dominance/all-prime tomography statement was not identified in the targeted literature search, but no priority claim is made.

The final publication explicitly states that HATTER-SOL-15 is not a proof or partial proof of the Riemann hypothesis.

## Release gate

The v0.2 PDF candidates have passed mathematical-source synchronization, independent certificate reproduction, and visual PDF QA. Remaining external actions before Zenodo release are:

- decide final author/byline metadata and ORCID placement;
- archive the exact release PDFs and source in the repository/release assets;
- optionally obtain an external specialist review of the Mahler-measure prior-art section;
- assign the final Zenodo DOI and replace `publication candidate` metadata with release metadata.
