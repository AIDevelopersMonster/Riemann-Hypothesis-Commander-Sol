# SOL-QFIELD — Minimal Finite History Memory and the Unitary-Character Obstruction

**Version:** 0.4  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FOURTH TARGET COMPLETE / H1 PROVED / MINIMAL 3-STATE HISTORY MONOID / UNITARY SCALARIZATION NO-GO  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`

---

## 1. Executive verdict

The previous report reduced the next frontier to the trichotomy

\[
H0/H1/H2:
\]

- `H0`: every natural compositional history quotient collapses the two radial associator histories;
- `H1`: a nontrivial finite/local history memory survives;
- `H2`: every nontrivial history distinction forces unbounded compositional memory.

For the native radial subtheory this question can now be answered exactly.

### Main theorem

The two elementary root-interaction step types

\[
L:\ x_0\oplus x_k=x_k,
\qquad
R:\ x_k\oplus x_0=\rho(x_k)
\tag{1}
\]

generate radial evaluation words. The native associator diamond has histories

\[
LR
\qquad\text{and}\qquad
RL.
\tag{2}
\]

There is a 3-element monoid

\[
M_{\mathrm{first}}=\{1,\ell,r\}
\tag{3}
\]

that remembers only the first nonempty step type and satisfies

\[
\ell^2=\ell,
\qquad
r^2=r,
\qquad
\ell r=\ell,
\qquad
r\ell=r.
\tag{4}
\]

The word map

\[
h(\varepsilon)=1,
\qquad
h(Lw)=\ell,
\qquad
h(Rw)=r
\tag{5}
\]

is a monoid homomorphism and distinguishes the two native histories:

\[
h(LR)=\ell\ne r=h(RL).
\tag{6}
\]

No 1- or 2-element monoid can do this. Hence three memory states are cardinality-minimal.

Therefore

\[
\boxed{\texttt{H1 is proved for the radial evaluation subtheory}.}
\tag{7}
\]

The history fiber is finite and does not force an unbounded independent coordinate.

### Stronger negative result

The minimal monoid is intrinsically irreversible/idempotent. Any homomorphism

\[
U:M_{\mathrm{first}}\to\mathcal U(H)
\tag{8}
\]

into a unitary group collapses both nonidentity memory states:

\[
U(\ell)=U(r)=I.
\tag{9}
\]

Thus the smallest compositional history memory that distinguishes \(LR\) from \(RL\) **cannot itself carry a nontrivial unitary phase representation**.

This yields the new boundary

\[
\boxed{
\text{finite history distinction}
\not\Rightarrow
\text{reversible/unitary phase memory}.
}
\tag{10}
\]

The next question is whether a slightly richer but still finite history quotient can distinguish the paths while admitting a nontrivial unitary representation, or whether reversible phase memory necessarily requires retaining an unbounded/free-path layer.

---

## 2. Radial rule alphabet

The signed radial operation satisfies, for \(k\ne0\),

\[
x_0\oplus x_k=x_k,
\tag{11}
\]

\[
x_k\oplus x_0=\rho(x_k),
\qquad
\rho(x_k)=x_{k-\operatorname{sgn}(k)}.
\tag{12}
\]

We label applications of (11) and (12) by the intrinsic operand role of the root:

\[
L:=\text{root occurs in the left input slot},
\tag{13}
\]

\[
R:=\text{root occurs in the right input slot}.
\tag{14}
\]

These labels do not refer to positive versus negative branch. Reflection fixes the root and swaps branch sign while preserving operand position. Therefore the alphabet \(\{L,R\}\) is reflection-invariant.

The native radial diamond from v0.3 consists of the two evaluation histories

\[
\pi_L: LR,
\qquad
\pi_R: RL.
\tag{15}
\]

Both have the same extensional endpoint \(\rho(x_k)\) for \(|k|\ge2\), but their first legal rule applications have different roles.

---

## 3. The first-role monoid

### Definition 3.1

Let

\[
M_{\mathrm{first}}=\{1,\ell,r\}.
\tag{16}
\]

Define multiplication by

\[
1m=m1=m
\qquad(m\in M_{\mathrm{first}}),
\tag{17}
\]

and for \(a,b\in\{\ell,r\}\),

\[
ab=a.
\tag{18}
\]

Thus the first nonidentity factor wins.

The multiplication table is

| \(\cdot\) | \(1\) | \(\ell\) | \(r\) |
|---|---|---|---|
| \(1\) | \(1\) | \(\ell\) | \(r\) |
| \(\ell\) | \(\ell\) | \(\ell\) | \(\ell\) |
| \(r\) | \(r\) | \(r\) | \(r\) |

This is the two-element left-zero semigroup with an identity adjoined.

### Proposition 3.2

\(M_{\mathrm{first}}\) is a monoid.

### Proof

The identity law is built into (17). If all three factors are nonidentity, then

\[
(ab)c=ac=a
\tag{19}
\]

and

\[
a(bc)=ab=a.
\tag{20}
\]

If one or more factors are \(1\), associativity reduces immediately to the identity law. Hence multiplication is associative. \(\square\)

---

## 4. Theorem A — finite compositional history invariant

Let

\[
\Sigma^*=\{L,R\}^*
\tag{21}
\]

be the free monoid of radial rule words.

### Theorem 4.1 — First-Role History Homomorphism

The map

\[
h:\Sigma^*\to M_{\mathrm{first}}
\tag{22}
\]

defined by

\[
h(\varepsilon)=1,
\tag{23}
\]

and, for nonempty words,

\[
h(w)=
\begin{cases}
\ell,&\text{if the first letter of }w\text{ is }L,\\
r,&\text{if the first letter of }w\text{ is }R
\end{cases}
\tag{24}
\]

is a monoid homomorphism.

Moreover,

\[
\boxed{h(LR)=\ell\ne r=h(RL).}
\tag{25}
\]

### Proof

Take words \(u,v\in\Sigma^*\).

If \(u=\varepsilon\), then

\[
h(uv)=h(v)=1\cdot h(v)=h(u)h(v).
\tag{26}
\]

If \(u\ne\varepsilon\), the first letter of \(uv\) is the first letter of \(u\). Hence

\[
h(uv)=h(u).
\tag{27}
\]

Since \(h(u)\in\{\ell,r\}\), equation (18) gives

\[
h(u)h(v)=h(u)
\tag{28}
\]

whether \(v\) is empty or nonempty. Thus

\[
h(uv)=h(u)h(v).
\]

Finally, \(LR\) begins with \(L\) and \(RL\) begins with \(R\), proving (25). \(\square\)

### Corollary 4.2 — Compositional congruence

Define

\[
u\sim_{\mathrm{first}}v
\iff
h(u)=h(v).
\tag{29}
\]

Then \(\sim_{\mathrm{first}}\) is a two-sided monoid congruence:

\[
u\sim v
\Longrightarrow
auw\sim avw
\tag{30}
\]

for all context words \(a,w\in\Sigma^*\).

Thus the memory is compatible with both prefixing and future continuation.

### Corollary 4.3 — Reflection covariance

Reflection changes \(x_k\leftrightarrow x_{-k}\) but does not exchange the left and right input slots. Therefore

\[
h(\nu\pi)=h(\pi)
\tag{31}
\]

for reflected radial histories.

---

## 5. Theorem B — three states are minimal

The previous theorem proves existence of finite memory. We now prove cardinality minimality.

### Lemma 5.1

Every monoid with at most two elements is commutative.

### Proof

A one-element monoid is trivial. Let a two-element monoid be

\[
N=\{1,a\}
\tag{32}
\]

with identity \(1\). The only undecided product is \(a^2\), which is either \(1\) or \(a\). All products involving \(1\) commute by the identity law, and \(a\) commutes with itself. Hence \(N\) is commutative. \(\square\)

### Theorem 5.2 — Minimality of the radial history monoid

Let \(N\) be a monoid and

\[
\phi:\{L,R\}^*\to N
\tag{33}
\]

a monoid homomorphism satisfying

\[
\phi(LR)\ne\phi(RL).
\tag{34}
\]

Then

\[
|N|\ge3.
\tag{35}
\]

The bound is sharp, realized by \(M_{\mathrm{first}}\).

### Proof

If \(|N|\le2\), Lemma 5.1 makes \(N\) commutative. Hence

\[
\phi(LR)
=\phi(L)\phi(R)
=\phi(R)\phi(L)
=\phi(RL),
\tag{36}
\]

contradicting (34). Therefore \(|N|\ge3\). Theorem 4.1 supplies a three-element example, so the bound is exact. \(\square\)

### Corollary 5.3 — H1

The native radial associator pair admits a finite compositional history quotient with exactly three monoid states, and no smaller monoid quotient can distinguish it.

Therefore

\[
\boxed{\texttt{H1 holds for the radial FCOA history problem}.}
\tag{37}
\]

In particular, `H0` and the strong form of `H2` are false for this subtheory.

---

## 6. Finite fiber realization over the line

A history-enriched radial endpoint may be represented as

\[
(x_k,m),
\qquad
m\in M_{\mathrm{first}}.
\tag{38}
\]

with forgetting projection

\[
\pi(x_k,m)=x_k.
\tag{39}
\]

The old extensional FCOA value is recovered exactly by \(\pi\). Each base point carries at most three history labels, so no second unbounded coordinate is introduced.

### Proposition 6.1 — Strict 1D closure of minimal history memory

The minimal radial history quotient is representable by a uniform finite fiber of cardinality three over the existing signed line.

Hence

\[
\boxed{\texttt{minimal radial history memory is 1D-CLOSED}.}
\tag{40}
\]

### Proof

The carrier coordinate remains \(k\in\mathbb Z\). The added component ranges over the fixed finite set \(M_{\mathrm{first}}\), independently of \(|k|\). Iterating the line coordinate does not create a new unbounded history coordinate because all nonempty words are collapsed to either \(\ell\) or \(r\). \(\square\)

---

## 7. Why this quotient is not arbitrary bookkeeping

A finite label set could always be invented by hand. The present quotient has three stronger properties.

First, its generators are intrinsic FCOA roles:

\[
L=\text{root-left interaction},
\qquad
R=\text{root-right interaction}.
\tag{41}
\]

Second, the history map is compositional:

\[
h(uv)=h(u)h(v).
\tag{42}
\]

Third, three states are minimal among all monoid-valued compositional invariants capable of separating the native diamond histories.

Thus the construction is a genuine minimal algebraic memory quotient of the radial rule-word system, not merely a tagged copy of the two paths.

### Qualification

Minimal cardinality does not prove unique canonicity. There are dual or differently presented three-state quotients, for example one remembering the last nonempty step rather than the first. The present first-role quotient is distinguished operationally by **persistence under future continuation**:

for every nonempty history \(u\) and every continuation \(v\),

\[
h(uv)=h(u).
\tag{43}
\]

Thus once the first radial role has been recorded, later legal continuation does not erase it.

---

## 8. Theorem C — scalar reversible phase cannot live on the minimal quotient

The next question is whether the finite history states \(\ell,r\) can themselves support a multiplicative complex phase.

### Theorem 8.1 — Unit-Character Collapse

Let

\[
\chi:M_{\mathrm{first}}\to\mathbb C^\times
\tag{44}
\]

be a monoid homomorphism into the nonzero complex numbers under multiplication. Then

\[
\boxed{\chi(\ell)=\chi(r)=1.}
\tag{45}
\]

Hence no multiplicative nonzero scalar character distinguishes \(\ell\) and \(r\).

### Proof

Because \(\ell^2=\ell\),

\[
\chi(\ell)^2=\chi(\ell).
\tag{46}
\]

Since \(\chi(\ell)\ne0\), divide by \(\chi(\ell)\) to obtain

\[
\chi(\ell)=1.
\tag{47}
\]

Likewise \(r^2=r\) implies

\[
\chi(r)=1.
\tag{48}
\]

Thus the two history states collapse under every nonzero scalar multiplicative character. \(\square\)

### Corollary 8.2

No assignment of pure multiplicative phases

\[
\ell\mapsto e^{i\theta_L},
\qquad
r\mapsto e^{i\theta_R}
\tag{49}
\]

can respect the monoid relations unless

\[
\theta_L\equiv\theta_R\equiv0\pmod{2\pi}.
\tag{50}
\]

Thus the minimal history quotient distinguishes paths combinatorially but cannot encode their distinction as a nontrivial scalar phase while preserving composition.

---

## 9. Theorem D — every unitary representation collapses the minimal history monoid

The scalar no-go extends to arbitrary Hilbert-space unitary representations.

### Theorem 9.1 — Unitary Representation Collapse

Let \(H\) be a complex Hilbert space and

\[
U:M_{\mathrm{first}}\to\mathcal U(H)
\tag{51}
\]

a monoid homomorphism into the group of unitary operators. Then

\[
\boxed{U(\ell)=U(r)=I_H.}
\tag{52}
\]

### Proof

The idempotence relation

\[
\ell^2=\ell
\tag{53}
\]

gives

\[
U(\ell)^2=U(\ell).
\tag{54}
\]

Since \(U(\ell)\) is unitary, it is invertible. Left-multiplying by \(U(\ell)^{-1}\) yields

\[
U(\ell)=I_H.
\tag{55}
\]

Exactly the same argument using \(r^2=r\) gives

\[
U(r)=I_H.
\tag{56}
\]

Therefore every unitary representation is trivial on the two nonidentity history states. \(\square\)

### Corollary 9.2 — Irreversibility of minimal history memory

The 3-state quotient is an irreversible memory device: once a first role is recorded, multiplication cannot invert that record. Its idempotent structure is incompatible with a faithful unitary realization.

Hence

\[
\boxed{
\texttt{QF3a finite history memory}
\not\Rightarrow
\texttt{QF3b reversible phase memory}.
}
\tag{57}
\]

This is a stronger obstruction than the terminal phase-erasure theorem: phase fails now not because histories are absent, but because the **minimal compositional quotient itself is non-group-like**.

---

## 10. Group-image obstruction

The previous theorem has a purely algebraic formulation.

### Proposition 10.1

Every homomorphism from \(M_{\mathrm{first}}\) to any group \(G\) is trivial on \(\ell\) and \(r\).

### Proof

A group has only one idempotent element, its identity. Since \(\ell\) and \(r\) are idempotent, their images must both be the identity. \(\square\)

### Consequence

Any reversible memory semantics that factors only through the minimal monoid necessarily forgets the distinction

\[
LR\ne RL.
\tag{58}
\]

Therefore a future phase-bearing history structure must retain more information than \(M_{\mathrm{first}}\), even though \(M_{\mathrm{first}}\) is sufficient for finite classical/combinatorial memory.

---

## 11. Revised QFIELD ladder

The structural ladder can now be sharpened again.

### QF2.5 — native evaluation diamonds

Present.

### QF3a-F — finite irreversible history memory

A finite compositional quotient distinguishes native paths.

**New theorem:** minimal size is three.

### QF3a-R — reversible history memory

A history quotient/groupoid with a nontrivial group/unitary image retains path distinction.

**Status:** not yet constructed.

### QF3b — coherent complex path algebra

Parallel path amplitudes add and sequential amplitudes compose.

**Status:** absent.

Thus

\[
\boxed{
QF2.5
<
QF3a\text{-}F
<
QF3a\text{-}R
<
QF3b
<
QF4
<
QF5.
}
\tag{59}
\]

The current native FCOA plus the minimal quotient reaches `QF3a-F`, but no farther.

---

## 12. H0/H1/H2 decision

For the radial subtheory the former trichotomy is now resolved.

### H0 — total history collapse

**False.** Theorem 4.1 separates \(LR\) and \(RL\).

### H1 — nontrivial finite/local history memory

**True.** Theorem 5.2 gives an exact minimal 3-state monoid.

### H2 — every distinction forces unbounded memory

**False in the strong form.** A bounded 3-state quotient already distinguishes the native pair.

Thus

\[
\boxed{\texttt{H1}.}
\tag{60}
\]

### Important refinement

Although unbounded memory is not required merely to distinguish the paths, the unitary-collapse theorem leaves open a new possibility:

\[
\boxed{
\text{perhaps nontrivial reversible/phase memory does require a larger or unbounded lift.}
}
\tag{61}
\]

That is now the correct next boundary.

---

## 13. Line-completion gate consequence

The finite history quotient is a fixed three-element fiber over the signed line. Therefore history distinction itself does not force a second spatial coordinate.

More strongly, even the **minimal compositional memory necessary to distinguish the native associator routes** is 1D-closed.

\[
\boxed{
\texttt{history distinction alone is not DIMENSION-FORCING}.}
\tag{62}
\]

If a future dimension-forcing theorem exists, it must use stronger requirements such as faithful reversible transport, unbounded independent iteration, or typed-output re-entry—not mere route distinction.

---

## 14. Hostile audit

### “Since the history quotient distinguishes LR and RL, it already carries a quantum phase.”

**Rejected.** Every multiplicative scalar character into \(\mathbb C^\times\) is trivial.

### “A higher-dimensional unitary representation may save the 3-state quotient.”

**Rejected.** Every unitary image of an idempotent is the identity, so every unitary representation collapses both \(\ell\) and \(r\).

### “Therefore history memory must be infinite.”

**Not proved.** Only the minimal 3-state quotient is ruled out as a reversible phase carrier. A richer finite non-idempotent quotient may exist.

### “The 3-state memory is arbitrary tagging.”

**Rejected as a minimality objection.** The quotient is a monoid homomorphism generated by intrinsic left/right root roles, is reflection invariant, and its cardinality is minimal among compositional monoid invariants distinguishing LR from RL.

### “The quotient creates a new dimension.”

**Rejected.** It is a bounded finite fiber over each line point.

---

## 15. Publication decision

`HOLD FOR APPLIED-DIRECTIONS SYNTHESIS` remains correct, but the mathematical content of SOL-QFIELD is now materially stronger.

The fourth strike contributes three theorem-level results that are genuinely FCOA-specific:

1. a cardinality-minimal compositional history quotient for the native radial diamond;
2. proof of `H1` and strict 1D closure of this memory;
3. a group/unitary representation no-go for the minimal quotient.

This is close to a publishable abstract note on history memory, but it should not yet be packaged as a QFT paper. The next reversible-memory barrier should be settled first.

---

## 16. Next strike — finite reversible separator problem

The new exact target is:

\[
\boxed{
\text{Does there exist a finite FCOA-internal history quotient }Q
\text{ that distinguishes }LR\text{ from }RL
\text{ and has a nontrivial group/unitary image?}
}
\tag{63}
\]

A quotient satisfying only

\[
[LR]\ne[RL]
\tag{64}
\]

is easy; the 3-state monoid already does that. The additional demand is that the distinction survive some reversible representation.

Three outcomes are now possible:

### R0 — finite reversible no-go

Every finite natural FCOA history quotient that distinguishes the diamond has only trivial group image on the distinguishing classes.

### R1 — finite reversible separator

A finite natural quotient exists whose group image still distinguishes the two routes. This would yield bounded phase-capable history memory and remain 1D-closed.

### R2 — unbounded reversible memory barrier

No finite quotient can retain the distinction reversibly, but an infinite group/groupoid lift can. This would identify the first genuinely unbounded history resource in SOL-QFIELD.

Resolving `R0/R1/R2` is now the sharp frontier.
