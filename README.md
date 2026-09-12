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

### Alice Throws Away the Ruler II · Phase Rigidity in Steiner Triple Systems

**Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects**  
Russian parallel: **Фазовая жёсткость в системах троек Штейнера: количественная устойчивость Холл–проективной дихотомии через anti-mitre-дефекты**  
Zenodo DOI: **[10.5281/zenodo.22722951](https://doi.org/10.5281/zenodo.22722951)**  
GitHub companion: [`alice-ruler-incidence/`](alice-ruler-incidence/)

Core result:

`small normalized anti-mitre count -> one of the two local closure phases (projective S_7 or Hall S_9) has small minority density`.

The paper introduces the independent-triple phase graph, proves the spectral gap `mu_2 >= v-3`, establishes `|D| <= 56 c_A`, controls direct `P/H` interfaces by `s <= C_I v |D|`, and derives the quantitative phase-profile stability theorem

`min(rho_P,rho_H) <= C c_A/N`.

The theorem is intentionally phase-profile stability, not an edit-distance theorem for the whole Steiner triple system.

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

## FCOA publication packages in final Zenodo stage

### FCOA-Z · Ray to Axis / Local Law Differentiation

**Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears**  
Assigned Zenodo DOI: **[10.5281/zenodo.22171473](https://doi.org/10.5281/zenodo.22171473)**  
GitHub companion: [`papers/FCOA-Z-RAY-AXIS/`](papers/FCOA-Z-RAY-AXIS/)

Core progression:

`rooted ray -> reversible completion -> two-sided axis -> derived reflection -> legacy transfer -> local-law differentiation -> mixed-sector frontier`

The theorem-complete bilingual v1.1 package has passed hostile-audit scope corrections and final PDF render/preflight. The DOI is embedded in both English and Russian publication PDFs. Until the Zenodo record is visibly published, this repository labels the item as final-stage rather than published.

### FCOA-Z · Prescribed-Stabilizer Support

**Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra: Wreath Coherence, Partition Compression, and Exact Orbital Separation**  
Russian parallel: **Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре: Wreath-когерентность, сжатие разбиений и точное орбитальное разделение**  
GitHub companion: [`papers/FCOA-Z-PRESCRIBED-STABILIZER-SUPPORT/`](papers/FCOA-Z-PRESCRIBED-STABILIZER-SUPPORT/)  
Zenodo DOI: **pending deposit**

Core results:

- exact global coherence support `b(b-1)t` for transitive branch action;
- exact arbitrary-partition phase-coherence support `t sum_j n_j(n_j-1)`;
- exact partition-only reduction `t^2 d(P)`;
- Partition-Overgroup Dichotomy and Macro-Mover Double-Coset Lemma;
- exact Orbital XOR-Separation Program for arbitrary finite partition type;
- explicit support/resource non-monotonicity between partition-only and phase-coherent memory.

The research, proof, bibliography, reproducibility, and PDF visual-QA gates are all passed. Exact verification covers every integer partition with `2 <= b <= 7`: 43 partition types and 1468 invariant orbital unions, all passing the direct symmetric-group check. The package is ready for Zenodo deposit; once a DOI is assigned, it must be propagated into this README and the branch release metadata.

## HATTER-SOL · Arithmetic Tea Party

**Tea Parties in the Additive–Multiplicative World with Hatter Sol** is the "Reflections" series on which parts of familiar arithmetic belong to representation, which belong to structure, and how prime symmetry changes as structural information is forgotten or partially restored.

### HATTER-SOL-01 · The Number Line, the Observer, and Two Operations

**A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations**  
Zenodo DOI: **[10.5281/zenodo.22639237](https://doi.org/10.5281/zenodo.22639237)**

Core hinge:

`Aut(N_{>0}, x) ~= Sym(P)`

versus

`Aut(N,+,x,0,1) = 1`.

### HATTER-SOL-02 · Two Teapots, One Cup: “Who Are You?” Among the Primes

Russian parallel: **Два чайника, одна чашка: «Кто ты?» среди простых**  
Zenodo DOI: **[10.5281/zenodo.22656414](https://doi.org/10.5281/zenodo.22656414)**

Core results:

- exact finite congruence-orbit count:
  `|F| + prod_{p in F} tau(p-1)`;
- exact finite quadratic-probe orbit count:
  `|F| + 2^|F|`;
- finite-information barrier;
- exact rigidity criterion via injective Legendre signatures;
- arbitrarily sparse rigidifying families;
- optimal finite coding law:
  `kappa_2(S) = ceil(log_2 |S|)`.

GitHub companion and permanent series folder: [`papers/HATTER-SOL/`](papers/HATTER-SOL/)  
Follow future notes here: **https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL**

Current HATTER-SOL-03 frontier: can a finite natural mechanism generate, internally, a separating family rich enough to recover rigidity without an externally named infinite family of probes?

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
- ALICE-RULER-II · PHASE RIGIDITY — published, DOI 10.5281/zenodo.22722951; quantitative Hall/projective phase-profile stability
- FCOA · ADMISSIBILITY GEOMETRY — published, DOI 10.5281/zenodo.22129787; GitHub companion restored
- FCOA · VALUE-RIGIDITY / IDENTITY DIGRAPHS — published, DOI 10.5281/zenodo.22160014
- FCOA-Z · RAY TO AXIS / LOCAL LAW DIFFERENTIATION — final Zenodo stage, DOI 10.5281/zenodo.22171473 assigned and embedded; publication package audited
- FCOA-Z · PRESCRIBED-STABILIZER SUPPORT — research/PDF/source thresholds passed; exact verifier `ALL PASS` through `b<=7`; ready for Zenodo deposit; DOI pending
- HATTER-SOL-01 — published, DOI 10.5281/zenodo.22639237
- HATTER-SOL-02 — published, DOI 10.5281/zenodo.22656414

## AI collaboration disclosure

Commander Sol is used as a research collaborator for hypothesis generation, computational design, code assistance, falsification planning, literature triage, and manuscript drafting. Mathematical claims remain subject to explicit computational or formal verification and are attributed to the human author unless otherwise stated.
