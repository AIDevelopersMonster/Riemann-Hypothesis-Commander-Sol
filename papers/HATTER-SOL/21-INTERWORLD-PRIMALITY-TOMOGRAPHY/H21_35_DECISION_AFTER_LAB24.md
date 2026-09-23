# HATTER-SOL-21 · DECISION AFTER LAB-24

Status: **RESEARCH ROUTING DECISION**

Two publication routes have now been tested.

## Route A — arithmetic reciprocal theorem

Current strongest reduction:

\[
\boxed{
\text{projective ray}
+
\text{norm datum}
+
\text{at most one binary lift bit}.
}
\]

LAB-22 shows a finite binary-lift covariance signal above deterministic
shift-control, but group sample sizes remain too small for a stable universal
law.

This route remains mathematically promising.

## Route B — runtime-safe world compiler

LAB-24 proves out-of-sample generalization of the compiler effect.

However the capped expected-cost improvement is currently modest:

\[
\sim0.7\%
\]

on the broad \(|D|\le127\) held-out test.

This route is useful engineering but is not currently strong enough for the
central publication claim.

## Decision

\[
\boxed{
\text{PRIMARY: reciprocal binary-lift arithmetic}
}
\]

\[
\boxed{
\text{SECONDARY: compiler/hardware validation}
}
\]

Do not spend major compute on larger greedy schedule scans until either:

- a better cost model/world family is introduced;
- or actual FPGA measurements show an amplified implementation-level benefit.

The next mathematical strike should seek a world-specific law for the
target-adjusted lift bits rather than another pooled covariance scan.
