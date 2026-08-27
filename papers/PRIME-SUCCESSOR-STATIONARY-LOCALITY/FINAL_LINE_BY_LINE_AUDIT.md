# Final Line-by-Line Proof Audit

**Date:** 2026-08-26  
**Target:** `FINITE_STATIONARY_LOCALITY_THEOREM.md` and publication manuscripts  
**Verdict:** PASS AFTER LOCAL REPAIRS

This audit treats every proof step as untrusted until rechecked. No external review verdict is used as evidence.

## 1. Structure and hypotheses

**PASS with one precision repair.**

The bridge assumptions must state not only that bridge inputs are prime, but that on prime atoms the bridge is the graph of the label map:

\[
U(p,x)\iff \operatorname{Prime}(p)\land x=u_p.
\]

The theorem uses this functionality in the mixed-quantifier induction.

The finite exceptional prime set is allowed to absorb:

- primes in the stationary atlas `S`;
- coefficient-dependent private places;
- private places meeting denominators of finitely many rational target parameters/current target coordinates;
- finitely many small arithmetic exceptions.

## 2. Fixed-depth predicates

**PASS.**

For fixed `m>0`,

\[
B_{\ell,m}(x)\iff \exists y\,(\ell^m y=x\land B_\ell(y)),
\]

and

\[
B_{\ell,-m}(x)\iff B_\ell(\ell^m x).
\]

Only fixed depths are definable this way; no variable-depth predicate is introduced.

## 3. Local Coverage Lemma

**PASS with notation repair.**

When a positive base ball

\[
P=a+B_{\ell,m}
\]

is present, discard forbidden balls disjoint from `P`; if a forbidden ball contains `P`, the cell is empty. The depth

\[
N=\max n_i
\]

must be taken only over the remaining proper forbidden subballs. If there are none, the cell is nonempty.

Coverage is decided in

\[
B_{\ell,m}/B_{\ell,N},
\qquad
|B_{\ell,m}/B_{\ell,N}|=\ell^{N-m}.
\]

The finite incidence pattern is expressible by Boolean combinations of fixed-depth center relations

\[
a-b_i\in B_{\ell,k},\qquad b_i-b_j\in B_{\ell,k}.
\]

If no positive base ball exists, finitely many forbidden balls do not cover `Q`: choose a rational of sufficiently negative `\ell`-valuation.

## 4. Multi-Place Target Normal Form

**PASS.**

After DNF, eliminate one target variable `y`.

- If an exact equation with nonzero `y`-coefficient occurs, substitute the unique value of `y`.
- Literals with zero `y`-coefficient remain as constraints on the other variables.
- At each fixed place, positive balls reduce to one deepest compatible base ball; negative balls are handled by the local coverage lemma.
- The resulting local sets are nonempty open subsets of `Q_\ell`.
- For finite `S`, weak approximation / CRT after clearing denominators produces a rational point satisfying all local requirements simultaneously.
- Finitely many exact inequalities remove finitely many points and cannot destroy a nonempty local cell.

Therefore every target formula is a Boolean combination of exact rational linear equations and fixed-depth local conditions.

## 5. Generic Multi-Place Cell

**PASS with one repair concerning exact inequalities.**

For a cell consisting only of fixed-depth local literals, choose a point `a` and depths `M_\ell` deeper than every local boundary. Then

\[
a+H_{\mathbf M},\qquad H_{\mathbf M}=\bigcap_{\ell\in S}B_{\ell,M_\ell},
\]

lies in the cell.

If finitely many exact inequalities `y\ne c_j` are also present, choose the refinement deeper still so that every excluded point stays outside the refinement coset. For nonempty `S`, it suffices to fix one place `\ell_0\in S` and require

\[
M_{\ell_0}>\max_j v_{\ell_0}(a-c_j).
\]

The publication theorem is stated for a nonempty stationary atlas. The empty-atlas additive case can be handled separately and is not needed for the multi-local result.

## 6. Exact Linear Separation

**PASS.**

After clearing rational coefficient denominators, group equal regular primes. For a regular-prime block with nonzero aggregate coefficient `d`, exclude the finitely many regular primes for which the private place divides `d`. At every remaining private place, the corresponding term has negative valuation while all other regular labels and defect labels are integral. Cancellation is impossible.

Hence homogeneous exact relations on the regular tail depend only on equality patterns and fixed defect-label relations.

