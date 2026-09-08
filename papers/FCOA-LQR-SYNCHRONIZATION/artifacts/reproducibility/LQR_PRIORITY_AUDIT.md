# QGE3 LQR — Literature and Priority Audit

**Branch:** `director/fcoa-rigidity-cost`  
**Scope:** point-image synchronization number `L_q(r)`, unique-coloring quotient, cut-space reduction, stabilization theorem.

## 1. Audit conclusion

No exact prior occurrence of the parameter

\[
L_q(r)=\min |S|
\]

for primitive same-source point-image constraints

\[
\pi_i(a)=\pi_j(a)
\]

forcing an arbitrary tuple in `S_q^r` to be diagonal was located in the searches performed for this audit.

This is **not** a universal priority proof. It is a negative dedicated search sufficient to support a narrow publication claim, provided the manuscript avoids claiming discovery of the surrounding classical theories.

The novelty claim should be restricted to the FCOA/LQR chain:

1. point-image synchronization problem extracted from the full-support phase sector;
2. exact synchronization/unique-coloring quotient equivalence;
3. exact formulas for `L_3(r)`, `L_q(3)`, and `L_q(4)`;
4. canonical partition-to-binary-cut-space reduction;
5. exact stabilization theorem and exact threshold

\[
L_q(r)=(r-1)q-(2^{r-1}-1),
\qquad
q\ge2^{r-1}-1.
\]

The following neighboring ingredients are classical and must not be claimed new.

---

## 2. Unique colorability

Classical reference:

- F. Harary, S. T. Hedetniemi, R. W. Robinson, **Uniquely colorable graphs**, *Journal of Combinatorial Theory* 6(3) (1969), 264–270. DOI `10.1016/S0021-9800(69)80086-4`.

A standard theorem from that paper says that in a uniquely colorable graph, the subgraph induced by any two color classes is connected.

This is exactly the external graph-theoretic ancestor of the LQR necessary condition

\[
\Gamma_a\cup\Gamma_b\text{ connected}.
\]

Therefore pair-union connectivity itself is not a new graph-coloring theorem.

The FCOA-specific contribution is that the point-image synchronization problem produces a restricted transversal quotient `H(S)` whose proper `q`-colorings are exactly satisfying phase tuples.

---

## 3. Permutation synchronization

Representative neighboring reference:

- D. Pachauri, R. Kondor, V. Singh, **Solving the multi-way matching problem by permutation synchronization**, *Advances in Neural Information Processing Systems 26* (2013).

That literature studies joint recovery of multiple pairwise permutations, mainly from noisy relative matching information and with algorithmic/statistical objectives.

It is conceptually adjacent but structurally different from LQR:

- LQR asks for the minimum number of exact primitive constraints of the special form `pi_i(a)=pi_j(a)`;
- the target is exact diagonal forcing in `S_q^r`;
- the optimization is combinatorial/extremal rather than noisy estimation;
- the cut-space and unique-coloring quotient arise from same-source equality constraints.

The audit did not locate the exact LQR extremal parameter in this synchronization literature.

---

## 4. Vector-space partitions and partial spreads

Classical references:

- O. Heden, **A survey of the different types of vector space partitions**, *Discrete Mathematics, Algorithms and Applications* 4(1) (2012), 1250001. DOI `10.1142/S1793830912500012`.
- T. Honold, M. Kiermaier, S. Kurz, **Partial Spreads and Vector Space Partitions**, in *Network Coding and Subspace Designs* (2018), 131–170. DOI `10.1007/978-3-319-70293-3_7`.

A vector-space partition is built from subspaces whose nonzero vectors are disjoint and cover the ambient nonzero vectors. Partial spreads and mixed-dimension subspace packings study closely related pairwise-trivial-intersection geometry.

Accordingly, the inequality

\[
\sum_a(2^{d_a}-1)\le2^{r-1}-1
\]

