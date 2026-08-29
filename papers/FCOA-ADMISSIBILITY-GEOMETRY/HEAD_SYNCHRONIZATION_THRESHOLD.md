# Head-Synchronization Threshold — From Finite-State Interval Tests to Additive Transport

**Project:** FCOA Admissibility Geometry  
**Status:** audited operational theorem; static-FO interpretation corrected  
**Scope:** central Arithmetic Leakage programme after the unary U1 wall

## 1. Motivation

The unary finite-state wall separates finite phase memory from variable displacement memory:

\[
AL0<AL\text{-}FS<AL1.
\]

The next question is whether the decisive resource is more internal state or something qualitatively different.

The audited answer is:

\[
\boxed{
\text{one-head finite-state interval predicates remain below EqGap,}
}
\]

while a synchronized two-coordinate walk **with unbounded traversal closure** generates EqGap exactly.

The critical resource is therefore not a second local symbol by itself, but synchronized product geometry together with unbounded iteration.

## 2. One-head interval generators

Work on the generic chain

\[
G_m=\{0<1<\cdots<m-1\}
\]

as metamathematical notation for the recovered G4-A order.

A **one-head finite-state interval predicate** is a binary relation \(R(x,y)\), with \(x\le y\), recognized by a fixed finite automaton that starts at \(x\), walks right by successor one step at a time, may read finitely many ultimately-periodic unary background colors, and accepts/rejects when it reaches \(y\).

The machine is independent of \(m\). A finite collection of such predicates and any further fixed FO-definitional compilation are allowed.

## 3. Marked-word regularity

Encode a finite chain as a finite word over a finite alphabet carrying the background colors and marker tracks for free variables.

Each one-head interval predicate has a regular marked-word language: a finite automaton ignores the prefix before the \(x\)-marker, simulates the interval machine from \(x\) through \(y\), then ignores the suffix.

### Lemma 3.1 — regular closure under FO

If every primitive relation in a finite positional signature has a regular marked-word encoding, then every uniformly FO-definable relation has a regular marked-word encoding.

### Proof

Atomic formulas are regular. Regular languages are closed under Boolean operations and projection of marker tracks. Universal quantification follows from complement. \(\square\)

## 4. EqGap has a nonregular positional skeleton

For forward intervals,

\[
EqGap(a,b;c,d)
\iff
b-a=d-c
\]

in external rank notation only.

Restrict to

\[
a=\min,
\qquad
c=Succ(b),
\qquad
d=\max.
\]

The resulting skeleton is

\[
L_{gap}=\{A a^{n-1}BCa^{n-1}D:n\ge1\}.
\]

### Lemma 4.1

\(L_{gap}\) is not regular.

### Proof

Use Myhill-Nerode. The prefixes

\[
p_n=Aa^{n-1}B
\]

are pairwise distinguishable: the suffix

\[
s_n=Ca^{n-1}D
\]

satisfies \(p_ns_n\in L_{gap}\), while for \(r\ne n\), \(p_rs_n\notin L_{gap}\). Hence infinitely many Nerode classes exist, so the language is not regular. \(\square\)

This replaces the earlier invalid shortcut using a plain homomorphism to an equal-block language.

## 5. One-Head Wall Theorem

### Theorem 5.1

No finite expansion of finite linear order by one-head finite-state interval predicates, even with finitely many ultimately-periodic unary background colors, uniformly FO-defines EqGap.

### Proof

If EqGap were definable, imposing the regular endpoint restrictions of Section 4 would yield a regular marked-word language by Lemma 3.1, contradicting Lemma 4.1. \(\square\)

Because Add and EqGap are uniformly FO-interdefinable over the ordered generic sector,

\[
\boxed{
Add\text{ is also impossible in the one-head finite-state layer.}
}
\]

## 6. Local synchronized product step

Let

\[
E(a,c;b,d)
\iff
Succ(a,b)\land Succ(c,d).
\]

This is the one-step edge of the synchronized product walk.

Crucially, \(E\) itself is FO-definable from the base order. Therefore adding \(E\) as a static primitive does not cross the additive leakage wall.

The new power appears only when one admits unbounded traversal of \(E\).

## 7. Synchronized-Product Closure Theorem

### Theorem 7.1

For all forward intervals,

\[
\boxed{
EqGap(a,b;c,d)
\iff
TC(E)((a,c),(b,d)).
}
\]

### Proof

After \(k\) synchronized product steps, the two coordinates are exactly the \(k\)-th successors of \(a\) and \(c\). Reachability from \((a,c)\) to \((b,d)\) therefore holds exactly when the two endpoint displacements are equal. \(\square\)

