# SOL-SELECTOR Research State

Date: 2026-08-31
Status: ACTIVE / foundational category layer stabilized

## Category closure audit

Completed in:

`CATEGORY_CLOSURE_AUDIT_0_1.md`

Verdict: **PASS AFTER TWO STRUCTURAL CORRECTIONS**.

The preservation-only morphisms do form the intended category once protected holes are treated as object admissibility conditions rather than reverse-definedness conditions on morphisms.

Two defects in the first sketch were found and repaired.

### Correction C1 — optional mixed domain

If admissible objects may leave mixed cells undefined, an object defining every mixed cell cannot be initial.

Therefore in the broad category

```math
\mathbf{Ext}_{\le M}(M_0)
```

the initial object is simply

```math
\boxed{M_0}.
```

The all-mixed free object belongs to the subcategory of **full mixed completions**.

### Correction C2 — ordered versus unordered mixed cells

Before mixed commutativity is imposed, the unbiased free completion must distinguish

```math
(x,y)
```

from

```math
(y,x).
```

Thus the true first full-completion free object is

```math
F_{\to},
```

with one formal output `e_(x,y)` for every ordered mixed cell.

The previously proposed

```math
F_{\mathrm{mix}}
```

is the quotient imposing mixed transposition symmetry.

## Current strongest structural theorem package

The corrected universal ladder is

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

with the following universal meanings.

1. `M0` is initial among optional mixed extensions.
2. `F_→` is initial among full mixed completions with no mixed commutativity assumed.
3. `F_mix` is initial among full mixed-commutative completions.
4. `B0` is initial among relation-only full mixed completions.
5. `BR` is the further weak quotient obtained by `E_cross=x0`.

The weak morphism

```math
B0\to BR
```

exists, while

```math
BR\to B0
```

does not exist if `E_cross != x0`.

Hence the weak selector category does not create a `B0/BR` bifurcation.

## First intrinsic information order

Inside the canonical quotient-generated subcategory of `F_mix`, admissible weak partial congruences control factorization:

```math
\theta_A\subseteq\theta_B
\iff
F_{\mathrm{mix}}/\theta_A
\longrightarrow
F_{\mathrm{mix}}/\theta_B.
```

Pure terminal-event quotients are classified by reflection-invariant partitions of the unordered mixed-pair set

```math
P=M/\tau.
```

`B0` is the one-block event partition. `BR` additionally anchors that event block to the old core point `x0`.

This separates:

```math
\text{event-event forgetting}
```

from

```math
\text{event-core collapse}.
```

No external real-valued cost is currently needed.

## First genuine bifurcation mechanisms identified

The arrow

```math
B0\to BR
```

is destroyed if one strengthens the first layer by either:

1. primitive output-sort/externalness preservation; or
2. strong reflection of definedness by morphisms.

Thus those stronger requirements are now identified as explicit **bifurcation axioms**, not neutral background structure.

## Transport convention

At the minimal one-step selector layer, inherited transport/translation acts exactly where it was already defined on the old core. No transport orbit is automatically added to fresh mixed events.

This avoids silently introducing re-entry or an additional unbounded coordinate resource.

## Re-entry status

Not part of the current theorem package.

If fresh outputs are required to re-enter the operation, the free object is expected to escalate from one-step event generators to a genuine term/tree closure modulo inherited equations and symmetries.

## Publication status

Still **not publication-ready** as a standalone paper.

The category nucleus is now substantially stronger and cleaner, but the next hostile-audit threshold is the classification of reflection-invariant event partitions and admissible event-to-core anchors, including concrete placement of radial `N_j` candidates.

## Immediate next strike

```math
\boxed{
\text{classify the quotient poset of }F_{\mathrm{mix}}
\text{ before introducing any numerical Cost functor.}
}
```

Specifically:

- classify reflection-invariant partitions of mixed event indices;
- classify which blocks may be anchored to old core points without violating weak compatibility;
- identify the radial statistics producing the `N_j` family;
- determine the first incomparable quotient kernels;
- decide whether the resulting quotient spectrum is a lattice or only a poset/preorder.
