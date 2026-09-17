# HATTER-SOL-11

# Orbital Port Filtrations: How Network Geometry Forgets Arithmetic Direction Data

**Malachevsky, A.A.**  
ORCID: `0009-0008-6009-3196`

**Series:** HATTER-SOL · Arithmetic Tea Party  
**Version:** EN v0.2 publication candidate  
**Date:** 2026-09-14  
**Scope:** imaginary-quadratic arithmetic interfaces; canonical orbit-total network quotient `Xi`; exact connected Pareto response.

---

## Abstract

Typed arithmetic-network models compress local arithmetic structure before global optimization. This raises two different information questions: what is already forgotten by the local interface, and what additional information is erased only after a network architecture is imposed?

For the imaginary-quadratic HATTER interface we resolve these questions at the level of shortest lattice directions. In a generic odd discriminant world, the natural symmetry action has one axial direction orbit and one conjugate oblique orbit. The published magnitude-sorted pair

\[
\Pi(\alpha)=(P,Q),\qquad P\ge Q\ge0,
\]

is therefore a forgetting map from an intrinsic direction-orbit datum rather than a complete direction label. We classify every fiber. In the strict interior case `P>Q>0` there are exactly three canonical orbital placements,

\[
(P;\{Q,0\}),\qquad(Q;\{P,0\}),\qquad(0;\{P,Q\}),
\]

whose canonical orbit-total network states are

\[
(P,Q),\qquad(Q,P),\qquad(0,P+Q).
\]

These states are operationally distinguishable already on the two-vertex connected host. Their later loss of distinguishability depends sharply on geometry. Every even path preserves all three states at every scale. In the outerplanar class, the three states remain distinct for every interior fiber except the unique mixed rank-swap collision `(2,1)\leftrightarrow(1,2)`; the pure-oblique state never joins that collision. On the other hand, if `H` is a connected even-order `d`-regular 1-factorizable host and total local capacity satisfies `P+Q\ge d`, the exact two-channel Pareto response depends only on `(n,d)` and the local capacities. Consequently the number of response classes in an interior fiber obeys the sharp degree filtration

\[
\boxed{
3\quad(d<P),\qquad
2\quad(P\le d<P+Q),\qquad
1\quad(d=P+Q).
}
\]

At the planar tetrahedral, octahedral, and icosahedral orders this fixed-host theorem lifts to the entire planar geometry class and yields exact host-scale memory trajectories, including `3\to2\to1` for the fiber `(4,1)` along orders `4\to6\to12`.

The result is deliberately not presented as a new theory of graph factors. Degree-constrained factors, factorization, colored degree constraints, and 1-factorization are classical. The contribution claimed here is their composition with an arithmetic symmetry quotient: intrinsic direction orbit \(\to\) folded interface \(\to\) exact Pareto network response \(\to\) geometry-controlled information loss. We also prove that the arithmetic orbit filtration does not imply a universal strongest-first activation law.

---

# 1. Introduction

## 1.1 The question behind the folded interface

HATTER-SOL-09 introduced world-dependent typed factor interfaces and Pareto network responses. HATTER-SOL-10 extended the construction from unique element factorization to prime ideals and minimal principalization witnesses. In both cases a local arithmetic object is compressed to a small interface before the global graph is optimized.

The present paper asks what that compression forgets.

The basic interface is a decreasingly sorted pair

\[
\Pi(\alpha)=(P,Q).
\]

Numerically, `P` is the larger magnitude. That fact alone does not tell us whether `P` belongs to a distinguished arithmetic direction orbit. In an arithmetic lattice with nontrivial symmetry, magnitude rank and orbit membership are different concepts.

The central architecture studied here is

\[
\boxed{
\Omega
\longrightarrow
\Xi
\longrightarrow
\Pi=(P,Q)
\longrightarrow
Z_{\mathcal C,n}^{\Xi}.
}
\]

Here:

- `Omega` is the intrinsic direction-orbit signature;
- `Xi` is the canonical orbit-total two-channel quotient;
- `Pi` is the magnitude-sorted HATTER interface;
- `Z` is the exact connected Pareto response for a fixed host or geometry class.

The paper separates three distinct operations:

1. **arithmetic forgetting**: losing orbit placement under `Omega -> Pi`;
2. **network forgetting**: distinct `Xi` states acquiring the same optimized response;
3. **observational forgetting**: a restricted probe or scalar observable identifying responses that the full Pareto object still separates.

Only the first two are needed for the main theorems.

## 1.2 Novelty boundary

The graph-theoretic ingredients used below belong to established factor theory. `(g,f)`-factors, minimum-deficiency factors, factor decompositions, `[a,b]`-factorizations, 1-factorizations, multiple degree constraints, colored matching variants, and degree-sequence optimization are classical or well-developed topics [1--7]. We therefore make no novelty claim for:

- degree-constrained spanning subgraphs as such;
- 1-factorization as such;
- decomposing a regular host into perfect matchings;
- polynomial encoding of a finite Pareto set;
- Gaussian/Eisenstein unit groups;
- the standard shortest-path metric of square or hexagonal lattices.

The paper's claim is narrower. A symmetry-resolved arithmetic interface has a nontrivial finite forgetting fiber, and exact network optimization imposes a second filtration on the visibility of that fiber. The main theorem identifies the corresponding memory thresholds on a broad regular-factorizable host class.

## 1.3 Main results

The proof spine has five stages.

**Arithmetic orbit classification.** The natural direction action has two orbits in every generic imaginary-quadratic world and one orbit exactly in the Gaussian and Eisenstein fusion cases.

**Exact generic-odd geodesics.** For odd discriminant `Delta<-3`, the unique shortest direction-labelled representation is obtained by a median formula. The published `(P,Q)` pair is exactly the decreasing sort of its two nonzero absolute counts.

