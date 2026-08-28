# FCOA Hybrid Memory — Rigidity without Order

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; proof architecture complete; hostile audit required  
**External calibration:** standard Gaifman locality for first-order logic is used as a classical finite-model-theory ingredient. No novelty claim is made for the locality theorem itself.

## 1. Purpose

The rigid-tree example showed that finite rigidity can coexist with failure of uniform first-order order recovery. The aim here is to extract a structural criterion that applies to an entire natural class of incidence skeletons rather than to one hand-built family.

The conclusion will be:

\[
\boxed{
\text{unbounded joint value rigidity}
\quad+
\text{no uniform FO total order}.
}
\]

The key separation is between **global asymmetry** and **local indistinguishability**.

## 2. Incidence compiler reminder

For a finite bipartite graph

\[
B=(L,R;E),
\]

with no isolated vertices, let

\[
\mathcal H(B)=(L\sqcup R\sqcup E;\oplus,\otimes)
\]

be the one-sorted two-operation structure

\[
e\oplus e=\ell(e),
\qquad
e\otimes e=r(e),
\]

for every `e\in E`, with all other cells undefined.

The previous incidence-transfer theorem gives

\[
\boxed{
\operatorname{Aut}(\mathcal H(B))
\cong
\operatorname{Aut}_{\rm bip}(B).
}
\]

After Value-Erasure,

\[
\boxed{
\operatorname{Aut}(D_\oplus,D_\otimes)
\cong
S_{|E|}\times S_{|L|+|R|}.
}
\]

Thus rigidity of `B` yields complete joint rigidity, while definedness retains factorial symmetry.

## 3. Local-swap property

Let `\mathcal C=(B_n)_{n\in I}` be an infinite family of finite bipartite graphs with `|B_n|\to\infty`.

Call `\mathcal C` **Gaifman-locally swappable** if for every radius

\[
r\ge1
\]

there is some sufficiently large member `B_n` containing two distinct vertices

\[
x_n,y_n
\]

in the same bipartition class such that:

1. their graph distance satisfies

\[
\operatorname{dist}(x_n,y_n)>2r;
\]

2. the rooted radius-`r` neighborhoods

\[
N_r(B_n,x_n),
\qquad
N_r(B_n,y_n)
\]

are isomorphic as rooted bipartite graphs;

3. the two neighborhoods are disjoint.

Equivalently, the radius-`r` neighborhood of the ordered pair `(x_n,y_n)` is isomorphic to that of `(y_n,x_n)` by a local isomorphism exchanging the two roots.

The property is intentionally local. It does **not** require a global automorphism interchanging `x_n` and `y_n`.

## 4. Bounded-degree corridor criterion

A convenient sufficient condition for local swappability is the following.

Suppose there is a fixed degree bound `\Delta` and every sufficiently large `B_n` contains a simple path segment

\[
z_0-z_1-\cdots-z_{M_n}
\]

with

\[
M_n\to\infty,
\]

such that all internal corridor vertices have the same bounded local incidence pattern away from the two ends.

Then for every fixed radius `r`, once `M_n` is large enough one may choose two internal vertices `x_n,y_n`:

- farther than `r` from both corridor ends and every exceptional attachment;
- farther than `2r` from each other;
- in the same bipartition class.

Their rooted radius-`r` neighborhoods are then isomorphic.

This motivates the term **long homogeneous corridor**.

## 5. Rigidity-without-Order Theorem

### Theorem HM-RWO

Let `\mathcal C=(B_n)` be an infinite family of finite bipartite graphs satisfying:

1. **rigidity:**

\[
\operatorname{Aut}_{\rm bip}(B_n)=1
\]

for every `n`;

2. **unbounded size:**

\[
|V(B_n)|+|E(B_n)|\to\infty;
\]

3. **uniformly bounded degree;**

4. **Gaifman-local swappability.**

Then the compiled two-operation family

\[
\mathcal H(\mathcal C)=\{\mathcal H(B_n)\}
\]

has all of the following properties.

### (a) Every finite member is rigid

\[
\boxed{
\operatorname{Aut}(\mathcal H(B_n))=1.
}
\]

### (b) Value-induced rigidity amplification is unbounded

After Value-Erasure,

\[
\operatorname{Aut}(D_\oplus,D_\otimes)
\cong
S_{|E(B_n)|}\times S_{|V(B_n)|},
\]

so the index of the full joint group is

\[
\boxed{
|E(B_n)|!\,|V(B_n)|!\to\infty.
}
\]

### (c) No uniform parameter-free FO strict total order exists

There is no single first-order formula

\[
\varphi(x,y)
\]

in the fixed language `\{\oplus,\otimes\}` that defines a strict total order on the uniformly interpretable vertex sector `L\sqcup R` of every `\mathcal H(B_n)`.

Hence, under the FCOA leakage convention,

\[
\boxed{
\mathcal H(\mathcal C)\text{ remains below AL0.}
}
\]

## 6. Proof of the order obstruction

Assume for contradiction that one formula `\varphi(x,y)` uniformly defines a strict total order on the vertex sector of every compiled member.

Encode the partial operations relationally by their operation graphs. The Gaifman graph of `\mathcal H(B_n)` is uniformly bounded-degree whenever the input bipartite graphs are uniformly bounded-degree: every edge-element is adjacent only to its two endpoint values, and every graph vertex is adjacent to its incident edge-elements.

Fix `\varphi`. Standard Gaifman locality gives a finite radius `r` governing the local information relevant to the two free variables, together with global local sentences independent of the ordering of those variables.

