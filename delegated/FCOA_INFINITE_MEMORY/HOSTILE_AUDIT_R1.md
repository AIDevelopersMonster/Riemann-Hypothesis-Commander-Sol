# Hostile Model-Theoretic Audit R1

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary  
**Date:** 2026-08-28  
**Target:** `FO_BOUNDARY.md`, `COUNTERMODELS.md`, `ARITHMETIC_LEAKAGE_NOTES.md`, `UPSTREAM_MEMO.md`  
**Status:** hostile audit with repairs and strengthening

## 1. Audit verdict

The central boundary survives audit:

\[
\boxed{
\operatorname{Aut}(G_\omega,S)=1
\quad\text{and}\quad
S\text{ is FO-recoverable}
\quad\not\Rightarrow\quad
<\text{ is FO-definable}.
}
\]

The following points are confirmed:

1. directed adjacency/successor is FO-recoverable from infinite G2 definedness;
2. full transitive order is not FO-definable from successor;
3. the full canonical M0+G2 decoration does not change that conclusion;
4. no single FO formula defines full order uniformly on all finite directed paths;
5. finite parameters and bounded/local G3-style enrichments do not cross the FO boundary;
6. FO+TC and MSO do recover the order;
7. the infinite complete two-value comparison layer does make order FO-definable;
8. the finite G4-C reversal/output-swap symmetry genuinely disappears on the one-ended \(\omega\)-carrier.

Two repairs are mandatory:

- `FO+TC/MSO` and computable recoverability must not be written as a strict general expressiveness chain. They are distinct notions; on this particular carrier both recover order while FO does not.
- two anonymous outputs are minimal only **inside the complete off-diagonal value-color architecture**. They are not globally minimal among FCOA enrichments: if the domain itself may carry global order, one terminal output suffices.

The audit also strengthens Arithmetic Leakage control: the canonical order-recovering enrichments studied here are interpretable in \((\mathbb N,<)\) with finitely many tags/copies, so ordinary index addition and multiplication remain FO-nondefinable.

---

## 2. Signature discipline

The primary model-theoretic language for nondefinability is relational.

Let

\[
S(x,y)
\]

be the directed successor-edge relation on

\[
G_\omega=\{P_2,P_3,\ldots\}.
\]

For a partial operation use its graph relation

\[
T(x,y,z)\iff x\star y=z.
\]

This avoids hidden assumptions about partial-function term semantics.

If a unary successor function symbol is used instead, a fixed formula can contain successor terms of finite but nonzero depth. The relational proof transfers after the standard graph translation; any locality bound must then account for both quantifier rank and term depth. Therefore the bare phrase “radius \(2^q\)” is valid only after the signature convention has been fixed.

---

## 3. Independent EF/locality proof of the infinite boundary

### Theorem HA-1 — no FO transitive order on the successor ray

There is no FO formula \(\varphi(x,y)\) in the relational language \(\{S\}\) such that

\[
\varphi(a,b)\iff a<_{\rm ray}b
\]

for all \(a,b\in G_\omega\).

### Proof

Fix an arbitrary FO formula \(\varphi(x,y)\) and let \(q\) be its quantifier rank.

The Gaifman graph of \((G_\omega,S)\) is the undirected one-way path. FO on a finite relational signature is local: for this fixed \(\varphi\) there is a finite radius \(r=r(\varphi)\) such that, for two free points whose \(r\)-neighborhoods are disjoint, the value of \(\varphi\) is determined by their rooted local types together with global sentences independent of the ordering of the two free variables.

Choose

\[
a<b
\]

so far from the root and from one another that

\[
d(a,P_2)>r,
\qquad
d(b,P_2)>r,
\qquad d(a,b)>2r.
\]

The rooted radius-\(r\) neighborhoods of \(a\) and \(b\) are isomorphic directed path segments. Since the two neighborhoods are disjoint, the local configuration of the ordered tuple \((a,b)\) is isomorphic to that of \((b,a)\) after exchanging the two isomorphic components. All global sentence components are unchanged.

Hence

