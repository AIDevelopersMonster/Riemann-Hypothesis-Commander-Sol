# Presburger Compression Barrier — A Sharp Quadratic Lower Bound

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem checkpoint  
**Scope:** fixed finite-signature, unvaried, base-sorted Presburger-definable primitive relations on the recovered generic order

## 1. Central problem

The Binary-History construction showed that a generated `BIT`-type history with

\[
\Theta(m\log m)
\]

support can recover truncated addition, but it overshoots to full finite arithmetic. The natural selective-compression problem is therefore:

\[
\boxed{
\text{Can one choose a Presburger-definable primitive memory }R
\text{ with }|R\cap[m]^r|=o(m^2)
}
\]

such that truncated addition is uniformly first-order definable from \((<,R)\)?

In the exact class declared below, the answer is **no**, and the quadratic bound is sharp.

## 2. Exact model

Let

\[
\mathcal R=(R_1,\ldots,R_s)
\]

be a fixed finite family of **unvaried** numerical predicates

\[
R_i\subseteq\mathbb N^{r_i}.
\]

Assume each \(R_i\) is Presburger-definable in

\[
(\mathbb N,<,+).
\]

For the finite generic chain of size \(m\), use the truncations

\[
R_{i,m}=R_i\cap[m]^{r_i}.
\]

Define total primitive support

\[
C_{\mathcal R}(m)
:=
\sum_{i=1}^s |R_i\cap[m]^{r_i}|.
\]

The question is whether canonical truncated addition

\[
\operatorname{Add}_m(x,y,z)
\iff
x+y=z<m
\]

can be defined by one first-order formula uniformly in

\[
([m],<,R_{1,m},\ldots,R_{s,m}).
\]

The predicates do not depend on the final size \(m\). Auxiliary growing sorts, size-dependent moduli, varied predicates, growing signatures and transitive-closure semantics are outside this theorem.

## 3. Classical semilinear input

By the Ginsburg–Spanier characterization, Presburger-definable subsets of \(\mathbb N^r\) are exactly the semilinear sets: finite unions of linear sets

\[
a+\mathbb N p_1+\cdots+\mathbb N p_k.
\]

Reference: Seymour Ginsburg and Edwin H. Spanier, “Semigroups, Presburger formulas, and languages,” *Pacific Journal of Mathematics* 16(2) (1966), 285–296, DOI `10.2140/pjm.1966.16.285`.

No novelty is claimed for semilinearity itself.

## 4. Semilinear growth dichotomy below degree two

### Lemma 4.1 — rank-two component forces quadratic support

Let

\[
L=a+\mathbb N p_1+\cdots+\mathbb N p_k\subseteq\mathbb N^r
\]

be a linear set. If the \(\mathbb Q\)-span of its period vectors has dimension at least two, then

\[
|L\cap[m]^r|=\Omega(m^2).
\]

### Proof

Choose two \(\mathbb Q\)-independent nonzero period vectors \(p,q\). Because their coordinates are fixed nonnegative integers, there is a constant \(c>0\) such that for all sufficiently large \(m\), every point

\[
a+up+vq,
\qquad
0\le u,v\le cm,
\]

lies in \([m]^r\). Independence makes these \(\Theta(m^2)\) points distinct. \(\square\)

### Corollary 4.2

If a semilinear set \(R\subseteq\mathbb N^r\) satisfies

\[
|R\cap[m]^r|=o(m^2),
\]

then every linear component in a semilinear decomposition has period rank at most one.

Consequently such an \(R\) is, after finite decomposition, a union of finite sets and one-dimensional arithmetic rays.

In particular there is no genuinely intermediate fixed-Presburger growth regime such as \(m\log m\): every rank-at-most-one component contributes \(O(m)\), so

\[
\boxed{
|R\cap[m]^r|=o(m^2)
\Longrightarrow
|R\cap[m]^r|=O(m).
}
\]

## 5. Rank-one Presburger relations reduce to finite-degree predicates

Consider one arithmetic ray

\[
L=\{a+nv:n\ge0\}.
\]

Coordinates with \(v_j=0\) are fixed constants. Since every fixed natural number is parameter-free definable from finite order by a fixed formula, these coordinates require no new numerical predicate.

Project to the coordinates with \(v_j>0\).

- If no coordinate varies, the component is finite.
- If exactly one coordinate varies, the remaining condition is unary. Every unvaried unary numerical predicate is finite-degree.
- If at least two coordinates vary, each fixed natural number can occur in only finitely many tuples of the projected ray: each varying coordinate determines the ray parameter \(n\) up to at most finitely many possibilities. Hence the projected relation is finite-degree.

Finite unions preserve first-order definability from finitely many such predicates.

Therefore:

### Lemma 5.1

Every unvaried Presburger-definable relation of subquadratic box support is first-order definable from

\[
<
\]

plus finitely many **finite-degree numerical predicates** in the sense of Cadilhac–Paperman.

For reference, an unvaried predicate \(P\subseteq\mathbb N^k\) is finite-degree when every natural number occurs in only finitely many tuples of \(P\).

## 6. The finite-degree obstruction to addition

Cadilhac and Paperman prove that

\[
FO[\le,FIN]
\]

has the strong Crane Beach Property, and as an application prove that it cannot “sum through” any nondecreasing unbounded function.

