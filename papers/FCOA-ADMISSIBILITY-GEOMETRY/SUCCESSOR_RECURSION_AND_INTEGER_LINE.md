# Successor Recursion and the Integer-Line Extension

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate with internal audit completed  
**Scope:** generated additive gateway on the given number line; then carrier extension from \(\mathbb N_0\) to \(\mathbb Z\)

## 1. Number-line convention

The ambient numerical carrier is treated as a given number line, not reconstructed as a quotient of abstract interval classes.

For the current finite/infinite natural-line phase we use

\[
\mathbb N_0=\{0,1,2,\ldots\}
\]

with its given order, distinguished \(0\), and successor map

\[
S(n)=n+1.
\]

When the programme passes to integers, the carrier is enlarged directly to the ordinary integer line

\[
\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}
\]

with given order, \(0\), successor \(S\), and predecessor \(P=S^{-1}\).

No representation of negative integers by equivalence classes of oriented intervals is required.

The Arithmetic Leakage question remains internal: which arithmetic relations can be **generated or recovered from the allowed FCOA mechanisms** after the carrier geometry is fixed?

## 2. Natural-line recursive generator

On \(\mathbb N_0\), introduce a binary operation \(\boxplus\) by the primitive recursion scheme

\[
\boxed{x\boxplus0=x}
\tag{R0}
\]

and

\[
\boxed{x\boxplus S(y)=S(x\boxplus y).}
\tag{RS}
\]

The local generator refers only to the already-given boundary point \(0\) and successor. It does not query the final carrier size and does not call an existing addition operation.

On a finite prefix

\[
[m]=\{0,1,\ldots,m-1\},
\]

\(\boxplus_m\) is partial: the recursion continues only while the output successor remains in \([m]\).

## 3. Natural-Line Recursion Theorem

### Theorem 3.1

There is a unique operation on \(\mathbb N_0\) satisfying (R0)-(RS). Extensionally it is ordinary addition:

\[
\boxed{x\boxplus y=x+y.}
\]

On \([m]\), the generated partial operation is exactly truncated addition:

\[
\boxed{
x\boxplus_m y=z
\iff
z=x+y<m.
}
\]

### Proof

Fix \(x\). Uniqueness follows by induction on \(y\). The value at \(0\) is forced by (R0). If the value at \(y\) is forced, then (RS) forces the value at \(S(y)\).

For existence, iterate (RS) starting from \(x\boxplus0=x\). After \(y\) successor steps the output is the point obtained from \(x\) by the same number of successor steps. On the standard natural line that point is \(x+y\). In a finite prefix the construction exists exactly while that point remains below \(m\). \(\square\)

The arithmetic equality in the conclusion is an extensional identification of the generated table, not a premise of the generator.

## 4. Least-recursive-closure formulation

Relationalize the generated operation by

\[
A(x,y,z)\iff x\boxplus y=z.
\]

Let \(\Phi\) act on ternary relations by

\[
\Phi(R)
=
\{(x,0,x):x\in\mathbb N_0\}
\cup
\{(x,S(y),S(z)):(x,y,z)\in R\}.
\]

Then

\[
\boxed{
A=\operatorname{lfp}(\Phi).
}
\]

This makes the relation to the previous synchronized-head result explicit: additive memory appears through **unbounded recursive propagation of one local successor rule**.

The leastness condition is essential. The two local closure clauses alone do not characterize the intended graph among arbitrary supersets.

No transitive-closure or least-fixed-point symbol is added to the final FCOA signature. The closure is part of the **generation semantics** used to construct an ordinary binary operation.

## 5. Generated leakage versus FO compilation

The previous FO-Compilation Barrier states that a uniformly FO-definable expansion of G4-A cannot leave \(FO[<]\).

The operation \(\boxplus\) does leave that wall, because its graph is not uniformly FO-definable from finite order.

There is no contradiction: the generator is recursive and has unbounded depth. It is not a fixed FO-definitional template.

Thus the main programme obtains a clean example of **generated leakage**:

\[
\boxed{
\text{local successor rule}
+\text{unbounded recursion}
\Longrightarrow
\text{AL1 additive memory}.
}
\]

This closes the gap between the synchronized two-head semantics and an ordinary final FCOA operation table.

## 6. Direct relation to EqGap

For forward intervals on \(\mathbb N_0\), define

\[
\operatorname{EqGap}(a,b;c,d)
\iff
b-a=d-c.
\]

Then the generated operation satisfies

\[
\boxed{
x\boxplus y=z
\iff
\operatorname{EqGap}(0,y;x,z).
}
\]

