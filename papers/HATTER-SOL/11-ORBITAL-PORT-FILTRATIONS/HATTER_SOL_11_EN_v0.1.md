# HATTER-SOL-11

# Orbital Port Filtrations: How Network Geometry Forgets Arithmetic Direction Data

**Malachevsky, A.A.**  
ORCID: 0009-0008-6009-3196

**Manuscript status:** EN v0.1 — theorem-spine draft for hostile audit.  
**Series:** HATTER-SOL-11.  
**Date:** 2026-09-14.

---

## Abstract

Typed arithmetic-network models compress local arithmetic data into a small interface before global optimization. This raises a basic information question: which distinctions are already lost by the local interface, and which of the remaining distinctions are later erased by network geometry and host scale?

We study this question for the direction structure underlying the folded HATTER interface `(P,Q)` in the imaginary-quadratic setting developed in HATTER-SOL-09 and HATTER-SOL-10. In the generic odd case, the natural symmetry action separates one axial direction orbit from an unordered oblique pair. This gives an intrinsic orbital datum `Omega`, and the usual magnitude-sorted pair `(P,Q)` is a genuine forgetting map rather than a complete local invariant. For every strict interior pair `P>Q>0`, we classify its fiber exactly: there are three canonical orbital placements, whose orbit-total network states are `(P,Q)`, `(Q,P)`, and `(0,P+Q)`.

The three states need not have the same network response. We define their exact connected two-channel Pareto response and prove geometry-dependent memory laws. On every even path, all three states remain distinguishable at every scale. In the outerplanar class, all three remain distinguishable except for the unique mixed rank-swap collision `(2,1) <-> (1,2)`. By contrast, on connected even-order `d`-regular 1-factorizable hosts in the critical/overfull regime, the full Pareto response is determined only by the order, degree, and two channel capacities. For an interior fiber this yields the sharp orbital-memory filtration

\[
3\quad(d<P),
\qquad
2\quad(P\le d<P+Q),
\qquad
1\quad(d=P+Q).
\]

Thus the folded interface forgets arithmetic direction placement statically, while network architecture supplies a second, operational filtration on the visibility of that lost information. The result is not a strongest-first activation law: we prove separately that no universal sequential activation order follows from the arithmetic symmetry data. All exact geometry theorems in the main text are stated for the canonical orbit-total quotient `Xi`; no complete planar classification or richer full-orbital network classification is claimed.

---

## 1. Introduction

### 1.1 From typed arithmetic interfaces to information loss

HATTER-SOL-09 introduced arithmetic-world-dependent factor interfaces and typed factor networks. In the Gaussian and Eisenstein laboratories, a factor could be represented by a folded pair

\[
\Pi(\alpha)=(P,Q),
\qquad
P\ge Q\ge0,
\]

and global network optimization was performed subject to the corresponding typed local capacities. HATTER-SOL-10 then removed the unique-element-factorization restriction by passing to prime ideals and minimal principalization witnesses. That extension introduced a second source of multistate behavior: even in a fixed arithmetic world, a nonprincipal ideal can possess several minimal witness states and can undergo host-size-dependent phase changes.

Both constructions leave open a more local question. The pair `(P,Q)` records two nonnegative magnitudes, sorted by size. But sorting can destroy where those magnitudes came from. If the arithmetic lattice has more than one natural direction orbit, then two witnesses may have the same folded pair while placing the same magnitudes in different symmetry orbits.

The present paper asks whether that missing direction information is mathematically canonical and, if so, whether a network can still detect it.

The resulting architecture is

\[
\boxed{
\Omega
\longrightarrow
\Xi
\longrightarrow
(P,Q)
\longrightarrow
Z_{\mathcal C,n}.
}
\]

Here:

- `Omega` denotes intrinsic direction-orbit data;
- `Xi` is an orbit-total two-channel quotient used for the exact network theorems;
- `(P,Q)` is the previously published magnitude-sorted interface;
- `Z_{C,n}` is the exact Pareto response polynomial for a chosen geometry class or fixed host.

The maps are not interchangeable. Each discards a different kind of information.

### 1.2 The first hostile test: does the larger coordinate come first?

A tempting interpretation is that `P>=Q` expresses a hierarchy: the `P`-orbit is intrinsically stronger, should be used first, and the `Q`-orbit becomes active only after the first one is saturated.

