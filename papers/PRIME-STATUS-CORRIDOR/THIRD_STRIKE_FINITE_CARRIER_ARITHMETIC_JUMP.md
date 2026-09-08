# Third Strike — Finite-Carrier Arithmetic Jump

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-29  
**Status:** theorem package proved; publication-significant

## 1. Setup

Work on the odd-prime Prime-Status Quotient

\[
\mathfrak P_0^{\rm odd}.
\]

Its elements are pairs `(A,e)`, where `A` is a finite set of odd prime atoms and `e in {0,1}` is the square-defect bit, with the impossible state `(empty,1)` omitted. The product is

\[
(A,e)\star(B,d)=
(A\cup B,\;e\vee d\vee[A\cap B\ne\varnothing]).
\]

Let `At(x)` denote the definable set of nonunit irreducibles. These are exactly the odd prime atoms.

Add true prime successor `S` on atoms and enumerate

\[
q_0=3,q_1=5,q_2=7,\ldots,
\qquad S(q_n,q_{n+1}).
\]

For atoms define the coordinate-addition relation

\[
\operatorname{Add}_{\rm idx}(q_i,q_j,q_k)
\iff i+j=k.
\]

The purpose of this strike is to determine the logical cost of adding this one relation.

---

## 2. Internal finite-set coding

### Lemma 2.1 — squarefree carriers are definable

For every nonempty element `x=(A,e)`,

\[
x\star x=(A,1).
\]

Hence `x` is squarefree exactly when either `x` is the unit or `x star x != x`.

Thus the squarefree elements form a definable copy of all finite subsets of the atom set.

### Lemma 2.2 — support equality is definable

For quotient elements `x,y`,

\[
\operatorname{supp}(x)=\operatorname{supp}(y)
\iff x\star x=y\star y,
\]

with the unit case included automatically.

Indeed squaring keeps the support and changes every nonempty defect bit to `1`.

### Lemma 2.3 — membership is definable

If `p` is an atom and `X` is a squarefree carrier, then

\[
p\in\operatorname{supp}(X)
\iff
(p\star X)\star(p\star X)=X\star X.
\]

The right-hand side says exactly that adjoining `p` does not change the support.

Therefore first-order quantification over squarefree quotient elements is exactly weak monadic quantification over finite sets of atom positions.

---

## 3. Successor already defines coordinate order

### Lemma 3.1

In `(P_0^odd; star,S)` the order of prime indices is definable.

### Proof

For atoms `x,y`, define `x <=_S y` iff there exists a squarefree carrier `X` such that

1. `x in X` and `y in X`;
2. for every atom `u in X` with `u != y`, there exists an atom `v in X` with `S(u,v)`.

If `x<=y` in the successor chain, the finite interval from `x` to `y` is a witness.

If `x>y`, any finite `X` containing `x` and satisfying successor-closure away from `y` would have to contain the infinite forward successor tail of `x`, impossible because `X` is finite.

Thus the formula defines the ordinary order of successor indices. QED.

The least atom

\[
z=q_0
\]

is therefore parameter-free definable as the unique atom with no `S`-predecessor.

---

## 4. Main theorem: coordinate addition is an arithmetic jump

### Theorem 4.1 — Finite-Carrier Arithmetic Jump

In the expansion

\[
\mathfrak A=
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{Add}_{\rm idx}),
\]

coordinate divisibility and coordinate multiplication are first-order definable on the atom sort. Consequently `Th(A)` is undecidable.

### Proof

Let `z=q_0` denote coordinate zero.

For atoms `x=q_a` and `y=q_b`, with `a>0`, define `Div_idx(x,y)` by existence of a squarefree finite carrier `X` satisfying:

1. `z in X`;
2. `y in X`;
3. every atom `t in X` satisfies `t <=_S y`;
4. whenever `t in X` and `t <_S y`, there exists `u in X` such that

   \[
   \operatorname{Add}_{\rm idx}(t,x,u).
   \]

For coordinate `a=0`, define divisibility separately by `0 | b` iff `b=0`.

We prove that for `a>0`, the displayed finite-carrier condition holds iff `a|b`.

If `a|b`, take

\[
X=\{q_0,q_a,q_{2a},\ldots,q_b\}.
\]

This is finite, bounded by `y`, contains `z,y`, and is closed under adding `a` below `b`.

