# HATTER-SOL-11 · Platonic Planar Threshold Theorem

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer for the orbit-total `Xi` model.

**Model scope.** Throughout,

\[
\Omega=(a;\{b,c\})\longmapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical two-channel orbit-total projection. The results below are complete for this `Xi` response model on the stated host sizes and do not claim completeness for richer semantics retaining the full `Omega` datum.

This note answers the next hostile target from `PLANAR_CRITICAL_CAPACITY_HOSTILE_PROBE.md`: what happens to the critical sums `S=6,7` on twelve planar vertices?

The answer is stronger than a case calculation. The tetrahedron, octahedron, and icosahedron form one exact theorem.

---

## 1. The three even regular planar triangulations

Let a simple planar triangulation on `n` vertices be `d`-regular. Euler gives

\[
|E|=3n-6,
\]

so

\[
nd=2|E|=6n-12.
\]

Hence

\[
\boxed{d=6-\frac{12}{n}.}
\]

For even `n>=4`, integrality forces

\[
\boxed{(n,d)=(4,3),(6,4),(12,5).}
\]

These are realized by the three simplicial Platonic graphs:

\[
K_4,\qquad \mathcal O_6,\qquad \mathcal I_{12},
\]

respectively the tetrahedral, octahedral, and icosahedral graphs.

Each will be used as an extremal planar support.

---

## 2. One-factorizations

The argument requires a decomposition of each `d`-regular support into `d` perfect matchings.

### Tetrahedron

`K_4` has the standard 1-factorization into three perfect matchings.

### Octahedron

As already used in `PLANAR_CRITICAL_CAPACITY_HOSTILE_PROBE.md`,

\[
\mathcal O_6=K_6-M_0
\]

for one perfect matching `M_0`. A 1-factorization of `K_6` containing `M_0` leaves four perfect matchings partitioning `E(\mathcal O_6)`.

### Icosahedron

Use the labeling

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
M_0={}&\{N-u_1,\ S-v_0,\ u_0-u_4,\ u_2-v_1,\ u_3-v_2,\ v_3-v_4\},\\
M_1={}&\{N-u_4,\ S-v_2,\ u_0-v_4,\ u_1-u_2,\ u_3-v_3,\ v_0-v_1\},\\
M_2={}&\{N-u_0,\ S-v_1,\ u_1-v_0,\ u_2-u_3,\ u_4-v_4,\ v_2-v_3\},\\
M_3={}&\{N-u_3,\ S-v_4,\ u_0-v_0,\ u_1-v_1,\ u_2-v_2,\ u_4-v_3\},\\
M_4={}&\{N-u_2,\ S-v_3,\ u_0-u_1,\ u_3-u_4,\ v_0-v_4,\ v_1-v_2\}.
\end{aligned}
\]

Each matching has six edges, so their union has thirty edges. Every displayed edge belongs to the icosahedral edge set, and

\[
5\cdot6=30=|E(\mathcal I_{12})|.
\]

Hence

\[
\boxed{E(\mathcal I_{12})=M_0\sqcup M_1\sqcup M_2\sqcup M_3\sqcup M_4.}
\]

Thus the icosahedron is explicitly 1-factorized for the purposes of this theorem.

---

## 3. Regular-support degree-window interpolation

Let `R_{n,d}` be one of

\[
(K_4,3),\qquad(\mathcal O_6,4),\qquad(\mathcal I_{12},5),
\]

with a fixed 1-factorization

\[
E(R_{n,d})=M_1\sqcup\cdots\sqcup M_d.
\]

Each perfect matching has `n/2` edges.

### Lemma T11.41 — Platonic degree-window interpolation

Let

\[
0\le l\le u\le d.
\]

For every integer `e` satisfying

\[
\boxed{\frac{nl}{2}\le e\le\frac{nu}{2},}
\]

there exists a spanning subgraph `H` of `R_{n,d}` with exactly `e` edges and

\[
\boxed{l\le d_H(v)\le u\quad\text{for every vertex }v.}
\]

### Proof

Write

\[
e=\frac n2 q+r,
\qquad
0\le r<\frac n2.
\]

Take the union of `q` full perfect matchings and, if `r>0`, add any `r` edges of the next matching.

Every vertex then has degree `q` or `q+1`. The endpoint inequalities imply these degrees lie in `[l,u]`. QED.

---

## 4. Exact planar response on the three Platonic host sizes

Fix one of

\[
(n,d)=(4,3),(6,4),(12,5).
\]

Take `n` identical orbit-total nodes with capacities

\[
(A,O),
\qquad
S:=A+O\ge d.
\]

For a typed planar simple-support network write

\[
B_A=nA-2e_A,
\qquad
B_O=nO-2e_O.
\]

Every planar graph on `n` vertices has at most

\[
3n-6=\frac{nd}{2}
\]

edges. Hence

