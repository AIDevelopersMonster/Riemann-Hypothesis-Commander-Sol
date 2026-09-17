# QGE3 LQR — Pfaffian Parity Route to the r=7 Fifteen-Plane Barrier

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** pure defect-two synchronization at `r=7`  
**Current target:** prove that every compatible fifteen-plane family has an even number of normalized resolutions

This note records a new algebraic route to the open bound `M_7<=14`. It does **not** yet prove the bound, but it converts the existence of a second resolution into a mod-2 mixed-Pfaffian problem and records strong threshold evidence that is absent at `q=14` and appears at `q=15`.

---

## 1. Complement graph and color matrices

For a compatible pure-plane family `F` with `q` source colors, fix phase `0` and write

\[
P_a=\{A_a,U_a,V_a\},\qquad 0\in A_a,\qquad M_a=X\setminus A_a=U_a\sqcup V_a.
\]

Let the `2q` unmarked block occurrences be the vertices of the complement graph `K(F)`. For every target color `a`, the color-`a` edges are all unordered pairs `B,C` satisfying

\[
B\cap C=\varnothing,\qquad B\cup C=M_a.
\]

Every color class is a matching.

Let `A_a` now denote the `2q x 2q` alternating adjacency matrix over `F_2` of the color-`a` matching. Introduce commuting color variables `z_1,...,z_q` and define

\[
A(z)=\sum_{a=1}^q z_a A_a.
\]

The Pfaffian polynomial

\[
P_F(z)=\operatorname{Pf} A(z)
\]

has one monomial for every perfect matching of the complement graph, with the product of the colors of its edges.

Therefore the coefficient

\[
\boxed{[z_1z_2\cdots z_q]P_F(z)}
\]

is exactly the parity of the number of rainbow perfect matchings using every target color once, hence exactly the parity of normalized quotient colorings/resolutions.

In particular, a synchronizing family must satisfy

\[
[z_1\cdots z_q]P_F(z)=1.
\]

---

## 2. Boolean Möbius form

Over `F_2`, the top squarefree coefficient of a multilinear Boolean polynomial can be recovered by summing all Boolean evaluations. Hence

\[
\boxed{
[z_1\cdots z_q]P_F(z)
=
\bigoplus_{S\subseteq[q]}
\operatorname{Pf}\left(\sum_{a\in S}A_a\right).
}
\]

For an alternating matrix over `F_2`, Pfaffian parity equals determinant parity, because

\[
\det A=(\operatorname{Pf}A)^2
\]

and squaring fixes `0,1` in `F_2`. Thus the same quantity is computable by Gaussian elimination alone:

\[
\boxed{
[z_1\cdots z_q]P_F(z)
=
\bigoplus_{S\subseteq[q]}
\det\left(\sum_{a\in S}A_a\right).
}
\]

This gives a deterministic mod-2 verifier that never enumerates resolutions explicitly.

---

## 3. Exterior-algebra interpretation

Let `e_1,...,e_{2q}` be the port basis and associate to color `a` the 2-form

\[
\omega_a=\sum_{ij\in E_a} e_i\wedge e_j.
\]

Then

\[
\omega_1\omega_2\cdots\omega_q
\]

has top-degree coefficient equal to the same rainbow-resolution parity.

Over characteristic two every 2-form satisfies

\[
\boxed{\omega^2=0.}
\]

Indeed, writing `omega` as a sum of basis bivectors, every square term vanishes because a basis vector repeats, while every cross-term occurs twice.

This immediately implies that linear dependence of the `omega_a` would force zero rainbow parity. However, this criterion is not sufficient for the fifteen-plane problem: the fifteen color forms of the current near-extremal fifteen-plane family are linearly independent. The desired vanishing is therefore a genuinely higher wedge relation, not an ordinary rank deficiency.

---

## 4. Threshold evidence

The exact parity routine was tested on random compatible pure-plane packings.

Observed samples:

```text
q=13 : both odd and even rainbow-resolution parity occur
q=14 : both odd and even rainbow-resolution parity occur
q=15 : 352 tested compatible packings, all even
q=16 : tested compatible packings, all even
```

The known synchronizing fourteen-plane construction has parity

\[
\boxed{1}.
\]

The near-extremal fifteen-plane family

