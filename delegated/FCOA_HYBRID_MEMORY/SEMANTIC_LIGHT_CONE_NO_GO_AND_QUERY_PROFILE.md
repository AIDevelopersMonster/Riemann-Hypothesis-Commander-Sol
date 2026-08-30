# FCOA Hybrid Memory — Semantic Light-Cone No-Go and Costed Logical Query Profile

**Status:** hostile-audit theorem + corrected resource proposal  
**Scope:** post-Article-A resource theory; bridges FO transductions, Boolean query complexity and static data-structure tradeoffs

## 1. Objective

After the standard-model bridge, the natural idea was to replace syntactic bounded fan-in by a semantic quantity:

> How many source elements or primitive facts can one output fact genuinely depend on?

The hope was that a small semantic light cone might be invariant under changes of presentation and therefore support an interpretation-stable version of HM-CFPT.

That hope fails if the light cone is measured without charging preprocessing/materialization.

---

## 2. Definitional-collapse theorem

Let `A_N` be a finite-structure family and let

\[
Q_N(\bar x)
\]

be a relation uniformly definable in `A_N` by one fixed FO formula `phi(\bar x)`.

Form the definitional expansion

\[
A_N^Q=(A_N,Q_N)
\]

by adding `Q` as a new primitive relation symbol interpreted exactly by `phi`.

Then:

1. `A` is FO interpretable in `A^Q` by forgetting `Q`;
2. `A^Q` is FO interpretable in `A` by defining `Q` with `phi`;
3. both interpretations are dimension `1` and preserve the universe exactly.

Hence

\[
\boxed{A\equiv_{FO}A^Q}
\]

in the strongest ordinary definitional sense relevant here.

But in `A^Q`, the truth of the output fact

\[
Q(\bar a)
\]

is directly stored in one primitive atomic fact.

Therefore any semantic-light-cone statistic which assigns dependency `1` to a primitive output atom can be collapsed to `1` by a definitional expansion, regardless of how globally complicated the original definition of `Q` was.

### Theorem HM-SLC-NOGO

No nontrivial support-only measure of output dependency can be invariant under arbitrary FO definitional equivalence / FO bi-interpretability while treating primitive atomic facts as unit-cost information.

### Proof

Apply the definitional expansion above to the relation whose dependency is being measured. The expanded family is FO-bi-interpretable with the original family, but the added primitive atom itself is a one-fact certificate for every query instance. `square`

This is the semantic analogue of the earlier target-hosting and incidence-compilation failures.

---

## 3. Atomic certificate complexity relative to a fixed presentation

Although support alone is not interpretation-invariant, there is a useful standard presentation-relative notion.

Fix a finite relational signature and an admissible class `Omega_N` of structures on a common labelled universe. Encode the primitive atomic diagram as Boolean coordinates.

For a query instance `q` (for example a tuple `(x,y,z)` asking whether `Mul(x,y,z)` holds), the output becomes a Boolean function

\[
F_q:\Omega_N\to\{0,1\}.
\]

For one structure `A in Omega_N`, an **atomic certificate** for `F_q(A)` is a set of primitive atomic literals whose values in `A` force the same query answer in every `B in Omega_N` agreeing with those literals.

Let

\[
C_{at}(A,q)
\]

be the minimum certificate size, and define the worst-case atomic certificate complexity

\[
C_{at}(A,Q)=\max_q C_{at}(A,q).
\]

This is exactly the finite-structure analogue of standard Boolean certificate complexity.

Classical Boolean complexity theory studies certificate complexity together with sensitivity and block sensitivity; these measures are standard query/decision-tree complexity parameters.

---

## 4. Why certificate complexity alone still does not solve the problem

Adding `Q` as a materialized primitive relation gives

\[
C_{at}(A^Q,Q)=1.
\]

The decrease is paid for by storing all primitive `Q` facts.

Therefore certificate complexity is meaningful only together with the size of the preprocessed presentation.

This yields the correct two-axis object:

\[
\boxed{\text{storage / query-dependency tradeoff}.}
\]

