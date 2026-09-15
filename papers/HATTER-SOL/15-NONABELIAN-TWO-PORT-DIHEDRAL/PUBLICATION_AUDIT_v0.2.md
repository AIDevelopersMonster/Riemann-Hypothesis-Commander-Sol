# HATTER-SOL-15 · Publication Audit v0.2

**Scope:** `MANUSCRIPT_EN_v0.1.md`, `MANUSCRIPT_RU_v0.1.md`, audited theorem layer H15.137–H15.139, exact certificate, and selected bibliography.

## Verdict

The mathematical core remains publication-ready after the hostile proof audit, but the v0.1 manuscripts are **not** the files to release. They contain publication-layer defects that do not alter the theorem but must be corrected before PDF/Zenodo assembly.

The release manuscript should be rebuilt as v0.2 with synchronized RU/EN structure and theorem numbering, using the audited v1.1 proof only.

## 1. Mandatory mathematical/textual corrections

1. **Broken LaTeX token in both language drafts.**
   The near-boundary tail line contains `\rac{2}{15\sqrt{15}}`; it must be
   `\frac{2}{15\sqrt{15}}`.

2. **Proof endings.**
   Literal backticked `square` markers must be replaced by a normal proof ending, preferably `\(\square\)` in the Markdown source or the standard LaTeX proof environment in the PDF source.

3. **Notation inside mathematics.**
   Raw prose-like tokens such as `a in V`, `a ne 0`, `F_p`, `chi mod p`, `mu>=4`, `lambda<=0` are acceptable in research notes but not in the final manuscript. They should be normalized to
   `a\in V`, `a\neq0`, `\mathbb F_p`, `\chi\pmod p`, `\mu\ge4`, `\lambda\le0`.

4. **Tail estimate language.**
   The audited proof gives a **one-sided lower bound** on the high-`m` tail. The final text must not describe it as an absolute-value bound.

5. **Far-region geometric-series estimate.**
   Only the repaired audited estimate may appear:
   \[
   \sum_{m\ge8}\frac{y^m}{m^2}<\frac1{15}y^8,
   \qquad 0<y\le\frac{400}{441}.
   \]
   The earlier stronger but incorrect estimate must not appear anywhere in publication files.

6. **All-prime statement at `p=3`.**
   The theorem is nontrivial for `p\ge5`; for `p=3`, the centered signless reaction space is zero-dimensional. State this explicitly.

7. **Causal language.**
   Keep the audited wording: the commutator identity and length-four holonomy organize the construction, but the paper must not claim that every later analytic identity is caused solely by `[R,S]=R^2`.

## 2. RU/EN structural synchronization

The publication versions should have identical section and theorem numbering:

1. Dihedral two-port setup and commutator.
2. Topological/Fourier signatures of noncommutativity.
3. Object-dependent curvature and arithmetic worlds.
4. What the unlabelled invariant spectrum forgets.
5. Primitive Mahler observer.
6. Mahler–Dirichlet–Gauss transform and Gram spectrum.
7. Universal first-harmonic dominance.
8. All-prime linear tomography.
9. Secondary motivic/regulator branch.
10. Interpretation: observer hierarchy and non-Abelian information.
11. Prior art and claim boundary.
12. Conclusion.

Appendices:

A. Exact certificate and reproducibility.
B. Proof dependency map.

The internal theorem-source crosswalk and release checklist should be moved out of the publication PDF into a separate supplement/reproducibility note.

## 3. Theorem numbering for both languages

Use the same publication numbering in EN and RU:

- Theorem 3.1 — square curvature is twice the world coordinate.
- Corollary 3.2 — flatness/splitting equivalence.
- Theorem 3.3 — projective curvature tomography.
- Proposition 4.1 — prime spectral blindness of the unlabelled full operator.
- Theorem 5.1 — positive Mahler harmonic expansion.
- Theorem 6.1 — Mahler–Dirichlet–Gauss bridge.
- Theorem 7.1 — universal first-harmonic dominance.
- Theorem 8.1 — nonvanishing of every nontrivial even character mode.
- Corollary 8.2 — full linear reaction tomography for every odd prime world.

Internal H15.73–H15.139 labels may be retained only in the supplement/crosswalk, not in the main narrative.

## 4. Equation-number policy

The v0.1 drafts are readable but under-numbered for a publication candidate. The v0.2 files should number the identities that are reused later, in particular:

