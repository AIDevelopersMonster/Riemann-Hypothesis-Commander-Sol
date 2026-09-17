# HATTER-SOL-11 · Network-blind extreme residue cube

Status: closed theorem layer.

This note closes the next target left by `GLOBAL_BINARY_TAIL_COMPOSITION.md`: it gives distinct principalization-residue sectors whose ordinary HATTER network response is exactly identical, while the residue-refined response remains different.

The mechanism is stronger than one accidental collision. For several independent binary-tail types, an entire Boolean cube of extreme residue sectors is invisible to the ordinary typed network response.

---

## 1. Setup

Let `K` be an imaginary quadratic field and let a principal rational input have a conjugation-stable prime-ideal factor system.

Fix binary-tail ideal classes

\[
c_1,\ldots,c_r,
\]

with least-norm companion pairs

\[
J_t^+,\qquad J_t^- = \overline{J_t^+},
\qquad
N(J_t^+)=N(J_t^-)=\delta_t.
\]

For each type `t`, assume that the factor nodes in class `c_t` occur in conjugation-stable pairs. This is the situation for split rational prime factors of a rational integer. Let the total number of nodes of type `t` be

\[
m_t=2e_t>0.
\]

For a node ideal `I` in class `c_t`, a minimal witness associated with companion `J_t^\varepsilon`, `\varepsilon\in\{+,-\}`, is represented by a generator `alpha` of

\[
(\alpha)=I J_t^\varepsilon.
\]

The HATTER-SOL-09 typed capacity satisfies

\[
\boxed{\Pi_K(\bar\alpha)=\Pi_K(\alpha).}
\]

For every sign vector

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_r)\in\{+,-\}^r,
\]

define the corresponding **extreme residue sector** by requiring every node of type `t` to choose the same companion `J_t^{\varepsilon_t}`.

Its residue ideal is

\[
\boxed{
R_{\varepsilon}
=
C\prod_{t=1}^r (J_t^{\varepsilon_t})^{m_t},
}
\]

where `C` is the fixed product of all deterministic-tail contributions.

These are the `2^r` corners of the affine box from T11.15.

---

## 2. Local pair-flip lemma

Consider one conjugate pair of factor nodes

\[
I,\qquad \bar I
\]

in one binary-tail class with companions

\[
J^+,\qquad J^- = \bar J^+.
\]

Choose the same companion `J^-` on both nodes. Let the corresponding witness generators be

\[
(\alpha)=I J^-,
\qquad
(\beta)=\bar I J^-.
\]

Now flip the pair so that both nodes choose `J^+`. Let

