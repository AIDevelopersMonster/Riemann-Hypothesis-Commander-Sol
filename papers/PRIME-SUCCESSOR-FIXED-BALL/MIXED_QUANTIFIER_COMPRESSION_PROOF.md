# Mixed Quantifier Compression for the Fixed-Ball Candidate

**Date:** 2026-08-25  
**Status:** proof checkpoint after adversarial review  
**Branch:** `research/fixed-ball-interior`

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

For a fixed \(K\ge0\), define the finite 13-adic color

\[
c_K(p):=u_p+B_K,
\qquad
B_K:=\{x\in\mathbb Q:v_{13}(x)\ge K\}.
\]

For \(p\ne13\), \(u_p\in B_0\), hence \(c_K(p)\) ranges over the finite quotient \(B_0/B_K\), of size \(13^K\).

---

## 2. Target finite-depth normal form

Expand the target language definitionally by all fixed predicates

\[
B_m(x)\iff v_{13}(x)\ge m,
\qquad m\in\mathbb Z.
\]

Every target formula in \((\mathbb Q,+,0,B)\) is equivalent to a Boolean combination of

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

* A non-trivial exact equality \(ay+t(\bar x)=0\) pins \(y\) uniquely and is eliminated by substitution.
* Without such an equality, each positive ball literal is a coset condition
  \[
  y\in a_i(\bar x)+B_{m_i}.
  \]
  Since the \(B_m\) form a chain, their intersection is empty or one coset of the deepest subgroup.
* Negative ball literals remove finitely many deeper subcosets. If \(N\) is the deepest level appearing, coverage of the surviving coset is decided in the finite quotient \(B_M/B_N\).
* Finitely many exact inequalities remove finitely many points and cannot cover a non-empty coset.

Thus projection again yields a Boolean combination of the same two forms.

This is the **Target Finite-Depth Normal Form**.

---

## 3. Private denominator and exact linear separation

For a good prime \(p\), write \(a=v_p(\tau(p))\). Deligne's bound implies \(a\le5\), hence

\[
v_p(u_p)=2a-11<0.
\]

For \(q\ne p\),

\[
v_p(u_q)\ge0.
\]

Consequently, for any fixed integer coefficient vector \(d_1,\ldots,d_s\), there is a finite coefficient-exception set \(F(d)\) such that for distinct good primes outside \(F(d)\),

\[
\sum_{j=1}^s d_j u_{p_j}=0
\]

can hold only when, after grouping equal primes, the aggregate coefficient of every equality block is zero.

In particular, on the good-prime tail, every fixed homogeneous linear relation is determined solely by its equality pattern.

---

## 4. Uniform affine-fiber bound

Fix coefficients \(c_1,\ldots,c_r\) and consider

\[
\sum_{i=1}^r c_i u_{p_i}=t,
\qquad t\in\mathbb Q.
\]

After excluding the finitely many primes dividing non-zero subset sums of the \(\pm c_i\), every non-structural affine fiber has uniformly bounded size, independently of \(t\).

Indeed, if \(\bar p\) and \(\bar q\) are two solutions, subtraction gives

\[
\sum_i c_i u_{p_i}-\sum_i c_i u_{q_i}=0.
\]

Exact linear separation forces every prime occurring on one side to occur on the other with the same aggregate coefficient. Thus, once one solution is fixed, every second solution uses only the finitely many primes already occurring in the first tuple, with one of finitely many coefficient-compatible equality patterns. A crude bound such as \(r^r\) is therefore sufficient after fixing the coefficient scheme.

Structural equality-pattern solutions are not exceptions; they are absorbed into the bulk relation.

This is the **Uniform Affine-Fiber Lemma**.

A useful corollary is injectivity on good primes:

\[
p\ne q\text{ good}\quad\Longrightarrow\quad u_p\ne u_q.
\]

---

## 5. Parameterized target traces

