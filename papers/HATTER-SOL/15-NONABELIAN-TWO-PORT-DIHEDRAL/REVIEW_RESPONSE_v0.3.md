# HATTER-SOL-15 · Response to Review and v0.3 Revision Gate

**Reviewed object:** HATTER-SOL-15 v0.2 publication candidate, 15 September 2026.  
**Decision:** accept the review as substantively useful; distinguish true publication issues from PDF/text-extraction artefacts; prepare v0.3 before Zenodo release.

---

## 1. Overall response

The review correctly identifies the central mathematical dependency of the paper: Theorem 7.1, the universal first-harmonic dominance inequality

\[
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n},\qquad \mu\ge4,
\]

is the publication-critical theorem. The paper should therefore make the proof and its finite certificate maximally reproducible and should remove every ambiguity that could prevent an independent reader from checking the argument.

The review also correctly asks for sharper separation between:

- the main analytic theorem;
- the observer/tomography interpretation;
- the secondary motivic/regulator branch.

However, several reported deficiencies are artefacts of extraction or of the reviewed rendering rather than defects of the underlying audited v0.2 source. These are documented below.

---

## 2. Resolution matrix

### R1. Code parameters in Theorem 3.3

**Review concern:** the extracted text appeared to show `p r - 1` and `2 p r - 2`.

**Status:** no mathematical correction needed; the manuscript source already uses

\[
\boxed{\operatorname{wt}=p^{r-1},\qquad d_{\min}=2p^{r-2}.}
\]

**v0.3 action:** add the counting proof explicitly to prevent extraction ambiguity:

\[
\#\{H:a\in H\}=\frac{p^{r-1}-1}{p-1},
\]

so the nonflat weight is

\[
\frac{p^r-1}{p-1}-\frac{p^{r-1}-1}{p-1}=p^{r-1},
\]

and for distinct projective classes the hyperplanes containing both have cardinality

\[
\frac{p^{r-2}-1}{p-1},
\]

giving distance `2p^{r-2}`.

---

### R2. Exact definition of `K_m`

**Review concern:** `K_m` looked damaged or ambiguous in the extracted text.

**Status:** already explicit in the audited source:

\[
\boxed{
K_m:=\frac{m}{4^m}\binom{2m}{m}I_{2m},
\qquad
I_{2m}:=\int_{-\infty}^{\infty}(1+u^2)^{-2m}\,du.
}
\]

**v0.3 action:** display this definition on its own numbered equation and immediately follow it by

\[
\boxed{
\frac{K_{m+1}}{K_m}=1-\frac1{16m^2}<1.
}
\]

This eliminates line-wrap ambiguity.

---

### R3. Complete certificate / all `H_m`

**Review concern:** only the first few polynomial numerators appeared in the reviewed extract.

**Status:** the audited publication source and certificate already contain all `H_m`, `m=2,...,7`, their denominators, the rational `beta_m`, the corrected far-tail series bound, and the endpoint comparison. The release package also contains a separate exact reproduction script and SHA-256 manifest.

**v0.3 action:** strengthen permanence rather than mathematics:

1. put all six polynomial numerators and denominators into Appendix A;
2. state the audited certificate filename;
3. state the release SHA-256 in the final manuscript/supplement;
4. archive an independent run transcript;
5. tag the exact release commit before Zenodo deposit.

---

### R4. Strict monotonicity of `M_mu(alpha)`

**Review concern:** positivity of the harmonic coefficients alone does not imply monotonicity; the claimed strict growth needs proof.

**Status:** fully agreed as a presentation criticism. A proof already exists in the theorem layer `PRIMITIVE_MAHLER_CHANNEL_SEPARATION.md` (H15.92–H15.93), but v0.2 only referred to a “separate autocorrelation argument.”

**v0.3 action:** import the proof into the paper.

For

\[
f(t)=(\mu-2\cos t)^{-m},
\]

`f` is positive, even, `2pi`-periodic, and strictly decreasing on `(0,pi)`. Its circular autocorrelation

\[
R(\delta)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)f(t+\delta)\,dt
\]

satisfies

\[
R'(\delta)=\frac1{2\pi}\int_0^\pi
\bigl(f(u-\delta)-f(u+\delta)\bigr)f'(u)\,du<0
\]

for `0<delta<pi`, because the first factor is positive and `f'(u)<0`. Hence every `R_{m,mu}(2alpha)` strictly decreases for `0<alpha<pi/2`; all weights in the Mahler autocorrelation expansion are positive, so

