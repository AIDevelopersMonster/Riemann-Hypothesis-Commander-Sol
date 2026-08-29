# FCOA QGE3 — Final Report

**Branch:** `director/fcoa-rigidity-cost`  
**Delegated line:** sparse anonymous alphabets `q>=3`  
**Completion status:** `READY FOR COMMANDER SOL REVIEW`

---

## A. Executive verdict

\[
\boxed{\text{SHARP NO-GO THEOREM ACHIEVED}}
\]

The originally expected componentwise `S_q` phase theory is false for sparse ternary equality data when `q>=3`. The failure is sharp already for `q=3`, three carrier points, and four defined cells.

The failed model has been replaced by an exact theorem:

> the universal local transport object is the orbit of a proper coloring of a canonical T-constraint quotient; a permutation-valued phase exists exactly on the sector where the transported coloring remains in the same color-relabeling orbit.

In that phase sector the local maps form a visible-support groupoid and obey an exact noncommutative composition law. An exact global gluing theorem is also proved.

### Publication-scale verdict

**Yes, inside the anonymous sparse-operation model**, as a focused theorem/note rather than a broad new theorem about graph coloring or switching theory.

The strongest publishable point is not “nonabelian switching exists”; that is classical territory. The publishable point is the sharp failure of universal permutation phase transport, its exact reduction to proper-coloring reconstruction, and the two-stage local/gluing obstruction specific to the FCOA sparse equality reduct.

---

## B. Main mathematical result

### B1. Sharp sparse no-go theorem

For every `q>=3`, connectedness of the ordered-cell comparison graph does not imply existence of one local permutation phase.

For `q=3` the minimum sparse witness has

\[
\boxed{|G|=3,\qquad |D|=4.}
\]

Take

\[
G=\{0,1,2\},
\]

\[
D=\{(0,1),(0,2),(1,0),(1,2)\},
\]

and

\[
c(0,1)=c(0,2)=0,
\qquad
c(1,0)=1,
\qquad
c(1,2)=2.
\]

The comparison graph `Lambda(D)` is connected. The carrier involution

\[
g=(0\ 1)
\]

preserves `D` and the ternary equality reduct, but it sends the two source-color-0 cells to colors 1 and 2. Hence no map on the local visible color set can satisfy

\[
c(gp)=\phi(c(p))
\]

throughout the component.

Therefore

\[
\boxed{
\operatorname{Aut}(G;D,Q_D)
\not\subseteq
\{\text{componentwise }S_q\text{-phase transports}\}
}
\]

for `q>=3`.

Minimality at `|D|=4` is proved: a surjective three-color layer with `|D|=3` uses every color exactly once, so every domain-preserving cell permutation automatically induces a permutation of the three colors.

### B2. Correct replacement theorem

For each comparison component `C`, contract all equality edges in the comparison graph. The resulting T-constraint quotient

\[
H_T(C)
\]

has equality atoms as vertices and forced inequalities as edges. The terminal fibers induce a proper coloring

\[
\kappa_C:V(H_T(C))\to O_C.
\]

Every ternary-reduct automorphism `g` induces a quotient isomorphism and therefore a transported proper coloring

\[
\kappa_C^g.
\]

The universally defined local state is

\[
\boxed{
[\kappa_C^g]
\in
\operatorname{Col}(H_T(C))/S_O.
}
\]

A local visible-support permutation exists if and only if

\[
\boxed{[\kappa_C^g]=[\kappa_C].}
\]

Equivalently, the full color-fiber partition inside `C` must be transported to itself up to relabeling.

### B3. Nonabelian phase law in the phase sector

Whenever local phases exist,

\[
\phi_{g,C}:O_C\to O_{gC},
\]

they satisfy

\[
\boxed{
\phi_{gh,C}
=\phi_{g,hC}\circ\phi_{h,C}.
}
\]

Thus the correct phase structure is generally a groupoid of visible-support bijections. It becomes `S_q`-valued when every component sees the entire alphabet.

### B4. Exact gluing theorem

Assume local phases exist on every component and define

\[
R_g
=
\bigcup_C\operatorname{graph}(\phi_{g,C})
\subseteq O\times O.
\]

Then

\[
\boxed{
g\in\operatorname{Aut}^{\rm an}(D,c)
\iff
R_g\text{ is the graph of one }\pi\in S_O.}
\]

