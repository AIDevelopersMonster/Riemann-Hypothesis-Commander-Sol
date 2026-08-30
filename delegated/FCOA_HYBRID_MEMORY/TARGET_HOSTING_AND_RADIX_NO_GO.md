# FCOA Hybrid Memory — Target Hosting and Radix Factorization No-Go

**Status:** new hostile-audit strike after Article A publication  
**Context:** tests the hypothesis that AL0 might admit sublinear target-independent internal-law memory while AL2 forces linear internal-law memory.

## 1. Candidate resource and why it looked promising

Let `X_N` be the `N`-point target sector. Split primitive records into:

- **target attachments:** records incident with at least one point of `X_N`;
- **internal-law records:** records entirely inside auxiliary sectors.

Write

\[
M_{tot}=M_{att}+M_{int}.
\]

The previous digit AL2 construction used a dense arithmetic lookup table on a digit sort of size `b≈sqrt(N)`, so it had

\[
M_{int}=Theta(N).
\]

This suggested a possible separation:

\[
AL0:\ M_{int}=o(N),
\qquad
AL2:\ M_{int}=Omega(N).
\]

That separation is false under the endpoint-based definition above.

---

## 2. Target-hosted lookup tables

Take

\[
N=b^2
\]

and identify each target point with one ordered digit pair:

\[
X_N=\{t_{a,b}:a,b\in D\},
\qquad |D|=b.
\]

Use auxiliary digit points `D`. For each target point `t_{a,b}`, attach four digit roles

\[
A_1(t_{a,b},a),
\qquad
A_2(t_{a,b},b),
\]

and, for multiplication,

\[
H_\times(t_{a,b},h),
\qquad
L_\times(t_{a,b},r),
\]

where

\[
ab=hb+r,
\qquad 0\le h,r<b.
\]

Likewise attach output roles for digit addition with carry.

Every lookup-table row is therefore represented by one **target point** rather than by an auxiliary table-entry point.

The digit multiplication relation is uniformly FO recoverable by

\[
P(a,b;h,r)
\iff
\exists t\in X_N\,
\bigl(
A_1(t,a)\land A_2(t,b)\land
H_\times(t,h)\land L_\times(t,r)
\bigr).
\]

The addition table is recovered analogously.

All table records are incident with `X_N`. Hence

\[
\boxed{M_{int}=0}
\]

under the endpoint-based definition, while the complete digit arithmetic law is still present.

Total records remain linear:

\[
M_{tot}=Theta(N),
\]

because each target row carries only a constant number of digit attachments.

---

## 3. AL2 survives target hosting

Use the target-hosted digit relations as the local laws in the two-digit multiplication construction.

Write target numbers as

\[
x=ib+j,
\qquad
y=kb+l,
\qquad z=hb+r.
\]

The same constant-size school-multiplication FO formula used in `RTP_INTERPRETATION_NO_GO.md` recovers exact truncated multiplication from the hosted digit add/multiply relations.

Therefore there exists a fixed bounded-arity, linearly sized presentation with

\[
\boxed{FTR=2,\qquad M_{tot}=Theta(N),\qquad M_{int}=0.}
\]

### Theorem HM-TH-NOGO

Endpoint-based internal-law memory is not a semantic resource invariant, even under BF1 recovery and linear total size.

### Reason

A law table can be moved from auxiliary entry points onto already-existing target points without changing its logical content or asymptotic total size. The endpoint classification changes from `internal` to `attachment`, but the encoded arithmetic law does not.

Thus

\[
\boxed{
AL2\not\Rightarrow M_{int}=Omega(N)
}
\]

for the naive endpoint-based `M_int`.

---

## 4. Why this is not merely a bookkeeping trick

Each target point already has a unique pair of digit coordinates. Hence the `N=b^2` target points form exactly the right row index set for a complete binary table on `b` digits.

No additional tuple-power universe is required. The target sector itself supplies the `D^2` table-entry space.

This exposes a general phenomenon:

\[
\boxed{
\text{a large target sector can act as free address space for auxiliary laws.}
}
\]

Any resource definition that declares every target-incident record “cheap attachment memory” is therefore vulnerable to law hosting.

---

## 5. Stronger no-go: arbitrarily small internal exponent by radix factorization

Suppose target hosting is forbidden and law tables must genuinely live in auxiliary sectors. Even then a positive internal-law exponent does not separate AL0 from AL2.

Fix an integer radix width

\[
k\ge2.
\]

Choose a bottom digit set `D` of size

\[
s\asymp N^{1/k}.
\]

Represent every target number by a fixed `k`-tuple of base-`s` digits:

\[
x=(d_{k-1},\ldots,d_0),
\qquad |D|^k\ge N.
\]

Because `k` is fixed, the representation uses only

\[
kN=Theta(N)
\]

target-to-digit attachments.

Store complete bottom-level digit tables for:

