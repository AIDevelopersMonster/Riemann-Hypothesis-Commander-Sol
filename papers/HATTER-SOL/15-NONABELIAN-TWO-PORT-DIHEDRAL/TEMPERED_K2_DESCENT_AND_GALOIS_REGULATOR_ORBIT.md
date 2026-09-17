# HATTER-SOL-15 · Tempered K2 Descent and Galois Regulator Orbit

**Status:** exact theorem layer under the generic smooth-normalization hypotheses already used for the mirror-channel spectral curve.  
**Purpose:** answer the next question left open by the spectral-orbit-collapse theorem: does an individual primitive spectral factor carry a genuine regulator class, and if so, what information survives before the full cyclotomic norm collapses the channel labels?

The answer has two parts:

1. the mirror-block Laurent polynomial is automatically tempered; hence the natural symbol `{z,w}` has torsion tame symbols at the toric boundary and defines a rational `K_2` class on the smooth projective normalization;
2. after the previously proved `abc` character projection, that class descends rationally to the selected genus-two quotient, and the resulting motivic classes form a Galois orbit across the real cyclotomic mirror channels.

Thus the full norm forgets channel labels, while an individual primitive regulator class retains the signless Galois coordinate.

---

## 1. Mirror-block Laurent polynomial and Newton polygon

Fix an odd prime `p`, a nonzero mirror channel `k`, and put

\[
\vartheta_k=2\cos\frac{2\pi k}{p},
\qquad
\mu=4-\lambda.
\]

The mirror-block determinant is

\[
D_k(\mu;X,Y)
=\mu^2-\mu X\vartheta_k+X^2+\vartheta_k^2-Y^2-4,
\]

with

\[
X=z+z^{-1},
\qquad
Y=w+w^{-1}.
\]

Expanding as a Laurent polynomial gives

\[
\boxed{
\begin{aligned}
D_k(z,w)
={}&z^2+z^{-2}-w^2-w^{-2}\\
&-\mu\vartheta_k(z+z^{-1})
+\mu^2+\vartheta_k^2-4.
\end{aligned}}
\]

Its Newton polygon is the diamond

\[
\operatorname{conv}\{(2,0),(0,2),(-2,0),(0,-2)\}.
\]

The terms involving `mu` and `vartheta_k` lie strictly inside this polygon or on the horizontal interior lattice points `(+-1,0)` and therefore do not alter the four outer face polynomials.

Along each edge, after choosing the natural one-variable edge parameter, the face polynomial is, up to a monomial and a nonzero scalar,

\[
\boxed{1-t^2}
\qquad\text{or}\qquad
\boxed{t^2-1}.
\]

Hence every face root is `+1` or `-1`.

---

## Theorem H15.85 — automatic temperedness of every mirror block

For every `mu` and every mirror channel `k`, the Laurent polynomial `D_k(z,w)` is tempered in the standard Newton-polygon sense: every face polynomial has only roots of unity.

### Proof

The Newton polygon and its face polynomials were computed above. Their only roots are `+-1`. QED.

### Consequence for tame symbols

Let `C_k^circ` be the affine spectral curve

\[
D_k(z,w)=0
\]

inside `(G_m)^2`, and let `C_k` denote the smooth projective normalization of its toric compactification. Consider

\[
\xi_k:=\{z,w\}\in K_2^M(K(C_k)).
\]

At an interior point of `C_k^circ`, both `z` and `w` are units, so the tame symbol is trivial. At a point above the toric boundary, the tame symbol is determined by the corresponding face root. Since every face root is `+-1`, every boundary tame symbol is torsion; in fact it is a root of unity of order dividing `2`.

Therefore all tame symbols vanish after tensoring with `Q`.

Using Matsumoto's theorem for the function field and the localization sequence for the smooth projective curve gives:

## Corollary H15.86 — the natural symbol is a rational curve-K2 class

\[
\boxed{
\xi_k
\in
K_2(C_k)\otimes\mathbf Q.
}
\]

