# Reflections on Stationary Locality with Commander Sol
## Private-Place Bridges, Finite Multi-adic Windows, and Formula-Relative Compression

**Alex Malachevsky**  
ORCID: 0009-0008-6009-3196  
Version 1.0 - 2026

## Abstract

We study a two-sorted expansion of Skolem arithmetic in which prime atoms are linked to rational labels and the additive target is equipped with finitely many fixed p-adic integrality predicates. The motivating labels are

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

where \(\tau\) is Ramanujan's tau function.

The main result is the **Finite Stationary Locality Theorem**. For a finite set of rational primes \(S\), consider

\[
\mathcal B_{u,S}=
\Bigl((\mathbb N_{>0},\times),
      (\mathbb Q,+,0,(B_\ell)_{\ell\in S}),U\Bigr),
\qquad
B_\ell(x)\iff v_\ell(x)\ge0.
\]

Assume that, outside a finite exceptional set, regular prime labels are integral at every stationary place \(\ell\in S\), and every regular prime possesses an injectively assigned private denominator place \(\lambda(p)\notin S\) that is negative on \(u_p\) and non-negative on all other regular labels. Finitely many exact common-label defect classes are allowed.

We prove that every fixed first-order formula admits a finite multi-place depth vector and a finite exceptional prime set such that, on the prime tail, truth is invariant under all prime permutations preserving the resulting finite local colors and exact defect classes. The proof has four ingredients: a direct finite-depth normal form for the target additive structure, private-place exact linear separation, fresh-private-place avoidance for non-pinned target witnesses, and a finite-fragment back-and-forth argument for mixed quantifiers.

Consequently, the ordinary order and ordinary successor relation on prime atoms are not definable in \(\mathcal B_{u,S}\), and every fixed grid-isolator has finite Grid-Isolation Rank. For the Ramanujan labels the hypotheses hold for every finite stationary atlas. Moreover, an infinite family of separately named predicates \((B_\ell)_{\ell\in\mathbb P}\) is still formula-by-formula finite, because an ordinary first-order formula mentions only finitely many place names. The next boundary is therefore a uniformly indexed relation \(\mathsf B(\ell,x)\), where the place itself becomes a first-order variable.

---

## 1. The question behind the theorem

The multiplicative structure

\[
(\mathbb N_{>0},\times)
\]

has a large symmetry on its prime atoms. Every permutation of the primes extends uniquely to an automorphism by preserving the exponent of each prime in the factorization of every positive integer. Standard prime order and prime successor are therefore invisible to pure multiplication.

A natural way to break this symmetry is to attach to each prime atom \(p\) a rational label \(u_p\) and to allow an additive target sort to inspect those labels. In the Ramanujan example,

\[
\Delta(q)=q\prod_{n\ge1}(1-q^n)^{24}
        =\sum_{n\ge1}\tau(n)q^n
\]

and

\[
u_p=\frac{\tau(p)^2}{p^{11}}-1.
\]

A single fixed p-adic ball can distinguish some labels. The natural next question is whether several independent local windows can cooperate to produce a two-dimensional address system. With two places, local subgroups are no longer a single chain. Chinese-remainder compatibility also becomes available. It is therefore reasonable to ask whether one place could encode rows, another columns, and the additive group the intersections.

The answer proved here is negative under the Private-Place hypotheses. A finite family of stationary local windows enlarges the finite color palette seen by a fixed formula, but it does not make the local depth into a uniformly movable coordinate.

This is the phenomenon we call **stationary locality**.

---

## 2. Source, target, and bridge

Fix a non-empty finite set of rational primes

\[
S=\{\ell_1,\dots,\ell_s\}.
\]

The source sort is

\[
\mathcal N=(\mathbb N_{>0},\times).
\]

Its prime atoms are first-order definable as the non-unit irreducible elements.

The target sort is

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\]

where

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

The bridge is the graph of the label map on prime atoms:

\[
\boxed{
U(n,x)\iff \operatorname{Prime}(n)\land x=u_n.
}
\]

