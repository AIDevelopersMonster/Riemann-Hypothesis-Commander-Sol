# PROJECTIVE_ASSOCIATOR_BRIDGE

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed first bridge, 2026-09-12  
**Parent input:** *Alice Throws Away the Ruler II — Phase Rigidity in Steiner Triple Systems*

## 1. Setup

Let `S=(X,B)` be an `STS(v)`. Its associated Steiner loop is

```math
L=X\sqcup\{0\},
```

with

```math
0\circ x=x\circ0=x,
\qquad
x\circ x=0,
```

and, for distinct `x,y\in X`, `x\circ y` equal to the third point of the unique block containing `x,y`.

The Steiner identities are

```math
x\circ y=y\circ x,
\qquad
x\circ(x\circ y)=y.
\tag{1.1}
```

For an independent root `tau={x,y,z}` put

```math
a=x\circ y,
\qquad
b=y\circ z,
\qquad
c=z\circ x.
\tag{1.2}
```

The parent article calls `tau` **P-phase** exactly when its Steiner closure is the Fano subsystem `S_7`.

Let

```math
\operatorname{Assoc}(p,q,r)
```

mean

```math
(p\circ q)\circ r=p\circ(q\circ r).
\tag{1.3}
```

The goal is to identify exactly what P-phase means in associator language and to quantify the resulting global defect density.

---

## 2. Where associativity can fail

### Lemma 2.1

In a Steiner loop, associativity holds automatically for an ordered triple `(p,q,r)` whenever at least one of the following occurs:

1. one of `p,q,r` is `0`;
2. two of `p,q,r` are equal;
3. `p,q,r` are three distinct collinear STS points.

Hence every associativity failure is an ordered independent triple of nonzero points.

### Proof

If one entry is `0`, (1.3) is immediate from the identity law.

If, say, `p=q`, then

```math
(p\circ p)\circ r=0\circ r=r
```

while

```math
p\circ(p\circ r)=r
```

by (1.1). The other repeated-variable cases are symmetric.

If `p,q,r` are distinct and collinear, then `p\circ q=r`, `q\circ r=p`, so

```math
(p\circ q)\circ r=r\circ r=0
```

and

```math
p\circ(q\circ r)=p\circ p=0.
```

`\square`

Thus, if

```math
R_{\rm ind}
=
\{(x,y,z)\in X^3:\ x,y,z\text{ distinct and }\{x,y,z\}\notin B\},
```

then

```math
|R_{\rm ind}|=6N=v(v-1)(v-3),
\tag{2.1}
```

where `N=v(v-1)(v-3)/6` is the number of unordered independent roots.

---

## 3. Root associators: three bracket values

For an ordered independent root `(x,y,z)` define

```math
u=(x\circ y)\circ z=a\circ z,
```

```math
v=x\circ(y\circ z)=x\circ b,
```

```math
w=(z\circ x)\circ y=c\circ y.
\tag{3.1}
```

Because the loop is commutative, the six permutations of the root test exactly the three pairwise equalities

```math
u=v,
\qquad
v=w,
\qquad
w=u,
\tag{3.2}
```

each equality occurring for two reversed orderings.

Consequently the number of failing ordered permutations of a fixed unordered independent root is always one of

```math
0,\ 4,\ 6.
\tag{3.3}
```

It is `0` when `u=v=w`, `4` when exactly two of `u,v,w` coincide, and `6` when they are pairwise distinct.

For a P-root, `u=v=w=x\circ y\circ z` in the elementary abelian group `C_2^3`, so all six root permutations associate.

For an H-root, identify its `S_9` closure with `AG(2,3)` and take, after an affine change of coordinates,

```math
x=(0,0),\qquad y=(1,0),\qquad z=(0,1).
```

For distinct points the Steiner product is `p\circ q=-p-q`. Then

```math
u=(1,2),\qquad v=(1,1),\qquad w=(2,1),
```

so `u,v,w` are pairwise distinct and all six root permutations fail associativity.

The D-phase is the dangerous case: even all six root permutations may associate without the root being P-phase.

---

## 4. Counterexample to the naive equivalence

The implication

> all six permutations of the root associate `=>` the root is P-phase

is false.

### Construction 4.1 (Pasch-traded `PG(3,2)`)

Start from the projective `STS(15)` on the nonzero vectors of `F_2^4`, with blocks

```math
\{p,q,p+q\}.
```

Choose

