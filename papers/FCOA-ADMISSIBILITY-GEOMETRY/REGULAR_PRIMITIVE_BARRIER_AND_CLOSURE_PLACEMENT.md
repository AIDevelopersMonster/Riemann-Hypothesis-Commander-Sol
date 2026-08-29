# Regular-Primitive Barrier and Closure Placement

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate; proof-complete in stated scope  
**Scope:** post-U1 / post-head-synchronization Arithmetic Leakage programme

## 1. Central question

The synchronized-head construction shows that

\[
\operatorname{EqGap}(a,b;c,d)
\iff
(a,c)\Rightarrow^*(b,d),
\]

where \(\Rightarrow\) is the local product-successor step.

The next question is whether the unbounded closure can be eliminated and the same memory obtained from two ordinary weak FCOA partial operations alone.

The answer is negative in the natural local/finite-state regime:

\[
\boxed{
\text{a finite family of position-regular primitive operations cannot FO-recover EqGap.}
}
\]

Thus synchronized closure cannot disappear. It can only be placed in one of three locations:

1. the ambient logic/semantics as unbounded closure or reachability;
2. a primitive operation/relation whose graph already contains nonregular displacement information;
3. an additional unbounded carrier/sort whose incidence structure materializes the closure.

This is the **Closure-Placement Principle**.

## 2. Position-regular relations

Let

\[
L_m=([m],<),
\qquad [m]=\{0,\dots,m-1\}.
\]

For a fixed arity \(r\), encode a tuple

\[
\bar x=(x_1,\dots,x_r)\in[m]^r
\]

by a length-\(m\) word whose letter at position \(j\) records which variables \(x_i\) are equal to \(j\). Coincident variables are allowed.

If fixed unary background colors are present, include their finite color label in the alphabet.

A uniform family of relations

\[
R_m\subseteq[m]^r
\]

is called **position-regular** if the language of all correctly marked finite words representing tuples in \(R_m\) is regular.

This is a semantic definition. It does not assume that \(R_m\) is FO-definable in pure order.

Examples include:

- order and equality;
- successor;
- fixed-distance relations;
- ultimately-periodic unary colors;
- every one-head finite-state interval predicate from `U1_FINITE_STATE_WALL.md`;
- any operation graph recognized by a fixed finite automaton scanning the marked ordered carrier.

## 3. Finite-copy FCOA presentation

The G4-A collapse already uses a fixed finite-copy transduction of the generic chain. To cover the same style of typed/output architecture, allow a fixed finite collection of copies

\[
C_1\times[m],\dots,C_s\times[m]
\]

plus finitely many singleton roles.

A primitive relation or partial-operation graph on these copies is **finite-copy position-regular** when, after recording the finitely many copy labels of its arguments and marking their source positions, its tuple language is regular.

This allows active points, terminal-output copies, and fixed boundary/singleton roles while keeping the presentation one-dimensional and finite-state.

## 4. Regular closure under first-order formulas

### Lemma 4.1 — base-sort version

Let a finite relational signature on \([m]\) consist only of position-regular primitive relations. Then every uniformly first-order definable relation is position-regular.

### Proof

Proceed by induction on formulas.

- Atomic formulas are regular by hypothesis.
- Boolean combinations preserve regularity.
- For \(\exists x\,\varphi(x,\bar y)\), add an \(x\)-marker track, recognize the regular marked-word language for \(\varphi\), and project away the \(x\)-track. Regular languages are closed under projection.
- Universal quantification follows from complement and existential quantification.

Correctness conditions saying that each variable marker occurs exactly once are themselves regular. \(\square\)

### Lemma 4.2 — finite-copy version

The same conclusion holds for a fixed finite-copy presentation.

### Proof

Quantifying over an element means choosing one of finitely many copy labels and one position, or one of finitely many singleton roles. Existential quantification is therefore a finite union of regular projections. The induction from Lemma 4.1 is unchanged. \(\square\)

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
a=\min,
\qquad
c=\operatorname{Succ}(b),
\qquad
d=\max.
\]

If \(b\) has zero-based rank \(n\ge1\), EqGap forces a marker skeleton of the form

\[
A\,u^{n-1}B\,C\,u^{n-1}D.
\]

If this language were regular, then intersecting with the fixed marker pattern and applying a homomorphism would make the equal-block language

\[
\{u^n v^n:n\ge0\}
\]

regular, contradiction.

Hence

