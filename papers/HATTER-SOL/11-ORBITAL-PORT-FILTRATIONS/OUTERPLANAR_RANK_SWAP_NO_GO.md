# HATTER-SOL-11 · Outerplanar Rank-Swap No-Go Beyond the `(2,1)` Exception

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer; hostile-audit corrections applied.

**Model scope.** All network responses in this note are responses of the canonical orbit-total projection

\[
\Xi=(A,O)=(a,b+c)
\]

from `ORBITAL_NETWORK_FIBER_SEPARATION.md`. They do not claim completeness for every richer network semantics retaining the full unordered oblique pair in `Omega=(a;{b,c})`.

This note attacks the hostile target left by `OUTERPLANAR_ORBITAL_MEMORY_21.md`: is the outerplanar collision

\[
(P,Q)=(2,1):
\qquad
(P,Q)\sim(Q,P)
\]

a universal rank-swap law, or a special subcubic phenomenon?

It is special.

---

## 1. Outerplanar low-degree obstruction revisited

Every finite simple outerplanar graph on at least two vertices has at least two vertices of total degree at most `2`.

Let a channel have uniform capacity `H>=3` on every vertex. Then at each of those two low-degree vertices the channel degree is at most `2`, regardless of how the other channel is used.

Hence its aggregate boundary satisfies

\[
\boxed{
B_H\ge2(H-2).
}
\]

In particular, a channel of capacity at least `3` can never have zero outerplanar boundary.

This is the structural reason why the `(2,1)` laboratory is exceptional: capacity `2` is exactly the largest uniform channel capacity that can still be saturated at the unavoidable low-degree outerplanar vertices.

---

## 2. A universal maximal outerplanar test graph

For

\[
n=2m\ge4,
\]
let `H_n` be the graph on vertices

\[
1,2,\ldots,n
\]
with edges

\[
\boxed{
\{i,i+1\},\quad1\le i\le n-1,
}
\]

and

\[
\boxed{
\{i,i+2\},\quad1\le i\le n-2.
}
\]

Equivalently, start with the triangle on `1,2,3` and repeatedly add vertex `j` adjacent to `j-1,j-2`.

This is a chain of triangles, hence outerplanar, and has

\[
(n-1)+(n-2)=2n-3
\]

edges, so it is maximal outerplanar.

For `n=4` its degree sequence is

\[
2,3,3,2,
\]

while for even `n>=6` it is

\[
2,3,4,\ldots,4,3,2.
\]

Therefore the uniform statement used below is

\[
\boxed{
\Delta(H_n)\le4,
}
\]

with `Delta(H_4)=3` and `Delta(H_n)=4` for even `n>=6`.

This one graph will provide all hostile witnesses below.

---

## 3. Capacity-1 channel can be saturated

Take the perfect matching

\[
\boxed{
M_1=
\{\{1,2\},\{3,4\},\ldots,\{n-1,n\}\}.
}
\]

Color `M_1` by a channel of capacity `1` and every remaining edge of `H_n` by the other channel.

Every vertex has exactly one capacity-1 incidence, so that channel is saturated.

Since removing the matching lowers every vertex degree by one,

\[
\deg_{H_n-M_1}(v)\le3.
\]

Therefore the complementary channel is feasible for every capacity

\[
P\ge3.
\]

So for the orbital state

\[
(1,P),
\qquad P\ge3,
\]
there exists an outerplanar feasible network with

\[
\boxed{B_A=0.}
\]

Among all feasible networks with `B_A=0`, choose one minimizing `B_O`. Its boundary vector lies on the Pareto front. Hence the outerplanar response of `(1,P)` always contains a monomial with zero `X` exponent.

---

## 4. Capacity-2 channel can also be saturated

The same graph has the Hamiltonian cycle

\[
\boxed{
C_n:
1,2,4,6,\ldots,n,
 n-1,n-3,\ldots,3,1.
}
\]

Every consecutive pair in this ordering differs by `1` or `2`, so every cycle edge belongs to `H_n`.

Color this Hamiltonian cycle by a channel of capacity `2`.

Every vertex then has exactly two incidences in that channel, so it is saturated.

The complementary graph `H_n-C_n` has degree at most

\[
\Delta(H_n)-2\le2
\]

at every vertex. Therefore it is feasible in the other channel for every

\[
P\ge2.
\]

Consequently the orbital state

