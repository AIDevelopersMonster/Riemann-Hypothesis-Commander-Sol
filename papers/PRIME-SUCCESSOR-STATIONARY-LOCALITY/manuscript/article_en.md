# Reflections on Stationary Locality with Commander Sol
## Private-Place Bridges, Finite Multi-adic Windows, and Formula-Relative Compression

**Alex Malachevsky**  
ORCID: 0009-0008-6009-3196  
2026

## Abstract

We study a two-sorted expansion of Skolem arithmetic in which prime atoms are linked to rational labels and the target additive group is equipped with finitely many fixed p-adic integrality predicates. The motivating example is the Ramanujan label

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

A single fixed p-adic ball was previously shown to break some prime symmetry without recovering the standard order or prime-successor relation. Here we isolate the mechanism behind that phenomenon and prove a finite multi-place version.

The target structure

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\qquad B_\ell(x)\iff v_\ell(x)\ge0,
\]

with finite \(S\), admits a finite-depth normal form: every target formula is equivalent to a Boolean combination of exact rational linear equations and fixed-depth local conditions \(L(\bar x)\in B_{\ell,m}\). For a class of **Private-Place Bridges**, exact affine relations among prime labels are controlled by private denominator valuations, while non-pinned target witnesses can be moved inside a multi-place cell using fresh private places that lie outside the stationary atlas.

This yields the **Finite Stationary Locality Theorem**: every fixed first-order formula has a finite exceptional prime set and a finite multi-place depth vector such that its truth on prime tuples is invariant under all admissible prime permutations preserving the resulting finite local color classes and exact defect classes. Consequently, the standard order and successor relation on primes are not definable, and every fixed grid-isolator has finite Grid-Isolation Rank.

For Ramanujan labels, the hypotheses hold for every finite stationary atlas. We further note that even an infinite family of separately named predicates \((B_\ell)_{\ell\in\mathbb P}\) remains formula-by-formula finite, because an ordinary first-order formula mentions only finitely many place names. The genuine next boundary is therefore not a finite versus infinite list of named local windows, but a **uniformly indexed atlas** in which the place itself becomes a first-order variable through a relation \(\mathsf B(\ell,x)\).

---

## 1. From one fixed ball to a stationary atlas

The question behind this paper is not how much arithmetic information one can add to multiplication, but how that information can be transported.

The multiplicative structure

\[
(\mathbb N_{>0},\times)
\]

has an enormous symmetry on its prime atoms: every permutation of the primes extends uniquely to an automorphism by preserving exponents in prime factorization. Any attempt to define the ordinary order of the primes, or the next-prime relation, must therefore break this symmetry in a coherent way.

One natural way to break symmetry is to attach a rational label \(u_p\) to each prime atom \(p\). In our motivating Ramanujan example,

\[
\Delta(q)=q\prod_{n\ge1}(1-q^n)^{24}
=\sum_{n\ge1}\tau(n)q^n
\]

and

\[
u_p=\frac{\tau(p)^2}{p^{11}}-1.
\]

A target additive group can then observe those labels through local p-adic windows. The simplest non-trivial version uses one fixed predicate

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

The single-place argument reveals a useful distinction. A fixed local window may distinguish some primes, but a fixed formula cannot automatically turn the integer depth \(m\) in

\[
B_{\ell,m}=\{x:v_\ell(x)\ge m\}
\]

into a moving internal coordinate. The present paper asks whether several independent stationary places can cooperate to create such a coordinate system.

At first sight the danger is real. With two places \(\ell_1,\ell_2\), the local subgroups are no longer linearly ordered. The geometry becomes a lattice, and the Chinese remainder principle allows independent local conditions to be satisfied simultaneously. One might therefore suspect an additive two-dimensional grid: one place for rows, another for columns.

The result below says that this does not happen under the Private-Place hypotheses. Finitely many stationary local windows increase the number of finite colors visible to a formula, but they do not provide a scalable addressing mechanism.

We call this phenomenon **stationary locality**.

---

## 2. The two-sorted structure

Fix a finite set of rational primes

\[
S=\{\ell_1,\dots,\ell_s\}.
\]

The source sort is

\[
\mathcal N=(\mathbb N_{>0},\times).
\]

Its prime atoms are first-order definable as the non-unit irreducible elements. Every permutation of the prime atoms extends to an automorphism of \(\mathcal N\).

