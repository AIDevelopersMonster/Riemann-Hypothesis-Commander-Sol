# HATTER-SOL-11 · Preliminary Literature and Novelty Audit

**Status:** preliminary external audit, 2026-09-14.  
**Purpose:** identify classical ingredients and nearest adjacent graph-factor literature before manuscript v0.2.  
**Important:** this is not yet an exhaustive systematic review.

---

## 1. Immediate conclusion

The external literature confirms that several graph-theoretic ingredients used by HATTER-SOL-11 are classical and must not be presented as new:

- `(g,f)`-factors and minimum-deficiency degree-constrained factors;
- decomposition into degree-constrained spanning subgraphs;
- `[a,b]`-factorizations;
- 1-factorization of regular graphs as a classical research area;
- reductions of degree-constrained factorization to edge coloring/matching;
- colored/multi-constraint factor problems;
- optimization over degree sequences.

The current HATTER-SOL-11 novelty claim should therefore remain at the **composed arithmetic/network level**:

1. canonical arithmetic direction-orbit refinement of the HATTER folded interface;
2. exact classification of the fold fibers;
3. exact operational visibility of those fibers under network optimization;
4. geometry-dependent collision/memory laws;
5. the resulting `3 -> 2 -> 1` orbital-memory filtration on the stated regular-factorizable hosts.

The search performed so far did **not** reveal a paper formulating this arithmetic orbital-fiber / Pareto-response / degree-controlled forgetting problem or an equivalent theorem under another name. This is only a preliminary negative search result, not proof of novelty.

---

## 2. Classical graph-factor foundations to cite

### 2.1 Minimum-deficiency `(g,f)` factors

A standard line of work studies spanning subgraphs whose degrees lie in prescribed intervals and algorithms minimizing failure of lower degree constraints.

Relevant source:

- **Algorithms for Degree Constrained Graph Factors of Minimum Deficiency**, *Journal of Algorithms* 14(1), 1993, 115--138. DOI: `10.1006/jagm.1993.1006`.

Publication use:

- cite as classical background for degree-constrained factors;
- do not describe HATTER local capacity bounds themselves as a new graph-factor concept.

### 2.2 Degree-constrained decompositions and edge coloring

Relevant source:

- Xiao Zhou, Takao Nishizeki, **Decompositions to Degree-Constrained Subgraphs Are Simply Reducible to Edge-Colorings**, *Journal of Combinatorial Theory, Series B* 75(2), 1999, 270--287. DOI: `10.1006/jctb.1998.1883`.

The paper treats decomposition problems including `(g,f)`-factorizations and gives polynomial reductions to edge coloring.

Publication use:

- cite when introducing the relationship between factorization and color/channel decomposition;
- explicitly state that HATTER's novelty is not the existence of degree-constrained graph decompositions.

### 2.3 `[a,b]`-factorization theory

Relevant reference:

- Jin Akiyama, Mikio Kano, **[a,b]-Factorizations**, in *Factors and Factorizations of Graphs: Proof Techniques in Factor Theory*, Lecture Notes in Mathematics 2031, Springer, 2011, pp. 193--218. DOI: `10.1007/978-3-642-21919-1_5`.

Publication use:

- strong background citation for regular/semi-regular factorization language;
- useful for final bibliography's graph-factor context.

### 2.4 Multiple degree constraints

Relevant source:

- **Factors with Multiple Degree Constraints in Graphs**, *SIAM Journal on Discrete Mathematics*. DOI: `10.1137/110850402`.

This work generalizes factor constraints to partitioned incident-edge classes and relates them to matching methods.

Publication use:

- nearest conceptual background for multiple local edge/channel constraints;
- HATTER should not imply that multi-channel degree constraints are new in themselves.

### 2.5 Degree-sequence optimization

Relevant source:

- Shmuel Onn, **On degree sequence optimization**, *Operations Research Letters* 48(6), 2020, 840--843. DOI: `10.1016/j.orl.2020.10.010`.

The paper considers optimization of functions over degree sequences of subgraphs and includes colored extensions.

Publication use:

- cite as nearby optimization literature;
- distinguish HATTER's exact two-coordinate Pareto boundary from general degree-sequence optimization.

### 2.6 1-factorization is deeply classical

Relevant source:

- A. G. Chetwynd and A. J. W. Hilton, **Regular Graphs of High Degree are 1-Factorizable**, *Proceedings of the London Mathematical Society* s3-50(2), 1985, 193--206. DOI: `10.1112/plms/s3-50.2.193`.

Later literature extensively studies existence and enumeration of 1-factorizations.

Publication use:

- 1-factorization must be presented purely as a hypothesis/tool;
- no novelty language around decomposing a regular host into perfect matchings.

---

