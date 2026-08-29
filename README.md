# Riemann Hypothesis with Commander Sol

**Research programme:** *Reflections on the Riemann Hypothesis and the Persistence of Logarithmic Arithmetic Structure with Commander Sol*

A reproducible research repository for computational experiments on Riemann-zeta Argand loops, integer-lattice encodings, Dirichlet-frequency persistence, sampling/aliasing interpretations, null models, and information survival under nonlinear geometric quantization.

## Zenodo mathematical community

**Reflections on Mathematics with Commander Sol**  
https://zenodo.org/communities/commander-sol-math/

The community collects the broader mathematical publication line, including work on the Riemann Hypothesis, prime structures, Prime-Successor Algebra, operator methods, adelic structures, FCOA/admissibility geometry, hybrid memory, and related rigorous explorations in the “Reflections / Размышлизмы” format.

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

### FCOA · Hybrid Memory — Article A

**Reflections on Hybrid Memory with Commander Sol: Minimal Joint Rigidity of Partial Operations**  
Zenodo DOI: **10.5281/zenodo.22165651**  
Persistent URL: https://doi.org/10.5281/zenodo.22165651  
GitHub companion: [`papers/FCOA-HYBRID-MEMORY/`](papers/FCOA-HYBRID-MEMORY/)

Core problem:

`Aut(star) != 1, Aut(diamond) != 1, but Aut(star,diamond) = 1`

with sharp finite hybrid-memory thresholds, Lift Compatibility, Joint Fiber Synchronization (JFS), and Carrier-Value Selection (CVS).

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
 data/          source and derived data (large files may be release assets)
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
- FCOA · HYBRID MEMORY · ARTICLE A — published, DOI 10.5281/zenodo.22165651; GitHub companion available

## AI collaboration disclosure

Commander Sol is used as a research collaborator for hypothesis generation, computational design, code assistance, falsification planning, literature triage, and manuscript drafting. Mathematical claims remain subject to explicit computational or formal verification and are attributed to the human author unless otherwise stated.
