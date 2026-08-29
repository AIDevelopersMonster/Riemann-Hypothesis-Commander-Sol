# Reflections on Sparse Anonymous Phase Geometry with Commander Sol

## Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Version: **1.0**  
Date: **29 August 2026**

Companion to: *Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition*, Zenodo DOI **10.5281/zenodo.22157403**.

---

## Abstract

The complete-domain theory of anonymous output fibers has an exact ternary phase reduct in the binary case: equality of values on composable operation cells forces one global $\mathbb Z_2$-phase. This paper studies what remains when the operation domain is sparse.

Let $D\subseteq G^2\setminus\Delta$ be a partial off-diagonal binary terminal layer and let $\Lambda(D)$ be the graph whose vertices are defined ordered cells and whose edges join composable cells. We prove that every automorphism of the sparse ternary equality reduct has a discrepancy bit that is constant on each connected component of $\Lambda(D)$. The resulting component phase signature is naturally a 1-cocycle for the action on the component set. The ternary reduct is carrier-exact precisely when every realized cocycle value is diagonal, i.e. when all components carry the same phase.

This distinction separates three costs. The fixed-domain phase-link number $\lambda(D,c)$ counts abstract component equalities needed to eliminate all realized non-diagonal signatures. The connectivity repair number $\mu(D)$ counts real cells needed to connect $\Lambda(D)$. The actual cell-extension cost $\alpha(D,c)$ counts real new operation cells needed only to restore exactness. We prove

$$
\alpha(D,c)\le \mu(D)\le \kappa(\Lambda(D))-1. \tag{1}
$$

We also construct an explicit family with

$$
\boxed{\lambda(D,c)=r-1,\qquad \alpha(D,c)=1,} \tag{2}
$$

where $r=\kappa(\Lambda(D))$. Hence one real cell can outperform abstract phase synchronization by an arbitrarily large factor.

Finally we isolate the unresolved comparison $\alpha(D,c)\le\lambda(D,c)$. We prove a no-old-obstruction theorem: if a $\lambda$-cell bridge realization fails, every bad automorphism must be genuinely new and must move the old domain inside the extension. Thus any counterexample is necessarily a deletion-symmetry phenomenon rather than a failure to synchronize the old phase cocycle. Exhaustive enumeration proves $\alpha\le\lambda$ for every binary sparse layer on at most four carrier points and for every five-point layer with at most five defined cells. The general inequality is left as a sharply localized conjecture.

**Keywords:** partial operations; sparse domains; automorphism groups; anonymous values; 1-cocycles; rigidity cost; switching; gain graphs; synchronization; reconstruction.

---

# 1. From complete binary phase to sparse phase

This paper is a companion to [1], but it is mathematically self-contained: all definitions and proofs needed for the sparse-domain results are given here. The anonymous-value framework arose from the broader FCOA programme, but no arithmetic or prime-successor background is required for the present arguments.

The companion paper [1] considers a complete off-diagonal binary anonymous layer

$$
c:G^2\setminus\Delta\to\{0,1\}
$$

and the ternary relation

$$
Q(x,y,z)\Longleftrightarrow c(x,y)=c(y,z). \tag{3}
$$

Because all ordered off-diagonal cells form one connected composability graph, every carrier automorphism preserving $Q$ changes all cell colors by one global discrepancy bit. Hence the ternary reduct is exact.

The complete-domain hypothesis is precisely what fails in the sparse case. Let

$$
D\subseteq G^2\setminus\Delta,\qquad c:D\to\{0,1\} \tag{4}
$$

be a surjective binary coloring of a partial operation domain. The two values are anonymous: a valid carrier automorphism may preserve both fibers or exchange them globally. Define

$$
\operatorname{Aut}^{\pm}(D,c)=
\{g\in S_G:gD=D,\ c(gp)=c(p)\ \forall p\in D\}
\cup
\{g\in S_G:gD=D,\ c(gp)=1-c(p)\ \forall p\in D\}. \tag{5}
$$

We retain the sparse definedness relation together with

$$
Q_D(x,y,z)\Longleftrightarrow (x,y),(y,z)\in D\text{ and }c(x,y)=c(y,z). \tag{6}
$$

The domain relation is essential: in a sparse structure, $Q_D$ alone need not recover which operation cells are defined.

# 2. The ordered-cell incidence graph

