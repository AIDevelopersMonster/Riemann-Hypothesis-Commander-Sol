# QGE3 LQR — Hyperplane Moments and the PDS Equality Regime at r=7

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** pure defect-two compatible 15-plane families on seven phases  
**Proof status:** analytic hyperplane moment identities and equality-case theorem; explicit equality witness verified computationally; the global `M_7=14` barrier remains open

This note records the hyperplane structure of a fifteen-line partial spread in `PG(5,2)` and isolates a rigid exceptional regime in which the eighteen holes form a `(64,18,2,6)` partial difference set.

---

## 1. Setup

Let

\[
V=\mathbb F_2^6,
\]

and let

\[
\mathcal L=\{L_1,\dots,L_{15}\}
\]

be fifteen pairwise point-disjoint projective lines. Thus the occupied set has

\[
45
\]

nonzero points and the hole set

\[
H=(V\setminus\{0\})\setminus\bigcup_iL_i
\]

has

\[
|H|=18.
\]

For every nonzero linear functional `a in V*`, let

\[
\Pi_a=\ker a
\]

be the corresponding projective hyperplane and define

\[
m_a=\#\{i:L_i\subseteq\Pi_a\}.
\]

There are 63 hyperplanes.

---

## 2. First two hyperplane moments

### Proposition 2.1
For every fifteen-line partial spread in `PG(5,2)`,

\[
\boxed{\sum_{a\ne0}m_a=225}
\]

and

\[
\boxed{\sum_{a\ne0}\binom{m_a}{2}=315.}
\]

### Proof
A projective line spans a 2-dimensional vector subspace. Exactly

\[
2^{6-2}-1=15
\]

nonzero linear functionals vanish on it. Hence each of the fifteen lines is counted in exactly fifteen hyperplanes, giving

\[
15\cdot15=225.
\]

Two disjoint projective lines span a 4-dimensional vector subspace. Exactly

\[
2^{6-4}-1=3
\]

nonzero functionals vanish on that span. Hence every unordered pair of the fifteen lines lies in exactly three hyperplanes, giving

\[
3\binom{15}{2}=315.
\]
\(\square\)

---

## 3. Fourier transform of the hole set

Let

\[
h=1_H
\]

on the additive group `V`, with `h(0)=0`, and let

\[
\widehat h(a)=\sum_{x\in V}h(x)(-1)^{a\cdot x}.
\]

### Proposition 3.1
For every nonzero `a`,

\[
\boxed{\widehat h(a)=14-4m_a.}
\]

### Proof
A line contained in `ker a` contributes three occupied points to the hyperplane, while a line not contained in it meets the hyperplane in exactly one projective point. Thus the occupied set contributes

\[
3m_a+(15-m_a)=15+2m_a
\]

points to `ker a\setminus{0}`.

The hyperplane has 31 nonzero points, so

\[
|H\cap\ker a|=31-(15+2m_a)=16-2m_a.
\]

Since `|H|=18`,

\[
\widehat h(a)=|H\cap\ker a|-|H\setminus\ker a|
=2(16-2m_a)-18
=14-4m_a.
\]
\(\square\)

---

## 4. Hole-line identity

Let

\[
L_H
\]

denote the number of projective lines lying entirely in the hole set.

### Theorem 4.1
For every fifteen-line partial spread,

\[
\boxed{
L_H=231-\sum_{a\ne0}\binom{m_a}{3}.
}
\]

### Proof
The number of ordered pairs `(x,y)` of distinct hole points for which `x+y` is again a hole equals `6L_H`, since every projective line `{x,y,x+y}` contributes its six ordered pairs.

Equivalently,

\[
\sum_{x,y\in V}h(x)h(y)h(x+y)=6L_H.
\]

Fourier inversion on the group of order 64 gives

\[
64\cdot6L_H=\sum_{a\in V^*}\widehat h(a)^3.
\]

The trivial character contributes `18^3`. For `a!=0`, use Proposition 3.1 and expand

\[
(14-4m)^3
=
2744-1744m+960\binom m2-384\binom m3.
\]

Substituting the two moment identities from Proposition 2.1 and simplifying yields

\[
384L_H=384\left(231-\sum_{a\ne0}\binom{m_a}{3}\right).
\]
\(\square\)

---

## 5. Hyperplane-dense inequality

Assume

\[
m_a\ge3
\qquad\text{for all }a\ne0.
\]

For every integer `m>=3`,

\[
\binom m3-3\binom m2+6m-10
=
\frac{(m-3)(m-4)(m-5)}6
\ge0.
\]

Summing over all 63 hyperplanes and using the first two moments gives

\[
\sum_a\binom{m_a}{3}
\ge
3\cdot315-6\cdot225+10\cdot63
=225.
\]

Therefore Theorem 4.1 implies

\[
\boxed{m_a\ge3\ \forall a\ne0\quad\Longrightarrow\quad L_H\le6.}
\]

This is a purely projective statement; no LQR partition realizability is used.

---

## 6. Equality case

### Theorem 6.1
Under the hyperplane-dense assumption `m_a>=3`, equality

\[
L_H=6
\]

is equivalent to

\[
\sum_a\binom{m_a}{3}=225,
\]

and then every `m_a` belongs to `{3,4,5}`. The two moment equations force in fact

\[
\boxed{
\#\{a:m_a=3\}=45,
\qquad
\#\{a:m_a=5\}=18,
\qquad
\#\{a:m_a=4\}=0.
}
\]

