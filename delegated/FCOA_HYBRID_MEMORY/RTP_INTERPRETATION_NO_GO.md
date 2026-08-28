# FCOA Hybrid Memory — RTP Interpretation No-Go and Semantic Transport Rank

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem package; explicit counterconstruction and proofs included  
**Purpose:** hostile-audit the proposal that `RTP=(rho,tau)` might be made invariant under arbitrary fixed-dimensional FO interpretations.

---

## 1. Main answer

The raw Resolution–Transport Profile

\[
RTP=(\rho,\tau)
\]

**cannot** be made invariant under unrestricted FO interpretation while retaining its present presentation-level meaning.

The obstruction is not merely technical. Canonical multiplication itself admits a natural linear-size digit presentation with

\[
\boxed{\rho=1,\qquad \tau=2,}
\]

whereas the direct four-modulus CRT verifier had

\[
(\rho,\tau)=(2,2).
\]

Thus the claimed multiplicative resolution exponent `2` is a property of the **direct-congruence normal form**, not of multiplication as an FO-interpretable relation.

Moreover the syntactic component `tau` is also not invariant: replacing a digit multiplication table by its incidence graph removes any primitive symbol that visibly looks bilinear while preserving FO recovery of multiplication.

Therefore no presentation statistic based only on primitive channels, table geometry, or the names/types of local laws can survive arbitrary FO recoding.

---

## 2. Base-b digit presentation

For clarity take

\[
N=b^2.
\]

Let

\[
D_b=\{0,1,\dots,b-1\}
\]

be a digit sort and represent each target number

\[
x\in X_N=\{0,\dots,N-1\}
\]

by its unique two-digit base-`b` expansion

\[
x=ib+j,
\qquad i,j\in D_b.
\]

Thus

\[
X_N\cong D_b^2.
\]

The coordinate capacity is exactly

\[
|D_b|^2=b^2=N.
\]

Hence the natural joint resolution exponent is

\[
\boxed{\rho=1.}
\]

If one insists on distinct channel sorts, use tagged copies `D_H,D_L` and a size-`b` definable bijection between them. The asymptotics are unchanged.

---

## 3. Primitive digit tables

Store two functional digit relations.

### 3.1 Add-with-carry

\[
S(a,b;c,r)
\iff
a+b=cb+r,
\]

where

\[
a,b,r\in D_b,
\qquad c\in\{0,1\}.
\]

For each ordered pair `(a,b)` there is one output `(c,r)`, hence

\[
|S|=b^2=N.
\]

### 3.2 Multiply-and-split

\[
P(a,b;c,r)
\iff
ab=cb+r,
\]

with all four variables in `D_b`.

Since `ab<b^2`, every ordered pair `(a,b)` has a unique high digit `c` and low digit `r`, so

\[
|P|=b^2=N.
\]

### 3.3 Coordinate maps

The two digit coordinates of all target points cost `2N` functional incidences.

Therefore the entire arithmetic seed has size

\[
\boxed{O(N).}
\]

---

## 4. Exact FO multiplication from two digits

Write

\[
x=ib+j,
\qquad
y=kb+l,
\qquad z=hb+r.
\]

We now give a fixed FO definition of the truncated multiplication graph

\[
Mul_N(x,y,z)\iff xy=z<N.
\]

Choose digit witnesses

\[
c_0,r_1,r_2,u\in D_b.
\]

Require

\[
P(j,l;c_0,r),
\tag{1}
\]

\[
P(i,l;0,r_1),
\tag{2}
\]

\[
P(j,k;0,r_2),
\tag{3}
\]

\[
P(i,k;0,0),
\tag{4}
\]

\[
S(c_0,r_1;0,u),
\tag{5}
\]

\[
S(u,r_2;0,h).
\tag{6}
\]

These six fixed atomic conditions define multiplication.

### Theorem HM-RTP-DIGIT-MUL

For `N=b^2`, conditions (1)–(6) hold exactly when

\[
xy=z<N.
\]

### Proof

Expand

\[
xy=(ib+j)(kb+l)
=ikb^2+(il+jk)b+jl.
\]

By (1),

\[
jl=c_0b+r.
\]

By (2) and (3),

\[
il=r_1,
\qquad
jk=r_2,
\]

with no carry into the `b^2` position.

By (4),

\[
ik=0.
\]

Hence

\[
xy=(c_0+r_1+r_2)b+r.
\]

Conditions (5) and (6), each with carry fixed to zero, say precisely that

\[
c_0+r_1+r_2=h<b.
\]

Therefore

\[
xy=hb+r=z<N.
\]

Conversely, if `xy=z<N`, the coefficient of `b^2` in the expansion above must vanish. Since all terms are nonnegative, necessarily

