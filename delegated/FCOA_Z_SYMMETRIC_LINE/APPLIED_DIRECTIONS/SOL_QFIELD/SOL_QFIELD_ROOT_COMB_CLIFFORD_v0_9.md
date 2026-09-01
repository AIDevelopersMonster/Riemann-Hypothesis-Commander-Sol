# SOL-QFIELD — Root-Comb Closure, Multi-Axis Breakthrough, and a Native Clifford Pair

**Version:** 0.9  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** NINTH TARGET COMPLETE / ONE-AXIS RADIAL-DIAMOND GUESS REFUTED / NATIVE ANTICOMMUTING PAIR PROVED  
**Depends on:** `SOL_QFIELD_BINARY_OBSERVABLE_v0_8.md`

---

## 1. Executive verdict

Version 0.8 extracted one canonical binary observable from the shortest native radial diamond,

\[
LR\quad\text{versus}\quad RL.
\tag{1}
\]

A natural hostile question was whether every further radial diamond produces only the same operator up to sign. If so, the history sector would be intrinsically one-axis.

That conjecture is false once the legacy operation is closed under its own finite iterated root interactions.

The decisive observation is elementary but strong. Define the two partial root actions on non-root base points by

\[
\mathsf L(x):=x_0\oplus x=x,
\qquad
\mathsf R(x):=x\oplus x_0=\rho(x).
\tag{2}
\]

For every finite word \(w\in\{L,R\}^*\), whenever the successive evaluations remain away from \(x_0\), its base endpoint depends only on the number of letters \(R\):

