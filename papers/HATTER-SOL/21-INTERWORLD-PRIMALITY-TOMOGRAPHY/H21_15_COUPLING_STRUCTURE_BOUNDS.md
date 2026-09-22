# HATTER-SOL-21 · COUPLING STRUCTURE AND EXACT BOUNDS

Status: **EXACT PROBABILITY THEOREM LAYER**

## 1. Setup

For a fixed quadratic world \(W\), let

\[
X=L_W(p\leftarrow q),
\qquad
Y=L_W(q\leftarrow p)
\]

be the two directional zero masks on the common semiprime population.

The mask alphabet is

\[
\mathcal Z=\{\varnothing,\{0\},\{1\},\{0,1\}\}.
\]

After symmetrizing pair orientation, \(X\) and \(Y\) have the same marginal

\[
\pi(a)=\Pr[X=a]=\Pr[Y=a].
\]

Let

\[
J(a,b)=\Pr[X=a,Y=b].
\]

The exact factor-exposure probability is

\[
Q=\Pr[X\ne Y].
\]

The independent-marginal benchmark is

\[
G=1-\sum_a\pi(a)^2.
\]

The coupling correction is

\[
K=Q-G.
\]

## Theorem H21-K1 — covariance form

For each mask \(a\), define the indicator

\[
I_a(X)=\mathbf 1_{\{X=a\}},
\qquad
I_a(Y)=\mathbf 1_{\{Y=a\}}.
\]

Then

\[
\boxed{
K
=
-\sum_{a\in\mathcal Z}
\operatorname{Cov}(I_a(X),I_a(Y)).
}
\]

### Proof

Since

\[
\operatorname{Cov}(I_a(X),I_a(Y))
=
J(a,a)-\pi(a)^2,
\]

we have

\[
-\sum_a\operatorname{Cov}
=
\sum_a\pi(a)^2-\sum_aJ(a,a).
\]

But

\[
Q=1-\sum_aJ(a,a)
\]

and

\[
G=1-\sum_a\pi(a)^2.
\]

Therefore

\[
Q-G
=
\sum_a\pi(a)^2-\sum_aJ(a,a).
\]

QED.

## 2. Sign criterion

The sign of \(K\) now has an exact interpretation:

\[
\boxed{
K>0
\iff
\sum_a J(a,a)
<
\sum_a\pi(a)^2.
}
\]

Thus positive coupling means the two directions collide on the **same**
zero-mask less often than independent directional samples would.

Likewise

\[
\boxed{
K<0
\iff
\sum_a J(a,a)
>
\sum_a\pi(a)^2.
}
\]

Negative coupling is total self-mask attraction.

Importantly,

\[
K=0
\]

does **not** imply independence.  It only says that the total diagonal mass
matches the independent benchmark.

## 3. Exact extremal bounds at fixed marginal

Let

\[
m=\max_{a\in\mathcal Z}\pi(a).
\]

For any coupling \(J\) with both marginals equal to \(\pi\),

\[
\boxed{
0
\le
\Pr[X=Y]
\le
1
}
\]

is sharpened to

\[
\boxed{
\Pr[X=Y]
\ge
\max(0,2m-1).
}
\]

The upper bound \(1\) is attained by the identity coupling \(X=Y\).

The lower bound is sharp.

### Proof of the lower bound

Choose a mask \(a_*\) with \(\pi(a_*)=m\).  By the union bound,

\[
\Pr[X=a_*,Y=a_*]
\ge
\Pr[X=a_*]+\Pr[Y=a_*]-1
=
2m-1.
\]

Hence

\[
\Pr[X=Y]\ge\max(0,2m-1).
\]

Sharpness follows from the standard antimonotone/cyclic-shift coupling:
represent \(\pi\) as intervals on the unit circle and shift one copy by one
half-turn.  If \(m\le1/2\), no category must overlap itself; if \(m>1/2\),
exactly \(2m-1\) self-overlap is unavoidable and achievable.

