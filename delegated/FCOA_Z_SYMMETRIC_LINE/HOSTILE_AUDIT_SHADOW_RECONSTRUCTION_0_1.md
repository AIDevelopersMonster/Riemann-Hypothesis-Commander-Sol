# Hostile Audit — FCOA-Z One-Dimensional Shadow Reconstruction 0.1

**Date:** 2026-08-30  
**Status:** PASS WITH SCOPE CORRECTIONS  
**Branch:** `director/fcoa-z-symmetric-line`

---

## 1. Audited packages

This audit covers the theorem chain developed in:

- `CLASSICAL_SHADOWS_AND_ASSOCIATIVE_COLLAPSE_0_1.md`;
- `SHADOW_LADDER_SELECTIVE_CLASSICALIZATION_0_1.md`;
- `UNIVERSAL_CLASSICAL_SHADOW_REALIZATION_0_1.md`;
- `ONE_DIMENSIONAL_CLASSICALIZATION_COST_0_1.md`;
- `INTRINSIC_1D_MATRIX_SHADOW_0_1.md`;
- `ONE_DIMENSIONAL_RECONSTRUCTION_RESOLUTION_0_1.md`;
- `OPERATION_PROVENANCE_AND_RECONSTRUCTION_NO_GO_0_1.md`.

The purpose is to determine whether there is now a publication-level theorem nucleus and to identify any statement that must be weakened, removed, or re-scoped.

---

## 2. Verdict

\[
\boxed{\text{PASS WITH SCOPE CORRECTIONS}.}
\]

No fatal defect was found in the central one-dimensional theorem chain.

The publication-safe nucleus is:

1. direct associative or commutative preservation of the legacy radial `oplus` base cells collapses the signed base carrier;
2. operator composition avoids this collapse and produces ordinary classical shadows;
3. the existing signed `otimes` translations isolate the root and generate a full infinite matrix-unit system on the same one-dimensional carrier;
4. the finitary matrix ideal together with the distinguished shift and reflection reconstructs the rooted signed line;
5. the generated base algebra does not reconstruct primitive-operation provenance;
6. base-only shadows do not reconstruct terminal definedness or terminal attachment;
7. the canonical `share` and `split` variants remain indistinguishable until terminal reflection/attachment data is restored.

The publication claim must remain strictly one-dimensional.

---

## 3. Audit of the Associative Collapse Theorem

The theorem assumes a map preserving all defined base-valued cells

\[
x_0\oplus x_k=x_k,
\qquad
x_k\oplus x_0=\rho(x_k).
\]

The derivation of

\[
f(x_k)=f(x_0)
\]

for every \(k\) in a semigroup target is valid.

### Scope correction A

The theorem is not a statement that **every** associative completion of an arbitrary enriched FCOA collapses. It is a statement about associative realizations that preserve the specified legacy radial base cells under one target multiplication.

Publication wording:

\[
\boxed{
\text{direct associative realization preserving the audited radial cells collapses the base coordinates.}
}
\]

Do not write “associativity itself collapses all FCOA”.

---

## 4. Audit of the root-isolation theorem

The signed `otimes` right translations

\[
a_+=R_{x_1}^{\otimes},
\qquad
a_-=R_{x_{-1}}^{\otimes}
\]

are indeed partial identities on

\[
\{x_0\}\cup\{x_k:k\ge2\}
\]

and

\[
\{x_0\}\cup\{x_k:k\le-2\},
\]

respectively.

Their domains intersect only at \(x_0\). Hence

\[
a_+a_-=a_-a_+=\operatorname{id}_{\{x_0\}}.
\]

The theorem is correct.

---

## 5. Audit of matrix-unit generation

From

\[
e_0=\operatorname{id}_{\{x_0\}}
\]

and the bilateral shift \(T\), define

\[
E_{ij}=T^ie_0T^{-j}.
\]

These are singleton partial maps

\[
x_j\mapsto x_i
\]

and satisfy

\[
E_{ij}E_{kl}
=
\begin{cases}
E_{il},&j=k,\\
0,&j\ne k.
\end{cases}
\]