\[
\boxed{B_A+B_O\ge D_{n,d}(S):=n(S-d).}
\]

Also

\[
e_A\le\min\left(\frac{nd}{2},\frac{nA}{2}\right),
\]

so

\[
\boxed{B_A\ge L_{n,d}(A):=n(A-d)_+,}
\]

and similarly

\[
\boxed{B_O\ge L_{n,d}(O):=n(O-d)_+.}
\]

### Theorem T11.42 — exact Platonic planar `Xi` front

For

\[
(n,d)\in\{(4,3),(6,4),(12,5)\}
\]

and

\[
A,O\ge0,
\qquad
A+O\ge d,
\]

the exact planar Pareto front on `n` vertices is

\[
\boxed{
\mathcal R^{\Xi}_{Pl,n}(A,O)
=
\left\{
(B_A,B_O):
\begin{array}{l}
B_A+B_O=D_{n,d}(A+O),\\
L_{n,d}(A)\le B_A\le D_{n,d}(A+O)-L_{n,d}(O),\\
B_A\equiv0\pmod2
\end{array}
\right\}.
}
\]

Equivalently,

\[
\boxed{
Z^{\Xi}_{Pl,n}(A,O;X,Y)
=
\sum_{\substack{b=L_{n,d}(A)\\b\equiv0\ (2)}}^{D_{n,d}(A+O)-L_{n,d}(O)}
X^bY^{D_{n,d}(A+O)-b}.
}
\]

### Proof

The displayed lower bounds hold for every feasible planar graph.

For sharpness, use the full support `R_{n,d}` and let the axial subgraph be `H`. The oblique subgraph is the complement of `H` in `R_{n,d}`, hence

\[
d_O(v)=d-d_H(v).
\]

The channel constraints are exactly

\[
(d-O)_+\le d_H(v)\le\min(A,d).
\]

Put

\[
l=(d-O)_+,
\qquad
u=\min(A,d).
\]

Since `A+O>=d`, we have `l<=u`.

By T11.41 every axial edge count

\[
\frac{nl}{2}\le e_A\le\frac{nu}{2}
\]

is realized on the full maximal planar support. Translating with

\[
B_A=nA-2e_A
\]

gives every parity-compatible point on the claimed segment.

Any feasible point above the minimum-total line has larger `B_A+B_O`; using the coordinate lower bounds and parity, it is componentwise dominated by a realized point on the segment. Hence no additional point is Pareto-minimal. QED.

---

## 5. Exact rank-swap threshold

Fix a generic-odd interior fiber

\[
P>Q>0.
\]

The mixed orbit-total states are

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P).
\]

Their response segments have identical total boundary. They coincide exactly when

\[
L_{n,d}(P)=L_{n,d}(Q).
\]

Because

\[
L_{n,d}(t)=n(t-d)_+,
\]

and `P>Q`, equality holds iff

\[
P\le d.
\]

### Theorem T11.43 — Platonic rank-swap threshold

For

\[
(n,d)=(4,3),(6,4),(12,5)
\]

and every generic-odd interior fiber with `P+Q>=d`,

\[
\boxed{
Z^{\Xi}_{Pl,n}(P,Q)
=Z^{\Xi}_{Pl,n}(Q,P)
\iff
P\le d.
}
\]

Thus the exact mixed-state memory thresholds are

\[
\boxed{
3\quad\text{on }n=4,
\qquad
4\quad\text{on }n=6,
\qquad
5\quad\text{on }n=12.
}
\]

---

## 6. Pure-state separation and complete closure

The pure state is

\[
\Xi_{III}=(0,S).
\]

T11.42 gives

\[
\boxed{
Z^{\Xi}_{Pl,n}(0,S)=Y^{D_{n,d}(S)}.
}
\]

If

\[
S=d,
\]

then

\[
D_{n,d}(S)=0,
\]

so all three states have zero boundary:

\[
\boxed{Z_I=Z_{II}=Z_{III}=1.}
\]

If

\[
S>d,
\]

then every mixed state has at least two Pareto monomials. Indeed,

\[
D_{n,d}(S)-L_{n,d}(P)-L_{n,d}(Q)>0
\]

for `P,Q>0`. Therefore the mixed states cannot equal the singleton pure response.

### Corollary T11.43a — class-count law on Platonic hosts

For `P>Q>0` and `S=P+Q>=d`,

\[
\boxed{
\nu^{\Xi}_{Pl,n}(P,Q)=
\begin{cases}
1,&S=d,\\
2,&S>d\text{ and }P\le d,\\
3,&S>d\text{ and }P>d.
\end{cases}}
\]

This completely unifies the exact `n=4`, `n=6`, and `n=12` calculations.

---

## 7. The requested `S=6,7` icosahedral classification

Now specialize to

\[
(n,d)=(12,5).
\]

### Total capacity `S=6`

Here

\[
D_{12,5}=12.
\]

