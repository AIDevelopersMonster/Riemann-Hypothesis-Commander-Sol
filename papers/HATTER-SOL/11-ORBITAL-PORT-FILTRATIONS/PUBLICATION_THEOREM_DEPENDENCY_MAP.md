# HATTER-SOL-11 · Publication Theorem Dependency Map

**Status:** publication-control document.  
**Purpose:** freeze the logical spine of the paper before manuscript numbering.

This file is not a source of new mathematical claims. It records which proved layers depend on which earlier layers, what belongs in the main theorem spine, and what should remain secondary or deferred.

---

## A. Central publication spine

### A1. Intrinsic direction-orbit classification

**Primary source:** `ODD_GEODESIC_ORBIT_CLASSIFICATION.md`, `ORBIT_FUSION_CLASSIFICATION.md`.

Outputs:

- generic imaginary-quadratic worlds carry a canonical axial/oblique orbit structure;
- Gaussian and Eisenstein are orbit-fusion exceptions;
- universal strongest-first activation is false.

Dependencies:

- arithmetic/geodesic setup inherited from HATTER-SOL-09/10;
- no network theorem required.

Feeds into:

- A2 exact forgetting fibers;
- A3 orbit-total network semantics.

### A2. Exact forgetting-map fiber classification

**Primary source:** `FORGETTING_MAP_FIBER_CLASSIFICATION.md`.

For generic odd worlds and `P>Q>0`, the folded pair has exactly three canonical orbital members

\[
(P;\{Q,0\}),\quad(Q;\{P,0\}),\quad(0;\{P,Q\}).
\]

Dependencies:

- A1 direction-orbit classification;
- geodesic fact that shortest usage has at most two nonzero direction counts.

Feeds into:

- A3 canonical orbit-total projection;
- every geometry-dependent memory theorem.

### A3. Canonical orbit-total projection and operational separation

**Primary source:** `ORBITAL_NETWORK_FIBER_SEPARATION.md`.

Projection:

\[
\Omega=(a;\{b,c\})\longmapsto\Xi=(A,O)=(a,b+c).
\]

Interior fiber becomes

\[
\Xi_I=(P,Q),\quad\Xi_{II}=(Q,P),\quad\Xi_{III}=(0,P+Q).
\]

Key conclusion: members of one folded `(P,Q)` fiber can have different network responses.

Dependencies:

- A2.

Feeds into:

- A4 path theorem;
- A5 outerplanar theorem;
- A6 regular-factorizable host theorem;
- A7 planar examples.

### A4. Strict-1D permanent-memory theorem

**Primary source:** `GEOMETRY_ORBITAL_MEMORY_PATH_POLYNOMIAL.md`.

Output:

\[
Z_I^{1D},Z_{II}^{1D},Z_{III}^{1D}
\]

are pairwise distinct on every even path for every interior `P>Q>0`.

Dependencies:

- A3;
- elementary path matching constraints.

Role in paper:

- first exact demonstration that geometry can protect information indefinitely.

### A5. Complete outerplanar `Xi` classification

**Primary sources:**

- `OUTERPLANAR_ORBITAL_MEMORY_21.md`;
- `OUTERPLANAR_HOSTILE_AUDIT.md`;
- `OUTERPLANAR_RANK_SWAP_NO_GO.md`;
- `OUTERPLANAR_RANK_SWAP_COMPLETE_CLASSIFICATION.md`;
- `OUTERPLANAR_FULL_INTERIOR_FIBER_CLASSIFICATION.md`.

Final output:

\[
\nu^{\Xi}_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}
\end{cases}
\]

for every even outerplanar host size `n>=4` in the exact geometry-class model.

Dependencies:

- A3;
- outerplanar extremal edge bounds and constructive hosts;
- hostile correction of earlier overstrong conjectures.

Role in paper:

- geometry-class theorem contrasting sharply with A4 and A6.

### A6. Regular-factorizable host universality and degree filtration

**Primary source:** `REGULAR_FACTORIZABLE_HOST_ORBITAL_MEMORY_THEOREM.md`.

Fixed-host hypotheses:

- connected;
- simple;
- even order `n`;
- `d`-regular;
- 1-factorizable;
- critical/overfull regime `A+O>=d`.

Exact response:

\[
B_A+B_O=n(A+O-d),
\]

\[
n(A-d)_+\le B_A\le n(A+O-d)-n(O-d)_+,
\]

with even parity.

For one interior fiber `P>Q>0`, `d<=P+Q`:

\[
\nu_H^{\Xi}(P,Q)=
\begin{cases}
3,&d<P,\\
2,&P\le d<P+Q,\\
1,&d=P+Q.
\end{cases}
\]

Dependencies:

- A3;
- exact degree-window construction from a 1-factorization.

Subsumes conceptually, but does not delete:

- critical/overfull part of `EVEN_COMPLETE_HOST_ORBITAL_FORGETTING.md`;
- the fixed-host mechanism behind `PLANAR_PLATONIC_THRESHOLD_THEOREM.md`.

Important scope boundary:

- this is a fixed-host theorem;
- geometry-class exactness needs an independent extremality argument;
- `A+O<d` needs a connected spanning factor hypothesis for automatic closure.

Role in paper:

- central title theorem: orbital information is filtered as accessible regular degree crosses `P` and `P+Q`.

### A7. Planar geometry witnesses and exact Platonic thresholds

**Primary sources:**

- `PLANAR_CRITICAL_CAPACITY_HOSTILE_PROBE.md`;
- `PLANAR_PLATONIC_THRESHOLD_THEOREM.md`.

Exact regular planar triangulation hosts:

\[
(n,d)=(4,3),(6,4),(12,5).
\]

Class-count law:

\[
\nu^{\Xi}_{Pl,n}(P,Q)=
\begin{cases}
1,&P+Q=d,\\
2,&P+Q>d\text{ and }P\le d,\\
3,&P+Q>d\text{ and }P>d.
\end{cases}
\]

Dependencies:

- A3;
- explicit 1-factorizations;
- planar edge extremality;
- A6 now supplies the common fixed-host mechanism.

Role in paper:

- geometry-class realization of A6;
- concrete host-scale trajectories, e.g. `(4,1): 3 -> 2 -> 1` along `4 -> 6 -> 12`.

---

## B. Supporting central results

### B1. Maximal-first no-go/control protocol

**Source:** `MAXIMAL_FIRST_GEOMETRY_PROBE.md`, plus complete-host comparison in `EVEN_COMPLETE_HOST_ORBITAL_FORGETTING.md`.

Purpose:

- prevent false interpretation of `P>=Q` as an activation order;
- demonstrate that a restricted search protocol can induce a different collision relation from the full Pareto model.

Main-text role:

- short methodological theorem/no-go section.

### B2. Complete-host calibration

**Source:** `EVEN_COMPLETE_HOST_ORBITAL_FORGETTING.md`.

Purpose:

- exact unrestricted benchmark;
- contains final closure for `c>=P+Q`, including underfull relative to complete-host degree, using complete-host structure beyond the minimal RFH theorem.

Main-text role:

- calibration/example after A6, not independent conceptual spine.

### B3. Large planar `(6,5)` programme

**Sources:** `PLANAR_65_*`, `ORDER_40_*`, `ORDER_42_*`, `ORDER_44_*`, `ORDER_46_*`, planar low-tail/capacity files.

Purpose:

- deep evidence that the planar problem beyond regular extremal hosts has genuine local repair structure;
- orders through 44 closed, order 46 partially closed.

Publication role:

- selected example or appendix;
- **not** a dependency of A1-A7;
- unresolved universal `n=46,r=17` closure must not be accidentally stated as proved.

---

## C. Secondary information-loss line

### C1. Principalization-tail valence and global sectors

Sources:

- `TAIL_VALENCE_NO_GO.md`;
- `DELTA_MINUS_35_BINARY_TAIL_LADDER.md`;
- `DELTA_MINUS_84_MIXED_TAIL_VALENCE.md`;
- `GLOBAL_BINARY_TAIL_COMPOSITION.md`.

Outputs:

- local binary tail structure;
- global affine subset-product residue sectors;
- explicit `9 -> 5` static folding loss.

### C2. Genuine network-induced residue collision

Sources:

- `GENUINE_NETWORK_COLLISION_17_SQUARED.md`;
- `BINARY_TAIL_COUNT_SUPPORT_THEOREM.md`.

Outputs:

- exact post-pair-flip network collision at `17^2`;
- general count-sector support law.

Publication role of C1-C2:

- appendix or one compact section showing information loss can occur at a second, arithmetic-residue layer;
- not needed to prove A6.

---

## D. Secondary world/geometry/tomography line

Sources:

- `WORLD_GEOMETRY_RESPONSE_CALCULUS.md`;
- `PRIME_61_WORLD_GEOMETRY_COUPLING.md`;
- `PRIME_61_GEOMETRY_SIGNAL_SPECTRUM_CORE.md`;
- `PROJECTION_LOSS_WORLD_SPECTRUM_THEOREM.md`;
- `TROPICAL_PARETO_TOMOGRAPHY_THEOREM.md`;
- `PRIME_61_WEIGHTED_GEOMETRY_TOMOGRAPHY.md`;
- `PRIME_61_TOMOGRAPHIC_DIMENSION_AND_SPECTRAL_BLINDNESS.md`;
- `TOMOGRAPHIC_RANK_THEOREM.md`.

Core outputs:

- typed world-geometry coupling can be nonzero while scalar projection is blind;
- exact projection-loss criterion;
- weighted tomography recovers lower convex envelope but not discrete support;
- finite-world tomographic dimension and blind complexes.

Publication role:

- optional final section or companion-paper seed;
- if included in HATTER-SOL-11, use only as consequence of the information-filtration viewpoint.

---

## E. Explicitly deferred

`TORUS_OBSERVABILITY_TRANSITION_SEED.md` is **not part of the HATTER-SOL-11 proof spine**.

It is retained only as a seed for later topology/genus/surfaces-of-revolution work.

No HATTER-SOL-11 theorem should depend on it.

---

## F. Dependency DAG in compressed form

\[
\boxed{
\text{H09/10 interface model}
\to
\text{A1 orbit classification}
\to
\text{A2 forgetting fibers}
\to
\text{A3 operational orbit-total model}
}
\]

then independently

\[
\boxed{
A3\to A4\ (1D),
\qquad
A3\to A5\ (outerplanar),
\qquad
A3\to A6\ (regular-factorizable),
\qquad
A6+\text{planar extremality}\to A7.
}
\]

B/C/D are supporting branches and are not prerequisites for the core publication theorem.

---

## G. Numbering policy for manuscript construction

Existing working labels `T11.xx`, `RFH.x`, `GS11.x`, etc. are branch-local research labels and are not publication numbering.

Before manuscript freeze:

1. assign one sequential theorem/lemma/proposition numbering system in the manuscript;
2. keep branch-local labels in an internal crosswalk only;
3. do not cite a branch-local theorem number in the final paper unless the crosswalk has been frozen;
4. ensure no theorem statement silently gains assumptions or scope while being consolidated.
