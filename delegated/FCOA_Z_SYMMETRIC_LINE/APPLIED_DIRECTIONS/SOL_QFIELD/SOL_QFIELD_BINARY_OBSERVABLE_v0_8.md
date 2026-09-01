# SOL-QFIELD — Native Binary Observable from the Route-Order Residue

**Version:** 0.8  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** EIGHTH TARGET COMPLETE / CANONICAL UNORDERED PURE-STATE PAIR PROVED / SINGLE PURE-STATE SELECTOR NO-GO  
**Depends on:** `SOL_QFIELD_ORDER_STATE_GNS_v0_7.md`

---

## 1. Executive verdict

Version 0.7 proved that the native route-order residue

\[
\Delta:=st-ts
\tag{1}
\]

canonically generates the entire order-sensitive ideal

\[
J_\Delta\cong M_2(\mathbb C),
\tag{2}
\]

and that history-conjugation symmetry selects the unique normalized tracial state on this sector.

The remaining question was whether the native FCOA data also select a pure state or a binary observable.

The answer is unexpectedly sharp.

Define

\[
\boxed{
Q:=\frac{i}{\sqrt3}\Delta.
}
\tag{3}
\]

Then, inside the order sector,

\[
\boxed{Q^*=Q,\qquad Q^2=e_{\rm std}.}
\tag{4}
\]

Therefore \(Q\) is a self-adjoint unitary on \(J_\Delta\), with spectrum

\[
\boxed{\sigma(Q)=\{+1,-1\}.}
\tag{5}
\]

Its spectral projectors are

\[
\boxed{
P_\pm=\frac12(e_{\rm std}\pm Q).
}
\tag{6}
\]

Each projector has rank one in the standard \(2D\) representation.

Thus the native route residue canonically determines a binary projective decomposition of the order-sensitive matrix sector.

However, the full history symmetry does **not** select one projector over the other. Even permutations of the three labels preserve each projector, while odd permutations exchange them.

Hence

\[
\boxed{
\text{no canonical single pure state, but a canonical unordered pair }\{P_+,P_-\}.
}
\tag{7}
\]

This provides the first intrinsic two-outcome observable skeleton in SOL-QFIELD, still conditional on the complex-linearization layer of v0.6.

---

## 2. Construction of the native observable

Let

\[
a:=st,
\qquad
b:=ts=a^{-1}.
\tag{8}
\]

Then

\[
\Delta=a-b.
\tag{9}
\]

From v0.7,

\[
\Delta^*=-\Delta
\tag{10}
\]

and

\[
\Delta^*\Delta=3e_{\rm std}.
\tag{11}
\]

Since \(\Delta^*=-\Delta\), equation (11) gives

\[
-\Delta^2=3e_{\rm std}.
\tag{12}
\]

Therefore

\[
Q^2
=
\frac{i^2}{3}\Delta^2
=
-\frac13\Delta^2
=
e_{\rm std}.
\tag{13}
\]

Also

\[
Q^*
=
\left(\frac{i}{\sqrt3}\Delta\right)^*
=
-\frac{i}{\sqrt3}\Delta^*
=
\frac{i}{\sqrt3}\Delta
=Q.
\tag{14}
\]

Hence Q is self-adjoint and unitary on the sector whose identity is \(e_{\rm std}\).

---

## 3. Theorem A — canonical rank-one spectral pair

### Theorem 3.1

The elements

\[
P_\pm:=\frac12(e_{\rm std}\pm Q)
\tag{15}
\]

are orthogonal self-adjoint projections satisfying

\[
P_++P_-=e_{\rm std},
\qquad
P_+P_-=0.
\tag{16}
\]

In the standard irreducible representation, each has rank one.

### Proof

Using \(Q^*=Q\) and \(Q^2=e_{\rm std}\),

\[
P_\pm^*=P_\pm
\tag{17}
\]

and

\[
P_\pm^2
=
\frac14(e_{\rm std}\pm2Q+Q^2)
=
\frac12(e_{\rm std}\pm Q)
=P_\pm.
\tag{18}
\]

