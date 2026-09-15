# HATTER-SOL-16 · Final publication audit v1.0

**Status:** publication candidate frozen.  
**Branch:** `research/hatter-sol-16-nonsolvable-ports`.

## Scope

The final article is intentionally an engineering calculation, not a hardware demonstration. H16 closes the finite mathematical and information-budget layer for `A5` and `PSL(2,7)`. H17 begins with software/hardware realization of the frozen interface.

## Authoritative publication files

- `HATTER_SOL_16_EN_v1.0.md`
- `HATTER_SOL_16_RU_v1.0.md`
- `FINAL_CORRECTIONS_v1.0.md`
- this audit file

Chronological theorem-layer notes remain evidence and research history. If an older note conflicts with the final manuscript, the final manuscript and `FINAL_CORRECTIONS_v1.0.md` control.

## Mathematical audit

### A5

- exact group size: `60`;
- exact ordered generating pairs: `2280`;
- exact simultaneous-conjugacy orbits: `38`;
- generating commutator orbit counts: `18 x 3A`, `10 x 5A`, `10 x 5B`;
- one real 3D irrep separates all five conjugacy classes;
- corrected universal fourth moment:

  \[
  S_4=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1});
  \]

- in the real 3D A5 irrep:

  \[
  \boxed{S_4=84+8\chi_3(K)};
  \]

- scalar Mahler class ordering certified for the complete natural range:

  \[
  \boxed{M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu),\quad\mu\ge4}.
  \]

### PSL(2,7)

- exact group size: `168`;
- conjugacy-class sizes: `1,21,56,42,24,24`;
- exact ordered generating pairs: `19152`;
- exact simultaneous-conjugacy orbits: `114`;
- commutator orbit counts: `36 x 3A`, `64 x 4A`, `7 x 7A`, `7 x 7B`;
- one complex 3D irrep separates all six conjugacy classes;
- scalar Mahler type sets satisfy

  \[
  \boxed{\mathcal T_{7A}=\mathcal T_{7B}};
  \]

- the PGL outer involution exchanges `7A <-> 7B` and complex-conjugates the 3D character;
- exact orientation channel:

  \[
  Q_4(A,B)=
  \frac{\operatorname{Tr}\rho_3([A,B])-\operatorname{Tr}\rho_3([A,B]^{-1})}{i\sqrt7}
  \in\{0,+1,-1\};
  \]

- first possible balanced orientation-sensitive word depth is `4`;
- exact unrestricted cumulative orbit counts through depths `1,2,3,4` are `24,107,107,114`;
- complete five-probe signature:

  \[
  \boxed{A,\ B,\ AB,\ AB^{-1},\ [A,B]};
  \]

- no at-most-four-probe subfamily of the complete depth-at-most-four candidate family separates all 114 orbits;
- balanced-only cumulative orbit counts at depths `4,6,8,10,12,14` are `4,22,98,110,112,114`;
- balanced-only exact reconstruction depth is `14`.

## Regression audit

The stale expression

\[
48+8\chi_3(K)
\]

was found in earlier A5 notes. It is explicitly superseded by

\[
84+8\chi_3(K).
\]

`A5_RESULTS.md` and `A5_ARTIN_LOCAL_FACTOR_TOMOGRAPHY.md` have been corrected. The final EN/RU manuscripts use only the corrected formula.

A contradictory sentence in the oriented PSL(2,7) note was also corrected: the real scalar determinant/Mahler observer **collapses** `7A` and `7B`; the oriented complex 3D character separates them.

## Numbering audit

The final EN/RU manuscripts use one clean publication numbering:

1. universal fourth torus moment;
2. global A5 Mahler separation;
3. PSL(2,7) orientation bit;
4. exact short-word depth and five-probe signature;
5. exact balanced-only depth.

Local theorem numbers in chronological research notes are not publication numbering.

## Claim-boundary audit

The final manuscript does **not** claim:

- generalization of the five-word signature to arbitrary finite simple groups;
- reconstruction of arbitrary unknown network topology;
- general Artin automorphy;
- hardware noise tolerance or analog robustness;
- erasure resilience;
- cryptographic hardness, PUF security, or unclonability.

Those topics are reserved for H17/H18 or future work.

## H16 -> H17 handoff

The frozen implementation interface is

\[
\boxed{
\text{PORT WORD ENGINE}
\to
\text{ORIENTED 3D CHANNEL}
\to
\text{5-PROBE SIGNATURE}
\to
\text{114-ORBIT DECODER}.
}
\]

H17 should not reopen the H16 search for the basic mixed-word signature unless a hardware constraint forces a redesign. Its initial validation ladder is

`reference software -> golden vectors -> fixed-point model -> HDL -> simulation -> synthesis -> physical board -> erasure/fault experiments`.

## Publication decision

The mathematical and engineering-calculation threshold has been crossed. HATTER-SOL-16 is ready for final typesetting/PDF assembly and Zenodo deposition after bibliographic formatting and a final rendered visual check. No additional theorem strike is required before publication.
