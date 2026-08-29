# FO Boundary — Infinite Carrier Memory

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Status:** working theorem checkpoint  
**Scope:** infinite generic carrier only; no change to the finite M0-G4 programme

## 1. Canonical infinite ray

Let

\[
G_\omega=\{P_2,P_3,P_4,\ldots\}
\]

and let

\[
S(x,y)
\]

mean directed generic adjacency:

\[
S(P_i,P_j)\iff j=i+1.
\]

Write

\[
x<_{\rm ray}y
\]

for the transitive successor order:

\[
x<_{\rm ray}y
\iff
\exists n\ge1\; S^n(x,y).
\]

The least generic point is first-order definable:

\[
\operatorname{Root}(x):=\neg\exists z\,S(z,x).
\]

Thus \((G_\omega,S)\) is definitionally equivalent, after naming its definable root, to the standard successor structure \((\mathbb N,0,S)\).

## 2. Typed infinite G2

Let \(O=\{\Omega\}\) be a singleton terminal-output sort and define

\[
x\star y=\Omega\iff S(x,y).
\]

Equivalently,

\[
S(x,y)\iff \operatorname{Def}(x\star y).
\]

Hence the typed infinite G2 operation and the successor ray are first-order interdefinable on the generic sort.

This immediately separates two questions:

1. local successor memory is FO-recoverable;
2. global transitive order need not be FO-recoverable.

## 3. Main theorem: successor does not FO-define full order

### Theorem FO-1 — Infinite G2 FO boundary

There is no first-order formula \(\varphi(x,y)\) in the successor language, equivalently in the typed constant-output G2 language, such that

\[
\varphi(x,y)\iff x<_{\rm ray}y
\]

for all \(x,y\in G_\omega\).

### Proof

Use quantifier elimination for the complete theory of \((\mathbb N,0,S)\). Every formula \(\varphi(x,y)\) is equivalent there to a Boolean combination of atomic equalities between successor terms

\[
S^m(u)=S^n(v),
\qquad u,v\in\{x,y,0\}.
\]

Let \(K\) be the largest successor exponent occurring in such a quantifier-free equivalent.

Choose \(a<b\) so that

\[
a>K,
\qquad
b-a>K.
\]

Then every cross-equality between bounded successor iterates of \(a\) and \(b\) is false in both orientations, every equality to a bounded successor iterate of \(0\) is false for both points, and all same-variable atomic equalities have the same truth value after swapping \(a,b\).

Therefore the full quantifier-free type of \((a,b)\) is the same as that of \((b,a)\), so

\[
\varphi(a,b)\iff\varphi(b,a).
\]

But

\[
a<_{\rm ray}b
\qquad\text{and}\qquad
\neg(b<_{\rm ray}a).
\]

Contradiction. \(\square\)

### Literature checkpoint

This is a classical model-theoretic boundary for successor structures. Enderton proves quantifier elimination for the natural numbers with zero and successor; Doets records explicitly the exercise that \(<\) is not definable in \((\mathbb N,S)\). The present FCOA contribution is not the classical nondefinability theorem itself, but its exact placement inside the domain-compilation / value-memory ladder.

## 4. Rigidity does not imply FO global memory

### Corollary FO-1A

\[
\operatorname{Aut}(G_\omega,S)=1,
\]

but \(<_{\rm ray}\) is not FO-definable.

Proof: the unique root is fixed, then its successor is fixed, and inductively every point is fixed. Combine this rigidity with Theorem FO-1. \(\square\)

Thus the infinite ray is an explicit counterexample to

\[
\boxed{\operatorname{Aut}=1\ \Longrightarrow\ \text{all canonical global geometry is FO-definable}.}
\]

This is the central warning for the infinite FCOA branch.

## 5. Finite parameters do not help

### Corollary FO-1B

Full order is not FO-definable from successor even with an arbitrary finite tuple of parameters.

Reason: every point of the standard ray is already parameter-free definable from the unique root by a finite successor chain. Hence adjoining finitely many parameters does not create a new definability class; each parameter can be replaced by its parameter-free defining formula. \(\square\)

## 6. Full M0+G2 decoration does not create order

Consider the canonical infinite M0+G2 multiplication decoration with:

- boundary points \(P_0,P_1\);
- generic ray \(G_\omega\);
- copies \(E_i^\ast,E_i^\times\) attached to each generic point;
- one terminal G2 output \(\Omega\);
- the same M0 multiplication laws as in the finite family;
- exactly the G2 cells \(P_i\otimes P_{i+1}=\Omega\).

This structure is a finite-copy first-order interpretation of the successor ray: \(P_0,P_1,\Omega\) are finitely many tags, the \(E^\ast\)- and \(E^\times\)-families are two tagged copies of \(G_\omega\), and every operation-graph clause is definable using only equality, the tags, and \(S\).

Consequently every first-order relation on the generic sort definable in this decorated structure pulls back to a first-order relation in \((G_\omega,S)\).

### Theorem FO-2 — Decorated G2 boundary

The full strict order on \(G_\omega\) is not FO-definable in the canonical infinite M0+G2 decoration.

This theorem is invariant under switching between the typed partial-operation presentation and its relational graph presentation.

## 7. Local value enrichments remain below the boundary

Any finite enrichment whose added relations/partial-operation layers are themselves FO-definable from bounded successor patterns is a definitional expansion of the successor ray. Therefore it cannot make \(<_{\rm ray}\) FO-definable.

In particular, the following do **not** cross the boundary:

