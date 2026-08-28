# Hostile Audit — Threshold Spectrum Rigidity

**Branch:** `research/threshold-spectrum-rigidity`  
**Date:** 2026-08-28  
**Target:** `FULL_PROOF.md`  
**Verdict:** PASS for the stated theorems, with one terminology correction retained below.

## 1. Audit protocol

The proof was attacked at the following pressure points:

1. whether fixed source primes are really parameter-free definable;
2. whether target `1` is genuinely definable without already having target scalar transport;
3. whether negative-valuation probes smuggle in a division operation not present in the language;
4. whether exact threshold sentences distinguish `kappa(l)=m` for `m=0` as well as `m>0`;
5. whether complete-theory rigidity is being confused with internal uniform reconstruction;
6. whether continuum-many theories follows in a countable language;
7. whether the many-one lower bound is effective;
8. whether the unanchored gauge-classification theorem overlooks source prime permutations;
9. whether finite-support interdefinability from the preceding paper contradicts theory inequivalence here;
10. whether any theorem relies on the residual Galois machinery from the Support-Cardinality Wall.

Each item is checked below.

---

## 2. Fixed-prime definability

The formula

\[
\Theta_\ell(r):=
\operatorname{Prime}(r)
\land
\exists x\,
(\neg B(r,x)\land B(r,\ell x))
\]

uses only the fixed target term `ell*x`, i.e. repeated addition.

For `r != ell`, `ell` is an `r`-adic unit, so

\[
v_r(\ell x)=v_r(x)
\]

and threshold crossing is impossible.

For `r=ell`, the witness

\[
x=\ell^{\kappa(\ell)-1}
\]

exists in `Q`; when `kappa(ell)=0` this is simply `1/ell`.

No target constant `ell`, source-target comparison, or variable scalar multiplication is used.

**Verdict:** PASS.

---

## 3. Target-unit calibration from `u_2`

The exact bridge computation is

\[
\tau(2)=-24,
\qquad
u_2=\frac{576-2048}{2048}=-\frac{23}{32}.
\]

Once source prime `2` is defined by `Theta_2`, the bridge gives the unique target `x=u_2`. The formula

\[
23z+32x=0
\]

has the unique solution `z=1` in the additive group of rationals.

The uniqueness argument uses only torsion-freeness: if `23z=23`, then `23(z-1)=0`, hence `z=1`.

No inverse scalar symbol is used in the formula itself.

**Verdict:** PASS.

The earlier two-prime Bezout calibration was redundant but not needed for the final proof.

---

## 4. Fixed rational probes

Once target `1` is definable, a fixed rational `a/b` is defined by one fixed linear equation

\[
bx=a\cdot1
\]

or its sign-adjusted equivalent. Since `a,b` are fixed metamathematical integers, this is a legitimate first-order formula in the additive-group language.

Existence follows because the actual target is `Q`; uniqueness follows from torsion-freeness. The proof does not assert that divisibility is first-order axiomatized abstractly in every model of the theory; it only constructs formulas in the standard structure family under study.

For negative valuation probes, `ell^{-s}` is therefore a fixed rational definable by a fixed equation such as

\[
\ell^s x=1.
\]

**Verdict:** PASS.

---

## 5. Exact coordinate sentence at depth zero

For `m=0`, the sentence uses probes with valuations `0` and `-1`. It asserts

\[
B_\kappa(\ell,1)
\land
\neg B_\kappa(\ell,\ell^{-1}).
\]

This is equivalent to

\[
0\ge\kappa(\ell)
\quad\land\quad
-1<\kappa(\ell).
\]

Because the profile codomain is `N_0`, this holds exactly when `kappa(ell)=0`.

No edge case remains.

**Verdict:** PASS.

---

## 6. Complete theory versus uniform internal reconstruction

The proof establishes an external countable family of parameter-free sentences

\[
\Sigma_{\ell,m}
\]

indexed by fixed standard pairs `(ell,m)`.

It does **not** construct a single formula whose variables range simultaneously over a source prime and a depth code. Thus it proves pointwise recoverability from the complete theory, not an internally definable function

\[
r\mapsto\kappa(r).
\]

The distinction is explicit in `FULL_PROOF.md`.

**Verdict:** PASS.

---

## 7. Threshold Spectrum Rigidity

If `kappa != lambda`, choose a standard prime `ell` where they differ and let `m=kappa(ell)`. Then

\[
\Sigma_{\ell,m}
\]

is true in the `kappa` structure and false in the `lambda` structure.

This is a direct complete-theory separator in the common literal language.

Conversely, identical profiles give literally identical standard structures.

Hence

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
=
\operatorname{Th}(\mathcal V_{\Delta,\lambda})
\iff
\kappa=\lambda.
\]

**Verdict:** PASS.

---

## 8. Continuum spectrum

Restrict to profiles taking values in `{1,2}` at every prime. There are

\[
2^{\aleph_0}
\]

such profiles. Rigidity makes their complete theories pairwise distinct.

The common first-order language is countable, so the set of all sentences is countable and the set of all complete theories has cardinality at most

\[
2^{\aleph_0}.
\]

Thus the cardinality is exactly continuum.

All these profiles have positive support equal to the full prime set, so the previously published wall puts them in the same amplifying phase.

**Verdict:** PASS.

---

## 9. Effective lower bound

