# Reflections on the Prime-Status Corridor with Commander Sol
## From Exact Primehood without Order to Cardinality-Induced Arithmetic

**Status:** canonical English manuscript draft v0.1  
**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-30

## Abstract

We introduce a multiplicative quotient of the positive integers that preserves primality exactly while erasing almost all exponent information and all numerical ordering of the prime atoms. For

\[
\Xi(n)=\bigl(\operatorname{supp}(n),Q(n)\bigr),
\qquad
Q(n)=1\iff \exists p\;p^2\mid n,
\]

the induced product is

\[
(A,e)\star(B,d)
=
\bigl(A\cup B,e\vee d\vee[A\cap B\ne\varnothing]\bigr).
\]

The nonunit irreducibles are exactly the ordinary primes, but the automorphism group on prime atoms is the full symmetric group. We use this quotient as the left endpoint of a definability corridor. Fixed finite congruence phases break symmetry but do not recover prime order or prime successor. Explicit nonperiodic block relations break symmetry further while still leaving global order undefinable. Even a relation that differs from true prime successor on only finitely many edges may fail to define successor.

After true prime successor is added, the internal finite-support carrier makes the quotient effectively equivalent to weak monadic second-order logic of a labelled successor word. This identifies arithmetic residue phases, such as the mod-4 sequence of consecutive primes, with concrete infinite-word model-theory problems. We prove that maximal recurrence of all finite binary factors does not by itself force coordinate addition.

The main transition is a finite-carrier arithmetic jump. If coordinate addition of prime indices is available, finite support sets define coordinate divisibility, and classical results of Julia Robinson then yield multiplication. More geometrically, equality of cardinalities of two finite supports already defines coordinate addition by comparison of interval lengths. Hence order alone is tame, equicardinality alone is tame, but their combination interprets full arithmetic. Transferring a theorem of Alexis Bès gives an exact zero-one boundary for every pure support-cardinality synchronizer: it is either already weak-monadically definable from order, or it immediately yields addition and multiplication. For unary support-size predicates, ultimate periodicity is the exact boundary.

The resulting Prime-Status Corridor isolates a distinction between local phase information, global successor geometry, and cardinality synchronization, and provides a controlled framework in which exact primehood survives long before prime order or arithmetic reappear.

---

## 1. Introduction

A recurring theme in arithmetic model theory is that apparently modest structural information can preserve some arithmetic notions while destroying others. The present paper asks for a particularly sharp separation:

> Can one preserve the distinction prime/composite exactly while removing the coordinate order of the primes, and then identify the first kinds of additional structure that reconstruct order and arithmetic?

The construction below is deliberately much smaller than the full exponent vector of an integer. It retains only the set of prime divisors and one bit recording whether any prime has appeared with multiplicity at least two.

This turns out to be enough to preserve primality exactly, but not enough to distinguish the numerical locations of the primes. The resulting quotient therefore supplies a natural left wall for a definability corridor.

The paper is not a claim that prime supports, squarefree information, weak monadic logic, or cardinality relations are new. These are classical ingredients. The contribution is the combined corridor architecture and the derived transition theorems inside this quotient.

---

## 2. The Prime-Status Quotient

### Definition 2.1
For every positive integer `n`, define

\[
S(n)=\{p:p\mid n\}
\]

and

\[
Q(n)=
\begin{cases}
0,&n\text{ is squarefree},\\
1,&\exists p\;p^2\mid n.
\end{cases}
\]

Set

\[
\Xi(n)=(S(n),Q(n)).
\]

Let `P_0` be the image of `Xi`.

### Definition 2.2
For finite prime sets `A,B` and bits `e,d`, define

\[
(A,e)\star(B,d)
=
\left(A\cup B,
 e\vee d\vee[A\cap B\ne\varnothing]
\right).
\]

The state `(empty,1)` is omitted because it is not in the image of `Xi`.

### Proposition 2.3
For all positive integers `a,b`,

\[
\Xi(ab)=\Xi(a)\star\Xi(b).
\]

#### Proof
The support identity

\[
S(ab)=S(a)\cup S(b)
\]

is immediate. The product `ab` has a repeated prime factor iff a repeated factor was already present in `a`, or already present in `b`, or a prime occurs in both supports. This is exactly the Boolean rule in Definition 2.2. ∎

Thus `Xi` is a quotient homomorphism of the multiplicative monoid.

### Proposition 2.4 — Exact primality
For `n>1`,

