# FCOA-Z — Terminal Cost-Memory Duality 0.2

**Date:** 2026-08-31  
**Status:** CORRECTED PROVED CORE / SUPERSEDES 0.1  
**Supersedes:** `TERMINAL_COST_MEMORY_DUALITY_0_1.md`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Hostile-audit correction

Version 0.1 contained one scope error in the extremal-selector wording.

For a fixed finite window \(W_N\), the value of a global profile outside \(W_N\) does not affect \(C_N\) or \(M_N\). Therefore global `share` is not the unique **global** minimizer of one fixed \(C_N\), and global `split` is not the unique **global** maximizer of one fixed \(M_N\).

The correct statements are:

1. on the visible restriction \(\mathcal I_N\), the all-share restriction uniquely minimizes \(C_N\);
2. on the visible restriction \(\mathcal I_N\), the all-split restriction uniquely maximizes \(M_N\);
3. global `share` is the unique global profile minimizing \(C_N\) simultaneously for every \(N\);
4. global `split` is the unique global profile maximizing \(M_N\) simultaneously for every \(N\).

All cost-memory identities remain unchanged.

---

## 2. Finite windows and orbit count

For

\[
W_N=\{x_0\}\cup\{x_n^+,x_n^-:1\le n\le N\},
\]

the terminal-producing reflection-orbit indices are:

\[
(+,n),\quad 1\le n\le N,
\]

\[
(*,n),\quad 2\le n\le N,
\]

\[
(\times,n),\quad 2\le n\le N.
\]

Hence, for \(N\ge2\),

\[
\boxed{Q_N=3N-2,}
\]

and \(Q_1=1\).

---

## 3. Cost and memory

For a global profile

\[
\epsilon:\mathcal I\to\{0,1\},
\]

define the finite-window mirror-extension cost

\[
C_N(\epsilon)=\sum_{q\in\mathcal I_N}\epsilon(q),
\tag{3.1}
\]

and the finite-window branch-memory score

\[
M_N(\epsilon)=\sum_{q\in\mathcal I_N}\epsilon(q).
\tag{3.2}
\]

The interpretation is:

- each shared orbit adds zero new reflected outputs and preserves zero terminal branch distinctions;
- each split orbit adds one fresh reflected output and preserves one terminal branch distinction.

### Theorem 3.1 — Exact Cost-Memory Duality

For every global orbitwise canonical profile \(\epsilon\) and every \(N\ge1\),

\[
\boxed{C_N(\epsilon)=M_N(\epsilon).}
\tag{3.3}
\]

### Proof

Both sides equal the number of split terminal-producing reflection orbits visible in \(W_N\). \(\square\)

---

## 4. Correct finite-window extremal theorem

Let

\[
\epsilon|_{\mathcal I_N}
\]

be the visible restriction of the global profile.

### Theorem 4.1 — Visible Minimal-Cost Selector

Among profiles on the finite index set \(\mathcal I_N\), the unique minimizer of \(C_N\) is the all-zero restriction:

\[
\boxed{
\epsilon(q)=0\quad\forall q\in\mathcal I_N.
}
\tag{4.1}
\]

The minimum is

\[
\boxed{C_N=0.}
\]

### Proof

Equation (3.1) is a sum of binary nonnegative terms. It vanishes exactly when every visible term is zero. \(\square\)

### Theorem 4.2 — Visible Maximal-Memory Selector

Among profiles on \(\mathcal I_N\), the unique maximizer of \(M_N\) is the all-one restriction:

\[
\boxed{
\epsilon(q)=1\quad\forall q\in\mathcal I_N.
}
\tag{4.2}
\]

The maximum is

\[
\boxed{M_N=Q_N.}
\]

### Proof

Equation (3.2) is a sum of \(Q_N\) binary terms and attains \(Q_N\) exactly when every visible term equals one. \(\square\)

---

## 5. Correct global extremal theorem

### Theorem 5.1 — Global Simultaneous Minimality

