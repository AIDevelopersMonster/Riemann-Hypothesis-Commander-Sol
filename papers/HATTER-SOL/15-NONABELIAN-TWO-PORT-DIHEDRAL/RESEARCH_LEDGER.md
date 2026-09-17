# HATTER-SOL-15 · Research Ledger

**Purpose:** preserve secondary lines without diluting the main research effort.

## Priority A — non-Abelian main line

### A1. Dihedral commutator -> Ramanujan -> zeta

The H15 core is the non-Abelian two-port Schreier system

\[
R:i\mapsto i+1,
\qquad
S:i\mapsto-i,
\qquad
K=[R,S]=R^2.
\]

On the centered Schreier representation

\[
V_0=\mathbf C[\mathbf F_p]\ominus\mathbf1,
\]

we now have the exact theorem

\[
\boxed{
\operatorname{Tr}(K^m\mid V_0)=c_p(m)
}
\]

for every `m>=1`, hence

\[
\boxed{
\mathcal Z_p^{\rm comm}(s)
:=\sum_{m\ge1}\frac{\operatorname{Tr}([R,S]^m\mid V_0)}{m^s}
=(p^{1-s}-1)\zeta(s).
}
\]

This reconnects the previously separate H15 layers:

\[
\boxed{
\text{non-Abelian route-order defect}
\to
\text{plaquette holonomy}
\to
\text{centered Schreier character}
\to
\text{Ramanujan sequence}
\to
\text{cyclotomic contour jump}
\to
\zeta(s).
}
\]

Exact contour/commutator identity:

\[
I_{p,m}(\rho>1)
=
\operatorname{Tr}([R,S]^m\mid V_0)
=c_p(m).
\]

**Primary return criterion:** find a genuinely new geometric/spectral constraint on this commutator response — positivity, self-adjoint transfer, trace identity, regulator identity, or another theorem not automatic from the classical Ramanujan/Dirichlet-series formula.

**Claim boundary:** Ramanujan sums, their character interpretations, the Dirichlet-series identity, dihedral character theory, and closed-walk holonomy traces are classical. Any H15 novelty must lie in the full composition through the non-normal Schreier world and ordered-port commutator, not in any one classical ingredient.

### A2. Non-Abelian spectral observer and Mahler regulator character filter

For the dihedral Floquet spectral curve,

\[
J(C_k)\sim E_{ab}\times E_{ac}\times E_{bc}\times J(C_{abc}).
\]

The natural Mahler regulator form is not a mixture of all four positive-genus sectors. It transforms by the pure `abc` character under the multiquadratic involutions. Therefore

\[
(\pi_{ab})_*\eta
=(\pi_{ac})_*\eta
=(\pi_{bc})_*\eta
=0,
\]

while

\[
\pi_{abc}^*\bar\eta=\eta.
\]

Thus the natural Mahler observer sees only the genus-two `abc` sector.

In the immediate laboratory `p=3`, `mu=4` (`lambda=0`),

\[
Q(u)=u^2+4u+13,
\qquad
Q(u)-4=u^2+4u+9,
\]

and

\[
C_{abc}:y^2=(u^2-4)(u^2+4u+13)(u^2+4u+9).
\]

After `x=u+2`,

\[
C:y^2=x(x-4)(x^2+5)(x^2+9).
\]

A separate theorem layer gives an absolutely-simple genus-two Jacobian in this laboratory.

**Return criterion:** verify the descended motivic `K_2` class/tame symbols, identify the genus-two `L`-data, and test whether the Jensen/Mahler period matches the selected simple motive.

### A3. Jensen / transfer-root representation

For each mirror block, after setting `t=w^2`,

\[
D_k=B_k(z)-t-t^{-1}.
\]

The roots satisfy

\[
t_+t_-=1,
\qquad
 t_\pm=\frac{B_k\pm\sqrt{B_k^2-4}}2.
\]

Hence the `w`-circle Jensen integral keeps only the exterior transfer root:

\[
\frac1{2\pi}\int_0^{2\pi}\log|D_k(z,e^{i\phi})|d\phi
=
\log\max(1,|t_+(z)|).
\]

Primary target: turn the full two-torus Mahler measure into a period/regulator integral on the observer-selected genus-two quotient.

## Priority B — strong secondary lines

### B1. Family of cyclotomic contours and Ramanujan-Fourier arithmetic

Generalize from prime conductor `p` to all odd `q`:

\[
\Phi_q'/\Phi_q\quad\leadsto\quad c_q(n).
\]