This is exactly the Brandt matrix-unit law.

The linear span of finitely supported combinations is therefore

\[
M_{fin}(\mathbb Z,K).
\]

The theorem is correct.

### Scope correction B

This construction is not historically new as a matrix-unit mechanism. Brandt semigroups, directly infinite algebras, algebraic Toeplitz/Jacobson algebras, and Leavitt path algebras contain closely related matrix-unit structures.

The FCOA-specific claim is only that these matrix units are generated **from the already audited legacy signed FCOA translations**, with no new coordinate or source fiber.

---

## 6. Audit of arbitrary finite matrix corners

For finite

\[
F\subset\mathbb Z,
\qquad |F|=n,
\]

the span of

\[
\{E_{ij}:i,j\in F\}
\]

is canonically isomorphic after a chosen enumeration of \(F\) to

\[
M_n(K).
\]

Correct.

### Scope correction C

The word “canonical” should not be used for the identification with the standard ordered matrix units unless an ordering of \(F\) has been chosen. The subalgebra itself is intrinsic; its standard \(M_n(K)\)-coordinate labeling is noncanonical.

---

## 7. Audit of the two-end quotient

The half-line projections generated from legacy `otimes` tails have neighboring differences equal to singleton projectors. The diagonal algebra modulo finite-support diagonals remembers the two eventual values at \(-\infty\) and \(+\infty\):

\[
D/D_{fin}\cong K\oplus K.
\]

Translation acts trivially on the two asymptotic values, yielding before reflection

\[
K[t,t^{-1}]\oplus K[t,t^{-1}].
\]

Reflection exchanges the two ends while inverting the Laurent parameter. The corresponding crossed product is isomorphic to

\[
M_2(K[t,t^{-1}]).
\]

The algebraic calculation is valid.

### Scope correction D

The short exact sequence

\[
0\to M_{fin}\to\mathcal A_{sym}\to M_2(K[t,t^{-1}])\to0
\]

has strong classical relatives. Publication novelty must not be attached to the bare extension shape.

---

## 8. Prior-art control

The following classical themes substantially overlap with isolated ingredients:

1. Brandt semigroups / matrix-unit semigroups;
2. algebraic Toeplitz/Jacobson algebras with finitary matrix ideals and Laurent polynomial quotients;
3. Leavitt path algebras with matrix blocks and Laurent polynomial components;
4. category/path algebras realizing matrix algebras;
5. transformation-semigroup and Cayley-type representations;
6. universal associative envelopes and free-algebra quotient presentations.

Therefore the article must explicitly say:

\[
\boxed{
\text{none of these classical constructions is claimed as new in itself.}
}
\]

The candidate contribution is their **forced organization inside the audited FCOA-Z one-dimensional source and the reconstruction-resolution theorem that follows from retaining or erasing specific FCOA layers**.

---

## 9. Audit of coordinate-projector reconstruction

The proposed intrinsic characterization is

\[
\mathscr C_U
=
\{p\in I:p\text{ primitive idempotent and }pU^np=0\ \forall n\ne0\}.
\]

The proof reduces a rank-one primitive idempotent to

\[
p=v\otimes\varphi
\]

with finite supports and converts

\[
\varphi(U^nv)=\delta_{n0}
\]

into a Laurent-polynomial identity

\[
q(z)v(z)=1.
\]

Because the units of \(K[z,z^{-1}]\) are monomials, \(v\) and \(\varphi\) must each have singleton support, giving

\[
p=E_{kk}.
\]

The proof is valid over a field \(K\).

### Scope correction E

The article should state explicitly that the linear reconstruction theorem is formulated over a field. General commutative coefficient rings would require separate treatment of primitive idempotents and units.

---

## 10. Audit of line and root reconstruction

From the recovered coordinate projectors,

\[
p\mapsto UpU^{-1}
\]

forms a free transitive \(\mathbb Z\)-orbit. This recovers the oriented line up to global translation.

Reflection