Define $\Lambda(D)$ as the undirected graph with vertex set $D$. Two cells are adjacent when, after choosing an orientation of the adjacency, they are composable:

$$
(x,y)\sim(y,z). \tag{7}
$$

Write

$$
\pi_0(\Lambda(D))=\{C_1,\ldots,C_r\},\qquad r=\kappa(\Lambda(D)). \tag{8}
$$

The components are the maximal regions over which ternary equality information can propagate.

# 3. Componentwise Phase Theorem

Let

$$
A_Q=\operatorname{Aut}(G;D,Q_D). \tag{9}
$$

For $g\in A_Q$ and $p\in D$, define

$$
\delta_g(p)=c(gp)\oplus c(p). \tag{10}
$$

## Theorem 1 (Componentwise phase)

For every $g\in A_Q$, the function $\delta_g$ is constant on each connected component of $\Lambda(D)$.

### Proof

If $p=(x,y)$ and $q=(y,z)$ are adjacent, preservation of $Q_D$ gives

$$
c(p)=c(q)\Longleftrightarrow c(gp)=c(gq).
$$

For binary values this is equivalent to $\delta_g(p)=\delta_g(q)$. The equality propagates along every path of $\Lambda(D)$. $\square$

Thus each reduct automorphism has a component phase signature

$$
\varepsilon_g=(\varepsilon_g(C_1),\ldots,\varepsilon_g(C_r))\in\mathbf F_2^r. \tag{11}
$$

# 4. Exactness criterion and the phase cocycle

## Theorem 2 (Sparse exactness criterion)

The sparse ternary reduct is carrier-exact if and only if every realized component signature is diagonal:

$$
\operatorname{Aut}(G;D,Q_D)=\operatorname{Aut}^{\pm}(D,c) \tag{12}
$$

if and only if

$$
\varepsilon_g\in\Delta_r:=\{0^r,1^r\}\qquad\forall g\in A_Q. \tag{13}
$$

### Proof

Theorem 1 shows that every reduct automorphism acts by one phase bit per component. It belongs to the full anonymous layer exactly when that bit is the same on all components. $\square$

In particular,

$$
\Lambda(D)\text{ connected}\Longrightarrow\operatorname{Aut}(G;D,Q_D)=\operatorname{Aut}^{\pm}(D,c). \tag{14}
$$

Connectedness is sufficient, not necessary. If the domain relation itself is carrier-rigid, then the reduct is already exact regardless of the number of components. Thus the genuinely nontrivial sparse regime is the conjunction

$$
\Lambda(D)\text{ disconnected}\qquad\text{and}\qquad \operatorname{Aut}(G;D,Q_D)\ne1.
$$

If the first condition fails, exactness follows from connected phase propagation; if the second fails, $\Sigma(D,c)=\{0^r\}$ and exactness is vacuous.

## Proposition 3 (Cocycle law)

For $g,h\in A_Q$ and each component $C$,

$$
\varepsilon_{gh}(C)=\varepsilon_h(C)+\varepsilon_g(hC). \tag{15}
$$

### Proof

For a cell $p\in C$,

$$
\delta_{gh}(p)=c(ghp)\oplus c(p)=\delta_g(hp)+\delta_h(p).
$$

Both terms are constant on their respective components. $\square$

Hence

$$
\varepsilon:A_Q\to\mathbf F_2^{\pi_0(\Lambda(D))} \tag{16}
$$

is a 1-cocycle for the permutation action on the component set. Put

$$
\Sigma(D,c)=\{\varepsilon_g:g\in A_Q\}. \tag{17}
$$

Then

$$
\boxed{\text{exactness}\Longleftrightarrow\Sigma(D,c)\subseteq\Delta_r.} \tag{18}
$$

This language resembles signed- and gain-graph switching, but the source of the phase is different: here the cocycle is induced by carrier automorphisms preserving a derived anonymous equality reduct; it is not an independently chosen switching function [2-5].

# 5. Three different repair costs

## Definition 4 (Fixed-domain phase-link number)

Let $\lambda(D,c)$ be the minimum number of component equalities

$$
\varepsilon_{i_s}=\varepsilon_{j_s} \tag{19}
$$

needed so that every realized signature in $\Sigma(D,c)$ satisfying all chosen equalities is diagonal. Thus $\lambda$ is an abstract fixed-domain synchronization cost. Always

