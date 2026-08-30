# FCOA-Z Signed M0 Reflection Transfer 0.1

**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** PROVED CORE PACKAGE / HOSTILE AUDIT STILL REQUIRED  
**Date:** 2026-08-30  
**Depends on:** `SIGNED_COMPLETION_FOUNDATION_0_1.md` and canonical FCOA M0

---

## 1. Question

Let

\[
B^{\pm}=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\]

be the symmetric signed completion with zero reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\]

Embed the original M0 natural ray by

\[
\iota(P_0)=P_0,
\qquad
\iota(P_n)=P_n^+\quad(n\ge1).
\tag{1}
\]

The problem is to extend the old M0 operations to the signed line while satisfying all of the following:

1. every old positive-ray cell is preserved exactly;
2. simultaneous reflection of both arguments is an operation symmetry after a suitable reflection action on output sorts;
3. no mixed-sign cell is introduced unless forced;
4. no ordinary sign law for `+` or `times` is imported;
5. the old positional asymmetry of the operation tables survives.

The main conclusion is positive:

\[
\boxed{\text{M0 has a canonical minimal-domain reflection closure on }B^{\pm}.}
\]

The base-domain closure is unique. The only first-stage nonuniqueness is how the terminal output fibers themselves are lifted under reflection.

---

## 2. Positive M0 data

On the positive embedded ray the old `oplus` rules are, for every \(n\ge1\),

\[
P_0\oplus P_n^+=P_n^+,
\tag{2}
\]

\[
P_n^+\oplus P_0=
\begin{cases}
P_0,&n=1,\\
P_{n-1}^+,&n\ge2,
\end{cases}
\tag{3}
\]

and

\[
P_n^+\oplus P_n^+=E_n^+.
\tag{4}
\]

All other positive-positive base cells are undefined.

For `otimes`,

\[
P_0\otimes P_n^+=P_0\qquad(n\ge1),
\tag{5}
\]

\[
P_n^+\otimes P_0=E_n^*\qquad(n\ge2),
\tag{6}
\]

\[
P_1^+\otimes P_n^+
=P_n^+\otimes P_1^+
=P_n^+\qquad(n\ge2),
\tag{7}
\]

\[
P_n^+\otimes P_n^+=E_n^\times\qquad(n\ge2),
\tag{8}
\]

with the remaining positive-positive cells undefined, including

\[
P_1^+\otimes P_0,
\qquad
P_1^+\otimes P_1^+.
\]

---

## 3. Reflection lift datum for terminal outputs

The old symbols \(E_n^+,E_n^*,E_n^\times\) already use `+` as an output-channel label, so branch sign and output-channel type must not be conflated.

For each old output \(E_n^\alpha\), where

\[
\alpha\in\{+,*,\times\},
\]

introduce a reflected image

\[
\overline E_n^\alpha:=\nu_O(E_n^\alpha),
\tag{9}
\]

where \(\nu_O\) is an involution on the corresponding output sort.

Two canonical lifts will be important.

### 3.1 Shared-fiber lift

\[
\overline E_n^\alpha=E_n^\alpha.
\tag{10}
\]

The two mirror cells share one terminal output. This uses no additional output elements and forgets branch sign at the output value.

### 3.2 Split-fiber lift

\[
\overline E_n^\alpha\ne E_n^\alpha,
\qquad
\nu_O(E_n^\alpha)=\overline E_n^\alpha,
\qquad
\nu_O(\overline E_n^\alpha)=E_n^\alpha.
\tag{11}
\]

The two mirror cells receive separate terminal outputs exchanged by reflection.

No claim is made that these are the only imaginable output extensions. They are the two canonical extremal lifts: fixed fibers and free doubled fibers.

---

## 4. Minimal simultaneous-reflection closure

For a partial binary operation \(\omega\), reflection equivariance means

\[
\omega(\nu x,\nu y)=\nu_*(\omega(x,y))
\tag{12}
\]

whenever the left or right side is defined, where \(\nu_*\) acts as \(\nu\) on base outputs and as \(\nu_O\) on terminal outputs.

