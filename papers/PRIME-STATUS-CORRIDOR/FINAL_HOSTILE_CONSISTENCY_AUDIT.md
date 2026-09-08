# Final Hostile Consistency Audit — Prime-Status Corridor

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-30  
**Verdict:** CORE PASS / PUBLICATION ASSEMBLY AUTHORIZED

## 1. Scope audited

This audit checks the complete current theorem chain:

1. Prime-Status Quotient;
2. finite periodic phase wall;
3. first nonperiodic block layer;
4. finite-injury near-successor obstruction;
5. successor-to-WMSO labelled-word interpretation;
6. mod-4 recurrence barrier;
7. finite-carrier arithmetic jump;
8. maximal-recurrence separation;
9. equinumerosity synchronization theorem;
10. transfer of Bès's cardinality dichotomy.

The purpose is to detect hidden contradictions, circular definitions, false novelty claims, or unsupported imported theorems before manuscript assembly.

---

## 2. Prime-Status Quotient — PASS

For

\[
\Xi(n)=(S(n),Q(n)),
\]

with `S(n)` the prime support and `Q(n)=1` iff some square divides `n`, the product

\[
(A,e)\star(B,d)
=(A\cup B,e\vee d\vee[A\cap B\ne\varnothing])
\]

satisfies

\[
\Xi(ab)=\Xi(a)\star\Xi(b).
\]

Primehood is exactly characterized by singleton support with zero defect. Prime atoms are therefore exactly the nonunit irreducibles.

Every prime permutation preserves the structure and every automorphism permutes the irreducible atoms, yielding the intended full prime symmetry.

No defect found.

---

## 3. Finite phase wall — PASS

For fixed modulus `M`, residue colours partition all but finitely many exceptional primes dividing `M` into infinite classes by Dirichlet.

Permutations within each colour class extend to quotient automorphisms. Hence prime order and true prime successor are not invariant and are not definable.

The stronger statement is restricted correctly to finite expansions whose restrictions to prime tuples factor through fixed finite residue data. No claim is made about arbitrary finite relational expansions.

No defect found.

---

## 4. Nonperiodic pair-block layer — PASS WITH WORDING CONSTRAINT

The relation pairing consecutive primes inside each residue class is genuinely nonperiodic relative to numerical prime coordinates and breaks atom permutations to block permutations.

It does not restore global prime order because equal-colour oriented blocks remain permutable.

The final paper should describe this as an explicit **intermediate symmetry-breaking example**, not as a minimality theorem. Minimality has not been proved.

---

## 5. Finite-injury obstruction — PASS

Deleting all true-successor edges incident with two distant same-colour atoms deletes at most four edges and makes their transposition an automorphism of the reduct.

Thus a relation agreeing with true prime successor on all but finitely many edges need not define true prime successor.

This correctly proves that density-one agreement is insufficient for reconstruction.

The paper must not strengthen this to a general characterization of reconstructibility from edge density.

---

## 6. Successor-to-WMSO interpretation — PASS

The crucial internal coding survives audit.

### 6.1 Squarefree finite carriers

For a nonempty state `(A,e)`, squaring yields `(A,1)`. Therefore a nonempty element is squarefree iff it is not idempotent. The unit is handled separately.

Thus squarefree quotient elements are a definable copy of all finite subsets of prime atoms.

### 6.2 Support equality

\[
\operatorname{supp}(x)=\operatorname{supp}(y)
\iff x\star x=y\star y.
\]

This includes the unit case.

### 6.3 Membership

For atom `p` and finite-set carrier `X`, membership is definable by equality of supports after adjoining `p`.

### 6.4 Reverse coding

Every quotient element is represented in WMSO by a finite set together with one Boolean defect tag. `star` is definable from finite-set union, nonempty intersection, and the tags.

Therefore the first-order Prime-Status successor structure and the corresponding labelled WMSO word structure are effectively bi-interpretable up to a finite Boolean tag.

No circularity found.

---

## 7. Successor defines order only because finite carriers exist — PASS

For atoms `x,y`, order is defined by existence of a finite support containing `x,y` that is successor-closed at every included point except `y`.

If `x<=y`, the finite interval is a witness.

If `x>y`, forward closure from `x` can never terminate at `y`, so any witness would be infinite, impossible.

Extraneous points do not create false positives: any point above `y` would also force an infinite forward tail.

Thus the argument is sound.

---

## 8. Mod-4 recurrence barrier — PASS WITH CLAIM LIMIT

A decision procedure for the monadic theory of the fixed prime-residue word would decide recurrence of every fixed finite residue block because the corresponding `occurs arbitrarily far out` sentence is effectively constructible.

The conclusion is only a lower bound on what such a decision procedure must resolve. It does **not** prove undecidability of the actual prime-residue word.

This limitation is already stated correctly and must be preserved.

---

## 9. Finite-Carrier Arithmetic Jump — PASS

The divisibility construction was retested at all boundary cases.

For atom indices `a>0,b>=0`, the existence of a finite carrier containing `0,b`, bounded by `b`, and closed under adding `a` below `b` is equivalent to `a|b`.

Boundary checks:

- `a>b>0`: closure from `0` immediately demands `a`, contradicting the bound, so false as required;
- `b=0,a>0`: the singleton `{0}` is a witness, so every positive `a` divides `0`;
- `a=0`: handled separately by `0|b iff b=0`.

The imported Julia Robinson theorem gives definability of multiplication (indeed addition and multiplication) from successor and divisibility in the natural numbers. Hence coordinate arithmetic is interpreted and the expansion is undecidable.

