# SOL-LOCALITY — AQFT, Orthogonality, and Geometry-Conditioned Commutation on the FCOA-Z Line

**Version:** 0.1  
**Date:** 2026-08-30  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIRST TARGET COMPLETE / DISCRETE LOCALITY FORMALIZED / LITERAL AQFT IDENTIFICATION REJECTED  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264

---

## 1. Executive verdict

The SOL-LOCALITY brief survives, but in a sharper form than the initial analogy.

The positive result is that the completed FCOA-Z axis carries a canonical **branch-separation relation** determined entirely by its rooted/reflected geometry. This relation can be used as an operation-independent locality predicate. One can then formulate

\[
L_{\pm}(x,y)\Longrightarrow \mathcal C_{\widehat\oplus}(x,y)=EQ,
\tag{1}
\]

for conservative mixed-sector extensions of the legacy FCOA operation. Such extensions exist entirely inside the one-dimensional carrier, preserve the old ray exactly, preserve reflection, and leave the full operation globally noncommutative.

Hence the central slogan is mathematically realizable:

\[
\boxed{\text{one fixed operation can be globally noncommutative while a geometrically selected pair class commutes}.}
\tag{2}
\]

The negative result is equally important. Literal Haag-Kastler microcausality is **not** present on the FCOA line. In Lorentzian dimension one, nontrivial causal disjointness does not occur; the AQFT literature explicitly notes that the Einstein-causality condition becomes nontrivial only in spacetime dimension at least two. Therefore opposite FCOA signs cannot be identified with spacelike separation.

The correct mature comparison is instead the more general language of **orthogonality relations** used in modern algebraic formulations of AQFT: a geometric or categorical relation selects pairs of subobjects whose images must commute. In that abstract sense, FCOA-Z admits a genuine discrete locality shadow.

A second obstruction is decisive for the line-completion programme: locality is only a **compatibility constraint**. It does not determine the value of a mixed interaction. In fact, locality + reflection + legacy exactness admit a countably infinite family of generated conservative one-dimensional mixed-sector realizations. Thus locality alone leaves LC3 underdetermined.

Programme verdict:

\[
\boxed{\texttt{FORMAL EMBEDDING}}
\]

with scope qualifier:

\[
\boxed{\text{orthogonality/locality shadow only; not an AQFT model and not a spacetime identification}.}
\tag{3}
\]

Line-completion verdict:

\[
\boxed{\texttt{1D-CLOSED for locality realization; UNDERDETERMINED as a mixed-value principle}.}
\tag{4}
\]

---

## 2. FCOA-Z input used

Write the completed axis as

\[
X=\{x_k:k\in\mathbb Z\},\qquad x_k=T^k x_0,
\tag{5}
\]

with derived reflection

\[
\nu(x_k)=x_{-k},\qquad \nu^2=\operatorname{id},\qquad \nu T=T^{-1}\nu.
\tag{6}
\]

The signed branches are

\[
X^+=\{x_k:k>0\},\qquad X^-=\{x_k:k<0\}.
\tag{7}
\]

For the legacy operation \(\oplus\), the right-root action is the proved radial contraction law

\[
x_k\oplus x_0=x_{k-\operatorname{sgn}(k)},\qquad k\ne0,
\tag{8}
\]

while

\[
x_0\oplus x_k=x_k.
\tag{9}
\]

Thus the operation remains noncommutative:

\[
x_0\oplus x_k\ne x_k\oplus x_0\qquad(k\ne0).
\tag{10}
\]

The Mixed-Sector Localization Theorem of the published FCOA-Z core fixes the positive legacy sector, forces the negative-negative sector by reflection, and leaves new binary base-interaction freedom only in

\[
(X^+\times X^-)\cup(X^-\times X^+).
\tag{11}
\]

No ordinary integer addition or multiplication is introduced below.

---

## 3. Target-field definitions: what AQFT locality actually says

In Haag-Kastler AQFT one assigns an algebra of observables to a spacetime region:

