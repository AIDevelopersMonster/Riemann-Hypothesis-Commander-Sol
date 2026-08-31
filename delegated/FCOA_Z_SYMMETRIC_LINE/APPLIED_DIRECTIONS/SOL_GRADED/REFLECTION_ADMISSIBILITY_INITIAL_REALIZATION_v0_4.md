# Reflection-Admissibility Schemas — Initial RPM Realization

**Version:** 0.4  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** RELATIVE-FREE THEOREM PROVED / WEAK-FREE–STRONG-NO-FREE TRICHOTOMY CLOSED  
**Depends on:** `REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`, `REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md`

---

## 1. Executive result

The post-review universal-property problem was:

\[
\boxed{
\text{Construct the initial RPM realization of a fixed reflection-admissibility schema}
\text{ while preserving protected `UNDEF` exactly.}
}
\tag{1}
\]

This report solves that problem for a precise base-relative schema.

The central design principle is that a schema separates input pairs into three logical statuses:

\[
\boxed{
\text{REQUIRED}
\quad/\quad
\text{PROTECTED}
\quad/\quad
\text{OPEN}.
}
\tag{2}
\]

- `REQUIRED` pairs must be defined and generate formal product terms;
- `PROTECTED` pairs must remain undefined in every realization;
- `OPEN` pairs are undefined in the initial realization but may be opened in later realizations.

This avoids both defects found after Review 1:

1. weak freeness over bare `Set` is multiplication-degenerate;
2. strong freeness over bare `Set` does not exist.

Instead, exact undefinedness is moved from a global condition on every morphism to **object-level negative data in the schema**.

For every consistent reflection-admissibility schema `S` over a base RPM `A_0`, we construct a canonical term RPM

\[
\boxed{F_{A_0}(S)}
\tag{3}
\]

and prove:

### Initial Realization Theorem

`F_{A_0}(S)` is initial in the category of `S`-realizations.

Equivalently, for every realization `(A,j)` there exists a unique RPM morphism

\[
\boxed{
\widehat j:F_{A_0}(S)\to A
}
\tag{4}
\]

that extends the prescribed embedding of the base.

The map `widehat j` is automatically **protected-strong**:

\[
(s,t)\in P
\Longrightarrow
(\widehat j(s),\widehat j(t))\notin D_A.
\tag{5}
\]

Thus protected undefinedness is preserved exactly without demanding global strongness on all undefined cells.

The construction has a unique finite-tree normal form, a stage/rank filtration, and a terminating finite algorithm whenever the required relation is finite.

The universal-property trichotomy is now complete:

\[
\boxed{
\begin{array}{lll}
\text{weak free over Set} &:& \text{exists but has empty product domain};\\
\text{strong free over Set} &:& \text{does not exist};\\
\text{schema-relative initial RPM} &:& \text{exists and can be nontrivial}.
\end{array}
}
\tag{6}
\]

---

## 2. Base RPM

Fix a reflection-partial magma

\[
\mathcal A_0=(A_0,D_0,\mu_0,\nu_0).
\tag{7}
\]

Thus

\[
\nu_0^2=\operatorname{id},
\tag{8}
\]

\[
(a,b)\in D_0
\iff
(\nu_0a,\nu_0b)\in D_0,
\tag{9}
\]

and

\[
\mu_0(\nu_0a,\nu_0b)
=
\nu_0\mu_0(a,b).
\tag{10}
\]

The role of `A_0` is to encode all operation cells and outputs that are already fixed before the new admissibility schema is imposed.

In FCOA language, `A_0` is the exact inherited core.

---

## 3. Raw reflected terms

Let

\[
\mathsf T(A_0)
\tag{11}
\]

be the set of finite ordered binary trees whose leaves are labelled by elements of `A_0`.

Inductively:

1. every `a in A_0` is a term;
2. if `s,t` are terms, then
   \[
   [s,t]
   \tag{12}
   \]
   is a term.

Extend reflection recursively by

\[
\overline a=\nu_0a,
\tag{13}
\]