The target sort is

\[
\mathcal A_S=(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
\]

where

\[
B_\ell(x)\iff v_\ell(x)\ge0.
\]

The bridge is a binary relation \(U\) between the source and target sorts. On prime atoms it is functional:

\[
U(p,x)\iff x=u_p.
\]

We impose that the bridge is **prime-only**:

\[
U(n,x)\Longrightarrow \operatorname{Prime}(n).
\]

Thus no bridge atom transmits the exponent of \(p^k\) into the target. This multiplicity blindness is essential: the source may see arbitrary prime powers, but the target receives only the label attached to the prime atom itself.

We write

\[
\mathcal B_{u,S}
=
\Bigl(\mathcal N,\mathcal A_S,U\Bigr).
\]

---

## 3. Private-Place Bridges

The proof uses only a small amount of arithmetic structure in the labels.

After removing a finite exceptional set of prime atoms, suppose the remaining primes split into an infinite set \(R\) of **regular primes** and finitely many exact defect classes

\[
D_1,\dots,D_t.
\]

Each defect class \(D_j\) carries a fixed rational label \(\delta_j\).

For regular primes we assume the following.

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

while for every distinct \(p,q\in R\),

\[
v_{\lambda(p)}(u_q)\ge0.
\]

Thus every regular label possesses a denominator witness that belongs to no other regular label.

Because the defect labels \(\delta_j\) are rational and there are only finitely many of them, their combined denominator support is finite. Since \(\lambda\) is injective, after enlarging the finite exceptional set we may also assume

\[
v_{\lambda(p)}(\delta_j)\ge0
\]

for every regular \(p\) and every defect label.

A bridge satisfying these conditions will be called a **Private-Place Bridge over the stationary atlas \(S\)**.

The point of the terminology is structural. The proof below does not depend on the special form of Ramanujan's tau function. It depends on the fact that regular prime labels carry private external denominator places, while the observed places in \(S\) remain stationary and integral on the regular tail.

---

## 4. Fixed-depth predicates

For a fixed integer \(m\), define

\[
B_{\ell,m}(x)\iff v_\ell(x)\ge m.
\]

No variable depth is being added to the language. For every fixed \(m\), the predicate is definable from \(B_\ell\).

If \(m>0\), then

\[
B_{\ell,m}(x)
\iff
\exists y\,(\ell^m y=x\wedge B_\ell(y)),
\]

while

\[
B_{\ell,-m}(x)
\iff
B_\ell(\ell^m x).
\]

Since \((\mathbb Q,+)\) is uniquely divisible, multiplication by any fixed rational scalar is definable by a linear equation. We may therefore speak freely of rational linear forms in the target sort.

The basic target literals are

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in B_{\ell,m}.
\]

---

## 5. One place: the local coverage lemma

Fix a place \(\ell\). Let

\[
P=a+B_{\ell,m}
\]

be a positive base coset and let

\[
C_i=b_i+B_{\ell,n_i}
\qquad (1\le i\le r)
\]

be finitely many forbidden cosets.

Two \(\ell\)-adic balls are either disjoint or one contains the other. Therefore each intersection \(C_i\cap P\) is empty, equal to \(P\), or a proper subcoset of \(P\).

If some \(C_i\) contains \(P\), the surviving set is empty. Otherwise every relevant forbidden coset has depth at least \(m\). Put

\[
N=\max_i n_i.
\]

Refine all surviving forbidden cosets to depth \(N\). Coverage of \(P\) is then decided in the finite quotient

\[
B_{\ell,m}/B_{\ell,N},
\]

whose cardinality is

\[
\ell^{N-m}.
\]

Hence

\[
P\setminus\bigcup_i C_i\ne\varnothing
\]

is determined by a finite Boolean combination of relations among the centers of the form

\[
a-b_i\in B_{\ell,k},
\qquad
b_i-b_j\in B_{\ell,k},
\]

for finitely many fixed depths \(k\).

If there is no positive base coset at \(\ell\), finitely many forbidden balls cannot cover all of \(\mathbb Q\). Indeed, choose \(y\) with \(v_\ell(y)\) smaller than all relevant depths and all valuations of the finitely many centers; then \(v_\ell(y-b_i)=v_\ell(y)\), so \(y\) lies in none of the forbidden balls.

