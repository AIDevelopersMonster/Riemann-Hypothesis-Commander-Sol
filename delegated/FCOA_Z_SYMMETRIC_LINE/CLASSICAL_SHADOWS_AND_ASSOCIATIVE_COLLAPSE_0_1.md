# FCOA-Z — Classical Shadows and Direct Associative Collapse

**Version:** 0.1  
**Date:** 2026-08-30  
**Status:** PROVED CORE PACKAGE / HOSTILE AUDIT REQUIRED  
**Branch:** `director/fcoa-z-symmetric-line`

---

## 1. Purpose

This note separates two very different ways in which a classical algebra can arise from the FCOA-Z signed pre-algebraic mechanism.

The first route is **direct classicalization of the legacy partial operation** `oplus` by forcing commutativity or associativity. That route collapses the signed coordinate carrier.

The second route is an **operator shadow**: retain the reversible coordinate operator `T` and, optionally, the reflection `nu`, form their operator group, and then apply standard group/ring/algebra constructions. That route canonically produces ordinary classical structures while forgetting much of the richer FCOA data.

The intended conclusion is therefore not

\[
\text{FCOA-Z is secretly an ordinary algebra},
\]

but rather

\[
\boxed{
\text{FCOA-Z can have ordinary classical algebras as irreversible shadows.}
}
\]

This is compatible with the Arithmetic Firewall because no binary `+` or `times` is inserted into the primitive FCOA signature.

---

## 2. Signed-line setup

Write the minimal reversible line as

\[
X=\{x_k:k\in\mathbb Z\},
\qquad
x_k=T^k x_0.
\]

Then

\[
T(x_k)=x_{k+1},
\qquad
\nu(x_k)=x_{-k},
\]

and

\[
\nu^2=\operatorname{id},
\qquad
\nu T\nu=T^{-1}.
\]

For the legacy signed `oplus` transfer, define the radial contraction

\[
\rho(x_k)=x_{k-\operatorname{sgn}(k)}
\qquad(k\ne0).
\]

The base-valued right-zero and left-zero cells are

\[
\boxed{x_0\oplus x_k=x_k}
\qquad(k\ne0),
\tag{2.1}
\]

and

\[
\boxed{x_k\oplus x_0=\rho(x_k)}
\qquad(k\ne0).
\tag{2.2}
\]

No value of \(x_0\oplus x_0\) is required in the source partial operation.

---

## 3. Direct commutative collapse

### Theorem 3.1 — Commutative Collapse

Let \((C,\cdot)\) be any commutative magma and let

\[
f:X\to C
\]

preserve every defined base-valued cell in (2.1)–(2.2), i.e.

\[
f(x_0)f(x_k)=f(x_k),
\qquad
f(x_k)f(x_0)=f(\rho(x_k))
\]

for every \(k\ne0\).

Then

\[
\boxed{f(x_k)=f(x_0)\quad\text{for every }k\in\mathbb Z.}
\]

In particular, the signed base carrier has no injective realization preserving these cells inside a commutative magma.

### Proof

By commutativity,

\[
f(x_k)
=f(x_0)f(x_k)
=f(x_k)f(x_0)
=f(\rho(x_k)).
\tag{3.1}
\]

Repeated application of \(\rho\) reaches \(x_0\) after \(|k|\) steps. Hence

\[
f(x_k)=f(\rho(x_k))=\cdots=f(x_0).
\]

This proves the claim. \(\square\)

### Corollary 3.2

Global commutativity cannot be imposed on the legacy radial `oplus` while retaining distinct signed coordinates.

Thus a commutative classical shadow, if desired, must arise through a coarser derived construction rather than by identifying `oplus` itself with a commutative operation on the same carrier.

---

## 4. Direct associative collapse

The associative obstruction is stronger: associativity alone already collapses all base coordinates.

### Theorem 4.1 — Associative Saturation Collapse

Let \((S,\cdot)\) be a semigroup and let

\[
f:X\to S
\]

preserve every defined base-valued cell in (2.1)–(2.2).

Then

\[
\boxed{f(x_k)=f(x_0)\quad\text{for every }k\in\mathbb Z.}
\]

Consequently, no injective partial-magma morphism from the signed base `oplus` structure into an associative semigroup exists.

### Proof

Fix \(k\ne0\) and \(j\ne0\). Using (2.1), (2.2), and associativity,