\[
\overline{[s,t]}=[\bar s,\bar t].
\tag{14}
\]

This is an involution on `T(A_0)`.

The brackets here are syntax, not an assertion that the corresponding RPM product is already defined.

---

## 4. Base normalization

The term universe must preserve old base values exactly. Therefore an old defined product must not create a new formal node.

### Definition 4.1 — normalization

Define

\[
N:\mathsf T(A_0)\to\mathsf T(A_0)
\tag{15}
\]

recursively.

For a base term,

\[
N(a)=a.
\tag{16}
\]

For a composite term, first compute

\[
u=N(s),
\qquad
v=N(t).
\tag{17}
\]

If

\[
u,v\in A_0
\quad\text{and}\quad
(u,v)\in D_0,
\tag{18}
\]

set

\[
N([s,t])=\mu_0(u,v).
\tag{19}
\]

Otherwise set

\[
N([s,t])=[u,v].
\tag{20}
\]

Let

\[
\mathsf{NF}(A_0)=\operatorname{im}N
\tag{21}
\]

be the normal-form term set.

### Lemma 4.2 — idempotence

\[
\boxed{N^2=N.}
\tag{22}
\]

### Proof

By induction on term depth. Base terms are fixed. At a composite node the children are normalized first. If the normalized children form an old defined base cell, the output is a base element and is fixed by `N`. Otherwise the normalized bracket already satisfies the defining normal-form condition, so applying `N` again changes nothing. QED.

### Lemma 4.3 — reflection compatibility

\[
\boxed{
N(\bar t)=\overline{N(t)}
}
\qquad(t\in\mathsf T(A_0)).
\tag{23}
\]

### Proof

Induct on term depth. The base case is immediate.

Suppose `N(s)=u` and `N(t)=v`.

If `u,v in A_0` and `(u,v) in D_0`, reflection invariance gives

\[
(\bar u,\bar v)\in D_0,
\]

and base equivariance gives

\[
\mu_0(\bar u,\bar v)=\overline{\mu_0(u,v)}.
\]

Hence both sides of (23) reduce to the same base output.

If the pair is not an old defined base cell, its reflected pair is likewise not an old defined base cell, so both sides remain corresponding reflected brackets. QED.

### Corollary 4.4

`NF(A_0)` is invariant under reflection.

---

## 5. Reflection-admissibility schema

### Definition 5.1 — base-relative reflection-admissibility schema

A **reflection-admissibility schema over `A_0`** is a triple

\[
\mathfrak S=(\mathcal A_0,R,P)
\tag{24}
\]

where

\[
R,P\subseteq\mathsf{NF}(A_0)^2
\tag{25}
\]

satisfy:

1. **reflection invariance**
   \[
   (s,t)\in R
   \iff
   (\bar s,\bar t)\in R,
   \tag{26}
   \]
   \[
   (s,t)\in P
   \iff
   (\bar s,\bar t)\in P;
   \tag{27}
   \]

2. **required/protected separation**
   \[
   R\cap P=\varnothing;
   \tag{28}
   \]

3. **legacy consistency**
   \[
   R\cap D_0=\varnothing,
   \qquad
   P\cap D_0=\varnothing,
   \tag{29}
   \]
   where `D_0` is viewed as a subset of `NF(A_0)^2`.

Interpretation:

- `R` lists new pairs whose product is required to exist;
- `P` lists pairs whose product is protected and must remain undefined;
- every pair outside
  \[
  D_0\cup R\cup P
  \tag{30}
  \]
  is `OPEN`.

Condition (29) does **not** prevent `R` from opening an old undefined base pair. It only prevents a pair already defined in the base from being redundantly reintroduced as a new cell.

Thus LC-style completion is allowed:

\[
(a,b)\notin D_0,
\quad
(a,b)\in R
\tag{31}
\]

means that the schema deliberately opens that old undefined cell.

---

## 6. Legal-term closure

Not every raw normal-form tree need occur in the initial realization. Only terms generated by required products are admitted.

Define a sequence

\[
L_0\subseteq L_1\subseteq\cdots
\tag{32}
\]

