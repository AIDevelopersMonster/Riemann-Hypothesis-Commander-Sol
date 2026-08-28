# FCOA Hybrid Memory — Minimal Witnesses

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** second internal research checkpoint; shared-output minimality classified; hostile audit still required  
**Convention:** `n=|X|` denotes the active carrier size. Terminal outputs lie in a pure common output sort `O`, are anonymous, and are never operation arguments.

## 1. Two output semantics must be separated

There are two mathematically different regimes.

### Independent-output regime

The output alphabets of `\oplus` and `\otimes` are disjoint/typed independently. Then value memory is controlled separately by the two Fiber-Transport partitions.

### Common-output regime

Both operations map into the same anonymous terminal-output sort `O`, and the same output element may occur as a value of both operations. Then equality of values **across operation symbols** is structural information.

This distinction is decisive for minimality.

For Association Spectra below we count triples in `X^3`. Since all displayed values are terminal and no terminal output is an admissible argument, every double product is undefined. Thus each displayed minimal reduct has spectrum

\[
(EQ,NEQ,LEFT,RIGHT,NONE)=(0,0,0,0,n^3).
\]

## 2. Minimal active-carrier theorem

### Theorem HM-0

A balanced hybrid-rigidity witness

\[
\operatorname{Aut}(\oplus)\ne1,
\qquad
\operatorname{Aut}(\otimes)\ne1,
\qquad
\operatorname{Aut}(\oplus,\otimes)=1
\]

requires at least three active points, and three points suffice.

For `n=2`, every nontrivial active automorphism subgroup is the unique `S_2`; hence two nonrigid reducts cannot have trivial common active action. The examples below realize the threshold at `n=3`.

---

## 3. DD-3 — domain-domain minimum

Let

\[
X=\{a,b,c\}.
\]

Define only

\[
a\oplus a=\alpha,
\qquad
b\otimes b=\beta,
\]

with anonymous terminal outputs.

Then

\[
\operatorname{Aut}(\oplus)=\langle(b\ c)\rangle\cong C_2,
\]

\[
\operatorname{Aut}(\otimes)=\langle(a\ c)\rangle\cong C_2,
\]

and

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

Value-Erasure changes nothing. Total defined-cell cost is `1+1=2`, which is minimal because an empty reduct contributes no restriction capable of killing the other reduct's required nontrivial symmetry.

The point `c` is jointly definable by

\[
\neg D_\oplus(x,x)\land\neg D_\otimes(x,x).
\]

Neither reduct alone defines `{c}`, since its residual transposition moves `c`.

---

## 4. A general lower bound for value memory inside one operation

### Lemma HM-V2

Let a partial operation have at most two defined cells and anonymous terminal outputs. Restoring its values cannot reduce the active automorphism group of its definedness reduct.

### Proof

Values contribute only the equality partition of the defined cells. A set of size `0` or `1` has only one partition. A set of size `2` has only the indiscrete partition and the discrete partition; both are invariant under every permutation of the two cells. Therefore every automorphism of the domain preserves the value-equality partition. `□`

Consequently, in the **independent-output regime**, any operation that contributes genuine value rigidity needs at least three defined cells.

---

## 5. DV-I-3 — strict domain-value minimum with independent outputs

Let

\[
a\oplus a=\alpha
\]

be the only `\oplus` cell. For `\otimes`, take the diagonal domain and a `2+1` anonymous value partition:

\[
a\otimes a=\beta_0,
\qquad
b\otimes b=\beta_1,
\qquad
c\otimes c=\beta_0.
\]

Then

\[
\operatorname{Aut}(\oplus)=\langle(b\ c)\rangle\cong C_2,
\]

\[
\operatorname{Aut}(D_\otimes)=S_3,
\qquad
\operatorname{Aut}(\otimes)=\langle(a\ c)\rangle\cong C_2,
\]

so

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

while erasing the `\otimes` values restores a nontrivial joint domain automorphism.

