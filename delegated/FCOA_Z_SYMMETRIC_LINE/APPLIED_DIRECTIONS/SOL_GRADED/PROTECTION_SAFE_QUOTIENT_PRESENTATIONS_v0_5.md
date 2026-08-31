# RPM / RGPA — Protection-Safe Quotients and Presentations

**Version:** 0.5  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** PROTECTION-SAFE QUOTIENT THEOREM PROVED / GENERATORS-AND-RELATIONS LAYER ESTABLISHED  
**Depends on:** `REFLECTION_ADMISSIBILITY_INITIAL_REALIZATION_v0_4.md`, `REVIEW_1_RESPONSE_AND_NOVELTY_AUDIT_v0_1.md`

---

## 1. Executive result

The next universal-algebra barrier was to add equations to a reflection-admissibility schema without allowing quotient identifications to destroy protected undefinedness.

Starting from a schema

\[
\mathfrak S=(\mathcal A_0,R,P)
\tag{1}
\]

with initial realization

\[
F=F_{A_0}(\mathfrak S),
\tag{2}
\]

we add a reflection-stable family of equations

\[
E\subseteq F\times F.
\tag{3}
\]

The central difficulty is that an ordinary quotient can create a new defined class-pair from previously unrelated representatives. Thus a protected pair `(p,q)` can become defined even if `(p,q)` itself was undefined before quotienting.

This report separates two logically different requirements:

1. **operation coherence** — equations must generate a partial congruence so that quotient multiplication is single-valued;
2. **protection safety** — no protected pair may become equivalent coordinatewise to any defined pair.

Let

\[
\theta_E=\operatorname{Cg}_{\mathrm{RPM}}(E)
\tag{4}
\]

be the least reflection-compatible partial congruence containing `E`.

The main theorem is:

### Protection-Safe Presentation Theorem

There exists a realization of `(A_0,R,P,E)` if and only if `theta_E` satisfies both

\[
\boxed{
\theta_E\cap(A_0\times A_0)=\Delta_{A_0}
}
\tag{5}
\]

and

\[
\boxed{
\forall(p,q)\in P\ \nexists(x,y)\in D_F:
 p\,\theta_E\,x,
\ q\,\theta_E\,y.
}
\tag{6}
\]

Condition (5) is **base separation**. Condition (6) is the **no-protection-collision criterion**.

If these conditions hold, then

\[
\boxed{
F/E:=F/\theta_E
}
\tag{7}
\]

is initial among all RPM realizations of the required/protected schema satisfying the equations `E`.

If either condition fails, then no such realization exists.

Thus equations in RPM presentations are not merely true or false algebraically. They can be rejected because they force a semantically protected absence to become an interaction.

For finite `F`, the criterion is decidable by a finite congruence-saturation algorithm followed by a protected-collision test.

This establishes a genuine generators-and-relations layer with protected undefinedness.

---

## 2. Fixed initial realization

Let

\[
F=(L,D,\mu,\nu)
\tag{8}
\]

be the initial RPM realization constructed from a consistent reflection-admissibility schema

\[
\mathfrak S=(\mathcal A_0,R,P).
\tag{9}
\]

Here

- `A_0 subseteq L` is the embedded exact base;
- `D` contains the inherited defined cells and all legal required cells;
- `P subseteq L^2` is reflection invariant and disjoint from `D`;
- cells outside `D union P` remain open.

The initiality theorem from v0.4 states that every schema realization receives a unique RPM morphism from `F`, and that protected pairs have undefined images in every realization.

We now impose equations between legal terms of `F`.

---

## 3. Equation data

### Definition 3.1 — reflection-stable equation family

An equation family is a relation

\[
E\subseteq L\times L
\tag{10}
\]

satisfying

\[
(s,t)\in E
\Longrightarrow
(\nu s,\nu t)\in E.
\tag{11}
\]

A realization `(A,j)` of the underlying schema **satisfies `E`** if its unique evaluation morphism

\[
\widehat j:F\to A
\tag{12}
\]

satisfies

\[
(s,t)\in E
\Longrightarrow
\widehat j(s)=\widehat j(t).
\tag{13}
\]

Denote the category of such realizations by

