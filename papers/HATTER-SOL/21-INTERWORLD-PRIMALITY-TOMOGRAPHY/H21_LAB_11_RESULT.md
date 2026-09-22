# HATTER-SOL-21 · H21-LAB-11 RESULT

Status: **CI REPRODUCED / EXACT COUPLING BOUNDS VALIDATED**

Run:

\`35702670461\`

## 1. Exact identities

For every scanned world on the common-core populations,

\[
\boxed{
K
=
-\sum_{a\in\mathcal Z}
\operatorname{Cov}
\big(
\mathbf 1_{X=a},
\mathbf 1_{Y=a}
\big)
}
\]

was verified.

Maximum covariance-identity error:

\[
1.44\times10^{-16}.
\]

The exact fixed-marginal bounds

\[
\boxed{
-G
\le K
\le
\min(1,2(1-\pi_{\max}))-G
}
\]

were also verified with zero bound violations.

Likewise,

\[
\boxed{
|K|
\le
\operatorname{TV}(J,\pi\otimes\pi)
}
\]

and the Pinsker consequence

\[
\boxed{
|K|
\le
\sqrt{\frac{\ln2}{2}I_{\rm bit}(X;Y)}
}
\]

had zero violations.

## 2. Broad common-core result

For

\[
|D|\le255,\qquad pq<2^{18},\qquad p,q>255,
\]

there are

\[
\boxed{156}
\]

fundamental worlds and

\[
\boxed{2162}
\]

common-core semiprime pairs.

The most negative coupling examples include

\[
D=5:
\qquad
Q=0.02451434,
\quad
G=0.032932,
\quad
K=-0.008418,
\]

and

\[
D=-84:
\qquad
Q=0.01665125,
\quad
G=0.024665,
\quad
K=-0.008014.
\]

Thus the independent-marginal benchmark can overestimate true factor exposure
substantially.

## 3. Coupling is diagonal self-mask attraction

The dominant positive covariance component for strongly negative-\(K\) worlds
is frequently one of

\[
\varnothing,
\qquad
\{0\},
\qquad
\{0,1\}.
\]

For example, in the \(D=5\) common-core scan the strongest diagonal attraction
is the empty mask:

\[
c_{\varnothing}>0.
\]

Since

\[
K=-\sum_a c_a,
\]

this means the two directional views

\[
p\leftarrow q,
\qquad
q\leftarrow p
\]

land in the same mask more often than independent local statistics predict.

The correction \(K\) is therefore not an abstract statistical nuisance.

It measures **directional synchronization of local Lucas zero-mask phases**.

## 4. Positive coupling is possible but small in the broad scan

For \(|D|\le255\), some worlds have

\[
K>0,
\]

for example

\[
D=93,\quad185,\quad113.
\]

Their magnitude is small:

\[
K\approx10^{-4}.
\]

Thus the observed broad family is dominated by neutral-to-negative coupling,
with only weak self-mask repulsion in the positive cases.

This is an empirical statement for the scanned population, not a theorem.

## 5. Total variation can be sharp

On both broad scans,

\[
\boxed{
\max \frac{|K|}{\operatorname{TV}(J,\pi\otimes\pi)}=1.
}
\]

Therefore the total-variation bound is not merely formal: some tested worlds
saturate it.

By contrast, the Pinsker bound is much looser.

For \(|D|\le255\),

\[
\max
\frac{|K|}
{\sqrt{(\ln2/2)I_{\rm bit}}}
\approx
0.107.
\]

Hence mutual information is useful as a certified upper bound but not as a
tight compiler score in this finite family.

## 6. Fixed-marginal ceiling

Let

\[
m=\max_a\pi(a).
\]

Then

\[
Q
\le
\boxed{
\min(1,2(1-m)).
}
\]

This gives a hard pre-screen ceiling using only the marginal mask
distribution.

A candidate world can therefore be rejected without pairwise coupling analysis
whenever this ceiling already lies below the current shortlist threshold.

This strengthens the H21 compiler:

\[
\boxed{
\pi
\to
G
\to
Q_{\max}(\pi)
\to
\text{shortlist}
\to
K
\to
Q.
}
\]

## 7. Exact interpretation of K

The previous broad heuristic

\[
Q\approx G
\]

now has a precise error term:

\[
\boxed{
Q-G
=
-\sum_a
\operatorname{Cov}
(
\mathbf1_{X=a},
\mathbf1_{Y=a}
).
}
\]

Therefore the remaining number-theoretic question is no longer vague.

It is:

\[
\boxed{
\text{Why do reciprocal Lucas views of }p\text{ and }q
\text{ synchronize on the same zero-mask?}
}
\]

## 8. Hardware/compiler consequence

The compiler now has certified pruning levels:

1. torsion/silent-world rejection;
2. marginal diversity \(G\);
3. hard marginal ceiling \(Q_{\max}\);
4. optional information bound on \(|K|\);
5. exact pairwise \(K\) only for surviving candidates.

Thus expensive pairwise analysis need not be run on every candidate world.

## 9. Publication status

This is the first H21 layer containing a clean exact bound architecture around
the empirical world compiler, but the probability bounds themselves are
classical.

\[
\boxed{\text{PUBLICATION: NOT YET}}
\]

A publication-strength H21 theorem now requires an arithmetic explanation or
bound for the diagonal covariance terms

\[
c_a
=
J(a,a)-\pi(a)^2
\]

in terms of the quadratic world itself.

## 10. Next strike

The next target is the arithmetic origin of

\[
c_{\varnothing},
\quad
c_{\{0\}},
\quad
c_{\{1\}},
\quad
c_{\{0,1\}}.
\]

For each mask, derive the simultaneous Lucas congruence system defining

\[
L_W(p\leftarrow q)=a
\]

and

\[
L_W(q\leftarrow p)=a.
\]

Then seek a reciprocity/symmetry mechanism that explains why the joint
same-mask event differs from the product of marginals.

That is now the narrowest route to a genuinely H21-specific theorem.
