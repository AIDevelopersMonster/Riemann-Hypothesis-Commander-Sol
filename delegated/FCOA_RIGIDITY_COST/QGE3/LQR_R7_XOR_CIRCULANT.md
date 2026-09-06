# QGE3 LQR — XOR Resolution Equivalence and Translation-Circulant Identities

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** active structural continuation  
**Scope:** pure defect-two synchronization, with `r=7` as the first critical case  
**Proof status:** analytic for the XOR reduction and circulant/Pfaffian identities; the final fifteen-plane parity theorem remains open

This note records two structural reductions that substantially simplify the remaining `r=7` barrier. The first removes the set-disjointness condition from the resolution problem. The second embeds the resulting additive matching problem into the regular representation of the elementary abelian group `F_2^6` and yields an exact complementary-Pfaffian identity.

---

## 1. Oriented partial line spreads

Let

\[
V=\mathbb F_2^d.
\]

An oriented projective line is a triple

\[
L_a=\{p_a,u_a,v_a\},
\qquad
p_a=u_a+v_a,
\]

where `p_a` is distinguished as the **parent** and `u_a,v_a` are the two **children**.

Let

\[
\mathcal L=\{L_a:a\in[q]\}
\]

be a family of pairwise point-disjoint lines. Put

\[
P=\{p_a:a\in[q]\},
\qquad
C=\{u_a,v_a:a\in[q]\}.
\]

Then

\[
|P|=q,\qquad |C|=2q,\qquad P\cap C=\varnothing.
\]

In the original LQR setting with `r=7`, normalized cuts live in `F_2^6`; every defect-two partition plane gives exactly such an oriented line.

---

## 2. Relaxed XOR resolutions

A **relaxed XOR resolution** of `(P,C)` is a perfect matching of the `2q` child points together with a bijective labeling of its `q` edges by the parent points such that an edge labeled by `p` joins points `x,y` satisfying

\[
\boxed{x+y=p.}
\]

The canonical resolution consists of the original pairs `u_a v_a` labeled by `p_a`.

For arbitrary oriented partial line spreads, this additive notion is the natural re-resolution problem.

For partition-realizable LQR lines there is a priori an extra condition: when vectors are regarded as subsets of the `d` coordinate set, a valid resolution pair must satisfy

\[
x\cap y=\varnothing,
\qquad
x\cup y=p.
\]

The next theorem shows that the additional condition is automatic.

---

## 3. XOR–Resolution Equivalence

### Theorem 3.1
Let the oriented lines arise from partition-realizable defect-two colors. Then every relaxed XOR resolution is automatically a genuine set-partition resolution.

Equivalently,

\[
\boxed{
\text{genuine resolutions}
=
\text{relaxed XOR resolutions}.
}
\]

### Proof
Fix a coordinate `t`. For any set/vector `x`, write `x_t in {0,1}` for its `t`-th coordinate.

Because every canonical line satisfies

\[
p_a=u_a\sqcup v_a,
\]

we have the exact **integer** equality

\[
\sum_{c\in C} c_t
=
\sum_{p\in P} p_t.
\tag{3.1}
\]

Now take any relaxed XOR resolution. Consider one matched pair `x,y` labeled by `p`, so

\[
x+y=p
\]

in `F_2^d`.

If `p_t=1`, then `x_t!=y_t`, so the pair contributes exactly one to the left side of (3.1).

If `p_t=0`, then `x_t=y_t`, so the pair contributes either zero or two. Let `k_t` be the number of parent labels with `p_t=0` for which the matched pair has

\[
x_t=y_t=1.
\]

Summing over all matched pairs gives

\[
\sum_{c\in C}c_t
=
\sum_{p\in P}p_t+2k_t.
\tag{3.2}
\]

Comparison with the fixed canonical equality (3.1) yields

\[
k_t=0.
\]

This holds for every coordinate `t`. Hence no matched pair has a coordinate in which both endpoints equal one. Therefore

\[
x\cap y=\varnothing.
\]

Together with `x+y=p`, this implies

\[
x\cup y=p.
\]

Thus every relaxed XOR resolution is a genuine partition resolution. \(\square\)