By Lemma HM-V2 the value-bearing reduct needs at least three cells; the other reduct must contribute at least one domain cell to kill its residual nontrivial symmetry. Hence

\[
\boxed{1+3=4}
\]

is the global cell minimum for **strict DV with independent output alphabets**.

---

## 6. VV-I-3 — strict value-value minimum with independent outputs

Take both domains equal to the diagonal `\Delta_X` and use transverse `2+1` value partitions:

\[
a\oplus a=\alpha_1,
\qquad
b\oplus b=c\oplus c=\alpha_0,
\]

\[
b\otimes b=\beta_1,
\qquad
a\otimes a=c\otimes c=\beta_0.
\]

Then each definedness group is `S_3`, each full reduct has automorphism group `C_2`, and their active carrier actions are transverse:

\[
\operatorname{Aut}(\oplus)=\langle(b\ c)\rangle,
\qquad
\operatorname{Aut}(\otimes)=\langle(a\ c)\rangle,
\]

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

By Lemma HM-V2 each independently value-sensitive operation needs at least three cells. Thus

\[
\boxed{3+3=6}
\]

is the cell minimum for **VV with independent output alphabets**.

This corrects the earlier wording: the diagonal construction is not merely minimal inside a clean template; it is minimal in the independent-output regime.

---

## 7. JFS-3 — shared-output synchronization beats the three-cell-per-operation wall

The independent-output lower bound is **not** the global lower bound once outputs may be shared across operations.

Let

\[
X=\{a,b,c\},
\qquad
O=\{u,v\}.
\]

Define exactly three cells:

\[
\boxed{a\oplus a=u,}
\]

\[
\boxed{b\otimes b=u,\qquad c\otimes c=v.}
\]

All other cells are undefined. The outputs are anonymous; neither `u` nor `v` is named.

### Individual reducts

For `\oplus`, the active transposition

\[
r=(b\ c)
\]

preserves the unique domain cell and forces `u` to remain fixed. Since `O={u,v}`, it also fixes `v`. Hence

\[
\operatorname{Aut}(\oplus)\cong C_2.
\]

For `\otimes`, the same active transposition survives only together with

\[
u\leftrightarrow v.
\]

Hence

\[
\operatorname{Aut}(\otimes)\cong C_2.
\]

The two **active projections coincide**:

\[
\pi_X\operatorname{Aut}(\oplus)
=
\pi_X\operatorname{Aut}(\otimes)
=\langle r\rangle.
\]

### Joint reduct

In the joint structure the same output permutation must serve both operation symbols. But `\oplus` requires

\[
u\mapsto u,
\]

while the nontrivial `\otimes` lift requires

\[
u\mapsto v.
\]

These requirements are incompatible. Therefore

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

although

\[
\boxed{
\operatorname{Aut}(D_\oplus,D_\otimes)
\cong C_2.
}
\]

This is genuinely value-induced joint rigidity.

### Double Value-Erasure test

Erase the values of `\oplus` but retain its domain: the transposition `r` survives using the `\otimes` output swap.

Erase the values of `\otimes` but retain its domain: `r` survives because the singleton `\oplus` value imposes no carrier distinction between `b,c`.

Thus

