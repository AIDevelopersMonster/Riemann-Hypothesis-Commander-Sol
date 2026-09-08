# FCOA Rigidity Cost — Affine Bad-Set Theorem for Fixed Extension Geometry

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** new post-publication theorem; Articles A and B remain frozen.

---

## 1. Setup

Let

\[
D\subseteq G^2\setminus\Delta,
\qquad c:D\to\mathbf F_2,
\]

and fix a set of new cells

\[
E\subseteq (G^2\setminus\Delta)\setminus D.
\]

The geometry `E` is fixed. The only variables are the binary colors

\[
b:E\to\mathbf F_2.
\]

Put

\[
D_E=D\cup E,
\qquad c_b=c\cup b.
\]

Let

\[
\Gamma_E=\{h\in S_G:hD_E=D_E\}
\]

be the carrier automorphism group of the **uncolored extended domain**.

For `p in D_E`, define the cell-value function

\[
x_p(b)=
\begin{cases}
 c(p),&p\in D,\\
 b(p),&p\in E.
\end{cases}
\]

For `h in Gamma_E`, define the discrepancy

\[
\delta_{h,p}(b)=x_{hp}(b)\oplus x_p(b).
\]

Because `hp` may lie in either `D` or `E`, each `delta_{h,p}` is an affine-linear function of the coordinates of `b`.

---

## 2. Reduct-survival space for an arbitrary extended-domain symmetry

### Theorem 2.1

For fixed `E` and fixed `h in Gamma_E`, the set

\[
\mathcal S_h(E)
=
\{b\in\mathbf F_2^E:
 h\in\operatorname{Aut}(G;D_E,Q_{D_E}^{c_b})
\}
\]

is either empty or an affine subspace of `F_2^E`.

### Proof

For adjacent ordered cells `p~q` in the fixed incidence graph `Lambda(D_E)`, preservation of the ternary equality relation is exactly

\[
x_p(b)=x_q(b)
\iff
x_{hp}(b)=x_{hq}(b).
\]

Over `F_2` this is equivalent to

\[
\delta_{h,p}(b)=\delta_{h,q}(b).
\]

Each side is affine-linear in `b`, so every adjacency gives an affine-linear equation. Their common solution set is therefore an affine subspace, possibly empty. \(\square\)

This theorem includes both old automorphisms preserving `D` and genuinely new domain-moving automorphisms which interchange old and new cells.

---

## 3. Component phase functions

Let

\[
\pi_0(\Lambda(D_E))=\{C_1,\dots,C_s\}.
\]

On `S_h(E)`, Theorem 2.1 implies that the discrepancy is constant on each component. Choose one representative cell `p_i in C_i` and define

\[
\theta_{h,i}(b)=\delta_{h,p_i}(b).
\]

Restricted to `S_h(E)`, each `theta_{h,i}` is a well-defined affine-linear phase function independent of the chosen representative.

The carrier permutation `h` is a full anonymous automorphism of the colored extension exactly when one global binary phase works on all cells, i.e.

\[
\theta_{h,1}(b)=\cdots=\theta_{h,s}(b).
\]

---

## 4. Bad-color set for one carrier permutation

Define

\[
\mathcal B_h(E)
=
\{b\in\mathbf F_2^E:
 h\in\operatorname{Aut}(G;D_E,Q_{D_E}^{c_b})
\setminus
\operatorname{Aut}^{\pm}(D_E,c_b)
\}.
\]

Choose `C_1` as a base component. Then

\[
\boxed{
\mathcal B_h(E)
=
\bigcup_{i=2}^s
\left(
\mathcal S_h(E)
\cap
\{b:\theta_{h,i}(b)\oplus\theta_{h,1}(b)=1\}
\right).
}
\]

### Theorem 4.1 — affine-union bad set

For fixed `E` and `h in Gamma_E`, `B_h(E)` is a union of at most

\[
\boxed{s-1}
\]

affine subspaces of `F_2^E`.

### Proof