by

\[
L_0=A_0,
\tag{33}
\]

and

\[
L_{n+1}
=
L_n
\cup
\left\{
N([s,t]):
 s,t\in L_n,
 (s,t)\in R
\right\}.
\tag{34}
\]

Set

\[
\boxed{
L_{\mathfrak S}=\bigcup_{n\ge0}L_n.
}
\tag{35}
\]

### Lemma 6.1 — reflection closure

For every `n`,

\[
\bar L_n=L_n.
\tag{36}
\]

Hence

\[
\boxed{
\bar L_{\mathfrak S}=L_{\mathfrak S}.
}
\tag{37}
\]

### Proof

Induct on `n`. The base carrier is reflection invariant. If a new term is generated from `(s,t) in R`, then the reflected pair belongs to `R`, the reflected children lie in `L_n`, and Lemma 4.3 gives the reflected generated term. QED.

### Definition 6.2 — rank

For a legal term `u`, define

\[
\operatorname{rk}(u)
=
\min\{n:u\in L_n\}.
\tag{38}
\]

Every base element has rank zero.

---

## 7. Normal-form theorem

### Theorem 7.1 — unique generated form

Every element

\[
u\in L_{\mathfrak S}\setminus A_0
\tag{39}
\]

has a unique representation

\[
\boxed{
u=[s,t]}
\tag{40}
\]

with

\[
s,t\in L_{\mathfrak S},
\qquad
(s,t)\in R.
\tag{41}
\]

Moreover

\[
\operatorname{rk}(s),\operatorname{rk}(t)<\operatorname{rk}(u).
\tag{42}
\]

### Proof

A nonbase legal element first enters at some positive stage, hence is generated by (34). Because `(s,t) in R` cannot be an old defined base cell by (29), its normalized output cannot collapse at the top to an old base value; thus it is a bracket term.

Ordered binary-tree syntax has a unique root decomposition, so `[s,t]=[s',t']` implies `s=s'` and `t=t'`. Minimality of the entry stage gives the rank inequality. QED.

This theorem is the normal form needed for recursive evaluation and uniqueness of the universal map.

---

## 8. Canonical initial RPM

### Definition 8.1

Define

\[
F_{A_0}(\mathfrak S)
=
(L_{\mathfrak S},D_{\mathfrak S},\mu_{\mathfrak S},\nu_{\mathfrak S})
\tag{43}
\]

as follows.

The carrier is `L_S`.

Reflection is the restriction of the reflected-tree involution.

The operation domain is

\[
\boxed{
D_{\mathfrak S}
=
D_0
\cup
\bigl(R\cap L_{\mathfrak S}^2\bigr).
}
\tag{44}
\]

For an old base cell,

\[
\mu_{\mathfrak S}(a,b)=\mu_0(a,b).
\tag{45}
\]

For a new required pair,

\[
\boxed{
\mu_{\mathfrak S}(s,t)=[s,t].
}
\tag{46}
\]

The two clauses do not conflict by (29).

### Theorem 8.2 — RPM theorem

\[
\boxed{
F_{A_0}(\mathfrak S)
\text{ is a reflection-partial magma.}
}
\tag{47}
\]

### Proof

Reflection is an involution by construction.

The old part `D_0` is reflection invariant. The new part is reflection invariant by (26) and Lemma 6.1. Hence `D_S` is invariant.

On old cells equivariance is inherited from `A_0`.

On a new cell,

\[
\begin{aligned}
\mu_{\mathfrak S}(\bar s,\bar t)
&=[\bar s,\bar t]\\
&=\overline{[s,t]}\\
&=\overline{\mu_{\mathfrak S}(s,t)}.
\end{aligned}
\]

Thus the RPM axioms hold. QED.

---

## 9. Exact status of old, required, protected, and open cells

Let

\[
\eta:A_0\hookrightarrow L_{\mathfrak S}
\tag{48}
\]

be the inclusion.

### Theorem 9.1 — conservative status theorem

The inclusion `eta` has the following exact properties.