This is the local coverage lemma. The finite object is not \(\mathbb Q/B_{\ell,m}\), which is generally infinite. The finite object is the **refinement quotient** \(B_{\ell,m}/B_{\ell,N}\).

---

## 6. Multi-place target normal form

We now show that independent places do not create a hidden infinite-dimensional target geometry.

### Theorem 6.1. Multi-Place Finite-Depth Normal Form

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

with only finitely many fixed depths occurring for a fixed formula.

### Proof

After disjunctive normal form, it suffices to eliminate one existential target quantifier \(\exists y\) from a conjunction of literals.

If a non-trivial exact equation

\[
ay+t(\bar x)=0,
\qquad a\ne0,
\]

occurs, it uniquely determines

\[
y=-a^{-1}t(\bar x),
\]

and elimination is by substitution.

Assume that no exact equation pins \(y\). Every positive local literal involving \(y\) can be rewritten as

\[
y\in a+B_{\ell,m}.
\]

For each fixed \(\ell\), the positive balls form a chain under inclusion once they meet. They therefore reduce either to inconsistency or to one deepest positive base coset. Negative ball conditions at that place are handled by the local coverage lemma. We obtain a non-empty local open set

\[
U_\ell\subseteq\mathbb Q_\ell
\]

or else the original conjunction is inconsistent.

Suppose every \(U_\ell\) is non-empty. Because \(S\) is finite, weak approximation for \(\mathbb Q\), equivalently a direct Chinese-remainder construction after clearing denominators, produces a rational \(y\) lying in every \(U_\ell\) simultaneously.

Finally, exact inequalities

\[
y\ne c_1,\dots,y\ne c_r
\]

remove only finitely many points. A non-empty multi-place cell contains a sufficiently deep coset

\[
a+\bigcap_{\ell\in S}B_{\ell,M_\ell}
\]

and therefore infinitely many rational points. Finite point deletion cannot destroy it.

Thus projection remains in the Boolean algebra generated by exact linear equations and fixed-depth local conditions. Repeating the argument eliminates all target quantifiers. ∎

The theorem may be viewed as a concrete instance of the general pp-geometry philosophy behind the model theory of abelian groups and modules. The proof here is direct because the specific semilocal geometry is simpler than the general theory.

---

## 7. Multi-place cells contain full refinements

The elimination proof gives the following form that will be used for witness transport.

### Lemma 7.1. Generic Multi-Place Cell

Every non-empty Boolean cell cut out by finitely many fixed-depth target conditions contains a coset

\[
a+H_{\mathbf M},
\]

where

\[
H_{\mathbf M}
=
\bigcap_{\ell\in S}B_{\ell,M_\ell}
\]

for a finite depth vector \(\mathbf M=(M_\ell)_{\ell\in S}\).

### Proof

Choose one point \(a\) in the cell. At each place choose \(M_\ell\) deeper than all boundaries appearing in the finite list of local literals. Adding an element of \(H_{\mathbf M}\) cannot cross any of those boundaries, so all memberships and non-memberships are preserved. ∎

This is the multi-place replacement for the deepest-ball argument in the one-place case.

---

## 8. Exact linear separation by private places

The target normal form controls local information. Exact equalities require a different mechanism.

Fix integers \(c_1,\dots,c_r\) and consider

\[
\sum_{i=1}^r c_i u_{p_i}=0.
\]

Group equal regular primes. If a block represented by \(p\) has non-zero aggregate coefficient \(d\), then, except when the private prime \(\lambda(p)\) divides the fixed integer \(d\),

\[
v_{\lambda(p)}(d u_p)<0.
\]

Every other regular label is \(\lambda(p)\)-integral, and so are all defect labels after the finite exceptional set has been enlarged. Therefore the relation cannot vanish.

Because the map \(\lambda\) is injective, only finitely many regular primes can have \(\lambda(p)\) dividing any fixed non-zero coefficient.

We obtain:

### Lemma 8.1. Exact Linear Separation

For a fixed homogeneous coefficient scheme, outside a finite coefficient-dependent exceptional set, the relation

\[
\sum_i c_i u_{p_i}=0
\]

holds only when the aggregate coefficient of every regular-prime equality block is zero, with the remaining behavior determined by the exact defect classes.

In particular, regular labels are injective on the tail.

---

## 9. Affine equations and bounded-anchor cylinders

