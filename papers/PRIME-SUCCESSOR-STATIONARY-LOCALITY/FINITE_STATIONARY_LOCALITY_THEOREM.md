# Finite Stationary Locality for Private-Place Bridges

**Research checkpoint**  
**Date:** 2026-08-26  
**Status:** theorem-level draft after adversarial repair  

## 1. Purpose

This note abstracts the fixed-ball argument from the Ramanujan bridge and proves the finite multi-place version needed for the next publication.

The central point is that finitely many stationary local windows increase the number of local colors seen by a fixed formula, but do not provide a scalable coordinate system. The proof combines finite-depth target normal form, private-place linear separation, fresh-private-place avoidance, and formula-relative witness transport.

---

## 2. Structure and hypotheses

Fix a finite set of rational primes

\[
S=\{\ell_1,\dots,\ell_s\}.
\]

For \(\ell\in S\), let

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

We study

\[
\mathcal B_{u,S}=\Bigl((\mathbb N_{>0},\times),(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U\Bigr),
\]

where \(U(p,x)\) links prime atoms \(p\) to rational labels \(u_p\).

Assume that, after removing a finite exceptional set of prime atoms, the remaining primes split into:

1. an infinite set \(R\) of **regular primes**;
2. finitely many **exact defect classes** \(D_1,\dots,D_t\), with a fixed common rational label \(\delta_j\) on each \(D_j\).

For regular primes assume:

### (H1) S-integrality

\[
\forall p\in R\ \forall \ell\in S\qquad v_\ell(u_p)\ge0.
\]

### (H2) Private place

There is an injective map

\[
\lambda:R\to\mathbb P\setminus S
\]

such that

\[
v_{\lambda(p)}(u_p)<0
\]

and for every distinct \(p,q\in R\),

\[
v_{\lambda(p)}(u_q)\ge0.
\]

### (H3) Defect integrality at private places

After enlarging the finite exceptional set if necessary, for every \(p\in R\) and every defect label \(\delta_j\),

\[
v_{\lambda(p)}(\delta_j)\ge0.
\]

### (H4) Prime-only bridge

\[
U(n,x)\Longrightarrow \operatorname{Prime}(n).
\]

Thus the bridge does not transmit source multiplicity from \(p^k\) into the target sort.

---

## 3. Fixed-depth predicates

For each fixed \(m\in\mathbb Z\), define

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

These are definable in the original language.

For \(m>0\),

\[
B_{\ell,m}(x)\iff \exists y\,(\ell^m y=x\land B_\ell(y)),
\]

and

\[
B_{\ell,-m}(x)\iff B_\ell(\ell^m x).
\]

---

## 4. Local coverage lemma

Fix one place \(\ell\). Let

\[
P=a+B_{\ell,m}
\]

be a positive base coset, and let

\[
C_i=b_i+B_{\ell,n_i}\qquad (1\le i\le r)
\]

be finitely many forbidden cosets.

Because \(\ell\)-adic balls are nested or disjoint, each \(C_i\cap P\) is empty, equal to \(P\), or a subcoset of \(P\). If one equals \(P\), the surviving set is empty. Otherwise, if

\[
N=\max_i n_i,
\]

coverage of \(P\) by the surviving forbidden subcosets is decided in the finite quotient

\[
B_{\ell,m}/B_{\ell,N},
\]

whose cardinality is

\[
\ell^{N-m}.
\]

Hence the condition

\[
P\setminus\bigcup_i C_i\ne\varnothing
\]

is equivalent to a finite Boolean combination of relations of the forms

\[
a-b_i\in B_{\ell,k},\qquad b_i-b_j\in B_{\ell,k},
\]

for fixed depths \(k\) appearing in the finite refinement tree.

If there is no positive base coset at the place \(\ell\), finitely many forbidden cosets cannot cover all of \(\mathbb Q\): choose an element of sufficiently negative \(\ell\)-adic valuation.

---

## 5. Multi-place target finite-depth normal form

### Theorem 5.1

Every first-order formula in

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in S})
\]