1. Every old defined cell is preserved with its old value:
   \[
   (a,b)\in D_0
   \Longrightarrow
   \eta(a)\mu_{\mathfrak S}\eta(b)
   =\eta\mu_0(a,b).
   \tag{49}
   \]

2. Every protected cell remains undefined:
   \[
   (s,t)\in P\cap L_{\mathfrak S}^2
   \Longrightarrow
   (s,t)\notin D_{\mathfrak S}.
   \tag{50}
   \]

3. Every legal required cell is defined:
   \[
   (s,t)\in R\cap L_{\mathfrak S}^2
   \Longrightarrow
   (s,t)\in D_{\mathfrak S}.
   \tag{51}
   \]

4. Every legal open cell
   \[
   (s,t)\in
   L_{\mathfrak S}^2\setminus(D_0\cup R\cup P)
   \tag{52}
   \]
   is undefined in the initial realization.

### Proof

All four statements follow directly from the domain formula (44) and the disjointness hypotheses. QED.

### Interpretation

The initial object is **least-defined** outside the required graph but it is not globally strong relative to the base.

This is exactly what conservative FCOA extension needs:

- protected legacy cells cannot change;
- designated cells may be opened;
- unspecified open cells are left undecided.

---

## 10. Realizations of a schema

We now define the category in which `F_{A_0}(S)` will be initial.

### Definition 10.1 — `S`-realization

An **`S`-realization** is a pair

\[
(\mathcal A,j)
\tag{53}
\]

where

\[
\mathcal A=(A,D_A,\mu_A,\nu_A)
\tag{54}
\]

is an RPM and

\[
j:A_0\hookrightarrow A
\tag{55}
\]

is an injective map satisfying:

#### Base compatibility

\[
j\nu_0=\nu_Aj,
\tag{56}
\]

and for every old defined cell,

\[
\mu_A(ja,jb)=j\mu_0(a,b).
\tag{57}
\]

#### Required-term evaluability

Define evaluation recursively along the rank filtration.

For base elements,

\[
\operatorname{ev}_j(a)=j(a).
\tag{58}
\]

Whenever

\[
u=[s,t]\in L_{\mathfrak S}\setminus A_0,
\tag{59}
\]

require

\[
(\operatorname{ev}_j(s),\operatorname{ev}_j(t))\in D_A
\tag{60}
\]

and define

\[
\operatorname{ev}_j(u)
=
\mu_A(\operatorname{ev}_j(s),\operatorname{ev}_j(t)).
\tag{61}
\]

By Theorem 7.1 the root decomposition is unique, so this recursion is unambiguous.

#### Protected undefinedness

For every protected legal pair,

\[
(s,t)\in P\cap L_{\mathfrak S}^2,
\tag{62}
\]

require

\[
\boxed{
(\operatorname{ev}_j(s),\operatorname{ev}_j(t))\notin D_A.
}
\tag{63}
\]

No condition is imposed on open pairs.

### Definition 10.2 — realization morphism

A morphism

\[
h:(\mathcal A,j)\to(\mathcal B,k)
\tag{64}
\]

is an RPM morphism

\[
h:\mathcal A\to\mathcal B
\tag{65}
\]

such that

\[
hj=k.
\tag{66}
\]

Write the resulting category as

\[
\mathbf{Real}(\mathfrak S).
\tag{67}
\]

---

## 11. Evaluation commutes with reflection

### Lemma 11.1

For every `S`-realization `(A,j)` and every legal term `u`,

\[
\boxed{
\operatorname{ev}_j(\bar u)
=
\nu_A\operatorname{ev}_j(u).
}
\tag{68}
\]

### Proof

Induct on rank.

For base terms this is (56).

Let `u=[s,t]`. Then

\[
\bar u=[\bar s,\bar t].
\]

By induction,

\[
\operatorname{ev}_j(\bar s)=\nu_A\operatorname{ev}_j(s),
\]

\[
\operatorname{ev}_j(\bar t)=\nu_A\operatorname{ev}_j(t).
\]

Reflection equivariance in `A` gives

