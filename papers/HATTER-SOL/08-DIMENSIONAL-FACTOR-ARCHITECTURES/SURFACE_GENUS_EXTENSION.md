# Surface-genus extension seed

**Parent:** HATTER-SOL-08 · Dimensional Factor Architectures  
**Status:** theorem candidate / future paper; not part of the current HATTER-SOL-08 publication claim.

## 1. Surface ladder

Let `Sigma_g` be the closed orientable surface of genus `g` and define

\[
M_g(\mathbf c)=\max\{|E(G)|:\;G\hookrightarrow\Sigma_g,\;G\text{ connected simple},\;\deg(v_i)\le c_i\},
\]

\[
\lambda_g(\mathbf c)=\sum_i c_i-2M_g(\mathbf c).
\]

Then

\[
\lambda_0\ge\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_{A},
\]

where `lambda_A` is the unrestricted value from HATTER-SOL-07. Here `g=0` is the sphere/planar class and `g=1` is the torus.

A toroidal embedding means crossing-free on the torus itself; edges that would cross in a planar projection may be routed through the handle.

## 2. Global fixed-genus barrier

Euler's formula on an orientable genus-`g` surface gives, for a simple embedded graph with `n>=3`,

\[
|E|\le 3n-6+6g.
\]

Thus a fixed-genus surface has only a linear edge budget, unlike the unrestricted complete-graph budget `binom(n,2)`.

For the complete-capacity vector

\[
\mathbf c^{(k)}=(k-1,\ldots,k-1),
\]

we obtain the calibration lower bound

\[
\lambda_g(\mathbf c^{(k)})
\ge
k(k-1)-2(3k-6+6g)
=(k-3)(k-4)-12g.
\]

For the torus (`g=1`):

\[
\boxed{\lambda_{T^2}(\mathbf c^{(k)})\ge k(k-7).}
\]

`K_7` embeds on the torus, so the complete-capacity vector with `k=7` is fully saturable. `K_8` has orientable genus `2`, so the torus already fails to saturate the `k=8` complete-capacity vector. The unrestricted/3D class still has `lambda_A=0` for every such complete-capacity vector.

This is a permanent fixed-genus obstruction: one handle makes the architecture richer than the plane but never asymptotically equivalent to unrestricted 3D.

## 3. Local clique-block reduction on a surface

Let

\[
h_g:=\max\{h:\;K_h\hookrightarrow\Sigma_g\}.
\]

By the complete-graph genus formula

\[
\gamma(K_h)=\left\lceil\frac{(h-3)(h-4)}{12}\right\rceil,
\]

so for orientable surfaces

\[
h_g=
\left\lfloor\frac{7+\sqrt{1+48g}}2\right\rfloor.
\]

In particular,

\[
h_0=4,
\qquad
h_1=7.
\]

Take `h_g` consecutive incidences at a vertex `x` in a fixed embedding on `Sigma_g`. If all `h_g` neighbors were pairwise adjacent, then together with `x` they would span `K_{h_g+1}`, contradicting the definition of `h_g`.

Hence some pair `u,v` in the block is nonadjacent. Delete the `h_g` spokes and insert `uv` inside the freed local disk sector. Every surface is locally a disk, so the HATTER-SOL-08 four-block argument generalizes locally.

The operation gives

\[
\Delta\deg(x)=-h_g,
\qquad
\Delta|E|=-(h_g-1).
\]

Therefore reducing the degree of `x` by `r` costs at most

\[
\boxed{
L_g(r)
\le
\left\lceil\frac{(h_g-1)r}{h_g}\right\rceil.
}
\]

For `g=0`, this recovers the planar coefficient `3/4`. For the torus it gives `6/7`.

## 4. Connectivity recovery on fixed genus

The orientable genus is additive over connected components and over blocks (Battle-Harary-Kodama-Youngs). This supplies the surface analogue of the planar connectivity-recovery lemma.

Choose a maximum-edge feasible graph of genus at most `g` with the minimum number of components.

- If two components contain unsaturated vertices, join them by a bridge; the added bridge is a genus-zero block, so genus does not increase, while edge count does.
- If a saturated component must be joined to an unsaturated component, delete a nonbridge edge in the saturated component and use one freed endpoint to connect to the unsaturated vertex. Edge count is preserved and genus cannot increase.
- If two saturated components must be joined, delete one nonbridge edge in each and perform a two-edge switch between the components. It can be embedded on the connected sum of the original component surfaces, so the total genus is no larger than the sum of the original genera.

