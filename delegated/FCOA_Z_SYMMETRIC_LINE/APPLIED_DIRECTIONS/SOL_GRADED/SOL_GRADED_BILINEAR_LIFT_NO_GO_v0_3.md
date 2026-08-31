# SOL-GRADED — Bilinear-Lift and Faithful Superbracket No-Go

**Version:** 0.3  
**Date:** 2026-08-30  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** THIRD TARGET COMPLETE / STRONG SUPERBRACKET ROUTE CLOSED NEGATIVELY  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_GRADED_REPORT_v0_1.md`, `SOL_GRADED_EXCHANGE_SELECTION_v0_2.md`, `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`, `HOSTILE_AUDIT_SIGNED_M0_TRANSFER_0_1.md`, `LINE_COMPLETION_GATE.md`

---

## 1. Executive verdict

The third SOL-GRADED target was deliberately stronger than the existence of a reflection grading or a mirror exchange law:

\[
\boxed{
\text{Can a conservative one-dimensional LC3 completion of the original partial }\oplus
\text{ induce a nonzero total bilinear law }
V_{\bar1}\times V_{\bar1}\to V_{\bar0}
\text{ without defining a new bracket by hand?}
}
\tag{1}
\]

Under the accepted FCOA-Z conservative rules, the answer is **no**.

Three independent obstructions are proved.

1. **Totality obstruction.** Even if every mixed-sign cell is opened, legacy exactness forces all distinct same-sign positive cells to remain `UNDEF`. Hence for `n != m` the odd tensor `a_n tensor a_m` is outside the canonical bilinearization domain. The odd-odd domain contains at most diagonal tensors `a_n tensor a_n`.

2. **Typed-output closure obstruction.** On a diagonal odd tensor, the two inherited same-sign terms produce the old terminal outputs `E_n^+` and its reflected image. A conservative mixed rule cannot turn their free typed linearization into a nonzero base-even vector without either projecting/identifying terminal outputs or adding new algebraic structure.

3. **Super-skew obstruction.** On the already-defined root/odd sector, the old FCOA role asymmetry gives
   \[
   \widetilde\oplus(e_0,a_n)=a_n,
   \qquad
   \widetilde\oplus(a_n,e_0)=a_{n-1}
   \tag{2}
   \]
   with `a_0=0`. A Lie-super bracket would require the second value to equal `-a_n`. This fails for every `n`.

Therefore:

\[
\boxed{
\text{the original FCOA }\oplus\text{ cannot be faithfully promoted to a Lie-super bracket}
\text{ on its reflection-linearized carrier by any LC3 mixed completion.}
}
\tag{3}
\]

The line-first verdict for this route is

\[
\boxed{\texttt{1D-OBSTRUCTED}.}
\tag{4}
\]

The applied verdict remains

\[
\boxed{\texttt{FORMAL EMBEDDING}}
\tag{5}
\]

for the reflection/operator shadow only. Direct identification of the FCOA operation with a Lie-super bracket is now

\[
\boxed{\texttt{REJECT}.}
\tag{6}
\]

This does **not** reject the earlier mirror-exchange theorem or the canonical operator superalgebra shadow. It closes only the stronger emergence claim that the old partial `oplus` itself becomes a Lie-super bracket after one-dimensional signed completion.

---

## 2. Fixed carrier and reflection grading

Let

\[
B^{\pm}=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\tag{7}
\]

with reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{8}
\]

Let `K` be a field with

\[
\operatorname{char}K\ne2.
\tag{9}
\]

Free-linearize the base carrier:

\[
V=K^{(B^{\pm})}.
\tag{10}
\]

Write

\[
e_0=e_{P_0},
\qquad
e_n^+=e_{P_n^+},
\qquad
e_n^-=e_{P_n^-}.
\tag{11}
\]

The linear reflection is

\[
Je_0=e_0,
\qquad
Je_n^+=e_n^-,
\qquad
Je_n^-=e_n^+.
\tag{12}
\]

Thus

\[
V=V_{\bar0}\oplus V_{\bar1},
\tag{13}
\]

where

\[
V_{\bar0}=\ker(J-I),
\qquad
V_{\bar1}=\ker(J+I).
\tag{14}
\]

Use the standard mirror modes

\[
s_n=e_n^++e_n^-,
\qquad
a_n=e_n^+-e_n^-.
\tag{15}
\]

Then

\[
Js_n=s_n,
\qquad
Ja_n=-a_n,
\tag{16}
\]

and

\[
V_{\bar1}=\operatorname{span}_K\{a_n:n\ge1\}.
\tag{17}
\]

---

## 3. Typed free output space

The FCOA operation is typed: some defined cells return base points, while others return terminal output symbols. These must not be silently identified.

Let `O` be the disjoint union of the base carrier with every active terminal output sort of the chosen conservative extension. Define the free output vector space

\[
W=K^{(O)}.
\tag{18}
\]

Since the base and terminal sorts are disjoint,

\[
W=V\oplus F,
\tag{19}
\]

where `F` is the free span of non-base output elements.

Extend the output reflection to an involution

\[
J_*:W\to W.
\tag{20}
\]

It acts as `J` on `V` and by the chosen output involutions on terminal fibers.

The direct sum (19) is not cosmetic. It is the linear expression of the FCOA rule that a terminal output is not a base point and `UNDEF` is not a null value.

---

## 4. Canonical partial bilinearization

Let `omega` be a reflection-compatible conservative extension of `oplus`, with domain

\[
D_\omega\subseteq B^{\pm}\times B^{\pm}.
\tag{21}
\]

Define the tensor-domain subspace

\[
\mathscr D_\omega
=
\operatorname{span}_K
\{e_x\otimes e_y:(x,y)\in D_\omega\}
\subseteq V\otimes V.
\tag{22}
\]

### Definition 4.1 — canonical partial bilinearization

The canonical partial bilinearization of `omega` is the unique linear map

\[
\widetilde\omega:\mathscr D_\omega\to W
\tag{23}
\]

such that on every defined basis cell

\[
\widetilde\omega(e_x\otimes e_y)=e_{\omega(x,y)},
\tag{24}
\]

where the right-hand basis vector belongs to the appropriate base or terminal output sort.

### Why this is the honest minimal linearization

Equation (23) assigns values only to basis tensors corresponding to actually defined FCOA cells. It does **not**:

- replace `UNDEF` by zero;
- project terminal outputs onto the base carrier;
- identify distinct output sorts;
- fill missing cells by bilinearity;
- introduce a separate bracket.

Any totalization beyond (23) therefore constitutes additional structure and must be declared explicitly.

---

## 5. Partial Grade-Covariance Theorem

The first new result is positive.

### Theorem 5.1

Suppose the domain is invariant under simultaneous reflection and

\[
\omega(\nu x,\nu y)=\nu_*\omega(x,y)
\tag{25}
\]

on every defined basis cell. Then

\[
(J\otimes J)\mathscr D_\omega=\mathscr D_\omega
\tag{26}
\]

and

\[
\boxed{
J_*\widetilde\omega
=
\widetilde\omega(J\otimes J)
\quad\text{on }\mathscr D_\omega.
}
\tag{27}
\]

Consequently, if

\[
u\in V_{\bar p},
\qquad
v\in V_{\bar q},
\qquad
u\otimes v\in\mathscr D_\omega,
\tag{28}
\]

then

\[
\boxed{
\widetilde\omega(u\otimes v)
\in W_{\overline{p+q}}.
}
\tag{29}
\]

### Proof

For every defined basis tensor, reflection invariance of the domain gives

\[
e_x\otimes e_y\in\mathscr D_\omega
\Longrightarrow
Je_x\otimes Je_y=e_{\nu x}\otimes e_{\nu y}\in\mathscr D_\omega.
\]

Hence (26). On basis tensors, equivariance gives

\[
\begin{aligned}
J_*\widetilde\omega(e_x\otimes e_y)
&=J_*e_{\omega(x,y)}\\
&=e_{\nu_*\omega(x,y)}\\
&=e_{\omega(\nu x,\nu y)}\\
&=\widetilde\omega(Je_x\otimes Je_y).
\end{aligned}
\]

Linearity proves (27). If `Ju=(-1)^p u` and `Jv=(-1)^q v`, then

\[
(J\otimes J)(u\otimes v)=(-1)^{p+q}(u\otimes v).
\]

Applying (27),

\[
J_*\widetilde\omega(u\otimes v)
=(-1)^{p+q}\widetilde\omega(u\otimes v),
\]

which is exactly (29). QED.

### Interpretation

Reflection-equivariant FCOA operations therefore have an honest **partial graded bilinear shadow** after free linearization. Grade addition is generated automatically wherever the partial operation is defined.

What fails below is not grade covariance. What fails is totality, closure on the same carrier, and super-skew compatibility.

---

## 6. LC3 domain hypothesis

The third-phase target allows a conservative one-dimensional LC3 extension of the mixed sectors, but the positive legacy ray must remain an exact partial substructure.

For the old signed `oplus` this means:

1. the same-depth same-sign diagonal cells remain defined;
2. distinct positive-positive cells
   \[
   (P_n^+,P_m^+),\qquad n\ne m,
   \tag{30}
   \]
   remain `UNDEF`;
3. by reflected legacy exactness,
   \[
   (P_n^-,P_m^-),\qquad n\ne m,
   \tag{31}
   \]
   also remain `UNDEF`;
4. LC3 may open arbitrary generated mixed cells
   \[
   (P_n^+,P_m^-),
   \qquad
   (P_n^-,P_m^+).
   \tag{32}
   \]

Call a domain satisfying these constraints an **LC3-conservative domain**.

---

## 7. Exact Odd-Odd Domain Intersection Theorem

For a chosen LC3-conservative domain, define

\[
I_\omega
=
\{n\ge1:
(P_n^+,P_n^-),(P_n^-,P_n^+)\in D_\omega\}.
\tag{33}
\]

These are the radial depths at which both orientations of the mirror pair have been opened.

### Theorem 7.1

For every LC3-conservative domain,

\[
\boxed{
\mathscr D_\omega\cap
(V_{\bar1}\otimes V_{\bar1})
=
\operatorname{span}_K
\{a_n\otimes a_n:n\in I_\omega\}.
}
\tag{34}
\]

In particular, even if **all** mixed-sign cells are opened,

\[
\mathscr D_\omega\cap
(V_{\bar1}\otimes V_{\bar1})
=
\operatorname{span}_K\{a_n\otimes a_n:n\ge1\},
\tag{35}
\]

which is a proper subspace of

\[
V_{\bar1}\otimes V_{\bar1}.
\tag{36}
\]

### Proof

Every odd-odd tensor has a unique finite expansion

\[
t=\sum_{n,m\ge1}c_{nm}a_n\otimes a_m.
\tag{37}
\]

Using (15),

\[
\begin{aligned}
a_n\otimes a_m
={}&e_n^+\otimes e_m^+
-e_n^+\otimes e_m^-\\
&-e_n^-\otimes e_m^+
+e_n^-\otimes e_m^-.
\end{aligned}
\tag{38}
\]

For `n != m`, the coefficient of the same-sign basis tensor

\[
e_n^+\otimes e_m^+
\tag{39}
\]

in (37) is exactly `c_nm`. That basis tensor is outside `mathscr D_omega` by positive legacy exactness. Since the basis tensors of `V tensor V` are linearly independent, membership `t in mathscr D_omega` forces

\[
c_{nm}=0\qquad(n\ne m).
\tag{40}
\]

The same conclusion is independently witnessed by the negative-negative term.

Thus only diagonal coefficients `c_nn` may survive. For a fixed `n`, the same-sign tensors in (38) are defined by the old diagonal rule. The two mixed tensors are in the domain exactly when `n in I_omega`. If either is absent, membership forces `c_nn=0`.

Therefore precisely the diagonal tensors listed in (34) survive. QED.

### Corollary 7.2 — totality no-go

No LC3-conservative completion makes the canonical partial bilinearization into a total bilinear map

\[
V_{\bar1}\times V_{\bar1}\to W.
\tag{41}
\]

### Proof

Choose `n != m`. Then `a_n tensor a_m` is an odd-odd pure tensor but is not in `mathscr D_omega` by Theorem 7.1. QED.

### Polarization does not repair the defect

For a symmetric bilinear law, one might try to recover cross terms from diagonal values. But

\[
(a_n+a_m)\otimes(a_n+a_m)
\tag{42}
\]

contains the forbidden off-diagonal tensors `a_n tensor a_m` and `a_m tensor a_n`, so it is itself outside the canonical domain for `n != m`. Declaring the cross terms zero or supplying them by a polarization rule is an additional totalization of `UNDEF`, not a consequence of the FCOA operation.

---

## 8. Odd-Square Output Formula

Assume `n in I_omega`, so the whole tensor `a_n tensor a_n` lies in the domain.

Let the inherited same-sign diagonal outputs be

\[
t_n^+=\omega(P_n^+,P_n^+),
\qquad
t_n^-=\omega(P_n^-,P_n^-)=J_*t_n^+.
\tag{43}
\]

For canonical signed M0 `oplus`, these are terminal outputs in the old `E^+` family or its reflected lift.

Let

\[
z_n=\omega(P_n^+,P_n^-).
\tag{44}
\]

Reflection equivariance forces

\[
\omega(P_n^-,P_n^+)=J_*z_n.
\tag{45}
\]

Then by (38),

\[
\boxed{
\widetilde\omega(a_n\otimes a_n)
=t_n^++t_n^- -z_n-J_*z_n.
}
\tag{46}
\]

Equation (46) is automatically reflection-even, agreeing with Theorem 5.1.

---

## 9. Typed-Output Closure No-Go

### Theorem 9.1

Under the free typed-output semantics (19), for every `n in I_omega`,

\[
\boxed{
\widetilde\omega(a_n\otimes a_n)\in V
\Longrightarrow
\widetilde\omega(a_n\otimes a_n)=0.
}
\tag{47}
\]

Hence no conservative mirror completion produces a **nonzero** odd-square output in the base-even carrier `V_0` through the canonical bilinearization of the old `oplus`.

### Proof

The inherited outputs `t_n^+` and `t_n^-` belong to the terminal subspace `F`.

There are two typed possibilities for the mixed output `z_n`.

**Case 1: `z_n` is base-valued.** Then `z_n+J_*z_n` lies in `V`. The terminal projection of (46) is

\[
t_n^++t_n^-.
\tag{48}
\]

This is nonzero. If the reflected fiber is split, the two terms are distinct basis vectors. If it is shared, (48) equals `2 t_n^+`, nonzero because `char K != 2`. Thus (46) is not in `V`.

**Case 2: `z_n` is terminal-valued.** Then every term of (46) lies in `F`. Therefore (46) can belong to `V` only if its terminal component is zero. Since `V cap F={0}`, this forces the entire vector (46) to be zero.

The same reasoning applies if the mixed value belongs to any new non-base output sort: it lies in `F`, not `V`.

Thus a nonzero base-even odd-square output is impossible. QED.

### Example: mirror cancellation

For the conservative rule

\[
P_n^+\oplus P_n^-=P_0,
\qquad
P_n^-\oplus P_n^+=P_0,
\tag{49}
\]

one obtains

\[
\widetilde\oplus(a_n\otimes a_n)
=t_n^++t_n^- -2e_0.
\tag{50}
\]

This is reflection-even but not base-valued because the inherited terminal component survives.

Projecting (50) to `V` would give `-2e_0`, but that projection is a new information-losing map

\[
W=V\oplus F\to V
\tag{51}
\]

and therefore is not a faithful realization of the original typed operation.

---

## 10. Root-Odd Super-Skew Obstruction

The preceding obstructions concern odd-odd totality and closure. The old operation already fails the super exchange law on an even-odd sector where no mixed completion is involved.

Set

\[
a_0:=0.
\tag{52}
\]

### Lemma 10.1

For every `n>=1`,

\[
\boxed{
\widetilde\oplus(e_0\otimes a_n)=a_n,
}
\tag{53}
\]

and

\[
\boxed{
\widetilde\oplus(a_n\otimes e_0)=a_{n-1}.
}
\tag{54}
\]

### Proof

The left-root rule is

\[
P_0\oplus P_n^\sigma=P_n^\sigma,
\tag{55}
\]

so linear subtraction of the two reflected cells gives (53).

The right-root rule is radial contraction. For `n>=2`,

\[
P_n^\sigma\oplus P_0=P_{n-1}^\sigma,
\tag{56}
\]

which gives `a_{n-1}` after subtraction. For `n=1`, both reflected cells return `P_0`, hence their difference is zero, equal to `a_0`. QED.

### Theorem 10.2 — faithful super-skew no-go

There is no bilinear Lie-super bracket

\[
[-,-]:V\times V\to V
\tag{57}
\]

that agrees with the canonical FCOA bilinearization on both root/odd orientations:

\[
[e_0,a_n]=\widetilde\oplus(e_0\otimes a_n),
\qquad
[a_n,e_0]=\widetilde\oplus(a_n\otimes e_0)
\tag{58}
\]

for all `n>=1`.

### Proof

The root vector `e_0` is even and `a_n` is odd. Graded skew-symmetry therefore requires

\[
[e_0,a_n]=-[a_n,e_0].
\tag{59}
\]

Using Lemma 10.1, this would imply

\[
a_n=-a_{n-1}.
\tag{60}
\]

For `n=1`, (60) gives

\[
a_1=0,
\]

contradicting the free linearization. For every `n>=2`, the independent odd basis vectors `a_n` and `a_{n-1}` also cannot satisfy (60). QED.

### Corollary 10.3

The obstruction is independent of every mixed-sector choice. It is inherited entirely from the original FCOA positional asymmetry

\[
P_0\oplus x=x,
\qquad
x\oplus P_0=\rho(x).
\tag{61}
\]

Thus no LC3 mixed completion can repair faithful super-skewness without changing how the bracket is extracted from `oplus`.

---

## 11. Combined Bilinear-Lift No-Go Theorem

### Theorem 11.1

Assume all of the following:

1. the positive legacy ray is preserved as an exact partial substructure;
2. the negative same-sign sector is its reflection-compatible copy;
3. only mixed-sign cells may be newly realized at LC3;
4. `UNDEF` is not identified with zero;
5. terminal outputs remain typed and distinct from base points;
6. the operation is free-linearized by the canonical partial bilinearization (23);
7. no independent bracket, quotient, or output projection is added.

Then no one-dimensional conservative LC3 completion of `oplus` induces a nonzero total bilinear operation

\[
B:V_{\bar1}\times V_{\bar1}\to V_{\bar0}
\tag{62}
\]

that can serve as the odd-odd sector of a Lie-super bracket faithfully extending the original operation.

### Proof

Theorem 7.1 prevents totality on `V_1 x V_1`. Theorem 9.1 prevents a nonzero base-even diagonal value even where odd squares are defined. Independently, Theorem 10.2 prevents any faithful Lie-super bracket from agreeing with the original operation on the already-defined root/odd sector. Any one obstruction is sufficient; together they close the route. QED.

---

## 12. Why the obvious escape routes do not count

The no-go theorem is intentionally conservative. Several mathematical constructions can evade it, but every one changes the research question.

### 12.1 Replace `UNDEF` by zero

One may extend the partial tensor map to all of `V tensor V` by declaring every missing basis tensor to have value zero.

This violates the FCOA semantic rule

\[
\boxed{\texttt{UNDEF} \ne 0.}
\tag{63}
\]

It collapses absence of interaction into a distinguished algebraic output.

### 12.2 Project away terminal outputs

The linear projection

\[
\pi_V:W=V\oplus F\to V
\tag{64}
\]

turns the cancellation example (50) into `-2e_0`.

But `pi_V` deletes inherited terminal-output information. It is a non-faithful observation map, not the original operation.

### 12.3 Identify terminal outputs with base states

A quotient that makes `E_n^+` equal to a base vector can force closure, but it destroys the typed output architecture and changes old values. This is not a conservative extension.

### 12.4 Open old positive-positive off-diagonal cells

That could remove the totality obstruction, but the positive legacy ray would cease to be an exact partial substructure. It is outside the LC3 mandate.

### 12.5 Define a super-skew symmetrization

One could introduce

\[
B(u,v)
=
\widetilde\omega(u,v)
-(-1)^{pq}\widetilde\omega(v,u)
\tag{65}
\]

where both terms make sense.

This is a **new bracket definition**. Moreover the standard theorem that a supercommutator satisfies graded Jacobi requires an associative graded multiplication. The original FCOA `oplus` is partial and nonassociative, so that theorem does not apply.

### 12.6 Move to the operator superalgebra

The v0.1 construction inside `End_K(V)` remains valid. There composition is associative and the standard supercommutator exists. But this is precisely the already-classified `FORMAL EMBEDDING` shadow, not an identification of `oplus` with the bracket.

---

## 13. Graded Jacobi status

The planned graded-Jacobi test is **not reached** for the original-operation route.

A Lie-super Jacobi identity is a condition on a total bilinear super-skew bracket. Theorems 7.1, 9.1, and 10.2 show that no such faithful bracket is induced by the original `oplus` under the accepted conservative rules.

Testing Jacobi after zero-filling, output projection, quotienting, or explicit super-skew symmetrization would test a newly introduced algebra rather than the claimed emergent FCOA operation.

Therefore the correct research action is to stop the faithful Lie-superbracket route here rather than manufacture a Jacobi candidate.

---

## 14. What survives positively

The negative result does not erase the earlier mathematics. The following remain proved:

1. reversible line completion derives reflection;
2. reflection derives a canonical `Z_2` eigenspace grading after free linearization;
3. reflection-equivariant operation linearization obeys the partial grade law (29);
4. on the mirror locus, simultaneous reflection equals argument exchange;
5. reflection-even mirror output is exchange-symmetric and reflection-odd mirror output is exchange-antisymmetric;
6. the current line core does not select the super bicharacter;
7. the associated endomorphism algebra has a genuine superalgebra structure after choosing the standard supercommutator.

The mathematically correct picture is therefore

\[
\boxed{
\text{FCOA-Z generates a reflection-graded partial shadow and mirror exchange law,}
\text{ not the Lie-super bracket of }\oplus.
}
\tag{66}
\]

---

## 15. Programme classification

### Strong claim tested

> The birth of the two sides of the FCOA axis makes the original operation itself into a Lie-superalgebra-type bracket without an independently inserted grading/exchange structure.

**Verdict:**

\[
\boxed{\texttt{REJECT}.}
\tag{67}
\]

under the conservative reflection-linearized model specified above.

### Line-first verdict

For a faithful nonzero total odd-odd bilinear lift of `oplus`:

\[
\boxed{\texttt{1D-OBSTRUCTED}.}
\tag{68}
\]

The obstruction is not lack of imagination in the mixed sector. It is already encoded in the preserved one-dimensional legacy structure.

### Overall SOL-GRADED verdict

\[
\boxed{\texttt{FORMAL EMBEDDING}}
\tag{69}
\]

remains valid for the reflection/operator shadow and mirror-exchange decomposition.

It does **not** upgrade to `MODEL CANDIDATE` for Lie superalgebras or SUSY.

---

## 16. Research consequence

The natural continuation, if SOL-GRADED is revisited, is no longer

\[
\text{“derive SUSY from }\oplus\text{”.}
\]

The mathematically earned object is instead a theory of

\[
\boxed{
\text{reflection-graded partial algebras with geometry-induced mirror exchange.}
}
\tag{70}
\]

That object is closer to the actual FCOA structure because it retains:

- partial domains;
- typed terminal outputs;
- rooted role asymmetry;
- reflection-generated grading;
- sector-local exchange behavior.

A future comparison with Lie superalgebras should treat the latter as one total/closed special case, not as the definition of the FCOA object.

---

## 17. Publication decision

The SOL-GRADED research question is now **mathematically closed at the current scope**: there is a positive reflection-graded/mirror-exchange theorem package and a rigorous negative theorem for the faithful Lie-superbracket route.

Standalone publication as a SUSY paper is **not recommended**. The result is not a SUSY model.

Publication-quality use is recommended in one of two forms:

1. a section of the FCOA-Z line-completion / applied-directions paper, where the superalgebra comparison functions as a hostile structural test; or
2. a later mathematical note on reflection-graded partial algebras, if that abstract theory is developed beyond the present example.

No stronger physics language should be used.

---

## 18. Standard comparison anchor

For a Lie superalgebra, the bracket is a total bilinear map on a `Z_2`-graded vector space, is graded skew-symmetric

\[
[x,y]=-(-1)^{|x||y|}[y,x],
\tag{71}
\]

and satisfies graded Jacobi. This standard target definition is the only external superalgebra fact needed for the no-go comparison.

FCOA-specific results above are derived from the repository's signed-line core and conservative completion rules.

Published FCOA base:

https://doi.org/10.5281/zenodo.22169264
