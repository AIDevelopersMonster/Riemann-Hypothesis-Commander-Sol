# HATTER-SOL-15 · Generic Full Mahler Tomography and Exceptional Spectral Parameters

**Status:** exact theorem layer for each fixed odd prime `p`.  
**Input:** `MAHLER_RESPONSE_ORBIT_CODE_AND_MULTIPLICATIVE_PARSEVAL.md` and `MAHLER_DIRICHLET_GAUSS_BRIDGE_AND_EVENTUAL_FULL_TOMOGRAPHY.md`.  
**Purpose:** determine how large the blind-mode set can be as the spectral parameter varies.

The answer is sharp at the qualitative level: for every fixed prime world, failure of full Mahler tomography can occur only at a discrete exceptional set of spectral parameters. In particular, on every compact interval in `mu>2` there are only finitely many bad values.

---

## 1. Character-channel response functions

Fix an odd prime `p` and write

\[
G_p=\mathbf F_p^\times/\{\pm1\}.
\]

For each nontrivial even Dirichlet character `chi mod p`, let

\[
F_{p,\chi}(\mu)
:=\widehat f_\mu(\chi),
\qquad \mu>2.
\]

Here `f_mu` is the centered primitive Mahler profile on the real mirror classes, and from the previous theorem layer

\[
F_{p,\chi}(\mu)
=-\frac12\tau(\overline\chi)\chi(2)
\sum_{\substack{n\ge1\\p\nmid n}}
B_{\mu,n}\chi(n).
\]

The Mahler Gram eigenvalue in character direction `chi` is

\[
\Lambda_{p,\chi}(\mu)
=|F_{p,\chi}(\mu)|^2.
\]

Full centered linear tomography holds exactly when every nontrivial `F_{p,chi}(mu)` is nonzero.

---

## Theorem H15.108 — real-analytic dependence on the spectral parameter

For every fixed odd prime `p` and every nontrivial even character `chi mod p`,

\[
\boxed{
F_{p,\chi}(\mu)
}
\]

is real-analytic on

\[
\boxed{\mu>2.}
\]

Equivalently, the corresponding Gram eigenvalue is real-analytic as a nonnegative real function.

### Proof

For `mu>2`, the kernel

\[
(\mu-2\cos t)^{-m}
\]

is real-analytic in `mu` uniformly on compact `mu`-intervals and uniformly in `t`. Its Fourier coefficients are therefore real-analytic. The absolutely convergent positive-harmonic expansion for `B_{mu,n}` is locally uniform in `mu`, hence termwise differentiation is valid to all orders on compact subsets of `(2,infinity)`.

The character twist is an absolutely convergent locally uniform series of those analytic coefficients. Therefore `F_{p,chi}` is real-analytic. QED.

---

## Theorem H15.109 — no character channel is identically blind

For every fixed `p` and every nontrivial even `chi`,

\[
\boxed{
F_{p,\chi}\not\equiv0.
}
\]

### Proof

The large-`mu` theorem already gives

\[
F_{p,\chi}(\mu)
=-2\mu^{-4}\tau(\overline\chi)\chi(2)
+O_p(\mu^{-6}).
\]

The leading coefficient is nonzero because Gauss sums do not vanish. Therefore `F_{p,chi}` cannot be identically zero. QED.

This rules out a structural arithmetic direction that is invisible for every spectral parameter.

---

## Theorem H15.110 — exceptional parameters are discrete

Define the blind set of a character channel by

\[
\mathcal E_{p,\chi}
:=\{\mu>2:F_{p,\chi}(\mu)=0\}.
\]

Then

\[
\boxed{
\mathcal E_{p,\chi}
\text{ is discrete in }(2,\infty).
}
\]

Consequently, for every compact interval

\[
[a,b]\subset(2,\infty),
\]

the set

\[
\mathcal E_{p,\chi}\cap[a,b]
\]

is finite.

### Proof

A nonzero real-analytic function on an interval has isolated zeros. Compactness then gives finiteness on compact subintervals. QED.

---

## Corollary H15.111 — generic full Mahler tomography

Let

\[
\mathcal E_p
:=
\bigcup_{\substack{\chi\ne1\\\chi(-1)=1}}
\mathcal E_{p,\chi}.
\]

Because there are only finitely many even characters modulo `p`,

\[
\boxed{
\mathcal E_p
\text{ is a discrete subset of }(2,\infty).
}
\]

For every

\[
\mu\in(2,\infty)\setminus\mathcal E_p,
\]

the centered primitive Mahler response operator is invertible on the full zero-sum reaction space.

Hence:

\[
\boxed{
\text{full linear Mahler tomography holds for generic spectral parameter }\mu.
}
\]

In particular, it holds on an open dense subset of every compact interval in `(2,infinity)`.

Since the exceptional set is discrete, it has Lebesgue measure zero and no accumulation point inside `(2,infinity)`.

---

## 2. Determinant form of the tomography obstruction

Let `A_{p,mu}` be the centered Mahler response matrix indexed by reactions and labelled mirror channels. Its restriction to the zero-sum subspace has character eigenvalues `F_{p,chi}(mu)` up to the Fourier normalization convention.

Define the reduced tomography determinant

\[
\boxed{
\Delta_p(\mu)
:=
\prod_{\substack{\chi\ne1\\\chi(-1)=1}}
F_{p,\chi}(\mu).
}
\]

Complex-conjugate character factors occur in conjugate pairs, so after a harmless constant normalization one may regard the reduced determinant as a real-analytic real-valued function.

