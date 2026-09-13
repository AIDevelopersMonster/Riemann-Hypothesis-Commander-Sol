# HATTER-SOL-11 · Planar Capacity-Six Memory Barrier

**Scope:** orbit-total `Xi=(A,O)` model only.  
**Host:** even `n>=4`.

This note attacks the first unresolved boundary case `(6,5)` after the low-tail theorem. The exact Pareto front of `(6,5)` is not claimed here. What is proved is stronger at the level of response-class separation: once the larger folded coordinate reaches six, the two mixed states and the pure state remain pairwise distinct for every even planar host.

## 1. Exact high-capacity channel floor

For a channel of uniform capacity `h>=6`, every planar graph on `n` vertices satisfies

\[
B_h=nh-2|E|\ge nh-2(3n-6)=n(h-6)+12.
\]

The bounded-degree triangulation `T_n` from `PLANAR_UNIT_TAIL_THEOREM.md` has `3n-6` edges and maximum degree at most six, so coloring all its edges by the capacity-`h` channel attains equality.

### Theorem T11.51

For every even `n>=4` and every integer `h>=6`,

\[
\boxed{\mu_{Pl,n}(h)=n(h-6)+12.}
\]

In particular,

\[
\boxed{\mu_{Pl,n}(6)=12.}
\]

## 2. A sub-twelve witness for every capacity below six

For `q=1,2,3`, the factor ladder from `PLANAR_LOW_TAIL_B_MATCHING_THEOREM.md` gives a spanning `q`-regular subgraph of `T_n`, so a capacity-`q` channel can be saturated and has boundary zero.

For `q=4`, the same holds for even `n>=6`; for `n=4`, using `K_4` gives boundary `4`.

It remains only to produce a capacity-five witness below the capacity-six floor `12`.

For `n=4`, color all edges of `K_4` by the capacity-five channel. Then

\[
B_5=20-12=8<12.
\]

For even `n=2m>=6`, use the triangulation `T_n` built from the `m`-antiprism. Its antiprism skeleton is spanning and `4`-regular. Each of the two polygonal cap faces is triangulated by a zig-zag diagonal path. Choose a matching in each diagonal path and add those chosen diagonals to the `4`-regular skeleton. The resulting spanning subgraph has maximum degree at most five.

Each cap path has `m-3` edges and therefore a matching of size at least `floor((m-2)/2)`. Using such a matching in each cap gives a capacity-five subgraph with at least

\[
2n+2\left\lfloor\frac{m-2}{2}\right\rfloor
\]

edges. Hence

\[
B_5\le n-4\left\lfloor\frac{m-2}{2}\right\rfloor.
\]

For `m>=3` this is at most `8`, and in particular is strictly below `12`.

### Lemma T11.52

For every even `n>=4` and every integer `1<=q<=5`, there exists a connected planar realization in which a capacity-`q` channel has boundary strictly below `12`.

## 3. Rank-swap separation once `P>=6`

Fix an interior pair

\[
P>Q>0,
\qquad P\ge6.
\]

For state `(P,Q)`, Theorem T11.51 gives

\[
\min B_A=n(P-6)+12\ge12.
\]

If `Q>=6`, then for the swapped state `(Q,P)`,

\[
\min B_A=n(Q-6)+12,
\]

and this is strictly smaller because `P>Q`.

If `Q<=5`, Lemma T11.52 gives a feasible swapped realization with axial boundary below `12`, hence below the axial floor of `(P,Q)`. Taking a Pareto-minimal point among realizations with minimum axial boundary shows that this smaller exponent occurs in the response polynomial.

### Theorem T11.53 — capacity-six rank-swap barrier

For every even `n>=4` and every interior pair

\[
P>Q>0,
\qquad P\ge6,
\]

\[
\boxed{Z^\Xi_{Pl,n}(P,Q)\ne Z^\Xi_{Pl,n}(Q,P).}
\]

Thus no planar mixed rank-swap collision is possible once the larger coordinate reaches six.

## 4. Separation from the pure state

Let `S=P+Q`. The pure state `(0,S)` has exact singleton response

\[
\boxed{Z^\Xi_{Pl,n}(0,S)=Y^{n(S-6)+12}}
\]

because `S>=7` and `T_n` attains the planar edge ceiling.

For `(P,Q)`, coloring all edges of `T_n` axial gives the Pareto point

\[
\bigl(n(P-6)+12,nQ\bigr),
\]

which lies on the minimum-total-boundary line

\[
B_A+B_O=n(S-6)+12.
\]

For `(Q,P)`, coloring all edges oblique gives

\[
\bigl(nQ,n(P-6)+12\bigr),
\]

again on the same minimum-total line.

Both mixed states therefore contain a Pareto monomial with positive `X` exponent, while the pure response contains only an `X^0` monomial.

### Theorem T11.54 — permanent three-state memory above six

For every even `n>=4` and every generic-odd interior fiber with

\[
P>Q>0,
\qquad P\ge6,
\]

\[
\boxed{\nu^\Xi_{Pl,n}(P,Q)=3.}
\]

## 5. The boundary case `(6,5)`

In particular,

\[
\boxed{\nu^\Xi_{Pl,n}(6,5)=3}
\]

for every even `n>=4`.

The three states are separated as follows:

- `(6,5)` has minimum axial exponent exactly `12`;
- `(5,6)` has a minimum axial exponent strictly below `12`;
- `(0,11)` is the singleton `Y^{5n+12}`.

The exact complete Pareto front of `(6,5)` is not claimed here.

## 6. Structural conclusion

The planar memory diagram now has a sharp barrier:

\[
\boxed{P\le5:\text{ collisions may occur depending on host scale},}
\]

whereas

\[
\boxed{P\ge6:\text{ every interior fiber keeps three response classes on every even host}.}
\]

The mechanism is the Euler residual `12`: capacity six is the first uniform channel capacity that no finite planar graph can saturate.

The next finer target is therefore not another class-count problem. It is the exact capacity-five floor and the exact `(6,5)` Pareto front as functions of host size.