\[
\mathcal O\longmapsto \mathcal A(\mathcal O).
\tag{12}
\]

The standard local-net structure contains several logically distinct ingredients.

### 3.1 Isotony

If

\[
\mathcal O_1\subseteq \mathcal O_2,
\]

then

\[
\mathcal A(\mathcal O_1)\subseteq \mathcal A(\mathcal O_2).
\tag{13}
\]

### 3.2 Locality / Einstein causality

If regions \(\mathcal O_1\) and \(\mathcal O_2\) are spacelike separated, then every observable in one local algebra commutes with every observable in the other:

\[
[A,B]=0
\quad
\text{for all }A\in\mathcal A(\mathcal O_1),\ B\in\mathcal A(\mathcal O_2).
\tag{14}
\]

Equivalently,

\[
\mathcal A(\mathcal O_1)\subseteq \mathcal A(\mathcal O_2)'.
\tag{15}
\]

This does **not** say that the global observable algebra is commutative.

### 3.3 Covariance and causal structure

In relativistic AQFT, the regions live in Lorentzian spacetime and their causal relation is part of the background structure. Covariance controls how the local net transforms under the relevant spacetime symmetries or, in locally covariant formulations, under suitable spacetime embeddings.

### 3.4 States

A state is represented algebraically by a positive normalized linear functional on the observable algebra. The state layer is essential for expectation values, correlations, representations, vacuum structure, spectrum conditions, and entanglement questions.

### 3.5 Modern abstraction by orthogonal categories

Benini-Schenkel-Woike abstract the locality mechanism away from a specific spacetime. An **orthogonal category** is a category equipped with a symmetric, composition-stable relation on pairs of morphisms with common target. A QFT-like functor into associative unital algebras is required to map orthogonal pairs to commuting subalgebras.

This abstraction is crucial for SOL-LOCALITY because it cleanly separates two statements:

\[
\boxed{\text{relation-selected commutation}}
\tag{16}
\]

from the specifically relativistic interpretation

\[
\boxed{\text{orthogonality = causal disjointness in Lorentzian spacetime}.}
\tag{17}
\]

FCOA-Z may realize (16) without possessing (17).

---

## 4. The first discrete locality predicate

### Definition 4.1 — branch-separation locality

For nonroot points define

\[
L_{\pm}(x,y)
\iff
(x\in X^+\wedge y\in X^-)
\vee
(x\in X^-\wedge y\in X^+).
\tag{18}
\]

Thus \(L_{\pm}\) says only that the two arguments lie on opposite components of the rooted axis after removal of the root.

It does **not** say that they are spacelike separated.

### Proposition 4.2

The relation \(L_{\pm}\) is:

1. symmetric;
2. irreflexive;
3. determined independently of the operation table;
4. invariant under reflection:
   \[
   L_{\pm}(x,y)\iff L_{\pm}(\nu x,\nu y).
   \tag{19}
   \]

#### Proof

Symmetry follows because exchanging the two arguments exchanges the two clauses in (18). Irreflexivity follows because no nonroot point belongs simultaneously to both branches. The definition uses only the branch decomposition of the completed rooted carrier, not \(\oplus\). Finally, reflection exchanges \(X^+\) with \(X^-\), so opposite-branch membership is preserved as a relation. \(\square\)

### Why operation-independence matters

If one defined locality by

\[
L(x,y)\iff \mathcal C_\oplus(x,y)=EQ,
\tag{20}
\]

then every operation would be “local” by construction. Such a predicate has no explanatory content.

Therefore any serious locality principle must satisfy the independence requirement:

\[
\boxed{L\text{ is fixed from carrier/support geometry before the commutation status is inspected}.}
\tag{21}
\]

This is the first hostile-audit condition for all future FCOA locality claims.

---

## 5. Region version and orthogonal-category shadow

Let \(\mathbf{Reg}(X)\) be the poset category of finite subsets of \(X\setminus\{x_0\}\), with inclusions as morphisms.

For inclusions

\[
U\hookrightarrow W\hookleftarrow V
\]

