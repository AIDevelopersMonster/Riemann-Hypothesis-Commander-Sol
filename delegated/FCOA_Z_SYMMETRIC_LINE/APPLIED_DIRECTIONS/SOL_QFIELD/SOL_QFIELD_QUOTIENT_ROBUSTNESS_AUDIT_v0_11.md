# SOL-QFIELD — Quotient Robustness Audit: What Is Forced by Minimality and What Is Not

**Version:** 0.11  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** HOSTILE AUDIT COMPLETE / CANONICITY DEFECT FOUND / v0.9–v0.10 QUALIFIED  
**Supersedes the unconditional wording of:** `SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md`, `SOL_QFIELD_CAR_ONE_MODE_BARRIER_v0_10.md`

---

## 1. Executive correction

Versions 0.9 and 0.10 contain correct algebra **for the particular cardinality-minimal reversible realization**

\[
L\mapsto s,
\qquad
R\mapsto t,
\tag{1}
\]

where \(s,t\) are distinct transpositions in \(S_3\). In that Coxeter realization,

\[
s^2=t^2=e,
\qquad
(st)^3=e,
\tag{2}
\]

and the depth-two/depth-three root-comb residues produce an exact native Clifford pair and hence an exact one-mode CAR pair.

The hostile audit asks whether **cardinality minimality alone** forces that generator assignment.

It does not.

The minimal non-Abelian reversible history group is indeed

\[
\boxed{S_3,}
\tag{3}
\]

but a route-separating homomorphism \(h:\{L,R\}^*\to S_3\) need only satisfy

\[
h(L)h(R)\ne h(R)h(L).
\tag{4}
\]

There are noncommuting generating pairs in \(S_3\) of ordered type

\[
(2,2),\qquad(2,3),\qquad(3,2),
\tag{5}
\]

where the entries denote element orders.

The v0.9 construction used the \((2,2)\) orbit. The original FCOA history axioms do **not** presently exclude the mixed \((2,3)\) or \((3,2)\) orbits.

For a mixed-order realization the relevant native root-comb route differences remain nonzero and still live in the standard \(M_2(\mathbb C)\) sector, but the direct depth-two/depth-three differences need not anticommute.

Therefore the correct verdict is

\[
\boxed{
\texttt{EXACT NATIVE CLIFFORD/CAR: REALIZATION-DEPENDENT, NOT FORCED BY MINIMALITY ALONE.}
}
\tag{6}
\]

The publication status is consequently downgraded from “publication candidate” until this dependence is either accepted and stated as a conditional theorem or a genuinely intrinsic selector for the \((2,2)\) realization is found.

---

## 2. What v0.5 actually proved

The shortest native reconvergence gives two history words

\[
LR,
\qquad
RL.
\tag{7}
\]

A group-valued reversible separator must satisfy

\[
h(LR)\ne h(RL),
\tag{8}
\]

so if

\[
p:=h(L),
\qquad
q:=h(R),
\tag{9}
\]

then

\[
pq\ne qp.
\tag{10}
\]

Hence the target group must be non-Abelian. Since every group of order below six is Abelian and \(S_3\) is non-Abelian,

\[
|G|_{\min}=6.
\tag{11}
\]

This establishes cardinality minimality of \(S_3\).

It does **not** establish

\[
p^2=q^2=e.
\tag{12}
\]

Equation (12) came from one convenient choice of two transpositions.

---

## 3. Ordered generating-pair classes in \(S_3\)

Every noncommuting pair generates \(S_3\). Since the only nonidentity orders in \(S_3\) are two and three, a noncommuting ordered generating pair has one of the following types:

\[
(2,2),\quad(2,3),\quad(3,2).
\tag{13}
\]

Two order-three elements lie in the cyclic normal subgroup \(A_3\) and commute, so type \((3,3)\) is impossible for route separation.

Inner automorphisms preserve element orders. Therefore the mixed-order cases cannot be converted into the transposition/transposition case merely by changing labels inside \(S_3\).

This already proves that cardinality minimality does not select the Coxeter realization.

---

## 4. The Coxeter orbit: the v0.9 theorem remains correct conditionally

Take

\[
p=(12),
\qquad
q=(23).
\tag{14}
\]

Then

\[
p^2=q^2=e.
\tag{15}
\]

For the depth-two class

\[
\mathcal W_{2,1}=\{LR,RL\},
\tag{16}
\]

the residue is

\[
D_2=pq-qp.
\tag{17}
\]

For the depth-three class

\[
\mathcal W_{3,1}=\{LLR,LRL,RLL\},
\tag{18}
\]

we have

\[
h(LLR)=q,
\qquad
h(LRL)=pqp,
\qquad
h(RLL)=q,
\tag{19}
\]

and may take

\[
D_3=pqp-q.
\tag{20}
\]

The calculations of v0.9 then give, after normalization,

\[
Q_2^2=Q_3^2=e_{\rm std},
\qquad
\{Q_2,Q_3\}=0.
\tag{21}
\]

Thus the Clifford/CAR theorem is valid under the explicit additional assumption

