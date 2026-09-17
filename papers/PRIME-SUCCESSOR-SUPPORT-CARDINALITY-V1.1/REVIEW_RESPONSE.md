# Review Response — Support-Cardinality Valuation Wall v1.1

**Reviewer verdict:** ACCEPT WITH MINOR REVISIONS  
**Date addressed:** 2026-08-28

The requested minor revisions have been incorporated without changing the mathematical statement of Theorem 14.1.

## Required revision 1 — Lemma 5.1 meta-constant clarification

Added an explicit statement that, for each exceptional prime \(\ell_i\), the integer

\[
k_i=\kappa(\ell_i)
\]

is a fixed metamathematical constant attached to the fixed profile. Therefore \(\ell_i^{k_i}\) is a fixed ordinary integer and multiplication by it in the additive target sort is represented by one finite repeated-addition term. No variable exponentiation or variable scalar multiplication is introduced.

## Required revision 2 — Why graph coding already suffices

Section 18 now states explicitly that uniform finite directed graph coding plus the effective two-way Trakhtenbrot reduction is already sufficient to prove undecidability of the complete theory. Interpretation of full arithmetic \((\mathbb N_0,+,\times)\) would be strictly stronger and is treated as a separate open problem, not as a hidden premise.

## Required revision 3 — Other modular forms

Section 17 now records the exact conditional extension of the proof mechanism: it applies verbatim, with exponent \(11\) replaced by \(k-1\), to a normalized non-CM newform \(f\) of weight \(k\) with rational coefficients and trivial nebentypus whenever the cyclotomic-kernel adelic image contains \(\operatorname{SL}_2(\mathbb Z_r)\) outside a finite set. The bridge becomes

\[
u_{f,p}=\frac{a_p(f)^2-p^{k-1}}{p^{k-1}}.
\]

No verbatim extension is claimed for CM forms, nontrivial nebentypus, or non-rational coefficient fields.

## Optional open questions incorporated

The manuscript now explicitly records:

1. whether the multiplicative source sort can be replaced by a weaker finite-subset carrier;
2. whether the amplifying side interprets full arithmetic.

The first question has already been attacked in the new branch `research/finite-subset-carrier-wall`; the first-strike theorem proves that multiplication is not needed on the wild side if genuine finite-set memory is supplied.

## QA

Post-review render QA passed. Equation numbering remains synchronized through (68). The revised binaries are 16 pages EN and 17 pages RU.