# SOL-SELECTOR — Category Closure Audit 0.1

**Branch:** `director/fcoa-selector`  
**Date:** 2026-08-31  
**Status:** FOUNDATIONAL AUDIT / PROVED CORE WITH EXPLICIT SCOPE

---

## 0. Executive verdict

The original selector idea survives, but its first universal-object claim requires two corrections.

1. If mixed cells are optional, a structure that defines **all** mixed cells cannot be initial. In the broad optional-extension category the old structure `M0` itself is initial.
2. If no new mixed commutativity law is built into the object class, then a free object indexed by **unordered** mixed pairs is still too restrictive. The unbiased full mixed completion must first remember **ordered** mixed cells.

After these corrections the canonical weak-morphism ladder is

```math
\boxed{
M_0
\longrightarrow
F_{\to}
\longrightarrow
F_{\mathrm{mix}}
\longrightarrow
B0
\longrightarrow
BR.
}
```

The meanings of the rungs are:

- `M0`: no mixed cell is required;
- `F_→`: every ordered mixed cell has its own formal output;
- `F_mix`: transposition is forgotten, hence mixed commutativity is imposed;
- `B0`: endpoint identity is forgotten, but a distinct cross-event remains;
- `BR`: even the distinct cross-event is forgotten by identifying it with the root.

Thus the first obstruction is **domain-totality / law-strength mismatch**, not a `B0/BR` bifurcation.

---

# 1. Frozen source data

Let the old partial structure be

```math
\mathcal M_0.
```

Its full old universe is denoted by `C0`. The signed base line is a distinguished subset

```math
X\subseteq C_0,
```

with root `x0 in X`.

Let

```math
D_0
=
\operatorname{Dom}(\oplus_0)\cap (X\times X)
```

be the old defined base-base cells.

The mixed frontier is

```math
M=(X^+\times X^-)\cup(X^-\times X^+).
```

The protected old holes are

```math
U_{\mathrm{prot}}
=(X\times X)\setminus(D_0\cup M).
```

The parent FCOA-Z line proves that all residual reflection-compatible freedom in the base-base table is localized in these mixed sectors. It also gives the concrete `B0` rule

```math
x\oplus_{B0}y=E_{\mathrm{cross}}
\qquad ((x,y)\in M),
```

where `E_cross` is a fresh terminal output fixed by reflection.

The present audit uses only those structural facts.

---

# 2. Minimal selector signature

The first selector layer is deliberately one-sorted after forgetting output-sort labels.

This is essential: if `external output` were a primitive sort or predicate, then a map sending a new event to an old core point would already be prohibited and the category would contain the desired answer in its signature.

We retain:

1. the exact old structure `M0` as a distinguished embedded core;
2. the root;
3. the old partial binary operation(s);
4. zero reflection `nu` and its declared action on any new outputs;
5. inherited transport/translation only where it is already defined.

## Minimal transport convention

On the old core, transport is exactly the inherited transport. On newly created one-step mixed outputs, **no new transport value is declared unless forced by a later axiom**.

Therefore a preservation-only morphism obeys

```math
T_A(a)\downarrow
\Longrightarrow
T_B(f(a))\downarrow
\quad\text{and}\quad
f(T_Aa)=T_Bf(a),
```

but if `T_A(a)` is undefined there is no reverse requirement.

This resolves the apparent need to assign a translation orbit to every fresh event. Adding such orbits would be a stronger category and is postponed.

Reflection is different: for the reflection-compatible subproblem, every active output is equipped with the required involution action, so reflection equivariance is part of the object data.

---

# 3. The broad category `Ext_{<=M}(M0)`

## Definition 3.1 — admissible object

An object `A` consists of a partial algebra containing an injective copy

```math
i_A:\mathcal M_0\hookrightarrow A
```

such that:

1. the copy of `M0` is exact on every old defined operation/value;
2. no protected cell in `U_prot` becomes defined;
3. any newly defined base-base core cell belongs to `M`;
4. any subset of `M` may be opened, subject to the declared reflection compatibility of the object;
5. no primitive output-sort distinction is imposed;
6. re-entry, new-state count, terminality, arithmetic leakage and model-theoretic complexity are not morphism invariants.