\[
n\text{ is prime}
\iff
|S(n)|=1\land Q(n)=0.
\]

#### Proof
If `n=p` is prime, its support is `{p}` and it is squarefree. Conversely, suppose `|S(n)|=1`. Then `n=p^k` for some prime `p`. If additionally `Q(n)=0`, then `k=1`, so `n=p`. ∎

### Corollary 2.5
The nonunit irreducible elements of `P_0` are exactly the states

\[
(\{p\},0),
\]

i.e. the ordinary primes.

#### Proof
A singleton squarefree state cannot be written as the product of two nonunit states. Every squarefree composite support splits as a union of two nonempty proper supports, while

\[
(\{p\},1)
=(\{p\},0)\star(\{p\},0).
\]
∎

---

## 3. Complete prime symmetry

### Theorem 3.1
Every permutation

\[
\sigma:\mathbb P\to\mathbb P
\]

extends uniquely to an automorphism of `P_0` by

\[
(A,e)\mapsto(\sigma A,e).
\]

Conversely every automorphism of `P_0` induces a permutation of the prime atoms. Hence

\[
\operatorname{Aut}(\mathfrak P_0)
\cong
\operatorname{Sym}(\mathbb P).
\]

#### Proof
The product `star` depends only on union, intersection-nonemptiness, and the defect bits, all preserved by any permutation of prime labels. Conversely, automorphisms preserve the definable set of nonunit irreducibles, which is exactly the set of prime atoms. Since every quotient state is determined by its finite support and defect bit, the atom permutation determines the automorphism uniquely. ∎

### Corollary 3.2
The ordinary numerical order of primes and the ordinary prime-successor relation are not definable in `P_0`.

#### Proof
Any definable relation is automorphism invariant. A transposition of two prime atoms destroys numerical order and successor while preserving the quotient structure. ∎

This is the left wall of the corridor: exact primehood is present, but prime coordinates are absent.

---

## 4. Finite periodic phase does not recover order

Fix `M>=2`. For reduced residue classes `r mod M`, add unary colours

\[
C_r(p)\iff p\equiv r\pmod M,
\]

with the finitely many primes dividing `M` treated separately.

### Theorem 4.1 — Finite Phase Wall
Within each reduced residue class there are infinitely many primes. Therefore

\[
\operatorname{Aut}(\mathfrak P_M)
\supseteq
\prod_r\operatorname{Sym}(\mathbb P_r).
\]

In particular standard prime order and true prime successor remain undefinable.

#### Proof
Dirichlet's theorem gives infinitely many primes in each reduced residue class. Any permutation within each colour class preserves all unary colours and extends to the quotient by Theorem 3.1. Such a permutation can move a prime arbitrarily far in the numerical ordering, contradicting invariance of either standard order or true prime successor. ∎

The same argument applies to any fixed finite relational enrichment whose restriction to prime tuples factors through finitely many congruence classes modulo a fixed modulus.

---

## 5. Nonperiodic symmetry breaking without global order

For a fixed residue class `r`, enumerate its primes numerically:

\[
p_{r,1}<p_{r,2}<p_{r,3}<\cdots.
\]

Add the oriented-pair relation

\[
R_2(p_{r,2j-1},p_{r,2j}).
\]

This relation is not periodic in the numerical prime coordinate. It destroys arbitrary permutations of individual atoms. Nevertheless entire oriented pairs of the same colour remain freely permutable.

### Proposition 5.1
In the expansion by `R_2`, neither global prime order nor true prime successor is definable.

#### Proof
Choose two oriented pairs in one colour class and swap the pairs as blocks. This preserves the quotient, all residue colours, and `R_2`, but changes the numerical positions of the four prime atoms. Therefore neither numerical order nor true successor is invariant. ∎

Thus symmetry can be reduced strictly without restoring coordinate order.

---

## 6. Near-successor relations may still fail to define successor

Let `S` denote true prime successor. Choose two distant same-colour prime atoms `x,y`. Delete every `S`-edge incident with either `x` or `y`. At most four edges are removed.

### Theorem 6.1 — Finite-Injury Obstruction
There exists a relation `E` differing from true prime successor in at most four edges such that true prime successor is not definable from the quotient, the finite phase colours, and `E`.

#### Proof
After deletion, `x` and `y` become isolated with respect to `E`. Their transposition, fixing all other atoms, preserves `E`, the colours, and the quotient structure. True prime successor is not preserved. ∎

