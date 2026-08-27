# Second Hostile Audit — Threshold-Profile Valuation Dichotomy

**Project:** Prime-Successor Algebra / Two Walls  
**Branch:** `research/threshold-profile-dichotomy`  
**Date:** 2026-08-27  
**Verdict:** PASS, with one notation correction: all definability claims below are parameter-free (empty-parameter) unless explicitly stated otherwise.

## 1. Audit target

The second audit attacks exactly the two proof obligations left open in the first checkpoint:

1. justify rigorously the passage from adelic open image to simultaneous surjectivity

\[
G_{\mathbb Q(\mu_\infty)}
\longrightarrow
\prod_{r\in R}\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z)
\]

for every finite set of sufficiently good primes and arbitrary positive depths \(k_r\);

2. make the Trakhtenbrot reduction fully first-order and effective without using any algorithm for the threshold profile \(\kappa\).

A third issue is audited at the same time: the definability boundary is an \(\emptyset\)-definability statement.

---

## 2. Adelic image: exact specialization to Delta

Let \(f=\Delta\), the level-one weight-12 cusp form.

Its coefficient field is \(\mathbb Q\), its nebentypus is trivial, and there are no nontrivial inner twists. Thus, in Loeffler's notation for a non-CM newform, the auxiliary field \(F\) is \(\mathbb Q\), the quaternion algebra is split, and the norm-one algebraic group is

\[
G^\circ=\operatorname{SL}_2.
\]

Moreover the subgroup called \(H\) in Loeffler's Section 2 is all of \(G_\mathbb Q\) in this specialization.

Write

\[
\widetilde\rho_\Delta:G_\mathbb Q\to G(\widehat{\mathbb Q})
\]

for the augmented adelic representation whose second coordinate is the cyclotomic character \(\chi\).

Loeffler's Theorem 2.3.1 says that

\[
U:=\widetilde\rho_\Delta(G_\mathbb Q)
\]

is open in \(G(\widehat{\mathbb Q})\).

The proof of Loeffler's Theorem 1.2.3 shows that

\[
U^\circ:=U\cap G^\circ(\widehat{\mathbb Q})
\]

is open in \(G^\circ(\widehat{\mathbb Q})\).

Because the second coordinate of \(\widetilde\rho_\Delta\) is exactly \(\chi\),

\[
U^\circ
=
\widetilde\rho_\Delta\bigl(\ker\chi\bigr)
=
\widetilde\rho_\Delta\bigl(G_{\mathbb Q(\mu_\infty)}\bigr).
\]

After forgetting the trivial cyclotomic coordinate, this is precisely the adelic image of

\[
G_{\mathbb Q(\mu_\infty)}
\]

inside

\[
\prod_r\operatorname{SL}_2(\mathbb Z_r).
\]

Hence this cyclotomic-kernel image is an open subgroup of the profinite product

\[
\prod_r\operatorname{SL}_2(\mathbb Z_r).
\]

---

## 3. Open subgroup implies full factors away from finitely many places

Let

\[
V\le \prod_r\operatorname{SL}_2(\mathbb Z_r)
\]

be open.

Since the product topology has a basis consisting of products

\[
\prod_r V_r
\]

with \(V_r=\operatorname{SL}_2(\mathbb Z_r)\) for all but finitely many \(r\), there exists a finite set \(S\) and open subgroups \(V_r\le\operatorname{SL}_2(\mathbb Z_r)\) for \(r\in S\) such that

\[
\left(\prod_{r\in S}V_r\right)
\times
\left(\prod_{r\notin S}\operatorname{SL}_2(\mathbb Z_r)\right)
\subseteq V.
\]

Therefore

\[
\prod_{r\notin S}\operatorname{SL}_2(\mathbb Z_r)
\subseteq V.
\]

This is also the concrete conclusion appearing in the proof of Loeffler's Theorem 1.2.2: outside a finite set, the full integral local factors lie inside the adelic subgroup.

Applying this to the cyclotomic-kernel image yields a finite exceptional set \(S_\Delta\) such that

\[
\prod_{r\notin S_\Delta}\operatorname{SL}_2(\mathbb Z_r)
\subseteq
\rho_\Delta\bigl(G_{\mathbb Q(\mu_\infty)}\bigr).
\]

This statement is stronger than mere surjectivity of each individual local projection: it gives simultaneous independent control of every finite collection of good local factors.

---

## 4. Arbitrary-depth simultaneous surjectivity

Fix a finite set

\[
R\subseteq\mathbb P\setminus S_\Delta
\]

and arbitrary integers

\[
k_r\ge1
\qquad(r\in R).
\]

From the full-factor inclusion we may prescribe independently any tuple

\[
(g_r)_{r\in R}
\in
\prod_{r\in R}\operatorname{SL}_2(\mathbb Z_r)
\]

while setting all other good coordinates equal to the identity.

Reduction modulo \(r^{k_r}\) gives a surjection

\[
\operatorname{SL}_2(\mathbb Z_r)
\to
\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z).
\]

Hence the combined map