The domain must therefore satisfy

\[
(x,y)\in D_\omega
\iff
(\nu x,\nu y)\in D_\omega.
\tag{13}
\]

Define the **minimal reflection closure** of the positive M0 domain by

\[
D_\omega^{\mathrm{min}}
=
D_\omega^{++}
\cup
\nu^{(2)}(D_\omega^{++}),
\tag{14}
\]

where

\[
\nu^{(2)}(x,y)=(\nu x,\nu y).
\]

Since \(P_0\) is fixed, (14) includes the positive old cells, their negative-negative mirrors, and the corresponding zero/branch cells. It introduces no genuinely mixed pair

\[
(P_i^+,P_j^-)
\quad\text{or}\quad
(P_i^-,P_j^+)
\qquad(i,j\ge1).
\tag{15}
\]

Those mixed sectors are mathematically `UNDEF` in the minimal structure, while remaining `OPEN` as locations for later research extensions.

---

## 5. Minimal Reflection-Closure Theorem

### Theorem 5.1

Fix a reflection lift \(\nu_O\) on every terminal output sort. There exists a unique partial-operation extension of each positive M0 operation to the domain (14) such that:

1. its positive restriction is the old M0 table;
2. it is simultaneously reflection-equivariant in the sense of (12);
3. no additional mixed-sign domain cell is opened.

### Proof

Existence is by definition. Keep every positive M0 value unchanged. For every positive defined pair \((x,y)\), define the reflected pair by

\[
\omega(\nu x,\nu y):=\nu_*(\omega(x,y)).
\tag{16}
\]

Because \(\nu^2=\operatorname{id}\) on the base and \(\nu_O^2=\operatorname{id}\) on outputs, applying (16) twice returns the original cell and value, so the definition is consistent.

The only overlap between the positive domain and its reflected image occurs in cells involving the fixed origin in a manner already paired by (16); the explicit formulas below verify consistency there. No mixed-sign pair is introduced by simultaneous reflection.

For uniqueness, every cell in (14) is either an old positive cell or the reflection of one. Old positive values are fixed by the restriction requirement, and every reflected value is then forced by (12). Thus no value on (14) remains free. \(\square\)

### Corollary 5.2

The signed M0 base-domain extension is unique **modulo the chosen reflection lift of the terminal output fibers**.

Thus the first genuine signed ambiguity lies in output-fiber geometry, not in the reflected base domain.

---

## 6. Explicit signed `oplus`

Define the radial-toward-zero map

\[
\rho(P_n^\sigma)=
\begin{cases}
P_0,&n=1,\\
P_{n-1}^\sigma,&n\ge2,
\end{cases}
\qquad
\sigma\in\{+,-\}.
\tag{17}
\]

No value \(\rho(P_0)\) is needed.

The minimal reflected `oplus` table is exactly

\[
P_0\oplus x=x
\qquad(x\in B^{\pm}\setminus\{P_0\}),
\tag{18}
\]

\[
x\oplus P_0=\rho(x)
\qquad(x\ne P_0),
\tag{19}
\]

\[
P_n^+\oplus P_n^+=E_n^+,
\tag{20}
\]

\[
P_n^-\oplus P_n^-=\overline E_n^+,
\tag{21}
\]

with every remaining base-base cell undefined.

### Lemma 6.1 — radial reflection covariance

\[
\boxed{\rho\nu=\nu\rho.}
\tag{22}
\]

### Proof

For \(n=1\), both sides send either \(P_1^+\) or \(P_1^-\) to \(P_0\). For \(n\ge2\), both sides send \(P_n^\sigma\) to \(P_{n-1}^{-\sigma}\). \(\square\)

### Proposition 6.2 — old predecessor becomes radial contraction

On the positive branch,

\[
P_n^+\oplus P_0=P_{n-1}^+
\]

moves one step left in the global order. On the negative branch,

\[
P_n^-\oplus P_0=P_{n-1}^-
\]

moves one step right in the global order.

