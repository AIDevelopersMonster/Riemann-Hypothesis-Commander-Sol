# Prime-Status Corridor — Research State

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-29  
**Status:** active research; GitHub checkpoint reached; publication threshold not yet reached

## 1. Prime-Status Quotient

For `n>=1` let

\[
S(n)=\{p:p\mid n\},\qquad
Q(n)=1\iff \exists p\;p^2\mid n.
\]

Define

\[
\Xi(n)=(S(n),Q(n)).
\]

On pairs `(A,e)` put

\[
(A,e)\star(B,d)
=
(A\cup B,\; e\vee d\vee[A\cap B\ne\varnothing]).
\]

Then

\[
\Xi(ab)=\Xi(a)\star\Xi(b).
\]

Hence `Xi` is a quotient homomorphism of `(N_{>0},x)`.

Primehood is exact:

\[
n\text{ prime}\iff |S(n)|=1\land Q(n)=0.
\]

Thus the nonunit irreducibles of the quotient are exactly the ordinary primes.

Every permutation of the prime atoms extends uniquely to an automorphism of the quotient, so

\[
\operatorname{Aut}(\mathfrak P_0)\cong\operatorname{Sym}(\mathbb P).
\]

Therefore ordinary prime order and prime successor are not definable in `P_0`.

## 2. Finite periodic phase wall

For fixed `M`, enrich prime atoms by residue colors

\[
C_r(p)\iff p\equiv r\pmod M
\]

for reduced residue classes, treating primes dividing `M` separately if desired.

Dirichlet's theorem gives infinitely many atoms in every reduced class. Therefore

\[
\operatorname{Aut}(\mathfrak P_M)
\cong
\prod_r\operatorname{Sym}(\mathbb P_r)
\]

up to the finite exceptional atoms dividing `M`.

Consequently neither ordinary prime order nor prime successor is definable in any fixed finite periodic phase expansion of this form. The same automorphism argument applies to any finite relational expansion whose restrictions to prime tuples depend only on finitely many congruence classes modulo one fixed modulus.

## 3. First nonperiodic symmetry-breaking layer

Let the primes in one residue class be

\[
p_{r,1}<p_{r,2}<p_{r,3}<\cdots.
\]

Add the relation

\[
R_2(p_{r,2j-1},p_{r,2j}).
\]

This relation is nonperiodic with respect to the numerical coordinate and breaks arbitrary atom permutations to permutations of oriented two-element blocks. Yet blocks of the same color remain freely permutable, so ordinary prime order and prime successor remain undefinable.

This gives an explicit intermediate corridor:

\[
\mathfrak P_0 < \mathfrak P_M < (\mathfrak P_M;R_2)
\]

with strictly decreasing coordinate symmetry but still no `PrimeOrder` or `PSucc`.

## 4. Finite-injury obstruction near full successor

Let `S` denote true prime successor on the atom chain. Choose distinct same-color atoms `x,y` far apart and delete all successor edges incident with `x` and `y`. At most four edges are deleted. In the resulting reduct, the transposition `x<->y` is an automorphism while true successor is not invariant.

Hence a relation agreeing with true prime successor on all but finitely many edges need not define true prime successor.

The point is structural: edge density tending to one is not by itself a reconstruction criterion. A finite number of strategically placed cuts can preserve a residual automorphism obstruction.

No stronger general synchronization theorem is claimed here yet.

## 5. Exact successor-to-word reduction

Now enrich the Prime-Status Quotient by true prime successor `S` and, optionally, finitely many unary prime colors `C_1,...,C_t`.

Enumerate the prime atoms by successor:

\[
q_0,q_1,q_2,\ldots,
\qquad S(q_i,q_{i+1}).
\]

The color data define a fixed infinite word

\[
w(i)=(C_1(q_i),\ldots,C_t(q_i))\in\{0,1\}^t.
\]

### Theorem — effective mutual interpretation with a weak monadic word structure

The first-order theory of the Prime-Status structure

\[
(\mathfrak P_0;S,C_1,\ldots,C_t)
\]

is effectively mutually interpretable with weak monadic second-order logic over the labelled successor word

\[
(\mathbb N;\operatorname{Succ},C_1^w,\ldots,C_t^w),
\]

where second-order variables range over finite subsets of positions.

