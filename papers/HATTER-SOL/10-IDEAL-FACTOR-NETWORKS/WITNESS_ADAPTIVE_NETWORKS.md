# HATTER-SOL-10 · Witness-adaptive ideal networks

Status: closed theorem layer resolving the set-valued node ambiguity.

Let `K` be an imaginary quadratic field, `O_K` its ring of integers, and `I` a nonzero integral ideal. Retain

\[
\delta(I)=\min_{0\ne\alpha\in I}\frac{|N(\alpha)|}{N(I)},
\]

and the minimal-witness set

\[
\mathcal M(I)=\{\alpha\in I\setminus\{0\}:|N(\alpha)|=\delta(I)N(I)\}.
\]

The earlier nodewise projection `ParetoMin{Pi(alpha): alpha in M(I)}` is **not** the correct network state in general. This file replaces it by the full witness state.

---

## 1. Minimal witness orbits

Define

\[
\boxed{\mathscr W_K(I):=\mathcal M(I)/O_K^\times.}
\]

Because an imaginary quadratic unit group is finite and the lattice `I` has only finitely many elements of a fixed norm, `W_K(I)` is finite.

Define the full typed capacity support

\[
\boxed{\Theta_K(I):=\{\Pi_K(\alpha):[\alpha]\in\mathscr W_K(I)\}.}
\]

If distinct witness orbits yield the same typed pair, retain their multiplicity separately by

\[
\nu_I(c):=\#\{[\alpha]\in\mathscr W_K(I):\Pi_K(\alpha)=c\}.
\]

The network-feasibility state is `Theta_K(I)`; `(W_K(I),nu_I)` is retained as richer arithmetic metadata.

---

## 2. Exact correspondence with least-norm ideals in the inverse class

Let

\[
\mathscr A_{\min}([I]^{-1})
:=
\{J\subset O_K:[J]=[I]^{-1},\ N(J)=\delta(I)\}.
\]

### Theorem T10.5 — witness/ideal bijection

The map

\[
\boxed{
[\alpha]\longmapsto J_\alpha:=(\alpha)I^{-1}
}
\]

is a bijection

\[
\boxed{
\mathscr W_K(I)
\cong
\mathscr A_{\min}([I]^{-1}).
}
\]

### Proof

For `alpha in M(I)`, the ideal

\[
J_\alpha=(\alpha)I^{-1}
\]

is integral, lies in class `[I]^{-1}`, and has norm

\[
N(J_\alpha)=\frac{|N(\alpha)|}{N(I)}=\delta(I).
\]

If two witnesses give the same `J`, then

\[
(\alpha)=IJ=(\beta),
\]

so `alpha` and `beta` differ by a unit; hence the map is injective on unit orbits.

Conversely, for every least-norm integral ideal `J` in the inverse class, `IJ` is principal, say

\[
IJ=(\alpha).
\]

Then `alpha in I` and

\[
\frac{|N(\alpha)|}{N(I)}=N(J)=\delta(I),
\]

so `alpha in M(I)`. QED.

### Consequence

Multiplicity of minimal witnesses is not arbitrary. It is exactly multiplicity of least-norm integral representatives of the inverse ideal class.

---

## 3. Principal scaling transports the full witness set

### Lemma T10.6

If `I=gamma J` for nonzero `gamma in K` and both ideals are integral, then multiplication by `gamma` induces a bijection

\[
\boxed{
\mathcal M(J)\xrightarrow{\sim}\mathcal M(I),
\qquad
\beta\mapsto\gamma\beta.
}
\]

### Proof

Multiplication by `gamma` is a bijection `J -> I`, and

\[
\frac{|N(\gamma\beta)|}{N(\gamma J)}
=
\frac{|N(\beta)|}{N(J)}.
\]

Therefore minimizers correspond exactly. QED.

This shows why `delta` is class-level while the typed witness geometry may vary under embedded principal scaling.

---

## 4. First genuinely multistate ideal: Q(sqrt(-15))

Let

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
O_K=\mathbb Z[\omega],
\qquad
\omega=\frac{1+\sqrt{-15}}2,
\]

so

\[
\omega^2-\omega+4=0,
\qquad
N(a+b\omega)=a^2+ab+4b^2.
\]

Let

\[
\mathfrak p=(2,\omega),
\qquad
\bar{\mathfrak p}=(2,1-\omega).
\]

Then

\[
N(\mathfrak p)=2,
\qquad
(2)=\mathfrak p\bar{\mathfrak p},
\qquad
\mathfrak p^2=(\omega).
\]

There is no element of norm `2`, so `p` is nonprincipal. Since both `p` and `pbar` have norm `2` and represent the inverse class of `p`,

\[
\delta(\mathfrak p)=2.
\]

The norm-four elements lying in `p` are exactly

\[
\boxed{\mathcal M(\mathfrak p)=\{\pm2,\pm\omega\}.}
\]

Modulo units `+-1`, there are two witness orbits.

For discriminant `-15`, the odd-discriminant capacity law gives

\[
\Pi(2)=(2,0),
\qquad
\Pi(\omega)=(1,0).
\]

Hence

\[
\boxed{\Theta_K(\mathfrak p)=\{(1,0),(2,0)\}.}
\]

The same support occurs for `pbar`.

---

## 5. A genuinely incomparable state set

Put

\[
\gamma=2-\omega,
\qquad
N(\gamma)=6,
\qquad
I=\gamma\mathfrak p.
\]