That interpretation is false in the general arithmetic setting treated here. The natural symmetry action can distinguish direction orbits, but it does not supply a universal sequential activation rule. In particular, admissible shortest representations exist whose use lies entirely in the nominally outer shell while the inner shell has zero usage.

This distinction is essential. Later we will obtain a sharp filtration with thresholds at `P` and `P+Q`, but those thresholds arise from **network response** as host degree increases. They do not prove that arithmetic ports activate sequentially.

Accordingly, throughout the paper

\[
\boxed{
\text{orbital order is structural; strongest-first order is not assumed.}
}
\]

A maximal-first construction may still be used as an explicitly chosen experimental probe, but it is not the model axiom.

### 1.3 Main results

The paper establishes four layers.

First, in the generic odd imaginary-quadratic case, the primitive shortest directions split into a natural axial orbit and an oblique orbit represented by an unordered pair. The Gaussian and Eisenstein worlds are the two symmetry-fusion exceptions relevant to this construction.

Second, the folding map to `(P,Q)` has an exact finite fiber. For every strict interior pair

\[
P>Q>0,
\]

the three canonical orbital placements are

\[
(P;\{Q,0\}),
\qquad
(Q;\{P,0\}),
\qquad
(0;\{P,Q\}).
\]

Their orbit-total images are

\[
(P,Q),
\qquad
(Q,P),
\qquad
(0,P+Q).
\]

Third, those three states can remain distinct after network optimization. Geometry controls how much of the orbital fiber survives:

- strict one dimension preserves all three states at every even host scale;
- outerplanar geometry preserves all three except for the unique mixed collision `(2,1) <-> (1,2)`;
- dense regular factorizable hosts erase the information in two sharp stages.

Fourth, for every connected even-order `d`-regular 1-factorizable host `H`, we compute the exact fixed-host Pareto response in the regime where total local capacity is at least `d`. The result depends on the host only through `(n,d)`. For an interior orbital fiber, the number of distinct response classes is exactly

\[
\boxed{
\nu_H(P,Q)=
\begin{cases}
3,&d<P,\\
2,&P\le d<P+Q,\\
1,&d=P+Q.
\end{cases}}
\]

This is the main orbital-port filtration theorem.

### 1.4 Scope

The main network theorems are exact for the canonical orbit-total state `Xi`. The richer orbital datum `Omega` may contain additional information, and no claim is made that every network semantics retaining all of `Omega` has the same collision classes.

Likewise, the regular-factorizable theorem is a fixed-host theorem. It becomes an exact theorem for a whole geometry class only when an independent extremality argument shows that the chosen host attains the relevant geometry-class edge bound. We apply this lift to complete hosts in unrestricted simple-support geometry and to the tetrahedral, octahedral, and icosahedral planar hosts at their orders.

No complete planar classification is claimed. A substantial larger-order planar programme exists in the research record, but it is not required for the central theorem proved here.

---

## 2. Direction orbits and the failure of a universal activation hierarchy

### 2.1 Intrinsic direction data

Consider the imaginary-quadratic lattice model used in the preceding HATTER papers. In the generic odd case, a shortest geodesic representation can be encoded by three nonnegative usage counts associated with the three undirected primitive step directions of the relevant lattice chart.

The natural arithmetic symmetry does not treat all three coordinates as independently labeled. Instead, one direction forms an axial orbit and the remaining two directions form one oblique orbit under the stabilizing symmetry. It is therefore natural to write the orbital datum as

\[
\boxed{
\Omega=(a;\{b,c\}),
}
\]

where the semicolon separates the axial orbit from the unordered oblique pair.

The unordered braces are structural: exchanging the two oblique representatives does not change the orbital state.

### 2.2 Orbit fusion exceptions

In the generic imaginary-quadratic worlds, the axial and oblique direction classes remain distinct under the natural symmetry action. The Gaussian and Eisenstein lattices possess larger unit symmetry groups, and those extra symmetries fuse direction classes that remain separate generically.

We therefore distinguish two regimes:

1. **generic orbital regime**, where the axial/oblique distinction is intrinsic;
2. **fusion regime**, represented by the Gaussian and Eisenstein cases, where the stronger symmetry identifies the corresponding direction classes.

This paper's nontrivial forgetting fibers occur in the generic orbital regime.

### 2.3 No-go theorem for strongest-first activation