**Forgetting fibers.** A strict interior pair `P>Q>0` has exactly three canonical orbital placements and hence three orbit-total states:

\[
(P,Q),\quad(Q,P),\quad(0,P+Q).
\]

**Geometry-dependent memory.** Paths preserve all three states. Outerplanar geometry has one and only one interior mixed collision, `(2,1)\leftrightarrow(1,2)`, with the pure state still visible.

**Regular-factorizable filtration.** On a connected even-order `d`-regular 1-factorizable host in the critical/overfull regime, the exact response depends only on `(n,d)`. For an interior fiber the class count is

\[
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
\]

This final filtration is an operational network theorem. It must not be read backwards as an intrinsic strongest-first activation rule.

---

# 2. Arithmetic direction orbits

## 2.1 Imaginary-quadratic step sets

Let `K` be an imaginary quadratic field with discriminant `Delta` and ring of integers `O_K`. The HATTER additive step set is

\[
S_\Delta=\{\pm1,\pm F_\Delta,\pm\overline{F_\Delta}\},
\]

with duplicates removed. Passing modulo sign gives the undirected direction set

\[
D_\Delta=S_\Delta/\{\pm1\}.
\]

Let `Gamma_Delta` be the permutation group on `D_Delta` generated by complex conjugation and by multiplication by units whenever that multiplication preserves the step-direction set.

The `Gamma_Delta`-orbits are the natural port-direction orbits.

### Even discriminants

For

\[
\Delta\equiv0\pmod4,\qquad\Delta<-4,
\]

write

\[
F=\frac{\sqrt\Delta}{2},\qquad F^2=-q,\qquad q=|\Delta|/4>1.
\]

Then

\[
D_\Delta=\{[1],[F]\}.
\]

The unit group is `+-1`, and conjugation fixes both undirected directions. Thus the two natural orbits are axial and transverse singleton orbits.

At `Delta=-4`, multiplication by the Gaussian unit `i` exchanges `[1]` and `[i]`, so they fuse.

### Odd discriminants

For

\[
\Delta\equiv1\pmod4,\qquad\Delta<-3,
\]

put

\[
F=\frac{1+\sqrt\Delta}{2},\qquad
\bar F=1-F,\qquad
q=F\bar F=\frac{1+|\Delta|}{4}>1.
\]

Then

\[
D_\Delta=\{[1],[F],[\bar F]\}.
\]

Again the generic unit group is `+-1`. Conjugation fixes `[1]` and exchanges `[F]` and `[\bar F]`. Hence

\[
\boxed{
A=\{[1]\},\qquad O=\{[F],[\bar F]\}.
}
\]

At `Delta=-3`, the Eisenstein unit group acts transitively on the three directions modulo sign, so all three fuse.

## Theorem 2.1 — orbit-fusion classification

For the HATTER direction set in an imaginary quadratic field,

\[
\boxed{
\#(D_\Delta/\Gamma_\Delta)=
\begin{cases}
1,&\Delta=-4,\\
1,&\Delta=-3,\\
2,&\text{otherwise}.
\end{cases}}
\]

The two fusion points are precisely the Gaussian and Eisenstein worlds, i.e. the imaginary-quadratic fields with extra roots of unity.

### Proof

The generic even and odd cases follow directly from the unit group `+-1` and the conjugation action described above. At `Delta=-4`, multiplication by `i` exchanges the two square-lattice directions. At `Delta=-3`, multiplication by an Eisenstein unit cycles the three hexagonal directions. No other imaginary-quadratic field has a larger unit group. ∎

## 2.2 Canonical norm-shell filtration and its limit

In every generic world, the rational direction has absolute norm one while the second orbit has absolute norm `q>1`. Therefore there is a canonical two-level norm-shell filtration

\[
\mathcal F_1\subsetneq\mathcal F_2=D_\Delta,
\]

where `F_1` consists of norm-one directions. At the Gaussian and Eisenstein fusion points every step direction already has norm one, so the filtration collapses.

This filtration is intrinsic, but it does **not** imply an activation order.

## Theorem 2.2 — no universal strongest-first activation law

In every generic imaginary-quadratic world there are arithmetic elements whose shortest HATTER representation uses only the outer norm shell while using zero capacity from the inner shell.

### Proof

In the generic even case take `alpha=mF`, `m>0`. Its shortest representation uses only transverse `F`-steps. In the generic odd case the same element `alpha=mF` has the unique geodesic triple `(0,m,0)` proved below. Hence in both cases outer-shell use can be positive while inner-shell use is zero. ∎

Thus

\[
\boxed{
\text{canonical orbit filtration exists, but universal sequential activation does not.}
}
\]

---

# 3. Generic-odd geodesics and the folded pair

From now on assume

\[
\Delta<-3,\qquad\Delta\equiv1\pmod4.
\]

Write

\[
\alpha=L+WF.
\]

## 3.1 Unique direction-labelled geodesic

Every representation by the three positive directions has the form

\[
\alpha=x+yF+z\bar F.
\]

Since `bar F=1-F`, comparison of coefficients gives

\[
L=x+z,\qquad W=y-z.
\]

Setting `t=z`, every integral representation is

\[
x=L-t,\qquad y=W+t,\qquad z=t.
\]

Its word length is

\[
f(t)=|L-t|+|W+t|+|t|.
\]

## Theorem 3.1 — median geodesic theorem

Let

\[
m=\operatorname{med}\{L,-W,0\}.
\]

Then `f(t)` has the unique minimizer `t=m`, and hence the unique minimal coefficient triple is

\[
\boxed{
g_\Delta(\alpha)=(L-m,W+m,m).}
\]

At least one of the three entries is zero.

### Proof

