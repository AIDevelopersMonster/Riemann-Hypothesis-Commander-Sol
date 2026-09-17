# HATTER-SOL-11 · Hostile Audit of the Outerplanar Theorem Spine

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Audit status:** theorem spine survives, with one literal small-host correction and one mandatory scope correction.

This audit covers the outerplanar chain developed in:

- `OUTERPLANAR_ORBITAL_MEMORY_21.md`;
- `OUTERPLANAR_RANK_SWAP_NO_GO.md`;
- `OUTERPLANAR_RANK_SWAP_COMPLETE_CLASSIFICATION.md`;
- `OUTERPLANAR_FULL_INTERIOR_FIBER_CLASSIFICATION.md`.

The purpose is adversarial: look for a counterexample, hidden feasibility failure, incorrect extremal bound, invalid Pareto inference, or an overclaim of model scope.

---

## 1. Model scope: mandatory publication correction

All results audited here are results for the **orbit-total two-channel projection**

\[
\Omega=(a;\{b,c\})
\longmapsto
\Xi=(A,O):=(a,b+c),
\]

introduced in `ORBITAL_NETWORK_FIBER_SEPARATION.md`.

That earlier file explicitly states that `Xi` is a minimal canonical two-channel object for testing axial/oblique orbit labels and is **not** claimed to be the unique final network semantics of the full orbital datum `Omega`.

Therefore every phrase such as

> complete outerplanar orbital classification

must be read, and in the publication manuscript must be written, as

> complete outerplanar classification **for the orbit-total response model `Xi`** on the stated host family.

In particular, the theorem

\[
\nu_{O,n}(P,Q)
=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}
\end{cases}
\]

is complete for the three `Xi` states attached to a generic-odd interior forgetting fiber on even hosts `n>=4`. It does **not** prove that every richer network semantics retaining the full unordered oblique pair `{b,c}` has the same collision pattern.

This is a scope correction, not a mathematical failure of the proved two-channel theorems.

---

## 2. Small-host literal correction for `H_n`

The chain-of-triangles graph

\[
H_n:
\quad
E(H_n)=\{\{i,i+1\}:1\le i<n\}
\cup
\{\{i,i+2\}:1\le i<n-1\}
\]

has `2n-3` edges and is maximal outerplanar.

For even `n>=6`, its degree sequence is

\[
2,3,4,\ldots,4,3,2
\]

and

\[
\Delta(H_n)=4.
\]

For the exceptional smallest host `n=4`, however,

\[
\deg(H_4)=(2,3,3,2),
\qquad
\boxed{\Delta(H_4)=3,}
\]

not `4`.

Thus the literal statement `Delta(H_n)=4` for all even `n>=4` in `OUTERPLANAR_RANK_SWAP_NO_GO.md` is false at `n=4`.

### Effect on the proofs

None.

Every downstream use requires only

\[
\boxed{\Delta(H_n)\le4,}
\]

which is true for all even `n>=4`.

In particular:

- the capacity-1 matching complement has maximum degree at most `3`;
- the capacity-2 Hamiltonian-cycle complement has maximum degree at most `2`;
- `H_n` is feasible as a pure channel for every capacity `A>=4`;
- all edge-count extremality statements remain unchanged.

The publication version must replace `Delta(H_n)=4` by

\[
\boxed{
\Delta(H_n)\le4,
\quad
\Delta(H_4)=3,
\quad
\Delta(H_n)=4\text{ for }n\ge6.
}
\]

---

## 3. Audit of the low-degree obstruction

The outerplanar spine uses the classical fact:

> every finite simple outerplanar graph on at least two vertices has at least two vertices of degree at most `2`.

For a uniform channel of capacity `A>=3`, those two vertices force

\[
B_A\ge2(A-2).
\]

This inference is valid even when a second channel is present, because channel degree is bounded above by total degree at each vertex.

No hidden assumption that the channel subgraph is connected is used.

Verdict: **sound**.

---

## 4. Audit of the sharp capacity-3 construction

The graph `G_m` on `n=2m` vertices is the outer cycle plus the nested chords