\[
\boxed{
\operatorname{EqGap}\text{ is not position-regular.}
}
\]

The same conclusion applies to truncated rank addition because EqGap and Add are already uniformly FO-interdefinable over the ordered generic sector.

## 6. Regular-Primitive Barrier

### Theorem 6.1

Let \(\mathfrak B_m\) be any uniform finite-signature, fixed finite-copy expansion of the G4-A generic order such that every added primitive relation and every relationalized partial-operation graph is finite-copy position-regular.

Then neither EqGap nor canonical truncated rank addition is uniformly first-order definable in \(\mathfrak B_m\).

### Proof

By Lemma 4.2 every FO-definable base-sort relation in \(\mathfrak B_m\) is position-regular. Section 5 shows EqGap is not. If Add were definable, EqGap would be definable from Add by the already fixed additive-gateway formula. Contradiction. \(\square\)

This theorem is insensitive to the number of primitive operation symbols as long as that number is finite and every primitive graph stays position-regular.

## 7. Consequence for two ordinary local partial operations

Suppose two new partial operations

\[
\star,\diamond
\]

are generated by fixed local/finite-state rules on the recovered carrier geometry, and their full operation graphs are position-regular.

Then even the joint reduct

\[
(G_m,<,\star,\diamond)
\]

cannot FO-recover EqGap.

Therefore:

\[
\boxed{
\text{two weak ordinary local partial operations do not internalize synchronized transport.}
}
\]

Hybrid interaction can destroy finite automorphisms, synchronize value fibers, or add modular information, but if all primitive graphs remain position-regular then no amount of finite first-order combination crosses the additive gateway.

This does not conflict with finite JFS phenomena: finite joint rigidity is much weaker than uniform variable-displacement memory.

## 8. Why repeated execution is not yet internal FO memory

Let \(S(x,y)\) be successor. Externally, an algorithm can compare two interval lengths by repeatedly applying successor in parallel:

\[
(a,c)\mapsto(Sa,Sc)\mapsto(S^2a,S^2c)\mapsto\cdots.
\]

This computes EqGap.

But the static first-order reduct containing only the one-step relation does not define the reflexive-transitive closure of the product step.

Thus two notions must not be conflated:

\[
\boxed{
\text{algorithmic recovery by unbounded execution}
\neq
\text{uniform FO definability in the static reduct}.
}
\]

The central Arithmetic Leakage levels AL0/AL-FS/AL1 concern the second notion.

If unbounded execution is admitted as part of semantics, the logic has effectively been strengthened by a closure mechanism.

## 9. Closure-Placement Theorem

### Theorem 9.1

Assume a fixed finite-copy FCOA expansion uniformly FO-recovers EqGap.

Then at least one of the following must occur:

1. some primitive relation/operation graph is not position-regular;
2. the recovery semantics uses an unbounded closure mechanism not expressible by ordinary FO over the primitive graphs;
3. the presentation uses an additional unbounded sort or incidence structure outside the finite-copy position-regular model, and that structure itself carries the missing nonregular information.

### Proof

If none of (1)-(3) occurs, the entire presentation falls under Theorem 6.1, which forbids FO-definition of EqGap. \(\square\)

The theorem is deliberately a placement result, not a claim that the three cases are disjoint or exhaustive for every conceivable formalism. It identifies where the nonregular displacement information must enter within the present FCOA programme.

## 10. Recursion does not make the closure disappear

A tempting construction defines an operation recursively by

\[
x\boxplus 0_G=x,
\]

\[
x\boxplus \operatorname{Succ}(y)
=
\operatorname{Succ}(x\boxplus y),
\]

whenever the result remains in the finite carrier.

This looks local, but its completed operation graph is exactly truncated addition:

\[
\operatorname{rk}(x\boxplus y)
=
\operatorname{rk}(x)+\operatorname{rk}(y).
\]

Hence its graph is non-position-regular by Theorem 6.1.

The recursive specification has therefore **compiled the unbounded closure into the primitive table**. It is not a counterexample to the barrier.

This gives the useful slogan

\[
\boxed{
\text{recursion can relocate closure; it cannot erase its logical cost.}
}
\]

## 11. Configuration-sort attempt

Another natural attempt introduces a configuration sort

\[
C_m=G_m^2
\]

and a local synchronized step

\[
(a,c)\mapsto(\operatorname{Succ}(a),\operatorname{Succ}(c)).
\]