The function `f(t)` is the sum of distances from `t` to the three points `L,-W,0` on the real line. For an odd number of points the sum of absolute distances has its unique minimum at the median. Since the data are integral, the minimizing median is integral. Because the median is one of `L,-W,0`, one of `L-m`, `W+m`, `m` vanishes. ∎

## 3.2 Recovery of the published HATTER pair

Let the three integers `L,-W,0` be arranged increasingly and let their adjacent gaps be `u,v>=0`. The three pairwise distances are

\[
u,\quad v,\quad u+v,
\]

which are also

\[
|L|,\quad|W|,\quad|L+W|.
\]

The two nonzero absolute entries of the median geodesic are exactly the adjacent gaps `u,v`.

## Theorem 3.2 — geodesic folding theorem

If the published odd-discriminant HATTER interface is

\[
\Pi_\Delta(\alpha)=(P,Q),\qquad P\ge Q\ge0,
\]

then

\[
\boxed{
\operatorname{sort}_{\downarrow}\{|x|,|y|,|z|\}=(P,Q,0),
}
\]

where `(x,y,z)=g_Delta(alpha)`. In particular,

\[
\boxed{
P+Q=|x|+|y|+|z|=\max\{|L|,|W|,|L+W|\}.
}
\]

Thus `(P,Q)` is exactly the magnitude-sorted forgetting of the unique direction-labelled geodesic triple.

## 3.3 Intrinsic orbital signature

Define

\[
\boxed{
\Omega_\Delta(\alpha)=\bigl(|x|;\{|y|,|z|\}\bigr).
}
\]

The semicolon separates the axial orbit from the unordered conjugate oblique pair. Multiplication by `-1` changes no absolute count, and conjugation only exchanges `y,z`; therefore `Omega` is invariant under the natural sign/conjugation quotient.

For the network model below define the canonical orbit-total projection

\[
\boxed{
\Xi_\Delta(\alpha)=(A,O):=(|x|,|y|+|z|).
}
\]

It preserves total word capacity:

\[
A+O=P+Q.
\]

The projection `Omega -> Xi` intentionally forgets the internal split inside the oblique orbit. All exact network theorems in this paper refer to `Xi`, not to an unspecified richer `Omega`-network semantics.

---

# 4. Exact fibers of the forgetting map

## Theorem 4.1 — complete generic-odd fiber classification

For fixed folded data `P>=Q>=0`, the number of symmetry-distinct generic-odd orbital signatures is

\[
\boxed{
|F^{-1}(P,Q)|=
\begin{cases}
1,&P=Q=0,\\
2,&P>0,\ Q=0,\\
2,&P=Q>0,\\
3,&P>Q>0.
\end{cases}}
\]

For every strict interior pair `P>Q>0`, the three signatures are

\[
\boxed{
\Omega_I=(P;\{Q,0\}),\qquad
\Omega_{II}=(Q;\{P,0\}),\qquad
\Omega_{III}=(0;\{P,Q\}),
}
\]

with orbit-total images

\[
\boxed{
\Xi_I=(P,Q),\qquad
\Xi_{II}=(Q,P),\qquad
\Xi_{III}=(0,P+Q).
}
\]

### Proof

Theorem 3.1 shows that a shortest representation has at most two nonzero undirected direction counts. For `P>Q>0`, placing the two positive magnitudes among the axial slot and two oblique slots yields, modulo exchange of the oblique slots, exactly three possibilities: `P` axial, `Q` axial, or neither axial. All three occur, for example through suitable elements of the forms `P+QF`, `Q+PF`, and an element using the two oblique directions. No fourth orbit placement exists.

If `Q=0<P`, the single positive magnitude is either axial or oblique. If `P=Q>0`, the first two interior placements coincide because the positive magnitudes are equal, leaving two signatures. The zero state is unique. ∎

## 4.2 Norm resolves the static ambiguity

Let

\[
q=(1+|\Delta|)/4>1.
\]

For an interior pair `P>Q>0`, the three placements have norms

\[
N_I=P^2+PQ+qQ^2,
\]

\[
N_{II}=Q^2+PQ+qP^2,
\]

\[
N_{III}=q(P^2+Q^2)+(2q-1)PQ.
\]

Their differences are

\[
N_{II}-N_I=(q-1)(P^2-Q^2)>0,
\]

\[
N_{III}-N_{II}=(q-1)Q(Q+2P)>0.
\]

Hence

\[
N_I<N_{II}<N_{III}.
\]

This gives an important discipline statement: `(N_Delta,Pi_Delta)` already determines `Omega`. The orbital signature is a canonical **unfolding** of `(P,Q)`, not an independent static invariant once the multiplicative norm is also retained. Its new role below is operational: the network is allowed to see the orbit placement before the fold discards it.

---

# 5. Exact orbit-total network response

## 5.1 Fixed-host response

Let `H=(V,E)` be a connected simple graph on `n` vertices. Put the same orbit-total state

\[
\Xi=(A,O),\qquad A,O\in\mathbb N_0
\]

at every vertex.

A feasible network is a connected spanning subgraph of `H` whose used edges are typed axial or oblique. At each vertex the axial degree is at most `A`, the oblique degree is at most `O`, and each host edge is used at most once in total.

If `e_A,e_O` are the two edge counts, define the remaining boundary

\[
\boxed{
B_A=nA-2e_A,\qquad B_O=nO-2e_O.
}
\]

Let `R_H^Xi(A,O)` be the set of Pareto-minimal feasible boundary vectors, and encode it by

\[
\boxed{
Z_H^{\Xi}(A,O;X,Y)
=\sum_{(B_A,B_O)\in\mathcal R_H^{\Xi}(A,O)}X^{B_A}Y^{B_O}.
}
\]

For a geometry class `C` at order `n`, define