Conversely,

\[
\boxed{
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,[a\boxplus s=b\land c\boxplus s=d].
}
\]

Hence the recursively generated \(\boxplus\) lands exactly at the already-fixed additive gateway AL1.

## 7. Internal algebraic check on \(\mathbb N_0\)

The usual additive laws are not assumed by analogy; they follow from the recursion.

### Lemma 7.1

\[
0\boxplus y=y.
\]

Proof by induction on \(y\).

### Lemma 7.2

\[
S(x)\boxplus y=S(x\boxplus y).
\]

Again by induction on \(y\).

### Proposition 7.3 — commutativity

\[
\boxed{x\boxplus y=y\boxplus x.}
\]

Proof by induction on \(y\), using Lemmas 7.1-7.2.

### Proposition 7.4 — associativity

\[
\boxed{(x\boxplus y)\boxplus z=x\boxplus(y\boxplus z).}
\]

Proof by induction on \(z\), using (RS).

Therefore

\[
\boxed{(\mathbb N_0,\boxplus,0)}
\]

is a commutative monoid generated from the number-line successor recursion.

For finite prefixes these identities hold whenever both sides are defined; truncation is the only obstruction.

## 8. Graph-prefix consistency

Let \(A_\infty\) be the infinite graph and \(A_m\) the finite-prefix graph. Then

\[
\boxed{
A_m=A_\infty\cap[m]^3.
}
\]

Hence no old triple changes truth value when the carrier is extended.

The partial-function domain can grow after extension only because a previously absent output point becomes available. This is truncation, not a size oracle.

## 9. Additive gateway closed at the generation level

The central AL1 problem had two separate components:

1. identify the logical relation EqGap / truncated addition;
2. exhibit a non-oracular FCOA-compatible mechanism that **generates** it rather than importing it.

The recursion scheme (R0)-(RS) supplies the second component.

Thus, modulo external hostile audit of the generator/signature distinction, the additive gateway is now internally implemented as an ordinary generated partial operation.

This is the point at which the integer-line extension becomes legitimate in the project plan.

---

# Part II. Direct extension to the integer line

## 10. Carrier extension

Replace the half-line carrier \(\mathbb N_0\) by the given integer line

\[
\mathbb Z.
\]

The background geometry now contains

\[
0,
\qquad
S(n)=n+1,
\qquad
P(n)=n-1,
\qquad
P=S^{-1}.
\]

This is a carrier extension, not an interpretation of integers inside the natural-line structure.

The finite-fragment version may use symmetric windows

\[
[-M,M]
\]

or another explicitly declared interval. No wrap-around is allowed.

## 11. Bi-directional successor recursion

Define \(\boxplus_{\mathbb Z}\) by

\[
\boxed{x\boxplus_{\mathbb Z}0=x,}
\tag{Z0}
\]

\[
\boxed{x\boxplus_{\mathbb Z}S(y)=S(x\boxplus_{\mathbb Z}y),}
\tag{ZS}
\]

and equivalently

\[
\boxed{x\boxplus_{\mathbb Z}P(y)=P(x\boxplus_{\mathbb Z}y).}
\tag{ZP}
\]

The two propagation laws agree because \(P=S^{-1}\).

No negative-number encoding is introduced: negative points are already points of the ambient carrier.

## 12. Integer-Line Recursion Theorem

### Theorem 12.1

There is a unique binary operation on \(\mathbb Z\) satisfying (Z0), (ZS), and (ZP). It is extensionally ordinary integer addition:

\[
\boxed{
x\boxplus_{\mathbb Z}y=x+y.
}
\]

### Proof

Fix \(x\). Starting from \(y=0\), repeated use of (ZS) uniquely determines the value for every \(y>0\). Repeated use of (ZP) uniquely determines the value for every \(y<0\). Thus uniqueness holds on the whole line.

Existence is obtained by the same outward recursion from \(0\). Moving the second argument one successor step moves the result one successor step; moving it one predecessor step moves the result one predecessor step. On the standard integer line the resulting point is exactly the translate of \(x\) by \(y\), namely \(x+y\). \(\square\)

Again, ordinary `+` appears only in the extensional identification of the generated operation.

## 13. Reflection and additive inverse

The given integer line has a canonical reflection about \(0\), generated geometrically by

\[
\nu(0)=0,
\]

\[
\nu(S(x))=P(\nu(x)),
\qquad
\nu(P(x))=S(\nu(x)).
\]

This is the ordinary map \(x\mapsto -x\), but the recursion above characterizes it from line geometry.

### Proposition 13.1

