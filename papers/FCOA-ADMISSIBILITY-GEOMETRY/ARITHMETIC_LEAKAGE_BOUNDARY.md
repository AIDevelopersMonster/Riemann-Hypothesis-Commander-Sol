# Arithmetic Leakage Boundary after G4

**Project:** FCOA Admissibility Geometry  
**Status:** main-line theorem candidate / classical calibration + new FCOA reduction step  
**Date opened:** 2026-08-27  
**Publication boundary:** post-publication; not part of Zenodo DOI 10.5281/zenodo.22129787

## 1. Why the next step is a boundary theorem, not G5

G4-A gives a uniformly definable total order on the generic sector:

\[
x<y
\iff
x,y\in G_N
\land
x\otimes_{4A}y=P_1\otimes_{4A}P_0.
\]

The next question is therefore no longer whether FCOA can remember orientation. It can.

The question is:

\[
\boxed{
\text{How much arithmetic, if any, is forced once exact order is internally available?}
}
\]

The first task is to prove a left wall: G4-A is still an **order-level** structure, not an additive or multiplicative arithmetic structure.

The second task is to identify a minimal geometric relation whose appearance would genuinely cross that wall.

## 2. Canonical rank relations on the generic sector

Let

\[
G_N=\{P_2,\ldots,P_N\},
\qquad
m=N-1.
\]

Externally define the rank map only for metamathematical comparison:

\[
\operatorname{rk}_N(P_{k+2})=k,
\qquad
0\le k<m.
\]

This rank map is **not** added to the FCOA signature.

Define the canonical truncated arithmetic graphs:

\[
\operatorname{Add}_N(x,y,z)
\iff
\operatorname{rk}_N(z)
=
\operatorname{rk}_N(x)+\operatorname{rk}_N(y)
<m,
\]

and

\[
\operatorname{Mul}_N(x,y,z)
\iff
\operatorname{rk}_N(z)
=
\operatorname{rk}_N(x)\operatorname{rk}_N(y)
<m.
\]

The leakage question is whether one formula in the FCOA signature defines these relations uniformly for every \(N\).

## 3. Order-Reduction Theorem for G4-A

### Theorem 3.1 — finite-copy order reduction

Let \(\mathfrak A_N\) be the full G4-A partial-operation structure, including the terminal outputs

\[
E_i^\ast,
\quad
E_i^\times,
\quad
\Omega_+,
\quad
\Omega_-.
\]

The family \(\{\mathfrak A_N:N\ge3\}\) is uniformly obtainable from the family of finite linear orders

\[
L_m=([m],<),
\qquad m=N-1,
\]

by a fixed finite-copy first-order interpretation/transduction.

### Construction

From one ordered generic copy \(G\), create fixed tagged copies:

\[
G,
\qquad
E^\ast(G),
\qquad
E^\times(G),
\]

and four fixed singleton tags

\[
b_0,b_1,\omega_+,\omega_-.
\]

Interpret

\[
P_0=b_0,
\qquad
P_1=b_1,
\]

and identify the ordered generic copy with

\[
P_2<\cdots<P_N.
\]

The operation graph is then given entirely by equality, tags and the order relation:

\[
b_0\otimes b_1=b_0,
\]

\[
b_0\otimes x=b_0
\qquad(x\in G),
\]

\[
x\otimes b_0=E^\ast(x),
\]

\[
b_1\otimes x=x,
\qquad
x\otimes b_1=x,
\]

\[
x\otimes x=E^\times(x),
\]

\[
x\otimes y=\omega_+
\qquad(x<y),
\]

\[
x\otimes y=\omega_-
\qquad(y<x),
\]

and the G4-A anchor is

\[
b_1\otimes b_0=\omega_+.
\]

All remaining cells are undefined.

Thus the complete G4-A operation is uniformly reconstructed from a finite linear order plus finitely many fixed tags/copies. \(\square\)

### Consequence

Every uniform first-order relation definable in G4-A pulls back, on the generic copy, to a first-order relation over finite linear orders.

This is the key upper bound on arithmetic leakage at G4.

## 4. Finite Order-Wall Theorem

A classical finite-model-theoretic fact is that parity of the cardinality of finite linear orders is not first-order definable in the language of order.

Using that fact, G4-A cannot uniformly define the canonical rank addition or multiplication graphs.

### Theorem 4.1 — no uniform rank addition in G4-A