New one-step outputs may be fresh, or a mixed value may already lie in the old core.

## Definition 3.2 — weak core-fixed morphism

A morphism

```math
f:A\to B
```

satisfies:

### (M1) Core fixation

```math
f\circ i_A=i_B.
```

### (M2) Preservation of every source-defined partial operation

For the binary operation:

```math
a\oplus_A b\downarrow
\Longrightarrow
f(a)\oplus_B f(b)\downarrow
```

and

```math
f(a\oplus_A b)
=
f(a)\oplus_B f(b).
```

The same one-way rule is used for declared partial unary maps such as transport.

### (M3) Reflection equivariance

```math
f(\nu_A a)=\nu_Bf(a)
```

on the declared reflection domain.

There is no converse definedness condition and no injectivity requirement outside the fixed old core.

---

# 4. Category closure

## Theorem 4.1 — Category Closure Theorem

The admissible objects and weak core-fixed morphisms form a category

```math
\mathbf{Ext}_{\le M}(M_0).
```

### Proof

For every object `A`, the identity map fixes the core, preserves every source-defined operation, and commutes with every declared unary symmetry. Hence `id_A` is a morphism.

Now let

```math
A\xrightarrow{f}B\xrightarrow{g}C
```

be morphisms.

Core fixation is closed under composition:

```math
(g\circ f)\circ i_A
=g\circ i_B
=i_C.
```

If

```math
a\oplus_A b\downarrow,
```

then preservation by `f` gives

```math
f(a)\oplus_B f(b)\downarrow
```

and

```math
f(a\oplus_A b)=f(a)\oplus_B f(b).
```

Preservation by `g` then gives

```math
gf(a)\oplus_C gf(b)\downarrow
```

and

```math
gf(a\oplus_A b)
=g(f(a)\oplus_B f(b))
=gf(a)\oplus_C gf(b).
```

The same argument applies to every partial unary map. Reflection equivariance composes:

```math
(gf)(\nu_Aa)
=g(\nu_Bf(a))
=\nu_Cgf(a).
```

Associativity of morphism composition and the identity laws are inherited from ordinary function composition. Therefore the data form a category. `square`

## Lemma 4.2 — protected holes belong to the object axioms

The condition

```math
U_{\mathrm{prot}}\cap\operatorname{Dom}(\oplus_A)=\varnothing
```

is an admissibility condition on each object, not a reverse-definedness requirement on morphisms.

### Proof

A morphism never changes the operation table of its target; it only maps elements. Therefore preservation of protected core holes is guaranteed by requiring every target object separately to satisfy the protected-hole axiom. Adding the converse implication

```math
f(a)\oplus_B f(b)\downarrow
\Longrightarrow
a\oplus_A b\downarrow
```

would strengthen the morphism notion and would no longer be the intended preservation-only category. `square`

---

# 5. The first obstruction: optional mixed definedness

## Proposition 5.1 — `M0` is initial in the broad category

The old structure `M0`, viewed as the extension with no new mixed cells, is an initial object of

```math
\mathbf{Ext}_{\le M}(M_0).
```

### Proof

For every admissible object `A`, core fixation forces any morphism

```math
M_0\to A
```

to be exactly the distinguished embedding `i_A`. Since `A` is an extension of `M0`, this embedding preserves every operation defined in `M0`, and it preserves all inherited unary structure. Hence it is a morphism. It is unique because every element of the source belongs to the fixed old core. `square`

This is the correct universal statement at the completely unbiased optional-domain level.

## Proposition 5.2 — Domain-Totality Obstruction

Suppose a candidate source `F` defines a mixed cell `p in M`. If the category contains an admissible target `A` in which `p` is undefined, then there is no weak morphism

```math
F\to A
```

that fixes the old core.

### Proof

If

```math
p=(x,y)
```

and `x oplus_F y` is defined, preservation of source-defined operations requires

```math
x\oplus_A y\downarrow,
```

because core fixation sends `x,y` to themselves. This contradicts the assumed undefinedness of `p` in `A`. `square`

### Corollary 5.3