is equivalent to a Boolean combination of formulas

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in B_{\ell,m},
\qquad \ell\in S,\ m\in\mathbb Z,
\]

where \(L\) is a rational linear form and only finitely many fixed pairs \((\ell,m)\) occur for a fixed formula.

### Proof

After DNF it is enough to eliminate one target quantifier \(\exists y\) from a conjunction of literals.

If a non-trivial exact equation

\[
ay+t(\bar x)=0,\qquad a\ne0,
\]

occurs, \(y\) is uniquely determined and eliminated by substitution.

Assume now that no exact equation pins \(y\). Every positive ball literal involving \(y\) is equivalent to a coset condition

\[
y\in a+B_{\ell,m}.
\]

For each fixed place \(\ell\), all positive cosets are nested/disjoint, hence they reduce either to inconsistency or to one deepest positive base coset. Negative cosets at that place are handled by the Local Coverage Lemma.

Thus for every \(\ell\in S\) we obtain a non-empty local set \(U_\ell\subseteq\mathbb Q_\ell\), open and defined by finitely many fixed-depth ball conditions, or else the original conjunction is inconsistent.

If all \(U_\ell\) are non-empty, weak approximation (equivalently, a direct CRT argument after clearing denominators) gives a rational \(y\) satisfying all local conditions simultaneously.

Finally, finitely many exact inequalities \(y\ne c_j\) remove finitely many points. Every non-empty multi-place cell contains a coset

\[
a+\bigcap_{\ell\in S}B_{\ell,M_\ell}
\]

and therefore infinitely many rational points, so finitely many point exclusions do not destroy non-emptiness.

Hence projection stays inside the stated Boolean algebra. ∎

---

## 6. Multi-place generic cell lemma

### Lemma 6.1

Every non-empty Boolean cell cut out by finitely many fixed-depth target conditions contains a refinement coset

\[
a+H_{\mathbf M},
\qquad
H_{\mathbf M}:=\bigcap_{\ell\in S}B_{\ell,M_\ell},
\]

for some rational \(a\) and some finite depth vector \(\mathbf M=(M_\ell)_{\ell\in S}\).

### Proof

Choose one point \(a\) in the non-empty cell. At each place \(\ell\), choose \(M_\ell\) deeper than every boundary depth occurring in the finitely many literals defining the cell. Any perturbation by an element of \(H_{\mathbf M}\) preserves all fixed-depth membership and non-membership relations at every place. ∎

---

## 7. Exact linear separation

Fix integers \(d_1,\dots,d_r\). Outside the finite set of regular primes whose private places divide a non-zero aggregate coefficient, a homogeneous relation

\[
\sum_i d_i u_{p_i}=0
\]

can hold only if, after grouping equal primes, the aggregate coefficient of every regular-prime block is zero.

Indeed, for a block with representative \(p\) and non-zero aggregate coefficient \(d\), valuation at \(\lambda(p)\) sees one negative contribution \(d u_p\), while all other regular labels and all defect labels are \(\lambda(p)\)-integral. This is impossible outside the finite coefficient-exception set.

Thus fixed homogeneous relations on the regular tail are determined by equality patterns and defect classes.

---

## 8. Reduced affine-fiber lemma

Consider

\[
\sum_{i=1}^r c_i u_{p_i}=t
\]

with fixed coefficients \(c_i\), and fix an equality pattern \(\pi\) on the prime variables. For every block \(C\in\pi\), set

\[
d_C=\sum_{i\in C}c_i.
\]

Blocks with \(d_C=0\) disappear from the reduced equation and remain free.

### Lemma 8.1

For the blocks with \(d_C\ne0\), the number of regular-prime assignments to the reduced affine equation is uniformly bounded in terms of the coefficient scheme alone, after excluding a finite coefficient-exception set.

### Proof