\[
p\mapsto VpV^{-1}
\]

has exactly one fixed coordinate projector, namely \(E_{00}\), so the root is recovered.

Correct.

### Terminology correction F

The article should say the line is reconstructed **up to unique isomorphism preserving the distinguished operators**. Avoid stronger categorical reconstruction language until a source/target category and functor are defined.

---

## 11. Audit of primitive-provenance loss

Every base-valued `oplus` translation component lies in the algebra already generated by

\[
U,U^{-1},V,a_+,a_-,C
\]

from signed kinematics and legacy `otimes` base translations.

Specifically:

- \(L_{x_0}^{\oplus}=I-e_0\);
- \(R_{x_0}^{\oplus}=\rho\) is generated by shifted tail projections;
- nonzero-argument base components are matrix units already generated from \(e_0\) and \(U\).

Thus adding distinguished `oplus` translations does not enlarge the generated base algebra.

The comparison source with the `oplus` primitive label/table removed therefore has the same generated base algebra.

The no-go theorem is correct.

### Scope correction G

This proves loss of **primitive provenance from the bare generated algebra**. It does not prove that provenance is unrecoverable from every conceivable enriched representation or from a category whose morphisms remember operation labels.

---

## 12. Audit of definedness erasure

A base-only shadow cannot distinguish:

- an undefined cell;
- a defined cell whose value lies in an erased terminal sort.

This is immediate and correct.

The minimal missing information is at least an operation-domain mask or equivalent typed incidence relation.

---

## 13. Audit of share/split separation

The `share` and `split` models agree on all base-valued translations and differ in terminal reflection cycles.

Hence:

- every base-only shadow collides;
- retaining the active terminal involutive set separates canonical share versus split;
- retaining terminal incidence is additionally required to reconstruct which operation cell produced which terminal element.

Correct.

---

## 14. Audit of finite-schema reconstruction

Within the **fixed minimal simultaneous-reflection-closure class**, the signed line plus the finite positive-ray schemata for `oplus` and `otimes`, terminal channel families, and terminal reflection uniquely determine the current signed M0 structure.

Correct.

### Scope correction H

The uniqueness depends essentially on the class restriction:

- legacy positive cells fixed;
- simultaneous reflection equivariance;
- no additional genuinely mixed-sign cells.

Without those constraints the same finite schema does not determine all possible signed extensions.

---

## 15. Publication novelty boundary

### Safe claims

The paper may claim the following as its own proved package:

1. an audited one-dimensional FCOA source has a direct-associativization collapse but a noncollapsing operator classicalization;
2. its existing legacy translations generate a root projector and hence a complete matrix-unit system;
3. the resulting finitary matrix layer and distinguished shift/reflection reconstruct the signed line geometry;
4. the same classical base algebra provably forgets primitive-operation provenance;
5. base erasure also forgets terminal-definedness and terminal-attachment layers;
6. these losses form a strict reconstruction-resolution ladder for the canonical signed M0 source family.

### Unsafe claims

Do not claim:

- discovery of matrix units;
- discovery of Toeplitz/Jacobson-style extensions;
- discovery of Leavitt path algebra phenomena;
- a universal reconstruction theorem for arbitrary partial algebras;
- Tannakian reconstruction;
- group-cohomological classification;
- a new spatial dimension;
- that all classical algebra is a quotient of FCOA in a physically meaningful sense.

---

## 16. Publication threshold

The package now contains:

- a positive theorem chain;
- an independent no-go chain;
- exact reconstruction statements;
- exact non-reconstruction statements;
- explicit classical prior-art boundaries;
- a closed one-dimensional scope.

Therefore:

\[
\boxed{\text{PUBLICATION THRESHOLD REACHED}.}
\]

Recommended article nucleus:

**Classical Algebra as a Resolution-Dependent Shadow of a One-Dimensional Partial Geometry: Collapse, Matrix Units, and Reconstruction in FCOA-Z**

The article should be prepared in English and Russian, with all statements numbered and proved, and should cite the earlier FCOA-Z publication as the signed-line foundation.