\[
\boxed{
\mathsf F_w(x_k)=\rho^{\#_R(w)}(x_k).
}
\tag{3}
\]

Hence every two words with the same number of \(R\)-steps are natively reconvergent.

The familiar \(LR/RL\) diamond is merely the first member of a much larger root-comb family.

Under the minimal reversible history map

\[
L\mapsto s,
\qquad
R\mapsto t,
\qquad
s^2=t^2=e,
\qquad
(st)^3=e,
\tag{4}
\]

there is already a second independent route residue at history length three:

\[
LLR\mapsto t,
\qquad
LRL\mapsto u:=sts,
\qquad
RLL\mapsto t.
\tag{5}
\]

Thus

\[
D:=u-t
\tag{6}
\]

is a second native route contrast.

Let

\[
\Delta:=st-ts,
\qquad
Q_y:=\frac{i}{\sqrt3}\Delta,
\qquad
Q_x:=\frac1{\sqrt3}D.
\tag{7}
\]

Inside the native order ideal

\[
J_\Delta\cong M_2(\mathbb C),
\tag{8}
\]

one has the exact relations

\[
\boxed{
Q_x^*=Q_x,
\quad
Q_y^*=Q_y,
\quad
Q_x^2=Q_y^2=e_{\rm std},
\quad
Q_xQ_y+Q_yQ_x=0.
}
\tag{9}
\]

Therefore the FCOA root-comb closure contains a **native anticommuting Clifford pair**.

Consequently

\[
\boxed{
C^*(Q_x,Q_y)=J_\Delta\cong M_2(\mathbb C).
}
\tag{10}
\]

The previous `ONE-AXIS` possibility is refuted for the unrestricted finite root-comb closure:

\[
\boxed{\texttt{MULTI-AXIS: YES}.}
\tag{11}
\]

This remains conditional on the complex-linearization layer of v0.6 and does not by itself turn FCOA into quantum mechanics.

---

## 2. Root-comb histories

For \(k\ne0\), define

\[
\mathsf L(x_k)=x_k,
\qquad
\mathsf R(x_k)=\rho(x_k).
\tag{12}
\]

For a word

\[
w=w_1w_2\cdots w_m\in\{L,R\}^m,
\tag{13}
\]

let \(\mathsf F_w\) denote the sequential evaluation obtained by applying the corresponding root action at each step.

Write

\[
r(w):=\#\{j:w_j=R\}.
\tag{14}
\]

We impose the safe-domain condition

\[
r(w)<|k|,
\tag{15}
\]

which guarantees that no intermediate evaluation reaches the root, where an additional root interaction could be undefined.

### Theorem 2.1 — Radial path-permutation theorem

For every \(x_k\) and every finite history word satisfying (15),

\[
\boxed{
\mathsf F_w(x_k)=\rho^{r(w)}(x_k).
}
\tag{16}
\]

### Proof

Induct on the word length.

For the empty word the claim is immediate. Suppose it holds for \(w\). If the next letter is \(L\), then the current non-root point \(y\) satisfies

\[
\mathsf L(y)=x_0\oplus y=y,
\tag{17}
\]

so the radial depth is unchanged. If the next letter is \(R\), then

\[
\mathsf R(y)=y\oplus x_0=\rho(y),
\tag{18}
\]

so the radial depth increases by exactly one. Thus only the number of \(R\)-letters matters. \(\square\)

### Corollary 2.2 — Binomial reconvergence classes

Fix \(m\) and \(0\le r<m\) with \(r<|k|\). All

\[
\binom mr
\tag{19}
\]

words in

\[
\mathcal W_{m,r}:=\{w\in\{L,R\}^m:r(w)=r\}
\tag{20}
\]

have the same endpoint

\[
\rho^r(x_k).
\tag{21}
\]

Thus the shortest \(LR/RL\) diamond is only

\[
\mathcal W_{2,1}=\{LR,RL\}.
\tag{22}
\]

---

## 3. Same source word, different evaluation history

A word \(w\in\mathcal W_{m,r}\) can also be read as an insertion history for a fixed ordered source word.

Every \(L\)-event inserts a root on the left of the current expression, and every \(R\)-event inserts a root on the right. Therefore all histories with

\[
\ell=m-r
\tag{23}
\]

left insertions and \(r\) right insertions have the same ordered leaf word

\[
\underbrace{x_0,\ldots,x_0}_{\ell},\ x_k,\ 
\underbrace{x_0,\ldots,x_0}_{r},
\tag{24}
\]

but generally different nesting/evaluation histories.

Thus the root-comb family is not merely a collection of unrelated state transitions. It is a controlled family of alternative evaluation histories of the same ordered source data for fixed \((m,r)\).

---

## 4. Minimal reversible history image

Retain the minimal reversible history quotient from v0.5:

\[
G_{\rm hist}=S_3,
\tag{25}
\]

with

\[
s=h(L),
\qquad
t=h(R),
\tag{26}
\]

chosen as distinct transpositions.

Put

\[
a:=st,
\qquad
b:=ts=a^{-1},
\qquad
u:=sts=tst.
\tag{27}
\]

To avoid collision with the FCOA carrier reflection symbol, the third transposition is denoted \(\nu\) only inside this group-theoretic subsection; below we write it as \(u\).

For clarity set

\[
u:=sts=tst.
\tag{28}
\]

The six group elements are

\[
\{e,s,t,u,a,b\}.
\tag{29}
\]

---

## 5. Length two: the first axis

For

\[
\mathcal W_{2,1}=\{LR,RL\},
\tag{30}
\]

we have

\[
h(LR)=st=a,
\qquad
h(RL)=ts=b.
\tag{31}
\]

The route residue is

\[
\Delta=a-b.
\tag{32}
\]

Version 0.8 normalized it to

\[
\boxed{
Q_y:=\frac{i}{\sqrt3}(a-b),
}
\tag{33}
\]

with

\[
Q_y^*=Q_y,
\qquad
Q_y^2=e_{\rm std}.
\tag{34}
\]

---

## 6. Length three: a genuinely new axis

Now consider

\[
\mathcal W_{3,1}=\{LLR,LRL,RLL\}.
\tag{35}
\]

All three histories have endpoint

\[
\rho(x_k).
\tag{36}
\]

But their history-group images are

\[
\begin{aligned}
h(LLR)&=s^2t=t,\\
h(LRL)&=sts=u,\\
h(RLL)&=ts^2=t.
\end{aligned}
\tag{37}
\]

Thus the middle route is separated from the two outer routes by

\[
D:=u-t.
\tag{38}
\]

Both \(u\) and \(t\) are transpositions, hence self-inverse, so

\[
D^*=D.
\tag{39}
\]

### Theorem 6.1 — Second native binary observable

Define

\[
\boxed{
Q_x:=\frac1{\sqrt3}(u-t).
}
\tag{40}
\]

Then

\[
\boxed{
Q_x^*=Q_x,
\qquad
Q_x^2=e_{\rm std}.
}
\tag{41}
\]

### Proof

Since \(u^2=t^2=e\), while

\[
ut=b,
\qquad
tu=a,
\tag{42}
\]

we obtain

\[
\begin{aligned}
(u-t)^2
&=u^2+t^2-ut-tu\\
&=2e-a-b\\
&=3e_{\rm std}.
\end{aligned}
\tag{43}
\]

Equation (41) follows. \(\square\)

Thus length three does not merely reproduce the v0.8 axis.

---

## 7. Theorem A — exact anticommutation

### Theorem 7.1 — Native Clifford Pair

The two independently generated native observables satisfy

\[
\boxed{
Q_xQ_y+Q_yQ_x=0.
}
\tag{44}
\]

### Proof

It suffices to prove

\[
(a-b)(u-t)+(u-t)(a-b)=0.
\tag{45}
\]

The required products in \(S_3\) are

\[
au=t,
\quad
at=s,
\quad
bu=s,
\quad
bt=u,
\tag{46}
\]

and

\[
ua=s,
\quad
ub=t,
\quad
ta=u,
\quad
tb=s.
\tag{47}
\]

Therefore

\[
(a-b)(u-t)=t+u-2s,
\tag{48}
\]

while

\[
(u-t)(a-b)=2s-t-u.
\tag{49}
\]

Their sum vanishes. Multiplication by the normalization factors in (33) and (40) proves (44). \(\square\)

Hence

\[
\boxed{
Q_x^2=Q_y^2=e_{\rm std},
\qquad
\{Q_x,Q_y\}=0.
}
\tag{50}
\]

These are precisely the defining relations of two complex Clifford generators on the order sector.

---

## 8. Theorem B — the native pair generates the entire matrix block

Let

\[
\mathrm{Cl}_2(\mathbb C)
\tag{51}
\]

denote the complex Clifford algebra on two generators satisfying

\[
e_1^2=e_2^2=1,
\qquad
e_1e_2+e_2e_1=0.
\tag{52}
\]

It is a four-dimensional simple algebra isomorphic to

\[
M_2(\mathbb C).
\tag{53}
\]

### Theorem 8.1

The assignment

\[
e_1\mapsto Q_x,
\qquad
e_2\mapsto Q_y
\tag{54}
\]

identifies the generated algebra with the full native order ideal:

\[
\boxed{
C^*(Q_x,Q_y)=J_\Delta\cong M_2(\mathbb C).
}
\tag{55}
\]

### Proof

Relations (50) define a unital homomorphism

\[
\Phi:\mathrm{Cl}_2(\mathbb C)\to J_\Delta.
\tag{56}
\]

The map is nonzero because \(Q_x^2=e_{\rm std}\ne0\). Since

\[
\mathrm{Cl}_2(\mathbb C)\cong M_2(\mathbb C)
\tag{57}
\]

is simple, \(\ker\Phi=0\). Both source and target have complex dimension four, hence \(\Phi\) is onto. \(\square\)

This strengthens v0.7: the matrix block is not only the ideal generated by one route residue. It is generated by **two separate native reconvergence contrasts satisfying exact Clifford relations**.

---

## 9. The third Pauli/Clifford direction is generated algebraically

Define

\[
\boxed{
Q_z:=-iQ_xQ_y.
}
\tag{58}
\]

Then

\[
Q_z^*=Q_z,
\qquad
Q_z^2=e_{\rm std},
\tag{59}
\]

and

\[
\boxed{
Q_xQ_y=iQ_z,
\quad
Q_yQ_z=iQ_x,
\quad
Q_zQ_x=iQ_y.
}
\tag{60}
\]

In group-algebra coordinates,

\[
\boxed{
Q_z=\frac13(2s-t-u).
}
\tag{61}
\]

Consequently

\[
\boxed{
Q_iQ_j+Q_jQ_i=2\delta_{ij}e_{\rm std}
}
\tag{62}
\]

for \(i,j\in\{x,y,z\}\).

Thus the standard block carries an exact Pauli/Clifford algebraic triple.

### Important qualification

Only \(Q_x\) and \(Q_y\) above were obtained directly as normalized **two-route differences** from native reconvergent histories. The third operator \(Q_z\) is generated multiplicatively from that pair. It must not be misreported as another primitive two-route residue.

---

## 10. Explicit standard-representation witness

Choose a real standard representation in which

\[
s=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad

t=
\begin{pmatrix}
-1/2&\sqrt3/2\\
\sqrt3/2&1/2
\end{pmatrix}.
\tag{63}
\]

Then

\[
u=sts=
\begin{pmatrix}
-1/2&-\sqrt3/2\\
-\sqrt3/2&1/2
\end{pmatrix}.
\tag{64}
\]

The native observables become

\[
Q_x=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix},
\tag{65}
\]

