# HATTER-SOL-11 · Regular Factorizable Host Orbital-Memory Theorem

**Status:** closed central theorem layer.  
**Model scope:** canonical orbit-total projection `Xi=(A,O)`; connected simple-support networks.  
**Numbering:** local descriptive theorem labels are used here; final publication numbering should be assigned only after the HATTER-SOL-11 spine is frozen.

This note unifies the even-complete-host law and the Platonic planar-host law. The point is not that complete and planar geometries are the same. The point is that, once a fixed host is connected, regular, and 1-factorizable, the exact uniform two-channel response in the critical/overfull regime depends only on the host degree.

A hostile correction is essential: 1-factorizability alone does **not** imply connected zero-boundary closure when the available total capacity is strictly smaller than the host degree. Accordingly, the universal theorem below is stated for `A+O >= d`. The underfull regime is treated separately at the end.

---

## 1. Fixed-host setup

Let `H` be a connected simple graph on an even number `n` of vertices. Assume that `H` is `d`-regular and admits a 1-factorization

\[
\boxed{
E(H)=M_1\sqcup\cdots\sqcup M_d,
}
\]

where every `M_i` is a perfect matching.

At every vertex place the same orbit-total capacity

\[
\Xi=(A,O),
\qquad A,O\in\mathbb N_0,
\]

and write

\[
S:=A+O.
\]

A feasible `Xi`-network is a connected spanning subgraph of `H` whose used edges are typed axial or oblique, with axial degree at most `A` and oblique degree at most `O` at every vertex. Each host edge may be used at most once in total.

For a feasible network let

\[
B_A=nA-2e_A,
\qquad
B_O=nO-2e_O
\]

be the unused axial and oblique boundary capacities.

Let

\[
\mathcal R_H^{\Xi}(A,O)
\]

be the Pareto-minimal set of boundary pairs.

---

## 2. Degree-window interpolation inside a 1-factorized host

### Lemma RFH.1 — exact spanning degree window

Let

\[
0\le l\le u\le d.
\]

For every integer `e` with

\[
\boxed{
\frac{nl}{2}\le e\le\frac{nu}{2},
}
\]

there exists a spanning subgraph `F\subseteq H` with exactly `e` edges and

\[
\boxed{
l\le d_F(v)\le u\quad\text{for every }v.}
\]

### Proof

Write

\[
e=\frac n2 q+r,
\qquad
0\le r<\frac n2.
\]

Take the union of `q` full 1-factors and, if `r>0`, add any `r` edges of the next 1-factor. Every vertex has degree `q` or `q+1`. The endpoint inequalities force these values into `[l,u]`. QED.

The subgraph `F` itself need not be connected. In the main theorem this causes no problem because `F` is only one channel of a two-channel decomposition whose **union is the whole connected host `H`**.

---

## 3. Exact response in the critical/overfull regime

Assume from now on

\[
\boxed{S=A+O\ge d.}
\]

Define

\[
D_H(S):=n(S-d),
\]

\[
L_A:=n(A-d)_+,
\qquad
L_O:=n(O-d)_+.
\]

### Theorem RFH.2 — regular-factorizable host universality

For every connected `d`-regular 1-factorizable host `H` on even `n` vertices and every uniform state `(A,O)` with `A+O>=d`, the exact connected Pareto front is

