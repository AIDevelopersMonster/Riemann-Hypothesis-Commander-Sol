# FCOA Rigidity Cost — Post-Article-B Research Ledger

**Branch:** `director/fcoa-rigidity-cost`  
**Published foundations:**
- Article A: DOI `10.5281/zenodo.22157403`.
- Article B: DOI `10.5281/zenodo.22159246`.

**Status:** active research after the two frozen publications. No result below retroactively modifies either article.

---

## P1. Conjecture 14 remains the primary open problem

The central question is

\[
\boxed{\alpha(D,c)\le\lambda(D,c)\ ?}
\]

for every finite sparse binary anonymous terminal layer.

Article B proves that any failure must arise from **symmetry creation under domain extension** / deletion-symmetry ambiguity. Classical reconstruction literature confirms that automorphism groups can change very freely under single-edge deletion, so this obstruction cannot be dismissed by a monotonicity argument.

Useful external comparison:

- S. G. Hartke, H. Kolb, J. Nishikawa, D. Stolee, *Automorphism Groups of a Graph and a Vertex-Deleted Subgraph*, Electronic Journal of Combinatorics 17 (2010), R134, DOI `10.37236/406`. The paper also treats the analogous edge-deleted question and shows that automorphism-group changes under deletion can be extremely flexible.

This literature does not settle the FCOA conjecture because our structure simultaneously carries a directed sparse domain and an anonymous binary equality reduct.

---

## P2. Complete five-carrier theorem

Article B proved the conjecture for all `|G|<=4` and for the five-carrier sector with at most five defined cells.

The remaining five-carrier space has now been exhausted using the theorem-level filters:

1. if `Lambda(D)` is connected, exactness is automatic;
2. if `Aut(G,D)=1`, then `Aut(G;D,Q_D)=1` and exactness is automatic;
3. only disconnected domains with nontrivial domain automorphism group require color enumeration.

There are exactly 10,095 such potentially nontrivial five-carrier domains. After quotienting each surjective binary coloring by global color complement, the complete candidate space contains

\[
\boxed{1,629,945}
\]

normalized colorings.

All were checked.

### Result

\[
\boxed{
|G|=5\Longrightarrow\alpha(D,c)\le\lambda(D,c)
}
\]

for every surjective sparse binary anonymous layer.

Among the candidate states the observed pairs are

\[
(\lambda,\alpha)=(0,0):1,540,065,
\]

\[
(\lambda,\alpha)=(1,1):89,240,
\]

\[
(\lambda,\alpha)=(2,1):640.
\]

No `alpha>lambda` case exists.

Therefore any counterexample to Conjecture 14 must satisfy

\[
\boxed{|G|\ge6.}
\]

This strictly strengthens the finite boundary published in Article B.

---

## P3. Six-carrier exhaustive sparse frontier

A second independent C++ implementation was used on six carrier points. The same theorem-level filters were applied before enumerating colors.

### Complete sector |D| <= 5

Potentially nontrivial normalized colorings checked:

\[
\boxed{473,295}.
\]

Observed positive pairs:

\[
(1,1):162,150,
\qquad
(2,1):3,300.
\]

No counterexample.

### Complete sector |D| <= 6

Potentially nontrivial normalized colorings checked cumulatively:

\[
\boxed{2,422,420}.
\]

Observed pairs:

\[
(0,0):1,688,065,
\]

\[
(1,1):722,895,
\]

\[
(2,1):10,680,
\]

\[
(2,2):60,
\]

\[
(3,1):720.
\]

No `alpha>lambda` case.

### Complete sector |D| <= 7

Potentially nontrivial normalized colorings checked cumulatively:

\[
\boxed{9,880,360}.
\]

Observed pairs:

\[
(0,0):7,292,725,
\]

\[
(1,1):2,550,255,
\]

\[
(2,1):36,600,
\]

\[
(2,2):60,
\]

\[
(3,1):720.
\]

Again no counterexample.

Therefore a counterexample on six carrier points, if one exists, must have

\[
\boxed{|D|\ge8.}
\]

---

## P4. First genuine alpha=2 layer

The first actual repair cost greater than one appears at `|G|=6`, `|D|=6`.

A minimal representative has three disjoint bidirected pairs:

\[
D=
\{(0,1),(1,0),(2,3),(3,2),(4,5),(5,4)\},
\]

with opposite colors on each pair, for example

\[
c(0,1)=0,\quad c(1,0)=1,
\]

\[
c(2,3)=1,\quad c(3,2)=0,
\]

\[
c(4,5)=1,\quad c(5,4)=0.
\]

For this layer

\[
\boxed{\lambda=2,\qquad\alpha=2.}
\]

Exactly 60 normalized six-carrier states in the exhaustive `|D|<=7` audit have `(lambda,alpha)=(2,2)`; all already occur at six cells.

This class is structurally important because it is the first place where actual cell repair does not collapse to one cell. It provides a complementary extremal geometry to the hub family from Article B, where `lambda=r-1` but `alpha=1`.

The next theoretical task is to classify the disjoint-bidirected-pair family for arbitrary `r` and determine its exact `alpha`, rather than infer a general law from the `r=3` computation.

---

## P5. Current conjecture boundary

The finite evidence is now substantially stronger than Article B:

\[
\boxed{
\alpha\le\lambda\text{ for every }|G|\le5,
}
\]

and

\[
\boxed{
\alpha\le\lambda\text{ for }|G|=6,\ |D|\le7.
}
\]

The open search region begins at

\[
\boxed{|G|=6,\ |D|\ge8}
\]

or larger carriers.

A direct exhaustive `|D|=8` six-carrier run is materially more expensive and was not completed in the current checkpoint. It should not be reported as audited.

---

## P6. Research priorities

1. **Disjoint-pair exact-cost theorem.** Determine `alpha` for `r` disjoint oppositely colored bidirected pairs and test whether it gives an infinite equality family `alpha=lambda=r-1` or a subtler law.
2. **Lambda=1 safe-extension theorem.** Try to prove that every layer with `lambda=1` has `alpha=1`; all exhaustive data currently support this.
3. **Deletion-symmetry classification.** Characterize extension automorphisms that move the old domain and identify when an optimal bridge set can be made intrinsically recognizable.
4. **Six-carrier |D|>=8 targeted search.** Use orbit representatives / symmetry-aware enumeration rather than raw coloring enumeration.
5. **Only after the binary conjecture is settled:** move to sparse `q>=3` and non-abelian `S_q` phase transport.

---

## Claim firewall

- Articles A and B are frozen publications and are cited, not silently revised.
- The five-carrier statement above is computationally exhaustive but should receive an independent verifier/audit before journal-style theorem promotion.
- The six-carrier statements are exhaustive only through `|D|<=7`.
- No result above proves Conjecture 14 in general.
- No broad novelty claim is made for automorphism-group changes under graph deletion; relevant reconstruction literature predates this branch.
