# Reflections on Sparse Anonymous Phase Geometry with Commander Sol

## Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Version: **1.0-rc1**  
Date: **29 August 2026**

Companion to: **Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition**, Zenodo DOI **10.5281/zenodo.22157403**.

---

## Abstract

The complete-domain theory of anonymous output fibers has an exact ternary phase reduct in the binary case: equality of values on composable operation cells forces one global \(\mathbb Z_2\)-phase. This paper studies what remains when the operation domain is sparse.

Let \(D\subseteq G^2\setminus\Delta\) be a partial off-diagonal binary terminal layer and let \(\Lambda(D)\) be the graph whose vertices are defined ordered cells and whose edges join composable cells. We prove that every automorphism of the sparse ternary equality reduct has a discrepancy bit that is constant on each connected component of \(\Lambda(D)\). The resulting component phase signature is naturally a 1-cocycle for the action on the component set. The ternary reduct is carrier-exact precisely when every realized cocycle value is diagonal, i.e. when all components carry the same phase.

This distinction separates three costs. The fixed-domain phase-link number \(\lambda(D,c)\) counts abstract component equalities needed to eliminate all realized non-diagonal signatures. The connectivity repair number \(\mu(D)\) counts real cells needed to connect \(\Lambda(D)\). The actual cell-extension cost \(\alpha(D,c)\) counts real new operation cells needed only to restore exactness. We prove

\[
\alpha(D,c)\le \mu(D)\le \kappa(\Lambda(D))-1,
\]

and construct an explicit family with

\[
\boxed{\lambda(D,c)=r-1,\qquad \alpha(D,c)=1,}
\]

where \(r=\kappa(\Lambda(D))\). Hence one real cell can outperform abstract phase synchronization by an arbitrarily large factor.

Finally we isolate the unresolved comparison \(\alpha(D,c)\le\lambda(D,c)\). We prove a no-old-obstruction theorem: if a \(\lambda\)-cell bridge realization fails, every bad automorphism must be genuinely new and must move the old domain inside the extension. Thus any counterexample is necessarily a deletion-symmetry phenomenon rather than a failure to synchronize the old phase cocycle. Exhaustive enumeration proves \(\alpha\le\lambda\) for every binary sparse layer on at most four carrier points and for every five-point layer with at most five defined cells. The general inequality is left as a sharply localized conjecture.

**Keywords:** partial operations; sparse domains; automorphism groups; anonymous values; signed graphs; gain graphs; switching; 1-cocycles; rigidity cost; synchronization; reconstruction.

---

# 1. From complete binary phase to sparse phase

The companion paper [1] considers a complete off-diagonal binary anonymous layer

\[
c:G^2\setminus\Delta\to\{0,1\}
\]

and the ternary relation

\[
Q(x,y,z)\Longleftrightarrow c(x,y)=c(y,z). \tag{1}
\]

Because all ordered off-diagonal cells form one connected composability graph, every carrier automorphism preserving \(Q\) changes all cell colors by one global discrepancy bit. Hence the ternary reduct is exact.

The complete-domain hypothesis is precisely what fails in the sparse case.

Let

\[
D\subseteq G^2\setminus\Delta,
\qquad
c:D\to\{0,1\} \tag{2}
\]

be a surjective binary coloring of a partial operation domain. The two values are anonymous: a valid carrier automorphism may preserve both fibers or exchange them globally.

Define

\[
\operatorname{Aut}^{\pm}(D,c)
=
\{g\in S_G:gD=D,\ c(gp)=c(p)\ \forall p\in D\}
\cup
\{g\in S_G:gD=D,\ c(gp)=1-c(p)\ \forall p\in D\}. \tag{3}
\]

We retain the sparse definedness relation together with

\[
Q_D(x,y,z)
\Longleftrightarrow
(x,y),(y,z)\in D
\text{ and }c(x,y)=c(y,z). \tag{4}
\]

The domain relation is essential: in a sparse structure, \(Q_D\) alone need not recover which operation cells are defined.

---

# 2. The ordered-cell incidence graph

Define \(\Lambda(D)\) as the undirected graph with vertex set \(D\). Two cells are adjacent when, after choosing an orientation of the adjacency, they are composable:

\[
(x,y)\sim(y,z). \tag{5}
\]

Write

\[
\pi_0(\Lambda(D))=\{C_1,\dots,C_r\},
\qquad
r=\kappa(\Lambda(D)). \tag{6}
\]

The graph \(\Lambda(D)\) is the sparse replacement for the connected ordered-cell graph used in [1]. Its components are the maximal regions over which equality information can propagate through ternary comparisons.

---

# 3. Componentwise Phase Theorem

