# Regular-Primitive Barrier and Closure Placement

**Project:** FCOA Admissibility Geometry  
**Status:** audited theorem in stated scope  
**Scope:** post-U1 / post-head-synchronization Arithmetic Leakage programme

## 1. Central question

The synchronized-head construction shows that

\[
\operatorname{EqGap}(a,b;c,d)
\iff
(a,c)\Rightarrow^*(b,d),
\]

where \(\Rightarrow\) is the local product-successor step.

Can the unbounded closure be eliminated and the same memory obtained from finitely many ordinary weak FCOA partial operations alone?

Within the natural local/finite-state regime the answer is negative:

\[
\boxed{
\text{a finite family of position-regular primitive operations cannot FO-recover EqGap.}
}
\]

Therefore synchronized closure cannot disappear. It can only be placed in one of three locations:

1. the ambient logic/semantics as unbounded closure or reachability;
2. a primitive operation/relation whose graph already contains nonregular displacement information;
3. an additional unbounded carrier/sort whose incidence structure materializes the missing nonregular information.

This is the working **Closure-Placement Principle**.

## 2. Position-regular relations

Let

\[
L_m=([m],<),\qquad [m]=\{0,\dots,m-1\}.
\]

For fixed arity \(r\), encode a tuple \(\bar x\in[m]^r\) by a length-\(m\) word whose letter at position \(j\) records which variables equal \(j\). Coincident variables are allowed. Fixed unary background colors may be included in the finite alphabet.

A uniform family \(R_m\subseteq[m]^r\) is **position-regular** when the language of correctly marked finite words representing tuples in \(R_m\) is regular.

Examples include order, equality, successor, fixed-distance predicates, ultimately-periodic unary colors, one-head finite-state interval predicates, and operation graphs recognized by a fixed finite automaton scanning the marked carrier.

## 3. Finite-copy presentation

Allow a fixed finite collection of copies

\[
C_1\times[m],\dots,C_s\times[m]
\]

plus finitely many singleton roles.

A primitive relation or relationalized partial-operation graph is **finite-copy position-regular** when its marked-tuple language, including the finite copy labels, is regular.

This covers the style of the G4-A fixed-copy transduction.

## 4. FO closure preserves position-regularity

### Lemma 4.1

Let a finite relational signature on \([m]\) consist only of position-regular primitive relations. Then every uniformly FO-definable relation is position-regular.

### Proof

Atomic formulas are regular by hypothesis. Regular languages are closed under Boolean operations. Existential quantification is projection of a marker track, and regular languages are closed under projection. Universal quantification follows from complement. Correct single-occurrence marker conditions are regular. \(\square\)

### Lemma 4.2

The same conclusion holds for a fixed finite-copy presentation.

### Proof

Quantification chooses one of finitely many copy labels and one position, or one of finitely many singleton roles. Existential quantification is therefore a finite union of regular projections. \(\square\)

## 5. EqGap is not position-regular

For forward intervals,

\[
\operatorname{EqGap}(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c).
\]

Restrict to

\[
a=\min,\qquad c=\operatorname{Succ}(b),\qquad d=\max.
\]

If \(b\) has zero-based rank \(n\ge1\), the restricted marker skeleton is

\[
L_{gap}=\{A a^{n-1}BCa^{n-1}D:n\ge1\}.
\]

### Lemma 5.1

\(L_{gap}\) is not regular.

### Proof

Assume it regular and let \(p\) be a pumping length. Choose

\[
w=Aa^pBCa^pD.
\]

After absorbing the fixed initial marker into the pumping constant, any pumping decomposition whose pumped part lies in the first variable \(a\)-block changes only that block while leaving the second block length \(p\). Pumping therefore produces a word not in \(L_{gap}\), contradiction. Equivalently one may use Myhill-Nerode with prefixes \(Aa^nB\), which require pairwise distinct continuations \(Ca^nD\). \(\square\)

Hence

\[
\boxed{\operatorname{EqGap}\text{ is not position-regular}.}
\]

Because EqGap and truncated rank addition are uniformly FO-interdefinable over the ordered generic sector, the same barrier applies to Add.

## 6. Regular-Primitive Barrier

### Theorem 6.1

Let \(\mathfrak B_m\) be any uniform finite-signature fixed finite-copy expansion of the G4-A generic order such that every added primitive relation and every relationalized partial-operation graph is finite-copy position-regular.

Then neither EqGap nor canonical truncated rank addition is uniformly first-order definable in \(\mathfrak B_m\).

### Proof

By Lemma 4.2 every FO-definable base-sort relation in \(\mathfrak B_m\) is position-regular. Section 5 shows EqGap is not. If Add were definable, EqGap would be definable from Add by the already fixed additive-gateway formula. Contradiction. \(\square\)

Thus the result holds for any finite number of position-regular primitive operation symbols.

## 7. Consequence for ordinary local partial operations

If \(\star,\diamond\) are generated by fixed local/finite-state rules and their full graphs remain position-regular, then

\[
(G_m,<,\star,\diamond)
\]

cannot FO-recover EqGap.

Finite joint-rigidity phenomena therefore do not imply variable-displacement memory.

## 8. Algorithmic execution versus static FO

Let \(S(x,y)\) be successor. Repeatedly applying successor in parallel can algorithmically compare interval lengths, but the static reduct containing only the one-step relation does not define the reflexive-transitive closure of the product step.