There is no parameter-free first-order formula \(\varphi_+(x,y,z)\) in the G4-A signature such that for every \(N\ge3\) and every \(x,y,z\in G_N\),

\[
\mathfrak A_N\models\varphi_+(x,y,z)
\iff
\operatorname{Add}_N(x,y,z).
\]

### Proof

Assume such a formula exists. By Theorem 3.1 it translates uniformly to an FO formula over finite linear orders defining truncated rank addition.

Let \(M\) be the maximum element of an \(m\)-element chain. Its rank is \(m-1\). Then

\[
\exists x\ \operatorname{Add}(x,x,M)
\]

holds exactly when \(m-1\) is even, i.e. exactly when \(m\) is odd.

Hence FO over finite linear orders would define cardinality parity, contradiction. \(\square\)

### Theorem 4.2 — no uniform rank multiplication in G4-A

There is no parameter-free first-order formula \(\varphi_\times(x,y,z)\) in the G4-A signature uniformly defining \(\operatorname{Mul}_N\).

### Proof

Again translate a hypothetical formula to FO over finite linear orders.

For every chain of length at least three, the element of rank \(2\) is uniformly FO-definable from order as the second successor of the minimum. Let it be \(T\), and let \(M\) be the maximum. Then

\[
\exists x\ \operatorname{Mul}(T,x,M)
\]

holds exactly when \(m-1\) is even.

Thus parity of chain length would be FO-definable on all sufficiently large finite linear orders. Finite exceptional sizes are themselves FO-definable and can be patched separately, yielding parity on all finite linear orders, contradiction. \(\square\)

Therefore:

\[
\boxed{
\text{G4-A uniformly defines order, but not canonical rank }+\text{ or }\times.
}
\]

## 5. Successor-only is not a higher leakage level

Once a total discrete order is present, successor is uniformly first-order definable:

\[
\operatorname{Succ}(x,y)
\iff
x<y
\land
\neg\exists z\,(x<z<y).
\]

Betweenness is likewise order-definable.

Therefore the earlier informal ladder

\[
\text{order}\to\text{successor}
\]

must not be read as an increase of first-order expressive power. In the G4-A environment, successor and betweenness are already consequences of order.

Conversely, on an infinite chain, pure successor does not first-order recover the transitive order. Thus successor-only is a weaker comparison layer, not a step beyond G4-A.

Because finite successor is itself FO-definable from order, Theorems 4.1 and 4.2 immediately imply that canonical rank addition and multiplication are not uniformly FO-definable from successor alone either.

## 6. Infinite Order-Wall Corollary

Define the natural infinite analogue \(\mathfrak A_\infty\) by taking

\[
G_\infty=P_2<P_3<P_4<\cdots
\]

and applying the same G4-A rules to all generic pairs.

The same finite-copy construction interprets \(\mathfrak A_\infty\) in

\[
(\mathbb N,<).
\]

The first-order theory of \((\mathbb N,<)\) is decidable; indeed the stronger monadic second-order theory is classically decidable. Hence the first-order theory of \(\mathfrak A_\infty\) is decidable as well.

Therefore:

### Corollary 6.1

\[
\boxed{
\mathfrak A_\infty
\text{ cannot parameter-free first-order interpret }
(\mathbb N,+,\times).
}
\]

Otherwise true first-order arithmetic would effectively reduce to the decidable theory of \(\mathfrak A_\infty\), contradicting the undecidability of true arithmetic.

The same decidability obstruction applies a fortiori to the pure successor structure \((\mathbb N,S)\), whose monadic second-order theory is also decidable.

This gives an infinite-carrier left wall:

\[
\boxed{
\text{order/successor memory does not by itself interpret full arithmetic.}
}
\]

## 7. The first genuine leakage gateway: variable gap geometry

Fixed finite distances do not cross the wall. For each fixed \(k\), the relation

\[
y=S^k(x)
\]

is already definable from order by a formula depending on \(k\).

What order does **not** provide is a variable displacement that can be compared across arbitrary intervals.

Define the directed equal-gap relation externally by ranks:

\[
\operatorname{EqGap}_N(a,b;c,d)
\iff
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c),
\]

with

\[
a\le b,
\qquad
c\le d.
\]

### Proposition 7.1 — Presburger Gateway

Over the ordered generic sector, uniform directed equal-gap geometry and truncated addition are first-order interdefinable.

