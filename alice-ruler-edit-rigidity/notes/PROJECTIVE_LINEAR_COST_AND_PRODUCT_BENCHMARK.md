# PROJECTIVE_LINEAR_COST_AND_PRODUCT_BENCHMARK

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed quantitative necessity theorem + infinite product benchmark, 2026-09-13  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`, `PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT.md`

---

## 1. Purpose

The surviving projective stability conjecture is formulated using the partial-core cost

```math
D_{pc}(S,\mathcal P).
```

This note establishes two facts needed before attempting an upper stability theorem.

1. **Linear necessity.** Small partial-core cost forces small associator/P-phase defect with an explicit linear bound. Thus any possible stability theorem has a fundamentally linear lower scale.
2. **Projective-product benchmark.** Direct products of two projective Steiner triple systems give an infinite wrong-order family with `rho_P -> 1` that is naturally close, in `D_pc`, to a larger projective model. The exact formulas show that `D_pc` and associator defect have the same first-order scale.

Together with Add-4 and sparse trades, this makes a linear partial-core stability conjecture the natural sharpened target.

---

## 2. Setup for the Lipschitz converse

Let

```math
S=(X,\mathcal B_S),
\qquad |X|=v,
```

be an `STS(v)`, and let

```math
P=(Y,\mathcal B_P),
\qquad |Y|=w,
```

be a projective STS, so `w+1` is a power of `2`.

Choose

```math
U\subseteq X,
\qquad
\phi:U\hookrightarrow Y.
```

Put

```math
R=X\setminus U,
\qquad r=|R|,
```

and

```math
h=|Y\setminus\phi(U)|.
```

Let `E` be the number of bad unordered pairs in `U` in the sense of `PROJECTIVE_PARTIAL_CORE_METRIC_AND_ADD4_AUDIT.md`: `{x,y}\subset U` is bad if either its `S`-completion leaves `U`, or its completion disagrees with the projective completion under `phi`.

Let

```math
N_*=\max\{v,w\}
```

and abbreviate

```math
D
:=
D_{pc}(S;P,U,\phi)
=
\frac{r+h}{N_*}
+
\frac{2E}{N_*(N_*-1)}.
\tag{2.1}
```

Let `s(S)` denote the total number of failed associativity triples in the associated Steiner loop. Since failures involving the loop identity, repeated points, or collinear triples are impossible, `s(S)` is also the number of failed ordered independent triples of nonzero STS points.

---

## 3. Four-pair certificate relative to a projective comparison

### Lemma 3.1

If `x,y,z\in U` and

```math
(x\circ y)\circ z\ne x\circ(y\circ z),
```

then at least one of the following four unordered pairs is bad:

```math
\{x,y\},
\qquad
\{y,z\},
\qquad
\{x\circ y,z\},
\qquad
\{x,y\circ z\}.
\tag{3.1}
```

### Proof

Assume all four pairs are good. Goodness of `{x,y}` and `{y,z}` implies

```math
a:=x\circ y\in U,
\qquad
b:=y\circ z\in U,
```

and

```math
\phi(a)=\phi(x)\oplus_P\phi(y),
\qquad
\phi(b)=\phi(y)\oplus_P\phi(z).
```

Goodness of the remaining two pairs gives

```math
\phi(a\circ z)=\phi(a)\oplus_P\phi(z),
```

and

```math
\phi(x\circ b)=\phi(x)\oplus_P\phi(b).
```

The projective Steiner loop is associative, so the two right-hand sides are equal. Injectivity of `phi` therefore yields

```math
a\circ z=x\circ b,
```

contradicting the assumed associativity failure. `\square`

---

## 4. Counting how many failures one bad pair can support

### Lemma 4.1

The associativity-failure count satisfies

```math
\boxed{
s(S)\le 3rv^2+8Ev.
}
\tag{4.1}
```

### Proof

First count failed ordered triples `(x,y,z)` having at least one coordinate in `R`. By a union bound there are at most

```math
3rv^2
```

ordered triples of this type.

Now take a failed triple entirely inside `U`. By Lemma 3.1 it can be charged to one of four bad-pair templates.

For a fixed bad unordered pair `e`:

- as `{x,y}`, it occurs in at most `2v` ordered triples;
- as `{y,z}`, again at most `2v`;
- as `{x\circ y,z}`, choose which endpoint of `e` is `z` (two choices), then for the other endpoint `a=x\circ y` there are at most `v-1` ordered pairs `(x,y)` with completion `a`, hence fewer than `2v` triples;
- as `{x,y\circ z}`, symmetrically fewer than `2v` triples.

Thus one bad pair supports fewer than `8v` charged ordered failures. Summing over the `E` bad pairs proves (4.1). `\square`

The estimate is deliberately simple; no optimization of the constant `8` is needed for the asymptotic conclusion.

---

## 5. Linear lower bound for partial-core cost

Write

```math
A=\frac{r+h}{N_*},
\qquad
B=\frac{2E}{N_*(N_*-1)},
```

so `D=A+B`.

Since

```math
w-v=h-r,
```

we have

```math
|w-v|\le r+h\le DN_*.
```

Hence, for `D<1`,

```math
\boxed{
\frac{N_*}{v}\le\frac1{1-D}.
}
\tag{5.1}
```

Also

```math
\frac rv
\le
\frac{A}{1-D},
\tag{5.2}
```

and

```math
\frac{2E}{v^2}
\le
\frac{B}{(1-D)^2}.
\tag{5.3}
```

Let

```math
\delta_{ind}(S)
=
\frac{s(S)}{v(v-1)(v-3)}.
```

### Theorem 5.1 (partial-core Lipschitz converse)

For every comparison `(P,U,phi)` with `D<1`,

```math
\boxed{
\delta_{ind}(S)
\le
\frac{4v^2}{(v-1)(v-3)}
\frac{D}{(1-D)^2}.
}
\tag{5.4}
```

Consequently, using the closed associator bridge,

```math
\boxed{
1-\rho_P(S)
\le
\frac{12v^2}{(v-1)(v-3)}
\frac{D}{(1-D)^2}.
}
\tag{5.5}
```

The same bounds hold with `D` replaced by the infimum `D_pc(S,\mathcal P)`.

### Proof

By Lemma 4.1,

```math
\frac{s(S)}{v^3}
\le
3\frac rv+8\frac{E}{v^2}.
```

Using (5.2)--(5.3),

```math
3\frac rv+8\frac{E}{v^2}
\le
\frac{3A}{1-D}
+
\frac{4B}{(1-D)^2}.
```

Since

```math
\frac3{1-D}\le\frac4{(1-D)^2},
```

this is at most

```math
\frac{4(A+B)}{(1-D)^2}
=
\frac{4D}{(1-D)^2}.
```

Multiplying by

```math
\frac{v^2}{(v-1)(v-3)}
```

gives (5.4).

The associator bridge proves

```math
1-\rho_P\le3\delta_{ind},
```

which gives (5.5). Taking an infimum over projective comparisons is legitimate by approximation of the infimum. `\square`

### Corollary 5.2 (asymptotic linear necessity)

Along any sequence with `v->infinity` and

```math
D_{pc}(S,\mathcal P)->0,
```

we have

```math
\boxed{
\delta_{ind}(S)
\le(4+o(1))D_{pc}(S,\mathcal P),
}
\tag{5.6}
```

and

```math
\boxed{
1-\rho_P(S)
\le(12+o(1))D_{pc}(S,\mathcal P).
}
\tag{5.7}
```

Equivalently,

```math
\boxed{
D_{pc}(S,\mathcal P)
\ge
\frac{1-\rho_P(S)}{12+o(1)}.
}
\tag{5.8}
```

Thus any future upper stability result must be at least linear in the phase impurity in the worst case; there is no possibility of a genuinely sublinear distance scale such as `o(1-rho_P)` uniformly.

---

## 6. Direct product of two projective STS

We now test the partial-core conjecture on a broad wrong-order family, not just Add-4.

Let

```math
m=2^a-1,
\qquad
n=2^b-1,
```

with `a,b>=2`. Let `S_m` and `S_n` be the projective Steiner triple systems on

```math
A=\mathbb F_2^a\setminus\{0\},
\qquad
B=\mathbb F_2^b\setminus\{0\}.
```

Their Steiner quasigroup laws are

```math
u\star v
=
\begin{cases}
 u,&u=v,\\
 u+v,&u\ne v.
