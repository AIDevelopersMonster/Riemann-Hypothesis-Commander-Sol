# HATTER-SOL-15 · Mahler–Dirichlet–Gauss Bridge and Eventual Full Tomography

**Status:** exact theorem layer for prime dihedral worlds.  
**Purpose:** attack the remaining blind-mode question from `MAHLER_RESPONSE_ORBIT_CODE_AND_MULTIPLICATIVE_PARSEVAL.md` by expressing the multiplicative Mahler Fourier coefficients explicitly through additive Mahler harmonics and Gauss sums.

The main results are:

1. the primitive Mahler profile has a strictly positive additive cosine spectrum;
2. every even Dirichlet-character mode is an exact Gauss-sum transform of that positive harmonic spectrum;
3. for each fixed odd prime `p`, every nontrivial even character mode is nonzero for all sufficiently large `mu`;
4. hence the centered Mahler response operator is eventually invertible on the full zero-sum reaction space.

This does not yet prove nonvanishing all the way down to the boundary value `mu=4`; it converts that remaining question into one explicit twisted positive-series problem.

---

## 1. Positive additive harmonic expansion of the primitive Mahler profile

Continue with

\[
M_\mu(\alpha)
=2L_\mu
-\sum_{m\ge1}
\frac1m\binom{2m}{m}
R_{m,\mu}(2\alpha),
\]

where

\[
f_{m,\mu}(t)=(\mu-2\cos t)^{-m}
\]

and

\[
R_{m,\mu}(\delta)
=\frac1{2\pi}\int_0^{2\pi}
f_{m,\mu}(t)f_{m,\mu}(t+\delta)dt.
\]

Let the Fourier expansion of `f_{m,mu}` be

\[
f_{m,\mu}(t)
=\sum_{n\in\mathbf Z}a_{m,n}(\mu)e^{int}.
\]

Since `f_{m,mu}` is real and even,

\[
a_{m,-n}=a_{m,n}\in\mathbf R.
\]

Moreover all these coefficients are strictly positive.

One way to see this is to set

\[
r_\mu:=\frac{\mu-\sqrt{\mu^2-4}}2\in(0,1)
\]

and use the Poisson-kernel expansion

\[
\frac1{\mu-2\cos t}
=\frac1{\sqrt{\mu^2-4}}
\sum_{n\in\mathbf Z}r_\mu^{|n|}e^{int}.
\]

Taking the `m`-th power convolves strictly positive coefficient sequences, hence

\[
\boxed{a_{m,n}(\mu)>0.}
\]

The autocorrelation therefore has the exact Fourier expansion

\[
R_{m,\mu}(\delta)
=\sum_{n\in\mathbf Z}a_{m,n}(\mu)^2e^{in\delta}
=a_{m,0}^2+2\sum_{n\ge1}a_{m,n}^2\cos(n\delta).
\]

Substitution gives:

## Theorem H15.104 — strictly positive additive Mahler harmonic spectrum

For every `mu>=4`,

\[
\boxed{
M_\mu(\alpha)
=C_\mu-
\sum_{n\ge1}B_{\mu,n}\cos(2n\alpha),
}
\]

where

\[
\boxed{
B_{\mu,n}
=2\sum_{m\ge1}
\frac1m\binom{2m}{m}
a_{m,n}(\mu)^2
>0.
}
\]

The series converges absolutely and exponentially in `n` for fixed `mu>2`.

Thus the primitive Mahler profile has no missing additive harmonics: every frequency `2n` occurs with a strictly positive coefficient.

---

## 2. Restriction to prime mirror channels

Let `p` be an odd prime and

\[
G_p=\mathbf F_p^\times/\{\pm1\}.
\]

For a mirror class `[k]`, put

\[
\alpha_k=\frac{2\pi k}{p},
\qquad
f_\mu([k])=M_\mu(\alpha_k).
\]

Let `chi` be a nontrivial even Dirichlet character modulo `p`, so

\[
\chi(-1)=1.
\]

We identify `chi` with a character of `G_p`.

Define the Mahler multiplicative Fourier coefficient

\[
\widehat f_\mu(\chi)
=\sum_{[k]\in G_p}f_\mu([k])\overline{\chi(k)}.
\]