Let

\[
A_Q=\operatorname{Aut}(G;D,Q_D). \tag{7}
\]

For \(g\in A_Q\) and \(p\in D\), define

\[
\delta_g(p)=c(gp)\oplus c(p). \tag{8}
\]

## Theorem 1 (Componentwise phase)

For every \(g\in A_Q\), the function \(\delta_g\) is constant on each connected component of \(\Lambda(D)\).

### Proof

If \(p=(x,y)\) and \(q=(y,z)\) are adjacent, preservation of \(Q_D\) gives

\[
c(p)=c(q)
\Longleftrightarrow
c(gp)=c(gq).
\]

For binary values this is equivalent to

\[
\delta_g(p)=\delta_g(q).
\]

The equality propagates along every path of \(\Lambda(D)\). \(\square\)

Thus each reduct automorphism has a component phase signature

\[
\varepsilon_g=(\varepsilon_g(C_1),\dots,\varepsilon_g(C_r))\in\mathbf F_2^r. \tag{9}
\]

This is the exact sparse analogue of the single global bit in the complete-domain theorem.

---

# 4. Exactness criterion and the phase cocycle

## Theorem 2 (Sparse exactness criterion)

The sparse ternary reduct is carrier-exact if and only if every realized component signature is diagonal:

\[
\operatorname{Aut}(G;D,Q_D)=\operatorname{Aut}^{\pm}(D,c) \tag{10}
\]

if and only if

\[
\varepsilon_g\in\Delta_r:=\{0^r,1^r\}
\qquad\forall g\in A_Q. \tag{11}
\]

### Proof

Theorem 1 shows that every reduct automorphism acts by one phase bit per component. Such an automorphism belongs to the full anonymous layer exactly when the phase is the same on all components. \(\square\)

In particular,

\[
\Lambda(D)\text{ connected}
\Longrightarrow
\operatorname{Aut}(G;D,Q_D)=\operatorname{Aut}^{\pm}(D,c). \tag{12}
\]

Connectedness is sufficient but not necessary. If the domain relation itself is carrier-rigid, then the sparse reduct is already exact even when \(\Lambda(D)\) has many components.

The signatures also obey a group-action law.

## Proposition 3 (Cocycle law)

For \(g,h\in A_Q\),

\[
\varepsilon_{gh}(C)
=
\varepsilon_h(C)+\varepsilon_g(hC) \tag{13}
\]

for every component \(C\) of \(\Lambda(D)\).

### Proof

For a cell \(p\in C\),

\[
\delta_{gh}(p)
=c(ghp)\oplus c(p)
=
\delta_g(hp)+\delta_h(p).
\]

Both terms are constant on their respective components, giving (13). \(\square\)

Thus

\[
\varepsilon:A_Q\to\mathbf F_2^{\pi_0(\Lambda(D))} \tag{14}
\]

is a 1-cocycle for the permutation action on the component set. The exactness defect is precisely the set of non-diagonal realized cocycle values.

Define

\[
\Sigma(D,c)=\{\varepsilon_g:g\in A_Q\}. \tag{15}
\]

Then

\[
\boxed{\text{exactness}\Longleftrightarrow\Sigma(D,c)\subseteq\Delta_r.} \tag{16}
\]

The cocycle language is structurally close to switching and gain-graph theory, where local labels are modified by group-valued switching functions and cycle data control global equivalence [2-5]. Our object is different: the phase is induced by **carrier automorphisms of an anonymous operation layer**, not chosen as an arbitrary switching function. The analogy is therefore useful but not an identification.

---

# 5. Three different repair costs

The sparse problem naturally produces three different quantities.

## Definition 4 (Fixed-domain phase-link number)

Let \(\lambda(D,c)\) be the minimum number of component equalities

\[
\varepsilon_{i_s}=\varepsilon_{j_s} \tag{17}
\]

needed so that every realized signature in \(\Sigma(D,c)\) satisfying all chosen equalities is diagonal.

Equivalently, \(\lambda\) is the minimum number of abstract phase comparisons needed to eliminate all realized non-global phase freedoms while leaving the domain fixed.

Always

\[
0\le\lambda(D,c)\le r-1. \tag{18}
\]

## Definition 5 (Connectivity repair number)

Let

\[
\mu(D)=
\min\{|E|:\Lambda(D\cup E)\text{ is connected}\}, \tag{19}
\]

where \(E\) ranges over undefined non-loop operation cells.

## Definition 6 (Actual cell-extension cost)

For an extension

\[
E\subseteq(G^2\setminus\Delta)\setminus D,
\qquad b:E\to\{0,1\},
\]