---

## 5. Presentation space

Let

\[
S(A_N)
\]

be the number of primitive bounded-arity records in the presentation (or the equivalent bit/word storage under a fixed compilation convention).

A definitional expansion may reduce certificate/query complexity, but generally increases `S`.

Instead of searching for one scalar invariant, define the Pareto set

\[
\mathcal P_Q(\mathcal C)
=
\operatorname{ParetoMin}
\left\{
(S(B_N),C_{at}(B_N,Q)):
B\equiv_{allowed}\mathcal C
\right\}.
\]

The equivalence relation must specify the allowed recodings (for example BF1, bounded-size incidence compilation, or a restricted local transduction class).

The key point is that materialization no longer destroys the theory: it moves a presentation along the space/query frontier instead of magically improving a free invariant.

---

## 6. Connection to static data structures

This is structurally the same optimization problem as a static data structure:

1. preprocess/store information using space `S`;
2. answer a later query using only a restricted amount of stored information.

The classical cell-probe model was introduced precisely to study space/query tradeoffs, and static-data-structure lower bounds treat preprocessing space and query probes as separate resources.

Standard references emphasize the same basic phenomenon relevant here: if storage is unrestricted, one may simply store every query answer and make query cost constant.

Thus our repeated “materialize the relation and collapse the light cone” counterexample is not pathological; it is the standard reason data-structure theory studies a **space–query tradeoff**, not query complexity in isolation.

---

## 7. Why ordinary cell-probe is too strong for FCOA arithmetic

Classical cell-probe allows arbitrary computation for free between memory probes.

For canonical arithmetic queries such as

\[
xy=z,
\]

if the numerical names/values of `x,y,z` are directly available to the query algorithm, an unrestricted cell-probe decoder can compute the arithmetic answer without probing any stored structural memory at all.

Therefore ordinary cell-probe query time is not the desired FCOA resource.

The FCOA problem is about what is recoverable by a **logically restricted decoder** from a structural presentation.

Hence the correct analogue is a restricted static-data-structure model:

\[
\boxed{\text{preprocessing space} + \text{FO/local/constant-depth query decoder}.}
\]

---

## 8. Logical preprocessing/query profile

For a target relation family `Q` define provisionally a **Logical Preprocessing Profile**

\[
LPP_Q=(S,q,\ell),
\]

where

- `S` is primitive presentation size;
- `q` is quantifier rank / bounded logical depth of the uniform query decoder;
- `ell` is a semantic local-dependency or atomic-certificate parameter measured **relative to that fixed presentation**.

One may replace `q` by a more suitable standard decoder class (immersive strongly-local FO, bounded-depth incidence circuit, bounded-fan-in factor circuit, etc.).

The invariant object is then not any coordinate separately but the **Pareto frontier of achievable profiles** under the selected recoding category.

---

## 9. Relation to HM-CFPT

HM-CFPT is exactly one slice of this general space/query picture.

In `CF(d,f)`:

- decoder depth/factorisation is fixed;
- primitive bottom gate arity/capacity is fixed;
- global cross-branch preprocessing shortcuts are forbidden;
- presentation space at the bottom layer is optimized.

Under those restrictions the Pair-Coverage Lemma gives the exact frontier slice

\[
AL0:\quad S_{bot}=Theta(N^{1/f^d}),
\]

\[
AL1/AL2:\quad S_{bot}=Theta(N^{2/f^d}).
\]

Thus HM-CFPT should now be understood as a **restricted logical data-structure space bound**.

This interpretation explains both why the theorem is meaningful and why it disappears when unrestricted preprocessing/materialization is allowed.

---

## 10. Sensitivity and block sensitivity as possible lower-bound tools

Once a presentation is fixed and primitive atomic facts are viewed as Boolean input coordinates, standard Boolean measures become available:

- sensitivity: number of single primitive facts whose change can flip a query answer;
- block sensitivity: maximum number of disjoint fact blocks each capable of flipping the answer;
- certificate complexity: minimum local fact set certifying the answer.