One might try to order direction orbits by norm shell and infer a sequential usage rule. Such a shell order can be defined, but it does not imply universal activation.

**Proposition 2.1 (no universal strongest-first law).**  
In the generic orbital regime there exist admissible shortest representations for which the usage count in the outer direction shell is positive while the usage in the inner shell is zero. Consequently, no universal rule of the form

\[
\text{inner orbit must saturate before outer orbit activates}
\]

is compatible with the exact arithmetic representation data.

**Proof.** The branch-level orbit-fusion classification supplies explicit admissible elements whose shortest geodesic representatives use only the outer-shell direction orbit. Since the inner-shell count vanishes while the outer-shell count is nonzero, any universal sequential-activation implication is contradicted. The conclusion is invariant under relabeling inside the oblique orbit because the statement concerns orbit occupancy, not a chosen representative direction. ∎

The proposition does not forbid a prioritized search algorithm. It only separates such an algorithm from the arithmetic invariant itself.

---

## 3. The forgetting map and its exact fibers

### 3.1 Orbit-total quotient

The full orbital datum

\[
\Omega=(a;\{b,c\})
\]

contains two levels of information: axial usage `a`, and the distribution inside the oblique orbit.

For the network model developed here, the first canonical quotient is the orbit-total state

\[
\boxed{
\Xi(\Omega)=(A,O):=(a,b+c).
}
\]

Thus `Xi` remembers how much capacity lies in the axial orbit and how much lies in the oblique orbit, but forgets the split between the two oblique representatives.

### 3.2 Folded magnitude interface

The previously published interface `(P,Q)` is obtained after forgetting the orbit placement and retaining the two nonzero geodesic magnitudes in decreasing order:

\[
P\ge Q\ge0.
\]

In the generic odd setting, shortest representatives use at most two of the three undirected primitive directions. Hence the fold can be analyzed exactly.

### 3.3 Fiber classification

**Theorem 3.1 (exact forgetting-fiber classification).**  
In the generic odd orbital regime, the fiber cardinality of the folded pair is

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

For every strict interior pair `P>Q>0`, the three canonical orbital states are

\[
\boxed{
\Omega_I=(P;\{Q,0\}),
\qquad
\Omega_{II}=(Q;\{P,0\}),
\qquad
\Omega_{III}=(0;\{P,Q\}).
}
\]

Their orbit-total images are

\[
\boxed{
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,P+Q).
}
\]

**Proof.** Because a shortest representation has at most two nonzero direction counts, an interior folded pair `P>Q>0` must place the two positive magnitudes in two of the three available undirected direction slots. Modulo exchange of the two oblique slots, there are exactly three orbit-distinct placements: the larger magnitude axial, the smaller magnitude axial, or neither magnitude axial. These give the three displayed `Omega` states and the three displayed orbit totals.

On the boundary `Q=0`, there is only one positive magnitude and hence two possible orbit placements: axial or oblique. On the diagonal `P=Q>0`, exchanging the two positive equal magnitudes removes one of the three interior distinctions, leaving two orbit classes. The zero state is unique. ∎

### 3.4 Static information loss

Theorem 3.1 already proves that `(P,Q)` is not a complete invariant of the intrinsic direction placement. However, a static multiplicity does not yet imply operational significance. It is logically possible that every member of a folded fiber produces the same optimized network response.

The rest of the paper shows that this is false, and then classifies when the network eventually becomes unable to distinguish the states.

---

## 4. Exact orbit-total network response

### 4.1 Fixed host and typed edges

Let `H=(V,E)` be a connected simple host graph with

\[
|V|=n.
\]

Every vertex carries the same orbit-total capacity

\[
\Xi=(A,O),
\qquad A,O\in\mathbb N_0.
\]

A feasible network is a connected spanning subgraph of `H` whose used edges are assigned one of two types:

- axial (`A`-type),
- oblique (`O`-type).

At every vertex, axial degree is at most `A` and oblique degree is at most `O`. Since the support is simple, a host edge can be used at most once in total.

If the network uses `e_A` axial edges and `e_O` oblique edges, define the unused boundary capacities

\[
\boxed{
B_A=nA-2e_A,
\qquad
B_O=nO-2e_O.
}
\]

### 4.2 Pareto response

A feasible boundary pair dominates another if it is coordinatewise no larger and strictly smaller in at least one coordinate. Let