\[
\{j,2m-j\},
\qquad
1\le j\le m-1.
\]

The chords are pairwise disjoint and noncrossing. The graph is outerplanar and connected, with degree sequence

\[
2,3,3,\ldots,3,2.
\]

Therefore a pure capacity-3 channel has exactly two unused ports:

\[
B=2.
\]

This attains the low-degree lower bound.

Verdict: **sound**.

---

## 5. Audit of the outerplanar edge ceiling and capacity `A>=4`

For every simple outerplanar graph on `n>=2` vertices,

\[
|E|\le2n-3.
\]

Therefore any single channel of capacity `A>=4` satisfies

\[
B_A=nA-2|E_A|
\ge
n(A-4)+6.
\]

The corrected property

\[
\Delta(H_n)\le4
\]

and

\[
|E(H_n)|=2n-3
\]

show that the lower bound is attained by coloring all edges of `H_n` with that channel.

Hence the exact channel floor

\[
\phi_n(A)=
\begin{cases}
2,&A=3,\\
n(A-4)+6,&A\ge4
\end{cases}
\]

survives the audit.

Verdict: **sound**.

---

## 6. Audit of capacity-1 saturation

For even `n`, the edge set

\[
M_1=\{\{1,2\},\{3,4\},\ldots,\{n-1,n\}\}
\]

is a perfect matching in `H_n`.

Coloring `M_1` by the capacity-1 channel saturates that channel at every vertex.

The complement has

\[
\Delta(H_n-M_1)\le3,
\]

including the `n=4` case. Thus it is feasible in a complementary channel of capacity at least `3`.

Verdict: **sound**.

---

## 7. Audit of capacity-2 saturation

For every even `n>=4`, the sequence

\[
1,2,4,6,\ldots,n,n-1,n-3,\ldots,3,1
\]

is a Hamiltonian cycle in `H_n`; every consecutive pair differs by `1` or `2`.

Coloring this cycle by the capacity-2 channel saturates that channel.

Every vertex loses exactly two incidences from `H_n`, so the complement has maximum degree at most `2`.

Thus the complementary channel is feasible whenever its capacity is at least `2`.

Verdict: **sound**.

---

## 8. Audit of exact `(2,1)` outerplanar response

For total node capacity `3`, the low-degree lemma implies total boundary at least `2`.

Because the host size is even, both typed boundary coordinates are even.

The `G_m` constructions attain both vectors

\[
(0,2),
\qquad
(2,0)
\]

for each mixed state `(2,1)` and `(1,2)`, while the pure state `(0,3)` attains only

\[
(0,2)
\]

at its optimum.

Any feasible point with larger total boundary is componentwise dominated by one of these extremal points.

Therefore

\[
Z_O(2,1)=Z_O(1,2)=X^2+Y^2,
\qquad
Z_O(0,3)=Y^2
\]

is exact in the `Xi` model.

Verdict: **sound**.

---

## 9. Audit of the `(3,1)` and `(2,2)` calibrations

For `(3,1)`, the universal constraints are

\[
B_A\ge2,
\qquad
B_A+B_O\ge6,
\qquad
B_A,B_O\in2\mathbb Z_{\ge0}.
\]

The three constructed points

\[
(2,4),(4,2),(6,0)
\]

therefore dominate every other feasible point and form the exact Pareto front.

Channel exchange gives the exact `(1,3)` front.

For `(2,2)`, the only universal constraints needed are

\[
B_A+B_O\ge6,
\qquad
B_A,B_O\in2\mathbb Z_{\ge0},
\]

and all four step-two points on the total-boundary-6 line are explicitly attained:

\[
(0,6),(2,4),(4,2),(6,0).
\]

Thus that front is also exact.

Verdict: **sound**.

---

## 10. Audit of the complete rank-swap theorem

For `P>=3`, the minimum axial boundary in state `(P,Q)` is exactly `phi_n(P)`.

For `P>Q>=3`, strict monotonicity

\[
\phi_n(P)>\phi_n(Q)
\]