\end{cases}
```

The direct product STS `S_m x S_n` is the standard Steiner-quasigroup direct product on

```math
X=A\times B,
\qquad |X|=V=mn,
```

with

```math
(u,s)\star(v,t)
=(u\star v,s\star t).
\tag{6.1}
```

This direct-product construction is standard; see M. Aryapoor, *The Pasch configuration and Steiner triple systems*, arXiv:1306.1257, Section 2.3.

Unless accidental small cases occur, `V+1=mn+1` is not a power of `2`, so this is generally a wrong projective order.

---

## 7. Three block types and exact local Pasch counts

Let

```math
b(t)=t(t-1)/6.
```

Blocks of the product fall into three types.

### Type H

A projective block in `A` and a fixed point of `B`.

Count:

```math
n b(m).
```

For such a block,

```math
\boxed{p_H=m-3.}
\tag{7.1}
```

### Type V

A fixed point of `A` and a projective block in `B`.

Count:

```math
m b(n).
```

For such a block,

```math
\boxed{p_V=n-3.}
\tag{7.2}
```

### Type D

A projective block in each factor together with one of the six bijections between their three points.

Count:

```math
6b(m)b(n).
```

For such a block,

```math
\boxed{
p_D=(m-2)(n-2)-1.
}
\tag{7.3}
```

### Proof of the local counts

Fix a projective factor block `{x,y,a}` with `a=x+y`, and orient it so the associativity/Pasch test through that block uses an external point `z`.

In a projective Steiner quasigroup one checks directly that

```math
(a\star z)=x\star(y\star z)
```

holds for every factor point `z` except exactly the two points `y,a`. Thus there are `m-2` successful factor choices, one of which is the first root point `x` itself.

For Type H the second coordinate is constant throughout the block. The second-coordinate identity holds only when the external second coordinate equals that constant. Removing the one block point that survives the first-coordinate test leaves `m-3` external successful points, proving (7.1). Type V is symmetric.

For Type D both coordinates vary along projective blocks. The test succeeds exactly when both coordinates avoid their respective two forbidden values, giving `(m-2)(n-2)` successful product points. Exactly one of the three block points is among them, so the external count is `(m-2)(n-2)-1`, proving (7.3). `\square`

---

## 8. Exact Pasch and associator defect formulas for the product

Each Pasch is counted through its four blocks, so

```math
P(S_m\times S_n)
=
\frac14\Bigl[
 n b(m)(m-3)
+m b(n)(n-3)
+6b(m)b(n)((m-2)(n-2)-1)
\Bigr].
\tag{8.1}
```

Equivalently,

```math
\boxed{
P(S_m\times S_n)
=
\frac{mn}{24}
\Bigl(
m^2n^2-3m^2n+3m^2-3mn^2+8mn-9m+3n^2-9n+9
\Bigr).
}
\tag{8.2}
```

Using the exact global identity

```math
s
=V(V-1)(V-3)-24P,
```

we obtain:

### Theorem 8.1 (exact product associator defect)

For `V=mn`,

```math
\boxed{
s(S_m\times S_n)
=3mn(m-1)(n-1)(m+n-2).
}
\tag{8.3}
```

Hence

```math
\boxed{
\delta_{ind}
=
\frac{3(m-1)(n-1)(m+n-2)}{(mn-1)(mn-3)}.
}
\tag{8.4}
```

If

```math
\min\{m,n\}\to\infty,
```

then

```math
\boxed{
\delta_{ind}
=
3\left(\frac1m+\frac1n\right)
+o\left(\frac1m+\frac1n\right)
\to0.
}
\tag{8.5}
```

By the associator bridge,

```math
\delta_{ind}
\le1-\rho_P
\le3\delta_{ind},
```

so these direct products give another infinite family of wrong-order systems with

```math
\boxed{\rho_P\to1.}
\tag{8.6}
```

---

## 9. Natural projective completion of the product

Consider the larger binary vector space

```math
\mathbb F_2^{a+b}
=\mathbb F_2^a\oplus\mathbb F_2^b.
```

Its nonzero vectors form a projective STS `P_W` of order

```math
W
=(m+1)(n+1)-1
=mn+m+n.
\tag{9.1}
```

Embed every product point by

```math
\phi:A\times B\hookrightarrow
(\mathbb F_2^a\oplus\mathbb F_2^b)\setminus\{0\},
\qquad
\phi(u,s)=(u,s).
\tag{9.2}
```

Take the full product carrier as the retained set:

```math
U=X.
```

The projective points not used by `phi` are exactly the two coordinate axes without the origin:

```math
(A\times\{0\})\cup(\{0\}\times B),
```

so there are

```math
\boxed{m+n}
\tag{9.3}
```

unused model points.

For two distinct product points `(u,s),(v,t)`:

- if `u!=v` and `s!=t`, their product completion is `(u+v,s+t)`, exactly the projective completion, and remains in `U`;
- if `u=v`, the product STS completion has first coordinate `u`, whereas the projective completion has first coordinate `0`;
- if `s=t`, symmetrically the second coordinate disagrees.

Thus a pair is bad exactly when its two points share one coordinate.

The two cases are disjoint for distinct points, so

```math
E
=m\binom n2+n\binom m2
=\frac{mn(m+n-2)}2.
\tag{9.4}
```

### Theorem 9.1 (exact product partial-core cost)

For the natural embedding (9.2),

```math
\boxed{
D_{pc}(S_m\times S_n;P_W,X,\phi)
=
\frac{m+n}{mn+m+n}
+
\frac{mn(m+n-2)}{(mn+m+n)(mn+m+n-1)}.
}
\tag{9.5}
```

Consequently, if `min{m,n}->infinity`,

```math
\boxed{
D_{pc}(S_m\times S_n,\mathcal P)
\le
2\left(\frac1m+\frac1n\right)
+o\left(\frac1m+\frac1n\right)
\to0.
}
\tag{9.6}
```

Combining with (8.5),

```math
\boxed{
\frac{D_{pc}(S_m\times S_n;P_W,X,\phi)}{\delta_{ind}}
\to\frac23.
}
\tag{9.7}
```

Thus this family exhibits an explicit **linear** defect-to-partial-core relation.

---

## 10. Interpretation

The projective product family is a substantially stronger benchmark than Add-4.

- The order mismatch is not constant: the natural projective completion adds `m+n` points.
- Nevertheless `m+n=o(mn)` when both factors grow.
- The multiplication error is supported exactly on pairs sharing one coordinate, again only `o(V^2)` pairs.
- The normalized associator defect is `Theta(1/m+1/n)`.
- The partial-core cost is also `Theta(1/m+1/n)`.

So a large class of wrong-order near-projective systems behaves exactly as the partial-core conjecture predicts.

The natural projective completion has a transparent geometry: the product carrier consists of the binary vectors having **both coordinate components nonzero**; the missing `m+n` projective points are precisely the two coordinate axes.

This is useful conceptually for Article III: wrong projective order need not be viewed as a mysterious global obstruction. It can arise from deleting a thin algebraic boundary from a genuine binary vector space and changing only the pair completions that touch that boundary.

---

## 11. Sharpened conjecture

All serious benchmark families checked so far have linear scale:

- sparse Pasch trades of projective systems;
- Grannell--Lovegrove Add-4;
- direct products of growing projective systems.

Theorem 5.1 proves the matching universal lower direction.

This motivates the stronger open target.

### Conjecture 11.1 (linear partial projective-core stability)

There exist absolute constants `C>0` and `epsilon_0>0` such that every sufficiently large Steiner triple system with

```math
1-\rho_P\le\epsilon_0
```

satisfies

```math
\boxed{
D_{pc}(S,\mathcal P)
\le C(1-\rho_P).
}
\tag{11.1}
```

A weaker qualitative version is

```math
1-\rho_P=o(1)
\Longrightarrow
D_{pc}(S,\mathcal P)=o(1).
```

Neither statement is proved here.

Theorem 5.1 shows that if a linear upper theorem holds, then it is of the correct order of magnitude:

```math
D_{pc}(S,\mathcal P)
=\Theta(1-\rho_P)
```

up to absolute constants in the small-defect regime.

---

## 12. Literature boundary

The standard direct product of Steiner quasigroups used in Section 6 is discussed in:

- M. Aryapoor, *The Pasch configuration and Steiner triple systems*, arXiv:1306.1257 (2013), Section 2.3.

The projective characterization by maximal Pasch count and the exact associative-triple/Pasch relation are classical and are also reviewed in:

- A. R. Kozlik, *The centre of a Steiner loop and the maxi-Pasch problem*, Comment. Math. Univ. Carolin. 61 (2020), 535--545, DOI `10.14712/1213-7243.2020.035`.

The exact product Pasch formulas (7.1)--(8.4), the partial-core computation (9.5), and the Lipschitz converse Theorem 5.1 are derived here for the present stability program. No claim of literature priority is made without a dedicated source search.

---

## 13. Closed conclusions

1. Partial-core closeness has a universal linear converse:

```math
1-rho_P
<=
[12v^2/((v-1)(v-3))]
D_pc/(1-D_pc)^2.
```

2. Hence asymptotically

```math
D_pc >= (1-rho_P)/(12+o(1)).
```

3. Direct products of two growing projective STS form an infinite wrong-order family with

```math
rho_P->1.
```

4. Their exact associator defect is

```math
s=3mn(m-1)(n-1)(m+n-2).
```

5. They possess a canonical partial-core embedding into `PG(a+b-1,2)` with exact cost (9.5).

6. In this family

```math
D_pc/\delta_ind -> 2/3,
```

so defect and structural distance have the same linear scale.

7. The natural sharpened open problem is therefore **linear partial projective-core stability**, not merely qualitative `o(1)` stability.