### Consequence
Density-one agreement with true successor is not a sufficient reconstruction criterion. The relevant resource is not merely edge density but global stitching.

---

## 7. Internal finite subsets

From this point it is convenient to work with odd primes, so the exceptional prime `2` is removed as a trivial parity layer.

### Lemma 7.1 — Squarefree carriers
The squarefree quotient elements form a definable copy of all finite subsets of prime atoms.

#### Proof
For any nonempty state `(A,e)`,

\[
(A,e)\star(A,e)=(A,1).
\]

Thus a nonempty state is squarefree iff it is not idempotent. The unit is handled separately. Every finite prime set `A` occurs as the squarefree state `(A,0)`. ∎

### Lemma 7.2 — Support equality
For quotient elements `x,y`,

\[
\operatorname{supp}(x)=\operatorname{supp}(y)
\iff
x\star x=y\star y.
\]

### Lemma 7.3 — Membership
For a prime atom `p` and squarefree carrier `X`, membership

\[
p\in X
\]

is first-order definable by requiring that adjoining `p` does not change support.

The quotient therefore contains an internal weak-monadic finite-set channel.

---

## 8. True successor yields a labelled weak-monadic word

Add true prime successor `S` on odd prime atoms and enumerate

\[
q_0=3,q_1=5,q_2=7,\ldots,
\qquad S(q_i,q_{i+1}).
\]

Optionally add finitely many unary colours `C_1,...,C_t`.

### Theorem 8.1 — Weak-Monadic Interpretation
The first-order theory of

\[
(\mathfrak P_0^{\rm odd};\star,S,C_1,\ldots,C_t)
\]

is effectively intertranslatable with weak monadic second-order logic over the labelled successor word

\[
(\mathbb N;\operatorname{Succ},C_1^w,\ldots,C_t^w).
\]

#### Proof
By Section 7, first-order quantification over squarefree quotient elements supplies quantification over arbitrary finite subsets of atom positions. Conversely every quotient element is represented by one finite set plus one Boolean defect tag. The operation `star` is definable from union, nonempty intersection, and the two tags. The successor and colours translate directly. ∎

### Corollary 8.2
With no extra colour word, the theory is decidable by classical WS1S.

### Lemma 8.3 — Order becomes definable
The successor order on atom indices is first-order definable in the quotient with `S`.

#### Proof
For atoms `x,y`, require the existence of a finite carrier containing both such that every included atom other than `y` has its successor also included. If `x<=y`, the finite interval is a witness. If `x>y`, closure from `x` can never terminate at `y`, so any witness would be infinite. ∎

Thus prime order reappears before arithmetic does.

---

## 9. The mod-4 prime word as a number-theoretic frontier

Define the binary word

\[
w_4(n)=
\begin{cases}
0,&q_n\equiv1\pmod4,\\
1,&q_n\equiv3\pmod4.
\end{cases}
\]

For every finite binary word `u`, the property that `u` occurs beginning at a position is first-order definable in the labelled successor chain.

### Theorem 9.1 — Recurrence-query lower bound
If the weak monadic theory of `w_4` is decidable, then there is an algorithm which decides, for every finite binary word `u`, whether `u` occurs infinitely often in `w_4`.

#### Proof
Construct a formula `Occ_u(y)` saying that the block beginning at `y` is `u`, and form

\[
\forall x\exists y\,(x<y\land Occ_u(y)).
\]

This sentence is true exactly when `u` occurs arbitrarily far out. ∎

Shiu's theorem supplies arbitrarily long monochromatic runs in each reduced residue class, but the general recurrence spectrum of prescribed mixed residue patterns remains beyond current unconditional prime-distribution theory. The theorem above is therefore a barrier statement, not an undecidability proof.

---

## 10. Finite-Carrier Arithmetic Jump

Define coordinate addition on atoms by

\[
\operatorname{Add}_{idx}(q_i,q_j,q_k)
\iff i+j=k.
\]

### Theorem 10.1
In

\[
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{Add}_{idx}),
\]

coordinate divisibility is first-order definable.

#### Proof
Let `q_0` denote coordinate zero. For `a>0`, define `a|b` by existence of a finite carrier `X` such that:

1. `q_0 in X` and `q_b in X`;
2. every element of `X` is at most `q_b`;
3. whenever `q_t in X` and `t<b`, the atom `q_{t+a}` is also in `X`.

If `a|b`, choose the finite progression