A surviving `h` is bad exactly when its component phase vector is non-diagonal. This occurs iff at least one component phase differs from the base phase. Over `F_2`, inequality is the affine equation

\[
\theta_{h,i}(b)\oplus\theta_{h,1}(b)=1.
\]

Intersecting this affine hyperplane with the affine survival space `S_h(E)` gives an affine subspace, possibly empty. Taking the union over `i=2,...,s` gives the formula. \(\square\)

### Important nuance

`B_h(E)` need not itself be a single affine subspace. The exact general statement is **finite affine union**.

In particular, the multicomponent badness condition is a disjunction of affine phase-disagreement slices.

---

## 5. Exact fixed-geometry unsafe set

Define the total unsafe-color set

\[
\mathcal U(E)
=
\{b\in\mathbf F_2^E:
(G;D_E,Q_{D_E}^{c_b})
\text{ is not carrier-exact}
\}.
\]

Then

\[
\boxed{
\mathcal U(E)
=
\bigcup_{h\in\Gamma_E}
\mathcal B_h(E).
}
\]

Hence:

### Theorem 5.1 — fixed-geometry affine-cover theorem

For every fixed extension geometry `E`, the unsafe binary colorings form a finite union of affine subspaces of the color cube

\[
\boxed{\mathbf F_2^E.}
\]

The exact colorings are precisely

\[
\boxed{
\mathbf F_2^E\setminus\mathcal U(E).
}
\]

Therefore

\[
\boxed{
E\text{ admits an exact coloring}
\iff
\mathcal U(E)\ne\mathbf F_2^E.
}
\]

This applies equally to old and newly created carrier symmetries.

---

## 6. Exact formula for alpha

The preceding theorem gives the fixed-geometry characterization

\[
\boxed{
\alpha(D,c)
=
\min_E
\left\{
|E|:
\mathbf F_2^E
\setminus
\bigcup_{h\in\Gamma_E}\mathcal B_h(E)
\ne\varnothing
\right\}.
}
\]

Thus `alpha` is exactly a minimum-size **affine-cover avoidance problem**, with the important complication that the acting group `Gamma_E` itself depends on the chosen cell geometry `E`.

For fixed `E`, however, all color dependence is affine-linear.

---

## 7. Exact formula for beta inside the same framework

Let

\[
B_{\rm old}=A_Q(D,c)\setminus A_{\rm an}(D,c).
\]

For an old bad automorphism `g`, if it survives an extension then it cannot become globally anonymous on the enlarged coloring: a global anonymous action would restrict to a global anonymous action on the old layer, contradicting `g in B_old`.

Therefore for old bad `g`, its forbidden set is simply the full survival space

\[
\mathcal S_g(E).
\]

Consequently

\[
\boxed{
\beta(D,c)
=
\min_E
\left\{
|E|:
\mathbf F_2^E
\setminus
\bigcup_{g\in B_{\rm old}}
\mathcal S_g(E)
\ne\varnothing
\right\}.
}
\]

This agrees with the orbit-sensitive formula in `ORBIT_SENSITIVE_REPAIR.md`.

---

## 8. Safe-Minimizer becomes an affine-cover statement

Let `m=beta(D,c)` and let `E` be a beta-optimal geometry. Define the old-safe region

\[
\mathcal O(E)
=
\mathbf F_2^E
\setminus
\bigcup_{g\in B_{\rm old}}
\mathcal S_g(E).
\]

By beta-optimality, `O(E)` is nonempty for at least one geometry of size `m`.

The stronger conjecture

\[
\alpha=\beta
\]

is equivalent to:

> there exists a beta-optimal geometry `E` such that `O(E)` is not covered by the affine bad slices contributed by carrier permutations in `Gamma_E` that are not old bad automorphisms.

Equivalently,

\[
\boxed{
\exists E,\ |E|=\beta:
\mathcal O(E)
\setminus
\bigcup_{h\in\Gamma_E\setminus B_{\rm old}}
\mathcal B_h(E)
\ne\varnothing.
}
\]

