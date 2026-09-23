# HATTER-SOL-21 · CROSS-MASK COUPLING DECOMPOSITION

Status: **EXACT PROBABILITY LAYER / WORLD-QUALITY COMPILER**

## 1. Why Shannon entropy is not the exact objective

For a fixed world \(W\) and distinct semiprime

\[
n=pq,
\]

the exact H21 factor criterion is

\[
A_W(p,q)
=
\mathbf 1[
L_W(p\leftarrow q)\ne L_W(q\leftarrow p)
].
\]

The local masks take values in

\[
\mathcal Z=
\{\varnothing,\{0\},\{1\},\{0,1\}\}.
\]

Shannon entropy measures uncertainty in a single mask distribution, but factor
exposure is a collision/noncollision event between two directional masks.

Therefore the natural one-direction benchmark is the collision probability,
not entropy itself.

## 2. Symmetrized directional marginal

On a finite unordered semiprime population \(\mathcal P_2\), for each pair
\(\{p,q\}\) write

\[
X=L_W(p\leftarrow q),
\qquad
Y=L_W(q\leftarrow p).
\]

Define the symmetrized joint law

\[
\bar J_W(a,b)
=
\frac12
\Pr[(X,Y)=(a,b)]
+
\frac12
\Pr[(X,Y)=(b,a)].
\]

Its two marginals are equal. Denote the common marginal by

\[
\boxed{
\pi_W(a)=\sum_b\bar J_W(a,b).
}
\]

Operationally, \(\pi_W\) is obtained by pooling both directional masks from
every eligible semiprime pair.

## 3. One-direction collision benchmark

If two masks were independent draws from \(\pi_W\), their mismatch probability
would be

\[
\boxed{
G_W
=
1-\sum_{a\in\mathcal Z}\pi_W(a)^2.
}
\]

This is the Gini impurity / one-minus-collision probability of the local mask
distribution.

Unlike Shannon entropy, \(G_W\) has the same operational units as factor
exposure: a probability of unequal masks.

## 4. Exact pairwise exposure

The actual H21 semiprime exposure probability is

\[
\boxed{
Q_{\rm asym}(W)
=
1-\sum_{a\in\mathcal Z}\bar J_W(a,a).
}
\]

This is exact because H21-SD1 says a factor is exposed iff the two local masks
differ.

## Theorem H21-CM1 — diversity plus coupling

Define

\[
\boxed{
K_W
=
\sum_{a\in\mathcal Z}
\left(
\pi_W(a)^2-\bar J_W(a,a)
\right).
}
\]

Then

\[
\boxed{
Q_{\rm asym}(W)
=
G_W+K_W.
}
\]

### Proof

Direct subtraction gives

\[
G_W+K_W
=
1-\sum_a\pi_W(a)^2
+
\sum_a
\left(
\pi_W(a)^2-\bar J_W(a,a)
\right)
\]

\[
=
1-\sum_a\bar J_W(a,a)
=
Q_{\rm asym}(W).
\]

QED.

## 5. Interpretation

The factor quality of a world has two irreducible pieces.

### Local phase diversity

\[
G_W
\]

measures how varied the one-direction zero masks are.

### Cross-direction coupling

\[
K_W
\]

measures how much the actual paired arithmetic deviates from an independent
pairing of those local masks.

- \(K_W>0\): opposite directions avoid equal masks more often than the
  independent benchmark predicts;
- \(K_W<0\): opposite directions are attracted toward equal masks;
- \(K_W=0\): one-direction mask diversity predicts exposure exactly.

Thus

\[
\boxed{
\text{world quality}
=
\text{local mask diversity}
+
\text{cross-prime coupling}.
}
\]

## 6. Shannon entropy remains secondary

Define

\[
H_W
=
-\sum_a\pi_W(a)\log_2\pi_W(a).
\]

A silent torsion world has

\[
H_W=G_W=Q_{\rm asym}=0.
\]

But in general two worlds can have similar \(H_W\) and different
\(Q_{\rm asym}\) because:

1. entropy does not directly encode collision probability;
2. neither \(H_W\) nor \(G_W\) contains the pair-coupling correction \(K_W\).

Therefore H21 keeps Shannon entropy as a descriptive statistic, not as the
primary factor-quality functional.

## 7. Compiler hierarchy

The world compiler now has an explicit hierarchy:

\[
(B,C,\Delta)
\to
\text{torsion no-go}
\to
\text{Lucas phase map}
\to
\pi_W
\to
G_W
\to
K_W
\to
Q_{\rm asym}(W).
\]

There are three possible outcomes.

### Level A — silent

\[
G_W=0.
\]

Reject the expensive world.

### Level B — diversity-dominated

\[
|K_W|\ll G_W.
\]

A one-direction phase model is already a useful quality predictor.

### Level C — coupling-dominated

\[
|K_W|
\text{ is material}.
\]

Pairwise arithmetic structure is essential and static one-prime summaries are
insufficient.

## 8. Hardware implication

A future adaptive scheduler need not estimate the full semiprime population if
a candidate world is diversity-dominated.

It can use compact marginal phase tables.

Coupling-dominated worlds require richer pair-conditioned scheduling logic.

The decomposition therefore separates cheap and expensive scheduler models.

## 9. Claim boundary

The probability identity itself is elementary.

The H21 content is its application to the exact Lucas zero-mask factor
observer and its use as a world-compiler decomposition.

No novelty priority is asserted before literature audit.