- naming the root;
- naming finitely many generic points;
- adding predecessor as a relation or function;
- adding finitely many fixed-distance jump relations \(S^k\);
- coloring only successor/reverse-successor cells by finitely many named or anonymous terminal values;
- adding a finite number of local boundary anchors of the G3 type.

Hence an infinite local G3 analogue may be rigid and may distinguish edge orientation in values, but it still does not FO-recover unbounded transitive order.

## 8. Logical-strength separation

### FO

\[
S\ \text{definable},
\qquad
<_{\rm ray}\ \text{not definable}.
\]

### FO+TC on the successor relation

With a transitive-closure operator,

\[
x<_{\rm ray}y
\iff
x\ne y\wedge \operatorname{TC}(S)(x,y).
\]

So the order boundary is crossed immediately once transitive closure is admitted.

### MSO

MSO also defines reachability/order. One standard formula is

\[
x\le_{\rm ray}y
\iff
\forall X\Bigl(
X(x)\wedge
\forall u\forall v((X(u)\wedge S(u,v))\to X(v))
\to X(y)
\Bigr).
\]

Strict order adds \(x\ne y\).

### Computable recoverability

In a computable presentation of a single successor ray with computable successor, order is decidable even though it is not FO-definable. Given distinct \(x,y\), dovetail the two forward orbits

\[
x,Sx,S^2x,\ldots
\qquad\text{and}\qquad
y,Sy,S^2y,\ldots.
\]

Exactly one orbit reaches the other, determining the order.

Therefore

\[
\boxed{
\text{FO definability}
\;<\;
\text{FO+TC/MSO reachability}
\;<\;\text{algorithmic reconstruction}
}
\]

must be treated as three distinct memory notions.

## 9. Uniform finite-family boundary

For each fixed finite ray

\[
G_N=P_2\to\cdots\to P_N,
\]

full order is FO-definable by the finite disjunction

\[
x<_{N}y
\iff
\bigvee_{1\le k\le N-2} S^k(x,y).
\]

The formula depends on \(N\).

### Theorem FO-3 — No uniform finite full-order formula

There is no single FO formula \(\varphi(x,y)\) that defines the full strict order on every finite directed ray \(G_N\).

Proof method: the standard Ehrenfeucht-Fraisse distance strategy on sufficiently long paths. For every quantifier rank \(q\), choose two points \(a<b\) whose distances from both endpoints and from each other exceed the corresponding \(2^q\)-scale. The pointed paths \((G_N,a,b)\) and \((G_N,b,a)\) are \(q\)-equivalent, while strict order separates them. \(\square\)

Thus

\[
\boxed{
\text{per-}N\text{ definability}
\not\Rightarrow
\text{uniform finite-family definability}
\not\Rightarrow
\text{infinite FO definability}.
}
\]

## 10. A natural FCOA enrichment that *does* cross the boundary

Consider the infinite complete comparison-value layer on \(G_\omega\): for distinct generic points,

\[
x\chi y=
\begin{cases}
\Omega_+,&x<_{\rm ray}y,\\
\Omega_-,&y<_{\rm ray}x,
\end{cases}
\]

with exactly two distinct anonymous terminal outputs and complete off-diagonal domain.

This is the infinite fixed-carrier analogue of the G4-C value geometry, studied here only as an infinite enrichment; it does not promote finite G4 status.

### Theorem FO-4 — Endpoint breaks anonymous output symmetry

In the infinite ray, \(\Omega_+\) is first-order definable even if the two outputs are initially anonymous.

Define

\[
\operatorname{Positive}(z):=
\exists r\Bigl(
\forall y\,(y\ne r\to r\chi y=z)
\Bigr).
\]

The least point has every off-diagonal outgoing comparison value equal to \(\Omega_+\), so \(\operatorname{Positive}(\Omega_+)\) holds. No point has all outgoing comparison values equal to \(\Omega_-\), because the ray has no greatest point. Hence exactly \(\Omega_+\) satisfies this property.

Therefore

\[
\boxed{
x<_{\rm ray}y\iff x\ne y\wedge x\chi y=\Omega_+.}
\]

So two anonymous terminal values suffice to make full order FO-definable on the infinite ray.

### Finite/infinite contrast

For a finite linear carrier, reversal can exchange \(\Omega_+\) and \(\Omega_-\), giving the finite G4-C residual \(C_2\). On \(\omega\), there is a least point but no greatest point, so reversal is not an automorphism and the two anonymous fibers become intrinsically distinguishable.

This is a genuine finite-to-infinite non-transfer phenomenon.

## 11. Minimality inside the complete-domain terminal-color family

With one terminal value on every off-diagonal pair, the value layer carries no orientation at all and the generic complete domain has full symmetric automorphism group. Hence full order cannot be recovered.

With two values, Theorem FO-4 recovers full order.

Therefore, within the complete-domain constant-terminal-color architecture,

\[
\boxed{|O|=2}
\]

is minimal for FO recovery of the absolute order of the infinite ray.

## 12. Current boundary picture

\[
\boxed{
\begin{array}{c}
\text{G2 successor/domain memory}\\
\Downarrow\\
\text{rigid infinite ray, but no FO full order}\\
\Downarrow\\
\text{finite/local G3-style decorations still no FO full order}\\
\Downarrow\\
\text{global two-fiber comparison layer}\\
\Downarrow\\
\text{FO full order recovered}
\end{array}}
\]

The operative distinction is therefore not simply rigidity versus symmetry. It is:

\[
\boxed{
\text{bounded/local directed memory}
\quad\big|\quad
\text{unbounded pairwise comparison memory}.
}
\]
