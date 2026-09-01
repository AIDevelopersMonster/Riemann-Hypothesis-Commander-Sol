# FCOA Hybrid Memory — Resolution–Transport Phase Boundary

**Status:** SUPERSEDED AS AN INTRINSIC PHASE PROFILE  
**Article B:** historical/direct-CRT normal-form result only

## Surviving theorem: flat direct-CRT capacity

For a flat presentation with `k` pairwise-coprime residue channels of sizes `m_1,...,m_k`, complete local binary tables, and total table cost

\[
\sum_i m_i^2\le C N,
\]

AM--GM gives

\[
\prod_i m_i\le (CN/k)^{k/2}.
\]

If exactness is tested directly by congruences for a defect `E` with `|E|=O(N^d)`, the product modulus must dominate the possible nonzero defect. In this **direct flat CRT template**, the required resolution exponent is therefore at least `d`.

This correctly explains the exhibited constructions:

- direct CRT addition: defect degree `1`, two `Theta(sqrt N)` channels suffice;
- direct CRT multiplication: defect degree `2`, four `Theta(sqrt N)` channels suffice after constants are chosen so the product modulus exceeds the full defect range.

The `k=4` statement is a constant-sensitive boundary case: exponent counting alone gives `k>=4`; exactness at `k=4` requires choosing sufficiently large constant multiples of `sqrt N`.

## Withdrawn interpretation

The former profile

\[
AL0=(1,0),\qquad AL1=(1,1),\qquad AL2=(2,2)
\]

must **not** be read as an intrinsic or interpretation-invariant phase invariant.

Later digit/radix constructions show that AL2 can be recovered with linear total storage without retaining direct-CRT resolution exponent `rho=2`. Resolution can be traded for factorisation/precomputation.

Accordingly the following are withdrawn from Article B's theorem chain:

- `rho(AL2)=2` as an intrinsic statement;
- RTP as a semantic invariant of AL0/AL1/AL2;
- any claim that four channels are absolutely necessary outside the direct complete-table CRT template.

## Publication use

Article B may cite this file only as a **failed-invariant / normal-form calibration**:

> Direct CRT verification exposes a defect-resolution tradeoff, but the tradeoff is presentation-dependent and collapses under alternative factorisations.

The canonical standard-model results are the FO preprocessing collapse and the exact CQ width theorem.
