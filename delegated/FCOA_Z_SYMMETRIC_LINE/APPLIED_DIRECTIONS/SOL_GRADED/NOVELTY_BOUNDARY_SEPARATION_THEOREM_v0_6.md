# RPM / RGPA — Novelty Boundary and Separation Theorems

**Version:** 0.6  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** DECISIVE NOVELTY BOUNDARY ESTABLISHED / BROAD NEW-CATEGORY CLAIM REJECTED  
**Depends on:** `REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`, `REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md`, `PROTECTION_SAFE_QUOTIENT_PRESENTATIONS_v0_5.md`, `REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md`

---

## 1. Executive verdict

The decisive publication question was whether reflection-partial magmas and their protected presentation theory define a genuinely new foundational algebraic category, or whether the construction is already subsumed by established equivariant partial-algebra and Horn-model machinery.

The answer is now sharp.

### Negative foundational verdict

At set level,

\[
\boxed{
\mathbf{RPM}
\cong
\mathbf{PMag}^{C_2}
=
\operatorname{Fun}(BC_2,\mathbf{PMag}).
}
\tag{1}
\]

A reflection-partial magma is exactly a partial magma equipped with an action of the cyclic group `C_2` by partial-magma automorphisms.

Thus `RPM` is not a new foundational algebraic category. It is a standard equivariant-object category once the ambient category of partial magmas has been fixed.

At the protected-presentation level, REQUIRED/PROTECTED/OPEN semantics admits a faithful universal-Horn encoding using a graph relation for partial multiplication together with negative Horn constraints excluding protected cells. Consequently the protected generators-and-relations layer lies inside the established model theory of partial algebras / universal Horn relational structures.

Therefore the broad claim

> “reflection-partial magmas constitute a new foundational algebraic theory not subsumed by existing frameworks”

is

\[
\boxed{\texttt{REJECT}.}
\tag{2}
\]

### Positive separation verdict

RPM is nevertheless **not** the same as a binary partial group (BPG), nor is either class contained in the other when the designated involution is retained.

The decisive distinction is:

\[
\boxed{
\text{RPM reflection is automorphism-type; BPG involution is inverse-property type.}
}
\tag{3}
\]

Thus the correct surviving research object is not a newly discovered species of algebra, but a specialized theory of

\[
\boxed{
C_2\text{-equivariant partial magmas with protected completion data and exchange loci.}
}
\tag{4}
\]

This remains mathematically useful and potentially publishable in a specialized form, but its novelty must be claimed only for specific derived theorems/invariants, not for the ambient category itself.

---

## 2. Ambient category of partial magmas

Let `PMag` denote the category whose objects are partial magmas

\[
\mathcal A=(A,D,\mu),
\tag{5}
\]

with

\[
D\subseteq A\times A,
\qquad
\mu:D\to A,
\tag{6}
\]

and whose morphisms are the weak homomorphisms used throughout the RPM programme:

\[
(x,y)\in D_A
\Longrightarrow
(fx,fy)\in D_B,
\tag{7}
\]

\[
f\mu_A(x,y)=\mu_B(fx,fy).
\tag{8}
\]

An automorphism in `PMag` is therefore a bijection whose map and inverse both preserve defined products. Equivalently it preserves the domain exactly and preserves product values.

Let `BC_2` denote the one-object category associated with the group

\[
C_2=\{1,r\},
\qquad r^2=1.
\tag{9}
\]

A `C_2`-object in `PMag` is a functor

\[
BC_2\to\mathbf{PMag}.
\tag{10}
\]

Concretely, it is a partial magma together with an involutive automorphism.

---

## 3. Equivariant Collapse Theorem

### Theorem 3.1

There is a canonical isomorphism of categories

\[
\boxed{
\mathbf{RPM}
\cong
\operatorname{Fun}(BC_2,\mathbf{PMag}).
}
\tag{11}
\]

### Proof

An RPM is data

\[
(A,D,\mu,\nu)
\tag{12}
\]

such that

\[
\nu^2=\operatorname{id},
\tag{13}
\]

\[
(x,y)\in D
\iff
(\nu x,\nu y)\in D,
\tag{14}
\]

and

