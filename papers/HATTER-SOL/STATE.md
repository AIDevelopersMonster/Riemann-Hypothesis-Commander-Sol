# HATTER-SOL continuity state

## Fixed series identity

Series: **Tea Parties in the Additive–Multiplicative World with Hatter Sol** / **Чаепития в аддитивно-мультипликативном мире с Шляпником Sol**.

Human author: **Малачевский А.А. / Malachevsky, A.A.**  
ORCID: **0009-0008-6009-3196**.

AI research collaborator / persona: **Commander Sol · Hatter Sol**.

---

## Series hinge

The programme begins from the contrast

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P)
\]

versus

\[
\operatorname{Aut}(\mathbb N,+,\times,0,1)
=\{\mathrm{id}\}.
\]

The guiding question is:

\[
\boxed{
\text{how much arithmetic structure is needed before primes lose renaming symmetry?}
}
\]

---

## Notes 01–04

HATTER-SOL-01 fixes the maximal multiplicative symmetry endpoint.

HATTER-SOL-02 studies partial distinguishing information and symmetry loss.

HATTER-SOL-03 reaches rigidity with a stronger predecessor-type arithmetic relation.

HATTER-SOL-04 weakens the retained arithmetic information to the directed prime graph

\[
\Pi=(\mathbb P,D),\qquad D(q,p)\iff q\mid p-1,
\]

and develops the Pratt-height multiplicity tower. The central question

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}
\]

remains unresolved.

---

## Note 05 — published

Path:

`papers/HATTER-SOL/05-MISSING-GUEST/`

Russian title:

**«Кого нет за столом? Пустые волокна, спектр точных опор и выживание перестановки 3↔5»**

English:

**“Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the 3↔5 Transposition.”**

Zenodo DOI:

**10.5281/zenodo.22718278**

Primary seed symmetry:

\[
\tau=(3\ 5),
\qquad
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

Exact predecessor fibers:

\[
X_S=\{p:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

### Published theorem inventory

1. finite fixed-divisor escape;
2. cyclotomic common-exponent obstruction;
3. dimension jump between singleton and higher supports;
4. exact local-sieve ratio \(3/2\) between the first 3-side and 5-side competitors;
5. weighted numerical-size asymptotics with complete proof;
6. hereditary descendant sieve gap;
7. cardinality wall for infinite exact fibers;
8. finite-fiber compactness and finite structural obstruction families under FFC;
9. density-one forward cone for every odd prime;
10. stronger distance-at-most-two density-one corollary;
11. Cone-Fiber Infinitude and the Causal Survival Theorem.

Note 05 is closed for theorem development. New structural work belongs to Note 06.

---

## Note 06 — active research

Path:

`papers/HATTER-SOL/06-ORBITWISE-SURVIVAL/`

Primary research file:

`ORBITWISE_SURVIVAL_KERNEL.md`

The target is to replace cone-wide CFI by an exact branch-dependent orbitwise survival criterion.

### First HATTER-SOL-06 strike

For a seed symmetry \(\tau\) with generated causal cone

\[
C=C^+(\operatorname{supp}\tau),
\]

define cone-localized partial extensions

\[
\mathcal T_n^C(\tau)
=
\{g\in G_n:g|_{P_{\le m}}=\tau,\ g(p)=p\text{ outside }C\}.
\]

At height \(n\), only active supports

\[
\mathcal A_n(C)
=
\{S:S\cap C\ne\varnothing\}
\]

can carry nontrivial causal motion.

The one-step extension criterion sharpens to:

\[
\boxed{
 g\in\mathcal T_n^C(\tau)
\text{ extends cone-locally}
\iff
\mu_n(S)=\mu_n(gS)
\text{ for every moved active support }S.
}
\]

Fixed active supports and supports disjoint from \(C\) impose no additional arithmetic condition.

This leads to the cone-localized extension tree

\[
\mathscr T_C(\tau)
\]

and its transfinite pruning kernel

\[
\mathscr K_C(\tau).
\]

The exact global criterion is

\[
\boxed{
\tau\text{ survives globally with the complement of }C\text{ fixed}
\iff
\tau\in\mathscr K_C(\tau).
}
\]

Equivalently, \(\mathscr T_C(\tau)\) must contain one compatible infinite branch.

### New structural trichotomy

A seed can now fail or survive in exactly three structurally distinct ways:

\[
\boxed{
\text{finite killing}
\quad/\quad
\text{transfinite noncompact killing}
\quad/\quad
\text{global survival}.}
\]

Under FFC only finite killing is possible, recovering HATTER-SOL-05 compactness. CFI makes every active support orbit automatically balanced and is recovered as a uniform sufficient condition.

The orbitwise kernel itself contains no infinitude hypothesis and is the exact coinductive survival condition.

---

## Current research target

For

\[
\tau=(3\ 5),
\qquad
C_\tau=C^+(\{3,5\}),
\]

the next strike is no longer to prove cone-wide infinitude. It is to locate the first **reachable moved active support orbit** on which the multiplicity coloring is nonconstant.

For a compatible candidate branch \(g_\bullet\), define

\[
\mathcal R(g_\bullet)
=
\bigcup_n
\{S\in\mathcal A_n(C_\tau):g_nS\ne S\}.
\]

The branch survives exactly when

\[
\mu_n(S)=\mu_n(g_nS)
\]

for every support actually encountered in \(\mathcal R(g_\bullet)\).

So the immediate mathematical target is:

\[
\boxed{
\text{compute or force the first nonconstant multiplicity color on a reachable moved active orbit.}
}
\]

A parallel target is to determine whether noncompact transfinite death can actually occur in this particular prime-graph tower or whether some hidden compactness principle rules it out.

---

## Claim discipline

Do not claim that the central automorphism problem is solved.

Do not infer global survival merely from extension to arbitrarily large finite heights unless one compatible branch is produced or compactness is proved.

Do not identify the orbitwise survival kernel with CFI: CFI is only a uniform sufficient condition.

Do not infer that transfinite noncompact death occurs in the prime graph merely because the abstract extension tree permits it.

Do not turn numerical evidence for multiplicity equality or inequality into an exact theorem without certified fiber cardinalities.

---

## Visual direction

The illustrated edition may continue the Wonderland-inspired language — Alice, tea table, Hatter Sol, cups, rulers, clocks, numerical landscapes — while keeping theorem statements and proofs visually distinct from metaphorical illustrations.