with common target \(W\), define

\[
U\perp_{\pm}V
\iff
L_{\pm}(u,v)\text{ for every }u\in U,\ v\in V.
\tag{22}
\]

### Theorem 5.1 — discrete orthogonality theorem

The pair

\[
(\mathbf{Reg}(X),\perp_{\pm})
\tag{23}
\]

is an orthogonal category: \(\perp_{\pm}\) is symmetric and stable under precomposition by subregion inclusions and postcomposition into larger ambient regions.

#### Proof

Symmetry follows from Proposition 4.2. If \(U'\subseteq U\) and \(V'\subseteq V\), then every pair in \(U'\times V'\) is already a pair in \(U\times V\), so orthogonality is preserved under precomposition. Postcomposition into a larger ambient region changes neither \(U\) nor \(V\), hence preserves the relation. \(\square\)

This is already a mathematically clean locality-style abstraction independent of QFT.

---

## 6. A minimal algebraic locality envelope

Let \(K\) be a field. For a finite region \(U\subseteq X\setminus\{x_0\}\), put

\[
U^+=U\cap X^+,
\qquad
U^-=U\cap X^-.
\tag{24}
\]

Define

\[
\mathfrak A_{\pm}(U)
:=
K\langle U^+\rangle\otimes_K K\langle U^-\rangle,
\tag{25}
\]

where \(K\langle S\rangle\) denotes the free associative unital algebra on the generators indexed by \(S\).

An inclusion \(U\subseteq V\) induces the evident injective homomorphism

\[
\mathfrak A_{\pm}(U)\hookrightarrow \mathfrak A_{\pm}(V).
\tag{26}
\]

### Theorem 6.1 — branch-locality envelope

The assignment

\[
U\longmapsto \mathfrak A_{\pm}(U)
\tag{27}
\]

is an isotonic algebra-valued net on \(\mathbf{Reg}(X)\). If

\[
U\perp_{\pm}V
\]

inside \(W\), then the images of \(\mathfrak A_{\pm}(U)\) and \(\mathfrak A_{\pm}(V)\) commute elementwise in \(\mathfrak A_{\pm}(W)\).

If one branch contains at least two generators, the ambient algebra is nevertheless noncommutative.

#### Proof

Isotony follows from the canonical embeddings of free algebras on subsets and tensor products over a field. If \(U\perp_{\pm}V\), one region lies entirely on one branch and the other entirely on the opposite branch. Their images therefore lie in the two different tensor factors in (25), and elements from different tensor factors commute.

On the other hand, two distinct generators in the same free-algebra factor do not commute. Hence the total algebra is noncommutative whenever a branch contains at least two generators. \(\square\)

Thus the abstract pattern

\[
\boxed{\text{global noncommutativity + geometry-selected commuting subalgebras}}
\tag{28}
\]

exists canonically on the signed FCOA carrier after one additional free-algebra envelope construction.

This is a formal locality shadow, not a quantum-field model.

---

## 7. Bringing locality back to the actual FCOA operation

The preceding envelope proves that the geometry supports a Haag-Kastler-style logical pattern, but the brief asks a stronger question: can the **existing FCOA operation** be conservatively completed so that branch separation controls commutation?

The answer is yes.

### 7.1 Intrinsic radial depth

Let

\[
R(x):=x\oplus x_0
\qquad(x\ne x_0).
\tag{29}
\]

By the radialization theorem, repeated application reaches the root. Define the radial depth \(d(x)\) intrinsically as the number of applications of \(R\) required to reach \(x_0\). Hence

\[
d(x_k)=|k|,
\qquad
 d(\nu x)=d(x).
\tag{30}
\]

This uses the already published rooted-line structure; no new ordinary addition or multiplication is inserted.

### 7.2 The nearest-branch selector

For \(L_{\pm}(x,y)\), define

\[
N(x,y)=
\begin{cases}
 x,&d(x)<d(y),\\
 y,&d(y)<d(x),\\
 x_0,&d(x)=d(y).
\end{cases}
\tag{31}
\]