### Proof sketch with the required internal coding

1. Prime atoms are exactly the nonunit irreducibles of `P_0`, hence form a definable sort.
2. Every finite set `A` of prime atoms occurs as a squarefree quotient element `(A,0)`.
3. Support equality is definable because

   \[
   (A,e)\star(A,e)=(A,1)
   \]

   for nonempty `A`, so squaring erases only the defect bit while retaining support; the empty support/unit is handled separately.
4. Membership of a prime atom `p` in the support of a squarefree carrier `X` is definable by the support identity

   \[
   \operatorname{supp}(p\star X)=\operatorname{supp}(X).
   \]
5. Thus first-order quantification over quotient elements supplies quantification over all finite subsets of prime positions, exactly the weak monadic set channel.
6. Conversely, a quotient element `(A,e)` is represented in WMSO by a finite set `A` together with one Boolean tag `e`; the operation `star`, atomhood, successor, and colors are WMSO-definable from finite-set union/intersection and the tag.

Therefore decision/definability questions for the successor-enriched Prime-Status Quotient reduce exactly to the corresponding fixed-word monadic problem.

## 6. Consequence for uncoloured successor

With no extra color word, the structure reduces to weak monadic successor arithmetic `WS1S`, whose theory is decidable by the classical Büchi-Elgot-Trakhtenbrot automata method.

Hence adding the full abstract prime-successor chain to the Prime-Status Quotient does **not** by itself recover full first-order arithmetic.

However, because finite-set carriers are internal, successor reachability/order becomes definable by quantifying over a finite set containing the finite interval/path between two positions. Thus `PSucc` plus the finite-support carrier does recover the prime-index order while remaining in the decidable monadic-successor regime.

## 7. Arithmetic residue colors become a genuine infinite-word problem

For residue colors modulo `M`, define

\[
w_M(i)=q_i\bmod M.
\]

After successor is present, the old finite phase is no longer merely a partition with independent symmetric fibers: it is a labelled infinite word along the now-rigid successor coordinate.

Shiu's theorem (2000) proves arbitrarily long strings of consecutive primes in any fixed reduced residue class modulo `M`. Thus `w_M` contains arbitrarily long constant blocks in every reduced class. Together with Dirichlet's theorem this rules out eventual periodicity whenever there is more than one reduced residue class.

But non-eventual-periodicity does not imply undecidability of the monadic theory. Classical work on infinite words gives nonperiodic words with decidable monadic theories. Therefore no arithmetic-collapse claim is licensed at this point.

## 8. Current exact frontier

The next central problem is:

\[
\boxed{
\text{Determine the monadic theory of }w_M(i)=p_i\bmod M,
\text{ beginning with }M=4.
}
\]

Equivalently, for

\[
w_4(i)\in\{1,3\},
\]

ask whether the WMSO/MSO theory of the two-colour prime-successor word is decidable and which index relations it defines.

This is now the true barrier. The algebraic part has been reduced to a classical infinite-word model-theory question whose predicate is number-theoretic.

## 9. Publication gate

### GitHub checkpoint

**PASS.** The quotient construction, exact primehood preservation, finite-phase automorphism wall, nonperiodic block layer, finite-injury obstruction, and successor-to-labelled-word reduction form a stable research block worth preserving.

### Zenodo / paper checkpoint

**NOT YET.** Before publication the branch still needs:

1. a hostile proof audit of the mutual-interpretation theorem;
2. a dedicated literature/priority audit around Skolem arithmetic quotients, finite-set carriers, WS1S/WMSO word interpretations, and labelled prime-residue words;
3. resolution or sharp conditional classification of the `M=4` word frontier;
4. a precise statement separating coordinate addition on prime indices from arithmetic operations on finite-set encodings;
5. complete theorem proofs in the final manuscript (no theorem without proof).

## 10. Literature anchors already verified

- D. K. L. Shiu, *Strings of Congruent Primes*, Journal of the London Mathematical Society 61 (2000), 359-373, DOI 10.1112/S0024610799007863.
- Classical Büchi-Elgot-Trakhtenbrot decidability of weak monadic successor arithmetic.
- Semenov-type theory of decidability for monadic theories of fixed infinite words is the appropriate literature corridor for the next strike; it must be audited carefully before importing an exact criterion into the paper.
