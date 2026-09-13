# HATTER-SOL-11 · Complete Outerplanar Rank-Swap Classification

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.

This note closes the regime left open in `OUTERPLANAR_RANK_SWAP_NO_GO.md`:

\[
P>Q\ge3.
\]

The smallest unresolved laboratory was `(4,3)`. In fact the same argument closes **all** interior fibers at once.

---

## 1. The invariant we need

Fix an even outerplanar host size

\[
n=2m\ge4.
\]

For a two-channel orbital capacity state `(A,O)`, define the axial boundary floor

\[
\boxed{
\mu_{O,n}(A,O)
:=
\min\{B_A:(B_A,B_O)\text{ is feasible in the outerplanar class}\}.
}
\]

A feasible point attaining the minimum `B_A` can be chosen with minimum `B_O` among all such points; that point is Pareto-minimal. Therefore

\[
\boxed{
\mu_{O,n}(A,O)
=
\min\{a:[X^aY^b]Z^{\mathrm{orb}}_{O,n}(A,O;X,Y)\ne0\}.
}
\]

Thus unequal axial floors force unequal response polynomials.

---

## 2. Exact axial floor for capacity `A>=3`

### Theorem T11.31 — exact outerplanar channel floor

For every even

\[
n\ge4
\]

and every second-channel capacity `O>=0`, the minimum axial boundary for an axial capacity `A>=3` is

\[
\boxed{
\mu_{O,n}(A,O)
=
\phi_n(A)
:=
\begin{cases}
2,&A=3,\\
n(A-4)+6,&A\ge4.
\end{cases}}
\]

### Proof: `A=3`

Every outerplanar graph has at least two vertices of total degree at most `2`. At each of those vertices the axial degree is at most `2`, so a uniform axial capacity `3` leaves at least one unused axial port. Hence

\[
B_A\ge2.
\]

The graph `G_m` from `OUTERPLANAR_ORBITAL_MEMORY_21.md` has degree sequence

\[
2,3,3,\ldots,3,2.
\]

Color every edge axial and use no oblique edge. Then the network is connected and

\[
B_A=2.
\]

So the lower bound is sharp.

### Proof: `A>=4`

The axial subgraph is itself outerplanar, hence

\[
|E_A|\le2n-3.
\]

Therefore

\[
B_A
=nA-2|E_A|
\ge
nA-2(2n-3)
=n(A-4)+6.
\]

Take any maximal outerplanar graph on `n` vertices, color every edge axial, and use no oblique edge. It has exactly `2n-3` edges, is connected, and is feasible because every vertex degree is at most `n-1` while only the channel bound matters locally; to make sharpness uniform in `A=4`, use the chain-of-triangles graph `H_n` from `OUTERPLANAR_RANK_SWAP_NO_GO.md`, whose maximum degree is exactly `4`. For `A>=4` the same graph is feasible and has `2n-3` axial edges. Thus equality holds. QED.

---

## 3. Strict monotonicity above the threshold

The function `phi_n` satisfies

\[
\phi_n(3)=2,
\qquad
\phi_n(4)=6,
\]

and for `A>=4`,

\[
\phi_n(A+1)-\phi_n(A)=n>0.
\]

Hence

\[
\boxed{
A>B\ge3
\Longrightarrow
\phi_n(A)>\phi_n(B).
}
\]

So once both swapped channels are at least `3`, the minimum exponent of `X` already remembers which channel carries the larger capacity.

---

## 4. Close the unresolved regime `P>Q>=3`

Let

\[
P>Q\ge3.
\]

The two rank-swapped orbital states are

\[
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P).
\]

By T11.31,

\[
\min_X Z_I=\phi_n(P),
\qquad
\min_X Z_{II}=\phi_n(Q).
\]

Strict monotonicity gives

\[
\phi_n(P)>\phi_n(Q).
\]

Therefore

\[
\boxed{
Z^{\mathrm{orb}}_{O,n}(P,Q;X,Y)
\ne
Z^{\mathrm{orb}}_{O,n}(Q,P;X,Y)
}
\]

for every even `n>=4`.

### Theorem T11.32 — high-capacity rank-swap no-go

For every generic-odd interior fiber with

\[
\boxed{P>Q\ge3}
\]

and every even outerplanar host of size at least four, the two rank-swapped canonical orbital states remain distinguishable by the full outerplanar response.

No outerplanar rank-swap collision exists in this regime.

---

## 5. The `(4,3)` laboratory

The smallest formerly unresolved case is now immediate.

For Type I

\[
(4,3),
\]

T11.31 gives

\[
\boxed{
\min B_A=\phi_n(4)=6.
}
\]

For Type II

\[
(3,4),
\]

\[
\boxed{
\min B_A=\phi_n(3)=2.
}
\]

Hence

\[
\boxed{
Z_O(4,3)\ne Z_O(3,4)
}
\]

on every even outerplanar host `n>=4`.

The gap in the smallest axial exponent is exactly

\[
\boxed{4.}
\]

independently of host size.

---

## 6. Complete rank-swap classification

We can now combine three earlier layers:

1. `OUTERPLANAR_ORBITAL_MEMORY_21.md` proves

\[
Z_O(2,1)=Z_O(1,2)
\]

