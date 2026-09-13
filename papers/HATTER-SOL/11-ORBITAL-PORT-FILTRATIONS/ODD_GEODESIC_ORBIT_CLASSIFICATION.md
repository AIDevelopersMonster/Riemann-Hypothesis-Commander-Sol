# HATTER-SOL-11 · Odd-world geodesic orbit classification

Status: first closed theorem layer. This file attacks the naive `P = strong orbit, Q = weak orbit` hypothesis and replaces it by the canonical object actually supported by the odd-discriminant geometry.

## 1. Setup

Let

\[
\Delta<-3,
\qquad \Delta\equiv1\pmod4,
\]

and put

\[
F=\frac{1+\sqrt\Delta}{2},
\qquad
\bar F=1-F,
\qquad
F\bar F=q=\frac{1+|\Delta|}{4}>1.
\]

Write

\[
\alpha=L+WF.
\]

The HATTER-SOL-09 step set is

\[
S_\Delta=\{\pm1,\pm F,\pm\bar F\}.
\]

Modulo sign there are three step directions

\[
d_0=1,
\qquad d_1=F,
\qquad d_2=\bar F.
\]

For these generic odd worlds the unit group is `+-1`; on undirected directions the only nontrivial natural symmetry is conjugation, which fixes `d_0` and exchanges `d_1,d_2`. Hence the natural direction-orbit partition is

\[
\boxed{
A=\{d_0\},
\qquad
O=\{d_1,d_2\}.
}
\]

Here `A` means axial/rational and `O` means oblique. This is an orbit statement only; no activation order is assumed.

---

## 2. Unique minimal geodesic coefficient triple

Any representation of `alpha` by the three positive directions has the form

\[
\alpha=x+yF+z\bar F.
\]

Since `bar F=1-F`, comparison with `L+WF` gives

\[
L=x+z,
\qquad
W=y-z.
\]

Thus every representation is parametrized by one integer `t=z`:

\[
x=L-t,
\qquad
y=W+t,
\qquad z=t.
\]

Its word length is

\[
f(t)=|L-t|+|W+t|+|t|.
\]

### Theorem T11.1 — unique geodesic triple

Let

\[
m=\operatorname{med}\{L,-W,0\}
\]

be the median of the three integers. Then `f(t)` has the unique minimizer `t=m`. Therefore

\[
\boxed{
g_\Delta(\alpha)
=(x,y,z)
=(L-m,\ W+m,\ m)
}
\]

is the unique minimal coefficient triple for the step directions `(1,F,bar F)`.

### Proof

`f(t)` is the sum of distances from `t` to the three points

\[
L,\quad -W,\quad 0.
\]

For three points on the line, the unique minimizer of the sum of absolute distances is their median. Since the three points are integers, `m` is an integer. Substitution gives the stated triple. QED.

### Corollary T11.1a — one direction vanishes

Because the median is one of `L,-W,0`, at least one of

\[
L-m,
\qquad W+m,
\qquad m
\]

is zero. Thus every odd-world shortest-step representation uses at most two of the three undirected directions.

---

## 3. Exact recovery of the HATTER-SOL-09 folded pair

Let the three numbers `L,-W,0` be arranged increasingly. If the two adjacent gaps are `u,v>=0`, then the three pairwise distances are

\[
u,\qquad v,\qquad u+v.
\]

But those same pairwise distances are

\[
|L|,
\qquad |W|,
\qquad |L+W|.
\]

The two nonzero entries of `g_Delta(alpha)` have absolute values exactly `u,v`.

### Theorem T11.2 — geodesic folding theorem

If

\[
\Pi_\Delta(\alpha)=(P,Q),
\qquad P\ge Q\ge0,
\]

is the HATTER-SOL-09 odd-discriminant typed pair, then

\[
\boxed{
\operatorname{sort}_{\downarrow}
\{|x|,|y|,|z|\}
=(P,Q,0).
}
\]

Consequently

\[
\boxed{
\rho_\Delta(\alpha)
=|x|+|y|+|z|
=P+Q
=
\max\{|L|,|W|,|L+W|\}.
}
\]

Thus the published `(P,Q)` pair is exactly the magnitude-sorted forgetting of a unique direction-labelled geodesic triple.

---

## 4. Canonical orbital geodesic signature

Define

\[
\boxed{
\Omega_\Delta(\alpha)
:=
\bigl(|x|;\{\,|y|,|z|\,\}\bigr),
}
\]

where `(x,y,z)=g_Delta(alpha)`.

The first entry belongs to the axial orbit `A`; the unordered pair belongs to the oblique orbit `O`.

### Proposition T11.3 — symmetry invariance

The signature `Omega_Delta` is invariant under multiplication by `-1` and conjugation, in the natural quotient sense.

Indeed,

\[
g_\Delta(-\alpha)=-g_\Delta(\alpha),
\]

while uniqueness of the geodesic triple gives

\[
g_\Delta(\bar\alpha)=(x,z,y)
\]

whenever

\[
g_\Delta(\alpha)=(x,y,z).
\]

Therefore sign changes no absolute count and conjugation only permutes the two entries inside the oblique orbit.

There is an exact forgetting map

\[
\boxed{
\Omega_\Delta(\alpha)
\longmapsto
\Pi_\Delta(\alpha)
}
\]

obtained by sorting the three recorded absolute counts and dropping the zero.

---

## 5. First no-go: `P` and `Q` are not fixed direction orbits

Take the HATTER-SOL-10 laboratory

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
F=\omega=\frac{1+\sqrt{-15}}2,
\qquad q=4.
\]

The two minimal witnesses of the nonprincipal prime ideal

\[
\mathfrak q=(23,\omega-7)
\]

