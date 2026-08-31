# FCOA Hybrid Memory — Exact CQ Width Threshold

**Status:** exact near-linear width theorem in the standard conjunctive-query preprocessing model  
**Main result:** the minimum CQ variable width for `N^{1+o(1)}` preprocessing of exact truncated addition is exactly `9`.

## 1. Statement

Let `k_+` be the minimum integer `k` such that exact truncated addition

\[
Add_N(x,y,z)\iff x+y=z<N
\]

admits a fixed `CQ^k` decoder over preprocessing structures of size

\[
N^{1+o(1)}.
\]

The two-channel CRT construction gives

\[
k_+\le 9.
\]

We prove the matching lower bound

\[
k_+\ge 9.
\]

Hence

\[
\boxed{k_+=9.}
\]

Because truncated multiplication has only `Theta(N log N)` true triples and can be materialized directly, the same threshold is the near-linear threshold for AL2:

\[
\boxed{k_{AL1}=k_{AL2}=9.}
\]

---

## 2. Entropy slice

As before, restrict to

\[
\mathcal T_m=\{(x,y,z):0\le x,y<m,\ z=x+y\},
\qquad m=\lfloor N/3\rfloor.
\]

Choose `(X,Y)` uniformly on `[m]^2` and set `Z=X+Y`.

Then, up to lower-order terms,

\[
H(X)=H(Y)=H(Z)=\log N,
\]

\[
H(X,Y)=H(X,Z)=H(Y,Z)=2\log N,
\]

and therefore

\[
I(X;Y)=I(X;Z)=I(Y;Z)=O(1).
\tag{2.1}
\]

Choose one satisfying helper tuple deterministically for every valid triple in the slice.

---

## 3. No free-pair atoms

Suppose the preprocessing size is

\[
N^{1+o(1)}.
\]

If a primitive atom contains two distinct free variables among `X,Y,Z`, then its projection contains `Theta(N^2)` distinct free pairs, so the primitive relation itself has quadratic size.

Hence every near-linear candidate has:

\[
\boxed{\text{at most one free arithmetic variable per atom}.}
\tag{3.1}
\]

For a fixed complete helper assignment, the accepted free tuples therefore form a Cartesian box. Exactness and the Latin property of addition imply every productive box is a singleton.

Thus the selected complete helper tuple determines `(X,Y,Z)`.

---

## 4. Information-colored helper regions

Let the five helpers of a hypothetical `CQ^8` representation be

\[
U_1,\dots,U_5.
\]

Call a helper tuple `S` **F-colored**, for `F in {X,Y,Z}`, if

\[
H(S\mid F)=o(\log N).
\]

Every helper that occurs in an atom together with `F` is F-colored, because a near-linear atom has entropy at most

\[
\log N+o(\log N)
\]

while `H(F)=\log N+o(\log N)`.

If a helper is both F-colored and G-colored for distinct free coordinates `F,G`, then by (2.1)

\[
H(U)=o(\log N).
\tag{4.1}
\]

Thus a helper carrying a positive fraction of one entropy unit cannot simultaneously belong to two different free-coordinate colors.

---

## 5. Boundary of a color region

For a free variable `F`, let `C_F` be the maximal set of helpers that are F-colored and are connected to the atoms containing `F` through helper-only atoms whose variables remain F-colored.

Let `B_F subseteq C_F` be the **effective boundary**: helpers in `C_F` that occur in a helper-only atom together with at least one helper outside `C_F` carrying non-negligible entropy.

### Lemma 5.1 — boundary sufficiency

On productive witnesses,

\[
H(F\mid B_F)=o(\log N).
\tag{5.1}
\]

### Proof

The CQ factor graph separates the `F`-colored interior from the rest of the query through `B_F`. If two productive witnesses agreed on `B_F` but carried two distinct `F` values, the non-`F` side of the witness could be kept fixed while changing the `F`-interior. This would create two accepted triples with the same other two free coordinates and different `F`, contradicting the pairwise functional dependency of the Latin relation. `square`

Hence the effective boundary must carry one full entropy unit:

\[
H(B_F)\ge\log N-o(\log N).
\tag{5.2}
\]

---

## 6. One effective boundary helper is impossible

### Lemma 6.1 — no singleton boundary

For every `F in {X,Y,Z}`,

\[
\boxed{|B_F|\ge2.}
\]

### Proof

Assume

\[
B_F=\{U\}.
\]

By (5.1), `U` determines `F` up to subpolynomial ambiguity, and because `U` is F-colored,

\[
H(U)=\log N-o(\log N).
\tag{6.1}
\]

Since `U` is an effective boundary helper, there is a helper-only primitive atom containing `U` and some outside helper tuple `T` with non-negligible entropy.

The atom belongs to a near-linear relation, so

\[
H(U,T)\le\log N+o(\log N).
\]

Combining with (6.1),

\[
H(T\mid U)=o(\log N).
\]

But `U` is itself an almost-function of `F`; therefore `T` is also F-colored. This contradicts that the atom leaves the maximal F-colored region through a non-negligible outside helper.

So a single helper cannot be an effective information boundary. `square`

The point is exactly the one exposed by all earlier compression examples: a full-entropy helper cannot cross a near-linear relation into genuinely new information. It can only generate further encodings of the same free coordinate. To leave the color region, the coordinate must first be split across at least two lower-entropy channels.

---

## 7. Boundaries of different free variables are disjoint