\[
\boxed{M_\mu'(\alpha)>0\quad(0<\alpha<\pi/2).}
\]

The symmetry `M_mu(pi-alpha)=M_mu(alpha)` follows from even circular autocorrelation.

This will become a numbered lemma/theorem in v0.3 rather than an unsupported sentence.

---

### R5. Gauss-transform normalization

**Review concern:** fix the exact conventions for `tau`, conjugation, Fourier transform, and Gram eigenvalues.

**Status:** accepted. The v0.2 formula is consistent with the convention used internally, but the paper should derive the factor `1/2` explicitly.

**v0.3 conventions:** for an even character `chi` modulo the odd prime `p`,

\[
\tau(\bar\chi)=\sum_{k=1}^{p-1}\bar\chi(k)e^{2\pi ik/p},
\]

and on the quotient

\[
\widehat f(\chi)=\sum_{[k]\in G_p}f([k])\bar\chi(k)
=\frac12\sum_{k=1}^{p-1}f(k)\bar\chi(k).
\]

Since

\[
\sum_{k=1}^{p-1}\bar\chi(k)e^{2\pi iak/p}
=\chi(a)\tau(\bar\chi),
\]

and `chi(-1)=1`,

\[
\sum_{k=1}^{p-1}\bar\chi(k)\cos\frac{4\pi nk}{p}
=\chi(2n)\tau(\bar\chi).
\]

Therefore

\[
\boxed{
\widehat f_\mu(\chi)
=-\frac12\tau(\bar\chi)\chi(2)
\sum_{\substack{n\ge1\\p\nmid n}}B_{\mu,n}\chi(n).
}
\]

For the Gram formula v0.3 will explicitly choose the unnormalised inner product

\[
\langle u,v\rangle=\sum_{x\in G_p}u(x)\overline{v(x)},
\]

under which

\[
\boxed{\Lambda_\chi=|\widehat f_\mu(\chi)|^2.}
\]

If a normalized inner product is preferred, the corresponding factor `1/|G_p|` will be stated rather than suppressed.

---

### R6. Cover assumptions in the genus formula

**Review concern:** the formula

\[
g=1+\frac{n-c(K)}2
\]

needs its topological hypotheses.

**Status:** accepted.

**v0.3 action:** state explicitly: connected, oriented, degree-`n`, one-point branched cover of a torus; local monodromy `K`; monodromy generated transitively by the chosen port pair. Then Riemann–Hurwitz / Euler characteristic gives the formula.

---

### R7. Definition of `D_{2p}`

**Review concern:** notation varies in the literature.

**v0.3 action:** add one sentence at first occurrence:

> Throughout, `D_{2p}` denotes the dihedral group of order `2p`.

---

### R8. Explicit constant term `C_mu`

**Review suggestion:** spell it out.

**Accepted.** From the autocorrelation expansion,

\[
\boxed{
C_\mu
=2L_\mu-
\sum_{m\ge1}\frac1m\binom{2m}{m}a_{m,0}(\mu)^2.
}
\]

This will be added immediately after the positive harmonic expansion.

---

### R9. Dimension of the centered reaction space

**Accepted.** Add

\[
\boxed{
\dim\mathbf C[G_p]_0
=\frac{p-3}{2}.
}
\]

This also makes the vacuous `p=3` case transparent.

---

### R10. 2026 Gaussian-period reference

**Review concern:** verify publication status.

**Status:** verified as a published article, not merely a future citation:

G. Cornelissen, D. Hokken, B. Ringeling, *The asymptotic Mahler measure of Gaussian periods*, *Proceedings of the London Mathematical Society* **133**(2) (2026), e70198, DOI `10.1112/plms.70198`; first published 25 August 2026.

No correction to status is needed; v0.3 will retain complete publication metadata.

---

## 3. Additional strengthening requested by the review

### 3.1. Stability margin

Define

\[
\Delta_\mu
:=B_{\mu,1}-\sum_{n\ge2}B_{\mu,n}>0.
\]

The current proof is pointwise-uniform in the sense `Delta_mu>0` for every `mu>=4`, but it does **not** imply a positive global constant

\[
\inf_{\mu\ge4}\Delta_\mu>0.
\]

Indeed `Delta_mu` decays as `mu->infinity`. Therefore the review's suggested bound

\[
\Delta_\mu\ge\Delta_*>0
\]

cannot hold on the whole half-line.

The correct quantitative strengthening is weighted/asymptotic. From the first harmonic expansion,

\[
\Delta_\mu=4\mu^{-4}+O(\mu^{-6}),
\]

so a meaningful global condition number should be scaled by `mu^4`, or restricted to a compact interval `4<=mu<=M`.

This is a useful correction to the review suggestion itself and will be discussed in the paper rather than asserted incorrectly.

### 3.2. Boundary `mu=4`

The boundary deserves an explicit paragraph. The primitive determinant remains strictly positive for `0<alpha<pi` even at `mu=4`, so the channel Mahler integral is finite. The global harmonic spectrum has slower, algebraic coefficient decay at the boundary; numerical exploration suggests `B_{4,n}~(2pi n^3)^{-1}`, but this asymptotic is **not** required for Theorem 7.1 and should not be promoted to theorem status without proof.

The v0.3 manuscript will distinguish this boundary regularity from the stronger `mu>4` exponential-decay regime.

### 3.3. Purely analytic replacement of the certificate

The review is correct that removing the finite certificate would strengthen the paper. This is an attractive post-publication research problem, but it is not required for reproducibility once the exact certificate and all finite inequalities are archived immutably.

The current release standard will therefore be:

\[
\boxed{\text{analytic infinite tail + finite exact rational certificate}.}
\]

No claim will be made that the proof is fully paper-and-pencil.

---

## 4. Motivic branch response

The review asks for sharper status labels. Agreed.

The v0.3 main manuscript will say explicitly:

- the universal tomography theorem is independent of the motivic branch;
- the genus/Jacobian/K2 assertions cited there are theorem-layer results under their stated genericity hypotheses;
- no Beilinson/Boyd-style regulator conjecture is used to prove Theorems 7.1 or 8.1;
- any heuristic interpretation will be labelled as interpretation rather than proof dependency.

The motivic material will remain concise and secondary.

---

## 5. Release decision after review

The review does **not** reveal a new mathematical defect in Theorem 7.1 or Theorem 8.1.

It does reveal a presentation/reproducibility gap that should be closed before Zenodo release: the strict monotonicity proof and transform conventions should be included directly in the final manuscript, and extraction-sensitive formulas should be made more explicit.

Therefore:

\[
\boxed{\text{v0.2 remains mathematically viable, but v0.3 is the release candidate.}}
\]

Zenodo release should wait for:

1. synchronized RU/EN v0.3;
2. imported strict-autocorrelation monotonicity proof;
3. explicit Gauss/Gram conventions;
4. explicit counting proof for the projective code parameters;
5. release hash/tag for the exact certificate and independent run transcript;
6. final PDF render audit.
