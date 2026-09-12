# Alice Throws Away the Ruler II

## Phase Rigidity in Steiner Triple Systems
### Quantitative Hall–Projective Stability from Anti-Mitre Defects

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Publication status:** Published on Zenodo  
**Zenodo DOI:** [10.5281/zenodo.22722951](https://doi.org/10.5281/zenodo.22722951)

Russian title:

**Фазовая жёсткость в системах троек Штейнера: количественная устойчивость Холл–проективной дихотомии через anti-mitre-дефекты**

---

## Abstract / Аннотация

This paper develops a quantitative version of the classical projective/Hall dichotomy for Steiner triple systems. Every independent triple is assigned one of three local closure phases:

- `P` if it generates the Fano subsystem `S_7`;
- `H` if it generates the affine plane `S_9`;
- `D` otherwise.

The independent-triple graph `G_ind(S)` joins two independent triples when they share exactly two points. Because this graph is a regular induced subgraph of the Johnson graph `J(v,3)`, Cauchy interlacing gives the Laplacian spectral gap

```math
\mu_2(G_{\rm ind})\ge v-3.
```

This yields a phase-isoperimetric inequality: a macroscopic mixture of the projective and Hall phases must pay either through a direct `P/H` interface or through a positive density of defective `D` roots.

The classical anti-mitre configuration `C_A` is then used as the local defect certificate. The proof establishes

```math
|D|\le 56c_A,
```

and a finite-interface charging argument gives an absolute constant `C_I` such that

```math
s=e(P,H)\le C_Iv|D|.
```

Combining these estimates with spectral expansion yields the main quantitative stability theorem: there exists an absolute constant `C>0` such that

```math
\boxed{
\min\{\rho_P,\rho_H\}
\le
C\frac{c_A}{N}
}
```

where

```math
N=\frac{v(v-1)(v-3)}6
```

is the number of independent triples. Thus a small normalized anti-mitre count forces almost all independent triples into one of the two pure closure regimes.

The zero-defect case recovers the exact projective/Hall dichotomy.

### Scope

The theorem is a **phase-profile stability theorem**. It does **not** claim an edit-distance theorem saying that the entire block set is close to a projective or Hall Steiner triple system. That stronger structural-reconstruction problem remains open in this research line.

---

## Important correction to research seed v0.6

The publication audit identified that the anti-mitre `C_A` used in the classical Hall/projective characterization is not isomorphic to the five-line residual configuration produced by the earlier mirror-completion experiment.

Using the standard five-line configuration numbering:

- anti-mitre `C_A` is configuration **#4**;
- the mirror residual is configuration **#7**.

Their occurrence counts satisfy the exact identity

```math
c_A=2r_7.
```

Therefore the completion-simplex coordinate remains valid after correcting the configuration identification:

```math
\alpha=\frac{r_7}{6P(v)}
      =\frac{c_A}{12P(v)},
```

so in particular

```math
\alpha=0\iff c_A=0.
```

The zero-defect and phantom-edge conclusions therefore survive the correction.

---

## Repository materials

- [English publication manuscript](paper/PHASE_RIGIDITY_EN.md)
- [Русская публикационная рукопись](paper/PHASE_RIGIDITY_RU.md)
- [Publication-core proof note](proofs/PHASE_STABILITY_PROOF.md)
- [Research status and proof obligations history](STATUS.md)
- [Publication checklist](paper/PUBLICATION_CHECKLIST.md)

Canonical publication record:

**Zenodo:** [https://doi.org/10.5281/zenodo.22722951](https://doi.org/10.5281/zenodo.22722951)

---

## Citation

Suggested short citation:

> Malachevsky, A.A. (2026). *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects*. Alice Throws Away the Ruler II. Zenodo. https://doi.org/10.5281/zenodo.22722951

---

## Research continuation

The natural next problem is to pass from **phase-profile stability** to genuine **structural/edit-distance rigidity**: determine whether sufficiently small anti-mitre density forces the complete Steiner triple system to be quantitatively close to an actual projective or Hall model whenever the order permits such a model.