Therefore right multiplication by zero is **not** a global predecessor or successor operator on the signed line. It is the coordinate-rooted contraction \(\rho\) toward \(P_0\).

### Consequence

The signed transfer preserves absolute-position sensitivity. It does not normalize the old operation to ordinary signed addition.

### Proposition 6.3 — noncommutativity survives everywhere off the origin

For every nonzero base point \(x\),

\[
P_0\oplus x=x
\qquad\text{but}\qquad
x\oplus P_0=\rho(x)\ne x.
\tag{23}
\]

Hence

\[
\boxed{P_0\oplus x\ne x\oplus P_0}
\]

for every \(x\ne P_0\).

### Proposition 6.4 — partial nonassociativity survives

For every nonzero \(x\),

\[
(P_0\oplus P_0)\oplus x
\]

is undefined because \(P_0\oplus P_0\) is undefined, while

\[
P_0\oplus(P_0\oplus x)
=P_0\oplus x
=x
\]

is defined. Therefore the signed `oplus` remains nonassociative as a partial operation.

---

## 7. Explicit signed `otimes`

For \(\sigma\in\{+,-\}\) and \(n\ge1\),

\[
P_0\otimes P_n^\sigma=P_0.
\tag{24}
\]

For \(n\ge2\),

\[
P_n^+\otimes P_0=E_n^*,
\qquad
P_n^-\otimes P_0=\overline E_n^*,
\tag{25}
\]

\[
P_1^+\otimes P_n^+
=P_n^+\otimes P_1^+
=P_n^+,
\tag{26}
\]

\[
P_1^-\otimes P_n^-
=P_n^-\otimes P_1^-
=P_n^-,
\tag{27}
\]

\[
P_n^+\otimes P_n^+=E_n^\times,
\qquad
P_n^-\otimes P_n^-=\overline E_n^\times.
\tag{28}
\]

The cells

\[
P_1^\sigma\otimes P_0,
\qquad
P_1^\sigma\otimes P_1^\sigma
\]

remain undefined, as do all distinct generic same-branch pairs and all genuinely mixed-sign pairs.

Thus `otimes` remains a symmetry-rich laboratory rather than becoming integer multiplication.

---

## 8. Two canonical signed M0 variants

The base-domain table is now fixed. The output lift produces two canonical baselines.

### `ZM0-share`

Use (10): mirror cells share old output values.

This has the smallest output universe compatible with simultaneous reflection. It preserves radial index through common value fibers but does not preserve branch sign in the output value.

### `ZM0-split`

Use (11): every old terminal output receives a distinct mirror partner.

This preserves branch-sensitive output memory. It is the natural candidate if output fibers are later to become transport channels between multiple signed lines.

Neither variant is declared universally canonical yet. Their different symmetry cost is itself a research invariant.

---

## 9. Finite-window automorphism audit

Fix the symmetric window

\[
W_N=\{P_0\}\cup\{P_n^+,P_n^-:1\le n\le N\}.
\]

All groups below are for the exact finite restriction and include only output elements actually used by that restriction.

### Theorem 9.1 — signed `oplus` rigidity up to reflection

For every \(N\ge1\), in either `ZM0-share` or `ZM0-split`,

\[
\boxed{\operatorname{Aut}(W_N,\oplus)\cong C_2.}
\tag{29}
\]

The nontrivial automorphism is simultaneous branch reflection

\[
P_n^+\leftrightarrow P_n^-
\]

with the corresponding output action.

### Proof

The origin is structurally distinguished by the property that left multiplication by it fixes every other base point:

\[
P_0\oplus x=x
\qquad(x\ne P_0).
\]

No nonzero point has this property, so every automorphism fixes \(P_0\).

Right multiplication by \(P_0\) is the parent map \(\rho\). Hence every automorphism of the operation preserves the rooted graph formed by the two chains

\[
P_N^+\to\cdots\to P_1^+\to P_0,
\]

\[
P_N^-\to\cdots\to P_1^-\to P_0.
\]

The only automorphisms of this rooted two-arm graph are the identity and the swap of the two arms. The operation values and either output lift are compatible with exactly these two maps. \(\square\)