\[
Q_y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix},
\tag{66}
\]

and

\[
Q_z=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\tag{67}
\]

These are Pauli matrices up to harmless sign conventions.

The statement is an exact finite-dimensional algebra identity, not an identification of the FCOA carrier with physical spin.

---

## 11. Canonical tracial geometry

For the order-sector state

\[
\tau_{\rm ord}(X)=\frac12\operatorname{Tr}(X),
\tag{68}
\]

we obtain

\[
\boxed{
\tau_{\rm ord}(Q_i)=0,
\qquad
\tau_{\rm ord}(Q_iQ_j)=\delta_{ij}.
}
\tag{69}
\]

Thus the three generated Clifford directions form an orthonormal basis of the traceless self-adjoint part of \(M_2(\mathbb C)\) with respect to the tracial inner product.

The continuous sphere

\[
Q(\mathbf n)=n_xQ_x+n_yQ_y+n_zQ_z,
\qquad
\|\mathbf n\|=1,
\tag{70}
\]

then satisfies

\[
Q(\mathbf n)^*=Q(\mathbf n),
\qquad
Q(\mathbf n)^2=e_{\rm std}.
\tag{71}
\]

This sphere is supplied by the complex-linear matrix algebra after the discrete native generators have been found. It is not itself a new spatial dimension of FCOA.