## 7. Reduced Affine-Fiber / Bounded-Anchor Cylinder Lemma

**PASS.**

The older bounded-tuple formulation is false because zero-sum equality blocks can move freely. The repaired statement is correct.

For a fixed equality pattern, remove blocks with zero aggregate coefficient. If two assignments solve the same reduced affine equation, subtraction gives a homogeneous relation. Exact Linear Separation implies that every regular prime in the second solution already occurs among the finitely many regular primes of the first solution. Thus the nonzero blocks have uniformly bounded assignments; a crude `m^m` bound suffices.

Exact traces are therefore finite unions of bounded-anchor cylinders, not finite sets of tuples.

## 8. Fresh-Private-Place Avoidance

**PASS after an important support repair.**

The fresh private places must be chosen outside the denominator support of **all finite current rational data**, including:

- stationary places `S`;
- fixed rational coefficients;
- external target parameters;
- every current target coordinate;
- the chosen center `a` of the refinement cell;
- labels of finitely many exceptional fixed source primes.

Because the regular reservoir is infinite and `\lambda` is injective, this excludes only finitely many private places.

Choose `r+1` regular primes `t_j` with private places `q_j=\lambda(t_j)` and set

\[
D=\prod_{j=1}^{r+1}q_j,
\qquad
L=\prod_{\ell\in S}\ell^{N_\ell},
\qquad
y=a+L/D.
\]

Then `y` stays in the required multi-place cell and, because `a` is `q_j`-integral,

\[
v_{q_j}(y)=-1.
\]

Every forbidden affine value uses at most `r` prime labels, so at least one `t_k` is absent. At `q_k` all terms in the forbidden affine value are integral, while `y` is not. Equality is impossible.

## 9. Coefficient-Adjusted Color Depth

**NEW EXPLICIT LEMMA - REQUIRED FOR PUBLICATION.**

A vague instruction to choose `K_{\Phi,\ell}` “large enough” is replaced by an explicit bound.

Consider a finite local template

\[
L=\alpha+\sum_i a_i u_{p_i}
\]

tested by

\[
L\in B_{\ell,m}.
\]

If `p_i` and `p_i'` have the same `B_{\ell,K}` color, then

