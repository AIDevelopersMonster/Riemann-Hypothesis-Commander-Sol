# Claim and bibliography audit — Stationary Locality manuscript

**Date:** 2026-08-26  
**Status:** pre-layout audit

## 1. Main theorem scope

The manuscript proves a formula-relative result for structures

\[
\mathcal B_{u,S}=((\mathbb N_{>0},\times),(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U)
\]

with finite \(S\), under the stated Private-Place Bridge hypotheses.

The following claims are supported by the proof architecture in `FINITE_STATIONARY_LOCALITY_THEOREM.md` and the manuscripts:

- Multi-Place Finite-Depth Normal Form for the target sort.
- Generic Multi-Place Cell Lemma.
- Exact Linear Separation on the regular tail.
- Reduced Affine-Fiber / bounded-anchor cylinder structure.
- Fresh-Private-Place Avoidance.
- Pinned/Free Target-Witness Transport.
- Formula-Relative Tail Symmetry.
- Non-definability of the standard prime order.
- Non-definability of the standard prime-successor relation.
- Finite GIR for every fixed isolator formula.

## 2. Explicit non-claims

The manuscript must not be read as claiming any of the following:

- quantifier elimination or decidability for the full two-sorted theory;
- model-theoretic stability, NIP, simplicity, or NTP2;
- global automorphism homogeneity of the whole two-sorted structure;
- non-interpretability of all arithmetic;
- infinite GIR for the uniformly indexed atlas;
- definability of prime successor in any right-wall structure unless separately proved;
- any historical priority statement for the programme terminology.

These exclusions are stated explicitly in the manuscript.

## 3. Formula-relative versus global symmetry

The admissible partition and exceptional set depend on the formula. The theorem therefore asserts

\[
\forall\Phi\ \exists F_\Phi,\mathbf K_\Phi
\]

and not

\[
\exists F,\mathbf K\ \forall\Phi.
\]

This quantifier order must remain visible in the theorem statement and in every summary.

## 4. Parameters

The main theorem is stated parameter-free. A parameterized extension requires the exceptional set to depend on the finite parameter tuple through the finite set of anchored regular primes exposed by reduced affine traces.

Do not state a parameter-uniform exceptional set without a separate theorem.

## 5. Target normal form

The finite quotient used in the local coverage argument is

\[
B_{\ell,m}/B_{\ell,N},
\]

not \(\mathbb Q/B_{\ell,m}\). The latter is generally infinite.

Cross-place compatibility uses finite weak approximation / CRT after clearing denominators. The proof does not rely on the false assertion that a multi-place quotient of \(\mathbb Q\) is finite.

## 6. Exact affine fibers

The manuscript intentionally rejects the false bounded-tuple statement for affine equations. Zero-sum equality blocks may remain free and generate infinite cylinders.

The supported statement is:

- after fixing an equality pattern, zero aggregate blocks are free;
- assignments to non-zero aggregate blocks are uniformly bounded, up to finite coefficient-dependent exceptions;
- exact traces are finite unions of bounded-anchor cylinders.

## 7. Ramanujan application

For

\[
u_p=(\tau(p)^2-p^{11})/p^{11},
\]

the private place for a good prime \(p\ge5\) is \(\lambda(p)=p\).

If \(a=v_p(\tau(p))\), Deligne's bound gives \(a\le5\), hence

\[
v_p(u_p)=2a-11<0.
\]

For \(q\ne p\), \(u_q\) is \(p\)-integral.

If \(\tau(p)=0\), then \(u_p=-1\), giving one exact common-label defect class.

An infinite reservoir of good primes can be obtained without a density theorem: the classical congruence

\[
\tau(p)\equiv1+p^{11}\pmod{691}
\]

shows that every prime \(p\equiv1\pmod{691}\) is good, and Dirichlet's theorem gives infinitely many such primes.

The successor non-definability argument itself uses only the resulting infinite movable tail and does not require a density-zero theorem for zero primes.

## 8. Infinite named atlas

For the language with one predicate symbol \(B_\ell\) for every rational prime, every ordinary first-order formula uses only finitely many such symbols. Therefore the finite theorem applies formula-by-formula to the Ramanujan bridge.

This is a syntactic finite-support argument. It is not a theorem that an infinitary logic or a uniformly indexed valuation relation remains harmless.

## 9. Uniformly indexed atlas

The relation

\[
\mathsf B(\ell,x)\iff v_\ell(x)\ge0
\]

with \(\ell\) a first-order variable lies beyond the present theorem. It removes the finite named-support barrier. For rational \(x\), quantifying over all prime places can define the integer subring by requiring non-negative valuation at every prime.

No stronger conclusion is claimed in this paper.

## 10. GIR terminology

Grid-Isolation Rank is programme terminology. Finite GIR must not be identified with standard model-theoretic stability or NIP.

## 11. Classical references checked

- S. Ramanujan, `On certain arithmetical functions`, *Transactions of the Cambridge Philosophical Society* 22 (1916), 159–184. The bibliographic data are confirmed by Cambridge references and later historical notes.
- W. Szmielew, `Elementary properties of Abelian groups`, *Fundamenta Mathematicae* 41 (1955), 203–271, DOI 10.4064/fm-41-2-203-271.
- W. Baur, `Elimination of quantifiers for modules`, *Israel Journal of Mathematics* 25 (1976), 64–70, DOI 10.1007/BF02756561.
- E. R. Fisher, `Abelian structures. I`, in *Abelian Group Theory*, Lecture Notes in Mathematics 616, Springer (1977), 270–322.
- P. Deligne, `Formes modulaires et représentations ℓ-adiques`, Séminaire Bourbaki Exp. 355, Lecture Notes in Mathematics 179 (1971), 139–172.

The classical references are background. The manuscript's target normal form is proved directly and does not depend on quoting a complete off-the-shelf quantifier-elimination theorem for the exact multi-place structure used here.

## 12. Publication status

After this audit, the mathematical manuscript is ready for one final line-by-line proof reread and then layout/Zenodo packaging. No new mathematical claim should be added during layout without reopening this audit.
