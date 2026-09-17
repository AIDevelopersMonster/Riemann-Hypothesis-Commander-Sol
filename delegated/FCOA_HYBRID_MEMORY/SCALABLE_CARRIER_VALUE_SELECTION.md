# FCOA Hybrid Memory — Scalable Carrier-Value Selection

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; internally proved; hostile audit required  
**Scope:** unrestricted one-sorted finite partial algebras.

## 1. Motivation

The absolute two-cell VV witness

\[
a\oplus a=u,
\qquad
a\otimes a=v
\]

shows that operation values can act as carrier selectors rather than merely as colors of domain cells.

The next question is quantitative:

> Can this one-sorted carrier-value mechanism scale, with almost no domain geometry, and how much symmetry can one value layer remove?

The answer is yes: a linear number of one-cell value layers removes a factorial amount of residual symmetry.

## 2. Selector-ladder family

Fix an integer

\[
m\ge2.
\]

Let the one-sorted universe be

\[
U_m=\{a,v_1,\ldots,v_m,w\}.
\]

Thus

\[
|U_m|=m+2.
\]

Introduce `m` distinguished binary partial-operation symbols

\[
\star_1,\ldots,\star_m.
\]

For each `i`, define exactly one operation cell:

\[
\boxed{a\star_i a=v_i.}
\]

Every other cell of every operation is undefined.

There are no named constants and no external active/output sorts.

## 3. Definedness carries essentially one bit of geometry

For every `i`,

\[
D_i=\{(a,a)\}.
\]

Therefore the entire joint definedness family merely distinguishes the point `a` and nothing else.

Hence

\[
\boxed{
\operatorname{Aut}(U_m;D_1,\ldots,D_m)
\cong S_{m+1},
}
\]

acting arbitrarily on

\[
R_0=\{v_1,\ldots,v_m,w\}.
\]

The domain geometry does not distinguish any of those `m+1` points.

## 4. Exact automorphism groups after restoring value layers

For a subset

\[
I\subseteq\{1,\ldots,m\}
\]

let

\[
\mathcal A_I=(U_m;D_j\ (j\notin I),\star_i\ (i\in I))
\]

be the structure in which precisely the value layers indexed by `I` are restored while all other operation symbols retain only their definedness relations.

Each restored equation

\[
a\star_i a=v_i
\]

fixes `v_i` individually.

No other point of `R_0` is distinguished by the displayed structure. Therefore

\[
\boxed{
\operatorname{Aut}(\mathcal A_I)
\cong S_{m+1-|I|}.
}
\]

The symmetric group acts on the unrecovered set

\[
R_I
=\{v_j:j\notin I\}\cup\{w\}.
\]

This gives the exact selector ladder

\[
\boxed{
S_{m+1}
\longrightarrow
S_m
\longrightarrow
S_{m-1}
\longrightarrow\cdots\longrightarrow
S_2
\longrightarrow1.
}
\]

The order of the group falls as

\[
(m+1)!
\to
m!
\to
(m-1)!
\to\cdots\to
2
\to1.
\]

Thus `m` one-cell value layers erase a factorial amount of symmetry while the union of all operation domains remains exactly one repeated loop.

## 5. Every value layer is essential

With all `m` values restored,

\[
\operatorname{Aut}(U_m;\star_1,\ldots,\star_m)=1.
\]

But if any one value layer, say `\star_i`, is erased back to definedness, then the two points

\[
v_i,\qquad w
\]

become interchangeable. Hence

\[
\operatorname{Aut}(U_m;\star_j\ (j\ne i),D_i)
\cong C_2.
\]

Therefore every operation-value layer is necessary for rigidity:

\[
\boxed{
\text{the family is irredundant.}
}
\]

More generally, any proper subfamily of `r<m` valued operations leaves

\[
S_{m+1-r}
\]

symmetry.

## 6. Each individual reduct remains highly nonrigid

For a single operation `\star_i`, the equation

\[
a\star_i a=v_i
\]

fixes `a` and `v_i`, while all remaining `m` points may be permuted arbitrarily. Therefore

\[
\boxed{
\operatorname{Aut}(U_m;\star_i)
\cong S_m.
}
\]

Thus the family is maximally balanced in the sense that no individual one-cell operation approaches rigidity as `m` grows.

The gap between individual and joint rigidity increases rapidly:

\[
|\operatorname{Aut}(\star_i)|=m!,
\qquad
|\operatorname{Aut}(\star_1,\ldots,\star_m)|=1.
\]

## 7. Sharp selector bound inside the common-loop template

Consider the template in which:

1. the universe is `\{a\}\cup R` with `|R|=q`;
2. every operation domain is the same singleton loop `\{(a,a)\}`;
3. every restored value is an element of `R`;
4. no additional structure exists on `R`.

After restoring `r` distinct output values, at most `r` points of `R` are fixed individually. The remaining

\[
q-r
\]

points are still freely permutable. Therefore the residual group contains

\[
S_{q-r}.
\]

Rigidity requires

\[
q-r\le1,
\]

or equivalently