is standard nonzero-vector packing logic once the subspaces `W(P_a)` have been produced. It should not be branded as a new theorem of finite geometry.

Recommended manuscript terminology:

> **LQR cut-space packing inequality**

or

> **binary cut-space defect bound**

rather than an unqualified named claim such as “Mersenne inequality”. The Mersenne number `2^{r-1}-1` is a useful descriptor, but not a priority claim.

The programme-specific theorem is the canonical implication

\[
\text{LQR synchronization}
\Longrightarrow
W(P_a)\cap W(P_b)=\{0\},
\]

followed by exact attainment of the classical packing cap by the binary-cut synchronization gadget.

---

## 5. Partition lattice / cut spaces

The map

\[
P\mapsto W(P)
\]

sending a set partition to the binary functions constant on its blocks is a natural classical construction. Likewise the identity

\[
W(P)\cap W(Q)=W(P\vee Q)
\]

is a basic lattice-theoretic fact once the spaces are defined.

No novelty should be claimed for that isolated identity.

The new role is its use as the exact bridge from component partitions of LQR constraint graphs to a finite-geometry defect bound.

---

## 6. What the manuscript can safely claim

A conservative claim set is:

### Claim A — model-specific parameter
Define and study the exact extremal synchronization number `L_q(r)` for same-source point-image constraints arising in the full-support multicolor FCOA phase sector.

### Claim B — quotient theorem
Show that synchronizing constraint systems are exactly those whose canonical transversal quotient is uniquely `q`-colorable relative to its canonical partition.

### Claim C — exact low-dimensional laws
Prove

\[
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil,
\]

\[
L_q(3)=2q-3,
\]

and the complete four-phase formula.

### Claim D — exact stabilization
Prove for every fixed `r>=2`

\[
L_q(r)=(r-1)q-(2^{r-1}-1)
\]

for all

\[
q\ge2^{r-1}-1,
\]

and prove that this threshold is exact.

### Claim E — structural bridge
Identify the LQR defect with dimensions of canonical binary cut spaces whose nonzero parts are pairwise disjoint.

These claims are sufficiently narrow to avoid appropriating classical unique-colorability, subspace-packing, partial-spread, or permutation-synchronization theory.

---

## 7. Claims to avoid

Do not write any of the following without a stronger priority search:

- “we introduce permutation synchronization”;
- “we discover the pairwise-color connectivity theorem”;
- “we introduce partial spreads / vector-space partitions”;
- “we prove a new general bound for pairwise disjoint subspaces”;
- “the partition lattice is embedded in a binary subspace lattice for the first time”;
- “Mersenne defect inequality is a new finite-geometry inequality”.

The paper is strongest when it states that classical tools become unexpectedly exact after the FCOA/LQR reduction.

---

## 8. Foundation citation gate

Any new LQR manuscript is unpublished work inside FCOA and must satisfy the direction-wide Foundation gate.

The abstract must explicitly identify the framework and print

`https://doi.org/10.5281/zenodo.22164246`

for:

**Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline**.

The bibliography must contain the same Foundation article with DOI `10.5281/zenodo.22164246`.

The body must explicitly identify:

1. the FCOA carrier involved in the upstream phase model;
2. relevant sorts;
3. primitive signature;
4. whether the LQR system is an abstract phase-level optimization rather than a real operation-cell extension;
5. erasure/recovery convention;
6. relation to the published QGE3 foundation article.

No multicolor real-cell `alpha_q` should be introduced in this paper.

---

## 9. Priority verdict

\[
\boxed{\text{NO DIRECT PRIOR INSTANCE FOUND IN THE DEDICATED SEARCH}}
\]

but

\[
\boxed{\text{CLAIM NOVELTY ONLY FOR THE LQR-SPECIFIC SYNTHESIS AND EXACT FORMULAS}.}
\]

The literature audit therefore supports publication preparation, subject to normal external peer review and bibliographic verification during manuscript assembly.
