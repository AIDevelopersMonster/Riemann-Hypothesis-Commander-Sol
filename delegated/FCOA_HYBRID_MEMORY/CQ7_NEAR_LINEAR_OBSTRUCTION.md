# FCOA Hybrid Memory — CQ7 Near-Linear Obstruction

**Status:** positive lower-bound theorem in the standard conjunctive-query preprocessing model  
**Main result:** exact truncated addition has no `N^{1+o(1)}` preprocessing representation with a seven-variable conjunctive-query decoder.

## 1. Problem

Let

\[
Add_N(x,y,z)\iff x+y=z<N.
\]

A `CQ^7` decoder has the three free arithmetic variables

\[
x,y,z
\]

and at most four helper variables

\[
u_1,u_2,u_3,u_4.
\]

We prove that no fixed `CQ^7` formula can decode exact truncated addition from preprocessing structures of size

\[
N^{1+o(1)}.
\]

Together with the previously proved `CQ^6` obstruction and the explicit `CQ^9` CRT upper bound, this raises the common AL1/AL2 near-linear width threshold to at least eight.

---

## 2. Regular addition slice and witnesses

As in the `CQ^6` entropy argument, restrict to

\[
\mathcal T_m=\{(x,y,z):0\le x,y<m,\ z=x+y\},
\qquad m=\lfloor N/3\rfloor.
\]

Choose `(X,Y)` uniformly from `[m]^2` and set `Z=X+Y`. Then, up to `O(1)` terms,

\[
H(X)=H(Y)=H(Z)=\log N,
\]

\[
H(X,Y)=H(X,Z)=H(Y,Z)=2\log N,
\]

and hence

\[
I(X;Y)=I(X;Z)=I(Y;Z)=O(1).
\tag{2.1}
\]

Choose one satisfying helper tuple deterministically for each valid addition triple.

For a fixed complete helper assignment, the free part of the CQ is a Cartesian box because no near-linear primitive atom can contain two distinct free arithmetic variables. Exactness and the Latin property of addition force every productive box to be a singleton.

Thus the chosen helper tuple determines the free triple and conversely is a deterministic function of it.

---

## 3. Shared free-adjacent helpers are asymptotically informationless

Call a helper `U` **shared** if it occurs in some atom with free variable `F` and in some atom with a distinct free variable `G`.

Since every primitive relation has `N^{1+o(1)}` tuples, an atom containing `F,U` gives

\[
H(U\mid F)=o(\log N).
\]

Similarly,

\[
H(U\mid G)=o(\log N).
\]

Using the common-information inequality

\[
H(U)\le I(F;G)+H(U\mid F)+H(U\mid G)
\]

and (2.1),

\[
\boxed{H(U)=o(\log N).}
\tag{3.1}
\]

Hence a helper directly shared by two free branches carries only subpolynomially many effective states on the selected witness distribution.

This is the key distinction between a genuine arithmetic coordinate channel and a merely shared syntactic variable.

---

## 4. Case I — at least one shared helper

There are only four helpers total.

Fix all directly shared helpers to values lying in a joint typical set of size

\[
N^{o(1)}.
\]

Since the selected addition slice has `Theta(N^2)` tuples, some joint value of the shared helpers leaves a fiber

\[
\mathcal T'\subseteq \mathcal T_m
\]

of size

\[
|\mathcal T'|=N^{2-o(1)}.
\tag{4.1}
\]

On this fiber the shared helpers are constants and may be substituted out of the query.

Because a projection of a Latin relation has degree at most `N`, (4.1) implies that each of the three free coordinates still takes

\[
N^{1-o(1)}
\]

distinct values. Thus the same normalized entropy relations as (2.1) remain valid up to `o(\log N)`.

Every free branch must still contain at least one nonconstant private helper; otherwise, after the shared constants are fixed, that free variable would be constrained independently of the other two branches and the Cartesian-box argument would force it to a singleton on every productive helper assignment.

Since one helper has already been consumed by the shared layer, at most three nonconstant private helpers remain. Therefore the fixed fiber reduces to a three-helper conjunctive representation of a Latin subrelation of size `N^{2-o(1)}`.

The `CQ^6` entropy proof applies verbatim to such a dense Latin subrelation: it uses only

1. pairwise functional dependencies;
2. `N^{1-o(1)}` entropy in each coordinate;
3. total output entropy `2\log N-o(\log N)`;
4. three helper variables.

That proof rules out near-linear preprocessing.

Hence no near-linear `CQ^7` representation can contain a directly shared helper.

---

## 5. Case II — no shared helper

Assume now that every helper occurring with a free variable occurs with exactly one of `X,Y,Z`.

There are four helpers, while all three free branches must be nonempty. Up to permutation there are only two structural types.

### Type A: `1+1+1` private helpers plus one purely internal helper

Let the private helpers be

\[
U_X,U_Y,U_Z
\]

and let `T` be helper-only.

Because `U_X` is the only helper adjacent to `X`, exactness implies that on productive witnesses `U_X` determines `X`: if the same productive `U_X` allowed two values `x\ne x'`, the unchanged remainder of the witness would yield two valid triples with the same `Y,Z`, contradicting the functional dependency