\[
\mathbf{Real}(\mathfrak S;E).
\tag{14}
\]

Morphisms are the same schema morphisms as in the equation-free realization category.

---

## 4. Reflection partial congruences

Ordinary equivalence of terms is insufficient because quotient multiplication must be independent of the chosen defined representatives.

### Definition 4.1 — RPM congruence

An equivalence relation

\[
\theta\subseteq L\times L
\tag{15}
\]

is an **RPM congruence** if:

1. **reflection compatibility**
   \[
   x\mathrel\theta x'
   \Longrightarrow
   \nu x\mathrel\theta\nu x';
   \tag{16}
   \]

2. **partial operation coherence**: whenever
   \[
   x\mathrel\theta x',
   \qquad
   y\mathrel\theta y',
   \tag{17}
   \]
   and both
   \[
   (x,y),(x',y')\in D,
   \tag{18}
   \]
   then
   \[
   \boxed{
   \mu(x,y)\mathrel\theta\mu(x',y').
   }
   \tag{19}
   \]

No condition says that definedness itself must be reflected by `theta`. Quotient definedness will be existential on equivalence classes.

### Remark 4.2

Condition (19) is exactly what is needed for a single-valued quotient product. It does not yet protect `UNDEF`.

---

## 5. Congruence closure

### Theorem 5.1 — existence of the least RPM congruence

For every equation family `E`, there exists a least RPM congruence containing `E`, denoted

\[
\boxed{
\theta_E=\operatorname{Cg}_{\mathrm{RPM}}(E).
}
\tag{20}
\]

### Proof

The universal equivalence relation `L x L` is an RPM congruence, so the family of RPM congruences containing `E` is nonempty.

The intersection of any family of equivalence relations is an equivalence relation. Reflection compatibility is preserved by intersection. If (17)-(18) hold in the intersection, then they hold in every member of the family, so (19) holds in every member and therefore in the intersection.

Hence the intersection of all RPM congruences containing `E` is itself an RPM congruence containing `E`, and it is least by construction. QED.

---

## 6. Quotient RPM

Let `theta` be an RPM congruence.

Write

\[
[x]_\theta
\tag{21}
\]

for the equivalence class of `x`.

Define the quotient carrier

\[
L/\theta.
\tag{22}
\]

Reflection is

\[
\bar\nu([x])=[\nu x].
\tag{23}
\]

This is well-defined by (16).

Define quotient domain existentially:

\[
\boxed{
([x],[y])\in D_\theta
\iff
\exists x'\theta x,\ y'\theta y
\text{ with }(x',y')\in D.
}
\tag{24}
\]

If the class-pair is defined, choose any defined representatives and set

\[
\boxed{
\mu_\theta([x],[y])
=[\mu(x',y')].
}
\tag{25}
\]

### Theorem 6.1 — quotient well-definedness

Equations (23)-(25) define a reflection-partial magma

\[
\boxed{
F/\theta=(L/\theta,D_\theta,\mu_\theta,\bar\nu).
}
\tag{26}
\]

The quotient map

\[
q_\theta:F\to F/\theta,
\qquad
q_\theta(x)=[x],
\tag{27}
\]

is an RPM morphism.

### Proof

Suppose two defined representative pairs `(x_1,y_1)` and `(x_2,y_2)` determine the same quotient input classes. Then

\[
x_1\theta x_2,
\qquad
y_1\theta y_2.
\]

By partial operation coherence,

\[
\mu(x_1,y_1)\theta\mu(x_2,y_2),
\]

so (25) is independent of representatives.

Reflection invariance of `D_theta` follows because a defined representative reflects to a defined representative in `D`. Equivariance follows from equivariance in `F` and reflection compatibility of `theta`.

Finally, every defined source pair maps to a quotient-defined pair with the correct output class, so `q_theta` is an RPM morphism. QED.

---

## 7. Why quotienting can destroy protected undefinedness

The quotient domain is existential. Therefore the class of a protected pair can become defined through a different representative.

### Example 7.1 — direct protection collision

Let `nu=id` and let an RPM contain distinct elements `a,b,c` with

\[
D=\{(b,b)\},
\qquad
\mu(b,b)=c.
\tag{28}
\]

Protect

\[
P=\{(a,a)\}.
\tag{29}
\]