- comparison/order on `D`;
- add-with-carry;
- multiply-and-split.

Each complete binary digit table has

\[
Theta(s^2)=Theta(N^{2/k})
\]

rows.

Only a constant number of such tables is needed.

Hence

\[
\boxed{M_{int}=O(N^{2/k}).}
\]

For any prescribed

\[
\varepsilon>0,
\]
choose a fixed

\[
k>2/\varepsilon.
\]

Then

\[
\boxed{M_{int}=O(N^\varepsilon).}
\]

while total target attachments remain `Theta(N)`.

---

## 6. Exact AL0, AL1 and AL2 at arbitrary positive internal exponent

Because `k` is a fixed constant independent of `N`, a single FO formula may quantify all required digit/carry witnesses.

### AL0

Lexicographically compare the `k` base-`s` digits. This uses the bottom digit order only.

### AL1

Perform school addition across the fixed `k` digit positions using add-with-carry. The number of carry witnesses is `O(k)`, hence constant with respect to `N`.

### AL2

Perform school multiplication using the `O(k^2)` digit products and a constant network of carry/addition witnesses. Since `k` is fixed, the entire multiplication graph is defined by one fixed FO formula.

Thus for every `epsilon>0` there are presentations of all three phases with

\[
M_{tot}=Theta(N)
\]

and

\[
\boxed{M_{int}=O(N^\varepsilon).}
\]

Therefore the infimum internal-law exponent is zero for AL0, AL1 and AL2 alike:

\[
\boxed{
\inf \lambda_{int}(AL0)
=
\inf \lambda_{int}(AL1)
=
\inf \lambda_{int}(AL2)
=0.
}
\]

The infimum statement does not claim an `O(1)` internal-law realization at fixed bounded FO complexity; it says that no positive exponent separates the phases.

---

## 7. Depth–memory tradeoff

The failed invariant reveals a more stable tradeoff.

Let `k` be the fixed number of base digits. Then

\[
\lambda_{int}=\frac{2}{k}.
\]

Increasing `k` reduces internal law memory but increases the size/quantifier complexity of the recovering formula:

- AL0 comparison uses `O(k)` digit tests;
- AL1 addition uses `O(k)` carry witnesses;
- AL2 multiplication uses `O(k^2)` local products plus carry witnesses.

Thus the meaningful resource is no longer `M_int` alone but a **joint depth/width versus memory profile**.

A convenient normal-form parameter is

\[
\boxed{
\mathcal D=(k,\lambda_{int},q)
}
\]

with approximately

\[
\lambda_{int}=2/k,
\]

and phase-dependent formula complexity:

\[
q_{AL0}=O(k),
\qquad
q_{AL1}=O(k),
\qquad
q_{AL2}=O(k^2)
\]

at the direct school-arithmetic level.

These are constructive upper bounds, not lower bounds.

---

## 8. What has now failed

The resource-separation search has successively eliminated:

1. total cell exponent;
2. maximum degree;
3. literal channel count;
4. direct CRT resolution exponent;
5. interpretation dimension alone;
6. endpoint-based internal-law memory;
7. any fixed positive internal-law exponent when radix width is unrestricted but constant.

Each failure is caused by a concrete compression mechanism, not by a vague objection.

---

## 9. Corrected next candidate

A nontrivial separation can only emerge after **simultaneously bounding the amount of factorization available to the recovery formula**.

The natural next object is therefore a quantifier/decomposition-sensitive resource function.

For phase `j in {0,1,2}` and a fixed logical complexity budget `q`, define provisionally

\[
\Lambda_j(q)
=
\inf\left\{
\lambda:
\begin{array}{l}
\text{there exists a BF1 presentation of phase }j,\\
M_{tot}=Theta(N),\\
M_{int}=O(N^\lambda),\\
\text{recovery quantifier rank}\le q
\end{array}
\right\}.
\]

The constructive radix families show only that

\[
\Lambda_j(q)\to0
\]

as the permitted logical/decomposition complexity grows.

The sharp question becomes whether for **fixed small q** one has a genuine separation such as

\[
\boxed{
\Lambda_0(q)<\Lambda_2(q)
}
\]

or, more generally, whether multiplication requires more decomposition depth than order at equal internal-law exponent.

---

## 10. Current conclusion

The proposed `AL0 sublinear / AL2 linear` separation is false.

In fact:

\[
\boxed{
AL2\text{ can have }M_{int}=0
}
\]

if target hosting is allowed, and even under honest auxiliary storage:

\[
\boxed{
\forall\varepsilon>0:\quad
AL0,AL1,AL2\text{ all admit }M_{int}=O(N^\varepsilon)
}
\]

with total `Theta(N)` memory and fixed, but epsilon-dependent, FO formulas.

The surviving phase-boundary candidate is therefore **memory conditioned on bounded decomposition/logical depth**, not internal memory by itself.