Conversely suppose such a finite `X` exists. Since `q_0 in X`, closure forces `q_a in X`, then `q_{2a}`, and inductively every `q_{ka}` as long as `ka<b`. If `b` were not divisible by `a`, let `ka<b<(k+1)a`. Then `q_{ka} in X` and condition 4 forces `q_{(k+1)a} in X`, contradicting condition 3. Hence `a|b`.

So coordinate divisibility is definable.

Julia Robinson proved that multiplication is first-order definable from successor and divisibility on the natural numbers: both addition and multiplication can be defined in the language containing successor and `|`. Applying that fixed first-order definition to the atom-index copy gives a definable relation

\[
\operatorname{Mul}_{\rm idx}(q_a,q_b,q_c)
\iff ab=c.
\]

Hence the atom sort of `A` definably carries ordinary arithmetic `(N,S,+,x)`. The true first-order theory of ordinary arithmetic is undecidable. Therefore `Th(A)` is undecidable. QED.

### Classical dependency

Julia Robinson, *Definability and decision problems in arithmetic*, Journal of Symbolic Logic 14 (1949), 98–114. The paper explicitly proves definability of addition and multiplication from successor and divisibility.

---

## 5. Coordinate addition is not definable in the abstract-successor layer

### Corollary 5.1

`Add_idx` is not first-order definable in

\[
(\mathfrak P_0^{\rm odd};\star,S).
\]

### Proof

The base structure is effectively mutually interpretable with WS1S: weak monadic second-order logic of one successor. Its theory is decidable by the classical Buechi-Elgot automata theorem.

If `Add_idx` were definable in the base structure, Theorem 4.1 would make coordinate multiplication definable there as well, so the decidable base theory would interpret true first-order arithmetic and become undecidable. Contradiction. QED.

This gives a sharp distinction between two kinds of addition already noted in the earlier checkpoint:

- addition of numbers **encoded as finite binary support sets** is available inside WS1S;
- addition of the **positions themselves**, `i+j=k`, is not.

The finite-support carrier makes the latter relation dramatically stronger: once position addition is present, the same finite sets define divisibility and force multiplication.

---

## 6. General phase-word obstruction

Let `w` be any finite-alphabet infinite word on the successor positions and let

\[
\mathfrak P(w)
=(\mathfrak P_0^{\rm odd};\star,S,C_1,\ldots,C_t)
\]

be the corresponding finitely coloured Prime-Status structure.

### Theorem 6.1

If the weak monadic theory of the labelled word `(N,S,w)` is decidable, then `Add_idx` is not definable in `P(w)`.

### Proof

By the mutual interpretation already proved for the corridor, `Th(P(w))` is decidable whenever the weak monadic theory of `(N,S,w)` is decidable.

If `Add_idx` were definable in `P(w)`, Theorem 4.1 would define coordinate multiplication and interpret ordinary first-order arithmetic, contradicting decidability. QED.

A sufficient condition is decidability of the full MSO theory of `w`, since WMSO is a fragment of MSO.

---

## 7. Maximal finite-pattern recurrence still does not force addition

The preceding theorem can be combined with Semenov's criterion to answer the question left open after the second strike.

### Construction 7.1 — an explicit maximally recurrent computable word

For each `n>=1`, let `B_n` be the concatenation, in lexicographic order, of all binary words of lengths at most `n`. Define

\[
w_*=B_1B_2B_3\cdots.
\]

Then `w_*` is computable.

Every finite binary word `u` appears as one of the explicit blocks inside every `B_n` with `n>=|u|`. Therefore every finite binary word occurs infinitely often in `w_*`.

So `w_*` is disjunctive and recurrent with the maximal possible finite factor language

\[
F(w_*)=\{0,1\}^*.
\]

### Lemma 7.2 — the recurrence indicator is recursive

Semenov's indicator asks, for an effectively given regular language `L`, whether factors from `L` occur beyond every position, and otherwise for a cutoff after which none occur.

For `w_*` this is trivial:

- if `L` is empty, no such factor occurs;
- if `L` is nonempty, choose any `u in L`; since every finite word occurs infinitely often in `w_*`, factors from `L` occur beyond every position.

Emptiness of a regular language is decidable. Hence `w_*` has a recursive recurrence indicator.

