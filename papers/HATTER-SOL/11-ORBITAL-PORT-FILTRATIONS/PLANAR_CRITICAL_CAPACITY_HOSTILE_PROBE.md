# HATTER-SOL-11 · Planar Critical-Capacity Hostile Probe

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** new closed theorem layer for the orbit-total `Xi` model; planar classification remains open beyond the hosts proved here.

**Model scope.** Throughout,

\[
\Omega=(a;\{b,c\})\longmapsto\Xi=(A,O)=(a,b+c)
\]

is the canonical orbit-total two-channel projection from `ORBITAL_NETWORK_FIBER_SEPARATION.md`. No claim is made here for every richer network semantics retaining the full `Omega` datum.

The outerplanar block suggested that the next hostile planar capacities are total capacities

\[
S=5,6,7.
\]

The first attack produces something stronger: an exact response theorem on the six-vertex planar host, plus an explicit twelve-vertex complete collapse at `S=5`.

---

## 1. The six-vertex maximal planar host

Let

\[
\mathcal O_6:=K_{2,2,2},
\]

the octahedral graph. It is planar, connected, `4`-regular, and has

\[
|E(\mathcal O_6)|=12=3\cdot6-6.
\]

Thus it is a maximal planar graph on six vertices.

A useful description is

\[
\mathcal O_6=K_6-M_0,
\]

where `M_0` is a perfect matching joining the three pairs of opposite octahedral vertices.

Since `K_6` has a 1-factorization into five perfect matchings and the factorization may be chosen to contain `M_0`, the remaining four perfect matchings

\[
M_1,M_2,M_3,M_4
\]

partition the octahedral edge set:

\[
\boxed{
E(\mathcal O_6)=M_1\sqcup M_2\sqcup M_3\sqcup M_4.
}
\]

Each `M_i` has three edges.

This gives an exact degree-window interpolation lemma.

### Lemma T11.38.1 — octahedral degree-window interpolation

Let

\[
0\le l\le u\le4.
\]

For every integer

\[
3l\le e\le3u
\]

there exists a spanning subgraph `H` of `O_6` with exactly `e` edges and

\[
\boxed{l\le d_H(v)\le u\quad\text{for every vertex }v.}
\]

### Proof

Write

\[
e=3q+r,
\qquad
0\le r\le2.
\]

Take the union of `q` full perfect matchings among `M_1,...,M_4`, and if `r>0` add any `r` edges of the next perfect matching.

Every vertex then has degree either `q` or `q+1`. Because `3l<=e<=3u`, these degrees lie in `[l,u]`. QED.

---

## 2. Exact six-vertex planar response

Take six identical orbit-total nodes of capacity

\[
(A,O),
\qquad
S:=A+O\ge4.
\]

For a typed simple-support planar graph write

\[
B_A=6A-2e_A,
\qquad
B_O=6O-2e_O.
\]

Every six-vertex planar graph has at most twelve edges, so

\[
\boxed{B_A+B_O\ge D_6(S):=6(S-4).}
\]

Also

\[
e_A\le\min(12,3A),
\]

and similarly for `O`. Therefore

\[
\boxed{
B_A\ge L_6(A):=6(A-4)_+,
\qquad
B_O\ge L_6(O):=6(O-4)_+.
}
\]

The octahedron realizes every point allowed by these inequalities on the minimum-total-boundary line.

### Theorem T11.38 — exact six-vertex planar orbit-total front

For every pair of nonnegative integers

\[
A,O\ge0,
\qquad
A+O\ge4,
\]

the exact planar Pareto front on six vertices is

\[
\boxed{
\mathcal R^{\Xi}_{Pl,6}(A,O)
=
\left\{
(B_A,B_O):
\begin{array}{l}
B_A+B_O=D_6(A+O),\\
L_6(A)\le B_A\le D_6(A+O)-L_6(O),\\
B_A\equiv0\pmod2
\end{array}
\right\}.
}
\]

Equivalently,

\[
\boxed{
Z^{\Xi}_{Pl,6}(A,O;X,Y)
=
\sum_{\substack{b=L_6(A)\\b\equiv0\ (2)}}^{D_6(A+O)-L_6(O)}
X^bY^{D_6(A+O)-b}.
}
\]

### Proof

The lower bounds above hold for every feasible planar graph.

For sharpness, use the full octahedral support. If the axial subgraph is `H`, then the oblique subgraph is its complement in `O_6`, so

\[
d_O(v)=4-d_H(v).
\]

The channel constraints are therefore exactly

\[
(4-O)_+\le d_H(v)\le\min(A,4).
\]

Put

\[
l=(4-O)_+,
\qquad
u=\min(A,4).
\]

Since `A+O>=4`, we have `l<=u`.

By Lemma T11.38.1 every axial edge count

\[
3l\le e_A\le3u
\]

is realized on the full twelve-edge support. Translating by

\[
B_A=6A-2e_A
\]

gives exactly the stated step-two segment.

Finally, any feasible boundary point outside the minimum-total line has

\[
B_A+B_O>D_6.
\]