In particular, a composite source element never carries a bridge label. The target sees \(u_p\), not the exponent of \(p\) in \(p^k\). This is the **prime-only** or **multiplicity-blind** bridge condition.

We write

\[
\mathcal B_{u,S}=\bigl(\mathcal N,\mathcal A_S,U\bigr).
\]

---

## 3. Private-Place Bridge hypotheses

After deleting a finite exceptional set of source primes, assume that the remaining primes split into an infinite set \(R\) of regular primes and finitely many exact defect classes

\[
D_1,\dots,D_t.
\]

All primes in \(D_j\) have one fixed rational label \(\delta_j\).

For regular primes assume:

### H1. Stationary-place integrality

For every \(p\in R\) and every \(\ell\in S\),

\[
v_\ell(u_p)\ge0.
\]

### H2. Injective private place

There is an injective map

\[
\lambda:R\to\mathbb P\setminus S
\]

such that

\[
v_{\lambda(p)}(u_p)<0
\]

and, for distinct \(p,q\in R\),

\[
v_{\lambda(p)}(u_q)\ge0.
\]

### H3. Defect integrality at private places

After enlarging the finite exceptional set if needed,

\[
v_{\lambda(p)}(\delta_j)\ge0
\]

for every regular \(p\) and every defect label \(\delta_j\).

This last assumption is automatic after finitely many exclusions once H2 holds, because the finitely many rational defect labels have finite total denominator support and \(\lambda\) is injective.

A bridge satisfying H1-H3 together with the prime-only functional bridge condition of Section 2 will be called a **Private-Place Bridge over \(S\)**.

---

## 4. Fixed-depth local predicates

For every fixed integer \(m\), let

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

These predicates are definable from \(B_\ell\). If \(m>0\),

\[
B_{\ell,m}(x)
\iff
\exists y\,(\ell^m y=x\land B_\ell(y)),
\]

whereas

\[
B_{\ell,-m}(x)
\iff
B_\ell(\ell^m x).
\]

Only fixed depths are introduced. No predicate with a variable depth parameter is available.

Because \((\mathbb Q,+)\) is uniquely divisible, multiplication by a fixed rational scalar is definable by a linear equation. Accordingly, we use rational linear forms

\[
L(\bar x)=a_1x_1+\cdots+a_nx_n+b.
\]

The two target atomic shapes relevant below are

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in B_{\ell,m}.
\]

---

## 5. Local coverage at one place

We first isolate the only finite combinatorics needed for negative ball conditions.

### Lemma 5.1. Local Coverage Lemma

Fix one place \(\ell\). Let

\[
P=a+B_{\ell,m}
\]

be a positive base coset and let

\[
C_i=b_i+B_{\ell,n_i}
\]

be finitely many forbidden cosets. Then the condition

\[
P\setminus\bigcup_iC_i\ne\varnothing
\]

is expressible by a finite Boolean combination of fixed-depth relations among the centers.

### Proof

Two \(\ell\)-adic balls are either disjoint or one contains the other. Discard every \(C_i\) disjoint from \(P\). If one of the remaining \(C_i\) contains \(P\), the surviving set is empty. Otherwise every remaining \(C_i\) is a proper subball of \(P\), hence \(n_i>m\).

If no proper forbidden subball remains, the surviving set is non-empty. Otherwise put

\[
N=\max_i n_i,
\]

where the maximum is taken only over the proper surviving subballs. Refining all of them to depth \(N\), coverage is decided in the finite quotient

\[
B_{\ell,m}/B_{\ell,N},
\qquad
|B_{\ell,m}/B_{\ell,N}|=\ell^{N-m}.
\]

The incidence pattern of the finitely many subcosets is determined by fixed-depth relations

\[
a-b_i\in B_{\ell,k},
\qquad
b_i-b_j\in B_{\ell,k},
\]

for finitely many \(k\). Therefore non-coverage is a finite Boolean combination of such relations. ∎

