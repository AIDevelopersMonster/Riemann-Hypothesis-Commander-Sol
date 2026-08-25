# RH-SOL-04 · FIREWALL-03 — phase-randomized surrogate results

Status: completed on both predeclared ranges.
Branch: `agent/rh-sol-04-firewall`.

## Surrogate definition

Within each 1000-loop block, the area sequence is mean-centered, transformed by the loop-index rFFT, and reconstructed with:

- the exact original rFFT magnitudes;
- independently randomized phases at all non-DC, non-Nyquist frequencies;
- a random sign at the Nyquist component when present;
- the original block mean restored afterward.

Thus the surrogate preserves the complete blockwise loop-index Fourier magnitude spectrum of the original area sequence, while destroying the original Fourier-phase organization and pointwise area sequence.

The frozen target-only FIREWALL score is then applied identically to observed and surrogate sequences against the actual zero-pair midpoint times.

Important technical precision: exact FFT-magnitude preservation applies to the original blockwise area sequence before the later actual-time linear detrending used by the target score.

Surrogate count: `B=5000` per range.

## Range 1: loops 1..20000

### Primary m=2..13

- observed: `0.04463219422177026`;
- null median: `0.015205002269165279`;
- null q95: `0.01608246359991711`;
- null q99: `0.01650421412186971`;
- null maximum: `0.017123358842466498`;
- empirical p-value: `0.0001999600079984003`.

Observed is about `2.70 x` the null q99 and about `2.61 x` the largest generated surrogate.

### Sensitivity m=2..11

- observed: `0.05027641438222484`;
- null median: `0.017132328887051504`;
- null q95: `0.01817637016062504`;
- null q99: `0.01868515998066936`;
- null maximum: `0.019295964549091063`;
- empirical p-value: `0.0001999600079984003`.

The predeclared sensitivity gives the same conclusion.

## Range 2: loops 20001..40000

### Primary m=2..13

- observed: `0.034228925875265076`;
- null median: `0.021308737383205666`;
- null q95: `0.02203779370031406`;
- null q99: `0.02235777790009856`;
- null maximum: `0.02307650288554061`;
- empirical p-value: `0.0001999600079984003`.

Observed is about `1.53 x` the null q99 and about `1.48 x` the largest generated surrogate.

### Sensitivity m=2..11

- observed: `0.03843732058522577`;
- null median: `0.023702828175850878`;
- null q95: `0.02458859075895677`;
- null q99: `0.024940423780241472`;
- null maximum: `0.025653415383020517`;
- empirical p-value: `0.0001999600079984003`.

Again the sensitivity reproduces the primary conclusion.

## Verdict

FIREWALL-03 passes on both disjoint ranges and on both target dictionaries.

In all four comparisons:

- observed exceeds surrogate q99;
- no generated surrogate reaches observed;
- empirical p-value is at the finite-surrogate floor `1/(5000+1)`.

Therefore preserving the complete blockwise loop-index power spectrum of the area sequence is not sufficient to reproduce the observed exact-`log(m)` target alignment after the original phase organization is destroyed.

## Interpretation

Combined with FIREWALL-01 and FIREWALL-02, the result narrows the surviving information:

- the marginal area distribution alone is insufficient;
- cyclic shifts preserving a common phase relation are insufficient;
- unordered reassignment of complete geometry blocks is insufficient;
- the complete blockwise second-order loop-index spectrum alone is insufficient.

The surviving signal therefore depends on phase organization and/or higher-order/nonlinear structure tied to the correct area-to-zero-time correspondence.

## Height-dependent nuance

As in FIREWALL-01, separation narrows at higher loops. For the primary dictionary, observed/q99 decreases from about `2.70` on loops 1..20000 to about `1.53` on loops 20001..40000.

The firewall remains cleanly passed at the tested surrogate resolution, but this narrowing is retained as a real descriptive feature. No rate law is inferred from two ranges.

## Implementation audit

After the run, `scripts/firewall_phase_surrogates.py` was reread. The implementation:

- preserves the original block mean;
- preserves all blockwise loop-index rFFT magnitudes;
- independently randomizes phases;
- treats the Nyquist coefficient with a random sign for an even block length;
- applies the same frozen target-only score to observed and surrogates;
- performs no frequency retargeting or post-view shift optimization.

No implementation defect requiring reinterpretation was identified.

## Next firewall

Pure phase randomization does not preserve the empirical amplitude distribution pointwise. The next stronger surrogate is therefore an IAAFT-style control that preserves the exact sorted area values in each block while also matching the original blockwise Fourier magnitude spectrum as closely as the frozen iteration scheme permits.

This will test whether the combination of marginal distribution plus second-order spectrum is sufficient without the original phase/higher-order organization.

## Guardrails

1. Failure of phase-randomized surrogates does not prove arithmetic causation.
2. The preserved spectrum is the loop-index spectrum of the area sequence, not an actual-time Lomb-Scargle spectrum.
3. Higher-order statistics are not preserved by this surrogate family.
4. The next IAAFT stage is required before claiming that distribution-plus-spectrum controls have been exhausted.
5. No Riemann-Hypothesis claim follows from this result.
