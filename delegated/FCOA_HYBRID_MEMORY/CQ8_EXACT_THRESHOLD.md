# FCOA Hybrid Memory — Exact CQ Width Threshold (Audited Repair)

**Status:** repaired theorem after hostile audit  
**Main result:** the minimum conjunctive-query variable width for `N^{1+o(1)}` preprocessing of exact truncated addition is exactly `9`.

## 0. Audit note

The first version of this file contained a real gap. It proved that each free-coordinate information boundary had at least two helpers, but then incorrectly concluded that both had to be private non-negligible helpers. A shared `o(log N)` boundary helper can still be topologically necessary, so that counting step was not justified.

The proof below removes that step completely. It conditions away all subpolynomial-information helpers first and works on the remaining positive-information core. In that core, color components are genuinely disjoint, and a singleton positive color component is impossible. This yields the required six-helper lower bound without counting low-information shared boundary nodes.

The repaired argument also subsumes the near-linear impossibility parts of the earlier `CQ^6`, `CQ^7`, and `CQ^8` analyses.

---

## 1. Model and target relation

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

A preprocessing representation consists of a finite structure `A_N` over one fixed finite bounded-arity relational signature and a fixed conjunctive query

\[
q(x,y,z)=\exists \bar u\;\bigwedge_i R_i(\bar t_i)
\]

whose answer on the target sector is exactly `Add_N`.

Assume total preprocessing size

\[
S_N=N^{1+o(1)}.
\]

Let `h` be the number of helper variables in `\bar u`; the total CQ width is

\[
k=3+h.
\]

We prove

\[
\boxed{h\ge6}.
\]

Hence

\[
\boxed{k\ge9}.
\]

---

## 2. Regular Latin slice

Put

\[
m=\lfloor N/3\rfloor
\]

and restrict attention to

\[
\mathcal T_m
=
\{(x,y,z):0\le x,y<m,\ z=x+y\}.
\]

Choose `(X,Y)` uniformly from `[m]^2` and put `Z=X+Y`.

Then

\[
H(X)=H(Y)=\log m,
\]

\[
H(X,Y)=H(X,Z)=H(Y,Z)=2\log m,
\]

and

\[
H(Z)=\log m+O(1).
\]

Thus, after normalization by `log N`,

\[
h(X)=h(Y)=h(Z)=1,
\]

\[
h(X,Y)=h(X,Z)=h(Y,Z)=2,
\]

and the pairwise mutual informations vanish asymptotically.

Every two free coordinates determine the third.

---

## 3. Deterministic witnesses and the Latin-box property

Choose one satisfying helper tuple deterministically for every triple in `\mathcal T_m`.

If any primitive atom contains two distinct free variables among `X,Y,Z`, its projection already contains `Theta(N^2)` distinct free pairs, contradicting near-linear preprocessing. Hence every atom contains at most one free arithmetic variable.

For a fixed complete helper assignment, the free-variable constraints therefore factor into a Cartesian box

\[
X_{\bar u}\times Y_{\bar u}\times Z_{\bar u}.
\]

A nonempty Cartesian box contained in `x+y=z` has size one: fixing any two coordinates determines the third, and varying either remaining coordinate would violate the equation.

Consequently every productive helper tuple determines a unique free triple. Together with deterministic witness selection,

\[
H(X,Y,Z\mid\bar U)=o(\log N),
\]

\[
H(\bar U\mid X,Y,Z)=0.
\]

The selected helper tuple therefore carries the two entropy units of the Latin surface.

---

## 4. Adjacent helpers encode their free coordinate

For `F in {X,Y,Z}`, let `A_F` be the set of helper variables appearing together with `F` in at least one atom.

Every helper tuple `S subseteq A_F` occurring with `F` in an atom satisfies

\[
H(S\mid F)=o(\log N),
\]

because that primitive relation has only `N^{1+o(1)}` tuples while `H(F)=\log N+o(\log N)`.

Since there are only constantly many atoms/helpers,

\[
H(A_F\mid F)=o(\log N).
\tag{4.1}
\]

Conversely, the Latin-box argument implies

\[
H(F\mid A_F)=o(\log N).
\tag{4.2}
\]

Indeed, if two productive witnesses agreed on all helper values adjacent to `F` but yielded two different values of `F`, then all atoms involving `F` would be unchanged; keeping the remainder of one witness fixed would produce two accepted triples with the same other two free coordinates, contradicting the Latin functional dependency.