More precisely, the function-field symbol `{z,w}` lies in the rational tame kernel of the smooth projective normalization.

This closes the boundary/temperedness obstruction left open in `MAHLER_REGULATOR_CHARACTER_FILTER.md`.

### Claim boundary

The implication

\[
\text{tempered Newton faces}
\Longrightarrow
\text{torsion tame symbols of }\{z,w\}
\]

is classical Mahler-measure/K-theory machinery. The H15-specific point is that the dihedral Floquet mirror block has a parameter-independent diamond boundary whose face polynomials are all `1-t^2` up to units, so temperedness holds uniformly in the spectral and cyclotomic parameters.

---

## 2. Promotion of the `abc` filter from differential form to motivic K2 class

Recall the multiquadratic presentation

\[
K(C_k)
=K(u)(\sqrt a,\sqrt b,\sqrt c),
\]

with

\[
a=u^2-4,
\qquad
b=Q_k(u),
\qquad
c=Q_k(u)-4,
\]

and Galois group

\[
G=\langle\sigma_a,\sigma_b,\sigma_c\rangle
\cong(C_2)^3.
\]

The previously proved rationalized symbol law is

\[
\sigma_a\xi_k
=
\sigma_b\xi_k
=
\sigma_c\xi_k
=-\xi_k
\quad\text{in }K_2(C_k)\otimes\mathbf Q.
\]

Thus `xi_k` lies in the pure character

\[
\chi_{abc}(\sigma_a)
=
\chi_{abc}(\sigma_b)
=
\chi_{abc}(\sigma_c)
=-1.
\]

Let

\[
H_{abc}=\ker\chi_{abc}
\]

and let

\[
\pi_k:C_k\to C_{abc,k}=C_k/H_{abc}
\]

be the genus-two quotient.

## Theorem H15.87 — exact rational K2 descent to the genus-two quotient

There exists

\[
\boxed{
\bar\xi_k
\in
K_2(C_{abc,k})\otimes\mathbf Q
}
\]

such that

\[
\boxed{
\pi_k^*\bar\xi_k=\xi_k.
}
\]

One may take

\[
\boxed{
\bar\xi_k
=\frac1{4}(\pi_k)_*\xi_k.
}
\]

### Proof

The subgroup `H_abc` has order `4` and consists of the even sign changes. Since each single sign change acts by `-1`, every element of `H_abc` acts trivially on `xi_k`.

For a finite quotient morphism, pullback after transfer satisfies

\[
\pi_k^*(\pi_k)_*\xi_k
=
\sum_{h\in H_{abc}}h^*\xi_k.
\]

The right side is `4 xi_k`. Dividing by `4` over `Q` gives the result. QED.

This strengthens the earlier differential-form descent:

\[
\boxed{
\text{the selected genus-two regulator is represented by an actual rational }K_2\text{ class,}
}
\]

not merely by a real one-form with the correct symmetry.

---

## Corollary H15.88 — regulator descent is motivic, not only formal

Let

\[
r_C:K_2(C)\otimes\mathbf Q\to H^1(C(\mathbf C),\mathbf R)^-
\]

be the real Beilinson/Bloch regulator on the curve. Then

\[
r_{C_k}(\xi_k)
=
\pi_k^*r_{C_{abc,k}}(\bar\xi_k).
\]

At the differential-form level this is exactly the previously obtained

\[
\pi_k^*\bar\eta_k=\eta(z,w).
\]

Therefore any Deninger/regulator period produced by the natural symbol factors through the genus-two quotient at the level of the underlying `K_2` class itself.

This still does not identify the period with a specific `L`-value; it establishes the correct motivic home for such an identity.

---

## 3. Galois orbit of the primitive regulator classes

Let

\[
F_p=\mathbf Q(\zeta_p+\zeta_p^{-1}),
\qquad
\Gamma_p=\operatorname{Gal}(F_p/\mathbf Q)
\cong(\mathbf Z/p\mathbf Z)^\times/\{\pm1\}.
\]

For `u in (Z/pZ)^x`, let `sigma_u` denote the real-cyclotomic automorphism