\[
\mathcal R_{C,n}^{\Xi}(A,O)
=\operatorname{ParetoMin}
\left(
\bigcup_{H\in\mathcal C_n}\mathcal R_H^{\Xi}(A,O)
\right),
\]

where `C_n` denotes the connected simple hosts in that class.

## 5.2 Two-node microscope

On the unique connected two-vertex host there is exactly one edge.

## Proposition 5.1 — exact two-node response

\[
\boxed{
\mathcal R_2^{\Xi}(A,O)=
\begin{cases}
\{(2A-2,2O),(2A,2O-2)\},&A>0,\ O>0,\\
\{(2A-2,0)\},&A>0,\ O=0,\\
\{(0,2O-2)\},&A=0,\ O>0,\\
\varnothing,&A=O=0.
\end{cases}}
\]

### Proof

Connectivity forces the unique host edge to be present. If both channels are available, typing that edge axial or oblique gives the two displayed incomparable vectors. If only one channel is available, the edge type is forced. ∎

## Theorem 5.2 — operational visibility of every interior fiber

For every `P>Q>0`, the three two-node responses of

\[
(P,Q),\qquad(Q,P),\qquad(0,P+Q)
\]

are pairwise distinct.

### Proof

The pure state has a singleton response, whereas each mixed state has two Pareto points. The minimum first coordinate of the two mixed responses is respectively `2P-2` and `2Q-2`; these differ because `P>Q`. ∎

Thus the folded pair loses information that a network can detect immediately.

---

# 6. Strict one-dimensional memory

For strict one-dimensional geometry the connected host on `n=2m` vertices is the path `P_{2m}`.

Suppose exactly `r` path edges are axial. Then

\[
B_A=2mA-2r,
\]

\[
B_O=2mO-2(2m-1-r).
\]

A capacity at least two imposes no additional restriction on a path. A capacity-one channel must occupy a matching, and the maximum matching size of `P_{2m}` is `m`.

Define

\[
r_{\max}(A)=
\begin{cases}
0,&A=0,\\
m,&A=1,\\
2m-1,&A\ge2,
\end{cases}
\]

and

\[
r_{\min}(O)=
\begin{cases}
2m-1,&O=0,\\
m-1,&O=1,\\
0,&O\ge2.
\end{cases}
\]

## Theorem 6.1 — exact path polynomial

For every feasible uniform state `(A,O)`,

\[
\boxed{
Z_{P,2m}^{\Xi}(A,O;X,Y)
=
\sum_{r=r_{\min}(O)}^{r_{\max}(A)}
X^{2mA-2r}Y^{2mO-2(2m-1-r)}.
}
\]

### Proof

Every integer `r` in the displayed interval is realizable: if a channel has capacity one, choose a matching of the required size; otherwise no adjacency restriction is imposed. Every realized point has the same total boundary

\[
2m(A+O)-2(2m-1),
\]

so distinct realized points are incomparable and the attainable set is already Pareto-minimal. ∎

## Corollary 6.2 — permanent interior memory in 1D

For every `P>Q>0` and every even path size,

\[
\boxed{
Z_I^{1D}\ne Z_{II}^{1D},\qquad
Z_I^{1D}\ne Z_{III}^{1D},\qquad
Z_{II}^{1D}\ne Z_{III}^{1D}.
}
\]

Hence strict one dimension has the memory law

\[
\boxed{3\to3\to3\to\cdots.}
\]

### Proof

If `Q>=2`, both mixed states permit all edge counts, but their maximal axial exponents are `2mP` and `2mQ`. If `Q=1`, the small channel is matching-limited and the two intervals are swapped asymmetrically; their maximal axial exponents again differ. The pure state has only one channel and therefore a singleton response. ∎

---

# 7. Complete outerplanar classification

Throughout this section `n=2m>=4`.

## 7.1 Two extremal outerplanar hosts

We use two explicit families.

First, let `G_m` be the outer cycle `C_{2m}` together with the nested chords

\[
\{j,2m-j\},\qquad1\le j\le m-1.
\]

Then `G_m` is outerplanar, has `3m-1` edges, two vertices of degree two, and all other vertices of degree three.

Second, let `H_n` have vertices `1,...,n` and edges

\[
\{i,i+1\},\quad1\le i\le n-1,
\]

and

\[
\{i,i+2\},\quad1\le i\le n-2.
\]

It is a chain of triangles, hence maximal outerplanar, has `2n-3` edges, and satisfies

\[
\Delta(H_n)\le4.
\]

Every outerplanar graph has at least two vertices of degree at most two; this follows by augmenting to a maximal outerplanar graph and using the two-ear property of polygon triangulations.

## 7.2 Exact pure-channel boundary

Define

\[
\psi_n(S)=
\begin{cases}
2,&S=3,\\
n(S-4)+6,&S\ge4.
\end{cases}
\]

## Proposition 7.1 — exact pure-oblique outerplanar response

For every `S>=3`,

\[
\boxed{
Z_{O,n}^{\Xi}(0,S;X,Y)=Y^{\psi_n(S)}.
}
\]

### Proof

For `S=3`, the two unavoidable vertices of degree at most two leave at least two unused ports in total. The graph `G_m`, with degree sequence `2,3,...,3,2`, attains boundary two.

For `S>=4`, the outerplanar edge bound gives

\[
B_O\ge nS-2(2n-3)=n(S-4)+6.
\]

The maximal graph `H_n` has `2n-3` edges and maximum degree at most four, so coloring all its edges oblique is feasible and attains equality. ∎

## 7.3 Exact single-channel floor

For `A>=3`, define

\[
\phi_n(A)=
\begin{cases}
2,&A=3,\\
n(A-4)+6,&A\ge4.
\end{cases}
\]

## Proposition 7.2 — exact outerplanar axial floor

For every second-channel capacity `O>=0` and every `A>=3`, the minimum feasible axial boundary is