\[
\boxed{p^2=q^2=e.}
\tag{22}
\]

---

## 5. Counterexample inside the same minimal group

Now keep the same cardinality-minimal history group \(S_3\) but choose

\[
p=(123),
\qquad
q=(12).
\tag{23}
\]

Then

\[
|p|=3,
\qquad
|q|=2,
\tag{24}
\]

and

\[
pq\ne qp.
\tag{25}
\]

So this is a fully valid minimal reversible separator for the original \(LR/RL\) requirement.

### Depth two

The images

\[
pq,
\qquad
qp
\tag{26}
\]

are two distinct transpositions. Define

\[
A:=pq-qp.
\tag{27}
\]

Since transpositions are self-inverse,

\[
A^*=A.
\tag{28}
\]

### Depth three

For the three reconvergent histories we obtain three distinct transpositions:

\[
h(LLR)=p^2q,
\qquad
h(LRL)=pqp,
\qquad
h(RLL)=qp^2.
\tag{29}
\]

Choose the direct route contrast

\[
B:=pqp-p^2q.
\tag{30}
\]

Again

\[
B^*=B.
\tag{31}
\]

A direct multiplication in \(\mathbb C[S_3]\) gives

\[
\boxed{
A^2=B^2=2e-p-p^2=3e_{\rm std}.
}
\tag{32}
\]

But, crucially,

\[
\boxed{
AB+BA=2e-p-p^2=3e_{\rm std}\ne0.
}
\tag{33}
\]

After normalization

\[
X:=\frac1{\sqrt3}A,
\qquad
Y:=\frac1{\sqrt3}B,
\tag{34}
\]

we have

\[
X^2=Y^2=e_{\rm std},
\tag{35}
\]

but

\[
\boxed{\{X,Y\}=e_{\rm std},}
\tag{36}
\]

not zero.

In Pauli-vector language the two axes have inner product \(1/2\), i.e. they meet at \(60^\circ\), rather than being orthogonal.

This is a counterexample to the unconditional `CLIFFORD` claim.

---

## 6. Consequence for v0.9

The statement

> “the natural finite root-comb closure contains a native anticommuting pair”

was too strong without specifying the history-generator realization.

The correct theorem is:

### Theorem 6.1 — Conditional Native Clifford Pair

If the cardinality-minimal reversible history realization is chosen so that both primitive history letters map to involutions,

\[
h(L)^2=h(R)^2=e,
\qquad
h(L)h(R)\ne h(R)h(L),
\tag{37}
\]

then the target is necessarily the transposition/transposition generating orbit of \(S_3\), and the v0.9 root-comb residues yield an exact Clifford pair.

Without the involutivity/equal-order condition, exact anticommutation is not forced.

---

## 7. Consequence for v0.10

The one-mode CAR construction

\[
c=\frac12(Q_x+iQ_y)
\tag{38}
\]

is algebraically correct whenever an exact Clifford pair has first been obtained.

Hence v0.10 becomes a conditional corollary:

\[
\boxed{
\text{Coxeter/involutive minimal history realization}
\Longrightarrow
\mathrm{Cl}_2(\mathbb C)
\Longrightarrow
\operatorname{CAR}_1.
}
\tag{39}
\]

The two-mode matrix-size no-go remains completely correct **once the history algebra is fixed to** \(\mathbb C[S_3]\):

\[
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)
\tag{40}
\]

cannot contain \(M_4(\mathbb C)\), so it cannot realize two independent CAR modes.

Thus the correction affects the **existence/canonicity of the first native CAR pair**, not the capacity bound of the fixed \(S_3\) algebra.

---

## 8. Can equal order repair the theorem?

Yes, but it is an additional axiom.

### Proposition 8.1

Let \(p,q\in S_3\) be noncommuting and suppose

\[
|p|=|q|.
\tag{41}
\]

Then

\[
|p|=|q|=2.
\tag{42}
\]

### Proof

The common order cannot be one. If it were three, both elements would lie in \(A_3\cong C_3\) and would commute. Therefore the common order is two. \(\square\)

Hence

\[
\boxed{
\text{minimality + noncommutation + equal generator order}
\Longrightarrow
\text{two transpositions}
\Longrightarrow
\text{v0.9 Clifford pair}.
}
\tag{43}
\]

However, current FCOA does not supply the equal-order premise.

---

## 9. Generator-exchange covariance is sufficient but not native

A stronger possible selector is an automorphism

\[
\alpha:S_3\to S_3
\tag{44}
\]

satisfying

\[
\alpha(p)=q,
\qquad
\alpha(q)=p.
\tag{45}
\]

Automorphisms preserve element order, so (45) implies

\[
|p|=|q|.
\tag{46}
\]

By Proposition 8.1, a noncommuting pair must then be two transpositions.

Thus history-letter exchange covariance would select the Coxeter orbit.

But this cannot presently be called an FCOA theorem because the primitive rules

\[
L:x_0\oplus x=x,
\qquad
R:x\oplus x_0=\rho(x)
\tag{47}
\]

are intentionally asymmetric. Carrier reflection does not exchange the two operand roles.

