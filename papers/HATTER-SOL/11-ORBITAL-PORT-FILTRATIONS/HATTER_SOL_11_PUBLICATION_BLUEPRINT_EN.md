# HATTER-SOL-11 · Publication Blueprint (EN)

**Working title**  
**Orbital Port Filtrations: How Network Geometry Forgets Arithmetic Direction Data**

**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Series:** HATTER-SOL-11

**Status:** manuscript blueprint; theorem content already proved in branch unless explicitly marked optional/deferred.

---

## 0. One-sentence paper thesis

A folded arithmetic interface `(P,Q)` can hide a finite canonical fiber of inequivalent direction-orbit states, and exact network optimization shows that the visibility of those states is filtered by host geometry and accessible degree: one-dimensional hosts can retain all orbital information indefinitely, outerplanar hosts lose only an exceptional rank swap, while regular factorizable hosts exhibit a sharp `3 -> 2 -> 1` degree-controlled forgetting law.

This is the single narrative. Every section must support it.

---

## 1. Abstract — target content

The abstract should state only four contributions.

1. **Orbital refinement.** Replace the folded two-coordinate interface by a canonical direction-orbit datum in the generic imaginary-quadratic setting; classify Gaussian/Eisenstein fusion exceptions.
2. **Exact forgetting fibers.** For generic odd interior pairs `P>Q>0`, prove that the fold has exactly three canonical orbital preimages.
3. **Operational memory.** Show that these three states can have different exact network responses and classify how geometry retains or erases them.
4. **Degree filtration.** Prove the regular-factorizable-host theorem giving `3 -> 2 -> 1` response classes as host degree crosses `P` and `P+Q`.

The abstract should also contain one explicit limitation sentence:

> The results are exact for the canonical orbit-total response model `Xi`; no universal strongest-first activation law or complete planar classification is claimed.

Do **not** mention torus, tomography, residue sectors, or the order-46 Gaussian technical programme in the abstract.

---

## 2. Introduction

### 2.1 Starting point from HATTER-SOL-09/10

Recall only what is needed:

- HATTER-SOL-09 associates a folded typed interface `(P,Q)` to arithmetic factor data and optimizes typed network boundary;
- HATTER-SOL-10 shows that arithmetic witness choice can itself be multistate;
- both leave open whether `(P,Q)` has already forgotten intrinsic direction structure.

### 2.2 Central question

Present the diagram

\[
\boxed{
\Omega
\longrightarrow
\Xi
\longrightarrow
(P,Q)
\longrightarrow
Z_{\mathcal C,k}
}
\]

where

- `Omega` is intrinsic orbital data;
- `Xi=(A,O)` is the orbit-total network interface;
- `(P,Q)` is the published magnitude-sorted fold;
- `Z` is the exact Pareto response polynomial.

Ask:

> Which distinctions lost by the static fold remain observable after network optimization, and how does the answer depend on geometry and host scale?

### 2.3 Main-results preview

State a compact theorem preview:

- generic odd interior fold has three states;
- path: `3` forever;
- outerplanar: `3`, except `(2,1)` gives `2`;
- regular 1-factorizable fixed host: `3/2/1` according to degree;
- Platonic planar hosts realize the same degree thresholds as exact geometry-class results.

### 2.4 No-go before construction

Explicitly say the paper first attacks the tempting hierarchy `P is stronger than Q` and rejects it. This is important conceptually: the filtration later proved is an **operational response filtration**, not a sequential activation law.

---

## 3. Arithmetic direction orbits

### 3.1 Lattice/direction setup

Define the shortest-direction decomposition in the generic imaginary-quadratic lattice used by the branch.

### 3.2 Natural symmetry action

Define unit/conjugation action on primitive directions.

### 3.3 Orbit classification

Publication Theorem 1 (assembled from branch orbital-classification results):

- generic worlds have axial and oblique direction orbits;
- Gaussian and Eisenstein are the exact fusion exceptions.

### 3.4 No universal strongest-first law

Publication Proposition/No-Go 2:

There exist admissible elements/witnesses whose shortest geodesic usage lies entirely in the nominally outer shell while inner-shell usage is zero; therefore no universal arithmetic activation law can be inferred from magnitude order.

End section with:

\[
\boxed{
\text{orbit structure is canonical; orbit priority is not.}
}
\]

---

## 4. The forgetting map

### 4.1 Orbital datum

Use one notation consistently:

\[
\boxed{
\Omega=(a;\{b,c\})
}
\]

with axial coordinate `a` and unordered oblique pair `{b,c}`.

### 4.2 Orbit-total quotient

Define

\[
\boxed{
\Xi(\Omega)=(A,O):=(a,b+c).
}
\]

Explain: `Xi` is the canonical network model studied in the exact geometry theorems; it is finer than folded `(P,Q)` but coarser than full `Omega`.

### 4.3 Folded magnitude pair

Define the existing HATTER fold

\[
F(\Omega)=(P,Q),
\qquad P\ge Q\ge0.
\]

### 4.4 Exact fiber theorem