So the unresolved Safe-Minimizer problem is now literally an affine-subspace covering problem in a finite binary cube.

---

## 9. Fatal geometries

A fixed geometry `E` is **fatal** if

\[
\mathcal U(E)=\mathbf F_2^E,
\]

so no binary coloring of its new cells can yield exactness.

A particularly strong sufficient condition for fatality is the existence of `h in Gamma_E` with

\[
\mathcal B_h(E)=\mathbf F_2^E.
\]

Such an `h` is an unavoidable bad symmetry of that geometry, independent of the coloring.

This notion cleanly separates:

- unsafe **color choices** on a salvageable geometry;
- intrinsically unsafe **geometries**.

The unsafe one-cell beta witness found earlier is salvageable only by changing geometry, because both colors on that particular cell remain bad.

---

## 10. Codimension criterion

Write the nonempty affine slices in a representation of `U(E)` as

\[
A_1,\dots,A_M\subseteq\mathbf F_2^E,
\]

and let

\[
\operatorname{codim}(A_j)=\rho_j.
\]

Since

\[
|A_j|=2^{|E|-\rho_j},
\]

the union bound gives:

### Corollary 10.1

If

\[
\boxed{
\sum_{j=1}^M2^{-\rho_j}<1,
}
\]

then `E` admits an exact coloring.

This criterion is sufficient, not necessary; affine slices can overlap heavily.

A relative version applies inside the old-safe region by counting intersections with `O(E)`.

---

## 11. Quotient-phase compression

The affine-union representation using at most `s-1` slices per carrier permutation is already much smaller than enumerating all `2^s-2` non-diagonal phase vectors.

For each surviving `h`, only the phase differences

\[
\theta_{h,i}\oplus\theta_{h,1}
\]

matter. These form an affine map

\[
\Phi_h:\mathcal S_h(E)\to\mathbf F_2^{s-1}.
\]

The bad set is precisely

\[
\boxed{
\mathcal B_h(E)=
\Phi_h^{-1}(\mathbf F_2^{s-1}\setminus\{0\}).
}
\]

Thus each carrier permutation is controlled by a finite-dimensional **relative phase map**.

The kernel `Phi_h^{-1}(0)` is exactly the anonymous-compatible part of its survival space.

---

## 12. Structural consequence

The original automorphism problem has now split into two layers:

\[
\boxed{
\text{choose geometry }E
\quad\longrightarrow\quad
\text{avoid affine bad sets in }\mathbf F_2^E.
}
\]

The geometry step determines:

- the uncolored domain automorphism group `Gamma_E`;
- the enlarged incidence components;
- the affine equations defining each `S_h(E)` and `B_h(E)`.

After that, the entire binary coloring problem is linear/affine over `F_2`.

This is the strongest current reduction of the Safe-Minimizer problem.

---

## 13. Next theorem target

The next target is an **Affine Non-Covering Theorem for beta-optimal geometries**.

Possible routes:

1. prove a codimension lower bound for every genuinely new bad slice;
2. bound the number of distinct maximal bad slices using orbit structure of `Gamma_E`;
3. exploit the large overlap forced among slices corresponding to the same domain-moving orbit;
4. choose among beta-optimal geometries one minimizing the affine-cover density

\[
\frac{|\mathcal U(E)|}{2^{|E|}}.
\]

If one can show this minimum is always strictly below 1, then

\[
\boxed{\alpha=\beta}
\]

follows.

---

## 14. Claim firewall

1. For fixed `h`, the reduct-survival set is affine.
2. The bad set for fixed `h` is generally a **union** of affine subspaces, not necessarily one affine subspace.
3. The total unsafe set for fixed geometry is a finite affine union.
4. The acting domain group depends on `E`; the global minimization over geometries remains nonlinear.
5. The codimension criterion is sufficient only.
6. The theorem is binary-specific; no multicolor analogue is claimed here.