The originally proposed all-mixed object `F_mix` is **not** initial in the broad category if objects are allowed to leave mixed cells undefined.

The failure is structural, not technical.

---

# 6. Full mixed completions and the orientation obstruction

Define the full mixed-completion subcategory

```math
\mathbf{Comp}_M(M_0)
\subseteq
\mathbf{Ext}_{\le M}(M_0)
```

by requiring

```math
M\subseteq\operatorname{Dom}(\oplus_A).
```

No commutativity is imposed yet.

## Proposition 6.1 — Unordered-Pair Obstruction

An object having a single generator `e_{\{x,y\}}` with

```math
x\oplus y
=
y\oplus x
=
e_{\{x,y\}}
```

cannot be initial in `Comp_M(M0)` if that category admits even one target with

```math
x\oplus_Ay\ne y\oplus_Ax.
```

### Proof

For any core-fixed homomorphism `f`, preservation would force simultaneously

```math
f(e_{\{x,y\}})=x\oplus_Ay
```

and

```math
f(e_{\{x,y\}})=y\oplus_Ax.
```

Hence the two target values would have to be equal. `square`

Thus mixed commutativity cannot be smuggled into the completely unbiased free object.

---

# 7. The true unbiased free full completion `F_→`

For every **ordered** mixed cell

```math
p=(x,y)\in M
```

introduce a fresh formal generator

```math
e_p=e_{(x,y)}.
```

Set

```math
|F_{\to}|
=C_0\sqcup\{e_{(x,y)}:(x,y)\in M\}.
```

The old structure on `C0` is unchanged, and

```math
x\oplus_{F_{\to}}y=e_{(x,y)}
\qquad((x,y)\in M).
```

No further operation with a fresh generator as input is declared at this stage.

Reflection acts by

```math
\nu(e_{(x,y)})
=e_{(\nu x,\nu y)}.
```

This is well-defined because simultaneous reflection preserves `M`.

Transport remains inherited on the old core and is left undefined on fresh one-step outputs in the minimal selector signature.

## Theorem 7.1 — Free Full-Completion Theorem

`F_→` is initial in `Comp_M(M0)` among reflection-compatible completions in the minimal selector signature.

### Proof

Let `A` be any object of `Comp_M(M0)`.

Define

```math
\Phi_A:F_{\to}\to A
```

by core fixation on `C0` and

```math
\Phi_A(e_{(x,y)})
=x\oplus_Ay.
```

This is defined for every generator because every mixed cell is defined in `A`.

For an old operation cell, preservation holds because the old core is exact. For a mixed cell,

```math
\Phi_A(x\oplus_{F_{\to}}y)
=\Phi_A(e_{(x,y)})
=x\oplus_Ay
=\Phi_A(x)\oplus_A\Phi_A(y).
```

There are no additional source-defined one-step operations requiring verification.

Reflection equivariance on a generator follows from reflection equivariance of `A`:

```math
\Phi_A(\nu e_{(x,y)})
=\Phi_A(e_{(\nu x,\nu y)})
=\nu x\oplus_A\nu y
=\nu(x\oplus_Ay)
=\nu\Phi_A(e_{(x,y)}).
```

On the old core it holds by the inherited structure.

Uniqueness is forced: every old element is fixed, and for every mixed generator homomorphism preservation gives

```math
\Phi(e_{(x,y)})
=\Phi(x\oplus_{F_{\to}}y)
=x\oplus_Ay.
```

Hence exactly one morphism exists. `square`

---

# 8. Mixed commutativity as the first quotient, not a base axiom

Let `theta_tau` be the least reflection-compatible equivalence identifying

```math
e_{(x,y)}\sim e_{(y,x)}
```

for every mixed pair.

Define

```math
F_{\mathrm{mix}}:=F_{\to}/\theta_\tau.
```

Its fresh generators may be written

```math
e_{\{x,y\}}.
```

Then

```math
x\oplus_{F_{\mathrm{mix}}}y
=
y\oplus_{F_{\mathrm{mix}}}x
=e_{\{x,y\}}.
```

Reflection is

```math
\nu(e_{\{x,y\}})
=e_{\{\nu x,\nu y\}}.
```