\[
G_{\mathbb Q(\mu_\infty)}
\longrightarrow
\prod_{r\in R}
\operatorname{SL}_2(\mathbb Z/r^{k_r}\mathbb Z)
\]

is surjective.

No boundedness of the family \((k_r)\) is needed: every proof instance uses only finitely many finite depths.

**Audit verdict for the first open obligation: PASS.**

---

## 5. EDGE/NONEDGE witnesses at arbitrary depth

Set

\[
A=\begin{pmatrix}0&-1\\1&1\end{pmatrix},
\qquad
J=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Then

\[
\det A=1,
\qquad
\operatorname{tr}(A)=1,
\qquad
\operatorname{tr}(A)^2-\det(A)=0,
\]

while

\[
\operatorname{tr}(J)^2-\det(J)=3.
\]

Thus for every \(r>3\) and every \(k\ge1\),

\[
\operatorname{tr}(A)^2\equiv\det(A)\pmod{r^k}
\]

and

\[
\operatorname{tr}(J)^2\not\equiv\det(J)\pmod{r^k}.
\]

The positive-depth incidence

\[
E_\kappa(p;r)
\iff
r^{\kappa(r)}\mid \tau(p)^2-p^{11}
\]

is therefore controlled by the exact same pair of integral witnesses for every positive depth.

The determinant-one choice is essential: it matches the cyclotomic-kernel image and removes all determinant entanglement between marker coordinates.

---

## 6. Chebotarev audit

For a finite marker set \(R\), let \(L/\mathbb Q\) be the finite Galois extension cut out by the product of the residual representations modulo \(r^{\kappa(r)}\), \(r\in R\).

Arbitrary-depth surjectivity gives an element

\[
\sigma\in G_{\mathbb Q(\mu_\infty)}
\]

whose image in the finite quotient has prescribed coordinates \(A\) or \(J\).

Chebotarev is applied to the conjugacy class of the image of \(\sigma\) in

\[
\operatorname{Gal}(L/\mathbb Q),
\]

not to the infinite extension \(\mathbb Q(\mu_\infty)\).

Thus there are infinitely many unramified rational primes \(p\) with Frobenius in this class. Trace and determinant are conjugacy invariants, so the prescribed EDGE/NONEDGE pattern survives passage from an element to its conjugacy class.

There is no requirement that a Frobenius element itself lie in the absolute cyclotomic kernel; only its image in the chosen finite quotient must equal the image of \(\sigma\). This is exactly what Chebotarev supplies.

**Chebotarev step: PASS.**

---

## 7. Formal first-order graph reduction

Work in the source sort \((\mathbb N_{>0},\times,1)\). Prime and divisibility are first-order definable.

For a source variable \(a\), define

\[
D_a(x):=\operatorname{Prime}(x)\land x\mid a.
\]

Since every positive integer has finitely many prime divisors, \(D_a\) is always finite.

Let the fixed formula

\[
I_\kappa(x,y;r)
\]

be the GIR isolator already constructed from the single language predicate \(B_\kappa\), and define

\[
R_\eta(x,y)
:=
\exists r\,
\bigl(
\operatorname{Prime}(r)
\land r\mid\eta
\land I_\kappa(x,y;r)
\bigr).
\]

Define the first-order condition \(\operatorname{Bij}(a,b,\mu)\) saying that \(R_\mu\) is a bijection from \(D_a\) to \(D_b\):

- every \(x\in D_a\) has exactly one \(y\in D_b\) with \(R_\mu(x,y)\);
- every \(y\in D_b\) has exactly one \(x\in D_a\) with \(R_\mu(x,y)\).

For source variables \(a,b,\mu,\nu\), put

\[
G_{a,b,\mu,\nu}(x,z)
:=
\exists y\,
\bigl(
D_b(y)
\land R_\mu(z,y)
\land R_\nu(x,y)
\bigr).
\]

Given a first-order sentence \(\varphi\) in the language of one binary relation, define effectively a sentence \(\widehat\varphi\) in the language of \(\mathcal V_{\Delta,\kappa}\) by:

1. relativizing every graph-domain quantifier to \(D_a\);
2. replacing each graph atom \(R(x,z)\) by \(G_{a,b,\mu,\nu}(x,z)\);
3. prefixing

\[
\exists a\,\exists b\,\exists\mu\,\exists\nu
\]

and requiring \(D_a\neq\varnothing\) and \(\operatorname{Bij}(a,b,\mu)\).

This translation is mechanical and contains no occurrence of the external function \(\kappa\). The only profile-dependent symbol it uses is the single relation symbol \(B_\kappa\), which is already part of the fixed structure's language.

---

## 8. Forward direction of the reduction

Suppose \(\varphi\) has a finite nonempty model with vertex set \(\{1,\dots,n\}\).

Choose a GIR grid

\[
(p_i,q_j,r_{ij})_{1\le i,j\le n}
\]

with all entries pairwise distinct.

Set

\[
a=\prod_i p_i,
\qquad
b=\prod_j q_j,
\qquad
\mu=\prod_i r_{ii}.
\]

Then \(R_\mu(p_i,q_j)\) holds exactly when \(i=j\), so \(R_\mu\) is a bijection between \(D_a\) and \(D_b\).

If the finite graph relation is \(E\subseteq[n]^2\), set

\[
\nu=\prod_{(i,j)\in E}r_{ij}.
\]

Then

\[
G_{a,b,\mu,\nu}(p_i,p_j)
\iff
(i,j)\in E.
\]

Hence \(\widehat\varphi\) is true in \(\mathcal V_{\Delta,\kappa}\).

---

## 9. Reverse direction of the reduction

Suppose

\[
\mathcal V_{\Delta,\kappa}\models\widehat\varphi.
\]

Choose witnesses \(a,b,\mu,\nu\). The domain \(D_a\) is finite and nonempty. The formula \(\operatorname{Bij}(a,b,\mu)\) identifies a unique copy of each element of \(D_a\) inside \(D_b\).

Regardless of whether \(\mu\) and \(\nu\) arose from a canonical GIR grid, the formula

\[
G_{a,b,\mu,\nu}
\]

defines some binary relation on the finite set \(D_a\). By construction of the relativization, that finite graph satisfies \(\varphi\).

Therefore

\[
\varphi\text{ has a finite nonempty model}
\iff
\mathcal V_{\Delta,\kappa}\models\widehat\varphi.
\]

If the complete theory of \(\mathcal V_{\Delta,\kappa}\) were decidable, finite satisfiability for one-binary-relation structures would be decidable, contradicting Trakhtenbrot.

**Audit verdict for the second open obligation: PASS.**

---

## 10. Noncomputable threshold profiles cause no problem

The proof never requires an algorithm which, given \(r\), outputs \(\kappa(r)\).

The values \(\kappa(r)\) appear only in the metamathematical existence proof of sufficiently many Frobenius patterns. For every finite marker set, these are finitely many ordinary positive integers, so the corresponding finite Galois quotient exists.

The effective reduction \(\varphi\mapsto\widehat\varphi\) is the same syntactic transformation for every threshold profile.

Hence undecidability holds for every fixed structure \(\mathcal V_{\Delta,\kappa}\) with infinite positive support, even when \(\kappa\) is not computable.

---

## 11. Definability notation correction

The theorem checkpoint used the notation

\[
B_\kappa\in\operatorname{Def}(\mathcal V_{\Delta,0}).
\]

The proof establishes the sharper and safer statement

\[
\boxed{
B_\kappa\in\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,0})
\iff
|P_+(\kappa)|<\infty.
}
\]