A naive affine-fiber claim would say that

\[
\sum_i c_i u_{p_i}=t
\]

has only boundedly many prime tuples. That is false when equality blocks cancel structurally. For example,

\[
u_{p_1}-u_{p_2}+u_{p_3}=u_q
\]

has all solutions

\[
(p_1,p_2,p_3)=(r,r,q).
\]

The correct object is a cylinder with free zero-sum blocks and finitely many anchored non-zero blocks.

Fix an equality pattern \(\pi\) on \(p_1,\dots,p_r\). For a block \(C\in\pi\), define

\[
d_C=\sum_{i\in C}c_i.
\]

Blocks with \(d_C=0\) disappear from the reduced affine equation.

### Lemma 9.1. Reduced Affine-Fiber Lemma

For the blocks with \(d_C\ne0\), the number of regular-prime assignments satisfying the reduced affine equation is uniformly bounded in terms of the fixed coefficient scheme, after removal of a finite coefficient-dependent exceptional set.

### Proof

Suppose there is one reduced solution \((q_C)\), and consider another \((q'_C)\). Subtraction yields a homogeneous relation. If a prime \(q'_C\) appeared in the second solution but not in the first, its private valuation would occur with a non-zero aggregate coefficient and could not be cancelled by any other term. Exact Linear Separation gives a contradiction.

Hence every second solution uses only the finitely many regular primes appearing in the first solution. If there are \(m\) non-zero blocks, a crude bound \(m^m\) on reassignments suffices. ∎

Thus exact affine traces are finite unions of **bounded-anchor cylinders**. Zero-sum equality blocks remain free; only the genuinely non-zero blocks can be anchored.

This repair is important. Formula-relative compression does not mean that all exceptional exact tuples are finite. It means that their non-structural prime support is bounded.

---

## 10. Fresh private places

We now reach the mechanism that makes non-pinned target witnesses movable.

Let a non-empty target cell contain

\[
a+H_{\mathbf M}.
\]

Suppose every relevant exact affine scheme involving a new target variable \(y\) uses at most \(r\) prime labels.

Choose regular primes

\[
t_1,\dots,t_{r+1}
\]

whose private places

\[
q_j=\lambda(t_j)
\]

lie outside:

1. the stationary atlas \(S\);
2. the denominator support of the finitely many already named target parameters;
3. the denominator support of the rational coefficients occurring in the finite template family.

This is possible because \(R\) is infinite and \(\lambda\) is injective.

Put

\[
D=q_1\cdots q_{r+1}
\]

and choose

\[
L=\prod_{\ell\in S}\ell^{N_\ell}
\]

with \(N_\ell\ge M_\ell\) for every \(\ell\in S\). Set

\[
y=a+\frac{L}{D}.
\]

At every stationary place \(\ell\in S\), the denominator \(D\) is a unit, so

\[
v_\ell(L/D)=N_\ell\ge M_\ell.
\]

Hence \(y\in a+H_{\mathbf M}\).

On the other hand, at each fresh private place \(q_j\), the center \(a\) is integral and

\[
v_{q_j}(L/D)=-1,
\]

so

\[
v_{q_j}(y)=-1.
\]

Consider any forbidden affine value

\[
z=\alpha+\sum_{i=1}^r c_i u_{p_i}.
\]

At most \(r\) prime labels occur. Among the \(r+1\) chosen primes \(t_j\), one, say \(t_k\), is absent. By private-place separation, every label occurring in \(z\) is \(q_k\)-integral; the same is true of \(\alpha\) and the coefficients by construction. Thus

\[
v_{q_k}(z)\ge0,
\]

whereas

\[
v_{q_k}(y)=-1.
\]

Therefore \(y\ne z\).

We have proved:

### Lemma 10.1. Fresh-Private-Place Avoidance

Inside every non-empty finite-depth multi-place cell one can choose a rational witness avoiding simultaneously all values of every fixed finite family of affine schemes involving at most \(r\) prime labels.

The important counting principle is simply

\[
r+1\ \text{fresh private places}\quad >\quad r\ \text{label slots}.
\]

---

## 11. Finite template closure and target-witness transport

Fix a mixed first-order formula \(\Phi\). Only finitely many rational coefficients, source terms, bridge occurrences, and local depths appear in its syntax.

Close this finite family under the operations that arise when eliminating a target variable:

- substitution from a pinning equation;
- differences of simultaneous pinning equations;
- the finite local refinements from Theorem 6.1;
- the exact affine consequences needed after substitution.

This produces a finite **template closure** attached to \(\Phi\).

Choose a depth vector

\[
\mathbf K_\Phi=(K_{\Phi,\ell})_{\ell\in S}
\]

large enough, after accounting for the finitely many rational coefficients, to determine every fixed-depth local template in the closure.

For a regular prime define its formula-relative multi-place color

\[
c_{\mathbf K_\Phi}(p)
=
\bigl(u_p+B_{\ell,K_{\Phi,\ell}}\bigr)_{\ell\in S}.
\]

By stationary-place integrality, only finitely many colors occur. If all \(K_{\Phi,\ell}\ge0\), a simple bound is

\[
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

Let \(\sigma\) be a permutation of prime atoms that fixes a finite exceptional set, preserves each regular color class, and preserves each exact defect class.

We transport target witnesses in two cases.

### 11.1. Pinned case

Suppose an exact equation

\[
ay+t=0,
\qquad a\ne0,
\]

holds for the witness \(y\). Transport all prime labels occurring in \(t\) by \(\sigma\) and define \(y'\) from the transported equation.

If several pinning equations hold, say

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0,
\]

their compatibility is equivalent to

\[
a_2t_1-a_1t_2=0.
\]

This is a template without \(y\), included in the finite closure and preserved by the induction hypothesis.

### 11.2. Free case

Suppose no relevant exact instance pins \(y\). The transported local literals determine a non-empty finite-depth target cell. By Lemma 7.1 it contains a full refinement coset. Fresh-Private-Place Avoidance then gives a target witness \(y'\) inside that cell while avoiding every exact affine incidence that was false before transport.

Thus every target witness for the finite fragment generated by \(\Phi\) can be transported.

---

## 12. Finite Stationary Locality Theorem

We can now state the main result.

### Theorem 12.1. Finite Stationary Locality

Let \(S\) be finite and let \(\mathcal B_{u,S}\) be a Private-Place Bridge structure satisfying the hypotheses of Section 3. For every parameter-free first-order formula

\[
\Phi(\bar p)
\]

whose free source variables are restricted to prime atoms, there exist:

- a finite exceptional set of primes \(F_\Phi\);
- a finite multi-place depth vector \(\mathbf K_\Phi\);

such that

\[
\mathcal B_{u,S}\models\Phi(\bar p)
\iff
\mathcal B_{u,S}\models\Phi(\sigma\bar p)
\]

for every prime permutation \(\sigma\) that:

1. fixes \(F_\Phi\) pointwise;
2. preserves every regular \(c_{\mathbf K_\Phi}\)-color class;
3. preserves every exact defect class setwise.

### Proof

Proceed by induction on the syntax of \(\Phi\).

Every prime permutation extends to an automorphism of \((\mathbb N_{>0},\times)\), so source atomic formulas are preserved. A bridge atom with composite source input is false both before and after transport. A bridge atom on a prime is an exact target incidence and belongs to the controlled finite template family.

Boolean connectives are immediate.

For an existential source witness \(n\), use its image under the multiplicative automorphism induced by \(\sigma\).

For an existential target witness, apply the pinned/free Target-Witness Transport of Section 11.

Universal quantifiers are reduced to existential quantifiers by negation. The finite exceptional set is enlarged only finitely many times through the finite syntax tree and the finite template closure. ∎

We call the conclusion **Formula-Relative Tail Symmetry**.

The theorem is deliberately formula-relative. It is not a claim that one global permutation group acts by automorphisms on the full two-sorted structure. The admissible tail partition depends on the formula under study.

---

## 13. Prime order and prime successor

Formula-Relative Tail Symmetry has immediate consequences for orientation on the prime atoms.

### Corollary 13.1. Prime order is not definable

The standard strict order \(<_{\mathbb P}\) on prime atoms is not definable in \(\mathcal B_{u,S}\).

### Proof

Assume a formula defines the standard order. Its formula-relative partition has finitely many movable classes outside a finite exceptional set. Since the regular tail is infinite, some class contains two distinct primes \(p\ne q\). Swapping \(p\) and \(q\) is admissible, but a strict linear order cannot be invariant under that swap. ∎

### Corollary 13.2. Prime successor is not definable

The standard relation

\[
\operatorname{Succ}_{\mathbb P}(p,q)
\]

saying that \(q\) is the next ordinary prime after \(p\) is not definable in \(\mathcal B_{u,S}\).

### Proof

Outside the finite exceptional set there are infinitely many consecutive prime pairs. The formula-relative partition has only finitely many ordered class pairs. Hence one ordered class pair occurs for two disjoint consecutive pairs

\[
(p,q),\qquad(p',q').
\]

The primes \(q,q'\) belong to the same movable class. Swap them while fixing \(p\). An admissible permutation would preserve the hypothetical successor formula and therefore make \(q'\) a successor of \(p\), contradiction. ∎

No density theorem for possible defect primes is used in this final successor argument.

---

## 14. Grid-Isolation Rank

To quantify a specific kind of two-dimensional addressing, we use the programme invariant **Grid-Isolation Rank**.

For a fixed formula \(I(p,q;r)\), say that \(I\) isolates an \(n\times n\) prime grid if there are distinct row primes \(p_1,\dots,p_n\), distinct column primes \(q_1,\dots,q_n\), and prime markers \(r_{ij}\) such that

\[
I(p_k,q_l;r_{ij})
\iff
(k,l)=(i,j).
\]

The supremum of such \(n\) is denoted \(\operatorname{GIR}(I)\).

### Corollary 14.1. Finite GIR

For every fixed isolator formula \(I\),

\[
\operatorname{GIR}(I)<\infty.
\]

### Proof

Apply Theorem 12.1 to \(I\). Outside a finite exceptional set there are only finitely many movable classes. In a sufficiently large row family, one class contains enough row primes that, for a chosen cell marker and column, two rows in that class can be swapped while fixing the column and marker. Formula-relative invariance then makes the same marker isolate two rows in the same column, contradicting the isolation property. ∎

This is not a statement of NIP, stability, or simplicity in the standard model-theoretic sense. GIR is a deliberately narrower programme invariant measuring the possibility of uniform cell isolation by a three-variable formula.

---

## 15. The Ramanujan bridge

We now verify the hypotheses for the motivating arithmetic labels

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}}.
\]

