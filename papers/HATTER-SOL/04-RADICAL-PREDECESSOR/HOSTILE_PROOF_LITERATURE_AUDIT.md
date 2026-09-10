# HATTER-SOL-04 · Hostile Proof and Literature Audit

**Audit date:** 2026-09-10  
**Branch:** `papers/HATTER-SOL/04-RADICAL-PREDECESSOR/`  
**Purpose:** decide whether the current theorem package is mathematically stable enough to cross the publication threshold without pretending to solve the underlying automorphism problem.

---

# 1. Executive verdict

## Verdict

\[
\boxed{\text{PUBLICATION THRESHOLD REACHED FOR A STRUCTURAL ARTICLE}}
\]

with one non-negotiable scope condition:

\[
\boxed{
\text{the article must NOT claim that }\operatorname{Aut}(\Pi)\text{ has been determined.}
}
\]

The original question whether the directed graph

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1,
\]

is rigid remains unresolved by the present work.

What is publication-ready is the **structural theorem package describing what any automorphism must look like and how finite-height symmetries propagate or die**.

No fatal proof defect was found in the main results after hostile rereading. Several wording and proof-completeness corrections are required before v1.0; they are listed below.

---

# 2. Literature collision: exact problem already existed

The automorphism problem itself is not new.

In 2012 David Feldman asked on MathOverflow for the automorphism group of the digraph on primes with an edge

\[
p\to q\iff p\mid q-1.
\]

Gjergji Zaimi answered that he expected many automorphisms but could not prove this unconditionally. He pointed out that:

- \(2\) is the unique vertex with no incoming edges;
- the vertices whose incoming support is exactly \(\{2\}\) are the Fermat primes;
- a strong conjecture asserting infinitely many primes in every exact finite predecessor support would imply many automorphisms.

Therefore the following must **not** be presented as new:

1. the graph itself;
2. the automorphism question;
3. the Fermat-prime first fiber;
4. the heuristic that uniform infinitude of exact-support fibers would produce many automorphisms.

The paper should cite the MathOverflow question and answer explicitly near the beginning.

---

# 3. Jones collision: finite universality is classical

Gareth A. Jones studied the directed graph with arcs

\[
q\to p\iff q\mid p-1
\]

in his 2010 paper on regular embeddings of complete bipartite graphs.

His Proposition 13.1 shows finite acyclic labelled universality for the corresponding prime-divisibility graphs. Proposition 14.1 shows that, after removing the vertex \(2\), forgetting orientation and retaining adjacency when one prime divides the predecessor of the other, the resulting odd-prime graph is the Rado graph.

Consequently:

- CRT + Dirichlet finite extension constructions are classical ingredients;
- our `FINITE_FUTURE_INDISCRIMINABILITY.md` should be presented as a **pinned forward-extension formulation and no-go consequence for the automorphism search**, not as the discovery of finite universality itself.

---

# 4. Audit of the Multiplicity Tower Theorem

File:

`MULTIPLICITY_TOWER_THEOREM.md`

## Result under audit

For

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n})
\]

and exact level-\(n+1\) predecessor fibers

\[
X_S=\{p\in L_{n+1}:\operatorname{Pred}(p)=S\},
\qquad
\mu_n(S)=|X_S|,
\]

the restriction map satisfies

\[
\operatorname{im}\rho_n
=
E_n
=
\{g\in G_n:\mu_n(S)=\mu_n(gS)\text{ for all }S\},
\]

and

\[
\ker\rho_n
\cong
\prod_S\operatorname{Sym}(X_S).
\]

The extension splits noncanonically, and

\[
\operatorname{Aut}(\Pi)
\cong
\varprojlim G_n.
\]

## Verdict

**PASS.**

The proof uses only the layered acyclic structure:

- all predecessors of a level \(n+1\) vertex lie below level \(n+1\);
- there are no edges inside one level;
- two vertices in the same exact predecessor fiber are indistinguishable from below;
- an extendable lower-level automorphism must permute fibers of equal cardinality.

The splitting argument using fixed model sets for equal-cardinality fibers is valid.

## Required wording correction

Do **not** call \(P_{\le n}\) a "finite truncation" in the cardinality sense. A fixed Pratt-height level need not be known to be finite; already height one is the Fermat-prime set, whose infinitude is open.

Use:

- **height truncation**;
- **finite-height truncation**;

and explicitly state that such a truncation may itself be infinite.

## Required definability correction

Replace the phrase "height is graph-theoretically definable by well-founded rank" by the safer invariant statement:

> Pratt height is the maximum length of a directed path from the unique source \(2\), hence is preserved by every graph automorphism.

No first-order definability claim is needed.

---

# 5. Audit of finite-future indistinguishability

File:

`FINITE_FUTURE_INDISCRIMINABILITY.md`

## Result under audit