Suppose \((q_C)\) and \((q'_C)\) are two reduced solutions. Subtracting gives a homogeneous relation. Exact linear separation implies that every prime occurring in the second solution must occur among the finitely many primes of the first solution with compatible aggregate coefficient. Therefore a second solution is obtained from a finite reassignment of those primes to the finitely many non-zero blocks. A crude bound \(m^m\), with \(m\) the number of non-zero blocks, suffices. ∎

Thus exact affine traces are finite unions of **bounded-anchor cylinders**: zero-sum blocks are free, while only finitely many non-zero blocks can be anchored to exceptional regular primes.

---

## 9. Fresh-private-place avoidance

Fix a non-empty multi-place cell containing

\[
a+H_{\mathbf M}.
\]

Assume every relevant exact affine template involving a new target variable \(y\) contains at most \(r\) prime labels.

Choose regular primes

\[
t_1,\dots,t_{r+1}
\]

such that their private places

\[
q_j:=\lambda(t_j)
\]

are outside \(S\) and outside the finite denominator support of all already named target parameters and rational coefficients in the finite template family.

Set

\[
D=q_1\cdots q_{r+1}
\]

and choose

\[
L=\prod_{\ell\in S}\ell^{N_\ell},\qquad N_\ell\ge M_\ell.
\]

Then

\[
y=a+\frac{L}{D}
\]

lies in \(a+H_{\mathbf M}\).

For every \(j\),

\[
v_{q_j}(y)<0.
\]

Now let

\[
z=\alpha+\sum_{i=1}^{r} c_i u_{p_i}
\]

be any forbidden affine value from a relevant scheme. Since at most \(r\) prime labels occur, one of \(t_1,\dots,t_{r+1}\), say \(t_k\), is absent from the tuple \((p_i)\). By the private-place property and the choice of \(q_k\),

\[
v_{q_k}(z)\ge0,
\]

while

\[
v_{q_k}(y)<0.
\]

Hence \(y\ne z\). This avoids all unwanted exact affine incidences simultaneously.

---

## 10. Target-witness transport

Fix a mixed first-order formula \(\Phi\). Close its finite target template family under the linear substitutions and consequences needed by Theorem 5.1 and by compatibility of simultaneous pinning equations.

Choose a depth vector

\[
\mathbf K_\Phi=(K_{\Phi,\ell})_{\ell\in S}
\]

large enough for all fixed-depth templates in this closure.

For a regular prime define the multi-place color

\[
c_{\mathbf K_\Phi}(p)=\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

By (H1), the number of such colors is finite:

\[
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

Let \(\sigma\) be a prime permutation fixing a finite exceptional set, preserving each regular color class and preserving each exact defect class.

### Pinned case

If an exact equation

\[
ay+t=0,\qquad a\ne0,
\]

holds, transport the finitely many prime labels occurring in \(t\) by \(\sigma\) and define \(y'\) by the transported equation. If several pinning equations hold, compatibility is equivalent to exact consequences such as

\[
a_2t_1-a_1t_2=0,
\]

which belong to the finite closure and are preserved by the induction hypothesis.

### Free case

If no exact equation pins \(y\), the transported fixed-depth literals define a non-empty multi-place Boolean cell. By Lemma 6.1 it contains a refinement coset. Apply Fresh-Private-Place Avoidance inside that coset to choose a witness \(y'\) satisfying all local conditions while avoiding every unwanted exact affine incidence.

Thus target witnesses can be transported for the finite fragment relevant to \(\Phi\).

---

## 11. Finite Stationary Locality Theorem

### Theorem 11.1

Let \(\mathcal B_{u,S}\) satisfy (H1)--(H4). Then for every parameter-free first-order formula \(\Phi(\bar p)\) with free source variables restricted to prime atoms, there exist a finite exceptional set \(F_\Phi\) and a finite depth vector \(\mathbf K_\Phi\) such that

\[
\mathcal B_{u,S}\models\Phi(\bar p)
\iff
\mathcal B_{u,S}\models\Phi(\sigma\bar p)
\]

for every prime permutation \(\sigma\) that:

1. fixes \(F_\Phi\) pointwise;
2. preserves every regular multi-place color class \(c_{\mathbf K_\Phi}\);
3. preserves every exact defect class.

### Proof

Induct on the syntax of \(\Phi\).

Source atomic formulas are preserved by the automorphism of \((\mathbb N_{>0},\times)\) induced by permuting prime coordinates and preserving exponents. Bridge atoms are exact target incidences and are part of the controlled template family. Boolean connectives are immediate.

For a source existential witness \(n\), use \(\sigma(n)\). For a target existential witness, use Target-Witness Transport. Universal quantifiers follow by negation. ∎

This is **Formula-Relative Tail Symmetry** for finitely many stationary local windows.

---

## 12. Consequences

### Corollary 12.1. Prime order

The standard strict order on prime atoms is not definable in \(\mathcal B_{u,S}\).

A finite formula-relative partition of an infinite regular tail has a movable class containing two distinct primes. Swapping them preserves the candidate formula but contradicts asymmetry of strict order.

### Corollary 12.2. Prime successor

The standard prime-successor relation is not definable in \(\mathcal B_{u,S}\).

There are infinitely many consecutive prime pairs and only finitely many ordered movable class pairs outside \(F_\Phi\). One ordered class pair therefore occurs for two disjoint consecutive pairs. Swapping the second element of one pair with the second element of the other preserves the hypothetical successor formula while destroying actual succession.

### Corollary 12.3. Finite Grid-Isolation Rank

For every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

In a sufficiently large purported isolated grid, two rows outside the finite exceptional support lie in the same movable class and can be exchanged while fixing the selected column and marker, contradicting isolation of a unique cell.

---

## 13. Ramanujan application

For

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

and any fixed finite \(S\), all primes \(p\notin S\) are \(S\)-integral. For every good prime \(p\ge5\) with \(\tau(p)\ne0\), take

\[
\lambda(p)=p.
\]

The private-denominator calculation gives

\[
v_p(u_p)<0,
\qquad
q\ne p\Longrightarrow v_p(u_q)\ge0.
\]

If \(\tau(p)=0\), then

\[
u_p=-1,
\]

so all zero primes form one exact defect class. Primes in \(S\) and finitely many small primes are absorbed into the exceptional set.

Hence the theorem applies to the Ramanujan bridge for every finite stationary atlas \(S\).

---

## 14. Infinite named stationary atlas

Suppose the language contains a distinct predicate \(B_\ell\) for every rational prime \(\ell\). Every ordinary first-order formula uses only finitely many of these symbols. Therefore, under the corresponding local-integrality hypothesis, Theorem 11.1 applies formula-by-formula to the finite subatlas actually mentioned by the formula.

Thus an infinite **named** stationary atlas does not by itself create a phase transition.

---

## 15. The next boundary: uniformly indexed locality

A genuinely stronger structure appears when the place itself becomes a first-order variable through a relation

\[
\mathsf B(\ell,x)\iff v_\ell(x)\ge0.
\]

Then one formula may quantify over unboundedly many places. For example, with a suitable place sort,

\[
\forall \ell\,(\operatorname{Prime}(\ell)\to\mathsf B(\ell,x))
\]

expresses global integrality of a rational number.

This is the natural next rightward experiment. The present theorem makes no claim about the definability, GIR, or arithmetic strength of that uniformly indexed atlas.

---

## 16. Claim discipline

The theorem does not claim:

* decidability of the complete theory;
* NIP, stability, or simplicity in the classical model-theoretic sense;
* non-interpretability of full arithmetic by every possible interpretation;
* a universal numerical bound on GIR independent of the isolator formula;
* historical priority for the general model-theoretic mechanisms.

The proved content is formula-relative compression for finite stationary local windows under the Private-Place Bridge hypotheses.