\[
\begin{aligned}
f(\rho(x_k))f(x_j)
&=(f(x_k)f(x_0))f(x_j)\\
&=f(x_k)(f(x_0)f(x_j))\\
&=f(x_k)f(x_j).
\end{aligned}
\tag{4.1}
\]

Iterating (4.1) radially until the first factor reaches \(x_0\) gives

\[
f(x_k)f(x_j)
=f(x_0)f(x_j)
=f(x_j).
\tag{4.2}
\]

Now choose \(j=1\). Then for every \(k\ne0\),

\[
f(x_k)f(x_1)=f(x_1).
\tag{4.3}
\]

Since

\[
f(x_1)f(x_0)=f(x_0),
\tag{4.4}
\]

associativity yields

\[
\begin{aligned}
f(\rho(x_k))
&=f(x_k)f(x_0)\\
&=f(x_k)(f(x_1)f(x_0))\\
&=(f(x_k)f(x_1))f(x_0)\\
&=f(x_1)f(x_0)\\
&=f(x_0).
\end{aligned}
\tag{4.5}
\]

Every \(x_m\) is equal to \(\rho(x_k)\) for some \(k\ne0\): for \(m>0\) take \(k=m+1\), for \(m<0\) take \(k=m-1\), and for \(m=0\) take \(k=1\). Therefore

\[
f(x_m)=f(x_0)
\]

for all \(m\in\mathbb Z\). \(\square\)

### Corollary 4.2 — Universal associative envelope collapses the base

Any universal semigroup or associative-algebra presentation obtained by adjoining generators for the base points and imposing all defined relations (2.1)–(2.2) necessarily identifies all base generators.

Hence the direct associative envelope is a **lossy quotient**, not an embedding of the coordinate geometry.

---

## 5. The translation operator group

The failure of direct associativization does not prevent classical algebra from emerging from the FCOA-Z mechanism.

Instead retain the reversible coordinate operator itself.

Define

\[
G_T:=\langle T\rangle\le\operatorname{Sym}(X).
\]

### Theorem 5.1 — Translation Group Emergence

\[
\boxed{G_T\cong(\mathbb Z,+).}
\]

### Proof

The map

\[
\theta:\mathbb Z\to G_T,
\qquad
n\mapsto T^n
\]

is a surjective group homomorphism by definition.

If \(T^n=\operatorname{id}\), then

\[
x_n=T^n x_0=x_0.
\]

By uniqueness of the integer orbit coordinate in the minimal reversible completion, this implies \(n=0\). Thus \(\theta\) is injective. \(\square\)

### Interpretation

Ordinary additive integer structure appears here as the composition law of iterated reversible shifts:

\[
T^mT^n=T^{m+n}.
\]

This does **not** identify the legacy `oplus` with integer addition.

---

## 6. The dihedral operator group

Define

\[
G_{T,\nu}:=\langle T,\nu\rangle\le\operatorname{Sym}(X).
\]

### Theorem 6.1 — Dihedral Symmetry Emergence

\[
\boxed{G_{T,\nu}\cong D_\infty\cong\mathbb Z\rtimes C_2,}
\]

where the nontrivial element of \(C_2\) acts on \(\mathbb Z\) by inversion.

### Proof

The defining coordinate identities give

\[
\nu^2=1,
\qquad
\nu T\nu=T^{-1}.
\tag{6.1}
\]

Using (6.1), every word in \(T^{\pm1}\) and \(\nu\) reduces to exactly one of the forms

\[
T^n,
\qquad
T^n\nu.
\tag{6.2}
\]

The elements \(T^n\) are pairwise distinct by Theorem 5.1. Likewise, if

\[
T^n\nu=T^m\nu,
\]

then right multiplication by \(\nu\) gives \(T^n=T^m\), hence \(n=m\).

Finally suppose

\[
T^n=T^m\nu.
\]

Evaluating at \(x_0\) gives \(x_n=x_m\), hence \(n=m\). Cancelling \(T^n\) would then give \(\nu=1\), impossible because \(\nu(x_1)=x_{-1}\ne x_1\).

Thus there are no extra relations beyond (6.1), giving the standard infinite-dihedral presentation. \(\square\)

---

## 7. Ordinary integer ring from the translation group

The previous theorem gives the additive group of integers. A second classical construction recovers ordinary integer multiplication.

