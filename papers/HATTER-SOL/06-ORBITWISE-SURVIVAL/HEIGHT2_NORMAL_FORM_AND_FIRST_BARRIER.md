# HATTER-SOL-06 · Height-2 Normal Form and the First Survival Barrier

## 0. Purpose

The compactness programme of HATTER-SOL-06 only becomes relevant after the seed

\[
\tau=(3\ 5)
\]

has actually survived the first nontrivial extension step.

This note isolates that step exactly.

The main conclusion is:

\[
\boxed{
T_2^C(\tau)\ne\varnothing
\iff
\mu_1(S)=\mu_1(\tau S)
\text{ for every height-1 exact support }S.
}
\]

For the transposition \((3\ 5)\), this becomes an infinite family of arithmetic equalities indexed by finite subsets of the remaining Fermat primes.

Thus the pair

\[
X_{\{2,3\}}
\leftrightarrow
X_{\{2,5\}}
\]

is only the **first visible member** of the height-2 balance system, not the whole barrier.

This correction matters: before studying noncompact death, EBFI failure, or Mittag-Leffler attrition at height 2, one must first know that the entire height-2 balance system is satisfied.

---

# 1. Height 0 and height 1

For the directed prime graph

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1,
\]

we have

\[
P_{\le0}=\{2\}.
\]

The height-1 primes are exactly the Fermat primes:

\[
\mathcal F
=
\{f\in\mathbb P:f-1=2^a\text{ for some }a\ge1\}.
\]

Hence

\[
P_{\le1}=\{2\}\cup\mathcal F.
\]

The seed

\[
\tau=(3\ 5)
\]

fixes \(2\) and every Fermat prime other than \(3,5\).

Let

\[
C=C^+(\{3,5\})
\]

be its forward cone.

At height 1,

\[
C\cap P_{\le1}=\{3,5\}.
\]

Therefore the cone-localized extension set at height 1 is the singleton

\[
\boxed{T_1^C(\tau)=\{\tau\}.}
\]

---

# 2. Immediate consequence for Mittag-Leffler attrition

Suppose the seed survives to arbitrarily large finite heights:

\[
T_N^C(\tau)\ne\varnothing
\qquad\forall N\ge1.
\]

Then every restriction

\[
T_N^C(\tau)\to T_1^C(\tau)
\]

has image exactly \(\{\tau\}\).

Thus

\[
A_{N,1}=\{\tau\}
\qquad\forall N\ge1.
\]

## Proposition 2.1

Mittag-Leffler stabilization at height 1 is automatic.

Hence any ML failure for the seed \((3\ 5)\) must occur at a height

\[
\boxed{n\ge2.}
\]

This is the first localization of possible infinite attrition.

---

# 3. Exact supports at height 2

Let

\[
p\in L_2.
\]

Its exact predecessor set is a finite subset

\[
S\subseteq P_{\le1}
\]

such that

\[
2\in S
\]

and

\[
S\cap\mathcal F\ne\varnothing.
\]

Equivalently,

\[
S=\{2\}\cup U,
\]

where \(U\) is a finite nonempty subset of \(\mathcal F\).

Define

\[
X_S
=
\{p\in L_2:\operatorname{Pred}(p)=S\},
\qquad
\mu_1(S)=|X_S|.
\]

The transposition \(\tau\) acts on support sets by swapping membership of \(3\) and \(5\).

---

# 4. Active and inactive height-2 supports

A height-1 support \(S\) is active for the seed iff

\[
S\cap C\ne\varnothing.
\]

Since

\[
C\cap P_{\le1}=\{3,5\},
\]

this is equivalent to

\[
3\in S
\quad\text{or}\quad
5\in S.
\]

There are three cases.

### Case A — neither \(3\) nor \(5\) lies in \(S\)

Then

\[
\tau S=S.
\]

Moreover

\[
X_S\cap C=\varnothing.
\]

Cone-localized extensions fix this whole fiber pointwise.

### Case B — both \(3\) and \(5\) lie in \(S\)

Again

\[
\tau S=S,
\]

but now

\[
X_S\subseteq C.
\]

Any cone-localized height-2 extension may permute \(X_S\) arbitrarily.

### Case C — exactly one of \(3,5\) lies in \(S\)

Then

\[
\tau S\ne S,
\]

and the two supports form a 2-cycle under \(\tau\).

These are the only support orbits that impose a nontrivial multiplicity equality.

---

# 5. Exact height-2 survival criterion

## Theorem 5.1

The seed \(\tau=(3\ 5)\) extends cone-locally to height 2 if and only if

\[
\boxed{
\mu_1(S)=\mu_1(\tau S)
}
\]

for every height-1 support \(S\) containing exactly one of \(3,5\).

### Proof

This is the one-step extension criterion from the Multiplicity Tower Theorem, specialized to \(g=\tau\in G_1\).