### Consequence 3.2
For the LQR pure-plane sector, the resolution problem can be studied entirely in the additive group `F_2^{r-1}`. The apparently extra Boolean disjointness condition carries no additional information once one asks for a **complete** re-resolution.

This is an exact reduction, not a parity-only statement.

---

## 4. Additive matching formulation

After Theorem 3.1, the `r=7,q=15` barrier becomes the following additive problem.

Let

\[
V=\mathbb F_2^6,
\qquad
|P|=15,
\qquad
|C|=30,
\qquad
P\cap C=\varnothing.
\]

Assume `C` has at least one perfect matching whose 15 distinct edge differences are exactly the points of `P`.

The desired parity theorem is:

> the number of such `P`-rainbow perfect matchings of `C` is even.

The canonical oriented partial line spread supplies one such matching.

If the parity theorem holds for arbitrary oriented partial 15-line spreads in `PG(5,2)`, then it holds a fortiori for partition-realizable LQR families and gives `M_7<=14`.

---

## 5. The full translation circulant

For every `p in V`, let `T_p` be the `64 x 64` permutation matrix of translation

\[
x\longmapsto x+p.
\]

For a parent set `P` introduce commuting variables `z_p` and define

\[
G(z)=\sum_{p\in P} z_p T_p,
\qquad
s(z)=\sum_{p\in P}z_p.
\]

Because translations commute and satisfy

\[
T_p^2=I,
\]

in characteristic two we obtain

\[
\boxed{
G(z)^2=s(z)^2 I.
}
\tag{5.1}
\]

Indeed all mixed terms occur twice and cancel.

Since every parent is nonzero, every `T_p` has zero diagonal, so `G(z)` is alternating over `F_2[z]`.

Over the fraction field, whenever `s!=0`,

\[
\boxed{
G(z)^{-1}=\frac{G(z)}{s(z)^2}.
}
\tag{5.2}
\]

Taking determinants in (5.1) gives

\[
\det G=s^{64}.
\]

Since `det G=(Pf G)^2` for an alternating matrix,

\[
\boxed{
\operatorname{Pf}G=s^{32}.
}
\tag{5.3}
\]

---

## 6. Child and complementary minors

Let `C subset V` be the 30 child points and put

\[
D=V\setminus C.
\]

Thus

\[
|C|=30,
\qquad
|D|=34.
\]

In the `q=15` canonical situation,

\[
D=\{0\}\sqcup P\sqcup H,
\]

where `H` is the set of 18 unused nonzero points.

The principal minor `G_C` is precisely the color-weighted XOR complement graph on the children. Hence

\[
[z_{p_1}\cdots z_{p_{15}}]\operatorname{Pf}G_C
\]

is the parity of `P`-rainbow child resolutions.

### Theorem 6.1 — complementary Pfaffian identity

For the complementary principal minors,

\[
\boxed{
\operatorname{Pf}G_D
=
s^2\operatorname{Pf}G_C.
}
\tag{6.1}
\]

### Proof
Jacobi's complementary-minor identity gives

\[
\det G_D
=
\det G\;\det (G^{-1})_C.
\]

Using (5.2) and (5.3),

\[
\det G_D
=
s^{64}\cdot s^{-60}\det G_C
=
s^4\det G_C.
\]

Both principal minors are alternating, hence

\[
(\operatorname{Pf}G_D)^2
=
s^4(\operatorname{Pf}G_C)^2.
\]

The polynomial ring over `F_2` is an integral domain and Frobenius squaring is injective, so

\[
\operatorname{Pf}G_D
=
s^2\operatorname{Pf}G_C.
\]
\(\square\)

### General form 6.2
For every even subset `S subseteq V`,

\[
\boxed{
\operatorname{Pf}G_{V\setminus S}
=
s^{32-|S|}\operatorname{Pf}G_S.
}
\]

The proof is identical.

---

## 7. Half-size corollaries

For a parent `p_i`, define

\[
C_i=C\cup\{0,p_i\},
\qquad
D_i=D\setminus\{0,p_i\}.
\]

Both sets have size 32 and are complementary. Hence

