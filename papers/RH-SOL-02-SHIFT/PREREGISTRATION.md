# RH-SOL-02 · SHIFT — preregistration

## Primary question

Does the Dirichlet-frequency structure seen in RH-SOL-01 persist under arbitrary translations of the lattice, or is the effect specific to the unshifted grid Z^2?

## Primary observable

For loop domain D_n and delta=(dx,dy) in [0,1)^2,

`I_delta(n,a,b) = 1_{D_n}((a,b)+delta)`

and the shift count

`C_n(delta) = sum_{k in Z^2} 1_{D_n}(k+delta)`.

## Interior convention

Primary: non-zero winding number. Boundary points are excluded with an explicit tolerance. Sensitivity control: even-odd fill rule.

The two conventions must be reported separately whenever they disagree.

## Translation grid

Primary finite approximation: q x q midpoint grid

`delta_ij = ((i+1/2)/q, (j+1/2)/q)`, 0<=i,j<q.

Primary q values: 8, 16, 32. The q=16 result is the nominal reference; q=8 and q=32 are resolution controls.

Midpoints are used to avoid systematic hits on the original integer-grid boundaries at delta=(0,0).

## Hypotheses

### H1 — translation-average identity

For each sufficiently resolved loop,

`mean_delta C_n(delta) -> Area(D_n)`

as the translation grid is refined.

This is a geometric calibration, not a zeta-specific discovery claim.

### H2 — shift persistence of Dirichlet structure

After applying the same temporal centering and spectral scoring rules across shifts, the aggregate Dirichlet comb at `log m` should remain detectable for a substantial subset of lattice translations.

Failure mode: the comb is concentrated near delta=(0,0) or a small exceptional set of translations.

### H3 — translation-averaged persistence

A spectrum formed after averaging over delta should retain predeclared Dirichlet-frequency structure better than geometry-matched null controls.

Failure mode: translation averaging removes the comb or produces a score indistinguishable from nulls.

### H4 — fill-rule robustness

The main qualitative conclusions should not depend on choosing winding vs even-odd fill for the majority of loops. Loops where the rules disagree must be counted and characterized.

## Controls

1. Translation resolution: q=8,16,32.
2. Fill rule: winding vs even-odd.
3. Boundary tolerance sensitivity.
4. Loop-order shuffle.
5. Local loop-order shuffle preserving height blocks.
6. Geometry-matched random closed curves.
7. Phase-randomized zeta-like surrogates when upstream loop generation is available.

## Calibration vs confirmation

Loops 1–10000 are a calibration/reproduction set because RH-SOL-01 was developed on that range.

After freezing the pipeline, loops 10001–20000 are the planned first independent confirmation range. Any change to metrics after viewing holdout results must create a new exploratory branch/version.

## Reporting rules

- Report positive and negative results.
- Do not use the phrase "new frequency" for lines explained by `log n`, prime powers, nonlinear mixing, or sampling aliases.
- Report all tested q values and both fill rules.
- Record exact code commit, zero source, loop-generation tolerance, and dataset checksum.
- Surrogate p-values are diagnostic unless the full null family and multiplicity correction are fixed in advance.