The rule is symmetric in the unordered pair and reflection-equivariant:

\[
N(y,x)=N(x,y),
\qquad
N(\nu x,\nu y)=\nu N(x,y).
\tag{32}
\]

### Definition 7.1 — nearest locality extension

Define \(\widehat\oplus_N\) by:

1. every old defined cell keeps exactly its old value;
2. every old non-mixed undefined cell remains undefined;
3. for every opposite-branch pair,
   \[
   x\widehat\oplus_N y
   =
   y\widehat\oplus_N x
   :=N(x,y).
   \tag{33}
   \]

### Theorem 7.2

The extension \(\widehat\oplus_N\) is a conservative one-dimensional mixed-sector realization satisfying

\[
L_{\pm}(x,y)
\Longrightarrow
\mathcal C_{\widehat\oplus_N}(x,y)=EQ.
\tag{34}
\]

It preserves reflection equivariance, base-line closure, the complete positive legacy ray, and finite-window coherence.

#### Proof

Only previously unrealized mixed-sign cells are assigned new values, so all legacy cells remain unchanged. Equation (31) always returns a base-line element, proving closure. Symmetry in (32) gives equality of the two input orders, hence (34). Reflection equivariance follows from depth invariance and the second identity in (32). Restriction to any finite depth window uses the same depth-comparison rule as the global structure, giving finite-window coherence. \(\square\)

### Corollary 7.3 — locality without global commutativity

For every \(k\ne0\), legacy root interaction still gives

\[
x_0\widehat\oplus_N x_k=x_k,
\qquad
x_k\widehat\oplus_N x_0=x_{k-\operatorname{sgn}(k)},
\tag{35}
\]

so \(\widehat\oplus_N\) is globally noncommutative even though every \(L_{\pm}\)-pair commutes.

This is the exact FCOA realization of the SOL-LOCALITY slogan.

---

## 8. Local commutativity does not force associativity

The nearest extension remains genuinely nonassociative.

### Proposition 8.1

For the triple \((x_2,x_{-1},x_0)\),

\[
\mathcal A_{\widehat\oplus_N}(x_2,x_{-1},x_0)=NEQ.
\tag{36}
\]

#### Proof

Because \(d(x_{-1})<d(x_2)\),

\[
x_2\widehat\oplus_N x_{-1}=x_{-1}.
\]

Therefore

\[
(x_2\widehat\oplus_N x_{-1})\oplus x_0
=x_{-1}\oplus x_0
=x_0.
\tag{37}
\]

But

\[
x_{-1}\oplus x_0=x_0,
\]

so

\[
x_2\oplus(x_{-1}\oplus x_0)
=x_2\oplus x_0
=x_1.
\tag{38}
\]

Since \(x_0\ne x_1\), the two bracketings are unequal. \(\square\)

Thus

\[
\boxed{L_{\pm}\text{-commutativity does not collapse the FCOA operation to an associative commutative law}.}
\tag{39}
\]

---

## 9. The crucial negative theorem: locality does not generate mixed values

AQFT microcausality tells us **which separated algebras commute**. It does not specify the detailed multiplication table of the theory. The same phenomenon appears in FCOA-Z.

To make this precise, define a clamped radial contraction

\[
R^{[j]}(z)=
\begin{cases}
R^j(z),&j\le d(z),\\
x_0,&j>d(z),
\end{cases}
\qquad j\in\mathbb N_0,
\tag{40}
\]

with \(R^{[j]}(x_0)=x_0\).

For every \(j\ge0\), define a mixed selector

\[
N_j(x,y):=R^{[j]}(N(x,y)).
\tag{41}
\]

and a corresponding conservative extension \(\widehat\oplus_{N_j}\) by using \(N_j\) on every opposite-branch pair while leaving the legacy operation untouched elsewhere.

### Theorem 9.1 — locality underdetermination theorem

For every \(j\ge0\), \(\widehat\oplus_{N_j}\) is a conservative, reflection-equivariant, one-dimensional extension satisfying

