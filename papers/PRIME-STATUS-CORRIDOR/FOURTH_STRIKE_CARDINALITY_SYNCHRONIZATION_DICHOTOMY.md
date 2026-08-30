# Fourth Strike — Cardinality Synchronization Dichotomy

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-30  
**Status:** theorem package proved; publication threshold reached

## 1. Question

The previous strike showed that coordinate addition on the prime-successor chain is an arithmetic jump:

\[
\operatorname{Add}_{\rm idx}
\Longrightarrow
\operatorname{Div}_{\rm idx}
\Longrightarrow
\operatorname{Mul}_{\rm idx}.
\]

The remaining question was whether there is a more primitive geometric/global synchronization relation, weaker in presentation than `Add_idx`, that already forces coordinate arithmetic when combined with the internal finite-support carrier.

The answer is yes.

The canonical synchronizer is **equinumerosity of finite supports**.

---

## 2. Setup

Work in the odd-prime Prime-Status Quotient with true prime successor:

\[
\mathfrak P_S=(\mathfrak P_0^{\rm odd};\star,S).
\]

The atom sort is

\[
q_0=3,q_1=5,q_2=7,\ldots,
\qquad S(q_i,q_{i+1}).
\]

Squarefree quotient elements are definable and represent exactly all finite subsets of the atom sort. Membership of an atom in a support is definable. The successor order `<=_S` is definable by finite-path closure.

For squarefree carriers `X,Y`, add the relation

\[
\operatorname{EqCard}(X,Y)
\iff
|\operatorname{supp}(X)|=|\operatorname{supp}(Y)|.
\]

This relation does not mention numerical prime coordinates. It compares only the sizes of two finite support-geometries.

---

## 3. The direct synchronization theorem

### Theorem 3.1 — Equinumerosity defines coordinate addition

In

\[
(\mathfrak P_0^{\rm odd};\star,S,\operatorname{EqCard}),
\]

the coordinate-addition relation

\[
\operatorname{Add}_{\rm idx}(q_i,q_j,q_k)
\iff i+j=k
\]

is first-order definable.

### Proof

Let `z0=q_0` be the least atom, definable as the unique atom with no `S`-predecessor.

For atoms `a,b` and a squarefree carrier `X`, define

\[
\operatorname{Interval}(a,b,X)
\]

to mean

\[
\forall u\bigl(\operatorname{At}(u)\to
[u\in X\leftrightarrow(a\le_S u\land u<_S b)]\bigr).
\]

Because the atom chain is discrete and `a<=b`, such an interval support is finite and therefore represented by a squarefree quotient element.

Now for atoms

\[
x=q_i,\qquad y=q_j,\qquad z=q_k,
\]

define `Add_idx(x,y,z)` by

\[
x\le_S z
\]

and the existence of squarefree carriers `X,Y` such that

\[
\operatorname{Interval}(x,z,X),
\qquad
\operatorname{Interval}(z_0,y,Y),
\qquad
\operatorname{EqCard}(X,Y).
\]

The first interval contains exactly

\[
k-i
\]

atoms, while the second contains exactly

\[
j
\]

atoms. Thus EqCard is equivalent to

\[
k-i=j,
\]

i.e.

\[
i+j=k.
\]

Therefore coordinate addition is definable. QED.

### Corollary 3.2 — Full arithmetic jump

By the Finite-Carrier Arithmetic Jump proved in the third strike,

\[
\operatorname{EqCard}
\Longrightarrow
\operatorname{Add}_{\rm idx}
\Longrightarrow
\operatorname{Div}_{\rm idx}
\Longrightarrow
\operatorname{Mul}_{\rm idx}.
\]

Hence the expansion interprets ordinary first-order arithmetic and its complete theory is undecidable.

---

## 4. Two safe ingredients, dangerous together

The point is sharper than the existence of one undecidable expansion.

### 4.1 Order without cardinality synchronization

The structure

\[
(\mathfrak P_0^{\rm odd};\star,S)
\]

is effectively mutually interpretable with WS1S, the weak monadic second-order theory of one successor, and is decidable.

### 4.2 Cardinality synchronization without order

Without `S`, the Prime-Status Quotient is the finite-subset carrier with one finite defect bit. Adding EqCard corresponds, up to this finite tag, to weak monadic logic of pure equality with equicardinality of finite sets.

