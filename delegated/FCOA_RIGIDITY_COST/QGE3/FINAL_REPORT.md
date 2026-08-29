# FCOA QGE3 — Final Report

**Branch:** `director/fcoa-rigidity-cost`  
**Delegated line:** sparse anonymous alphabets `q>=3`  
**Completion status:** `READY FOR COMMANDER SOL REVIEW`

## A. Executive verdict

\[
\boxed{\text{SHARP NO-GO THEOREM ACHIEVED}}
\]

The naive sparse multicolor analogue of the binary Componentwise Phase Theorem is false: for `q>=3`, even one connected comparison component need not carry a well-defined `S_q` phase.

The failed model is replaced by an exact theorem: the universal local transport object is the orbit of a proper coloring of a canonical T-constraint quotient. A permutation-valued phase exists exactly when the transported proper coloring remains in the original color-relabeling orbit.

On that phase-admissible sector, the local maps form a visible-support groupoid with an exact noncommutative composition law and an exact global gluing criterion.

**Publication-scale verdict:** yes inside the FCOA sparse anonymous-operation programme, after independent hostile audit and a deeper priority search. No broad novelty claim about switching, gain graphs, or graph coloring is made.

---

## B. Main mathematical result

### B1. Sharp sparse q=3 no-go theorem

There is a connected sparse `q=3` witness with

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

and temporary color names

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

preserves `D` and the ternary equality reduct, but would require simultaneously

\[
0\mapsto1
\qquad\text{and}\qquad
0\mapsto2.
\]

Hence no local color function exists. In this witness

\[
\boxed{
|\operatorname{Aut}(G;D,Q_D)|=2,
\qquad
|\operatorname{Aut}^{\rm an}(D,c)|=1.
}
\]

The domain size is optimal: surjectivity forces `|D|>=3`, and with exactly three cells every color occurs once, so any domain permutation automatically induces a permutation of the three colors. Thus

\[
\boxed{|D|_{\min}=4.}
\]

A separate six-cell witness shows that failure persists with nonempty `Q_D`.

### B2. Correct universal local theorem

For each comparison component `C`, contract the equal-comparison edges of `Lambda(D)` into **T-equality atoms** and form the quotient graph

\[
H_T(C).
\]

The terminal fibers induce a proper coloring

\[
\kappa_C:V(H_T(C))\to O_C.
\]

Every ternary-reduct automorphism induces a quotient isomorphism and transports `kappa_C` to another proper coloring. A local visible-support phase exists exactly when

\[
\boxed{[\kappa_C^g]=[\kappa_C]}
\]

modulo anonymous color relabeling.

Therefore

\[
\boxed{
\text{the universal local state is a proper-coloring orbit, not an }S_q\text{ element.}
}
\]

### B3. Conditional nonabelian phase law

Whenever local phases exist,

\[
\phi_{g,C}:O_C\to O_{gC},
\]

they are unique on visible supports and satisfy

\[
\boxed{
\phi_{gh,C}
=\phi_{g,hC}\circ\phi_{h,C}.
}
\]

The intrinsic object is thus a groupoid of visible-support bijections. It becomes `S_q`-valued only in the full-support sector.

### B4. Exact gluing theorem

For a phase-admissible automorphism `g`, define

\[
R_g
=
\bigcup_C\operatorname{graph}(\phi_{g,C})
\subseteq O\times O.
\]

Then

\[
\boxed{
\{\phi_{g,C}\}_C\text{ glue to one global }\pi_g\in S_O
\iff
R_g\text{ is the graph of a permutation of }O.
}
\]

The two independent obstruction types are source disagreement and target collision. In the full-support sector this reduces to equality of all component phases.

---

## C. Definitions introduced

1. **T-equality atom** — a connected component of the equal-comparison subgraph of `Lambda(D)`.
2. **T-constraint quotient `H_T(C)`** — equality atoms as vertices, with inequality adjacency inherited from the comparison graph.
3. **Proper-coloring transport state `[kappa_C]`** — the hidden color partition modulo color-name permutation.
4. **Phase-admissible pair `(g,C)`** — a reduct automorphism/component pair admitting a visible-support bijection.
5. **Visible-support phase groupoid** — arrows `O_C -> O_{gC}` where phases exist.
6. **Global phase relation `R_g`** — the union of local phase graphs.
7. **Full-support abstract phase-link number `lambda_q^ph`** — synchronization cost for realized `S_q` phase tuples.

No cyclic or additive structure is attached to anonymous colors.

---

## D. Proof architecture

\[
(D,c)
\to
\Lambda(D)
\to
\text{equal-comparison subgraph}
\to
\text{T-equality atoms}
\to
H_T(C)+\kappa_C.
\]

