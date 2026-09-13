# HATTER-SOL-10 · IDEAL_TYPED_CAPACITY

## Closed theorem layer T10.1--T10.4

Let `K` be an imaginary quadratic field with ring of integers `O_K`. Let `I` be a nonzero integral ideal.

Define

\[
\delta(I):=
\min_{0\ne\alpha\in I}
\frac{|N_{K/\mathbb Q}(\alpha)|}{N(I)}.
\]

Since `(alpha) subset I`, define also

\[
\mathcal M(I):=
\{\alpha\in I\setminus\{0\}: |N(\alpha)|=\delta(I)N(I)\}.
\]

For the world-dependent element capacity `Pi_K(alpha)` inherited from HATTER-SOL-09, put

\[
\mathcal P_K(I):=
\operatorname{ParetoMin}\{\Pi_K(\alpha):\alpha\in\mathcal M(I)\}.
\]

The candidate ideal state is

\[
\mathfrak C_K(I):=(\delta(I),\mathcal P_K(I)).
\]

---

## Theorem T10.1 — integrality and principality

For every nonzero integral ideal `I`,

\[
\boxed{\delta(I)\in\mathbb Z_{\ge1}.}
\]

Moreover

\[
\boxed{\delta(I)=1\iff I\text{ is principal}.}
\]

### Proof

For every nonzero `alpha in I`, `(alpha) subset I`. Ideal norm is index, so

\[
[I:(\alpha)]
=\frac{[O_K:(\alpha)]}{[O_K:I]}
=\frac{|N(\alpha)|}{N(I)}.
\]

Hence every value in the defining minimum is a positive integer. Therefore `delta(I)` is a positive integer.

If `delta(I)=1`, some `alpha in I` satisfies `[I:(alpha)]=1`, hence `I=(alpha)` is principal. Conversely, if `I=(alpha)`, the same element gives ratio `1`. QED.

---

## Theorem T10.2 — inverse ideal-class interpretation

Because `O_K` is Dedekind, every nonzero ideal is invertible. Then

\[
\boxed{
\delta(I)
=
\min\{N(J):J\subset O_K,\ [J]=[I]^{-1}\}.
}
\]

### Proof

For every nonzero `alpha in I`, set

\[
J=(\alpha)I^{-1}.
\]

Since `(alpha) subset I`, multiplication by `I^{-1}` gives `J subset O_K`; hence `J` is integral. Its ideal class is

\[
[J]=[(\alpha)][I]^{-1}=[I]^{-1}.
\]

By multiplicativity of ideal norm,

\[
N(J)=\frac{N((\alpha))}{N(I)}
=\frac{|N(\alpha)|}{N(I)}.
\]

Conversely, if `J` is an integral ideal in class `[I]^{-1}`, then `IJ` is principal, say `IJ=(alpha)`. Because `J subset O_K`, we have `(alpha)=IJ subset I`, so `alpha in I`, and

\[
\frac{|N(\alpha)|}{N(I)}=N(J).
\]

Taking minima in both directions proves the formula. QED.

### Corollary T10.2a

`delta(I)` depends only on the ideal class `[I]`.

Thus `delta` is a **class-level principalization cost**.

---

## Theorem T10.3 — exact recovery of HATTER-SOL-09

If `I=(alpha)` is principal, then

\[
\boxed{\mathcal M(I)=O_K^\times\alpha.}
\]

Consequently, if `Pi_K` is unit-invariant,

\[
\boxed{\mathcal P_K((\alpha))=\{\Pi_K(\alpha)\}.}
\]

### Proof

By T10.1, `delta(I)=1`. Hence `beta in M(I)` exactly when `(beta) subset I` has the same ideal norm as `I`, equivalently `[I:(beta)]=1`. Therefore `(beta)=I=(alpha)`, so `beta=u alpha` for a unit `u`. The converse is immediate. Unit invariance of `Pi_K` collapses all minimal witnesses to the same typed pair. QED.

This closes the mandatory compatibility requirement: the ideal theory is a strict extension of the element theory rather than a parallel replacement.

---

## Theorem T10.4 — conjugation

For every nonzero integral ideal `I`,

\[
\boxed{\delta(\bar I)=\delta(I).}
\]

If the element capacity is conjugation-invariant after folding, then

\[
\boxed{\mathcal P_K(\bar I)=\mathcal P_K(I).}
\]

### Proof

Conjugation is a bijection `I -> bar I`, preserves absolute field norm, and preserves ideal norm. Therefore it carries the optimization problem defining `delta(I)` bijectively to that defining `delta(bar I)`. It also maps `M(I)` onto `M(bar I)`. Conjugation-invariance of `Pi_K` then gives equality of the folded Pareto frontiers. QED.

---

## 5. First non-UFD laboratory: Q(sqrt(-5))

Let

