# RH-SOL-04 · FIREWALL-06 — adversarial constrained-permutation results

Status: completed on both predeclared ranges.
Branch: `agent/rh-sol-04-firewall`.

## Frozen question

FIREWALL-06 asked whether an exact-multiset permutation can move substantially away from the original ordering while remaining inside the high-fidelity loop-index Fourier-magnitude region

`E_spec <= 0.05`.

The search objective was normalized mean absolute displacement `D_abs`. The exact-`log(m)` target score was excluded from proposal acceptance, annealing energy, restart selection, feasibility, and stopping. It was computed only after the adversarial surrogate had been frozen.

Per block:

- `20` independent restarts;
- `20000` transposition proposals per restart;
- exact multiset preservation;
- spectral constraint `E_spec <= 0.05`;
- objective: maximize `D_abs`.

## Range 1: loops 1..20000

### Adversarial feasibility

Range summary:

- mean `E_spec`: `0.04753040662442896`;
- maximum block `E_spec`: `0.04991238484690028`;
- mean moved fraction `D_move`: `0.07350000000000001`;
- mean normalized absolute displacement `D_abs`: `0.024997497497497495`;
- mean normalized RMS displacement `D_rms`: `0.11102963437695709`;
- blocks with a non-identity feasible solution: `20/20`;
- blocks with `D_move >= 0.10`: `0/20`;
- blocks with `D_abs >= 0.02`: `18/20`.

The preregistered flexible-regime criterion is satisfied because

`mean E_spec <= 0.05`

and

`mean D_abs >= 0.02`.

Thus the low-mismatch region is not confined to a trivial identity neighborhood under the adversarial search.

### Post-freeze target score

Primary `m=2..13`:

- observed: `0.04463219422177026`;
- adversarial: `0.04393091811554368`;
- adversarial / observed: `0.984287662337593`;
- score reduction: `1.5712337662406983%`.

Sensitivity `m=2..11`:

- observed: `0.05027641438222484`;
- adversarial: `0.049481430955543394`;
- adversarial / observed: `0.9841877461539399`;
- score reduction: `1.581225384606011%`.

The exact-target score therefore remains essentially intact under the adversarial joint-constraint surrogate.

## Range 2: loops 20001..40000

### Adversarial feasibility

Range summary:

- mean `E_spec`: `0.04701093114715471`;
- maximum block `E_spec`: `0.049828513151975146`;
- mean moved fraction `D_move`: `0.08230000000000001`;
- mean normalized absolute displacement `D_abs`: `0.029193093093093092`;
- mean normalized RMS displacement `D_rms`: `0.12203405459297192`;
- blocks with a non-identity feasible solution: `20/20`;
- blocks with `D_move >= 0.10`: `3/20`;
- blocks with `D_abs >= 0.02`: `19/20`.

Again the preregistered flexible-regime criterion is satisfied by

`mean E_spec <= 0.05`

and

`mean D_abs >= 0.02`.

### Post-freeze target score

Primary `m=2..13`:

- observed: `0.034228925875265076`;
- adversarial: `0.03360467469940894`;
- adversarial / observed: `0.9817624666888177`;
- score reduction: `1.8237533311182275%`.

Sensitivity `m=2..11`:

- observed: `0.03843732058522577`;
- adversarial: `0.03773732669433139`;
- adversarial / observed: `0.9817886918173107`;
- score reduction: `1.8211308182689345%`.

The same qualitative result therefore replicates on the independent higher-loop range.

## Preregistered verdict

FIREWALL-06 lands in the **flexible joint-constraint regime** on both ranges.

The adversarial optimizer constructs exact-multiset surrogates that are nontrivially displaced from the original ordering while satisfying `E_spec <= 0.05` at every selected block and on average. After those surrogates are frozen, the exact-`log(m)` target score remains within about `1.6%` of observed on loops `1..20000` and within about `1.8%` on loops `20001..40000`.

This directly overturns the strong rigidity reading suggested by FIREWALL-05. The zero counts from random partial permutations reflected the weakness of that random family in reaching the constrained low-mismatch region, not evidence that the region itself was empty.

## Scientific interpretation

The strongest defensible conclusion is now:

> For the present scalar filled-area observable and target-only exact-`log(m)` score, preserving the exact blockwise area multiset together with the loop-index Fourier magnitude spectrum to within about `5%` is sufficient to preserve almost all of the target score, even after a nontrivial adversarial rearrangement of the area ordering.

Equivalently, the present target statistic is **not strongly sensitive to exact pointwise area-to-zero-time assignment once these joint invariants are preserved**.

This materially narrows the earlier FIREWALL-01/02 interpretation. Circular offsets, block reassignment, pure phase randomization, and ordinary IAAFT controls destroy or distort the relevant joint spectral structure and strongly reduce the target score. FIREWALL-06 shows that the surviving sufficient feature is much closer to the combination

`exact area-value distribution + near-preserved loop-index Fourier magnitude spectrum`

than to the exact original pointwise ordering itself.

## Relation to REALZERO

REALZERO remains valid: the comb sits at the declared `log(m)` frequencies when actual zero-pair midpoint times are used directly.

FIREWALL-06 changes the interpretation of **where the information resides**. The result does not require the exact original area ordering at every loop. A nontrivial equivalence class of reordered area sequences can retain the target alignment provided the second-order loop-index spectrum is kept sufficiently close.

Because zero spacing is locally close to regular over 1000-loop blocks, preservation of the loop-index spectrum can naturally preserve substantial actual-time sinusoidal response. FIREWALL-06 therefore identifies a concrete structural mechanism that must be accounted for before assigning stronger arithmetic specificity to the area-time pairing.

## Consequence for FIREWALL

The central FIREWALL question has reached a scientifically informative stopping point:

- naive preserved-structure controls fail strongly;
- exact phase destruction fails strongly;
- approximate joint-preservation IAAFT controls fail statistically but do not reach sufficient fidelity;
- direct adversarial joint-preservation succeeds in reaching the declared fidelity region;
- once it does, the exact-target score largely survives.

Therefore the strongest proposed interpretation — that the exact geometry-to-zero-time assignment itself carries indispensable information beyond preserved scalar spectral structure — is **not supported** by FIREWALL-06.

The correct forward direction is no longer to add more assignment surrogates to the same scalar area statistic. It is to move to the next programme layer and ask what survives under controls specifically designed to remove or quotient out this identified second-order equivalence class.

## Guardrails

1. `E_spec <= 0.05` is near-preservation, not exact preservation of the loop-index Fourier magnitudes.
2. Mean displacement is nontrivial but still moderate; FIREWALL-06 does not show arbitrary reordering freedom.
3. The adversarial search is computational and does not characterize the full feasible set.
4. No arithmetic causation theorem or Riemann-Hypothesis claim follows from this result.