Regard \(G_T\cong\mathbb Z\) as an abelian group and form its endomorphism ring

\[
\operatorname{End}(G_T).
\]

For each \(n\in\mathbb Z\), define

\[
\alpha_n(T^k):=T^{nk}.
\tag{7.1}
\]

### Theorem 7.1 — Integer Endomorphism Ring Emergence

The map

\[
\Phi:\mathbb Z\to\operatorname{End}(G_T),
\qquad
n\mapsto\alpha_n
\]

is an isomorphism of unital rings:

\[
\boxed{\operatorname{End}(G_T)\cong(\mathbb Z,+,\times).}
\]

### Proof

Every endomorphism of the infinite cyclic group \(G_T\) is determined uniquely by the image of its generator \(T\), and that image is \(T^n\) for a unique \(n\in\mathbb Z\). Thus \(\Phi\) is bijective.

The additive operation in \(\operatorname{End}(G_T)\) is pointwise multiplication in the abelian group \(G_T\). Hence

\[
(\alpha_m+\alpha_n)(T^k)
=T^{mk}T^{nk}
=T^{(m+n)k}
=\alpha_{m+n}(T^k).
\tag{7.2}
\]

Composition gives

\[
(\alpha_m\circ\alpha_n)(T^k)
=\alpha_m(T^{nk})
=T^{mnk}
=\alpha_{mn}(T^k).
\tag{7.3}
\]

Therefore \(\Phi\) preserves both ring operations, the zero map, and the identity endomorphism. \(\square\)

### Firewall clarification

This is a **derived external ring construction**. It is not a claim that binary integer addition or multiplication is primitive, first-order definable, or already equal to a legacy FCOA operation on the base carrier.

---

## 8. Classical associative group algebras

Let \(K\) be a field.

### Theorem 8.1 — Laurent Polynomial Shadow

\[
\boxed{K[G_T]\cong K[t,t^{-1}].}
\]

### Proof

By Theorem 5.1, \(G_T\) is infinite cyclic generated by \(T\). The group algebra therefore has basis \(\{T^n:n\in\mathbb Z\}\), with multiplication \(T^mT^n=T^{m+n}\). Sending \(T\mapsto t\) gives the Laurent polynomial algebra. \(\square\)

### Theorem 8.2 — Dihedral Associative Shadow

\[
\boxed{
K[G_{T,\nu}]
\cong
K[D_\infty]
\cong
K[t,t^{-1}]\rtimes C_2,
}
\]

where the nontrivial element of \(C_2\) acts by

\[
t\mapsto t^{-1}.
\]

### Proof

The first isomorphism is Theorem 6.1 followed by functoriality of the group algebra. The semidirect-product presentation

\[
D_\infty\cong\mathbb Z\rtimes C_2
\]

with inversion action induces the displayed skew-group algebra description. \(\square\)

### Interpretation

The same FCOA-Z source therefore has at least two immediate classical associative shadows:

- a commutative one, \(K[t,t^{-1}]\), when only the translation operator is retained;
- a generally noncommutative one, \(K[D_\infty]\), when reflection is retained as well.

Thus ordinary associativity can emerge at the shadow level even though the legacy `oplus` itself admits no injective associative realization.

---

## 9. Irreversible many-to-one shadowing

The classical shadows intentionally forget FCOA information.

Consider the two already established reflection-compatible signed M0 lifts:

1. `ZM0-share`, where reflected terminal outputs are identified and therefore fixed by the output reflection;
2. `ZM0-split`, where positive and negative terminal outputs are distinct and exchanged by reflection.

These are not isomorphic as typed reflection structures: their output-reflection fixed-point behavior differs.

However, both have the same base coordinate operators \(T\) and \(\nu\). Therefore they have exactly the same operator groups

\[
G_T\cong\mathbb Z,
\qquad
G_{T,\nu}\cong D_\infty,
\]

and consequently the same classical group-algebra shadows

\[
K[t,t^{-1}],
\qquad
K[D_\infty].
\]

### Theorem 9.1 — Non-Reconstruction Theorem

Let \(\mathcal S\) be any shadow construction that depends only on \((T,\nu)\) and then passes to one of the abstract classical structures above.

On any class of FCOA-Z expansions containing both `ZM0-share` and `ZM0-split`, \(\mathcal S\) is not injective on isomorphism classes.

Consequently there is no reconstruction functor \(\mathcal R\) on that class satisfying