\[
\mathcal R_H^{\Xi}(A,O)
\]

be the Pareto-minimal boundary set.

We encode it by

\[
\boxed{
Z_H^{\Xi}(A,O;X,Y)
=
\sum_{(B_A,B_O)\in\mathcal R_H^{\Xi}(A,O)}
X^{B_A}Y^{B_O}.
}
\]

Polynomial equality is simply a compact way to state equality of finite Pareto sets; no novelty is claimed for the encoding itself.

### 4.3 Operational separation

The first important fact is that the three states in Theorem 3.1 are not generally network-equivalent.

**Theorem 4.1 (operational visibility of orbital placement).**  
There exist generic odd interior folded pairs `P>Q>0` and connected hosts for which

\[
Z_H^{\Xi}(P,Q),
\qquad
Z_H^{\Xi}(Q,P),
\qquad
Z_H^{\Xi}(0,P+Q)
\]

are not all equal.

**Proof.** This follows from the explicit small-host constructions established in the branch-level orbital-network separation theorem. The constructions realize different attainable Pareto boundary sets for distinct orbit-total placements inside one folded fiber. ∎

The theorem converts the static fiber of `(P,Q)` into an operational distinction: a network can detect information that the fold has erased.

---

## 5. Geometry as an orbital-memory filter

### 5.1 Strict one dimension

Take the strict one-dimensional host `P_{2m}`, a path on

\[
n=2m
\]

vertices. It has `2m-1` edges.

Suppose exactly `r` path edges are axial. Then the boundary pair is

\[
B_A=2mA-2r,
\]

\[
B_O=2mO-2(2m-1-r).
\]

If a channel capacity is at least two, it imposes no additional restriction because a path has maximum degree two. If a channel has capacity one, its edges must form a matching; the maximum matching size of `P_{2m}` is `m`.

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

**Theorem 5.1 (exact path response).**  
For every feasible uniform state `(A,O)`,

\[
\boxed{
Z_{P_{2m}}^{\Xi}(A,O;X,Y)
=
\sum_{r=r_{\min}(O)}^{r_{\max}(A)}
X^{2mA-2r}
Y^{2mO-2(2m-1-r)}.
}
\]

**Proof.** Every feasible edge typing is determined at the level of total channel counts by `r`. The only possible obstruction is adjacency of two edges belonging to a capacity-one channel. A path has matchings of every size from zero through `m`, so every integer in the displayed interval is realizable. All realized points have the same total boundary

\[
2m(A+O)-2(2m-1),
\]

hence none dominates another. ∎

**Corollary 5.2 (permanent orbital memory in 1D).**  
For every strict interior fiber `P>Q>0` and every even path size,

\[
\boxed{
Z_I^{1D}\ne Z_{II}^{1D},
\qquad
Z_I^{1D}\ne Z_{III}^{1D},
\qquad
Z_{II}^{1D}\ne Z_{III}^{1D}.
}
\]

Hence

\[
\boxed{1D:\quad3\to3\to3\to\cdots.}
\]

**Proof.** For `Q>=2`, both mixed states allow all path color counts, but their maximum `X` exponents are `2mP` and `2mQ`, which differ because `P>Q`; the pure state has a singleton response. For `Q=1`, the small channel is matching-limited and the exact intervals differ under rank swap; the resulting maximum `X` exponents remain distinct. The pure state remains a singleton. ∎

Thus severe geometric restriction can protect arithmetic direction information indefinitely.

### 5.2 Outerplanar geometry

Outerplanar graphs permit more connectivity than paths but obey the sharp edge bound

\[
|E|\le2n-3.
\]

The branch-level hostile programme classifies the full `Xi` response of every generic odd interior fiber on even outerplanar hosts. The detailed constructions are lengthy; here we state the final theorem.

**Theorem 5.3 (complete outerplanar interior-fiber law).**  
For every strict interior pair

\[
P>Q>0
\]

and every even outerplanar host size

\[
n\ge4,
\]

let

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

The pure-oblique state never collides with either mixed state. The sole loss of information is the mixed rank-swap collision

\[
(2,1)\leftrightarrow(1,2).
\]