---

## 12. Minimality of the multi-axis breakthrough

### Proposition 12.1

The two-step class \(\mathcal W_{2,1}\) supplies only one nonzero route-difference line in \(\mathbb C[S_3]\).

The first new route-difference line occurs at length three in \(\mathcal W_{3,1}\) (and symmetrically in \(\mathcal W_{3,2}\)).

Hence the minimal history depth at which the native root-comb closure can exhibit two independent binary-observable directions is

\[
\boxed{m=3.}
\tag{72}
\]

No larger carrier radius is conceptually required; one only needs \(|k|>1\) for the \(r=1\) classes to stay in the safe non-root domain.

---

## 13. Hostile audit — is the second axis only identity padding?

The new length-three class contains an extra \(L\)-event, and \(\mathsf L\) is extensionally the identity on every non-root base point. This raises a serious objection:

> Should insertion/deletion of an \(L\)-event be treated as a gauge-stutter and therefore ignored by history memory?

The answer exposes a sharp dichotomy.

### Theorem 13.1 — Stutter-collapse dichotomy

Let \(h:\{L,R\}^*\to G\) be a monoid homomorphism into any group. If history semantics are invariant under arbitrary insertion/deletion of \(L\), i.e.

\[
h(vLw)=h(vw)
\tag{73}
\]