\[
\boxed{
\mathcal R_H^{\Xi}(A,O)
=
\left\{
(B_A,B_O):
\begin{array}{l}
B_A+B_O=D_H(A+O),\\
L_A\le B_A\le D_H(A+O)-L_O,\\
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
\sum_{\substack{b=L_A\\b\equiv0\ (2)}}^{D_H(S)-L_O}
X^bY^{D_H(S)-b}.
}
\]

In particular, among hosts satisfying the stated hypotheses, the response depends on `H` only through `(n,d)`.

### Proof

Every feasible network uses at most all `nd/2` host edges. Therefore

\[
B_A+B_O
=nS-2(e_A+e_O)
\ge nS-nd
=D_H(S).
\]

Also

\[
e_A\le\min\left(\frac{nd}{2},\frac{nA}{2}\right),
\]

hence

\[
B_A=nA-2e_A\ge n(A-d)_+=L_A.
\]

Similarly

\[
B_O\ge L_O.
\]

We now realize every parity-compatible point on the lower-total-boundary line by using **all** edges of `H`. Let `F` be the axial subgraph; every edge of `H\setminus F` is declared oblique. Then the oblique degree at a vertex is

\[
d-d_F(v).
\]

The channel constraints are exactly

\[
(d-O)_+\le d_F(v)\le\min(A,d).
\]

Set

\[
l=(d-O)_+,
\qquad
u=\min(A,d).
\]

Because `A+O>=d`, we have `l<=u`. By Lemma RFH.1, every edge count

\[
\frac{nl}{2}\le e_A\le\frac{nu}{2}
\]

is attainable. Translating via `B_A=nA-2e_A` gives exactly

\[
L_A\le B_A\le D_H(S)-L_O
\]

in steps of two.

The union of the axial and oblique subgraphs is the full host `H`, hence is connected. Thus every displayed boundary point is a valid connected HATTER realization.

Finally, take any feasible point above the lower-total line. Its coordinates obey `B_A>=L_A`, `B_O>=L_O` and even parity. Since its sum is strictly larger than `D_H(S)`, choose a parity-compatible `b` in the realized interval with

\[
L_A\le b\le B_A
\]

and

\[
D_H(S)-b\le B_O.
\]

Such a `b` exists because these inequalities are equivalent to choosing an even integer in

\[
\left[
\max(L_A,D_H(S)-B_O),
\min(B_A,D_H(S)-L_O)
\right],
\]

whose endpoints are even and whose lower endpoint does not exceed the upper one by the assumed coordinate and total-sum inequalities. The corresponding realized point on the lower-total line componentwise dominates the original point. Hence no point above that line is Pareto-minimal. QED.

---

## 4. Generic-odd orbital forgetting fiber

Fix a generic-odd interior forgetting fiber

\[
P>Q>0,
\qquad
S=P+Q.
\]

Its three canonical orbit-total states are

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,S).
\]

Assume the regular host degree satisfies

\[
d\le S,
\]

so RFH.2 applies to all three states.

Define the fixed-host response-class count

\[
\nu_H^{\Xi}(P,Q)
:=
\left|
\left\{
Z_H^{\Xi}(P,Q),
Z_H^{\Xi}(Q,P),
Z_H^{\Xi}(0,S)
\right\}
\right|.
\]

### Theorem RFH.3 — exact orbital-memory degree filtration

For every connected even-order `d`-regular 1-factorizable host with `d<=P+Q`,

\[
\boxed{
\nu_H^{\Xi}(P,Q)
=
\begin{cases}
3,&d<P,\\
2,&P\le d<P+Q,\\
1,&d=P+Q.
\end{cases}}
\]

More precisely:

- if `d<P`, then the two mixed responses are distinct and both are distinct from the pure-oblique response;
- if `P<=d<S`, then the mixed rank swap is forgotten,
  \[
  Z_H^{\Xi}(P,Q)=Z_H^{\Xi}(Q,P),
  \]
  while the pure state remains distinct;
- if `d=S`, then all three states close completely,
  \[
  Z_H^{\Xi}(P,Q)=Z_H^{\Xi}(Q,P)=Z_H^{\Xi}(0,S)=1.
  \]

### Proof

For the mixed states, RFH.2 gives the same total boundary `D=n(S-d)`. Their lower axial endpoints are respectively

\[
n(P-d)_+
\quad\text{and}\quad
n(Q-d)_+.
\]

Since `P>Q`, these are equal iff `P<=d`. Thus the mixed responses are distinct for `d<P` and identical for `d>=P` within the regime `d<=S`.

For the pure state `(0,S)`, RFH.2 gives the singleton

\[
\boxed{(0,n(S-d)).}
\]

when `d<S`. If `d<P`, Type I has positive minimum axial boundary. Type II either has positive minimum axial boundary or, when `Q<=d<P`, has a nontrivial response segment extending to positive axial boundary. Hence neither mixed response equals the pure singleton.

If `P<=d<S`, both mixed responses are the full even step segment

\[
B_A+B_O=n(S-d),
\qquad
0\le B_A\le n(S-d),
\]

