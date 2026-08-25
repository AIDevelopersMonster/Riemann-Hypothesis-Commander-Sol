# Mixed Quantifier Compression for the Fixed-Ball Interior

**Version:** 1.1  
**Date:** 2026-08-25  
**DOI:** https://doi.org/10.5281/zenodo.22101603  
**Status:** proof checkpoint revised after adversarial review

## 1. Structure

We work with

\[
\mathcal B_\Delta=
\Bigl(
(\mathbb N_{>0},\times),
(\mathbb Q,+,0,B),
U_\Delta
\Bigr),
\]

where

\[
B(x)\iff v_{13}(x)\ge0,
\qquad
u_p:=U_\Delta(p)=\frac{\tau(p)^2-p^{11}}{p^{11}}
\]

for prime atoms \(p\). A prime is called **good** if \(p\ge5\) and \(\tau(p)\ne0\).

For a fixed \(K\ge0\), define

\[
B_K:=\{x\in\mathbb Q:v_{13}(x)\ge K\},
\qquad
c_K(p):=u_p+B_K.
\]

For \(p\ne13\), \(u_p\in B_0\), hence the good-prime color \(c_K(p)\) ranges over the finite quotient

\[
B_0/B_K\cong\mathbb Z/13^K\mathbb Z.
\]

If \(\tau(p)=0\), then

\[
u_p=-1.
\]

Thus all zero primes, if any, form one exact common-label class.

---

## 2. Definability of the fixed depth chain

The language names only

\[
B=B_0=\mathbb Z_{(13)}.
\]

Nevertheless every fixed level

\[
B_m(x)\iff v_{13}(x)\ge m,
\qquad m\in\mathbb Z,
\]

is definable in the original language \((+,0,B)\).

For \(m>0\),

\[
B_m(x)\iff B(13^{-m}x),
\]

which may be written without naming scalar multiplication by \(13^{-m}\) as

\[
B_m(x)\iff \exists y\,(13^m y=x\land B(y)).
\]

For \(m>0\),

\[
B_{-m}(x)\iff B(13^m x).
\]

Here \(13^m y\) and \(13^m x\) are definable by repeated addition. Since \((\mathbb Q,+)\) is divisible, the first formula defines exactly the required inverse image.

This justifies the use of the definitional expansion by the full fixed chain \(\{B_m:m\in\mathbb Z\}\).

---

## 3. Target finite-depth normal form

Every target formula in \((\mathbb Q,+,0,B)\) is equivalent, after the definitional expansion by the fixed \(B_m\), to a Boolean combination of atoms

\[
L(\bar x)=0
\]

and

\[
L(\bar x)\in B_m,
\]

where \(L\) is a rational linear form and only finitely many fixed depths \(m\) occur for a fixed formula.

### Elimination of one target quantifier

After DNF it suffices to eliminate \(\exists y\) from a conjunction of literals.

* If a non-trivial exact equality
  \[
  ay+t(\bar x)=0,
  \qquad a\ne0,
  \]
  occurs, then \(y\) is uniquely determined and eliminated by substitution.
* Otherwise each positive ball literal is a coset condition
  \[
  y\in a_i(\bar x)+B_{m_i}.
  \]
  Because the \(B_m\) form a linearly ordered chain, the intersection of finitely many positive cosets is empty or is one coset of the deepest subgroup among them.
* Negative ball literals remove finitely many deeper subcosets. If \(N\) is the deepest level occurring, the question whether these removed subcosets cover the surviving positive coset is a finite question in a quotient \(B_M/B_N\), whose cardinality is a power of 13.
* If there are no positive ball conditions, finitely many forbidden cosets and finitely many exact inequalities cannot cover all of \(\mathbb Q\).
* Finitely many exact inequalities remove finitely many points and therefore cannot cover a non-empty coset.

Projection therefore produces again a Boolean combination of exact linear equalities and fixed-depth ball conditions.

This is the **Target Finite-Depth Normal Form**.

---

## 4. Private denominator

Let \(p\ge5\) be good and write

\[
\tau(p)=p^a b,
\qquad p\nmid b.
\]

Deligne's estimate

\[
|\tau(p)|\le2p^{11/2}
\]

implies \(a\le5\). Hence

\[
11-2a\in\{1,3,5,7,9,11\}.
\]

Now

\[
\tau(p)^2-p^{11}
=p^{2a}\bigl(b^2-p^{11-2a}\bigr).
\]

Because \(p\nmid b\) and \(11-2a\ge1\),

\[
p\nmid b^2-p^{11-2a}.
\]

Therefore