\[
\boxed{\mu_{O,n}(A,O)=\phi_n(A).}
\]

### Proof

If `A=3`, the two vertices of total degree at most two force at least one unused axial port each, hence `B_A>=2`. Coloring all edges of `G_m` axial attains equality.

If `A>=4`, the axial subgraph is outerplanar and hence has at most `2n-3` edges. Therefore

\[
B_A\ge nA-2(2n-3)=n(A-4)+6.
\]

Color every edge of `H_n` axial. Since `Delta(H_n)<=4`, this is feasible and attains the lower bound. ∎

The function `phi_n` is strictly increasing on integers `A>=3`.

## 7.4 The exceptional `(2,1)` fiber

For the fiber `(P,Q)=(2,1)`, the three states are

\[
(2,1),\qquad(1,2),\qquad(0,3).
\]

The graph `G_m` admits two exact colorings. Coloring the outer cycle by the capacity-two channel and the nested chords by the capacity-one channel gives one boundary endpoint; coloring an alternating perfect matching by the capacity-one channel and the connected complement by the capacity-two channel gives the other.

## Proposition 7.3 — exact `(2,1)` outerplanar response

For every `m>=2`,

\[
\boxed{
Z_{O,2m}^{\Xi}(2,1)=Z_{O,2m}^{\Xi}(1,2)=X^2+Y^2,
}
\]

while

\[
\boxed{
Z_{O,2m}^{\Xi}(0,3)=Y^2.
}
\]

### Proof

Every outerplanar total-capacity-three realization has total free boundary at least two, by the two low-degree vertices. Both even boundary allocations of total two, `(0,2)` and `(2,0)`, are attained by the two colorings just described for each mixed state. They therefore form the complete mixed Pareto front. The pure state attains `(0,2)` on `G_m`, and no smaller total boundary is possible. ∎

## 7.5 Rank-swap separation for every other interior fiber

Take `P>Q>0`.

### Low `Q`: `Q=1,2`

If `P>=3`, the state `(P,Q)` has positive axial boundary in every outerplanar realization because a channel of capacity `P>=3` cannot be saturated at both unavoidable low-degree vertices.

For the swapped state `(Q,P)`, the axial channel can be saturated:

- for `Q=1`, use the perfect matching
  \[
  \{\{1,2\},\{3,4\},...,\{n-1,n\}\}
  \]
  inside `H_n`;
- for `Q=2`, use the Hamiltonian cycle
  \[
  1,2,4,6,...,n,n-1,n-3,...,3,1,
  \]
  whose consecutive labels differ by one or two and hence are edges of `H_n`.

The complements have maximum degree at most three and two, respectively, and are therefore feasible in the capacity-`P` channel. Thus the swapped response contains a Pareto point with `B_A=0`, while the unswapped response does not.

### High `Q`: `Q>=3`

By Proposition 7.2 the minimum axial exponents of the two response polynomials are

\[
\phi_n(P),\qquad\phi_n(Q).
\]

Since `P>Q>=3` and `phi_n` is strictly increasing, these minima differ.

Therefore:

## Theorem 7.4 — complete outerplanar rank-swap classification

For every `P>Q>0` and even `n>=4`,

\[
\boxed{
Z_{O,n}^{\Xi}(P,Q)=Z_{O,n}^{\Xi}(Q,P)
\iff
(P,Q)=(2,1).
}
\]

## 7.6 Mixed states never collide with the pure state

### Type I versus pure

If `P>=3`, Proposition 7.2 gives a positive minimum axial exponent for `Z(P,Q)`, while the pure state is a single monomial with zero axial exponent. The only remaining interior pair with `P<3` is `(2,1)`, where Proposition 7.3 gives `X^2+Y^2` versus `Y^2`.

Hence Type I never equals the pure state.

### Type II versus pure

If `Q>=3`, Proposition 7.2 again gives positive minimum axial exponent for the swapped mixed state, excluding equality with the pure monomial.

Suppose `Q=1` or `2`. Apart from `(2,1)`, we have `P>=3`. The oblique channel of `(Q,P)` has capacity `P`, so among Pareto points its minimum oblique exponent is `phi_n(P)`. The pure state has the unique oblique exponent `psi_n(P+Q)`.

If `P=3`, then `phi_n(P)=2`, whereas `psi_n(4)=6` and `psi_n(5)=n+6`. If `P>=4`,

\[
\psi_n(P+Q)-\phi_n(P)=nQ>0.
\]

Thus equality is impossible. The special `(2,1)` case was already separated in Proposition 7.3.

We have proved:

## Theorem 7.5 — complete outerplanar interior-fiber law

For every generic-odd interior fiber `P>Q>0` and every even outerplanar host size `n>=4`, let

\[
\nu_{O,n}^{\Xi}(P,Q)
=
\left|
\left\{
Z_{O,n}^{\Xi}(P,Q),
Z_{O,n}^{\Xi}(Q,P),
Z_{O,n}^{\Xi}(0,P+Q)
\right\}
\right|.
\]

Then

\[
\boxed{
\nu_{O,n}^{\Xi}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}.
\end{cases}}
\]

The only loss is the exceptional mixed rank swap `(2,1)\leftrightarrow(1,2)`.

---

# 8. Regular factorizable hosts

We now identify the common mechanism behind the dense-host transition.

Let `H` be a connected simple `d`-regular graph on an even number `n` of vertices. Assume that

\[
\boxed{E(H)=M_1\sqcup\cdots\sqcup M_d}
\]

is a 1-factorization.

## Lemma 8.1 — exact degree-window interpolation

Let `0<=l<=u<=d`. For every integer `e` with

\[
\boxed{\frac{nl}{2}\le e\le\frac{nu}{2},}
\]

there is a spanning subgraph `F` of `H` with exactly `e` edges and