The local step itself is weak. EqGap is again reachability in this configuration graph.

If the configuration sort is merely the Cartesian product with only local product-successor incidence, ordinary FO still has no transitive closure. Adding a primitive relation saying that one configuration reaches another is exactly adding the missing closure relation.

Thus a product sort by itself does not solve the internalization problem.

## 12. Fiber-only encoding needs unboundedly many gap labels

There is also a simple value-fiber obstruction.

Let

\[
I_m=\{(a,b):a\le b\}
\]

be forward intervals, and suppose a value map

\[
c:I_m\to O_m
\]

is required to satisfy

\[
\operatorname{EqGap}(I,J)
\iff
c(I)=c(J).
\]

There are exactly \(m\) possible interval lengths \(0,1,\dots,m-1\). Different lengths must receive different values. Therefore

\[
\boxed{|O_m|\ge m.}
\]

Hence a bounded anonymous output alphabet cannot encode EqGap purely as equality of interval-output fibers.

Bounded outputs remain possible if EqGap is stored in **domain placement** instead, but then the domain itself is the nonregular AL1 relation and closure has again been compiled into the operation.

## 13. What the synchronized-head result really established

The synchronized two-head mechanism is best read as a **generator theorem**:

\[
\boxed{
\text{a weak local product step + unbounded synchronized closure generates EqGap.}
}
\]

It is not yet a theorem that ordinary FCOA first-order semantics automatically contains that closure.

The Regular-Primitive Barrier now makes the missing ingredient exact.

Therefore the previous working slogan

\[
H_2^{\mathrm{sync}}=AL1
\]

should be read as

\[
\boxed{
H_2^{\mathrm{sync}}+\text{unbounded traversal semantics}=AL1,
}
\]

not as a claim that two local operation symbols alone reach AL1.

## 14. Central negative answer

The targeted question was:

\[
\text{Can synchronized transport be realized inside two ordinary weak FCOA partial operations without explicit transitive closure?}
\]

Within finite-copy, local/finite-state, static FO semantics, the answer is

\[
\boxed{\textbf{No}.}
\]

If the two operations remain position-regular, Theorem 6.1 blocks EqGap.

If one operation is recursively completed until it transports arbitrary gaps, its graph is already nonregular and the closure has merely moved into that primitive operation.

So the scientific boundary is not “one operation versus two operations.” It is

\[
\boxed{
\text{regular local primitives}
\quad\text{versus}\quad
\text{materialized/unbounded closure}.
}
\]

## 15. New optimization problem

The main line should therefore stop asking whether two weak local operations can magically create Add by finite FO interaction. They cannot in the stated class.

The next genuine optimization problem is:

\[
\boxed{
\text{What is the cheapest nonregular but non-oracular primitive memory that materializes synchronized closure?}
}
\]

Three concrete representations should be compared:

1. **active-output addition graph** — quadratic operation domain \(\Theta(m^2)\);
2. **domain-compiled EqGap** — one terminal output but \(\Theta(m^3)\) four-ary support on interval pairs;
3. **history/nesting materialization** — add intermediate witness objects generated locally and ask whether their total number/support can be made subquadratic while FO exposing equal displacement.

The third route is now the strongest candidate for a genuinely FCOA-native improvement because it may turn unbounded traversal into explicit finite composition witnesses rather than importing a numerical function.

## 16. Connection to sandbox nesting

The sandbox-atomicity direction supplies a natural language for well-founded predecessor depth. However, ordinal rank there is a semantic invariant of the factor relation; it is not automatically an FO-definable function inside the reduct.

Therefore simply observing that two objects have equal nesting depth would already use a rank-comparison mechanism stronger than the local factor graph.

A central bridge would require **materializing depth witnesses** inside FCOA so that equal depth becomes first-order visible without naming numerical ranks.

This is precisely the history/nesting route in Section 15.

## 17. Status

The mathematical closure argument is fixed in the following stated scope:

\[
\boxed{
\mathbf F:\ \text{finite-copy position-regular primitive expansions cannot FO-define EqGap/Add.}
}
\]

\[
\boxed{
\mathbf F:\ \text{bounded-output pure fiber coding of EqGap requires }|O_m|\ge m.
}
\]

The programme-level formulation remains working terminology:

\[
\boxed{
\mathbf W:\ \text{Closure-Placement Principle / Regular-Primitive Barrier terminology.}
}
\]

No new G5 operation is accepted here.