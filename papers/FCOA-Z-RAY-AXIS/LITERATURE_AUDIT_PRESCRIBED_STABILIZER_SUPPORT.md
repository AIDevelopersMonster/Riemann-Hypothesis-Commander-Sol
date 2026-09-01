# Hostile Literature Audit — Prescribed-Stabilizer Support in FCOA-Z

Status: publication audit v1.0  
Date: 2026-09-01

This audit tests the post-publication FCOA-Z branch-coherence and partition-support results against the closest established literature in permutation groups, relation groups, distinguishing theory, point-determining graphs, 2-closure/orbital theory, and minimum graph-realization problems.

The audit is intentionally conservative. It does **not** claim that the abstract notion

\[
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\}
\]

has never appeared in equivalent language. The question is narrower and publication-oriented:

> Are the exact FCOA theorems, resource laws, and partition-orbital solver obtained here already standard consequences explicitly present in the closest literature?

The answer after this audit is:

\[
\boxed{\text{No direct duplication found.}}
\]

However, several ingredients are classical and must be cited rather than presented as new.

---

## 1. FCOA framework citation

Any publication from this branch must cite the framework in both abstract and bibliography:

A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026, DOI `10.5281/zenodo.22164246`.

The concrete FCOA structure used in the present branch is a terminal-valued partial operation on a fixed active carrier whose values reduce a declared active automorphism group while the connection/partition information itself is erased from the carrier signature.

---

## 2. Regular sets and trivial set-stabilizers

### Classical line

A subset `Delta` in a `G`-set is regular when its setwise stabilizer is trivial. This is a standard power-set action problem.

Key references:

- D. Gluck, *Trivial Set-Stabilizers in Finite Permutation Groups*, Canadian Journal of Mathematics 35 (1983), 59–67. DOI `10.4153/CJM-1983-005-2`.
- L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society, 2026. DOI `10.1112/blms.70201`.

Sabatini explicitly treats set-stabilizers as stabilizers of subsets in the power-set action and studies existence of subsets whose stabilizers have controlled orbit/derived structure.

### Overlap with FCOA

The FCOA quantity `m_G(H;S)` contains the regular-set problem as the special case

\[
H=1.
\]

Thus the underlying language of setwise stabilizers is classical.

### Difference

The present programme:

1. prescribes an arbitrary exact target subgroup `H`, usually nontrivial;
2. fixes the ambient `G`-set `S` (often a natural ordered-pair orbit);
3. minimizes the cardinality/weight of the chosen support;
4. interprets that support as value-memory cost in an FCOA operation.

The regular-set literature does not by itself supply the exact wreath-coherence support formulas or the partition-orbital solver proved here.

### Audit verdict

`CLASSICAL FOUNDATION — NOT A NOVELTY CLAIM.`

---

## 3. Subgroup-relative distinguishing number

### Classical line

Alikhani and Soltani define

\[
D_{\Gamma,H}(X),
\]

the minimum number of labels for a labeling whose label-preserving elements of `Gamma` all lie in `H`.

Reference:

- S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, arXiv:1701.00141; later Journal of Information and Optimization Sciences 43 (2022), 311–321, DOI `10.1080/02522667.2021.2003011`.

Their definition is explicitly a **containment** condition:

\[
\operatorname{Stab}_{\Gamma}(\text{labeling})\le H.
\]

### Overlap with FCOA

Both theories ask for controlled residual symmetry rather than necessarily trivial residual symmetry.

### Difference

The FCOA prescribed-support quantity asks for

\[
\operatorname{Stab}_{G}(F)=H
\]

**exactly**, not merely a subgroup of `H`, and minimizes support size/weight rather than number of labels.

The two resources are independent: two labels can be sufficient while support cardinality still carries a nontrivial extremal problem.

### Audit verdict

`CLOSEST DISTINGUISHING-THEORY NEIGHBOR, BUT NOT EQUIVALENT.`

The paper must cite this work prominently and state the exact-vs-contained stabilizer distinction explicitly.

---

## 4. Wreath-product distinguishing theory

### Classical line

Melody Chan determined distinguishing numbers for direct and wreath product actions.

Reference:

- M. Chan, *The distinguishing number of the direct product and wreath product action*, Journal of Algebraic Combinatorics 24 (2006), 331–345. DOI `10.1007/s10801-006-0006-7`.

### Overlap with FCOA

The FCOA branch groups

\[
A\wr S_b
\]

are standard natural imprimitive wreath-product actions, and symmetry breaking on such actions is a classical subject.

### Difference

Chan minimizes the **number of colors** needed to destroy all nontrivial symmetry (or characterizes distinguishing colorings). The present FCOA results instead prescribe structured residual groups such as

\[
\Delta A\times S_b
\]

or