### Corollary 9.2

The signed `oplus` reduct remembers the origin and radial depth but forgets the choice of positive versus negative branch.

This is a new memory type relative to the one-sided ray:

\[
\boxed{\text{rooted radial memory without signed orientation}.}
\]

No claim of uniform FO definability of the full integer coordinate is made here.

---

### Theorem 9.3 — signed `otimes`, split fibers

For \(N\ge2\), let

\[
G_N^+=\{P_2^+,\ldots,P_N^+\},
\qquad
G_N^-=\{P_2^-,\ldots,P_N^-\}.
\]

For `ZM0-split`,

\[
\boxed{
\operatorname{Aut}(W_N,\otimes)
\cong
(S_{N-1}\times S_{N-1})\rtimes C_2
=S_{N-1}\wr C_2.
}
\tag{30}
\]

### Proof

The origin is distinguished by its left-absorbing pattern. The two points \(P_1^+,P_1^-\) are exactly the two local unit points, each incident to one generic branch. Once the two units are fixed, every permutation of \(G_N^+\) and every independent permutation of \(G_N^-\) preserves the base domain and operation pattern; the attached split outputs are carried along uniquely. The two complete branch structures may also be exchanged by reflection. No other base permutation can preserve the unit/generic incidence pattern. \(\square\)

### Theorem 9.4 — signed `otimes`, shared fibers

For `ZM0-share`,

\[
\boxed{
\operatorname{Aut}(W_N,\otimes)
\cong
S_{N-1}\times C_2.
}
\tag{31}
\]

### Proof

The base domain alone allows the independent branch permutations of Theorem 9.3. Shared terminal values add a matching between the two generic branches: the positive and negative points of radial index \(n\) produce the same `*` and `times` outputs. Therefore an automorphism must send the two members of each matched radial fiber to another matched radial fiber. The permutation of generic radial indices must consequently be the same on both branches. A global branch reflection remains possible and commutes with the common radial permutation. \(\square\)

### Corollary 9.5 — fiber choice has measurable rigidity cost

The two equally reflection-compatible output lifts have different full-operation symmetry:

\[
\boxed{
ZM0\text{-split}:S_{N-1}\wr C_2,
\qquad
ZM0\text{-share}:S_{N-1}\times C_2.
}
\tag{32}
\]

Thus **sharing mirror output fibers creates cross-branch rigidity by value coupling**, whereas splitting them preserves independent branch exchangeability.

---

### Theorem 9.6 — both legacy operations together

For \(N\ge2\), in either output-lift variant,

\[
\boxed{
\operatorname{Aut}(W_N,\oplus,\otimes)\cong C_2.
}
\tag{33}
\]

### Proof

By Theorem 9.1, any automorphism preserving `oplus` is already either identity or global branch reflection. Both preserve the reflected `otimes` table by construction. \(\square\)

---

## 10. Exact commutation counts on symmetric windows

These counts use ordered base pairs for which both reversed products are defined and equal.

### Proposition 10.1

For signed `oplus` on \(W_N\),

\[
\boxed{|\operatorname{Comm}_{\oplus}|=2N.}
\tag{34}
\]

### Proof

The only commuting base pairs are the nonzero diagonal pairs \((x,x)\). There are \(2N\) of them. For every nonzero \(x\), the pair \((P_0,x)\) has reversed values \(x\) and \(\rho(x)\), which differ. All remaining off-diagonal pairs fail definedness in at least one direction. \(\square\)

### Proposition 10.2

For signed `otimes` on \(W_N\), \(N\ge2\),

\[
\boxed{|\operatorname{Comm}_{\otimes}|=6(N-1).}
\tag{35}
\]

### Proof

On each branch, every generic point \(g\) commutes with its local unit in both ordered directions, giving \(2(N-1)\) commuting ordered pairs per branch, and each generic diagonal \((g,g)\) contributes one more per generic, giving \(N-1\) per branch. Thus each branch contributes \(3(N-1)\), and the two branches contribute \(6(N-1)\). No cross-branch pair is defined, and zero/generic reversed values are unequal. \(\square\)

