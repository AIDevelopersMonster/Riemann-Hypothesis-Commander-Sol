# H19-13 · Prior-Art and Novelty Audit

Status: **FIRST HOSTILE AUDIT / CLAIM NARROWING REQUIRED**

Date: 20 September 2026.

## 1. Audit purpose

H19 has now accumulated three kinds of material:

1. exact finite/compiler observations on DIRECT12, PREFIX19 and NIELSEN12;
2. elementary observer/partition formalism;
3. a parameterized temporal/spatial calibration family.

Before manuscript assembly, these layers must be separated from classical
decision-tree, branching-program, compiler-equivalence and equality-saturation
theory.

The audit question is not whether H19 terminology is new.

The question is:

> Which H19 claims remain specific after the known theory is stated in its own
> standard language?

---

## 2. Decision trees, branching programs and circuits

Classical complexity theory already compares:

- decision trees;
- branching programs;
- formulas;
- Boolean circuits;
- time/space trade-offs;
- restricted branching-program complexity.

Relevant classical references include:

1. Ingo Wegener,
   *Branching Programs and Binary Decision Diagrams: Theory and Applications*,
   SIAM, especially the chapter comparing branching programs, decision trees,
   formulas and circuits.

2. Ingo Wegener,
   "Time-space trade-offs for branching programs",
   *Journal of Computer and System Sciences* 32(1), 1986, 91-96,
   DOI 10.1016/0022-0000(86)90004-8.

3. Classical work on optimal decision trees / one-time-only branching programs
   already contains exponential separations between restricted representation
   models.

### Audit consequence

H19-10's address-selection family is **not a novelty theorem about complexity
models**.

It remains useful as an exact calibration lemma for the frozen H19
presentation-preserving compiler discipline:

\[
D_{\rm query}=n+1,
\qquad
N_{\rm spatial}=2^{D_{\rm query}}-1
\]

under \(\Pi_{\rm DAG}\).

Publication wording must therefore be:

> calibration family / construction accounting inside the declared
> spatialization discipline,

not:

> new exponential separation between adaptive computation and circuits.

---

## 3. Observational equivalence

Observational equivalence is a classical semantic idea across programming
languages and logic programming.

Different observation families induce different equivalence relations and
different semantic quotients.

### Audit consequence

H19-06/H19-09 do not claim novelty for:

\[
M_1\sim_O M_2
\iff
O(M_1)=O(M_2),
\]

nor for the fact that a finer observer refines equivalence classes.

The pullback-equivalence / kernel-relation formalism is foundational
bookkeeping.

The H19-specific question is empirical and structural:

> Which equivalence classes are induced by concrete synthesis observables on a
> controlled E0-equivalent family, and how do those classes change along a
> real compiler/technology flow?

---

## 4. Compiler correctness and translation validation

Compiler optimization correctness and translation validation already study
whether transformed programs preserve semantics.

Representative prior work includes equivalence checking of optimized programs
and validation of compiler transformations such as constant folding,
reassociation, common-subexpression elimination, code motion and branch
optimization.

### Audit consequence

H19 must not describe E0 semantic preservation as a new compiler-theory
concept.

E0 is a controlled experimental contract that permits presentation-sensitive
comparison after semantic equivalence has been frozen.

---

## 5. Equality saturation and e-graphs

Equality saturation represents many equivalent expressions/programs in one
structure and delays destructive choice of a single optimized form.

The foundational compiler work of Tate, Stepp, Tatlock and Lerner introduced
equality saturation as an alternative to sequential destructive optimization.

More recent work pushes this idea across compiler abstraction levels.

A 2026 line on **persistent e-graphs as a compiler abstraction** explicitly
targets retaining equality information while code passes through multiple IR
levels.

### Audit consequence

H19 must not claim as novel:

- that compilers may forget structural alternatives;
- that equivalence information can be preserved deliberately;
- that optimization order matters;
- that multiple equivalent representations can coexist in a compiler IR.

H19's module-preserving/open-flow experiment is therefore an experimental
control, not a new general compiler paradigm.

---

## 6. Partition lattices

The lattice of partitions of a finite set is classical.

The statements

\[
O_a\preceq O_b
\Longrightarrow
\mathcal P_{O_a}\preceq\mathcal P_{O_b}
\]

and the reduction of pairwise equivalence to partition blocks are elementary.

### Audit consequence