If \(S\) contains neither or both of \(3,5\), then

\[
\tau S=S,
\]

so the required equality is tautological.

If \(S\) contains exactly one of \(3,5\), extension requires a bijection

\[
X_S\to X_{\tau S},
\]

which exists exactly when the two fibers have equal cardinality. \(\square\)

---

# 6. Arithmetic normal form of the criterion

Every support containing exactly one of \(3,5\) can be written uniquely as

\[
S_U^{(3)}
=
\{2,3\}\cup U,
\]

or

\[
S_U^{(5)}
=
\{2,5\}\cup U,
\]

where

\[
U\subseteq\mathcal F\setminus\{3,5\}
\]

is finite.

Therefore Theorem 5.1 becomes:

## Corollary 6.1 — full height-2 balance system

\[
\boxed{
T_2^C(\tau)\ne\varnothing
\iff
\mu_1(\{2,3\}\cup U)
=
\mu_1(\{2,5\}\cup U)
}
\]

for every finite

\[
U\subseteq\mathcal F\setminus\{3,5\}.
\]

The first instance

\[
U=\varnothing
\]

is

\[
\boxed{
\mu_1(\{2,3\})
=
\mu_1(\{2,5\}).
}
\]

This is precisely the comparison between the pure 3-side and pure 5-side exact fibers studied in HATTER-SOL-05.

But height-2 survival requires the entire infinite family of equalities, not only this first one.

---

# 7. Arithmetic form of the paired fibers

For finite

\[
U=\{f_1,\dots,f_r\}
\subseteq\mathcal F\setminus\{3,5\},
\]

membership in the two exact fibers means

\[
p-1
=
2^a3^b\prod_{j=1}^r f_j^{e_j}
\]

or

\[
p-1
=
2^a5^b\prod_{j=1}^r f_j^{e_j},
\]

with every displayed exponent positive and with no additional prime divisor of \(p-1\).

Equivalently,

\[
X_{\{2,3\}\cup U}
=
\left\{
1+2^a3^b\prod f_j^{e_j}\in\mathbb P:
 a,b,e_j\ge1
\right\},
\]

and

\[
X_{\{2,5\}\cup U}
=
\left\{
1+2^a5^b\prod f_j^{e_j}\in\mathbb P:
 a,b,e_j\ge1
\right\}.
\]

No further exact-support exclusion condition is needed in these formulas: if the displayed number is prime, then its predecessor set is exactly the set of primes appearing in the factorization of \(p-1\).

Thus the full height-2 problem is a family of paired shifted \(S\)-unit prime-value cardinality problems.

---

# 8. Height-2 extension-space normal form

Assume from now on that the balance system of Corollary 6.1 holds, so

\[
T_2^C(\tau)\ne\varnothing.
\]

We describe every height-2 extension explicitly.

Let \(\mathscr O_2\) be the set of \(\tau\)-orbits of active height-1 supports.

There are two types.

## Type I — fixed active support

These are supports satisfying

\[
\{3,5\}\subseteq S.
\]

For each such support, a height-2 extension chooses an arbitrary permutation

\[
\pi_S\in\operatorname{Sym}(X_S).
\]

## Type II — paired active supports

These are support pairs

\[
\{S,\tau S\}
\]

with exactly one of \(3,5\) in \(S\).

A height-2 extension chooses independently a bijection

\[
\beta_S:X_S\to X_{\tau S}
\]

and a bijection

\[
\gamma_S:X_{\tau S}\to X_S.
\]

There is **no requirement** that

\[
\gamma_S=\beta_S^{-1}.
\]

Indeed the extension need not remain an involution above the seed layer. Its square may act nontrivially inside the two fibers.

Inactive fibers are fixed pointwise.

## Theorem 8.1 — height-2 normal form

Every element of \(T_2^C(\tau)\) is obtained uniquely by making the independent choices above over all active support orbits.

In particular, after choosing one reference bijection on every paired orbit, \(T_2^C(\tau)\) is a torsor for a product of symmetric groups on the active exact fibers.

### Proof

The fibers partition \(L_2\). The lower action \(\tau\) forces an extension to send each fiber \(X_S\) onto \(X_{\tau S}\). Conversely, arbitrary bijections on these fiber blocks, together with \(\tau\) below and the identity on inactive fibers, preserve every edge between \(P_{\le1}\) and \(L_2\), and there are no edges inside \(L_2\). \(\square\)

---

# 9. First important correction to the escape-channel discussion

The earlier first-channel notation

\[
7\mapsto X_{\{2,5\}}
\]

is useful only **after** the full height-2 balance system has been assumed or proved.

The seed can already die before any noncompact phenomenon appears, simply because for some finite

\[
U\subseteq\mathcal F\setminus\{3,5\}
\]

one has

