# HATTER-SOL-11 · Complete Outerplanar Classification of Interior Forgetting Fibers

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.

This note closes the outerplanar interior-fiber problem for every generic-odd folded pair

\[
P>Q>0.
\]

The mixed/mixed relation was completely classified in `OUTERPLANAR_RANK_SWAP_COMPLETE_CLASSIFICATION.md`. The remaining question was whether either mixed state could collide with the pure-oblique state.

The answer is no.

---

## 1. The three canonical orbital states

Fix a generic-odd interior forgetting fiber

\[
P>Q>0,
\qquad
S:=P+Q.
\]

Its three canonical orbit-total states are

\[
\boxed{
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,S).
}
\]

Let the outerplanar host size be even:

\[
n=2m\ge4.
\]

Write

\[
Z_I:=Z^{\mathrm{orb}}_{O,n}(P,Q;X,Y),
\]

\[
Z_{II}:=Z^{\mathrm{orb}}_{O,n}(Q,P;X,Y),
\]

\[
Z_{III}:=Z^{\mathrm{orb}}_{O,n}(0,S;X,Y).
\]

---

## 2. Exact pure-oblique outerplanar response

The pure-oblique state has only one channel. Therefore its Pareto front is a singleton at the minimum possible oblique boundary.

### Proposition T11.34 — pure-channel boundary law

For every integer

\[
S\ge3
\]

and every even

\[
n\ge4,
\]

\[
\boxed{
Z^{\mathrm{orb}}_{O,n}(0,S;X,Y)
=
Y^{\psi_n(S)},
}
\]

where

\[
\boxed{
\psi_n(S)=
\begin{cases}
2,&S=3,\\
n(S-4)+6,&S\ge4.
\end{cases}}
\]

### Proof

If `S=3`, every outerplanar graph has at least two vertices of degree at most `2`, so the unused capacity is at least `2`. The extremal graph `G_m` from `OUTERPLANAR_ORBITAL_MEMORY_21.md` has degree sequence

\[
2,3,3,\ldots,3,2
\]

and attains boundary `2`.

If `S>=4`, every outerplanar graph has at most `2n-3` edges, hence

\[
B_O\ge nS-2(2n-3)=n(S-4)+6.
\]

The chain-of-triangles graph `H_n` from `OUTERPLANAR_RANK_SWAP_NO_GO.md` has exactly `2n-3` edges and maximum degree `4`, so it is feasible for every `S>=4` and attains equality. QED.

---

## 3. Type I can never equal the pure state

Recall

\[
\Xi_I=(P,Q).
\]

If

\[
P\ge3,
\]

then Theorem T11.31 gives a strictly positive minimum axial boundary:

\[
\boxed{
\min B_A=
\phi_n(P)>0.
}
\]

Thus every monomial of `Z_I` contains a positive power of `X`, whereas `Z_{III}` contains only the single monomial

\[
Y^{\psi_n(S)}.
\]

Therefore

\[
Z_I\ne Z_{III}.
\]

The only interior pair with `P<3` is

\[
(P,Q)=(2,1).
\]

That case was solved exactly in `OUTERPLANAR_ORBITAL_MEMORY_21.md`:

\[
Z_I=X^2+Y^2,
\qquad
Z_{III}=Y^2.
\]

Hence the Type-I state never collides with the pure-oblique state for any interior fiber.

### Theorem T11.35 — Type-I / pure separation

For every

\[
P>Q>0
\]

and every even outerplanar host `n>=4`,

\[
\boxed{
Z_O(P,Q)\ne Z_O(0,P+Q).
}
\]

---

## 4. Type II when `Q>=3`

Now consider

\[
\Xi_{II}=(Q,P).
\]

If

\[
Q\ge3,
\]

Theorem T11.31 again gives

\[
\min B_A=\phi_n(Q)>0.
\]

Thus `Z_{II}` has no monomial with zero `X` exponent, while `Z_{III}` is a pure `Y` monomial.

Therefore

\[
\boxed{
Q\ge3
\Longrightarrow
Z_{II}\ne Z_{III}.
}
\]

The only unresolved cases are

\[
Q=1
\quad\text{or}\quad
Q=2.
\]

---

## 5. Type II when `Q=1,2`

Here the axial channel may be fully saturated, so zero `X` exponent no longer separates the responses.

Instead, compare the **minimum oblique boundary**.

The oblique channel of Type II has capacity `P>=3`. By channel symmetry of T11.31,

\[
\boxed{
\min B_O=\phi_n(P),
}
\]

where

\[
\phi_n(P)=
\begin{cases}
2,&P=3,\\
n(P-4)+6,&P\ge4.
\end{cases}
\]

Choose, among all feasible networks with `B_O=\phi_n(P)`, one with minimum `B_A`. Its boundary vector is Pareto-minimal. Therefore `Z_{II}` contains a monomial whose `Y` exponent is exactly

\[
\phi_n(P).
\]

The pure state has only the exponent

\[
\psi_n(P+Q).
\]

We now compare them.

### Case `P=3`

Since `P>Q`, we have `Q=1` or `2`. Then

\[
\phi_n(3)=2.
\]

But

\[
\psi_n(4)=6,
\]

and

