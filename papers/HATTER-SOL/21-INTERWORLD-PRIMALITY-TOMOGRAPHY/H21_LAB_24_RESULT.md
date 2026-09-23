# HATTER-SOL-21 · H21-LAB-24 RESULT

Status: **CI REPRODUCED / OUT-OF-SAMPLE COMPILER GENERALIZES, EFFECT MODEST**

Run:

\`35740409015\`

Training and test bands are disjoint:

\[
S_{\rm train}: n<2^{17},
\]

\[
S_{\rm test}: 2^{17}\le n<2^{18}.
\]

All populations use the same common-core prime cutoff.

## 1. |D| <= 127

Training semiprimes:

\[
\boxed{2294}.
\]

Test semiprimes:

\[
\boxed{4142}.
\]

Candidate worlds:

\[
\boxed{76}.
\]

Per-world train/test hit-rate rank correlation:

\[
\boxed{
\rho_S=0.817446.
}
\]

Thus world quality generalizes substantially, but not perfectly, across
magnitude bands.

### Train-greedy schedule on held-out test band

Coverage after 20 worlds:

\[
\boxed{32.448093\%}.
\]

Capped expected cost:

\[
\boxed{16.910913}.
\]

### Train individual ranking

Coverage:

\[
31.965234\%.
\]

Capped cost:

\[
16.999759.
\]

### Hand schedule

Coverage:

\[
31.627233\%.
\]

Capped cost:

\[
17.033076.
\]

### Oracle test-greedy benchmark

Coverage:

\[
33.800097\%.
\]

Capped cost:

\[
16.713906.
\]

The train-greedy schedule shares:

- 3 of the oracle top 5 worlds;
- 6 of the oracle top 10;
- 12 of the oracle top 20.

## 2. Operational gain

Relative to the hand schedule, train-greedy improves test coverage by about

\[
\boxed{0.82\text{ percentage points}}
\]

and reduces capped expected world executions by

\[
\boxed{0.1222}
\]

worlds, about

\[
\boxed{0.72\%}
\]

of the hand-schedule capped cost.

This is a real out-of-sample compiler effect, but it is modest.

## 3. |D| <= 63 control

Train/test hit-rank correlation is stronger:

\[
\boxed{\rho_S=0.941727}.
\]

Train-greedy test coverage:

\[
38.256363\%.
\]

Hand coverage:

\[
38.134431\%.
\]

Capped costs:

\[
15.989026
\]

versus

\[
15.992684.
\]

The gain is positive but very small.

## 4. Scientific conclusion

The offline world compiler does generalize across disjoint number ranges.

Therefore the H21 scheduling effect is not purely in-sample overfitting.

However the measured advantage is currently too small to carry the central
publication claim without further hardware-specific leverage or a better
cost-aware world family.

## 5. Publication decision

LAB-24 strengthens the engineering architecture but does **not** cross the
publication threshold.

The mathematical binary-lift / reciprocal-sampling line remains the stronger
candidate for a central H21 result.
