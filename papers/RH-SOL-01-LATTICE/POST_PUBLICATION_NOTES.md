# Post-publication notes

RH-SOL-01 v0.1.1 is frozen at Zenodo DOI `10.5281/zenodo.22060296`.

This file records later methodological clarification without rewriting the published article.

## Review-driven questions retained for the programme

A post-publication review identified several issues that should be answered in later work:

1. define loop interior rigorously for possible self-intersections;
2. state boundary-point handling explicitly;
3. package the full upstream pipeline from zero ordinates to lattice incidence;
4. repeat the spectral test using actual zero ordinates rather than only a smooth zero-density warp;
5. add shifted-lattice sensitivity tests;
6. add geometry-matched, phase-randomized and order-randomized null models;
7. compare the structured frequency dictionary with random dictionaries of equal size;
8. test an independent height range.

These points do not invalidate the published computational observation by themselves; they determine how strongly it can be interpreted and what must be tested next.

## Routing

- Interior convention + lattice translation -> **RH-SOL-02 · SHIFT**
- Actual `gamma_n` timing -> **RH-SOL-03 · REALZERO**
- Geometry/order/phase nulls -> **RH-SOL-04 · FIREWALL**
- Poisson structure exposed by translated lattices -> **RH-SOL-05 · POISSON**

## Claim discipline

The published paper remains an exploratory computational note about persistence of Dirichlet-frequency structure after severe binary geometric quantization. No later programme document should retroactively describe RH-SOL-01 as a theorem or as evidence proving RH.
