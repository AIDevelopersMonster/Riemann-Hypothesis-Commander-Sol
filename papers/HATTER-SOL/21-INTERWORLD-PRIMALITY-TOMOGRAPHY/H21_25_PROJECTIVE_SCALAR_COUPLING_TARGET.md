# HATTER-SOL-21 · PROJECTIVE / SCALAR COUPLING DECOMPOSITION TARGET

Status: **NEXT ACTIVE THEOREM STRIKE**

## 1. Reciprocal phase coordinates

For each local prime \(p\),

\[
m=q\bmod h_p
\]

has the unique decomposition

\[
m=r_p+k_p e_p,
\]

with

\[
r_p\in\mathbf Z/e_p\mathbf Z,
\qquad
k_p\in\mathbf Z/d_p\mathbf Z.
\]

Similarly,

\[
p\bmod h_q
=
r_q+k_q e_q.
\]

The zero-mask is determined by incidence of \((r,k)\) with complete fibers and
partial-transversal graphs.

## 2. Three candidate sources of coupling

### Projective coupling

The projective residues

\[
r_p=q\bmod e_p,
\qquad
r_q=p\bmod e_q
\]

may be correlated.

### Scalar-fiber coupling

Conditioned on projective phases, the fiber coordinates

\[
k_p,\ k_q
\]

may be correlated.

### Graph coupling

Even if \(r\) and \(k\) were separately near-independent, the deterministic
observer graph

\[
k=k_c(r)
\]

can convert weak arithmetic correlation into strong mask correlation.

## 3. Exact decomposition target

Introduce increasingly fine sigma-algebras:

\[
\mathcal F_{\chi}
\subset
\mathcal F_{\chi,r}
\subset
\mathcal F_{\chi,r,k}.
\]

Apply the law of total covariance to the same-mask indicators.

The goal is an exact identity of the form

\[
\boxed{
K
=
K_{\rm residual}
-
H_{\rm projective}
-
H_{\rm fiber}
-\cdots
}
\]

where every heterogeneity term is nonnegative and attached to an explicit
arithmetic coordinate.

This will identify the first coordinate level at which the remaining
reciprocal dependence actually lives.

## 4. Immediate finite lab

For the broad common-core family:

1. compute \((r_p,k_p,r_q,k_q)\) for every semiprime pair;
2. stratify first by character signs;
3. then by projective residue classes or coarser projective relations;
4. then by scalar-fiber classes;
5. measure how much of \(K_s\) is removed at each refinement.

## 5. Decision rule

If projective stratification explains most coupling, the geometry is genuinely
projective.

If not, but scalar-fiber refinement does, the hidden mechanism lives in the
base-field scalar action.

If both fail, the essential object is the detailed partial-transversal graph

\[
r\mapsto k(r).
\]

This provides a clean hierarchy instead of further ad hoc clock statistics.