\[
(2,P),
\qquad P\ge3,
\]
also has an outerplanar Pareto response containing a point with

\[
\boxed{B_A=0.}
\]

---

## 5. Rank-swap no-go for `Q=1,2`

Now take a generic-odd interior forgetting fiber

\[
P>Q>0.
\]

Its two rank-swapped orbit-total states are

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P).
\]

### Theorem T11.30 — outerplanar rank-swap separation for `Q<=2`

Let

\[
P\ge3,
\qquad
Q\in\{1,2\},
\qquad
n=2m\ge4.
\]

Then

\[
\boxed{
\mathcal R^{\mathrm{orb}}_{O,n}(P,Q)
\ne
\mathcal R^{\mathrm{orb}}_{O,n}(Q,P).
}
\]

Equivalently,

\[
\boxed{
Z^{\mathrm{orb}}_{O,n}(P,Q;X,Y)
\ne
Z^{\mathrm{orb}}_{O,n}(Q,P;X,Y).
}
\]

### Proof

In Type I, the axial channel has capacity `P>=3`. By the outerplanar low-degree obstruction,

\[
B_A\ge2(P-2)>0
\]

for every feasible network. Therefore no monomial of its response polynomial has `X` exponent zero.

In Type II, the axial channel has capacity `Q`.

- If `Q=1`, Section 3 constructs a feasible outerplanar network with `B_A=0`.
- If `Q=2`, Section 4 constructs one with `B_A=0`.

Taking a Pareto-minimal boundary vector among those with zero axial boundary shows that the Type-II response contains a monomial with zero `X` exponent.

Hence the two response polynomials cannot be equal. QED.

---

## 6. Low-`Q` classification

Combine T11.30 with the exact `(2,1)` theorem from `OUTERPLANAR_ORBITAL_MEMORY_21.md`.

### Corollary T11.30a — complete low-`Q` rank-swap picture

For generic-odd interior fibers with

\[
Q\le2
\]

on every even outerplanar host of size at least four:

- `(P,Q)=(2,1)` is the unique proved rank-swap collision family;
- every `P>=3`, `Q=1` remains rank-swap distinguishable;
- every `P>=3`, `Q=2` remains rank-swap distinguishable.

Thus the outerplanar identity

\[
(P,Q)\sim(Q,P)
\]

is **not** a generic law. The `(2,1)` collapse is tied to the outerplanar degree-2 floor.

---

## 7. Exact calibration: the `(3,1)` fiber

The first hostile counterexample is already

\[
(P,Q)=(3,1).
\]

We can compute its complete outerplanar Pareto fronts exactly for every even

\[
n=2m\ge4.
\]

For Type I `(3,1)`, the low-degree obstruction gives

\[
B_A\ge2.
\]

Also every outerplanar graph has at most `2n-3` edges, so total boundary satisfies

\[
B_A+B_O\ge4n-2(2n-3)=6.
\]

Both coordinates are even.

On the maximal outerplanar graph `H_n`, define the matching

\[
M_{m-2}
=
\{\{3,4\},\{5,6\},\ldots,\{n-3,n-2\}\}.
\]

It covers every degree-4 vertex (vacuously at `n=4`). Coloring this matching by the capacity-1 channel and the complement by the capacity-3 channel gives

\[
(B_A,B_O)=(2,4).
\]

Adding the edge `{1,2}` to the matching gives

\[
(4,2),
\]

and adding also `{n-1,n}` gives the perfect matching

\[
(6,0).
\]

Therefore

\[
\boxed{
\mathcal R_O(3,1)
=
\{(2,4),(4,2),(6,0)\}.
}
\]

By channel exchange,

\[
\boxed{
\mathcal R_O(1,3)
=
\{(0,6),(2,4),(4,2)\}.
}
\]

Hence

\[
\boxed{
Z_O(3,1)=X^2Y^4+X^4Y^2+X^6,
}
\]

\[
\boxed{
Z_O(1,3)=Y^6+X^2Y^4+X^4Y^2.
}
\]

The rank swap is visible for every even host size at least four.

For the pure-oblique member `(0,4)`, the same graph `H_n` is feasible because its maximum degree is at most four, so

\[
\boxed{
\mathcal R_O(0,4)=\{(0,6)\},
\qquad
Z_O(0,4)=Y^6.
}
\]