### Proof
Equality in the summed cubic inequality requires equality pointwise. For integer `m>=3`, equality occurs exactly at `m=3,4,5`. Write their multiplicities as `n_3,n_4,n_5`. Then

\[
n_3+n_4+n_5=63,
\]

\[
3n_3+4n_4+5n_5=225,
\]

\[
3n_3+6n_4+10n_5=315.
\]

Solving gives

\[
n_3=45,\quad n_4=0,\quad n_5=18.
\]
\(\square\)

Hence the nontrivial Fourier spectrum of the hole indicator is

\[
\boxed{2^{(45)},\quad(-6)^{(18)}}
\]

with the trivial value `18` at zero.

---

## 7. Partial-difference-set consequence

Assume the equality case. Let

\[
S=\{a\ne0:\widehat h(a)=-6\},
\qquad |S|=18.
\]

Since the remaining 45 nontrivial Fourier values equal `2`, Fourier inversion gives

\[
\sum_{a\in S}(-1)^{a\cdot x}
=2-8h(x)
\qquad(x\ne0).
\]

The ordered difference multiplicity

\[
N(g)=\#\{(x,y)\in H^2:x+y=g\}
\]

therefore satisfies

\[
\boxed{
N(g)=
\begin{cases}
2,&g\in H,\\
6,&g\notin H,\ g\ne0.
\end{cases}}
\]

Thus `H` is a regular partial difference set with parameters

\[
\boxed{(64,18,2,6).}
\]

In particular, for each `g in H` there is exactly one unordered pair `{x,y} subset H` with

\[
x+y=g.
\]

Hence the eighteen holes partition uniquely into six disjoint projective lines.

Therefore every equality-case fifteen-line partial spread extends to a full 21-line spread of `PG(5,2)` by adjoining those six hole lines.

---

## 8. Explicit partition-realizable equality witness

The following compatible fifteen-plane LQR family was obtained by exact MILP search:

```text
(15, 57, 86, 98, 114, 127, 143, 190, 196, 201, 204, 243, 244, 275, 288)
```

Its parent cut-points are

```text
60,30,62,57,45,61,29,31,23,55,47,59,27,39,63
```

and its thirty child cut-points are

```text
12,48,22,8,18,44,41,16,13,32,5,56,9,20,7,
24,19,4,3,52,11,36,17,42,1,26,33,6,25,38
```

with

\[
\bigoplus P=\bigoplus C=0.
\]

Its hyperplane distribution is exactly

\[
3^{45},5^{18}.
\]

The eighteen holes are

```text
2,10,14,15,21,28,34,35,37,40,43,46,49,50,51,53,54,58
```

and split into the six projective lines

```text
(2,49,51)
(10,34,40)
(14,37,43)
(15,53,58)
(21,35,54)
(28,46,50)
```

The exact resolution count of the original fifteen-color system is

\[
\boxed{776=8\cdot97,}
\]

so its resolution parity is zero.

This family is therefore a useful adversarial test object for any proposed proof of the fifteen-plane parity theorem.

---

## 9. Nonuniqueness of the exceptional orbit

A no-good MILP enumeration produced several additional compatible partition-realizable fifteen-plane families satisfying `m_a>=3` for every hyperplane. The first eight solutions all had the same equality distribution

\[
3^{45},5^{18}
\]

but canonicalization under the natural `S_7` action gave distinct representatives.

Therefore one must **not** identify the hyperplane-dense regime with a single `S_7` orbit. The rigid object is the PDS/full-spread geometry, not a unique labeled LQR family.

No theorem is currently claimed that every partition-realizable hyperplane-dense family must attain equality `L_H=6`, although every exact example found so far does.

---

## 10. Failed simple full-spread averaging

In the equality case, adjoining the six hole lines gives a full 21-line spread. For any orientation of those six new lines, the 42-child Pfaffian satisfies the complementary identity

\[
\operatorname{Pf}G_{C^+}=s^{10}\operatorname{Pf}G_{D^+}.
\]

Since in characteristic two

\[
s^{10}=\left(\sum z_i^8\right)\left(\sum z_i^2\right),
\]

it has no squarefree degree-10 monomial, so the full 21-color rainbow coefficient vanishes.

However, two tempting reductions fail:

1. there need not exist an orientation of the six added lines for which each new color has only its canonical child edge;
2. averaging over all `3^6` orientations does not pair all mixed full resolutions automatically — examples with full-rank `6 x 6` orientation-incidence matrix occur.

Thus the full-spread completion is structurally useful but does not by itself prove the original fifteen-color parity theorem.

---

## 11. Current dichotomy target

The hyperplane moment theory suggests the following division of the global parity problem:

### Generic regime
There exists a hyperplane with

\[
m_H\le2.
\]

Then almost all selected lines cross the two hyperplane cosets, suggesting a reduction to a lower-dimensional prescribed-difference matching problem.

### Exceptional regime
Every hyperplane satisfies

\[
m_H\ge3.
\]

Then

\[
L_H\le6.
\]

All partition-realizable examples found so far attain the rigid equality case `L_H=6`, hence have `(64,18,2,6)` PDS holes and extend to a full spread.

The immediate exact subproblem is therefore:

\[
\boxed{
\text{Does partition realizability plus }m_H\ge3\ \forall H
\text{ force }L_H=6?
}
\]

A positive answer would reduce the fifteen-plane parity theorem to two sharply different and much smaller cases.

---

## 12. Rigorous status

Nothing in this note by itself proves the global parity theorem. The LQR extremal status remains

\[
\boxed{14\le M_7\le21.}
\]