```math
x=e_1,\qquad y=e_2,\qquad z=e_3,
```

and put

```math
a=x+y,\qquad
b=y+z,\qquad
c=x+z,\qquad
t=x+y+z.
```

Choose `d=e_4`. The following four projective blocks form a Pasch configuration:

```text
{a,b,c}
{a,d,a+d}
{b,d,b+d}
{c,a+d,b+d}
```

Replace them by the complementary Pasch trade

```text
{a,b,d}
{a,c,a+d}
{b,c,b+d}
{d,a+d,b+d}.
```

The result is again an `STS(15)`.

None of the six blocks

```text
{x,y,a}
{y,z,b}
{z,x,c}
{a,z,t}
{x,b,t}
{y,c,t}
```

is touched by the trade. Therefore, for the root `{x,y,z}`,

```math
u=v=w=t,
```

so **all six root permutations associate**.

However the block `{a,b,c}` has been removed and the pair `a,b` now completes to `d`. Thus

```math
a\circ b=d\ne c.
```

The root closure is no longer the Fano plane. It is not H-phase either, because an H-root has all six root permutations nonassociative. Hence the root is D-phase.

This counterexample shows that root associativity alone does not characterize P-phase, even if every permutation of the root associates.

`\square`

---

## 5. The missing local identity

The missing condition is itself an associativity identity, but at a derived triple.

Since `a=x\circ y`, the Steiner identity gives

```math
a\circ y=x.
```

Therefore

```math
\operatorname{Assoc}(a,y,z)
```

is equivalent to

```math
(a\circ y)\circ z
=
a\circ(y\circ z),
```

hence to

```math
x\circ z=a\circ b,
```

or

```math
\boxed{a\circ b=c.}
\tag{5.1}
```

Thus the missing Fano block `{a,b,c}` is exactly one nearby associativity test.

---

## 6. Exact local bridge

### Theorem 6.1 (three-associator certificate for P-phase)

Let `(x,y,z)` be any ordered independent root, and let `a=x\circ y`. Then the underlying unordered root `tau={x,y,z}` is P-phase if and only if the following three identities hold:

```math
\operatorname{Assoc}(x,y,z),
\tag{6.1}
```

```math
\operatorname{Assoc}(y,z,x),
\tag{6.2}
```

```math
\operatorname{Assoc}(x\circ y,y,z).
\tag{6.3}
```

Equivalently: P-phase is characterized by two cyclic root-associator tests plus one derived-associator test.

### Proof

If the root is P-phase, its closure together with `0` is the elementary abelian group `C_2^3`; hence all three identities hold.

Conversely, write `a,b,c` as in (1.2). From (6.1),

```math
a\circ z=x\circ b.
\tag{6.4}
```

From (6.2),

```math
b\circ x=y\circ c.
\tag{6.5}
```

By commutativity, the right side of (6.4) equals the left side of (6.5). Hence there is a common point `t` with

```math
a\circ z=b\circ x=c\circ y=t.
\tag{6.6}
```

By Section 5, (6.3) is exactly

```math
a\circ b=c.
\tag{6.7}
```

The seven points

```math
x,y,z,a,b,c,t
```

are distinct because the root is independent and the Steiner loop has cancellation via (1.1). They support the seven blocks

```text
{x,y,a}
{y,z,b}
{z,x,c}
{a,z,t}
{b,x,t}
{c,y,t}
{a,b,c}.
```

These seven triples contain `7*3=21` distinct pairs, which is every pair on seven points. Hence they form a closed `STS(7)`, necessarily the Fano plane. Therefore `tau` is P-phase.

`\square`

### Corollary 6.2

The naive root-only criterion can be repaired in either of two equivalent forms:

1. the root is P-phase iff all six root permutations associate **and** `a\circ b=c`;
2. the root is P-phase iff all six root permutations associate **and** the derived triple `(a,y,z)` associates.

The Pasch-trade example in Section 4 satisfies the root-only part and fails exactly the derived test.

---

## 7. Quantitative global bridge

Let

```math
F_{\rm assoc}
=
|\{(p,q,r)\in L^3:
(p\circ q)\circ r\ne p\circ(q\circ r)\}|.
\tag{7.1}
```

By Lemma 2.1, every failure lies in `R_ind`.

Define the associativity-failure density conditioned on ordered independent triples by

```math
\delta_{\rm ind}
=
\frac{F_{\rm assoc}}{6N}.
\tag{7.2}
```

