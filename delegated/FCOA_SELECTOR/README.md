# SOL-SELECTOR / FCOA Selector Line

Status: **OPEN RESEARCH LINE**

Branch: `director/fcoa-selector`

Parent checkpoint: `director/fcoa-z-symmetric-line`

## Purpose

`SOL-SELECTOR` studies whether candidate mixed-frontier completions of the base partial algebra `M0` can be selected by **intrinsic universal structure**, rather than by inserting a hidden preference for a particular completion such as `BR`, `B0`, or an `N_j` family.

The first layer is intentionally poor. It preserves the old `M0` exactly and allows the mixed frontier to vary.

The initial guiding principle is:

```math
\boxed{\text{preserve the old holes by identity, not their number.}}
```

## Frozen base data

Let

```math
D_0=\{\text{cells originally defined in }M_0\},
```

```math
M=(X^+\times X^-)\cup(X^-\times X^+),
```

and

```math
U_{\mathrm{prot}}=(X\times X)\setminus(D_0\cup M).
```

`M` is the mixed frontier that may be completed. `U_prot` is the protected part of the original undefinedness mask.

An admissible object must contain an exact copy of `M0`, preserve `D0`, not realize protected cells in `U_prot`, and may realize cells in `M`.

## First morphism layer

A morphism

```math
f:A\to B
```

is required to preserve only the inherited structure:

1. **Core fixation**: `f \circ i_A=i_B`.
2. **Root preservation**: `f(x_0)=x_0`.
3. **Translation equivariance** wherever translation is defined: `f(Tx)=Tf(x)`.
4. **Reflection equivariance**: `f(\nu x)=\nu f(x)`.
5. **Preservation of defined operations**:
   ```math
   a\oplus_A b\downarrow \Longrightarrow f(a)\oplus_B f(b)\downarrow,
   ```
   and
   ```math
   f(a\oplus_A b)=f(a)\oplus_B f(b).
   ```
6. No global injectivity requirement is imposed on newly created mixed outputs.

The first layer deliberately does **not** preserve any of the following as morphism data:

- the cardinality of `UNDEF` / `NONE`;
- number of new states;
- base-vs-external output sort;
- terminality or re-entry;
- Association Spectrum;
- exact automorphism group;
- `c_state`, `c_reentry`, or similar costs;
- arithmetic leakage;
- NIP, dp-minimality, or other model-theoretic complexity measures.

These may later become observables or secondary invariants, but they must not be built into the first category if they would preselect the desired completion.

## Initial universal objects to audit

### Pair-sensitive free one-step completion

For every unordered mixed pair `{x,y}` introduce a formal symbol

```math
e_{\{x,y\}}.
```

Define

```math
F_{\mathrm{mix}}
  =X\sqcup\{e_{\{x,y\}}:L_\pm(x,y)\},
```

with

```math
x\oplus_F y=y\oplus_F x=e_{\{x,y\}},
```

and

```math
\nu(e_{\{x,y\}})=e_{\{\nu x,\nu y\}}.
```

No re-entry operations on the new symbols are added at this stage.

**Working theorem T1 (Free one-step mixed extension).** Under the minimal morphism definition above, `F_mix` is the candidate initial object among locality-compatible one-step mixed extensions.

For any admissible target `A`, the forced map is

```math
\Phi_A(x)=x,
```

on the old carrier and

```math
\Phi_A(e_{\{x,y\}})=x\oplus_A y.
```

The theorem is currently accepted as the first target for formal proof and hostile audit, not yet as a publication theorem.

### Relation-only quotient

If the mixed law is allowed to see only the relation `L_\pm(x,y)` and not the endpoints, all mixed pairs become indistinguishable. The free one-step object then has a single mixed generator `e_L`:

```math
x\oplus y=e_L\qquad\forall L_\pm(x,y).
```

This object is identified with the structural candidate `B0`, with

```math
e_L=E_{\mathrm{cross}}.
```

**Working theorem T2 (Relation-only universality of B0).** `B0` is the candidate free relation-only mixed extension. Externality of `E_cross` is not an axiom of the category.

Therefore a target may map `E_cross` to an old state, including `x0`.

### Quotient ladder

The initial factorization pattern to investigate is

```math
\boxed{F_{\mathrm{mix}}\longrightarrow B0\longrightarrow BR.}
```

The first map forgets endpoint identity while retaining a distinct interaction event. The second additionally imposes

```math
E_{\mathrm{cross}}=x_0.
```

Thus `BR` is treated, at this stage, as a further quotient of `B0`, not as a categorically disconnected alternative.

In particular, under the weak preservation-only morphisms the candidate map

```math
B0\to BR,
\qquad E_{\mathrm{cross}}\mapsto x_0,
```

is expected to exist, whereas `BR\to B0` is expected to fail because the core-fixed mixed value `x0` cannot map to the distinct `E_cross`.

Other families `N_j` are to be tested as alternative quotient images of `F_mix` retaining radial information.

## Main research question

Before introducing an external real-valued cost functor, determine the kernel/congruence structure of admissible quotient maps:

```math
A\succeq B \iff \exists\,(A\to B).
```

The first goal is to decide whether a meaningful information order already arises from factorization and congruence inclusion.

Only if genuinely incomparable congruences survive should the branch escalate to an explicit multi-component cost vector such as

```math
\kappa=(c_{\mathrm{state}},c_{\mathrm{reentry}},c_{\mathrm{arith}},\ldots).
```

## Immediate audit queue

1. Formalize the object class precisely, including the status of protected undefined cells.
2. Prove or refute T1 with all equivariance conditions explicit.
3. Prove or refute T2 and isolate the exact meaning of `relation-only`.
4. Verify rigorously the existence of `B0 -> BR` and nonexistence of `BR -> B0`.
5. Compute kernels/congruences for `F_mix -> B0`, `F_mix -> BR`, and representative `F_mix -> N_j`.
6. Determine whether these quotients form a chain, lattice, preorder with nontrivial equivalence, or a more general factorization poset.
7. Check whether adding re-entry changes the initial object from one-step generators to genuine syntax trees.
8. Identify the first additional axiom that causes a true categorical bifurcation.

## Anti-bias rule

No future definition may be accepted merely because it makes `BR`, `B0`, or another favored model terminal, initial, minimal, rigid, or cheapest. Any added invariant must be justified independently of which candidate it selects.

---

Opened as an independent mathematical line inside the Commander Sol FCOA programme on 2026-08-31.