H19-12 uses the partition lattice as a language.

It does not claim the lattice construction itself as new.

---

## 7. What remains specifically H19

After removing the classical layers, the strongest H19-specific content is the
controlled composition of the following ingredients.

### A. One frozen mathematical task

The H18 restricted-12 task and external E0 contract are fixed.

### B. Several exact mathematical presentations

The same task is realized by source factorizations including

\[
DIRECT12,\quad PREFIX19,\quad NIELSEN12.
\]

These are not arbitrary compiler rewrites introduced after the fact; they are
mathematically motivated observer factorizations.

### C. Matched compiler tower

The presentations are passed through one frozen compilation methodology.

### D. Multi-resolution observer atlas

H19 records not only final area but partitions/frontiers under:

- source-operation observers;
- cell count;
- cell histogram;
- wire count/profile;
- preserved module instances;
- ABC Boolean image;
- later physical FPGA coordinates.

### E. Measured re-separation

For DIRECT12 and PREFIX19:

\[
24\ne19
\]

at source,

\[
4919=4919
\]

at post-proc cells,

\[
63719=63719
\]

at post-techmap Boolean cells,

but

\[
60374\ne60383
\]

after ABC-fast.

At the same intermediate stages, wire observables still distinguish the pair.

Thus the experimentally correct description is not information destruction but
**observer-relative hiding and re-exposure**.

### F. Frontier migration

For the frozen pair, the minimal declared visible observer moves as

\[
O_{\rm comp}
\to
O_{\rm wiretot}
\to
O_{\rm wiretot}
\to
O_{\rm celltot}.
\]

### G. Family-level partition dynamics

For the three-presentation family, the cell observer produces

\[
\{\{D,P\},\{N\}\}
\]

at post-proc and post-techmap, then

\[
\{\{D\},\{P\},\{N\}\}
\]

after ABC-fast.

This is a concrete compiler-generated partition trajectory on one
mathematically controlled E0 family.

---

## 8. Current novelty assessment

### Clearly classical / background

Do not claim novelty for:

- decision-tree versus circuit comparisons;
- branching-program complexity;
- multiplexer/address-selection complexity;
- observational equivalence;
- pullback equivalence relations;
- partition lattices;
- compiler semantic preservation;
- equality saturation;
- e-graphs;
- phase-ordering problems.

### Potentially publishable H19-specific synthesis

Subject to a deeper literature search, the plausible contribution is:

> a reproducible experimental/theoretical framework for tracking how
> distinctions among mathematically motivated E0-equivalent presentations are
> merged, hidden, re-exposed and physically realized across a fixed compiler
> tower, represented by observer frontiers and presentation-partition
> trajectories.

This wording is intentionally narrower than "new compiler complexity theory".

---

## 9. Publication-threshold correction

The previous status "theoretical publication threshold crossed" was too strong
before prior-art separation.

H19-09 and H19-10 are mathematically correct but their abstract cores are too
close to elementary observer theory and classical branching-program/circuit
theory to carry novelty by themselves.

Therefore the correct status after this audit is:

\[
\boxed{
\text{FRAMEWORK THRESHOLD CROSSED;}
\quad
\text{NOVELTY/PUBLICATION THRESHOLD NOT YET SECURE.}
}
\]

A publication candidate becomes justified if at least one of the following is
closed convincingly:

1. a nontrivial theorem specifically about compiler-induced
   presentation-partition dynamics beyond elementary order theory;
2. a predictive source invariant that correctly predicts visibility/frontier
   changes across several controlled E0 presentation families;
3. a robust cross-tool or cross-technology persistence theorem/experiment
   showing a stable presentation-survival law not reducible to one compiler
   run;
4. a physical visibility atlas whose structure supports a nontrivial,
   reproducible law.

---

## 10. Immediate research direction

The strongest next target is not another classical decision-tree separation.

Use deterministic full-state transport to define the **latent partition gap**:

\[
\mathcal P^{\rm full}_i
\preceq
\mathcal P^{O}_i,
\]

where the full-state partition can only coarsen along a deterministic compiler
tower, while an observed partition may split or merge.

Then quantify the presentations that are merged only by the observer but
remain distinct internally.

For the current H19 family this gap is already nonzero at post-proc and
post-techmap for the cell observer, and disappears at ABC-fast.

This is the next H19 theorem layer to formalize and test.
