# HATTER-SOL-07 — hostile literature audit

**Branch:** `research/hatter-sol-free-ports`  
**Audit date:** 2026-09-12  
**Scope:** free-port / capacity factor networks, maximum simple b-matching, degree-bounded subgraphs, vertex detachment/splitting, arithmetic-to-tree encodings.

## Audit question

The candidate theorem package introduces a multiplicative refinement operation

\[
ab\longmapsto a,b
\]

on a complete-host simple capacity network and studies the change in minimum unused capacity

\[
\lambda(\mathbf c)=\min_G\sum_i(c_i-\deg_G v_i).
\]

The central candidate result is the sharp ambient inversion formula

\[
\sup_{\text{ambient decompositions}}
\left[\lambda(\ldots,a,b,\ldots)-\lambda(\ldots,ab,\ldots)\right]
=ab-a-b.
\]

The audit asks whether this is already a standard theorem under another name.

---

## 1. Maximum simple b-matching / f-bounded subgraphs — DIRECT CLASSICAL BACKBONE

The free-port minimization problem for a **fixed capacity vector** is exactly a maximum-cardinality simple b-matching problem on a complete host graph. If

\[
M(\mathbf c)=\max\{|E(H)|:\ H\subseteq K_k,\ \deg_H(v_i)\le c_i\},
\]

then

\[
\lambda(\mathbf c)=\sum_i c_i-2M(\mathbf c).
\]

This is classical territory and must not be claimed as new.

Relevant standard sources:

- Korte and Vygen, *Combinatorial Optimization*, chapter on b-matchings: a simple b-matching is an edge subset satisfying vertex degree upper bounds; maximum-weight / maximum-cardinality b-matching is classical.
- Schrijver, *Combinatorial Optimization*, chapters on b-matchings and f-factors.
- The generalized Tutte–Berge / f-bounded-subgraph formula expresses the maximum size of an f-bounded subgraph via a deficiency maximization. A modern proof appears in Qu (2026), “Another Proof of the Generalized Tutte—Berge Formula for f-Bounded Subgraphs,” *Journal of Graph Theory*, DOI `10.1002/jgt.70019`.

### Consequence for HATTER-SOL-07

The quantity `lambda` is best described as a **free-port interpretation of classical b-matching deficiency**. The fixed-vector optimization is not the novelty claim.

---

## 2. Sensitivity under changing one vertex capacity — CLOSE PRIOR ART

Guillaume Ducoffe and Alexandru Popa study how maximum b-matching cardinality changes when the capacity of one fixed vertex varies.

References:

- G. Ducoffe, A. Popa, “The b-Matching Problem in Distance-Hereditary Graphs and Beyond,” ISAAC 2018, LIPIcs 123, paper 30, DOI `10.4230/LIPIcs.ISAAC.2018.30`.
- Journal version: *Discrete Applied Mathematics* 305 (2021), 233–246, DOI `10.1016/j.dam.2021.09.012`.

Their auxiliary function `mu(t)` is the maximum b-matching cardinality after assigning capacity `t` to one selected vertex. In particular they prove the elementary sensitivity bound

\[
\mu(t+1)-\mu(t)\le1
\]

and develop a stronger piecewise-linear description used in their algorithmic decomposition.

### Consequence for HATTER-SOL-07

A claim such as “changing a vertex capacity by one changes the maximum matching size by at most one” is classical/known and cannot be presented as new.

Our operation is different: it simultaneously

1. replaces **one vertex by two vertices**;
2. changes total capacity from `ab` to `a+b`;
3. enlarges the complete host from `K_k` to `K_{k+1}`;
4. imposes the arithmetic relation that the old capacity is the **product** of the two new capacities.

The sharp formula `ab-a-b` concerns this combined operation, not ordinary one-vertex capacity perturbation.

---

## 3. Vertex detachment / vertex splitting — CLOSE BUT DIFFERENT TRANSFORMATION

There is a substantial classical detachment literature.

Key references:

- C. St. J. A. Nash-Williams, “Connected Detachments of Graphs and Generalized Euler Trails,” *Journal of the London Mathematical Society* 31 (1985), 17–29, DOI `10.1112/jlms/s2-31.1.17`.
- C. St. J. A. Nash-Williams, “Amalgamations of Almost Regular Edge-Colourings of Simple Graphs,” *Journal of Combinatorial Theory, Series B* 43 (1987), 322–342, DOI `10.1016/0095-8956(87)90008-6`.
- B. Fleiner, “Detachment of Vertices of Graphs Preserving Edge-Connectivity,” *SIAM Journal on Discrete Mathematics* 18, 581–591, DOI `10.1137/S0895480198341511`.
- B. Jackson and T. Jordán, “Non-separable detachments of graphs,” *Journal of Combinatorial Theory, Series B* 87 (2003), 17–37, DOI `10.1016/S0095-8956(02)00026-6`.
- A. R. Berg, B. Jackson, T. Jordán, “Highly edge-connected detachments of graphs and digraphs,” *Journal of Graph Theory* 43 (2003), 67–77, DOI `10.1002/jgt.10104`.

Classical detachment starts with an actual graph and redistributes the **existing incident edges** of a vertex among its pieces, often with prescribed degrees and connectivity constraints.

### Difference from the HATTER-SOL-07 operation