For every \(x\in\mathbb Z\),

\[
\boxed{
x\boxplus_{\mathbb Z}\nu(x)=0.
}
\]

### Proof

For \(x=0\) this is immediate. If the identity holds for \(x\), then

\[
S(x)\boxplus\nu(S(x))
=
S(x)\boxplus P(\nu(x)).
\]

Using the recursion in the second argument and translation covariance in the first argument gives the predecessor of

\[
S(x)\boxplus\nu(x)
=
S(x\boxplus\nu(x))
=S(0),
\]

hence \(0\). The predecessor direction is symmetric. \(\square\)

Thus inverses arise from the actual two-sided line geometry rather than from quotienting oriented intervals.

## 14. Group laws on \(\mathbb Z\)

The natural-line proofs extend by induction outward from \(0\) in both directions.

Therefore

\[
\boxed{
(\mathbb Z,\boxplus_{\mathbb Z},0)
}
\]

is an abelian group:

\[
x\boxplus y=y\boxplus x,
\]

\[
(x\boxplus y)\boxplus z=x\boxplus(y\boxplus z),
\]

\[
x\boxplus0=x,
\]

\[
x\boxplus\nu(x)=0.
\]

These are proved consequences of the recursive line-translation law, not imported axioms.

## 15. Signed EqGap becomes immediate

On the integer line define the signed displacement externally by

\[
\Delta(a,b)=b-a.
\]

The corresponding four-place relation is

\[
\operatorname{EqSignedGap}(a,b;c,d)
\iff
b-a=d-c.
\]

Once \(\boxplus_{\mathbb Z}\) is generated,

\[
\boxed{
\operatorname{EqSignedGap}(a,b;c,d)
\iff
\exists s\,[a\boxplus s=b\land c\boxplus s=d].
}
\]

Unlike the earlier natural-line EqGap, no forward-orientation restriction is needed.

Thus the passage to \(\mathbb Z\) removes the truncation/orientation asymmetry of additive displacement while introducing no new arithmetic generator beyond predecessor as the second direction of the given line.

## 16. What has and has not been achieved

### Achieved

- direct generated truncated addition on the given \(\mathbb N_0\) line;
- no transitive-closure symbol in the final operation signature;
- exact recursive explanation of why the generator crosses the FO wall;
- direct carrier extension to the actual integer line \(\mathbb Z\);
- generated ordinary integer addition from \(0,S,P\);
- additive inverses from line reflection;
- signed displacement / EqSignedGap without quotient representations.

### Not achieved

- no multiplication is generated here;
- no claim is made that addition is minimal among all possible non-oracular AL1 mechanisms;
- no full bi-infinite analogue of every finite G4-A automorphism calculation is asserted;
- no claim is made that primitive recursion from successor is mathematically new.

The new content for the FCOA programme is the placement of standard successor recursion exactly at the **generated-leakage gateway** identified by the preceding order/finite-state walls.

## 17. Internal hostile audit

The following objections were checked.

1. **Hidden addition in the generator?** No. The generator uses only \(0\), successor, and on \(\mathbb Z\) predecessor. Addition occurs only in the extensional theorem identifying the generated table.
2. **Is leastness hidden?** Yes, recursive generation/least closure is essential and is stated explicitly. This is the resource that crosses the FO-Compilation Barrier.
3. **Is transitive closure secretly added to the final language?** No. It is generation semantics, not a target-language symbol.
4. **Does finite truncation use final size?** Only to determine whether the generated output remains in the finite carrier. Graph-prefix truth is stable.
5. **Are integers being reconstructed abstractly?** No. The carrier is directly enlarged to the given integer line.
6. **Are group laws merely assumed?** No. They follow from the recursion by induction.
7. **Does this already imply multiplication?** No. No multiplication recursion or variable repeated-addition closure is introduced.

No internal defect was found. External hostile audit is still appropriate before promoting the entire note to fixed status.

## 18. Central next step

The programme has now reached a clean junction.

The additive operation exists on \(\mathbb N_0\) and extends naturally to \(\mathbb Z\). The next central question should **not** immediately import multiplication.

The sharper problem is:

\[
\boxed{
\text{what is the weakest generated mechanism beyond integer addition that first leaks multiplicative structure?}
}
\]

Before attacking that boundary, one optimization remains important:

\[
\boxed{
\text{can AL1 addition be recoverably encoded with subquadratic support while respecting the Uniformity Firewall?}
}
\]

The threshold-compression calibration shows that subquadratic relational support is possible in principle, but not yet for an internally generated relation known to recover full addition.

That is the recommended immediate next strike.