Thus the `(3,1)` fiber retains all three canonical orbit-total members under the full outerplanar response:

\[
\boxed{
\nu_{O,2m}(3,1)=3
\qquad(m\ge2).
}
\]

This is the direct hostile counterexample to any naive extension of the `(2,1)` staircase.

---

## 8. Exact calibration: the diagonal `(2,2)` fiber

For

\[
(P,Q)=(2,2),
\]
the generic-odd fiber has only two canonical orbital signatures, whose orbit-total states are

\[
\Xi_D=(2,2),
\qquad
\Xi_O=(0,4).
\]

On `H_n`, color all distance-one edges

\[
\{i,i+1\}
\]
by the first channel and all distance-two edges

\[
\{i,i+2\}
\]
by the second. Each monochromatic subgraph has maximum degree at most two. Since `H_n` has `2n-3` edges, this gives

\[
(B_A,B_O)=(2,4).
\]

Swapping colors gives

\[
(4,2).
\]

Coloring the Hamiltonian cycle `C_n` by the first channel and its complement by the second gives

\[
(0,6),
\]

because the complement has maximum degree at most two. Swapping gives

\[
(6,0).
\]

The outerplanar edge bound forces total boundary at least six, and both coordinates are even. Hence these are exactly all Pareto-minimal possibilities:

\[
\boxed{
\mathcal R_O(2,2)
=
\{(0,6),(2,4),(4,2),(6,0)\}.
}
\]

Therefore

\[
\boxed{
Z_O(2,2)=Y^6+X^2Y^4+X^4Y^2+X^6.
}
\]

The pure-oblique member remains

\[
\boxed{
Z_O(0,4)=Y^6.
}
\]

So the diagonal fiber remains nontrivially separated in the orbit-total outerplanar model.

---

## 9. What the `(2,1)` result really meant

The previous exact staircase

\[
(2,1):
\qquad
3\to2\to1
\]

might have suggested that outerplanarity generically forgets which mixed orbit carries the larger folded coordinate.

T11.30 disproves that interpretation.

The correct structural reading is:

\[
\boxed{
\text{outerplanar graphs force low-degree vertices, and capacity }2
\text{ sits exactly at that threshold.}
}
\]

For `(2,1)`, either mixed state can accommodate the unavoidable degree-2 vertices without leaving a compulsory defect in its larger channel. This permits the two mixed Pareto fronts to coincide.

Once the larger channel has capacity at least `3`, the low-degree vertices force a visible residual defect in whichever coordinate carries that larger capacity.

So the `(2,1)` collapse is a **threshold phenomenon**, not a symmetry law.

---

## 10. Relation to the polynomial viewpoint

The response polynomial exposes the distinction immediately.

For `(2,1)`:

\[
Z_O(2,1)=Z_O(1,2)=X^2+Y^2.
\]

For `(3,1)`:

\[
Z_O(3,1)-Z_O(1,3)=X^6-Y^6\ne0.
\]

The two shared middle monomials survive, but the extreme monomial records which channel carries the capacity-3 obstruction.

This is exactly the sort of information that a scalar total boundary would miss: both fronts have scalar minimum `6`, yet the polynomial response distinguishes them.

---

## 11. What is now closed

Within the orbit-total `Xi` model we now have:

1. exact outerplanar collapse for `(2,1)`;
2. a general low-degree obstruction `B_H>=2(H-2)` for any channel capacity `H>=3`;
3. a universal maximal outerplanar test graph `H_n` with `Delta(H_n)<=4`;
4. saturation constructions for capacity-1 and capacity-2 channels;
5. an infinite no-go family proving rank-swap separation for every `P>=3`, `Q=1,2`;
6. exact full outerplanar polynomials for `(3,1)` and `(2,2)`.

Thus the naive universal outerplanar rule `I=II` is dead in the `Xi` response model.

---

## 12. Next target

The unresolved regime now begins at

\[
\boxed{P>Q\ge3.}
\]

There the low-degree obstruction hits **both** rank-swapped channels, so the zero-exponent witness used in T11.30 no longer separates them.

The next hostile question is therefore:

> for `P>Q>=3`, can the two outerplanar rank-swapped orbit-total response polynomials ever coincide, or does the asymmetry survive in a subtler boundary profile?

The smallest test is

\[
\boxed{(P,Q)=(4,3).}
\]

This is now the correct next laboratory.