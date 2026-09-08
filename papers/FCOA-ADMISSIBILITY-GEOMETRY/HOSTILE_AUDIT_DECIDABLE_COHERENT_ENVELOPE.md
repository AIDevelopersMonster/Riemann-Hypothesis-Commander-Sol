# Hostile Audit — Decidable Coherent Envelope Phase Barrier

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Audited target:** `DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md`  
**Status:** hostile audit passed for the stated prefix-coherent / same-base / ordinary-FO scope

---

## 1. Audit target

The claimed barrier is

\[
\boxed{DCE+Add\Longrightarrow\neg Mul}
\]

for prefix-coherent families of finite structures on the ordered initial segments `[m]`.

The dangerous points are not the final undecidability contradiction itself. They are:

1. whether finite-prefix truth can really be lifted into one infinite envelope by a fixed FO formula;
2. whether the bound `q` smuggles the external size `m` back into the language;
3. whether existential choice of `q` can create false positives;
4. whether definitional invariance survives boundary-sensitive finite formulas;
5. whether the Zeckendorf event family really supplies a decidable coherent envelope;
6. whether the AL2 obstruction rules out every decidable envelope or only the natural one.

All six attacks pass inside the declared scope.

---

## 2. Attack A — the prefix truth lemma

Let `A_infty` be a coherent envelope and let `phi^{<q}` be obtained by restricting every quantified variable to the initial segment strictly below `q`.

For a tuple `a_bar<q`, the induced substructure of `A_infty` on `[q]` is exactly `A_q`. A standard induction on formulas therefore gives

\[
A_\infty\models\phi^{<q}(\bar a)
\iff
A_q\models\phi(\bar a).
\tag{2.1}
\]

No assumption of quantifier locality is needed. The relativization explicitly forces all witnesses and counterexamples into `[q]`.

**Verdict A:** PASS.

---

## 3. Attack B — is `q` a hidden size oracle?

The lifted formula has the shape

\[
R^\uparrow(\bar x)
\iff
\exists q\left(\bigwedge_i x_i<q\land\phi_R^{<q}(\bar x)\right).
\tag{3.1}
\]

Here `q` is not the external finite size. In the infinite envelope it is an ordinary first-order variable ranging over natural numbers.

The formula contains no distinguished final point, no size constant, and no predicate selecting the original construction stage.

Thus prefix lifting does not violate the no-size-oracle firewall.

**Verdict B:** PASS.

---

## 4. Attack C — can existential `q` create a false positive?

Yes for an arbitrary boundary-sensitive family relation; no for a prefix-coherent relation.

This is exactly why prefix coherence is an explicit theorem hypothesis.

Suppose (3.1) holds for some `q`. By (2.1), `R` holds in finite prefix `A_q`. If the intended finite relation is prefix-coherent, that old-tuple fact remains true in all later prefixes and hence belongs to the unique infinite union.

Conversely, if an old-tuple fact belongs to the coherent union, it holds in every sufficiently large prefix, so one suitable `q` witnesses (3.1).

Therefore

\[
\boxed{
\text{prefix coherence is sufficient to eliminate existential-bound false positives.}
}
\tag{4.1}
\]

It is also essential to the proof as written.

**Verdict C:** PASS, with prefix coherence retained as a non-removable hypothesis.

---

## 5. Attack D — do truncated Add and Mul satisfy the coherence hypothesis?

Define

\[
Add_m(a,b,c)\iff a+b=c<m,
\]

\[
Mul_m(a,b,c)\iff ab=c<m.
\]

For a fixed tuple `(a,b,c)` already contained in `[m]`, enlarging the prefix changes neither equality `a+b=c` nor `ab=c`. Hence both relation families are prefix-coherent.

The truncation condition is not an extra boundary predicate once the tuple itself lies in the prefix: `c<m` is automatic.

Therefore both arithmetic relations satisfy the lift lemma exactly.

**Verdict D:** PASS.

---

## 6. Attack E — does lifted finite Add equal ordinary infinite addition?

Assume `phi_Add` uniformly defines every finite `Add_m`.

If `a+b=c`, choose any `q>max(a,b,c)`. Then `Add_q(a,b,c)` holds, so the prefix truth lemma gives the lifted formula.

If the lifted formula holds, it holds through some finite `Add_q`, so necessarily `a+b=c` in the ordinary natural numbers.

Thus the lift defines exactly

\[
\boxed{Add_\infty(a,b,c)\iff a+b=c.}
\tag{6.1}
\]

The same proof gives

\[
\boxed{Mul_\infty(a,b,c)\iff ab=c}
\tag{6.2}
\]

if a uniform finite multiplication formula existed.

**Verdict E:** PASS.

---

## 7. Attack F — undecidability contradiction

If both (6.1) and (6.2) are FO-definable in a coherent envelope `A_infty`, every first-order arithmetic sentence can be effectively translated into the language of `A_infty` by replacing the two arithmetic graphs with their fixed definitions.

Therefore decidability of `Th(A_infty)` would decide `Th(N,+,times)`.

The latter is undecidable.