Any admissible finite forward extension over a pinned finite base can be realized using CRT + Dirichlet. Therefore vertices with the same exact predecessor set have the same pinned finite forward age.

In particular,

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}
\]

implies that no finite forward incidence motif of the stated type can distinguish \(3\) from \(5\).

## Verdict

**PASS, with scope discipline.**

The induction correctly controls all incidences among previously chosen vertices. Extra predecessor primes outside the chosen finite substructure may occur; this is precisely why the result does not control exact predecessor support.

## Required scope warning

The result does **not** prove:

- equality of unrestricted first-order types;
- existence of a back-and-forth system for the entire graph;
- global automorphy of equal-predecessor vertices.

The publication should retain this warning prominently.

---

# 6. Audit of infinite propagation

File:

`INFINITE_PROPAGATION_THEOREM.md`

## Result under audit

If

\[
g(x)=y\ne x,
\]

then every prime \(p\) satisfying

\[
x\mid p-1,
\qquad
y\nmid p-1
\]

must move.

CRT + Dirichlet gives infinitely many such \(p\). Iteration yields moved vertices of arbitrarily large Pratt height and an infinitely branching forward moved configuration.

## Verdict

**PASS.**

The proof is direct:

if \(p\) were fixed, edge preservation would force

\[
D(x,p)\iff D(y,p),
\]

contradicting the construction.

The branching statement should continue to say "contains a recursively selected infinitely branching forward tree" rather than claiming that the chosen tree is induced.

---

# 7. Audit of the Density-One Movement Theorem

File:

`DENSITY_ONE_MOVEMENT_THEOREM.md`

## Result under audit

Every nonidentity automorphism satisfies

\[
\boxed{
d_{\mathbb P}(\operatorname{Fix}(g))=0,
\qquad
d_{\mathbb P}(\operatorname{supp}(g))=1.
}
\]

## Verdict

**PASS**, but the publication proof needs one auxiliary step stated explicitly.

### Step A — positive-density seed

From one moved pair \(x\mapsto y\), the symmetric difference

\[
N^+(x)\triangle N^+(y)
\]

is contained in the moved set and has relative prime density

\[
\frac1{x-1}
+
\frac1{y-1}
-
\frac{2}{(x-1)(y-1)}
>0.
\]

This is correct by the prime number theorem in arithmetic progressions.

### Step B — divergent reciprocal weight

The manuscript currently jumps from positive relative prime density to

\[
\sum_{q\in\operatorname{supp}(g)}\frac1{q-1}=\infty.
\]

This is correct, but should be justified explicitly. The cleanest route here is even stronger than a general density lemma: the seed set is a finite union of reduced residue classes modulo \(xy\), so the PNT in arithmetic progressions plus partial summation gives divergence of the reciprocal-prime sum directly.

### Step C — orbit pairing

The weighted pairing lemma is valid. Infinite orbits can be perfectly paired; finite odd orbits lose at most half their total reciprocal weight when the minimum-weight vertex is omitted.

### Step D — independent finite congruence conditions

For pairwise disjoint prime pairs \(\{a_j,b_j\}\), the conditions

\[
[a_j\mid p-1]=[b_j\mid p-1]
\]

are independent at every finite stage by CRT. Their relative prime density is the product

\[
\prod_{j=1}^{N}
\frac{(a_j-2)(b_j-2)+1}{(a_j-1)(b_j-1)}.
\]

The exponential estimate is correct and the product tends to zero because the selected reciprocal weight diverges.

Thus the density-one conclusion survives hostile audit.

---

# 8. Audit of analytic wildness / near-identity rigidity

File:

`ANALYTIC_WILDNESS_THEOREM.md`

## Result under audit

If

\[
g(p_n)=p_{\sigma(n)}
\]

and

\[
\frac{\sigma(n)}n\to1,
\]

then \(g=\mathrm{id}\).

Likewise,

\[
\frac{g(p)}p\to1
\]

forces \(g=\mathrm{id}\).

## Verdict

**PASS.**

A permutation \(\sigma(n)=n(1+o(1))\) preserves every existing natural density on \(\mathbb N\). The outgoing prime neighborhood

\[
N^+(q)=\{p:q\mid p-1\}
\]

has relative prime density

\[
\frac1{q-1},
\]

and automorphisms satisfy

\[
g(N^+(q))=N^+(g(q)).
\]

These densities are pairwise distinct, forcing \(g(q)=q\).

For the numerical version, use

\[
\pi(x)\sim\frac{x}{\log x}
\]

directly to justify

\[
\frac{p_{\sigma(n)}}{p_n}\to1
\Longrightarrow
\frac{\sigma(n)}n\to1.
\]

This is cleaner than an informal subsequence argument.

---

# 9. Audit of the conditional large-automorphism theorem

File:

`FERMAT_SWAP_AND_LITERATURE_COLLISION.md`

Under the strong hypothesis

\[
\mu(S)=\aleph_0
\]

