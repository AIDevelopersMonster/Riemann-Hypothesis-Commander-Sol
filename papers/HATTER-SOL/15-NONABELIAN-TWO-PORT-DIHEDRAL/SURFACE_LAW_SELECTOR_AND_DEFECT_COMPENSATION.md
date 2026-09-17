# HATTER-SOL-15 · Surface-Law Selector and Defect Compensation

**Status:** exact theorem layer. Surface-group presentations and representation varieties are classical; H15 contributes the explicit dihedral port comparison and the defect-storage/defect-compensation synthesis.

Let

\[
D_{2p}=\langle R,S\mid R^p=S^2=1,\ SRS^{-1}=R^{-1}\rangle,
\]

with `p` an odd prime.

## 1. Surface relations as observer laws

A labelled port assignment to generators of a surface group is flat precisely when the defining relator evaluates to the identity.

Thus a surface itself supplies a word observer:

\[
\boxed{\text{surface law} + \text{port assignment} \longrightarrow \text{relator defect}.}
\]

Different square edge pairings impose different laws on the same ports.

## 2. Torus: impossible faithful flat dihedral realization

The torus has

\[
\pi_1(T^2)=\langle a,b\mid [a,b]=1\rangle.
\]

Any image of `pi_1(T^2)` is abelian. Therefore no homomorphism from the torus group can have image `D_{2p}`.

For the direct assignment `a->R`, `b->S`,

\[
[R,S]=R^2\ne1.
\]

Hence a single unbranched torus cannot carry the full dihedral port algebra flatly.

## 3. Klein bottle: exact one-square fit

The Klein bottle has presentation

\[
\pi_1(K)=\langle a,b\mid aba^{-1}=b^{-1}\rangle.
\]

Set

\[
a\mapsto S,
\qquad
b\mapsto R.
\]

Then the defining relation becomes exactly

\[
SRS^{-1}=R^{-1}.
\]

Since `R,S` generate `D_{2p}`, this gives a surjection

\[
\boxed{\pi_1(K)\twoheadrightarrow D_{2p}.}
\]

Thus the same two ports that are curved relative to the torus law are flat relative to the Klein-bottle law.

## 4. Orientable genus two: exact defect cancellation

For the closed orientable genus-two surface,

\[
\pi_1(\Sigma_2)
=\langle a_1,b_1,a_2,b_2\mid
[a_1,b_1][a_2,b_2]=1\rangle.
\]

Assign

\[
(a_1,b_1)\mapsto(R,S),
\qquad
(a_2,b_2)\mapsto(R^{-1},S).
\]

Then

\[
[R,S]=R^2,
\qquad
[R^{-1},S]=R^{-2},
\]

so

\[
\boxed{[R,S][R^{-1},S]=1.}
\]

The image contains `R` and `S`, hence is all of `D_{2p}`.

Therefore

\[
\boxed{\pi_1(\Sigma_2)\twoheadrightarrow D_{2p}.}
\]

## Theorem H15.46 — minimal orientable genus for a flat faithful dihedral port world

The minimal genus of a closed orientable surface whose fundamental group surjects onto `D_{2p}` is

\[
\boxed{g_{or}=2.}
\]

### Proof

Genus zero has trivial fundamental group. Genus one has abelian fundamental group and therefore only abelian finite images. Genus two admits the explicit surjection above. QED.

## Theorem H15.47 — minimal closed nonorientable genus

The projective plane has fundamental group `C_2`, so it cannot surject onto `D_{2p}`. The Klein bottle (nonorientable genus two) admits the explicit surjection above. Hence

\[
\boxed{g_{nonor}=2.}
\]

in the crosscap-count convention.

## 5. Branch storage versus handle compensation

For the one-handle torus assignment `(R,S)`, the commutator defect is

\[
K=R^2.
\]

There are at least two exact ways to absorb it:

### A. Localized branch storage

Keep one torus handle and allow one branch value. Since `R^2` is one `p`-cycle, Riemann-Hurwitz gives the compact covering surface genus

\[
\boxed{g_{branch}=(p+1)/2.}
\]

### B. Global handle compensation

Add a second handle carrying the inverse commutator `R^{-2}`. Then the total surface relator is exactly trivial and no branching is required:

\[
\boxed{g_{flat}=2.}
\]

Thus for large `p`, localizing the entire defect in one branch point has linearly growing genus cost, whereas global compensation needs only one additional handle.

Safe synthesis:

\[
\boxed{\text{topology can store a defect locally or cancel it globally}.}
\]

These are different geometric realizations of the same port algebra.

## 6. Surface compatibility fingerprint

For a port algebra `G` and a family of surface relators `r_Sigma`, define the compatibility response

\[
\mathcal C_\Sigma(\text{ports})
:=r_\Sigma(\text{assigned port elements}).
\]

For the dihedral pair:

- torus response: `R^2`;
- Klein response: `1`;
- genus-two orientable paired response: `1`.

Hence the same ports have a nontrivial **surface-law fingerprint**.

## Claim boundary

Finite quotients of surface groups, representation varieties, and the Klein/torus presentations are classical. The explicit genus-two construction is elementary. H15 does not claim those general facts as new.

The H15-specific point is the comparison of the same arithmetic two-port algebra under several surface observers and the quantitative contrast between branching cost `(p+1)/2` and unbranched two-handle compensation.