for all words \(v,w\), then

\[
h(L)=e_G.
\tag{74}
\]

Consequently

\[
h(LR)=h(R)=h(RL),
\tag{75}
\]

so the original v0.5 order distinction disappears.

### Proof

Set \(v=w=\varepsilon\) in (73). Then \(h(L)=h(\varepsilon)=e_G\). Equation (75) follows immediately. \(\square\)

### Consequence

One cannot simultaneously maintain both of the following:

1. the v0.5 premise that \(LR\ne RL\) must remain distinguishable in reversible history memory;
2. arbitrary deletion of the extensionally neutral \(L\)-event as a history gauge.

Thus within the already adopted **history-sensitive** semantics, the length-three route is legitimate. Rejecting it requires a new explicit depth/minimality axiom, not something already contained in FCOA.

---

## 14. What is and is not forced

### Forced inside finite root-comb history closure

Given:

1. the legacy root laws (2);
2. retention of finite evaluation histories;
3. the minimal reversible history quotient \(S_3\);
4. the conditional complex-linearization hypothesis of v0.6;

then the root-comb closure contains the exact anticommuting pair (9).

### Not forced by the original carrier operation alone

The following are still additional semantic layers:

- retaining history rather than quotienting entirely by endpoints;
- selecting the minimal reversible quotient \(S_3\);
- choosing \(\mathbb C\) as coefficient field;
- interpreting self-adjoint elements as physical observables;
- interpreting projectors or traces as experimental outcomes/probabilities.

Thus the physical verdict remains conservative.

---

## 15. Dimensional gate

Although arbitrarily long root histories exist, their minimal reversible quotient remains the finite group \(S_3\), and the complex order sector remains the finite internal fiber

\[
M_2(\mathbb C).
\tag{76}
\]

Nothing in the present theorem forces a second spatial carrier coordinate.

Therefore

\[
\boxed{\texttt{LINE STATUS: 1D-CLOSED}.}
\tag{77}
\]

---

## 16. Updated verdict

The one-axis hypothesis is false for the natural finite-history closure:

\[
\boxed{
\texttt{ONE-AXIS-RADIAL: FALSE AFTER ROOT-COMB CLOSURE}.
}
\tag{78}
\]

The positive theorem is

\[
\boxed{
\texttt{MULTI-AXIS: TWO NATIVE ANTICOMMUTING GENERATORS AT DEPTH }3.
}
\tag{79}
\]

and the generated algebra is exactly

\[
\boxed{
\mathrm{Cl}_2(\mathbb C)
\cong
M_2(\mathbb C)
\cong
J_\Delta.
}
\tag{80}
\]

---

## 17. Next strike

Two self-adjoint Clifford generators immediately suggest the algebraic combinations

\[
c:=\frac12(Q_x+iQ_y),
\qquad
c^*:=\frac12(Q_x-iQ_y).
\tag{81}
\]

The next question is whether the native relations force

\[
c^2=0,
\qquad
(c^*)^2=0,
\qquad
cc^*+c^*c=e_{\rm std},
\tag{82}
\]

and, if so, exactly what can legitimately be claimed:

- merely an algebraic copy of the one-mode CAR algebra;
- a canonical occupation-projector pair;
- or something stronger.

A second hostile question is then unavoidable: can the current \(M_2(\mathbb C)\) sector ever support **two independent fermionic modes**, or is there a strict matrix-size barrier?

That is the next SOL-QFIELD strike.

---

## 18. References

1. `SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`.
2. `SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`.
3. `SOL_QFIELD_LINEARIZATION_v0_6.md`.
4. `SOL_QFIELD_ORDER_STATE_GNS_v0_7.md`.
5. `SOL_QFIELD_BINARY_OBSERVABLE_v0_8.md`.
6. Standard representation theory of \(S_3\) and the identity \(\mathrm{Cl}_2(\mathbb C)\cong M_2(\mathbb C)\).
7. FCOA-Z v1.1, DOI: https://doi.org/10.5281/zenodo.22169264