If no positive base coset is present at \(\ell\), finitely many forbidden balls cannot cover \(\mathbb Q\): choose \(y\in\mathbb Q\) with \(v_\ell(y)\) smaller than all relevant depths and all valuations of the finitely many centers. Then

\[
v_\ell(y-b_i)=v_\ell(y)
\]

for every \(i\), so \(y\) lies in none of the forbidden balls.

The finite quotient in this argument is the **refinement quotient** \(B_{\ell,m}/B_{\ell,N}\). No finiteness of \(\mathbb Q/B_{\ell,m}\) is asserted.

---

## 6. Multi-Place Finite-Depth Normal Form

### Theorem 6.1

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
\qquad \ell\in S,\quad m\in\mathbb Z,
\]

with only finitely many fixed depths occurring for any fixed formula.

### Proof

After passing to disjunctive normal form, it suffices to eliminate one existential target variable \(y\) from one conjunction of literals.

If an exact equation

\[
ay+t(\bar x)=0,
\qquad a\ne0,
\]

occurs, it uniquely determines

\[
y=-a^{-1}t(\bar x),
\]

and elimination is by substitution. Exact equations with zero \(y\)-coefficient simply remain conditions on \(\bar x\).

Assume now that no exact equation pins \(y\). Every positive local literal involving \(y\) may be rewritten as

\[
y\in a+B_{\ell,m}.
\]

For each fixed \(\ell\), positive balls that intersect are nested, so their conjunction is either inconsistent or equivalent to one deepest positive base ball. Negative balls at that place are treated by Lemma 5.1. Thus at every \(\ell\in S\) we obtain either inconsistency or a non-empty open local set

\[
U_\ell\subseteq\mathbb Q_\ell
\]

defined by finitely many fixed-depth conditions.

If every \(U_\ell\) is non-empty, weak approximation for \(\mathbb Q\) gives a rational number \(y\) satisfying all local conditions simultaneously. Equivalently, after clearing denominators, the same assertion follows from a finite Chinese-remainder construction.

Finally, finitely many exact inequalities

\[
y\ne c_1,\dots,y\ne c_r
\]

remove only finitely many points. A non-empty multi-place local cell contains an infinite refinement coset, so finite point deletion cannot destroy it.

The projection is therefore a Boolean combination of exact linear equations and fixed-depth local conditions. Repeating the argument eliminates all target quantifiers. ∎

The proof is direct. Classical pp-elimination for modules and abelian structures supplies useful background, but no general elimination theorem is needed as a black box here.

---

## 7. Refinement of a non-empty target cell

### Lemma 7.1. Generic Multi-Place Cell

Let \(C\subseteq\mathbb Q\) be a non-empty cell described by finitely many fixed-depth local literals together with finitely many exact inequalities. Then there are \(a\in C\) and a finite depth vector

\[
\mathbf M=(M_\ell)_{\ell\in S}
\]

such that

\[
a+H_{\mathbf M}\subseteq C,
\qquad
H_{\mathbf M}:=\bigcap_{\ell\in S}B_{\ell,M_\ell}.
\]

### Proof

Choose \(a\in C\). For each place \(\ell\), choose \(M_\ell\) deeper than every local boundary occurring in the description of \(C\). Then perturbations by \(H_{\mathbf M}\) preserve all local memberships and non-memberships.

If exact exclusions \(a\ne c_j\) occur, choose one place \(\ell_0\in S\) and increase \(M_{\ell_0}\) further so that

\[
M_{\ell_0}>\max_j v_{\ell_0}(a-c_j).
\]

Then no excluded point belongs to the refinement coset. ∎

---

## 8. Exact linear separation by private places

Fix a homogeneous coefficient scheme

\[
\sum_{i=1}^r c_i u_{p_i}=0.
\]

Clear denominators in the fixed rational coefficients, so the \(c_i\) may be taken as integers. Group equal regular primes. Let \(p\) represent one equality block and let \(d\ne0\) be its aggregate coefficient.

Outside the finite set of regular primes for which \(\lambda(p)\mid d\),

\[
v_{\lambda(p)}(d u_p)<0.
\]

