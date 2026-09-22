# HATTER-SOL 20-21 - RC1 REVIEW REPORT

Status: **INDEPENDENT SKEPTICAL PASS COMPLETED**

Date: 2026-09-22

## Verdict

[
oxed{	ext{RC1 ACCEPTABLE FOR AUTHOR REVIEW WITH MINOR REVISIONS}}
]

No fatal mathematical or hardware contradiction was found in the frozen claim set.

## 1. Exact theorem layer

The central identity

[
x^n=C^{(n-1)/2}x
]

under

[
x^2=C
]

is immediate and correct for odd (n).

The induced defect formula and factor-gcd preservation follow directly once

[
(D/n)=(C/n)
]

for (D=4C) is stated under the declared odd/coprime assumptions.

No hidden factor information is used by the compiler predicate (B=0).

**Verdict:** supported.

## 2. H20 semantic/physical separation

The manuscript correctly keeps these layers separate:

- SAT equivalence is exact for the declared widths;
- ABC separation is a measured synthesis result;
- Cyclone V / Gowin results are finite physical measurements.

The backend-dependent BALANCED/LINEAR crossover is stated only for the measured widths.

**Reviewer caution:** inequalities such as (L_W<B_W) should be understood as the declared primary area/timing comparison, not as a universal total ordering over every physical metric.

The manuscript already gives the physical observer as vector-valued, which adequately limits the claim.

## 3. Cycle-ratio wording

LAB-27 contains two distinct legitimate summaries:

- mean of per-vector ratios:
  [
  4.981273;
  ]
- ratio of mean cycle counts:
  [
  861/175=4.92.
  ]

The manuscript uses (4.981273) for the controller-level mean ratio and uses the authoritative mean cycle counts (175,861) for Fmax-derived latency.

This is mathematically consistent.

**Required editorial rule:** never describe (861/175) as the mean per-vector ratio. Keep the two quantities explicitly named.

## 4. Timing claim

The Quartus comparison supports:

- matched utilization;
- internal register-to-register timing;
- matched Fmax comparison;
- Fmax-derived core latency.

It does not support complete board-level sign-off because external pin/I/O timing is not fully constrained.

The manuscript states this limitation.

**Verdict:** supported with current wording.

## 5. Area-latency calculation

Using

[
T_s=175/157.33=1.112312 mu s
]

and

[
T_q=861/123.20=6.988636 mu s,
]

the reported area-latency values

[
215T_s=239.147016
]

and

[
328T_q=2292.272727
]

give

[
2292.272727/239.147016approx9.5852.
]

**Verdict:** arithmetic consistent.

## 6. Prior-art boundary

The manuscript correctly disclaims novelty for:

- Euler-Jacobi / Solovay-Strassen;
- Frobenius/Lucas probable-prime testing;
- Lucas/Jacobi hardware;
- generic partial evaluation / specialization.

The manuscript claims novelty only for the bounded end-to-end H21 descriptor-to-lowering-to-matched-device chain.

**Reviewer caution:** retain the phrase

> targeted literature audit did not identify a direct analogue

rather than any firstness claim.

## 7. H20-EXT

H20-EXT is presented as a falsification stage and not as a positive result.

**Verdict:** appropriate.

## 8. Reproducibility

Scientific reproducibility is strong, but archival reproducibility is not yet complete until the release records:

- author list;
- exact final commit;
- final tag;
- archived PDF;
- DOI.

These are release-management blockers, not scientific blockers.

## 9. Minor revisions before archival PDF

1. Insert confirmed author name(s) and affiliation(s).
2. Insert exact final repository commit and release tag.
3. Keep a note distinguishing mean-of-ratios from ratio-of-means.
4. Preserve device and architecture qualifiers adjacent to the (9.5852	imes) number.
5. Add DOI after Zenodo deposit.

## Final recommendation

[
oxed{	ext{Proceed to author metadata + frozen release + Zenodo deposit}}
]

The deeper H21 reciprocal-coupling programme should remain outside this manuscript unless it later becomes a separately audited result.