\[
\mu(\nu x,\nu y)=\nu\mu(x,y).
\tag{15}
\]

Equations (14)-(15) state exactly that `nu` is an automorphism of the underlying partial magma. Equation (13) states that this automorphism has order dividing two. Therefore assigning the nonidentity element `r in C_2` to `nu` defines a functor `BC_2 -> PMag`.

Conversely, a functor `BC_2 -> PMag` assigns to its unique object a partial magma and to `r` an automorphism `nu` satisfying `nu^2=id`. Since `nu` is a partial-magma automorphism, (14)-(15) hold, giving an RPM.

A natural transformation between two such functors is exactly a partial-magma morphism `f` satisfying

\[
f\nu_A=\nu_Bf,
\tag{16}
\]

which is exactly an RPM morphism.

The two constructions are inverse on objects and morphisms. QED.

### Corollary 3.2

Every categorical property of `RPM` that follows formally from the general theory of `G`-objects in `PMag` must be treated as inherited equivariant-category machinery, not as a new RPM-specific phenomenon.

### Corollary 3.3 — strong version

If `PMag_str` denotes the category with strong homomorphisms, then

\[
\boxed{
\mathbf{RPM}_{str}
\cong
\operatorname{Fun}(BC_2,\mathbf{PMag}_{str}).
}
\tag{17}
\]

The proof is identical after replacing weak morphisms by strong ones.

---

## 4. Linear consequence

The same collapse occurs at the linear level.

An RGPA

\[
(V,\mathscr D,m,J)
\tag{18}
\]

has an involution `J` preserving the partial tensor domain and satisfying

\[
Jm=m(J\otimes J).
\tag{19}
\]

Hence it is a `C_2`-equivariant partial bilinear algebra.

When `char K != 2`, the decomposition

\[
V=V_{\bar0}\oplus V_{\bar1}
\tag{20}
\]

is the ordinary eigenspace decomposition of a representation of `C_2`.

Therefore the reflection-generated `Z_2` grading remains correct, but its existence is a standard representation-theoretic consequence of an involution. The FCOA-specific content lies in the fact that the involution itself was derived from the completed line geometry, not in the abstract eigenspace decomposition.

---

## 5. Universal-Horn encoding of protected RPMs

The second novelty question concerns the REQUIRED/PROTECTED/OPEN semantics and protection-safe presentations.

Introduce a first-order signature

\[
\Sigma_H=\{\nu,M,P\},
\tag{21}
\]

where

- `nu` is a unary function symbol;
- `M(x,y,z)` is a ternary relation interpreted as “the partial product of `x,y` is defined and equals `z`”;
- `P(x,y)` is a binary relation interpreted as “this pair is protected from becoming defined”.

Consider the following universal Horn axioms.

### Involution

\[
\nu(\nu x)=x.
\tag{22}
\]

### Functionality of the product graph

\[
M(x,y,z)\wedge M(x,y,w)
\Longrightarrow z=w.
\tag{23}
\]

### Reflection equivariance

\[
M(x,y,z)
\Longrightarrow
M(\nu x,\nu y,\nu z).
\tag{24}
\]

Because `nu^2=id`, (24) also gives the reverse implication after applying it again.

### Reflection invariance of protection

\[
P(x,y)
\Longrightarrow
P(\nu x,\nu y).
\tag{25}
\]

### Protected absence

\[
\boxed{
P(x,y)\wedge M(x,y,z)
\Longrightarrow
\bot.
}
\tag{26}
\]

Here `bot` denotes the false conclusion of a Horn integrity constraint.

---

## 6. Horn Representation Theorem

### Theorem 6.1

Models of (22)-(26) are exactly protected reflection-partial magmas

\[
(A,D,\mu,\nu,P)
\tag{27}
\]

where `P` is reflection invariant and disjoint from `D`.

### Proof

Given a Horn model, define

\[
D=\{(x,y):\exists z\ M(x,y,z)\}.
\tag{28}
\]

Functionality (23) makes the corresponding output `z` unique, hence defines a partial operation `mu:D->A`.

Axiom (24) gives reflection invariance of `D` and

\[
\mu(\nu x,\nu y)=\nu\mu(x,y).
\tag{29}
\]