A global profile \(\epsilon\) satisfies

\[
C_N(\epsilon)=0
\quad\text{for every }N\ge1
\]

if and only if \(\epsilon\) is global `share`.

### Proof

The forward direction: every terminal orbit \(q\in\mathcal I\) appears in some finite \(\mathcal I_N\). If all \(C_N\) vanish, Theorem 4.1 forces \(\epsilon(q)=0\) for every orbit. Thus \(\epsilon\) is global share. The converse is immediate. \(\square\)

### Theorem 5.2 — Global Simultaneous Maximality

A global profile \(\epsilon\) satisfies

\[
M_N(\epsilon)=Q_N
\quad\text{for every }N\ge1
\]

if and only if \(\epsilon\) is global `split`.

### Proof

Every orbit appears in some finite window. Simultaneous maximality forces every visible bit to one in every window, hence every global bit is one. The converse is immediate. \(\square\)

Thus the correct global selector statement is

\[
\boxed{
\text{simultaneous all-window cost minimization}\Rightarrow ZM0\text{-share},
}
\]

\[
\boxed{
\text{simultaneous all-window memory maximization}\Rightarrow ZM0\text{-split}.
}
\]

---

## 6. Infinite cardinality warning

Both global terminal universes are countably infinite:

\[
|E_{share}|=|E_{split}|=\aleph_0.
\]

Therefore ordinary infinite cardinality does not select one endpoint.

The relevant resource is finite-window incremental cost, not bare infinite size.

---

## 7. Density version

For \(N\ge2\), let

\[
c_N(\epsilon)=\frac{C_N(\epsilon)}{Q_N},
\qquad
m_N(\epsilon)=\frac{M_N(\epsilon)}{Q_N}.
\]

Then pointwise

\[
\boxed{c_N(\epsilon)=m_N(\epsilon).}
\]

Hence any limsup, liminf, or actual limit of one normalized sequence equals the corresponding quantity for the other.

For the global endpoints:

\[
(c_N,m_N)_{share}=(0,0),
\]

\[
(c_N,m_N)_{split}=(1,1)
\]

for every \(N\).

---

## 8. Exact tradeoff set on one window

For a fixed \(N\), every integer

\[
0\le k\le Q_N
\]

is realized by choosing exactly \(k\) visible split orbits. Therefore the aggregate attainable set is exactly

\[
\boxed{
\{(C_N,M_N)=(k,k):0\le k\le Q_N\}.
}
\tag{8.1}
\]

When the optimization directions are “minimize cost” and “maximize memory”, every different value of \(k\) lies on the exact one-for-one tradeoff frontier: reducing cost necessarily removes the same number of branch-separated terminal orbits.

---

## 9. Weighted version

For positive channel weights \(w_+,w_*,w_\times\), define

\[
C_N^w(\epsilon)
=
\sum_{q=(\alpha,n)\in\mathcal I_N}w_\alpha\epsilon(q),
\]

\[
M_N^w(\epsilon)
=
\sum_{q=(\alpha,n)\in\mathcal I_N}w_\alpha\epsilon(q).
\]

Then

\[
\boxed{C_N^w(\epsilon)=M_N^w(\epsilon)}
\]

for every profile and every finite window.

---

## 10. Correct selector-conflict statement

### Theorem 10.1

Within the canonical orbitwise lift class:

1. all-window cost minimization uniquely selects global `share`;
2. all-window branch-memory maximization uniquely selects global `split`;
3. on every finite window, the corresponding visible restrictions are opposite unique extrema.

### Proof

Theorems 4.1, 4.2, 5.1, and 5.2. \(\square\)

Thus the structural conflict survives hostile audit; only the uniqueness quantifier required correction.

---

## 11. Dimensional status

All windows lie on the already published one-dimensional signed line, and terminal outputs remain terminal.

\[
\boxed{c_{coord}=0.}
\]

No spatial interpretation is introduced.