\[
\boxed{r\ge q-1.}
\]

The selector ladder takes

\[
q=m+1,
\qquad r=m=q-1,
\]

and attains equality.

Hence within this zero-extra-domain-geometry template, the construction is resource-optimal.

## 8. Factorial value-rigidity amplification

Define provisionally for a one-sorted family of value layers over a fixed definedness skeleton

\[
\operatorname{CVRI}
=
\left[
\operatorname{Aut}(\text{joint definedness})
:
\operatorname{Aut}(\text{full valued family})
\right].
\]

For the selector ladder,

\[
\boxed{
\operatorname{CVRI}=(m+1)!.
}
\]

With only `m` value-bearing cells and a domain skeleton consisting of one repeated loop, the rigidity index grows factorially.

`Carrier-Value Rigidity Index` is working terminology only.

## 9. Marginal gain of the r-th selector

Suppose `r-1` value layers have already been restored. The residual group is

\[
S_{m+2-r}.
\]

Restoring one more value gives

\[
S_{m+1-r}.
\]

The index of this step is

\[
\boxed{m+2-r.}
\]

Thus the first selector removes a factor `m+1`, the next a factor `m`, and so on, until the final selector removes the last factor `2`.

Multiplying the marginal gains gives

\[
(m+1)m\cdots2=(m+1)!.
\]

This makes the factorial amplification completely explicit.

## 10. Definability ladder

Once a value layer `\star_i` is present, its selected point is parameter-free definable by

\[
V_i(x)
\iff
\exists y\,\bigl(D_i(y,y)\land y\star_i y=x\bigr).
\]

In the exact family, the common loop point `a` is definable as the unique argument of any defined operation cell. Hence every restored selector produces one new definable singleton.

After `r` selectors, exactly `r+1` distinguished singleton roles are forced (`a` plus the selected values), while the remaining `m+1-r` points form one automorphism orbit.

At `r=m`, the final residual singleton `w` becomes definable by exclusion, and the structure is rigid.

## 11. Association spectra and commutation

For each individual operation `\star_i`, the only defined pair is `(a,a)` and its value `v_i` is not an argument of any defined cell. Hence every twice-nested product is undefined.

On `U_m^3`, each reduct has

\[
\boxed{
(EQ,NEQ,LEFT,RIGHT,NONE)
=(0,0,0,0,(m+2)^3).
}
\]

Its commutation locus is exactly

\[
\boxed{\operatorname{Comm}_{\star_i}=\{(a,a)\}.}
\]

Thus the factorial rigidity growth is invisible to Association Spectra and almost invisible to commutation geometry.

## 12. Arithmetic Leakage firewall

The selector family contains no external order on

\[
\{v_1,\ldots,v_m,w\}.
\]

The labels are only specification labels for operation symbols and their outputs. Structurally, any subset of restored selectors merely names that many isolated carrier roles; the unrecovered points remain a pure symmetric orbit.

There is no successor relation, betweenness, EqGap, addition graph, multiplication graph, or rank calculation.

Therefore the family is below AL0 in the intended arithmetic-leakage sense:

\[
\boxed{
\text{factorial rigidity does not imply arithmetic leakage.}
}
\]

This is an important calibration against interpreting a large automorphism-group collapse as hidden arithmetic.

## 13. Relation to JFS

The selector ladder and JFS are genuinely different mechanisms.

### JFS

A common carrier symmetry survives each reduct separately but requires incompatible actions on a shared output role/fiber.

### Carrier-Value Selection

The operation values are themselves elements of the one-sorted carrier. Each value layer fixes one point inside a common residual carrier orbit.

No cross-operation equality of values is needed in the selector ladder; indeed all

\[
v_1,\ldots,v_m
\]

are distinct.

Thus one-sorted value memory has at least two independent channels:

\[
\boxed{
\text{cross-operation fiber synchronization}
\quad\text{and}\quad
\text{carrier-point selection}.
}
\]

## 14. The two-operation case

For `m=2`, the selector ladder is exactly the absolute minimum VV witness:

\[
U_2=\{a,v_1,v_2,w\},
\]

\[
a\star_1 a=v_1,
\qquad
a\star_2 a=v_2.
\]

The symmetry ladder is

\[
\boxed{S_3\to S_2\to1,}
\]

recovering the unique four-point two-cell class recorded in `UNRESTRICTED_ONE_SORTED_MINIMALITY.md`.

Thus the minimum example is not exceptional: it is the first member of an infinite sharp family.

## 15. Current conclusion

The scalable answer is affirmative and exact:

\[
\boxed{
\text{linear value resources}
\Rightarrow
\text{factorial carrier-rigidity gain}
}
\]

with essentially no additional domain geometry.

More precisely, `m` one-cell operations on an `(m+2)`-point one-sorted universe produce

\[
S_{m+1}\to1
\]

while every individual operation retains automorphism group `S_m`, every proper value subfamily is nonrigid, and the common-loop template is selector-optimal.

This converts Carrier-Value Selection from a four-point curiosity into a scalable rigidity mechanism.
