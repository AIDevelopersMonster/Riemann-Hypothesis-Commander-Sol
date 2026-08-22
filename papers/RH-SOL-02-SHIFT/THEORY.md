# RH-SOL-02 · SHIFT — theory notes

## 1. Shifted lattice count

For a bounded measurable domain D in R^2 and translation delta in [0,1)^2, define

`C_D(delta) = sum_{k in Z^2} 1_D(k + delta)`.

This counts points of the translated unit lattice lying in D.

## 2. Translation-average identity

The average count over one fundamental cell equals the area of D:

`integral_[0,1)^2 C_D(delta) d delta = Area(D)`.

Proof sketch:

`integral_F sum_k 1_D(k+delta) ddelta`

interchanges sum and integral by non-negativity, and the translated cells `k+F` tile R^2. Therefore the expression equals

`integral_R^2 1_D(x) dx = Area(D)`.

This identity provides a theorem-level geometric calibration for the numerical shifted-lattice pipeline.

## 3. Poisson representation

Formally, and rigorously under standard regularity/distributional hypotheses,

`C_D(delta) = sum_{ell in Z^2} hat(1_D)(ell) exp(2*pi*i*ell·delta)`.

The zero mode is

`hat(1_D)(0) = Area(D)`.

Thus varying delta exposes the spatial Fourier coefficients of the domain indicator rather than merely perturbing the original integer grid.

## 4. Translation variance

Using Parseval on the translation torus, one obtains the structural relation

`Var_delta[C_D] = sum_{ell != 0} |hat(1_D)(ell)|^2`

whenever the required square-integrability/normalization conventions are satisfied.

For RH-SOL-02 this gives a geometric quantity that can be tracked across loop index n before any temporal Dirichlet-frequency analysis.

## 5. Why SHIFT is a stronger control than one fixed lattice

RH-SOL-01 observed arithmetic spectral structure after sampling one fixed lattice. A fixed placement can accidentally emphasize geometry aligned with the coordinate grid. SHIFT asks whether the signal is stable over the translation torus.

Three qualitatively distinct outcomes are possible:

1. **Persistent:** the Dirichlet comb survives across most translations and/or after translation averaging.
2. **Localized:** the signal survives only for a small set of translations; this suggests lattice-placement sensitivity.
3. **Destroyed:** the comb disappears under generic shifts; this strongly weakens the interpretation that arithmetic information robustly survives geometric quantization.

All three outcomes are scientifically useful.

## 6. Interior conventions

For self-intersecting closed curves, "interior" is not unique. RH-SOL-02 therefore fixes non-zero winding number as the primary convention and uses even-odd filling as a sensitivity control. Boundary points are excluded.

No theorem or numerical result may silently mix these conventions.
