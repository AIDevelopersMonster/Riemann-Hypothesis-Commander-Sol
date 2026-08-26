# Finite Stationary Locality for Private-Place Bridges

**Date:** 2026-08-26  
**Status:** theorem-ready proof checkpoint after final line-by-line audit

## 1. Structure

Fix a non-empty finite set of rational primes

\[
S=\{\ell_1,\dots,\ell_s\}.
\]

For \(\ell\in S\), put

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

We study

\[
\mathcal B_{u,S}=\Bigl((\mathbb N_{>0},\times),(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U\Bigr),
\]

with functional prime-only bridge

\[
U(n,x)\iff \operatorname{Prime}(n)\land x=u_n.
\]

After deleting a finite exceptional set, primes split into an infinite regular set \(R\) and finitely many exact defect classes \(D_j\) with fixed rational labels \(\delta_j\).

Assume:

### H1. S-integrality

\[
\forall p\in R\ \forall\ell\in S\qquad v_\ell(u_p)\ge0.
\]

### H2. Injective private place

There is an injective map

\[
\lambda:R\to\mathbb P\setminus S
\]

such that

\[
v_{\lambda(p)}(u_p)<0,
\]

and for distinct \(p,q\in R\),

\[
v_{\lambda(p)}(u_q)\ge0.
\]

### H3. Defect integrality

After a further finite exclusion,

\[
v_{\lambda(p)}(\delta_j)\ge0
\]

for every regular \(p\) and defect label \(\delta_j\).

These assumptions define a **Private-Place Bridge over \(S\)**.

---

## 2. Fixed-depth predicates

For fixed \(m\in\mathbb Z\), define

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

For \(m>0\),

\[
B_{\ell,m}(x)\iff \exists y\,(\ell^m y=x\land B_\ell(y)),
\]

and

\[
B_{\ell,-m}(x)\iff B_\ell(\ell^m x).
\]

Because \((\mathbb Q,+)\) is uniquely divisible, fixed rational scalar maps are definable by linear equations.

---

## 3. Local Coverage Lemma

### Lemma 3.1

Fix \(\ell\). Let

\[
P=a+B_{\ell,m}
\]

and let \(C_i=b_i+B_{\ell,n_i}\) be finitely many forbidden cosets. Then

\[
P\setminus\bigcup_iC_i\ne\varnothing
\]

is equivalent to a finite Boolean combination of fixed-depth relations among the centers.

### Proof

Two \(\ell\)-adic balls are nested or disjoint. Discard all forbidden balls disjoint from \(P\). If one contains \(P\), the surviving set is empty. Otherwise each remaining forbidden ball is a proper subball, so \(n_i>m\).

If none remains, the surviving set is non-empty. Otherwise put

\[
N=\max_i n_i
\]

over the proper surviving subballs. Refining to depth \(N\), coverage is decided in

\[
B_{\ell,m}/B_{\ell,N},
\qquad
|B_{\ell,m}/B_{\ell,N}|=\ell^{N-m}.
\]

The finite incidence pattern is determined by relations

\[
a-b_i\in B_{\ell,k},
\qquad
b_i-b_j\in B_{\ell,k}
\]

at finitely many fixed depths. ∎

If no positive base coset is present at \(\ell\), finitely many forbidden balls cannot cover \(\mathbb Q\): choose a rational element of sufficiently negative \(\ell\)-valuation.

---

## 4. Multi-Place Target Normal Form

### Theorem 4.1

Every first-order formula in

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in S})
\]

is equivalent to a Boolean combination of

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in B_{\ell,m},
\qquad \ell\in S,\quad m\in\mathbb Z,
\]

with finitely many fixed depths for each fixed formula.

### Proof

After DNF, eliminate one existential target variable \(y\) from a conjunction of literals.

If an exact equation

\[
ay+t(\bar x)=0,
\qquad a\ne0,
\]

occurs, it pins \(y\) uniquely and is eliminated by substitution. Equations with zero \(y\)-coefficient remain conditions on \(\bar x\).

Assume no exact equation pins \(y\). At each place, positive local conditions become coset conditions \(y\in a+B_{\ell,m}\). Compatible positive balls reduce to one deepest base ball; negative balls are handled by Lemma 3.1. Thus every place yields either inconsistency or a non-empty open subset \(U_\ell\subseteq\mathbb Q_\ell\).