## 3. Colored degree constraints — adjacent but not equivalent

A nearby modern direction studies colored-degree objectives and colored matching/factor problems. Example:

- Mariia Anapolska, Christina Buesing, Martin Comis, et al., **Minimum color-degree perfect b-matchings**, *Networks* 77(4), 2021, 477--494. DOI: `10.1002/net.21974`.

This confirms that colored local constraints and matching optimization form an established area.

Difference from HATTER-SOL-11:

- colors in that literature are graph/edge attributes or optimization constraints;
- in HATTER-SOL-11 the two channels are the image of an arithmetic direction-orbit quotient;
- the object of interest is the collision/retention of **arithmetic states** under exact network Pareto response, not only feasibility or algorithmic complexity.

This difference should be stated carefully rather than by claiming a wholly new graph-theoretic problem class.

---

## 4. Reassessment of the RFH theorem's novelty wording

The mathematical proof of `REGULAR_FACTORIZABLE_HOST_ORBITAL_MEMORY_THEOREM.md` is elementary once a 1-factorization is available:

- use complete perfect matchings plus a partial next matching to realize every admissible degree window;
- use the complementary channel to consume the remaining host edges;
- derive the exact Pareto interval.

Because factorization theory contains many stronger and more general degree-constrained decomposition results, the manuscript should **not** market the degree-window construction by itself as a major new graph theorem.

The publishable claim is instead:

> When the arithmetic forgetting fiber is inserted into this exact host response, the three intrinsic orbital states undergo a sharp, explicitly classified information transition at host degrees `P` and `P+Q`.

Thus the likely novelty is in the derived **orbital-memory filtration**, not in the factorization lemma used to prove it.

---

## 5. Arithmetic direction-orbit novelty boundary

Gaussian and Eisenstein lattice symmetries themselves are classical. Their enhanced unit groups and square/hexagonal rotational symmetries must not be claimed as new.

Likewise, symmetry orbits of primitive lattice directions are classical objects in lattice/arithmetic geometry.

The paper's claim should instead be:

> the HATTER folded capacity pair is factored through a specific symmetry-orbit datum, its fibers are classified, and those fibers are then tested through an exact graph-response functor.

That composition appears to be the distinctive contribution of the paper.

A more specialized arithmetic literature search is still required before final v1.0 to rule out an equivalent existing 'direction-orbit profile' construction under different terminology.

---

## 6. Information-loss terminology

There is broad modern literature on information loss, identifiability, graph summaries, and topology inference, but those subjects are much broader and do not by themselves anticipate the present arithmetic-network theorem.

For publication discipline:

- use `information loss`, `memory`, `forgetting`, and `observability` as mathematically defined internal terms;
- do not suggest a new general information-theoretic framework unless entropy/statistical experiments are actually introduced;
- keep the paper combinatorial/arithmetic.

---

## 7. Required bibliography additions for manuscript v0.2

At minimum, add and verify full metadata for:

1. Zhou & Nishizeki (1999), degree-constrained decompositions / edge coloring, DOI `10.1006/jctb.1998.1883`.
2. Minimum-deficiency degree-constrained graph factors (1993), DOI `10.1006/jagm.1993.1006`.
3. Akiyama & Kano (2011), `[a,b]`-factorizations, DOI `10.1007/978-3-642-21919-1_5`.
4. Multiple-degree-constraint factor paper, DOI `10.1137/110850402`.
5. Onn (2020), degree-sequence optimization, DOI `10.1016/j.orl.2020.10.010`.
6. Chetwynd & Hilton (1985), high-degree 1-factorization, DOI `10.1112/plms/s3-50.2.193`.
7. Anapolska et al. (2021), minimum color-degree perfect b-matchings, DOI `10.1002/net.21974`.
8. Classical source(s) for Tutte's 1-factor theorem and standard `(g,f)`-factor theory.
9. Classical source(s) for Gaussian/Eisenstein unit-lattice symmetries.
10. HATTER-SOL-07--10 with final Zenodo metadata.

---

## 8. Preliminary verdict

### Mathematical novelty risk

**Moderate but controllable.** The graph ingredients are classical, but the present arithmetic-interface composition and exact collision filtration were not matched by this initial search.

### Main wording correction

Do not write:

> We introduce a new theory of degree-constrained graph factorization.

Write instead:

> We use classical factorization structure to compute an exact network response for arithmetic orbital states and derive a new information-filtration law for the HATTER interface.

### Next literature-audit target

Before manuscript v1.0, perform a dedicated search in:

- graph factors / colored factors / multiobjective b-matching;
- lattice-direction orbit invariants in imaginary quadratic integer rings;
- arithmetic graph/network representations that quotient factor data by symmetry.

Only after that search should the final novelty paragraph be frozen.