Equivalently:

1. local phases agree on every shared source color;
2. distinct source colors never collide at one target color across components.

Hence ternary exactness has two independent obstruction layers:

\[
\boxed{
\text{local proper-coloring ambiguity}
+
\text{inter-component gluing ambiguity}.
}
\]

---

## C. Definitions introduced

Only the following new objects are needed.

1. **T-equality atom** — a connected component of the equal-colored-edge subgraph of `Lambda(D)`.
2. **T-constraint quotient `H_T(C)`** — equality atoms contracted to vertices, with edges recording forced inequalities.
3. **Proper-coloring transport state** — the color-relabeling orbit `[kappa_C^g]` of the transported quotient coloring.
4. **Color-rigid component** — a quotient whose relevant proper coloring partition is unique up to permutation of color names.
5. **Visible-support phase groupoid** — local bijections `O_C -> O_{gC}` where they exist.
6. **Union relation `R_g`** — the union of graphs of local visible-support phases, used for exact global gluing.

No cyclic structure, additive phase, or artificial `Z_q` structure is introduced.

---

## D. Proof architecture

The dependency graph is:

\[
(D,c)
\longrightarrow
\Lambda(D)
\longrightarrow
\Lambda_{=}(D,c)
\longrightarrow
\text{T-equality atoms}
\longrightarrow
H_T(C)
\longrightarrow
\kappa_C.
\]

Then:

\[
g\in\operatorname{Aut}(G;D,Q_D)
\Longrightarrow
\bar g_C:H_T(C)\cong H_T(gC)
\Longrightarrow
\kappa_C^g.
\]

Next:

\[
[\kappa_C^g]=[\kappa_C]
\Longleftrightarrow
\text{local visible-support phase exists}.
\]

Where phases exist:

\[
\phi_{gh,C}
=
\phi_{g,hC}\circ\phi_{h,C}.
\]

Finally:

\[
\{\phi_{g,C}\}_C
\Longrightarrow
R_g
\Longrightarrow
\bigl(R_g\text{ is a permutation graph}\bigr)
\Longleftrightarrow
\text{global anonymous phase}.
\]

The sharp no-go witness attacks the first attempted implication directly:

\[
\Lambda(D)\text{ connected}
\centernot\Longrightarrow
[\kappa_C^g]=[\kappa_C].
\]

---

## E. Counterexamples and failure modes

### E1. False conjecture: one `S_q` phase per connected component

**False.** Minimum `q=3` witness: `|G|=3`, `|D|=4`.

### E2. False intuition: the issue is only disconnected sparse geometry

**False.** The minimum witness already has connected `Lambda(D)`.

### E3. False intuition: the issue is only vacuous `Q_D`

**False.** Exhaustive small search finds connected non-vacuous ternary failures as well; on `|G|=3` the first such witness appears at six defined cells.

The six-cell minimum is currently recorded as computational evidence, not promoted to a theorem without a separate proof.

### E4. False gluing rule: overlap agreement alone is enough

**False in general.** If supports are partial, different source colors occurring in different components can be mapped to the same target color without violating restriction agreement on overlaps.

A second condition — cross-support injectivity — is necessary.

### E5. False generalization: binary cocycle becomes an `S_q` cocycle automatically

**False.** For `q>=3`, a permutation phase may not exist at all. The obstruction precedes noncommutativity.

---

## F. Computational evidence

A reproducible script is stored at

`QGE3/verify_qge3.py`.

It exhaustively checks the small `q=3`, `|G|=3` search needed for the witness boundary.

### Exhaustive claims used

- no connected surjective counterexample exists at `|D|=3`;
- a connected counterexample exists at `|D|=4`;
- a connected non-vacuous-`Q_D` counterexample exists at `|D|=6`.

The first boundary also has an independent mathematical proof and therefore does not rely on computation.

### Search normalization

- carrier labels are exhaustively permuted;
- all off-diagonal domains of the stated size are considered;
- all surjective colorings onto `{0,1,2}` are considered;
- color-label quotient normalization is not required for correctness because the search is small and exhaustive;
- every carrier permutation preserving `D` is checked;
- exact ternary-reduct preservation and anonymous-phase realizability are tested directly.

No random search is used for the promoted minimum theorem.

---

## G. Literature comparison and novelty boundary

### Classical prior structure