Also

\[
P_+P_-
=
\frac14(e_{\rm std}-Q^2)
=0.
\tag{19}
\]

Their sum is \(e_{\rm std}\).

In \(M_2(\mathbb C)\), a nontrivial self-adjoint unitary with eigenvalues \(\pm1\) has one-dimensional eigenspaces because its trace is zero. Thus the spectral projections have rank one. \(\square\)

---

## 4. Symmetry action

The element \(a=st\) is a 3-cycle and \(b=a^{-1}\) is the opposite 3-cycle.

For every even permutation \(g\in A_3\), conjugation preserves \(a\) and \(b\) individually because \(A_3\) is cyclic and abelian. Therefore

\[
\operatorname{Ad}_g(\Delta)=\Delta,
\qquad g\in A_3.
\tag{20}
\]

For every odd permutation \(g\in S_3\setminus A_3\), conjugation exchanges the two 3-cycles:

\[
gag^{-1}=b,
\qquad
gbg^{-1}=a.
\tag{21}
\]

Hence

\[
\operatorname{Ad}_g(\Delta)=-\Delta.
\tag{22}
\]

Therefore

\[
\operatorname{Ad}_g(Q)
=
\begin{cases}
Q,&g\in A_3,\\
-Q,&g\notin A_3.
\end{cases}
\tag{23}
\]

and consequently

\[
\operatorname{Ad}_g(P_\pm)
=
\begin{cases}
P_\pm,&g\in A_3,\\
P_\mp,&g\notin A_3.
\end{cases}
\tag{24}
\]

---

## 5. Theorem B — no fully symmetric pure state

### Theorem 5.1

No rank-one state supported on \(J_\Delta\cong M_2(\mathbb C)\) is invariant under the full conjugation action of \(S_3\).

### Proof

Suppose a rank-one projector \(P\) were invariant under all history conjugations. Then its range would be a one-dimensional invariant subspace of the standard irreducible representation of \(S_3\). But the standard representation is irreducible and has dimension two. Contradiction. \(\square\)

Thus the unique fully symmetric state remains the mixed tracial state

\[
\tau_{\rm ord}=\frac12\operatorname{Tr}.
\tag{25}
\]

---

## 6. Theorem C — canonical unordered pure-state pair

### Theorem 6.1

The set

\[
\boxed{\{P_+,P_-\}}
\tag{26}
\]

is invariant under the full history symmetry \(S_3\), although neither member is individually invariant.

Hence the FCOA order residue canonically selects a binary decomposition **up to exchange of labels**.

### Interpretation

This is structurally stronger than selecting an arbitrary basis in \(M_2(\mathbb C)\). The decomposition is generated by the native FCOA order residue itself.

No convention is needed to determine the pair. A convention is needed only to name one eigenspace “+” and the other “−”.

Thus the theory naturally distinguishes

\[
\boxed{\text{binary observable structure}}
\]

without canonically distinguishing

\[
\boxed{\text{one preferred outcome}}.
\]

---

## 7. Relation to the canonical tracial state

Under

\[
\tau_{\rm ord}(X)=\frac12\operatorname{Tr}(X),
\tag{27}
\]

we have

\[
\tau_{\rm ord}(P_+)=\tau_{\rm ord}(P_-)=\frac12.
\tag{28}
\]

Thus the unique fully symmetric state assigns equal weight to the two native spectral alternatives.

Equivalently,

\[
\tau_{\rm ord}(Q)=0.
\tag{29}
\]

This equality is forced by the odd history symmetry which sends \(Q\mapsto-Q\).

### Important warning

Equation (28) is a state-theoretic probability assignment inside the conditional \(C^*\)-algebraic layer. It is not yet an experimentally justified Born rule for a physical FCOA system.

---

## 8. Minimal matrix realization

In a suitable basis of the standard representation one may write

\[
Q=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
\tag{30}
\]

This is unitarily equivalent to a Pauli matrix up to sign/basis convention.

Then

\[
P_\pm=\frac12
\begin{pmatrix}
1&\pm i\\
\mp i&1
\end{pmatrix}.
\tag{31}
\]