Together with the coordinate lower bounds and parity, it is componentwise dominated by a point of the realized step-two segment. Hence no other point is Pareto-minimal. QED.

---

## 3. Exact six-vertex rank-swap law

Fix a generic-odd interior fiber

\[
P>Q>0,
\qquad
S=P+Q\ge4.
\]

The mixed orbit-total states are

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P).
\]

Their six-vertex planar fronts have the same total boundary `D_6(S)`. The first has `B_A` interval

\[
L_6(P)\le B_A\le D_6-L_6(Q),
\]

while the swapped state has

\[
L_6(Q)\le B_A\le D_6-L_6(P).
\]

Since

\[
L_6(t)=6(t-4)_+,
\]

the two intervals coincide iff `L_6(P)=L_6(Q)`.

For `P>Q`, this happens exactly when both lie at or below the octahedral degree threshold:

\[
P\le4.
\]

### Theorem T11.39 — six-vertex planar rank-swap classification

For every generic-odd interior orbit-total fiber with

\[
P>Q>0,
\qquad
P+Q\ge4,
\]

\[
\boxed{
Z^{\Xi}_{Pl,6}(P,Q)=Z^{\Xi}_{Pl,6}(Q,P)
\iff
P\le4.
}
\]

Thus the six-vertex planar host has an exact **degree-4 memory threshold**.

This is the planar analogue of the outerplanar degree-2 threshold, but it is a theorem only for the six-vertex octahedral extremal host problem, not a universal planar threshold for all host sizes.

---

## 4. Mixed versus pure state on six vertices

The pure-oblique state is

\[
\Xi_{III}=(0,S).
\]

T11.38 gives the singleton

\[
\boxed{
Z^{\Xi}_{Pl,6}(0,S)=Y^{D_6(S)}.
}
\]

For a mixed state `(P,Q)` the T11.38 segment is a singleton iff

\[
L_6(P)+L_6(Q)=D_6(P+Q).
\]

For positive `P,Q` this equality occurs at total capacity `S=4`; for every

\[
S>4
\]

the mixed response has at least two monomials.

Therefore:

### Corollary T11.39a

For every interior fiber with

\[
P+Q>4,
\]

the pure-oblique state remains distinct from both mixed states on six planar vertices.

At the boundary value `S=4`, the fiber `(3,1)` completely closes on the octahedron:

\[
Z^{\Xi}_{Pl,6}(3,1)
=Z^{\Xi}_{Pl,6}(1,3)
=Z^{\Xi}_{Pl,6}(0,4)=1.
\]

---

## 5. The critical capacities `S=5,6,7`

For `S>4`, define the six-vertex response-class count

\[
\nu^{\Xi}_{Pl,6}(P,Q)
=
\left|
\{Z(P,Q),Z(Q,P),Z(0,P+Q)\}
\right|.
\]

T11.39 and Corollary T11.39a give the exact table.

| `S` | interior `(P,Q)` | mixed rank swap | `nu^Xi_Pl,6` |
|---:|:---:|:---:|---:|
| 5 | `(4,1)` | collision | 2 |
| 5 | `(3,2)` | collision | 2 |
| 6 | `(5,1)` | separated | 3 |
| 6 | `(4,2)` | collision | 2 |
| 7 | `(6,1)` | separated | 3 |
| 7 | `(5,2)` | separated | 3 |
| 7 | `(4,3)` | collision | 2 |

So the hostile search kills any naive statement that a fixed total capacity `S` determines one planar memory regime.

Already at `S=6`, the fibers `(5,1)` and `(4,2)` behave differently on the same six-vertex planar host.

---

## 6. Four-vertex calibration

On four vertices, the planar class contains the complete graph `K_4`, so the exact HATTER-SOL-09 even-complete-host theorem applies with

\[
c=3.
\]

For an interior state `(P,Q)`, rank-swapped mixed responses coincide iff both capacities lie at or below the host degree threshold `3`.

For the critical fibers this gives:

| `S` | `(P,Q)` | `nu^Xi_Pl,4` |
|---:|:---:|---:|
| 5 | `(4,1)` | 3 |
| 5 | `(3,2)` | 2 |
| 6 | `(5,1)` | 3 |
| 6 | `(4,2)` | 3 |
| 7 | `(6,1)` | 3 |
| 7 | `(5,2)` | 3 |
| 7 | `(4,3)` | 3 |

Thus merely moving from four to six planar vertices already changes the memory class of `(4,1)`, `(4,2)`, and `(4,3)`.

---

## 7. A twelve-vertex planar collapse at total capacity five

The six-vertex result still leaves the pure state distinct at `S=5`. We now try to kill that distinction.

Use the icosahedral graph `I`, a planar `5`-regular graph on twelve vertices with thirty edges:

\[
|E(I)|=30=3\cdot12-6.
\]

A concrete labeling is:

- two poles `N,S`;
- upper pentagon `u_0,...,u_4`;
- lower pentagon `v_0,...,v_4`;

with indices modulo five and edges

\[
N u_i,
\quad
S v_i,
\quad
u_i u_{i+1},
\quad
v_i v_{i+1},
\quad
u_i v_i,
\quad
u_i v_{i-1}.
\]

