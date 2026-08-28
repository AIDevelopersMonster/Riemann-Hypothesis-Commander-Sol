# Internal Digit Scaffold and the Collapse of the Dimension-1 Barrier

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate; internal hostile audit included  
**Backend normalization:** `FCOA_DEFINITION_1_0.md` and `FCOA_MORPHISMS_EQUIVALENCE_REPRESENTATION_1_0.md`  
**Scope:** explicit base carrier, fixed finite relational signature, ordinary FO query language, varied size-dependent digit scaffold

---

## 1. Question

The previous frontier suggested that the sharp contrast

\[
\Theta(N^2)
\quad\text{versus}\quad
\Theta(N)
\]

for additive memory might be controlled by FO interpretation dimension `1` versus `2`.

That suggestion is false in the permissive varied-scaffold model.

One can keep the target carrier itself explicit and one-dimensional,

\[
X_N=\{0,\ldots,N-1\},
\]

and place a small digit coordinate system **inside the same carrier**. The target elements are still represented by themselves, so the interpretation of the target in the scaffold is dimension `1`; nevertheless two coordinate maps expose a latent Cartesian factorization.

The resulting structure has linear support, uniformly FO-defines truncated addition, and still does not uniformly FO-define multiplication.

Thus:

\[
\boxed{
\text{FO interpretation dimension alone is not the missing additive resource.}
}
\]

The new resource is **internal coordinate factorization**.

---

## 2. Construction

Let

\[
b_N=\lceil\sqrt N\rceil,
\qquad
D_N=\{0,\ldots,b_N-1\}\subseteq X_N.
\]

Every `x<N` has unique base-`b_N` coordinates

\[
x=h(x)b_N+\ell(x),
\]

with

\[
0\le h(x),\ell(x)<b_N.
\]

Because `x<N<=b_N^2`, this is well-defined and unique.

The scaffold is

\[
\mathcal D_N
=(X_N,<,D,H,L,S),
\]

where:

- `D(x)` says `x in D_N`;
- `H(x,d)` iff `d=h(x)`;
- `L(x,d)` iff `d=ell(x)`;
- `S(a,d;c,r)` is the digit add-with-carry table

\[
S(a,d;c,r)
\iff
a+d=cb_N+r,
\]

with

\[
a,d,r\in D_N,
\qquad
c\in\{0,1\}.
\]

The order `<` is the already available AL0 background order on the explicit target carrier.

### Provenance status

The family is **varied size-dependent**: `b_N`, `D_N`, the coordinate maps, and the digit table depend on final carrier size `N`.

It is therefore outside the unvaried Presburger class of `PRESBURGER_COMPRESSION_BARRIER.md`.

No arbitrary one-bit size oracle is used. The dependence on `N` is the explicit deterministic rule `b_N=ceil(sqrt N)`.

---

## 3. Resource vector

The unary digit predicate has

\[
|D_N|=b_N=O(\sqrt N).
\]

The two coordinate graphs are functional on all target points:

\[
|H|=|L|=N.
\]

For every ordered digit pair `(a,d)` there is exactly one `(c,r)`, hence

\[
|S|=b_N^2=N+O(\sqrt N).
\]

Therefore the total primitive support is

\[
C(N)=2N+b_N^2+b_N
=3N+O(\sqrt N).
\]

Thus

\[
\boxed{C(N)=\Theta(N).}
\]

There is no growing auxiliary sort: `D_N` is a distinguished subset of the already explicit base carrier `X_N`.

Under the backend terminology:

- target representation dimension: `d=1`;
- auxiliary-carrier size: `A_N=0`;
- coordinate-map support: `Q_N=2N`;
- latent coordinate width: `2`;
- provenance: varied deterministic numerical scaffold;
- intended semantic phase: AL1.

---

## 4. Uniform FO definition of addition

Let `Zero(z)` mean that `z` is the least carrier point, and let `One(o)` mean that `o` is its successor. Since `<` is present, both are uniformly FO-definable.

For target points `x,y,z`, existentially choose digits