$$
0\le\lambda(D,c)\le r-1. \tag{20}
$$

## Definition 5 (Connectivity repair number)

Let

$$
\mu(D)=\min\{|E|:\Lambda(D\cup E)\text{ is connected}\}, \tag{21}
$$

where $E$ ranges over undefined non-loop operation cells.

## Definition 6 (Actual cell-extension cost)

For an extension $E\subseteq(G^2\setminus\Delta)\setminus D$ and a binary assignment $b:E\to\{0,1\}$, put $D'=D\cup E$, $c'=c\cup b$. Define

$$
\alpha(D,c)=\min\{|E|:\operatorname{Aut}(G;D',Q_{D'})=\operatorname{Aut}^{\pm}(D',c')\}. \tag{22}
$$

The three quantities answer different questions: $\lambda$ synchronizes phases on a fixed action; $\mu$ repairs incidence connectivity; $\alpha$ recomputes the entire carrier action after genuine operation cells are added.

# 6. One-cell bridges and the universal upper bound

## Lemma 7 (One-cell bridge)

Any two distinct components of $\Lambda(D)$ can be joined by one undefined non-loop operation cell.

### Proof

Choose $p=(a,b)$ in one component and $q=(c,d)$ in the other. Consider $(b,c)$ and $(d,a)$. If both were loops, then $b=c$ and $d=a$, so $q=(b,a)$ and $p,q$ would already be composable. Thus at least one candidate is non-loop. If that candidate were already defined, it would already connect the components. $\square$

## Theorem 8 (Universal sparse repair bound)

$$
\boxed{\alpha(D,c)\le\mu(D)\le r-1.} \tag{23}
$$

### Proof

Apply Lemma 7 along a spanning tree of the $r$ components. At most $r-1$ new cells make $\Lambda$ connected. Equation (14) then gives exactness, independently of the bridge colors. $\square$

Neither $r-1$ nor $\mu$ is a lower bound for $\alpha$: a disconnected domain can already have trivial carrier automorphism group.

# 7. Worst-case abstract synchronization

Take $r$ disjoint carrier pairs $\{a_i,b_i\}$ and define

$$
D_i=\{(a_i,b_i),(b_i,a_i)\} \tag{24}
$$

with opposite colors on the two cells. Swapping $a_i$ and $b_i$ flips phase only on component $i$. Hence the reduct realizes $(C_2)^r$, while the full anonymous layer permits only the diagonal simultaneous flip. Therefore

$$
\boxed{\lambda(D,c)=r-1,\qquad M_{\mathrm{sync}}^{\mathrm{worst}}(r)=r-1.} \tag{25}
$$

# 8. Actual cells can outperform abstract links without bound

For a candidate cell $e\notin D$, define its old-component touch set

$$
\mathcal T_D(e)=\{C\in\pi_0(\Lambda(D)): \exists p\in C\text{ adjacent to }e\}. \tag{26}
$$

One real cell can merge every component in $\mathcal T_D(e)$ at once.

## Theorem 9 (Unbounded $\lambda/\alpha$ separation)

For every $r\ge2$ there exists a sparse binary anonymous layer with

$$
\boxed{\lambda(D,c)=r-1,\qquad\alpha(D,c)=1.} \tag{27}
$$

### Construction and proof

Use

$$
G=\{h,t\}\cup\{a_i,b_i:1\le i\le r\}. \tag{28}
$$

For each $i$ let

$$
D_i=\{(a_i,h),(b_i,h),(a_i,b_i),(b_i,a_i)\}. \tag{29}
$$

Color

$$
c(a_i,h)=c(a_i,b_i)=0,\qquad c(b_i,h)=c(b_i,a_i)=1. \tag{30}
$$

The $D_i$ are pairwise disconnected in $\Lambda(D)$, and $s_i=(a_i\ b_i)$ realizes an independent phase flip on component $i$. Hence $\lambda=r-1$.

Add one cell

$$
e=(h,t) \tag{31}
$$

with either color. It is adjacent to $(a_i,h)$ and $(b_i,h)$ for every $i$, so the enlarged incidence graph is connected. Thus $\alpha=1$. $\square$

Consequently

$$
\lambda-\alpha=r-2,\qquad \frac{\lambda}{\alpha}=r-1, \tag{32}
$$

