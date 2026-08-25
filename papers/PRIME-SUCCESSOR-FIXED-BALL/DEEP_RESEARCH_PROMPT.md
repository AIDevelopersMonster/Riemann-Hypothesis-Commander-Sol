# Deep Research Prompt — Fixed-Ball Interior Candidate

## Role

Act as an adversarial mathematical researcher in model theory, abelian groups, Skolem arithmetic, weak direct products, Feferman–Vaught methods, Presburger arithmetic, and p-adic/valued additive structures.

Your job is **not** to confirm the proposed theorem. Your job is to try to destroy it. Accept a positive result only after every plausible mixed-quantifier escape route has been eliminated.

## Structure under audit

Study

\[
\mathcal B_\Delta=
\Bigl(
(\mathbb N_{>0},\times),
(\mathbb Q,+,0,B),
U_\Delta
\Bigr),
\]

where

\[
B(x)\iff v_{13}(x)\ge0,
\]

and for prime \(p\),

\[
U_\Delta(p,u_p),
\qquad
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

For \(p\neq13\), \(u_p\in B\). For \(p=13\), \(v_{13}(u_{13})=-11\), so the prime 13 is definable in the coupled structure.

The programme seeks a genuine intermediate structure between pure multiplicative symmetry and right-wall grid amplification.

## Existing ingredients to treat as inputs only if independently justified

1. The source sort \((\mathbb N_{>0},\times)\) is Skolem arithmetic, viewed as a free commutative monoid on prime atoms / a weak direct product of Presburger exponent coordinates.
2. The target sort is \((\mathbb Q,+,0,B)\), with \(B=\mathbb Z_{(13)}\).
3. Previous work in the programme supplies a private-denominator / linear-separation phenomenon for finite rational-linear combinations of Frobenius labels on a good-prime tail.
4. Previous work also establishes Local Frobenius Thickness in relevant 13-adic channels. Use it aggressively when searching for counterexamples.

Do not assume any stronger theorem than is actually proved.

# Main objective

Determine whether the following statement is true, false, or requires correction.

## Proposed Mixed Quantifier Compression Theorem

For every first-order formula \(\varphi(\bar p)\) of \(\mathcal B_\Delta\), with free variables restricted to sufficiently large good primes, there exist:

- a finite depth \(K_\varphi\),
- a finite exceptional set \(F_\varphi\),
- finitely many 13-adic residue colors \(c_{K_\varphi}(p)=u_p\bmod 13^{K_\varphi}\),
- a uniform finite bound on exact affine exceptional fibers,
- and only finite-threshold source-side occupancy/counting data,

such that the truth of \(\varphi\) is invariant under every permutation of the good-prime tail that fixes \(F_\varphi\) and preserves the resulting finite formula-relative types.

If true, derive rigorously:

\[
S_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\qquad
<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta),
\]

and, if justified,

\[
\forall I\qquad \operatorname{GIR}(I)<\infty.
\]

# Mandatory attack sequence

## Attack A — Target normal form

Prove or refute a quantifier-elimination / normal-form theorem for

\[
(\mathbb Q,+,0,B),
\qquad B=\mathbb Z_{(13)}.
\]

Test the claim that every formula is equivalent to a Boolean combination of

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in 13^mB
\]

for finitely many fixed integers \(m\), with rational-linear \(L\).

Do not merely cite general module theory unless the hypotheses truly cover a divisible group with this distinguished non-pure subgroup. Provide a direct proof or an exact literature theorem.

## Attack B — Uniform Affine-Fiber Bound

For a fixed linear scheme

\[
\sum_{i=1}^r c_i u_{p_i}=t,
\]

where \(t\in\mathbb Q\) is an arbitrary target parameter, determine whether the number of good-prime tuples solving the equation is uniformly bounded independently of \(t\), after fixing the equality pattern and excluding finitely many coefficient primes.

Attempt to construct counterexamples using:

- repeated coefficients;
- cancellations between several tuples;
- parameter choices \(t\) adapted to many Frobenius labels;
- multiple target parameters;
- degenerate linear forms;
- tuples with repeated primes;
- interactions with the exceptional prime 13.

If the claim is true, state the sharpest bound you can prove and identify exactly which prior linear-separation lemma is required.

## Attack C — Alternating mixed quantifiers

Search systematically for formulas of the forms

\[
\exists x\,\forall p\,\Psi(x,p),
\]

\[
\forall x\,\exists p\,\Psi(x,p),
\]

\[
\exists x\,\forall p\,\exists n\,\Psi(x,p,n),
\]

\[
\exists n\,\forall x\,\exists p\,\Psi(n,x,p),
\]

and longer alternations that can defeat finite-color reduction.

