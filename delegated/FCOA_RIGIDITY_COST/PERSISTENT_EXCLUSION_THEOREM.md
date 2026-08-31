# FCOA Rigidity Cost — Persistent Exclusion Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication theorem note.

## 1. Setup

Assume

\[
\beta(D,c)=1.
\]

Let `e` be an **anchored beta-killing cell**. Put

\[
S=D\cup\{e\}.
\]

Let `b in F_2` be the color assigned to `e`.

A carrier permutation `h` is called a **persistent replacement obstruction for e** if:

1. `h` preserves the uncolored singleton domain `S`;
2. `h(D) != D`;
3. `h` is a bad automorphism of the ternary reduct for both color choices `b=0` and `b=1`.

The purpose of this note is to show that such an `h` cannot exist.

## 2. Variable-coefficient cells

Fix a domain-moving `h in Aut(G;S)`. Since `S=D union {e}` and `h(D) != D`, there is a unique old cell

\[
p=h(e)\in D
\]

and a unique old cell

\[
q=h^{-1}(e)\in D.
\]

For a cell `x in S`, define the discrepancy

\[
\delta_h^b(x)=c_b(hx)\oplus c_b(x),
\]

where `c_b` extends the old coloring by `c_b(e)=b`.

As a function of the single variable `b`, the discrepancy has coefficient 1 exactly at

\[
\boxed{e\text{ and }q=h^{-1}(e),}
\]

and coefficient 0 on every other cell of `S`.

## 3. Two-color survival forces a two-cell incidence component

### Lemma 3.1

If `h` preserves the ternary reduct for both values `b=0,1` and `e` is anchored, then

\[
\boxed{
C_e=\{e,q\}
}
\]

is a connected component of `Lambda(S)`.

Moreover

\[
\boxed{p=q,}
\]

so `h` swaps the two cells `e` and `p`.

### Proof

For either color, reduct preservation is equivalent to discrepancy constancy on each connected component of `Lambda(S)`.

Because this must hold **as an identity in the variable b**, all discrepancy functions on one incidence component must have the same coefficient of `b`.

The only coefficient-1 cells are `e` and `q`. Since `e` is anchored, its component contains an old cell. Therefore that old cell must be `q`, and no coefficient-0 cell can lie in the same component. Hence

\[
C_e=\{e,q\}.
\]

Because `h` is an automorphism of the fixed incidence graph `Lambda(S)`, it maps `C_e` to another connected component:

\[
h(C_e)=\{h(e),h(q)\}=\{p,e\}.
\]

The image component contains `e`, so it must equal `C_e`. Therefore `p=q`. `square`

## 4. The replacement cell is the reverse old cell

Write

\[
p=(a,b).
\]

Since `C_e={p,e}` is connected, `p` and `e` are composable. Since `h` swaps `p` and `e`, the carrier action satisfies `h^2(p)=p`.

### Lemma 4.1

Under these conditions,

\[
\boxed{e=(b,a),}
\]

and `h` swaps the carrier points `a` and `b`.

### Proof

Let

\[
e=h(p)=(h(a),h(b)).
\]

Composability of `p=(a,b)` and `e` gives either

\[
b=h(a)
\]

or

\[
h(b)=a.
\]

Since `h^2(p)=p` as an ordered cell,

\[
h^2(a)=a,\qquad h^2(b)=b.
\]

Either composability relation therefore forces

\[
h(a)=b,\qquad h(b)=a.
\]

Hence

\[
e=(b,a).
\]
`\square`

## 5. The endpoints are absent from the rest of the old domain

Since `C_e={p,e}` is a full incidence component of `Lambda(S)`, the old cell `p=(a,b)` has no old composability neighbour. Therefore:

- no old cell ends at `a`;
- no old cell starts at `b`.

Because `h` maps `D\setminus\{p\}` to itself and swaps `a,b`, two further incidences are impossible:

- if an old cell started at `a`, its image would start at `b`, contradicting the previous bullet;
- if an old cell ended at `b`, its image would end at `a`, again a contradiction.

Thus the carrier points `a,b` occur in the old domain only in the single cell `p=(a,b)`.

Consequently

\[
\boxed{
D=\{p\}\sqcup D_0
}
\]

where every cell of `D_0` is supported on `G\setminus\{a,b\}`.