put \(D'=D\cup E\), \(c'=c\cup b\). Define

\[
\alpha(D,c)
=
\min\{|E|:\operatorname{Aut}(G;D',Q_{D'})
=
\operatorname{Aut}^{\pm}(D',c')\}. \tag{20}
\]

The quantities \(\lambda,\mu,\alpha\) answer different questions. The first counts abstract synchronization constraints on a fixed action. The second ignores colors and repairs connectivity. The third recomputes the full carrier action after genuine operation cells are added.

---

# 6. One-cell bridge lemma and the universal upper bound

## Lemma 7 (One-cell bridge)

Any two distinct components of \(\Lambda(D)\) can be joined by one undefined non-loop operation cell.

### Proof

Choose \(p=(a,b)\) in one component and \(q=(c,d)\) in the other. The natural bridge candidates are

\[
(b,c),\qquad(d,a). \tag{21}
\]

If both were loops then \(b=c\) and \(d=a\), so \(q=(b,a)\) and the two original cells would already be composable, contradicting distinctness of the components. At least one candidate is therefore non-loop. If that candidate were already defined, it would already connect the two components. Hence an undefined bridge exists. \(\square\)

## Theorem 8 (Universal sparse repair bound)

\[
\boxed{
\alpha(D,c)\le\mu(D)\le r-1.} \tag{22}
\]

### Proof

Use Lemma 7 along a spanning tree on the \(r\) components. At most \(r-1\) new cells make \(\Lambda\) connected. Then (12) gives exactness, independently of the colors assigned to the bridge cells. \(\square\)

Neither \(r-1\) nor \(\mu\) is a lower bound for \(\alpha\): a disconnected domain can already have trivial carrier group, giving \(\alpha=0\).

---

# 7. Worst-case abstract synchronization

The upper bound \(r-1\) is exact for abstract phase synchronization.

Take \(r\) disjoint carrier pairs \(\{a_i,b_i\}\) and define

\[
D_i=\{(a_i,b_i),(b_i,a_i)\} \tag{23}
\]

with opposite colors on the two cells. Swapping \(a_i\) and \(b_i\) flips phase only on component \(i\). Hence the reduct realizes

\[
(C_2)^r. \tag{24}
\]

The full anonymous layer permits only the diagonal simultaneous flip. Therefore

\[
\boxed{\lambda(D,c)=r-1.} \tag{25}
\]

Thus

\[
M_{\rm sync}^{\rm worst}(r)=r-1. \tag{26}
\]

This is a worst-case theorem about abstract phase links, not about operation cells.

---

# 8. Actual cells can outperform abstract links without bound

The crucial separation is that one real operation cell may touch many old components at once.

For a candidate cell \(e\notin D\), define its old-component touch set

\[
\mathcal T_D(e)=
\{C\in\pi_0(\Lambda(D)):\exists p\in C\text{ adjacent to }e\}. \tag{27}
\]

One new cell merges every component in \(\mathcal T_D(e)\) into one component of the enlarged incidence graph.

## Theorem 9 (Unbounded \(\lambda/\alpha\) separation)

For every \(r\ge2\) there exists a sparse binary anonymous layer with

\[
\boxed{\lambda(D,c)=r-1,\qquad\alpha(D,c)=1.} \tag{28}
\]

### Construction

Use carrier

\[
G=\{h,t\}\cup\{a_i,b_i:1\le i\le r\}. \tag{29}
\]

For each \(i\), let

\[
D_i=
\{(a_i,h),(b_i,h),(a_i,b_i),(b_i,a_i)\}. \tag{30}
\]

Color

\[
c(a_i,h)=c(a_i,b_i)=0,
\qquad
c(b_i,h)=c(b_i,a_i)=1. \tag{31}
\]

The components \(D_i\) are pairwise disconnected in \(\Lambda(D)\), and the transpositions

\[
s_i=(a_i\ b_i) \tag{32}
\]

realize independent component flips. Therefore \(\lambda=r-1\).

Now add the single cell

\[
e=(h,t) \tag{33}
\]

with either color. It is adjacent to \((a_i,h)\) and \((b_i,h)\) for every \(i\), so the enlarged incidence graph is connected. Hence the extended ternary reduct is exact and \(\alpha=1\). \(\square\)

Consequently

\[
\lambda(D,c)-\alpha(D,c)=r-2 \tag{34}
\]

and

\[
\frac{\lambda(D,c)}{\alpha(D,c)}=r-1. \tag{35}
\]

Both gaps are unbounded.

This is the basic operational lesson of the paper: an abstract equality link is binary at the component level, whereas one genuine operation cell can act as a high-degree incidence hub.

---

