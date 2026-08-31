# SOL-SELECTOR Research State

Date: 2026-08-31
Status: ACTIVE / quotient geometry established

## Completed packages

1. `CATEGORY_CLOSURE_AUDIT_0_1.md`
2. `QUOTIENT_POSET_0_1.md`

## Universal category layer

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

with:

- `M0` initial among optional mixed extensions;
- `F_→` initial among full ordered mixed completions;
- `F_mix` initial after mixed commutativity is imposed;
- `B0` initial among relation-only mixed completions;
- `BR` the further weak quotient `E_cross=x0`.

`B0 -> BR` exists; `BR -> B0` does not when `E_cross != x0`.

## New quotient-poset theorem package

After mixed commutativity, fresh events are canonically indexed by

```math
p_{ij}=\{P_i^+,P_j^-\},
\qquad i,j\ge1,
```

and reflection acts by

```math
\nu(p_{ij})=p_{ji}.
```

Therefore pure terminal-event quotients are exactly transposition-invariant equivalence relations on

```math
\mathbb N_{>0}^2.
```

They form a **complete lattice** under intersection and equivalence closure of unions.

## First exact incomparable quotients

Canonical radial test quotients were introduced:

```math
N_\Sigma(i,j)=i+j,
```

```math
N_\Delta(i,j)=|i-j|.
```

Their kernels are incomparable:

```math
\boxed{
\ker N_\Sigma\not\subseteq\ker N_\Delta,
\qquad
\ker N_\Delta\not\subseteq\ker N_\Sigma.
}
```

Exact meet:

```math
\boxed{
\ker N_\Sigma\wedge\ker N_\Delta
=\ker N_{orb},
}
```

where

```math
N_{orb}(i,j)=\{i,j\}.
```

Exact join:

```math
\boxed{
\ker N_\Sigma\vee\ker N_\Delta
=\ker N_{par},
}
```

where

```math
N_{par}(i,j)=(i+j)\bmod2.
```

Hence the selector spectrum is provably **not a chain**. It contains a genuine internal diamond-like interval before any numerical cost is introduced.

## B1 placement resolved

The parent `B1` construction assigns a separate terminal output to each unoriented mixed bridge.

At the `F_mix` stage this is exactly the free mixed-commutative event object, so in the current one-step selector category:

```math
\boxed{B1\cong F_{mix}.}
```

## Anchoring theorem package

Allowing event classes to identify with old core points changes the order theory.

At the one-step weak level, anchored kernels are reflection-stable equivalence relations on

```math
C_0\sqcup E
```

whose restriction to `C0` is equality.

Every event block contains at most one core anchor.

Reflection forces an anchor of `C` at `a` to be paired with an anchor of `nu(C)` at `nu(a)`.

For a reflection-fixed event block, the anchor must be reflection-fixed. On the signed base line the unique such base point is `P0`.

Therefore:

```math
\boxed{
BR\text{ is the unique reflection-compatible base-line anchoring of }B0.
}
```

## First non-lattice obstruction

If one admissible quotient anchors the same event block to core point `a` and another anchors it to distinct core point `b`, no common admissible upper bound exists: any upper kernel would force `a~b`, violating pointwise core separation.

Thus:

```math
\boxed{
\text{pure event quotients form a complete lattice,}
}
```

but

```math
\boxed{
\text{the anchored quotient spectrum is generally only a poset; joins may fail.}
}
```

This is the first intrinsic non-lattice bifurcation of SOL-SELECTOR.

## Status of `N_j`

Earlier repository notes referred generically to radial `N_j` candidates but did not freeze a unique formula.

`QUOTIENT_POSET_0_1.md` therefore introduces rigorously specified canonical test families (`N_orb`, `N_Sigma`, `N_Delta`, `N_par`) without retroactively claiming that these were the exact intended historical `N_j` formulas.

A reflection-paired depth-anchor family is also available if a future naming decision wants to reserve `N_j` for anchored radial quotients.

## Cost-functor decision

The trigger condition for considering a Pareto cost has been met because incomparable kernels exist.

Nevertheless **do not introduce a scalar cost yet**. The intrinsic quotient order contains more structure than a scalar ranking and would be damaged by premature linearization.

First compute intrinsic order-theoretic observables: meet/join profile, reflection-orbit profile, fixed classes, anchorability and anchor-incompatibility graph.

## Publication status

**Not yet standalone-publication ready, but now close to the first real publication threshold.**

The category and quotient-order nuclei are substantive. The remaining critical audit is whether the radial statistics used to exhibit incomparability are intrinsic to the inherited FCOA geometry or silently import ordinary arithmetic.

## Immediate next strike

```math
\boxed{
\text{Intrinsic Definability Audit of radial quotient statistics.}
}
```

Determine whether `N_orb`, `N_Sigma`, `N_Delta`, and `N_par` can be generated/defined from the rooted reflected FCOA line without importing forbidden binary integer addition or subtraction.

The publication-grade target is an incomparable pair of quotients whose defining statistics are themselves intrinsic FCOA constructions.