No defect found.

---

## 10. Maximal-recurrence separation — PASS

The constructed computable binary word

\[
w_*=B_1B_2B_3\cdots
\]

contains every finite binary word infinitely often.

Its factor recurrence indicator is recursive: for a regular language `L`, if `L` is empty there is no recurrent factor from `L`; if nonempty, choose any finite word in `L`, which recurs infinitely often.

By Semenov's criterion the MSO theory is decidable. Therefore coordinate addition cannot be definable there, because its definability together with the internal finite-set carrier would trigger the Arithmetic Jump.

This proves only that maximal finite-factor recurrence is insufficient. It does not classify the actual prime-residue word.

No defect found.

---

## 11. Equinumerosity synchronization — PASS

For atoms `x=q_i`, `y=q_j`, `z=q_k`, use finite support carriers for half-open intervals

\[
[x,z),\qquad [q_0,y).
\]

Their cardinalities are respectively

\[
k-i,\qquad j.
\]

Therefore

\[
|[x,z)|=|[q_0,y)|
\iff k-i=j
\iff i+j=k.
\]

All ingredients are first-order definable in the Prime-Status expansion with successor and EqCard.

Thus EqCard defines coordinate addition directly, after which the Arithmetic Jump gives divisibility and multiplication.

No off-by-one error remains.

---

## 12. Order alone / EqCard alone / together — PASS

### Order alone

Prime-Status + successor is a WS1S layer and decidable.

### EqCard alone

Feferman-Vaught decidability of `WMSO(N,EqCard)` without order is explicitly recalled in Bès (2013). The Prime-Status quotient adds only finite-set Boolean operations and one finite defect tag, all interpretable in that weak monadic equality/equicardinality setting.

Therefore the order-free EqCard expansion remains decidable.

### Together

Bès Proposition 3.1 directly states that `+` and `x` are definable in `WMSO(N,<,EqCard)`. Our explicit interval proof independently reconstructs `+` in the Prime-Status presentation.

Thus the interaction law is secure:

\[
\boxed{
\text{order alone tame; EqCard alone tame; order+EqCard wild}.
}
\]

---

## 13. Bès cardinality dichotomy — PASS

Bès (2013) studies cardinality relations

\[
R(X_1,\ldots,X_n)
\]

whose truth depends only on the tuple of finite cardinalities.

The verified main result states:

- if `R` is not definable in `WMSO(N,<)`, then `+` and `x` are definable in the expansion;
- for unary cardinality predicates, definability is equivalent to ultimate periodicity of the corresponding set of cardinalities;
- in general the definable cardinality sets are recognizable in the precise finite-union-of-products/ultimately-periodic sense developed in the paper.

Our transfer is legitimate because squarefree quotient elements are exactly finite-set variables and successor internally defines `<`.

The final manuscript must clearly label Bès's abstract dichotomy as classical imported theory. Novelty lies only in its placement and consequences inside the Prime-Status Corridor.

---

## 14. Cumulative-drift / Thomas layer — QUARANTINED FROM CORE

The fourth strike also recorded a possible earlier undecidability threshold using cumulative-drift maps and cited Wolfgang Thomas (1975).

The bibliographic existence of the Thomas paper is verified. However the exact general condition on arbitrary strictly increasing functions used in the research note has not yet been checked against the original theorem text with the same confidence as the Bès/Robinson/Semenov dependencies.

Therefore:

- this layer is **not required** for any core theorem;
- it must not appear as a theorem in the publication manuscript unless separately source-verified;
- it may be omitted entirely without weakening the Prime-Status Corridor result.

This quarantine removes the only currently under-verified imported claim from the publication dependency graph.

---

## 15. Novelty audit — PASS WITH RESTRICTED CLAIMS

The following are classical ingredients and must not be claimed as new:

- radicals/prime supports;
- squarefree predicates and support coding;
- prime permutations in Skolem arithmetic;
- WS1S and finite-set automata methods;
- Semenov recurrence criterion;
- Robinson definability from successor/divisibility;
- Feferman-Vaught equicardinality decidability without order;
- Bès cardinality-relation dichotomy.

The publication claim is the **combined Prime-Status Corridor architecture**:

1. the one-bit quotient preserving exact prime/composite status while retaining full prime symmetry;
2. the sequence of symmetry-breaking but still order-free layers;
3. density-one failure of successor reconstruction by finite injury;
4. exact reduction of successor-enriched quotient structures to labelled weak monadic words;
5. isolation of the actual prime-residue word as a number-theoretic recurrence barrier;
6. the finite-carrier arithmetic jump;
7. maximal-recurrence separation;
8. the identification of finite-support equinumerosity as a primitive geometric synchronizer for coordinate arithmetic;
9. the transferred zero-one boundary for pure cardinality synchronizers.

No direct prior paper containing this combined theorem package has been located in the literature audit performed so far.

This is a publication-positioning statement, not a claim of exhaustive priority proof.

---

## 16. Final verdict

### Mathematical core

**PASS.** No fatal contradiction or proof gap was found in the core theorem chain.

### Dependency hygiene

**PASS after quarantine of the nonessential Thomas/cumulative-drift claim.**

### Publication threshold

\[
\boxed{\text{REACHED}.}
\]

### Action

Research at the current scope should now be frozen as **Prime-Status Corridor v1.0** and publication assembly should begin.

Further investigation of the exact prime-residue word, cumulative-drift functions, or minimal synchronizers below EqCard belongs to sequel work and should not delay the present paper.
