# HATTER-SOL-15 · Research Ledger

**Purpose:** preserve secondary lines without diluting the main research effort.

## Priority A — main line

### A1. Mahler / regulator decomposition of the dihedral spectral curve

Current exact input:

\[
J(C_k)\sim E_{ab}\times E_{ac}\times E_{bc}\times J(C_{abc}).
\]

Primary target: determine whether the regulator class underlying the Mahler measure of the block determinant decomposes compatibly with these factors, yielding a formula in elliptic/genus-two L-data.

Immediate laboratory: `p=3`, `mu=4` (`lambda=0`). Then `theta=-1` and

\[
Q(u)=u^2+4u+13,
\qquad
Q(u)-4=u^2+4u+9.
\]

The three elliptic quotient quartics are

\[
E_{ab}: y^2=(u^2-4)(u^2+4u+13),
\]

\[
E_{ac}: y^2=(u^2-4)(u^2+4u+9),
\]

\[
E_{bc}: y^2=(u^2+4u+13)(u^2+4u+9).
\]

The genus-two factor is

\[
C_{abc}:y^2=(u^2-4)(u^2+4u+13)(u^2+4u+9).
\]

One elliptic quotient has rational model

\[
y^2=x^3+117x+918
\]

and is a classical modular elliptic curve (conductor 360; verify minimal model/isogeny label before publication).

**Return criterion:** exact regulator pullback/pushforward identity, recognized L-value relation, or a rigorous obstruction showing no simple decomposition.

### A2. Jensen / transfer-root representation

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

Primary target: turn the full two-torus Mahler measure into a period/regulator integral on the quotient curves above.

## Priority B — strong secondary lines

### B1. Cyclotomic contour / Ramanujan / zeta

Exact identity already proved:

\[
I_{p,m}(\rho>1)=c_p(m)
\]

and

\[
\sum_{m\ge1}\frac{c_p(m)}{m^s}
=(p^{1-s}-1)\zeta(s).
\]

Interpretation:

\[
\text{contour jump}
=\text{Ramanujan sum}
=\text{centered rotation character}.
\]

**Return criterion:** a new transform or positivity/spectral statement constraining the non-explicit zeros of this Dirichlet series, not merely rephrasing RH.

### B2. Family of cyclotomic contours and Ramanujan-Fourier arithmetic

Generalize from prime conductor `p` to all `q`:

\[
\Phi_q'/\Phi_q\quad\leadsto\quad c_q(n).
\]

Potential target: reconstruct prime-sensitive arithmetic functions by a controlled Ramanujan expansion and interpret the coefficients as contour/observer weights.

**Caution:** Ramanujan expansions of classical arithmetic functions are old; novelty could only lie in a new port/surface/spectral constraint or in a new convergence/positivity structure.

### B3. Double Fourier -> Dirichlet channels

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

### B4. Square torus / Dirac zeta split

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
- become flat on orientable genus 2 by commutator compensation.

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

For permutation ports this counts fixed points of the commutator.

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

1. Classical components (Riemann-Hurwitz, Kani–Rosen, Mahler measure, Jensen, Ramanujan sums, Artin formalism, Dirichlet characters, Epstein zeta) must be cited as classical.
2. H15 novelty, if any, must lie in a **specific synthesis, exact arithmetic specialization, or new constraint**, not in renaming known machinery.
3. No RH/GRH claim unless a genuinely new zero-control theorem is proved.
4. Keep distinct:

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

5. Primary working hypothesis to test, not assume:

\[
\boxed{
\text{Mahler/regulator of the dihedral spectral determinant}
\stackrel{?}{=}
\text{sum of quotient-motive L-data}.
}
\]