Let \(\theta(\bar y;\bar x)\) be a fixed target formula. Substitute prime labels \(\bar y=(u_{p_1},\ldots,u_{p_r})\).

By the target normal form, \(\theta\) is a Boolean combination of valuation literals and exact linear equalities.

For fixed target parameters \(\bar a\):

1. valuation literals depend only on a sufficiently deep finite color \(c_K(p_i)\) and the equality pattern of the prime tuple;
2. each non-structural exact equality contributes a uniformly bounded exceptional set of prime tuples by the Uniform Affine-Fiber Lemma;
3. structural exact equalities depend only on equality pattern.

Hence there are constants \(K_\theta,N_\theta\) such that every trace

\[
R_{\bar a}(\bar p):=\theta(u_{p_1},\ldots,u_{p_r};\bar a)
\]

has the form

\[
R_{\bar a}=R^{\rm bulk}_{\eta(\bar a)}\triangle E_{\bar a},
\qquad |E_{\bar a}|\le N_\theta,
\]

where the bulk relation depends only on finite colors and equality pattern. Only finitely many bulk states are possible for a fixed \(\theta\).

This is the **Parameterized Target Trace Lemma**.

---

## 6. Why alternating quantifiers do not defeat compression

The essential point is not a naive interchange of source and target quantifiers. Instead we use a **formula-relative transport argument**.

Fix a mixed formula \(\Phi\). Close the finite set of target linear templates occurring in \(\Phi\) under the finite linear consequences and fixed-depth projection conditions needed by the target normal form. Choose \(K_\Phi\) deep enough for every valuation template in this closure, and enlarge a finite set \(F_\Phi\) to contain all coefficient exceptions and all finite good-prime color classes.

Now let \(\sigma\) be any permutation of primes satisfying:

* \(\sigma\) fixes \(F_\Phi\);
* \(\sigma\) fixes non-good primes (they may simply be left pointwise fixed);
* on good primes outside \(F_\Phi\), \(\sigma\) preserves \(c_{K_\Phi}\).

The permutation extends canonically to an automorphism of the pure multiplicative source monoid by permuting prime coordinates and preserving exponents.

What remains is to transport target witnesses.

### Target-witness transport lemma

