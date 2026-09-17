# HATTER-SOL · WORLD RESPONSE FIELD PROGRAM

**Status:** programme-level research architecture. This note is not a theorem claim. It fixes the object that future HATTER-SOL work is intended to study.

## 1. The number is a probe, not the final object

The programme is not primarily about isolated properties of an integer, its divisors, or even one fixed port/network realization.

For a rational integer `n`, the central object is the family of representations produced when the ambient arithmetic world, geometric realization class, interface quotient, and host scale are changed.

Symbolically, the intended object is a response field

\[
\boxed{
(R,\mathcal C,k)\longmapsto Z_{R,\mathcal C,k}(n)
}
\]

where:

- `R` is an arithmetic world (for example a quadratic order/field, or later a more general algebraic environment);
- `\mathcal C` is a geometry/architecture class;
- `k` is the host scale;
- `Z` is a sufficiently rich response object, currently represented by an orbital/typed Pareto polynomial when that quotient is appropriate.

The integer `n` is therefore a **probe of the space of worlds**. Different integers provide different signals on the same world space.

## 2. World space

A world should not be indexed merely by a label. It should belong to a graph/category whose transitions have mathematical meaning.

The first established transition family is the HATTER-SOL-09 prime-toggle action on negative squareclasses:

\[
T_q[d]=[qd],
\qquad T_q^2=I,
\qquad T_pT_q=T_qT_p.
\]

This gives canonical finite world cubes after a finite prime set is chosen.

Other possible transition families must be justified before use. Candidates include conductor/order changes, localization/completion directions, extension/restriction of scalars, and ideal-theoretic transitions. Numerical proximity of discriminants is not by itself an admissible world geometry.

## 3. State assigned to a world

For each world `R` and probe `n`, the state should be layered rather than collapsed too early:

\[
\boxed{
\mathsf S_R(n)
=
(\text{factor/ideal data},
\text{interface data},
\text{network data},
\text{response data}).
}
\]

Current HATTER-SOL layers include:

1. world-dependent factorization or prime-ideal factorization;
2. local capacity/interface coordinates;
3. richer orbital datum `\Omega`;
4. orbit-total quotient `\Xi=(A,O)` when justified;
5. admissible network realizations inside a geometry class;
6. Pareto boundary set;
7. polynomial encoding `Z` of that Pareto set.

No quotient should be mistaken for the full state. In particular, the current planar theorems in HATTER-SOL-11 are often exact only for `\Xi`, not for the full `\Omega` semantics.

## 4. Response field and world derivatives

For a fixed probe `n`, geometry `\mathcal C`, and scale `k`, define a world signal

\[
R\longmapsto Z_{R,\mathcal C,k}(n;X,Y,\ldots).
\]

Along a canonical world edge `R -> T_qR`, define

\[
\boxed{
\nabla_q Z_n(R)
=Z_n(R)-Z_n(T_qR).
}
\]

On a finite prime-toggle cube with weights `w_q`, use the already established world Laplacian

\[
\boxed{
\mathcal L_W
=\sum_q w_q(I-T_q).
}
\]

The standard cube spectrum is not the novelty. The research content lies in the arithmetic/network signal on which this operator acts.

## 5. Spectral questions

For each `n`, one may study:

- world Dirichlet energy;
- spectral coefficients of `Z_n` in the world eigenbasis;
- low- versus high-frequency world sensitivity;
- heat flow `e^{-t\mathcal L_W}Z_n` as a controlled coarse-graining of world dependence;
- equality or collision of scalar projections despite nonzero typed/orbital spectral modes;
- reconstruction of splitting/interface information from the world spectrum.

This shifts the question from

> what are the divisors of `n`?

to

> what signal does `n` generate on the space of admissible arithmetic worlds, and what structure is visible in the spectrum of that signal?

## 6. Geometry is a second direction

HATTER-SOL-08/11 already give a second coordinate:

\[
\text{1D}\subseteq\text{outerplanar}\subseteq\text{planar}\subseteq\text{unrestricted}.
\]

At present this is an inclusion hierarchy, not yet a canonical reversible geometry graph, so a geometry Laplacian is not automatically justified.

Nevertheless finite geometry differences are meaningful:

\[
\nabla_{\mathcal C\to\mathcal D}Z
:=Z_{\mathcal D}-Z_{\mathcal C}.
\]

For one world edge and one geometry transition, define the mixed second difference

\[
\boxed{
H_{q,\mathcal C\to\mathcal D}Z
=
Z_{T_qR,\mathcal D}
-Z_{T_qR,\mathcal C}
-Z_{R,\mathcal D}
+Z_{R,\mathcal C}.
}
\]