\[
\begin{aligned}
\operatorname{ev}_j(\bar u)
&=
\mu_A(\nu_A\operatorname{ev}_j(s),
       \nu_A\operatorname{ev}_j(t))\\
&=
\nu_A\mu_A(\operatorname{ev}_j(s),
            \operatorname{ev}_j(t))\\
&=
\nu_A\operatorname{ev}_j(u).
\end{aligned}
\]

QED.

---

## 12. Initial Realization Theorem

### Theorem 12.1

The canonical realization

\[
\boxed{
(F_{A_0}(\mathfrak S),\eta)
}
\tag{69}
\]

is initial in

\[
\mathbf{Real}(\mathfrak S).
\tag{70}
\]

That is, for every `S`-realization `(A,j)` there exists a unique realization morphism

\[
\boxed{
\widehat j:F_{A_0}(\mathfrak S)\to A
}
\tag{71}
\]

with

\[
\widehat j\eta=j.
\tag{72}
\]

### Proof — existence

Define

\[
\widehat j(u)=\operatorname{ev}_j(u).
\tag{73}
\]

This extends `j` by (58).

Lemma 11.1 shows that it commutes with reflection.

For an old defined cell `(a,b) in D_0`, base compatibility gives

\[
\begin{aligned}
\widehat j\mu_{\mathfrak S}(a,b)
&=j\mu_0(a,b)\\
&=\mu_A(ja,jb)\\
&=\mu_A(\widehat j a,\widehat j b).
\end{aligned}
\tag{74}
\]

For a new required cell `(s,t) in R`,

\[
\mu_{\mathfrak S}(s,t)=[s,t],
\]

so by recursive evaluation,

\[
\begin{aligned}
\widehat j\mu_{\mathfrak S}(s,t)
&=\widehat j([s,t])\\
&=\mu_A(\widehat j s,\widehat j t).
\end{aligned}
\tag{75}
\]

Required-term evaluability guarantees that the target product in (75) is defined.

Hence `widehat j` is an RPM morphism and is a morphism of realizations.

### Proof — uniqueness

Let

\[
h:F_{A_0}(\mathfrak S)\to A
\tag{76}
\]

be any RPM morphism with `h eta=j`.

We prove `h=widehat j` by induction on rank.

For rank zero, both equal `j`.

For a positive-rank term, Theorem 7.1 gives the unique form

\[
u=[s,t]
\]

with `(s,t) in R`. Since `h` preserves the required product,

\[
\begin{aligned}
h(u)
&=h\mu_{\mathfrak S}(s,t)\\
&=\mu_A(hs,ht).
\end{aligned}
\]

By induction `hs=widehat j(s)` and `ht=widehat j(t)`, so

\[
h(u)=\operatorname{ev}_j(u)=\widehat j(u).
\]

QED.

---

## 13. Protected-Strongness Theorem

The universal map is not generally a strong RPM morphism, nor should it be. It has the exact weaker property needed by conservative completion.

### Definition 13.1 — `P`-strong map

A map from the initial realization to an `S`-realization is **`P`-strong** if for every protected legal pair

\[
(s,t)\in P\cap L_{\mathfrak S}^2,
\tag{77}
\]

the image pair is undefined.

### Theorem 13.2

For every `S`-realization `(A,j)`, the unique universal morphism

\[
\widehat j:F_{A_0}(\mathfrak S)\to A
\]

is `P`-strong:

\[
\boxed{
(s,t)\in P
\Longrightarrow
(\widehat j(s),\widehat j(t))\notin D_A.
}
\tag{78}
\]

### Proof

This is exactly the protected-undefinedness axiom (63) of an `S`-realization together with (73). QED.

### Significance

This is the categorical repair of the strong-free obstruction:

\[
\boxed{
\text{do not demand reflection of every undefined cell by every morphism;}
\text{mark the cells whose undefinedness is semantically protected.}
}
\tag{79}
\]

Global `UNDEF` and protected `UNDEF` are different notions.

---

## 14. Open-Cell Freedom Theorem

Let