and both gaps are unbounded.

# 9. Why $\alpha\le\lambda$ is subtle

Theorem 9 shows that $\lambda$ may drastically overestimate actual cost. It is natural to ask

$$
\boxed{\alpha(D,c)\le\lambda(D,c)\ ?} \tag{33}
$$

A monotonicity proof is impossible because adding a cell can increase the automorphism group of the domain. For example, $D=\{(0,1)\}$ has trivial carrier automorphism group on three points, whereas $D'=\{(0,1),(2,1)\}$ admits $(0\ 2)$.

# 10. No-old-obstruction theorem

Let

$$
L=\{(C_{i_s},C_{j_s}):1\le s\le\lambda\} \tag{34}
$$

be an optimal abstract phase-link system. Realize each link by one bridge cell, obtaining $D'=D\cup E$ with $|E|=\lambda$.

## Theorem 10 (No-old-obstruction)

If $g\in\operatorname{Aut}(G;D',Q_{D'})$ preserves the old domain $D$ setwise, then $g$ is a full anonymous automorphism of the extended colored layer.

### Proof

Restriction of $g$ to $D$ lies in the old group $A_Q$. Each bridge forces equality of the phase bits on its linked old components. Hence the old signature satisfies every equality in $L$. By definition of $\lambda$, every realized old signature satisfying those equalities is diagonal. Theorem 1 then forces the bridge-cell discrepancies to agree with the same phase inside their enlarged components. $\square$

Thus

$$
\boxed{\alpha>\lambda\Longrightarrow\text{every }\lambda\text{-cell realization creates a new bad automorphism moving }D.} \tag{35}
$$

# 11. Deletion-symmetry reformulation

Suppose a $\lambda$-cell bridge extension $D'=D\cup E$ admits a bad automorphism $g$ with $gD\ne D$. Then

$$
gD=D'\setminus gE \tag{36}
$$

is a different deletion of $\lambda$ cells from the same extended domain, and

$$
D'\setminus E\cong D'\setminus gE. \tag{37}
$$

Therefore any counterexample to (33) is necessarily a deletion-symmetry phenomenon.

## Corollary 11 (Recognizable-bridge criterion)

If an optimal $\lambda$-cell bridge realization can be chosen so that the old domain $D$ is setwise invariant under every automorphism of $(G;D',Q_{D'})$, then

$$
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{38}
$$

# 12. Exhaustive finite audit

## Theorem 12 (Complete four-point audit)

For every surjective partial binary layer on a four-point carrier,

$$
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{39}
$$

All **523,250** layers were enumerated. The only observed pairs $(\lambda,\alpha)$ were

$$
(0,0),\qquad(1,1),\qquad(2,1), \tag{40}
$$

with counts

$$
522398,\qquad804,\qquad48. \tag{41}
$$

## Proposition 13 (Five-point sparse audit)

For every surjective five-point binary layer with at most five defined ordered cells,

$$
\alpha(D,c)\le\lambda(D,c). \tag{42}
$$

The exhaustive sector contains **270,085** layers, of which **10,640** have $\lambda>0$. Positive cases observed are only $(1,1)$ and $(2,1)$. Targeted searches beyond this sector and on six-point carriers found no counterexample; those searches are evidence, not exhaustive theorems.

# 13. Conjecture and minimal-counterexample constraints

## Conjecture 14

For every finite sparse binary anonymous terminal layer,

$$
\boxed{\alpha(D,c)\le\lambda(D,c).} \tag{43}
$$

If false, a minimal counterexample must satisfy:

1. $|G|\ge5$;
2. if $|G|=5$, then $|D|\ge6$;
3. $\lambda\ge1$;
4. every optimal $\lambda$-cell bridge realization creates a deletion-symmetry ambiguity of the form (37), equivalently a new bad automorphism that moves the old domain $D$.

The conjecture is deliberately not promoted to a theorem.

# 14. Relation to signed and gain graphs

Signed graphs attach a $\mathbb Z_2$-label to edges and admit switching operations that modify signs while preserving cycle-balance data [2]. Gain graphs replace $\mathbb Z_2$ by an arbitrary group and organize local labels, switching functions, and global cycle constraints [3-5]. Switching isomorphism also combines switching with automorphisms of the underlying graph.

