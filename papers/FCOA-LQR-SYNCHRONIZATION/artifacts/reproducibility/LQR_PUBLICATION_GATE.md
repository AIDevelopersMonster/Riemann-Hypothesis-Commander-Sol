# QGE3 LQR — Publication Gate After Hostile Audit

**Branch:** `director/fcoa-rigidity-cost`  
**Status:** MATHEMATICAL CONTENT APPROVED FOR MANUSCRIPT ASSEMBLY

## 1. Accepted theorem package

The following results passed hostile audit and may be treated as theorem-level manuscript content.

### Exact three-color row

\[
\boxed{
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil.
}
\]

### Exact two-phase column

\[
\boxed{L_q(2)=q-1.}
\]

### Exact three-phase column

\[
\boxed{L_q(3)=2q-3\qquad(q\ge3).}
\]

### Exact four-phase column

\[
\boxed{
L_q(4)=
\begin{cases}
3, & q=2,\\
2q-1, & 3\le q\le5,\\
12, & q=6,\\
3q-7, & q\ge7.
\end{cases}
}
\]

### General large-alphabet stabilization

For every `r>=2`,

\[
\boxed{
L_q(r)=(r-1)q-(2^{r-1}-1)
}
\]

for every

\[
\boxed{q\ge2^{r-1}-1,}
\]

and the threshold is exact.

### Structural equivalence

A point-image constraint system synchronizes exactly when its canonical transversal quotient admits only the canonical `q`-coloring up to global color relabeling.

### Cut-space reduction

For a color partition `P_a`, the canonical binary cut space satisfies

\[
\dim W(P_a)=|P_a|-1,
\]

and synchronization forces

\[
W(P_a)\cap W(P_b)=\{0\}
\qquad(a\ne b).
\]

This yields the packing bound

\[
\sum_a(2^{d_a}-1)\le2^{r-1}-1.
\]

---

## 2. Audit findings

`LQR_HOSTILE_AUDIT.md` records:

- stabilization theorem: PASS;
- exact threshold: PASS;
- binary-cut construction: PASS;
- four-phase package: PASS WITH ONE PRESENTATION REPAIR.

The only repair is local: the concrete `q=3,r=4` five-constraint realization in `LQR_R4_THEOREM.md` must explicitly state why that particular realization synchronizes, rather than infer synchronization merely from the already known optimum cardinality. The realization was independently verified and is equivalent to a previously proved three-color gadget after relabeling.

This does not affect any theorem statement or numerical value.

---

## 3. Independent finite verification

Two verifier layers now exist.

### `verify_lqr.py`
Checks:

- theorem constructions for the exact `q=3` row;
- theorem constructions for `r=3`;
- general upper-bound constructions;
- exact selected `r=4` cells.

### `verify_lqr_cutspace.py`
Checks independently:

- all set partitions through `r=6`;
- `|W(P)|=2^(|P|-1)`;
- `W(P) cap W(Q)=W(P vee Q)`;
- exact weighted partition-packing defect capacity for `r=5`, `q=1,...,15`.

The theorem proofs do not depend on either verifier.

---

## 4. Literature firewall

The manuscript must explicitly treat the following as classical neighboring mathematics:

1. unique colorability;
2. pairwise connectivity of color classes in uniquely colorable graphs;
3. permutation synchronization as a broader algorithmic field;
4. partial spreads and vector-space partitions;
5. nonzero-vector packing bounds for pairwise trivially intersecting subspaces;
6. partition-lattice / block-constant function constructions.

The safe novelty claim is the FCOA/LQR synthesis and exact extremal formulas.

Recommended references include:

- Harary, Hedetniemi, Robinson (1969), DOI `10.1016/S0021-9800(69)80086-4`;
- Pachauri, Kondor, Singh (NIPS 2013), permutation synchronization;
- Heden (2012), DOI `10.1142/S1793830912500012`;
- Honold, Kiermaier, Kurz (2018), DOI `10.1007/978-3-319-70293-3_7`.

Do not present the subspace counting inequality itself as a new finite-geometry theorem.

---

## 5. Terminology repair

Avoid an unqualified branded name such as

> “Mersenne defect inequality”

if it could suggest priority for the underlying subspace packing count.

Preferred manuscript language:

- **LQR cut-space packing inequality**;
- **binary cut-space defect bound**;
- **Mersenne-sized defect cap** only descriptively.

The exact threshold theorem is genuinely the programme-level result; the counting step is classical once the cut spaces are identified.

---

## 6. Mandatory Foundation gate

The manuscript abstract must explicitly say that the work uses the FCOA framework fixed by Definition 1.0 and must print:

`https://doi.org/10.5281/zenodo.22164246`

The bibliography must contain the full Foundation reference with DOI:

`10.5281/zenodo.22164246`.

The body must identify:

- exact FCOA carrier/sorts inherited from the phase model;
- primitive signature at the LQR level;
- relation to the published QGE3 theorem package;
- that `L_q(r)` is an abstract full-support phase synchronization number;
- that no multicolor real-cell `alpha_q` is defined;
- erasure/recovery interpretation appropriate to the phase abstraction.

---

## 7. Manuscript architecture recommendation

Recommended article structure:

1. FCOA/QGE3 context and problem extraction;
2. definition of `L_q(r)`;
3. synchronization/unique-coloring equivalence;
4. pair-union lower bound;
5. exact `q=3` row;
6. exact `r=3` column;
7. exact `r=4` column and phase transition;
8. binary-cut construction for arbitrary `r`;
9. cut-space reduction;
10. exact large-alphabet stabilization theorem and threshold;
11. finite pre-stabilization sector;
12. literature comparison and novelty boundary;
13. open problems.

The paper should emphasize that the final general theorem was obtained by combining the LQR-specific cut-space reduction with a classical disjoint-nonzero-vector packing principle.

---

## 8. Publication decision

\[
\boxed{\text{MATHEMATICAL PUBLICATION GATE: PASS}}
\]

\[
\boxed{\text{LITERATURE POSITIONING GATE: PASS WITH CONSERVATIVE CLAIMS}}
\]

\[
\boxed{\text{MANUSCRIPT ASSEMBLY: APPROVED}}
\]

The next task is article construction and final pre-release audit, not further theorem hunting as a prerequisite for publication.