\[
\varphi(a,b)\iff\varphi(b,a).
\]

But

\[
a<_{\rm ray}b,
\qquad
\neg(b<_{\rm ray}a).
\]

Contradiction. \(\square\)

### EF formulation

Equivalently, for every finite number of rounds, choose \(a<b\) sufficiently deep and sufficiently separated. Duplicator maintains two disjoint interior path neighborhoods around the distinguished points and exchanges the two neighborhoods between the two pointed copies. A finite game cannot force traversal of the unbounded gap. Thus

\[
(G_\omega,S,a,b)\equiv_q(G_\omega,S,b,a)
\]

for suitable \(a,b\), while order separates the tuples.

This proof is independent of quantifier elimination and therefore closes the requested hostile-audit route.

---

## 4. Quantifier-elimination route: retained only as a secondary proof

The standard theory of natural numbers with zero and successor admits a quantifier-elimination treatment in the appropriate successor language. This gives a second proof: a fixed formula can only compare finitely many bounded successor iterates, so sufficiently separated \((a,b)\) and \((b,a)\) have the same formula type.

The branch does not rely on this literature fact after HA-1; it is now only a cross-check.

---

## 5. Full M0+G2 decoration: explicit interpretation audit

### Theorem HA-2 — M0+G2 does not secretly add global FO memory

The canonical infinite M0+G2 structure is FO-interpretable in the successor ray using finitely many tagged copies. Consequently, if full order were FO-definable on its generic sort, full order would be FO-definable in \((G_\omega,S)\), contradicting HA-1.

### Interpretation

Use finitely many tags for:

- the generic base copy \(G\);
- the \(E^\ast\)-copy;
- the \(E^\times\)-copy;
- the singleton boundary points \(P_0,P_1\);
- the singleton G2 output \(\Omega\).

All tag positions can be represented by finitely many parameter-free definable initial points of the ray. The operation graph is then defined by the following successor/equality clauses:

\[
P_0\otimes P_i=P_0,
\]

\[
P_i\otimes P_0=E_i^\ast,
\]

\[
P_1\otimes P_i=P_i\otimes P_1=P_i,
\]

\[
P_i\otimes P_i=E_i^\times,
\]

and

\[
P_i\otimes P_j=\Omega\iff S(P_i,P_j)
\]

for distinct generic inputs.

Thus every formula in the decorated structure pulls back effectively to an FO formula over successor. No extra unbounded relation is hidden in the M0 output families.

### One-sorted role definability

In the one-sorted graph presentation let

\[
A(x):=\exists y\exists z\,T(x,y,z)\lor\exists y\exists z\,T(y,x,z)
\]

mean that \(x\) is active as an argument.

The left-zero boundary point is intrinsically definable by

\[
B_0(x):=A(x)\wedge
\forall y\bigl(A(y)\wedge y\ne x\to T(x,y,x)\bigr).
\]

The identity-like boundary point is definable by

\[
B_1(x):=A(x)\wedge\neg B_0(x)\wedge
\forall y\Bigl(
A(y)\wedge\neg B_0(y)\wedge y\ne x
\to T(x,y,y)\wedge T(y,x,y)
\Bigr).
\]

Hence the generic base class is

\[
G(x):=A(x)\wedge\neg B_0(x)\wedge\neg B_1(x).
\]

This closes the one-sorted sorting loophole: the generic carrier need not be externally named for the transfer argument.

---

## 6. Uniform finite-family audit

### Theorem HA-3 — no uniform FO order formula on all finite rays

There is no single FO formula defining strict transitive order on every finite directed path

\[
P_2\to\cdots\to P_N.
\]

### Proof sketch

Fix a candidate formula \(\varphi(x,y)\). In the relational successor signature it has finite locality radius \(r\). Choose a finite path with two points \(a<b\) such that both are farther than \(r\) from both endpoints and farther than \(2r\) from one another. The two rooted neighborhoods are isomorphic interior path segments and disjoint. Swapping their roles preserves every local configuration visible to \(\varphi\), so

\[
\varphi(a,b)\iff\varphi(b,a),
\]