Our component phase cocycle has a related algebraic shape, but the source and logical role of the cocycle are different. In signed/gain-graph theory, switching is an **active operation**: one chooses a switching function and changes labels while preserving the appropriate switching invariants. Here there is no independently available switching operation. The cocycle is a **passive invariant**: a carrier permutation preserving the **derived anonymous equality reduct** induces the discrepancy, and sparse composability then forces that discrepancy to be constant on incidence components. The parameters $\lambda,\mu,\alpha$ likewise are not standard switching distances: they measure abstract phase synchronization, incidence repair, and actual operation-cell exactness repair.

Accordingly, the claims of this paper are restricted to the anonymous-operation model rather than presented as a replacement for signed/gain-graph theory.

# 15. Structural hierarchy

The fixed-domain phase problem is

$$
D\longrightarrow\Lambda(D)\longrightarrow\varepsilon\longrightarrow\Sigma(D,c)\longrightarrow\lambda(D,c). \tag{44}
$$

The real extension problem is

$$
D\longrightarrow\mathcal T_D\longrightarrow\mu(D)\longrightarrow\alpha(D,c). \tag{45}
$$

Universally,

$$
0\le\lambda(D,c)\le r-1, \tag{46}
$$

and

$$
\boxed{0\le\alpha(D,c)\le\mu(D)\le r-1.} \tag{47}
$$

There is no growing lower bound on $\alpha$ in terms of $\lambda$: Theorem 9 has $\lambda=r-1$ and $\alpha=1$. The opposite comparison is Conjecture 14.

# 16. Conclusion

Sparse anonymous value geometry is controlled not merely by the number of disconnected cell regions but by the phases that carrier automorphisms actually realize on them. The correct invariant is a componentwise $\mathbb Z_2$-valued 1-cocycle, and exactness is equivalent to diagonality of all realized cocycle values.

This separates three notions of repair cost. Abstract phase synchronization can require $r-1$ links, yet one operation cell may synchronize all components at once. Consequently $\lambda/\alpha$ is unbounded. Real cell extensions are therefore not merely implementations of abstract constraints; they can reorganize incidence geometry itself.

The remaining comparison $\alpha\le\lambda$ is subtler because operation-cell addition is not monotone at the level of automorphism groups. The No-old-obstruction theorem shows that any failure must come from genuinely new symmetries created by the extension, equivalently from deletion ambiguity in the extended domain. Exhaustive small cases support the conjecture but do not settle it.

This gives a clean boundary for further work: the next problem is no longer phase propagation itself, but the reconstruction theory of sparse operation domains under symmetry-creating extensions. A second, independent continuation is the sparse $q\ge3$ problem. In that setting the anonymous alphabet has no canonical $\mathbb Z_q$ structure; the natural local phase is generally permutation-valued, suggesting a non-abelian $S_q$-phase transport problem rather than a formal replacement of $\mathbf F_2$ by $\mathbb Z_q$. The algorithmic complexity of computing $\lambda$, $\mu$, and $\alpha$ is likewise left open; no complexity classification is claimed here.

---

# References

[1] A. Malachevsky, *Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition*, Zenodo, 2026. DOI: **10.5281/zenodo.22157403**.

[2] T. Zaslavsky, “Signed graphs,” *Discrete Applied Mathematics* **4** (1982), 47-74. DOI: **10.1016/0166-218X(82)90033-6**.

[3] T. Zaslavsky, “Biased graphs. I. Bias, balance, and gains,” *Journal of Combinatorial Theory, Series B* **47** (1989), 32-52. DOI: **10.1016/0095-8956(89)90063-4**.

[4] N. A. Neudauer and D. Slilaty, “Bounding and stabilizing realizations of biased graphs with a fixed group,” *Journal of Combinatorial Theory, Series B* **122** (2017), 149-166. DOI: **10.1016/j.jctb.2016.05.008**.

[5] M. Cavaleri, D. D'Angeli, and A. Donno, “Gain-line graphs via G-phases and group representations,” *Linear Algebra and its Applications* **613** (2021), 241-270. DOI: **10.1016/j.laa.2020.11.009**.

---

## Publication note

Conjecture 14 is intentionally open. Every theorem and finite audit stated above is logically independent of its truth. The conjecture is the precise handoff to the next research phase, not an unproved dependency of the present article.