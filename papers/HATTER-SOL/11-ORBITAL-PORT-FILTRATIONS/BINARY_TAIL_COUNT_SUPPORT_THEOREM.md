# HATTER-SOL-11 · Binary-tail count-sector support theorem

Status: closed combinatorial theorem layer.

This note abstracts the mechanism behind T11.19. It is independent of the numerical capacities `(1,0)` and `(17,0)` and applies to any single conjugate binary-tail species appearing with balanced multiplicity.

---

## 1. Setup

Let

\[
I_+,\ I_- = \overline{I_+}
\]

be a conjugate factor-ideal pair belonging to one binary-tail class, and let

\[
J_+,\ J_- = \overline{J_+}
\]

be its two minimal companion ideals.

By unit/conjugation invariance of the HATTER fold, the four local products carry only two ordinary typed states:

\[
\boxed{
X:=\Pi(I_+J_+)=\Pi(I_-J_-),
}
\]

\[
\boxed{
Y:=\Pi(I_+J_-)=\Pi(I_-J_+).
}
\]

Call `X` the same-sign state and `Y` the opposite-sign state. No ordering between them is assumed.

Take a conjugation-balanced factor multiset consisting of

\[
e\ \text{copies of }I_+
\quad\text{and}\quad
 e\ \text{copies of }I_-.
\]

Thus the total number of factor nodes is

\[
2e.
\]

For a minimal-witness configuration let

\[
j\in\{0,1,\dots,2e\}
\]

be the number of nodes choosing companion `J_+`.

The exact residue sector is determined by `j` whenever the binary-tail ratio is nontrivial, as in T11.15.

---

## 2. Internal count parameter

Let

\[
x
\]

be the number of the `e` positive factor nodes `I_+` that choose companion `J_+`, and let

\[
y
\]

be the number of the `e` negative factor nodes `I_-` that choose companion `J_+`.

Then

\[
\boxed{j=x+y.}
\]

The number `k` of same-sign typed states `X` is

\[
k=x+(e-y).
\]

Using `y=j-x`,

\[
\boxed{
k=e+2x-j.
}
\]

The feasibility constraints are

\[
0\le x\le e,
\qquad
0\le j-x\le e,
\]

hence

\[
\boxed{
\max(0,j-e)\le x\le\min(e,j).
}
\]

---

## 3. Theorem T11.20 — exact typed-composition support of a residue sector

For fixed residue count `j`, the possible numbers of `X` states are exactly

\[
\boxed{
K_e(j)
=
\left\{
|e-j|,
|e-j|+2,
\dots,
 e+\min(j,2e-j)
\right\}.
}
\]

Equivalently,

\[
\boxed{
k\in K_e(j)
\iff
|e-j|\le k\le e+\min(j,2e-j)
\quad\text{and}\quad
k\equiv e-j\pmod2.
}
\]

For every such `k`, the residue sector contains the ordinary typed multiset

\[
\boxed{
X^kY^{2e-k}.
}
\]

No other typed-composition count occurs in that sector.

### Proof

From

\[
k=e+2x-j
\]

and

\[
\max(0,j-e)\le x\le\min(e,j),
\]

the minimum is

\[
e+2\max(0,j-e)-j
=
|e-j|,
\]

while the maximum is

\[
e+2\min(e,j)-j
=
 e+\min(j,2e-j).
\]

Increasing `x` by one increases `k` by two, so precisely one parity class is attained. Conversely every integer in the stated interval with that parity corresponds to an integral feasible value

\[
x=\frac{k-e+j}{2}.
\]

Hence the support is exact. QED.

---

## 4. Immediate symmetry

Pair flip sends

\[
j\longmapsto2e-j.
\]

The support theorem gives

\[
\boxed{
K_e(j)=K_e(2e-j).
}
\]

Thus pair-flip-equivalent sectors have exactly the same set of ordinary typed-composition counts before any network optimization.

This recovers the response blindness of T11.17 at the combinatorial level.

---

## 5. Extreme sectors

For `j=0` or `j=2e`,

\[
|e-j|=e,
\qquad
 e+\min(j,2e-j)=e.
\]

Therefore

\[
\boxed{
K_e(0)=K_e(2e)=\{e\}.
}
\]

So every extreme sector has exactly the balanced typed multiset

\[
\boxed{
X^eY^e.
}
\]

This is the general form of the network-blind extreme cube phenomenon for a single species.

---

## 6. Central sector

For the central residue count

\[
j=e,
\]

we obtain

\[
\boxed{
K_e(e)=\{0,2,4,\dots,2e\}
}
\]

when `e` is even, and more generally the displayed set is always the even counts because `e-j=0`.

Thus the central residue sector contains every even same-sign composition:

\[
\boxed{
Y^{2e},
X^2Y^{2e-2},
X^4Y^{2e-4},
\dots,
X^{2e}.
}
\]