Hence

\[
H(A_F)=\log N+o(\log N).
\tag{4.3}
\]

So the adjacent-helper set is an asymptotically lossless encoding of `F`.

---

## 5. Remove all zero-information helpers

Call a helper `U` **zero-information** on the selected witness distribution if

\[
H(U)=o(\log N).
\]

There are only constantly many helpers, so their joint entropy is also `o(log N)`. Hence they assume only

\[
N^{o(1)}
\]

typical joint values.

Fix a joint value whose fiber contains

\[
N^{2-o(1)}
\]

selected addition triples. Substitute those helpers as constants in the CQ and restrict to that fiber.

On a Latin relation of size `N^{2-o(1)}`, each pair projection has the same size and each coordinate still assumes `N^{1-o(1)}` values. Thus on the restricted fiber

\[
H(F)=\log N-o(\log N),
\]

\[
H(F,G)=2\log N-o(\log N)
\]

for distinct `F,G in {X,Y,Z}`.

Repeat this conditioning finitely many times if a previously positive helper collapses to zero normalized entropy. At the end we obtain a dense Latin fiber and a reduced query in which every remaining helper has

\[
H(U)=\Omega(\log N).
\tag{5.1}
\]

All subsequent entropy statements refer to this stable positive-information core.

---

## 6. Information colors

A remaining helper `U` is **F-colored** if

\[
H(U\mid F)=o(\log N).
\]

Every helper adjacent to `F` is F-colored by Section 4.

### Lemma 6.1 — positive helpers have a unique color

No remaining positive-information helper can be both F-colored and G-colored for two distinct free coordinates.

### Proof

For distinct `F,G`, the normalized mutual information is `o(log N)`. The standard common-information inequality gives

\[
H(U)
\le
I(F;G)+H(U\mid F)+H(U\mid G)
=o(\log N),
\]

contradicting (5.1). `square`

Thus the positive-information F-colors are pairwise disjoint.

---

## 7. Maximal colored components

For each free coordinate `F`, define `C_F` as follows.

Start with all helpers adjacent to `F`. Repeatedly add a remaining helper whenever it appears in a helper-only atom together with variables already in `C_F` and the near-linear relation forces it to be F-colored. Continue to maximality.

Equivalently, `C_F` is the maximal connected positive-information region reachable from the `F`-branch while staying inside F-colored helpers.

By (4.3),

\[
H(C_F)\ge H(A_F)=\log N-o(\log N),
\]

so each `C_F` is nonempty and carries one entropy unit.

By Lemma 6.1,

\[
C_X,C_Y,C_Z
\]

are pairwise disjoint.

---

## 8. Singleton colored components are impossible

### Lemma 8.1

For each `F in {X,Y,Z}`,

\[
\boxed{|C_F|\ge2.}
\]

### Proof

Assume

\[
C_F=\{U\}.
\]

Because `C_F` carries the information of `F`,

\[
H(U)=\log N-o(\log N).
\tag{8.1}
\]

If no helper-only atom connects `U` to any positive-information helper outside `C_F`, then after the zero-information helpers have been fixed the CQ factor graph separates the `F`-branch from the other two free branches.

The resulting query answer factors as a Cartesian product in coordinate `F` versus the other two coordinates. A dense Latin subrelation with `N^{1-o(1)}` values of `F` cannot have this form because the other two coordinates determine `F` uniquely. Contradiction.

Therefore some helper-only atom contains `U` and a nonempty tuple `T` of positive-information helpers outside `C_F`.

That atom belongs to a relation of size `N^{1+o(1)}`, so

\[
H(U,T)\le\log N+o(\log N).
\]

Using (8.1),

\[
H(T\mid U)=o(\log N).
\]

Since

\[
H(U\mid F)=o(\log N),
\]

we get

\[
H(T\mid F)=o(\log N).
\]

Thus every component of `T` is F-colored. By construction it is connected to `U` through this helper-only atom, so it belongs to the maximal F-colored component `C_F`, contradicting `C_F={U}`.

Therefore `|C_F|>=2`. `square`

---

## 9. Six-helper lower bound

The three positive colored components are pairwise disjoint and each contains at least two helpers:

\[
|C_X|\ge2,
\qquad
|C_Y|\ge2,
\qquad
|C_Z|\ge2.
\]