Hence no coherent envelope with decidable FO theory can coexist with uniform finite-prefix definitions of both addition and multiplication.

This proves

\[
\boxed{DCE+Add\Rightarrow\neg Mul.}
\tag{7.1}
\]

**Verdict F:** PASS.

---

## 8. Attack G — does the AL2 corollary exclude all decidable envelopes?

`DCE` was defined existentially: at least one decidable coherent envelope.

Theorem (7.1) takes an arbitrary such envelope and derives contradiction from uniform Add and Mul. Consequently an AL2 prefix family cannot possess **any** decidable coherent envelope in the same signature whose finite induced prefixes are the family.

Thus the result is not merely

> the natural binary envelope is undecidable.

It is the stronger statement

\[
\boxed{
\text{no decidable coherent envelope exists for that AL2 family.}
}
\tag{8.1}
\]

**Verdict G:** PASS.

---

## 9. Attack H — boundary-sensitive definitional equivalence

Suppose family `B_m` is uniformly FO-definable inside `A_m`, but the defining formula is boundary-sensitive when evaluated directly in `A_infty`.

Naively reusing the formula in `A_infty` would indeed be invalid.

The theorem does **not** do that. It first relativizes the formula to a variable prefix bound and then existentially prefix-lifts it. Because the target primitive relation of `B` is itself prefix-coherent, Section 4 proves the lifted relation equals the unique coherent union.

Thus boundary sensitivity is neutralized explicitly.

The resulting `B_infty` is FO-definable in `A_infty`, so decidability transfers by effective formula substitution.

Hence DCE is preserved under coherent uniform FO definitional reduction, and under mutual reduction it is invariant:

\[
\boxed{
A\equiv_{FO-def}^{coh}B
\Longrightarrow
(DCE(A)\iff DCE(B)).
}
\tag{9.1}
\]

**Verdict H:** PASS.

---

## 10. Attack I — Zeckendorf DCE witness

The full Zeckendorf incidence structure can be presented over canonical Fibonacci words.

The required relations are synchronous-regular:

- the canonical representation language has no adjacent `1`s;
- a digit anchor `p` has exactly one `1` in its canonical word;
- `Z(n,p)` checks that the unique `1` position of `p` is also `1` in the word for `n`;
- natural order is automatic in the numeration presentation.

The infinite event relations `U_F,D_F` are FO-definable from `Z` and predecessor/order. Classical automatic-structure closure therefore gives a word-automatic presentation of the event envelope, and classical automatic-structure decidability gives decidable FO theory.

Its restriction to `[m]` is exactly the generated finite event history because event facts concerning old rows and old anchors never change at later construction stages.

Thus

\[
\boxed{DCE(Zeckendorf\ events).}
\tag{10.1}
\]

**Verdict I:** PASS.

---

## 11. Attack J — binary event comparison

Binary differential history satisfies the same latest-event reconstruction theorem as Zeckendorf history. The finite verifier checks the exact event count and reconstruction independently.

The previously established binary/BIT result supplies uniform finite-prefix Add and Mul. Therefore Theorem (7.1) immediately forces

\[
\boxed{\neg DCE(binary\ events).}
\tag{11.1}
\]

This conclusion does not require proving separately that a chosen binary infinite presentation is nonautomatic or undecidable.

**Verdict J:** PASS.

---

## 12. Scope attack — what is not yet invariant

The theorem is deliberately not promoted beyond its proof.

It covers:

- one fixed finite signature;
- same explicit ordered base carrier `[m]`;
- induced-prefix coherence;
- ordinary first-order queries;
- uniform FO definitional recodings handled by prefix lift.

It does not yet prove invariance under:

- arbitrary multi-dimensional interpretations;
- quotient interpretations;
- non-prefix-preserving carrier recodings;
- interpretations using growing auxiliary domains;
- stronger logics than FO.

Therefore `DCE` is a genuine semantic phase separator but not yet the final interpretation-invariant resource requested by the wider programme.

**Verdict on scope:** claim discipline PASS.

---

## 13. Literature firewall

The external ingredients are classical:

- automatic structures have decidable first-order theories;
- FO-definable relations in automatic structures remain automatic;
- Fibonacci/Zeckendorf numeration supports finite-automaton presentations.

No novelty claim should attach to those facts.

The programme-specific result is their combination with the prefix-lift lemma to produce a finite-family arithmetic-phase obstruction and apply it to two equal-linear-cost generated histories.

Publication text must keep this boundary explicit.

---

## 14. Final audit verdict

No defect was found in the DCE barrier inside the stated model.

The central equal-cost phase split may therefore be promoted to hostile-audited theorem status:

\[
\boxed{
\begin{array}{c|c|c}
\text{generated history} & \text{support} & \text{semantic phase}\\
\hline
Zeckendorf\ events & \Theta(m) & DCE+AL1\\
binary/BIT\ events & \Theta(m) & \neg DCE+AL2
\end{array}
}
\]

The main unresolved issue is no longer finding *a* separator. It is extending this separator from coherent FO-definitional equivalence to a genuinely broad interpretation-invariant notion.
