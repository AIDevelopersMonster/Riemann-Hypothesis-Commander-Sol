# RH-SOL-05 · POISSON-01B — q-stability audit preregistration

Status: preregistered after POISSON-01 compact results and before inspection of exact stable-vector identities.
Branch: `agent/rh-sol-05-poisson`.

## Motivation

POISSON-01 verified the zero-mode/area and Parseval identities and found reproducible temporal exact-target structure in nonzero spatial-energy observables after blockwise linear removal of area.

However, the compact POISSON-01 output reported only the number of q-stable individual modes while shell energies were computed from all q32 coefficients. The original preregistration requires q-stability before promoting a discrete low shell to a resolved continuous-spatial interpretation.

POISSON-01B closes that gap without changing the frozen q-stability rule and without selecting modes using temporal target scores.

## Data

Use exactly the same existing SHIFT tensors as POISSON-01:

- calibration loops `1..10000`;
- holdout loops `10001..20000`;
- winding fill;
- q=`16,32` primary for stability;
- q=`8` report-only secondary diagnostic.

## Frozen spatial mode universe

Consider all nonzero integer vectors

`ell=(a,b)` with `max(|a|,|b|)<=3`.

For every vector compute the same frozen power discrepancy

`R_16_32(ell) = median_n |P16(n,ell)-P32(n,ell)| / (P32(n,ell)+1e-15)`.

A vector is q-stable iff

`R_16_32 <= 0.10`.

This rule is unchanged from POISSON-01.

## Independent-range sets

Let

- `S_cal` = q-stable vectors on loops `1..10000`;
- `S_hold` = q-stable vectors on loops `10001..20000`.

Define the frozen robust set

`S_intersection = S_cal intersection S_hold`.

The intersection is determined only by q16/q32 spatial agreement. Temporal target scores play no role in selection.

## Shell-completeness audit

For shells

- `r^2=1`: `(±1,0),(0,±1)`;
- `r^2=2`: `(±1,±1)`;
- `r^2=4`: `(±2,0),(0,±2)`;

report for calibration, holdout, and the intersection:

- number of shell vectors stable;
- whether the entire shell is stable;
- exact vector list.

A shell may be called resolved only if all of its vectors belong to `S_intersection`.

## Stable-subset energies

Using q32 coefficients define per-loop

`E_stable32 = sum_{ell in S_intersection} |F32(ell)|^2`.

Using the same vector set define

`E_stable16 = sum_{ell in S_intersection} |F16(ell)|^2`.

Also define shell-specific stable energies using only vectors from each declared shell that lie in `S_intersection`. Partial-shell quantities must be labeled partial and must not be called resolved-shell energies.

## Cross-resolution temporal replication

Score `E_stable16` and `E_stable32` using the unchanged FIREWALL target-only statistic:

- actual zero-pair midpoint time;
- 1000-loop blocks;
- linear detrending in time;
- exact `omega=log(m)` targets;
- primary `m=2..13`;
- sensitivity `m=2..11`.

The same is done after blockwise linear residualization against area.

No threshold on temporal score is used for mode selection.

## Required outputs

For each range report:

1. full `R_16_32` table for all candidate vectors;
2. `S_cal` or `S_hold`;
3. shell-completeness table;
4. stable-intersection energy summaries;
5. q16 vs q32 correlation for stable-intersection energy;
6. q16 vs q32 relative discrepancy for stable-intersection energy;
7. raw target scores for q16 and q32 stable-intersection energies;
8. area correlations;
9. area-residualized target scores.

Also report the exact `S_intersection` once globally.

## Interpretation

### Resolved low-shell outcome

If at least one full low shell belongs to `S_intersection` and its stable-shell area-residualized target score remains reproducibly positive on both ranges, POISSON-01 supports a genuine resolved nonzero-spatial layer beyond area.

### Stable-subset but incomplete-shell outcome

If `S_intersection` is nonempty but no full declared shell is stable, the data support resolved individual low modes or a stable subset, but not rotational shell localization. The next phase-sensitive stage should work vector-by-vector rather than through full shell energies.

### Collapse outcome

If stable-intersection energy residualized against area loses the temporal target structure, the stronger POISSON-01 effect was driven mainly by unresolved or aliased components.

## Guardrails

1. Temporal scores cannot influence the stable-vector set.
2. A partial shell is not a resolved shell.
3. q16/q32 agreement is empirical discretization stability, not proof of exact continuous Fourier recovery.
4. No significance p-value is introduced in this audit.
5. No Riemann-Hypothesis claim follows from any outcome.
