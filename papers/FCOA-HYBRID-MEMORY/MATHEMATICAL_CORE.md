# Mathematical core — Article A

This file is the claim ledger for the published manuscript. A theorem may appear in the paper only if its proof is present in the manuscript or explicitly computer-assisted with released verification code.

## T1 — Sharp DD cost

**Claim.** Pure domain–domain balanced hybrid rigidity has absolute total cell minimum 2.

**Witness.** On `X={a,b,c}`:

\[
a\star a=\alpha,\qquad b\diamond b=\beta.
\]

The active groups are `<(b c)>` and `<(a c)>`; their intersection is trivial. One total cell cannot suffice because one operation would be empty and hence a spectator.

**Proof status:** complete, manuscript.

## T2 — Typed Lift-Compatibility

For active sort `X`, common pure terminal output sort `O`, tagged domain union `T`, globally surjective value map `c:T→O`, and joint definedness group `Γ_D`,

\[
Aut(X,O;\star_1,\ldots,\star_k)\cong Stab_{\Gamma_D}(\equiv_c).
\]

For non-surjective output maps, the exact active projection is

\[
\{g\in\Gamma_D:\bigcap_i L_i(g)\ne\varnothing\}.
\]

**Proof status:** complete, manuscript.

**Novelty boundary:** stabilizer/equalizer/fiber-product principles are not claimed as new; the FCOA-specific contribution is the tagged-operation formulation and its threshold consequences.

## T3 — JFS-3 and sharp typed value threshold

Typed common-output witness:

\[
a\star a=u,\quad b\diamond b=u,\quad c\diamond c=v.
\]

Each reduct has a surviving carrier `C2`; the forced output lifts are incompatible; the joint structure is rigid.

With at most two tagged cells, every equality partition is invariant under every cell permutation, so values cannot shrink the joint definedness group. Therefore 3 is sharp.

**Proof status:** complete, manuscript.

## T4 — JFS-2 Pareto point

On two active points, the common-output construction with two loop cells per operation is balanced and rigid. Four cells are necessary because the transposition orbits on `X²` both have size 2, and both operations must have nonempty invariant domains.

**Proof status:** complete, manuscript.

## T5 — Independent-output thresholds

Under independent terminal outputs:

- DV: sharp `1+3=4`;
- VV, requiring each operation separately to be value-sensitive: sharp `3+3=6`.

Lower bound: a value partition on at most two cells cannot shrink a domain automorphism group. Explicit 3-point transverse constructions attain the bounds.

**Proof status:** complete, manuscript.

## T6 — Absolute one-sorted two-cell theorem

On `U={a,u,v,w}`:

\[
a\star a=u,\qquad a\diamond a=v.
\]

Then

\[
Aut(\star)\cong C_2,\qquad Aut(\diamond)\cong C_2,\qquad Aut(\star,\diamond)=1,
\]

joint definedness is `S3`, and either one-sided value erasure leaves `C2`. Zero or one total cell cannot produce balanced joint rigidity.

**Proof status:** complete, manuscript.

## T7 — Computer-assisted one-sorted classification

Exact scope: two distinguished binary partial-operation symbols; exactly one defined cell per operation; strong VV/erasure conditions.

Counts:

- n=2: 0 witnesses;
- n=3: 0 witnesses;
- n=4: 24 labeled witnesses; 1 isomorphism class.

**Proof status:** exhaustive released verifier with hard assertions.

## T8 — Computer-assisted typed JFS-3 classification

Exact scope: n=3 active points; common pure terminal output sort; exactly 3 tagged cells split 1+2 or 2+1; nonrigid individual valued reducts; nonrigid joint definedness; nontrivial separate-fiber stabilizer; rigid global-fiber structure.

Count: 48 labeled witnesses; 8 operation-preserving isomorphism classes.

**Proof status:** exhaustive released verifier with hard assertions.

## T9 — CVS selector ladder

For

\[
U_m=\{a,v_1,\ldots,v_m,w\},\qquad a\star_i a=v_i,
\]

restoring exactly `r` value layers yields residual group

\[
S_{m+1-r}.
\]

Every layer is essential; each individual operation has group `S_m`; the common-loop template needs at least `m` selectors for rigidity.

**Proof status:** complete, manuscript.

## Excluded claims

No Article A theorem claims uniform order, successor, EqGap, addition, multiplication, AL0/AL1/AL2 cost, CRT compression, RTP invariance, or superlinear resource barriers.