\[
h_x,l_x,h_y,l_y,h_z,l_z,c,t.
\]

Require

\[
H(x,h_x),\quad L(x,l_x),
\]

\[
H(y,h_y),\quad L(y,l_y),
\]

\[
H(z,h_z),\quad L(z,l_z).
\]

Then require the low-digit sum

\[
S(l_x,l_y;c,l_z),
\tag{1}
\]

the high-digit sum without overflow

\[
S(h_x,h_y;0,t),
\tag{2}
\]

and addition of the incoming carry, again without overflow,

\[
S(t,c;0,h_z).
\tag{3}
\]

All displayed constants `0` are expressed in FO by `Zero`.

### Theorem 4.1 — Internal Digit Addition

For every `N>=4`, the fixed FO formula given by (1)-(3) satisfies

\[
\boxed{
\operatorname{Add}_{\mathcal D}(x,y,z)
\iff
x+y=z<N.
}
\]

### Proof

Write

\[
x=h_xb+l_x,
\qquad
y=h_yb+l_y,
\]

where `b=b_N`.

Condition (1) gives

\[
l_x+l_y=cb+l_z.
\]

Condition (2) gives

\[
h_x+h_y=t<b,
\]

and condition (3) gives

\[
t+c=h_z<b.
\]

Therefore

\[
x+y=(h_x+h_y+c)b+l_z=h_zb+l_z=z.
\]

Conversely, if `x+y=z<N`, ordinary base-`b` digit addition has a unique low carry `c in {0,1}`. Since the total result is below `N<=b^2`, no carry may leave the high digit. The unique digit witnesses satisfy (1)-(3).

If the base-`b` arithmetic sum lies in `[N,b^2)`, there is simply no target `z in X_N` with those coordinates, so the formula does not create wraparound.

Hence the definition is exact. `□`

Therefore

\[
\boxed{
\operatorname{FTR}(\mathcal D)\ge1.
}
\]

---

## 5. Square subsequence and the Presburger upper bound

To show that multiplication does not appear, it is enough to inspect the infinite subsequence

\[
N=b^2.
\]

Then every digit pair occurs:

\[
X_{b^2}\cong D_b^2.
\]

Let

\[
\mathsf P_b=([b],<,+_{tr})
\]

be finite Presburger arithmetic on the digit carrier.

### Lemma 5.1 — the scaffold is uniformly interpretable in digit Presburger arithmetic

On the square subsequence,

\[
\mathcal D_{b^2}\le_{FO}\mathsf P_b
\]

by a fixed dimension-2 interpretation.

### Proof

Represent target `x=hb+l` by the pair `(h,l) in [b]^2`.

- Target order is lexicographic order on pairs, FO-definable from `<`.
- The digit subset `D_b` is represented by pairs `(0,d)`.
- `H` and `L` are the coordinate projections, with digit values represented as `(0,h)` and `(0,l)`.

It remains to define the digit table `S` from `<,+_{tr}`.

For carry `0`,

\[
S(a,d;0,r)\iff a+d=r<b,
\]

which is the primitive truncated addition graph.

For carry `1`, let `M=b-1` be the maximum digit and choose `u,s` such that

\[
a+u=M,
\qquad
s=u+1,
\qquad
s+r=d.
\]

Then `u=b-1-a` and `s=b-a`, so the last equation is exactly

\[
d=(b-a)+r,
\]

or

\[
a+d=b+r.
\]

All three conditions use only order, truncated addition, definable min/max and successor. Thus `S` is uniformly FO-definable in `P_b`. `□`

---

## 6. Multiplication is not uniformly definable

A classical finite-model-theory separation due to Troy Lee states that finite truncated multiplication is not uniformly first-order definable from order and truncated addition:

\[
\boxed{
\operatorname{TIMES}\notin FO(<,\operatorname{PLUS}).
}
\]

Reference: Troy Lee, “Arithmetical Definability over Finite Structures,” *Mathematical Logic Quarterly* 49(4), 2003, 385-392, DOI `10.1002/malq.200310041`.

### Theorem 6.1 — Exact AL1