```text
(0, 42, 73, 78, 145, 148, 149, 166, 186, 198, 224, 236, 271, 275, 288)
```

has exactly two normalized resolutions (canonical plus one alternative), hence parity

\[
\boxed{0}.
\]

No compatible fifteen-plane family with odd parity has been found.

These computations are evidence only; no exhaustive parity theorem is claimed here.

---

## 5. Algebraic-normal-form degree

Define the Boolean function

\[
f_F(S)=\operatorname{Pf}\left(\sum_{a\in S}A_a\right)\in F_2.
\]

Equivalently, `f_F(S)` is the parity of ordinary perfect matchings in the graph obtained by retaining the color classes indexed by `S`.

The top rainbow coefficient is the full-degree ANF coefficient of `f_F`. Therefore

\[
\deg_{\mathrm{ANF}} f_F<q
\quad\Longrightarrow\quad
[z_1\cdots z_q]P_F(z)=0.
\]

For the known synchronizing fourteen-plane construction,

\[
\boxed{\deg f_F=14},
\]

and its degree-14 ANF layer consists of the unique full monomial.

For the near-extremal fifteen-plane family above,

\[
\boxed{\deg f_F=13}.
\]

Thus its even rainbow parity arises through an actual drop of Boolean algebraic degree, not through a trivial translation symmetry of `f_F`.

---

## 6. Failed simplifications

Several simpler mod-2 mechanisms have been tested and rejected.

### 6.1 Linear dependence of color 2-forms

False as a universal explanation: the fifteen color forms of the near-extremal family have full linear rank `15`.

### 6.2 Translation symmetry of the Pfaffian parity function

It would suffice to have a nonzero `H subseteq [q]` such that

\[
f_F(S)=f_F(S\triangle H)
\]

for all `S`, because the Boolean cube would pair off. The near-extremal fifteen-plane family has no such nontrivial translation period.

### 6.3 Unoriented projective-line replacement

Every partition plane is a projective line

\[
\{u,v,u+v\}\subset PG(5,2),
\]

and the 15 canonical planes occupy 45 distinct points. Counting decompositions of those 45 points into partition-realizable projective lines gives the correct parity on the principal fourteen- and fifteen-plane test objects. However, it disagrees with true resolution parity for some smaller compatible families. The loss is exactly the marked/unmarked orientation and set-disjointness condition. Thus a proof cannot simply forget the Boolean orientation.

---

## 7. The proposed parity theorem

The sharp algebraic target is now:

### Pfaffian Parity Conjecture for `r=7`
For every compatible family of fifteen partition planes on seven phases,

\[
\boxed{
[z_1z_2\cdots z_{15}]
\operatorname{Pf}\left(\sum_{a=1}^{15}z_aA_a\right)=0.
}
\]

Equivalently, every such family has an even number of normalized resolutions.

Since the canonical resolution always exists, even parity would force at least one noncanonical resolution. Therefore the conjecture implies

\[
M_7\le14.
\]

Combined with the explicit synchronizing fourteen-plane family already constructed,

\[
\boxed{M_7=14}.
\]

A sufficient stronger statement would be

\[
\boxed{\deg_{\mathrm{ANF}} f_F\le14}
\]

for every compatible fifteen-plane family.

---

## 8. Why this route is preferable to further core enumeration

The minimal-trade orbit counts already grow as

\[
6,\ 25,\ 162,\ 1908
\]

for supports `3,4,5,6`, with genuine higher-support trades also present. A direct forbidden-core catalogue therefore grows too quickly.

The Pfaffian route compresses the entire obstruction hypergraph into one mixed coefficient. It has three advantages:

1. it treats all support sizes simultaneously;
2. it is compatible with exact linear algebra over `F_2`;
3. it suggests a route to a general theorem via exterior-algebra nilpotence or ANF-degree bounds.

The next attack should therefore identify a structural reason, specific to the six Boolean coordinates and the 45-of-63 compatible-state density, that forces the top mixed Pfaffian coefficient to vanish.

---

## 9. Current rigorous status

Nothing in this note changes the proven numerical bound

\[
\boxed{14\le M_7\le21.}
\]

The parity-vanishing statement is at present a sharply formulated conjecture supported by exact computation, not yet a theorem.
