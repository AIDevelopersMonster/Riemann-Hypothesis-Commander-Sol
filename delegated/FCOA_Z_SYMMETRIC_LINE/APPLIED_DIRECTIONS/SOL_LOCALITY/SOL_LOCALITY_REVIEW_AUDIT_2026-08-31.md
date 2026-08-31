# SOL-LOCALITY — Audit of External Reviews

**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** REVIEW AUDIT COMPLETE  
**SOL-LOCALITY status after audit:** `THEORETICALLY CLOSED / LOCALITY CEILING PRESERVED`

## 1. Accepted parts

The reviews correctly recognize the main structural result: locality/branch separation can constrain commutation without selecting a unique mixed-sector value law. They also correctly identify the output-sort question and the BR/B0 tradeoff as the central post-locality obstruction.

The proposed publication orientation toward partial/universal algebra is substantially safer than presenting the result as a physical AQFT model.

## 2. Necessary corrections to Review 1

### 2.1 Not a direct superalgebra correspondence

The SOL-LOCALITY law

\[
L_{\pm}(x,y)\Rightarrow \widehat\oplus(x,y)=\widehat\oplus(y,x)
\]

is not directly the supercommutation law of a \(\mathbb Z_2\)-graded algebra. Supercommutation is controlled by parity and generally carries the sign \((-1)^{|a||b|}\). The correct AQFT-side abstraction is orthogonality/locality selecting commuting pairs. Any relation to superalgebras belongs to SOL-GRADED and must not be merged into the locality theorem.

### 2.2 The root \(x_0\) is not an absorbing zero

In the signed FCOA core,

\[
x_0\oplus x_k=x_k,
\qquad
x_k\oplus x_0=\rho(x_k),
\]

so \(x_0\) is not an annihilator or absorbing element. Therefore BR must not be described as an extension by a zero/absorbing singularity.

### 2.3 Incomparability does not by itself prove absence of an initial object

The fact that BR and B0 have incomparable cost vectors does not prove that the whole category of conservative extensions lacks an initial object. Such a statement requires a category, a morphism class, and an explicit universal-property proof.

### 2.4 Free extension does not automatically mean B0

A genuinely free mixed completion normally retains formal generators/terms unless relations identify them. Depending on the chosen category, a free construction may resemble a bridge-orbit/formal-term object rather than the single-event collapse B0. B0 becomes free only after additional quotient/typing assumptions are built into the category.

### 2.5 Closed monoidal and NIP/dp-minimality proposals are hypotheses, not consequences

Closed monoidal structure does not by itself force the FCOA mixed output into a terminal fiber. Likewise NIP or dp-minimality can only be discussed after choosing a first-order language/theory and proving the relevant definability properties. Neither currently selects BR or B0.

## 3. Necessary corrections to Review 2

### 3.1 UNDEF is not already a zero morphism

A zero morphism is canonical only after passing to a category with suitable pointed/zero-morphism structure. Present FCOA partiality treats UNDEF as absence of a primitive value. Replacing it by \(0_{op}\) is a genuine enrichment of the theory, not a reinterpretation forced by the old axioms.

### 3.2 Opposite translations do not annihilate

The signed line has an invertible shift \(T\) with

\[
T^{-1}T=TT^{-1}=\operatorname{id}.
\]

Hence the claim that left and right translations canonically annihilate to the zero operator in \(\operatorname{End}(G_T)\) is false for the present translation structure.

After a linearization, an additive zero operator may exist, but nothing in the FCOA core implies that a mixed interaction must be mapped to it.

### 3.3 Operator-UNDEF does not evade the no-go

If one postulates

\[
X^+\times X^-\longrightarrow 0_{op},
\]

one has introduced an additional selector axiom: pointed/additive operator semantics plus an annihilation rule. This may define an interesting new completion, but it is exactly the kind of extra structure that the Locality-Only Selector No-Go says is required.

### 3.4 Higher-dimensional/operator-space output is not forced

Sending mixed pairs to an operator space, covering space, or bulk is another output-sort policy. It can be studied, but locality does not force it and the present SOL-LOCALITY result remains `1D-CLOSED`.

## 4. Correct categorical next question

Category theory is useful only if the category is specified independently of the desired answer.

Let a future category \(\mathsf{Ext}_{loc}(M_0)\) consist of conservative locality-compatible extensions of the fixed FCOA core, with a precisely stated notion of typed homomorphism fixing the legacy structure.

The first theorem to seek is not

> "B0 is the free extension",

but rather:

> **Does any independently justified category of locality-compatible FCOA extensions possess a universal object that selects an output policy?**

This must be tested under at least three regimes:

1. base-valued extensions;
2. terminal-valued extensions;
3. sort-changing/formal-output extensions.

## 5. Universal-Property Relocation Principle

The existing locality results already suggest the following meta-principle.

If the admissible category is restricted to relation-only, base-valued, reflection-equivariant completions, BR is the unique object and hence trivially both initial and terminal.

If the admissible category is restricted to relation-only completions with one fresh reflection-fixed terminal event, B0 is the unique object and hence trivially both initial and terminal.

Therefore a universal property cannot be counted as a selector unless the surrounding category and its morphisms are justified without already encoding the BR/B0 output-sort choice.

This is the next theorem-level target:

\[
\boxed{
\text{Universal properties may relocate the selector from the object to the category.}
}
\]

## 6. Publication effect

The external reviews strengthen the publication case but do not alter the mathematical verdict of SOL-LOCALITY.

The safe article claim remains:

\[
\boxed{
\text{geometry-conditioned commutation exists, while locality alone leaves value and output sort underdetermined.}
}
\]

Do not publish the following stronger statements without new proofs:

- direct equivalence with superalgebra locality;
- AQFT kinematics in a physical sense;
- absence of an initial object for all conservative extensions;
- B0 as the automatic free/coproduct completion;
- Operator-UNDEF as a canonical consequence of \(\operatorname{End}(G_T)\);
- dimension forcing into an operator/bulk space.

## 7. Final verdict on the reviews

**Review 1:** `ACCEPT WITH MATHEMATICAL CORRECTIONS`. Its publication strategy and universal-property direction are valuable, but several categorical and graded-algebra claims are stronger than proved.

**Review 2:** `PARTIAL ACCEPT / CENTRAL OPERATOR CLAIM REJECTED`. Treating UNDEF as a zero morphism is a legitimate new research hypothesis, but it is not forced by FCOA, and opposite translations compose to the identity rather than to zero.

**SOL-LOCALITY remains closed.** Any categorical or Operator-UNDEF investigation should be opened as a post-locality selector layer, not silently folded back into the locality theorem.
