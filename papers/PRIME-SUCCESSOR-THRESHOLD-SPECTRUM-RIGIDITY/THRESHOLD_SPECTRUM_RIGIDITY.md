# Theorem Checkpoint — Threshold Spectrum Rigidity

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Working title:** *Reflections on Threshold Spectrum Rigidity with Commander Sol*  
**Author:** Alex Malachevsky  
**ORCID:** 0009-0008-6009-3196  
**Status:** theorem checkpoint; first internal audit passed  
**Date:** 2026-08-28

## 1. Motivation

The Support-Cardinality Valuation Wall classifies threshold profiles coarsely by

\[
P_+(\kappa)=\{r:\kappa(r)\ge1\}.
\]

Finite positive support lies on the zero-depth compression side; infinite positive support lies on the residual graph-universality side.

The next question is whether all profiles on the same side collapse to essentially the same first-order theory.

They do not.

The threshold profile is pointwise recoverable from the complete first-order theory. Consequently the amplifying side contains continuum many pairwise distinct complete theories, even when every profile has the same support and takes only the two values \(1\) and \(2\).

This separates two notions which the support-cardinality theorem deliberately compressed:

- **phase type**: finite versus infinite positive support;
- **spectral identity**: the exact numerical threshold attached to every fixed standard prime.

## 2. Structures

For

\[
\kappa:\mathbb P\to\mathbb N_0,
\]

let

\[
\mathcal V_{\Delta,\kappa}
=
\Bigl(
(\mathbb N_{>0},\times,1),
(\mathbb Q,+,0),
U_\Delta,B_\kappa
\Bigr),
\]

where