Then

\[
g\in\operatorname{Aut}(G;D,Q_D)
\to
\text{transported proper coloring }\kappa_C^g.
\]

The first obstruction is

\[
[\kappa_C^g]\ne[\kappa_C],
\]

in which case no local phase exists. If the orbits agree, one obtains `phi_{g,C}` and then the composition law. Finally the family of local phases is tested by `R_g`; it is globally anonymous exactly when `R_g` is a permutation graph.

---

## E. Counterexamples and failure modes

The following tempting formulations are false for `q>=3`:

1. connected `Lambda(D)` implies one `S_q` phase per component;
2. every ternary-reduct automorphism induces a visible-color permutation;
3. the multicolor theory is obtained by replacing `F_2` by `S_q`;
4. all sparse defects are inter-component gluing defects;
5. overlap agreement of partial phases alone guarantees gluing;
6. the binary synchronization cost can be copied unchanged.

The correct failure taxonomy is:

- complete-domain arity obstruction from Article A;
- sparse vacuity;
- connected proper-coloring ambiguity;
- partial-support/inter-component gluing ambiguity.

---

## F. Computational evidence

A reproducible script is included:

`QGE3/verify_qge3.py`.

It exhaustively checks the `q=3`, `|G|=3` small sector used for the first witness boundary. The theorem-level minimum `|D|=4` also has an independent direct proof and therefore does not rely on computation.

The observed first connected non-vacuous failure on three carrier points occurs at six defined cells; that six-cell minimality remains computational evidence until independently audited.

---

## G. Literature comparison and novelty boundary

Classical prior art includes:

- Cameron–Tarzi multicolor switching;
- Zaslavsky gain/biased graphs and group-valued switching;
- Gross–Tucker permutation voltage assignments;
- coherent configurations and colored relational structures;
- Wielandt `k`-closures and relational complexity;
- unique graph colorability.

Therefore no novelty is claimed for nonabelian switching, permutation-valued labels, groupoid composition, or unique colorability themselves.

The safe model-specific theorem package is the exact chain

\[
\boxed{
\text{sparse ternary anonymous equality}
\to
\text{equality-atom quotient}
\to
\text{proper-coloring transport}
\to
\text{sharp local phase no-go}
\to
\text{conditional support-bijection groupoid}
\to
\text{permutation-graph gluing criterion}.
}
\]

Broader priority language is deferred.

---

## H. Relationship to Articles A and B

**Article A**, DOI `10.5281/zenodo.22157403`, remains frozen and supplies the complete-domain arity transition

\[
q=2:k_{exact}=3,
\qquad
q\ge3:k_{exact}=4.
\]

QGE3 explains the sparse mechanism more finely: ternary data expose only a constraint graph whose proper coloring may not be reconstructible.

**Article B**, DOI `10.5281/zenodo.22159246`, remains frozen and supplies the sparse binary component-phase theory. QGE3 isolates why binary is exceptional: after equality contraction, connected binary comparison geometry has a unique two-color partition up to exchange, while multicolor quotients may have inequivalent proper-coloring states.

---

## I. Recommended upstream action

\[
\boxed{\text{MERGE THEOREM INTO MAIN RIGIDITY THEORY}}
\]

and, after hostile audit, prepare a separate focused continuation paper.

The paper should lead with the sharp `|G|=3, |D|=4` no-go theorem, then present the T-constraint quotient, proper-coloring transport theorem, conditional nonabelian phase law, and exact gluing theorem.

`COST_THEORY.md` **has been created**, but only for the mathematically safe full-support phase sector. It defines

\[
\lambda_q^{\rm ph}
\]

and proves

\[
\boxed{0\le\lambda_q^{\rm ph}(D,c)\le(q-1)(r-1)}.
\]

It explicitly does **not** define a real-cell multicolor `alpha_q` or assert an analogue of the binary `alpha<=lambda` conjecture.

---

## J. Open obligations

1. Determine the exact extremal synchronization number `L_q(r)` for point-image constraints on arbitrary tuples in `S_q^r`.
2. Develop a real operation-cell repair theory only after controlling local proper-coloring ambiguity.
3. Prove or independently audit the six-cell non-vacuous minimum.
4. Characterize color-rigid T-quotients arising from actual ordered-cell domains.
5. Deepen the literature equivalence audit for edge-colored reducts and switching-isomorphism formulations.

None of these blocks the main no-go and replacement theorems.

---

# Completion marker

\[
\boxed{\texttt{READY FOR COMMANDER SOL REVIEW}}
\]