Equation (22) makes `nu` involutive. Axiom (25) makes `P` reflection invariant. Axiom (26) says exactly that no protected pair belongs to `D`.

Conversely, from a protected RPM define

\[
M(x,y,z)
\iff
(x,y)\in D\ \text{and}\ \mu(x,y)=z.
\tag{30}
\]

The RPM and protection axioms immediately imply (22)-(26). QED.

### Corollary 6.2 — three statuses

For a fixed protected RPM, a pair can be read as

- `DEFINED` if it lies in the projection of `M`;
- `PROTECTED` if it lies in `P`;
- `OPEN` if it lies in neither.

Thus the three-way semantics

\[
\boxed{
\text{DEFINED / PROTECTED / OPEN}
}
\tag{31}
\]

is faithfully representable in ordinary relational Horn semantics.

---

## 7. Fixed schemas as Horn presentations

A finite schema

\[
\mathfrak S=(A_0,R,P,E)
\tag{32}
\]

can be translated into the Horn language by adding constants/names for the base and generated legal terms.

- old and REQUIRED products are positive graph facts
  \[
  M(s,t,[s,t]);
  \tag{33}
  \]
- equations in `E` are equality facts;
- protected cells are negative domain constraints, equivalently facts `P(s,t)` together with (26), or direct Horn clauses
  \[
  M(s,t,z)\Longrightarrow\bot;
  \tag{34}
  \]
- OPEN cells receive no fact and no negative constraint.

Therefore the schema-relative term model, equation closure, and protection collision test are specialized instances of standard partial-algebra / universal-Horn model semantics.

The literature of Burmeister explicitly develops universal Horn formulas and existence/undefinedness reasoning for partial algebras; modern work continues to treat categories of partial algebras and strong morphisms as standard categorical objects.

---

## 8. Reinterpretation of the v0.5 quotient theorem

The protection-safe quotient criterion remains mathematically correct and useful, but its foundational status must be narrowed.

Recall

\[
\theta_E=\operatorname{Cg}_{RPM}(E).
\tag{35}
\]

The v0.5 criterion says consistency requires

\[
\theta_E\cap(A_0\times A_0)=\Delta_{A_0}
\tag{36}
\]

and no protected pair to become coordinatewise equivalent to a defined pair.

Under the Horn translation:

- congruence closure is ordinary algebraic equality saturation under the functional graph and reflection;
- a protection collision is exactly the simultaneous derivability of the positive domain graph for a pair and its negative Horn constraint;
- the initial safe quotient is the term/quotient model of the consistent presentation.

Hence the v0.5 theorem is best positioned as an explicit RPM-specialized criterion and finite algorithm, not as evidence that protected partial algebra lies outside standard Horn model theory.

---

## 9. Essentially algebraic versus Horn positioning

Standard essentially algebraic theories allow partial operations whose domains are specified by equations in previously given total operations. This is a classical framework for categories of partial algebras.

Our direct REQUIRED/PROTECTED/OPEN syntax is broader-looking because arbitrary protected absence is negative data rather than a positive equational domain definition.

However this does **not** create a novelty escape hatch. Once relational enrichment and universal Horn integrity constraints are allowed, protected absence is standardly expressible by (26).

Accordingly, the safe positioning is:

\[
\boxed{
\text{protected RPM presentations belong to the established partial-Horn / relational-model ecosystem.}
}
\tag{37}
\]

No claim is made here that the direct one-sorted syntax `(partial mu,nu,P)` is definitionally identical to every standard essentially algebraic presentation. The decisive point is weaker and sufficient for novelty audit: the semantics is already captured by established general model-theoretic machinery.

---

## 10. Separation from binary partial groups

The broad partial-Horn collapse does not identify RPM with Chermak/Hackney partial groups.

Hackney's definition of a binary partial group is a **unital partial magma** `P` with a map

\[
\dagger:P\to P
\tag{38}
\]

such that whenever `ab` is defined,

\[
\boxed{
a^\dagger(ab)=b,
\qquad
(ab)b^\dagger=a.
}
\tag{39}
\]

This is inverse-property behavior.

RPM instead requires

\[
\boxed{
\nu(ab)=\nu(a)\nu(b)
}
\tag{40}
\]