For finite \(S\), weak approximation gives a rational \(y\) lying in all non-empty \(U_\ell\) simultaneously. Equivalently, after clearing denominators, one may use finite CRT.

Finitely many exact inequalities remove finitely many points from an infinite local cell and therefore do not destroy non-emptiness. Projection remains in the stated Boolean algebra. Iteration eliminates all target quantifiers. ∎

---

## 5. Generic Multi-Place Cell

### Lemma 5.1

Every non-empty one-variable Boolean cell defined by finitely many fixed-depth local literals and finitely many exact inequalities contains

\[
a+H_{\mathbf M},
\qquad
H_{\mathbf M}=\bigcap_{\ell\in S}B_{\ell,M_\ell}
\]

for some rational \(a\) and finite depth vector \(\mathbf M\).

### Proof

Choose \(a\) in the cell. Choose each \(M_\ell\) deeper than every local boundary in the finite description. Then all local truth values are preserved under perturbation by \(H_{\mathbf M}\).

If exact exclusions \(y\ne c_j\) occur, fix one place \(\ell_0\in S\) and increase \(M_{\ell_0}\) so that

\[
M_{\ell_0}>\max_j v_{\ell_0}(a-c_j).
\]

Then no excluded point lies in the refinement coset. ∎

---

## 6. Exact Linear Separation

### Lemma 6.1

Fix a homogeneous coefficient scheme

\[
\sum_i c_i u_{p_i}=0.
\]

After clearing denominators and deleting a finite coefficient-dependent set, the relation can hold on the regular tail only if the aggregate coefficient of every regular-prime equality block is zero, together with the fixed exact relations among defect labels.

### Proof

Group equal regular primes. For a block represented by \(p\) with non-zero integer aggregate coefficient \(d\), exclude the finitely many regular primes for which \(\lambda(p)\mid d\). At every remaining such \(p\),

\[
v_{\lambda(p)}(d u_p)<0,
\]

while all other regular labels and all defect labels are \(\lambda(p)\)-integral. The sum cannot vanish. ∎

Regular labels are therefore injective on the tail.

---

## 7. Reduced Affine-Fiber Lemma

Consider

\[
\sum_{i=1}^r c_i u_{p_i}=t
\]

and fix an equality pattern \(\pi\). For a block \(C\in\pi\), let

\[
d_C=\sum_{i\in C}c_i.
\]

Blocks with \(d_C=0\) are structurally free.

### Lemma 7.1

After deleting a finite coefficient-dependent set, the assignments to blocks with \(d_C\ne0\) are uniformly bounded in terms of the coefficient scheme.

### Proof

Subtract two reduced solutions. By Lemma 6.1 every regular prime in the second solution must already occur in the first; otherwise its private place produces an uncancelled negative valuation. If there are \(m\) non-zero blocks, a crude bound \(m^m\) suffices. ∎

Thus affine traces are finite unions of **bounded-anchor cylinders**, not necessarily finite sets of complete tuples.

---

## 8. Coefficient-Adjusted Colors

Consider a local template

\[
L=\alpha+\sum_i a_i u_{p_i}
\]

and a test

\[
L\in B_{\ell,m}.
\]

If labels are replaced by labels in the same \(B_{\ell,K}\)-cosets, then