In particular test whether a target parameter can code an unbounded set of individually addressable primes through exact equalities, nested cosets, or finite-support source elements.

The burden of proof is to show that target parameters induce only:

\[
\text{finite-color bulk}+\text{uniformly bounded exact exceptions},
\]

not an unbounded family of individual prime addresses.

## Attack D — Source exponent to target depth synchronization

Because 13 is definable, the source chain

\[
1,13,13^2,\ldots
\]

is available.

Try to define one mixed formula \(\Sigma(n,x)\) satisfying on \(n=13^k\)

\[
\Sigma(13^k,x)\iff v_{13}(x)\ge k,
\]

or any weaker relation sufficient to recover a non-eventually-periodic depth filtration, parity of depth, angular information, or a grid-isolation mechanism.

Do not assume the atom-only bridge is automatically multiplicity-blind under arbitrary mixed quantification. Prove the relevant preservation theorem or find a counterexample.

## Attack E — Occupancy and finite support

A source element can encode a finite set of prime divisors. Determine exactly what mixed formulas can say about the set

\[
\{p:\theta(u_p;\bar a)\}
\]

for target parameters \(\bar a\).

Can the structure distinguish:

- empty / nonempty;
- exactly \(m\) elements;
- at least \(m\) elements;
- finite / infinite;
- arbitrarily large finite;
- membership in some Presburger-definable cardinality class?

Determine whether such occupancy information remains finite-threshold for each fixed formula or can be amplified into an unbounded address system.

## Attack F — Grid isolation

Try directly to construct a fixed formula

\[
I(p,q;r)
\]

with \(\operatorname{GIR}(I)=\infty\).

Use every available mechanism:

- exact affine equations;
- fixed-depth cosets;
- source divisibility;
- the definable prime 13 and its powers;
- quantified finite supports;
- Local Frobenius Thickness;
- parameter-coded exceptional tuples;
- alternating source-target quantifiers.

If no construction works, prove a finite upper bound \(C(I)\) from Mixed Quantifier Compression.

# Literature audit

Search current and classical literature for exact results on:

1. Skolem arithmetic and definable sets in \((\mathbb N_{>0},\times)\);
2. weak direct products and Feferman–Vaught / Mostowski decomposition;
3. two-sorted products with a stationary shared sort and known failures of naive Feferman–Vaught transfer;
4. Presburger eventual periodicity along a single prime-power coordinate;
5. divisible abelian groups with a named subgroup, especially \((\mathbb Q,+,\mathbb Z_{(p)})\);
6. quantifier elimination or pp-normal forms for chains of subgroups;
7. dp-minimal / NIP expansions of abelian groups by subgroup chains;
8. any theorem already implying or contradicting the proposed fixed-ball result.

Distinguish carefully between:

- exact theorem already in the literature;
- straightforward corollary;
- new argument needed here;
- conjectural step.

Do not make priority claims without evidence.

# Required output

Produce a research report with the following sections:

1. **Verdict:** theorem true / false / only a corrected weaker form survives.
2. **Minimal counterexample**, if any.
3. **Exact target normal form**, with proof or authoritative theorem.
4. **Uniform Affine-Fiber Bound:** proof, counterexample, or corrected statement.
5. **Mixed Quantifier Compression:** full induction/decomposition argument or precise obstruction.
6. **No Scale Synchronization:** proof status after mixed-quantifier audit.
7. **Occupancy theorem:** exactly what finite-support source quantification can recover.
8. **Consequences for prime order and prime successor.**
9. **Consequences for GIR.**
10. **Novelty/prior-art audit.**
11. **Publication recommendation:** reject, revise, GitHub checkpoint only, or Zenodo-ready.
12. **List of every claim that still lacks proof.**

# Research discipline

- Try to falsify before proving.
- Never infer full Mixed Quantifier Compression merely from target QE plus pure Skolem arithmetic.
- Never call a color-preserving permutation an automorphism of the original coupled structure unless it actually preserves \(U_\Delta\).
- Formula-relative tail indistinguishability is sufficient; genuine automorphism is not required.
- Do not use “first in history”, “new theorem”, “Holy Grail”, or equivalent priority language without a serious literature audit.
- Preserve finite exceptional sets explicitly.
- Separate exact equalities from valuation/coset conditions.
- Treat the prime 13 separately whenever necessary.
- If the proposed theorem fails, identify the **minimal additional definable datum** responsible for the collapse. That negative result is itself a valid research outcome.

The purpose of the investigation is to determine whether

\[
(\mathbb N_{>0},\times)
<
\mathcal B_\Delta
<
\text{right-wall grid regime}
\]

is a genuinely provable intermediate zone, or whether another hidden amplification mechanism pushes the right wall still farther left.