Hence

\[
\boxed{
\text{algorithmic recovery by unbounded execution}
\ne
\text{uniform FO definability in the static reduct}.
}
\]

The Arithmetic Leakage levels AL0/AL-FS/AL1 concern the second notion unless stated otherwise.

## 9. Dimension-Two Closure Threshold

The audited reconciliation with the head-synchronization note is especially clean.

In one dimension,

\[
TC(S)(a,b)\iff a\le b,
\]

which is already FO-definable in the ordered carrier.

Define the local product-successor edge

\[
E(a,c;b,d)
\iff
S(a,b)\land S(c,d).
\]

The edge \(E\) itself is FO-definable from order and therefore adds no static FO power. But

\[
TC(E)((a,c),(b,d))
\iff
EqGap(a,b;c,d).
\]

Thus

\[
\boxed{
TC(S)\in AL0,
\qquad
TC(S\times S)=EqGap\in AL1.
}
\]

The power source is not “two heads” by itself, but unbounded closure on synchronized two-dimensional product geometry.

## 10. Closure-Placement Theorem

### Theorem 10.1

Assume a fixed finite-copy FCOA expansion uniformly FO-recovers EqGap. Then at least one of the following occurs:

1. some primitive relation/operation graph is not position-regular;
2. recovery semantics uses an unbounded closure mechanism not expressible by ordinary FO over the primitive graphs;
3. an additional unbounded sort/incidence structure outside the finite-copy position-regular model carries the missing nonregular information.

### Proof

If none occurs, the presentation falls under Theorem 6.1, contradiction. \(\square\)

This is a placement theorem, not a claim that the three cases are disjoint in every formalism.

## 11. Recursion relocates closure

A recursively specified operation

\[
x\boxplus0_G=x,
\qquad
x\boxplus\operatorname{Succ}(y)=\operatorname{Succ}(x\boxplus y)
\]

has completed graph equal to truncated addition. Therefore its graph is non-position-regular. The recursive specification has compiled the unbounded closure into the primitive table.

\[
\boxed{
\text{recursion can relocate closure; it cannot erase its logical cost}.}
\]

## 12. Cartesian-product sort is a separate case

The fixed finite-copy theorem does not literally cover a quadratic configuration sort

\[
C_m=G_m^2.
\]

Nevertheless, if this sort is introduced only as the Cartesian product with coordinate projections and relations FO-definable from \((G_m,<)\), including local product successor, it is a fixed-dimensional FO interpretation of the base order.

Every FO formula over that interpreted pair structure translates to FO over the base order. Since EqGap is not FO-definable in finite linear order, the pair sort plus local step still cannot define EqGap.

Adding a primitive reachability relation on the pair sort is exactly adding the missing closure.

## 13. Fixed-depth nesting barrier

Any fixed-depth term or formula nesting over a finite position-regular primitive signature is still FO-definable in that signature and therefore position-regular.

Hence

\[
\boxed{
\text{fixed syntactic nesting depth cannot cross the Regular-Primitive Barrier}.}
\]

To reach EqGap via nesting, depth must grow with input/carrier and be materialized, or a non-position-regular primitive/incidence relation must be introduced.

## 14. Fiber-only encoding needs unboundedly many gap labels

Let

\[
I_m=\{(a,b):a\le b\}
\]

and suppose \(c:I_m\to O_m\) satisfies

\[
EqGap(I,J)\iff c(I)=c(J).
\]

There are exactly \(m\) possible interval lengths, so distinct lengths require distinct values:

\[
\boxed{|O_m|\ge m.}
\]

Bounded outputs can encode EqGap only if the nonregular information is placed elsewhere, for example in the domain.

## 15. Central consequence

Within finite-copy local/finite-state static FO semantics:

\[
\boxed{
\text{regular local primitives}
\quad\text{versus}\quad
\text{materialized/unbounded closure}
}
\]

is the genuine boundary.

The previous shorthand

\[
H_2^{sync}=AL1
\]

must therefore be read only operationally as

\[
\boxed{
H_2^{sync}+\text{unbounded traversal closure}=AL1.
}
\]

## 16. New optimization problem

The next central question is:

\[
\boxed{
\text{What is the cheapest nonregular but non-oracular primitive memory that materializes synchronized closure?}
}
\]

Direct addition costs \(\Theta(m^2)\) operation-domain support; direct EqGap domain compilation costs \(\Theta(m^3)\) four-ary support. History/nesting materialization may compress this further and is now the main constructive route.

## 17. Status

After hostile audit:

\[
\boxed{
\mathbf F:\ \text{finite-copy position-regular primitive expansions cannot FO-define EqGap/Add.}
}
\]

\[
\boxed{
\mathbf F:\ TC(S)\in AL0\text{ and }TC(S\times S)=EqGap\in AL1.
}
\]

\[
\boxed{
\mathbf F:\ \text{fixed-depth nesting over regular primitives cannot cross the barrier.}
}
\]

\[
\boxed{
\mathbf F:\ \text{pure fiber EqGap coding requires }|O_m|\ge m.
}
\]

Programme terminology remains

\[
\boxed{
\mathbf W:\ \text{Closure-Placement Principle / Regular-Primitive Barrier terminology.}
}
\]

No numbered G5 operation family is opened here.