\[
YZ\to X.
\]

Thus

\[
H(X\mid U_X)=o(\log N),
\]

and similarly for `U_Y,U_Z`. Therefore each private helper has entropy

\[
\log N-o(\log N).
\tag{5.1}
\]

No near-linear helper-only atom can contain two of these private helpers, since any pair, say `U_X,U_Y`, has entropy

\[
H(U_X,U_Y)=2\log N-o(\log N)
\]

by (2.1) and (5.1).

The internal helper `T` cannot repair this. If the `X`-branch reaches the rest only through `T`, then exactness forces `T` to determine `X`; otherwise two `X` values with the same separator value would combine with the same `Y,Z` side. Hence `H(T)=\log N-o(\log N)`. But then `T` cannot occur in a near-linear atom together with `U_Y` or `U_Z`, again because the corresponding pair entropy is asymptotically `2\log N`.

Thus the three branches cannot be coupled, contradicting exact addition.

### Type B: private-helper counts `2+1+1`

Assume `X` has private helpers `A,B`, while `Y` and `Z` have single private helpers `C,D`.

As above,

\[
H(C)=H(D)=\log N-o(\log N).
\tag{5.2}
\]

Every helper from the `X` branch that participates in a helper-only atom with `C` or `D` must have entropy `o(\log N)`. Indeed, such an `X`-helper is an almost-function of `X`, while `C` is an almost-copy of the pairwise-independent variable `Y` and `D` an almost-copy of `Z`; a positive `\Theta(\log N)` amount of `X`-information together with either `C` or `D` would force the atom entropy above `\log N+o(\log N)`.

Let `B_X\subseteq\{A,B\}` be the set of `X`-helpers through which the `X` branch can reach either singleton branch. Exactness forces `B_X` to determine `X`: if two distinct `X` values agreed on the entire boundary `B_X`, then the internal `X`-branch could be changed while all constraints on the `Y,Z` side remained fixed, producing two valid triples with the same `Y,Z`.

Hence

\[
H(B_X)\ge H(X)-o(\log N)=\log N-o(\log N).
\tag{5.3}
\]

But every member of `B_X` has entropy `o(\log N)`, and there are at most two such helpers. Therefore

\[
H(B_X)=o(\log N),
\]

contradicting (5.3).

So Type B is impossible as well.

---

## 6. CQ7 near-linear obstruction theorem

### Theorem HM-CQ7-NL

No fixed seven-variable conjunctive query can decode exact truncated addition from preprocessing structures of size

\[
N^{1+o(1)}.
\]

Equivalently, the common near-linear CQ width threshold for AL1 and AL2 satisfies

\[
\boxed{k_+=k_{AL1}=k_{AL2}\ge 8.}
\]

Together with the explicit `CQ^9` CRT construction,

\[
\boxed{8\le k_+\le 9.}
\]

Thus only the eight-variable case remains unresolved.

---

## 7. Why no universal exponent formula is claimed

The first attempt was to extrapolate the `CQ^6` exponent `7/6` to a formula depending only on the number `h` of helper variables.

That extrapolation is not currently justified.

With four or more helpers, a free branch may contain serial splitters and purely internal helper variables. These can redistribute one unit of free-variable information among several lower-entropy channels before it interacts with the other branches. A simple count of helpers directly shared between free variables does not control such internal factorization.

The present theorem therefore claims exactly what is proved:

\[
\boxed{\text{near-linear impossibility for }CQ^7,}
\]

not an explicit universal lower exponent `1+c(h)`.

This claim ceiling is important because the `CQ^9` CRT construction shows that no positive lower gap can persist for all fixed helper counts.

---

## 8. Relation to entropy bounds for CQs

The proof uses the same information-theoretic language that appears in standard worst-case size bounds for conjunctive queries with functional dependencies. Gogacz and Torunczyk characterize such CQ size bounds through entropy vectors; the present argument is specialized instead to representation lower bounds for one exact Latin/quasigroup relation and uses its pairwise functional dependencies as a separator obstruction.

The distinction matters: we are not invoking a generic entropy theorem that automatically proves the result. The new ingredient is the branch/separator analysis forced by exact addition.

Reference:

- Tomasz Gogacz, Szymon Torunczyk, *Entropy Bounds for Conjunctive Queries with Functional Dependencies*, ICDT 2017, DOI 10.4230/LIPIcs.ICDT.2017.15.

---

## 9. Current width frontier

The strict near-linear threshold picture is now

\[
\boxed{
\begin{array}{c|ccc}
 k & AL0 & AL1 & AL2\\
\hline
3 & 1 & 2 & 2\\
4 & 1 & 2 & 2\\
5 & 1 & 2 & 2\\
6 & 1 & >1 & >1\\
7 & 1 & >1 & >1\\
8 & 1 & ? & ?\\
9 & 1 & 1 & 1
\end{array}
}
\]

Here `>1` means that near-linear `N^{1+o(1)}` preprocessing is impossible; no exact storage exponent is asserted for `CQ^7`.

The next and now unique sharp problem is:

\[
\boxed{\text{does }CQ^8\text{ already admit near-linear exact addition, or is }k_+=9?}
\]
