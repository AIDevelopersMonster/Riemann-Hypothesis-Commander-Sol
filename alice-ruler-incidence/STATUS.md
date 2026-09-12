# Alice Throws Away the Ruler — research status

**Branch:** `research/alice-ruler-incidence`  
**Working folder:** `alice-ruler-incidence/`  
**Status date:** 2026-09-12  
**Author line:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196

## Scope

Research line on arithmetic and rigidity emerging from bounded incidence rules in Steiner triple systems (STS), continuing the RU/EN research seed **“Alice Throws Away the Ruler / Алиса выбрасывает линейку” v0.6**.

Current target: a quantitative Hall/projective two-phase rigidity theorem built from local closure types of independent triples.

## Mandatory correction to v0.6: residual #7 is not Král's anti-mitre C_A

This nomenclature error was found during the publication audit.

The residual five-line configuration produced by the mirror-completion test is Danziger–Mendelsohn–Grannell–Griggs configuration **#7**:

`R_7 = {012,034,135,246,567}`.

Its count is

`r_7 = n(v)/4 - 6p - 3m`,

where `n(v)=v(v-1)(v-3)=24P(v)`.

The anti-mitre configuration `C_A` used by Král–Máčajová–Pór–Sereni is a different eight-point five-line configuration. In the same 56-configuration table it is configuration **#4**, e.g.

`C_A ~= {012,034,135,236,457}`,

with count

`c_A = n(v)/2 - 12p - 6m`.

Therefore the two configurations are not isomorphic, but their counts satisfy the exact identity

`c_A = 2 r_7`.

Hence the completion-simplex coordinate must be written

`alpha = r_7/(6P(v)) = c_A/(12P(v))`.

Consequently the important zero-set statement survives unchanged:

`alpha=0  <=>  r_7=0  <=>  c_A=0`.

Thus the Hall/projective phantom-edge argument is still valid, but the manuscript must never identify `R_7` itself with the anti-mitre `C_A`.

## Completion simplex and six-line projection

For an STS(v), let

- `p` = Pasch count,
- `m` = mitre count,
- `r_7` = count of residual configuration #7,
- `P(v)=v(v-1)(v-3)/24`.

Define

`kappa=p/P(v)`, `eta=m/(2P(v))`, `alpha=r_7/(6P(v))=c_A/(12P(v))`.

Then

`kappa+eta+alpha=1`.

At six lines, with `f` the Fano-line count, set `psi=f/P(v)`. The projected coherence polytope yields

`d:=kappa-psi >= 0`,

`d <= min{kappa,alpha,(alpha+eta)/2}`.

On `alpha=0`, the convex relaxation contains the Hall/projective segment

`E={(t,1-t,t):0<=t<=1}`,

while realizable systems lie only at the Hall or projective endpoints because `alpha=0 <=> c_A=0` and the classical characterization applies. This is the **phantom-edge / ghost-edge** phenomenon.

## Phase graph

For every independent (non-block) triple `tau`, define

- `P` if `<tau> ~= S_7`,
- `H` if `<tau> ~= S_9`,
- `D` otherwise.

Let `G_ind(S)` have independent triples as vertices, adjacent when they share exactly two points.

`N=|V(G_ind)|=C(v,3)-v(v-1)/6=v(v-1)(v-3)/6`.

`d_G=3(v-4)`.

### Spectral expansion — rigorous

`G_ind(S)` is the induced principal subgraph of `J(v,3)` obtained by deleting the STS blocks. The Johnson adjacency eigenvalues are

`3(v-3), 2v-9, v-7, -3`.

Cauchy interlacing gives

`lambda_2(G_ind)<=2v-9`.

Because `G_ind` is `3(v-4)`-regular,

`mu_2(G_ind)>=3(v-4)-(2v-9)=v-3`.

Therefore for every `A subset V(G_ind)`,

`e_G(A,A^c) >= (v-3)|A|(1-|A|/N)`.

For `|A|<=N/2`,

`e_G(A,A^c) >= ((v-3)/2)|A|`.

## Quantitative phase isoperimetry — rigorous

Write

`V=P sqcup H sqcup D`,

`s=e_G(P,H)`,

`q=min{|P|,|H|}`.

Then

`(v-3)q(1-q/N) <= s+3(v-4)|D|`.       (PI)

In particular,

`((v-3)/2) min{|P|,|H|} <= s+3(v-4)|D|`.  (PI-coarse)

With

`rho_P=|P|/N`, `rho_H=|H|/N`, `rho_D=|D|/N`,

`sigma=s/[3(v-4)N]`,

we get

`min(rho_P,rho_H) <= [6(v-4)/(v-3)](sigma+rho_D)`.