\[
L_{\pm}(x,y)
\Longrightarrow
\mathcal C_{\widehat\oplus_{N_j}}(x,y)=EQ.
\tag{42}
\]

The family

\[
\{\widehat\oplus_{N_j}:j\in\mathbb N_0\}
\tag{43}
\]

contains infinitely many distinct mixed-sector laws.

#### Proof

The radial map commutes with reflection because the root is reflection-fixed and the legacy transfer is reflection-equivariant. Therefore every clamped iterate \(R^{[j]}\) is reflection-equivariant. Since \(N\) is symmetric, each \(N_j\) is symmetric, proving the commutation status in (42). All values remain on the old base line and no old cell is altered.

To distinguish the laws, compare consecutive parameters \(j\) and \(j+1\) on a pair whose nearer element has depth \(j+1\), for example \((x_{j+1},x_{-(j+2)})\). The nearest selector returns \(x_{j+1}\). Then

\[
R^{[j]}(x_{j+1})=x_1,
\qquad
R^{[j+1]}(x_{j+1})=x_0.
\tag{44}
\]

Hence the two extensions differ. \(\square\)

### Consequence for LC3

Locality + reflection + legacy exactness do **not** determine a unique mixed-sector operation and do not even reduce the choices to a finite family.

Therefore, in the Line Completion Gate vocabulary, locality used by itself yields

\[
\boxed{\texttt{REALIZABLE WILD / UNDERDETERMINED}.}
\tag{45}
\]

This is not a failure of the analogy. It is exactly the correct lesson from AQFT: microcausality constrains compatibility; it is not a value-generation principle.

A further FCOA invariant is still needed to select one mixed law.

---

## 10. The literal 1D-AQFT obstruction

The strongest physical-sounding version of the analogy fails for a simple structural reason.

For ordinary Lorentzian AQFT, locality is based on **causal disjointness**, especially spacelike separation. But in one-dimensional Lorentzian spacetime there is only a time direction; nontrivial causally disjoint open regions do not occur. Modern work on one-dimensional AQFT states explicitly that Einstein causality becomes a nontrivial phenomenon only in dimensions \(m\ge2\).

Therefore the implication

\[
L_{\pm}(x,y)\Longrightarrow \mathcal C(x,y)=EQ
\]

cannot be interpreted as a literal discretization of spacelike microcausality on a 1D spacetime.

In particular:

\[
\boxed{X^+\text{ and }X^-\text{ are not left/right spacelike regions}.}
\tag{46}
\]

This directly enforces the prohibited shortcut in the director brief.

The useful comparison survives only at the abstract relation-locality level of orthogonal categories.

---

## 11. Required negative test: AQFT ingredients absent from FCOA-Z

The present FCOA-Z line lacks the following structures required for a physical AQFT identification.

### 11.1 No Lorentzian causal structure

FCOA-Z has a rooted discrete shift, reflection, branch decomposition, and radial depth. It has no light cones, causal future/past relation, Lorentzian metric, or spacelike complement.

### 11.2 No native local net

FCOA-Z assigns elements and partial-operation values, not an observable algebra \(\mathcal A(\mathcal O)\) to each localization region. The net in Section 6 is an added envelope construction, not part of the published FCOA core.

### 11.3 No AQFT isotony axiom in the core

The FCOA carrier has nested finite windows and substructures, but there is no native theorem assigning nested observable algebras to nested regions. Isotony only appears after the additional algebra-valued net construction.

### 11.4 No spacetime covariance

The shift/reflection relations of FCOA-Z are not Lorentz/Poincare covariance. The infinite-dihedral symmetry shadow of the rooted axis is a different structure.

### 11.5 No state space

FCOA-Z currently has no positive normalized linear functionals, GNS representations, vacuum state, spectrum condition, expectation values, or probabilistic measurement interpretation.

### 11.6 No local quantum operator structure

