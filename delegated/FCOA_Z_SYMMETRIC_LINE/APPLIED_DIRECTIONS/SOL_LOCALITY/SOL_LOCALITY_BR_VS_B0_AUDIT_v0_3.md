# SOL-LOCALITY — BR vs B0 Conservativity Audit v0.3

**Date:** 2026-08-30  
**Status:** THIRD TARGET COMPLETE / TWO-MINIMALITY TRADEOFF PROVED  
**Depends on:** `SOL_LOCALITY_REPORT_v0_1.md`, `SOL_LOCALITY_SELECTOR_AUDIT_v0_2.md`, `MIXED_COMMUTATIVE_BRIDGE_GENERATOR_0_1.md`  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264

## 1. Problem

After the locality-only selector no-go, two depth-blind canonical regimes remain:

\[
BR(x,y)=x_0
\qquad ((x,y)\in M),
\]

and

\[
B0(x,y)=E_{cross}
\qquad ((x,y)\in M).
\]

Both are relation-only, mixed-commutative, reflection-equivariant, legacy-exact and one-dimensional. The question is whether one is internally forced by FCOA conservativity.

## 2. One-step information firewall

### Proposition 2.1

Neither `BR` nor `B0` retains radial endpoint information in its mixed output.

#### Proof

Each mixed-output map is constant on the whole mixed domain `M`. Therefore every observable that factors only through that one-step mixed output is constant on `M` as well. It cannot distinguish endpoint depth, equal-vs-unequal depth, signed gap, or endpoint identity. QED.

### Consequence

It would be incorrect to claim that `BR` by itself reconstructs signed addition or `EqSignedGap`. Its one-step mixed-output leakage is as depth-blind as `B0`.

The already rejected synchronous-cancellation control is qualitatively different because its output varies with signed magnitude difference.

## 3. State-extension cost

Define the **state-extension cost** of a conservative mixed realization to be the number of genuinely new output values/sorts required beyond the audited signed FCOA structure.

Then

\[
c_{state}(BR)=0,
\qquad
c_{state}(B0)=1
\]

at the minimal-event level.

### Theorem 3.1 — base-carrier minimality of BR

Among relation-only, reflection-equivariant mixed completions that introduce no new values or output sorts and whose mixed values lie in the old base carrier, `BR` is unique.

#### Proof

A relation-only law is constant on `M`. Reflection equivariance forces that constant to be a reflection-fixed base element. The root `x_0` is the unique such base element. Hence the law is `BR`. QED.

Thus `BR` is the unique zero-new-state locality completion.

## 4. Re-entry and composition cost

Call a newly generated mixed output **primitive-reenterable** if it is already a legal argument of the old binary operation without adding another rule.

Under `BR`, every mixed interaction returns `x_0`, an old base element. Hence it immediately re-enters all legacy operation contexts in which the root is legal.

Under baseline `B0`, the result is the fresh terminal event `E_cross`, which has no primitive re-entry law.

Define the coarse **re-entry cost**

\[
c_{re}(F)=
\begin{cases}
0,&\text{no new mixed result re-enters the primitive operation},\\
1,&\text{a mixed result re-enters immediately}.
\end{cases}
\]

Then

\[
c_{re}(BR)=1,
\qquad
c_{re}(B0)=0.
\]

### Theorem 4.1 — terminal compositional minimality of B0

Among relation-only locality completions whose mixed interaction is represented by one fresh terminal event and whose baseline terminal semantics forbids re-entry, `B0` introduces no new second-stage primitive compositions through the mixed output.

By contrast, `BR` necessarily opens second-stage compositions because its output is the old root.

#### Proof

For `B0`, the inner mixed result has terminal sort, outside the primitive base-input domain, so a second primitive application through that result is undefined unless a separate LC2 re-entry law is added. For `BR`, the inner result equals `x_0`, which is already an admissible old argument in legacy root cells. QED.

## 5. Explicit composition witness

For `a,b>=1`, `BR` gives

\[
(x_a\oplus_{BR}x_{-b})\oplus x_a
=x_0\oplus x_a=x_a,
\]

while

\[
x_a\oplus_{BR}(x_{-b}\oplus_{BR}x_a)
=x_a\oplus x_0=\rho(x_a)\ne x_a.
\]

Thus mixed interaction immediately participates in new alternating association tests.

For `B0`, the corresponding inner mixed product is `E_cross`; under baseline terminal semantics neither second-stage primitive bracketing is admitted through that terminal result. `B0` therefore creates an association-definedness wall rather than new base-valued association equations.

This is a difference in compositional topology, not in one-step locality.

## 6. No-new-arithmetic caution

The preceding re-entry difference must not be overstated.

Because the FCOA root `x_0` already belongs to the legacy structure, composing an original endpoint with the root uses an already existing radial rule. The `BR` bridge supplies the root as the result of a mixed subterm, but its constant mixed output does not itself encode the endpoint depths.

Therefore the present audit proves:

\[
\boxed{BR\text{ has greater primitive re-entry than }B0}
\]