In particular, the balanced multiset `X^eY^e` belongs to the central sector **iff `e` is even**.

Indeed `e` must lie in the even set `K_e(e)`.

Therefore:

\[
\boxed{
e\ \text{even}
\Longrightarrow
K_e(0)\cap K_e(e)=\{e\},
}
\]

whereas

\[
\boxed{
e\ \text{odd}
\Longrightarrow
K_e(0)\cap K_e(e)=\varnothing.
}
\]

This parity obstruction explains why the first extreme-versus-central collision occurs at total multiplicity four (`e=2`) rather than two (`e=1`).

---

## 7. Corollary T11.20a — universal multiplicity-four support pattern

Set

\[
e=2.
\]

Then

\[
\boxed{
K_2(0)=K_2(4)=\{2\},
}
\]

\[
\boxed{
K_2(1)=K_2(3)=\{1,3\},
}
\]

\[
\boxed{
K_2(2)=\{0,2,4\}.
}
\]

Hence the five residue sectors have the universal typed-composition support pattern

\[
\boxed{
\begin{array}{c|c}
 j & \text{typed-composition support}\\
\hline
0 & X^2Y^2\\
1 & XY^3,\ X^3Y\\
2 & Y^4,\ X^2Y^2,\ X^4\\
3 & XY^3,\ X^3Y\\
4 & X^2Y^2
\end{array}}
\]

independent of the field and independent of the numerical port capacities.

T11.19 is therefore an arithmetic/network realization of a universal binary-tail support law.

---

## 8. Corollary T11.20b — exact multiplicity-four collision criterion

Let

\[
\mathcal F_k
:=
\mathcal F(X^kY^{4-k})
\]

be the ordinary connected Pareto response of the fixed typed multiset with `k` copies of `X` and `4-k` copies of `Y`, allowing `\mathcal F_k=\varnothing` when no connected realization exists.

Then the residue-sector responses satisfy

\[
\boxed{
\mathcal R_0=\mathcal R_4=\mathcal F_2,
}
\]

\[
\boxed{
\mathcal R_1=\mathcal R_3
=
\operatorname{ParetoMin}(\mathcal F_1\cup\mathcal F_3),
}
\]

and

\[
\boxed{
\mathcal R_2
=
\operatorname{ParetoMin}(\mathcal F_0\cup\mathcal F_2\cup\mathcal F_4).
}
\]

Therefore the central sector collides with the extreme pair exactly when

\[
\boxed{
\operatorname{ParetoMin}(\mathcal F_0\cup\mathcal F_2\cup\mathcal F_4)
=\mathcal F_2.
}
\]

Equivalently: adding the two pure typed configurations `Y^4` and `X^4` produces no new Pareto-minimal point beyond the balanced configuration `X^2Y^2`.

This is the abstract criterion realized in T11.19.

---

## 9. General residue response formula

For arbitrary `e`, define

\[
\mathcal F_k:=\mathcal F(X^kY^{2e-k}).
\]

Then T11.20 gives the exact residue response formula

\[
\boxed{
\mathcal R_j
=
\operatorname{ParetoMin}
\left(
\bigcup_{k\in K_e(j)}\mathcal F_k
\right).
}
\]

This separates HATTER-SOL-11 into two layers:

1. **arithmetic/count support** — the exact set `K_e(j)`;
2. **network optimization** — which fixed-composition responses `\mathcal F_k` survive Pareto minimization.

Thus every post-pair-flip collision is now reduced to an explicit finite support-comparison problem.

---

## 10. What remains genuinely network-dependent

T11.20 classifies all typed-composition supports but does **not** claim that equal support is necessary for equal ordinary response.

Two distinct supports may still produce the same Pareto response because network optimization can discard different dominated configurations. T11.19 is exactly such a phenomenon at the residue-sector level: the central support strictly contains the extreme support, yet both produce the same final Pareto response.

The remaining problem is therefore sharper:

> classify when distinct support sets `K_e(j)` and `K_e(j')` have the same Pareto envelope under the family `\{\mathcal F_k\}`.

That is the correct next network theorem.

---

## 11. Next target

For the scalar one-port case

\[
X=(x,0),
\qquad
Y=(y,0),
\]

derive `\mathcal F_k` in closed form from the maximum-edge problem for a simple connected graph with `k` vertices of capacity `x` and `2e-k` vertices of capacity `y`.

This should turn the post-quotient collision problem into explicit inequalities in

\[
(e,k,x,y).
\]

The first benchmark is to recover T11.19 with

\[
e=2,
\qquad
x=1,
\qquad
y=17
\]
(up to interchanging the labels `X,Y`).

A successful closed formula would likely classify an infinite family of genuine network-induced residue collisions rather than isolated examples.