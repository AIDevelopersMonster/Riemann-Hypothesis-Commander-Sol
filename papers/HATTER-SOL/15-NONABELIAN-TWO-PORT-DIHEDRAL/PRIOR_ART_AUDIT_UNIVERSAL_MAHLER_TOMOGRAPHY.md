# HATTER-SOL-15 · Prior-Art Audit for Universal Mahler Tomography

**Status:** targeted hostile literature audit after proof repair.  
**Target theorem:** H15.137–H15.139 in `UNIVERSAL_FIRST_HARMONIC_DOMINANCE_AND_ALL_PRIME_TOMOGRAPHY.md`.  
**Scope:** determine whether the exact inequality

\[
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4)
\]

or its all-prime Dirichlet-character tomography consequence appears already in the literature, and identify the closest known components.

This audit is deliberately conservative. It does **not** assert novelty priority. It records what was found and what was not found in a targeted search.

---

## 1. Search targets

The audit searched combinations of the following themes:

- Mahler measure + Fourier coefficients;
- first-harmonic dominance;
- autocorrelation expansions of Mahler families;
- Dirichlet characters + Mahler measure + Gauss sums;
- cyclotomic/Galois Mahler transforms;
- Mahler measure + regulators + genus-2 curves;
- Toeplitz/Fuglede–Kadison determinant connections;
- asymptotic Mahler measure of Gaussian periods;
- lower bounds and coefficient inequalities for Mahler measure.

The exact H15 object is unusual: a one-parameter primitive mirror-block Mahler profile arising from a dihedral noncommuting port pair, followed by multiplicative Fourier analysis on

\[
\mathbf F_p^\times/\{\pm1\}.
\]

No search hit matching this whole package was found.

---

## 2. Closest prior-art families

### A. Mahler measure, regulators, and higher-genus curves

A substantial literature studies Mahler measures of genus-2 and genus-3 curves, often via regulator maps and `K_2` classes.

Representative items found include:

- works on Mahler measure of families of polynomials defining genus-2 and genus-3 curves;
- regulator proofs for Boyd-type identities;
- hyperelliptic Mahler families;
- Mahler measures and computations with regulators;
- Deninger/Rodriguez-Villegas style regulator formulas.

These sources strongly overlap with the **motivic/regulator** side of H15, especially the earlier layers involving temperedness, `K_2`, quotient curves, and genus-2 motives.

However, the search did not reveal the H15 first-harmonic dominance inequality or an all-character nonvanishing theorem of the same form.

### B. Dirichlet characters and Gauss transforms in Mahler formulas

The literature contains explicit Mahler-measure formulas transformed by finite Fourier analysis at roots of unity and rewritten in terms of Dirichlet `L`-values.

In particular, some classical and recent formulas use:

\[
\tau(\chi)
\]

and finite character sums of Bloch–Wigner dilogarithm values at roots of unity.

A recent 2026 paper on an exact family of bivariate polynomials explicitly recalls Gauss sums and rewrites Mahler measures through primitive Dirichlet characters and `L`-values.

Thus the general bridge

\[
\text{root-of-unity data}
\leftrightarrow
\text{Dirichlet-character transform}
\]

is classical and must not be presented as new.

What is H15-specific is the exact route

\[
\text{dihedral mirror Mahler harmonics}
\to
\text{positive }B_{\mu,n}
\to
\text{Gauss transform}
\to
\text{reaction-space Gram eigenvalues}
\]

and then the uniform first-harmonic domination sufficient to force all character modes nonzero.

### C. Mahler measure and Fourier/Toeplitz machinery

The literature around Szegő theory, Toeplitz determinants, and Fuglede–Kadison determinants connects Mahler measure with Fourier coefficients and determinant limits.

There are also classical coefficient bounds for one-variable polynomials and trigonometric polynomials in terms of Mahler measure.

These results are conceptually adjacent to the harmonic analysis used in H15, but they concern a different direction:

- they bound polynomial/Fourier coefficients using Mahler measure;
- H15 studies the Fourier expansion **of a Mahler-response profile itself** and proves domination of its first nonconstant harmonic over the total higher-harmonic tail.

No exact analogue was found in the targeted search.

### D. Gaussian periods and asymptotic Mahler measure

A 2026 paper on the asymptotic Mahler measure of Gaussian periods uses constant-term expansions and Bessel-function-type coefficient formulas.

This is relevant because it confirms current interest in cyclotomic/Gaussian-period Mahler asymptotics and harmonic decompositions.

The searched material does not appear to contain the H15 dihedral mirror-block theorem or its first-harmonic dominance statement.

---

## 3. Exact claim-by-claim priority assessment

The following components should be treated as **known/classical machinery**:

1. Jensen formulas for Mahler measure;
2. Mahler/regulator connections;
3. tempered Newton-face criterion and `K_2` use;
4. finite Fourier transforms at roots of unity;
5. Dirichlet characters and Gauss sums;
6. Legendre-polynomial integral formulas for powers of the resolvent kernel;
7. Fourier/Parseval identities;
8. Wallis/Beta integral estimates;
9. Toeplitz/Szegő and determinant viewpoints;
10. general Mahler coefficient inequalities.

The following statements were **not located** in the targeted search and therefore remain H15 candidate contributions, subject to broader expert review:

### Candidate H15-A

For the specific primitive dihedral Mahler profile,

\[
M_\mu(\alpha)
=C_\mu-
\sum_{n\ge1}B_{\mu,n}\cos(2n\alpha),
\qquad B_{\mu,n}>0,
\]

the universal inequality

\[
\boxed{
B_{\mu,1}>\sum_{n\ge2}B_{\mu,n}
\qquad(\mu\ge4).
}
\]

### Candidate H15-B

The resulting uniform character theorem:

\[
\boxed{
\widehat f_\mu(\chi)\ne0
}
\]

for every odd prime `p`, every nontrivial even Dirichlet character modulo `p`, and every `mu>=4`.

### Candidate H15-C

The interpretation of these character coefficients as Gram eigenvalues of the full primitive Mahler reaction orbit and hence as a full linear tomography theorem on

\[
\mathbf C[\mathbf F_p^\times/\{\pm1\}]_0.
\]

### Candidate H15-D

The exact synthesis

\[
\text{noncommuting dihedral ports}
\to
\text{commutator square response}
\to
\text{primitive mirror Mahler profile}
\to
\text{all-prime linear reaction tomography}.
\]

The synthesis, rather than any single classical ingredient, is the strongest plausible originality claim.

---

## 4. Important negative result of the audit

The search did **not** justify any claim of the form:

> “No one has ever proved anything comparable.”

That wording must not appear in the paper.

The Mahler-measure literature is large, and terminology varies substantially. The exact theorem may exist under a different parametrization or inside an analytic study of a related family.

Therefore publication wording should be:

> “We did not identify this exact first-harmonic dominance statement or the resulting all-prime reaction-tomography theorem in the literature searched.”

not:

> “This theorem is new.”

Priority should remain explicitly provisional until external specialist review.

---

## 5. Bibliographic anchors to include in publication assembly

At minimum the H15 paper should cite literature in the following categories:

### Mahler measure fundamentals and multivariable theory

- standard references on Mahler measure, Jensen formulas, and multivariable Mahler measure;
- a modern survey/book on variations of Mahler measures.

### Mahler measure and regulators

- Deninger-style regulator approach;
- Rodriguez-Villegas / Boyd identity literature;
- Lalín and collaborators on Mahler measures and regulators;
- genus-2/genus-3 Mahler measure papers.

### Dirichlet characters and roots-of-unity transforms

- a standard analytic number theory reference for Gauss sums and finite Fourier transforms of primitive Dirichlet characters;
- Mahler-measure papers explicitly translating roots-of-unity dilogarithm sums into Dirichlet `L`-values.

### Determinant/Fourier context

- Szegő/Toeplitz determinant references where relevant;
- Mahler measure and Fuglede–Kadison determinant literature.

### Recent context

- the 2026 Gaussian-period Mahler asymptotics paper as a current cyclotomic/Mahler comparison point.

---

## 6. Publication-safe novelty language

Recommended language for the abstract/introduction:

> We prove, for the dihedral primitive mirror-block Mahler family considered here, a uniform first-harmonic dominance inequality on `mu>=4`. Combined with a Gauss-sum transform, this yields nonvanishing of every nontrivial even Dirichlet-character response mode for every odd prime. We have not identified this exact statement in the Mahler-measure literature searched; the proof uses classical harmonic, Legendre, and Beta-integral tools in a specific non-Abelian port construction.

Recommended language to avoid:

- “first ever”;
- “completely new area”;
- “unprecedented theorem”;
- any implication that Gauss transforms of Mahler/root-of-unity data are themselves new.

---

## 7. Audit verdict

The targeted literature search found substantial prior art for the components but no exact match for the universal H15 dominance/tomography theorem.

Current internal classification:

\[
\boxed{
\text{plausibly publication-worthy synthesis; novelty priority unresolved.}
}
\]

This is sufficient to proceed to publication assembly, provided the final text:

1. cites the classical machinery explicitly;
2. separates proven H15-specific statements from known ingredients;
3. avoids unsupported priority claims;
4. includes the audited v1.1 proof and exact certificate;
5. preserves the caveat that external specialist review may uncover closer antecedents.