Therefore imposing \(L\leftrightarrow R\) covariance at the history level would be a new structural axiom, not a consequence of the old operation.

---

## 10. What survives without the Coxeter selector

The counterexample does **not** collapse the whole operator programme.

In the mixed \((3,2)\) realization, the normalized native residues \(X,Y\) satisfy

\[
X^2=Y^2=e_{\rm std},
\qquad
\{X,Y\}=e_{\rm std}.
\tag{48}
\]

They are distinct nonparallel self-adjoint binary observables in the same \(M_2(\mathbb C)\) block.

One may orthogonalize them algebraically, for example

\[
Y_\perp:=\frac{2Y-X}{\sqrt3},
\tag{49}
\]

which satisfies

\[
Y_\perp^2=e_{\rm std},
\qquad
\{X,Y_\perp\}=0.
\tag{50}
\]

Thus \(M_2(\mathbb C)\) still contains a Clifford pair.

But \(Y_\perp\) is a **linear combination** of native route residues, not itself the direct normalized difference used in v0.9. The Clifford structure is therefore available after linearization, not natively forced by the raw route contrasts.

This distinction is publication-critical.

---

## 11. Universal reversible history object

At the opposite extreme, if no finite quotient is imposed at all, the universal group generated by the two primitive history letters is the free group

\[
F_2=\langle L,R\rangle.
\tag{51}
\]

The original route condition

\[
LR\ne RL
\tag{52}
\]

holds in \(F_2\), but the finite Coxeter relations

\[
L^2=R^2=e,
\qquad
(LR)^3=e
\tag{53}
\]

do not.

Therefore the exact finite Clifford identities of v0.9 cannot be universal identities of reversible history semantics. They arise after a specific finite quotient choice.

This independently rules out the strongest `ROBUST-FACTOR` interpretation.

---

## 12. Correct robustness verdict

The previous trichotomy was:

- `ARTIFACT` — another admissible reversible realization preserves route distinctions but destroys native anticommutation;
- `MINIMAL-ONLY` — cardinality minimality itself forces Clifford/CAR;
- `ROBUST-FACTOR` — every admissible reversible separator carries the same structure.

The audit yields:

\[
\boxed{\texttt{ARTIFACT / REALIZATION-DEPENDENT}.}
\tag{54}
\]

More precisely:

\[
\boxed{
\begin{array}{ll}
\text{minimal group size }6 &: \text{robust},\\
S_3\text{ as minimal group} &: \text{robust},\\
M_2\text{ standard block after }\mathbb C\text{-linearization} &: \text{robust for the chosen }S_3\text{ algebra},\\
\text{direct native Clifford pair} &: \text{not robust},\\
\text{direct native CAR}_1 &: \text{not robust},\\
\text{CAR}_2\text{ size obstruction in }\mathbb C[S_3] &: \text{robust once }S_3\text{ is fixed}.
\end{array}
}
\tag{55}
\]

---

## 13. Publication correction

The v0.9 and v0.10 results must not be published with unconditional wording.

They may be retained as a conditional branch:

\[
\boxed{
\texttt{INVOLUTIVE MINIMAL HISTORY REALIZATION}
\Rightarrow
\texttt{NATIVE CLIFFORD}
\Rightarrow
\texttt{ALGEBRAIC CAR}_1.
}
\tag{56}
\]

The unconditional core remains the stronger-safe chain

\[
\boxed{
\text{native reconvergence}
\to
\text{minimal reversible size }6
\to
S_3\text{ available}
\to
\mathbb C[S_3]
\to
\text{non-Abelian }M_2\text{ sector},
}
\tag{57}
\]

but the step from that sector to a **directly native orthogonal Clifford frame** requires an extra selector.

Publication status is therefore reset to

\[
\boxed{\texttt{PREPUBLICATION — CANONICITY GAP OPEN}.}
\tag{58}
\]

---

## 14. Next strike

The next question is now narrower and more fundamental:

> Can the FCOA root-comb itself select a generator metric / angle on the two-dimensional order sector without imposing artificial \(L\leftrightarrow R\) symmetry?

Equivalent formulations:

1. Is there a history-invariant positive form on route residues that canonically orthogonalizes distinct reconvergence contrasts?
2. Can the tracial state \(\tau_{\rm ord}\) plus a canonical choice of **which** two native contrasts select a unique Gram matrix and hence a canonical orthogonal frame?
3. Does the entire family of root-comb residues, rather than a chosen pair, have a symmetry-determined tight-frame operator whose normalization removes generator-choice dependence?

If yes, Clifford structure may re-emerge **after a canonical frame construction**, rather than from a privileged generator quotient.

If no, the correct endpoint of SOL-QFIELD is a robust non-Abelian \(M_2\) order sector with realization-dependent internal axes.

That is the next hostile strike.

---

## 15. References

1. `SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`.
2. `SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md`.
3. `SOL_QFIELD_CAR_ONE_MODE_BARRIER_v0_10.md`.
4. Standard finite group and representation theory of \(S_3\).
5. FCOA-Z v1.1, DOI: https://doi.org/10.5281/zenodo.22169264