Define `Comp_M^comm(M0)` to be the full subcategory of `Comp_M(M0)` whose mixed law is commutative.

## Theorem 8.1 — Corrected Free Mixed Theorem

```math
\boxed{
F_{\mathrm{mix}}
\text{ is initial in }
\mathbf{Comp}^{\mathrm{comm}}_M(M_0).
}
```

### Proof

The proof of Theorem 7.1 factors through `theta_tau` precisely when

```math
x\oplus_Ay=y\oplus_Ax
```

for every mixed pair. In that case

```math
\Phi_A(e_{\{x,y\}})=x\oplus_Ay
```

is well-defined, operation preserving, reflection-equivariant and forced on every generator. Conversely, existence of a homomorphism from `F_mix` forces the same equality by Proposition 6.1. `square`

This is the rigorous form of the original `F_mix` claim.

---

# 9. `B0` as the relation-only quotient

Let

```math
P=M/\tau
```

be the set of unordered mixed pairs.

Let `theta_L` be the least reflection-compatible equivalence on `F_mix` identifying **all** fresh mixed generators:

```math
e_p\sim e_q
\qquad(p,q\in P).
```

Do not identify that common class with any old core element.

Then

```math
F_{\mathrm{mix}}/\theta_L
```

has one fresh mixed event, call it `E_cross`, and

```math
x\oplus y=E_{\mathrm{cross}}
\qquad((x,y)\in M).
```

This is exactly the `B0` construction recorded in the parent file

`MIXED_COMMUTATIVE_BRIDGE_GENERATOR_0_1.md`.

Because reflection permutes `P`, the unique class is reflection-fixed:

```math
\nu(E_{\mathrm{cross}})=E_{\mathrm{cross}}.
```

## Definition 9.1 — relation-only target

A full mixed target `A` is relation-only at this layer if there exists one element `c_A` such that

```math
x\oplus_Ay=c_A
\qquad\text{for every }(x,y)\in M.
```

No requirement says that `c_A` is new or external.

Reflection equivariance automatically implies

```math
\nu(c_A)=c_A.
```

## Theorem 9.2 — Relation-Only Universality of `B0`

`B0` is initial in the full subcategory of relation-only targets.

### Proof

For a relation-only target `A`, define the map to fix the old core and send

```math
E_{\mathrm{cross}}\mapsto c_A.
```

Every mixed source cell then preserves its value, and reflection equivariance holds because both event values are reflection-fixed. Uniqueness follows because the image of `E_cross` is forced by any one mixed cell. `square`

### Consequence

The universal property of `B0` does **not** require externality.

In particular, `c_A` may equal `x0`.

---

# 10. `BR` is a further weak quotient

For SOL-SELECTOR, define the root-return object `BR` by keeping the old core fixed and setting

```math
x\oplus_{BR}y=x_0
\qquad((x,y)\in M).
```

This is the `BR` used in the selector brief. It is a selector object, not a newly claimed canonical object of the parent FCOA-Z line.

## Proposition 10.1 — canonical collapse `B0 -> BR`

There is a weak core-fixed morphism

```math
q_R:B0\to BR
```

with

```math
q_R(E_{\mathrm{cross}})=x_0
```

and identity on the old core.

### Proof

Old operation values are preserved by identity. For every mixed pair,

```math
q_R(x\oplus_{B0}y)
=q_R(E_{\mathrm{cross}})
=x_0
=x\oplus_{BR}y.
```

Reflection is preserved because both `E_cross` and `x0` are reflection-fixed. Under the minimal transport convention, no transport value is defined on `E_cross`, so mapping it to the transport-active core point `x0` creates no reverse-definedness obligation. `square`

## Proposition 10.2 — no reverse morphism

If

```math
E_{\mathrm{cross}}\ne x_0
```

in `B0`, then there is no core-fixed weak morphism

```math
BR\to B0.
```

### Proof

Assume `h:BR -> B0` exists. For any mixed pair `(x,y)`, source preservation gives

```math
h(x_0)
=h(x\oplus_{BR}y)
=h(x)\oplus_{B0}h(y)
=E_{\mathrm{cross}}.
```

But core fixation requires

```math
h(x_0)=x_0.
```