The constant term in H15.104 vanishes against a nontrivial character.

Since the quotient sum is half the sum over all nonzero residues,

\[
\widehat f_\mu(\chi)
=-\frac12
\sum_{n\ge1}B_{\mu,n}
\sum_{k=1}^{p-1}
\cos\frac{4\pi nk}{p}
\overline{\chi(k)}.
\]

For an even character, the cosine Gauss sum equals the full exponential Gauss sum. With

\[
\tau(\overline\chi)
:=\sum_{k=1}^{p-1}
\overline{\chi(k)}e^{2\pi ik/p},
\]

one has, for `p not dividing n`,

\[
\sum_{k=1}^{p-1}
\overline{\chi(k)}e^{4\pi ink/p}
=
\chi(2n)\tau(\overline\chi),
\]

while the sum is zero when `p|n` because `chi` is nontrivial.

Therefore:

## Theorem H15.105 — exact Mahler–Dirichlet–Gauss bridge

For every nontrivial even character `chi mod p`,

\[
\boxed{
\widehat f_\mu(\chi)
=-\frac12\,	au(\overline\chi)\,\chi(2)
\sum_{\substack{n\ge1\\p\nmid n}}
B_{\mu,n}\chi(n).
}
\]

Since `chi` is primitive modulo the prime `p`,

\[
|\tau(\chi)|=\sqrt p.
\]

Hence the Mahler Gram eigenvalue from the previous theorem layer is

\[
\boxed{
\Lambda_\chi
=|\widehat f_\mu(\chi)|^2
=\frac p4
\left|
\sum_{\substack{n\ge1\\p\nmid n}}
B_{\mu,n}\chi(n)
\right|^2.
}
\]

Thus the possible blind directions are exactly the zeros of an explicit multiplicative twist of the strictly positive additive Mahler spectrum.

This is much sharper than the abstract criterion `hat f_mu(chi) ne 0`.

---

## 3. The first holonomy harmonic dominates asymptotically

The large-`mu` behavior can be extracted directly from the torus determinant.

Write

\[
\vartheta=2\cos\alpha,
\qquad
X=2\cos t,
\qquad
Y=2\cos\phi.
\]

Then

\[
D_{\alpha,\mu}
=\mu^2\left(
1-\frac{X\vartheta}{\mu}
+\frac{X^2+\vartheta^2-Y^2-4}{\mu^2}
\right).
\]

Expanding `log D` in powers of `mu^{-1}` and averaging over both torus angles gives

\[
\boxed{
M_\mu(\alpha)
=2\log\mu
-\frac4{\mu^2}
-\frac{14}{\mu^4}
-\frac4{\mu^4}\cos(2\alpha)
+O(\mu^{-6}),
}
\]

uniformly in `alpha`.

The crucial point is structural: the first channel-dependent term occurs at order `mu^{-4}` and is exactly the first additive harmonic.

Equivalently,

\[
\boxed{
B_{\mu,1}=4\mu^{-4}+O(\mu^{-6}),
}
\]

while

\[
\boxed{
B_{\mu,n}=O(\mu^{-6})
\quad(n\ge2)
}
\]

in the aggregate sense needed below; more precisely the sum of all higher harmonics is `O(mu^{-6})`.

This is the analytic shadow of the earlier square-holonomy theorem: the first genuinely non-Abelian closed-walk contribution appears at length four.

---

## Theorem H15.106 — asymptotic nonvanishing of every even character mode

Fix an odd prime `p` and a nontrivial even Dirichlet character `chi mod p`.

Then, as `mu -> +infinity`,

\[
\boxed{
\widehat f_\mu(\chi)
=-2\mu^{-4}\tau(\overline\chi)\chi(2)
+O_p(\mu^{-6}).
}
\]

In particular,

\[
\boxed{
\widehat f_\mu(\chi)\ne0
}
\]

for all sufficiently large `mu`.

### Proof

In H15.105, the `n=1` term contributes

\[
-\frac12\tau(\overline\chi)\chi(2)B_{\mu,1}
=-2\mu^{-4}\tau(\overline\chi)\chi(2)+O(\mu^{-6}).
\]