Feferman and Vaught proved the corresponding theory without order decidable; Bès explicitly recalls this as decidability of `WMSO(N,EqCard)` without `<`.

Therefore the order-free Prime-Status + EqCard layer remains decidable.

### 4.3 Interaction

But together,

\[
\boxed{
\text{finite order geometry}
+
\text{finite-set equinumerosity}
\Longrightarrow
\text{full arithmetic}
}
\]

by Theorem 3.1 and Corollary 3.2.

Thus neither component is individually dangerous. The collapse is caused by their alignment.

This is an exact interaction law:

\[
\boxed{
\text{Order alone: tame}
\qquad
\text{EqCard alone: tame}
\qquad
\text{Order + EqCard: wild}.
}
\]

---

## 5. Exact zero-one theorem for pure cardinality synchronizers

The previous theorem has a complete generalization due to Alexis Bès.

Let `R(X_1,...,X_n)` be any relation on squarefree carriers depending only on support cardinalities. Thus there is

\[
I(R)\subseteq\mathbb N^n
\]

such that

\[
R(X_1,\ldots,X_n)
\iff
(|X_1|,\ldots,|X_n|)\in I(R).
\]

Call such an `R` a **pure cardinality synchronizer**.

### Classical theorem (Bès, transferred to the Prime-Status carrier)

For every pure cardinality synchronizer `R`, exactly one of the following holds.

#### Tame case

`R` is already definable in the weak monadic order structure.

Equivalently, `I(R)` is a recognizable subset of `N^n`: a finite union of products

\[
E_1\times\cdots\times E_n
\]

with every `E_i` ultimately periodic.

Adding `R` therefore does not enlarge the definability power of the successor Prime-Status layer and preserves decidability.

#### Wild case

`R` is not already definable in weak monadic order.

Then Bès proves that both

\[
+
\qquad\text{and}\qquad
\times
\]

are definable in the expansion.

Transferred through the Prime-Status finite-support interpretation, coordinate addition and multiplication of prime indices are definable.

Therefore:

\[
\boxed{
R\text{ pure cardinality}
\Rightarrow
\begin{cases}
R\text{ is already tame},\\
\text{or}\quad R\text{ collapses the corridor to full arithmetic.}
\end{cases}
}
\]

There is **no intermediate pure-cardinality phase**.

---

## 6. Unary specialization: periodicity is the exact wall

Suppose `R_A(X)` has the form

\[
R_A(X)\iff |X|\in A,
\qquad A\subseteq\mathbb N.
\]

Bès's criterion specializes to

\[
\boxed{
R_A\text{ is tame}
\iff
A\text{ is ultimately periodic}.
}
\]

Therefore:

### Safe examples

- `|X|` even;
- `|X| congruent to r mod m`;
- any finite Boolean combination of eventually periodic size conditions.

### Arithmetic-collapse examples

- `|X|` is prime;
- `|X|` is a square;
- `|X|` is a power of two;
- any non-ultimately-periodic unary size predicate.

The last point is particularly important. A unary predicate on **positions** such as powers of two can coexist with decidable MSO. The same pattern, when applied to **support cardinalities**, is wild.

Hence nonperiodicity itself is not the resource.

Its **geometric location** is the resource.

---

## 7. Contrast with the residue-word corridor

Earlier we proved that a nonperiodic arithmetic colour word

\[
w_M(n)=q_n\bmod M
\]

need not automatically define coordinate arithmetic. Indeed there are highly nonperiodic, even maximally recurrent, computable words with decidable monadic theory.

The present theorem shows the opposite behavior for support-cardinality predicates:

\[
\boxed{
\text{nonperiodic position colour can remain tame,}
}
\]

while

\[
\boxed{
\text{nonperiodic support-cardinality law is automatically wild.}
}
\]

This sharply separates two notions of phase information that previously looked superficially similar.

---

## 8. A still thinner undecidability synchronizer: cumulative drift

There is a second classical route to leaving the tame corridor before explicit coordinate addition appears.

Let `J subseteq N` be any infinite set and define

\[
c_J(n)=|J\cap[0,n)|,
\qquad
f_J(n)=n+c_J(n).
\]

Then

\[
f_J(n+1)-f_J(n)=1+[n\in J].
\]

So `f_J` is strictly increasing and has a jump larger than one exactly at the positions of `J`.