\[
U_\Delta(p,x)
\iff
\operatorname{Prime}(p)\land x=u_p,
\qquad
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

and

\[
B_\kappa(r,x)
\iff
\operatorname{Prime}(r)\land v_r(x)\ge\kappa(r).
\]

All structures are viewed in the same first-order language; only the interpretation of \(B\) varies with \(\kappa\).

## 3. Every fixed standard prime is parameter-free definable

For a fixed ordinary prime \(\ell\), define

\[
\Theta_\ell(r)
:
\operatorname{Prime}(r)
\land
\exists x\,
\bigl(
\neg B(r,x)
\land
B(r,\ell x)
\bigr),
\]

where \(\ell x\) is the fixed additive scalar term.

Then in every \(\mathcal V_{\Delta,\kappa}\),

\[
\Theta_\ell(r)\iff r=\ell.
\]

If \(r\ne\ell\), multiplication by \(\ell\) is an \(r\)-adic unit and cannot cross the threshold. If \(r=\ell\), choose \(x\) with

\[
v_\ell(x)=\kappa(\ell)-1.
\]

This works also when \(\kappa(\ell)=0\), using valuation \(-1\).

Thus every fixed standard source prime is named without parameters uniformly across the whole threshold-profile family.

## 4. A parameter-free target unit

The bridge labels at \(2\) and \(5\) are

\[
u_2=-\frac{23}{32},
\qquad
u_5=-\frac{1019969}{5^9}.
\]

Hence

\[
32u_2=-23,
\qquad
5^9u_5=-1019969.
\]

The Bezout identity

\[
88693\cdot23-2\cdot1019969=1
\]

gives

\[
-88693(32u_2)+2(5^9u_5)=1.
\]

Since the source primes \(2\) and \(5\) are parameter-free definable by \(\Theta_2\) and \(\Theta_5\), the bridge relation \(U_\Delta\) parameter-free defines \(u_2,u_5\). Fixed additive scalar multiplication then parameter-free defines the target element

\[
1\in\mathbb Q.
\]

### Lemma 4.1. Uniform target-unit definability

There is one parameter-free formula \(\operatorname{One}(z)\), independent of \(\kappa\), such that in every threshold-profile structure

\[
\operatorname{One}(z)\iff z=1.
\]

No numerical transport from a variable source element to the target sort is used; only the two fixed standard primes \(2,5\) and fixed integer scalar terms occur.

## 5. Definable rational probes of arbitrary fixed valuation

Fix a standard prime \(\ell\) and an integer \(t\in\mathbb Z\).

Using the definable target unit \(1\), define a unique rational probe \(q_{\ell,t}\) as follows.

For \(t\ge0\),

\[
q_{\ell,t}=\ell^t.
\]

For \(t=-s<0\), define \(q_{\ell,-s}\) as the unique rational satisfying

\[
\ell^s q_{\ell,-s}=1.
\]

The target sort \((\mathbb Q,+,0)\) is torsion-free and divisible, so the latter element exists uniquely.

Thus \(q_{\ell,t}\) is parameter-free definable for every fixed pair \((\ell,t)\), and

\[
v_\ell(q_{\ell,t})=t.
\]

## 6. Exact pointwise decoding of the threshold profile

For every fixed standard prime \(\ell\) and every \(m\in\mathbb N_0\), define the sentence

\[
\Sigma_{\ell,m}
\]

by

\[
B(\ell,q_{\ell,m})
\land
\neg B(\ell,q_{\ell,m-1}),
\]

where the displayed constants are shorthand for the parameter-free definitions from Sections 3--5.

Because

\[
B_\kappa(\ell,q_{\ell,t})
\iff
t\ge\kappa(\ell),
\]

we obtain

\[
\boxed{
\mathcal V_{\Delta,\kappa}\models\Sigma_{\ell,m}
\iff
\kappa(\ell)=m.
}
\]

### Theorem 6.1. Pointwise Threshold Recovery

For every fixed standard prime \(\ell\), the exact integer \(\kappa(\ell)\) is recoverable from the parameter-free first-order theory of \(\mathcal V_{\Delta,\kappa}\).

Equivalently, the complete theory determines the full threshold profile coordinate by coordinate.

This is a pointwise recovery theorem. It does **not** assert that the binary graph

\[
\{(r,m):\kappa(r)=m\}
\]

is uniformly definable with both \(r\) and \(m\) variable inside the structure.

## 7. Elementary rigidity of the profile

### Theorem 7.1. Threshold Spectrum Rigidity

For threshold profiles

\[
\kappa,\lambda:\mathbb P\to\mathbb N_0,
\]

if

\[
\kappa\ne\lambda,
\]

then

\[
\boxed{
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
\ne
\operatorname{Th}(\mathcal V_{\Delta,\lambda}).
}
\]

### Proof

Choose a standard prime \(\ell\) with

\[
\kappa(\ell)\ne\lambda(\ell).
\]

Let

\[
m=\kappa(\ell).
\]

Then

\[
\mathcal V_{\Delta,\kappa}\models\Sigma_{\ell,m},
\]

while

\[
\mathcal V_{\Delta,\lambda}\not\models\Sigma_{\ell,m}.
\]

Hence the complete theories differ. ∎

The converse is tautological for this fixed standard model family: if \(\kappa=\lambda\), the two structures are identical.

Therefore

\[
\boxed{
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
=
\operatorname{Th}(\mathcal V_{\Delta,\lambda})
\iff
\kappa=\lambda.
}
\]

within the standard threshold-profile family.

## 8. Continuum many theories on the same amplifying side

Let \(A\subseteq\mathbb P\) be arbitrary and define

\[
\kappa_A(r)
=
\begin{cases}
1,&r\in A,\\
2,&r\notin A.
\end{cases}
\]

Then for every \(A\),

\[
P_+(\kappa_A)=\mathbb P.
\]

Hence the Support-Cardinality Valuation Wall gives, for every \(A\),

\[
\exists I_A\quad \operatorname{GIR}(I_A)=\infty,
\]

uniform coding of all finite directed graphs, and

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa_A})
\text{ undecidable}.
\]