contradicting strict order.

For a function-symbol presentation, first translate the fixed candidate formula to the relational graph language; the required radius then depends on the translated formula, including its finite term depth.

Thus per-size formulas

\[
\varphi_N(x,y)=\bigvee_{1\le k\le N-2}S^k(x,y)
\]

do not yield a uniform family formula.

---

## 7. Stronger negative result: finite unary coloring still does not give order

### Theorem HA-4 — unary-color robustness

Let \(P_1,\ldots,P_m\subseteq G_\omega\) be arbitrary unary predicates, with \(m<\infty\). Then full strict order is not FO-definable in

\[
(G_\omega,S,P_1,\ldots,P_m).
\]

The predicates need not themselves be definable from successor.

### Proof

Assume \(\varphi(x,y)\) defines order and let \(r\) be a locality radius for \(\varphi\).

At an interior point, a radius-\(r\) neighborhood is a directed segment of fixed finite length with each vertex carrying one of finitely many \(m\)-bit color patterns. Hence there are only finitely many rooted colored radius-\(r\) neighborhood types.

Infinitely many deep points therefore realize the same local type. Choose two such points \(a<b\) farther than \(2r\) apart. Their neighborhoods are disjoint and isomorphic as rooted colored structures. Swapping the two components leaves the local data of \((a,b)\) unchanged, hence

\[
\varphi(a,b)\iff\varphi(b,a),
\]

contradiction. \(\square\)

Consequences:

- finitely many named points do not help;
- finitely many arbitrary unary colors do not help;
- crossing the boundary requires more than merely attaching finitely many local labels to the ray.

This is stronger than the previous bounded-successor-definitional-expansion statement.

---

## 8. The value-route theorem survives in typed and one-sorted form

Consider the complete comparison-value layer on distinct generic points:

\[
x\chi y=
\begin{cases}
\Omega_+,&x<y,\\
\Omega_-,&y<x.
\end{cases}
\]

with \(\Omega_+,\Omega_-\) anonymous terminal outputs.

### Typed form

The least generic point has all outgoing off-diagonal comparison values equal to \(\Omega_+\). No point has all outgoing values equal to \(\Omega_-\), because there is no greatest point.

Thus

\[
\operatorname{Positive}(z):=
\exists r\,\forall y\,(y\ne r\to r\chi y=z)
\]

selects \(\Omega_+\), and

\[
x<y\iff x\ne y\wedge x\chi y=\Omega_+.
\]

### One-sorted form

Use the intrinsic predicate \(G(x)\) from Section 5. Define comparison outputs by

\[
C(z):=\exists x\exists y\,
(G(x)\wedge G(y)\wedge x\ne y\wedge T(x,y,z)).
\]

Then define

\[
\operatorname{Positive}(z):=C(z)\wedge
\exists r\Bigl(
G(r)\wedge
\forall y\bigl(G(y)\wedge y\ne r\to T(r,y,z)\bigr)
\Bigr).
\]

Exactly one element satisfies this formula, namely \(\Omega_+\). Therefore

\[
\boxed{
x<y\iff
G(x)\wedge G(y)\wedge x\ne y\wedge
\exists z(\operatorname{Positive}(z)\wedge T(x,y,z)).}
\]

Hence the anonymous-output claim is not an artifact of an externally named output sort.

---

## 9. Repair of the minimality claim: one output already suffices via domain memory

The previous checkpoint correctly stated two-output minimality only inside the **complete-domain terminal-color architecture**. The hostile audit makes the contrasting domain route explicit.

### Construction G∞-D — one-output global domain compilation

Take one terminal output \(\Omega\) and define, for distinct generic points,

\[
\boxed{
x\diamond y=\Omega\iff x<_{\rm ray}y.}
\]

Reverse pairs remain undefined.

Then

\[
\boxed{x<_{\rm ray}y\iff\operatorname{Def}(x\diamond y).}
\]

Thus a single output is sufficient once the operation domain itself is allowed to contain the whole transitive order.

### Exact minimality split