\[
K=\mathbb Q(\sqrt{-5}),
\qquad
O_K=\mathbb Z[\sqrt{-5}],
\qquad
\Delta_K=-20.
\]

This field has class number `2`; the ideal

\[
\mathfrak p_2=(2,1+\sqrt{-5})
\]

has norm `2`, is nonprincipal, and satisfies

\[
(2)=\mathfrak p_2^2.
\]

The norm form on elements is

\[
N(a+b\sqrt{-5})=a^2+5b^2.
\]

### Proposition 5.1 — the ramified prime ideal over 2

\[
\boxed{\delta(\mathfrak p_2)=2.}
\]

Moreover

\[
\boxed{\mathcal M(\mathfrak p_2)=\{\pm2\}.}
\]

### Proof

The ideal is nonprincipal, so T10.1 gives `delta>=2`. Since `2 in p_2` and

\[
\frac{N(2)}{N(\mathfrak p_2)}=\frac4{2}=2,
\]

we have `delta<=2`, hence equality. Elements of norm `4` satisfy

\[
a^2+5b^2=4,
\]

whose only integral solutions are `a=+-2,b=0`. QED.

Using the `Delta=-20` even-discriminant interface law from HATTER-SOL-09,

\[
\boxed{\mathcal P_K(\mathfrak p_2)=\{(2,0)\}.}
\]

### Proposition 5.2 — a split nonprincipal prime ideal over 3

Let

\[
\mathfrak p_3=(3,1+\sqrt{-5}),
\qquad N(\mathfrak p_3)=3.
\]

Then

\[
\boxed{\delta(\mathfrak p_3)=2}
\]

and

\[
\boxed{\mathcal M(\mathfrak p_3)=\{\pm(1+\sqrt{-5})\}.}
\]

### Proof

`p_3` lies in the nontrivial class (the class group has order two), hence it is nonprincipal and `delta>=2`. But

\[
1+\sqrt{-5}\in\mathfrak p_3,
\qquad
N(1+\sqrt{-5})=6,
\]

so the ratio is `6/3=2`, hence `delta=2`.

The norm-six equation

\[
a^2+5b^2=6
\]

has solutions `(a,b)=(+-1,+-1)`. Membership in `p_3` is the congruence `a-b congruent 0 mod 3`; among those four solutions only `+- (1+sqrt(-5))` satisfy it. QED.

Therefore

\[
\boxed{\mathcal P_K(\mathfrak p_3)=\{(1,1)\}.}
\]

### First nonprincipal typed separation

The two nonprincipal ideals satisfy

\[
\delta(\mathfrak p_2)=\delta(\mathfrak p_3)=2,
\]

but

\[
\boxed{
\mathcal P_K(\mathfrak p_2)=\{(2,0)\}
\ne
\{(1,1)\}=\mathcal P_K(\mathfrak p_3).
}
\]

Thus the class-level principalization cost alone is strictly coarser than the embedded typed witness geometry.

---

## 6. Ideal norm alone is also too coarse

Even among principal ideals in this same non-UFD field, equal ideal norm does not determine typed geometry.

Consider

\[
I_1=(3),
\qquad
I_2=(2+\sqrt{-5}).
\]

Both have ideal norm

\[
N(I_1)=N(I_2)=9,
\]

because

\[
N(3)=9,
\qquad
N(2+\sqrt{-5})=4+5=9.
\]

By T10.3,

\[
\mathcal P_K(I_1)=\{(3,0)\},
\qquad
\mathcal P_K(I_2)=\{(2,1)\}.
\]

Hence

\[
\boxed{
N(I_1)=N(I_2)
\quad\text{but}\quad
\mathcal P_K(I_1)\ne\mathcal P_K(I_2).
}
\]

So ideal norm is not a sufficient node state for HATTER-SOL networks.

---

## 7. What is now closed

The following are proved:

1. `delta(I)` is an integer principalization cost.
2. `delta(I)=1` exactly for principal ideals.
3. `delta(I)` is the least norm in the inverse ideal class.
4. The ideal typed frontier exactly recovers HATTER-SOL-09 on principal ideals.
5. Conjugation compatibility holds.
6. In `Q(sqrt(-5))`, nonprincipal prime ideals with the same class-level cost can have different typed frontiers.
7. Equal ideal norm can also hide different typed geometry.

## 8. Next obligation

The remaining conceptual issue is the **network law for set-valued nodes**. A nonprincipal ideal can have more than one inequivalent minimal witness and therefore `P_K(I)` can contain several incomparable typed pairs.

The next target is to determine whether the correct network semantics is:

- choose one witness pair per ideal node globally;
- optimize jointly over witness selection and graph edges; or
- retain a higher response object that sums/minimizes over all witness choices.

Publication must wait until this ambiguity is resolved and hostile-tested.