\[
l\le d_F(v)\le u
\]

for every vertex.

### Proof

Write

\[
e=\frac n2q+r,\qquad0\le r<\frac n2.
\]

Take `q` complete 1-factors and, if `r>0`, add any `r` edges of the next factor. Every vertex has degree `q` or `q+1`, and the endpoint inequalities place both values in `[l,u]`. ∎

The interpolating subgraph itself need not be connected. In the next theorem it is only one channel; the union of both channels will be the full connected host.

## Theorem 8.2 — exact regular-factorizable response

Let every vertex have uniform capacities `(A,O)` and suppose

\[
S=A+O\ge d.
\]

Define

\[
D=n(S-d),
\]

\[
L_A=n(A-d)_+,\qquad L_O=n(O-d)_+.
\]

Then

\[
\boxed{
\mathcal R_H^{\Xi}(A,O)
=
\left\{
(B_A,B_O):
\begin{array}{l}
B_A+B_O=D,\\
L_A\le B_A\le D-L_O,\\
B_A\equiv0\pmod2
\end{array}
\right\}.
}
\]

Equivalently,

\[
\boxed{
Z_H^{\Xi}(A,O;X,Y)
=
\sum_{\substack{b=L_A\\b\equiv0\ (2)}}^{D-L_O}
X^bY^{D-b}.
}
\]

Consequently, within the stated host class and regime, the response depends on `H` only through `(n,d)`.

### Proof

Every feasible network uses at most `nd/2` host edges, so

\[
B_A+B_O=nS-2(e_A+e_O)\ge nS-nd=D.
\]

Likewise

\[
e_A\le\min(nd/2,nA/2)
\]

gives

\[
B_A\ge n(A-d)_+=L_A,
\]

and similarly `B_O>=L_O`.

We now realize every parity-compatible point on the line `B_A+B_O=D` by using **all** edges of `H`. Let `F` be the axial subgraph and type the complement `H\setminus F` oblique. The local constraints are exactly

\[
(d-O)_+\le d_F(v)\le\min(A,d).
\]

Since `A+O>=d`, the interval is nonempty. Lemma 8.1 realizes every axial edge count between its two endpoint values. Translating by `B_A=nA-2e_A` gives exactly the displayed even-step interval. The union of the channels is `H`, so the network is connected.

It remains to exclude Pareto points above the line. Let `(B_A,B_O)` be any feasible point with sum greater than `D`. Its coordinates satisfy `B_A>=L_A`, `B_O>=L_O`. Consider

\[
I=
\left[
\max(L_A,D-B_O),
\min(B_A,D-L_O)
\right].
\]

The lower endpoint does not exceed the upper endpoint because of the coordinate lower bounds and the inequality `B_A+B_O>=D`. All quantities have even parity. Choose an even `b` in `I`. The already realized point `(b,D-b)` is coordinatewise no larger than `(B_A,B_O)`, so the latter is not Pareto-minimal. ∎

## 8.3 Orbital-memory filtration

Fix an interior fiber

\[
P>Q>0,\qquad S=P+Q,
\]

and assume `d<=S`.

## Theorem 8.3 — degree-controlled orbital-port filtration

For every connected even-order `d`-regular 1-factorizable host,

\[
\boxed{
\nu_H^{\Xi}(P,Q)=
\begin{cases}
3,&d<P,\\
2,&P\le d<S,\\
1,&d=S.
\end{cases}}
\]

### Proof

The mixed states have the same total-boundary line. Their lower axial endpoints are

\[
n(P-d)_+,\qquad n(Q-d)_+.
\]

Because `P>Q`, they are unequal exactly when `d<P`. Hence the mixed states are separate for `d<P` and coincide for `d>=P` within the regime `d<=S`.

For `d<S`, the pure-oblique state has the singleton response

\[
\{(0,n(S-d))\}.
\]

If `d<P`, one mixed state has positive minimum axial boundary; the other either does too or contains a nontrivial segment with positive axial values, so neither can equal the pure singleton. If `P<=d<S`, both mixed responses are the full nontrivial even-step segment on the line `B_A+B_O=n(S-d)`, whereas the pure response is only its endpoint with `B_A=0`. Finally, at `d=S`, the lower-total boundary is zero and all three responses equal `{(0,0)}`. ∎

Thus

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
}
\]

The first threshold forgets which orbit-total channel carries the larger folded magnitude. The second forgets the remaining mixed-versus-pure placement.

## 8.4 Hostile boundary: the underfull regime

When `S<d`, 1-factorizability alone does **not** imply zero boundary, because the union of an arbitrary selected set of `S` perfect matchings can be disconnected.

A sufficient condition is immediate.

## Proposition 8.4 — connected-factor closure criterion

If `S<d` and `H` contains a connected spanning union `J` of `S` 1-factors from the chosen factorization, then any partition of those `S` factors into `A` axial and `O` oblique factors, `A+O=S`, yields

\[
\mathcal R_H^{\Xi}(A,O)=\{(0,0)\}.
\]

No converse is claimed.

This is the precise point where topology can re-enter after `(n,d)` universality ends.

---

# 9. Exact planar lifts

## 9.1 Even regular planar triangulations

A simple planar triangulation on `n` vertices has `3n-6` edges. If it is `d`-regular,

\[
nd=6n-12,
\]

so

\[
d=6-\frac{12}{n}.
\]

For even `n>=4`, integrality leaves exactly

\[
\boxed{(n,d)=(4,3),(6,4),(12,5).}
\]

These are the tetrahedron `K_4`, the octahedral graph, and the icosahedral graph. Each is connected and 1-factorizable; explicit factorizations are recorded in Appendix A.

Because each is a planar triangulation, it attains the global planar edge ceiling at its order. Therefore the lower-total-boundary bound used in Theorem 8.2 is not merely a fixed-host bound: it is the geometry-class bound.