Wolfgang Thomas proved that weak monadic successor arithmetic expanded by a strictly monotone unary function `f` is undecidable whenever

\[
f(n+1)>f(n)+1
\]

for infinitely many `n`.

Therefore every infinite `J` yields

\[
\boxed{
\operatorname{WMSO}(\mathbb N,S,f_J)\text{ undecidable}.
}
\]

Transferred to prime atoms by

\[
F_J(q_n,q_{f_J(n)}),
\]

we obtain an `O(N)`-edge synchronization graph that already crosses the decidability wall.

The jump set can be arbitrarily sparse. For example choose

\[
J=\{2^k:k\ge0\}.
\]

Then

\[
f_J(n)=n+O(\log n),
\]

so the total drift from the identity is only logarithmic, yet the weak monadic theory is undecidable.

This gives a second structural lesson:

\[
\boxed{
\text{sparse local events can be tame as colours, but wild after cumulative integration.}
}
\]

No claim is made here that such a cumulative-drift map necessarily defines `Add_idx`; Thomas's theorem supplies undecidability. Thus the decidability threshold can occur strictly before the explicit addition threshold is identified.

---

## 9. Revised synchronization spectrum

The corridor now contains three conceptually different thresholds.

### Layer A — local / periodic memory

Examples:

- residue colours modulo fixed `M` without successor alignment;
- ultimately periodic support-cardinality predicates.

Status: tame.

### Layer B — global synchronization without explicit addition

Examples:

- cumulative transport maps `f_J` with infinitely many sparse jumps.

Status: weak monadic theory already undecidable by Thomas.

Whether a particular such relation defines `Add_idx` is a finer question and is not assumed.

### Layer C — length comparison / nontrivial cardinality law

Examples:

- EqCard;
- any pure cardinality relation outside the Bès-recognizable class.

Status:

\[
\boxed{\text{coordinate }+\text{ and }\times\text{ definable}.}
\]

Thus the first **proved sufficient geometric synchronizer for coordinate addition** is equinumerosity of finite supports.

Within the class of pure cardinality synchronizers, Bès's theorem makes this boundary exact: every genuinely new cardinality law already collapses to full arithmetic.

---

## 10. Literature boundary

The following components are classical and must be cited as such in any final paper:

1. Büchi-Elgot-Trakhtenbrot decidability of WS1S;
2. Feferman-Vaught decidability of the order-free equicardinality setting;
3. Raphael M. Robinson / later monadic-successor-extension literature for doubling-type undecidability;
4. Wolfgang Thomas, *A note on undecidable extensions of monadic second order successor arithmetic*, Archiv fuer mathematische Logik 17 (1975), 43-44;
5. Alexis Bès, *Expansions of MSO by cardinality relations*, Logical Methods in Computer Science 9(4:18), 2013, DOI 10.2168/LMCS-9(4:18)2013.

The Bès theorem already contains the abstract WMSO cardinality dichotomy. The new contribution of this programme is therefore **not** that abstract logical theorem.

The programme contribution is the identification and proof of its role inside the Prime-Status Quotient corridor, together with:

- exact preservation of prime/composite under the one-bit quotient;
- complete prime-atom symmetry at the left wall;
- finite-periodic phase wall;
- nonperiodic block symmetry-breaking layers;
- finite-injury near-successor obstruction;
- exact reduction of successor-enriched quotients to labelled weak monadic words;
- the mod-4 prime-residue recurrence barrier;
- the finite-carrier arithmetic jump;
- maximal-recurrence separation;
- and the present order-cardinality interaction law.

Novelty claims must be restricted to this combined architecture and its derived corridor theorems.

---

## 11. Publication decision after the fourth strike

### Mathematical completeness

**PASS.** The central question left by the third strike now has a strong answer.

A primitive geometric relation exists that forces coordinate arithmetic:

\[
\boxed{
\text{equality of finite support lengths}.
}
\]

Moreover the entire class of pure cardinality synchronizers has an exact tame/wild dichotomy by transfer of Bès's theorem.

### Research continuation

Further work remains possible, especially the exact definability strength of cumulative-drift functions such as doubling. However this is now a sequel-level refinement, not a missing piece of the present Prime-Status Corridor.

### Publication threshold

\[
\boxed{\text{REACHED}.}
\]

The branch is now strong enough for standalone manuscript assembly after one final hostile consistency audit across all four strikes.