\[
v_\ell(u_{p_i}-u_{p_i'})\ge K.
\]

Therefore

\[
v_\ell\left(\sum_i a_i(u_{p_i}-u_{p_i'})\right)
\ge \min_i\bigl(v_\ell(a_i)+K\bigr).
\]

It is enough to require

\[
K\ge \max_i\{m-v_\ell(a_i)\}.
\]

Taking the maximum over the finite template closure and also `K\ge0` makes every local truth value invariant under color-preserving prime substitutions.

Hence the number of regular colors is finite:

\[
\prod_{\ell\in S}\ell^{K_{\Phi,\ell}}.
\]

## 10. Pinned Target-Witness Transport

**PASS.**

A true equation

\[
ay+t=0,\qquad a\ne0,
\]

pins `y`. Transport the source prime coordinates in `t` and solve the transported equation.

For simultaneous pins, compatibility is equivalent to `y`-free exact consequences such as

\[
a_2t_1-a_1t_2=0.
\]

The finite template closure is explicitly closed under these consequences.

## 11. Free Target-Witness Transport

**PASS after Sections 5, 8, and 9.**

The transported local literals have the same truth pattern by the coefficient-adjusted color lemma. They determine a nonempty multi-place cell. Refine it to a full coset avoiding any finite exact point exclusions. Fresh-Private-Place Avoidance then selects a witness in the cell avoiding all unwanted exact affine incidences simultaneously.

## 12. Mixed Quantifiers

**PASS after strengthening the proof into finite-fragment back-and-forth.**

The final proof should not merely say “induct on syntax”. For the finite syntactic closure attached to `\Phi`, define a relation between two states consisting of:

- the source tuple and its image under the multiplicative automorphism induced by `\sigma`;
- the current target tuple and its transported target tuple;
- preservation of all exact and fixed-depth target templates in the finite closure;
- preservation of bridge incidences.

Then prove:

1. source forth/back: a source witness `n` is transported to `\sigma(n)` (and backward by `\sigma^{-1}`);
2. target forth/back: use pinned/free target-witness transport;
3. atomic and Boolean formulas are preserved.

Standard finite-fragment induction then proves preservation of every subformula of `\Phi`.

This removes any hidden circularity in the target-witness argument.

## 13. Prime order

**PASS.**

The regular tail is infinite and has only finitely many formula-relative colors. One color class contains two distinct regular primes. Swapping them is admissible and contradicts asymmetry of any formula claiming to define standard strict prime order.

## 14. Prime successor

**PASS.**

There are infinitely many consecutive prime pairs outside any fixed finite exceptional set and only finitely many ordered movable-class pairs. One ordered pair of classes occurs infinitely often, hence for two disjoint consecutive pairs. Swapping their second elements preserves an alleged successor formula but destroys ordinary succession.

No density theorem for possible Ramanujan zero primes is used in this contradiction.

## 15. Finite GIR

**PASS with a more explicit pigeonhole threshold.**

For a fixed isolator `I`, Formula-Relative Tail Symmetry gives finitely many movable classes plus a finite exceptional set. In a sufficiently large row family some movable class contains at least four rows. For a chosen column and cell marker, at most two of those rows can coincide with the fixed column or marker. Choose two other rows in the class and swap them while fixing the selected column and marker. The same marker would then isolate two cells in that column, contradiction.

Thus `GIR(I)<\infty`. No universal formula-independent numerical bound is claimed.

## 16. Ramanujan specialization

**PASS.**

For

\[
u_p=\frac{\tau(p)^2-p^{11}}{p^{11}},
\]

fixed stationary places are integral away from `p`. For good primes `p\ge5` with `\tau(p)\ne0`, Deligne's estimate gives `v_p(\tau(p))\le5`, hence

\[
v_p(u_p)=2v_p(\tau(p))-11<0,
\]

and for `q\ne p`, `v_p(u_q)\ge0`. Thus `\lambda(p)=p`.

If `\tau(p)=0`, then `u_p=-1`, giving one exact defect class.

An infinite reservoir of good primes follows without a zero-density theorem from Ramanujan's congruence

\[
\tau(p)\equiv1+p^{11}\pmod{691}
\]

and Dirichlet's theorem: every prime `p\equiv1 (mod 691)` satisfies `\tau(p)\equiv2 (mod 691)` and is therefore good.

## 17. Infinite named atlas

**PASS for the Ramanujan bridge.**

A first-order formula in the language with separately named predicates `(B_\ell)_{\ell\in\mathbb P}` mentions only finitely many place symbols. Apply the finite theorem to that syntactic support. This is a formula-by-formula result, not a global automorphism theorem.

## 18. Uniformly indexed atlas

**STATUS: OPEN BOUNDARY, correctly separated from the theorem.**

With a relation

\[
\mathsf B(\ell,x)\iff v_\ell(x)\ge0
\]

and a variable place coordinate, the finite syntactic-support argument no longer applies. The formula

\[
\forall\ell\,(\operatorname{Prime}(\ell)\to\mathsf B(\ell,x))
\]

defines `Z` inside `Q`. The current paper makes no claim that this yields infinite GIR, prime successor, or full arithmetic.

## 19. Bibliographic claims

**PASS after verification.**

- Baur, *Elimination of quantifiers for modules*, Israel J. Math. 25 (1976), 64-70, DOI 10.1007/BF02756561.
- Fisher, *Abelian structures. I*, LNM 616 (1977), 270-322.
- Stonestrom, *Some model theory of Th(N,·)*, Math. Log. Quart. 68 (2022), 288-303, DOI 10.1002/malq.202100049.
- Ramanujan congruence `\tau(n)\equiv\sigma_{11}(n) (mod 691)` is classical and independently verified before publication.

## 20. Final verdict

After the repairs above, no surviving line of the proof requires:

- a finite quotient `Q/H_m`;
- a bounded number of complete affine tuples;
- a density theorem for Ramanujan zero primes;
- a global automorphism theorem;
- classical stability/NIP;
- a finite-versus-infinite named-atlas phase transition.

The proof architecture closes as

\[
\text{Target finite-depth normal form}
\Rightarrow
\text{coefficient-adjusted finite colors}
\Rightarrow
\text{private-place exact separation}
\Rightarrow
\text{pinned/free witness transport}
\Rightarrow
\text{finite-fragment back-and-forth}
\Rightarrow
\text{Formula-Relative Tail Symmetry}.
\]

**Publication status after incorporation of these local repairs: theorem-ready.**
