# HATTER-SOL-04 · RESEARCH STATE

## Working title

**«Чашка забывает кратности: достаточно ли `rad(p-1)` для жёсткости?»**

English working title:

**“The Cup Forgets Multiplicities: Is `rad(p-1)` Enough for Rigidity?”**

## Starting object

The fourth HATTER-SOL line begins from the unresolved frontier isolated in HATTER-SOL-03.

Let

\[
R_{\mathbb P}(r,p)
\iff
p\in\mathbb P
\text{ and }
r=\operatorname{rad}(p-1),
\]

and consider

\[
\mathcal R
=
(\mathbb N_{>0},\times,R_{\mathbb P}).
\]

Equivalently, on the prime generators define the directed graph

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

The central problem is

\[
\boxed{
\operatorname{Aut}(\mathcal R)
\stackrel{?}{=}
\{\mathrm{id}\}.
}
\]

In words: after exact multiplicities in the factorization of \(p-1\) are erased, does the global directed support network still recover enough individuality to make every prime fixed?

---

# First strike summary

The first strike does **not** force a premature yes/no answer. Instead it isolates the exact location of the difficulty.

Three facts are now proved.

## A. Radical structure = directed prime graph

Every automorphism of the multiplicative monoid is induced by a permutation of the prime generators, and preservation of \(R_{\mathbb P}\) is equivalent to preservation of the directed relation \(D(q,p)\iff q\mid p-1\). Therefore

\[
\boxed{
\operatorname{Aut}(\mathcal R)
\cong
\operatorname{Aut}(\Pi).
}
\]

So HATTER-SOL-04 is exactly an automorphism problem for the directed prime-support graph.

## B. The finite future is generic

Given a finite set of already chosen primes \(F\) and any admissible subset \(U\subseteq F\), there are infinitely many new primes \(p\) such that

\[
\operatorname{Pred}(p)\cap F=U.
\]

The only unavoidable condition is that if \(2\in F\), then \(2\in U\), since every odd prime has \(2\mid p-1\).

This follows directly from the Chinese remainder theorem plus Dirichlet's theorem.

Thus **every finite one-sided future incidence pattern is reproducible**.

This is closely related to the classical finite-universality constructions in the directed prime graph and to Jones's Rado-graph shadow result. The formulation here is used to isolate the rigidity mechanism, not to claim novelty for CRT/Dirichlet itself.

## C. The obstruction lives in exact predecessor fibers

For a finite set of primes \(S\), define

\[
X_S
=
\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Equivalently,

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:
 e_q\ge1
\right\}.
\]

So \(\mu(S)\) is a shifted \(S\)-smooth-prime multiplicity.

The first fiber is already

\[
X_{\{2\}}
=
\{\text{Fermat primes}\}.
\]

Hence exact extension of a symmetry is controlled by arithmetic multiplicity data that are not reduced to finite CRT patterns.

---

# New conceptual split

The first strike produces the central dichotomy for HATTER-SOL-04:

\[
\boxed{
\text{finite future pattern}
\Longrightarrow
\text{generic / freely reproducible}
}
\]

but

\[
\boxed{
\text{exact full predecessor fiber}
\Longrightarrow
\text{shifted-smooth prime arithmetic}.
}
\]

The support-only rigidity problem therefore does **not** fail because finite future patterns are too rigid. Quite the opposite: the finite future is maximally flexible. Any rigidity must be carried by the exact global pattern of which predecessor fibers exist and with what multiplicities.

---

# Structural target

The immediate next theorem is a full **multiplicity-tower description** of the automorphism group by Pratt height.

Let

\[
L_n=\{p:h(p)=n\},
\qquad
P_{\le n}=\bigcup_{j\le n}L_j,
\]

where \(h\) is Pratt height.

The expected exact recursion is:

- an automorphism on \(P_{\le n}\) extends to level \(n+1\) exactly when it preserves all multiplicities \(\mu(S)\) of predecessor fibers at that level;
- the kernel of restriction at the next level is the product of symmetric groups on the fibers \(X_S\);
- the full automorphism group is the inverse limit of this restriction tower.

This converts the radical-predecessor question into a precise survival problem:

> does any nontrivial permutation inside an equal-predecessor fiber survive all higher multiplicity constraints?

That is the next strike.

## Publication threshold

Not reached. HATTER-SOL-04 has a clear object and a first structural theorem package, but the branch remains in research phase until the multiplicity tower is proved and at least one genuine rigidity/non-rigidity consequence is extracted from it.
