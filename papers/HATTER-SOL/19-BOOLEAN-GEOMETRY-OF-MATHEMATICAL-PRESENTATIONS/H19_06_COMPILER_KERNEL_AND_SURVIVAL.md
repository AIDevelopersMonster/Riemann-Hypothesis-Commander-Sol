# H19-06 · Compiler Kernel and Presentation Survival

Status: **FOUNDATIONAL DRAFT / motivated by closed H19-04 evidence**

## 1. Motivation

H19-04 gives an exact controlled example:

\[
DIRECT12\neq PREFIX19
\]

as source mathematical/SLP presentations, because

\[
24\neq19
\]

declared permutation-composition nodes.

Yet under the fixed open Yosys flow they have the same reported cell
histogram both after \`proc/flatten/opt\` and after \`techmap/opt\`:

\[
4919=4919,
\]

\[
63719=63719.
\]

Their wire graphs are still different, so one must not call the resulting
netlists identical.  What is equal is a declared observable of the compiled
images.

This motivates a precise quotient construction.

---

## 2. Compilation stage

Fix:

- a semantic task \(\Phi\);
- a class \(\mathcal P(\Phi)\) of E0-equivalent mathematical presentations;
- an encoding convention;
- a realization front-end \(B_\Pi\);
- a deterministic or seed-frozen compiler stage \(S\).

Define

\[
C_{S,\Pi}(M)=S(B_\Pi(M)).
\]

The codomain may be RTL netlists, generic Boolean netlists, technology-mapped
netlists, or placed/routed implementations.

---

## 3. Observable

A compiled object can be observed at different resolutions.

Let

\[
O:C\to Z
\]

be a declared observable.

Examples:

- total cell count;
- complete cell-type histogram;
- wire-count vector;
- graph isomorphism class;
- critical-path depth;
- FPGA physical profile;
- Pareto resource vector.

No observable is assumed complete.

---

## 4. Compiler-profile equivalence

### Definition 4.1

For fixed \((S,\Pi,O)\), define

\[
M_1\sim_{S,\Pi,O} M_2
\]

iff

\[
O(C_{S,\Pi}(M_1))
=
O(C_{S,\Pi}(M_2)).
\]

### Proposition 4.2

\(\sim_{S,\Pi,O}\) is an equivalence relation on the domain on which
\(C_{S,\Pi}\) and \(O\) are defined.

### Proof

Equality in \(Z\) is reflexive, symmetric, and transitive.  Pulling equality
back through the map \(O\circ C_{S,\Pi}\) preserves these three properties.
\(\square\)

The equivalence classes form the quotient

\[
\boxed{
\mathcal P(\Phi)/{\sim_{S,\Pi,O}}.
}
\]

We call this the **compiler-profile quotient**.

---

## 5. Compiler kernel

By analogy with a kernel relation of a map, define

\[
\boxed{
\ker_O(C_{S,\Pi})
=
\{(M_1,M_2):
O(C_{S,\Pi}(M_1))=O(C_{S,\Pi}(M_2))\}.
}
\]

This is a kernel **relation**, not necessarily an algebraic kernel in the
group/ring sense.

A nontrivial pair

\[
M_1\ne M_2,
\qquad
(M_1,M_2)\in\ker_O(C_{S,\Pi})
\]

means that the compiler stage has made the two presentations indistinguishable
at observable resolution \(O\).

H19-04 supplies such a pair for the cell-histogram observable:

\[
\boxed{
DIRECT12\sim_{\rm Yosys,open,cellhist}PREFIX19.
}
\]

---

## 6. Observable refinement

Suppose \(O_2\) refines \(O_1\), meaning that equality under \(O_2\) implies
equality under \(O_1\).

Then

\[
\ker_{O_2}(C)
\subseteq
\ker_{O_1}(C).
\]

Thus a coarse metric such as total cell count has a larger kernel than a full
netlist-isomorphism observable.

This is important for H19-04:

- total cell count: DIRECT12 and PREFIX19 coincide;
- complete reported cell histogram: they still coincide;
- wire-count vector: they differ.

Therefore the statement is not

\[
C(DIRECT12)=C(PREFIX19),
\]

but rather

\[
O_{\rm cellhist}(C(DIRECT12))
=
O_{\rm cellhist}(C(PREFIX19)).
\]

---

## 7. Compilation tower

Let a compiler flow have stages

\[
S_0,S_1,\ldots,S_k.
\]

For H19 one useful tower is

\[
\text{source}
\to
\text{proc/opt}
\to
\text{techmap}
\to
\text{ABC}
\to
\text{FPGA synthesis}
\to
\text{place/route}.
\]

For one presentation pair \((M_1,M_2)\), define its **survival signature**

\[
\boxed{
\Sigma_O(M_1,M_2)
=
(\epsilon_0,\ldots,\epsilon_k),
}
\]

where

\[
\epsilon_i=
\begin{cases}
1,&O(C_{S_i}(M_1))\ne O(C_{S_i}(M_2)),\\
0,&O(C_{S_i}(M_1))=O(C_{S_i}(M_2)).
\end{cases}
\]

This records at which compiler stages a mathematical distinction remains
visible at resolution \(O\).

For DIRECT12 versus PREFIX19, current evidence gives:

### source composition-node observable

\[
24\ne19.
\]

### post-proc cell histogram

\[
4919=4919.
\]

### post-techmap Boolean-cell histogram

\[
63719=63719.
\]

Hence, for the corresponding mixed-resolution record,

\[
\boxed{
\text{visible at source}
\to
\text{invisible in optimized cell histogram}.
}
\]

The wire-profile observable survives longer because the wire counts remain
different.

---

## 8. Forgetting stage

For a fixed observable and a monotone compiler tower, one may define the first
stage at which a distinction becomes invisible:

\[
f_O(M_1,M_2)
=
\min\{i:
O(C_{S_i}(M_1))=O(C_{S_i}(M_2))\}.
\]

This definition is meaningful only if later stages do not re-separate the
chosen observable, or if the definition is explicitly interpreted as the
**first** forgetting event rather than permanent forgetting.

H19 will therefore measure complete survival signatures rather than assume
monotonicity.

---

## 9. Presentation-preserving versus open compilation

The new H19-05 experiment compares two realization disciplines:

\[
\Pi_{\rm open}
\]

and

\[
\Pi_{\rm preserve}.
\]

The intended question can now be written as a kernel comparison:

\[
\boxed{
\ker_O(C_{S,\Pi_{\rm preserve}})
\subseteq
\ker_O(C_{S,\Pi_{\rm open}})?
}
\]

This inclusion is not assumed universally.

For the controlled H19 family we ask empirically whether preservation
boundaries make the compiler kernel strictly smaller.

The module-preserving DIRECT12/PREFIX19 experiment is designed to test exactly
this statement.

---

## 10. Presentation sensitivity

For a finite controlled family

\[
\mathcal F=\{M_1,\ldots,M_n\},
\]

define the observable number of compiler-profile classes

\[
N_{S,\Pi,O}(\mathcal F)
=
\left|
\mathcal F/{\sim_{S,\Pi,O}}
\right|.
\]

A compiler/observable pair with

\[
N=1
\]

forgets all differences inside the family at that resolution.

A larger \(N\) preserves more distinctions.

This is deliberately a relative finite-family statistic, not a universal
complexity invariant.

For the current family under the open post-techmap cell-histogram observable:

\[
\{DIRECT12,PREFIX19,NIELSEN12\}
\]

forms two observed classes:

\[
\boxed{
\{DIRECT12,PREFIX19\},
\qquad
\{NIELSEN12\}.
}
\]

Thus

\[
\boxed{
N_{\rm open,cellhist}=2
}
\]

on the three-presentation family.

---

## 11. Why this matters

The original H18 question was:

> How do different mathematics map into different hardware?

H19-04 forces a sharper version:

> Which distinctions between mathematical presentations survive a given
> compiler, and which are quotiented out before physical mapping?

This turns the compiler from a passive implementation tool into an explicit
map whose information loss can itself be studied.

---

## 12. Claim boundary

The compiler kernel is relative to:

- presentation family;
- encoding;
- realization discipline;
- compiler and version;
- compiler settings/seed;
- chosen observable.

It is not a technology-independent invariant of mathematics.

The theoretical object is the pullback equivalence relation of a declared map.
The scientific work is to identify useful observables and determine whether
their survival/forgetting behavior has stable structural predictors.


## 13. First strict kernel-separation experiment

H19-05 supplies a direct comparison of two realization disciplines on the same
E0 family.

Let

\[
\mathcal F=
\{DIRECT12,PREFIX19,NIELSEN12\}.
\]

### Open flow

At the post-techmap generic cell-histogram level,

\[
DIRECT12\sim PREFIX19,
\]

while NIELSEN12 is separated.

Thus

\[
\boxed{
N_{\rm open,cellhist}(\mathcal F)=2.
}
\]

The observed classes are

\[
\{DIRECT12,PREFIX19\},
\qquad
\{NIELSEN12\}.
\]

### Module-preserving flow

With declared permutation primitives retained as hierarchy, the core instance
profiles are:

\[
DIRECT12:
24\,compose+2\,inverse,
\]

\[
PREFIX19:
19\,compose+2\,inverse,
\]

\[
NIELSEN12_{\rm decomposed}:
24\,compose+21\,inverse.
\]

The corresponding core cell counts are

\[
1591,\qquad1586,\qquad1610.
\]

Hence all three presentations are distinguished by the hierarchical
cell/instance observable:

\[
\boxed{
N_{\rm module,hier}(\mathcal F)=3.
}
\]

In particular, on the controlled pair

\[
\mathcal F_2=\{DIRECT12,PREFIX19\},
\]

the open compiler identifies the pair while the module-preserving compiler
separates it.

Therefore, for the induced equivalence relations on \(\mathcal F_2\),

\[
\boxed{
\ker(C_{\Pi_{\rm module}})
\subsetneq
\ker(C_{\Pi_{\rm open}})
}
\]

at the stated profile resolutions.

This is a finite experimental theorem-example of **compiler-controlled
presentation forgetting**.

### Caution

The current NIELSEN12 module profile decomposes Nielsen moves into direct
permutation primitives.  A native Nielsen-move hierarchy is being tested
separately.  The strict DIRECT12/PREFIX19 kernel separation does not depend on
that refinement.