**Proof sketch.** The outerplanar analysis consists of three exact components. First, the pure-oblique boundary is determined by the outerplanar edge ceiling together with explicit extremal hosts. Second, lower endpoint bounds for each channel classify when the two mixed response intervals can coincide; the only interior solution is `(2,1)`. Third, in the low-capacity cases where a zero coordinate endpoint is possible, comparison with the exact pure-oblique minimum excludes mixed/pure equality. The complete constructive proof is retained in the branch supplement and will be reproduced in the technical appendix of the typeset version. ∎

The contrast with strict one dimension is already nontrivial: increasing geometric freedom creates one exceptional forgetting class, but outerplanar geometry still preserves almost the entire orbital fiber.

---

## 6. Regular factorizable hosts

We now isolate the structural mechanism behind the dense-host forgetting transition.

### 6.1 Hypotheses

Let `H` be a connected simple graph on an even number `n` of vertices. Assume `H` is `d`-regular and admits a 1-factorization

\[
\boxed{
E(H)=M_1\sqcup\cdots\sqcup M_d,
}
\]

where every `M_i` is a perfect matching.

### 6.2 Degree-window interpolation

**Lemma 6.1 (factorized degree window).**  
Let

\[
0\le l\le u\le d.
\]

For every integer `e` satisfying

\[
\frac{nl}{2}\le e\le\frac{nu}{2},
\]

there exists a spanning subgraph `F` of `H` with exactly `e` edges and

\[
l\le d_F(v)\le u
\]

at every vertex.

**Proof.** Write

\[
e=\frac n2q+r,
\qquad0\le r<\frac n2.
\]

Take `q` complete 1-factors and, if `r>0`, any `r` edges of the next factor. Every vertex has degree `q` or `q+1`, and the endpoint inequalities place both values inside `[l,u]`. ∎

The constructed channel subgraph need not be connected. The main theorem avoids this problem because the two typed channel subgraphs together use the full connected host.

### 6.3 Exact fixed-host response

Assume

\[
S:=A+O\ge d.
\]

Define

\[
D=n(S-d),
\]

\[
L_A=n(A-d)_+,
\qquad
L_O=n(O-d)_+.
\]

**Theorem 6.2 (regular-factorizable host universality).**  
Under the hypotheses above,

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

In this regime the response therefore depends on `H` only through its order and regular degree.

**Proof.** Every feasible network uses at most all `nd/2` host edges, so

\[
B_A+B_O=nS-2(e_A+e_O)\ge nS-nd=D.
\]

Also

\[
e_A\le\min(nd/2,nA/2),
\]

which gives

\[
B_A\ge n(A-d)_+=L_A,
\]

and similarly `B_O>=L_O`.

To attain the lower-total-boundary line, use every edge of `H`. Let `F` be the axial subgraph and declare every edge in `H\setminus F` oblique. The channel constraints become

\[
(d-O)_+\le d_F(v)\le\min(A,d).
\]

Since `A+O>=d`, the interval is nonempty. Lemma 6.1 realizes every axial edge count between the two corresponding endpoints, and therefore every parity-compatible boundary point in the displayed segment. The union of the two channel subgraphs is the full host `H`, hence connected.

Finally, let `(B_A,B_O)` be any feasible point with sum greater than `D`. Its coordinates satisfy the two lower bounds. The interval

\[
\left[
\max(L_A,D-B_O),
\min(B_A,D-L_O)
\right]
\]

is nonempty; all endpoints are even. Choosing an even `b` in this interval gives a realized lower-line point `(b,D-b)` that componentwise dominates `(B_A,B_O)`. Hence every Pareto-minimal point lies on the realized lower line. ∎

### 6.4 The orbital-port filtration

Return to a strict interior folded pair

\[
P>Q>0,
\qquad
S=P+Q.
\]

The three orbit-total states are

\[
(P,Q),
\qquad
(Q,P),
\qquad
(0,S).
\]

Assume

\[
d\le S.
\]

**Theorem 6.3 (degree-controlled orbital-memory filtration).**  
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

**Proof.** The two mixed responses have the same total boundary. By Theorem 6.2 their lower axial endpoints are

\[
n(P-d)_+,
\qquad
n(Q-d)_+.
\]

Because `P>Q`, they are equal exactly when `P<=d`. Thus the mixed states are distinct for `d<P` and collide for `d>=P`.

If `d<S`, the pure-oblique response is the singleton

\[
(0,n(S-d)).
\]