- **domain-memory route:** one terminal output is sufficient and trivially minimal among nonempty output alphabets;
- **complete-domain value-memory route:** one output carries no orientation, while two anonymous outputs suffice on \(\omega\).

Therefore the correct statement is

\[
\boxed{
|O|_{\min}=1\text{ for global order in domain},
\qquad
|O|_{\min}=2\text{ for orientation in values with complete domain}.}
\]

This is a structural distinction, not a contradiction.

---

## 10. Arithmetic Leakage audit: global order is still below ordinary arithmetic

Both order-recovering constructions above add only the information of a discrete linear order:

- G∞-D compiles \(<\) into definedness;
- the complete two-value layer is interdefinable with \(<\) on the generic sort once \(\Omega_+\) is internally recovered.

The associated M0 decorations are finite-copy interpretations over this ordered carrier.

### Theorem HA-5 — addition is not FO-definable from order alone

Ordinary index addition

\[
\operatorname{Add}(x,y,z)\iff x+y=z
\]

is not FO-definable in \((\mathbb N,<)\).

Proof: fix a candidate formula of quantifier rank \(q\). EF theory of linear orders gives a finite threshold \(L=L(q)\) such that intervals longer than \(L\) cannot have their exact lengths distinguished in \(q\) rounds. Choose \(M\gg L\). Compare the pointed tuples

\[
(M,2M,3M)
\]

and

\[
(M,2M,3M+1).
\]

They have the same order type and all corresponding finite gaps relevant to the game exceed \(L\). Hence they are \(q\)-equivalent, while the first satisfies \(x+y=z\) and the second does not. Contradiction. \(\square\)

### Theorem HA-6 — multiplication is not FO-definable from order alone

The same interval argument applies to

\[
(M,M+1,M(M+1))
\]

and

\[
(M,M+1,M(M+1)+1),
\]

for sufficiently large \(M\). Thus ordinary index multiplication is not FO-definable in \((\mathbb N,<)\).

### Consequence

Because the canonical order-memory FCOA structures are interpreted in \((\mathbb N,<)\) using only finitely many tags/copies, neither ordinary external-index addition nor multiplication becomes FO-definable there.

Hence, for the exact enrichments audited here,

\[
\boxed{
\text{FO global order memory}
\quad\not\Rightarrow\quad
\text{FO arithmetic leakage}.}
\]

This strengthens the previous cautious statement “arithmetic does not automatically follow” to a theorem for these canonical constructions.

---

## 11. Logical-strength repair

The safe statement is not a single strict hierarchy

\[
\text{FO}<\text{FO+TC/MSO}<\text{computable}.
\]

Instead record separate facts on the same carrier:

\[
\boxed{
\begin{array}{c|c}
\text{notion} & \text{full order from successor}\
\hline
\text{FO} & \text{no}\\
\text{FO+TC} & \text{yes}\\
\text{MSO} & \text{yes}\\
\text{computable reconstruction of a computable one-ray presentation} & \text{yes}
\end{array}}
\]

FO+TC, MSO, and algorithmic recoverability are different frameworks; no general inclusion claim between the latter logical and algorithmic notions is needed here.

---

## 12. Hostile-audit conclusion

The branch now supports a sharper boundary diagram:

\[
\boxed{
\begin{array}{c}
\text{successor compiled locally into G2 definedness}\\
\Downarrow\\
\text{rigid carrier, but FO cannot take unbounded transitive closure}\\
\Downarrow\\
\text{finite parameters / finite unary colors / bounded local enrichments still fail}\\
\Downarrow\\
\text{global order can enter either through domain (1 output)}\\
\text{or through complete-domain value orientation (2 anonymous outputs)}\\
\Downarrow\\
\text{FO full order recovered, while ordinary }+\text{ and }\times\text{ remain FO-absent.}
\end{array}}
\]

The central research distinction is therefore two-dimensional:

\[
\boxed{
\text{local versus global memory}
\qquad\text{and}\qquad
\text{domain versus value-fiber memory}.}
\]

No finite G4 theorem status is changed by this audit.