The following six edges form a perfect matching:

\[
\boxed{
M=
\{Nu_0,Sv_0,u_1v_1,u_2v_2,u_3v_3,u_4v_4\}.
}
\]

Hence

\[
H:=I-M
\]

is a spanning `4`-regular graph.

By the classical 2-factorization theorem for even-regular graphs,

\[
\boxed{H=F_1\sqcup F_2}
\]

for two spanning `2`-factors `F_1,F_2`.

This single decomposition saturates every positive split of total capacity five that occurs in a generic-odd interior fiber.

### Theorem T11.40 — icosahedral full collapse at `S=5`

On twelve planar vertices, for both interior folded pairs

\[
(P,Q)=(4,1),
\qquad
(P,Q)=(3,2),
\]

all three orbit-total states have zero boundary:

\[
\boxed{
Z^{\Xi}_{Pl,12}(P,Q)
=
Z^{\Xi}_{Pl,12}(Q,P)
=
Z^{\Xi}_{Pl,12}(0,5)
=1.
}
\]

### Proof

- Pure state `(0,5)`: color all icosahedral edges oblique. Since `I` is `5`-regular, every oblique port is saturated.
- `(4,1)`: color `M` by the capacity-1 channel and `H` by the capacity-4 channel.
- `(1,4)`: swap channel labels.
- `(3,2)`: color `F_1` by the capacity-2 channel and `M\cup F_2` by the capacity-3 channel.
- `(2,3)`: swap channel labels.

Every construction uses all thirty support edges and saturates both channel capacities at every vertex. Hence `(0,0)` is attainable and dominates every other boundary vector. QED.

---

## 8. A genuine planar host-scale memory loss

For the fiber

\[
(P,Q)=(4,1),
\]

the exact class counts at three planar host sizes are

\[
\boxed{
\nu^{\Xi}_{Pl,4}(4,1)=3,
\qquad
\nu^{\Xi}_{Pl,6}(4,1)=2,
\qquad
\nu^{\Xi}_{Pl,12}(4,1)=1.
}
\]

Thus along the explicit host-size sequence

\[
4\to6\to12
\]

we obtain the full information cascade

\[
\boxed{3\to2\to1.}
\]

This is **not** claimed as monotonicity in every intermediate host size; it is an exact three-scale witness.

For the second `S=5` fiber,

\[
(P,Q)=(3,2),
\]

the corresponding exact values are

\[
\boxed{2\to2\to1.}
\]

The four-vertex host has already forgotten the mixed rank swap because both capacities lie at or below degree `3`.

---

## 9. What the hostile probe changed

Before this calculation, it was tempting to look for a planar analogue of the outerplanar classification based only on total capacity.

That is false.

The exact six-vertex law shows that the relevant local invariant is the placement of the capacities relative to the extremal host degree `4`:

\[
\boxed{
P\le4
\Longleftrightarrow
\text{mixed rank-swap collision on }Pl,6.
}
\]

Meanwhile the icosahedron shows that at `S=5` a larger planar host can erase even the remaining mixed/pure distinction.

Thus planar orbital memory depends simultaneously on

\[
\boxed{
\text{capacity placement} + \text{host scale} + \text{available planar regularity}.}
\]

A single scalar threshold in `S` is not enough.

---

## 10. Relation to the polynomial language

The polynomial representation is essential here because scalar minimum boundary does not distinguish many of these states.

For example, at six vertices and `S=6`, every Pareto point lies on

\[
B_A+B_O=12.
\]

Yet `(5,1)` and `(1,5)` have different polynomial supports, while `(4,2)` and `(2,4)` have identical supports.

The scalar boundary sees only `12`; the polynomial sees whether the orbit placement survives.

No planar geometry Laplacian is introduced.

---

## 11. What is now proved, and what is not

Closed:

1. exact planar `Xi` response on six vertices for every `A+O>=4`;
2. exact six-vertex rank-swap criterion `P<=4`;
3. exact `S=5,6,7` memory-class table on six vertices;
4. exact four-vertex calibration from the complete-host theorem;
5. exact twelve-vertex full collapse for all generic-odd interior fibers with total capacity five;
6. explicit `3 -> 2 -> 1` planar host-scale witness for `(4,1)`.

Not closed:

- a classification for arbitrary planar host size;
- the `S=6` and `S=7` behavior at twelve vertices and beyond;
- whether there is a canonical planar analogue of the outerplanar boundary-floor spectrum independent of the host family;
- the full `Omega` semantics beyond the orbit-total projection `Xi`.

---

## 12. Next target

The next hostile target should stay with the icosahedral host and ask:

\[
\boxed{
S=6,7:\quad
\text{which mixed rank swaps survive on }Pl,12?
}
\]

The icosahedron is the natural next laboratory because it is a maximal planar `5`-regular graph. It should test whether the octahedral degree-4 threshold shifts to a degree-5 threshold, or whether icosahedral factorization introduces a more subtle obstruction.

That question should be answered before attempting a general planar theorem.