\[
v_\ell(u_{p_i}-u_{p_i'})\ge K
\]

and

\[
v_\ell\left(\sum_i a_i(u_{p_i}-u_{p_i'})\right)
\ge
\min_i(v_\ell(a_i)+K).
\]

Hence the truth of the local test is preserved whenever

\[
K\ge\max_i\{m-v_\ell(a_i)\}.
\]

For a fixed formula \(\Phi\), close the finite target-template family under the substitutions and compatibility consequences used below and choose \(K_{\Phi,\ell}\ge0\) satisfying every resulting bound.

Define the regular prime color

\[
c_{\mathbf K_\Phi}(p)
=
\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

By H1, the number of colors is finite and bounded by

\[
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

---

## 9. Fresh-Private-Place Avoidance

### Lemma 9.1

Let a non-empty finite-depth cell contain \(a+H_{\mathbf M}\). Suppose every relevant forbidden affine scheme for a new target variable uses at most \(r\) prime labels. Then there is a rational witness in the refinement coset avoiding all values of all those schemes.

### Proof

Form the finite rational support consisting of:

- \(S\);
- denominators of all fixed rational coefficients;
- denominators of external target parameters;
- denominators of every current target coordinate;
- the denominator of the current center \(a\);
- labels of finitely many exceptional fixed source primes.

Choose regular primes \(t_1,\dots,t_{r+1}\) whose private places

\[
q_j=\lambda(t_j)
\]

avoid this finite support. This is possible because \(R\) is infinite and \(\lambda\) is injective.

Set

\[
D=q_1\cdots q_{r+1},
\qquad
L=\prod_{\ell\in S}\ell^{N_\ell},
\qquad
N_\ell\ge M_\ell,
\]

and

\[
y=a+\frac LD.
\]

Then \(y\in a+H_{\mathbf M}\). Since \(a\) is integral at every \(q_j\),

\[
v_{q_j}(y)=-1.
\]

Any forbidden affine value

\[
z=\alpha+\sum_{i=1}^r c_i u_{p_i}
\]

uses at most \(r\) prime labels. Hence one \(t_k\) is absent. At \(q_k\), every term in \(z\) is integral, so \(v_{q_k}(z)\ge0\), while \(v_{q_k}(y)=-1\). Therefore \(y\ne z\). ∎

---

## 10. Target-Witness Transport

Fix a formula \(\Phi\) and its finite template closure. Let \(\sigma\) fix a finite exceptional prime set, preserve every regular \(c_{\mathbf K_\Phi}\)-class, and preserve every defect class setwise.

### Pinned case

If

\[
ay+t=0,
\qquad a\ne0,
\]

holds, transport the source primes occurring in \(t\) by \(\sigma\) and solve the transported equation for \(y'\). Multiple pinning equations remain compatible because conditions such as

\[
a_2t_1-a_1t_2=0
\]

are \(y\)-free exact templates included in the finite closure.

### Free case

If no exact instance pins \(y\), coefficient-adjusted color preservation gives the same finite local pattern after transport. The transported local literals form a non-empty cell; Lemma 5.1 gives a refinement coset; Lemma 9.1 chooses a witness there avoiding every unwanted exact affine incidence.

The same arguments work with \(\sigma^{-1}\).

---

## 11. Finite-Fragment Back-and-Forth

For the finite syntactic closure generated by \(\Phi\), relate two states when:

1. the source tuples are related by the multiplicative automorphism induced by \(\sigma\);
2. all exact target templates in the closure have the same truth value;
3. all fixed-depth target templates in the closure have the same truth value;
4. all bridge incidences in the closure agree.

Source witnesses are transported by \(n\mapsto\sigma(n)\) and back by \(\sigma^{-1}\). Target witnesses are transported by Section 10. Atomic formulas and Boolean connectives are preserved. Standard induction on subformulas of \(\Phi\) therefore preserves every subformula.

No global automorphism of the complete two-sorted structure is asserted.

---

## 12. Finite Stationary Locality Theorem

### Theorem 12.1

Let \(S\ne\varnothing\) be finite and let \(\mathcal B_{u,S}\) satisfy H1-H3 and the functional prime-only bridge condition. For every parameter-free first-order formula

\[
\Phi(\bar p)
\]

whose free source variables are restricted to prime atoms, there exist a finite exceptional set \(F_\Phi\) and a finite depth vector

\[
\mathbf K_\Phi=(K_{\Phi,\ell})_{\ell\in S}
\]

such that

\[
\mathcal B_{u,S}\models\Phi(\bar p)
\iff
\mathcal B_{u,S}\models\Phi(\sigma\bar p)
\]

for every prime permutation \(\sigma\) that fixes \(F_\Phi\) pointwise, preserves all regular \(c_{\mathbf K_\Phi}\)-classes, and preserves every defect class setwise.

### Proof

Choose the finite template closure of \(\Phi\), the coefficient-adjusted depths of Section 8, and enlarge the finite exceptional set by the finite exclusions required by Sections 6-10. The finite-fragment back-and-forth of Section 11 then preserves every subformula of \(\Phi\). ∎

This is **Formula-Relative Tail Symmetry**.

---

## 13. Consequences

### Corollary 13.1. Prime order

The ordinary strict order on prime atoms is not definable.

A formula-relative partition has finitely many movable classes on an infinite regular tail. Two distinct regular primes in one class can be swapped, contradicting asymmetry of strict order.

### Corollary 13.2. Prime successor

The ordinary prime-successor relation is not definable.

Outside any finite set there are infinitely many consecutive prime pairs but only finitely many ordered movable-class pairs. One ordered pair of classes occurs for two disjoint consecutive pairs \((p,q)\), \((p',q')\). Swapping \(q\) and \(q'\) while fixing \(p\) preserves the hypothetical formula and destroys actual succession.

### Corollary 13.3. Finite GIR

For every fixed isolator \(I(p,q;r)\),

\[
\operatorname{GIR}(I)<\infty.
\]

In a sufficiently large alleged grid, some movable class contains at least four row primes. After fixing one column and one marker, at most two of those rows can coincide with the fixed objects. Swap two other rows in the class. The same marker would then isolate two cells in the fixed column, contradiction.

No universal formula-independent GIR bound is claimed.

---

## 14. Ramanujan Bridge

Let

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

For finite \(S\), every \(p\notin S\) is \(S\)-integral.

For a good prime \(p\ge5\) with \(\tau(p)\ne0\), put \(a=v_p(\tau(p))\). Deligne gives

\[
|\tau(p)|\le2p^{11/2},
\]

hence \(a\le5\). Thus

\[
v_p(u_p)=2a-11<0,
\]

whereas for \(q\ne p\),

\[
v_p(u_q)\ge0.
\]

Hence \(\lambda(p)=p\) on the good-prime tail.

If \(\tau(p)=0\), then \(u_p=-1\), so all zero primes form one exact defect class.

The regular reservoir is infinite without using a zero-density theorem. Ramanujan's congruence

\[
\tau(p)\equiv1+p^{11}\pmod{691}
\]

implies

\[
p\equiv1\pmod{691}
\quad\Longrightarrow\quad
\tau(p)\equiv2\pmod{691}\ne0.
\]

Dirichlet's theorem gives infinitely many primes in this progression.

Therefore Theorem 12.1 applies to every finite non-empty Ramanujan stationary atlas.

---

## 15. Infinite Named Atlas

If every \(B_\ell\) is separately named in an infinite language, each ordinary first-order formula still mentions only finitely many place symbols. For the Ramanujan bridge, apply Theorem 12.1 to that finite syntactic support. Thus the infinite named atlas remains formula-by-formula compressed.

This is compatible with pointwise definability of a good prime by its own named predicate:

\[
q=p
\iff
\operatorname{Prime}(q)\land
\exists x\bigl(U_\Delta(q,x)\land\neg B_p(x)\bigr).
\]

Hence

\[
\text{pointwise distinguishability}\ne\text{uniform orientation}.
\]

---

## 16. Uniformly Indexed Atlas: Open Boundary

If the language contains a variable place relation

\[
\mathsf B(\ell,x)\iff v_\ell(x)\ge0,
\]

then one formula can aggregate information over unboundedly many places. For rational \(x\),

\[
\forall\ell\,(\operatorname{Prime}(\ell)\to\mathsf B(\ell,x))
\]

defines \(\mathbb Z\subseteq\mathbb Q\).

The finite syntactic-support mechanism no longer applies. No claim is made here about infinite GIR, prime successor, decidability, or interpretation of full arithmetic in this uniformly indexed structure.

---

## 17. Claim Discipline

The theorem does **not** assert:

- decidability of the complete theory;
- NIP, stability, or simplicity;
- global non-interpretability of arithmetic;
- a global automorphism theorem for the full two-sorted structure;
- a universal numerical GIR bound independent of the isolator;
- infinite GIR or prime-successor definability for the uniformly indexed atlas;
- historical priority for the general model-theoretic mechanisms.

The proved content is formula-relative compression for finite stationary local windows under the stated Private-Place Bridge hypotheses, together with the consequences above.
