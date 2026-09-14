# HATTER-SOL-15 · Spectral Observer Orbit Collapse and Divisor Strata

**Status:** exact theorem layer.  
**Input:** `WORLD_REACTION_CURVATURE_TOMOGRAPHY.md`, `NONABELIAN_FLOQUET_PAIRING.md`, `CYCLOTOMIC_NORM_SPECTRAL_CURVE.md`.  
**Question:** does the heavy spectral/Mahler observer preserve the finer world coordinate

\[
\alpha\in\mathbf F_p,
\]

or does it collapse to the same coarse information as the flat/curved commutator observer?

The answer is exact:

- in a prime dihedral world, the **full basis-invariant spectrum, determinant, spectral curve and full Mahler measure see only `alpha=0` versus `alpha!=0`**;
- a labelled real mirror channel sees `alpha` up to sign;
- an oriented complex channel sees `alpha` exactly;
- in odd composite dihedral worlds, the full spectral observer becomes richer and detects the divisor stratum `gcd(alpha,n)`, equivalently the order of the rotation response.

This closes the observer-resolution question at the determinant/Mahler level.

---

## 1. Object-dependent two-port spectral operator

Let

\[
D_{2n}=\langle R,S\mid R^n=S^2=1,\ SRS^{-1}=R^{-1}\rangle,
\]

with `n` odd, acting on the Schreier set `Z/nZ` by

\[
R(x)=x+1,
\qquad
S(x)=-x.
\]

For a world-reaction coordinate

\[
a\in\mathbf Z/n\mathbf Z,
\]

replace the horizontal rotation port by

\[
R^a.
\]

The square-lattice connection Laplacian symbol is

\[
L_a(z,w)
=4I-zR^a-z^{-1}R^{-a}-(w+w^{-1})S.
\]

For spectral parameter `lambda`, put

\[
\mu=4-\lambda,
\qquad
X=z+z^{-1},
\qquad
Y=w+w^{-1}.
\]

We study

\[
P_{n,a}(z,w,\lambda)
:=\det(L_a(z,w)-\lambda I).
\]

---

## Theorem H15.79 — unit rescaling is simultaneous port conjugacy

For every unit

\[
u\in(\mathbf Z/n\mathbf Z)^\times,
\]

let `U_u` be the permutation operator induced by

\[
x\mapsto ux.
\]

Then

\[
\boxed{
U_u R^a U_u^{-1}=R^{ua},
\qquad
U_u S U_u^{-1}=S.
}
\]

Consequently

\[
\boxed{
U_u L_a(z,w)U_u^{-1}=L_{ua}(z,w)
}
\]

for every `z,w`, and therefore

\[
\boxed{
P_{n,a}=P_{n,ua}.
}
\]

More strongly, the complete matrix-valued Bloch spectra are identical pointwise in `(z,w)`.

### Proof

Conjugating the translation `x -> x+a` by `x -> ux` gives `x -> x+ua`. Since multiplication by `u` commutes with negation,

\[
u(-x)=-ux,
\]

so the reflection is fixed. The operator identity follows term by term. QED.

### Corollary H15.80 — the full invariant spectral observer sees unit orbits

Two residues `a,b mod n` lie in the same orbit under multiplication by units iff

\[
\boxed{\gcd(a,n)=\gcd(b,n).}
\]

Hence the full spectrum, determinant and any basis-invariant spectral functional depend on `a` at most through

\[
\boxed{d=\gcd(a,n).}
\]

Equivalently they depend at most on the order

\[
\boxed{q=\operatorname{ord}(R^a)=\frac{n}{d}.}
\]

Thus the natural invariant spectral observer forgets the coordinate inside each arithmetic unit orbit.

---

## 2. Prime-world collapse

Now let `n=p` be an odd prime.

There are only two unit orbits in `F_p`:

\[
\{0\}
\qquad\text{and}\qquad
\mathbf F_p^\times.
\]

Therefore:

## Theorem H15.81 — exact prime spectral blindness theorem

For every two nonzero world coordinates

\[
a,b\in\mathbf F_p^\times,
\]

\[
\boxed{
L_a(z,w)\sim L_b(z,w)
}
\]

by a fixed permutation conjugacy independent of `(z,w,lambda)`. Hence

\[
\boxed{
P_{p,a}(z,w,\lambda)
=P_{p,b}(z,w,\lambda).
}
\]

Consequently all of the following are identical for every `a!=0`:

1. the unordered Bloch band spectrum;
2. the full characteristic polynomial;
3. the full complex spectral variety;
4. the cyclotomic-norm polynomial;
5. the logarithmic Mahler measure of the full determinant;
6. every basis-invariant trace/spectral moment built from the same operator.