\[
v_p(\tau(p)^2-p^{11})=2a
\]

and hence

\[
v_p(u_p)=2a-11\in\{-11,-9,-7,-5,-3,-1\}<0.
\]

For \(q\ne p\), the denominator of \(u_q\) is a power of \(q\), so

\[
v_p(u_q)\ge0.
\]

Thus every good prime carries its own non-13 private denominator signature.

---

## 5. Exact linear separation

Fix integers \(d_1,\ldots,d_s\), not all zero. Let \(p_1,\ldots,p_s\) be distinct good primes outside the finite set of primes dividing any non-zero coefficient which can arise after grouping equal variables.

If

\[
\sum_{j=1}^s d_j u_{p_j}=0,
\]

then for each \(j\), the \(p_j\)-adic valuation of \(d_j u_{p_j}\) is negative while all other terms are \(p_j\)-integral, unless \(p_j\mid d_j\). Outside the coefficient-exception set this is impossible. Therefore after grouping equal primes, every aggregate coefficient must vanish.

Hence, on the good-prime tail, every fixed homogeneous linear relation among labels is determined by the equality pattern.

### Corollary 5.1. Injectivity on good primes

If \(p\ne q\) are good, then

\[
u_p\ne u_q.
\]

Indeed, \(u_p=u_q\) would give the homogeneous relation

\[
u_p-u_q=0.
\]

At valuation \(v_p\), the first term is negative and the second is non-negative, contradiction.

---

## 6. Uniform affine-fiber bound

Fix coefficients \(c_1,\ldots,c_r\) and consider

\[
\sum_{i=1}^r c_i u_{p_i}=t,
\qquad t\in\mathbb Q.
\]

After excluding the finitely many primes dividing non-zero signed subset sums arising from the coefficient scheme, every non-structural affine fiber has uniformly bounded size, independently of \(t\).

If \(\bar p\) and \(\bar q\) are two solutions, subtraction gives

\[
\sum_i c_i u_{p_i}-\sum_i c_i u_{q_i}=0.
\]

After collecting equal primes, the resulting aggregate coefficients belong to a finite set determined solely by the original coefficient vector. Exact linear separation forces every prime appearing on one side to appear on the other with the same aggregate coefficient. Thus once one solution is fixed, any second solution uses only the finitely many primes already present in the first tuple, with one of finitely many coefficient-compatible equality patterns.

Hence there is a constant \(N_c<\infty\), depending only on the fixed coefficient scheme, such that each non-structural affine fiber contains at most \(N_c\) good-prime tuples. A crude combinatorial bound such as \(r^r\) is sufficient.

This is the **Uniform Affine-Fiber Lemma**.

---

## 7. Parameterized target traces

Let \(\theta(\bar y;\bar x)\) be a fixed target formula and substitute

\[
\bar y=(u_{p_1},\ldots,u_{p_r}).
\]

By the target normal form, \(\theta\) is a Boolean combination of fixed-depth ball literals and exact linear equalities.

For fixed target parameters \(\bar a\):

1. fixed-depth literals depend only on sufficiently deep finite colors \(c_K(p_i)\), equality pattern, and one of finitely many target parameter states modulo the relevant fixed quotient;
2. each non-structural exact equality contributes a uniformly bounded exceptional set by the Uniform Affine-Fiber Lemma;
3. structural exact equalities depend only on equality pattern.

Therefore there are constants \(K_\theta,N_\theta\) such that

\[
R_{\bar a}(\bar p):=\theta(u_{p_1},\ldots,u_{p_r};\bar a)
\]

has the form

\[
R_{\bar a}=R^{\rm bulk}_{\eta(\bar a)}\triangle E_{\bar a},
\qquad |E_{\bar a}|\le N_\theta,
\]

where only finitely many bulk states \(\eta(\bar a)\) are possible for the fixed formula \(\theta\).

This is the **Parameterized Target Trace Lemma**.

---

## 8. Multiplicity-Blind Bridge Principle

The bridge predicate links only prime atoms to target labels:

\[
U_\Delta(p,x)\quad\Longrightarrow\quad p\text{ is prime and }x=u_p.
\]

It does not attach a target value to a prime power \(p^k\) for \(k\ge2\), and it does not provide any relation of the form

\[
p^k\longmapsto k,
\qquad
p^k\longmapsto ku_p,
\qquad
p^k\longmapsto B_k.
\]

A source formula may inspect the factorization of \(p^k\), but every prime divisor it can feed into the bridge is still the same atom \(p\). In particular, from \(13^k\) the bridge extracts only the fixed target label \(u_{13}\), not the exponent \(k\).