Here \(\operatorname{Def}_{\emptyset}\) means definability without parameters.

The finite-support direction is explicitly parameter-free: each exceptional standard prime \(\ell\) is defined by the fixed-scalar formula

\[
\Theta_\ell(r)
:
\operatorname{Prime}(r)
\land
\exists x\,
\bigl(\neg B_\kappa(r,x)\land B_\kappa(r,\ell x)\bigr),
\]

and the finite case split uses only finitely many fixed additive scalar terms.

The infinite-support contradiction uses the parameter-free zero-depth compression theorem and therefore establishes non-\(\emptyset\)-definability. No claim about definability with arbitrary parameters is made here.

---

## 12. Final theorem after audit

For every profile

\[
\kappa:\mathbb P\to\mathbb N_0,
\]

let

\[
P_+(\kappa)=\{r:\kappa(r)\ge1\}.
\]

Then:

### Safe phase

If \(P_+(\kappa)\) is finite, then

\[
\mathcal V_{\Delta,\kappa}
\equiv_{\emptyset\text{-def}}
\mathcal V_{\Delta,0},
\]

so ordinary prime order and prime successor are not parameter-free definable and every fixed parameter-free GIR is finite.

### Amplifying phase

If \(P_+(\kappa)\) is infinite, then one fixed parameter-free ternary formula has infinite GIR, all finite directed graphs are uniformly coded, and

\[
\operatorname{Th}(\mathcal V_{\Delta,\kappa})
\]

is undecidable.

Hence

\[
\boxed{
|P_+(\kappa)|<\infty
\iff
\forall I\;\operatorname{GIR}(I)<\infty
}
\]

for fixed parameter-free ternary formulas \(I\), and

\[
\boxed{
B_\kappa\in\operatorname{Def}_{\emptyset}(\mathcal V_{\Delta,0})
\iff
|P_+(\kappa)|<\infty.
}
\]

The phase transition is a support-cardinality transition.

---

## 13. Publication verdict

The two obligations left after the first hostile audit are closed.

- arbitrary-depth finite residual independence: PASS;
- Chebotarev finite-pattern realization: PASS;
- parameter-free finite graph interpretation: PASS;
- independence from computability of \(\kappa\): PASS;
- finite-support safe side by explicit interdefinability: PASS;
- definability statement corrected to \(\emptyset\)-definability: PASS.

**Second hostile audit verdict: PASS.**

The mathematical publication threshold is reached, subject only to the ordinary pre-publication literature/metadata/document audit.