\[
A^{\mathcal P}\rtimes K_{\mathcal P}
\]

and determine exact pair-support costs, including

\[
m_{A\wr S_b}(\Delta A\times S_b;S_\times)=b(b-1)t
\]

for transitive `A` of degree `t`.

### Audit verdict

`CLASSICAL WREATH CONTEXT; EXACT SUPPORT LAW NOT FOUND THERE.`

---

## 5. Relation groups and automorphism groups of relations

### Classical line

A permutation group is a relation group if it is the full automorphism group of a suitable relation/hypergraph. The theory is tied to orbit closure and Boolean-function symmetry groups.

Key references:

- F. Dalla Volta, J. Siemons, *Orbit equivalence and permutation groups defined by unordered relations*, Journal of Algebraic Combinatorics 35 (2012), 547–564. DOI `10.1007/s10801-011-0313-5`.
- M. Grech, A. Kisielewicz, *Orbit closed permutation groups, relation groups, and simple groups*, Journal of Algebraic Combinatorics 57 (2023). DOI `10.1007/s10801-022-01214-2`.

### Overlap with FCOA

The partition-only reduction

\[
d(\mathcal P)=\min\{|R|:R\subseteq\Omega_b^{(2)},\ \operatorname{Aut}(R)=K_{\mathcal P}\}
\]

is a constrained relation-realization problem.

### Difference

The established relation-group question is primarily whether a permutation group is representable as the full automorphism group of some relation and how relation/closure classes behave.

The FCOA problem fixes:

1. the specific permutation representation `K_P <= S_b`;
2. the relation arity (`2`, directed and loopless);
3. the allowed support as a union of orbitals of `K_P`;
4. the objective: minimize the total number/weight of selected ordered pairs;
5. the FCOA lift cost `t^2 d(P)`.

No direct formula or exact partition-stabilizer orbital optimization matching this package was located.

### Audit verdict

`VERY CLOSE STRUCTURAL NEIGHBOR; EXISTENCE THEORY IS CLASSICAL, WEIGHTED FIXED-ACTION OPTIMIZATION IS DISTINCT.`

---

## 6. 2-closure and orbital digraphs

### Classical line

Wielandt's 2-closure of a permutation group is the largest subgroup of the symmetric group having the same orbits on ordered pairs. Automorphism groups of colored digraphs are 2-closed.

Reference:

- M. W. Liebeck, C. E. Praeger, J. Saxl, *On the 2-Closures of Finite Permutation Groups*, Journal of the London Mathematical Society 37 (1988), 241–252. DOI `10.1112/jlms/s2-37.2.241`.

Modern treatments continue to use orbitals and 2-closure as the natural framework for binary relational representations.

### Overlap with FCOA

The exact partition-only solver is explicitly orbital:

\[
R=\bigcup_{i:y_i=1}O_i,
\]

where the `O_i` are `K_P`-orbitals on ordered pairs.

The condition that a union of orbitals have full automorphism group exactly `K_P` is a concrete 2-closure/orbital problem.

### Difference

2-closure theory does not by itself optimize the **weight of a subcollection of orbitals** whose uncolored union already has exact automorphism group `K_P`.

The present Orbital XOR-Separation Program is precisely this extra optimization layer for the partition-stabilizer family.

### Audit verdict

`FOUNDATIONAL FRAMEWORK IS CLASSICAL; OPTIMAL ORBITAL SUBSELECTION IS THE FCOA-SPECIFIC CONTRIBUTION.`

---

## 7. Point-determining / twin-free graph and digraph theory

### Classical line

Point-determining (twin-free) graphs and digraphs separate vertices by their neighborhoods/incidence signatures.

Key references:

- D. P. Sumner, *Point determination in graphs*, Discrete Mathematics 5 (1973), 179–187. DOI `10.1016/0012-365X(73)90109-X`.
- R. C. Entringer, L. D. Gassman, *Line-critical point determining and point distinguishing graphs*, Discrete Mathematics 10 (1974), 43–55. DOI `10.1016/0012-365X(74)90019-3`.
- P. Hell, C. Hernández-Cruz, *Point determining digraphs, {0,1}-matrix partitions, and dualities in full homomorphisms*, Discrete Mathematics 338 (2015), 1755–1762. DOI `10.1016/j.disc.2014.12.001`.

### Overlap with FCOA

The forbidden-transposition criterion in `PARTITION_ONLY_EXACT_TWIN_SOLVER.md` is a weighted quotient/twin-separation condition: two points that are not allowed to be permuted by the target group must have distinguishable incidence behavior in the chosen orbital union.

### Difference

Classical point-determining theory usually treats individual graph vertices and neighborhood equality. Here:

