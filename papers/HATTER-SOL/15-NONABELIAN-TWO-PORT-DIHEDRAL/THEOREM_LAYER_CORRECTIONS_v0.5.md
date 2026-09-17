# HATTER-SOL-15 · Publication-canonical theorem layer corrections v0.5

**Date:** 15 September 2026  
**Status:** normative publication note for the HATTER-SOL-15 release candidate.  
**Applies to:** historical exploratory theorem layers that contain broader or stronger wording than the audited publication theorem.

The final publication candidate is governed by the hostile-audited universal-dominance layer and the v0.5 manuscript. If an older theorem-layer note conflicts with the statements below, this file and the v0.5 release manuscript are the canonical statements.

## 1. Mahler harmonic coefficient decay

The exploratory file `MAHLER_DIRICHLET_GAUSS_BRIDGE_AND_EVENTUAL_FULL_TOMOGRAPHY.md` used wording asserting exponential decay of the additive Mahler coefficients too broadly.

Publication-safe statement:

- in the release range `mu >= 4`, the harmonic expansion is absolutely convergent;
- for each fixed `mu > 4`, the coefficients decay exponentially in the harmonic index;
- at the boundary `mu = 4`, the proof uses absolute/uniform convergence for each fixed primitive channel obtained from the strict positive determinant gap, and does **not** require an exponential boundary-decay claim;
- no publication claim is made here for the interval `2 < mu < 4`.

This correction does not affect the proof of universal first-harmonic dominance on `mu >= 4`.

## 2. Analyticity in the spectral parameter

The exploratory file `GENERIC_FULL_MAHLER_TOMOGRAPHY_AND_EXCEPTIONAL_PARAMETERS.md` stated real-analyticity on `mu > 2`. That domain is not used in the final theorem and is broader than the audited release argument justifies without a separate zero-set analysis of the torus determinant.

Publication-safe statement:

- for every fixed odd prime and nontrivial even character, the primitive Mahler character response is real-analytic on `(4, infinity)`;
- the endpoint `mu = 4` is handled separately: for every fixed primitive angle `0 < alpha < pi`,

  `A_4(t+alpha) A_4(t-alpha) > 4`

  for all `t`, so compactness yields a channel-dependent `rho_alpha < 1` controlling the logarithmic expansion uniformly on the torus;
- no generic-exceptional-set theorem on `(2,4)` is part of the publication claims.

## 3. The historical `p=43,q=8` certificate obstruction

The exploratory automatic-certificate layer must not be read as proving an intrinsic impossibility theorem for the `p=43,q=8` mode.

Canonical interpretation:

- the automatic exact engine failed to close that channel within the tested order-Abel and single-phase shifted moment-Abel certificate templates;
- this was a **proof-template obstruction**, not a zero of the Mahler response and not a failure of tomography;
- the later universal theorem

  `B_{mu,1} > sum_{n>=2} B_{mu,n}` for every `mu >= 4`

  supersedes the prime-by-prime frontier and proves the `p=43,q=8` character mode nonzero together with every other odd-prime mode.

No claim of exhaustive impossibility of all phases, all shifts, or all conceivable certificate templates is part of the release.

## 4. Gauss-sum convention

The v0.5 release fixes the convention

`tau(conj(chi)) = sum_{k=1}^{p-1} conj(chi(k)) exp(2 pi i k/p)`

and the unnormalised quotient transform

`hat f_mu(chi) = sum_[k] f_mu([k]) conj(chi(k))`.

With these conventions,

`hat f_mu(chi) = -(1/2) tau(conj(chi)) chi(2) sum_{p not dividing n} B_{mu,n} chi(n)`.

The factor `1/2`, conjugations, and Gram eigenvalue `Lambda_chi = |hat f_mu(chi)|^2` are therefore fixed and not convention-free shorthand.

## 5. Boundary monotonicity

The v0.5 manuscript strengthens the presentation of the autocorrelation lemma by assuming explicitly `f'(u)<0` on `(0,pi)` and splitting the circular-distance comparison into the two cases `u+delta <= pi` and `u+delta > pi`.

At `mu=4`, the primitive determinant has a strict channel-dependent positive gap, so the logarithmic series converges absolutely and uniformly for every fixed primitive channel. Strict primitive Mahler separation at the boundary therefore does not rely on unjustified termwise differentiation.

## 6. Release hierarchy

Historical files such as `MANUSCRIPT_EN_v0.1.md`, `MANUSCRIPT_RU_v0.1.md`, prime-by-prime certificate notes, and earlier release-assembly notes remain in the repository as research history.

For publication claims, use the following hierarchy:

1. hostile-audited universal theorem layer;
2. this correction note;
3. v0.5 final release manuscript and release audit;
4. exact audited certificate and independent execution transcript.

This note is intended to prevent stale exploratory wording from being mistaken for the final theorem statement.