Impose the equation

\[
a=b.
\tag{30}
\]

Then in the quotient

\[
[a]=[b],
\]

so

\[
([a],[a])=([b],[b])\in D_\theta.
\]

Thus the protected undefined cell `(a,a)` becomes defined.

The problem is not ambiguity of output: the quotient operation may be perfectly well-defined. The problem is semantic loss of protected absence.

---

## 8. Protection-safe congruences

### Definition 8.1 — protection safety

An RPM congruence `theta` is **`P`-safe** if

\[
\boxed{
\forall(p,q)\in P\ \nexists(x,y)\in D:
 p\theta x,
\ q\theta y.
}
\tag{31}
\]

Equivalently,

\[
\boxed{
([p]_\theta,[q]_\theta)\notin D_\theta
\qquad((p,q)\in P).
}
\tag{32}
\]

### Definition 8.2 — base separation

A congruence `theta` is **base-separating** if

\[
\boxed{
\theta\cap(A_0\times A_0)=\Delta_{A_0}.
}
\tag{33}
\]

This guarantees that the inherited base embeds injectively into the quotient.

### Definition 8.3 — admissible presentation congruence

A congruence is **admissible** if it is both `P`-safe and base-separating.

---

## 9. Monotonicity of failure

The key simplification is that protection failure cannot be repaired by adding more identifications.

### Lemma 9.1 — unsafe is upward closed

Let

\[
\theta\subseteq\rho
\tag{34}
\]

be RPM congruences.

If `theta` is not `P`-safe, then `rho` is not `P`-safe.

If `theta` is not base-separating, then `rho` is not base-separating.

### Proof

If `theta` is unsafe, there exist `(p,q) in P` and `(x,y) in D` with `p theta x` and `q theta y`. Since `theta subseteq rho`, the same witnesses show `p rho x` and `q rho y`; hence `rho` is unsafe.

If two distinct base points are `theta`-equivalent, they remain `rho`-equivalent. QED.

### Consequence

There is no need to search among larger congruences hoping to repair a bad least closure. Once the least algebraic closure collides with protection or collapses the base, the presentation is impossible.

---

## 10. Exact consistency criterion

### Theorem 10.1 — Protection-Safe Quotient Criterion

Let

\[
\theta_E=\operatorname{Cg}_{\mathrm{RPM}}(E).
\tag{35}
\]

The following are equivalent:

1. there exists an admissible RPM congruence containing `E`;
2. `theta_E` is admissible;
3. `theta_E` satisfies the explicit conditions
   \[
   \theta_E\cap(A_0\times A_0)=\Delta_{A_0}
   \tag{36}
   \]
   and
   \[
   \forall(p,q)\in P\ \nexists(x,y)\in D:
   p\theta_Ex,
   q\theta_Ey.
   \tag{37}
   \]

### Proof

`(2) iff (3)` is the definition of admissibility.

`(2) => (1)` is immediate.

For `(1) => (2)`, let `rho` be an admissible congruence containing `E`. By leastness,

\[
\theta_E\subseteq\rho.
\]

If `theta_E` failed base separation or protection safety, Lemma 9.1 would force `rho` to fail the same condition, contradicting admissibility. Hence `theta_E` is admissible. QED.

This is the central decision theorem.

---

## 11. Kernel theorem for realizations

### Theorem 11.1 — realization kernels are admissible

Let `(A,j)` be a realization of the underlying schema and let

\[
\widehat j:F\to A
\tag{38}
\]

be its unique evaluation morphism.

Define

\[
x\ker(\widehat j)y
\iff
\widehat j(x)=\widehat j(y).
\tag{39}
\]

Then `ker(hat j)` is an RPM congruence.

If `j:A_0->A` is injective and the realization respects protected undefinedness, then `ker(hat j)` is admissible.

If the realization satisfies `E`, then

\[
E\subseteq\ker(\widehat j).
\tag{40}
\]

### Proof

Kernel equivalence is reflection compatible because `hat j` commutes with reflection.

If `x~x'`, `y~y'`, and both source pairs are defined, then their image input pairs are equal in `A`; the morphism law therefore gives equal image outputs. Hence the two source outputs lie in the kernel relation.