for every finite exact predecessor support \(S\ni2\), every tower restriction is surjective and every finite-height automorphism extends globally. In particular the automorphism group has cardinality continuum.

## Verdict

**PASS AS A CONDITIONAL THEOREM.**

But the hypothesis is deliberately very strong and must never be advertised as evidence that the hypothesis is likely. The case \(S=\{2\}\) already implies infinitely many Fermat primes.

Its proper role is conceptual:

\[
\boxed{
\text{uniform infinite fibers}\Rightarrow\text{maximal survival of symmetry}.
}
\]

---

# 10. Literature audit result

Targeted searches were run for:

- the exact automorphism problem for \(q\mid p-1\);
- prime-divisibility graph automorphisms;
- Pratt-tree automorphisms;
- density/fixed-point restrictions on such automorphisms;
- near-identity permutations of the prime graph.

The search located:

1. the 2012 MathOverflow question and Zaimi answer, which already isolate the basic automorphism problem and Fermat-fiber difficulty;
2. Jones's finite acyclic universality and Rado-shadow results;
3. the classical Pratt-certificate and prime-chain literature;
4. standard analytic number theory supplying Dirichlet's theorem and the PNT in arithmetic progressions.

The targeted audit **did not locate** a prior source stating the present package of:

- the multiplicity-tower split exact sequence;
- the inverse-limit survival formulation;
- density-one movement for every hypothetical nonidentity automorphism;
- near-identity prime-rank/size rigidity.

This is **not a literature-wide proof of priority**. Publication wording must say only that these formulations were not located in the present targeted audit.

---

# 11. Required publication boundary

The article may safely claim:

> We give a structural analysis of the unresolved automorphism problem for the directed prime graph \(q\mid p-1\), reducing finite-height extension to exact predecessor-fiber multiplicities and proving strong unconditional constraints on every hypothetical nontrivial automorphism.

It must not claim:

> We solve the automorphism problem.

Nor should it imply that the full graph is known to be rigid or nonrigid.

---

# 12. Article-level theorem package

The publication should be built around the following chain.

### Theorem A — radical reduction

Over the full multiplicative carrier, retaining

\[
\operatorname{rad}(p-1)
\]

is equivalent to retaining the directed graph

\[
D(q,p)\iff q\mid p-1.
\]

### Theorem B — multiplicity tower

Finite-height extension is controlled exactly by the multiplicities of exact predecessor fibers, with split kernel

\[
\prod_S\operatorname{Sym}(X_S),
\]

and the global automorphism group is the corresponding inverse limit.

### Theorem C — finite-future no-go

Equal-predecessor vertices have the same pinned finite forward age; finite future motifs cannot kill their symmetry.

### Theorem D — infinite propagation

One moved prime forces infinitely many moved successors and movement to unbounded Pratt height.

### Theorem E — density-one movement

Every nonidentity automorphism, if one exists, moves a relative-density-one subset of all primes.

### Theorem F — analytic wildness

Every asymptotically rank-local or size-local automorphism is the identity. Hence a nonidentity automorphism must make macroscopic rank and numerical displacements infinitely often.

### Theorem G — conditional opposite regime

Under full exact-support infinitude, finite-height symmetries survive globally and the automorphism group has cardinality continuum.

This is a coherent publishable story even though the original yes/no question remains open.

---

# 13. Final audit decision

The research phase has crossed the article threshold.

The correct next action is:

\[
\boxed{
\text{freeze theorem hunting for v1.0 and assemble the Russian publication draft.}
}
\]

Further attempts to solve the full automorphism problem can continue after the article source has been stabilized.

The publication should be framed not as a failed rigidity proof, but as a sharp theorem about the **price of any hypothetical symmetry**:

\[
\boxed{
\text{if nontrivial symmetry exists, it must be global, density-one, and analytically wild.}
}
\]

---

# References checked in this audit

1. David Feldman, *Automorphisms of a certain digraph defined on the set of primes? [Edited]*, MathOverflow, 2012, with answer by Gjergji Zaimi.
2. Gareth A. Jones, *Regular embeddings of complete bipartite graphs: classification and enumeration*, Proceedings of the London Mathematical Society 101 (2010), 427–453. DOI: `10.1112/plms/pdp061`.
3. Vaughan R. Pratt, *Every Prime Has a Succinct Certificate*, SIAM Journal on Computing 4(3) (1975), 214–220. DOI: `10.1137/0204018`.
4. Kevin Ford, Sergei V. Konyagin, Florian Luca, *Prime Chains and Pratt Trees*, Geometric and Functional Analysis 20(5) (2010), 1231–1258. DOI: `10.1007/s00039-010-0089-0`.
5. Harold Davenport, *Multiplicative Number Theory*, 3rd ed., Graduate Texts in Mathematics 74, Springer, 2000; standard reference for primes in arithmetic progressions and the PNT in arithmetic progressions.