By local swappability, choose a sufficiently large `B_n` and vertices `x_n,y_n` such that the radius-`r` neighborhoods are disjoint and rooted-isomorphic. Since the incidence compiler is a fixed local interpretation, the corresponding radius-bounded neighborhoods in `\mathcal H(B_n)` are also isomorphic, and the union neighborhood of `(x_n,y_n)` is isomorphic to that of `(y_n,x_n)` by exchanging the two components.

The global basic-local part of Gaifman normal form has the same truth value because both tuples lie in the same finite structure. The local part is invariant under the component-exchange isomorphism. Therefore

\[
\mathcal H(B_n)\models\varphi(x_n,y_n)
\iff
\mathcal H(B_n)\models\varphi(y_n,x_n).
\]

But a strict total order on distinct points must satisfy exactly one of these two statements. Contradiction. `□`

## 7. Natural marker-corridor families

The hypotheses are not restricted to the earlier `T_m` example.

A broad construction is obtained as follows.

Take a fixed finite rooted bipartite **marker gadget** `M` with distinguished attachment vertex `\rho`, chosen so that every bipartition-preserving automorphism of `M` fixes `\rho` and is trivial.

Attach to `\rho` a path

\[
\rho-z_1-z_2-\cdots-z_n
\]

whose length tends to infinity. Optionally attach a second fixed terminal gadget at `z_n`, provided its rooted type is different from the marker end and the resulting total graph remains rigid.

If the marker fixes the attachment end, then every automorphism fixes the path pointwise by distance from `\rho`. Hence each finite graph is rigid.

At the same time, the middle of the growing path is an arbitrarily long homogeneous corridor. Therefore the family is Gaifman-locally swappable and satisfies HM-RWO.

Thus the theorem applies to an entire natural class of **rigid marker-corridor graphs**.

## 8. Earlier rigid trees as a special case

The family

\[
p_0-p_1-\cdots-p_m
\]

with an attached two-edge branch

\[
p_1-q_1-q_2
\]

is a marker-corridor family:

- the unique degree-3 vertex and unequal short branches form a finite asymmetric marker near one end;
- the long branch supplies the homogeneous corridor;
- rigidity follows globally from the marker;
- FO order fails locally in the corridor.

So the previous tree theorem is not isolated; it is the first concrete member of HM-RWO.

## 9. Why rigidity does not rescue order

For each fixed finite `B_n`, rigidity implies that every element is fixed by every automorphism. In a finite structure this means each singleton is definable by some parameter-free first-order formula **depending on that particular structure**.

What HM-RWO blocks is a single formula working uniformly across the entire growing family.

The distinction is therefore exact:

\[
\boxed{
\text{pointwise rigidity of every finite member}
\not\Rightarrow
\text{uniform FO coordinate system}.
}
\]

Long homogeneous corridors force the defining quantifier depth needed to distinguish distant positions to grow with the structure.

## 10. Memory size versus logical strength

The theorem gives families with

\[
\operatorname{Aut}(\mathcal H(B_n))=1,
\]

and factorially growing value-rigidity amplification

\[
|E(B_n)|!\,|V(B_n)|!,
\]

while still forbidding uniform order.

Thus three quantities are provably independent at this level:

1. size of the automorphism collapse;
2. finite rigidity;
3. uniform first-order order/arithmetic strength.

In particular,

\[
\boxed{
\text{unbounded memory capacity}
\not\Rightarrow
AL0.
}
\]

## 11. Stronger locality formulation

Bounded degree and literal path corridors are convenient sufficient hypotheses, not the conceptual core.

The actual order obstruction only needs the following **tuple-swap locality property**:

> For every FO locality radius `r`, some member contains distinct points `x,y` in the intended ordered sector such that the relevant radius-`r` neighborhoods of `(x,y)` and `(y,x)` are isomorphic.

Any rigid family with this property defeats uniform FO strict order, regardless of whether the locally repeated geometry is a path, strip, tree corridor, repeated cell complex, or another bounded relational pattern.

This is the natural general interface for future FCOA skeletons.

## 12. Arithmetic firewall consequence

If a candidate hybrid skeleton family is rigid but satisfies tuple-swap locality on an unbounded sector, then it cannot be at AL0.

Consequently it cannot uniformly recover canonical ordered rank addition or EqGap on that sector in any way that would first-order recover the corresponding total order.

No blanket claim is made about arbitrary non-order arithmetic interpretations on unrelated definable quotients. The theorem is an order-wall result, not a universal decidability theorem.

## 13. Branch-level criterion

The SOL-HYBRID branch can now use the following practical test.

A growing skeleton family is a **safe rigidity-without-order candidate** if it has:

- a fixed finite signature;
- uniformly bounded Gaifman degree;
- rigid finite members;
- unbounded Value-Erasure automorphism groups;
- arbitrarily large regions of repeated local type allowing tuple swap.

If all five hold, then one should expect large joint memory without uniform AL0 leakage, and HM-RWO supplies the formal proof route.

## 14. Current conclusion

The rigid-tree phenomenon extends to a structural class:

\[
\boxed{
\text{global rigid marker}
+
\text{unbounded locally homogeneous corridor}
}
\]

produces

\[
\boxed{
\text{finite rigidity}
+
\text{unbounded value-memory}
+
\text{failure of uniform FO order}.
}
\]

This is the desired **Rigidity-without-Order theorem pattern** for the fixed-two-operation FCOA incidence compiler.