Suppose a finite tuple of target parameters has already been transported so that every target template in the finite closure has the same truth value after applying \(\sigma\) to all prime arguments. For any additional target witness \(y\), there exists a witness \(y'\) extending this finite-fragment equivalence.

There are two cases.

#### Pinned case

If some relevant exact equation with non-zero coefficient of \(y\) holds, then \(y\) is pinned to a rational affine combination of the already named target parameters and a uniformly bounded set of prime labels. Transport the finite prime tuple by \(\sigma\) and solve the same affine equation for \(y'\).

Consistency of all other pinning equations is preserved because subtracting two such equations produces one of the finitely many homogeneous linear templates already controlled by exact linear separation. Any new unintended exact incidence on the transported side would, after subtraction from a pinning equation, yield a forbidden homogeneous relation; applying \(\sigma^{-1}\) would produce the corresponding unintended incidence on the original side.

#### Free case

If no exact equation pins \(y\), the valuation literals cut out a non-empty finite Boolean cell in the chain of 13-adic cosets. The corresponding transported cell is non-empty by the target finite-depth normal form and preservation of its finite projection conditions.

We must also avoid all unwanted exact equations indexed by prime tuples. Every such equation would force \(y'\) to be an affine combination of:

* the already fixed target parameters;
* at most \(r\) prime labels, where \(r\) depends only on the formula;
* fixed rational coefficients.

Choose inside the required 13-adic cell a rational whose denominator contains more than \(r\) fresh non-13 primes outside the denominator support of the already fixed parameters and coefficient set. Such a rational exists in every non-empty fixed-depth coset: if \(a\) is one point of the coset, take

\[
y'=a+\frac{13^M}{D},
\]

with \(M\) deep enough and \(D\) a product of sufficiently many fresh primes. None of these fresh denominator primes can be cancelled by an affine combination involving only \(r\) prime labels. Therefore all unwanted exact incidences are avoided simultaneously.

Thus target witnesses can always be transported for the finite fragment relevant to \(\Phi\).

---

## 7. Mixed Quantifier Compression / formula-relative tail symmetry

Induct on the syntax of \(\Phi\).

* Boolean connectives are immediate.
* For a source existential witness \(n\), use \(\sigma(n)\). Multiplication and all source equations are preserved because \(\sigma\) is a prime-coordinate permutation.
* For a target existential witness, apply the target-witness transport lemma above.
* Universal quantifiers follow by negation.

Therefore, for every mixed formula \(\Phi(\bar p)\) with free good-prime variables, there exist \(K_\Phi\) and finite \(F_\Phi\) such that

\[
\Phi(\bar p)\iff\Phi(\sigma(\bar p))
\]

for every color-preserving permutation \(\sigma\) of the good-prime tail fixing \(F_\Phi\) and the non-good primes.

This is the precise theorem needed by the programme. It is **formula-relative tail symmetry**, not an automorphism statement about the full exact bridge structure.

---

## 8. Prime order and prime successor

### Prime order

A finite color partition of an infinite good-prime tail has an infinite color class. Swapping two distinct good primes in that class preserves every fixed defining formula by formula-relative tail symmetry, but reverses the truth value required by a strict linear order. Hence the standard prime order is not definable.

### Prime successor

Serre's theorem gives density zero for primes \(p\) with \(\tau(p)=0\). Hence there are infinitely many consecutive prime pairs in which both primes are good after removing any fixed finite exceptional set.

For a hypothetical successor-defining formula \(S(p,q)\), only finitely many ordered color pairs occur. One ordered pair of colors therefore occurs for infinitely many consecutive good-good pairs

\[
(p,q),\quad(p',q'),\ldots.
\]

Choose two such pairs and swap \(q\) with \(q'\) while fixing \(p\). Formula-relative tail symmetry gives

\[
S(p,q)\iff S(p,q'),
\]

but only \(q\) is the next prime after \(p\), contradiction.

Thus neither the standard prime order nor prime successor is first-order definable in \(\mathcal B_\Delta\).

---

## 9. Finite Grid-Isolation Rank

Fix an isolator formula \(I(p,q;r)\). Its formula-relative compression supplies finitely many prime colors, a finite exceptional set, and only bounded exact exceptions for the target traces appearing in \(I\).

After removing the finitely many exceptional rows, columns, and marker coincidences, two sufficiently many rows (or columns) have the same formula-relative type. A color-preserving permutation exchanging them while fixing the relevant column and marker preserves the truth value of \(I\), contradicting isolation of a single cell.

Therefore there exists a formula-dependent finite constant \(C(I)\) such that

\[
\operatorname{GIR}(I)\le C(I)<\infty.
\]

No universal numerical bound such as \(13^{2K_I}\) is claimed without further bookkeeping of equality patterns and bounded exact exceptions.

---

## 10. Interior status

The fixed-ball structure is strictly stronger than pure Skolem arithmetic because prime 13 is definable:

\[
p=13\iff \operatorname{Prime}(p)\land\exists x\bigl(U_\Delta(p,x)\land\neg B(x)\bigr).
\]

For every prime \(p\ne13\), \(u_p\in B\), while \(v_{13}(u_{13})=-11\).

At the same time, formula-relative tail symmetry gives:

\[
S_{\mathbb P},<_{\mathbb P}\notin\operatorname{Def}(\mathcal B_\Delta)
\]

and every fixed isolator has finite GIR.

Thus \(\mathcal B_\Delta\) is a rigorous fixed-ball interior candidate between pure prime-permutation symmetry and the previously established right-wall grid-amplification layers.

The statement does **not** claim decidability of the complete theory, non-interpretability of full arithmetic by every possible interpretation, or historical priority.