## Corollary 9.1 — exact Platonic planar response

Let

\[
(n,d)\in\{(4,3),(6,4),(12,5)\}
\]

and let `A+O>=d`. The exact planar geometry-class Pareto front at order `n` is precisely the front in Theorem 8.2.

For an interior fiber `P>Q>0`, `S=P+Q>=d`,

\[
\boxed{
\nu_{Pl,n}^{\Xi}(P,Q)=
\begin{cases}
1,&S=d,\\
2,&S>d\text{ and }P\le d,\\
3,&S>d\text{ and }P>d.
\end{cases}}
\]

## 9.2 Exact planar scale trajectory

For the fiber

\[
(P,Q)=(4,1),
\]

the three Platonic orders give

\[
\boxed{
\nu_{Pl,4}^{\Xi}=3,\qquad
\nu_{Pl,6}^{\Xi}=2,\qquad
\nu_{Pl,12}^{\Xi}=1.
}
\]

Hence the explicit planar scale sequence

\[
4\to6\to12
\]

realizes

\[
\boxed{3\to2\to1.}
\]

This is not asserted to be monotone through every intermediate order. It is an exact three-scale witness.

## 9.3 Why this does not solve all planar hosts

For larger planar orders a triangulation cannot be 6-regular: the average degree remains strictly below six. Local overload and repair therefore matter. The research branch contains a substantial separate programme for the Gaussian state `(6,5)`, including exact larger-order fronts and unresolved order-46 cases. Those theorems are not dependencies of the present publication spine and are not imported into the main claim.

---

# 10. Observation protocols are separate filters

The full Pareto response and a restricted search protocol need not induce the same collision relation.

For example, an explicitly chosen maximal-first probe prioritizes the currently larger orbit-total capacity. On complete hosts, such a restricted trace can identify a different pair of orbital states than the full Pareto optimization identifies in the same host-degree regime.

Therefore

\[
\boxed{
\text{probe-induced forgetting need not equal model-induced forgetting.}
}
\]

This is why Theorem 2.2 matters conceptually: a priority convention may be useful experimentally, but it is not licensed as an intrinsic arithmetic activation law.

---

# 11. Discussion

## 11.1 A two-stage loss after the arithmetic fold

For a strict interior generic-odd pair, the arithmetic fold already maps three intrinsic placements to the same `(P,Q)`. An orbit-aware network can recover that lost placement on sparse hosts. As the regular incidence budget grows, the network itself performs a second compression:

\[
3\to2\to1.
\]

The two thresholds have different meanings. At `d=P`, the network can absorb either rank placement of the two positive capacities and therefore forgets the mixed rank swap. At `d=P+Q`, it can absorb the entire local capacity and forgets the distinction between mixed and pure-oblique placement.

## 11.2 Geometry protects memory

Host size alone does not force forgetting. A path can grow indefinitely while preserving all three orbital responses because its local incidence ceiling stays two. Outerplanar geometry permits more edges but has unavoidable low-degree vertices, leaving almost every interior fiber visible. Regular factorizable hosts expose a clean local-degree filtration.

Thus the relevant scale is not simply the number of vertices. It is the incidence budget that can be supplied coherently at every vertex.

## 11.3 Degree universality and its boundary

In Theorem 8.2, once `S>=d`, a 1-factorization supplies every degree window needed on the full connected host. The exact uniform `Xi` response is therefore blind to further topology at fixed `(n,d)`.

The underfull regime `S<d` is different: one no longer uses the full host, so connectivity of the selected spanning factor becomes a new topological condition. This gives a sharp conceptual boundary rather than an unqualified claim of topology independence.

## 11.4 What is not proved

This paper does not prove:

- a strongest-first arithmetic activation law;
- a complete network semantics retaining every component of `Omega=(a;{b,c})`;
- a full planar classification for all orders and capacities;
- a genus/topology theorem;
- fixed-host universality for arbitrary regular graphs without the stated factorization hypothesis;
- automatic underfull closure from 1-factorizability alone;
- novelty of classical graph-factor or matching theory.

---

# 12. Conclusion

The magnitude-sorted pair `(P,Q)` can hide canonical arithmetic direction placement. In generic odd imaginary-quadratic worlds, a strict interior pair is the image of exactly three intrinsic orbital states. Their orbit-total network images are

\[
(P,Q),\qquad(Q,P),\qquad(0,P+Q).
\]

They are operationally distinct on the smallest connected host. Geometry then determines how much of this information survives optimization.

Strict one dimension preserves all three at every scale. Outerplanar geometry has exactly one interior mixed collision, `(2,1)`, and never merges a mixed state with the pure state. Connected regular 1-factorizable hosts in the critical/overfull regime obey the exact degree law

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
}
\]

The resulting picture is not a hierarchy of stronger and weaker arithmetic ports. It is a hierarchy of **observable arithmetic memory**.

---

# Appendix A. Explicit Platonic 1-factorizations

This appendix records concrete decompositions needed for the planar lift.

## A.1 Tetrahedron

For `K_4` on vertices `1,2,3,4`, take

\[
M_1=\{12,34\},\qquad
M_2=\{13,24\},\qquad
M_3=\{14,23\}.
\]

Then

\[
E(K_4)=M_1\sqcup M_2\sqcup M_3.
\]

## A.2 Octahedron

Write the octahedral graph as

\[
\mathcal O_6=K_6-M_0,
\]

where `M_0` is one perfect matching. Choose any 1-factorization of `K_6` containing `M_0`; deleting `M_0` leaves four pairwise disjoint perfect matchings whose union is `E(O_6)`.

## A.3 Icosahedron

Use vertices

\[
N,S,u_0,\ldots,u_4,v_0,\ldots,v_4
\]