\[
\boxed{
\text{erasing either operation's value layer restores }C_2.
}
\]

The mechanism is therefore a genuine **shared-output value-value synchronization** effect, even though one reduct has only one defined cell.

### Jointly recoverable active points

`a` is the unique active point with a `\oplus` loop. Among the two `\otimes`-loop points, `b` is characterized by equality with the `\oplus` output:

\[
B(x)\iff
D_\otimes(x,x)
\land
\exists y\,
\bigl(D_\oplus(y,y)\land x\otimes x=y\oplus y\bigr).
\]

Then `c` is the other `\otimes`-loop point. Neither reduct alone separates `b` from `c`.

### Passport

- active carrier: `3` points — minimal;
- total defined cells: `1+2=3`;
- global used output alphabet: `|O|=2` — minimal;
- individual full groups: `C_2`, `C_2`;
- joint definedness group: `C_2`;
- joint full group: `1`;
- commutation loci: one diagonal pair for `\oplus`, two for `\otimes`;
- Association Spectrum of each reduct on `X^3`: `(0,0,0,0,27)`;
- `\oplus` translation profiles are not injective; `\otimes` left/right profiles are injective on `X`;
- no named anchor and no external carrier order are used.

---

## 8. Global three-cell lower bound for any value-induced joint effect

### Theorem HM-JV3

In the relative typed setup with a common anonymous terminal-output sort, any genuinely value-induced joint rigidity requires at least **three total defined cells across all operation symbols**.

### Proof

Tag each operation cell by its operation symbol and take the disjoint union `T` of all defined cells. All value information is the equality partition `\equiv_c` of `T` induced by the common output map.

If `|T|\le2`, every set partition of `T` is invariant under every permutation of `T`. Hence restoring values cannot shrink the joint definedness automorphism group. Therefore no value-induced joint effect exists with at most two total cells.

JFS-3 has `|T|=3`, so the bound is sharp. `□`

Thus the global resource threshold is

\[
\boxed{
2\text{ cells for pure DD},
\qquad
3\text{ cells for any genuinely value-induced joint memory}.
}
\]

---

## 9. Complete classification at the three-cell value threshold

For `|X|=3`, impose:

1. both reducts are nonrigid;
2. the joint definedness reduct is nonrigid;
3. the joint valued structure is rigid;
4. there are exactly three tagged defined cells in total.

Then, up to relabeling `X`, every witness has cell split `1+2` or `2+1`.

The one-cell domain must be a loop, say `(a,a)`, because one off-diagonal ordered cell already fixes all three active points. Its residual symmetry is `r=(b c)`.

The two-cell domain must be one two-element orbit of `r`. There are exactly four geometric possibilities:

\[
\{(a,b),(a,c)\},
\]

\[
\{(b,a),(c,a)\},
\]

\[
\{(b,b),(c,c)\},
\]

\[
\{(b,c),(c,b)\}.
\]

On the three tagged cells, the only partition capable of killing `r` has type `2+1` and pairs the singleton-operation cell with exactly one cell of the two-cell operation. Therefore a cross-operation shared output is necessary.

An exhaustive `S_3` search confirms:

\[
\boxed{48\text{ labeled witnesses}}
\]

and

\[
\boxed{8\text{ isomorphism classes with operation symbols distinguished}.}
\]

These are the four geometries above and the four obtained by exchanging `\oplus` and `\otimes`.

## 10. Revised minimality table

| mechanism / semantics | minimum active points | minimum total cells | minimum value-bearing cells | status |
|---|---:|---:|---:|---|
| DD | 3 | 2 = 1+1 | 0 | sharp |
| DV, independent outputs | 3 | 4 = 1+3 | 3 in one reduct | sharp |
| VV, independent outputs | 3 | 6 = 3+3 | 3 in each reduct | sharp |
| shared-output value synchronization | 3 | 3 = 1+2 | global 3-cell partition | sharp |

## 11. Current conclusion

The attempted attack on the old DV/VV minimality succeeded in a precise way.

The three-diagonal-cell lower bound is real **inside one anonymous-output reduct** and therefore remains exact for independent-output DV/VV. But it is not the global hybrid lower bound. A common anonymous output sort permits cross-operation fiber equality, and this creates a new three-cell synchronization mechanism:

\[
\boxed{
\pi_X\operatorname{Aut}(\oplus)\cap
\pi_X\operatorname{Aut}(\otimes)
\ne1
\quad\text{while}\quad
\operatorname{Aut}(\oplus,\otimes)=1.
}
\]

The obstruction is not transverse carrier symmetry. It is **incompatible lifting of the same carrier symmetry to the shared output sort**.
