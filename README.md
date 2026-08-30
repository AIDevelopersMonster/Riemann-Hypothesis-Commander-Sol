# Riemann Hypothesis with Commander Sol

**Research programme:** *Reflections on the Riemann Hypothesis and the Persistence of Logarithmic Arithmetic Structure with Commander Sol*

A reproducible research repository for computational experiments on Riemann-zeta Argand loops, integer-lattice encodings, Dirichlet-frequency persistence, sampling/aliasing interpretations, null models, and information survival under nonlinear geometric quantization.

## Zenodo mathematical community

**Reflections on Mathematics with Commander Sol**  
https://zenodo.org/communities/commander-sol-math/

The community collects the broader mathematical publication line, including work on the Riemann Hypothesis, prime structures, Prime-Successor Algebra, operator methods, adelic structures, FCOA/admissibility geometry, and related rigorous explorations in the “Reflections / Размышлизмы” format.

## Published starting point

**RH-SOL-01 · LATTICE**  
*Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization*  
Author: **Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Zenodo DOI: **10.5281/zenodo.22060296**

## Additional published mathematical branches

### FCOA · Admissibility Geometry

**Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier**  
Zenodo DOI: **10.5281/zenodo.22129787**  
GitHub companion: [`papers/FCOA-ADMISSIBILITY-GEOMETRY/`](papers/FCOA-ADMISSIBILITY-GEOMETRY/)  
Interactive demo: [`demos/fcoa-domain-compilation/`](demos/fcoa-domain-compilation/)

Core progression:

`M0 -> G1 -> G2`

with the central mechanism

`relation -> partial-operation domain -> recoverable structural memory`.

### FCOA · Value-Rigidity / Identity Digraphs

**Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers**  
Zenodo DOI: **[10.5281/zenodo.22160014](https://doi.org/10.5281/zenodo.22160014)**  
GitHub companion: [`papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/`](papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/)

Core results:

`|O|=1 -> VRI=1`, while `|O|=2 -> VRI=n!` is attainable; the sparsest maximally rigid two-output fiber is linked to the classical minimum identity-digraph extremal `m(n)`, with exact finite evaluation, second-order asymptotics, and a partial-layer phase law.

### FCOA-Z · Symmetric Coordinate Completion

**Reflections on How a Ray Becomes an Axis: And Why Old Operations Reveal New Local Laws after a Second Direction Appears**  
Zenodo DOI: **[10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)**  
GitHub companion: [`delegated/FCOA_Z_SYMMETRIC_LINE/`](delegated/FCOA_Z_SYMMETRIC_LINE/)

Core progression:

`rooted ray -> minimal reversible completion -> derived reflection -> legacy-operation transfer -> punctured radialization -> mixed-sector localization`.

### FCOA-Z · Classical Shadows and Reconstruction

**Classical Algebra as a Resolution-Dependent Shadow of a One-Dimensional Partial Geometry: Collapse, Matrix Units, and Reconstruction in FCOA-Z**  
Zenodo DOI: **[10.5281/zenodo.22179357](https://doi.org/10.5281/zenodo.22179357)**  
GitHub companion: [`delegated/FCOA_Z_SYMMETRIC_LINE/`](delegated/FCOA_Z_SYMMETRIC_LINE/)

Core progression:

`associative collapse -> root isolation -> matrix units -> finitary matrix shadow -> signed-line reconstruction -> provenance/definedness/terminal no-go`.

All results in this paper remain on the single signed FCOA-Z coordinate line; matrix rank is not interpreted as spatial dimension.

## Programme map

The project is organized as a sequence of labeled research branches:

`LATTICE -> SHIFT -> REALZERO -> FIREWALL -> POISSON -> NYQUIST -> SURVIVAL -> RATE -> DECODE -> MINCODE -> LFUNCTIONS -> PRIMESET -> ENVELOPE -> RESIDUAL -> SYNTHESIS`

See [`programme/SERIES_MAP.md`](programme/SERIES_MAP.md).

## Reproducibility principle

Each article branch should contain:

1. a precise mathematical object;
2. a preregistered or clearly stated hypothesis;
3. a complete data-generation pipeline;
4. null/surrogate controls;
5. scripts that regenerate figures/tables;
6. a `RESULTS.md` that records positive **and negative** results;
7. release metadata for Zenodo.

## Repository layout

```text
programme/      programme map, terminology, research questions
papers/         one folder per RH-SOL article and related mathematical publication branches
src/            reusable research code
experiments/    executable experiment branches
data/           source and derived data (large files may be release assets)
demos/          interactive demonstrations
reviews/        external reviews and audit notes
releases/       Zenodo/release metadata
scripts/        utility and reproducibility scripts
```

## Status

- RH-SOL-01 · LATTICE — published
- RH-SOL-02 · SHIFT — next priority
- RH-SOL-03 · REALZERO — planned
- RH-SOL-04 · FIREWALL — planned
- FCOA · ADMISSIBILITY GEOMETRY — published, DOI 10.5281/zenodo.22129787; GitHub companion restored
- FCOA · VALUE-RIGIDITY / IDENTITY DIGRAPHS — published, DOI 10.5281/zenodo.22160014
- FCOA-Z · SYMMETRIC COORDINATE COMPLETION — published, DOI 10.5281/zenodo.22169264; research branch continues
- FCOA-Z · CLASSICAL SHADOWS / RECONSTRUCTION — published, DOI 10.5281/zenodo.22179357; one-dimensional research continues

## AI collaboration disclosure

Commander Sol is used as a research collaborator for hypothesis generation, computational design, code assistance, falsification planning, literature triage, and manuscript drafting. Mathematical claims remain subject to explicit computational or formal verification and are attributed to the human author unless otherwise stated.