The total contribution of `n>=2` is `O_p(mu^{-6})` by the uniform large-`mu` expansion. Since a Gauss sum never vanishes, the leading coefficient is nonzero. QED.

---

## Corollary H15.107 — eventual full linear Mahler tomography

For every fixed odd prime `p`, there exists a finite threshold

\[
\boxed{\mu_0(p)\ge4}
\]

such that for every

\[
\mu>\mu_0(p)
\]

and every nontrivial even character `chi mod p`,

\[
\boxed{
\widehat f_\mu(\chi)\ne0.
}
\]

Hence the centered Mahler response operator is invertible on the entire zero-sum reaction space:

\[
\boxed{
\text{full primitive Mahler ensemble}
\Longleftrightarrow
\text{full zero-sum signless reaction signal}
}
\]

for sufficiently negative spectral parameter

\[
\lambda=4-\mu.
\]

This is the first genuine full-tomography theorem for the continuous Mahler observer.

It is stronger than orbit injectivity: arbitrary zero-sum superpositions of reaction states can be reconstructed linearly mode by mode.

---

## 4. What remains at the physical boundary `mu=4`

The large-`mu` theorem does **not** prove that no character mode crosses zero as `mu` decreases toward `4`.

The exact obstruction is now the explicit twisted series

\[
\boxed{
S_{p,\chi}(\mu)
:=
\sum_{\substack{n\ge1\\p\nmid n}}
B_{\mu,n}\chi(n).
}
\]

Every coefficient `B_{mu,n}` is strictly positive, but for a nontrivial character the phases `chi(n)` can cancel.

Thus the physical-boundary problem has been reduced to:

\[
\boxed{
S_{p,\chi}(4)\stackrel{?}{\ne}0
\quad\text{for every nontrivial even }\chi.
}
\]

A proof of a first-harmonic dominance bound

\[
B_{\mu,1}
>
\sum_{n\ge2}B_{\mu,n}
\]

would immediately imply nonvanishing for every character, by the triangle inequality. Numerical experiments strongly suggest this inequality at `mu=4`, but no theorem is claimed here.

A weaker route is to prove nonvanishing of each finite character twist directly.

---

## 5. New bridge to Dirichlet arithmetic

The earlier H15 double-Fourier heuristic

\[
\text{additive mirror channel}
\to
\text{multiplicative Dirichlet character}
\]

is now exact at the Mahler level.

The sequence

\[
B_{\mu,n}>0
\]

is the additive spectral content of the primitive Mahler observer, while the multiplicative reaction-space eigenmodes are obtained by twisting that sequence with even Dirichlet characters and multiplying by the Gauss factor.

Thus:

\[
\boxed{
\text{Mahler additive harmonics}
\xrightarrow{\text{Gauss transform}}
\text{Dirichlet-character Mahler modes}.
}
\]

This is a more precise arithmetic mechanism than simply observing that both cyclotomic fields and Dirichlet characters occur in the same construction.

---

## 6. Claim boundary

The following ingredients are classical:

- Poisson-kernel Fourier expansions;
- positivity under convolution;
- Gauss-sum evaluation of additive Fourier transforms of Dirichlet characters;
- diagonalization of group-circulant matrices;
- asymptotic logarithmic determinant expansions.

The H15-specific candidate is the exact chain

\[
\boxed{
\text{non-Abelian primitive Mahler profile}
\to
\text{strictly positive additive harmonic spectrum}
\to
\text{Gauss transform}
\to
\text{even Dirichlet-character response modes}
\to
\text{eventual full linear tomography}.
}
\]

No novelty priority is asserted before a publication-stage hostile literature audit.

---

## 7. Next attack

The next narrow target is now unambiguous:

\[
\boxed{
B_{4,1}
\stackrel{?}{>}
\sum_{n\ge2}B_{4,n}.
}
\]

If true, it closes all Mahler blind modes at the physical laboratory value `lambda=0` in one stroke.

If false, the fallback target is character-by-character nonvanishing of

\[
S_{p,\chi}(4).
\]

Either result will sharply determine whether the `lambda=0` primitive Mahler ensemble is a complete linear observer or has genuine arithmetic blind directions.