\[
ik=0,
\]

and the products `il`, `jk`, together with the accumulated middle digit, create no carry beyond the high digit. The unique digit decompositions therefore supply witnesses satisfying (1)–(6).

Thus the formula is exact. `□`

---

## 5. Linear resource bound

The digit structure uses

- `2N` coordinate incidences;
- `N` add-with-carry records;
- `N` multiply-and-split records;
- only constant-size role markers/gadgets.

Hence

\[
\boxed{M=\Theta(N).}
\]

After fixed incidence compilation into the two partial operations, each source record expands by only a constant number of cells, so the operation-cell cost remains

\[
\Theta(N).
\]

Thus canonical AL2 is realized with joint target-coordinate resolution only

\[
\boxed{R_N=N,\quad \rho=1.}
\]

---

## 6. Collapse of the direct-CRT exponent

The previous four-modulus direct CRT verifier used four channels of size `Theta(sqrt N)`, giving

\[
R_N=\Theta(N^2),
\qquad
\rho=2.
\]

The digit construction gives the same canonical multiplication relation with

\[
R_N=N,
\qquad
\rho=1.
\]

Therefore

\[
\boxed{(2,2)\longrightarrow(1,2)}
\]

under a natural change of representation.

This is the desired hostile counterexample.

The difference is conceptual:

- direct CRT verifies the single defect `xy-z`, whose magnitude is `Theta(N^2)`;
- digit arithmetic does not resolve that defect in one shot;
- it factors the computation into constant-many local carry constraints, each living at scale `b=sqrt N`.

Hence **defect exponent is not invariant under bounded-depth factorization**.

---

## 7. The lower floor rho >= 1

In any genuinely coordinate-based representation in which `N` target points are distinguished injectively by a fixed tuple of channel coordinates, the joint coordinate capacity must be at least `N`.

If the coordinate slots have sizes `m_1,...,m_k`, injectivity gives

\[
N\le\prod_{i=1}^k m_i.
\]

Hence

\[
\rho\ge1.
\]

The digit AL2 construction attains equality.

Therefore, after allowing bounded-depth digit factorization,

\[
\boxed{\rho_{\min}(AL0)=\rho_{\min}(AL1)=\rho_{\min}(AL2)=1}
\]

within the coordinate model.

So resolution exponent cannot separate the three AL levels once arbitrary natural encodings are admitted.

---

## 8. Why FO interpretation causes exactly this problem

A fixed-dimensional FO interpretation represents one output element by a fixed tuple of input elements. Thus a dimension-`d` interpretation has access to a tuple space of polynomial size up to

\[
|A|^d.
\]

This is standard in finite model theory and is precisely the mechanism used by the digit encoding: an `N`-element arithmetic sector is represented by pairs over a `sqrt N`-scale arithmetic digit sector.

Consequently, an exponent that measures how much range is stored in primitive coordinates cannot remain invariant unless interpretation dimension / tuple factorization is charged as part of the resource.

---

## 9. The transport grade tau also fails syntactically

Suppose `P(a,b;c,r)` is stored as a primitive multiply-and-split relation. Then it naturally looks like grade-2 bilinear transport.

Now replace every tuple of `P` by an incidence entry-node with four role edges to its arguments/results. This is the standard bounded-size incidence compilation.

The new primitive signature contains only generic incidence relations / partial-operation cells. No primitive symbol is visibly multiplication, bilinear, or even algebraic.

Nevertheless `P` is recovered by one fixed FO formula, and hence so is target multiplication.

Thus any **syntactic** definition of `tau` based on primitive local-law type is destroyed by definitional/incidence recoding.

Therefore

\[
\boxed{\tau_{syntactic}\text{ is not FO-interpretation invariant}.}
\]

---

## 10. No-Go theorem

### Theorem HM-RTP-NOGO

No profile whose components are determined solely by

1. primitive channel cardinalities / their product,
2. primitive table density,
3. primitive relation names or local algebraic appearance,

can be invariant under unrestricted fixed-dimensional FO interpretations and bounded-size incidence compilation while still assigning direct CRT multiplication the mandatory value `rho=2`.

### Proof

The two-digit construction realizes the same canonical multiplication relation with linear cell cost and joint coordinate capacity exactly `N`, hence `rho=1`.

Furthermore incidence compilation erases the primitive algebraic appearance of the local multiplication table while preserving it by FO interpretation.

Thus both presentation-dependent components can change while the interpreted target arithmetic remains the same. `□`

---

## 11. What *is* interpretation-invariant

The correct invariant object is not the primitive memory layout but **semantic FO interpretability strength**.