Publication Theorem 3:

For generic odd worlds the fiber cardinalities are

\[
1,2,2,3
\]

for zero, axis/boundary, diagonal, and strict interior folded states respectively.

For

\[
P>Q>0,
\]

the three canonical members are

\[
\boxed{
\Omega_I=(P;\{Q,0\}),
\quad
\Omega_{II}=(Q;\{P,0\}),
\quad
\Omega_{III}=(0;\{P,Q\}).
}
\]

Their `Xi` images are

\[
\boxed{
(P,Q),\quad(Q,P),\quad(0,P+Q).
}
\]

This theorem is the static information-loss layer on which the rest of the paper operates.

---

## 5. Exact network response and operational separation

### 5.1 Connected typed simple-support model

Freeze definitions:

- connected spanning network;
- one edge total per unordered vertex pair/support edge;
- each used edge is axial or oblique;
- degree constraints from `(A,O)`;
- boundary
  \[
  B_A=nA-2e_A,
  \qquad
  B_O=nO-2e_O;
  \]
- Pareto front `R`;
- response polynomial
  \[
  Z(X,Y)=\sum_{(B_A,B_O)\in R}X^{B_A}Y^{B_O}.
  \]

### 5.2 First operational separation theorem

Publication Theorem 4:

Give the smallest/cleanest branch example showing that two or three states in one folded `(P,Q)` fiber yield different `Xi` response polynomials.

Purpose:

\[
\boxed{
\text{the fold forgets data that the network can still see.}
}
\]

Avoid spending pages on all early examples; use one decisive exact example and move technical variants to appendix.

---

## 6. Geometry as a memory filter

This section should be the conceptual center before the general degree theorem.

### 6.1 Strict one dimension

Publication Theorem 5 — exact path polynomial.

For even path `P_{2m}`, state the exact feasible axial-edge interval and response polynomial.

Then Publication Corollary 6:

For every interior fiber `P>Q>0`, all three states remain pairwise distinct for every even path size.

Display:

\[
\boxed{
1D:\qquad 3\to3\to3\to\cdots
}
\]

### 6.2 Outerplanar class

Do not reproduce the entire hostile-search history in main text.

State one preparatory extremal lemma and then Publication Theorem 7:

\[
\boxed{
\nu^{\Xi}_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise},
\end{cases}
}
\]

for even `n>=4`.

Emphasize:

- pure-oblique state never collides with a mixed state;
- outerplanar geometry nearly preserves the full three-state fiber.

### 6.3 Contrast with unrestricted complete hosts

Briefly state the known exact complete-host filtration as calibration:

\[
3\to2\to1.
\]

Do not yet present it as the final theorem; Section 7 explains why this pattern is structural.

---

## 7. Regular-factorizable hosts: the main filtration theorem

This should be the principal new theorem section.

### 7.1 Host hypotheses

Let `H` be:

- connected;
- simple;
- even order `n`;
- `d`-regular;
- 1-factorizable.

### 7.2 Degree-window lemma

Publication Lemma 8:

For every

\[
0\le l\le u\le d
\]

and

\[
\frac{nl}{2}\le e\le\frac{nu}{2},
\]

construct a spanning subgraph with exactly `e` edges and all degrees in `[l,u]` using full perfect matchings plus a partial next matching.

### 7.3 Exact fixed-host Pareto theorem

Publication Theorem 9:

For `S=A+O>=d`, define

\[
D=n(S-d),
\quad
L_A=n(A-d)_+,
\quad
L_O=n(O-d)_+.
\]

Then

\[
\boxed{
R_H^{\Xi}(A,O)
=
\{(b,D-b):L_A\le b\le D-L_O,\ b\equiv0\pmod2\}.
}
\]

Key proof sentence to preserve:

> the channel subgraph constructed from factors need not be connected because the two channel subgraphs together use the full connected host `H`.

### 7.4 Orbital-port filtration theorem

Publication Theorem 10 (title theorem):

For an interior fiber `P>Q>0`, `S=P+Q`, and `d<=S`,

\[
\boxed{
\nu_H^{\Xi}(P,Q)=
\begin{cases}
3,&d<P,\\
2,&P\le d<S,\\
1,&d=S.
\end{cases}}
\]

Interpretation:

- `d<P`: host cannot hide placement of the large orbital component;
- `P<=d<S`: rank swap becomes invisible, pure-oblique placement remains visible;
- `d=S`: full closure erases the remaining distinction.

Use the phrase:

\[
\boxed{
\text{degree-controlled orbital memory filtration}
}
\]

not “activation hierarchy”.

### 7.5 Underfull hostile boundary

State a proposition, not a theorem of equivalence:

If `S<d` and a connected spanning union of `S` host factors exists, then zero-boundary closure follows.

Explicitly say 1-factorizability alone is insufficient because selected factors may have disconnected union.

---

## 8. Planar realization of the degree filtration

### 8.1 Platonic even regular triangulations

Derive via Euler:

\[
(n,d)=(4,3),(6,4),(12,5).
\]

Give/reference explicit factorization constructions.

