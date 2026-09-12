# Alice Throws Away the Ruler — research status

**Branch:** `research/alice-ruler-incidence`  
**Working folder:** `alice-ruler-incidence/`  
**Status date:** 2026-09-12  
**Author line:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## Scope

Research line on arithmetic and rigidity emerging from bounded incidence rules in Steiner triple systems (STS), continuing the RU/EN research seed **“Alice Throws Away the Ruler / Алиса выбрасывает линейку” v0.6**.

The current goal is a quantitative Hall/projective two-phase rigidity theorem built from local closure types of independent triples.

## Stable input from v0.6

For an STS(v), with

- `p` = Pasch count,
- `m` = mitre count,
- `a=c_A` = residual five-line configuration count `C_A`,
- `P(v)=v(v-1)(v-3)/24`,

use

`kappa = p/P(v)`, `eta = m/(2P(v))`, `alpha = a/(6P(v))`,

so that

`kappa + eta + alpha = 1`.

At six lines, with `f` the Fano-line count, set

`psi = f/P(v)`

(and `phi=f/p` when `p>0`, so `psi=kappa*phi`).

The projected six-line coherence polytope has vertices

`A=(0,0,0)`, `H=(0,1,0)`, `B=(1/3,0,0)`, `D=(1/3,1/3,0)`, `P=(1,0,1)`

in `(kappa,eta,psi)` and yields

`d := kappa-psi >= 0`,

`d <= min{kappa, alpha, (alpha+eta)/2}`.

On `alpha=0`, the convex relaxation contains the entire Hall/projective segment

`E={(t,1-t,t):0<=t<=1}`,

while realizable `C_A`-free STS lie only at the Hall or projective endpoints. This is the **phantom-edge / ghost-edge** phenomenon. Any convex outer relaxation containing both endpoints necessarily contains the whole segment, so linear projected configuration inequalities alone cannot prove the exact dichotomy.

## Phase graph

For every independent (non-block) triple `tau`, define its closure phase

- `P` if `<tau> ~= S_7` (Fano/projective closure),
- `H` if `<tau> ~= S_9` (affine Hall closure),
- `D` otherwise.

Let `G_ind(S)` be the graph whose vertices are independent triples, with adjacency when two triples share exactly two points.

Number of vertices:

`N = C(v,3) - v(v-1)/6 = v(v-1)(v-3)/6`.

Degree:

`d_G = 3(v-4)`.

### Spectral expansion — rigorous

`G_ind(S)` is the induced principal subgraph of the Johnson graph `J(v,3)` obtained by deleting the STS blocks. The Johnson adjacency eigenvalues are

`3(v-3), 2v-9, v-7, -3`.

By Cauchy interlacing,

`lambda_2(G_ind) <= 2v-9`.

Since `G_ind` is `3(v-4)`-regular, its Laplacian gap satisfies

`mu_2(G_ind) >= 3(v-4)-(2v-9)=v-3`.

Hence for every `A subset V(G_ind)`,

`e_G(A,A^c) >= (v-3)|A|(1-|A|/N)`.

In particular, when `|A|<=N/2`,

`e_G(A,A^c) >= ((v-3)/2)|A|`.

This sharpens the earlier crude coefficient `(v/2-3)` and proves connectivity for every nontrivial STS.

## Quantitative phase isoperimetry — rigorous

Write

`V = P sqcup H sqcup D`,

let

`s = e_G(P,H)`,

and put

`q = min{|P|,|H|}`.

Applying the spectral cut bound to the smaller pure phase and using

`e(P,D) <= 3(v-4)|D|`

(or the symmetric H version) gives

`(v-3) q (1-q/N) <= s + 3(v-4)|D|`.       (PI)

The coarse consequence is

`((v-3)/2) min{|P|,|H|} <= s + 3(v-4)|D|`.  (PI-coarse)

With

`rho_P=|P|/N`, `rho_H=|H|/N`, `rho_D=|D|/N`,

`sigma = s/[3(v-4)N]`,

we obtain

`min(rho_P,rho_H) <= [6(v-4)/(v-3)] (sigma+rho_D)`.

Define the phase-coherence energy

`E(S)=s+3(v-4)|D|`.