with indices modulo five and edge families

\[
N-u_i,\quad S-v_i,\quad u_i-u_{i+1},\quad v_i-v_{i+1},\quad u_i-v_i,\quad u_i-v_{i-1}.
\]

The following five perfect matchings are pairwise edge-disjoint:

\[
\begin{aligned}
M_0={}&\{N-u_1,S-v_0,u_0-u_4,u_2-v_1,u_3-v_2,v_3-v_4\},\\
M_1={}&\{N-u_4,S-v_2,u_0-v_4,u_1-u_2,u_3-v_3,v_0-v_1\},\\
M_2={}&\{N-u_0,S-v_1,u_1-v_0,u_2-u_3,u_4-v_4,v_2-v_3\},\\
M_3={}&\{N-u_3,S-v_4,u_0-v_0,u_1-v_1,u_2-v_2,u_4-v_3\},\\
M_4={}&\{N-u_2,S-v_3,u_0-u_1,u_3-u_4,v_0-v_4,v_1-v_2\}.
\end{aligned}
\]

Each matching has six edges. Their union therefore has thirty edges, equal to the full icosahedral edge count, so

\[
E(\mathcal I_{12})=M_0\sqcup\cdots\sqcup M_4.
\]

---

# Appendix B. Claim and dependency discipline

The main publication dependencies are:

1. orbit action on the HATTER direction set;
2. median geodesic theorem;
3. forgetting-fiber classification;
4. exact `Xi` network definition;
5. path theorem;
6. complete outerplanar theorem;
7. regular-factorizable response theorem;
8. planar extremality of the three Platonic triangulations.

The following research layers are intentionally **not** dependencies of the present paper:

- large-order Gaussian `(6,5)` planar repair programme;
- prime-61 world spectrum and tomography;
- residue-tail collision programme;
- torus observability seed;
- any future genus or surface classification.

This separation is intentional: it keeps HATTER-SOL-11 falsifiable and prevents an open side problem from contaminating the central result.

---

# References

## Previous HATTER-SOL papers

[H07] Malachevsky, A.A. **HATTER-SOL-07 · Free-Port Factorization / Alice in the Land of Free Threads: Factors as Nodes and the Cost of Organization.** HATTER-SOL series, 2026. Repository publication record: `papers/HATTER-SOL/07-FREE-PORT-FACTORIZATION/`.

[H08] Malachevsky, A.A. **HATTER-SOL-08 · Dimensional Factor Architectures.** HATTER-SOL series, 2026. Repository publication record: `papers/HATTER-SOL/08-DIMENSIONAL-FACTOR-ARCHITECTURES/`.

[H09] Malachevsky, A.A. **World-Dependent Factor Networks and a Prime-Toggle Response Operator.** HATTER-SOL-09, 2026. Repository publication record: `papers/HATTER-SOL/09-WORLD-INTERFACE-OPERATORS/`.

[H10] Malachevsky, A.A. **Ideal Factor Networks Beyond Unique Element Factorization: Minimal Principalization Witnesses, Residue Fibers, and Witness-State Phase Transitions.** HATTER-SOL-10, 2026. Repository publication record: `papers/HATTER-SOL/10-IDEAL-FACTOR-NETWORKS/`.

## Classical and adjacent graph literature

[1] W. T. Tutte, **The Factorization of Linear Graphs**, *Journal of the London Mathematical Society* 22 (1947), 107--111.

[2] Pavol Hell and David G. Kirkpatrick, **Algorithms for Degree Constrained Graph Factors of Minimum Deficiency**, *Journal of Algorithms* 14(1) (1993), 115--138. DOI: `10.1006/jagm.1993.1006`.

[3] Xiao Zhou and Takao Nishizeki, **Decompositions to Degree-Constrained Subgraphs Are Simply Reducible to Edge-Colorings**, *Journal of Combinatorial Theory, Series B* 75(2) (1999), 270--287. DOI: `10.1006/jctb.1998.1883`.

[4] Jin Akiyama and Mikio Kano, **[a,b]-Factorizations**, in *Factors and Factorizations of Graphs: Proof Techniques in Factor Theory*, Lecture Notes in Mathematics 2031, Springer (2011), 193--218. DOI: `10.1007/978-3-642-21919-1_5`.

[5] Richard C. Brewster, Sean McGuinness, and Morten Hegner Nielsen, **Factors with Multiple Degree Constraints in Graphs**, *SIAM Journal on Discrete Mathematics* 27(4) (2013), 1734--1747. DOI: `10.1137/110850402`.

[6] A. G. Chetwynd and A. J. W. Hilton, **Regular Graphs of High Degree are 1-Factorizable**, *Proceedings of the London Mathematical Society* s3-50(2) (1985), 193--206. DOI: `10.1112/plms/s3-50.2.193`.

[7] Shmuel Onn, **On degree sequence optimization**, *Operations Research Letters* 48(6) (2020), 840--843. DOI: `10.1016/j.orl.2020.10.010`.

[8] Mariia Anapolska, Christina Buesing, Martin Comis, and Tabea Krabs, **Minimum color-degree perfect b-matchings**, *Networks* 77(4) (2021), 477--494. DOI: `10.1002/net.21974`.

---

## Publication status after v0.2

The theorem spine is complete in manuscript form. Remaining gates before v0.9/PDF are editorial and audit gates rather than new theorem obligations:

1. verify the final DOI/version metadata for HATTER-SOL-07--10;
2. perform a line-by-line hostile audit of every displayed theorem against the source theorem files;
3. check theorem numbering, notation, parity conventions, and geometry-class versus fixed-host scope;
4. perform one more specialized literature search for equivalent arithmetic direction-orbit interface constructions;
5. only then freeze EN v0.9, prepare RU v0.9, and run the mandatory publication audit.