When `d<P`, at least one mixed state has positive minimum axial boundary, and the other either does as well or has a nontrivial segment containing positive axial values; hence neither equals the pure singleton. When `P<=d<S`, the two mixed states share the full nontrivial step-two segment on the line `B_A+B_O=n(S-d)`, whereas the pure state is only one endpoint. Finally, at `d=S`, the total-boundary floor is zero and all three responses are the singleton `(0,0)`. ∎

The theorem is the central filtration law of this paper:

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
}
\]

The first threshold erases the **placement of the larger folded component** between the two orbit totals. The second threshold erases the remaining distinction between a mixed state and the pure-oblique placement.

Again, this is an operational network-memory theorem, not a sequential arithmetic activation law.

### 6.5 The underfull boundary

If

\[
S<d,
\]

then a 1-factorization alone does not guarantee zero boundary. Selecting `S` perfect matchings may produce a disconnected spanning subgraph.

**Proposition 6.4 (sufficient underfull closure condition).**  
If `H` contains a connected spanning union `J` of `S` factors from the fixed 1-factorization, then any partition of those factors into `A` axial and `O` oblique factors with `A+O=S` yields

\[
\mathcal R_H^{\Xi}(A,O)=\{(0,0)\}.
\]

No converse is claimed.

This is the point where host topology can re-enter even after degree and factorization are fixed.

---

## 7. Exact planar realizations

### 7.1 Even regular planar triangulations

A simple planar triangulation on `n` vertices has

\[
|E|=3n-6.
\]

If it is `d`-regular, then

\[
nd=6n-12,
\]

so

\[
d=6-\frac{12}{n}.
\]

For even `n>=4`, integrality gives exactly

\[
\boxed{
(n,d)=(4,3),(6,4),(12,5).
}
\]

These are realized by the tetrahedral, octahedral, and icosahedral graphs. Each has an explicit 1-factorization.

Because each graph attains the planar edge ceiling at its order, Theorem 6.2 is not merely a fixed-host result here: its lower-total-boundary bound is also the global planar bound.

### 7.2 Platonic planar threshold theorem

**Corollary 7.1 (exact planar response at the Platonic orders).**  
Let

\[
(n,d)\in\{(4,3),(6,4),(12,5)\}.
\]

For `A+O>=d`, the exact planar `Xi` Pareto front on `n` vertices is the response given by Theorem 6.2.

For every interior fiber `P>Q>0` with `S=P+Q>=d`,

\[
\boxed{
\nu_{Pl,n}^{\Xi}(P,Q)=
\begin{cases}
1,&S=d,\\
2,&S>d\text{ and }P\le d,\\
3,&S>d\text{ and }P>d.
\end{cases}}
\]

Thus the mixed-state memory thresholds are exactly the regular degrees

\[
3,4,5
\]

at planar orders

\[
4,6,12.
\]

### 7.3 Host-scale trajectories

The fiber

\[
(P,Q)=(4,1)
\]

provides the cleanest exact planar trajectory:

\[
\boxed{
\nu_{Pl,4}=3,
\qquad
\nu_{Pl,6}=2,
\qquad
\nu_{Pl,12}=1.
}
\]

Hence along the explicit sequence of exact planar hosts

\[
4\to6\to12
\]

we observe the full forgetting cascade

\[
\boxed{3\to2\to1.}
\]

The trajectory is fiber dependent. Equal total capacity does not force equal memory behavior at each scale. For example, the `S=6` fibers `(5,1)` and `(4,2)` occupy different threshold positions at the smaller Platonic hosts before both enter the icosahedral degree-5 regime.

### 7.4 Beyond regular extremal hosts

The regular-factorizable theorem does not solve the complete planar problem. Larger planar hosts cannot be regular triangulations of degree six: Euler forces average degree below six, and exact response depends on how overload can be repaired locally.

A separate technical programme in the research branch studies the Gaussian state `(6,5)` by comparing 5-regular planar supports with triangulations. Exact fronts have been closed through order 44, with the first order-46 overload cases also resolved. The universal order-46 closure remains open.

Those results demonstrate that nonregular planar geometry contains genuine additional combinatorics, but they are not needed for Theorem 6.3 and are therefore not used as a publication dependency here.

---

## 8. Observation protocol is another forgetting map

The preceding theorems use the full Pareto response. A restricted search protocol can forget different information.