These counts are independent of shared versus split output lift.

---

## 11. Zero-Reflection Definability Barrier

The signed M0 operational reduct in either variant admits the nontrivial base reflection

\[
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+,
\qquad
\nu(P_0)=P_0
\]

as an automorphism, extended appropriately to output sorts.

Any parameter-free first-order definable base relation must therefore be invariant under simultaneous application of \(\nu\) to all of its arguments.

### Theorem 11.1 — orientation barrier

The standard signed order relation on the identified integer coordinates is not parameter-free FO-definable in a reflection-symmetric signed M0 operational reduct.

### Proof

If \(x<y\), then under reflection \(-x>-y\), not \(-x<-y\). Thus `<` is not invariant under the automorphism \(\nu\). Every parameter-free definable relation is automorphism-invariant. \(\square\)

The same argument excludes the oriented successor relation.

### Theorem 11.2 — signed multiplication barrier

Let

\[
Mul(x,y,z)\iff xy=z
\]

be ordinary integer multiplication under the external coordinate identification of the signed line. Then `Mul` is not parameter-free FO-definable in any reflection-symmetric signed M0 operational reduct.

### Proof

Take, for example,

\[
Mul(1,1,1).
\]

Applying zero reflection simultaneously to all three coordinates gives

\[
(-1,-1,-1).
\]

But

\[
(-1)(-1)=1\ne-1,
\]

so

\[
\neg Mul(-1,-1,-1).
\]

Hence the multiplication graph is not invariant under \(\nu\). Automorphism invariance of parameter-free definability gives the result. \(\square\)

### Proposition 11.3 — reflection does not itself block addition

For

\[
Add(x,y,z)\iff x+y=z,
\]

simultaneous reflection preserves the relation:

\[
x+y=z
\Longrightarrow
(-x)+(-y)=-z.
\]

Therefore the zero-reflection automorphism does **not** by itself prove non-definability of addition.

This asymmetry is important:

\[
\boxed{
\text{zero reflection is compatible with signed additive structure but incompatible with signed multiplication as a ternary graph.}
}
\tag{36}
\]

### Corollary 11.4 — symmetry-breaking requirement for signed AL2

Any future FCOA-Z construction that parameter-free recovers ordinary signed multiplication must break zero reflection somewhere in the operational/relational reduct, or else change the target/equivalence notion being recovered.

This is a necessary condition, not a sufficient one.

---

## 12. What is fixed by this package

Subject to hostile audit, the following statements are now proved internally:

1. a minimal simultaneous-reflection closure of positive M0 exists;
2. it is unique once the output reflection involution is fixed;
3. mixed-sign sectors are not forced by reflection and can remain undefined;
4. old `oplus` becomes a radial contraction operation around the fixed origin, not ordinary signed addition;
5. noncommutativity and partial nonassociativity survive the signed transfer;
6. `otimes` remains symmetry-rich and does not become multiplication;
7. shared versus split mirror output fibers create different rigidity costs;
8. signed `oplus` remembers the root/radial structure but leaves a global sign reflection;
9. a reflection-symmetric reduct cannot parameter-free recover standard oriented order or signed multiplication;
10. reflection symmetry alone does not exclude signed addition.

---

## 13. Immediate research frontier

The next step should not yet impose a mixed-sign arithmetic law.

The four signed sectors are

\[
(++),\quad (+-),\quad (-+),\quad (--).
\]

The first and fourth sectors are now controlled by reflection closure. The genuine new FCOA-Z information therefore lives in the pair

\[
\boxed{(+-),\quad(-+).}
\]

The next question is:

\[
\boxed{
\text{What is the weakest admissible mixed-sector rule that couples the two branches}
\text{ without collapsing the signed M0 operation to ordinary arithmetic?}
}
\tag{37}
\]

A parallel output-fiber question is whether `ZM0-share` or `ZM0-split` is the correct base for later inter-line transport. The symmetry calculation (32) shows that this is not cosmetic: the choice changes value-rigidity before any mixed-sign cell is opened.