# FCOA Rigidity Cost — Global Escape-Cover Reduction at Beta One

**Status:** post-publication structural theorem.

## 1. Setup
Let beta(D,c)=1 and let W_kill be the set of missing singleton cells whose addition kills every old bad automorphism. For e in W_kill and b in F_2, let B_b(e) be the set of bad carrier automorphisms of the enlarged ternary reduct on D union {e} with c(e)=b.

Call (e,b) **covered** if B_b(e) is nonempty. Then a one-cell exact repair exists iff some pair (e,b) is uncovered.

## 2. Global Escape-Cover Theorem

### Theorem 2.1
If beta(D,c)=1, then

alpha(D,c)>1

if and only if every beta-killing color-state is covered:

\[
\boxed{\forall e\in W_{kill},\ \forall b\in F_2,\quad B_b(e)\ne\varnothing.}
\]

### Proof
Because beta=1, every e in W_kill is an old-obstruction repair. The singleton extension (e,b) is exact precisely when it has no bad automorphism. Therefore alpha=1 iff at least one beta-killing color-state is uncovered. Negating gives the statement. square

This elementary equivalence is important because Persistent Exclusion and the split-transporter analysis now make the cover highly structured.

## 3. Anchored sector
Assume e is anchored. Persistent Exclusion gives

\[
B_0(e)\cap B_1(e)=\varnothing.
\]

Hence if both color-states of e are covered, they must be covered by genuinely different defect-one replacement symmetries. No single carrier permutation covers both.

For h in B_b(e), define the replacement target

\[
p_h=h(e)\in D.
\]

For fixed e,b,p, all bad replacements with target p form one H_e-coset, where

\[
H_e=\{g\in A^+(D,c):g(e)=e\}.
\]

Thus anchored coverage is encoded by target-color fibers

\[
P_b(e)=\{h(e):h\in B_b(e)\}\subseteq D.
\]

A fully covered anchored cell requires

\[
P_0(e)\ne\varnothing,\qquad P_1(e)\ne\varnothing.
\]

## 4. Isolated sector
If e is isolated in Lambda(D union {e}), the new component has phase 0 for every D-preserving automorphism fixing e. Hence an old global phase-1 automorphism fixing e creates the isolated phase trap. Domain-moving replacements may also cover a color-state.

Therefore every beta-one counterexample must globally cover W_kill x F_2 by the union of:

1. anchored defect-one replacement fibers;
2. isolated phase traps;
3. isolated defect-one replacement fibers.

## 5. Defect-one boundary necessity
For an anchored beta-killing cell, any bad enlarged automorphism moves D, hence e lies in R_1(D). Consequently, in a beta-one counterexample,

\[
\boxed{W_{kill}^{anch}\subseteq R_1(D).}
\]

This recovers danger saturation but strengthens its interpretation: membership in R_1 is only the geometric eligibility condition; actual failure requires both color states to be covered by bad replacement fibers.

## 6. Capacity inequality
Define the global anchored color-state set

\[
\Omega_{anch}=W_{kill}^{anch}\times F_2.
\]

For every defect-one carrier permutation h define its coverage set

\[
C_h=\{(e,b)\in\Omega_{anch}: h(D\cup\{e\})=D\cup\{e\},\ h\in B_b(e)\}.
\]

Then a beta-one counterexample necessarily satisfies

\[
\boxed{\Omega_{anch}\subseteq\bigcup_h C_h.}
\]

Persistent Exclusion implies the vertical-fiber restriction

\[
\boxed{|C_h\cap(\{e\}\times F_2)|\le1}
\]

for every anchored beta-killing e.

Therefore each carrier permutation can cover at most one color-state over each anchored killing cell.

This is the first genuine global capacity restriction on the replacement cover.

## 7. Orbit form of a replacement cover
If h covers (e,b), then h preserves S_e=D union {e} while moving D. Hence

\[
h(D)=D-\{q_h(e)\}+\{p_h(e)\}
\]

with positive defect p_h(e)=e when the replacement boundary is parameterized from D to hD, equivalently h(e) is the unique omitted old target in hD. Thus one carrier permutation cannot arbitrarily choose killing cells: the admissible e are constrained by the defect-one orbit of D under h.

In particular, for fixed h the set of missing cells e for which h preserves D union {e} is determined entirely by the symmetric difference

\[
D\triangle hD.
\]

It is nonempty only when d_D(h)=1, and then the admissible singleton is unique:

\[
\boxed{e=P_D(h),}
\]

where P_D(h)=hD\setminus D is the singleton positive defect set.

### Corollary 7.1 — one permutation, one killing geometry
A defect-one carrier permutation can cover color-states over at most one singleton geometry e.

Combining with Persistent Exclusion:

\[
\boxed{|C_h|\le1}
\]

on the anchored beta-killing sector.

This sharpens the capacity statement drastically.

## 8. Counting obstruction
Let R be the set of defect-one carrier permutations h whose unique positive defect cell e=P_D(h) belongs to W_kill^anch and which are bad for at least one color of that extension. Full anchored coverage requires two distinct bad replacement symmetries per anchored killing cell. Hence

\[
\boxed{|R|\ge2|W_{kill}^{anch}|.}
\]

More invariantly, quotienting same-color same-target symmetries by H_e, every fully covered anchored e requires at least two distinct replacement cosets.

This is a necessary condition for beta=1<alpha.

## 9. Escape criterion
### Corollary 9.1
If

\[
|R|<2|W_{kill}^{anch}|,
\]

and no isolated beta-killing cell has both color-states covered, then

\[
\boxed{alpha=1.}
\]

Even without controlling isolated cells, the strict inequality guarantees an exact color on at least one anchored beta-killing cell whenever the anchored sector is nonempty and all isolated cells are irrelevant.

## 10. Structural significance
The beta-one problem is now a finite global capacity problem, not a local exclusion problem.

A counterexample must simultaneously satisfy:

- kappa(Lambda(D)) >= 3;
- danger saturation;
- every anchored beta-killing cell lies on a defect-one boundary;
- each anchored killing cell consumes at least two distinct defect-one replacement permutations/cosets, one for each color;
- no one permutation can service two different killing geometries;
- isolated killing cells must also have both colors trapped.

Thus the next decisive target is a lower bound on |W_kill| versus the number of relevant defect-one replacement symmetries. Any universal inequality of the form

\[
|R|<2|W_{kill}^{anch}|
\]

under beta=1 would prove the anchored Safe-Minimizer theorem immediately.

## Claim firewall
1. The global cover equivalence is exact.
2. The one-permutation/one-geometry lemma is exact for defect-one singleton extensions.
3. The counting inequality is necessary, not yet known to be impossible globally.
4. Split fatality is real, so no claim that every beta-minimizer is safe is made.
5. The global implication beta=1 => alpha=1 remains open.