separates the rank-swapped response polynomials by their smallest `X` exponent.

For `Q=1,2`, the swapped low-capacity axial channel can be saturated, producing `X` exponent zero, while the `P>=3` axial channel cannot.

Combining this with the exact `(2,1)` calculation gives

\[
\boxed{
Z_O(P,Q)=Z_O(Q,P)
\iff
(P,Q)=(2,1)
}
\]

for `P>Q>0`, even `n>=4`, in the orbit-total `Xi` model.

Verdict: **sound**.

---

## 11. Audit of mixed/pure separation

The pure state `(0,S)`, `S=P+Q`, has singleton polynomial

\[
Z_O(0,S)=Y^{\psi_n(S)},
\]

where

\[
\psi_n(S)=
\begin{cases}
2,&S=3,\\
n(S-4)+6,&S\ge4.
\end{cases}
\]

For Type I `(P,Q)`:

- if `P>=3`, every Pareto monomial has positive `X` exponent;
- the exceptional `P=2,Q=1` case was computed directly.

For Type II `(Q,P)`:

- if `Q>=3`, again every Pareto monomial has positive `X` exponent;
- if `Q=1,2`, its minimum `Y` exponent is `phi_n(P)`, while the pure state's unique exponent is strictly larger:

\[
\psi_n(P+Q)>\phi_n(P).
\]

For `P>=4`, the exact gap is

\[
\psi_n(P+Q)-\phi_n(P)=nQ>0.
\]

No mixed/pure collision remains.

Verdict: **sound**.

---

## 12. Pareto-minimality audit

Several proofs use the following step:

> minimize one boundary coordinate over all feasible networks, then among those minimizers minimize the other coordinate.

Because the feasible boundary set is finite at fixed host size, such a lexicographic minimizer exists. It is Pareto-minimal: a point dominating it would either lower the first coordinate or preserve the first while lowering the second, contradicting its construction.

Thus the minimum-coordinate witnesses really do appear in the response polynomial.

Verdict: **sound**.

---

## 13. Host-size and parity scope

The audited theorems are stated for

\[
\boxed{n=2m\ge4.}
\]

Evenness is used materially:

- perfect matchings saturating capacity `1`;
- the chosen Hamiltonian-cycle constructions;
- even typed boundary coordinates.

No theorem in this audit is promoted to odd host size.

The `n=2` case is separately governed by the earlier two-node theorem and must not be silently folded into the outerplanar `n>=4` classification.

Verdict: **scope correct after explicit statement**.

---

## 14. Audit conclusion

No counterexample was found to the mathematical theorem spine.

The outerplanar block survives hostile audit with exactly two corrections:

1. **literal small-host correction:** `Delta(H_4)=3`, while `Delta(H_n)=4` only for even `n>=6`; all proofs require only `Delta(H_n)<=4` and remain valid;
2. **model-scope correction:** all claims are complete for the canonical orbit-total two-channel projection `Xi=(A,O)`, not for every possible richer network semantics built from the full orbital datum `Omega`.

Subject to these corrections, the publication-grade outerplanar statement is:

\[
\boxed{
\nu^{\Xi}_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&P>Q>0,\ (P,Q)\ne(2,1),
\end{cases}
\qquad n\in2\mathbb Z,\ n\ge4.
}
\]

Here `nu^Xi` counts distinct **orbit-total response polynomials** among

\[
(P,Q),
\quad
(Q,P),
\quad
(0,P+Q).
\]

---

## 15. Publication and next-research decision

The outerplanar theorem spine has crossed the internal proof threshold **within the `Xi` model**.

It is ready to be used as a proved section of HATTER-SOL-11 after the two wording corrections above are propagated into the manuscript.

The next mathematical target should therefore move to planar geometry, beginning with the critical total capacities

\[
S=5,6,7,
\]

where the planar edge ceiling and low-degree constraints change regime.

Do not introduce a geometry Laplacian yet. Continue to use the polynomial-valued response and finite differences between geometry classes until a canonical geometry-transition operator is independently justified.