\[
\{q_0,q_a,q_{2a},\ldots,q_b\}.
\]

Conversely closure from `0` forces every multiple of `a` until the bound `b`. If `b` is not a multiple of `a`, the last forced multiple below `b` forces the next one above `b`, contradiction. The case `a=0` is handled separately by `0|b iff b=0`. ∎

### Theorem 10.2 — Arithmetic Jump
Coordinate multiplication is definable, and the complete theory of the expansion is undecidable.

#### Proof
Julia Robinson proved that addition and multiplication are first-order definable from successor and divisibility on the natural numbers. Apply the fixed defining formulas to the atom-index copy. Thus ordinary first-order arithmetic is interpreted. ∎

### Corollary 10.3
Coordinate addition is not definable in the uncoloured successor layer `P_0+S`, because that layer has decidable WS1S theory.

---

## 11. Maximal local recurrence is insufficient

For each `n>=1`, let `B_n` be the concatenation, in lexicographic order, of all binary words of lengths at most `n`, and define

\[
w_*=B_1B_2B_3\cdots.
\]

Every finite binary word occurs explicitly inside every sufficiently large block `B_n`, hence infinitely often in `w_*`.

### Theorem 11.1 — Maximal-Recurrence Separation
There exists a computable binary word in which every finite binary word occurs infinitely often, but coordinate addition is not weak-monadically definable.

#### Proof
The word `w_*` is computable. Its recurrence indicator for regular factor languages is recursive: an empty regular language contributes no recurrent factor; a nonempty regular language contains some finite word, and every such word occurs infinitely often. By Semenov's criterion the MSO theory of `w_*` is decidable. If coordinate addition were definable, Theorem 10.2 would interpret full arithmetic and contradict decidability. ∎

Thus

\[
\boxed{
\text{maximal finite-pattern recurrence}
\not\Rightarrow
\text{coordinate addition}.
}
\]

The missing resource is some form of global synchronization, not merely local factor richness.

---

## 12. Equinumerosity as a primitive synchronizer

Add a relation on finite squarefree carriers:

\[
\operatorname{EqCard}(X,Y)
\iff |X|=|Y|.
\]

### Theorem 12.1 — Equinumerosity Synchronization
In

\[
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{EqCard}),
\]

coordinate addition is first-order definable.

#### Proof
For atoms `a<=b`, let `Interval(a,b,X)` state that `X` is exactly the set of atoms in the half-open interval `[a,b)`.

For

\[
x=q_i,\qquad y=q_j,\qquad z=q_k,
\]

we have

\[
|[x,z)|=k-i,
\qquad
|[q_0,y)|=j.
\]

Therefore

\[
i+j=k
\]

iff `x<=z` and there exist finite carriers `X,Y` coding those two intervals with

\[
\operatorname{EqCard}(X,Y).
\]
∎

### Corollary 12.2

\[
\operatorname{EqCard}
\Longrightarrow
\operatorname{Add}_{idx}
\Longrightarrow
\operatorname{Div}_{idx}
\Longrightarrow
\operatorname{Mul}_{idx}.
\]

Hence the EqCard expansion interprets full arithmetic.

---

## 13. Two tame ingredients, wild together

### Proposition 13.1
`P_0+S` is decidable.

This is Corollary 8.2.

### Proposition 13.2
The order-free structure `P_0+EqCard` is decidable.

#### Justification
Feferman and Vaught proved decidability of weak monadic logic of pure equality with equicardinality of finite sets. The Prime-Status operation on finite supports is definable from Boolean set operations and one finite defect tag, so the quotient is interpretable in that decidable setting.

### Theorem 13.3 — Interaction Law

\[
\boxed{
\text{order alone tame; EqCard alone tame; order+EqCard wild}.
}
\]

This is not a paradox: order converts cardinality equality into equality of interval lengths, which is exactly coordinate translation.

---

## 14. Zero-one boundary for pure cardinality synchronizers

Let `R(X_1,...,X_n)` depend only on

\[
(|X_1|,\ldots,|X_n|).
\]

Such an `R` is called a pure cardinality synchronizer.

Alexis Bès proved for WMSO over `(N,<)` that if such a relation is not already definable in the base weak-monadic order structure, then both addition and multiplication are definable in the expansion.

### Theorem 14.1 — Transferred Cardinality Dichotomy
For every pure cardinality synchronizer `R` on Prime-Status finite carriers, exactly one of the following holds:

1. `R` is already definable in the successor/order Prime-Status layer, hence adds no definability power and preserves decidability;
2. `R` defines coordinate addition and coordinate multiplication, hence the expansion is undecidable.

#### Proof
By Theorem 8.1 the Prime-Status successor structure supplies exactly the weak-monadic finite-set variables over the ordered atom positions. Apply Bès's theorem and translate the resulting coordinate relations back to the atom sort. ∎

### Corollary 14.2 — Unary wall
For a unary support-size predicate

\[
R_A(X)\iff |X|\in A,
\]

we are in the tame case iff `A` is ultimately periodic.

Thus parity and fixed congruence conditions on support size are tame, while support-size primality, squareness, powers of two, or any other non-ultimately-periodic unary size law cause arithmetic collapse.

This should be contrasted with unary colours on positions: a nonperiodic position word may still have decidable monadic theory. The location of the nonperiodicity is therefore decisive.

---

## 15. Discussion

The corridor separates several resources that are often conflated.

### 15.1 Exact primehood is very cheap
One support set plus one square-defect bit is enough to distinguish every prime from every composite.

### 15.2 Prime order is much more expensive
Finite residue phases and even explicit nonperiodic local block relations leave substantial automorphism groups.

### 15.3 Successor is not yet arithmetic
Once true successor is supplied, order becomes definable because finite supports can store finite paths, but the uncoloured structure remains WS1S-decidable.

### 15.4 Local recurrence is not global synchronization
Even maximal recurrence of every finite binary block can coexist with decidable MSO and failure of coordinate addition.

### 15.5 Cardinality comparison is a geometric translation operator
EqCard does not explicitly mention addition. Nevertheless order turns equality of finite support lengths into translation equality of intervals, which is coordinate addition.

This provides the cleanest transition found in the present work.

---

## 16. Limitations and open problems

The paper deliberately leaves the following questions open:

1. What is the exact monadic theory of the prime-residue word `w_4`?
2. Does `w_4` define coordinate addition?
3. What is the weakest non-cardinality synchronizer that defines coordinate addition?
4. Can one classify finite-injury successor reconstruction under stronger structural hypotheses?
5. Which sparse transport relations cause undecidability strictly before coordinate addition becomes definable?

None of these open problems is needed for the theorem package proved here.

---

## 17. Conclusion

The Prime-Status Quotient shows that exact prime/composite information can survive after all numerical prime coordinates have disappeared. From this highly symmetric left wall, one can reintroduce structure in controlled stages.

Finite periodic phase breaks symmetry but not order. Nonperiodic local relations break it further but still do not determine the coordinate chain. True successor restores order and weak-monadic finite-set geometry, yet remains decidable. Maximal local recurrence still does not force coordinate arithmetic.

The decisive transition occurs when finite intervals can be compared by cardinality. Equinumerosity turns ordered finite-support geometry into coordinate translation, yielding addition, divisibility, multiplication, and full arithmetic. Within the whole class of pure cardinality synchronizers, Bès's theorem makes this boundary exact.

The resulting corridor can therefore be summarized as

\[
\boxed{
\text{exact primehood}
\;<\;
\text{phase}
\;<\;
\text{order}
\;<\;
\text{cardinality synchronization}
\Longrightarrow
\text{arithmetic}.
}
\]

---

## References — verified core anchors

1. J. R. Büchi, *Weak second-order arithmetic and finite automata*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 6 (1960), 66-92.
2. S. Feferman and R. L. Vaught, classical work on generalized products and decidability, including the equicardinality result cited by Bès.
3. J. Robinson, *Definability and decision problems in arithmetic*, Journal of Symbolic Logic 14 (1949), 98-114.
4. D. K. L. Shiu, *Strings of Congruent Primes*, Journal of the London Mathematical Society 61 (2000), 359-373, DOI 10.1112/S0024610799007863.
5. A. Bès, *Expansions of MSO by cardinality relations*, Logical Methods in Computer Science 9(4:18) (2013), DOI 10.2168/LMCS-9(4:18)2013.
6. D. Kuske, J. Liu, A. Moskvina, *Infinite and Bi-infinite Words with Decidable Monadic Theories*, Logical Methods in Computer Science 14(3:9) (2018), DOI 10.23638/LMCS-14(3:9)2018.
7. Modern model-theoretic literature on Skolem arithmetic and prime permutations/support decomposition; exact bibliography to be finalized in v0.2 after the dedicated citation audit.