\[
(\alpha')=I J^+,
\qquad
(\beta')=\bar I J^+.
\]

Conjugating the first two principal ideals gives

\[
(\bar\alpha)=\bar I J^+ = (\beta'),
\]

\[
(\bar\beta)=I J^+ = (\alpha').
\]

Therefore, up to units,

\[
\beta'\sim\bar\alpha,
\qquad
\alpha'\sim\bar\beta.
\]

Since `Pi_K` is unit- and conjugation-invariant,

\[
\boxed{
\Pi_K(\alpha')=\Pi_K(\beta),
\qquad
\Pi_K(\beta')=\Pi_K(\alpha).
}
\]

### Lemma T11.17a — binary pair-flip invisibility

Flipping both companion choices in a conjugate binary-tail factor pair does not change the multiset of typed node capacities. It only exchanges the two typed states between the conjugate factor nodes.

This statement is arithmetic: it uses conjugation of the principalization equations. It does not assume any geometric port hierarchy.

---

## 3. Ordinary network response is blind to independent pair flips

For a fixed witness configuration `theta`, write

\[
\mathfrak B^{(2)}(\theta)
\]

for the connected typed-boundary region of the conservative HATTER simple-support model, and

\[
\partial_P\mathfrak B^{(2)}(\theta)
\]

for its Pareto frontier.

The canonical HATTER response depends on the typed capacities attached to the factor vertices but not on their arbitrary names. A permutation of the vertices therefore induces a boundary-preserving bijection on all connected typed simple-support networks.

Applying Lemma T11.17a independently to every conjugate node pair shows that changing any coordinate `\varepsilon_t` merely permutes typed capacities inside the nodes of type `t`.

Hence all extreme sectors have the same ordinary network response.

### Theorem T11.17 — network-blind extreme residue cube

For every two sign vectors

\[
\varepsilon,\eta\in\{+,-\}^r,
\]

their sector-conditioned ordinary HATTER responses satisfy

\[
\boxed{
\mathfrak B^{(2)}(R_{\varepsilon})
=
\mathfrak B^{(2)}(R_{\eta}),
}
\]

and therefore

\[
\boxed{
\partial_P\mathfrak B^{(2)}(R_{\varepsilon})
=
\partial_P\mathfrak B^{(2)}(R_{\eta}),
}
\]

with identical ordinary response polynomials after residue labels are forgotten.

If in addition the companion ratios

\[
g_t=J_t^+(J_t^-)^{-1}
\]

are multiplicatively independent, then the `2^r` residue ideals `R_epsilon` are pairwise distinct.

Consequently,

\[
\boxed{
2^r\ \text{distinct exact residue sectors}
\longrightarrow
1\ \text{ordinary HATTER network response}
}
\]

on the extreme corner cube.

### Proof

The response equality follows from repeated application of Lemma T11.17a: each sign flip exchanges typed states only inside conjugate factor pairs. The resulting witness configurations differ by a permutation of factor vertices, and vertex relabeling preserves connectedness, edge types, feasibility, and both boundary coordinates.

For distinct sign vectors `epsilon` and `eta`, equality of residues would give

\[
\prod_t g_t^{d_t}=1,
\]

where each exponent `d_t` is `0` or `+-m_t`, and at least one is nonzero. Multiplicative independence of the `g_t` forbids this. Hence all corner residues are distinct. QED.

---

## 4. Why this is stronger than static folding loss

T11.16 showed that the HATTER fold of a residue generator can identify distinct exact residues.

T11.17 is a different statement. It performs the full network step:

\[
\text{witness choice}
\to
\text{typed node capacities}
\to
\text{connected edge optimization}
\to
\text{ordinary Pareto response}.
\]

Even after this optimization, all extreme sectors in the Boolean cube remain indistinguishable.

Thus the information loss is not merely

\[
R\mapsto\Pi(R).
\]

There is an exact arithmetic symmetry that survives into the complete ordinary network observable.

The residue-refined response of HATTER-SOL-10 does not lose this information because the formal residue labels remain distinct.

---

## 5. Exact two-dimensional laboratory: Delta = -1155

Retain the field from T11.15--T11.16:

\[
K=\mathbb Q(\sqrt{-1155}),
\qquad
\omega=\frac{1+\sqrt{-1155}}2,
\]

with

\[
\omega^2-\omega+289=0.
\]

The two independent binary-tail companion pairs are

\[
A_+=(17,\omega-1),
\qquad
A_-=(17,\omega),
\]

\[
A_+^2=(\omega-1),
\qquad
A_-^2=(\omega),
\]

and

\[
B_+=(19,\omega-9),
\qquad
B_-=(19,\omega+8),
\]

\[
B_+^2=(\omega-9),
\qquad
B_-^2=(\omega+8).
\]

For the rational input

\[
(323)=(17)(19)=A_+A_-B_+B_-,
\]

the four corner sectors are obtained by choosing the same `A` companion on both `A` nodes and the same `B` companion on both `B` nodes.

Because the `17` and `19` companion ratios have disjoint prime-ideal support, they are multiplicatively independent. Hence all four corner residues are distinct.

---

## 6. Typed witness states at the four factor nodes

For the `A` pair:

\[
A_+A_+=(\omega-1),
\qquad
A_+A_-=(17),
\]

\[
A_-A_+=(17),
\qquad
A_-A_-=(\omega).
\]

The odd-discriminant HATTER fold gives

\[
\Pi(\omega-1)=\Pi(\omega)=(1,0),
\qquad
\Pi(17)=(17,0).
\]

Therefore flipping both `A` companions exchanges the states

\[
(1,0)\quad\text{and}\quad(17,0)
\]

between `A_+` and `A_-`.

For the `B` pair:

\[
B_+B_+=(\omega-9),
\qquad
B_+B_-=(19),
\]

\[
B_-B_+=(19),
\qquad
B_-B_-=(\omega+8),
\]

with

\[
\Pi(\omega-9)=\Pi(\omega+8)=(8,1),
\qquad
\Pi(19)=(19,0).
\]

Thus every corner sector has exactly the same typed capacity multiset

\[
\boxed{
\{(1,0),(17,0),(8,1),(19,0)\}.
}
\]

Only the assignment of these states to conjugate factor vertices changes.

---

## 7. Exact ordinary Pareto response of all four corners

For any corner configuration,

\[
\sum P_i=1+17+8+19=45,
\qquad
\sum Q_i=1.
\]

Exactly one factor vertex has positive `Q`-capacity, namely `Q=1`. A `Q`-edge needs positive `Q`-capacity at both endpoints, so

\[
\boxed{|E_Q|=0}
\]

in every feasible typed network. Hence

\[
\boxed{B_Q=1.}
\]

For the `P` layer, one vertex has capacity `1` and the other three have capacity at least `3`. Among the three high-capacity vertices there are at most three simple edges, and the capacity-one vertex can support at most one additional edge. Therefore

\[
|E_P|\le4.
\]

This bound is attained by a triangle on the three high-capacity vertices plus one pendant `P`-edge from the capacity-one vertex. The support is connected.

Thus

\[
\boxed{
B_P=45-2\cdot4=37
}
\]

is the Pareto-minimal `P` boundary.

Consequently every one of the four distinct corner residue sectors has the exact ordinary response

\[
\boxed{
\partial_P\mathfrak B^{(2)}=\{(37,1)\}
}
\]

and ordinary response polynomial

\[
\boxed{Z_{\rm ord}(X,Y)=X^{37}Y.}
\]

---

## 8. Exact information-loss ladder in the Delta = -1155 laboratory

Label the corner count vectors by

\[
(j_{17},j_{19})\in\{0,2\}\times\{0,2\}.
\]

Their exact residue generators are

\[
(0,0):\quad \omega(\omega+8)=-289+9\omega,
\]

\[
(2,0):\quad (\omega-1)(\omega+8)=-297+8\omega,
\]

\[
(0,2):\quad \omega(\omega-9)=-289-8\omega,
\]

\[
(2,2):\quad (\omega-1)(\omega-9)=-280-9\omega.
\]

They are four distinct principal ideals.

Under the ordinary odd-discriminant HATTER fold,

\[
\Pi(-289+9\omega)=\Pi(-280-9\omega)=(280,9),
\]

\[
\Pi(-297+8\omega)=\Pi(-289-8\omega)=(289,8).
\]

Hence the corner cube exhibits the strict ladder

\[
\boxed{
4\ \text{exact residue sectors}
\longrightarrow
2\ \text{folded residue states}
\longrightarrow
1\ \text{ordinary network response}.
}
\]

The residue-refined response keeps all four labels separate:

\[
[R_{00}]X^{37}Y,
\quad
[R_{20}]X^{37}Y,
\quad
[R_{02}]X^{37}Y,
\quad
[R_{22}]X^{37}Y.
\]

This is an explicit network-level separation, not only a static arithmetic fold collision.

---

## 9. Consequence for HATTER-SOL-11

The target left at the end of T11.16 is now closed:

\[
\boxed{
\text{distinct residue sectors can have identical ordinary network response.}
}
\]

Moreover the loss can grow exponentially with the number of independent binary-tail types:

\[
\boxed{2^r\to1}
\]

on the extreme residue cube.

No new intrinsic ordered port filtration has been proved here. The result instead shows that the already canonical principalization-residue label carries information that the ordinary typed network response necessarily forgets.

---

## 10. Next target

The next question should separate symmetry-forced blindness from genuinely dynamical network collapse.

Define two residue sectors to be **pair-flip equivalent** if they differ only by independent extreme flips inside conjugate binary-tail node pairs. T11.17 shows that each such class has one ordinary response.

The next target is therefore:

\[
\boxed{
\text{find or exclude ordinary-response collisions between residue sectors that are not pair-flip equivalent.}
}
\]

Equivalently, determine the kernel of the map

\[
\text{exact residue sector}
\longrightarrow
\text{ordinary HATTER Pareto response}
\]

after quotienting the obvious conjugate-pair flip symmetry.

A positive example would show information loss created by network optimization itself, beyond arithmetic relabeling symmetry. A no-go theorem would classify the precise residue information retained by the ordinary network observable in the binary-tail regime.