Injectivity on `A_0` gives base separation.

For protection safety, suppose `(p,q) in P` and there were a defined `(x,y) in D` with `hat j(p)=hat j(x)` and `hat j(q)=hat j(y)`. Since `(x,y)` is defined and `hat j` is an RPM morphism, the image pair `(hat j(x),hat j(y))` is defined in `A`. This is exactly `(hat j(p),hat j(q))`, contradicting protected undefinedness in the realization.

Finally, satisfaction of `E` is precisely inclusion (40). QED.

---

## 12. Existence theorem for presented realizations

### Theorem 12.1 — exact satisfiability

The category

\[
\mathbf{Real}(\mathfrak S;E)
\tag{41}
\]

is nonempty if and only if

\[
\boxed{
\theta_E\text{ is admissible.}
}
\tag{42}
\]

### Proof

If an `E`-realization exists, Theorem 11.1 gives an admissible kernel congruence containing `E`. Theorem 10.1 then implies `theta_E` is admissible.

Conversely, if `theta_E` is admissible, the quotient `F/theta_E` is an RPM by Theorem 6.1. Base separation gives an injective base map. Required cells remain defined because quotient maps preserve every defined source cell. Protection safety gives undefinedness of every protected class-pair. Since `E subseteq theta_E`, the quotient satisfies all equations. Hence it is an `E`-realization. QED.

Thus failed protection safety is not merely a defect of one quotient construction. It proves **nonexistence of every realization** satisfying the equations while respecting the protected schema.

---

## 13. Initial Presented-Realization Theorem

Assume from now on that `theta_E` is admissible.

Set

\[
\boxed{
F(\mathfrak S;E)=F/\theta_E.
}
\tag{43}
\]

Let

\[
q:F\to F(\mathfrak S;E)
\tag{44}
\]

be the quotient morphism.

### Theorem 13.1 — generators-and-relations universal property

The quotient

\[
\boxed{
F(\mathfrak S;E)
}
\tag{45}
\]

is initial in

\[
\boxed{
\mathbf{Real}(\mathfrak S;E).
}
\tag{46}
\]

Explicitly, for every `E`-realization `(A,j)` there exists a unique RPM morphism

\[
\boxed{
\widetilde j:F(\mathfrak S;E)\to A
}
\tag{47}
\]

such that

\[
\widetilde j\circ q=\widehat j.
\tag{48}
\]

### Proof

Let `(A,j)` be an `E`-realization. By the equation-free initiality theorem there is a unique evaluation morphism

\[
\widehat j:F\to A.
\]

By Theorem 11.1 its kernel is an admissible RPM congruence containing `E`. Since `theta_E` is the least RPM congruence containing `E`,

\[
\theta_E\subseteq\ker(\widehat j).
\tag{49}
\]

Hence `hat j` is constant on `theta_E` classes and factors uniquely as a set map through `q`:

\[
\widetilde j([x])=\widehat j(x).
\tag{50}
\]

To prove this is an RPM morphism, suppose `([x],[y])` is quotient-defined. Choose defined representatives `x',y'` in the corresponding classes. Then