Thus the maximum feasible edge count may again be taken connected.

This step should receive a hostile proof audit before publication, but it has a standard genus-additivity foundation unavailable in the naive outerplanar argument.

## 5. Candidate surface-suppression theorem

For the arithmetic split

\[
2q\to(2,q),
\qquad
\delta=q-2,
\]

the HATTER-SOL-08 proof scheme then yields

\[
\boxed{
\Delta_g^{\max}(2,q)
\le
U_g(q)
:=
2\left\lceil
\frac{(h_g-1)(q-2)}{h_g}
\right\rceil
-(q-2).
}
\]

Asymptotically,

\[
U_g(q)
=
\frac{h_g-2}{h_g}(q-2)+O(1).
\]

Since `h_g` is finite for fixed genus, every fixed closed orientable surface remains strictly below the unrestricted coefficient `1` for sufficiently large `q`.

Strict separation from unrestricted/3D is guaranteed once

\[
q-2\ge h_g.
\]

## 6. Toroidal specialization

For the torus,

\[
h_1=7.
\]

Hence the candidate bound is

\[
\boxed{
\Delta_{T^2}^{\max}(2,q)
\le
2\left\lceil\frac{6(q-2)}7\right\rceil-(q-2).
}
\]

Asymptotically,

\[
\boxed{
\Delta_{T^2}^{\max}(2,q)
\lesssim
\frac57(q-2),
}
\]

whereas

\[
\Delta_{Pl}^{\max}(2,q)\lesssim\frac12(q-2)
\]

and

\[
\Delta_A^{\max}(2,q)=q-2.
\]

Thus the predicted hierarchy is

\[
\boxed{
\frac12
\quad\longrightarrow\quad
\frac57
\quad\longrightarrow\quad
1
}
\]

for planar, toroidal, and unrestricted/3D worst-case refinement sensitivity on this family.

For the torus the bound becomes strictly smaller than the unrestricted value for all

\[
\boxed{q\ge9.}
\]

So the torus moves the amplitude toward the 3D law but does not reach it.

## 7. Surface-specific barriers beyond clique size

The clique-block bound cannot be expected to be exact in general. Toroidal embeddability has non-clique obstructions as well, so a torus can impose additional architecture-specific restrictions not visible from `h_1=7` alone.

This suggests two layers of surface arithmetic:

1. a coarse genus barrier controlled by the largest embeddable clique;
2. finer surface-specific obstruction patterns that may lower `Delta_g^max` below `U_g`.

The torus is therefore expected to be a genuine intermediate arithmetic regime, not merely a numerical interpolation between planar and unrestricted models.

## 8. Homological enrichment

The present free-boundary invariant depends only on the abstract edge count. A surface embedding contains additional information.

For an embedding

\[
G\hookrightarrow\Sigma_g,
\]

define the surface-use rank

\[
\rho(G\hookrightarrow\Sigma_g)
:=
\operatorname{rank}
\operatorname{im}
\bigl(H_1(G;\mathbb Z)\to H_1(\Sigma_g;\mathbb Z)\bigr).
\]

Then

\[
0\le\rho\le2g.
\]

On the torus, `rho` can be `0,1,2`, distinguishing networks whose cycles are all contractible from networks using one or both fundamental directions of the torus.

A future enriched optimization could study the Pareto family

\[
(\lambda_g,\rho)
\]

or conditional minima `lambda_{g,rho}`. This would make the handle itself part of the arithmetic architecture instead of using genus only as an admissibility constraint.

## 9. Research decision

Do not expand the current HATTER-SOL-08 publication candidate with this material. Treat it as a direct sequel / surface-genus theorem programme.

Immediate proof obligations:

1. hostile-audit the fixed-genus connectivity-recovery lemma;
2. prove the local `h_g`-block reduction in full surface-embedding notation;
3. verify the toroidal `q>=9` threshold and small cases computationally;
4. search literature for capacity-constrained extremal sensitivity on fixed-genus surfaces;
5. determine whether the toroidal bound is ever sharp;
6. test whether homology rank introduces additional refinement obstructions.