Thus the heavy invariant spectral observer sees exactly the same binary partition as the coarse curvature observer:

\[
\boxed{
a=0\quad\text{versus}\quad a\ne0.}
\]

This is a genuine **no-gain theorem** for the full invariant spectrum: moving from the commutator trace to the complete determinant does not reveal the nonzero Frobenius coordinate in a prime dihedral world.

---

## 3. Why labelled channels were finer

Let

\[
\omega=e^{2\pi i/p}
\]

and use the Fourier basis `e_k`. Then

\[
R^a e_k=\omega^{ak}e_k,
\qquad
S e_k=e_{-k}.
\]

A fixed labelled mirror block `k <-> -k` depends on

\[
\vartheta_{ak}
=\omega^{ak}+\omega^{-ak}
=2\cos\frac{2\pi ak}{p}.
\]

Therefore a labelled real block sees `a` up to sign, while the oriented line `e_k` sees the phase `omega^{ak}` and hence `a` exactly.

But multiplication by a nonzero `a` merely permutes the mirror labels:

\[
[k]\longmapsto[ak].
\]

The full determinant multiplies over all those labels, so the permutation disappears.

Thus there is no contradiction between the observer ladder and H15.81:

\[
\boxed{
\text{oriented complex sheet}
\succ
\text{labelled real mirror sheet}
\succ
\text{unlabelled full spectral norm}.
}
\]

The loss of information occurs exactly when the observer quotients by the frequency-channel permutation symmetry.

---

## 4. Exact determinant for an arbitrary odd composite world

Let now `n` be any odd positive integer and let

\[
d=\gcd(a,n),
\qquad
q=\frac nd.
\]

For `q>1`, put

\[
\xi_q=e^{2\pi i/q},
\qquad
\vartheta_{q,j}=\xi_q^j+\xi_q^{-j}
=2\cos\frac{2\pi j}{q}.
\]

Define

\[
D_{q,j}(\mu;X,Y)
:=
\vartheta_{q,j}^2
-\mu X\vartheta_{q,j}
+\mu^2+X^2-Y^2-4,
\]

and

\[
N_q(\mu;X,Y)
:=
\prod_{j=1}^{(q-1)/2}D_{q,j}(\mu;X,Y),
\]

with `N_1:=1`.

Also define the zero-frequency factors

\[
S_-(\mu;X,Y):=\mu-X-Y,
\]

\[
D_0(\mu;X,Y)
:=(\mu-X)^2-Y^2
=S_-(\mu;X,Y)(\mu-X+Y).
\]

## Theorem H15.82 — divisor-stratum determinant factorization

For every odd `n` and every reaction coordinate `a`,

\[
\boxed{
P_{n,a}
=
S_-
\,D_0^{(d-1)/2}
\,N_q^{\,d},
\qquad
q=n/d.
}
\]

### Proof

In the Fourier basis indexed by `k mod n`, the horizontal phase is

\[
e^{2\pi i ak/n}.
\]

Write `a=d a'` with `(a',q)=1`. As `k` ranges modulo `n`, the residue `a'k mod q` takes each value modulo `q` exactly `d` times.

The value `0 mod q` occurs for `d` Fourier labels. One of them is `k=0`, giving the scalar factor `S_-`; the remaining `d-1` labels form `(d-1)/2` mirror pairs and each contributes `D_0`.

Every nonzero mirror pair `[j]` modulo `q` has exactly `d` preimage mirror pairs modulo `n`, each contributing the same block determinant `D_{q,j}`. Multiplying all blocks gives the formula. QED.

### Interpretation

The full spectral determinant detects the order `q` of the reaction rotation, not its exact exponent:

\[
\boxed{
a\longmapsto q=\operatorname{ord}(R^a).}
\]

For prime `p`, this reduces to only `q=1` or `q=p`. For composite `n`, intermediate divisor strata become spectrally visible.

---

## 5. Primitive cyclotomic layer factorization

For odd `e>1`, let

\[
F_e=\mathbf Q(\zeta_e+\zeta_e^{-1})
\]

and let

\[
\theta_e=\zeta_e+\zeta_e^{-1}.
\]

Define the primitive real-cyclotomic determinant

\[
\mathcal N_e(\mu;X,Y)
:=
N_{F_e/\mathbf Q}
\left(
\theta_e^2-\mu X\theta_e+\mu^2+X^2-Y^2-4
\right).
\]

The nonzero `q`-frequency mirror labels split according to the exact order of `xi_q^j`. Therefore:

## Theorem H15.83 — primitive divisor decomposition of the spectral norm

\[
\boxed{
N_q(\mu;X,Y)
=
\prod_{\substack{e\mid q\\e>1}}
\mathcal N_e(\mu;X,Y).
}
\]

Hence

