# HATTER-SOL-11 · Orbital-Network Separation of Forgetting Fibers

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the first operational test after `FORGETTING_MAP_FIBER_CLASSIFICATION.md`.

## 1. Question

For a generic odd discriminant world, `FORGETTING_MAP_FIBER_CLASSIFICATION.md` proves that the same folded pair

\[
\Pi_\Delta(\alpha)=(P,Q)
\]

can come from up to three distinct canonical orbital geodesic signatures.

The next question is operational:

> does a network that sees the natural axial/oblique orbit labels distinguish members of one `(P,Q)` fiber before the HATTER-SOL fold forgets those labels?

We answer this exactly for the smallest connected host.

---

## 2. Canonical orbit-total capacity

Let

\[
\Omega_\Delta(\alpha)
=(a;\{b,c\})
\]

be the generic-odd orbital geodesic signature from `ODD_GEODESIC_ORBIT_CLASSIFICATION.md`:

- `a` is the axial usage;
- `b,c` are the two conjugate oblique-direction usages, unordered.

Define the **orbit-total capacity**

\[
\boxed{
\Xi_\Delta(\alpha)=(A,O):=(a,b+c).
}
\]

This projection is canonical under sign and conjugation because conjugation only exchanges `b,c`.

It also preserves the scalar word capacity exactly:

\[
\boxed{
A+O=a+b+c=P+Q=\rho_\Delta(\alpha).
}
\]

`Xi` is not asserted to replace the full orbital datum `Omega`; it is the minimal two-channel object needed to test whether the natural orbit labels can survive network optimization.

---

## 3. Minimal orbit-labelled network

Take two identical factor nodes with orbit-total capacity `(A,O)`.

Use the HATTER-SOL simple-support rule:

- the unique unordered vertex pair supports at most one edge total;
- that edge may be typed `A` or `O`;
- an `A` edge consumes one axial port at each endpoint;
- an `O` edge consumes one oblique-orbit port at each endpoint.

Let

\[
\mathcal R_2^{\mathrm{orb}}(A,O)
\]

denote the Pareto-minimal labelled boundary set `(B_A,B_O)`.

Because a connected two-vertex graph has exactly one edge, the response is immediate:

\[
\boxed{
\mathcal R_2^{\mathrm{orb}}(A,O)=
\begin{cases}
\{(2A-2,2O),(2A,2O-2)\},&A>0,\ O>0,\\
\{(2A-2,0)\},&A>0,\ O=0,\\
\{(0,2O-2)\},&A=0,\ O>0,\\
\varnothing,&A=O=0.
\end{cases}}
\]

The two points in the first case are incomparable, so both belong to the Pareto front.

---

## 4. Interior three-point fiber

Fix

\[
P>Q>0.
\]

By T11.21, the folded fiber contains exactly three symmetry-distinct orbital signatures:

\[
\Omega_I=(P;\{Q,0\}),
\]

\[
\Omega_{II}=(Q;\{P,0\}),
\]

\[
\Omega_{III}=(0;\{P,Q\}).
\]

Their orbit-total capacities are

\[
\boxed{
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,P+Q).
}
\]

Hence

\[
\mathcal R_I
=
\{(2P-2,2Q),(2P,2Q-2)\},
\]

\[
\mathcal R_{II}
=
\{(2Q-2,2P),(2Q,2P-2)\},
\]

and

\[
\mathcal R_{III}
=
\{(0,2(P+Q)-2)\}.
\]

### Theorem T11.22 — interior orbital-fiber separation

For every generic odd discriminant and every `P>Q>0`,

\[
\boxed{
\mathcal R_I,
\mathcal R_{II},
\mathcal R_{III}
\text{ are pairwise distinct.}
}
\]

### Proof

`R_III` is a singleton, while `R_I` and `R_II` each contain two points, so it differs from both.

For `R_I` and `R_II`, the minimum first boundary coordinate is respectively

\[
2P-2
\quad\text{and}\quad
2Q-2.
\]

Since `P>Q`, these are unequal. Therefore the two Pareto sets cannot coincide. QED.

### Consequence

The published folded pair `(P,Q)` loses information that is operationally visible already on the smallest connected orbit-labelled host.

Thus the orbital refinement is not merely a different notation for the same two-channel response.

---

## 5. Diagonal fiber

Let

\[
P=Q=r>0.
\]

T11.21 gives two orbital signatures:

\[
\Omega_D=(r;\{r,0\}),
\qquad
\Omega_O=(0;\{r,r\}).
\]

Their orbit totals are

\[
\Xi_D=(r,r),
\qquad
\Xi_O=(0,2r).
\]