Then (PI) is a discrete surface-tension inequality: a macroscopic P/H mixture has a macroscopic interface-or-bulk cost.

A sharper inverted form is available. Put

`eps = E(S)/[(v-3)N]`.

If `eps<=1/4`, then

`q/N <= (1-sqrt(1-4 eps))/2`.

## Source audit: published proof versus technical report

This distinction is now mandatory.

### Published Král–Máčajová–Pór–Sereni paper (Canadian J. Math. 62 (2010))

The published proof establishes:

1. `C_A`-free implies every independent triple generates `S_7` or `S_9`;
2. a theorem of Teirlinck then implies that all independent triples have one type: all `S_7` or all `S_9`;
3. hence a `C_A`-free STS is projective or Hall.

The published paper does **not** contain the earlier claimed standalone “15-point local phase-switch lemma”. That claim is withdrawn.

### Authors' 2007 technical report

An earlier official technical report by the same authors contains a longer finite local proof of the purity step. Starting from an `S_7` subsystem `F`, an external point `D`, and a mixed red/blue assignment of Fano-line pairs corresponding to `S_7/S_9` behavior, it performs a finite sequence of Steiner completions and derives a contradiction under the assumption that every queried independent triple remains of type `S_7` or `S_9`.

Safe consequence for the current program:

> a local P/H phase mixture around `(F,D)` forces at least one `D`-phase triple in a bounded Steiner closure of `(F,D)`.

The bound is an absolute constant independent of `v`; do not use the earlier unsupported number 15 until the finite proof is fully template-audited.

This qualitative bounded-witness principle is classical/source-derived. The intended **quantitative charging theorem** below is the new target.

## Current proof obligations

There are now two clean finite-fiber problems.

### A. Phase-interface charging

Every `P-H` edge determines a Fano subsystem `F` from its P endpoint and an external point `D_ext` from its H endpoint. For fixed `(F,D_ext)`, only constantly many P-H edges are possible (at most the number of point-pairs/triples inside the seven-point Fano subsystem).

The 2007 finite proof supplies at least one `D`-phase triple in a bounded term-closure of a mixed `(F,D_ext)`.

Need to prove a fiber bound of the form

`# {(F,D_ext): canonical witness is a fixed tau_D} <= C_switch * v`.

This would give

`s <= C_1 v |D|`.

### B. Rooted anti-mitre charging

The published local proof that `C_A`-free forces each independent triple into `S_7` or `S_9` is constructive: starting from a root independent triple it performs finitely many Steiner completions; if one of the required identities fails, a copy of `C_A` is exposed.

Need to choose a canonical first failure and prove

`# {root D-triples charged to a fixed C_A copy} <= C_D`

with an absolute constant `C_D`.

This would give

`|D| <= C_D c_A`.

Combining A+B with (PI) would yield the target anti-mitre stability theorem

`min(rho_P,rho_H) <= C * rho_{C_A}`

(up to the exact normalization chosen for the density of `C_A`).

## Nearby literature / novelty boundary

Known ingredients:

- projective/Hall characterization and `C_A`-free dichotomy;
- local `S_7/S_9` generation in the `C_A`-free case;
- the old finite local proof of phase purity;
- Johnson graph spectrum / interlacing.

Current candidate new layer:

- the independent-triple phase graph as the carrier of the Hall/projective dichotomy;
- the explicit spectral phase-isoperimetric inequality (PI);
- the phase-coherence energy interpretation;
- quantitative finite-fiber charging of P/H interfaces and `D` closures into `C_A` copies;
- consequent anti-mitre stability theorem, if A+B close.

Priority search has not yet found an equivalent quantitative phase-graph theorem; this remains provisional until the final literature audit.

## Publication gate

Do **not** publish yet.

Publication threshold is crossed only after:

1. finite-template audit of the 2007 mixed-phase proof;
2. proof or failure of the `O(v)` phase-interface fiber bound;
3. proof or failure of the `O(1)` D-to-`C_A` fiber bound;
4. priority search for STS stability / phase-graph / Johnson-expansion formulations;
5. theorem/proof and bibliography/DOI audit, RU/EN synchronization.

If A+B close, immediately move from research seed to a publication manuscript and prepare Zenodo-ready RU/EN versions without an intermediate PDF.
