# Second Strike — The M=4 Recurrence Barrier

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-29  
**Status:** proved reduction + externally verified open-number-theory barrier

## 1. The binary prime-residue word

Ignore the exceptional prime `2` and enumerate odd primes

\[
q_0=3,q_1=5,q_2=7,\ldots.
\]

Define

\[
w_4(n)=
\begin{cases}
0,&q_n\equiv1\pmod4,\\
1,&q_n\equiv3\pmod4.
\end{cases}
\]

The successor-enriched Prime-Status Quotient with mod-4 phase is effectively mutually interpretable with the weak monadic theory of the labelled chain `(N,Succ,w_4)`.

## 2. Cylinder recurrence is already visible to the theory

For every finite binary word

\[
u=u_0u_1\cdots u_{k-1}\in\{0,1\}^k,
\]

let `Occ_u(n)` assert that the length-`k` block of `w_4` beginning at `n` is exactly `u`.

Because `k` is fixed, `Occ_u(n)` is first-order definable from successor and the colour predicates.

The sentence

\[
\forall x\,\exists y\,(x<y\land Occ_u(y))
\]

therefore says exactly that `u` occurs arbitrarily far out, equivalently infinitely often.

Thus any decision procedure for the full WMSO/MSO theory of `w_4` would in particular decide, for every finite residue word `u`, whether `u` occurs infinitely often among consecutive primes modulo 4.

## 3. What is known unconditionally

### Constant words

Shiu proved that for every modulus `q`, every reduced residue class `a`, and every length `k`, there are arbitrarily long strings of consecutive primes all congruent to `a mod q`.

For `q=4`, both

\[
0^k\quad\text{and}\quad1^k
\]

occur infinitely often for every fixed `k`.

### Length two for phi(q)=2

For a modulus with exactly two reduced residue classes, in particular `q=4`, all four length-two residue patterns occur infinitely often. This follows for the mixed transitions from Dirichlet together with the infinite occurrence of constant runs; it is also recorded in the modern literature on consecutive residue patterns.

## 4. What is not known

The general assertion

\[
\forall u\in\{0,1\}^{<\omega},
\quad u\text{ occurs infinitely often in }w_4
\]

is not currently known unconditionally.

Modern work on residue-class patterns of consecutive primes explicitly treats the general prescribed-pattern problem as open beyond special families. Random/Hardy-Littlewood models predict equidistribution of every fixed pattern, but this is conjectural rather than an unconditional theorem.

Therefore the exact monadic theory problem for `w_4` reaches a genuine analytic-number-theory frontier almost immediately.

## 5. Formal barrier theorem for the programme

### Theorem (recurrence-query lower bound)

If `Th_WMSO(w_4)` is decidable, then there is an algorithm which, on input any finite binary word `u`, decides whether the corresponding residue pattern occurs infinitely often among consecutive odd primes modulo 4.

### Proof

Construct effectively the WMSO sentence

\[
\rho_u:=\forall x\,\exists y\,(x<y\land Occ_u(y)).
\]

A decision procedure for `Th_WMSO(w_4)` decides the truth of `rho_u`. By construction, `rho_u` is true exactly when `u` occurs arbitrarily far out, hence infinitely often. QED.

This theorem does **not** prove undecidability. It proves that an unconditional decidability theorem must contain, or bypass in a genuinely nontrivial way, an effective solution of a family of prime-pattern recurrence questions currently beyond known unconditional distribution results.

## 6. Semenov corridor

For fixed infinite words, classical Semenov-type characterisations reduce decidability of the monadic theory to recursiveness of the word plus an effective recurrence indicator. The prime word `w_4` is recursive: one can enumerate primes and compute residues modulo 4.

Hence the hard component is exactly the recurrence side, not computability of the word itself.

The programme should therefore distinguish:

1. **computable phase:** `w_4` can be generated effectively;
2. **local proven recurrence:** constant runs, all two-letter patterns;
3. **general finite-pattern recurrence:** open;
4. **effective regular-factor recurrence indicator:** stronger still, and the natural target for the full monadic-theory question.

## 7. Consequence for the Prime Corridor

The previous corridor

\[
P_0\to P_M\to P_M+R_2\to\cdots\to P_0+PSucc
\]

can now be sharpened.

`P_0+PSucc` is a tame decidable WS1S layer.

But adding the arithmetic phase `p mod 4` converts the harmless abstract chain into the concrete number-theoretic word `w_4`. The obstruction is not merely that this word is nonperiodic. It is that its finite-pattern recurrence spectrum is only partially understood.

So the first genuine arithmetic frontier is

\[
\boxed{\text{abstract successor}+\text{arithmetic colour alignment}.}
\]

This is stronger and more precise than saying that either successor or finite phase alone is dangerous.

## 8. Publication assessment after the second strike

This strengthens the branch considerably, but publication is still held.

Reasons:

- the algebraic reduction is now stable;
- the exact external barrier has been identified;
- but a standalone article would be stronger if we either derive a useful conditional theorem (e.g. under a standard prime-pattern conjecture) or obtain a structural theorem showing what arithmetic relations still cannot be defined even assuming maximal finite-pattern recurrence.

**Current verdict:** preserve in GitHub; continue research; do not assemble Zenodo manuscript yet.
