# HATTER-SOL-11 · Complete Outerplanar Classification of Interior Forgetting Fibers in the Orbit-Total Model

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer; hostile-audit corrections applied.

**Model scope.** This note classifies the two-channel response of the canonical orbit-total projection

\[
\Xi=(A,O)=(a,b+c)
\]

from `ORBITAL_NETWORK_FIBER_SEPARATION.md`. It does not claim completeness for every richer network semantics retaining the full orbital datum `Omega=(a;{b,c})`.

This note closes the outerplanar interior-fiber problem in the `Xi` model for every generic-odd folded pair

\[
P>Q>0.
\]

The mixed/mixed relation was completely classified in `OUTERPLANAR_RANK_SWAP_COMPLETE_CLASSIFICATION.md`. The remaining question was whether either mixed state could collide with the pure-oblique state.

The answer is no.

---

## 1. The three canonical orbit-total states

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

The chain-of-triangles graph `H_n` from `OUTERPLANAR_RANK_SWAP_NO_GO.md` has exactly `2n-3` edges and satisfies

\[
\Delta(H_n)\le4
\]

(with `Delta(H_4)=3` and `Delta(H_n)=4` for even `n>=6`), so it is feasible for every `S>=4` and attains equality. QED.

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

Hence the Type-I state never collides with the pure-oblique state for any interior fiber in the `Xi` model.

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

## 6. Complete interior three-state classification in the `Xi` model

We now combine:

- T11.33: the two mixed states collide iff `(P,Q)=(2,1)`;
- T11.35: Type I never collides with the pure state;
- T11.36: Type II never collides with the pure state.

Define

\[
\nu^{\Xi}_{O,n}(P,Q)
:=
\left|
\left\{
Z_O(P,Q),
Z_O(Q,P),
Z_O(0,P+Q)
\right\}
\right|.
\]

### Theorem T11.37 — complete outerplanar interior-fiber law in the orbit-total model

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
\nu^{\Xi}_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}.
\end{cases}}
\]

Thus the only information loss among the three canonical `Xi` states is the collision

\[
(2,1)\leftrightarrow(1,2).
\]

---

## 7. Publication interpretation

The outerplanar theorem spine is complete for the canonical orbit-total network response:

\[
\boxed{
\Omega
\to
\Xi=(A,O)
\to
Z_O^{\Xi}.
}
\]

The full orbital signature `Omega=(a;{b,c})` contains finer information than `Xi`, and no theorem here asserts that every network model using that finer information has the same collision classes.

The publication statement must preserve this distinction.

---

## 8. Next target

The outerplanar `Xi` classification is closed.

The next mathematical target is planar geometry, beginning with the critical total capacities

\[
S=5,6,7,
\]

where the planar edge ceiling and low-degree constraints change regime.

Continue to use the polynomial-valued response. Do not introduce a geometry Laplacian until a canonical geometry-transition operator is independently justified.