Their definition says that a logic sums through \(f\) if it can define uniformly

\[
a=b+f(c).
\]

Reference: Michaël Cadilhac and Charles Paperman, “A Crevice on the Crane Beach: Finite-Degree Predicates,” LICS 2017, DOI `10.1109/LICS.2017.8005148`, especially Theorem 5 and Proposition 4.

Canonical truncated addition would sum through the identity function

\[
f(c)=c,
\]

which is unbounded. Hence

\[
\boxed{
\operatorname{Add}
\notin
FO[<,FIN].
}
\]

## 7. Presburger Compression Barrier

### Theorem 7.1 — sharp quadratic lower bound

Let \(R_1,\ldots,R_s\) be a fixed finite family of unvaried Presburger-definable numerical predicates. If canonical truncated addition is uniformly first-order definable in

\[
([m],<,R_{1,m},\ldots,R_{s,m}),
\]

then

\[
\boxed{
C_{\mathcal R}(m)=\Omega(m^2).
}
\]

### Proof

Suppose instead that

\[
C_{\mathcal R}(m)=o(m^2).
\]

Since the summands are nonnegative, each \(R_i\) has subquadratic support. By Lemma 5.1 every \(R_i\) is first-order definable from order plus finitely many finite-degree predicates. Therefore every formula over

\[
(<,R_1,\ldots,R_s)
\]

translates into \(FO[<,FIN]\).

If truncated addition were definable from the \(R_i\), it would therefore be definable in \(FO[<,FIN]\). But addition sums through the unbounded identity function, contradicting Cadilhac–Paperman Proposition 4. \(\square\)

## 8. Sharpness

The addition graph itself is Presburger-definable and has exactly

\[
|\operatorname{Add}_m|
=
|\{(x,y,z):x+y=z<m\}|
=
\sum_{x=0}^{m-1}(m-x)
=
\frac{m(m+1)}2.
\]

Thus

\[
|\operatorname{Add}_m|=\Theta(m^2).
\]

Combining with Theorem 7.1:

\[
\boxed{
\min_{\substack{\mathcal R\text{ fixed unvaried Presburger}\\
\operatorname{Add}\in FO(<,\mathcal R)}}
C_{\mathcal R}(m)
=
\Theta(m^2).
}
\]

This solves the selective Presburger Compression Corridor **exactly in the declared base-sorted unvaried model**.

## 9. Consequence for the earlier binary-history result

The generated BIT history achieved

\[
\Theta(m\log m)
\]

support and recovered addition. Theorem 7.1 explains why this cannot happen inside fixed unvaried Presburger geometry:

\[
\boxed{
\Theta(m\log m)\text{ additive compression necessarily leaves this Presburger class.}
}
\]

BIT does exactly that and consequently permits the previously observed arithmetic overshoot.

The contrast is now structural rather than anecdotal:

\[
\boxed{
\text{Presburger-selective base memory: quadratic floor}
}
\]

versus

\[
\boxed{
\text{non-Presburger distributed memory: subquadratic compression possible.}
}
\]

## 10. Why CRT auxiliary-carrier constructions are not counterexamples

A family that, for each final size \(m\), chooses moduli

\[
p_m,q_m,\ldots
\]

and introduces residue sorts or modular tables depending on those moduli is **varied** and uses auxiliary growing carriers. It is not represented by one fixed finite family of unvaried base-sort predicates

\[
R_i\subseteq\mathbb N^{r_i}.
\]

Therefore linear-cost CRT presentations lie outside Theorem 7.1.

This is not a defect in such constructions. It means their cost vector must include the complexity/provenance of the size-dependent modulus scaffold and the auxiliary carriers. Raw record count and base-sorted Presburger support are different resource models.

## 11. Scope firewall

The theorem does **not** prove a universal quadratic lower bound for every FCOA encoding of addition.

It leaves open:

1. varied but provenance-restricted predicates depending on final carrier size;
2. auxiliary sorts whose total size is separately charged;
3. growing signatures;
4. generated non-Presburger histories;
5. fixed-point/reachability/closure semantics;
6. interpretation-based encodings whose base-sort trace is sparse but whose auxiliary representation carries additional resolution.

The claim is exactly:

\[
\boxed{
\text{fixed finite-signature}
+
\text{unvaried}
+
\text{base-sorted}
+
\text{Presburger primitives}
\Longrightarrow
\text{quadratic additive floor}.}
\]

## 12. Central consequence

The original Presburger Compression Corridor bifurcates.

### Base-sorted unvaried corridor

Closed:

\[
\boxed{
\text{exact optimum}=\Theta(m^2).
}
\]

### Extended representation corridor

Still open:

\[
\boxed{
\text{Can a provenance-safe varied or auxiliary-sort FCOA realization achieve }o(m^2)
}
\]

while remaining genuinely AL1 and not smuggling/defining multiplication?

This is now the next correct central question.

## 13. Status

\[
\boxed{
\mathbf F:\ \text{Presburger Compression Barrier in the declared model.}
}
\]

\[
\boxed{
\mathbf F:\ \Theta(m^2)\text{ is asymptotically sharp.}
}
\]

\[
\boxed{
\mathbf O:\ \text{extended varied/auxiliary-sort selective compression.}
}
\]

`Presburger Compression Barrier` is programme terminology; the semilinear and finite-degree ingredients are classical and explicitly attributed.