but does **not** prove

\[
BR\Longrightarrow Add
\quad\text{or}\quad
BR\Longrightarrow EqSignedGap.
\]

Any stronger arithmetic-leakage statement requires a separate definability theorem.

## 7. Two-Minimality Tradeoff Theorem

Associate to a depth-blind locality completion the cost vector

\[
\kappa(F)=(c_{state}(F),c_{re}(F)).
\]

For the two canonical regimes,

\[
\boxed{\kappa(BR)=(0,1),\qquad \kappa(B0)=(1,0).}
\]

### Theorem 7.1

`BR` and `B0` are incomparable under componentwise conservativity:

- `BR` is strictly better in state-extension cost;
- `B0` is strictly better in primitive re-entry cost.

Hence no unweighted minimality principle based only on these two natural conservativity coordinates selects one of them.

#### Proof

The values follow from Sections 3–4. Componentwise comparison gives neither

\[
(0,1)\le(1,0)
\]

nor

\[
(1,0)\le(0,1).
\]

Therefore neither realization dominates the other. QED.

### Corollary 7.2 — priority is extra structure

Any scalar cost

\[
C_{\alpha,\beta}(F)=\alpha c_{state}(F)+\beta c_{re}(F)
\]

selects `BR` or `B0` only after choosing the relative priority of `alpha` and `beta`.

That priority is an additional modelling axiom, not a consequence of locality.

## 8. Universal-property split

The two laws do possess different conditional universal characterizations.

### BR universal characterization

`BR` is the unique relation-only, reflection-equivariant conservative mixed completion **internal to the old base carrier with no new output value**.

### B0 universal characterization

`B0` is the unique relation-only completion into a **single fresh reflection-fixed terminal event** under the declared no-reentry terminal policy.

These are not competing proofs of one theorem. They are universal properties in different categories of admissible extensions.

Therefore the missing programme decision is categorical:

\[
\boxed{\text{Should conservative completion minimize new states, or minimize new composable paths?}}
\]

FCOA locality itself does not answer this.

## 9. Relation to the Line Completion Gate

### LC1

Both `BR` and `B0` realize every mixed cell conservatively.

### LC2

This audit shows that LC2 is not downstream bookkeeping. Re-entry policy is exactly what separates the two minimal locality completions.

- `BR`: automatic re-entry through the base root;
- `B0`: no baseline re-entry; any re-entry requires an explicit new law.

### LC3

Within either predeclared output regime the law is unique, but across regimes locality remains underdetermined.

### Dimension status

Both remain one-dimensional. `B0` adds a finite/internal terminal fiber, not an independently iterable coordinate.

Hence

\[
\boxed{\texttt{1D-CLOSED}}
\]

and no `DIMENSION-FORCING` claim follows.

## 10. Final SOL-LOCALITY no-go

Combining v0.1, v0.2 and the present audit yields:

### Theorem 10.1 — Locality Ceiling Theorem

Within the present audited FCOA-Z line, geometry-conditioned locality can determine **where** mixed commutation holds, but cannot by itself determine:

1. the output sort of the mixed interaction;
2. whether that output re-enters the primitive operation;
3. how much radial information a richer mixed law may retain.

Even after imposing relation-only behavior, reflection equivariance, legacy exactness, finite-window coherence and minimality, two incomparable canonical regimes survive:

\[
BR:M\to\{x_0\},
\qquad
B0:M\to\{E_{cross}\}.
\]

Thus locality is a genuine compatibility principle but not a complete interaction-generation principle.

## 11. Scientific verdict

The AQFT bridge survives at exactly the correct abstraction level:

\[
\boxed{\text{geometry can select algebraic compatibility without selecting interaction value or output ontology}.}
\]

This is stronger and cleaner than a superficial spacetime analogy, but weaker than a physical AQFT model.

Programme status:

\[
\boxed{\texttt{FORMAL EMBEDDING / LOCALITY CEILING REACHED}}
\]

Line status:

\[
\boxed{\texttt{1D-CLOSED + UNDERDETERMINED ACROSS OUTPUT POLICIES}.}
\]

## 12. Publication and continuation decision

The internally natural SOL-LOCALITY research question is now closed at this level. Further work would require adding a new independent principle about output typing, re-entry, information preservation, or universality; that would be a new cross-direction obligation rather than a further consequence of AQFT locality.

Recommendation:

\[
\boxed{\texttt{READY FOR APPLIED-DIRECTIONS SYNTHESIS, NOT STANDALONE PHYSICAL PUBLICATION}.}
\]

The three SOL-LOCALITY documents should be treated as one completed package:

1. `SOL_LOCALITY_REPORT_v0_1.md` — construction and first underdetermination theorem;
2. `SOL_LOCALITY_SELECTOR_AUDIT_v0_2.md` — output-sort obstruction and locality-only selector no-go;
3. `SOL_LOCALITY_BR_VS_B0_AUDIT_v0_3.md` — two-minimality tradeoff and final locality ceiling.