By Semenov's characterization, because `w_*` is recursive and has a recursive recurrence indicator, its full MSO theory is decidable.

### Theorem 7.3 — Maximal Recurrence Separation

There exists a computable binary word in which **every finite binary pattern occurs infinitely often**, yet coordinate addition on positions is not WMSO-definable.

### Proof

Use `w_*`. By Lemma 7.2 and Semenov's theorem, its full MSO theory, hence its weak monadic theory, is decidable. Theorem 6.1 therefore excludes `Add_idx`. QED.

Thus

\[
\boxed{
\text{maximal finite-pattern recurrence}\not\Rightarrow
\text{coordinate addition}.
}
\]

The missing resource is not pattern richness. It must be some stronger global/effective alignment property.

### Semenov dependency

The criterion used here is the classical characterization: for a computable omega-word `(N,<=,P)`, decidability of its MSO theory is equivalent to the existence of a recursive indicator of recurrence. A modern verified source is:

D. Kuske, J. Liu, A. Moskvina, *Infinite and Bi-infinite Words with Decidable Monadic Theories*, Logical Methods in Computer Science 14(3:9), 2018, DOI `10.23638/LMCS-14(3:9)2018`, which states Semenov's criterion and compares it with later characterizations.

---

## 8. Consequence for the actual mod-4 prime word

Recall

\[
w_4(n)=q_n\bmod4\in\{1,3\}.
\]

The word `w_4` is computable because primes can be effectively enumerated.

### Corollary 8.1 — Necessary Non-Effective Recurrence Condition

If `Add_idx` is definable in the actual mod-4 Prime-Status successor structure

\[
(\mathfrak P_0^{\rm odd};\star,S,w_4),
\]

then `w_4` has **no recursive Semenov recurrence indicator**. In particular its full MSO theory is undecidable.

### Proof

Suppose `w_4` had a recursive recurrence indicator. Since `w_4` is computable, Semenov's theorem would imply decidability of its full MSO theory and therefore of its WMSO theory. Theorem 6.1 would then imply that `Add_idx` is not definable. Contradiction. QED.

This is a genuine necessary condition for arithmetic recovery from residue alignment.

It is much stronger than nonperiodicity or even the conjectural recurrence of every fixed finite residue pattern: Section 7 proves that complete finite-pattern recurrence can coexist with decidable MSO and failure of coordinate addition.

---

## 9. Revised corridor

The logical progression is now:

\[
\mathfrak P_0
\;<\;
\mathfrak P_M
\;<\;
\mathfrak P_M+R_2
\;<\;\cdots\;<\;
\mathfrak P_0+S
\;<\;
\mathfrak P_0+S+\operatorname{Add}_{\rm idx}.
\]

The endpoint jump is sharp in logical character:

- `P_0+S`: prime order available; finite-set carrier available; WS1S; decidable;
- `P_0+S+Add_idx`: divisibility definable; multiplication definable; ordinary arithmetic interpretable; undecidable.

For arithmetic colours such as `p mod 4`, the central question is no longer merely whether all residue patterns recur. The exact question is whether the labelled word supplies enough **global synchronization** to define position addition.

---

## 10. Publication assessment after the third strike

### Mathematical core

**PASS.** This strike supplies the missing structural theorem requested at the end of the second strike:

1. maximal finite-pattern recurrence alone does not recover coordinate addition;
2. coordinate addition is itself the arithmetic phase transition because the finite-set carrier upgrades it to divisibility and multiplication;
3. for the actual prime residue word, definability of addition would force non-effectivity of the Semenov recurrence indicator.

### Archival threshold

**PASS and committed to GitHub.**

### Zenodo threshold

**NOW CLOSE, BUT HOLD FOR ONE AUDIT CYCLE.**

Before authorizing a standalone publication, perform:

1. hostile proof audit of the finite-carrier divisibility formula and the WMSO mutual interpretation;
2. literature audit separating classical components (Skolem arithmetic prime permutations, radicals/squarefree supports, Buechi/WS1S, Semenov, Robinson) from the new combined Prime-Status Corridor theorem package;
3. consistency repair of earlier notes: wherever they suggested that coordinate addition might remain merely Presburger-tame in the finite-support structure, replace that with the Arithmetic Jump Theorem proved here.

No theorem should enter the final manuscript without its proof.
