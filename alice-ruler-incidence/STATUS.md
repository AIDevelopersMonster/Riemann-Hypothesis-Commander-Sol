# Alice Throws Away the Ruler — research status

**Branch:** `research/alice-ruler-incidence`  
**Working folder:** `alice-ruler-incidence/`  
**Status date:** 2026-09-12  
**Author line:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## STATUS: PUBLICATION THRESHOLD REACHED

The research line now contains a closed quantitative result strong enough to justify a standalone publication manuscript:

> **Hall/projective phase stability.** There exists an absolute constant `C` such that for every nontrivial `STS(v)`,
>
> `min(rho_P,rho_H) <= C alpha`,
>
> where `rho_P,rho_H` are the proportions of independent triples generating `S_7` and `S_9`, and `alpha` is the residual completion-simplex coordinate, equivalently one third of the normalized Král anti-mitre count: `c_A/N=3alpha`.

The exact proof is isolated in:

`alice-ruler-incidence/proofs/PHASE_STABILITY_PROOF.md`.

This is **phase-profile stability**, not edit-distance stability of the whole block set.

## Mandatory correction to research seed v0.6

The mirror-completion residual and Král's anti-mitre `C_A` were incorrectly identified as the same five-line configuration in the seed. They are different configurations:

- mirror residual = Danziger et al. configuration #7:
  `R_7={012,034,135,246,567}`;
- Král anti-mitre = Danziger et al. configuration #4, e.g.
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

A branch-by-branch audit of the constructive local `S_7/S_9` lemma shows that every `D` root lies in an eight-point anti-mitre `C_A` witness containing all three root points.

Therefore

`|D|<=56c_A`,

and since `c_A/N=3alpha`,

`rho_D<=168alpha`.

### Interface charging

The old finite local purity proof can be read as a fixed finite list of phase queries around a mixed pair `(F,D_ext)` with `F~=S_7`.

Every queried D-root has, up to Fano symmetry, one of four reconstruction forms:

`{D_ext,u,v}`,
`{D_x,u,v}`,
`{u,D_x,D_y}`,
`{D_x,D_y,D_z}`.

The reverse fiber of each form is `O(v)`. For the first two forms this uses the bound that a fixed block lies in at most `(v-3)/4` Fano subsystems; for the last two, choosing `D_ext` recovers a generating triple of the Fano subsystem.

Thus an absolute constant `C_I` exists with

`s<=C_I v |D|`.                                (IB)

Combining (PI), (IB), and the bulk bound gives

`min(rho_P,rho_H)<=C alpha`.

## Source audit

Classical/source-derived:

- Danziger–Mendelsohn–Grannell–Griggs five-line count formulas;
- Král–Máčajová–Pór–Sereni forbidden-configuration characterization;
- local `S_7/S_9` generation in the `C_A`-free case;
- their earlier finite local purity argument;
- Johnson graph spectrum and Cauchy interlacing.

Candidate new layer:

- independent-triple phase graph;
- spectral phase isoperimetry;
- root-preserving quantitative anti-mitre charging `|D|<=56c_A`;
- finite-template interface charging;
- quantitative Hall/projective phase stability.

Dedicated searches on Hall/projective stability, anti-mitre supersaturation, Steiner-quasigroup stability/removal, and phase-graph formulations found no equivalent quantitative theorem as of 2026-09-12. This is a serious priority check, not an absolute priority guarantee.

## Publication assembly now active

Next actions are publication work, not another research-seed PDF:

1. rewrite the English manuscript around the quantitative phase theorem;
2. produce synchronized Russian version;
3. correct residual `R_7` versus anti-mitre `C_A` throughout v0.6;
4. state all constants and finite-template claims conservatively;
5. full theorem/numbering/bibliography/DOI audit;
6. only then generate final RU/EN publication PDFs and Zenodo package.

The next mathematical extension after this paper is **edit-distance rigidity**: whether `alpha=o(1)` forces the entire STS, after few block edits, close to a projective or Hall system. This is explicitly not claimed in the present theorem.