Fix a computable enumeration of the standard primes. For the `{1,2}` coding profile `kappa_A`, membership

\[
i\in A
\]

is equivalent to truth of the effectively constructible sentence

\[
\Sigma_{p_i,1}.
\]

Given `i`, one can compute the ordinary prime `p_i`, then mechanically print the finite repeated-addition terms required by `Theta_{p_i}` and the fixed rational probes.

Therefore the many-one reduction

\[
A\le_m\operatorname{Th}(\mathcal V_{\Delta,\kappa_A})
\]

is valid.

No upper bound on the Turing degree is claimed.

**Verdict:** PASS.

---

## 10. Unanchored gauge classification

This is the most vulnerable new theorem.

Any automorphism of `(Q,+)` is multiplication by a unique nonzero rational `c`.

Let an isomorphism send source prime `p` to source prime `q`. Preservation of `B` gives equality of subgroups

\[
H_{p,\kappa(p)}
=
H_{q,\lambda(q)-v_q(c)}.
\]

For distinct primes `p != q`, these subgroups cannot be equal. A concrete separating witness is

\[
x=p^{\kappa(p)}q^{\lambda(q)-v_q(c)-1},
\]

which has exactly the required valuations, even when the exponents are negative because `x` is allowed to be rational.

Therefore `q=p`. Every source prime is fixed, hence every source positive integer is fixed by unique factorization.

For the same prime, threshold subgroups form a strict chain, so equality forces

\[
\lambda(p)=\kappa(p)+v_p(c).
\]

A rational `c` has finite valuation support, proving necessity of finite profile difference.

Conversely, if profiles differ on finitely many primes, the rational

\[
c=\prod_p p^{\lambda(p)-\kappa(p)}
\]

is well-defined and multiplication by `c` gives the required target isomorphism.

**Verdict:** PASS.

---

## 11. Bridge gauge fixing

In the anchored structure, `Theta_2` parameter-free defines source prime `2`, hence every automorphism fixes it. Bridge preservation fixes its unique label

\[
u_2=-23/32\ne0.
\]

A target scaling `x -> cx` compatible with this label must satisfy

\[
cu_2=u_2,
\]

hence `c=1`.

Thus the bridge destroys the full rational-scaling gauge responsible for finite-shift isomorphisms in the unanchored structure.

**Verdict:** PASS.

---

## 12. No contradiction with finite-support interdefinability

The preceding Support-Cardinality Wall result says finite-support profiles are parameter-free **interdefinable** with `B_0`.

The present result says different profiles have different complete theories in the same literal language where the predicate symbol `B` is interpreted differently.

These statements are compatible. Definitional equivalence/interdefinability need not imply equality of the original complete theories before translation of predicate symbols.

**Verdict:** PASS.

---

## 13. Independence from residual Galois machinery

Threshold Spectrum Rigidity itself uses only:

- the threshold predicate;
- fixed additive scalar terms;
- one explicit nonzero bridge value `u_2`;
- elementary properties of `(Q,+)`.

No Chebotarev theorem, residual representation, open-image theorem, or GIR construction is used in the proof of rigidity.

The published Support-Cardinality Wall is invoked only to say that the continuum family with full positive support lies in the same previously established amplifying phase.

**Verdict:** PASS.

---

## 14. Counterexample search

The following attempted counterexamples fail for explicit reasons.

### Attempt A: shift one threshold and compensate by target scaling

Without the bridge this works. With the bridge, scaling changes `u_2`, so bridge preservation forces scale `1`.

### Attempt B: permute source primes while simultaneously scaling target

A single rational scaling changes valuations at fixed named places; it cannot convert one `p`-threshold subgroup into a different `q`-threshold subgroup. The subgroup-separation lemma forces source primes to remain fixed.

### Attempt C: exploit threshold `0`

The exact decoder uses the `-1` probe, so zero depth is still separated.

### Attempt D: choose a noncomputable profile

Rigidity is semantic and does not require the profile to be computable. Only Proposition 9.1 discusses effective coding, and there the subset itself is allowed to be arbitrary while the reduction map is computable.

### Attempt E: recover only the support, not the depth

The adjacent probes `m` and `m-1` distinguish the exact threshold integer, so profiles with the same support and different positive depths are separated.

No counterexample survives.

---

## 15. Terminology correction

The initial checkpoint was prematurely titled `Theorem Checkpoint` before a full proof file existed. Under the project's strengthened publication rule, its historical status should be read as **candidate theorem checkpoint**.

The theorem status is justified only now, by `FULL_PROOF.md` plus this hostile audit.

No publication is authorized by this audit alone; literature and claim audits remain required if this result is to be released as a separate paper.

---

## 16. Final verdict

The following statements have complete proofs and survived hostile audit:

- Pointwise Threshold Recovery;
- Threshold Spectrum Rigidity;
- continuum many complete theories at fixed full support and threshold alphabet `{1,2}`;
- arbitrary-set many-one information lower bound;
- Abstract Threshold Calibration under a definable target scale;
- unanchored finite-shift gauge classification up to isomorphism;
- bridge gauge fixing.

**HOSTILE AUDIT: PASS.**

The branch is not mathematically exhausted, because uniform internal profile reconstruction remains genuinely open. That problem should be continued as a separate theorem candidate rather than folded into the proved rigidity theorem.