This is a discrete mixed Hessian. It measures whether the effect of changing geometry depends on the arithmetic world. It should not be called curvature unless a genuine noncommuting transport structure is later defined.

A nonzero mixed Hessian would be direct evidence that arithmetic-world change and geometric restriction interact rather than contributing independently.

## 7. Host scale is a third direction

The host size `k` is not merely a nuisance parameter. HATTER-SOL-11 already shows exact scale transitions such as memory loss, permanent memory, and Euler-defect regimes.

Hence the full laboratory is at least three-dimensional:

\[
\boxed{
\text{world}\times\text{geometry}\times\text{scale}.
}
\]

A probe `n` generates a trajectory/surface/field on this parameter space.

Discrete scale derivatives and critical scales should be treated on the same footing as world derivatives.

## 8. Arithmetic operations become transformations of response fields

The next long-range objective is not only to compare numbers but to understand arithmetic operations as transformations of world-response fields.

For multiplication and addition, do not assume a simple homomorphism law for `Z`. Instead define and measure composition defects.

For any proposed multiplication-composition rule `\Phi_\times`, define

\[
\boxed{
\Delta_\times(n,m;R)
=
Z_R(nm)-\Phi_\times(Z_R(n),Z_R(m)).
}
\]

Likewise for addition with a candidate `\Phi_+`:

\[
\boxed{
\Delta_+(n,m;R)
=
Z_R(n+m)-\Phi_+(Z_R(n),Z_R(m)).
}
\]

The defects themselves may be more informative than an exact composition law. Their world spectra can reveal where an arithmetic operation is stable or highly world-sensitive.

No universal form of `\Phi_\times` or `\Phi_+` is claimed here; finding the correct operations is a research problem.

## 9. Regime transitions are observable data

A world change can move one probe between qualitatively different theorem regimes:

- pure/inert state;
- subcritical regular-support regime;
- low-tail factor regime;
- Euler-defect regime;
- critical-tail balancing regime;
- multi-overload regime.

Therefore the **proof regime itself** is part of the coarse response signature.

The current `(6,5)` planar programme and its `r=14,15,16,17,...` complement parameter should be viewed as one local chart of this larger field, not as the final object of study.

## 10. First canonical laboratory: the prime 61

The prime `61` is especially useful because its interface state changes strongly across quadratic class-number-one worlds.

In the Gaussian world it lies in the difficult planar `(6,5)` regime. In other worlds it can move to low-tail, sub-six, or inert/pure regimes.

Thus `61` is a natural first probe for a complete finite experiment:

\[
R\in\{-1,-2,-3,-7,-11,-19,-43,-67,-163\}
\quad\longmapsto\quad
Z_{R,Pl,k}(61).
\]

The objective is not a table of curious factorizations. The objective is to compute a finite world signal on a canonical graph and then study its derivatives, spectrum, regime transitions, and information loss under projections.

## 11. Immediate theorem programme

The next programme-level targets are:

1. **Complete UFD world-response table for 61.** Determine exact factor/interface states in all nine imaginary quadratic class-number-one worlds, clearly separating element-factorization inputs from network theorems.
2. **Planar response transport.** For each resulting interface state, identify which existing HATTER-SOL-11 theorem gives the exact planar response and isolate the genuinely unresolved states.
3. **World derivative of a planar response.** Compute exact `\nabla_q Z^{Pl}_{61,k}` on every prime-toggle edge available inside the finite UFD laboratory.
4. **World spectral decomposition.** Compute the response energy/eigenmodes on the induced world graph.
5. **Mixed world-geometry Hessian.** Compare at least strict-1D and planar responses for the same world edges and test whether arithmetic and geometry effects separate.
6. **Operation test.** After a single-prime probe is understood, choose the smallest product of two probes for which the multiplication defect can be computed exactly across more than one world.

## 12. Publication discipline

No claim should be made that a Laplacian, hypercube spectrum, quadratic splitting law, graph-factor theorem, or standard algebraic-number-theory construction is new.

Potential new content must lie in proved statements about the composed object

\[
\boxed{
\text{arithmetic world}
\to
\text{factor/ideal state}
\to
\text{interface/network state}
\to
\text{geometry-dependent response}
\to
\text{world/scale operators and spectra}.
}
\]

The long-range success criterion is not another catalog of number properties. It is the emergence of reusable operators and invariants that allow arithmetic objects, arithmetic operations, and arithmetic worlds to be compared inside one response-field formalism.