Both interior fibers satisfy `P<=5`:

\[
(5,1),
\qquad
(4,2).
\]

Hence both mixed rank swaps collide, while the pure state remains distinct:

\[
\boxed{
\nu^{\Xi}_{Pl,12}(5,1)=2,
\qquad
\nu^{\Xi}_{Pl,12}(4,2)=2.
}
\]

For either pair the mixed response is the full step-two segment

\[
\boxed{
Z_{mix}
=
\sum_{j=0}^{6}X^{2j}Y^{12-2j},
}
\]

while

\[
\boxed{Z_{pure}=Y^{12}.}
\]

### Total capacity `S=7`

Now

\[
D_{12,5}=24.
\]

For

\[
(P,Q)=(6,1),
\]

the larger capacity crosses the degree-5 threshold, so the mixed states remain distinct:

\[
\boxed{
\nu^{\Xi}_{Pl,12}(6,1)=3.
}
\]

Their `B_A` supports are

\[
12\le B_A\le24
\]

for `(6,1)`, and

\[
0\le B_A\le12
\]

for `(1,6)`, both in steps of two.

For

\[
(P,Q)=(5,2)
\quad\text{and}\quad
(4,3),
\]

we have `P<=5`, so the mixed rank swaps collide:

\[
\boxed{
\nu^{\Xi}_{Pl,12}(5,2)=2,
\qquad
\nu^{\Xi}_{Pl,12}(4,3)=2.
}
\]

The common mixed response in both cases is

\[
\boxed{
\sum_{j=0}^{12}X^{2j}Y^{24-2j},
}
\]

while the pure response is `Y^{24}`.

---

## 8. Exact host-scale trajectories across `4 -> 6 -> 12`

The Platonic theorem turns the three host sizes into a clean scale sequence with thresholds

\[
3\to4\to5.
\]

For the critical fibers:

| `(P,Q)` | `nu^Xi_Pl,4` | `nu^Xi_Pl,6` | `nu^Xi_Pl,12` |
|:---:|---:|---:|---:|
| `(4,1)` | 3 | 2 | 1 |
| `(3,2)` | 2 | 2 | 1 |
| `(5,1)` | 3 | 3 | 2 |
| `(4,2)` | 3 | 2 | 2 |
| `(6,1)` | 3 | 3 | 3 |
| `(5,2)` | 3 | 3 | 2 |
| `(4,3)` | 3 | 2 | 2 |

The first two rows have `S=5`; the remaining rows are `S=6,7`.

Thus host-scale memory loss is **fiber dependent** even within a fixed planar geometry.

---

## 9. Why the threshold sequence stops at five

For a regular planar triangulation,

\[
d=6-\frac{12}{n}<6.
\]

The only even regular triangulation sizes are exactly

\[
4,6,12,
\]

with thresholds

\[
3,4,5.
\]

There is no finite `6`-regular planar triangulation.

This has a direct memory interpretation: the Platonic mechanism can raise the exact full-support threshold from `3` to `4` to `5`, but never to `6`.

For a pure channel of capacity `6`, Euler already forces

\[
B\ge 12
\]

on every finite simple planar graph:

\[
B=6n-2|E|
\ge6n-2(3n-6)=12.
\]

So complete planar saturation of uniform capacity `6` is impossible at every finite host size.

This is the first structural obstruction showing that the planar host-scale forgetting process cannot simply continue the unrestricted complete-host closure law.

---

## 10. What is classical and what is claimed here

Classical ingredients:

- Euler's planar edge formula for triangulations;
- perfect matchings and 1-factorizations;
- the tetrahedral, octahedral, and icosahedral graphs;
- elementary degree-capacity counting.

The HATTER-SOL claim is the exact composition of these ingredients with the previously defined orbit-total response model:

\[
\boxed{
\text{regular maximal planar support}
\to
\text{exact polynomial Pareto front}
\to
\text{degree threshold for orbital rank memory}.
}
\]

The resulting threshold sequence

\[
\boxed{3\to4\to5}
\]

and the corresponding exact fiber-dependent memory trajectories are the theorem content of this note.

---

## 11. Next target

The Platonic hosts are now completely solved in the `Xi` model.

The next planar question should no longer be another isolated regular host. It should attack the obstruction beyond degree five:

> for total capacity `S>=6`, can irregular triangulations produce new mixed-state collisions that are invisible to the Platonic threshold theorem, and what invariant replaces regular degree `d`?

The first sharp laboratory is the fiber

\[
(P,Q)=(6,1),
\]

because it remains fully separated on all three Platonic hosts while pure capacity `7` is far above the planar regularity ceiling.

A candidate invariant is the degree-defect profile

\[
\delta_G(v):=6-d_G(v),
\]

whose total on every triangulation is fixed:

\[
\sum_v\delta_G(v)=12.
\]

This may be the correct planar replacement for the scalar host degree threshold.