These measures are related in classical Boolean query complexity and can lower-bound restricted decision-tree/query access.

They do not automatically give FCOA lower bounds, because the admissible perturbation class `Omega_N` and decoder model must be specified carefully.

But this is now a standard toolkit rather than an invented FCOA-only vocabulary.

---

## 11. New no-go hierarchy

The resource search has now ruled out the following as standalone interpretation invariants:

1. total cell exponent;
2. maximum degree;
3. literal channel count;
4. direct CRT resolution exponent;
5. interpretation dimension;
6. endpoint-based internal-law memory;
7. any fixed positive internal-law exponent under unrestricted fixed radix width;
8. semantic support / light-cone size by itself.

The eighth failure is fundamental: **precomputation can always trade space for apparent locality**.

---

## 12. Correct research target

The next invariant should therefore be a **tradeoff frontier**, not a scalar.

A defensible target is:

\[
\boxed{
\mathcal F_j(q)
=
\inf\{\text{presentation space }S:
\text{phase }AL_j\text{ is recoverable by a decoder of logical depth }\le q\}.
}
\]

or a normalized exponent version

\[
\sigma_j(q)
=
\inf\limsup_N\frac{\log S_N}{\log N}.
\]

HM-CFPT provides a first exact value for a strongly restricted decoder class.

The ambitious standard-model problem is to determine or separate

\[
\sigma_0(q),\qquad\sigma_1(q),\qquad\sigma_2(q)
\]

for a recognized logical/circuit query model.

---

## 13. Literature-facing interpretation

The appropriate external interfaces are now clearer:

- **FO transductions / immersive strongly-local transductions:** language for structural interpretation and locality;
- **NC^0 / bounded-depth bounded-fan-in circuits:** language for bounded light cones;
- **extensional CSP constraints:** language for primitive table-size cost;
- **Boolean certificate/sensitivity complexity:** language for presentation-relative semantic query dependence;
- **static data structures / cell-probe:** language for preprocessing-space versus query-cost tradeoffs.

No single one of these theories is exactly the FCOA model, but their intersection describes the right research object much more accurately than a new scalar “semantic light cone”.

---

## 14. Main conclusion

The desired interpretation-invariant light-cone scalar does not exist under unrestricted definitional equivalence:

\[
\boxed{\text{semantic dependency can be precomputed and materialized}.}
\]

What survives is a space/query tradeoff:

\[
\boxed{
\text{preprocessing space}
\quad\leftrightarrow\quad
\text{logical query depth/local dependency}.
}
\]

This is the first formulation in the branch that simultaneously explains:

- target hosting;
- lookup-table materialization;
- digit/radix factorization;
- definitional expansion;
- the success of bounded-depth HM-CFPT.

The next serious theorem should therefore fix a standard restricted query decoder and prove a lower bound on this tradeoff frontier, rather than search for another presentation-independent scalar.

## 15. References for calibration

1. H. Buhrman and R. de Wolf, *Complexity measures and decision tree complexity: a survey*, Theoretical Computer Science 288 (2002), 21–43. DOI 10.1016/S0304-3975(01)00144-X.
2. P. Hatami, R. Kulkarni, D. Pankratov, *Variations on the Sensitivity Conjecture*, Theory of Computing Graduate Surveys 4 (2011). DOI 10.4086/toc.gs.2011.004.
3. A. Gál and P. B. Miltersen, *The Cell Probe Complexity of Succinct Data Structures*, Theoretical Computer Science 379 (2007), 405–417. DOI 10.1016/j.tcs.2007.02.047.
4. J. Nešetřil, P. Ossona de Mendez, S. Siebertz, *Structural Properties of the First-Order Transduction Quasiorder*, CSL 2022, DOI 10.4230/LIPIcs.CSL.2022.31.
5. S. Braunfeld, J. Nešetřil, P. Ossona de Mendez, S. Siebertz, *On first-order transductions of classes of graphs*, Logical Methods in Computer Science 21(2), 2025, DOI 10.46298/lmcs-21(2:26)2025.
