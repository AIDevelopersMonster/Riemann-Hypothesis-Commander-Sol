# FCOA QGE3 — Literature Notes and Novelty Boundary

**Branch:** `director/fcoa-rigidity-cost`  
**Purpose:** literature firewall for sparse anonymous `q>=3` phase transport

This file records structural comparisons only. It does not claim priority for classical graph-coloring, switching, gain-graph, coherent-configuration, or permutation-group concepts.

---

## 1. Uniquely colorable graphs

A classical graph is uniquely colorable when its vertex partition into the minimum number of color classes is unique up to permutation of the classes.

A standard early reference is:

- F. Harary, S. T. Hedetniemi, R. W. Robinson, **Uniquely colorable graphs**, *Journal of Combinatorial Theory* 6(3) (1969), 264–270. DOI: `10.1016/S0021-9800(69)80086-4`.

The paper develops structural properties of uniquely colorable graphs, including connectivity of the subgraph induced by any two color classes.

### Relevance to QGE3

The QGE3 T-constraint quotient `H_T(C)` turns a ternary anonymous-equality component into an ordinary proper-coloring problem. If the quotient is uniquely colorable with the number of colors actually used by the component, then every quotient automorphism transports the color partition only by a permutation of the classes. This supplies the sufficient hypothesis in `NONABELIAN_PHASE_LAW.md`.

### Boundary

Unique colorability itself is classical. The QGE3 contribution is the reduction from the sparse anonymous-operation ternary reduct to the proper-coloring quotient and the identification of unique colorability as the precise structural mechanism that restores a local permutation phase in this FCOA model.

---

## 2. Switching with more than two colors

Reference:

- P. J. Cameron, S. Tarzi, **Switching with more than two colours**, *European Journal of Combinatorics* 25(2) (2004), 169–177. DOI: `10.1016/S0195-6698(03)00097-0`.

The paper studies switching operations on finite and infinite `m`-colored complete graphs. A notable finite-case phenomenon is that for more than two colors all `m`-colored graphs on a fixed finite vertex set lie in the same switching class under the switching operation considered there.

### Relevance to QGE3

This is close in spirit because color names are not the main invariant and local changes of color phase are considered.

### Difference from QGE3

The QGE3 local phase is **not an allowed switching operation supplied as part of the model**. It is a discrepancy that must be *induced* by a carrier automorphism preserving only sparse equality data. The central QGE3 no-go theorem says that such an induced discrepancy need not even be a permutation of the local visible colors. Thus the failure occurs before ordinary nonabelian switching language becomes available.

The QGE3 comparison graph is also sparse and built from operation-cell composability rather than a complete colored graph on the original carrier.

---

## 3. Gain graphs and nonabelian switching

Gain graphs attach elements of a group `Gamma` to oriented edges, with reversal sending a gain to its inverse. Switching by a vertex function `eta` modifies gains by the familiar rule

\[
\varphi^\eta(e:u\to v)
=\eta(u)^{-1}\varphi(e)\eta(v).
\]

Representative references and expositions include Thomas Zaslavsky's gain-graph programme and later literature using group gain graphs. A recent accessible statement of the standard definition and switching rule occurs in work on gain-graph switching and spectral theory.

### Relevance to QGE3

Once a QGE3 component genuinely possesses a permutation-valued phase, its law

\[
\phi_{gh,C}
=
\phi_{g,hC}\circ\phi_{h,C}
\]

has the same noncommutative flavor as group-valued transport and switching.

### Difference from QGE3

In a gain graph, the group `Gamma` and gain labels are part of the input structure. In QGE3:

1. the output alphabet is anonymous and has no canonical group structure;
2. the candidate group is `S_q`, acting on color names rather than labeling comparison edges;
3. a local `S_q` element is not always defined;
4. the always-defined object is a transported proper-coloring state;
5. partial visible-support phases naturally form a groupoid rather than one fixed coefficient group.

Therefore QGE3 should not be presented as a new theorem about gain graphs. Gain/switching language is a useful comparison only in the phase sector.

---

## 4. Coherent configurations and colored relational structures

A coherent configuration is, in particular, a partition of `V^2` into binary relations subject to transpose and intersection-number regularity conditions. Schurian coherent configurations arise from orbitals of permutation groups. Modern expositions also emphasize the view as an edge-colored complete directed graph with strong regularity.

