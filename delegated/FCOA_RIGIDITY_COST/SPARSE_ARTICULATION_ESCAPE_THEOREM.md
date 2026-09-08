# FCOA Rigidity Cost — Sparse-Articulation Escape Theorem

**Status:** post-publication theorem note.

## 1. Setup
Assume

\[
\beta(D,c)=1.
\]

Let `e` be an anchored beta-killing missing cell. Let

\[
t=t_D(e)
\]

be the number of old connected components of `Lambda(D)` touched by `e`.

For an old cell `p in D`, define

\[
\Delta_D(p)=\kappa(\Lambda(D\setminus\{p\}))-\kappa(\Lambda(D)).
\]

Let

\[
N_j(D)=|\{p\in D:\Delta_D(p)\ge j\}|.
\]

Recall the replacement multiplicity

\[
m_D(e)=|\{p\in D:D-\{p\}+\{e\}\cong D\}|.
\]

Let

\[
A_e=\{a\in\operatorname{Aut}(G;D):a(e)=e\}
\]

and

\[
H_e=\{a\in A^+(D,c):a(e)=e\}.
\]

## 2. Sparse-articulation multiplicity bound
From the Component Compensation Theorem, every replacement target `p` satisfies

\[
\Delta_D(p)\ge t-2.
\]

If the touch of `e` on every old component is robust relative to the replacement target, then

\[
\Delta_D(p)\ge t-1.
\]

Therefore

\[
\boxed{m_D(e)\le N_{t-2}(D)}
\]

in general, and

\[
\boxed{m_D(e)\le N_{t-1}(D)}
\]

under robust touch.

## 3. Sparse-Articulation Escape Theorem

### Theorem 3.1
Assume `e` is robustly anchored to `t>=2` old incidence components and

\[
\boxed{N_{t-1}(D)\le1.}
\]

If, in addition,

\[
\boxed{A_e=H_e,}
\]

then

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

### Proof
The robust component-compensation bound gives

\[
m_D(e)\le N_{t-1}(D)\le1.
\]

Since `A_e=H_e`, the stabilizer-splitting factor is

\[
s(e)=[A_e:H_e]=1.
\]

Hence the weighted replacement capacity satisfies

\[
w(e)=m_D(e)s(e)\le1.
\]

Persistent Exclusion shows that a fatal anchored beta-killing cell requires at least two distinct color-specific replacement cosets, so necessarily `w(e)>=2`. Contradiction. Therefore at least one binary color on `e` is exact. Since beta=1, alpha=1. `square`

## 4. Zero-articulation corollary

### Corollary 4.1
If `e` robustly touches at least two old components and

\[
N_{t-1}(D)=0,
\]

then

\[
\boxed{m_D(e)=0}
\]

and both colors on `e` are free of domain-moving replacement symmetries. Hence

\[
\boxed{\alpha=\beta=1}
\]

without any stabilizer hypothesis.

In particular, if every component of `Lambda(D)` is 2-vertex-connected and `e` robustly touches two distinct old components, then `e` is automatically an exact beta-one repair.

## 5. Unique-target dichotomy

### Theorem 5.1
Let `e` be an anchored beta-killing cell with

\[
\boxed{m_D(e)\le1.}
\]

Then exactly one of the following holds:

1. some color on `e` is exact, so `alpha=beta=1`;
2. `e` is split-fatal, there is a unique replacement target `p`, and
   \[
   \boxed{[A_e:H_e]\ge2.}
   \]

### Proof
Persistent fatality is impossible by Persistent Exclusion. If both colors are unsafe, they must therefore be defeated by two distinct replacement `H_e`-cosets. Since `m_D(e)<=1`, all replacement symmetries have the same unique target `p`. Hence the two color-specific cosets lie over that same target. The number of `H_e`-cosets over one target is at most `[A_e:H_e]`, so at least two such cosets force the displayed inequality. `square`

Thus a unique replacement target is not by itself dangerous; fatality additionally requires genuine stabilizer splitting.

## 6. One-articulation corollary

### Corollary 6.1
Suppose `Lambda(D)` has at most one articulation cell in total. If there exists a robustly two-component anchored beta-killing cell `e` such that

\[
A_e=H_e,
\]

then

\[
\boxed{\alpha=\beta=1.}
\]

This covers the broad class of sparse domains whose incidence components are articulation-poor.

## 7. Higher-touch strengthening
If `e` robustly touches `t>=3` old components, then a replacement target must satisfy

\[
\Delta_D(p)\ge t-1\ge2.
\]

Hence only high-order cut cells can support replacement danger. If there is at most one such high-order cut cell and `A_e=H_e`, Theorem 3.1 applies.

Therefore increasing the number of phase components joined by one killing cell makes replacement danger increasingly concentrated on rare high-separation cells.

## 8. Counterexample profile
A counterexample to

\[
\beta=1\Longrightarrow\alpha=1
\]

must now satisfy the following for every robust multi-component anchored beta-killing orbit:

- either at least two articulation-compatible replacement targets exist;
- or a unique target exists but stabilizer splitting satisfies
  \[
  [A_e:H_e]\ge2.
  \]

Equivalently, every such orbit must pay replacement complexity either in **target multiplicity** or in **same-target transporter multiplicity**.

This is sharper than the scalar condition

\[
m_D(e)[A_e:H_e]\ge2
\]

because it identifies the two geometrically distinct ways the threshold can be reached.

## 9. Articulation–Killing programme
The remaining hard sector is articulation-rich in a precise sense. To defeat every robust multi-component killing cell, the domain must supply enough cells with large deletion defect `Delta_D(p)`, or else enough non-phase-zero stabilizer structure over the few available targets.

The next target is therefore a dichotomy theorem:

> high articulation multiplicity should force additional beta-killing bridge cells, while high same-target stabilizer splitting should force a new old phase obstruction or another safe orbit.

Either branch would push toward the global beta-one theorem.

## Claim firewall
1. The sparse-articulation theorem is sufficient, not necessary.
2. Robust touch is required for the stronger `N_{t-1}` bound.
3. Same-target split fatality is known to occur, so the condition `A_e=H_e` cannot be dropped naively.
4. No global proof of `beta=1 => alpha=1` is claimed.