\[
\boxed{
\mathcal R\circ\mathcal S\cong\operatorname{Id}
}
\]

on all such FCOA-Z objects.

### Proof

Let \(F_{share}\) and \(F_{split}\) denote the two nonisomorphic typed expansions. By construction,

\[
\mathcal S(F_{share})=\mathcal S(F_{split}).
\]

If \(\mathcal R\circ\mathcal S\cong\operatorname{Id}\), then

\[
F_{share}
\cong
\mathcal R(\mathcal S(F_{share}))
=
\mathcal R(\mathcal S(F_{split}))
\cong
F_{split},
\]

contradicting their nonisomorphism. \(\square\)

### Scope clarification

This rules out faithful recovery of the original FCOA-Z object from the classical shadow. It does **not** rule out choosing some canonical representative \(\mathcal R(A)\) for each classical algebra \(A\); such a section would not reconstruct which richer source object originally produced the shadow.

---

## 10. The resulting hierarchy

The present result gives two sharply different diagrams.

### 10.1 Bad route: direct associativization

\[
\boxed{
(X,\oplus)
\longrightarrow
\text{associative or commutative envelope}
\longrightarrow
\text{base-coordinate collapse}.
}
\]

### 10.2 Good route: operator shadow

\[
\boxed{
\text{FCOA-Z}
\longrightarrow
\langle T\rangle\cong\mathbb Z
\longrightarrow
\operatorname{End}(\langle T\rangle)\cong\mathbb Z_{ring}
}
\]

and

\[
\boxed{
\text{FCOA-Z}
\longrightarrow
\langle T,\nu\rangle\cong D_\infty
\longrightarrow
K[D_\infty].
}
\]

The first chain produces the ordinary integer ring as a derived classical object. The second produces a standard noncommutative associative algebra. Neither chain is invertible back to the full FCOA-Z pre-algebra.

---

## 11. Conceptual consequence

The important distinction is now exact:

\[
\boxed{
\text{classical algebra need not be the source law; it may be a quotient/shadow law of a richer pre-algebraic mechanism.}
}
\]

In particular:

- the source legacy operation can remain partial, role-sensitive, and nonassociative;
- global associativity and commutativity may appear only after a derived operator construction;
- different FCOA source structures can have the same classical shadow;
- therefore the classical algebra can be strictly less informative than the pre-algebra that generates it.

This gives a mathematically precise version of the one-way-generation programme:

\[
\boxed{
\text{FCOA pre-algebra}\to\text{classical algebra},
\qquad
\text{classical algebra}\not\to\text{unique FCOA source}.
}
\]

---

## 12. Prior-art boundary

The generic idea that partial structures may admit universal/global completions is classical. In particular:

- Stallings pregroups have universal groups extending a partial multiplication;
- partial group actions have a substantial globalization/enveloping-action literature;
- Lie and operadic structures have classical universal enveloping associative algebras.

Accordingly, no novelty claim is made for the abstract slogan “partial structure generates a classical algebra.”

The FCOA-specific candidate contribution is narrower:

1. the exact direct-collapse theorem for the signed radial `oplus` cells;
2. the simultaneous existence of non-collapsing operator shadows \(\mathbb Z\), \(D_\infty\), \(\operatorname{End}(\mathbb Z)\), and their group algebras;
3. the explicit many-to-one/non-reconstruction theorem using distinct signed FCOA output lifts with identical classical operator shadows.

A publication claim requires a separate exact-priority literature audit.

---

## 13. Next research strike

The next useful question is not whether classical algebra can emerge — it can.

The sharper problem is to classify **which information each classical shadow forgets**.

Define a shadow ladder

\[
\mathfrak F
\to
\mathcal G_T
\to
\mathcal R_{End}
\to
\mathcal A_T,
\qquad
\mathfrak F
\to
\mathcal G_{T,\nu}
\to
\mathcal A_{D_\infty},
\]

and compute for each arrow:

1. which FCOA invariants survive;
2. which signed/output/mixed-sector distinctions become invisible;
3. whether two nonisomorphic source structures first coalesce at that stage;
4. whether any shadow admits a canonical but non-inverse lift;
5. how the answer changes after genuinely mixed-sign interaction is introduced.

This is the correct route for testing whether familiar algebraic systems are emergent irreversible quotients of the FCOA mechanism rather than primitive replacements for it.