For composite odd `q`, the full centered Schreier representation is larger than the primitive cyclotomic sector; the primitive frequency subspace recovers

\[
\operatorname{Tr}(R^{2m}\mid V_q^{\rm prim})=c_q(m).
\]

Potential target: determine whether the primitive-sector projection has a natural port/surface meaning rather than being an imposed Fourier truncation.

### B2. Double Fourier -> Dirichlet channels

Exact two-stage structure:

\[
\mathbb F_p
\xrightarrow{\text{additive Fourier}}
k
\xrightarrow{/\pm}
[k]
\xrightarrow{\text{multiplicative Fourier}}
\chi,
\]

where `chi` ranges over even Dirichlet characters mod `p`.

**Return criterion:** geometry-induced relations between character channels that are not automatic from character orthogonality or cyclotomic Galois theory.

### B3. Square torus / Dirac zeta split

Known exact identities:

\[
\zeta_{\Delta_{T^2}}(s)
=4(4\pi^2)^{-s}\zeta(s)\beta(s),
\]

and for quarter-twist eta observer

\[
\eta_{1/4}(s)=4^s\beta(s).
\]

Hence a ratio isolates `zeta(s)` meromorphically.

**Return criterion:** a natural port/observer construction that produces a new positivity, self-adjointness, or trace identity for the isolated zeta factor. Merely isolating it algebraically is classical.

## Priority C — structural geometry retained for synthesis

### C1. Surface law selector

Same ports `(R,S)`:

- violate torus law `[R,S]=1`;
- exactly satisfy Klein bottle law `SRS^{-1}=R^{-1}`;
- become flat on orientable genus `2` by commutator compensation.

### C2. Branched torus genus cost

For square-loop defect `K=[A,B]`, closing the puncture gives

\[
g=1+\frac{n-c(K)}2.
\]

For dihedral `(R,S)`, `K=R^2` is one `p`-cycle, hence

\[
g=(p+1)/2.
\]

### C3. Spectral detection of path-order defect

The first closed square walk appears at length four, so the fourth spectral moment contains

\[
\operatorname{Tr}[A,B]+\operatorname{Tr}[A,B]^{-1}.
\]

Repeated plaquette traversals give

\[
\operatorname{Tr}([A,B]^m).
\]

For the dihedral H15 pair, their centered values are exactly `c_p(m)`.

### C4. Non-Abelian Floquet pairing and Dirac-like cones

Exact mode pairing

\[
k\leftrightarrow-k
\]

and explicit `2x2` dispersion blocks are retained as the local spectral mechanism behind the cyclotomic field.

## Priority D — inter-world arithmetic retained

### D1. Projective tomography/code

Dihedral class-field worlds indexed by `P(V*)` recover projective ideal classes in `P(V)` and realize a constant-weight projective incidence code with exact distance

\[
2p^{r-2}.
\]

### D2. Zeta assembly

Centered world representations sum to the large generalized-dihedral world, giving

\[
\prod_H\frac{\zeta_{K_H}(s)}{\zeta(s)}
=
\frac{\zeta_{K_*}(s)}{\zeta(s)}.
\]

### D3. Gram/Parseval and no-free-cancellation barrier

World-space transform is a regular-simplex/tight-frame transform. It exactly repackages projective prime-class variance but does not create analytic cancellation for free.

## Global claim discipline

1. H15 is fundamentally the **non-Abelian two-port article**. Spectral curves, surfaces, regulators and zeta transforms are observers of that noncommutative structure, not replacements for the central subject.
2. Classical components (Riemann-Hurwitz, Kani-Rosen, Mahler measure, Jensen, Ramanujan sums, Artin formalism, Dirichlet characters, Epstein zeta, standard dihedral representation theory) must be cited as classical.
3. H15 novelty, if any, must lie in a **specific synthesis, exact arithmetic specialization, or new constraint**, not in renaming known machinery.
4. No RH/GRH claim unless a genuinely new zero-control theorem is proved.
5. Keep distinct:

\[
\text{graph genus},
\quad
\text{surface-law flatness},
\quad
\text{branched-cover genus},
\quad
\text{spectral genus},
\quad
\text{arithmetic L-data}.
\]

6. The two most serious active H15 questions are now:

\[
\boxed{
\text{Does non-Abelian geometry impose a new analytic constraint on }
\mathcal Z_p^{\rm comm}(s)?
}
\]

and

\[
\boxed{
\text{Does the natural Mahler observer produce an exact regulator/}L\text{-value law on the selected simple genus-two motive?}
}
\]