There is no fixed FO formula defining canonical truncated multiplication uniformly in the family

\[
(\mathcal D_N)_{N\ge4}.
\]

Hence

\[
\boxed{
\operatorname{FTR}(\mathcal D)=1.
}
\]

### Proof

Assume a fixed formula defines

\[
\operatorname{Mul}_N(x,y,z)
\iff xy=z<N
\]

in every `D_N`.

Restrict to `N=b^2`. By Lemma 5.1, substitute the fixed dimension-2 interpretation of `D_{b^2}` into that formula. This gives a fixed FO formula over `P_b`.

Now restrict its three target arguments to the low-digit copy

\[
\{(0,a):a<b\}.
\]

For `a,d,r<b`, target multiplication on these points is exactly

\[
a\cdot d=r<b.
\]

Therefore the translated formula uniformly defines finite truncated multiplication on `P_b`, contradicting the classical separation

\[
\operatorname{TIMES}\notin FO(<,\operatorname{PLUS}).
\]

Thus multiplication is not uniformly definable in the scaffold. Together with Theorem 4.1, the scaffold is exactly AL1. `□`

---

## 7. Dimension-1 Collapse Theorem

### Theorem 7.1

There exists a uniform finite-signature family on an explicit `N`-element target carrier such that:

1. the target is represented dimension-1 by itself;
2. no growing auxiliary sort is added;
3. total primitive support is `Theta(N)`;
4. truncated addition is uniformly FO-definable;
5. truncated multiplication is not uniformly FO-definable.

Therefore

\[
\boxed{
\text{dimension-1 + explicit carrier does not force the quadratic additive floor.}
}
\]

The quadratic theorem from `PRESBURGER_COMPRESSION_BARRIER.md` remains correct because the present scaffold is varied and not one fixed unvaried Presburger relation family.

---

## 8. What actually supplied the compression

Although the target itself stays one-dimensional, the pair of maps

\[
(H,L)
\]

is jointly injective:

\[
x\mapsto(h(x),l(x)).
\]

Its codomain capacity is

\[
|D_N|^2=\Theta(N).
\]

Thus the scaffold contains a **latent two-coordinate factorization** inside one physical carrier.

This motivates a presentation parameter distinct from FO interpretation dimension.

### Working definition — Coordinate Factorization Width

A presentation has coordinate factorization width at most `k` if there are `k` uniformly named coordinate maps

\[
c_i:X_N\to D_{i,N}
\]

whose joint map

\[
x\mapsto(c_1(x),\ldots,c_k(x))
\]

is injective and whose local coordinate structures are part of the declared resource profile.

For the present construction,

\[
\boxed{\operatorname{CFW}=2.}
\]

`CFW` is working normal-form terminology, not an interpretation-invariant semantic invariant.

---

## 9. General fixed radix width

The same mechanism works with any fixed `k>=2` on the exact-power subsequence

\[
N=b^k.
\]

Use `k` base-`b` coordinate maps and the same digit add-with-carry table.

The support is

\[
kN+b^2+O(b)=\Theta(N),
\]

while a fixed FO formula performs the `k` digit additions because `k` is constant.

On the exact-power subsequence the whole scaffold is dimension-`k` interpretable in finite Presburger arithmetic on `[b]`, so the same restriction argument blocks multiplication.

Hence for every fixed `k>=2` there are linear-cost exact-AL1 presentations with latent coordinate width `k`.

The case `k=2` is already sufficient to destroy any claimed phase boundary based solely on target interpretation dimension.

---

## 10. FCOA compilation

The scaffold is written relationally because this is the clean FO interface required by the backend specification.

A fixed bounded-incidence compilation can replace the finite relational signature

\[
D,H,L,S
\]

by a fixed collection of typed partial-operation gadgets, with only constant-factor blow-up per primitive record.

Therefore an FCOA partial-operation realization remains

\[
\Theta(N)
\]

in cell/incidence cost.

Such a compilation is target-equivalent and phase-equivalent to the relational scaffold, but it is not literally the same partial algebra. The exact equivalence level must be declared according to `FCOA_MORPHISMS_EQUIVALENCE_REPRESENTATION_1_0.md`.