The resemblance to a two-level quantum observable is exact at the level of finite-dimensional operator algebra.

However, one must not reverse the logical direction:

\[
\boxed{
\text{Pauli-matrix form arises because every traceless self-adjoint unitary in }M_2(\mathbb C)
\text{ is unitarily equivalent to such a matrix.}
}
\tag{32}
\]

It does not prove that the original FCOA operation is a spin observable or a fermionic degree of freedom.

---

## 9. Updated selector verdict

The pure-state problem now has a three-level answer.

### Full symmetry, single pure state

\[
\boxed{\texttt{PURE-1: NO-GO}.}
\tag{33}
\]

No single rank-one state is invariant under all of \(S_3\).

### Even-history subgroup

\[
\boxed{\texttt{PURE-2: FINITE PAIR}.}
\tag{34}
\]

The subgroup \(A_3\) preserves each of \(P_+,P_-\), while odd history symmetry exchanges them.

### Unordered binary observable

\[
\boxed{\texttt{BINARY-OBS: CANONICAL}.}
\tag{35}
\]

The unordered spectral pair is fully invariant and derived from \(\Delta\) without choosing a basis.

---

## 10. QFIELD ladder update

The theorem chain is now

\[
\boxed{
\begin{aligned}
&\text{native associator diamond}\\
&\to S_3\text{ minimal reversible history memory}\\
&\to \mathbb C[S_3]\text{ conditional universal complex linearization}\\
&\to J_\Delta\cong M_2(\mathbb C)\text{ native order-sensitive sector}\\
&\to \tau_{\rm ord}=\tfrac12\operatorname{Tr}\text{ unique symmetric sector state}\\
&\to Q=i\Delta/\sqrt3\text{ native self-adjoint unitary}\\
&\to \{P_+,P_-\}\text{ canonical unordered rank-one pair}.
\end{aligned}
}
\tag{36}
\]

This is the strongest operator-theoretic structure obtained in SOL-QFIELD so far.

---

## 11. Hostile audit

### Claim: “FCOA has produced a preferred pure state.”

**Rejected.** Full symmetry forbids one.

### Claim: “The two pure states were chosen as a convenient basis.”

**Rejected.** They are the spectral projections of the internally generated residue \(Q=i\Delta/\sqrt3\).

### Claim: “The signs + and − are canonical physical labels.”

**Rejected.** Odd history symmetry exchanges them. Only the unordered pair is canonical.

### Claim: “This is already a qubit measurement.”

**Too strong.** It is a canonical binary projective decomposition in an \(M_2(\mathbb C)\) sector. Physical preparation, measurement postulates, dynamics, tensor products, and operational interpretation remain absent.

### Claim: “This proves the Pauli principle connection.”

**Rejected.** The operator is Pauli-like only because of the universal structure of \(M_2(\mathbb C)\), not because exchange antisymmetry or CAR has been derived.

---

## 12. Publication assessment

The prepublication nucleus is now materially stronger.

The chain from a native FCOA evaluation-order difference to a canonical non-Abelian sector, invariant state, and binary observable is mathematically coherent and nontrivial.

Nevertheless, the publication gate remains:

\[
\boxed{\texttt{PREPUBLICATION NUCLEUS — HOSTILE AUDIT NEXT}.}
\tag{37}
\]

The main unresolved dependency is still the conditional introduction of complex linear superposition in v0.6.

---

## 13. Next strike

The next sharp question is whether the binary observable \(Q\) is merely an isolated consequence of the smallest \(S_3\) history quotient, or the first member of a larger algebra generated by **multiple independent native associator diamonds**.

The target is:

\[
\boxed{
\text{Can two or more geometrically distinct native diamonds generate noncommuting }Q_i?
}
\tag{38}
\]

If all native diamonds yield the same \(Q\) up to sign, the operator layer is rigid but one-axis only.

If independent diamonds yield anticommuting or otherwise noncommuting observables, then a genuinely richer internal matrix geometry appears without importing it by hand.

That is the next strike.