- variables are entire partition-stabilizer orbitals;
- weights are orbital cardinalities;
- many point transpositions are intentionally allowed because they lie in `K_P`;
- the exact target automorphism group is nontrivial;
- there is an additional singleton macro-swap obstruction not captured by ordinary pairwise twin separation alone.

### Audit verdict

`THE TWIN IDEA IS CLASSICAL; THE WEIGHTED ORBITAL QUOTIENT AND MACRO-SWAP COMPLETION MUST NOT BE PRESENTED AS THE INVENTION OF TWIN-FREENESS.`

---

## 8. Minimum graph realization of a prescribed abstract group

### Classical line

There is a substantial literature minimizing the size or edge count of graphs with a given abstract automorphism group.

Examples:

- D. J. McCarthy, L. V. Quintas, *A stability theorem for minimum edge graphs with given abstract automorphism group*, Transactions of the AMS 208 (1975), 27–39. DOI `10.1090/S0002-9947-1975-0369148-4`.
- L. Babai, A. J. Goodman, L. Lovász, *Graphs with Given Automorphism Group and Few Edge Orbits*, European Journal of Combinatorics 12 (1991), 185–203. DOI `10.1016/S0195-6698(13)80085-6`.
- L. Babai, A. J. Goodman, *Subdirectly Reducible Groups and Edge-Minimal Graphs with Given Automorphism Group*, Journal of the London Mathematical Society 47 (1993), 417–432. DOI `10.1112/jlms/s2-47.3.417`.
- D. Deligeorgaki, *Smallest graphs with given automorphism group*, Journal of Algebraic Combinatorics 56 (2022), 609–633. DOI `10.1007/s10801-022-01125-2`.

### Overlap with FCOA

Both minimize relational support subject to an automorphism-group constraint.

### Difference

The classical minimum-representation literature generally fixes an **abstract group up to isomorphism** and is free to choose the graph representation and sometimes even the number of vertices.

The FCOA partition problem fixes the concrete action

\[
K_{\mathcal P}\le S_b
\]

on the existing branch carrier and minimizes a directed binary relation inside that representation, with the further constraint of orbital invariance.

Therefore those results do not directly determine `d(P)`.

### Audit verdict

`IMPORTANT ADJACENT EXTREMAL LITERATURE; NOT A DIRECT DUPLICATE.`

---

## 9. Set-stabilizers with prescribed qualitative properties

### Recent line

Sabatini (2026) studies subsets whose set-stabilizers have bounded orbit lengths / derived length, rather than insisting that the stabilizer be trivial.

This is important because it shows that **nontrivial target stabilizers** are unquestionably part of current permutation-group research.

### Difference

The target in that work is a qualitative property of the stabilizer, not a prescribed exact subgroup `H`, and there is no fixed-action support-minimization invariant corresponding to the present wreath/partition formulas.

### Audit verdict

`CURRENTLY ACTIVE NEIGHBOR; CITE TO AVOID OVERSTATING THE GENERAL IDEA OF SEEKING NONTRIVIAL SET-STABILIZERS.`

---

## 10. Complexity analogues

### Nearby classical problems

- Minimum Test Cover is NP-hard.
- Minimum base size for permutation groups is NP-hard.
- graph/digraph symmetry breaking and distinguishing problems have their own complexity literature.

### Why this does not settle our complexity question

The FCOA Orbital XOR-Separation Program has highly constrained clauses generated by partition-stabilizer orbital comparisons. It is not an arbitrary Test Cover or arbitrary Boolean CSP instance.

Therefore no hardness claim is justified merely by analogy.

### Audit verdict

\[
\boxed{\text{Complexity classification remains open in this branch.}}
\]

Do **not** claim NP-hardness until an explicit reduction respecting the partition-orbital structure is proved.

---

## 11. Claim-by-claim novelty discipline

### Claim A — `m_G(H;S)` as an abstract invariant

**Status:** use cautiously.

The exact notation and packaging were not found in the searched literature, but the underlying orbit-type question “find a subset with stabilizer exactly `H`” is a natural group-action concept. Do not claim universal invention of the abstract idea.

Safe wording:

> We use the prescribed-stabilizer support quantity `m_G(H;S)` to organize the FCOA value-memory problem.

Avoid:

> We introduce the first ever notion of minimizing a subset with prescribed stabilizer.

### Claim B — index-two formula

\[
m_G(H;S)=\min\{|O|:O\in H\backslash S,\ qO\neq O\}
\]

for normal index-two `H`.

**Status:** elementary consequence of quotient action. Treat as a lemma/organizational tool, not a major novelty claim.

### Claim C — global wreath coherence support

For transitive `A` of degree `t`:

\[
\boxed{m_{A\wr S_b}(\Delta A\times S_b;S_\times)=b(b-1)t.}
\]

**Status:** no direct published duplicate found in the audited literature.

Safe claim:

> Exact support theorem for the declared wreath-product pair action.

### Claim D — arbitrary partition + phase coherence

\[
\boxed{m_G(H_{\mathcal P};S_\times)=t\sum_j n_j(n_j-1).}
\]

**Status:** no direct duplicate found.

The distinction between block-set recovery and phase recovery is FCOA-specific and should be emphasized.

### Claim E — partition-only reduction

\[
\boxed{m_G(J_{\mathcal P};S_\times)=t^2d(\mathcal P).}
\]

**Status:** reduction itself is straightforward once `A^b`-invariance is observed, but the exact resource interpretation and subsequent optimization are useful original packaging.

### Claim F — exact formulas for two blocks / singleton families / three distinct blocks

Examples:

\[
d(p,q)=q(q-1)\quad(p>q\ge2),
\]

\[
d(p,q,r)=qr\quad(p>q>r).
\]

**Status:** no direct duplicate found in searched minimum-realization literature.

These are publishable as exact special-family propositions but should not be marketed as deep standalone group-theory breakthroughs.

### Claim G — Partition-Overgroup Dichotomy

Every proper overgroup of `K_P` either contains a forbidden cross-block transposition or the exceptional singleton macro-swap phenomenon occurs.

**Status:** no direct literature match found in searches for Young-subgroup/partition-stabilizer overgroups, block structures, relation groups, or 2-closure.

This is one of the strongest candidate original theorems in the follow-up paper.

Publication requirement: proof must be independently reread and the macro-swap double-coset step stated with exact hypotheses.

### Claim H — exact orbital XOR recognition/optimization

\[
\operatorname{Aut}(R)=K_P
\]

iff all representative forbidden transpositions and the possible macro-swap are broken, leading to an exact weighted OR-of-XOR program.

**Status:** no direct duplicate found.

Classical twin-free theory supplies the local separation intuition, but not the complete partition-stabilizer criterion with weighted orbitals and the singleton exception.

This is the second strongest candidate original result.

### Claim I — resource non-monotonicity

A stronger residual-symmetry reduction can require fewer FCOA cells because stronger target symmetry restrictions permit thinner diagonal internal fibers than partition-only invariance.

**Status:** this is an FCOA resource interpretation, not a claim about an unknown group-theoretic phenomenon.

It is safe and conceptually valuable if phrased explicitly in terms of the chosen support model.

---

## 12. Hostile conclusions

### What must be removed from any novelty rhetoric

The following are classical and must be cited:

- regular sets / trivial set-stabilizers;
- setwise stabilizers in power-set actions;
- distinguishing number and wreath-product distinguishing;
- subgroup-relative distinguishing with surviving group contained in `H`;
- relation groups and orbit closure;
- orbital digraphs and 2-closure;
- twin-free / point-determining graph and digraph concepts;
- minimum graph representations of an abstract automorphism group.

### What survives the audit as the real contribution

The strongest surviving package is:

1. prescribed **exact** residual symmetry as an FCOA value-memory resource on a fixed pair action;
2. exact wreath-coherence support formulas;
3. exact arbitrary-partition phase-coherence formula;
4. partition-only full-fiber reduction;
5. exact complement-compression formulas for several infinite partition families;
6. Partition-Overgroup Dichotomy;
7. exact forbidden-transposition + singleton-macro-swap recognition theorem;
8. exact weighted Orbital XOR-Separation formulation;
9. verifier-backed agreement with direct symmetric-group enumeration on all tested small partition types;
10. the resource non-monotonicity between partition-only memory and partition+phase memory.

No searched paper was found that presents this combined theorem chain or its FCOA interpretation.

---

## 13. Publication-readiness verdict

After the literature audit:

\[
\boxed{\text{the mathematical branch has crossed the article threshold.}}
\]

This does **not** mean the manuscript may be uploaded immediately. It means the research content is now sufficiently coherent and externally differentiated to justify publication assembly.

Before Zenodo release the following are mandatory:

1. hostile proof reread of the Partition-Overgroup Dichotomy;
2. proof audit of the exact lower bound for arbitrary partition+phase coherence;
3. rerun and freeze the finite verifier outputs;
4. ensure every theorem has explicit hypotheses, especially singleton conventions and directed/loopless pair domains;
5. number formulas/theorems consistently;
6. cite FCOA Foundation DOI `10.5281/zenodo.22164246` in abstract and bibliography;
7. include the classical-neighbor references in this audit;
8. avoid any NP-hardness claim;
9. frame `m_G(H;S)` as an organizing invariant rather than claiming universal priority for the abstract definition.

Recommended article scope:

> **Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra: Wreath Coherence, Partition Compression, and Exact Orbital Separation**

The article should be mathematically self-contained after a short FCOA setup and should not require the reader to know the entire earlier Riemann/prime-successor programme.