The partial operation \(\oplus\) is not operator multiplication in a C*- or von Neumann algebra. Equality of two FCOA values is therefore not the same mathematical statement as vanishing of an operator commutator.

### 11.7 No statistical independence or entanglement layer

Even in AQFT, commuting spacelike-separated algebras can support entangled states; microcausality is not the statement that correlations vanish. FCOA-Z has no state layer at all, so no claim about no-signalling, independence, or entanglement follows from (34).

### 11.8 No time-slice / primitive-causality structure

No analogue has yet been constructed of Cauchy evolution or the time-slice axiom.

These absences block every present physical identification.

---

## 12. Correspondence dictionary

| AQFT / orthogonal-category object | FCOA-Z locality shadow | Status |
|---|---|---|
| spacetime region \(\mathcal O\) | finite carrier region \(U\subset X\setminus\{x_0\}\) | formal only |
| causal/spacelike disjointness | branch relation \(L_{\pm}\) | analogy, not causal |
| orthogonality relation \(\perp\) | \(\perp_{\pm}\) on region inclusions | exact formal analogue |
| local algebra \(\mathcal A(\mathcal O)\) | \(\mathfrak A_{\pm}(U)\) free-algebra envelope | added construction |
| isotony | inclusion-induced embeddings | exact in envelope |
| Einstein causality | commuting opposite-branch tensor factors | exact in envelope, nonphysical |
| observable commutator \([A,B]=0\) | \(\mathcal C_{\widehat\oplus}(x,y)=EQ\) | logical analogue only |
| global noncommutative algebra | legacy FCOA root asymmetry survives | exact structural match |
| Lorentz covariance | none | absent |
| states / vacuum / GNS | none | absent |
| spectrum condition | none | absent |
| causal propagation | none | absent |

The strongest exact common structure is therefore

\[
\boxed{\text{an independently defined relation selects the input pairs on which an algebraic compatibility law holds}.}
\tag{47}
\]

---

## 13. Hostile tests

### 13.1 Derived-locality vacuity

If locality is defined from the commutation table, the principle is tautological. Therefore \(L\) must be generated independently from carrier/support geometry.

### 13.2 Singleton-disjointness collapse

If one used ordinary set-theoretic point disjointness on the FCOA axis, then every pair of distinct singleton supports would be “local.” A locality axiom would then force almost all distinct arguments to commute, destroying the selective mixed-sector phenomenon. Thus mere disjointness of points is too coarse for the intended FCOA law spectrum.

### 13.3 Opposite-sign is not causal complement

The relation \(L_{\pm}\) is complete bipartite branch separation. AQFT spacelike separation has very different causal geometry. No metric or causal cone is encoded by the sign split.

### 13.4 Locality does not imply statistical independence

Even in genuine AQFT, commuting algebras need not have product states; entanglement can remain. Hence no FCOA interpretation of \(EQ\) as “no influence,” “no correlation,” or “independent systems” is justified.

### 13.5 Locality does not determine the interaction law

Theorem 9.1 supplies infinitely many conservative generated mixed laws satisfying the same locality relation. Any claim that AQFT locality “selects” the missing FCOA mixed operation is therefore false without additional axioms.

---

## 14. Line Completion Gate assessment

### LC1 — cell realization

For mixed-sign old `UNDEF` cells, geometry-conditioned commutation is conservatively realizable. The nearest family gives explicit base-valued realizations.

However locality alone leaves infinitely many choices:

\[
\boxed{\text{LC1/LC3 under locality alone: REALIZABLE WILD}.}
\tag{48}
\]

### LC2 — output re-entry

SOL-LOCALITY does not require re-entry of \(E^+,E^*,E^\times\), and no AQFT analogy licenses such a move. This remains open and must be handled by an independent invariant.

### LC3 — mixed-sign realization

The relation

\[
L_{\pm}\Longrightarrow EQ
\]

is consistent with a fully base-valued one-dimensional realization. Therefore locality does not force a new coordinate, new fiber, or second dimension.

### One-dimensional closure status

\[
\boxed{\texttt{1D-CLOSED}.}
\tag{49}
\]