Every other regular label is \(\lambda(p)\)-integral by H2, and every defect label is \(\lambda(p)\)-integral by H3. Hence the sum cannot vanish.

We have proved:

### Lemma 8.1. Exact Linear Separation

For every fixed homogeneous coefficient scheme there is a finite coefficient-dependent exceptional set such that, on the remaining regular tail, the relation

\[
\sum_i c_i u_{p_i}=0
\]

can hold only when the aggregate coefficient of every regular-prime equality block is zero, together with whatever fixed exact relations occur among the finitely many defect labels.

In particular, regular labels are injective on the tail.

---

## 9. Affine equations and bounded-anchor cylinders

Exact affine equations require one further distinction.

A statement of the form “every affine fiber contains only boundedly many prime tuples” is false. For example,

\[
u_{p_1}-u_{p_2}+u_{p_3}=u_q
\]

has the infinite family

\[
(p_1,p_2,p_3)=(r,r,q).
\]

The first two coordinates form a zero-sum equality block and are structurally free.

Fix an equality pattern \(\pi\) on \(p_1,\dots,p_r\). For a block \(C\in\pi\), set

\[
d_C=\sum_{i\in C}c_i.
\]

Blocks with \(d_C=0\) disappear from the reduced equation.

### Lemma 9.1. Reduced Affine-Fiber Lemma

For the blocks with \(d_C\ne0\), the number of regular-prime assignments to a fixed reduced affine equation is uniformly bounded in terms of the coefficient scheme, after a finite coefficient-dependent exclusion.

### Proof