Fix a finite stationary atlas \(S\).

### 15.1. Integrality away from the label prime

If \(p\notin S\), then for every \(\ell\in S\), the denominator \(p^{11}\) is an \(\ell\)-adic unit. Therefore

\[
v_\ell(u_p)\ge0.
\]

This is H1.

### 15.2. Private denominator at a good prime

Call \(p\ge5\) **good** if

\[
\tau(p)\ne0.
\]

Let

\[
a=v_p(\tau(p)).
\]

Deligne's bound gives

\[
|\tau(p)|\le2p^{11/2}.
\]

If \(a\ge6\), then \(|\tau(p)|\ge p^6\), hence

\[
p^6\le2p^{11/2},
\]

which implies \(\sqrt p\le2\), impossible for \(p\ge5\). Thus

\[
a\le5.
\]

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

Hence on the good-prime tail we may take

\[
\lambda(p)=p.
\]

This map is injective and lies outside \(S\) after the finitely many primes in \(S\) have been excluded.

### 15.3. The zero-prime defect class

If

\[
\tau(p)=0,
\]

then

\[
u_p=-1.
\]

Thus all zero primes, if they exist, form one exact common-label defect class.

### 15.4. Infinitely many good primes without a density theorem

For the abstract theorem we need an infinite reservoir of regular primes. This follows from classical facts without using a density estimate for the possible zeros of \(\tau(p)\).