whenever `ab` is defined, with the **same order of the arguments**.

These are structurally different involution laws.

---

## 11. Incomparability Theorem

### Theorem 11.1

With the designated involution retained,

\[
\boxed{
\mathbf{RPM}\not\subseteq\mathbf{BPG}
\qquad\text{and}\qquad
\mathbf{BPG}\not\subseteq\mathbf{RPM}.
}
\tag{41}
\]

### Proof

#### RPM not contained in BPG

Let

\[
A=\{x,\bar x\},
\qquad
\nu(x)=\bar x,
\tag{42}
\]

with empty multiplication domain

\[
D=\varnothing.
\tag{43}
\]

This is an RPM: reflection invariance and product equivariance are vacuous.

A BPG is unital, hence has defined multiplication by a unit. The empty-domain RPM has no unit and cannot be a BPG.

#### BPG not contained in RPM

Take any nonabelian group `G`, for example `S_3`. As a total group it is a BPG with

\[
g^\dagger=g^{-1}.
\tag{44}
\]

If it were an RPM with the same designated involution, RPM equivariance would require

\[
(xy)^{-1}=x^{-1}y^{-1}.
\tag{45}
\]

But group inversion gives

\[
(xy)^{-1}=y^{-1}x^{-1}.
\tag{46}
\]

Thus (45) for all `x,y` would force

\[
x^{-1}y^{-1}=y^{-1}x^{-1},
\]

hence `xy=yx`, contradicting noncommutativity. Therefore `S_3` as a BPG is not an RPM with its inversion involution. QED.

### Corollary 11.2

RPM should not be described as a weak form of BPG obtained merely by deleting axioms. The involution has a different variance with respect to multiplication.

---

## 12. Separation from partial *-algebras

The same variance distinction explains the earlier comparison with partial `*`-algebras.

A standard `*`-law is anti-multiplicative:

\[
(xy)^*=y^*x^*.
\tag{47}
\]

RPM reflection is multiplicative/covariant:

\[
\nu(xy)=\nu x\,\nu y.
\tag{48}
\]

Thus the mirror-exchange locus in RPM is not tautological: swap is absent from the reflection axiom and arises only where

\[
(\nu x,\nu y)=(y,x).
\tag{49}
\]

That is precisely the graph-of-reflection locus

\[
\{(x,\nu x)\}.
\tag{50}
\]

---

## 13. What survives as RPM-specific mathematics

The novelty audit removes the right to claim novelty for the ambient category and for generic universal-algebra machinery. It does **not** invalidate the proved theorems.

The following remain useful RPM/FCOA-specific derived results:

1. the geometric exchange equalizer
   \[
   \operatorname{Eq}(\nu\times\nu,\operatorname{swap})
   =\operatorname{graph}(\nu);
   \tag{51}
   \]
2. forced mirror exchange on defined cells;
3. fixed/split/excess exchange loci;
4. reflection-even versus reflection-odd output exchange after linearization;
5. FCOA-specific LC3 odd-odd domain obstruction;
6. the root-odd super-skew no-go;
7. explicit conservative completion moduli and their minimal examples;
8. explicit protected-completion algorithms specialized to a fixed inherited FCOA core.

Of these, items 1-4 are elementary structural consequences of equivariance; items 5-6 are genuinely tied to the FCOA legacy operation; items 7-8 use classical orbit/Horn machinery but may still be useful as concrete specialized classification results.

---

## 14. Revised publication classification

The proposed standalone claim

> “Reflection-Graded Partial Algebras: a new algebraic theory”

is no longer defensible after Theorems 3.1 and 6.1.

### Publication decision

\[
\boxed{
\text{DO NOT publish a standalone paper claiming discovery of a new foundational category RPM/RGPA.}
}
\tag{52}
\]

Two publication routes remain scientifically sound.

### Route A — preferred

Use RPM/RGPA as an **abstract toolkit inside the broader FCOA-Z paper**. There it explains exactly why the SUSY analogy partially survives as reflection grading and mirror exchange but fails as a faithful Lie-super bracket.

### Route B — specialized standalone note

A possible independent title would be along the lines of

> **Protected completions and exchange loci in `C_2`-equivariant partial magmas**