Therefore the reduced positive-information core contains at least

\[
2+2+2=6
\]

helpers.

Conditioning only removed helpers; it never created new helper variables. Hence the original CQ also had at least six helpers.

Thus

\[
\boxed{h\ge6}.
\]

Since there are three free variables,

\[
\boxed{k=3+h\ge9}.
\]

This argument applies to **every** near-linear CQ representation, not merely `CQ^8`.

---

## 10. Matching CQ9 upper bound

Choose coprime

\[
p,q=\Theta(\sqrt N)
\]

with

\[
pq>2N.
\]

Store target residue maps and the complete modular addition tables modulo `p` and `q`. Total preprocessing is `Theta(N)`.

Use the CQ

\[
\begin{aligned}
Add(x,y,z)\iff\exists x_p,y_p,z_p,x_q,y_q,z_q\;(&P(x,x_p)\land P(y,y_p)\land P(z,z_p)\\
&\land Q(x,x_q)\land Q(y,y_q)\land Q(z,z_q)\\
&\land A_p(x_p,y_p,z_p)\\
&\land A_q(x_q,y_q,z_q)).
\end{aligned}
\]

This uses exactly

\[
3+6=9
\]

variables.

The two congruences imply

\[
pq\mid x+y-z,
\]

and

\[
|x+y-z|<2N<pq,
\]

so `x+y=z` exactly.

Hence

\[
\boxed{k_+\le9}.
\]

Combining with Section 9:

### Theorem HM-CQ-EXACT (audited)

\[
\boxed{k_+=9.}
\]

---

## 11. AL2 threshold

The truncated multiplication graph

\[
Mul_N(x,y,z)\iff xy=z<N
\]

contains

\[
Theta(N\log N)=N^{1+o(1)}
\]

true tuples. It can therefore be directly materialized as one ternary relation without changing the near-linear preprocessing exponent and queried atomically with three variables.

Thus

\[
\boxed{k_{AL2}=k_{AL1}=9.}
\]

This equality is specific to the near-linear total-storage benchmark and the truncated multiplication graph.

---

## 12. Final phase diagram

For near-linear preprocessing:

\[
\boxed{
\begin{array}{c|ccc}
\text{CQ width }k & AL0 & AL1 & AL2\\
\hline
3 & \checkmark & \times & \times\\
4 & \checkmark & \times & \times\\
5 & \checkmark & \times & \times\\
6 & \checkmark & \times & \times\\
7 & \checkmark & \times & \times\\
8 & \checkmark & \times & \times\\
9 & \checkmark & \checkmark & \checkmark
\end{array}
}
\]

The exact width jump between near-linear order memory and near-linear additive transport is therefore

\[
\boxed{3\longrightarrow9}.
\]

---

## 13. Relation to the earlier CQ6/CQ7 proofs

The repaired positive-core argument is stronger at the threshold level than the separate CQ6 and CQ7 analyses:

- it immediately rules out near-linear preprocessing for every width below `9`;
- it does **not** replace the quantitative `CQ^6` lower bound `sigma_1^{CQ}(6)>=7/6`, which remains independently useful;
- the CQ7 case analysis is no longer needed for the threshold theorem, though it remains a useful structural audit.

---

## 14. Claim ceiling and publication status

What is proved:

\[
\boxed{\text{near-linear exact addition requires at least six helper variables, and six suffice}.}
\]

What is not proved:

- exact storage exponents for widths `6,7,8`;
- the same threshold for arbitrary full `FO^k` with negation/disjunction;
- an encoding-independent statement outside the static relational CQ preprocessing model.

The theorem is suitable for publication only together with the audit note above, which records and repairs the original boundary-counting flaw.

---

## 15. Literature calibration

Entropy-vector methods for conjunctive-query size bounds under functional dependencies are standard; Gogacz and Torunczyk give a characterization in terms of entropy vectors and finite groups. The present proof is a specialized representation lower bound for the exact Latin/quasigroup relation of finite addition and is not an immediate corollary of their general theorem. citeturn265085search0

Relevant references:

- Tomasz Gogacz, Szymon Torunczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.
- Dan Olteanu, Jakub Zavodny, *Factorised Representations of Query Results: Size Bounds and Readability*, ICDT 2012.
- Christoph Berkholz, Harry Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026.