for the existence of locality-conditioned mixed commutation.

But because the value law is not selected uniquely,

\[
\boxed{\texttt{UNDERDETERMINED}.}
\tag{50}
\]

for the full locality-driven completion problem.

There is no `DIMENSION-FORCING` result here.

---

## 15. What is genuinely learned from AQFT

The physical analogy contributes one robust methodological idea:

\[
\boxed{\text{commutativity need not be a global axiom; it may be conditional on an independently given relation of localization}.}
\tag{51}
\]

Modern AQFT mathematics goes further and shows that the causal interpretation can be abstracted to an orthogonality relation. This validates the mathematical seriousness of relation-conditioned commutation without granting a spacetime interpretation.

For FCOA-Z the potentially distinctive question is now narrower:

\[
\boxed{\text{can the reflected-axis geometry select not merely the commuting sector, but a unique natural mixed value law?}}
\tag{52}
\]

Theorem 9.1 says locality alone cannot do so.

---

## 16. Next research target

The next SOL-LOCALITY strike should not search for a stronger physics analogy. It should search for an **internal selector invariant** that reduces the wild family of locality-compatible mixed extensions.

A useful selector must be independent of ordinary addition and multiplication and should be tested against at least:

1. radial-depth monotonicity;
2. reflection equivariance;
3. finite-window coherence;
4. no new coordinate memory beyond the published line;
5. association-spectrum constraints;
6. compatibility with terminal-output typing;
7. automorphism rigidity;
8. minimality/universality.

The sharp problem is:

\[
\boxed{
\text{Does any natural FCOA-internal axiom reduce }
\{\widehat\oplus_{N_j}\}_{j\ge0}
\text{ to one equivalence class?}
}
\tag{53}
\]

If yes, SOL-LOCALITY would become a value-selection mechanism rather than only a compatibility principle. If no, a no-go theorem would show that locality can never complete LC3 by itself.

---

## 17. Publication recommendation

The result is mathematically clean and useful, but a standalone AQFT/FCOA paper is premature because the strongest physical identification is explicitly rejected and the mixed law remains underdetermined.

Recommendation:

\[
\boxed{\texttt{HOLD FOR APPLIED-DIRECTIONS SYNTHESIS}.}
\tag{54}
\]

The publishable components for a later synthesis are:

1. the discrete branch-locality predicate;
2. the orthogonal-category theorem;
3. the branch-locality algebra envelope;
4. the explicit conservative FCOA locality extension;
5. the locality-under\-determination theorem;
6. the 1D Lorentzian AQFT obstruction.

These results should be combined with the other applied directions only after their own hostile audits are complete.

---

## 18. References

1. R. Haag and D. Kastler, **An Algebraic Approach to Quantum Field Theory**, *Journal of Mathematical Physics* 5 (1964), 848-861. DOI: `10.1063/1.1704187`.
2. C. J. Fewster and K. Rejzner, **Algebraic Quantum Field Theory — an introduction**, arXiv:`1904.04051`.
3. M. Benini, A. Schenkel, and L. Woike, **Operads for algebraic quantum field theory**, *Communications in Contemporary Mathematics* 23 (2021), 2050007. DOI: `10.1142/S0219199720500078`; arXiv:`1709.08657`.
4. R. Brunetti, K. Fredenhagen, and R. Verch, **The Generally Covariant Locality Principle — A New Paradigm for Local Quantum Field Theory**, *Communications in Mathematical Physics* 237 (2003), 31-68. DOI: `10.1007/s00220-003-0815-7`.
5. M. Benini, M. Perin, and A. Schenkel, **Smooth 1-Dimensional Algebraic Quantum Field Theories**, *Annales Henri Poincare* 23 (2022), 2069-2111. DOI: `10.1007/s00023-021-01132-2`; arXiv:`2010.13808`.
6. A. Ivanov and Commander Sol, **FCOA-Z v1.1** (published mathematical base), Zenodo DOI: `10.5281/zenodo.22169264`.
