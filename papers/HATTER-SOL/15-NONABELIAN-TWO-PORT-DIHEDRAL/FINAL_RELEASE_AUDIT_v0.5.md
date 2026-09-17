# HATTER-SOL-15 · Final Release Audit v0.5

**Date:** 15 September 2026  
**Status:** final release candidate after external review delta v0.4 -> v0.5.

## 1. Review items closed

The external review of v0.4 identified four publication-critical presentation/reproducibility issues. They are closed as follows.

1. `K_m` and far-region endpoint comparison were checked against the audited theorem layer. The mathematical source was already correct; the apparent damage arose in text extraction. The v0.5 TeX keeps both formulas explicitly displayed.
2. The Gauss convention is fixed with `tau(conj chi)` and the quotient Fourier transform using `conj chi`; the factor `1/2` and Gram normalization are explicit.
3. The circular-autocorrelation lemma now assumes explicitly `f'(u)<0` on `(0,pi)` and the circular-distance comparison is split into the two cases `u+delta <= pi` and `u+delta > pi`.
4. At the boundary `mu=4`, the manuscript now proves a strict primitive-channel determinant gap and obtains a channel-dependent `rho_alpha<1`, giving absolute and uniform convergence of the logarithmic series on the torus.
5. The exact certificate now has both an immutable Git commit link and an active-branch link in the manuscript, in addition to its SHA-256.

## 2. Series/author metadata

- Author shown in both PDFs: **A. A. Malachevsky**.
- ORCID shown and linked: `https://orcid.org/0009-0008-6009-3196`.
- HATTER-SOL-14 DOI inserted: `10.5281/zenodo.22757307`.
- HATTER-SOL installments 07-14 are present both as a historical roadmap and as explicit bibliography entries with DOI data.
- Series umbrella DOI remains `10.5281/zenodo.17996774`.

## 3. Exact certificate

Independent execution of `HATTER_SOL_15_certificate_reproduction_v0.5.py` returned:

```text
PASS: all exact assertions succeeded
near_lower = 0.035403115821673055
near_margin_sq = 6.819542469761168e-05
series_bound = 0.06661764484578646 < 0.06666666666666667
far_endpoint_squared_ratio = 5.012771695274961
global_H_min = 3.513888888888889
```

Certificate SHA-256:

`164f077a1b1da9e10a7232f807a0982cac87f2e8288119af9c8423c2d21731de`

Immutable audited source commit:

`e0de61073e55bb6e3d8c305a63679775da5f49c9`

## 4. PDF build audit

Both TeX sources were compiled with XeLaTeX through three passes.

- EN PDF: 15 pages.
- RU PDF: 16 pages.
- No unresolved cross references after the final pass.
- No remaining overfull boxes after the final formatting pass.
- Both PDFs pass structural preflight: openable, unencrypted, non-scanned.
- Page renders were visually inspected, including title pages, the monotonicity/boundary section, universal-dominance proof, exact certificate appendix, series history, and bibliography.

## 5. Release hashes

Final artifact hashes are recorded in `HATTER_SOL_15_SHA256_v0.5.txt` in the release package.

## 6. Canonical publication status

The following are the canonical mathematical claims of the release:

- for every `mu>=4`,

  `B_{mu,1} > sum_{n>=2} B_{mu,n}`;

- for every odd prime `p`, every nontrivial even character modulo `p`, and every `mu>=4`, the primitive Mahler character response is nonzero;
- equivalently, the centered primitive Mahler response operator is invertible on the full zero-sum signless reaction space; for `p=3` this space is zero-dimensional, and for `p>=5` the statement is nontrivial;
- no Riemann-hypothesis claim is made.

Older exploratory theorem layers with broader parameter domains or stronger certificate-obstruction language are subordinated to `THEOREM_LAYER_CORRECTIONS_v0.5.md`.

## 7. Release verdict

**v0.5 passes the publication gate.**

No further mathematical correction is required before Zenodo deposit unless a subsequent independent review identifies a new substantive defect. The Zenodo deposit should include both PDFs, both TeX sources, the exact certificate, the independent run transcript, and the SHA-256 manifest.