Also define the full multiplication-table density

```math
\delta_L
=
\frac{F_{\rm assoc}}{(v+1)^3}.
\tag{7.3}
```

### Theorem 7.1 (two-sided phase/associator comparison)

For every `STS(v)`,

```math
\boxed{
\frac{1-\rho_P}{3}
\le
\delta_{\rm ind}
\le
1-\rho_P.
}
\tag{7.4}
```

Equivalently,

```math
\boxed{
\frac{v(v-1)(v-3)}{3(v+1)^3}(1-\rho_P)
\le
\delta_L
\le
\frac{v(v-1)(v-3)}{(v+1)^3}(1-\rho_P).
}
\tag{7.5}
```

In particular, on any sequence with `v\to\infty`,

```math
\delta_L=\Theta(1-\rho_P)
```

with absolute constants.

### Proof

Let

```math
M=6N(1-\rho_P)
```

be the number of ordered independent roots whose underlying unordered root is not P-phase.

**Upper bound.** If an ordered independent triple fails associativity, its underlying root cannot be P-phase, since the Fano closure is associative. Therefore

```math
F_{\rm assoc}\le M.
\tag{7.6}
```

This gives the upper inequality in (7.4).

**Lower bound.** For each ordered independent root `r=(x,y,z)`, Theorem 6.1 gives

```math
1_{\{r\text{ non-P}\}}
\le
1_{\{\neg\operatorname{Assoc}(x,y,z)\}}
+
1_{\{\neg\operatorname{Assoc}(y,z,x)\}}
+
1_{\{\neg\operatorname{Assoc}(x\circ y,y,z)\}}.
\tag{7.7}
```

Sum (7.7) over `R_ind`.

The first map

```math
(x,y,z)\mapsto(x,y,z)
```

is the identity on `R_ind`.

The second map

```math
(x,y,z)\mapsto(y,z,x)
```

is a bijection of `R_ind`.

The third map

```math
T(x,y,z)=(x\circ y,y,z)
\tag{7.8}
```

is also a bijection of `R_ind`: independence is preserved, and

```math
T^2(x,y,z)=((x\circ y)\circ y,y,z)=(x,y,z)
```

by (1.1).

Hence each of the three sums on the right side of (7.7) is exactly `F_assoc`. Therefore

```math
M\le3F_{\rm assoc}.
\tag{7.9}
```

Combining (7.6) and (7.9) yields (7.4). Multiplying by

```math
\frac{6N}{(v+1)^3}
=
\frac{v(v-1)(v-3)}{(v+1)^3}
```

gives (7.5).

`\square`

---

## 8. Consequence for the edit-rigidity program

The projective branch of Article II gives, in the P-dominant regime,

```math
1-\rho_P=O(\varepsilon),
\qquad
\varepsilon=c_A/N.
```

Theorem 7.1 immediately converts this into

```math
\boxed{\delta_L=O(\varepsilon).}
\tag{8.1}
```

No extra local charging lemma is needed: the conversion is constant-factor and reversible.

Thus the next projective task is now sharply isolated:

> **Almost-associative Steiner-loop stability.** If a finite Steiner loop of order `v+1` has `\delta_L=o(1)`, must its multiplication table be `o(1)`-close to an associative elementary abelian `2`-group table, with quantitative control strong enough to recover block edit distance?

This is the correct place to invoke or prove an external almost-associativity stability theorem. Any such theorem must be checked against the special facts already available here: commutativity, exponent `2`, inverse property, and the exact same underlying set size.

---

## 9. Closed conclusions

1. Associativity failures occur only on ordered independent STS roots.
2. P-roots have zero root associator failures; H-roots have six.
3. Even **zero failures on all six permutations of a root does not imply P-phase**; an explicit Pasch trade in `PG(3,2)` gives a D-root counterexample.
4. P-phase has an exact constant-size certificate consisting of three associativity identities, two at the root and one at a derived root.
5. The global associativity-failure density and the non-P phase density satisfy the two-sided bound (7.4), hence are equivalent up to factor `3`.
6. Therefore Article II's P-dominant phase stability already implies an `O(\varepsilon)` almost-associative Steiner loop.

This closes `PROJECTIVE_ASSOCIATOR_BRIDGE` at the local-to-algebraic level. The remaining projective obstruction is no longer the bridge; it is the stability/reconstruction theorem from an almost-associative Steiner loop to a nearby Boolean group / projective STS.
