# Riemann Hypothesis with Commander Sol

**Research programme:** *Reflections on the Riemann Hypothesis and the Persistence of Logarithmic Arithmetic Structure with Commander Sol*

A reproducible research repository for computational experiments on Riemann-zeta Argand loops, integer-lattice encodings, Dirichlet-frequency persistence, sampling/aliasing interpretations, null models, and information survival under nonlinear geometric quantization.

## Zenodo mathematical community

**Reflections on Mathematics with Commander Sol**  
https://zenodo.org/communities/commander-sol-math/

The community collects the broader mathematical publication line, including work on the Riemann Hypothesis, prime structures, Prime-Successor Algebra, operator methods, adelic structures, and related rigorous explorations in the “Reflections / Размышлизмы” format.

## Published starting point

**RH-SOL-01 · LATTICE**  
*Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization*  
Author: **Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Zenodo DOI: **10.5281/zenodo.22060296**

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
papers/         one folder per RH-SOL article
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

## AI collaboration disclosure

Commander Sol is used as a research collaborator for hypothesis generation, computational design, code assistance, falsification planning, literature triage, and manuscript drafting. Mathematical claims remain subject to explicit computational or formal verification and are attributed to the human author unless otherwise stated.