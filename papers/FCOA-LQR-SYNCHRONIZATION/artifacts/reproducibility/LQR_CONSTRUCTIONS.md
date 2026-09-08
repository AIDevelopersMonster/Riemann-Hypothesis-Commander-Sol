# QGE3 LQR — Exact Constructions

## 1. Exact formula for q=3

### Theorem 1.1
For every `r>=1`,

\[
\boxed{
L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil.
}
\]

The lower bound is proved in `LQR_LOWER_BOUNDS.md`.

### Three-phase synchronization gadget

Suppose one phase `rho` is already synchronized with the old block and two new phases are `sigma,tau in S_3`. Impose

\[
[rho,sigma;0],\qquad [rho,tau;1],\qquad [sigma,tau;2].
\]

After global left normalization take `rho=id`. Then

\[
sigma(0)=0,
\qquad
\tau(1)=1,
\qquad
\sigma(2)=\tau(2).
\]

We show `sigma=tau=id`.

Because `sigma` fixes `0`, its restriction to `{1,2}`` is either the identity or the transposition `(1 2)`. Because `tau` fixes `1`, its restriction to `{0,2}` is either the identity or `(0 2)`.

If `sigma=(1 2)`, then `sigma(2)=1`; but `tau(1)=1`, so bijectivity forbids `tau(2)=1`. Hence `sigma` cannot be `(1 2)`, so `sigma=id` and `sigma(2)=2`. Then `tau(2)=2`; together with `tau(1)=1`, this forces `tau=id`.

Thus three constraints synchronize two new phases to an already synchronized phase.

### Recursive construction

Base cases:

- `r=1`: cost `0`;
- `r=2`: impose two point-image equalities, e.g. colors `0,1`, cost `2`;
- `r=3`: use the three-phase gadget, cost `3`.

For every additional pair of phases, attach them to one already synchronized anchor phase using the three constraints above. Therefore

- for odd `r=2k+1`, cost `3k=3(r-1)/2`;
- for even `r=2k`, cost `2+3(k-1)=(3r-2)/2=ceil(3(r-1)/2)`.

This matches the lower bound. \(\square\)

---

## 2. Exact formula for r=2

### Theorem 2.1
For every `q>=2`,

\[
\boxed{L_q(2)=q-1.}
\]

### Construction
Impose

\[
\pi_1(a)=\pi_2(a)
\]

for any fixed `q-1` source colors. Two permutations agreeing on `q-1` points agree on the final point. The lower bound is in `LQR_LOWER_BOUNDS.md`. \(\square\)

---

## 3. Exact formula for r=3

### Theorem 3.1
For every `q>=3`,

\[
\boxed{L_q(3)=2q-3.}
\]

### Construction
Let the three phases be `pi_0,pi_1,pi_2`.

On source colors `0,1,2`, impose the three-color triangle gadget

\[
[0,1;0],
\qquad
[0,2;1],
\qquad
[1,2;2].
\]

For every remaining source color `a=3,...,q-1`, impose

\[
[0,1;a],
\qquad
[0,2;a].
\]

Total cost:

\[
3+2(q-3)=2q-3.
\]

To prove synchronization, left-normalize `pi_0=id`. For every `a>=3`, the two constraints force

\[
\pi_1(a)=\pi_2(a)=a.
\]

Therefore both `pi_1` and `pi_2` preserve the remaining set `{0,1,2}` and restrict there to elements of `S_3`. The first three constraints are exactly the three-phase `S_3` gadget of Section 1, so both restrictions are the identity. Hence

\[
\pi_0=\pi_1=\pi_2=id.
\]

The lower bound `2q-3` is proved independently in `LQR_LOWER_BOUNDS.md`. \(\square\)

---

## 4. General construction beating the old spanning-tree bound

The published safe construction used

\[
(q-1)(r-1)
\]

constraints by identifying each pair of adjacent phases on `q-1` source colors along a spanning tree.

The exact `q=3` theorem gives a systematic improvement for every `q>=3`.

### Theorem 4.1 — three-active-color reduction

For every `q>=3` and `r>=1`,

\[
\boxed{
L_q(r)
\le
(q-3)(r-1)
+
\left\lceil\frac{3(r-1)}2\right\rceil.
}
\]

### Proof
Choose `q-3` source colors and synchronize each of them across all `r` phases using a spanning tree. This costs `(q-3)(r-1)` constraints.

After global left normalization by the inverse of one phase, every phase fixes those `q-3` colors pointwise. Consequently every phase restricts to a permutation of the remaining three colors.

On those three active colors apply an optimal `L_3(r)` synchronization system. By Theorem 1.1 this costs `ceil(3(r-1)/2)`.

The resulting tuple is diagonal. \(\square\)

The gain over the naive bound is

\[
(q-1)(r-1)
-
\left[(q-3)(r-1)+\left\lceil\frac{3(r-1)}2\right\rceil\right]
=
2(r-1)-\left\lceil\frac{3(r-1)}2\right\rceil,
\]

which equals `floor((r-1)/2)`.

Thus for every `q>=3`,

\[
\boxed{
L_q(r)\le(q-1)(r-1)-\left\lfloor\frac{r-1}{2}\right\rfloor.
}
\]

This is a uniform strict improvement whenever `r>=3`.

---

## 5. Current exact frontier

We now have theorem-level exact formulas on three infinite slices:

\[
\boxed{L_2(r)=r-1,}
\]

\[
\boxed{L_3(r)=\left\lceil\frac{3(r-1)}2\right\rceil,}
\]

\[
\boxed{L_q(2)=q-1,}
\]

and, independently,

\[
\boxed{L_q(3)=2q-3.}
\]

The remaining genuinely two-parameter regime begins at

\[
q\ge4,\qquad r\ge4.
\]

The quotient/unique-coloring formulation in `LQR_DEFINITIONS.md` is intended for that regime.