Representative references:

- D. G. Higman, **Coherent configurations. I. Ordinary representation theory**, *Geometriae Dedicata* 4 (1975), 1–32. DOI: `10.1007/BF00147398`.
- modern surveys/expositions connecting coherent configurations with Weisfeiler–Leman refinement and permutation groups.

### Relevance to QGE3

The complete four-ary equality model E remembers the partition of defined operation cells into anonymous terminal fibers. This is relational/partition data and sits naturally near the general world of colored relational structures.

### Difference from QGE3

QGE3 does not assume the terminal-fiber partition satisfies coherent-configuration intersection regularity. More importantly, Model T is a deliberately lossy **derived ternary reduct**: it retains equality only on composable cell pairs. The main question is precisely how much of the original fiber partition survives this reduct.

Hence coherent configurations provide a natural ambient language but do not by themselves yield the QGE3 sparse no-go or proper-coloring quotient theorem.

---

## 5. Relational complexity / k-ary recovery

Reference:

- G. Cherlin, **On the relational complexity of a finite permutation group**, *Journal of Algebraic Combinatorics* 43 (2016), 339–374. DOI: `10.1007/s10801-015-0636-8`.

Relational complexity studies the least arity needed to realize a permutation group as the automorphism group of an appropriate homogeneous relational structure, with an equivalent permutation-group formulation.

### Relevance to QGE3

Article A's complete-domain threshold

\[
q=2:\ k_{exact}=3,
\qquad
q\ge3:\ k_{exact}=4
\]

is clearly adjacent in spirit to bounded-arity recovery of automorphism groups.

### Difference from QGE3

The FCOA arity statements are relative to a highly specific reduct class generated from anonymous equality of operation outputs. They are not claims about the unrestricted relational complexity of the same permutation groups. QGE3 keeps this restriction explicit.

---

## 6. Colored structures with unlabeled relation classes

There is standard literature in which a coloring or partition of binary relations is treated either with named colors (isomorphisms preserve each relation) or with an unordered relation partition (isomorphisms may permute relation classes). This latter viewpoint is especially close to anonymous output values.

### Relevance to QGE3

Model E exactly belongs to this partition-preserving spirit: a carrier permutation is valid when it permutes the terminal fibers as blocks.

### Difference from QGE3

The ternary Model T does not expose the full partition. It exposes only local equality tests on the cell-composability graph. The new issue is reconstruction of an unnamed partition from a sparse family of equality/inequality tests.

---

## 7. Novelty boundary after comparison

The following objects/results are **not** claimed new in general mathematics:

- proper graph coloring;
- unique colorability;
- permutation-valued switching;
- group-valued gain graphs;
- groupoids of partial bijections;
- coherent configurations;
- relational complexity / k-closures.

The local QGE3 results that appear genuinely specific to the FCOA anonymous sparse-operation model are:

1. the exact T-equality-atom / constraint-quotient reduction of sparse composable-cell equality data;
2. the sharp three-carrier, four-defined-cell `q=3` counterexample to universal componentwise `S_q` phase transport;
3. the theorem that the universally defined transport datum is the proper-coloring orbit of the quotient, with an `S_q`/visible-support phase existing exactly when the transported fiber partition remains in the same color-relabeling orbit;
4. the exact two-stage obstruction to ternary exactness: local proper-coloring ambiguity plus inter-component gluing ambiguity;
5. the exact gluing criterion for partial visible-support permutations as the requirement that their union be the graph of one element of `S_q`.

These should be presented as results **inside the anonymous sparse-operation model**, not as claims of discovering proper-coloring or switching theory.

---

## 8. Publication positioning

A defensible publication claim is narrow:

> Sparse anonymous ternary equality transport for `q>=3` is governed first by a proper-coloring reconstruction problem, not by a universal nonabelian phase cocycle. The binary cocycle picture survives exactly in a color-rigid sector, while four-ary arbitrary-cell equality eliminates the obstruction universally.

This is a model-specific structural theorem connecting the FCOA sparse-operation problem to classical graph coloring and switching language.

No broader priority claim should be made without a deeper dedicated search for partition reconstruction from local equality tests.