## Theorem H15.112 — one analytic discriminant controls all blind modes

\[
\boxed{
\Delta_p(\mu)=0
\iff
\text{the centered Mahler observer has a nontrivial blind direction at }\mu.
}
\]

Moreover,

\[
\boxed{
\Delta_p\not\equiv0.
}
\]

Hence the complete tomography failure locus is the zero set of one nonzero real-analytic function.

This packages all character-by-character obstructions into one spectral discriminant.

---

## 3. Exact low-prime closure

The first prime worlds can be closed without any asymptotic argument.

### Theorem H15.113 — `p=5` has no blind parameter for `mu>=4`

For `p=5`,

\[
|G_5|=2.
\]

There is exactly one nontrivial character direction. After centering, the response profile is proportional to

\[
(f_\mu(x_1)-f_\mu(x_2),\;f_\mu(x_2)-f_\mu(x_1)).
\]

Strict primitive Mahler channel separation gives

\[
f_\mu(x_1)\ne f_\mu(x_2)
\]

for every `mu>=4`. Therefore

\[
\boxed{
\mathcal E_5\cap[4,\infty)=\varnothing.
}
\]

So `p=5` has full linear tomography throughout the entire nonnegative spectral half-line `lambda<=0`.

### Theorem H15.114 — `p=7` has no blind parameter for `mu>=4`

For `p=7`,

\[
|G_7|=3.
\]

Let the three centered primitive values be `x,y,z` with

\[
x+y+z=0.
\]

A nontrivial Fourier coefficient is

\[
x+y\omega+z\omega^2,
\qquad
\omega=e^{2\pi i/3}.
\]

If it vanished, its real and imaginary parts would force

\[
x=y=z.
\]

But strict primitive channel separation gives three distinct uncentered values, hence the centered values cannot all agree.

Therefore every nontrivial character channel is nonzero for every `mu>=4`, and

\[
\boxed{
\mathcal E_7\cap[4,\infty)=\varnothing.
}
\]

Thus `p=7` also has full linear Mahler tomography throughout `lambda<=0`.

### Remarks

For larger `p`, injectivity of the scalar profile alone no longer rules out a vanishing multiplicative Fourier coefficient: there are enough coordinates for nontrivial linear cancellations. The character-twist problem becomes genuinely arithmetic from `p=11` onward.

---

## 4. Stability away from the exceptional set

Let

\[
\sigma_{\min}(p,\mu)
:=
\min_{\chi\ne1}|F_{p,\chi}(\mu)|.
\]

Whenever `mu notin E_p`, this is positive.

## Corollary H15.115 — local conditioning theorem

If

\[
\mu_0\notin\mathcal E_p,
\]

then there is an open interval `I` containing `mu_0` and a constant `c>0` such that

\[
\boxed{
|F_{p,\chi}(\mu)|\ge c
}
\]

for every nontrivial even `chi` and every `mu in I`.

Hence the inverse Mahler tomography operator is uniformly bounded on `I`.

So reconstructibility is not a pointwise fragile phenomenon: it persists under small changes of spectral parameter until an exceptional zero is crossed.

---

## 5. World interpretation

The result has a direct HATTER meaning.

For one fixed prime dihedral world, changing `mu` changes the spectral observer while leaving the underlying non-Abelian port algebra fixed.

The theorem says:

\[
\boxed{
\text{the same world is fully visible to almost every observer setting,}
}
\]

and loss of one arithmetic reaction mode can occur only at isolated tuned observer settings.

Thus blind modes, if they exist, are not a permanent property of the object/world pair. They are **observer resonances**.

This distinction is important:

\[
\boxed{
\text{structural invisibility}
\ne
\text{spectral-parameter cancellation}.
}
\]

H15.109 rules out the first for every even character direction. H15.110 says only the second can remain.

---

## 6. Relation to `lambda=0`

The principal laboratory value is

\[
\lambda=0,
\qquad
\mu=4.
\]

The present theorem does not yet prove that `4 notin E_p` for every prime `p`. It proves instead:

1. `p=5` and `p=7` are completely closed at `mu=4` and for all `mu>=4`;
2. for every fixed larger prime, any failure at `mu=4` would be an isolated exceptional cancellation, not a structural blind mode;
3. sufficiently large `mu` is always outside the exceptional set.

Thus the remaining universal boundary question is now very narrow:

\[
\boxed{
4\stackrel{?}{\notin}\mathcal E_p
\quad\text{for every odd prime }p.
}
\]

The first-harmonic dominance criterion remains a sufficient uniform route, but it is no longer the only route.

---

## 7. Claim boundary

The zero-set theorem for nonzero real-analytic functions and continuity of singular values are classical analysis.

The H15-specific content is the identification of the Mahler blind-mode problem with finitely many explicit real-analytic Dirichlet-character channels generated by the non-Abelian mirror observer, together with the conclusion that full reaction tomography is generic and that failures are isolated observer resonances.

No novelty priority is asserted before a publication-stage literature audit.

---

## 8. Next attack

There are now two complementary routes:

1. **uniform route:** prove first-harmonic dominance at `mu=4`, closing every prime simultaneously;
2. **arithmetic route:** attack the finite twisted sums `F_{p,chi}(4)` directly, beginning with `p=11,13,17`, and look for a structural noncancellation theorem weaker than global first-harmonic dominance.

The arithmetic route is now especially attractive because any counterexample would be a mathematically meaningful isolated Mahler-observer resonance rather than a failure of the whole H15 architecture.