Let \(0_G\) denote the least generic point.

If \(\operatorname{EqGap}\) is available, then

\[
\boxed{
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_G,y;x,z).
}
\]

Conversely, if truncated addition is available, then for forward intervals

\[
\boxed{
\operatorname{EqGap}(a,b;c,d)
\iff
\exists s\,
\bigl(
\operatorname{Add}(a,s,b)
\land
\operatorname{Add}(c,s,d)
\bigr).
}
\]

Thus the first natural geometric boundary beyond pure order is not another fixed successor relation but **variable equal displacement**.

Combining Proposition 7.1 with Theorem 4.1 gives immediately:

\[
\boxed{
\operatorname{EqGap}_N
\text{ is not uniformly FO-definable in G4-A.}
}
\]

This identifies a concrete FCOA-native target for the next construction.

## 8. Classical calibration of the leakage zones

The following classical structures calibrate the intended boundary. These are background facts, not FCOA novelty claims.

### Order zone

\[
(\mathbb N,<)
\]

has decidable first-order theory and lies below uniform addition.

### Presburger zone

\[
(\mathbb N,<,+)
\]

has decidable first-order theory. Multiplication is not first-order definable there; otherwise full arithmetic would inherit decidability.

### Full-arithmetic zone

In

\[
(\mathbb N,<,\times),
\]

addition is classically first-order definable from order, successor and multiplication (Robinson-style definability). Hence this structure reaches full first-order arithmetic strength.

So the calibration ladder is

\[
\boxed{
\text{order}
\;<\;
\text{order + addition}
\;<\;
\text{order + multiplication}
\simeq
\text{full first-order arithmetic},
}
\]

where the displayed relations describe definability/expressive-strength calibration, not an FCOA operation hierarchy.

## 9. Revised leakage levels for the FCOA programme

The main line should therefore use the following levels.

### AL0 — Order Wall

Uniformly definable total order, hence also successor and betweenness, but no uniformly definable canonical rank addition/multiplication.

G4-A is at AL0.

### AL1 — Additive / Presburger Leakage

A variable displacement relation such as \(\operatorname{EqGap}\), or equivalently truncated rank addition, becomes uniformly definable.

This is genuine arithmetic leakage, but not yet full arithmetic.

### AL2 — Full Arithmetic Leakage

A mechanism strong enough to define multiplication in the additive ordered structure, or otherwise uniformly interpret full first-order arithmetic.

The transition

\[
\boxed{
AL0\to AL1
}
\]

is now the immediate research target.

## 10. What the next construction is allowed to seek

Do **not** add arbitrary arithmetic cells.

The next branch, if opened, must target the weakest FCOA-native mechanism that makes variable displacement comparable while preserving as much of the G4 discipline as possible.

Preferred questions:

1. Can equal-gap geometry be encoded in definedness without differentiated values?
2. Can a bounded anonymous output alphabet encode equal-gap classes?
3. Can two partial operations jointly recover \(\operatorname{EqGap}\) while neither does alone?
4. What is the minimum domain density / output alphabet / anchor cost for AL0 \(\to\) AL1?
5. Does any candidate accidentally jump directly to AL2?

The main line should not open a numbered successor branch until one of these mechanisms has a clean minimal witness.

## 11. Literature calibration

Classical results used as external calibration include:

- J. R. Büchi, decidability of the monadic second-order theory of successor/order on the natural numbers;
- R. McNaughton and S. Papert, first-order logic with order and star-free languages, including the standard parity inexpressibility consequence for finite linear orders/words;
- M. Presburger, decidability of first-order addition on the natural numbers;
- J. Robinson, definability results showing the strength of multiplication together with order/successor.

No priority claim is made for these classical logical facts. The FCOA-specific contribution in this note is the reduction of the exact G4-A family to the order wall and the identification of variable equal-gap geometry as the first natural leakage gateway.

## 12. Status

The direct G4-A interpretation and the EqGap/addition interdefinability are proved above. The finite inexpressibility step depends on the classical theorem that parity is not FO-definable on finite linear orders. The infinite non-interpretability step depends on classical decidability/undecidability results.

Current classification:

\[
\boxed{
\mathbf W:\ \text{Arithmetic Leakage Boundary theorem candidate; hostile audit pending.}
}
\]

No new G5 operation cells have been introduced.