Let \((q_C)\) and \((q'_C)\) be two reduced solutions of the same affine equation. Subtracting them gives a homogeneous relation. If a regular prime occurred in the second solution but not in the first, its private place would see one non-zero aggregate negative contribution and only integral contributions from all other terms. This contradicts Lemma 8.1.

Hence every second solution uses only the finitely many regular primes appearing in the first. If there are \(m\) non-zero blocks, a crude bound \(m^m\) on reassignments suffices. ∎

Thus exact affine traces are finite unions of **bounded-anchor cylinders**: zero-sum blocks remain free, while only non-zero blocks can be anchored to finitely many regular primes.

---

## 10. Coefficient-adjusted local colors

A fixed local formula can contain rational coefficients. The depth used to color the labels must therefore absorb the p-adic orders of those coefficients.

Consider one local template

\[
L=\alpha+\sum_i a_i u_{p_i}
\]

and the test

\[
L\in B_{\ell,m}.
\]

Suppose \(p_i\) and \(p_i'\) have the same color modulo \(B_{\ell,K}\), so that

\[
v_\ell(u_{p_i}-u_{p_i'})\ge K.
\]

Then

\[
v_\ell\left(\sum_i a_i(u_{p_i}-u_{p_i'})\right)
\ge
\min_i\bigl(v_\ell(a_i)+K\bigr).
\]

Therefore the truth of the test is unchanged whenever

\[
K\ge \max_i\{m-v_\ell(a_i)\}.
\]

For a fixed formula \(\Phi\), close the finite family of target templates under the linear substitutions and compatibility consequences used below. Choose

\[
K_{\Phi,\ell}\ge0
\]

larger than every bound of the preceding form arising in that finite closure.

For a regular prime define

\[
c_{\mathbf K_\Phi}(p)
=
\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

By H1, only finitely many colors occur, with the simple bound

\[
\#\operatorname{Colors}(\Phi)
\le
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

This is the exact sense in which a fixed formula sees only finite local information.

---

## 11. Fresh-Private-Place Avoidance

We now construct witnesses that stay inside one target cell while avoiding every value from a fixed family of forbidden affine schemes.

### Lemma 11.1

Let a non-empty finite-depth target cell contain

\[
a+H_{\mathbf M}.
\]

Suppose every relevant forbidden affine scheme for a new target variable \(y\) uses at most \(r\) prime labels. Then there is a rational \(y\in a+H_{\mathbf M}\) avoiding all values of all those schemes.

### Proof

The proof is carried out relative to the finite current state of the back-and-forth argument. Form a finite rational support consisting of:

- all stationary places in \(S\);
- denominators of all fixed rational coefficients;
- denominators of all external target parameters;
- denominators of all current target coordinates;
- the denominator of the chosen center \(a\);
- labels of any finitely many exceptional fixed source primes.

Because \(R\) is infinite and \(\lambda\) is injective, choose regular primes

\[
t_1,\dots,t_{r+1}
\]

whose private places

\[
q_j=\lambda(t_j)
\]

avoid this entire finite support.

Set

\[
D=q_1\cdots q_{r+1}
\]

and choose

\[
L=\prod_{\ell\in S}\ell^{N_\ell},
\qquad N_\ell\ge M_\ell.
\]

Define

\[
y=a+\frac{L}{D}.
\]

Since every \(q_j\notin S\), the denominator \(D\) is a unit at all stationary places, and hence

\[
y\in a+H_{\mathbf M}.
\]

At every fresh private place \(q_j\), both \(a\) and \(L\) are integral, while \(D\) contains \(q_j\) to exponent one. Thus

\[
v_{q_j}(y)=-1.
\]

Now take any forbidden affine value

\[
z=\alpha+\sum_{i=1}^r c_i u_{p_i}.
\]

At most \(r\) prime labels occur, so one of \(t_1,\dots,t_{r+1}\), say \(t_k\), is absent. By the choice of \(q_k\) and the private-place property, all terms occurring in \(z\) are \(q_k\)-integral. Hence

\[
v_{q_k}(z)\ge0,
\]

whereas \(v_{q_k}(y)=-1\). Therefore \(y\ne z\). The argument applies simultaneously to every tuple of every fixed scheme. ∎

The counting principle is simply

\[
r+1\text{ fresh private places}>r\text{ prime-label slots}.
\]

---

## 12. Target-witness transport

Fix a first-order formula \(\Phi\) and its finite template closure. Let \(\sigma\) be a permutation of prime atoms that fixes a finite exceptional set, preserves every regular \(c_{\mathbf K_\Phi}\)-color class, and preserves every exact defect class setwise.

There are two cases for a new target witness \(y\).

### 12.1. Pinned case

Suppose an exact equation

\[
ay+t=0,
\qquad a\ne0,
\]

holds. Transport every prime coordinate occurring in \(t\) by \(\sigma\) and define \(y'\) from the transported equation.

If several pinning equations hold, for example

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0,
\]

their compatibility is equivalent to the \(y\)-free exact condition

\[
a_2t_1-a_1t_2=0.
\]

The template closure is chosen to contain all such finite compatibility consequences, so they are preserved at the preceding stage of the argument.

### 12.2. Free case

Suppose no exact instance in the relevant template family pins \(y\). Coefficient-adjusted color preservation ensures that the transported fixed-depth local literals have the same finite local pattern. They therefore form a non-empty target cell. By Lemma 7.1 that cell contains a full refinement coset. Lemma 11.1 then supplies a witness \(y'\) in that coset that avoids all exact affine incidences that must remain false.

Thus target witnesses can be transported in both directions for the finite fragment attached to \(\Phi\).

---

## 13. Finite-fragment back-and-forth

To make the mixed-quantifier step explicit, we do not appeal to an unspecified global automorphism of the two-sorted structure.

For the finite syntactic closure generated by \(\Phi\), relate two finite states when:

1. their source tuples are carried to one another by the multiplicative automorphism induced by \(\sigma\);
2. all exact target templates in the closure agree in truth value;
3. all fixed-depth target templates in the closure agree in truth value;
4. all bridge incidences in the closure agree.

The relation has the following finite-fragment back-and-forth properties.

### Source forth/back

If the first state has a source witness \(n\), use \(\sigma(n)\) in the second state. The inverse step uses \(\sigma^{-1}\). Source atomic formulas are preserved because prime-coordinate permutations are automorphisms of \((\mathbb N_{>0},\times)\).

### Target forth/back

For a target witness, use the pinned/free construction of Section 12. The same construction applied with \(\sigma^{-1}\) gives the reverse direction.

### Atomic and Boolean preservation

Source atomics, target atomics, and bridge atomics belong to the controlled finite closure. Boolean connectives preserve equivalence immediately.

Standard induction on subformulas of \(\Phi\) now gives preservation of every subformula. This is a finite-fragment argument: neither the coloring nor the exceptional set is claimed to work uniformly for all formulas at once.

---

## 14. Finite Stationary Locality Theorem

### Theorem 14.1

Let \(S\ne\varnothing\) be finite and let \(\mathcal B_{u,S}\) be a Private-Place Bridge structure satisfying the hypotheses of Sections 2-3. Then for every parameter-free first-order formula

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

for every prime permutation \(\sigma\) that

1. fixes \(F_\Phi\) pointwise;
2. preserves every regular multi-place color class \(c_{\mathbf K_\Phi}\);
3. preserves every exact defect class setwise.

### Proof

Construct the finite template closure of \(\Phi\), choose coefficient-adjusted depths as in Section 10, and enlarge the finite exceptional set by all coefficient, defect, and finite-support exclusions required in Sections 8-12. The finite-fragment back-and-forth of Section 13 then preserves every subformula of \(\Phi\), and in particular \(\Phi\) itself. ∎

We call the conclusion **Formula-Relative Tail Symmetry**.

The theorem is deliberately formula-relative. It is not a global automorphism theorem for \(\mathcal B_{u,S}\).

---

## 15. Consequences for order, successor, and GIR

### Corollary 15.1. Prime order is not definable

The ordinary strict order on prime atoms is not definable in \(\mathcal B_{u,S}\).

### Proof

A hypothetical defining formula has only finitely many movable color/defect classes outside a finite exceptional set. Since the regular tail is infinite, one movable class contains two distinct regular primes \(p\ne q\). Swapping them is admissible, while a strict linear order is not invariant under that swap. ∎

### Corollary 15.2. Prime successor is not definable

The ordinary prime-successor relation is not definable in \(\mathcal B_{u,S}\).

### Proof

There are infinitely many consecutive ordinary prime pairs outside any finite set. There are only finitely many ordered formula-relative class pairs. Hence one ordered class pair occurs for infinitely many consecutive prime pairs, and in particular for two disjoint pairs

\[
(p,q),\qquad(p',q').
\]

The second elements \(q,q'\) are in the same movable class. Swapping \(q\) and \(q'\) while fixing \(p\) preserves the hypothetical successor formula but destroys ordinary succession. ∎

No density theorem for defect primes is used in this argument.

### Corollary 15.3. Finite Grid-Isolation Rank

For every fixed isolator formula \(I(p,q;r)\),

\[
\operatorname{GIR}(I)<\infty.
\]

### Proof

Apply Theorem 14.1 to \(I\). Outside the finite exceptional set there are only finitely many movable classes. In a sufficiently large alleged isolated grid, some movable class contains at least four row primes. Fix one column and one cell marker. At most two of those four row primes can coincide with the fixed column or the fixed marker. Choose two other rows in the same movable class and swap them while fixing the column and marker. Formula-relative invariance would then make the same marker isolate two cells in the same column, contradiction. ∎

Grid-Isolation Rank is a programme invariant for this specific cell-isolation mechanism. Finite GIR is not identified here with stability, NIP, or any other standard global classification property.

---

## 16. Ramanujan specialization

We now verify the abstract hypotheses for

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Fix a finite non-empty stationary atlas \(S\).

### 16.1. Integrality at stationary places

If \(p\notin S\) and \(\ell\in S\), then \(p^{11}\) is an \(\ell\)-adic unit. Hence

\[
v_\ell(u_p)\ge0.
\]

### 16.2. Private denominator for good primes

Call \(p\ge5\) good when \(\tau(p)\ne0\), and write

\[
a=v_p(\tau(p)).
\]

Deligne's bound

\[
|\tau(p)|\le2p^{11/2}
\]

implies \(a\le5\): if \(a\ge6\), then \(p^6\le|\tau(p)|\le2p^{11/2}\), hence \(\sqrt p\le2\), impossible for \(p\ge5\).

Since \(2a<11\),

\[
v_p(\tau(p)^2-p^{11})=2a,
\]

and therefore

\[
v_p(u_p)=2a-11<0.
\]

For \(q\ne p\), the denominator of \(u_q\) is a power of \(q\), so

\[
v_p(u_q)\ge0.
\]

Thus for good primes outside \(S\) we may take

\[
\lambda(p)=p.
\]

### 16.3. Zero primes as one exact defect class

If \(\tau(p)=0\), then

\[
u_p=-1.
\]

Hence all such primes, if any exist, form one exact common-label defect class.

### 16.4. An infinite good-prime reservoir

The abstract theorem requires infinitely many regular primes. This can be obtained without a density theorem for the possible zeros of \(\tau(p)\).

Ramanujan's congruence gives

\[
\tau(p)\equiv1+p^{11}\pmod{691}
\]

for prime \(p\). If

\[
p\equiv1\pmod{691},
\]

then

\[
\tau(p)\equiv2\pmod{691},
\]

so \(\tau(p)\ne0\). Dirichlet's theorem gives infinitely many primes in the progression \(1\pmod{691}\). Therefore the good-prime reservoir is infinite.

We conclude:

### Corollary 16.1

For every finite non-empty set of rational primes \(S\), the Ramanujan bridge structure

\[
\mathcal B_{\Delta,S}
=
\Bigl((\mathbb N_{>0},\times),
      (\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
      U_\Delta\Bigr)
\]

satisfies Formula-Relative Tail Symmetry. The ordinary prime order and prime-successor relation are not definable in it, and every fixed isolator has finite GIR.

---

## 17. The infinite named stationary atlas

Consider now the target language

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}),
\]

with one separately named predicate for every rational prime.

Although the language is infinite, each ordinary first-order formula is a finite string. Therefore every fixed formula \(\Phi\) mentions only finitely many place names. Let this finite support be \(S_\Phi\).

For the Ramanujan labels, primes outside \(S_\Phi\) are \(S_\Phi\)-integral, and the finite theorem applies to the formula. Thus:

### Corollary 17.1. Infinite Named Stationary Atlas

The Ramanujan structure with every \(B_\ell\) separately named remains formula-by-formula compressed. Each fixed formula has its own finite exceptional set and finite local color partition on the prime tail.

This is compatible with a striking pointwise phenomenon. If \(p\) is good, then its own named predicate \(B_p\) isolates \(p\) among prime labels:

\[
q=p
\iff
\operatorname{Prime}(q)\land
\exists x\bigl(U_\Delta(q,x)\land\neg B_p(x)\bigr).
\]

Thus individual primes can be distinguished by different formulas without any one formula providing a uniform standard orientation of all primes.

In programme terminology,

\[
\boxed{
\text{pointwise distinguishability}\ne\text{uniform orientation}.
}
\]

---

## 18. The next boundary: uniformly indexed locality

The preceding corollary shows that the passage from finitely many to infinitely many **named** stationary predicates is not itself a first-order phase transition.

A genuinely stronger language appears when the place becomes a variable of the structure through one relation

\[
\mathsf B(\ell,x)
\iff
v_\ell(x)\ge0.
\]

Then a single formula can quantify over unboundedly many places. For rational \(x\), the formula

\[
\forall\ell\,
\bigl(\operatorname{Prime}(\ell)\to\mathsf B(\ell,x)\bigr)
\]

expresses absence of every prime denominator and therefore defines

\[
\mathbb Z\subseteq\mathbb Q.
\]

This is exactly where the finite syntactic-support mechanism used in the present proof stops applying.

The present paper makes no claim that the uniformly indexed atlas has infinite GIR, defines prime successor, or interprets full arithmetic. It is the next open boundary.

---

## 19. Stationary information versus scalable information

The theorem suggests a useful distinction. Expressive strength is not measured simply by the number of local bits supplied to the structure.

For a fixed formula, finitely many stationary places yield a finite product of finite local color spaces. More places can greatly increase the number of colors, but the number remains finite and tied to the syntax of that formula.

What the proof excludes is a mechanism that turns those fixed local windows into a uniformly variable scale or coordinate. This motivates the heuristic boundary

\[
\boxed{
\text{stationary local information}
\quad\Big|\quad
\text{uniformly scalable local information}.
}
\]

The theorem establishes one rigorous region on the stationary side of that boundary. It does not assert that every scalable observable yields infinite GIR, nor that stationary locality is the only possible compression mechanism.

---

## 20. Relation to classical model theory

The target sort lies in the classical territory of abelian groups and modules. Szmielew's analysis of abelian groups, Baur's elimination theorem for modules, and Fisher's theory of abelian structures provide the natural background for positive-primitive geometry with distinguished additive subgroups.

The argument here is deliberately direct. The concrete finite family of localization predicates admits a simple local-coverage plus weak-approximation proof of the exact finite-depth normal form required by the bridge theorem.

The source sort is Skolem arithmetic. Its model theory is not globally tame in the sense of classical stability theory. In particular, finite GIR should not be read as a statement of stability or NIP. Likewise, the theorem proves non-definability of the standard prime order and prime successor and finite GIR for fixed isolators; it does not prove decidability of the complete theory or global non-interpretability of every copy of arithmetic.

---

## 21. Conclusion

A single fixed p-adic window was an interior point between prime symmetry and previously identified grid-amplification mechanisms. The present theorem turns that point into a region.

For every finite stationary atlas \(S\), a Private-Place Bridge satisfies Formula-Relative Tail Symmetry. In the Ramanujan case this applies to every finite atlas and, formula by formula, to the full family of separately named local predicates.

The proof separates two kinds of information. Fixed-depth local conditions are compressed into finitely many formula-relative colors. Exact affine accidents are controlled by private denominator places; non-pinned target witnesses remain movable because one can always choose more fresh private places than a fixed affine template can mention.

The central statement can therefore be summarized as

\[
\boxed{
\text{finitely many stationary local windows break symmetry without creating a scalable prime-addressing machine}.
}
\]

The next experiment begins when the local place itself is allowed to move as a first-order variable.

---

## References

1. W. Szmielew, **Elementary properties of Abelian groups**, *Fundamenta Mathematicae* **41** (1955), 203-271. DOI: 10.4064/fm-41-2-203-271.

2. W. Baur, **Elimination of quantifiers for modules**, *Israel Journal of Mathematics* **25** (1976), 64-70. DOI: 10.1007/BF02756561.

3. E. R. Fisher, **Abelian structures. I**, in *Abelian Group Theory*, Lecture Notes in Mathematics **616**, Springer, 1977, 270-322.

4. S. Ramanujan, **On certain arithmetical functions**, *Transactions of the Cambridge Philosophical Society* **22** (1916), 159-184.

5. P. Deligne, **Formes modulaires et représentations ℓ-adiques**, Séminaire Bourbaki, Exp. 355, Lecture Notes in Mathematics **179**, Springer, 1971, 139-172.

6. A. Stonestrom, **Some model theory of Th(N,·)**, *Mathematical Logic Quarterly* **68** (2022), 288-303. DOI: 10.1002/malq.202100049.

7. A. Bès and C. Richard, **Undecidable extensions of Skolem arithmetic**, *Journal of Symbolic Logic* **63** (1998). DOI: 10.2307/2586837.

---

## Author note

This work belongs to the “Riemann Hypothesis - Commander Sol” research programme and continues the Prime-Successor Algebra / Two Walls line. **Private-Place Bridge**, **Finite Stationary Locality**, **Formula-Relative Tail Symmetry**, **bounded-anchor cylinder**, and **Grid-Isolation Rank** are programme terms used for the mechanisms isolated here.
