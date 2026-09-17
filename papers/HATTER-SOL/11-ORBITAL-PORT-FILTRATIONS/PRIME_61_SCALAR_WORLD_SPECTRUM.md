# HATTER-SOL-11 · PRIME 61 SCALAR WORLD SPECTRUM

**Status:** closed theorem layer.

Probe: `N=61^6`. Geometry comparison: strict `1D -> planar`. World graph: induced nine-world class-number-one UFD star centered at the Gaussian world.

## Theorem GS11.1 — exact splitting-character law

For every world in the nine-world laboratory,

`g_R := Lambda_1D(R)-Lambda_Pl(R)`

satisfies

`g_R = 38` if 61 splits, and `g_R = 14` if 61 is inert.

Equivalently,

`g_R = 26 + 12 chi_R(61)`.

Proof. In a split world `61^6` has 12 irreducible factor nodes. Strict 1D uses 11 edges and the exact 12-vertex Platonic planar support uses 30, so the scalar gain is `2(30-11)=38`. In an inert world the canonical host has 6 nodes; strict 1D uses 5 edges and the octahedral planar host uses 12, so the gain is `2(12-5)=14`. QED.

Thus scalarization forgets the four distinct split interfaces `(6,5),(5,4),(7,1),(4,1)` and retains only split versus inert.

## Theorem GS11.2 — hidden split-sector sensitivity

Let `Gamma_R := Z_Pl(R)-Z_1D(R)` in the additive polynomial group.

Along each UFD-star edge from Gaussian `Delta=-4` to the split leaves `Delta=-3,-19,-163`, one has

`D_e^W g = 0`

but

`D_e^W Gamma != 0`.

Indeed the Gaussian typed response reaches Y-degree 60; Eisenstein reaches only 48; the `Delta=-19` response only 12; and the `Delta=-163` planar response contains the constant monomial 1 because `(4,1)` saturates the icosahedral host.

Hence scalar projection annihilates genuine split-world directions that remain visible before scalarization.

## Exact scalar Laplacian spectrum

Use the unweighted world star `K_{1,8}`, whose standard Laplacian spectrum is `0^(1),1^(7),9^(1)`.

The scalar signal is 38 at the center, 38 on three split leaves and 14 on five inert leaves.

The leaf mean is `23`, the global mean is `74/3`, and with

`v_*=(8,-1,-1,-1,-1,-1,-1,-1,-1)`

one has `Lv_*=9v_*` and

`g=(74/3)1+(5/3)v_*+h`,

where `h(center)=0`, `h=15` on the three split leaves and `h=-9` on the five inert leaves. Hence `Lh=h`.

The scalar signal therefore has nonzero components in both nonconstant eigenspaces.

## Exact Dirichlet energy

Only the five center-to-inert edges contribute, each with jump 24. Thus

`E(g)=5*24^2=2880`.

The radial part has squared norm 200 and contributes `9*200=1800`.

The leaf-contrast part has squared norm

`3*15^2+5*9^2=1080`

and contributes 1080.

Therefore

`2880=1800+1080`,

so the scalar world-sensitivity energy splits as `5/8` radial and `3/8` leaf-contrast.

## Programme consequence

For the probe `61^6`, the scalar geometry signal is exactly an affine function of the quadratic splitting character, while the full typed response contains strictly more world information.

The next operator target is therefore a projection-loss theorem: determine when a coarse response projection preserves, merges, or annihilates world-Laplacian eigenspaces.