Hence `x0=E_cross`, contradiction. `square`

Therefore

```math
\boxed{B0\longrightarrow BR}
```

is a genuine directed comparison in the weak selector category.

---

# 11. Why this is a weak-congruence problem

For total universal algebras, quotient kernels are ordinary congruences. Here partiality matters.

The collapse

```math
E_{\mathrm{cross}}\sim x_0
```

identifies a terminal one-step event with a core state that may possess additional defined operations or transport. Thus it need not be a congruence under a **strong** notion that reflects definedness.

The appropriate first-layer notion is weaker.

## Definition 11.1 — weak partial congruence

An equivalence relation `theta` on a partial algebra `A` is weakly compatible if whenever

```math
a_i\mathrel\theta b_i
```

and the same primitive operation is defined on both tuples, the two results are `theta`-equivalent.

No requirement is imposed when the operation is defined for one representative tuple and undefined for another.

For the selector quotient class we additionally require:

1. distinct old core elements are never identified;
2. reflection compatibility holds;
3. the induced quotient does not realize a protected core cell in `U_prot`.

The quotient operation is defined on classes whenever at least one representative tuple is defined; weak compatibility guarantees independence of the chosen **defined** representative.

Under this notion the root collapse is admissible.

---

# 12. The factorization order must be scoped to canonical quotients

For arbitrary weak morphisms

```math
A\to B,
```

kernel inclusion alone need not control factorization, because a target may contain extra defined operations or unrelated states not generated by the source.

Therefore the congruence spectrum is defined first on the canonical quotient-generated subcategory

```math
\mathbf{Quot}(F_{\mathrm{mix}}).
```

Its objects are quotients

```math
q_\theta:F_{\mathrm{mix}}\twoheadrightarrow F_{\mathrm{mix}}/\theta
```

by admissible weak partial congruences, with the quotient structure induced from representatives.

## Theorem 12.1 — Kernel/Factorization Correspondence

For admissible weak congruences `theta_A, theta_B`, the canonical quotient map

```math
F_{\mathrm{mix}}/\theta_A
\longrightarrow
F_{\mathrm{mix}}/\theta_B
```

exists if and only if

```math
\theta_A\subseteq\theta_B.
```

### Proof

If `theta_A subseteq theta_B`, define

```math
[a]_{\theta_A}\mapsto[a]_{\theta_B}.
```

This is well-defined by inclusion and preserves every quotient operation by construction from representatives. It fixes the old core because both congruences separate old core points.

Conversely, if the canonical quotient through `theta_A` factors through the quotient by `theta_B`, then any pair identified by `theta_A` must have the same image in the `theta_B` quotient, hence is also `theta_B`-equivalent. `square`

Thus within the quotient-generated sector,

```math
A\succeq B
\iff
A\to B
```

is exactly growth of the weak kernel:

```math
\ker q_A\subseteq\ker q_B.
```

This is the first intrinsic information order. No real-valued cost has been introduced.

---

# 13. Pure event quotient spectrum

Remain inside `F_mix`, so the index set is

```math
P=M/\tau.
```

Consider quotients that do not attach a fresh-event class to an old core element and add no re-entry law.

## Theorem 13.1 — event partitions

Pure event quotients of `F_mix` are classified by reflection-invariant partitions of `P`.

### Proof

Because fresh event generators are terminal at the one-step level, the only non-core structural relation among them is the reflection action

```math
p\mapsto\nu p.
```

An equivalence relation among event generators therefore yields a well-defined pure quotient exactly when it is invariant under this action. Such equivalence relations are precisely reflection-invariant partitions of `P`. `square`

Important examples:

- `F_mix`: the discrete partition of `P`;
- `B0`: the one-block partition of `P`, still disjoint from the core;
- radial `N_j`-type candidates: intermediate partitions when their output law depends only on a declared radial statistic.

The `BR` step is not merely another pure partition: it **anchors** the unique `B0` event block to the fixed core point `x0`.

This cleanly separates two information losses:

```math
\text{event-event identification}
```

from

```math
\text{event-core identification}.
```

---

# 14. Where a true `B0/BR` bifurcation actually appears