Let the benchmark families be

\[
\mathsf O_N=([N],<),
\]

\[
\mathsf P_N=([N],<,+_{tr}),
\]

\[
\mathsf A_N=([N],<,+_{tr},\times_{tr}).
\]

For a family `C=(C_N)`, define its **FO Transport Rank**

\[
\operatorname{FTR}(\mathcal C)
:=
\max\{j\in\{0,1,2\}:\mathsf B_j\le_{FO}\mathcal C\},
\]

where

\[
\mathsf B_0=\mathsf O,
\qquad
\mathsf B_1=\mathsf P,
\qquad
\mathsf B_2=\mathsf A.
\]

Here `B <=_FO C` means that one fixed parameter-free FO interpretation uniformly recovers the benchmark family from `C`.

### Theorem HM-FTR-INV

`FTR` is monotone under FO interpretations and invariant under FO bi-interpretability.

### Proof

FO interpretations compose. Hence if

\[
\mathsf B_j\le_{FO}\mathcal C
\]

and

\[
\mathcal C\le_{FO}\mathcal D,
\]

then

\[
\mathsf B_j\le_{FO}\mathcal D.
\]

Thus `FTR(C)<=FTR(D)`. Mutual interpretability gives equality. `□`

This is the semantic core that RTP was trying to approximate.

---

## 12. Relation to Presburger versus full arithmetic

The distinction between additive and multiplicative transport is genuinely semantic, not merely notational.

The infinite Presburger structure

\[
(\mathbb N,<,+)
\]

has decidable first-order theory, whereas multiplication is not definable there; adding multiplication yields full first-order arithmetic and a radically stronger definability theory.

This supports using the benchmark interpretability jump

\[
\mathsf P<_{FO}\mathsf A
\]

as the invariant phase distinction rather than the direct CRT defect exponent.

For the finite FCOA programme the relevant notion is uniform interpretation across the finite initial segments, exactly as in the AL hierarchy.

---

## 13. What remains of RTP

RTP is still useful, but its status must change.

It should be called a **normal-form resource profile**:

\[
RTP_{NF}=(\rho_{NF},\tau_{NF}).
\]

It answers:

> How is a given construction organizing its memory?

It does **not** answer:

> What resources are intrinsically forced by the interpreted arithmetic relation?

For direct CRT:

\[
RTP_{CRT}(AL2)=(2,2).
\]

For two-digit arithmetic:

\[
RTP_{digit}(AL2)=(1,2).
\]

Both are correct descriptions of their normal forms.

---

## 14. Correct phase picture

The branch should now distinguish two layers.

### Semantic phase invariant

\[
\boxed{FTR=0,1,2}
\]

according to whether order, Presburger/additive arithmetic, or full arithmetic is uniformly FO-interpretable.

This is interpretation-invariant.

### Resource realization profile

Cell count, degree, auxiliary carriers, channel resolution, and local-table organization describe **how cheaply a particular representation realizes that semantic phase**.

These quantities are optimization parameters, not invariants of the phase itself.

Thus the corrected architecture is

\[
\boxed{
\text{semantic phase}\quad+\quad\text{representation cost profile}.
}
\]

Trying to merge these into a single invariant RTP loses information and is unstable under interpretation.

---

## 15. Strong consequence for the superlinear-wall search

Digit factorization shows why the superlinear wall kept disappearing.

A fixed algebraic operation on `N`-scale numbers can often be evaluated through a constant number of local operations on `sqrt N`-scale digits. Since a full binary digit table costs

\[
(\sqrt N)^2=N,
\]

linear memory survives.

This mechanism is not special to CRT and not special to multiplication.

Therefore a genuine superlinear wall cannot be proved in the current permissive model merely from polynomial defect magnitude or fixed algebraic degree.

One must impose an additional restriction such as:

- bounded interpretation dimension;
- no recursive/digit factorization;
- bounded number of auxiliary tuple coordinates;
- locality restrictions on the interpreting formulas;
- or a primitive-operation constraint forbidding precomputed lookup tables.

Without such a restriction, presentation-level exponents are too plastic.

---

## 16. New sharp question

The correct next problem is no longer

\[
\text{Can }RTP\text{ itself be interpretation-invariant?}
\]

The answer is no.

The next problem is:

\[
\boxed{
\text{What is the weakest natural restriction on FO interpretations under which a nontrivial resource rank becomes invariant?}
}
\]

A particularly promising candidate is **size-faithful bounded-fiber dimension-1 interpretation** (or a similarly strict notion of linear interpretation). Under such a restriction, tuple-power digitization is forbidden, while incidence compilation can remain allowed.

That is the next plausible location of a genuine resource phase boundary.
