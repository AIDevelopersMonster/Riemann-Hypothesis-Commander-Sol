# Alice Throws Away the Ruler — research status

**Branch:** `research/alice-ruler-incidence`  
**Working folder:** `alice-ruler-incidence/`  
**Status date:** 2026-09-12  
**Author line:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## STATUS: MATHEMATICAL PUBLICATION THRESHOLD REACHED; PROOF AUDIT PASSED

The research line contains a closed quantitative result strong enough for a standalone publication manuscript:

> **Hall/projective phase-profile stability.** There exists an absolute constant `C` such that for every nontrivial `STS(v)`,
>
> `min(rho_P,rho_H) <= C c_A/N`,
>
> where `rho_P,rho_H` are the proportions of independent triples generating `S_7` and `S_9`, `c_A` is the Král anti-mitre count, and `N=v(v-1)(v-3)/6`.

Equivalently, since `c_A/N=3alpha`,

`min(rho_P,rho_H) <= C_alpha alpha`.

The exact proof is isolated and publication-hardened in:

`alice-ruler-incidence/proofs/PHASE_STABILITY_PROOF.md`.

The mathematical audit was completed in commit
`5c8fc288973fe77ca9ee1d8f65dc83e9a21815ab`.

This is **phase-profile stability**, not edit-distance stability of the whole block set.

## Mandatory correction to research seed v0.6

The mirror-completion residual and Král's anti-mitre `C_A` were incorrectly identified as the same five-line configuration in the seed. They are different configurations:

- mirror residual = Danziger et al. configuration #7:
  `R_7={012,034,135,246,567}`;
- Král anti-mitre = Danziger et al. configuration #4:
  `C_A~={012,034,135,236,457}`.

Their exact five-line counting formulas imply

`c_A=2r_7`.

Therefore

`alpha=r_7/(6P(v))=c_A/(12P(v))`,

so the crucial zero-set equivalence survives:

`alpha=0 <=> c_A=0`.

The publication manuscript must correct the picture/name while retaining the completion simplex.

## Core rigorous results

### Completion layer

`kappa=p/P(v)`, `eta=m/(2P(v))`, `alpha=r_7/(6P(v))`,

`kappa+eta+alpha=1`.

At six lines, with `psi=f/P(v)`,

`d=kappa-psi`,

`0<=d<=min{kappa,alpha,(alpha+eta)/2}`.

The convex relaxation has the Hall/projective phantom edge on `alpha=0`, but exact realizability allows only the pure endpoints.

### Independent-triple phase graph

For an independent triple `tau`:

- phase P if `<tau>~=S_7`;
- phase H if `<tau>~=S_9`;
- phase D otherwise.

`G_ind` joins triples sharing two points.

`N=|V(G_ind)|=v(v-1)(v-3)/6`,

`deg G_ind=3(v-4)`.

Using `G_ind` as a principal induced subgraph of `J(v,3)` and Cauchy interlacing:

`mu_2(G_ind)>=v-3`.

Hence for every `A subset V(G_ind)`,

`e(A,A^c)>=(v-3)|A|(1-|A|/N)`.

For `V=P sqcup H sqcup D`, `s=e(P,H)`, `q=min{|P|,|H|}`:

`(v-3)q(1-q/N)<=s+3(v-4)|D|`.          (PI)

### Bulk charging

Every `D` root lies in an eight-point anti-mitre `C_A` witness containing all three root points.

The publication audit now includes explicit incidence-preserving relabellings from each representative five-block failure witness to canonical

`C_A=012,034,135,236,457`.

Therefore

`|D|<=56c_A`,

and since `c_A/N=3alpha`,

`rho_D<=168alpha`.

### Interface charging

For a mixed pair `(F,d)` with `F~=S_7` and at least one Hall line relative to `d`, the finite phase-purity proof forces a `D` query.

The localization audit now includes:

- a direct proof that every two-colouring of the Fano lines has a monochromatic pencil;
- a direct proof that `S_9=AG(2,3)` contains no `S_7` subsystem;
- isolation of the only use of four-point independence in the 2007 source proof and its valid replacement in the localized setting;
- complete classification of phase queries into four reconstruction forms:

`{d,u,v}`,
`{d_x,u,v}`,
`{u,d_x,d_y}`,
`{d_x,d_y,d_z}`.

The reverse fiber of each form is `O(v)`. For the first two forms this uses the bound that a fixed block lies in at most `(v-3)/4` Fano subsystems; for the last two, choosing `d` recovers a noncollinear generating triple of the Fano subsystem.

Thus an absolute constant `C_I` exists with

`s<=C_I v |D|`.                                (IB)

Combining (PI), (IB), and the bulk bound gives

`min(rho_P,rho_H)<=C c_A/N`.

## Proof-audit verdict

No unresolved logical step remains in the proof chain currently used for the main theorem.

The proof audit specifically closed the reviewer-sensitive points:

1. anti-mitre witness identification;
2. Fano line-colouring claim;
3. `S_9`/`S_7` exclusion;
4. localized dependence on four-point independence;
5. exhaustive phase-query templates;
6. `O(v)` reverse multiplicity;
7. normalization of the final stability constant;
8. separation of new quantitative deductions from the classical exact dichotomy.

This verdict concerns the mathematics, not yet final typesetting/release QA.

## Source audit

Classical/source-derived:

- Danziger–Mendelsohn–Grannell–Griggs five-line count formulas;
- Král–Máčajová–Pór–Sereni forbidden-configuration characterization;
- local `S_7/S_9` generation in the `C_A`-free case;
- their earlier finite local purity argument;
- Teirlinck's exact projective/affine local-to-global theorem;
- Johnson graph spectrum and Cauchy interlacing.

Candidate new layer:

- independent-triple phase graph;
- spectral phase isoperimetry;
- root-preserving quantitative anti-mitre charging `|D|<=56c_A`;
- localized finite-template interface charging;
- quantitative Hall/projective phase-profile stability.

Dedicated searches on Hall/projective stability, anti-mitre supersaturation, Steiner-quasigroup stability/removal, and phase-graph formulations found no equivalent quantitative theorem as of 2026-09-12. This is a serious priority check, not an absolute priority guarantee.

## Publication assembly now active

The mathematical threshold is crossed. The remaining work is publication hardening:

1. synchronize the strengthened proof text into `paper/PHASE_RIGIDITY_EN.md`;
2. synchronize the same additions into `paper/PHASE_RIGIDITY_RU.md`;
3. finish bibliography normalization for the remaining background references;
4. normalize notation and theorem cross-references across EN/RU;
5. generate final RU/EN publication PDFs;
6. run visual PDF QA;
7. prepare the final Zenodo package and metadata;
8. after DOI issuance, insert the DOI into both manuscripts and this status file.

Do **not** upload the current manuscript package to Zenodo before steps 1–6 are complete.

The next mathematical extension after this paper is **edit-distance rigidity**: whether `alpha=o(1)` forces the entire STS, after few block edits, close to a projective or Hall system. This is explicitly not claimed in the present theorem.