---

## 11. Hostile audit

### 11.1 Is ordinary multiplication smuggled into `S`?

No. `S` is digit addition with one carry bit and is uniformly FO-definable from finite Presburger arithmetic on the square subsequence.

### 11.2 Is the target secretly represented by pairs?

Semantically the target carrier in `D_N` is the explicit set `X_N`; target identity is dimension-1. However the coordinate maps encode a latent pair decomposition. This is precisely why interpretation dimension alone is an insufficient resource statistic.

### 11.3 Is a growing auxiliary sort hidden in `D_N`?

No. `D_N` is a subset of `X_N`, not a disjoint added sort. Its unary predicate has only `O(sqrt N)` support. The two coordinate maps are fully charged at `2N` records.

### 11.4 Is the family unvaried Presburger?

No. The cutoff `b_N=ceil(sqrt N)` changes with final size, so the construction is outside the earlier quadratic lower-bound theorem by design.

### 11.5 Could multiplication be definable because the varying cutoff leaks extra information?

Not uniformly. Any alleged multiplication formula would also work on the square subsequence. There the entire scaffold is uniformly interpretable in finite Presburger arithmetic, and restriction to the low-digit copy would define finite multiplication from `<,+`, contradicting the classical separation.

### 11.6 Does the non-square boundary create wraparound errors in addition?

No. A digit sum in `[N,b_N^2)` has no corresponding target element `z`, so the existential coordinate match fails. The formula defines truncated addition on the actual carrier.

### 11.7 Is the `Theta(N)` claim hiding output/alphabet cost?

No unbounded output alphabet is needed beyond the base carrier and the fixed relational symbols. If compiled through incidence gadgets, all new records/nodes are charged and remain linear.

No fatal defect was found in this audit.

---

## 12. Corrected frontier

The former candidate boundary

\[
\text{interpretation dimension }1
\quad\text{vs}\quad
2
\]

must be abandoned as a stand-alone explanation.

The new decomposition is:

\[
\boxed{
\text{unvaried one-carrier Presburger memory}
\Rightarrow
\Theta(N^2)\text{ additive floor}
}
\]

but

\[
\boxed{
\text{varied internal coordinate factorization}
\Rightarrow
\Theta(N)\text{ exact AL1 even on the same explicit carrier.}
}
\]

Thus the next intrinsic resource question is not target tuple dimension alone. It is the interaction of

\[
\boxed{
\text{provenance}
+
\text{coordinate factorization width}
+
\text{coordinate-map support}
+
\text{local law strength}.
}
\]

---

## 13. Next central problem

The strongest remaining question is now:

\[
\boxed{
\text{Can exact AL1 be compressed below linear total support}
}
\]

under a provenance-safe model that charges coordinate maps and forbids arbitrary oracular size dependence?

Equivalently, is

\[
\Theta(N)
\]

the genuine floor once latent coordinate factorizations are admitted but every target point remains explicitly represented and all coordinate incidences are charged?

A second direction is semantic:

\[
\boxed{
\text{Can Coordinate Factorization Width be normalized under bounded-fiber recodings,}
}
\]

or is it itself only a presentation-level statistic like the earlier RTP exponent?

These are now the correct frontier questions.

---

## 14. Status

\[
\boxed{
\mathbf F:\ \Theta(N)\text{ exact-AL1 internal digit scaffold exists.}
}
\]

\[
\boxed{
\mathbf F:\ \text{target FO interpretation dimension }1\text{ alone does not imply a quadratic floor.}
}
\]

\[
\boxed{
\mathbf F:\ \text{the earlier unvaried Presburger quadratic barrier survives unchanged.}
}
\]

\[
\boxed{
\mathbf W:\ \text{Coordinate Factorization Width as resource terminology.}
}
\]

\[
\boxed{
\mathbf O:\ \text{linear lower bound under fully charged provenance-safe internal factorization.}
}
\]

No new numbered G5 family is opened by this note.