By Lemma T10.6,

\[
\mathcal M(I)=\gamma\mathcal M(\mathfrak p).
\]

Two unit-orbit representatives are

\[
2\gamma=4-2\omega
\]

and

\[
\omega\gamma=4+\omega.
\]

Their typed capacities are

\[
\Pi(4-2\omega)=(2,2),
\]

\[
\Pi(4+\omega)=(4,1).
\]

Therefore

\[
\boxed{
\Theta_K(I)=\{(2,2),(4,1)\}.
}
\]

These two points are incomparable in coordinatewise order. Thus a genuinely set-valued typed ideal node exists even after removing unit ambiguity.

---

## 6. Nodewise Pareto pruning is invalid

The previous definition

\[
\operatorname{ParetoMin}\{\Pi(\alpha):\alpha\in\mathcal M(I)\}
\]

can delete a witness state that is required for the globally optimal or even globally feasible network.

### Theorem T10.7 — local-pruning counterexample

In `Q(sqrt(-15))`, factor the rational principal ideal

\[
(4)=(2)^2=\mathfrak p^2\bar{\mathfrak p}^{\,2}.
\]

Each of the four prime-ideal factor nodes has capacity support

\[
\Theta=\{(1,0),(2,0)\}.
\]

If one performs coordinatewise nodewise Pareto minimization, only `(1,0)` survives at every node. Then the total P-capacity is `4`. A connected graph on four vertices needs at least three edges and hence degree sum at least `6`; therefore no connected typed network exists.

With the full state set retained, choose `(2,0)` for two nodes and `(1,0)` for the other two. The capacity sequence is

\[
2,2,1,1.
\]

A four-vertex path has degree sequence

\[
2,2,1,1
\]

and saturates all ports. Hence

\[
\boxed{(B_P,B_Q)=(0,0)}
\]

is attainable.

Therefore local Pareto pruning changes global feasibility. QED.

### Consequence

Witness selection and edge optimization must be performed jointly.

---

## 7. Canonical witness-adaptive network semantics

Let an integral ideal have prime-ideal factorization, with multiplicity,

\[
\mathfrak a=\mathfrak p_1\cdots\mathfrak p_k.
\]

Each node `j` carries the finite state set

\[
\Theta_j:=\Theta_K(\mathfrak p_j).
\]

Define the witness-configuration space

\[
\boxed{
\Sigma_K(\mathfrak a)
:=\Theta_1\times\cdots\times\Theta_k.
}
\]

For a configuration

\[
\theta=((P_1,Q_1),\ldots,(P_k,Q_k))\in\Sigma_K(\mathfrak a),
\]

let `B^(2)(theta)` be the attainable connected typed-boundary region of HATTER-SOL-09.

Define the full ideal-network attainable region by joint optimization:

\[
\boxed{
\mathfrak B_{K,\mathrm{ideal}}^{(2)}(\mathfrak a)
:=
\bigcup_{\theta\in\Sigma_K(\mathfrak a)}
\mathfrak B^{(2)}(\theta).
}
\]

Its canonical response is

\[
\boxed{
\partial_P\mathfrak B_{K,\mathrm{ideal}}^{(2)}(\mathfrak a)
:=
\operatorname{ParetoMin}
\mathfrak B_{K,\mathrm{ideal}}^{(2)}(\mathfrak a).
}
\]

The corresponding response polynomial is

\[
\boxed{
Z_{K,\mathrm{ideal}}(\mathfrak a;X,Y)
=
\sum_{(b_P,b_Q)\in
\partial_P\mathfrak B_{K,\mathrm{ideal}}^{(2)}(\mathfrak a)}
X^{b_P}Y^{b_Q}.
}
\]

The richer witness-resolved family should also be retained before projection when multiplicities or alternative principalizations matter.

---

## 8. Exact recovery of HATTER-SOL-09

### Theorem T10.8 — UFD/PID compatibility

If every prime ideal factor `p_j` of `a` is principal, then every `Theta_K(p_j)` is a singleton by T10.3. Hence `Sigma_K(a)` has one element and

\[
\boxed{
\partial_P\mathfrak B_{K,\mathrm{ideal}}^{(2)}(\mathfrak a)
=
\partial_P\mathfrak B_{K,\mathrm{element}}^{(2)}(\mathfrak a).
}
\]

Thus witness-adaptive ideal networks strictly extend the HATTER-SOL-09 element model.

---

## 9. What is now resolved

The set-valued-node ambiguity is closed:

1. minimal witnesses modulo units form a canonical finite set;
2. witness orbits are exactly least-norm ideals in the inverse class;
3. truly multiple and even incomparable typed states occur;
4. nodewise Pareto pruning is mathematically invalid;
5. witness selection must be optimized jointly with network edges;
6. the union-then-Pareto construction is canonical;
7. the construction exactly recovers HATTER-SOL-09 in the principal/UFD case.

## 10. Next target

The next barrier is **principalization bookkeeping across a whole ideal factorization**. Every node has a fixed class-level cost `delta(p_j)`, but local witness choices correspond to different least-norm companion ideals. Determine what global arithmetic information must be retained in addition to the network boundary:

- product of companion ideals;
- cancellation in the class group;
- whether globally compatible witness selections can reduce total principalization overhead;
- whether the response should carry a third `class-defect` coordinate in addition to `(B_P,B_Q)`.

This is the next theorem target before publication.