\[
O_{\mathfrak S}
=
L_{\mathfrak S}^2
\setminus
(D_0\cup R\cup P).
\tag{80}
\]

### Theorem 14.1

Every pair in `O_S` is undefined in the initial realization, but the definition of `S`-realization imposes no requirement that its image remain undefined.

Hence two realizations can agree on

- the complete base `A_0`;
- every required generated cell;
- every protected cell;

while differing arbitrarily on open cells, subject only to the RPM reflection law and any additional axioms imposed externally.

### Proof

Undefinedness in the initial object follows from (44). The realization axioms mention required and protected pairs only. QED.

This theorem formalizes the exact distinction used repeatedly in signed FCOA work:

\[
\boxed{
\text{protected absence}
\ne
\text{currently unrealized but open interaction}.
}
\tag{81}
\]

---

## 15. Generated-image corollary

Let `(A,j)` be an `S`-realization and define

\[
A_{\mathfrak S,j}
=
\operatorname{ev}_j(L_{\mathfrak S})\subseteq A.
\tag{82}
\]

### Corollary 15.1

The universal map

\[
\widehat j:F_{A_0}(\mathfrak S)\to A
\]

is surjective onto `A_{S,j}`.

Thus every schema-generated realization is a homomorphic image of the initial term realization.

If `widehat j` is injective, then the realization is **term-separating**, and `F_{A_0}(S)` embeds as the exact schema-generated part of `A`.

This gives the usual free-object dichotomy between syntax and identifications in a target realization without forcing those identifications into the schema itself.

---

## 16. Finite construction theorem

### Theorem 16.1

Assume

\[
|A_0|<\infty,
\qquad
|R|<\infty.
\tag{83}
\]

Then

\[
\boxed{
|L_{\mathfrak S}|
\le
|A_0|+|R|.
}
\tag{84}
\]

Moreover the stage construction (33)-(34) terminates after at most `|R|` strict growth stages.

### Proof

Every nonbase legal term has a unique root pair in `R` by Theorem 7.1. Distinct nonbase terms have distinct root pairs. Hence there are at most `|R|` nonbase legal terms.

At every strict stage at least one previously absent nonbase term is added, so there can be at most `|R|` strict growth stages. QED.

### Algorithm

For finite explicit schemas:

1. initialize `L := A_0`;
2. scan `R` for pairs whose two inputs lie in `L`;
3. add their bracket outputs;
4. close under reflection automatically or verify paired insertion;
5. repeat until no new term appears;
6. set the domain to `D_0 union (R cap L^2)`;
7. verify `P cap D = empty`.

Thus the initial finite realization is directly computable.

---

## 17. The completed freeness trichotomy

The post-review programme now has all three legs.

### Theorem 17.1 — trichotomy

#### A. Weak free RPM over bare `Set`

Exists, but its multiplication domain is empty.

#### B. Strong free RPM over bare `Set`

Does not exist, already on one generator.

#### C. Initial RPM over a reflection-admissibility schema

Exists by Theorem 12.1 and is nontrivial whenever a legal required cell is present.

Therefore

\[
\boxed{
\text{the nontrivial universal object lives over admissibility data, not over a bare carrier set.}
}
\tag{85}
\]

This is the exact structural lesson anticipated after Review 1.

---

## 18. Relation to classical free partial-model theory

The construction above must be positioned conservatively.

Free and initial models for classes of partial algebras are classical. In particular, partial Horn / cartesian / essentially algebraic theories admit term-model constructions and left adjoints under standard hypotheses. Palmgren and Vickers give a constructive free partial model theorem using partial terms and partial congruences.

Therefore Theorem 12.1 is **not claimed as the first free-object theorem for partial algebras**.

The specific feature being isolated here is the FCOA/RPM schema semantics:

\[
\boxed{
\text{prescribed old graph}
+
\text{required new cells}
+
\text{negative protected-UNDEF constraints}
+
\text{open cells}
+
\text{covariant reflection}.
}
\tag{86}
\]

This explicit three-status completion semantics is the feature to compare against existing partial-algebra presentations in the next novelty audit.