Our multiplicative split is not an edge-preserving detachment. We re-optimize from scratch in a complete host after replacing capacity `ab` by capacities `a,b`. Thus old incident edges are not conserved, and new adjacencies are allowed. The objective is maximum saturation / minimum unused capacity, not preservation of edge connectivity.

Therefore detachment theory is essential background, but the exact candidate theorem is not an immediate restatement of the standard detachment existence theorems found in this audit.

---

## 4. Vertex splitting as a reduction for matching — RELATED LANGUAGE

Vertex splitting is routinely used to reduce generalized matching problems to ordinary matching and in algorithmic graph transformations.

For example, standard b-matching reductions replace a capacity-`b(v)` vertex by several capacity-one copies in an expanded graph. Modern b-matching papers explicitly discuss such reductions.

This reinforces the need to avoid novelty claims for “capacity as multiple matching slots” or “splitting a capacity vertex.”

The research claim, if retained, must be about the **sharp free-boundary response to the multiplicatively constrained split**.

---

## 5. Matula–Göbel numbers — NUMBER/GRAPH CORRESPONDENCE PRIOR ART

There is classical work encoding natural numbers by rooted trees through prime factorization:

- D. W. Matula, “A Natural Rooted Tree Enumeration by Prime Factorization,” *SIAM Review* 10 (1968), 273.
- F. Göbel, “On a 1-1-correspondence between rooted trees and natural numbers,” *Journal of Combinatorial Theory, Series B* 29 (1980), 141–143.
- E. Deutsch, “Rooted tree statistics from Matula numbers,” *Discrete Applied Mathematics* 160 (2012), 2314–2322, DOI `10.1016/j.dam.2012.05.012`.

### Consequence

HATTER-SOL-07 must not claim novelty for the broad idea “factorization gives a graph/tree representation of an integer.”

The present model differs because factor values are interpreted directly as **vertex degree capacities**, and factorization refinement is studied as a transformation of a capacity vector with a free-boundary objective.

---

## 6. Audit of the candidate sharp theorem

Searches were performed around the following combinations:

- `b-matching sensitivity vertex capacity split`;
- `maximum b-matching capacity perturbation`;
- `vertex split b-matching capacity`;
- `degree constrained subgraph vertex splitting`;
- `graph detachment prescribed degrees`;
- `complete graph simple b-matching capacities`.

The audit located:

1. general maximum b-matching / f-bounded-subgraph theory;
2. one-vertex capacity sensitivity results;
3. extensive edge-preserving detachment theorems;
4. matching reductions using vertex copies;
5. number-to-tree encodings via prime factorization.

It did **not** locate an explicit theorem equivalent to

\[
\sup_{\text{ambient decompositions}}
[\lambda(\ldots,a,b,\ldots)-\lambda(\ldots,ab,\ldots)]
=ab-a-b
\]

for the complete-host, simple-graph, multiplicative-refinement operation used here.

This is a **serious negative search, not an absolute priority guarantee**.

---

## 7. Novelty discipline for a publication

A publication must separate three layers.

### Classical layer

- simple b-matching / f-bounded subgraph;
- generalized Tutte–Berge deficiency;
- handshake and degree-sum identities;
- graphical degree sequence criteria;
- vertex detachment and vertex splitting;
- Matula–Göbel number/tree encodings.

### Model-definition layer

Potentially original as a synthesis, but not by itself a theorem:

- factor `m` interpreted as a degree-capacity-`m` node;
- free boundary interpreted as unused capacity;
- multiplicative refinement `ab -> a,b` as an operation on the capacity vector.

### Candidate theorem layer

The main candidate contribution is the exact worst-case response of classical b-matching deficiency to the multiplicatively constrained vertex split:

\[
\boxed{
\Delta_{a,b}^{\max}=ab-a-b.
}
\]

Accompanying results:

- refinement inversion can be arbitrarily large;
- `4 -> 2*2` is the unique split with zero worst-case inversion among `a,b>=2`;
- explicit sharpness constructions;
- iterated bound

\[
\lambda(\mathbf d)-\lambda(\mathbf c)
\le S(\mathbf c)-S(\mathbf d),
\qquad S(\mathbf c)=\sum_i c_i.
\]

The last monotonicity should be presented as a corollary of the sharp one-step theorem, not as an independent classical invariant claim.

---

## 8. Publication recommendation

**Recommendation: publication threshold reached for a short HATTER-SOL research note, subject to conservative priority language.**

Reason:

1. the model has been reduced to standard b-matching language, so the classical content is now cleanly identified;
2. the main nontrivial statement is exact and sharp, not only experimental;
3. there is an infinite family and a universal sharp bound rather than a single counterexample;
4. the closest literatures located do not state the same multiplicatively constrained split theorem;
5. the Wonderland/“Размышлизмы” presentation can motivate the model while the mathematical section can be fully conventional.

The article must **not** claim invention of b-matching deficiency, graph detachment, number-to-tree arithmetic, or general vertex-capacity sensitivity.

Recommended publication framing:

> We introduce a factor-capacity network viewpoint on multiplicative decompositions and isolate a sharp sensitivity law for the minimum unused capacity under the arithmetic split `ab -> (a,b)`. The optimization for each fixed capacity vector is classical maximum simple b-matching; the contribution is the exact interaction between this deficiency and multiplicative refinement.
