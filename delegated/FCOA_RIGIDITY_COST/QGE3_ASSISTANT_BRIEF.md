# FCOA Rigidity Cost — Assistant Brief for Sparse q>=3 Phase Transport

**Parent branch:** `director/fcoa-rigidity-cost`  
**Parent direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** delegated secondary research line  
**Lead line retained by Commander Sol:** binary sparse Safe Minimum Extension / `alpha=beta` problem  
**Assistant line:** sparse anonymous alphabets `q>=3`, non-abelian phase transport

---

## 1. Published foundations

Treat the following as frozen published dependencies:

1. **Article A** — *Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition*, DOI `10.5281/zenodo.22157403`.
   - Complete-domain anonymous equality reducts.
   - Exact arity transition: `q=2 -> k_exact=3`; `q>=3 -> k_exact=4` in the stated equality-reduct class.

2. **Article B** — *Reflections on Sparse Anonymous Phase Geometry with Commander Sol: Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation*, DOI `10.5281/zenodo.22159246`.
   - Sparse binary componentwise phase theorem.
   - `F_2`-valued component cocycle.
   - Costs `lambda`, `mu`, `alpha`.
   - No-old-obstruction theorem.
   - Conjecture `alpha<=lambda` remains open in the published paper.

Do not silently revise either publication.

---

## 2. Scientific task

Develop the correct sparse-domain analogue for `q>=3` anonymous terminal outputs.

Given

\[
c:D\to O,\qquad |O|=q\ge3,
\]

with anonymous output alphabet `O`, determine the local-to-global transport law induced by carrier automorphisms preserving an appropriate derived equality reduct.

The binary model

\[
\delta_g(p)=c(gp)\oplus c(p)\in\mathbf F_2
\]

must **not** be copied formally. For `q>=3` there is no canonical cyclic or additive structure on anonymous colors.

The natural local discrepancy is expected to be permutation-valued:

\[
\phi_{g,C}\in S_q
\]

or in a subgroup / groupoid determined by the colors actually visible on a cell-incidence component.

---

## 3. First theorem target

Find the correct sparse multicolor replacement of the binary Componentwise Phase Theorem.

Candidate form:

> On each connected region of an appropriate comparison/incidence structure, every reduct automorphism induces one locally consistent permutation of the visible anonymous color classes.

Then determine the compatibility law when a carrier automorphism permutes those regions. Expect a non-abelian twisted cocycle / crossed-homomorphism law rather than an additive one.

Do not call the object a cocycle until the action and composition law are stated exactly.

---

## 4. Critical design question

For `q=2`, ternary composable-cell equality is exact on complete domains. Article A proves that for `q>=3`, complete-domain ternary equality data are not universally exact and four variables are needed in general.

Therefore sparse `q>=3` has two possible information models which must be separated:

1. **ternary sparse equality model** — intentionally lossy; classify the resulting local gauge freedom;
2. **four-ary arbitrary-cell equality model** — equality partition is exact on the currently defined domain; classify how sparsity affects extension cost and anonymous color transport.

Do not mix these two models.

---

## 5. Required early deliverables

Produce, in order:

1. `MODEL_DEFINITIONS.md`
   - precise carrier, sparse domain, anonymous alphabet;
   - exact reduct(s) under study;
   - automorphism notion;
   - visible-color support of a component.

2. `TERNARY_FAILURES.md`
   - smallest explicit sparse `q=3` examples where ternary equality admits local color permutations that do not glue globally;
   - distinguish incompleteness caused by sparse domain from the complete-domain obstruction already published in Article A.

3. `NONABELIAN_PHASE_LAW.md`
   - theorem candidate and proof or counterexample;
   - exact composition law for local color permutations.

4. `UPSTREAM_MEMO_QGE3.md`
   - only theorem-level results or sharp counterexamples that materially affect the main rigidity programme.

---

## 6. Research firewall

1. **No `Z_q` assumption.** Anonymous colors have no canonical addition or cyclic order.
2. **No import from binary results without proof.** `F_2` is exceptional.
3. **No arithmetic on external carrier labels.**
4. **No modification of Articles A/B.** Cite them as frozen dependencies.
5. **No claim that a local permutation exists on a component unless all equality constraints make it well-defined.**
6. **No claim that local permutations glue globally unless overlap compatibility is proved.**
7. **Keep complete-domain and sparse-domain obstructions separate.**
8. **Do not compete with the lead binary line.** The parent line retains `alpha=beta`, Safe Minimum Extension, exposure cost, and binary deletion-symmetry.

---

## 7. Literature boundary

Compare against, at minimum:

- gain graphs and non-abelian switching;
- permutation-valued voltage/gain structures;
- coherent configurations / colored relational structures;
- switching isomorphism for multi-colored graphs;
- relational complexity / k-closures of permutation groups.

The purpose is to identify prior structure, not to force novelty. Any claim of new mathematics must be stated inside the anonymous sparse-operation model unless a wider theorem is genuinely proved.

---

## 8. Success criteria

The delegated line is successful if it produces one of the following:

- an exact non-abelian local phase transport theorem;
- a sharp no-go theorem showing why no componentwise `S_q` phase exists under the chosen reduct;
- a new arity threshold caused specifically by sparsity;
- a finite or infinite family exhibiting genuinely new multicolor extension-cost behavior;
- a theorem connecting sparse anonymous color transport to a known switching/gain structure with a precise equivalence.

A collection of examples without a structural statement is not sufficient for publication handoff.

---

## 9. Handoff to lead

Return only results that answer:

1. What is the correct local phase object for `q>=3`?
2. What is the correct compatibility law across sparse components?
3. What exactness information is lost at arity 3 and recovered at arity 4?
4. Is there a multicolor analogue of `lambda`, `beta`, or `alpha` that is mathematically natural?
5. Does the result create a new publication-scale theorem or only a future-work note?

Until such a handoff, the lead branch continues independently on the binary `alpha=beta` problem.