\[
\operatorname{Pf}G_{C_i}=\operatorname{Pf}G_{D_i}.
\]

Inside `C_i`, the vertex `0` can be matched only to `p_i`, via the color `p_i`. Therefore expansion at `0` gives

\[
\operatorname{Pf}G_{C_i}
=z_i\operatorname{Pf}G_C.
\]

Consequently

\[
\boxed{
\operatorname{Pf}G_{D_i}
=z_i\operatorname{Pf}G_C.
}
\tag{7.1}
\]

Summing the corresponding expansions of `Pf G_D` at the vertex `0` recovers (6.1).

---

## 8. Boolean specialization

For a subset `S subseteq P`, specialize

\[
z_p=1\ (p\in S),
\qquad
z_p=0\ (p\notin S).
\]

Write the resulting matrix as `G_S`. Then (5.1) becomes

\[
\boxed{
G_S^2=(|S|\bmod2)I.
}
\tag{8.1}
\]

Hence:

- if `|S|` is odd, `G_S` is an involution and is invertible;
- if `|S|` is even, `G_S` is square-zero and therefore has rank at most 32.

Let

\[
f_C(S)=\operatorname{Pf}(G_S)_C,
\qquad
f_D(S)=\operatorname{Pf}(G_S)_D.
\]

Specializing (6.1) gives the exact Boolean relation

\[
\boxed{
f_D(S)=(|S|\bmod2)f_C(S).
}
\tag{8.2}
\]

Thus the child Pfaffian parity function is tied to rank/minor strata of square-zero group-circulant operators on even subsets and invertible involutions on odd subsets.

---

## 9. Group-algebra filtration

Identify the regular representation algebra with

\[
\mathbb F_2[V]
\cong
\mathbb F_2[t_1,\dots,t_6]/(t_1^2,\dots,t_6^2),
\]

where `t_i=T_{e_i}+I`, and let `J=(t_1,\dots,t_6)` be the augmentation ideal.

For an even subset `S`, the group-algebra element

\[
g_S=\sum_{p\in S}T_p
\]

has zero augmentation and lies in `J`. Its image in `J/J^2` is exactly

\[
\boxed{
\bigoplus_{p\in S}p\in V.
}
\tag{9.1}
\]

Hence the even subsets split naturally into:

- first-order strata with nonzero XOR sum;
- deeper strata with zero XOR sum, for which `g_S in J^2`.

This filtration is a promising route to the remaining mixed-Pfaffian coefficient, but no complete rank theorem sufficient for the fifteen-plane parity result is claimed here.

---

## 10. The remaining parity barrier

The exact theorem still needed is:

### Oriented 15-Line Parity Conjecture
Let 15 pairwise point-disjoint oriented projective lines in `PG(5,2)` have parent set `P` and child set `C`. Then the number of perfect matchings of `C` whose 15 distinct edge differences are exactly `P` is even.

Equivalently,

\[
\boxed{
[z_{p_1}\cdots z_{p_{15}}]\operatorname{Pf}G_C(z)=0.
}
\]

Computational evidence is strong:

- parity is mixed at `q=13,14`;
- hundreds of arbitrary oriented `q=15` partial spreads tested so far have even parity;
- the known synchronizing LQR 14-plane system has odd parity;
- every tested line extension of that system to 15 oriented lines has even parity.

The present note does not promote this evidence to a theorem.

If the conjecture is proved, then every compatible LQR fifteen-plane family has a noncanonical resolution, so

\[
M_7\le14.
\]

Together with the explicit synchronizing fourteen-plane construction already recorded,

\[
\boxed{M_7=14}.
\]

---

## 11. Scope firewall

1. The XOR–Resolution Equivalence is proved only for the partition-realizable LQR Boolean interpretation; the additive re-resolution problem is then extended as a separate, stronger geometric conjecture to arbitrary oriented partial line spreads.
2. The translation-circulant and complementary-Pfaffian identities are exact algebraic statements over `F_2`.
3. The oriented 15-line parity statement remains conjectural in this note.
4. No failure to find an odd fifteen-line example is treated as a proof.