\[
\psi_n(5)=n+6.
\]

Hence

\[
\psi_n(P+Q)>\phi_n(P).
\]

### Case `P>=4`

Then

\[
\phi_n(P)=n(P-4)+6,
\]

while

\[
\psi_n(P+Q)=n(P+Q-4)+6.
\]

Therefore

\[
\boxed{
\psi_n(P+Q)-\phi_n(P)=nQ>0.
}
\]

Thus in every low-`Q` case the Type-II response contains a Pareto monomial with strictly smaller `Y` exponent than the only monomial of the pure-oblique response.

Hence equality is impossible.

### Theorem T11.36 — Type-II / pure separation

For every

\[
P>Q>0
\]

and every even outerplanar host `n>=4`,

\[
\boxed{
Z_O(Q,P)\ne Z_O(0,P+Q).
}
\]

---

## 6. Complete interior three-state classification

We now combine:

- T11.33: the two mixed states collide iff `(P,Q)=(2,1)`;
- T11.35: Type I never collides with the pure state;
- T11.36: Type II never collides with the pure state.

Define

\[
\nu_{O,n}(P,Q)
:=
\left|
\left\{
Z_O(P,Q),
Z_O(Q,P),
Z_O(0,P+Q)
\right\}
\right|.
\]

### Theorem T11.37 — complete outerplanar interior-fiber law

For every generic-odd interior forgetting fiber

\[
P>Q>0
\]

and every even outerplanar host

\[
n=2m\ge4,
\]

\[
\boxed{
\nu_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}.
\end{cases}}
\]

Equivalently:

- the unique nontrivial outerplanar collision is

\[
\boxed{
(2,1)\leftrightarrow(1,2);
}
\]

- the pure-oblique state is never identified with either mixed state;
- every other interior fiber remains fully resolved by the outerplanar polynomial response.

This completely solves the outerplanar classification for generic-odd interior fibers.

---

## 7. Structural interpretation

The result is sharper than the first dimensional-memory staircase suggested.

Strict 1D preserves all interior orbital states:

\[
\nu_P=3.
\]

Outerplanar geometry performs only one exceptional identification:

\[
\boxed{
(2,1)\sim(1,2),
}
\]

because capacities `1` and `2` are exactly the two positive uniform channel capacities that can still occupy the outerplanar zero-floor phase.

All capacities `>=3` carry a positive, strictly ordered boundary floor. That floor prevents further rank-swap collapse.

The pure-oblique state remains distinguishable because concentrating the entire total capacity `P+Q` in one orbit raises the optimal single-channel boundary above the minimum boundary visible in the mixed state, except in the already separately solved `(2,1)` case where the full polynomial still separates it.

So outerplanar geometry is much less destructive than planar/unrestricted geometry:

\[
\boxed{
\text{it forgets exactly one mixed rank swap and nothing else in the interior family.}
}
\]

---

## 8. Polynomial witness hierarchy

The classification can be read from three increasingly strong polynomial witnesses.

### Witness 1 — zero `X` exponent

If one mixed state's axial capacity is at least `3`, a positive axial floor prevents any zero-`X` monomial.

### Witness 2 — minimum `X` exponent

For both capacities at least `3`, the strict monotonicity

\[
\phi_n(P)>\phi_n(Q)
\]

distinguishes the rank swap.

### Witness 3 — minimum `Y` exponent

When the axial capacity is `1` or `2`, zero-`X` no longer helps. The minimum oblique exponent

\[
\phi_n(P)
\]

still lies strictly below the pure-oblique exponent

\[
\psi_n(P+Q),
\]

and separates the mixed state from the pure one.

Thus the full classification does not require enumerating every Pareto monomial for every pair. A small set of extremal polynomial exponents suffices.

---

## 9. Publication significance

HATTER-SOL-11 now has, for generic odd discriminant worlds:

1. a canonical symmetry-resolved orbital geodesic object;
2. an exact forgetting map to the published `(P,Q)` pair;
3. a complete classification of the forgetting-map fibers;
4. proof that the hidden orbital information is operationally visible to networks;
5. exact host-scale forgetting on unrestricted even complete hosts;
6. exact permanent memory in strict 1D;
7. an exact dimensional staircase for the minimal `(2,1)` fiber;
8. a complete outerplanar classification for every interior fiber.

This is now beyond an exploratory note. The branch has a coherent theorem spine suitable for assembling a publication candidate, subject to hostile audit and consolidation of duplicated lemmas.

---

## 10. Next target

The next mathematical frontier is planar geometry.

The coarse edge-density obstruction already shows that pure total capacity

\[
S\ge6
\]

cannot fully close in a planar graph, while smaller capacities can.

The natural next question is the planar analogue of T11.37:

> classify the number of distinct orbital response classes for every generic-odd interior fiber under planar geometry.

The first hostile tests should be organized by total capacity

\[
S=P+Q,
\]

with critical values around

\[
S=5,6,7,
\]

because `S=6` is exactly where the planar edge-density obstruction changes the saturation regime.

Before extending further, the present outerplanar theorem spine should undergo a hostile proof audit, especially the shared use of the extremal graphs `G_m` and `H_n` and the exact polynomial claims at small host sizes.