### 8.2 Exact planar class theorem at these orders

Because these hosts attain the planar edge ceiling, Theorem 9 lifts from fixed host to exact planar geometry-class response.

State Publication Corollary 11:

\[
\nu^{\Xi}_{Pl,n}(P,Q)=
\begin{cases}
1,&P+Q=d,\\
2,&P+Q>d,\ P\le d,\\
3,&P+Q>d,\ P>d.
\end{cases}
\]

### 8.3 Host-scale examples

Use a small table, not many separate theorems.

Key row:

\[
(P,Q)=(4,1):\qquad3\to2\to1
\]

for planar orders `4 -> 6 -> 12`.

Also show one nonmonolithic same-total-capacity comparison, e.g. at `S=6`:

- `(5,1)` and `(4,2)` do not have identical memory trajectories at all scales.

This demonstrates dependence on the fiber, not only on total capacity.

### 8.4 Beyond Platonic hosts

One concise paragraph:

- larger planar orders require local repair/balancing arguments;
- the branch closes many `(6,5)` cases through order 44;
- order-46 universal closure remains open;
- these results support the programme but are not needed for the title theorem.

Move detailed repair lemmas to Appendix C or a companion technical note.

---

## 9. Observation protocol and information loss

Keep this section compact.

### 9.1 Maximal-first is not the law

State exact example where full response collision classes and maximal-first collision classes differ.

Conclusion:

\[
\boxed{
\text{what a probe forgets need not equal what the full model forgets.}
}
\]

### 9.2 Optional short tomography corollary

Only if manuscript length remains reasonable:

Mention that weighted scalarizations form a further forgetting layer and can hide distinctions visible in the Pareto polynomial.

Do not develop the full `61` spectral programme here unless needed for a stronger conclusion. Preferred placement: Appendix D or separate follow-up.

---

## 10. Arithmetic residue information as a second forgetting layer — optional appendix/main-text box

Recommended minimal inclusion:

- state that HATTER-SOL-10 witness/residue sectors provide another source of hidden arithmetic data;
- give the clean `Delta=-1155` `9 -> 5` fold example;
- give one genuine network-induced collision result if space permits.

Purpose:

show that the orbital phenomenon is part of a more general hierarchy

\[
\text{arithmetic state}
\to
\text{interface state}
\to
\text{network response}
\to
\text{coarse observable}.
\]

Do not let residue theory become a second paper inside this one.

---

## 11. Discussion

### 11.1 What is genuinely learned

The important point is not merely that a richer label contains more information.

The exact theorems identify **when network architecture itself preserves or erases that information**.

The paper should distinguish:

- static forgetting under `Omega -> Xi -> (P,Q)`;
- operational forgetting under network optimization;
- observational forgetting under restricted probes/scalarization.

### 11.2 Geometry versus degree

Explain:

- low-dimensional geometry can protect memory by limiting accessible incidence;
- on regular factorizable hosts, degree alone controls the exact critical/overfull `Xi` response;
- topology may re-enter outside these hypotheses, especially in the underfull connected-factor problem.

### 11.3 What is not proved

Explicit list:

- no universal strongest-first activation;
- no complete planar classification;
- no complete richer-`Omega` network semantics classification;
- no genus/topology theorem;
- no claim that all regular hosts are response-equivalent;
- no claim that scalar tomography reconstructs discrete Pareto support.

---

## 12. Conclusion

End with the shortest possible structural summary:

\[
\boxed{
\Omega
\to
\Xi
\to
(P,Q)
}
\]

is an information filtration, and network geometry supplies a second filtration on the visibility of its fibers.

The regular-factorizable theorem gives the cleanest exact law:

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
}
\]

Strict 1D and outerplanar geometry show that this forgetting is not inevitable: architectural constraints can preserve arithmetic direction information that denser hosts erase.

---

## Appendices — recommended

### Appendix A. Notation crosswalk

Branch labels `Omega`, `Xi`, `(P,Q)`, boundary, response polynomial.

### Appendix B. Outerplanar constructions and hostile corrections

Move most detailed outerplanar search/proofs here while keeping final theorem in main text.

### Appendix C. Larger planar Gaussian balancing programme

Summarize exact orders 40/42/44 and the open order-46 boundary. Include only if manuscript size permits; otherwise cite branch supplement/repository.

### Appendix D. Projection loss and tomography

Optional:

- linear projection-Laplacian commutation;
- tropical Pareto tomography;
- `61` laboratory.

### Appendix E. Residue-tail information loss

Optional compressed version of the principalization-residue side line.

---

## Manuscript length target

Main paper target: approximately 22--30 pages before optional appendices.

Main-text theorem count target: about 10--12 substantial statements, not the dozens of branch-local lemmas.

The manuscript should read as one theorem chain, not a chronological laboratory notebook.

---

## Publication-readiness decision

The content is mathematically above the threshold for manuscript construction.

The next step is **not** another exploratory theorem. It is to write the EN manuscript against this blueprint, while running a line-by-line assumption and literature audit in parallel.
