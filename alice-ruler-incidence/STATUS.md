# Alice Throws Away the Ruler — research status

**Branch:** `research/alice-ruler-incidence`  
**Working folder:** `alice-ruler-incidence/`  
**Status date:** 2026-09-12  
**Author line:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## Scope

Research line on arithmetic and rigidity emerging from bounded incidence rules in Steiner triple systems (STS), continuing the RU/EN research seed **“Alice Throws Away the Ruler / Алиса выбрасывает линейку” v0.6**.

The current goal is no longer another catalogue of small configurations. The target is a quantitative Hall/projective two-phase rigidity theorem built from local closure types of independent triples.

## Stable input from v0.6

For an STS(v), with

- `p` = Pasch count,
- `m` = mitre count,
- `a` = residual five-line anti-mitre configuration count `C_A`,
- `P(v)=v(v-1)(v-3)/24`,

use

`kappa = p/P(v)`, `eta = m/(2P(v))`, `alpha = a/(6P(v))`,

so that

`kappa + eta + alpha = 1`.

At six lines, with `f` the Fano-line count, set

`psi = f/P(v)`

(and `phi=f/p` when `p>0`, so `psi=kappa*phi`).

The projected six-line coherence polytope has candidate vertices

`A=(0,0,0)`, `H=(0,1,0)`, `B=(1/3,0,0)`, `D=(1/3,1/3,0)`, `P=(1,0,1)`

in `(kappa,eta,psi)` and yields the defect budget

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

The graph is the induced subgraph of the Johnson graph `J(v,3)` obtained by deleting the STS blocks. The earlier spectral-cut argument gave, for `A subset V(G_ind)` with `|A|<=N/2`,

`e_G(A,A^c) >= (v/2 - 3)|A|`.

A stronger interlacing route is under audit: because deleting STS blocks gives a principal submatrix of the Johnson adjacency matrix, one expects `lambda_2(G_ind) <= 2v-9`, hence Laplacian gap at least `v-3`, which would sharpen the universal cut inequality.

## Quantitative phase inequality — proved modulo the local phase-switch audit

Write the vertex partition

`V = P sqcup H sqcup D`,

and let

`s = e_G(P,H)`.

From the expansion estimate and `e(P,D) <= 3(v-4)|D|`, one obtains

`(v/2 - 3) min{|P|,|H|} <= s + 3(v-4)|D|`.

Define the phase-coherence energy

`E(S) = s + 3(v-4)|D|`.

Then macroscopic P/H phase mixture has a positive interface-or-bulk cost.

The exact `C_A`-free Hall/projective dichotomy is recovered if two classical local implications are used:

1. no `C_A` => no defective closure `D`;
2. no `C_A` => no adjacent `P/H` phase switch.

**Important:** the second implication must be re-audited directly against the cited Král–Máčajová–Pór–Sereni proof before being promoted to a standalone new lemma.

## Current proof obligation

The intended strengthening is to eliminate the rooted/interface quantities and bound everything by the ordinary anti-mitre count `c_A`.

Introduce rooted witness counts

`R_D = # {(tau,C): tau in D and C ~= C_A is a canonical local witness}`,

`R_PH = # {(e,C): e in E(P,H) and C ~= C_A is a canonical switch witness}`.

Need bounds of the form

`R_D >= |D|`, `R_PH >= s`,

and multiplicity controls

`R_D <= M_D(v)c_A`, `R_PH <= M_PH(v)c_A`.

The hoped-for scaling is

`M_D = O(1)`, `M_PH = O(v)`.

If achieved, the target anti-mitre stability theorem is

`min(rho_P,rho_H) <= C * rho_{C_A}`

with the correct normalizations.

## Publication gate

Do **not** publish yet merely from the v0.6 seed.

Publication threshold is crossed only after:

1. direct proof audit of the local phase-switch implication;
2. rigorous rooted witness multiplicity count, or a deliberately weaker theorem stated in interface-or-bulk form;
3. priority search for existing STS stability / phase-graph / Johnson-expansion formulations;
4. final novelty separation between classical ingredients and new deductions;
5. theorem numbering, proofs, bibliography/DOI audit, RU/EN synchronization.

If rooted anti-mitre counting closes, immediately prepare the publication manuscript and Zenodo-ready RU/EN versions without an intermediate research-seed PDF.