Suppose a helper `U` belonged to both `B_F` and `B_G` for two distinct free variables. Then `U` is both F-colored and G-colored.

By (4.1),

\[
H(U)=o(\log N).
\]

Such a helper cannot contribute a positive share of the one entropy unit required by either boundary in (5.2). Removing all shared `o(log N)` helpers changes the boundary entropy by only `o(log N)` because the total number of helpers is fixed.

Therefore each free coordinate needs at least two **private, non-negligible** effective boundary helpers.

Consequently

\[
|B_X|+|B_Y|+|B_Z|\ge6.
\tag{7.1}
\]

---

## 8. CQ8 contradiction

A `CQ^8` formula has exactly three free arithmetic variables and at most

\[
8-3=5
\]

helper variables.

But (7.1) shows that every near-linear exact representation needs at least six private non-negligible helper channels.

Contradiction.

Therefore:

### Theorem HM-CQ8-NL

No fixed eight-variable conjunctive query can decode exact truncated addition from preprocessing structures of size

\[
N^{1+o(1)}.
\]

Hence

\[
\boxed{k_+\ge9.}
\]

---

## 9. Exact threshold from CRT

`CQ6_ENTROPY_BOTTLENECK.md` gave the explicit two-channel CRT decoder using the variables

\[
x,y,z,x_p,y_p,z_p,x_q,y_q,z_q,
\]

exactly nine distinct variables.

Its preprocessing size is `Theta(N)`:

- target-to-residue maps: `Theta(N)`;
- modular addition table modulo `p`: `Theta(p^2)=Theta(N)`;
- modular addition table modulo `q`: `Theta(q^2)=Theta(N)`.

With `pq>2N`, the two congruences imply exact ordinary addition.

Thus

\[
\boxed{k_+\le9.}
\]

Combining upper and lower bounds:

### Theorem HM-CQ-EXACT

\[
\boxed{k_+=9.}
\]

---

## 10. AL2 threshold

The truncated multiplication graph

\[
Mul_N(x,y,z)\iff xy=z<N
\]

has only

\[
Theta(N\log N)=N^{1+o(1)}
\]

true tuples. Therefore it may be added to any near-linear AL1 preprocessing structure as one directly materialized ternary relation and queried atomically.

Hence

\[
\boxed{k_{AL2}=k_{AL1}=9.}
\]

There is no separate multiplication width threshold under this specific near-linear total-storage benchmark.

---

## 11. Final standard-model phase diagram

For near-linear preprocessing:

\[
\boxed{
\begin{array}{c|ccc}
\text{CQ width }k & AL0 & AL1 & AL2\\
\hline
3 & \checkmark & \times & \times\\
4 & \checkmark & \times & \times\\
5 & \checkmark & \times & \times\\
6 & \checkmark & \times & \times\\
7 & \checkmark & \times & \times\\
8 & \checkmark & \times & \times\\
9 & \checkmark & \checkmark & \checkmark
\end{array}
}
\]

Thus the standard finite-variable preprocessing model exhibits an exact width jump

\[
\boxed{3\longrightarrow9}
\]

between near-linear order memory and near-linear additive transport.

---

## 12. Interpretation

The exact threshold has a transparent information-flow meaning.

Near-linear order uses one extra witness variable:

\[
(x,y)+w.
\]

Near-linear exact addition needs **two independent information channels for each of the three free coordinates**:

\[
(X_p,X_q),\qquad(Y_p,Y_q),\qquad(Z_p,Z_q).
\]

That is six helpers, plus the three free arithmetic variables:

\[
\boxed{3+6=9.}
\]

CRT realizes this lower bound exactly.

The number `9` is therefore not an artifact of the particular residue construction: it is forced by the near-linear information-boundary argument.

---

## 13. Literature calibration

This theorem belongs to the intersection of finite-variable conjunctive-query logic, factorised database representations, and entropy bounds under functional dependencies.

Recent factorised-representation work studies lower bounds for succinct join representations via structural and communication-complexity methods, while entropy methods are standard for CQ bounds with functional dependencies. The present argument is specialized to the Latin/quasigroup relation of exact addition and uses a colored-boundary information-flow obstruction rather than claiming a generic CQ theorem.

Relevant calibration:

- Tomasz Gogacz, Szymon Torunczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.
- Dan Olteanu, Jakub Zavodny, *Factorised Representations of Query Results: Size Bounds and Readability*, ICDT 2012, DOI 10.1145/2274576.2274607.
- Christoph Berkholz, Harry Vinall-Smeeth, *Factorised Representations of Join Queries: Tight Bounds and a New Dichotomy*, ICDT 2026, DOI 10.4230/LIPIcs.ICDT.2026.11.

The 2026 factorised-representation work confirms that succinct join representations and lower bounds are an active standard research direction, but its general theorems do not directly imply the specialized width-9 addition threshold proved here.

---

## 14. Next question

The CQ-width problem is now closed at the near-linear exponent level.

The next nontrivial refinement is quantitative rather than existential:

\[
\boxed{\text{determine the optimal storage exponent }\sigma_1^{CQ}(k)\text{ for }k=6,7,8.}
\]

We currently know only:

- `k=3,4,5`: exponent `2`;
- `k=6`: exponent at least `7/6`;
- `k=7,8`: exponent strictly greater than `1`;
- `k=9`: exponent `1`.

Finding the exact interpolation between `2` and `1` would turn the sharp threshold theorem into a full width-space tradeoff curve.