\[
\sigma_u(\vartheta_k)=\vartheta_{uk}.
\]

Because `z,w,mu` are fixed and only the cyclotomic coefficient is conjugated,

\[
\boxed{
\sigma_u(D_k)=D_{uk}.
}
\]

Hence `sigma_u` sends the mirror curve, its multiquadratic quotient data, and the natural symbol to the corresponding conjugate channel.

## Theorem H15.89 — Galois covariance of the selected motivic regulator class

For every `u in (Z/pZ)^x`,

\[
\boxed{
\sigma_u(C_{abc,k})=C_{abc,uk},
}
\]

and

\[
\boxed{
\sigma_u(\bar\xi_k)=\bar\xi_{uk}.
}
\]

Consequently their real regulator classes form a single Galois orbit:

\[
\boxed{
\sigma_u\bigl(r(\bar\xi_k)\bigr)
=r(\bar\xi_{uk})
}
\]

in the natural semilinear sense after identifying the conjugate cohomology spaces.

### Proof

The equations defining `Q_k`, the three radicals, and the genus-two quotient are polynomial/rational expressions in `vartheta_k` with rational coefficients and `mu`. Applying `sigma_u` therefore replaces every occurrence of `vartheta_k` by `vartheta_{uk}`.

The torus coordinate functions `z,w` are unchanged as formal functions, so the Milnor symbol `{z,w}` is carried to the identical symbol on the conjugate curve. Transfer and pullback commute with base-field automorphisms, hence the descended class is carried to `bar xi_{uk}`. Regulator functoriality gives the final statement. QED.

---

## Corollary H15.90 — an individual primitive motivic sheet retains the signless world coordinate

Fix a labelled mirror channel `k!=0`. In a prime world, an object reaction `a in F_p^x` replaces the channel coefficient by

\[
\vartheta_{ak}
=2\cos\frac{2\pi ak}{p}.
\]

For two nonzero reactions `a,b`,

\[
\vartheta_{ak}=\vartheta_{bk}
\iff
ak\equiv\pm bk\pmod p
\iff
\boxed{a\equiv\pm b\pmod p}.
\]

Therefore the **labelled primitive spectral curve together with its descended K2 class** determines the reaction coordinate up to the unavoidable dihedral reflection:

\[
\boxed{
(C_{abc,ak},\bar\xi_{ak})
\quad\text{retains}\quad
\{a,-a\}.
}
\]

By contrast, the full rational cyclotomic norm multiplies over the complete Galois orbit and is invariant under the permutation

\[
[k]\mapsto[ak].
\]

Hence

\[
\boxed{
\text{individual primitive regulator sheet}
\succ
\text{full norm/Mahler observer}
}
\]

at the algebraic-motivic information level.

This is the precise positive answer to the observer-resolution question that the full determinant could not answer: **the finer information survives before Galois-orbit multiplication, and is erased by the norm step itself.**

---

## 4. Scalar Mahler/regulator periods: what is proved and what is not

The theorem above concerns the algebraic curve and the `K_2` regulator class. A stronger scalar statement would be:

\[
\boxed{
\text{the numerical Mahler/regulator period itself separates the Galois-conjugate channels.}
}
\]

That is not automatic: distinct Galois-conjugate motivic classes can in principle produce coincident real periods under a particular cycle.

For `lambda=0` (`mu=4`) the block determinant is positive on the physical torus for every nontrivial real-cyclotomic channel. Indeed, with `theta=vartheta_k` and `X,Y in[-2,2]`,

\[
D_\theta
=X^2-4\theta X+\theta^2+12-Y^2>0
\]

for every `|theta|<2` occurring at a nontrivial root-of-unity channel. Thus the scalar logarithmic Mahler integral has no branch ambiguity.

After the `w`-circle Jensen reduction,

\[
\boxed{
m(D_\theta)
=\frac1{2\pi}\int_0^{2\pi}
\operatorname{arcosh}\left(
\frac{A_\theta(t)-2}{2}
\right)dt,
}
\]