The weak selector category intentionally permits

```math
B0\to BR.
```

That arrow disappears as soon as one adds either of the following stronger structures.

## 14.1 Output-sort preservation

If `External(z)` is a primitive predicate with

```math
External(E_{\mathrm{cross}})
```

and

```math
not External(x_0),
```

then a morphism preserving that predicate cannot send `E_cross` to `x0`.

## 14.2 Strong reflection of definedness

If morphisms are required to satisfy the converse condition

```math
f(a)\oplus_Bf(b)\downarrow
\Longrightarrow
a\oplus_A b\downarrow
```

(and analogously for unary transport), then a terminal event generally cannot collapse to a re-entering core point without violating strong partiality preservation.

Hence a genuine categorical bifurcation is created by **adding output typing or strong definedness reflection**.

That is precisely why neither belongs to the first selector layer.

---

# 15. Re-entry escalation

The one-step free objects above are not term algebras.

If a later axiom requires fresh mixed outputs to re-enter the operation, then new expressions such as

```math
(e_p\oplus x),
\qquad
(x\oplus e_p),
\qquad
(e_p\oplus e_q)
```

may themselves have to exist. Repeated closure then produces genuine syntax trees modulo the inherited equations and symmetry relations.

Therefore:

```math
\boxed{
\text{one-step free events}
\quad\longrightarrow\quad
\text{free term/tree closure}
}
```

is a separate categorical transition, not part of the present theorem.

---

# 16. Corrected universal ladder

The audit yields four nested levels rather than one prematurely chosen category.

## Level U0 — optional domain

```math
\mathbf{Ext}_{\le M}(M_0),
\qquad
\operatorname{Init}=M_0.
```

## Level U1 — all mixed ordered cells required

```math
\mathbf{Comp}_M(M_0),
\qquad
\operatorname{Init}=F_{\to}.
```

## Level U2 — mixed commutativity required

```math
\mathbf{Comp}^{\mathrm{comm}}_M(M_0),
\qquad
\operatorname{Init}=F_{\mathrm{mix}}.
```

## Level U3 — relation-only mixed law

```math
\mathbf{Rel}_M(M_0),
\qquad
\operatorname{Init}=B0.
```

`BR` is a further quotient obtained by the additional equation

```math
E_{\mathrm{cross}}=x_0.
```

It is not selected by the preceding universal properties.

---

# 17. Final verdict

The original Free-Syntax intuition was correct but one level too compressed.

The first unbiased free object is not `F_mix`; it is the ordered-cell object `F_→`. Mixed commutativity is itself an information-losing quotient. The corrected structural picture is therefore

```math
\boxed{
M_0
\to
F_{\to}
\to
F_{\mathrm{mix}}
\to
B0
\to
BR.
}
```

The first layer does **not** force a `B0/BR` bifurcation.

Instead it exposes an intrinsic hierarchy of forgetting:

```math
\text{optional interaction}
\to
\text{ordered event identity}
\to
\text{unoriented event identity}
\to
\text{relation-only event}
\to
\text{root collapse}.
```

This is stronger than an externally chosen Pareto cost because the first information order is already encoded by weak kernels and factorization.

The next research strike should classify the reflection-invariant event partitions and the admissible event-to-core anchors, then place concrete `N_j` laws inside that poset.

---

## Parent files checked in this audit

- `delegated/FCOA_Z_SYMMETRIC_LINE/SIGNED_COMPLETION_FOUNDATION_0_1.md`
- `delegated/FCOA_Z_SYMMETRIC_LINE/MIXED_SECTOR_LOCALIZATION_PRINCIPLE_0_1.md`
- `delegated/FCOA_Z_SYMMETRIC_LINE/MIXED_SECTOR_MINIMAL_COUPLING_0_1.md`
- `delegated/FCOA_Z_SYMMETRIC_LINE/MIXED_COMMUTATIVE_BRIDGE_GENERATOR_0_1.md`
- `delegated/FCOA_Z_SYMMETRIC_LINE/STATE.md`
- `delegated/FCOA_Z_SYMMETRIC_LINE/ONE_DIMENSIONAL_CLASSICALIZATION_COST_0_1.md`