# 9. Why \(\alpha\le\lambda\) is subtle

The preceding theorem shows that \(\lambda\) can drastically overestimate actual cost. It is natural to ask whether actual cost is always bounded above by \(\lambda\):

\[
\boxed{\alpha(D,c)\le\lambda(D,c)\ ?} \tag{36}
\]

A direct monotonicity argument is impossible. Adding a cell can **increase** the automorphism group of the domain. For example,

\[
D=\{(0,1)\}
\]

has trivial domain automorphism group on three carrier points, while

\[
D'=\{(0,1),(2,1)\}
\]

admits the transposition \((0\ 2)\).

Thus real extensions can create symmetries that did not act on the old domain.

Nevertheless, the old phase obstruction can be completely controlled.

---

# 10. No-old-obstruction theorem

Let

\[
L=\{(C_{i_s},C_{j_s}):1\le s\le\lambda\} \tag{37}
\]

be an optimal abstract phase-link system. Realize each link by one bridge cell, obtaining an extension \(D'=D\cup E\) with \(|E|=\lambda\).

## Theorem 10 (No-old-obstruction)

If

\[
g\in\operatorname{Aut}(G;D',Q_{D'}) \tag{38}
\]

preserves the old domain \(D\) setwise, then \(g\) is a full anonymous automorphism of the extended colored layer.

### Proof

Restriction to \(D\) lies in the old group \(A_Q\). Each bridge forces equality of the phase bits on the linked old components. Hence the old phase signature satisfies every equality in the optimal link system \(L\). By definition of \(\lambda\), every realized old signature satisfying those equalities is diagonal. Therefore \(g\) either preserves all old colors or globally swaps them.

Within each enlarged incidence component, Theorem 1 forces the discrepancy on the bridge cells to agree with the discrepancy on the old cells to which they are attached. Thus the same global phase extends over \(E\). \(\square\)

Therefore

\[
\boxed{
\alpha>\lambda
\Longrightarrow
\text{every }\lambda\text{-cell realization creates a new bad automorphism that moves }D.} \tag{39}
\]

This is the only possible obstruction to (36).

---

# 11. Deletion-symmetry reformulation

Suppose a \(\lambda\)-cell bridge extension \(D'=D\cup E\) admits a bad automorphism \(g\) with \(gD\ne D\). Then

\[
gD=D'\setminus gE \tag{40}
\]

is a different deletion of \(\lambda\) cells from the same extended domain. Since \(g\) is an automorphism of the extended reduct,

\[
D'\setminus E\cong D'\setminus gE. \tag{41}
\]

Thus any counterexample to \(\alpha\le\lambda\) is necessarily tied to a deletion ambiguity: every optimal bridge extension must admit an alternative deletion deck that is carrier-equivalent but carries a non-diagonal phase behavior.

This converts the remaining problem into a reconstruction-style question rather than a phase-synchronization question.

A useful conditional form is immediate.

## Corollary 11 (Recognizable-bridge criterion)

If an optimal \(\lambda\)-cell bridge realization can be chosen so that the old domain \(D\) is setwise invariant under every automorphism of \((G;D',Q_{D'})\), then

\[
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{42}
\]

Equivalently, any bridge set that is intrinsically recognizable in the extended reduct is safe.

---

# 12. Exhaustive finite audit of \(\alpha\le\lambda\)

The inequality (36) has been checked exhaustively in the first nontrivial finite ranges.

## Theorem 12 (Complete four-point audit)

For every surjective partial binary layer on a four-point carrier,

\[
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{43}
\]

All \(523250\) layers were enumerated. The only observed pairs were

\[
(\lambda,\alpha)=(0,0),(1,1),(2,1). \tag{44}
\]

with counts

\[
522398,\qquad804,\qquad48, \tag{45}
\]

respectively.

## Proposition 13 (Five-point sparse audit)

For every surjective five-point binary layer with at most five defined ordered cells,

\[
\alpha(D,c)\le\lambda(D,c). \tag{46}
\]

The exhaustive sector contains \(270085\) layers, of which \(10640\) have \(\lambda>0\). The positive cases observed are only \((1,1)\) and \((2,1)\).

Targeted searches on larger five-point layers and on six-point layers found no counterexample; these additional searches are evidence, not theorem-level exhaustions.

---

# 13. Conjecture and minimal-counterexample constraints

## Conjecture 14

For every finite sparse binary anonymous terminal layer,

\[
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{47}
\]

If the conjecture is false, a minimal counterexample must satisfy all of the following:

1. \(|G|\ge5\);
2. at \(|G|=5\), it has at least six defined cells;
3. \(\lambda\ge1\);
4. every optimal \(\lambda\)-cell bridge realization creates a new bad automorphism that moves the old domain;
5. equivalently, every optimal realization exhibits a deletion-symmetry ambiguity of the form (41).

Thus the unresolved part has been localized to **symmetry creation under domain extension**.

The conjecture is deliberately not promoted to a theorem in this paper.

---

# 14. Relation to signed and gain graphs

Signed graphs attach a \(\mathbb Z_2\)-label to edges and admit switching operations that modify signs while preserving cycle-balance data [2]. Gain graphs replace \(\mathbb Z_2\) by an arbitrary group and similarly organize local labels, switching functions, and global cycle constraints [3-5].

Our component phase cocycle has a related algebraic flavor, but the source of the cocycle is different. We do not freely switch vertices of a fixed signed graph. Instead, a **carrier permutation preserving a derived anonymous equality reduct** induces a discrepancy on operation cells. Sparse composability forces that discrepancy to be constant on incidence components, and component permutations twist the multiplication law into (13).

Likewise, the costs \(\lambda,\mu,\alpha\) are not standard switching distances. They measure three distinct resources in a partial-operation setting: abstract phase synchronization, domain connectivity repair, and actual operation-cell exactness repair.

The paper therefore uses signed/gain-graph language as mathematical context while keeping its claims limited to the anonymous-operation model.

---

# 15. Structural hierarchy

The sparse binary theory can be summarized as

\[
D
\longrightarrow
\Lambda(D)
\longrightarrow
\varepsilon
\longrightarrow
\Sigma(D,c)
\longrightarrow
\lambda(D,c) \tag{48}
\]

for the fixed-domain phase problem, and

\[
D
\longrightarrow
\mathcal T_D
\longrightarrow
\mu(D)
\longrightarrow
\alpha(D,c) \tag{49}
\]

for real domain extension.

The universal relations among the costs are

\[
0\le\lambda(D,c)\le r-1, \tag{50}
\]

\[
\boxed{0\le\alpha(D,c)\le\mu(D)\le r-1.} \tag{51}
\]

There is no growing lower bound on \(\alpha\) in terms of \(\lambda\): Theorem 9 has \(\lambda=r-1\) and \(\alpha=1\). The opposite comparison is Conjecture 14.

---

# 16. Conclusion

Sparse anonymous value geometry is controlled not merely by the number of disconnected cell regions but by the phases that carrier automorphisms actually realize on them. The correct invariant is a componentwise \(\mathbb Z_2\)-valued 1-cocycle, and exactness is equivalent to diagonality of all realized cocycle values.

This immediately separates three notions of repair cost. Abstract phase synchronization can require \(r-1\) links, yet one operation cell may synchronize all components at once. Consequently \(\lambda/\alpha\) is unbounded. Real cell extensions are therefore not merely implementations of abstract constraints; they can reorganize the incidence geometry itself.

The remaining comparison \(\alpha\le\lambda\) is subtler because operation-cell addition is not monotone at the level of automorphism groups. The No-old-obstruction theorem shows that any failure must come from genuinely new symmetries created by the extension, equivalently from deletion ambiguity in the extended domain. Exhaustive small cases support the conjecture but do not settle it.

This gives a clean boundary for further work: the next problem is no longer phase propagation itself, but the reconstruction theory of sparse operation domains under symmetry-creating extensions.

---

# References

[1] A. Malachevsky, *Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition*, Zenodo, 2026. DOI: `10.5281/zenodo.22157403`.

[2] T. Zaslavsky, “Signed graphs,” *Discrete Applied Mathematics* **4** (1982), 47-74. DOI: `10.1016/0166-218X(82)90033-6`.

[3] T. Zaslavsky, “Biased graphs. I. Bias, balance, and gains,” *Journal of Combinatorial Theory, Series B* **47** (1989), 32-52. DOI: `10.1016/0095-8956(89)90063-4`.

[4] A. Slilaty and H. Qin, “Bounding and stabilizing realizations of biased graphs with a fixed group,” *Journal of Combinatorial Theory, Series B* **119** (2016), 76-89. DOI: `10.1016/j.jctb.2016.05.008`.

[5] M. Cavaleri, D. D’Angeli, and A. Donno, “Gain-line graphs via G-phases and group representations,” *Linear Algebra and its Applications* **613** (2021), 241-270. DOI: `10.1016/j.laa.2020.11.009`.

---

## Publication note

This paper intentionally leaves Conjecture 14 open. All theorems through Theorem 12 and Proposition 13 are independent of that conjecture. The article is designed as a complete publication of the proved sparse-domain theory, with the conjecture serving as the precise handoff to the next research phase.