But if \(A\ne A'\), then \(\kappa_A\ne\kappa_{A'}\), so Threshold Spectrum Rigidity gives

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa_A})
\ne
\operatorname{Th}(\mathcal V_{\Delta,\kappa_{A'}}).
\]

Since \(\mathbb P\) is countably infinite,

\[
|\mathcal P(\mathbb P)|=2^{\aleph_0}.
\]

### Corollary 8.1. Continuum Spectrum on the Right-Hand Phase

There are

\[
\boxed{2^{\aleph_0}}
\]

pairwise distinct complete first-order theories among threshold-profile structures with

\[
P_+(\kappa)=\mathbb P
\]

and with threshold values restricted to

\[
\{1,2\}.
\]

Every one of these theories is on the same GIR-infinite / finite-graph-universal / undecidable side of the Support-Cardinality Wall.

Thus the right-hand phase is not a single theory or a small finite family of theories. It contains a continuum-sized threshold spectrum.

## 9. Continuum many theories even at fixed support

The preceding corollary already fixes the support to all primes. More generally, let \(S\subseteq\mathbb P\) be any infinite set whose complement may be finite or infinite. Consider profiles satisfying

\[
P_+(\kappa)=S
\]

and, on \(S\), taking values only in \(\{1,2\}\).

If \(S\) is infinite, there are

\[
2^{\aleph_0}
\]

such profiles, hence continuum many pairwise distinct complete theories all sharing the same positive-depth support \(S\).

Therefore support cardinality determines the coarse logical phase, but even the entire support set does not determine the complete theory.

The exact threshold spectrum remains visible.

## 10. A two-scale phase picture

The previous theorem supplied a coarse quotient:

\[
\kappa
\mapsto
\begin{cases}
\text{compression phase},&|P_+(\kappa)|<\infty,\\
\text{amplifying phase},&|P_+(\kappa)|=\infty.
\end{cases}
\]

Threshold Spectrum Rigidity now shows that inside each coarse phase the complete first-order theory still remembers every fixed coordinate of \(\kappa\).

For the amplifying side:

\[
\boxed{
\text{same support-cardinality phase}
\not\Rightarrow
\text{same complete theory}.
}
\]

Indeed, even

\[
P_+(\kappa)=P_+(\lambda)=\mathbb P
\]

and

\[
\kappa(r),\lambda(r)\in\{1,2\}
\]

for every prime \(r\) do not force elementary equivalence.

The phase diagram therefore has two scales:

1. **macroscopic phase invariant:** finiteness versus infinitude of positive-depth support;
2. **microscopic spectral invariant:** the exact pointwise threshold profile.

## 11. What is and is not uniformly definable

The proof relies on fixed standard probes. For each fixed \(\ell\) and fixed \(m\), there is a parameter-free sentence detecting

\[
\kappa(\ell)=m.
\]

This should not be confused with a single formula capable of reading \(\kappa(r)\) uniformly as \(r\) varies.

The language still lacks a known variable numerical transport map from the source sort to the target sort. In particular, no formula of the form

\[
J(r,z)\iff z=r
\]

with \(r\) variable source and \(z\) its target integer value is assumed or proved.

So there is a genuine distinction between:

- **theory-level pointwise recovery**, proved here;
- **internal uniform profile reconstruction**, open.

This distinction is the natural next boundary to investigate.

## 12. Claim boundary

This checkpoint does **not** claim:

- that \(\kappa\) is uniformly definable as a variable source-to-depth function;
- that different profiles are non-isomorphic in every expanded/nonstandard setting beyond the standard family considered here;
- that pairwise elementary inequivalence implies pairwise non-interpretability;
- that all infinite-support theories have different decidability degrees;
- that all profiles on the finite-support side are pairwise non-interdefinable (indeed finite-support profiles are all interdefinable with \(B_0\));
- that arbitrary parameters cannot collapse some of the distinctions;
- ordinary prime order or prime successor definability on the amplifying side.

## 13. First hostile audit

The following failure modes were checked.

1. **Circular naming of 2 and 5:** avoided. \(\Theta_2\) and \(\Theta_5\) use only fixed additive scalar multiplication by 2 and 5, not target constants 2 and 5.
2. **Dependence on \(\kappa(2)\) or \(\kappa(5)\):** none. Fixed-prime definability works at every threshold, including zero.
3. **Target unit uniqueness:** the bridge gives unique rational labels and the displayed fixed linear combination is exactly 1.
4. **Negative valuation probe:** definable by the unique solution to \(\ell^s y=1\) in the torsion-free divisible additive group \(\mathbb Q\).
5. **Uniformity over profiles:** formulas \(\Theta_\ell\), \(\operatorname{One}\), and each fixed probe sentence \(\Sigma_{\ell,m}\) do not depend on the unknown value \(\kappa(\ell)\); the latter merely tests candidate value \(m\).
6. **Variable numerical transport:** not used and not claimed.
7. **Continuum count:** already obtained with profiles \(\kappa_A\in\{1,2\}^{\mathbb P}\), all having support equal to \(\mathbb P\).
8. **Compatibility with the previous wall:** no contradiction. The support-cardinality theorem classifies the GIR/undecidability phase, not complete elementary theory.

## 14. Current verdict

**Theorem checkpoint: PASS after first internal hostile audit.**

The next strike should test the genuinely harder question suggested by Section 11:

> Which relations between two profiles \(\kappa\) and \(\lambda\) make \(B_\lambda\) definable from \(B_\kappa\) by one uniform parameter-free formula?

The known cases are already asymmetric and informative:

- every finite-support profile is parameter-free interdefinable with \(B_0\);
- \(B_1\) is not parameter-free definable from \(B_0\);
- pointwise threshold values are nevertheless recoverable from complete theory.

Thus **theory-level recovery is strictly weaker than uniform internal definability**. The gap between these two notions is now the principal open boundary beyond the Support-Cardinality Wall.