with novelty claims restricted to concrete completion/exchange results not already found in the literature.

Before Route B, one further literature audit must target specifically

- equivariant partial algebras / partial magmas with automorphism group actions;
- extensions and completions of equivariant partial operations;
- forbidden-domain or signed partial-algebra presentations.

---

## 15. Effect on the FCOA programme

The negative novelty result is scientifically useful.

It tells us that the value of the SOL-GRADED branch is **not** the invention of a new ambient algebraic category. The value is instead the precise placement of FCOA-Z inside a known abstract envelope:

\[
\boxed{
\text{FCOA reflection completion}
\longrightarrow
C_2\text{-equivariant partial magma}
\longrightarrow
C_2\text{-graded linearized shadow}.
}
\tag{53}
\]

Within that envelope, FCOA contributes additional nonstandard data:

- a derived rather than postulated reflection;
- an exact inherited legacy domain;
- protected undefined cells;
- role-asymmetric root laws;
- typed terminal outputs;
- a constrained mixed completion frontier.

Those extra constraints are exactly what caused the superbracket obstruction and remain the mathematically substantive FCOA content.

---

## 16. Final novelty verdict

The decisive boundary can now be stated without ambiguity.

### Ambient category

\[
\boxed{
\texttt{NOT NEW AS A FOUNDATIONAL CATEGORY}
}
\tag{54}
\]

because

\[
\mathbf{RPM}\cong\mathbf{PMag}^{C_2}.
\]

### Protected presentation semantics

\[
\boxed{
\texttt{SUBSUMED BY GENERAL PARTIAL-HORN / RELATIONAL MODEL THEORY}
}
\tag{55}
\]

at the level of expressive framework.

### Binary partial groups

\[
\boxed{
\texttt{STRICTLY DIFFERENT / INCOMPARABLE WITH DESIGNATED INVOLUTION}
}
\tag{56}
\]

because BPG involution is inverse-property type, while RPM reflection is automorphism-type.

### FCOA-derived exchange/no-go package

\[
\boxed{
\texttt{SURVIVES AS SPECIALIZED MATHEMATICS}
}
\tag{57}
\]

and should be retained in the broader FCOA-Z publication architecture.

---

## 17. Literature anchors

The decisive comparison uses the following established sources.

- Peter Burmeister, *A Model Theoretic Oriented Approach to Partial Algebras*, de Gruyter, 1986 — partial algebras, free objects, existence equations, universal Horn formulas, strong/closed morphisms.
- Peter Burmeister, “Closed sets of universal Horn formulas for many-sorted (partial) algebras,” *Banach Center Publications* 21 (1988), 129-143.
- H. L. Bentley and N. Murthy, “Essentially Algebraic Categories of Partial Algebras,” *Quaestiones Mathematicae* 13 (1990), 361-384, DOI 10.1080/16073606.1990.9631966.
- J. Adámek and J. Rosický, *Locally Presentable and Accessible Categories*, Cambridge University Press, 1994 — essentially algebraic / locally presentable categories.
- Michael Hoefnagel and Pierre-Alain Jacqmin, “Partial Algebras and Implications of (Weak) Matrix Properties,” *Applied Categorical Structures* 32 (2024), Article 34, DOI 10.1007/s10485-024-09790-z.
- Edoardo Salati, “Limits and colimits, generators and relations of partial groups,” *Journal of Algebra* 622 (2023), 291-327, DOI 10.1016/j.jalgebra.2023.01.014.
- Philip Hackney, “On partial groups of small order,” arXiv:2605.26199 (2026), especially Definition 2.7 for binary partial groups.

---

## 18. Next action

The broad novelty question is closed. Do not spend further effort trying to prove that RPM itself is a new category.

The next valuable action is editorial and architectural:

1. revise every RPM/RGPA file so that inherited/classical mechanisms are labelled as such;
2. preserve the proved FCOA-specific theorems and minimal examples;
3. decide whether the material belongs only as an abstract appendix/toolkit to the FCOA-Z article or whether a narrower specialized note on protected `C_2`-equivariant partial-magma completions still has enough literature-separated content.

A further standalone research strike should occur only if it targets a theorem specific to the **derived FCOA constraints**, not merely to equivariant partial magmas in general.