\[
\widetilde j([x])=\widehat j(x')
\]

and similarly for `y`. Since `(x',y') in D` and `hat j` is a morphism, the target pair is defined and

\[
\widetilde j\mu_{\theta_E}([x],[y])
=\widehat j\mu(x',y')
=\mu_A(\widehat jx',\widehat jy').
\]

Reflection compatibility is inherited similarly.

Uniqueness follows because `q` is surjective and any factor satisfying (48) is determined on every quotient class. QED.

---

## 14. Presentation theorem

The previous results can be summarized in standard generators-and-relations language, with a new negative-data component.

### Definition 14.1 — protected RPM presentation

A **protected RPM presentation** is data

\[
\boxed{
\langle \mathcal A_0; R\mid E; P\rangle
}
\tag{51}
\]

where

- `A_0` is the exact reflected base;
- `R` specifies required new product cells;
- `E` specifies equations between legal generated terms;
- `P` specifies semantically protected undefined cells.

### Theorem 14.2 — presentation dichotomy

Every protected RPM presentation has exactly one of two statuses.

#### Consistent

If `Cg_RPM(E)` is base-separating and `P`-safe, then

\[
\boxed{
\langle \mathcal A_0;R\mid E;P\rangle
\cong
F_{A_0}(R,P)/\operatorname{Cg}_{\mathrm{RPM}}(E)
}
\tag{52}
\]

is the initial presented realization.

#### Inconsistent

If the congruence closure either

- identifies two distinct base elements; or
- makes any protected pair coordinatewise equivalent to a defined pair,

then

\[
\boxed{
\mathbf{Real}(\mathfrak S;E)=\varnothing.
}
\tag{53}
\]

No alternative quotient or larger congruence can repair the failure.

### Proof

Combine Theorems 10.1, 12.1, and 13.1. QED.

---

## 15. Quotient-induced definedness frontier

The quotient can create new defined class-pairs even when no chosen representative pair was originally the same syntactic pair.

Define

\[
\operatorname{NewDef}(\theta)
=
D_\theta\setminus q_\theta(D),
\tag{54}
\]

where `q_theta(D)` denotes class-pairs represented by original defined cells.

Strictly speaking every quotient-defined pair has some original defined representative by definition, so the meaningful notion is instead the set of **previously undefined source pairs whose class becomes defined**:

\[
\boxed{
\operatorname{Activated}(\theta)
=
\{(x,y)\notin D:
([x],[y])\in D_\theta\}.
}
\tag{55}
\]

Then protection safety is exactly

\[
\boxed{
P\cap\operatorname{Activated}(\theta)=\varnothing.
}
\tag{56}
\]

This separates allowed quotient activation of OPEN cells from forbidden activation of PROTECTED cells.

Thus equations themselves become a controlled completion mechanism:

\[
\boxed{
\text{equational identification may activate OPEN cells, but never PROTECTED cells.}
}
\tag{57}
\]

---

## 16. Minimal ambiguity example

Protection is not the only issue. Equations can also force further equations purely to make multiplication single-valued.

Let `nu=id` and suppose

\[
(a,c),(b,c)\in D,
\tag{58}
\]

with

\[
\mu(a,c)=u,
\qquad
\mu(b,c)=v.
\tag{59}
\]

Impose

\[
a=b.
\tag{60}
\]

Then any RPM congruence containing `(a,b)` must also identify

\[
\boxed{u=v}
\tag{61}
\]

by operation coherence.

Hence the equation closure is genuinely algebraic; it is not merely the equivalence closure of the listed equations.

After this algebraic saturation one must still perform the independent protection test.

---

## 17. Finite congruence-saturation algorithm

Assume `L` is finite.

The least RPM congruence `theta_E` can be computed by iterative union-find closure.

### Algorithm

Initialize an equivalence relation with all pairs in `E` and the diagonal.

Repeat until no class changes:

1. **reflection closure**: if
   \[
   x\sim y,
   \]
   merge
   \[
   \nu x\sim\nu y;
   \tag{62}
   \]

2. **operation closure**: for every two defined cells
   \[
   (x_1,y_1),(x_2,y_2)\in D,
   \]
   if
   \[
   x_1\sim x_2,
   \qquad
   y_1\sim y_2,
   \]
   merge
   \[
   \mu(x_1,y_1)\sim\mu(x_2,y_2).
   \tag{63}
   \]

At the fixed point, test:

3. **base separation**: no class contains two distinct elements of `A_0`;

4. **protection collision**: for each `(p,q) in P`, there is no `(x,y) in D` with
   \[
   p\sim x,
   \qquad
   q\sim y.
   \tag{64}
   \]

### Theorem 17.1 — finite correctness

The fixed-point relation produced by steps 1-2 is exactly

\[
\operatorname{Cg}_{\mathrm{RPM}}(E).
\tag{65}
\]

The presentation is realizable if and only if tests 3-4 pass.

### Proof

Each closure step is forced in every RPM congruence containing the current relation. Therefore all performed merges lie in `Cg_RPM(E)`.

At termination the resulting equivalence is reflection compatible and satisfies operation coherence, hence is itself an RPM congruence containing `E`. By leastness it equals `Cg_RPM(E)`.

The final consistency statement is Theorem 10.1. QED.

### Termination

Every strict merge reduces the number of equivalence classes. Hence at most

\[
|L|-1
\tag{66}
\]

strict merge events can occur after initialization. Thus the algorithm terminates.

No claim of optimal time complexity is made here.

---

## 18. Kernel-intersection representation

The least safe congruence admits a semantic characterization whenever the presentation is consistent.

### Theorem 18.1 — semantic kernel theorem

If `Real(S;E)` is nonempty, then

\[
\boxed{
\theta_E
=
\bigcap_{(A,j)\in\mathbf{Real}(\mathfrak S;E)}
\ker(\widehat j).
}
\tag{67}
\]

### Proof

Every realization kernel is an RPM congruence containing `E`, so by leastness

\[
\theta_E\subseteq\bigcap\ker(\widehat j).
\]

Conversely, the initial quotient `F/theta_E` is itself an `E`-realization. Its quotient map has kernel exactly `theta_E`. Since that kernel occurs among the intersected kernels, the reverse inclusion follows. QED.

Thus two terms are identified in the presented initial RPM exactly when **every admissible protected realization satisfying the equations identifies them**.

---

## 19. FCOA interpretation

For FCOA-style completion, the presentation data have a direct meaning.

\[
\mathcal A_0
=
\text{exact inherited legacy core},
\tag{68}
\]

\[
R
=
\text{generated completion cells that must be realized},
\tag{69}
\]

\[
P
=
\text{protected structural `UNDEF`},
\tag{70}
\]

\[
E
=
\text{new equations/identifications demanded by a candidate theory}.
\tag{71}
\]

The criterion says that a proposed equation is not admissible merely because it is algebraically consistent with the defined products. It must also avoid turning a protected absence into a defined interaction.

This gives a precise formal version of a long-standing FCOA design rule:

\[
\boxed{
\text{equational simplification may not silently fill protected holes.}
}
\tag{72}
\]

For example, any proposed symmetry equation that identifies a protected mixed cell with a defined same-sign cell is rejected automatically by the quotient criterion.

---

## 20. Structural consequence

The protected presentation theory now has three layers:

### Syntax

Required pairs build the least legal term universe.

### Equations

`Cg_RPM(E)` closes identifications under reflection and all already-defined products.

### Negative semantics

The resulting congruence must avoid the protected relation `P`.

Hence the presented object is not ordinary universal algebra with a partial operation appended. It has an explicit positive/negative asymmetry:

\[
\boxed{
\text{positive equations are closed algebraically; negative domain constraints are checked geometrically.}
}
\tag{73}
\]

This is the point at which protected undefinedness becomes a first-class part of the presentation theory.

---

## 21. Publication significance

The RPM/RGPA programme now possesses:

1. a category of reflection-partial magmas;
2. strong exact embeddings;
3. reflection-generated linear grading;
4. completion dcpo;
5. exchange-locus theory;
6. one- and multi-orbit completion moduli;
7. relative initial realizations for required/protected/open schemas;
8. weak-free / strong-no-free / relative-free trichotomy;
9. protected generators-and-relations presentations;
10. an exact consistency criterion;
11. a finite decision procedure for presented finite schemas.

This materially raises the mathematical maturity of the standalone theory.

However, the novelty audit remains binding: general partial-algebra presentations and partial Horn theories are classical. A future paper must isolate precisely which part of the **protected reflection-admissibility semantics** is not already subsumed by standard essentially algebraic or relational presentation frameworks.

---

## 22. Next frontier

The next high-value question is no longer whether protected quotients exist. Their exact criterion is now known.

Two directions become natural.

### A. Protection closure / minimal repair

If a presentation fails because `theta_E` activates a protected cell, characterize the **minimal equation deletion** or **minimal protection relaxation** needed to restore consistency.

This is a combinatorial optimization problem on collision certificates.

### B. Separation theorem against neighboring frameworks

Determine whether protected RPM presentations are equivalent to models of a known partial Horn / essentially algebraic theory with negative relation data, or whether the REQUIRED/PROTECTED/OPEN completion semantics defines a stricter institution/category not captured by the standard frameworks without enrichment.

For publication strategy, direction B is now the priority. It can either prove a genuine novelty boundary or tell us exactly how to reposition the theory as a specialized application of an existing categorical framework.