A second close precedent is Salati's free partial-group construction over input data richer than `Set`. This supports, rather than weakens, the strategic conclusion that the correct universal problem for partial structures is relative to structured admissibility data.

---

## 19. FCOA transfer

The schema language directly matches the signed-line architecture.

Let

\[
D_0=\{\text{old fixed operation cells}\},
\tag{87}
\]

let

\[
P=U_{\mathrm{prot}}
\tag{88}
\]

be the protected `UNDEF` region, and let chosen generated completion rules determine `R` inside the admissible frontier.

Then

\[
F_{A_0}(\mathfrak S)
\tag{89}
\]

is the canonical **least conservative realization** of those generated rules:

- exact old outputs are retained;
- protected cells remain absent;
- chosen new cells exist;
- every other admissible frontier cell remains open.

This is a sharper categorical replacement for counting `NONE/UNDEF` cells: it preserves **where undefinedness is protected** rather than how many empty cells happen to remain.

---

## 20. What is not yet included

The present schema deliberately has no additional equations between new formal outputs.

Thus it does not yet encode requirements such as

\[
[s,t]=r
\tag{90}
\]

for a pre-existing term `r`, except when the equation is already part of the base RPM.

The next extension is a **presented reflection-admissibility schema**

\[
(\mathcal A_0,R,P,E)
\tag{91}
\]

with a reflection-stable family `E` of equations between legal terms.

The expected construction is

\[
F_{A_0}(R,P)/{\equiv_E},
\tag{92}
\]

but partial quotients are delicate: identifying terms can cause a protected pair to collide with a required/defined pair.

Therefore a quotient exists only when the generated congruence is **protection-safe**.

This is now the sharp next barrier.

---

## 21. Next frontier: Protection-Safe Quotient Theorem

Define an equivalence relation `equiv` on `L_S` to be **protection-safe** if

\[
(s,t)\in P
\tag{93}
\]

and

\[
s\equiv s',
\qquad
t\equiv t'
\tag{94}
\]

never place `(s',t')` into the defined graph forced by `D_0 union R` in the quotient.

The next theorem target is:

\[
\boxed{
\text{characterize exactly when a reflection-stable equation set }E
\text{ generates a protection-safe partial congruence,}
}
\tag{95}
\]

and then prove that the corresponding quotient is initial among schema realizations satisfying `E`.

This would upgrade the current **free schema** theorem to a full **generators-and-relations theory with protected undefinedness**.

---

## 22. Publication consequence

The universal-property gap identified after Review 1 is now substantially closed.

RPM/RGPA now possesses:

1. weak free object over `Set` and its degeneracy theorem;
2. strong-free nonexistence theorem;
3. nontrivial initial realization over structured admissibility data;
4. unique term normal form;
5. exact protected/open separation;
6. finite construction algorithm;
7. schema-generated quotient interpretation.

This strengthens the theory materially.

However the result should still be presented as a **specialized partial-algebra presentation theorem** until the novelty audit against partial Horn theories, essentially algebraic theories, and classical partial-algebra presentations is complete.

The next publication-quality mathematical threshold is the protection-safe quotient/presentation theorem, because that is where negative `UNDEF` constraints interact nontrivially with identifications.

---

## 23. Literature anchors

- Erik Palmgren and Steven Vickers, *Partial Horn Logic and Cartesian Categories*, Annals of Pure and Applied Logic 145 (2007), 314-353. DOI 10.1016/j.apal.2006.10.001. Their free partial model theorem constructs term models for cartesian / quasi-equational theories.
- Edoardo Salati, *Limits and colimits, generators and relations of partial groups*, Journal of Algebra 622 (2023), 291-327. DOI 10.1016/j.jalgebra.2023.01.014. In particular, free partial groups are constructed over structured input data richer than bare `Set`.
- Peter Burmeister, *A Model Theoretic Oriented Approach to Partial Algebras*, de Gruyter, 1986.

These references establish that free partial constructions are classical. The present theorem isolates the specific protected/open reflection-admissibility semantics required by the FCOA completion programme.
