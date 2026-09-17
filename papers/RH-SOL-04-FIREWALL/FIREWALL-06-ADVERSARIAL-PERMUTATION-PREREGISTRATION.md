# RH-SOL-04 · FIREWALL-06 — adversarial constrained-permutation search preregistration

Status: preregistered before adversarial-search inspection.
Branch: `agent/rh-sol-04-firewall`.

## Motivation

FIREWALL-05 mapped random controlled exact-multiset permutations and found a strong empirical rigidity pattern: among 5400 sampled realizations across two ranges, none simultaneously achieved mean Fourier-magnitude mismatch `E_spec <= 0.05` and substantial ordering displacement.

Random sampling cannot establish that the far, low-mismatch region is empty. FIREWALL-06 therefore replaces random sampling by an explicit adversarial search.

## Core question

> Can one construct an exact-multiset permutation that is substantially displaced from the original ordering while keeping the original blockwise loop-index Fourier magnitude spectrum within a fixed high-fidelity tolerance?

The arithmetic `log(m)` target score is **not** used in the optimization objective or feasibility constraints.

## Data and blocks

Use exactly the same winding-filled-area sequences and actual zero-pair midpoint times as FIREWALL-01..05.

Analyze independently:

1. loops `1..20000`;
2. loops `20001..40000`.

Block size: `1000`.

## Per-block optimization object

For a block with original area vector `y` and a permutation `pi`, define:

- exact-multiset surrogate `y_pi[i] = y[pi(i)]`;
- normalized spectral mismatch

`E_spec(pi) = || |FFT(y_pi-mean)| - |FFT(y-mean)| ||_2 / || |FFT(y-mean)| ||_2`;

- moved fraction

`D_move(pi) = mean_i [pi(i) != i]`;

- normalized mean absolute displacement

`D_abs(pi) = mean_i |pi(i)-i| / 999`;

- normalized RMS displacement

`D_rms(pi) = sqrt(mean_i (pi(i)-i)^2) / 999`.

## Primary constraint and objective

Primary spectral-fidelity constraint:

`E_spec <= 0.05`.

Primary adversarial objective:

maximize `D_abs` subject to the exact-multiset condition and `E_spec <= 0.05`.

Secondary report-only objectives:

- `D_move`;
- `D_rms`.

The `log(m)` score must never enter proposal acceptance, objective weighting, restart selection, or stopping.

## Search algorithm

Use a permutation-state local search with simulated-annealing style exploration under a lexicographic feasibility objective.

For each block and each independent restart:

1. initialize from the identity permutation;
2. proposals are random transpositions of two indices;
3. compute the proposed `E_spec` and `D_abs` exactly;
4. rank states lexicographically by:
   - first, lower violation `max(E_spec-0.05, 0)`;
   - among equally feasible states, larger `D_abs`;
5. accept strict improvements always;
6. allow occasional non-improving moves according to a frozen temperature schedule to escape local traps;
7. retain the best feasible state encountered during the full trajectory;
8. never use target score during the search.

Frozen schedule per restart:

- `20000` transposition proposals;
- initial temperature `T0 = 0.02` in lexicographic energy units;
- geometric decay to `Tend = 1e-5`;
- energy for annealing only:

`J = 100 * max(E_spec-0.05,0)^2 - D_abs`.

The final reported state for each restart is selected lexicographically by feasibility then `D_abs`, not by `J` and not by target score.

## Restarts and seeds

Per block:

- `20` independent restarts.

Seeds:

- calibration range base seed `20260904`;
- holdout range base seed `20260905`;
- deterministic block/restart offsets allowed.

## Range-level construction

For each block independently, retain the feasible permutation with largest `D_abs` among the 20 restarts.

If no non-identity feasible state is found in a block, retain identity and record that fact explicitly.

The resulting 20-block adversarial surrogate defines one range-level sequence.

## Required outputs

Per block report:

- best `E_spec`;
- `D_move`;
- `D_abs`;
- `D_rms`;
- whether a non-identity feasible state was found;
- number of feasible non-identity states encountered;
- restart index of selected state.

Range-level report:

- mean and maximum `E_spec`;
- mean `D_move`, `D_abs`, `D_rms`;
- number of blocks with non-identity feasible solutions;
- number of blocks with `D_move >= 0.10`;
- number of blocks with `D_abs >= 0.02`.

Only after the adversarial surrogate is frozen, compute the unchanged FIREWALL exact-target scores for:

- primary `m=2..13`;
- sensitivity `m=2..11`.

## Predeclared interpretation

### Flexible joint-constraint regime

If the search finds a range-level surrogate with:

- mean `E_spec <= 0.05`;
- mean `D_move >= 0.10` or mean `D_abs >= 0.02`,

then the low-mismatch region is demonstrably not confined to trivial neighborhoods of the original order. The resulting surrogate becomes a strong joint-invariant firewall control.

If its `log(m)` score collapses relative to observed, this supports information beyond exact multiset plus near-exact second-order spectrum.

If its `log(m)` score remains high, the present target signal is likely tightly tied to those joint invariants.

### Rigid joint-constraint regime

If repeated independent searches cannot produce substantially displaced feasible permutations and most blocks terminate near identity, this materially strengthens the empirical rigidity interpretation suggested by FIREWALL-05.

It remains computational evidence, not a proof of permutation uniqueness.

## Guardrails

1. The search optimizes only order displacement under spectral fidelity; target score is completely excluded until after construction.
2. Search failure is not a mathematical impossibility theorem.
3. Search success does not imply uniqueness of the found surrogate.
4. Results from both ranges must be reported.
5. No Riemann-Hypothesis claim follows from any outcome.
