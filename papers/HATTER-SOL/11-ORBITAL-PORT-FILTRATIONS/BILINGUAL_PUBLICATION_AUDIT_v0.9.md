# HATTER-SOL-11 · Bilingual Publication Audit v0.9

**Date:** 2026-09-14  
**EN source:** `HATTER_SOL_11_EN_v0.9.md`  
**RU source:** assembly defined by `HATTER_SOL_11_RU_v0.9_INDEX.md`  
**Status:** PASS with no mathematical divergence found between language versions.

## 1. Theorem-set parity

The EN and RU candidates contain the same publication spine:

1. orbit-fusion classification with unique fusion worlds `Delta=-4,-3`;
2. no universal sequential strongest-first activation law;
3. median geodesic theorem;
4. geodesic folding theorem;
5. exact generic-odd forgetting-fiber classification;
6. operational visibility on the two-node host;
7. exact strict-1D response and permanent three-state memory;
8. exact outerplanar pure-channel and channel-floor laws;
9. unique outerplanar mixed rank-swap collision `(2,1)`;
10. no outerplanar mixed/pure collision;
11. regular-factorizable exact Pareto interval theorem for `A+O>=d`;
12. degree-controlled orbital-memory filtration;
13. sufficient connected-factor criterion for the underfull regime;
14. exact planar lift at the tetrahedral, octahedral, and icosahedral orders;
15. exact planar `3->2->1` trajectory for `(4,1)` on orders `4->6->12`.

No theorem appears in only one language version.

## 2. Central formula parity

Both versions state

\[
\boxed{3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.}
\]

with identical hypotheses:

- `P>Q>0`;
- `S=P+Q`;
- connected even-order `d`-regular host;
- fixed 1-factorization;
- `d<=S`.

## 3. Type-III witness audit

Both versions use

\[
\alpha_{III}=Q-(P+Q)F
\]

and the corrected median-geodesic triple

\[
\boxed{(0,-P,Q).}
\]

The derived data agree:

\[
\Omega_{III}=(0;\{P,Q\}),
\qquad
\Xi_{III}=(0,P+Q).
\]

The former patch-set sign typo `(0,-P,-Q)` is not present in either v0.9 candidate.

## 4. Fixed-host versus geometry-class scope

Both candidates distinguish:

\[
Z_H^{\Xi}
\]

for a fixed host from

\[
Z_{\mathcal C,n}^{\Xi}
\]

for a geometry class.

The planar lift is justified only after the independent fact that the tetrahedron, octahedron, and icosahedron attain the global planar edge ceiling at their orders. Neither candidate claims that arbitrary planar 1-factorizable hosts automatically determine the full planar-class response.

## 5. Connectedness audit

Both candidates state that HATTER connectedness applies to the union of channel edge sets. In the low-`Q` outerplanar proof, the channel sets partition the full connected host `H_n`; no separate connectedness of each color/channel subgraph is required.

For Theorem 8.2 the lower Pareto line is realized by using every edge of the full connected host `H`, so connectedness is automatic.

## 6. Underfull boundary audit

Both candidates retain the hypothesis

\[
\boxed{A+O\ge d}
\]

inside the regular-factorizable universality theorem.

Both explicitly reject the false extrapolation that 1-factorizability alone forces zero boundary when `A+O<d`. Both give only the sufficient connected-union criterion in that regime.

## 7. Outerplanar boundary audit

Both language versions state:

\[
Z_{O,n}^{\Xi}(P,Q)=Z_{O,n}^{\Xi}(Q,P)
\iff
(P,Q)=(2,1)
\]

for `P>Q>0`, and both state the complete class count

\[
\nu_{O,n}^{\Xi}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}.
\end{cases}
\]

No mixed/pure collision is claimed.

## 8. Planar trajectory audit

Both candidates state exactly

\[
\nu_{Pl,4}^{\Xi}(4,1)=3,
\qquad
\nu_{Pl,6}^{\Xi}(4,1)=2,
\qquad
\nu_{Pl,12}^{\Xi}(4,1)=1.
\]

Both explicitly say this is a three-scale witness and not monotonicity through every intermediate order.

## 9. Bibliography and metadata audit

Verified series metadata included in both candidates:

- HATTER-SOL-07 DOI `10.5281/zenodo.22724185`;
- HATTER-SOL-10 DOI `10.5281/zenodo.22734865`.

Both candidates deliberately avoid inventing metadata:

- HATTER-SOL-08 remains `v1.0`, with Zenodo DOI marked pending in the repository record as of 2026-09-14;
- HATTER-SOL-09 remains `v0.9 preprint candidate`, with no verified Zenodo DOI recorded.

The eight external graph-theory references and DOI values match across languages.

## 10. Deferred-result audit

Both candidates exclude from the dependency graph:

- universal order-46 Gaussian `(6,5)` planar closure;
- prime-61 tomography and spectral work;
- residue-tail collision work;
- torus observability;
- future genus/surface classifications;
- full network semantics retaining every component of `Omega=(a;{b,c})`.

## 11. Publication verdict

**Mathematical consistency:** PASS.  
**EN/RU claim-set parity:** PASS.  
**Scope discipline:** PASS.  
**Numbering discipline:** PASS.  
**Known DOI discipline:** PASS.  
**Open-side-problem isolation:** PASS.

### Remaining pre-deposit work

No new theorem is required for HATTER-SOL-11 v0.9.

The remaining tasks are artifact-level:

1. typeset EN and RU publication PDFs;
2. visual QA of formulas, page breaks, and references;
3. prepare Zenodo metadata and source package;
4. compute final checksums;
5. only after PDF QA, promote v0.9 to frozen v1.0/deposit candidate.