which contains more than one point because `n` is even and `S-d>=1`. The pure response is its single endpoint `(0,n(S-d))`, so it remains distinct.

If `d=S`, the total boundary floor is zero and all capacities fit exactly into the full `d`-regular host. RFH.2 gives the singleton `(0,0)` for all three states. QED.

---

## 5. What this theorem unifies

RFH.2 contains as special cases:

1. the critical/overfull portion of the even-complete-host theorem, because `K_{2m}` is `(2m-1)`-regular and 1-factorizable;
2. the tetrahedral, octahedral, and icosahedral response theorems, because their edge sets admit the explicit 1-factorizations already recorded in `PLANAR_PLATONIC_THRESHOLD_THEOREM.md`.

RFH.3 shows that the repeated pattern

\[
\boxed{3\to2\to1}
\]

is not a coincidence of complete graphs or Platonic solids. It is the universal orbital-memory filtration of the generic-odd interior fiber on the stated regular-factorizable host class as the accessible regular degree crosses

\[
\boxed{P\quad\text{and then}\quad P+Q.}
\]

This gives a precise operational meaning to the phrase **orbital-port filtration**: the host degree acts as an interface budget that first erases the placement of the larger folded component and only at the total-capacity threshold erases the remaining pure-oblique distinction.

---

## 6. Host topology: what is and is not forgotten

Within the fixed-host family of RFH.2 and for `S>=d`, the uniform two-channel Pareto response is topology-blind once `(n,d)` is fixed.

This statement must not be overextended.

It does **not** say that:

- arbitrary `d`-regular hosts have the same response;
- 1-factorizability is necessary;
- geometry classes with different extremal edge budgets have the same response;
- richer `Omega=(a;{b,c})` semantics collapse to `Xi`;
- host topology is irrelevant in the underfull regime `S<d`.

The theorem isolates a sufficient structural mechanism: connectedness plus a 1-factorization makes the critical/overfull uniform `Xi` response depend only on the accessible degree budget.

---

## 7. Hostile audit of the underfull regime `S<d`

A tempting but false extrapolation would be

\[
S<d\Longrightarrow\mathcal R_H^{\Xi}(A,O)=\{(0,0)\}.
\]

A 1-factorization does provide `S` pairwise edge-disjoint perfect matchings, but their union need not be connected. Since the HATTER network is required to be connected, zero boundary requires more: a connected spanning `S`-regular factor whose edges can be split into `A` and `O` admissible channel factors.

Therefore:

### Proposition RFH.4 — sufficient underfull closure condition

If `S<d` and the host contains a connected spanning subgraph `J` that is the union of `S` 1-factors from the host factorization, then for every split `S=A+O` obtained by partitioning those `S` factors into `A` axial and `O` oblique factors,

\[
\boxed{
\mathcal R_H^{\Xi}(A,O)=\{(0,0)\}.
}
\]

The proposition is immediate because `J` is connected and saturates every channel capacity exactly.

No converse is claimed.

This is the correct boundary between the universal theorem and host-specific topology.

---

## 8. Geometry-class lifting rule

RFH.2 is a **fixed-host** theorem.

To identify its front with the exact response of an entire geometry class `C`, one needs an independent extremality statement showing that no admissible `C`-host can improve the total-edge or channel bounds used in RFH.2.

Examples already proved in the branch:

- on `K_{2m}`, the host is unrestricted-edge maximal;
- on the tetrahedron, octahedron, and icosahedron, the host is planar-edge maximal at its order.

Accordingly, those earlier geometry-class theorems remain valid and are now conceptually unified by RFH.2 rather than replaced by it.

---

## 9. Publication-level conclusion

For the canonical orbit-total model, a generic-odd folded pair `(P,Q)` carries a three-member intrinsic forgetting fiber. On connected regular 1-factorizable hosts in the exact critical/overfull regime, the network remembers these three members according to a sharp degree filtration:

\[
\boxed{
\begin{array}{ccl}
d<P&:&3\text{ observable orbital states},\\
P\le d<P+Q&:&2\text{ response classes},\\
d=P+Q&:&1\text{ closed class}.
\end{array}}
\]

The thresholds are derived from the network response itself. They are not a strongest-first activation axiom and they do not follow merely from sorting `P>=Q`.
