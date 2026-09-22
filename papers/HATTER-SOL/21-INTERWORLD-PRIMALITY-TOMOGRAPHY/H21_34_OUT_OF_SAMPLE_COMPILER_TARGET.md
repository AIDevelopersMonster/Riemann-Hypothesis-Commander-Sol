# HATTER-SOL-21 · OUT-OF-SAMPLE WORLD-COMPILER TARGET

Status: **NEXT HARDWARE-SAFE COMPILER TEST**

## 1. Training and test split

Use the same candidate world family on disjoint magnitude bands.

Example:

\[
S_{\rm train}
=
\{pq<2^{17}\},
\]

\[
S_{\rm test}
=
\{2^{17}\le pq<2^{18}\},
\]

with the same common-core prime cutoff.

Compile the greedy schedule only from \(S_{\rm train}\).

Evaluate it unchanged on \(S_{\rm test}\).

## 2. Baselines

Compare:

1. train-greedy schedule;
2. train individual-hit ranking;
3. original hand schedule;
4. oracle test-greedy schedule, reported only as an upper benchmark.

The oracle is not deployable; it measures the generalization gap.

## 3. Runtime cost

For schedule length \(K\), define

\[
C_K(n)
=
\begin{cases}
\tau(n),&\text{factor exposed by step }\tau\le K,\\
K+1,&\text{not exposed}.
\end{cases}
\]

Report

\[
\boxed{
\bar C_K
=
\frac1{|S|}
\sum_{n\in S}C_K(n).
}
\]

Also report:

- coverage at \(K=1,2,3,5,10,20\);
- generalization gap to oracle;
- schedule prefix overlap;
- rank correlation of per-world hit rates between train and test.

## 4. Publication relevance

A stable out-of-sample reduction in

\[
\bar C_K
\]

would establish a real compiler effect rather than dataset-specific
reordering.

It would still not by itself prove novelty, but it would justify an FPGA
scheduler experiment and strengthen Gate E.