were

\[
\alpha_S=2+3\omega,
\qquad
\alpha_T=7-\omega.
\]

For `alpha_S`,

\[
m=0,
\qquad
 g(\alpha_S)=(2,3,0),
\]

so

\[
\boxed{
\Omega(\alpha_S)=(2;\{3,0\}),
\qquad
\Pi(\alpha_S)=(3,2).
}
\]

Here the larger folded coordinate `P=3` is oblique, while `Q=2` is axial.

For `alpha_T`,

\[
m=1,
\qquad
 g(\alpha_T)=(6,0,1),
\]

so

\[
\boxed{
\Omega(\alpha_T)=(6;\{1,0\}),
\qquad
\Pi(\alpha_T)=(6,1).
}
\]

Here the larger folded coordinate `P=6` is axial, while `Q=1` is oblique.

Therefore

\[
\boxed{
P\text{ is not a canonical port orbit},
\qquad
Q\text{ is not a canonical port orbit}.
}
\]

In particular the naive interpretation

\[
P=\text{strong orbit},
\qquad
Q=\text{secondary orbit}
\]

cannot be invariant even inside the single field `Q(sqrt(-15))`.

### Stronger hostile example

Take

\[
\beta=1-3\omega.
\]

Then

\[
m=1,
\qquad
 g(\beta)=(0,-2,1),
\qquad
\Pi(\beta)=(2,1).
\]

Both nonzero folded coordinates now come from the **same** natural oblique orbit `O`; the axial orbit has zero usage.

Thus `(P,Q)` can distinguish two directional counts that the ambient natural symmetry exchanges. The HATTER-SOL-09 fold is therefore a rank-by-magnitude quotient, not a fixed orbit labelling.

This does not invalidate HATTER-SOL-09/10: their typed network is mathematically well-defined. It clarifies the semantics of the labels.

---

## 6. Hostile correction: the orbital signature is not independent of `(N,Pi)`

A static orbital refinement would be much stronger if two elements could share the same multiplicative norm and the same folded pair while having different `Omega`. In the generic odd worlds this does **not** happen.

Let

\[
\Pi_\Delta(\alpha)=(P,Q),
\qquad P\ge Q\ge0.
\]

Because one geodesic coefficient vanishes, there are only three support types up to sign and conjugation.

### Type I: axial count `P`, oblique count `Q`

The two used directions have the same sign along a geodesic, and

\[
\boxed{
N_I(P,Q)=P^2+PQ+qQ^2.
}
\]

### Type II: axial count `Q`, oblique count `P`

\[
\boxed{
N_{II}(P,Q)=Q^2+PQ+qP^2.
}
\]

### Type III: two oblique directions

The two oblique coefficients have opposite signs, giving

\[
\boxed{
N_{III}(P,Q)
=q(P^2+Q^2)+(2q-1)PQ.
}
\]

For `P>Q>0` and `q>1`,

\[
N_{II}-N_I
=(q-1)(P^2-Q^2)>0,
\]

and

\[
N_{III}-N_{II}
=(q-1)Q(Q+2P)>0.
\]

Hence

\[
\boxed{
N_I<N_{II}<N_{III}.
}
\]

If `Q=0`, pure axial and pure oblique states have norms `P^2` and `qP^2`, again distinct. If `P=Q>0`, Types I and II already have the same orbital signature, while Type III still has strictly larger norm.

### Theorem T11.4 — norm-resolved fold

For every generic odd discriminant `Delta<-3`, the pair

\[
\boxed{
\bigl(N_\Delta(\alpha),\Pi_\Delta(\alpha)\bigr)
}
\]

uniquely determines the canonical orbital geodesic signature

\[
\boxed{
\Omega_\Delta(\alpha).
}
\]

Indeed the norm identifies which of Types I--III occurs, and the folded pair supplies the two counts.

### Corollary T11.4a

Up to multiplication by `+-1` and conjugation, `(N_Delta,Pi_Delta)` determines the direction-labelled geodesic orbit of `alpha`.

So HATTER-SOL-11 has found a real canonical **unfolding** of `(P,Q)`, but not yet a new independent static arithmetic invariant beyond information already present in `(N,Pi)`.

---

## 7. Consequence for the activation-filtration programme

The first hostile pass gives a precise boundary:

1. **Rejected:** treating `P` and `Q` themselves as two intrinsic ordered port orbits.
2. **Established:** a unique symmetry-compatible direction-labelled geodesic signature exists in generic odd worlds.
3. **Established:** the natural orbit partition is axial versus oblique, not `P` versus `Q`.
4. **Established:** the HATTER-SOL-09 pair is the magnitude-sorted forgetting of that finer object.
5. **No-go:** the static orbital signature adds no independent node information once both multiplicative norm and `(P,Q)` are retained.

Therefore any genuinely new HATTER-SOL-11 layer must come from one of the following:

- an **activation law** on the canonical orbital signature;
- network dynamics that depend on orbit labels before the HATTER-SOL fold;
- a classification of when natural direction orbits admit an intrinsic ordering;
- an exact theorem comparing orbital-network optimization with the published rank-channel network.

The next target is to classify the natural direction-orbit partition for **all** imaginary quadratic discriminant worlds (generic even, Gaussian, generic odd, Eisenstein) and determine whether any universal nontrivial ordered filtration survives the high-symmetry `Delta=-4,-3` cases.

## Prior-art boundary

The hex/axial distance identity

\[
\max(|L|,|W|,|L+W|)
\]

is standard hexagonal-grid geometry and is not claimed as new. The contribution under investigation is its use as a symmetry-resolved refinement of the published HATTER-SOL factor-network capacity and the resulting no-go/classification statements.