One example is a maximal-first probe that explicitly prioritizes one capacity according to a chosen rule. Such a probe defines a restricted feasible family and a response no better than the full optimum.

The branch-level complete-host calculation shows that maximal-first and full Pareto optimization can induce different collision relations among the three states of the same orbital fiber. In particular, in an intermediate host-degree regime the full response can identify the two mixed states while the maximal-first probe instead identifies one mixed state with the pure-oblique state.

Therefore

\[
\boxed{
\text{probe-induced forgetting need not equal model-induced forgetting.}
}
\]

This observation reinforces the no-go result of Section 2: a priority convention may be useful experimentally, but it must not be mistaken for the intrinsic arithmetic structure.

---

## 9. Discussion

### 9.1 Three different information losses

The results separate three logically distinct operations.

First is **static arithmetic forgetting**:

\[
\Omega\to\Xi\to(P,Q).
\]

Second is **operational network forgetting**: distinct interface states can acquire the same optimized Pareto response on a sufficiently permissive host.

Third is **observational forgetting**: a restricted probe or scalar projection can merge responses that remain distinct in the full Pareto object.

The first is a property of the local representation. The second is a property of the architecture. The third is a property of what one chooses to observe.

Conflating these levels obscures the main phenomenon.

### 9.2 Geometry can preserve arithmetic memory

The path theorem shows that increasing host size alone does not force forgetting. In strict one dimension, the local degree ceiling never becomes large enough to erase the orbit placement of an interior fiber.

Outerplanar geometry is more permissive but still protects almost all fibers. The exact classification has only one mixed rank-swap exception.

By contrast, regular factorizable hosts expose a sharp degree-controlled filtration. The transition is therefore not merely about the number of vertices; it is about the incidence budget that the host can make simultaneously available at every node.

### 9.3 Degree universality and its boundary

Within the hypotheses of Theorem 6.2 and for `S>=d`, the detailed topology of the host disappears from the uniform `Xi` response: `(n,d)` is sufficient.

That statement has a precise boundary. In the underfull regime `S<d`, zero-boundary closure requires a connected spanning factor of the correct degree, and connectivity need not follow from the existence of a 1-factorization. Thus topology can return exactly where the full host is no longer used.

This boundary suggests a natural next problem: classify connected unions of selected 1-factors and determine when the underfull response is also degree-universal. That problem is deliberately left outside the present paper.

### 9.4 What the paper does not prove

We do not prove:

- a universal strongest-first port activation law;
- a complete network theory retaining the full `Omega=(a;{b,c})` datum;
- a complete planar classification for all capacities and orders;
- a topology/genus theorem;
- response universality for arbitrary regular hosts;
- automatic underfull closure from 1-factorizability alone.

These limitations are structural, not editorial omissions.

---

## 10. Conclusion

The folded arithmetic interface `(P,Q)` is not always the end of the local story. In the generic odd imaginary-quadratic regime it is the image of a finite orbital fiber. For a strict interior pair `P>Q>0`, three canonical direction placements survive in the orbit-total model:

\[
(P,Q),
\qquad
(Q,P),
\qquad
(0,P+Q).
\]

Networks can distinguish these states, and geometry controls how long that distinction survives.

Strict one dimension preserves all three indefinitely. Outerplanar geometry loses only the exceptional mixed rank swap `(2,1)`. Connected regular 1-factorizable hosts obey the exact degree filtration

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
}
\]

Thus arithmetic folding and network optimization form successive information filters. The first forgets where magnitudes live in the intrinsic direction-orbit structure; the second forgets some or all of what remains, depending on the host's incidence capacity.

The main lesson is therefore not a hierarchy of stronger and weaker ports. It is a hierarchy of **observable arithmetic memory**.

---

## Appendix plan for v0.2

The next manuscript revision should add, after literature audit:

- Appendix A: exact arithmetic definitions and the orbit/fusion proof in publication notation;
- Appendix B: full outerplanar constructive proof replacing the proof sketch in Theorem 5.3;
- Appendix C: explicit tetrahedral/octahedral/icosahedral 1-factorizations;
- Appendix D: selected larger-planar `(6,5)` theorem table, with open `n=46` boundary clearly marked;
- bibliography crosswalk to HATTER-SOL-07--10 and all classical graph/arithmetic ingredients.

Secondary `61` tomography, residue-tail collisions, and torus material are intentionally excluded from v0.1 of the main manuscript.