The following are established areas and are not claimed new:

- unique graph colorability;
- multicolor switching;
- gain graphs and group-valued switching;
- partial-bijection groupoids;
- coherent configurations and colored relational structures;
- relational complexity and bounded-arity reconstruction.

Relevant references include:

- Harary–Hedetniemi–Robinson, *Uniquely colorable graphs*, JCT 6 (1969), DOI `10.1016/S0021-9800(69)80086-4`;
- Cameron–Tarzi, *Switching with more than two colours*, EJC 25 (2004), DOI `10.1016/S0195-6698(03)00097-0`;
- Higman, *Coherent configurations. I*, Geometriae Dedicata 4 (1975), DOI `10.1007/BF00147398`;
- Cherlin, *On the relational complexity of a finite permutation group*, J. Algebraic Combin. 43 (2016), DOI `10.1007/s10801-015-0636-8`.

### Model-specific new content

The result that appears new **inside the anonymous sparse-operation model** is the exact reduction

\[
\text{sparse ternary equality transport}
\rightsquigarrow
\text{proper-coloring reconstruction of }H_T(C),
\]

plus the sharp FCOA counterexample and the exact two-stage local/gluing criterion.

The gain/switching analogy begins only after a local phase exists; it does not supply that existence.

No broad priority claim beyond this model is recommended.

---

## H. Relationship to Articles A and B

### Article A — DOI `10.5281/zenodo.22157403`

Used as a frozen foundation for the complete-domain arity transition:

\[
q=2:\ k_{exact}=3,
\qquad
q\ge3:\ k_{exact}=4.
\]

QGE3 does not change that result. It explains the sparse `q>=3` mechanism more finely: ternary data expose only a constraint graph, while four-ary arbitrary-cell equality exposes the full terminal-fiber partition.

### Article B — DOI `10.5281/zenodo.22159246`

Used as a frozen foundation for the sparse binary component-phase theory.

QGE3 identifies why the binary theorem does not generalize formally. In the binary case, the relevant connected quotient has only one proper two-coloring orbit up to swapping colors; hence the local discrepancy is automatically a bit. For `q>=3`, several inequivalent proper-coloring states may survive in one connected component.

Thus Article B becomes the uniquely color-rigid binary special case of the wider reconstruction picture, without any modification to its statements.

---

## I. Recommended upstream action

\[
\boxed{\text{MERGE THEOREM INTO MAIN RIGIDITY THEORY}}
\]

The delegated line has met its completion rule by producing both a sharp no-go theorem and a mathematically natural replacement object.

After hostile Commander Sol review, a **separate focused publication** is justified if desired. The strongest title-level message would be that sparse multicolor anonymous equality is governed by proper-coloring transport rather than a universal nonabelian phase cocycle.

A `COST_THEORY.md` file was deliberately **not** created. The binary cost `lambda` counts synchronization of one bit per component. QGE3 shows that for `q>=3` the local state may be an entire proper-coloring orbit, so copying binary cost definitions would be mathematically premature.

---

## J. Open obligations

The delegated first-stage problem is solved, but the following questions remain genuinely worthwhile.

1. **Characterize color-rigid T-quotients intrinsic to operation domains.** Which sparse domain geometries force unique colorability of `H_T(C)`?
2. **Find sharp carrier/domain bounds for non-vacuous failures.** The `|G|=3, |D|=6` non-vacuous boundary currently has exhaustive computational evidence; a short proof would strengthen publication presentation.
3. **Develop a natural multicolor cost only after choosing the state space.** Candidate cost should measure how many new equality comparisons or operation cells collapse realized proper-coloring orbits and then enforce global gluing.
4. **Study Model E extension cost for `q>=3`.** Fixed-domain exactness is trivial under four-ary arbitrary-cell equality, but actual sparse cell extension may still create carrier symmetries, analogously to Article B.
5. **Classify full-support phase sectors.** When every component sees all colors and is color-rigid, the local law is genuinely `S_q`-valued; this is the cleanest place to compare with nonabelian switching/gain structures.
6. **Check whether the T-constraint quotient equivalence has appeared explicitly in partition-reconstruction literature.** Current literature comparison supports model-specific novelty but not a broad novelty claim.

---

# Completion marker

\[
\boxed{\text{READY FOR COMMANDER SOL REVIEW}}
\]
