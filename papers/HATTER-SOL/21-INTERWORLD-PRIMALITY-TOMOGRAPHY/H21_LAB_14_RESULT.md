# HATTER-SOL-21 · H21-LAB-14 RESULT

Status: **CI REPRODUCED / NONTRIVIAL CLOCK LOCKS CLASSIFIED**

Run:

\`35717303051\`

## 1. Exact lock equivalence

For every tested pair,

\[
\boxed{
p\equiv q\pmod g
\iff
pq\equiv1\pmod g
}
\]

and

\[
\boxed{
p\equiv-q\pmod g
\iff
pq\equiv-1\pmod g.
}
\]

Mismatch counts:

\[
\boxed{0,\ 0}.
\]

Thus the correct nontrivial lock variable is

\[
pq\bmod g\in\{+1,-1,\text{other}\}.
\]

## 2. Broad result for |D|<=255

After removing the trivial \(g\le2\) contamination:

### Positive lock

\[
L_+:\ pq\equiv1\pmod g.
\]

Mean population fraction:

\[
27.50\%.
\]

Mean same-mask lift relative to the fixed-character stratum:

\[
\boxed{-0.020045}.
\]

Only

\[
20.35\%
\]

of rows have positive raw same-mask lift.

Yet the conditional coupling shift is

\[
\boxed{-0.004653}.
\]

Thus \(L_+\) creates a more diverse marginal mask population while retaining
enough diagonal dependence to make \(K\) more negative.

### Negative lock

\[
L_-:\ pq\equiv-1\pmod g.
\]

Mean population fraction:

\[
24.02\%.
\]

Mean same-mask lift:

\[
\boxed{+0.008906},
\]

positive in

\[
85.71\%
\]

of rows.

But the conditional coupling shift is

\[
\boxed{+0.002062}.
\]

Hence the extra same-mask mass is more than explained by the changed marginal
concentration; relative to its own independent benchmark this class is less
negatively coupled.

### Other nontrivial phases

Mean same-mask lift:

\[
-0.010473,
\]

mean coupling shift:

\[
-0.002455.
\]

## 3. Stability

The \(|D|\le127\) scan gives the same qualitative signs:

\[
L_+:
\quad
\Delta\text{same}=-0.027059,
\quad
\Delta K=-0.005152,
\]

\[
L_-:
\quad
\Delta\text{same}=+0.013724,
\quad
\Delta K=+0.002768.
\]

Thus the effect is not a one-range artifact.

## 4. Conclusion

The hypothesis

\[
\boxed{
\text{nontrivial clock lock directly means more same-mask synchronization}
}
\]

is false.

However the lock classes strongly reorganize both the marginal and joint
zero-mask laws.

The correct next object is therefore an exact lock-stratified coupling
decomposition, not a scalar clock-gcd score.

## 5. Surviving target

Inside each fixed character stratum, let

\[
L\in\{\text{trivial},+,-,0\}
\]

be the shared-clock lock class.

Apply the law of total covariance again:

\[
K_s
=
K_{s,\mathrm{within-lock}}
-
H_{s,\mathrm{lock}}.
\]

This will quantify whether lock-class heterogeneity explains the remaining
negative coupling or whether the true mechanism still survives inside each
lock class.