Define the phase-coherence energy

`E(S)=s+3(v-4)|D|`.

## Rooted anti-mitre charging — CLOSED

The constructive proof of the classical local lemma (Král–Máčajová–Pór–Sereni) starts from an independent root triple

`tau={A,B,C}`

and puts

`a=B⊕C`, `b=A⊕C`, `c=A⊕B`.

If the root does not close to `S_7` or `S_9`, one of the completion identities used in the proof fails. Auditing both principal branches and the second-level completion shows that the exposed anti-mitre witness can always be chosen to contain **all three root points A,B,C**. The symmetric branches have the same property.

Therefore charge each `D`-root to one such copy of `C_A` containing the root. Every `D`-root receives a witness, whereas a fixed eight-point `C_A` contains at most

`C(8,3)=56`

three-point subsets. Hence

`|D| <= 56 c_A`.                                      (BD)

Since

`c_A = 12P(v) alpha`

and

`N = 4P(v)`,

we have

`c_A/N = 3 alpha`,

so

`rho_D <= 168 alpha`.                                 (BD-density)

This closes the bulk-defect half of the desired stability theorem with an explicit absolute constant. The constant 56 is intentionally crude; it counts all triples inside the eight-point witness, not only admissible roots.

## Source audit: published proof versus technical report

### Published Král–Máčajová–Pór–Sereni paper (Canadian J. Math. 62 (2010))

The published proof establishes:

1. `C_A`-free implies every independent triple generates `S_7` or `S_9`;
2. Teirlinck's theorem then implies all independent triples have one type;
3. hence a `C_A`-free STS is projective or Hall.

### Earlier technical report

An earlier official technical report by the same authors gives a longer finite local proof of the purity step, based on an `S_7` subsystem `F`, an external point, and a red/blue (`S_7/S_9`) analysis of the Fano lines. This finite proof is useful for quantitative charging but must not be cited as a standalone published “15-point phase-switch lemma”.

Safe classical consequence: a local pure-phase mixture around `(F,D_ext)` cannot persist without producing a local defect/anti-mitre witness after finitely many Steiner completions.

## Remaining proof obligation: phase-interface charging

Only the interface term remains.

Need an explicit bound

`s=e_G(P,H) <= C_I v c_A`,

or, equivalently using (BD), it would suffice to prove

`s <= C'_I v |D|`.

A `P-H` edge determines

1. the Fano subsystem `F` generated by its P endpoint;
2. one external point supplied by its H endpoint;
3. a bounded finite completion template from the old local purity proof.

For a fixed `(F,D_ext)`, only constantly many `P-H` edges can occur. The remaining task is the reverse-fiber bound: for a fixed local `D` or `C_A` witness, count the number of `(F,D_ext)` pairs that can charge to it.

The expected `O(v)` scale is natural because a fixed STS block can lie in only `O(v)` Fano subsystems: after fixing the block, choosing one point outside it determines the generated Fano candidate, and each actual Fano subsystem is counted by its four points outside the block.

This argument must still be matched branch-by-branch to the finite purity proof before the interface theorem is declared proved.

## Candidate final theorem after interface closure

Combining

- phase isoperimetry (PI),
- `|D|<=56c_A`,
- `s<=C_I v c_A`,

would yield a quantitative Hall/projective stability inequality

`min(rho_P,rho_H) <= C alpha`

with an absolute constant `C` (after translating `c_A=3N alpha`).

Exact `alpha=0` recovers the classical Hall/projective dichotomy.

## Nearby literature / novelty boundary

Known ingredients:

- five-line counting formulas;
- projective/Hall characterization by forbidden configurations;
- local `S_7/S_9` generation in the `C_A`-free case;
- old finite local purity proof;
- Johnson graph spectrum / interlacing.

Candidate new layer:

- independent-triple phase graph;
- explicit spectral phase-isoperimetric inequality;
- phase-coherence energy;
- rooted quantitative bound `|D|<=56c_A`;
- quantitative interface charging and consequent anti-mitre stability, if the last bound closes.

Priority search has not yet found an equivalent quantitative phase-graph theorem; this remains provisional until final audit.

## Publication gate

Do **not** publish yet.

Publication threshold is crossed after:

1. branch-by-branch finite-template audit of phase-interface charging;
2. proof (or principled failure) of the `O(v)` interface fiber bound;
3. final priority search;
4. correction of the residual/#7 versus anti-mitre `C_A` nomenclature throughout RU/EN v0.6;
5. theorem numbering, complete proofs, bibliography/DOI audit, RU/EN synchronization.

If the interface bound closes, immediately move from research seed to publication manuscript and prepare Zenodo-ready RU/EN versions without an intermediate research-seed PDF.