## 6. Extracting an old bad automorphism

Define a new carrier permutation `g` by

\[
g(a)=a,\qquad g(b)=b,
\]

and

\[
g(x)=h(x)\qquad(x\notin\{a,b\}).
\]

Because no cell of `D_0` uses `a` or `b`, `g` preserves `D_0` exactly as `h` does, while `g` fixes `p`. Hence

\[
gD=D.
\]

On every incidence component contained in `D_0`, the discrepancy of `g` equals that of `h` and is therefore constant. On the isolated old component `{p}`, the discrepancy of `g` is 0. Thus

\[
\boxed{g\in A_Q(D,c).}
\]

## 7. Persistence for both colors forces g to be old-bad

For the two-cell component `{p,e}`, the phase of `h` is

\[
\theta_e(b)=c(p)\oplus b,
\]

so it takes both values 0 and 1 as `b` varies.

All phases of `h` on the remaining old-only components are independent of `b`.

If those remaining component phases were all equal to one common bit `theta`, then choosing the unique color `b` with

\[
c(p)\oplus b=\theta
\]

would make every component phase equal, so `h` would be globally anonymous for that color. This contradicts persistent badness for **both** colors.

Therefore the remaining old-only components realize both phase values 0 and 1.

The extracted old automorphism `g` has phase 0 on `{p}` and the same two-valued phase pattern as `h` on the remaining components. Hence

\[
\boxed{g\in B_{old}(D,c).}
\]

## 8. The contradiction with beta-killing

The same extracted `g` fixes the new cell `e=(b,a)` because it fixes both carrier endpoints `a,b`.

On the enlarged two-cell component `{p,e}`, `g` has discrepancy 0 on both cells. On every other component its discrepancy is the same constant component phase as before. Therefore `g` preserves the ternary reduct after adding `e`.

Thus the supposedly beta-killing cell `e` fails to destroy the old bad automorphism `g`.

Contradiction.

This proves the main theorem.

## 9. Main theorem

### Theorem 9.1 — Persistent Exclusion

Let `e` be an anchored beta-killing singleton cell. Then there is no domain-moving carrier permutation which is bad for both binary colors of `e`.

Equivalently,

\[
\boxed{
B_0\cap B_1=\varnothing
}
\]

for the bad replacement sets of the two singleton colorings.

Therefore **Type P persistent fatality is impossible** for anchored beta-killing cells.

## 10. Consequence: anchored fatality is purely split

Combining Theorem 9.1 with `BETA_ONE_FATAL_GEOMETRY_CLASSIFICATION.md` gives:

### Corollary 10.1

If an anchored beta-killing cell is fatal for both colors, the fatality must be Type S (split-color): distinct replacement cosets defeat the two colors separately.

In particular,

\[
\boxed{
[\Gamma_e:H_e]\ge3.
}
\]

Thus the one-cell obstruction problem has been reduced from two mechanisms to exactly one.

## 11. Updated beta-one counterexample conditions

Any counterexample to

\[
\beta=1\Longrightarrow\alpha=1
\]

must now satisfy:

1. at least three old incidence components;
2. every anchored beta-killing cell lies in `R_1(D)`;
3. every anchored beta-killing cell has replacement index at least three:
   \[
   [\Gamma_e:H_e]\ge3;
   \]
4. for each such cell, one nontrivial replacement coset is bad only for color 0 and a distinct coset is bad only for color 1;
5. isolated beta-killing cells, if used, must remain trapped by the isolated phase-safety obstruction or replacement geometry.

This is substantially narrower than danger saturation alone.

## 12. Next target

The only remaining anchored beta-one mechanism is **Split Exclusion**.

The next theorem target is therefore:

> show that an anchored beta-killing singleton extension cannot have two distinct defect-one replacement cosets whose bad-color sets are exactly `{0}` and `{1}`.

A proof would establish exactness of at least one color on every anchored beta-killing cell and would reduce the full beta-one theorem to the isolated-cell sector.

## Claim firewall

1. Persistent Exclusion is proved only for anchored beta-killing singleton cells.
2. Persistent bad symmetries can still occur for isolated singleton cells; the earlier unsafe witness is of this type.
3. The split-color mechanism remains open.
4. The global implication `beta=1 => alpha=1` remains open.
