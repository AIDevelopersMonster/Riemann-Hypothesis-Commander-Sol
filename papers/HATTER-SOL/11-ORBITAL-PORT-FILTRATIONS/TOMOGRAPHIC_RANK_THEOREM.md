# HATTER-SOL-11 · TOMOGRAPHIC RANK THEOREM

**Status:** closed theorem layer.

Let `W={1,...,m}` be a finite world family, `Omega` an observation space, and let `f_i:Omega->R` be the scalar response signature of world `i`.

For a finite observation set `A={omega_1,...,omega_k}`, define

`E_A(i)=(f_i(omega_1),...,f_i(omega_k))`.

Call `A` separating when `E_A` is injective, and define

`tdim(f_1,...,f_m)=min |A|`

over finite separating observation sets, with value `+infinity` if none exists.

For `i<j`, put

`C_ij={omega:f_i(omega)=f_j(omega)}` and `D_ij=Omega\C_ij`.

## TR11.1 — exact hitting-set characterization

A finite set `A` is separating iff

`A cap D_ij != empty`

for every pair `i<j`. Hence `tdim` is exactly the transversal number of the family of pair-separation sets `{D_ij}`.

### Proof

`E_A(i)=E_A(j)` iff every selected observation lies in `C_ij`; equivalently `A cap D_ij` is empty. QED.

## TR11.2 — finite upper bound

If all signatures are pairwise distinct as functions, then

`1 <= tdim <= m-1`.

### Proof

Start with the indiscrete partition of worlds by currently observed values. If it is not discrete, choose two distinct worlds in one current class. Their functions differ somewhere, so add an observation separating them. The partition strictly refines. At most `m-1` refinements are required. QED.

## TR11.3 — one-shot criterion

`tdim=1` iff

`Omega \ union_{i<j} C_ij`

is nonempty. Thus a single observation fails exactly when pair-collision sets cover the entire observation space.

## TR11.4 — collision-complex theorem

Assume `Omega` is a polyhedral cone (or projective slice) and every `f_i` is continuous piecewise-linear on a common finite fan. Then every collision set `C_ij` is a finite polyhedral subcomplex after finite refinement.

### Proof

On each common linearity cone, `f_i-f_j` is a linear form. Its zero set is either the whole cone or its intersection with a hyperplane. Refining by these hyperplanes gives the claim. QED.

Therefore blindness may occur on isolated walls/rays or on full-dimensional cones when two response laws agree throughout a regime.

## TR11.5 — spectral blind-complex theorem

Let a connected world graph have Laplacian `L`, and let

`F(omega)=(f_1(omega),...,f_m(omega))`.

For a Laplacian eigenspace `E_lambda` with orthogonal projection `P_lambda`, define

`B_lambda={omega:P_lambda F(omega)=0}`.

Also define the fully world-blind set

`B_*={omega:L F(omega)=0}`.

If the signatures are piecewise-linear on a finite common fan, every `B_lambda` and `B_*` is a finite polyhedral subcomplex after finite refinement.

### Proof

On each linearity cone, `F` is a linear vector-valued map. The equations `P_lambda F=0` and `LF=0` are finite homogeneous linear systems in the observation variables. QED.

Because the world graph is connected,

`LF(omega)=0`

iff all worlds have the same observed value at `omega`.

## Interpretation

Three notions are distinct:

1. pair collision — two worlds agree at one observation;
2. tomographic insufficiency — the chosen observations fail to identify all worlds;
3. spectral blindness — specified nonconstant world-Laplacian modes vanish.

For finite piecewise-linear response families, all three are governed by a finite collision/blind polyhedral complex.