Ramanujan's congruence gives, for prime \(p\),

\[
\tau(p)\equiv1+p^{11}\pmod{691}.
\]

For every prime

\[
p\equiv1\pmod{691},
\]

we have

\[
\tau(p)\equiv2\pmod{691},
\]

so \(\tau(p)\ne0\). Dirichlet's theorem on primes in arithmetic progressions supplies infinitely many such primes.

Therefore the set of good regular primes is infinite.

We conclude:

### Corollary 15.1. Finite stationary Ramanujan atlases

For every finite set of rational primes \(S\), the structure

\[
\mathcal B_{\Delta,S}
=
\Bigl(
(\mathbb N_{>0},\times),
(\mathbb Q,+,0,(B_\ell)_{\ell\in S}),
U_\Delta
\Bigr)
\]

satisfies Formula-Relative Tail Symmetry. Consequently the ordinary prime order and prime-successor relation are not definable, and every fixed isolator has finite GIR.

---

## 16. The infinite named stationary atlas

There is a useful strengthening specific to ordinary first-order syntax.

Consider the target language with one separate predicate symbol \(B_\ell\) for every rational prime:

\[
\mathcal A_{\mathrm{name}}
=
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}).
\]

The language is infinite, but each first-order formula is a finite string. Therefore a fixed formula \(\Phi\) mentions only finitely many place symbols. Let that finite support be

