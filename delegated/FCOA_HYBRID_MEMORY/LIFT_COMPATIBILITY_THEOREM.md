# FCOA Hybrid Memory — Lift Compatibility Theorem

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; internally proved; hostile audit required  
**Priority discipline:** the abstract automorphism/stabilizer/pullback principle is not claimed as novel. The FCOA-specific content is the tagged-operation formulation, the separation of carrier and lift obstructions, and the minimal JFS witness.

## 1. Relative typed setup

Let `X` be an active sort and `O` a common pure terminal-output sort. Let

\[
\star_i:D_i\rightharpoonup O,
\qquad i=1,\ldots,k,
\]

be partial operations of arities `r_i`, where

\[
D_i\subseteq X^{r_i}.
\]

Outputs are terminal: no element of `O` is used as an active argument in this layer. Operation symbols are distinguished.

Define the **tagged cell set**

\[
T=\bigsqcup_{i=1}^k \bigl(\{i\}\times D_i\bigr).
\]

Let

\[
c:T\to O
\]

be the global value map

\[
c(i,p)=\star_i(p).
\]

Assume first that every element of `O` is used by at least one operation cell, so `c` is surjective.

Let

\[
\Gamma_D
=
\{g\in\operatorname{Sym}(X):gD_i=D_i\text{ for every }i\}
\]

be the automorphism group of the joint definedness reduct on the active sort. It acts on `T` by

\[
g(i,p)=(i,gp).
\]

Define the global value-fiber equivalence on tagged cells:

\[
t\equiv_c t'
\iff
c(t)=c(t').
\]

Crucially, `\equiv_c` is allowed to relate cells belonging to **different operation symbols**.

## 2. Joint Fiber-Transport / Lift-Compatibility Theorem

### Theorem HM-LC

Restriction to the active sort gives a canonical isomorphism

\[
\boxed{
\operatorname{Aut}(X,O;\star_1,\ldots,\star_k)
\cong
\operatorname{Stab}_{\Gamma_D}(\equiv_c).
}
\]

Equivalently, a carrier permutation survives the full joint reduct exactly when it preserves the equality partition of **all tagged operation cells simultaneously**.

### Proof

Let `(g,h)` be an automorphism of the joint structure, with `g` acting on `X` and `h` on `O`. Since operation symbols are distinguished, `g` preserves every `D_i`, hence `g\in\Gamma_D`.

For every tagged cell `t=(i,p)`, automorphism preservation gives

\[
h(c(t))=c(gt).
\]

Therefore if `c(t)=c(t')`, then

\[
c(gt)=h(c(t))=h(c(t'))=c(gt').
\]

Applying the inverse automorphism gives the converse implication, so `g` preserves `\equiv_c`.

Conversely, let `g\in\Gamma_D` preserve `\equiv_c`. Define

\[
h(c(t)):=c(gt).
\]

This is well-defined because equality of `c(t)` values is exactly `\equiv_c`, which `g` preserves. Surjectivity of `c` defines `h` on all of `O`. Applying the same argument to `g^{-1}` shows that `h` is bijective. Then

\[
h(\star_i(p))=\star_i(gp)
\]

for every `i` and every `p\in D_i`, so `(g,h)` is an automorphism. Surjectivity makes `h` uniquely determined by `g`. `□`

## 3. Why separate reducts can mislead

For one operation `\star_i`, let `\equiv_i` be the restriction of global value equality to the cells tagged by `i`.

Define

\[
\Gamma_{\mathrm{sep}}
=
\{g\in\Gamma_D:
 g\text{ preserves every }\equiv_i\text{ separately}\}.
\]

This group records everything visible from the value partitions of the operations **when cross-operation equality of outputs is ignored**.

The joint group is

\[
\Gamma_{\mathrm{joint}}
=
\operatorname{Stab}_{\Gamma_D}(\equiv_c).
\]

Always

\[
\boxed{
\Gamma_{\mathrm{joint}}
\le
\Gamma_{\mathrm{sep}}
\le
\Gamma_D.
}
\]

The first inclusion may be strict because `\equiv_c` contains additional relations of the form

\[
\star_i(p)=\star_j(q),
\qquad i\ne j.
\]

These are invisible in either operation's internal fiber partition considered alone.

## 4. Lift-set formulation

For each operation and each active permutation preserving its domain, define the set of compatible output lifts

\[
L_i(g)
=
\{h\in\operatorname{Sym}(O):
 h(\star_i(p))=\star_i(gp)
 \text{ for all }p\in D_i\}.
\]

Then the carrier projection of the full joint automorphism group is exactly

\[
\boxed{
\pi_X\operatorname{Aut}(\star_1,\ldots,\star_k)
=
\left\{
 g\in\Gamma_D:
 \bigcap_{i=1}^k L_i(g)\ne\varnothing
\right\}.
}
\]

Thus joint failure can occur even when

\[
g\in\pi_X\operatorname{Aut}(\star_i)
\]

for every `i`: the separate lift sets can be nonempty but have empty common intersection.

This is the precise **lift-compatibility obstruction**.

### Surjective-per-operation corollary

If every individual map

\[
\star_i:D_i\to O
\]

is surjective, then any compatible output lift is uniquely determined. Write it as

\[
\lambda_i(g)\in\operatorname{Sym}(O).
\]

Then

\[
\boxed{
\pi_X\operatorname{Aut}(\star_1,\ldots,\star_k)
=
\{g\in\Gamma_D:
\lambda_1(g)=\cdots=\lambda_k(g)\}.
}
\]

Hence the joint carrier group is an **equalizer of forced output actions**.

## 5. Independent-output regime as a special case

If the operations use disjoint output sorts

\[
O_1,\ldots,O_k
\]

rather than one common `O`, there is no cross-operation equality relation to preserve. The global tagged fiber partition is simply the disjoint union of the individual partitions.

Then

\[
\Gamma_{\mathrm{joint}}=\Gamma_{\mathrm{sep}},
\]

so no JFS-type obstruction exists.

This explains exactly why the old independent-output VV lower bound was `3+3`, whereas a common output sort admits the `1+2` JFS witness.

## 6. JFS-3 as the first nontrivial case

Let

\[
X=\{a,b,c\},
\qquad O=\{u,v\},
\]

with

\[
a\oplus a=u,
\]

\[
b\otimes b=u,
\qquad c\otimes c=v.
\]

The joint definedness group is

\[
\Gamma_D=\langle(b\ c)\rangle\cong C_2.
\]

Let `r=(b c)`. Each within-operation value partition is preserved by `r`, so

\[
r\in\Gamma_{\mathrm{sep}}.
\]

But globally the tagged cells

\[
(\oplus,(a,a))
\quad\text{and}\quad
(\otimes,(b,b))
\]

lie in the same `u`-fiber, while

\[
(\otimes,(c,c))
\]

lies in the `v`-fiber. Under `r`, the first tagged cell is fixed and the latter two are exchanged. Hence `r` does not preserve the global fiber equivalence.

Therefore

\[
\boxed{
\Gamma_{\mathrm{sep}}\cong C_2,
\qquad
\Gamma_{\mathrm{joint}}=1.
}
\]

In lift language:

- `\oplus` forces `u` to stay fixed;
- the nontrivial `\otimes` symmetry forces `u\leftrightarrow v`;
- no single output permutation satisfies both.

## 7. Joint Fiber Synchronization Index

For a finite active carrier define provisionally

\[
\boxed{
\operatorname{JFSI}(\star_1,\ldots,\star_k)
=
[\Gamma_{\mathrm{sep}}:\Gamma_{\mathrm{joint}}].
}
\]

This measures rigidity contributed specifically by **cross-operation equality of output fibers**, after all within-operation domain and value information has already been imposed.

For JFS-3,

\[
\boxed{\operatorname{JFSI}=2.}
\]

`Joint Fiber Synchronization Index` is working terminology only and should not be promoted before hostile audit and prior-art review.

## 8. Three-cell lower bound revisited

Let

\[
T=\bigsqcup_i(\{i\}\times D_i)
\]

be the total tagged cell set.

If

\[
|T|\le2,
\]

every equivalence relation on `T` is invariant under every permutation of `T`: for two cells the only partitions are `2` and `1+1`. Therefore restoring a common anonymous value map cannot reduce the joint definedness automorphism group.

Hence any JFS/value-induced joint rigidity satisfies

\[
\boxed{|T|\ge3.}
\]

JFS-3 attains equality.

## 9. Exact conceptual decomposition

The hybrid programme now has two logically distinct joint-rigidity channels.

### Carrier-transversality channel

\[
\pi_X\operatorname{Aut}(\oplus)
\cap
\pi_X\operatorname{Aut}(\otimes)
=1.
\]

DD-3 and the independent-output DV/VV witnesses live here.

### Lift-incompatibility channel

\[
\pi_X\operatorname{Aut}(\oplus)
\cap
\pi_X\operatorname{Aut}(\otimes)
\ne1,
\]

but every nontrivial common carrier symmetry has incompatible output lifts. JFS-3 is the minimal example.

Thus the earlier slogan

\[
\text{hybrid rigidity}=\text{transverse residual carrier symmetries}
\]

must be replaced by

\[
\boxed{
\text{hybrid rigidity}
=
\text{carrier compatibility}
+
\text{output-lift compatibility}.
}
\]

## 10. Non-surjective and unused-output caveat

If the global map `c:T\to O` is not surjective, unused outputs form an invisible pure subset. They may be permuted independently, producing an additional kernel in the full automorphism group.

The theorem for the **active carrier projection** remains governed by preservation of the used-output fiber partition, but restriction from the full automorphism group to `X` need no longer be injective.

Therefore all exact group-isomorphism statements above assume global output surjectivity, while projection statements remain valid with the lift-set formulation.

## 11. One-sorted caveat

The theorem is relative to structurally separated active and output sorts. In a one-sorted presentation, terminal outputs can in principle mix with inactive carrier points after some operation symbols are erased.

Before upstream adoption, JFS-3 must therefore be checked in both:

1. the typed active/output model used by the Fiber-Transport theorem;
2. a one-sorted FCOA presentation with an explicit proof of whatever structural predicates separate active arguments from terminal outputs.

No one-sorted theorem is claimed here yet.

## 12. Status

The theorem follows directly from the same equality-partition argument as the existing Fiber-Transport theorem, applied to the tagged disjoint union of all operation domains.

The new substantive consequence for SOL-HYBRID is not the abstract stabilizer identity itself. It is the discovery that cross-operation equality fibers create a second source of joint memory which is invisible to the intersection of carrier projections, and that this mechanism appears at the sharp three-cell threshold.