where

\[
A_\theta(t)
=(2\cos t)^2-4\theta(2\cos t)+\theta^2+12.
\]

The symmetry `t -> pi-t` gives

\[
\boxed{m(D_\theta)=m(D_{-\theta}),}
\]

so a scalar real Mahler observer can never distinguish the reflection pair, exactly as predicted by the real mirror-channel analysis.

### Numerical witness: `p=5`, `lambda=0`

The two real mirror embeddings are

\[
\vartheta_1=\frac{\sqrt5-1}{2}
\approx0.618033988749895,
\]

\[
\vartheta_2=-\frac{\sqrt5+1}{2}
\approx-1.618033988749895.
\]

High-resolution quadrature of the exact one-dimensional Jensen integral gives

\[
\boxed{
m(D_{\vartheta_1})\approx2.464770092778702,}
\]

\[
\boxed{
m(D_{\vartheta_2})\approx2.414943773393007.}
\]

The difference is approximately

\[
\boxed{0.049826319385695.}
\]

This is strong numerical evidence that an individual scalar Mahler period can distinguish different signless Galois channels. It is **not yet promoted to a theorem**; an exact monotonicity/separation argument or an exact `L`-value identification is still required.

For comparison, the same experiment gives distinct channel values for `p=7`:

\[
2.443054889728918,
\quad
2.467621006544297,
\quad
2.390601550442258
\]

for the three mirror embeddings.

---

## 5. Relation to classical Mahler/regulator theory

The use of tempered face polynomials, tame symbols and curve `K_2` is standard in the Mahler-measure literature. Classical work of Rodriguez-Villegas, Boyd, Deninger and later regulator treatments use precisely this bridge from a tempered Laurent polynomial to the symbol `{x,y}` in the tame kernel and then to real regulator periods.

Likewise, pushforward/pullback of `K_2` classes on higher-genus curves is established machinery and has been used to explain Mahler-measure identities for genus-two and genus-three curves.

The H15-specific candidate is therefore not `tempered => K2` by itself. It is the exact composition

\[
\boxed{
\text{dihedral mirror block}
\to
\text{uniform diamond temperedness}
\to
\chi_{abc}\text{-pure }K_2\text{ class}
\to
\text{motivic descent to a selected genus-two quotient}
\to
\text{Galois orbit of primitive regulator sheets}
\to
\text{information loss only at the full norm step}.
}
\]

No novelty priority is asserted until a dedicated hostile literature audit of this full composition is complete.

---

## 6. Updated H15 observer hierarchy

The world-reaction hierarchy can now be refined to include the motivic level:

\[
\boxed{
\begin{array}{c|c}
\text{observer} & \text{reaction information retained}\\
\hline
\text{oriented complex Fourier sheet} & a\\
\text{labelled real mirror block} & \{\pm a\}\\
\text{labelled primitive }(C_{abc},\bar\xi)\text{ regulator sheet} & \{\pm a\}\\
\text{full rational spectral norm, prime }p & \mathbf1_{a\ne0}\\
\text{full invariant spectrum, odd composite }n & \gcd(a,n)
\end{array}}
\]

Thus the regulator layer does not automatically restore orientation, but it does preserve the signless channel label that the norm erases.

---

## 7. Next serious attack

The boundary obstruction is now closed. The next unresolved point is genuinely arithmetic/analytic rather than formal:

\[
\boxed{
\text{prove that the scalar primitive regulator period separates Galois channels,}
}
\]

or identify an exact obstruction forcing coincidences.

Two routes are now natural:

1. prove monotonicity/injectivity of the Jensen period `m(D_theta)` as a function of `|theta|` on the nontrivial cyclotomic range;
2. identify `r(bar xi_k)` with special values of the Hasse--Weil/automorphic `L`-function of the selected genus-two Jacobian and use the Galois-conjugate `L`-data to prove channel separation.

The first route is analytically local and may close quickly. The second is deeper and is the route most likely to reveal genuinely new arithmetic structure.