\[
S_\Phi\subset\mathbb P.
\]

For the Ramanujan bridge, all primes outside \(S_\Phi\) are \(S_\Phi\)-integral. The finite theorem therefore applies to \(\Phi\).

### Corollary 16.1. Infinite Named Stationary Atlas

The Ramanujan structure with every \(B_\ell\) separately named remains formula-by-formula compressed: every fixed formula still has a finite exceptional set and a finite local color partition on the prime tail.

This gives a striking distinction.

For a good prime \(p\), the predicate symbol \(B_p\) can individually distinguish \(p\):

\[
q=p
\iff
\operatorname{Prime}(q)
\wedge
\exists x\bigl(U_\Delta(q,x)\wedge\neg B_p(x)\bigr),
\]

because \(u_p\) is not \(p\)-integral while every other Ramanujan label is.

Thus many individual prime atoms can be pointwise distinguishable in the infinite named language even though there is still no single formula that uniformly orients them by the standard order or successor relation.

In programme terminology:

\[
\boxed{\text{pointwise distinguishability}\ne\text{uniform orientation}.}
\]

---

## 17. Where the next phase boundary actually lies

The preceding corollary removes a tempting but false boundary. The difference

\[
|S|<\infty
\quad\text{versus}\quad
|S|=\infty
\]

is not by itself a first-order phase transition if the places are merely separately named predicates.

A genuinely different language is obtained by introducing a place sort and a single relation

\[
\mathsf B(\ell,x)
\iff
v_\ell(x)\ge0,
\]

where \(\ell\) is now a first-order variable.

Then one formula can aggregate information over unboundedly many places. For example,

\[
\forall\ell\,
\bigl(\operatorname{Prime}(\ell)\rightarrow\mathsf B(\ell,x)\bigr)
\]

expresses, for rational \(x\), the absence of every prime denominator and therefore defines

\[
\mathbb Z\subset\mathbb Q.
\]

The finite-syntax support barrier has disappeared.

We call this the **Uniformly Indexed Atlas** problem. The present paper does not claim that the uniformly indexed structure has infinite GIR, defines prime successor, or interprets full arithmetic. It identifies the point at which the mechanism of the present proof ceases to apply: the observed place is no longer stationary syntax, but a variable that can be quantified over.

This is the next natural rightward experiment in the corridor between prime symmetry and full arithmetic.

---

## 18. Stationary versus scalable information

The theorem suggests a broader principle.

A fixed local observable can be informative without being scalable. The predicates

\[
B_{\ell,m}
\]

for fixed \(m\) distinguish finitely many residue-depth colors relevant to a fixed formula. Several independent places multiply the number of colors, but the number remains finite.

The dangerous transition is not simply

\[
\text{little information}\to\text{more information}.
\]

It is closer to

\[
\boxed{\text{stationary local information}\to\text{uniformly scalable local information}.}
\]

This perspective explains why a one-bit observable can sometimes be more expressive than a richer additive structure: if that bit persists under arbitrarily deep, uniformly addressable refinement, it may support grid amplification. Conversely, a large but stationary finite atlas may remain formula-relatively compressed.

The present theorem establishes one rigorous region of this proposed phase diagram. It does not assert that stationary locality is the unique possible mechanism of safety, nor that every scalable observable necessarily yields infinite GIR. Those are separate research questions.

---

## 19. Relation to classical model theory

The additive target belongs to the broad territory of the model theory of abelian groups and modules. Szmielew's analysis of elementary properties of abelian groups and the Baur-Monk elimination theory for modules provide the classical background for reducing definability questions to positive-primitive geometry and finite invariant data. Fisher's abelian structures provide a natural framework for additive groups expanded by distinguished subgroups.