QED.

Therefore the exact feasible exposure interval is

\[
\boxed{
0
\le
Q
\le
Q_{\max}(\pi)
=
\min(1,2(1-m)).
}
\]

Because \(K=Q-G\),

\[
\boxed{
-G
\le
K
\le
\min(1,2(1-m))-G.
}
\]

Both endpoints are sharp for the fixed marginal.

## 4. Meaning of the bounds

The lower endpoint

\[
K=-G
\]

corresponds to

\[
Q=0,
\]

i.e. perfect same-mask locking.

The upper endpoint corresponds to the most anti-aligned coupling permitted by
the marginal mass imbalance.

Thus a highly concentrated marginal can never achieve arbitrary factor
exposure even under optimal cross-prime anti-correlation.

This gives a second reason the diversity score \(G\) is useful: the marginal
itself constrains the maximal attainable exposure.

## Theorem H21-K2 — total-variation bound

Let

\[
P_{\rm ind}=\pi\otimes\pi.
\]

Let

\[
\Delta=\{(a,a):a\in\mathcal Z\}
\]

be the diagonal event.

Then

\[
K
=
P_{\rm ind}(\Delta)-J(\Delta).
\]

Hence

\[
\boxed{
|K|
\le
\operatorname{TV}(J,\pi\otimes\pi).
}
\]

This is immediate because total variation is the supremum of event-probability
differences.

## Corollary H21-K3 — mutual-information bound

Because \(J\) has marginals \(\pi\),

\[
D_{\rm KL}(J\|\pi\otimes\pi)
=
I(X;Y).
\]

Pinsker's inequality gives, with natural logarithms,

\[
\operatorname{TV}(J,\pi\otimes\pi)
\le
\sqrt{\frac12 I_{\rm nat}(X;Y)}.
\]

Therefore

\[
\boxed{
|K|
\le
\sqrt{\frac12 I_{\rm nat}(X;Y)}.
}
\]

If mutual information is reported in bits,

\[
I_{\rm nat}=(\ln2)I_{\rm bit},
\]

so

\[
\boxed{
|K|
\le
\sqrt{\frac{\ln2}{2}I_{\rm bit}(X;Y)}.
}
\]

This is a rigorous information-theoretic upper bound on how far the exact
factor-exposure rate can move away from the cheap diversity benchmark.

## 5. Per-mask coupling decomposition

Define

\[
c_a
=
J(a,a)-\pi(a)^2.
\]

Then

\[
\boxed{
K=-\sum_a c_a.
}
\]

Each \(c_a\) measures whether a particular zero-mask is self-attractive
(\(c_a>0\)) or self-repulsive (\(c_a<0\)) across the two directional views.

Thus a coupling-dominated world can be diagnosed at mask resolution, not only
through one scalar \(K\).

The four components are:

\[
c_{\varnothing},
\quad
c_{\{0\}},
\quad
c_{\{1\}},
\quad
c_{\{0,1\}}.
\]

## 6. World-compiler consequence

The exact compiler hierarchy becomes

\[
\boxed{
\pi
\to
G
\to
[m,Q_{\max}]
\to
I(X;Y)
\to
K
\to
Q.
}
\]

This gives progressively more expensive certificates:

1. marginal concentration gives a hard ceiling on possible exposure;
2. Gini diversity gives the independent benchmark;
3. mutual information bounds the maximum correction magnitude;
4. per-mask diagonal covariance identifies the mechanism;
5. exact joint masks give the final \(K\).

A candidate world can therefore be pruned before full pairwise ranking if its
marginal-implied upper bound is already below the current shortlist threshold.

## 7. Claim boundary

The covariance identity, coupling extremum, total-variation inequality, and
Pinsker bound are classical probability/information theory.

H21 does not claim those ingredients.

The H21-specific use is their composition with the exact Lucas zero-mask
factor observer to produce a mathematically certified world-quality compiler.