Therefore

\[
\mathcal R_D
=
\{(2r-2,2r),(2r,2r-2)\},
\]

while

\[
\mathcal R_O
=
\{(0,4r-2)\}.
\]

These are distinct for every `r>0`.

---

## 6. Boundary fiber and the unique two-node blind spot

Let

\[
P>0,
\qquad Q=0.
\]

The two signatures are pure axial and pure oblique:

\[
(P;\{0,0\}),
\qquad
(0;\{P,0\}).
\]

Their responses are

\[
\{(2P-2,0)\}
\quad\text{and}\quad
\{(0,2P-2)\}.
\]

They are distinct iff

\[
P>1.
\]

At

\[
\boxed{(P,Q)=(1,0)}
\]

both responses equal

\[
\boxed{\{(0,0)\}}.
\]

This is not an orbital-symmetry identification. It is a network saturation collision: one unit port of either label is completely consumed by the unique edge, so the boundary vector forgets which label carried that edge.

### Corollary T11.22a — complete two-node visibility classification

For every nonzero generic-odd `(P,Q)` fiber, the two-node orbit-labelled Pareto response separates all canonical orbital members **except** the single pure-unit fiber

\[
\boxed{(P,Q)=(1,0)}.
\]

---

## 7. Maximal-first probe on the same fibers

Now apply the explicitly noncanonical probe from `MAXIMAL_FIRST_GEOMETRY_PROBE.md`.

For this two-node experiment define the priority rule `pi_max`:

> use the edge type with the larger currently available orbit-total capacity; if the two maxima are equal, retain both tied choices rather than inventing an order.

This is a search convention only.

For `P>Q>0`, the three maximal-first traces are

\[
M_I=\{(2P-2,2Q)\},
\]

\[
M_{II}=\{(2Q,2P-2)\},
\]

\[
M_{III}=\{(0,2(P+Q)-2)\}.
\]

The third trace is always distinct from the first two.

The first two coincide exactly when

\[
2P-2=2Q,
\]

that is,

\[
\boxed{P=Q+1.}
\]

### Theorem T11.23 — exact maximal-first blind line

On an interior generic-odd fiber `P>Q>0`, the maximal-first probe separates all three orbital members iff

\[
\boxed{P-Q\ne1.}
\]

When

\[
\boxed{P-Q=1,}
\]

the Type-I and Type-II maximal-first traces collide even though their full orbit-labelled Pareto fronts remain distinct.

This gives an exact example of the methodological distinction introduced in `MAXIMAL_FIRST_GEOMETRY_PROBE.md`:

\[
\boxed{
\text{the cheap probe can lose information that the full response retains.}
}
\]

---

## 8. Tie discipline matters

For the diagonal fiber `(r,r)`, the mixed axial/oblique state has equal orbit totals. The maximal-first convention therefore has no canonical unique first choice.

Retaining both tied maxima reproduces

\[
\{(2r-2,2r),(2r,2r-2)\}
\]

and still distinguishes the pure-oblique member.

If one arbitrarily breaks the tie, artificial collisions can be created. In particular, at `r=1`, choosing the axial edge gives `(0,2)`, the same boundary as the pure-oblique state `(0,2)`.

Therefore the experimental protocol must obey:

\[
\boxed{
\text{equal maxima are retained as ties unless an external tie-break is explicitly declared.}
}
\]

---

## 9. What is proved and what is not

Proved here:

1. a canonical orbit-total projection `Xi=(A,O)` from the symmetry-resolved geodesic signature;
2. an exact two-node orbit-labelled Pareto response;
3. full separation of every interior and diagonal forgetting-map fiber;
4. a unique boundary saturation blind spot at `(1,0)`;
5. an exact maximal-first probe blind line `P-Q=1` in the interior fiber.

Not claimed:

- that orbit-total aggregation is the only possible orbital network semantics;
- that maximal-first is canonical;
- that a two-node result classifies all larger hosts;
- that the network boundary alone recovers multiplicative norm or principalization residue.

---

## 10. Next target

The next serious step is to lift T11.22 from the two-node laboratory to even complete hosts `K_{2m}`.

For the three generic-odd fiber types

\[
(P,Q),
\qquad
(Q,P),
\qquad
(0,P+Q)
\]

in axial/oblique orbit totals, derive the exact full Pareto fronts as a function of host degree

\[
c=2m-1.
\]

Then determine the first host scale at which the three orbital responses collide after saturation / interface forgetting.

This will quantify how long the information hidden by the HATTER-SOL `(P,Q)` fold remains visible to an orbit-aware network.