Our use is deliberately narrower and self-contained. We do not require a complete classification of the theory of

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in S}).
\]

The direct local-coverage and weak-approximation argument proves exactly the target normal form needed for the bridge theorem.

Likewise, the conclusion \(\operatorname{GIR}(I)<\infty\) should not be identified with model-theoretic stability. Pure Skolem arithmetic itself has substantial combinatorial complexity. GIR measures only the specific uniform cell-isolation mechanism introduced in this programme.

Finally, our conclusions are weaker than global non-interpretability claims. We prove non-definability of the standard prime order and successor in the stated bridge structures and finite GIR for each fixed isolator. We do not claim decidability of the complete theory, NIP, stability, or the impossibility of every interpretation of arithmetic.

---

## 20. What the corridor now contains

The fixed-ball construction gave one interior point between multiplicative prime symmetry and the previously identified right-wall grid-amplification mechanisms. The present theorem turns that point into a region.

For the Ramanujan bridge we now have the family

\[
\{\mathcal B_{\Delta,S}:|S|<\infty\},
\]

and, formula by formula, even the full named stationary atlas

\[
(\mathbb Q,+,0,(B_\ell)_{\ell\in\mathbb P}).
\]

Within this region:

- stationary local information can distinguish primes;
- every fixed formula sees only finitely many local colors;
- exact affine accidents are confined to bounded-anchor cylinders;
- fresh private places remain available outside the observed atlas;
- target witnesses can be transported;
- the ordinary prime order and successor remain undefinable;
- every fixed grid-isolator has finite GIR.

The corridor is therefore not merely an empty interval between two previously known behaviors. It has internal structure.

The next boundary is no longer “one p-adic ball versus several” or “finitely many named balls versus infinitely many named balls.” It is the passage from stationary names to a uniformly quantified local coordinate:

\[
(B_\ell)_{\ell\in\mathbb P}
\quad\Big|\quad
\mathsf B(\ell,x).
\]

That is where the next investigation begins.

---

## 21. Conclusion

The central result may be summarized in one sentence:

\[
\boxed{\text{finitely many stationary local windows break symmetry without creating a scalable prime-addressing machine}.}
\]

The proof has two independent halves. The target half says that finite multi-adic additive geometry reduces to fixed-depth local cells. The bridge half says that exact prime-label relations are controlled by private denominator places, and that a non-pinned witness can always be moved using more fresh private places than any fixed affine template can mention.

Together they yield Formula-Relative Tail Symmetry.

For Ramanujan labels this applies to every finite stationary atlas and, formula by formula, to the infinite named atlas. The result sharpens the emerging phase picture of the Prime-Successor programme: the significant resource is not merely local information, but the ability to make the local coordinate itself move uniformly inside a first-order formula.

---

## References

1. W. Szmielew, **Elementary properties of Abelian groups**, *Fundamenta Mathematicae* **41** (1955), 203–271. DOI: 10.4064/fm-41-2-203-271.

2. W. Baur, **Elimination of quantifiers for modules**, *Israel Journal of Mathematics* **25** (1976), 64–70. DOI: 10.1007/BF02756561.

3. E. R. Fisher, **Abelian structures. I**, in *Abelian Group Theory*, Lecture Notes in Mathematics **616**, Springer, 1977, 270–322.

4. S. Ramanujan, **On certain arithmetical functions**, *Transactions of the Cambridge Philosophical Society* **22** (1916), 159–184.

5. P. Deligne, **Formes modulaires et représentations ℓ-adiques**, Séminaire Bourbaki, Exp. 355, Lecture Notes in Mathematics **179**, Springer, 1971, 139–172.

6. A. Stonestrom, **Some model theory of Th(N,·)**, *Mathematical Logic Quarterly* **68** (2022). DOI: 10.1002/malq.202100049.

7. A. Bès and C. Richard, **Undecidable extensions of Skolem arithmetic**, *Journal of Symbolic Logic* **63** (1998). DOI: 10.2307/2586837.

---

## Author note

This work is part of the “Riemann Hypothesis — Commander Sol” research programme and continues the Prime-Successor Algebra / Two Walls line. The terminology **Private-Place Bridge**, **Finite Stationary Locality**, **Formula-Relative Tail Symmetry**, **bounded-anchor cylinder**, and **Grid-Isolation Rank** is programme terminology used to organize the mechanisms proved here.