- dihedral commutator `[R,S]=R^2`;
- primitive determinant `D_{\alpha,\mu}`;
- autocorrelation expansion;
- positive harmonic expansion;
- Gauss-transform identity;
- definition of `E_m`;
- Legendre reduction `E_m=c_ms^{-2m}Q_m(x)`;
- high-`m` tail estimate;
- near-boundary lower bound;
- far-region tail estimate;
- universal first-harmonic dominance;
- all-prime nonvanishing theorem.

EN and RU must use the same equation numbers.

## 5. Main-text versus supplement decision

### Keep in the main paper

- non-Abelian port setup;
- topology/Fourier interpretation;
- arithmetic-world curvature tomography, but only at the level needed to establish the observer hierarchy;
- full-spectrum orbit-collapse control result;
- primitive Mahler construction;
- Gram/character transform;
- complete audited proof of universal dominance;
- all-prime tomography consequence;
- concise motivic branch as an independent consistency/interpretation layer;
- prior-art/claim-boundary section;
- compact certificate appendix and proof-dependency map.

### Move to supplement/repository only

- prime-by-prime low-prime certificate history (`p=5,7,11,...,43`);
- automatic search architecture details;
- internal H15 theorem-layer crosswalk;
- publication/release checklist;
- raw hostile-audit transcript;
- exploratory numerical reconnaissance.

This keeps the paper focused on the uniform theorem rather than its discovery history.

## 6. Bibliography verification

The following entries were checked against publisher/arXiv records and should be used in v0.2.

1. D. W. Boyd, “Mahler's Measure and Special Values of L-functions,” *Experimental Mathematics* **7**(1) (1998), 37–82. DOI: `10.1080/10586458.1998.10504357`.
2. F. Rodriguez Villegas, “Identities between Mahler measures,” arXiv:`math/0612670` (2006).
3. M. N. Lalín, “Mahler measures and computations with regulators,” *Journal of Number Theory* **128**(5) (2008), 1231–1271. DOI: `10.1016/j.jnt.2007.03.002`.
4. M. Lalín and G. Wu, “Regulator proofs for Boyd's identities on genus 2 curves,” *International Journal of Number Theory* **15**(5) (2019), 945–967. DOI: `10.1142/S1793042119500519`.
5. C. Deninger, “Mahler measures and Fuglede–Kadison determinants,” *Münster Journal of Mathematics* **2** (2009), 45–64. arXiv:`0905.0604`.
6. C. J. Smyth, “The Mahler measure of algebraic numbers: a survey,” in *Number Theory and Polynomials*, London Mathematical Society Lecture Note Series, Cambridge University Press (2008), 322–349. DOI: `10.1017/CBO9780511721274.021`.
7. H. Davenport, *Multiplicative Number Theory*, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics **74**, Springer, 2000.
8. G. Cornelissen, D. Hokken and B. Ringeling, “The asymptotic Mahler measure of Gaussian periods,” *Proceedings of the London Mathematical Society* **133**(2) (2026), e70198. DOI: `10.1112/plms.70198`.

Bibliographic note: one Münster institutional index displays pages 45–63, while the journal/ULB record gives 45–64. Use the journal pagination 45–64 and retain arXiv:0905.0604 as an unambiguous locator.

## 7. Publication-safe claim language

Allowed:

> For the dihedral primitive mirror-block Mahler family considered here, we prove a uniform first-harmonic dominance inequality on `\mu\ge4`. Combined with a Gauss-sum transform, this yields nonvanishing of every nontrivial even Dirichlet-character response mode for every odd prime. We did not identify this exact statement in the literature searched.

Do not write:

- “first ever”;
- “unprecedented”;
- “completely new theory”;
- any claim that finite Fourier transforms, Gauss sums, Mahler/regulator methods, or Legendre identities are new.

## 8. Riemann-hypothesis boundary

The repository context contains Riemann-hypothesis research, but HATTER-SOL-15 does **not** prove the Riemann hypothesis and the publication package must say so explicitly. The result concerns a dihedral non-Abelian port model, its primitive Mahler response, and a uniform finite-character tomography theorem.

## 9. Release gate

After the corrections above, the paper may proceed to PDF/Zenodo assembly if the following are completed:

- synchronized RU/EN v0.2 manuscripts;
- independent execution of the audited exact certificate;
- checksum of the certificate used for the release;
- final visual PDF review;
- final DOI/bibliography pass;
- archive of the hostile proof audit and prior-art audit in the repository.

**Audit conclusion:** proceed to publication assembly from v0.2; do not release v0.1.
