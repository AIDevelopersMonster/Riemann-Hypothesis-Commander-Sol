# HATTER-SOL-15 · Final Release Audit v0.3

**Date:** 15 September 2026  
**Branch:** `research/hatter-sol-nonabelian-two-port-dihedral`  
**Status:** reviewer revisions incorporated; RU/EN v0.3 rendered and visually audited.

## Reviewer-driven revisions completed

The v0.3 publication source incorporates the substantive recommendations in the external review:

1. `D_{2p}` is explicitly declared to mean the dihedral group of order `2p`.
2. The genus formula is stated only for a connected oriented degree-`n` one-point branched torus cover with transitive monodromy and local branch monodromy `K`.
3. The projective-code theorem now includes the counting proof
   \[
   \operatorname{wt}=p^{r-1},\qquad d_{\min}=2p^{r-2}.
   \]
4. The primitive Mahler section gives the explicit constant term
   \[
   C_\mu=2L_\mu-\sum_{m\ge1}\frac1m\binom{2m}{m}a_{m,0}(\mu)^2.
   \]
5. The strict monotonicity claim is no longer delegated to an unnamed argument: the manuscript now contains the circular-autocorrelation lemma and the proof that
   \[
   M_\mu'(\alpha)>0\qquad(0<\alpha<\pi/2).
   \]
6. The boundary `\mu=4` is treated explicitly: every nontrivial primitive determinant stays strictly positive, and no unproved boundary coefficient asymptotic is used in the main theorem.
7. The Mahler–Dirichlet–Gauss transform now fixes all conventions explicitly:
   \[
   \tau(\bar\chi)=\sum_{k=1}^{p-1}\bar\chi(k)e^{2\pi ik/p},
   \]
   \[
   \widehat f(\chi)=\sum_{[k]\in G_p}f([k])\bar\chi(k)
   =\frac12\sum_{k=1}^{p-1}f(k)\bar\chi(k),
   \]
   together with the unnormalised Gram inner product.
8. The centered reaction-space dimension is stated:
   \[
   \dim\mathbf C[G_p]_0=\frac{p-3}{2}.
   \]
9. The high-`m` auxiliary quantity is displayed as a numbered equation:
   \[
   K_m:=\frac{m}{4^m}\binom{2m}{m}I_{2m},
   \qquad
   I_{2m}=\int_{-\infty}^{\infty}(1+u^2)^{-2m}\,du,
   \]
   followed immediately by
   \[
   \frac{K_{m+1}}{K_m}=1-\frac1{16m^2}<1.
   \]
10. Appendix A now prints all six numerator polynomials `N_2,...,N_7`, all denominators `(2,8,16,128,256,1024)`, and the complete rational vector `beta_1,...,beta_7`.
11. The motivic/regulator section is explicitly marked secondary and logically independent of the universal dominance/tomography proof.
12. The manuscript discusses the reviewer-suggested stability margin correctly: a global positive constant `Delta_*` cannot exist because
   \[
   \Delta_\mu=4\mu^{-4}+O(\mu^{-6})\to0.
   \]
   Quantitative conditioning should instead be studied on compact `\mu`-intervals or after `\mu^4` rescaling.
13. The 2026 Gaussian-period Mahler reference remains listed as a published PLMS article with DOI `10.1112/plms.70198`.

## Exact certificate reproduction

The release companion script uses only Python standard-library exact rational arithmetic. Independent execution result:

```text
PASS: all exact assertions succeeded
near_lower = 0.035403115821673055
near_margin_sq = 6.819542469761168e-05
series_bound = 0.06661764484578646 < 0.06666666666666667
far_endpoint_squared_ratio = 5.012771695274961
global_H_min = 3.513888888888889
```

SHA-256 of the exact release reproduction script:

`164f077a1b1da9e10a7232f807a0982cac87f2e8288119af9c8423c2d21731de`

## Render audit

- English v0.3: 13 pages.
- Russian v0.3: 14 pages.
- Both PDFs were rendered page-by-page after compilation.
- Appendix A was inspected at full rendered resolution; the long `N_5,N_6,N_7` polynomials, denominator vector, `beta` vector, and certificate SHA are visible without clipping.
- The proof dependency map was reflowed after an initial overfull-box warning.
- Remaining small TeX overfull/underfull warnings are typographic and do not clip content in the rendered pages.

## Release-file hashes

```text
90376d09013f1d6421655670d6cafd67617da98da541ea364ad1aff7000d2624  HATTER_SOL_15_EN_v0.3.pdf
8d11341b8d8f84aa62cb38711e49489575a8ffca5711a240ec0837dcbc8b24fe  HATTER_SOL_15_RU_v0.3.pdf
f9d17a99cc541a67e0046d1b2ebc1ba21122a77d743518a91abe6d657e2981f7  HATTER_SOL_15_EN_v0.3.tex
cfcb581ba8e6b1bb8f747db5d15d275ead5e61444191f6b7ed4f3c9e46a988b9  HATTER_SOL_15_RU_v0.3.tex
164f077a1b1da9e10a7232f807a0982cac87f2e8288119af9c8423c2d21731de  HATTER_SOL_15_certificate_reproduction_v0.3.py
fd5206793b1cbc0a646b88ef22e9ed05aef41b54e16666d9575beae2df4038cd  HATTER_SOL_15_certificate_run_v0.3.txt
```

## Release verdict

The external review did not expose a new defect in the universal first-harmonic dominance theorem. Its reproducibility and presentation objections have now been addressed directly in the v0.3 manuscript.

**Internal status:** `v0.3` is the current release candidate. The remaining release actions are metadata/Zenodo packaging and, if desired, one independent external rerun of the exact certificate from the archived release files.