This is the **Multiplicity-Blind Bridge Principle**. It is not by itself the full No Scale Synchronization theorem, but it is the structural reason why exponent multiplicity is not directly transmitted into target depth.

---

## 9. Fresh-denominator avoidance

Fix finitely many already named target parameters and finitely many affine templates in which a new target witness \(y\) can occur together with at most \(r\) prime labels.

Let \(C\) be a non-empty Boolean cell determined by finitely many fixed-depth ball conditions. Choose one point \(a\in C\). There exists \(M\) such that every perturbation in \(B_M\) remains inside the same cell.

Choose pairwise distinct non-13 primes

\[
\ell_1,\ldots,\ell_{r+1}
\]

outside the finite denominator support of all already named target parameters and all rational coefficients occurring in the templates. Set

\[
D=\ell_1\cdots\ell_{r+1}
\]

and take

\[
y=a+\frac{13^{M'}}{D}
\]

with \(M'\) large enough that the perturbation lies in \(B_M\).

Then \(y\in C\), while any affine combination involving at most \(r\) good-prime labels can introduce at most \(r\) fresh private non-13 denominator primes outside the fixed coefficient and parameter support. Hence it cannot equal \(y\), whose denominator contains \(r+1\) fresh primes.

This yields simultaneous avoidance of every unwanted exact affine incidence represented by the finite template family.

---

## 10. Target-witness transport

Fix a mixed formula \(\Phi\). Close its finite target template family under all finite linear consequences and projection conditions needed by the target normal form. Choose \(K_\Phi\) large enough for every fixed-depth template and a finite exceptional set \(F_\Phi\) containing all coefficient exceptions and all finite color classes.

Let \(\sigma\) be a permutation of prime atoms which:

* fixes \(F_\Phi\);
* preserves the relevant good-prime colors \(c_{K_\Phi}\);
* preserves the common-label zero-prime class \(\{p:\tau(p)=0\}\) setwise;
* fixes any other finite special prime classes required by the formula.

The permutation extends canonically to an automorphism of the pure multiplicative source monoid by permuting prime coordinates and preserving exponents.

Suppose a finite tuple of target parameters has already been transported so that every template in the finite closure has the same truth value after applying \(\sigma\) to all prime arguments. Let \(y\) be one additional target witness.

### Pinned case

If a relevant exact equation

\[
a_1y+t_1=0,
\qquad a_1\ne0,
\]

holds, then \(y\) is pinned to a rational affine combination of the already transported parameters and a bounded set of prime labels. Transport those prime labels and define \(y'\) by the same affine equation.

If several pinning equations hold simultaneously,

\[
a_1y+t_1=0,
\qquad
a_2y+t_2=0,
\]

their compatibility is equivalent to the exact consequence

\[
a_2t_1-a_1t_2=0.
\]

This consequence contains no \(y\) and belongs to the finite linear closure used in the inductive invariant. Hence if the pinning equations are compatible before transport, they remain compatible after transport. The same argument applies to any finite family of pinning equations.

Any new unintended exact incidence after transport would, after subtraction from one pinning equation, produce another controlled homogeneous template. Applying \(\sigma^{-1}\) would yield the corresponding unintended incidence before transport, contradiction.

### Free case

If no exact equation pins \(y\), the fixed-depth literals define a non-empty Boolean cell in the chain of 13-adic cosets. The corresponding transported cell is non-empty because the target normal form and the finite projection conditions are preserved.

Use Fresh-Denominator Avoidance inside this transported cell. It gives a witness \(y'\) satisfying the same fixed-depth data while simultaneously avoiding every unwanted exact affine incidence represented by the finite formula-relative template family.

Thus target witnesses can always be transported for the finite fragment relevant to \(\Phi\).

---

## 11. Mixed Quantifier Compression / Formula-Relative Tail Symmetry

Induct on the syntax of \(\Phi\).

* Boolean connectives are immediate.
* For a source existential witness \(n\), use \(\sigma(n)\). All source multiplication relations are preserved because \(\sigma\) is a prime-coordinate permutation.
* For a target existential witness, use Target-Witness Transport.
* Universal quantifiers follow by negation.

Therefore for every mixed formula \(\Phi(\bar p)\) with free prime variables there exist \(K_\Phi\), a finite exceptional set \(F_\Phi\), finitely many movable good-prime color classes, and the common-label zero-prime class such that

\[
\Phi(\bar p)\iff\Phi(\sigma(\bar p))
\]

for every formula-admissible permutation \(\sigma\) preserving those classes and fixing \(F_\Phi\).

This is **Formula-Relative Tail Symmetry**. It is intentionally not stated as a global automorphism theorem for the full exact bridge structure.

---

## 12. No Scale Synchronization

Consider the definable source chain

\[
1,13,13^2,\ldots.
\]

By the Multiplicity-Blind Bridge Principle, the bridge sends every source occurrence extracted from \(13^k\) only to the fixed label \(u_{13}\). The remaining dependence on \(k\) lies in the pure multiplicative source coordinate, whose one-prime-power fiber is Presburger. Hence every fixed formula induces eventually periodic dependence on sufficiently large \(k\).

The family

\[
B_k=\{x:v_{13}(x)\ge k\}
\]

is strictly decreasing and is not eventually periodic in \(k\). Therefore no fixed mixed formula can realize

\[
\Sigma(13^k,x)\iff x\in B_k
\]

for all sufficiently large \(k\).

This is the **Periodic-Depth Mismatch / No Scale Synchronization** consequence.

---

## 13. Prime order

A finite formula-relative partition of the infinite prime tail has an infinite movable class. Swapping two distinct primes in that class preserves any fixed candidate defining formula, but reverses the asymmetry required by a strict linear order.

Therefore the standard prime order is not first-order definable in \(\mathcal B_\Delta\).

---

## 14. Prime successor without a Lehmer/Serre hypothesis

For a hypothetical successor-defining formula \(S(p,q)\), Formula-Relative Tail Symmetry gives only finitely many ordered movable class pairs outside a finite exceptional set.

There are infinitely many consecutive prime pairs

\[
(p_n,p_{n+1}).
\]

Since only finitely many ordered formula-relative class pairs are available, one ordered class pair occurs for at least two distinct consecutive pairs

\[
(p,q),\qquad(p',q').
\]

The classes may be good-prime color classes or, if zero primes occur, the common exact-label class \(u_p=-1\). No density statement about zero primes is required.

Choose the two pairs so that the relevant elements are outside the finite exceptional set and distinct. A formula-admissible permutation can fix \(p\) and replace \(q\) by \(q'\) inside its movable class. Hence

\[
S(p,q)\iff S(p,q'),
\]

while only \(q\) is the next prime after \(p\), contradiction.

Thus prime successor is not first-order definable in \(\mathcal B_\Delta\).

**External note.** Serre proved that the set of primes \(p\) with \(\tau(p)=0\) has density zero. This is compatible with the argument above but is not used as a hypothesis in the successor proof.

---

## 15. Finite Grid-Isolation Rank

Fix an isolator formula \(I(p,q;r)\). Formula-relative compression supplies finitely many movable prime classes, a finite exceptional set, and only bounded exact exceptional configurations.

In a sufficiently large putative isolated grid, after removing exceptional rows, columns and marker coincidences, two rows must have the same formula-relative class. A formula-admissible permutation exchanging those two rows while fixing the relevant column and marker preserves the truth value of \(I\), contradicting isolation of a single cell.

Therefore there is a formula-dependent finite constant \(C(I)\) such that

\[
\operatorname{GIR}(I)\le C(I)<\infty.
\]

No universal numerical bound such as \(13^{2K_I}\) is claimed without explicit bookkeeping of equality patterns, finite special classes and bounded exact exceptions.

---

## 16. Interior status and scope

Prime 13 is parameter-free definable:

\[
p=13\iff \operatorname{Prime}(p)\land\exists x\bigl(U_\Delta(p,x)\land\neg B(x)\bigr).
\]

Indeed, for every prime \(p\ne13\), \(u_p\in B\), while

\[
v_{13}(u_{13})=-11.
\]

Thus the fixed-ball expansion is strictly stronger than pure prime-permutation symmetry in the concrete sense that it distinguishes a specific prime atom.

At the same time,

\[
S_{\mathbb P},<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta)
\]

and every fixed isolator has finite GIR.

The programme therefore places \(\mathcal B_\Delta\) strictly inside the corridor between the left symmetry wall and the previously exhibited right-wall grid-amplification mechanisms. The phrase

\[
(\mathbb N_{>0},\times)<\mathcal B_\Delta<\text{right-wall grid regime}
\]

is a programme diagram, not a claim that a fully formal global preorder of interpretations between these three displayed objects has been established.

The result does **not** claim:

* decidability of the complete theory \(\operatorname{Th}(\mathcal B_\Delta)\);
* non-interpretability of full arithmetic by every possible interpretation;
* an explicit effective map \(\Phi\mapsto K_\Phi\);
* historical priority for the general model-theoretic mechanisms.