\[
\boxed{
P_{n,a}
=
S_-\,D_0^{(d-1)/2}
\prod_{\substack{e\mid q\\e>1}}
\mathcal N_e^{\,d}.
}
\]

For prime `q=p`, there is only one nontrivial divisor and this reduces exactly to the previously proved maximal-real-cyclotomic norm formula.

For composite `q`, the full spectral observer is therefore not governed by one real cyclotomic field but by all primitive real-cyclotomic layers whose conductors divide the reaction order.

---

## Corollary H15.84 — Mahler measure respects the divisor-layer decomposition

Let `m(P)` denote the logarithmic two-variable Mahler measure in `(z,w)` for fixed spectral parameter `lambda` whenever the integral is defined in the usual sense. Since

\[
m(PQ)=m(P)+m(Q),
\]

H15.82--83 give the exact identity

\[
\boxed{
\begin{aligned}
m(P_{n,a})
={}&m(S_-)
+\frac{d-1}{2}m(D_0)\\
&+d\sum_{\substack{e\mid q\\e>1}}
m(\mathcal N_e).
\end{aligned}}
}
\]

Thus at the **full determinant / full Mahler-measure level**, the primitive divisor layers do not create mysterious nonlinear cross-terms: they factor multiplicatively before the logarithm and add after it.

This answers one of the active H15 questions:

\[
\boxed{
\text{divisor-world structure survives the full spectral/Mahler observer as an exact factorization.}
}
\]

The possible genuinely new nonlinear arithmetic can only enter at a finer level — for example through the regulator class on an individual primitive spectral curve, its Deninger cycle, boundary/tame-symbol conditions, or interactions introduced by a different observer that does not simply take the full determinant product.

---

## 6. Consequence for the `p=3` genus-two motive

In the prime laboratory `p=3`, every nonzero reaction coordinate is related by a unit rescaling. Therefore the full determinant is identical for all curved worlds/reactions.

Hence the previously isolated simple genus-two curve

\[
C:y^2=x(x-4)(x^2+5)(x^2+9)
\]

and its absolutely-simple Jacobian belong to the **nonzero/curved spectral phase**, not to a finer distinction between the two nonzero coordinates.

In particular, the natural full Mahler observer cannot distinguish `a=1` from `a=-1`; this is forced before any regulator calculation by the simultaneous port conjugacy.

For larger prime `p`, the individual mirror-block curves are permuted through the real cyclotomic Galois orbit as `a` changes, while their full norm product remains fixed.

So the correct interpretation is:

\[
\boxed{
\text{individual labelled spectral sheets carry signless coordinate data,}
}
\]

but

\[
\boxed{
\text{the full rational spectral norm intentionally forgets that labelling.}
}
\]

---

## 7. Observer hierarchy after the spectral attack

The H15 world-reaction ladder is now exact at four levels:

\[
\boxed{
\begin{array}{c|c}
\text{observer} & \text{reaction information retained}\\
\hline
\text{oriented complex Fourier sheet} & a\\
\text{labelled real mirror block} & \{\pm a\}\\
\text{full invariant spectrum, prime }p & \mathbf 1_{a\ne0}\\
\text{full invariant spectrum, odd composite }n & \gcd(a,n)\ \text{or }\operatorname{ord}(R^a)
\end{array}}
\]

This is a precise example of **observer-dependent structural memory**: more mathematically elaborate does not automatically mean more informative. The decisive issue is which symmetry quotient the observer takes.

---

## 8. Claim boundary

The following ingredients are classical:

- simultaneous conjugacy under automorphisms of a cyclic group;
- Fourier block diagonalization;
- cyclotomic factorization by exact root order;
- multiplicativity of Mahler measure over products.

The H15-specific candidate is the synthesis inside the non-Abelian world-reaction architecture:

\[
\boxed{
\text{object reaction }a
\to
(R^a,S)
\to
\text{dihedral commutator curvature}
\to
\text{observer-resolution hierarchy}
\to
\text{prime orbit collapse / composite divisor strata}
\to
\text{primitive cyclotomic spectral factors}.
}
\]

No novelty priority is asserted before hostile prior-art review.

---

## 9. Next serious target

The determinant/Mahler question is now structurally settled: the full invariant observer cannot recover more than the unit-orbit/divisor stratum.

The next attack should therefore move one level finer and ask:

\[
\boxed{
\text{Does the regulator/Deninger-cycle observer on an individual primitive factor }
\mathcal N_e
\text{ preserve information that the full norm erases?}
}
\]

For prime `p`, this means comparing Galois-conjugate mirror-block regulator classes before multiplying them into the rational norm. A positive result would identify a genuinely finer observer; a negative result would prove that the arithmetic regulator also collapses to the same world orbit.