for every even `n>=4`.

2. T11.30 in `OUTERPLANAR_RANK_SWAP_NO_GO.md` proves separation for

\[
P\ge3,
\qquad
Q\in\{1,2\}.
\]

3. T11.32 proves separation for

\[
P>Q\ge3.
\]

These cases exhaust all integers

\[
P>Q>0.
\]

### Theorem T11.33 — complete outerplanar rank-swap classification

For every generic-odd interior forgetting fiber

\[
P>Q>0
\]

and every even outerplanar host

\[
n=2m\ge4,
\]

we have

\[
\boxed{
Z^{\mathrm{orb}}_{O,n}(P,Q;X,Y)
=
Z^{\mathrm{orb}}_{O,n}(Q,P;X,Y)
\iff
(P,Q)=(2,1).
}
\]

Thus the unique rank-swapped mixed-state collision in the entire generic-odd interior family is

\[
\boxed{(2,1)\leftrightarrow(1,2).}
\]

There is no infinite hidden collision family at larger capacities.

---

## 7. Why `(2,1)` is unique

The classification is controlled by the outerplanar degree threshold.

For a channel capacity `A`:

- `A=1` can be saturated by a perfect matching;
- `A=2` can be saturated by a Hamiltonian cycle;
- `A=3` already has an unavoidable defect `2` because every outerplanar graph has at least two vertices of degree at most `2`;
- `A>=4` is governed by the global outerplanar edge ceiling `2n-3`, producing the strictly increasing floor

\[
n(A-4)+6.
\]

Therefore capacities `1` and `2` lie in the same zero-floor phase, while every capacity from `3` upward occupies its own strictly separated boundary-floor level.

The pair `(2,1)` is the only strictly ordered positive pair whose two capacities lie inside that same zero-floor phase.

This explains the collision structurally rather than experimentally.

---

## 8. Boundary-floor spectrum

For the rank-swap problem it is useful to record the effective outerplanar floor spectrum

\[
\boxed{
1,2\mapsto0,
\qquad
3\mapsto2,
\qquad
A\ge4\mapsto n(A-4)+6.
}
\]

For the low-capacity values `1,2`, the zero floor assumes the complementary channel is large enough to supply connectivity; that is exactly the situation in the rank-swapped fibers covered by T11.30. The `(2,1)` case is handled separately by its exact full response theorem.

The key point is that the spectrum has exactly one nontrivial degeneracy:

\[
\boxed{\phi(1)=\phi(2)=0.}
\]

That degeneracy is the source of the unique rank-swap collision.

---

## 9. Small-host polynomial microscope for `(4,3)`

At the smallest common host

\[
n=4,
\]

a maximal outerplanar graph is `K_4` minus one edge and has five edges and maximum degree three. Thus neither capacity `3` nor capacity `4` restricts any edge coloring.

For `(4,3)`, if `r` of the five edges are axial,

\[
B_A=16-2r,
\qquad
B_O=12-2(5-r).
\]

Therefore

\[
\boxed{
Z_{O,4}(4,3)
=
X^{16}Y^2
+X^{14}Y^4
+X^{12}Y^6
+X^{10}Y^8
+X^8Y^{10}
+X^6Y^{12}.
}
\]

For `(3,4)`,

\[
\boxed{
Z_{O,4}(3,4)
=
X^{12}Y^6
+X^{10}Y^8
+X^8Y^{10}
+X^6Y^{12}
+X^4Y^{14}
+X^2Y^{16}.
}
\]

The four middle monomials coincide, but the two extreme monomials on each side reveal the rank placement.

This is the same qualitative mechanism seen in `(3,1)`, now entirely inside the high-capacity regime.

---

## 10. Consequence for the dimensional-memory programme

The outerplanar stage is now much more rigid than the first `(2,1)` experiment suggested.

For mixed interior fibers:

\[
\boxed{
\text{outerplanar geometry forgets the rank swap only at }(2,1).
}
\]

So the exact staircase

\[
3\to2\to1
\]

found for `(2,1)` is a minimal exceptional phenomenon, not the generic dimensional law.

For every other interior fiber, at least the two mixed orbital members remain distinct in the outerplanar class.

The remaining question is no longer rank-swap collision. It is the **full three-state class count**:

> when, if ever, can one of the mixed states collide with the pure-oblique state `(0,P+Q)` in outerplanar geometry?

That is the next genuine open outerplanar problem.

---

## 11. Next target

Define

\[
\nu_{O,n}(P,Q)
=
\left|
\left\{
Z_O(P,Q),
Z_O(Q,P),
Z_O(0,P+Q)
\right\}
\right|.
\]

T11.33 fixes the mixed/mixed relation completely.

The next hostile target is to classify mixed/pure collisions:

\[
Z_O(P,Q)=Z_O(0,P+Q)
\quad\text{or}\quad
Z_O(Q,P)=Z_O(0,P+Q).
\]

The smallest already-known example is `(2,1)`, where the pure-oblique state remains distinct. The next tests should determine whether

\[
\boxed{\nu_{O,n}(P,Q)=3}
\]

for every interior fiber except `(2,1)`, which has `nu=2`, or whether a second exceptional family exists.