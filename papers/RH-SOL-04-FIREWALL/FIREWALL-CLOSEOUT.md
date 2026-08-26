# RH-SOL-04 · FIREWALL — research closeout

Status: research phase complete; manuscript synthesis pending.
Branch: `agent/rh-sol-04-firewall`.

## Core question

RH-SOL-04 asked whether the exact `log(m)` alignment of the winding-filled zeta-loop area is tied to the exact geometry-to-zero-time assignment, or whether preserved structural features are sufficient to reproduce the target score.

The programme deliberately escalated from simple assignment surrogates to stronger joint-invariant controls.

## Stage summary

### FIREWALL-01 — within-block circular offsets

Random non-zero circular rotations of each 1000-loop area block, with actual zero times fixed, strongly reduced the exact-target score on both ranges. All primary/sensitivity tests passed at the finite-surrogate floor.

### FIREWALL-02 — whole-block reassignment

Complete area trajectories were reassigned among fixed actual-time blocks. The exact-target score again collapsed strongly on both ranges.

### FIREWALL-03 — phase randomization

Blockwise loop-index Fourier magnitudes were preserved exactly while Fourier phases were randomized. The target score again collapsed strongly. Therefore the power spectrum alone, without the original phase organization, was insufficient under this surrogate family.

### FIREWALL-04 — IAAFT

The exact blockwise area-value multiset was preserved while Fourier magnitudes were matched approximately. The target score remained strongly separated from the surrogate family, but spectral mismatch was about 17%, preventing a strong joint-invariant interpretation.

### FIREWALL-04B — convergence stress

Increasing IAAFT effort to four independent starts and 2000 iterations reduced mismatch only to about 14.8% on loops 1..20000 and 12.9% on loops 20001..40000. The statistical firewall still passed, but the preregistered 5% fidelity gate failed completely.

### FIREWALL-05 — permutation-rigidity map

Random controlled partial permutations showed a strong empirical relation between ordering displacement, Fourier-magnitude mismatch, and exact-target score. Among 5400 sampled realizations across both ranges, none simultaneously achieved `E_spec <= 0.05` and substantial displacement.

This suggested empirical rigidity, but random sampling could not determine whether the low-mismatch far-from-identity region was genuinely empty.

### FIREWALL-06 — adversarial constrained permutation

The final targeted test explicitly maximized ordering displacement under the hard spectral-fidelity constraint `E_spec <= 0.05`, while preserving the exact area multiset and excluding the exact-`log(m)` score from the optimizer.

The optimizer found feasible non-identity solutions in every block on both ranges.

Calibration range 1..20000:

- mean `E_spec = 0.04753040662442896`;
- mean `D_abs = 0.024997497497497495`;
- non-identity feasible blocks: `20/20`;
- target-score retention, m=2..13: `98.4288%`;
- target-score reduction: about `1.57%`.

Holdout range 20001..40000:

- mean `E_spec = 0.04701093114715471`;
- mean `D_abs = 0.029193093093093092`;
- non-identity feasible blocks: `20/20`;
- target-score retention, m=2..13: `98.1762%`;
- target-score reduction: about `1.82%`.

The preregistered flexible joint-constraint regime is therefore realized on both disjoint ranges.

## Final FIREWALL conclusion

The strongest initial interpretation does not survive the adversarial joint-invariant test.

It is **not supported** that the exact pointwise geometry-to-zero-time assignment is indispensable for the present scalar filled-area exact-`log(m)` target score.

Instead, the experiments identify a broader equivalence class:

> exact preservation of the blockwise area-value multiset together with preservation of the loop-index Fourier magnitude spectrum to roughly 5% relative error is sufficient to retain almost all of the exact-target score under a nontrivial adversarial reordering.

Thus the present target statistic is much more tightly coupled to a second-order spectral/distributional equivalence class than to the exact original pointwise ordering.

## What remains valid

1. REALZERO remains valid: the Dirichlet comb is aligned with the declared `log(m)` frequencies under direct use of actual zero-pair midpoint times.
2. The simple FIREWALL controls remain valid as statements about those surrogate families: circular offsets, whole-block reassignment, and independent phase randomization destroy the target score.
3. FIREWALL-06 explains why those earlier controls were too destructive: they did not preserve the joint invariant structure now identified.
4. The signal therefore survives substantial pointwise rearrangement whenever this joint spectral structure is retained.

## What FIREWALL rules out

The programme should no longer describe the scalar area signal as evidence that each individual zeta-loop area must be paired with its original zero-time location in order to produce the `log(m)` comb.

It should also not present the FIREWALL-05 random-map rigidity as a structural uniqueness result. FIREWALL-06 directly demonstrates that the constrained low-mismatch region contains nontrivial displaced solutions.

## Forward implication

The next programme layers should quotient out or explicitly control the identified equivalence class rather than continue generating more assignment surrogates for the same scalar area statistic.

Two directions are now especially natural:

1. **RH-SOL-05 · POISSON**: analyze the shifted-lattice observable in terms of actual Fourier coefficients of loop interiors and separate zero-mode/second-order contributions from higher geometric information.
2. **RH-SOL-06 · NYQUIST**: formalize how near-uniform zero sampling, loop-index Fourier structure, and actual-time `log(m)` response interact.

These are now better motivated because FIREWALL has identified the specific preserved structure that future tests must factor out.

## Research status

RH-SOL-04 FIREWALL is complete as an experimental research phase.

Manuscript synthesis remains pending.

No arithmetic causation theorem and no Riemann-Hypothesis claim follows from this closeout.
