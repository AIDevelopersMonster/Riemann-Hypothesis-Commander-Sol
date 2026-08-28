# FCOA Branch Passport Laboratory — Upstream Memo

**Rounds:** P0–P3  
**Audience:** main Commander Sol scientific director

## U3-01 — STRONGER ABSOLUTE TWO-OUTPUT THEOREM FOUND

The P2 question is now answered positively.

There exists a pure family of partial operations with total terminal-output carrier exactly

`O={Omega_+,Omega_-}`

for every carrier size `n`, yet with factorial Value-Rigidity Index.

Let `X_n={x_1,...,x_n}` and define on distinct pairs

`x_i star x_j = Omega_+` for `i<j`,

`x_i star x_j = Omega_-` for `i>j`,

with diagonal undefined.

Then

`Aut(D|X_n) ~= S_n`,

because definedness is simply inequality, while

`Aut(star) ~= C2`,

because a full automorphism must either preserve the finite linear orientation (identity) or reverse it while swapping the two anonymous outputs (unique reversal).

Therefore

`VRI(star)=n!/2`.

This proves the absolute statement:

> A globally bounded total terminal-output alphabet of size two can support factorially unbounded value-induced rigidity.

No growing M0 terminal-output families are needed for this absolute cardinality theorem.

### Anchored rigid variant

Add only

`x_1 star_A x_1 = Omega_+`.

The same total output carrier of size two is retained. Definedness now fixes `x_1` and otherwise allows arbitrary permutations, so

`Aut(D_A|X_n) ~= S_{n-1}`.

The unique nontrivial full symmetry of the unanchored structure, reversal, is destroyed by the anchor. Hence

`Aut(star_A)=1`,

`VRI(star_A)=(n-1)!`.

Thus two total terminal outputs suffice even for a rigid full operation with factorial VRI.

### Independent finite check

Formula-blind exhaustive enumeration for `n=3..7` gives:

- unanchored `(DefAut,FullAut)` = `(6,2),(24,2),(120,2),(720,2),(5040,2)`;
- anchored = `(2,1),(6,1),(24,1),(120,1),(720,1)`.

The proof and finite data agree exactly.

## U3-02 — One-sorted caveat survives cleanly

In the one-sorted universe `U_n=X_n disjoint_union O`, base elements are precisely those that occur as operation arguments; the two output elements never occur as arguments. Hence the active/output partition is internally recoverable for `n>=3` and no hidden sort naming is required.

After value erasure the isolated output pair contributes an independent `S_2`, while in the full operation its swap must be coupled to base reversal. Thus the active-sort VRI is `n!/2`; a separate full one-sorted order ratio would be `n!`. These invariants must remain distinguished.

## U2-01 — G4 theorem-scope repair remains required

The new pure theorem does not retroactively make the original M0-relative G4 phrase `bounded total output alphabet` correct. G4 itself has `2N` terminal outputs because of inherited `E_i^*`,`E_i^x` families. Its safe statement remains `two added anonymous orientation values over M0`.

The pure P3 theorem is a separate stronger absolute output-cardinality result and should be imported upstream as a new checkpoint, not used to blur the G4 accounting.

## U2-02 — Translation-fingerprint proof of G4

For generic `P_i`, the G4-C orientation multiplicity fingerprint is `{i-2,N-i}`, determining the point up to global reversal. The G4-A anchor orders the pair and determines every generic point uniquely. This gives an independent proof route to `C2` and then `1`.

## Director recommendation

P3 has crossed the threshold for upstream mathematical consideration. Recommended architecture:

1. repair G4 wording to `bounded added two-value layer over M0`;
2. retain G4 as the backbone-relative theorem;
3. add the pure two-output construction as a distinct absolute theorem/checkpoint;
4. keep active-sort VRI and full one-sorted ratio explicitly separate.

The next hard question is no longer whether constant total output cardinality permits factorial VRI — it does. The sharper frontier is minimality:

> Is two terminal outputs minimal for unbounded VRI, and what is the maximal VRI growth possible with exactly one terminal output?

That is now the natural next strike.