\[
\boxed{
\mu_1(\{2,3\}\cup U)
\ne
\mu_1(\{2,5\}\cup U).
}
\]

Such a mismatch is an ordinary finite-height killing witness for the seed.

Therefore the research tree has a strict logical order:

\[
\boxed{
\begin{array}{c}
\text{(I) establish or refute full height-2 balance;}\\[1mm]
\text{(II) only if balance holds, classify which }g_2\in T_2\text{ survive deeper;}\\[1mm]
\text{(III) only then can ML failure / EBFI failure / noncompact death arise.}
\end{array}
}
\]

---

# 10. What HATTER-SOL-05 already says about the first member

For

\[
U=\varnothing,
\]

HATTER-SOL-05 established strong quantitative asymmetry in the candidate lattices for

\[
\{2,3\}
\quad\text{and}\quad
\{2,5\}.
\]

The local-sieve survival ratio is

\[
\frac32,
\]

and the weighted candidate-count asymptotic ratio is

\[
\frac{3\log5}{2\log3}
\approx2.197460281.
\]

But the cardinality wall remains decisive:

if both exact fibers are infinite, then

\[
\mu_1(\{2,3\})
=
\mu_1(\{2,5\})
=
\aleph_0,
\]

so all quantitative counting asymmetry disappears from the graph-visible multiplicity color.

Thus the known sieve asymmetry does not decide even the first equality in the height-2 balance system.

---

# 11. Why finite-future universality does not solve height 2

Pinned finite-future universality says that finite relative descendant patterns over equal-predecessor vertices can be reproduced by CRT + Dirichlet.

That theorem does not control exact support cardinalities.

The height-2 condition is precisely about exact fibers:

\[
\mu_1(\{2,3\}\cup U)
\stackrel?=
\mu_1(\{2,5\}\cup U).
\]

So finite-future universality and height-2 survival live on opposite sides of the exact-support boundary already identified in HATTER-SOL-04.

No finite named-incidence construction can replace the required exact multiplicity comparison.

---

# 12. A clean first dichotomy

The seed programme therefore begins with the following unconditional dichotomy.

## Theorem 12.1 — first survival dichotomy

Exactly one of the following two situations holds.

### Death at height 2

There exists a finite

\[
U\subseteq\mathcal F\setminus\{3,5\}
\]

such that

\[
\mu_1(\{2,3\}\cup U)
\ne
\mu_1(\{2,5\}\cup U).
\]

Then \((3\ 5)\) does not extend to \(G_2\), hence cannot extend globally.

### Survival to height 2

For every such finite \(U\),

\[
\mu_1(\{2,3\}\cup U)
=
\mu_1(\{2,5\}\cup U).
\]

Then \(T_2^C(\tau)\ne\varnothing\), with the explicit extension-space normal form of Theorem 8.1.

No third possibility exists. \(\square\)

This is the exact first arithmetic fork of HATTER-SOL-06.

---

# 13. The next arithmetic strike

The correct next target is now not yet ML stabilization of \(T_2\) itself.

First we must attack the full balance family

\[
\boxed{
\mu_1(\{2,3\}\cup U)
\stackrel?=
\mu_1(\{2,5\}\cup U)
\qquad
(U\subseteq\mathcal F\setminus\{3,5\}\text{ finite}).
}
\]

There are two possible wins.

### Rigidity win

Find one explicit finite \(U\) with unequal cardinalities. Then the seed dies already at height 2.

### Survival win

Prove the equality for all finite \(U\). Then height-2 survival is established and the compactness machinery of HATTER-SOL-06 becomes genuinely active.

At present neither direction is proved here.

The simplest unresolved case remains

\[
U=\varnothing,
\]

namely

\[
\mu_1(\{2,3\})
\stackrel?=
\mu_1(\{2,5\}).
\]

But the series must now remember that this is the first member of an infinite balance system.

---

# 14. Status

This strike establishes:

1. \(T_1^C((3\ 5))\) is a singleton;
2. ML stabilization at height 1 is automatic;
3. any ML failure must begin at height at least 2;
4. the exact necessary-and-sufficient height-2 survival criterion;
5. the full arithmetic balance family indexed by finite subsets of the remaining Fermat primes;
6. an explicit normal form for every cone-localized height-2 extension;
7. the correction that the channel \(7\to X_{\{2,5\}}\) is meaningful only after the full height-2 balance condition is met;
8. the exact first dichotomy: finite height-2 killing witness versus complete height-2 balance.

The next strike should attack the paired shifted-\(S\)-unit families

\[
1+2^a3^b\prod_{f\in U}f^{e_f}
\qquad\text{and}\qquad
1+2^a5^b\prod_{f\in U}f^{e_f}
\]

for strategically chosen small \(U\), looking first for a **finite/empty versus infinite/nonempty cardinality separation**, since asymptotic-density differences alone are invisible once both fibers are countably infinite.