This theorem is operational/dynamic. It is not a claim that ordinary FO over \((G_m,<,E)\) already contains \(TC(E)\).

## 8. Dimension-Two Closure Threshold

The one-dimensional successor closure is harmless:

\[
TC(Succ)(a,b)\iff a\le b,
\]

which is already FO-definable in finite linear order.

But synchronized product closure gives EqGap:

\[
TC(Succ\times Succ)=EqGap.
\]

Hence

\[
\boxed{
TC(Succ)\in AL0,
\qquad
TC(Succ\times Succ)=EqGap\in AL1.
}
\]

This is the clean threshold statement replacing the older unqualified slogan \(H_2^{sync}=AL1\).

## 9. Direct synchronized transport operation

An operational generator for truncated addition is obtained by starting one head at \(0_G\) with target \(y\), the other at \(x\), and advancing synchronously until the first reaches \(y\). If the second remains in the carrier, output its current point \(z\).

Then

\[
x\triangleplus y=z
\iff
EqGap(0_G,y;x,z),
\]

so externally

\[
\operatorname{rk}(z)=\operatorname{rk}(x)+\operatorname{rk}(y)<m.
\]

The local generator uses only successor, equality to targets, and unbounded iteration. The completed operation graph is non-position-regular: the closure has been compiled into the primitive table.

## 10. Uniformity and prefix consistency

The generator does not inspect final size \(m\). For the completed graph,

\[
Graph(\triangleplus_m)
=
Graph(\triangleplus_\infty)\cap G_m^3.
\]

Truth of every old triple is stable under extension. Only the existential domain projection may grow when a previously absent result enters the larger carrier.

EqGap itself is prefix-stable on old quadruples.

## 11. Relative head threshold

Within the declared **operational traversal model**:

\[
\boxed{
H_1\;<\;H_2^{sync}+TC
}
\]

with respect to EqGap.

More precisely:

\[
\boxed{
H_1:\ \text{finite-state interval predicates stay below EqGap},
}
\]

while

\[
\boxed{
H_2^{sync}+\text{unbounded traversal closure}:\ \text{generates EqGap exactly}.
}
\]

The statement “two heads are minimal” is valid only inside this operational hierarchy. It is not a global minimality theorem for arbitrary FCOA presentations.

## 12. Cost of materializing the closure

If EqGap itself is materialized, then for gap \(k\) there are \(m-k\) intervals of that length, so

\[
|EqGap_m|
=
\sum_{k=0}^{m-1}(m-k)^2
=
\frac{m(m+1)(2m+1)}6
=
\Theta(m^3).
\]

If truncated addition is materialized as a partial operation,

\[
|Dom(\triangleplus)|
=
\sum_{i=0}^{m-1}(m-i)
=
\frac{m(m+1)}2
=
\Theta(m^2).
\]

These are representation costs, not lower bounds for AL1 in all models.

## 13. Product-sort caution

The Cartesian configuration sort

\[
C_m=G_m^2
\]

is not a fixed finite-copy sort. If it is introduced only with coordinate projections and relations FO-definable from base order, including local product successor, it is a fixed-dimensional FO interpretation of the base chain.

Therefore ordinary FO on that interpreted structure translates back to FO on finite linear order and still cannot define EqGap.

A primitive reachability relation on \(C_m\) would be exactly the missing closure.

## 14. Fixed-depth nesting does not suffice

Because fixed-depth composition of position-regular primitives remains FO-definable from a finite position-regular signature,

\[
\boxed{
\text{fixed syntactic nesting depth cannot cross to EqGap}.}
\]

A successful nesting construction must use depth growing with the carrier/input and materialize that history, or otherwise introduce nonregular incidence information.

## 15. Arithmetic-leakage status

The static local product step remains in the order layer:

\[
FO[<,E]=FO[<]
\]

because \(E\) is definable from successor/order.

The unbounded closure of \(E\) reaches the additive gateway:

\[
TC(E)=EqGap.
\]

No multiplication result follows from this note alone.

## 16. Status

After hostile audit and reconciliation with the Regular-Primitive Barrier:

\[
\boxed{
\mathbf F:\ \text{one-head finite-state interval layers do not FO-define EqGap/Add}.}
\]

\[
\boxed{
\mathbf F:\ TC(Succ)\in AL0,
\qquad
TC(Succ\times Succ)=EqGap\in AL1.
}
\]

\[
\boxed{
\mathbf F:\ \text{two-head synchronization alone, as a static local primitive, does not imply AL1}.}
\]

The retired working slogan

\[
H_2^{sync}=AL1
\]

is replaced by

\[
\boxed{
H_2^{sync}+\text{unbounded traversal closure}=AL1.
}
\]

No numbered G5 operation family is opened here.