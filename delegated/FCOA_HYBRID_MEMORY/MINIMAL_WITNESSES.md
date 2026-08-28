# FCOA Hybrid Memory — Minimal Witnesses

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** first internal research checkpoint; not upstreamed; not publication-ready  
**Convention:** this note uses `n=|X|` for the active carrier size, to avoid collision with the main-line parameter `N` in `X_N={P_0,...,P_N}`.

## 1. Automorphism convention

Let `X` be the active carrier. Terminal outputs are anonymous, used, and never accepted as operation arguments. Automorphisms may permute anonymous outputs only when the induced equality partition of operation cells permits it. Equivalently, on the active sort the Fiber-Transport criterion is used.

All groups below are full operation automorphism groups; restriction to `X` is an isomorphism in the displayed witnesses because every terminal output is used and its action is forced by the active permutation.

For Association Spectra we count triples in `X^3`. Since every operation value is terminal and no terminal value is an admissible argument, every double product on an active triple is undefined. Hence every witness below has

\[
(EQ,NEQ,LEFT,RIGHT,NONE)=(0,0,0,0,n^3).
\]

This deliberately removes associativity artifacts from the hybrid-memory effect.

## 2. Minimal carrier theorem

### Theorem HM-0

A balanced hybrid-rigidity witness

\[
\operatorname{Aut}(\oplus)\neq1,
\qquad
\operatorname{Aut}(\otimes)\neq1,
\qquad
\operatorname{Aut}(\oplus,\otimes)=1
\]

requires at least three active points, and three points suffice.

### Proof

For one active point no reduct has a nontrivial active automorphism. For two active points, the only nontrivial subgroup of `S_2` is `S_2` itself. Hence if both reducts are nonrigid, both active automorphism groups contain the unique transposition, so their intersection is nontrivial.

The constructions below realize all three requested synergy mechanisms on three active points. `□`

---

## 3. DD-3 — minimal domain-domain witness

Let

\[
X=\{a,b,c\}.
\]

Define

\[
a\oplus a=\alpha
\]

and no other `\oplus` cell, while

\[
b\otimes b=\beta
\]

and no other `\otimes` cell. The terminal outputs `\alpha,\beta` are distinct operation outputs; each is the unique used value of its own reduct.

### Automorphism groups

The first operation fixes `a` and swaps `b,c`:

\[
\operatorname{Aut}(\oplus)=\langle(b\ c)\rangle\cong C_2.
\]

The second fixes `b` and swaps `a,c`:

\[
\operatorname{Aut}(\otimes)=\langle(a\ c)\rangle\cong C_2.
\]

Therefore

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

The same statements hold after Value-Erasure because the values are constant and all information is already in the two domains:

\[
\operatorname{Aut}(D_\oplus)=C_2,
\qquad
\operatorname{Aut}(D_\otimes)=C_2,
\qquad
\operatorname{Aut}(D_\oplus,D_\otimes)=1.
\]

### Jointly recoverable point

The point `c` is uniformly definable in the joint three-point structure by

\[
C(x)\iff
\neg D_\oplus(x,x)\land\neg D_\otimes(x,x).
\]

It is not recoverable from either reduct alone, because the corresponding nontrivial automorphism moves `c`.

### Passport

- defined cells: `1+1`;
- output alphabet: one used terminal output per operation;
- commutation loci: `{(a,a)}` and `{(b,b)}`;
- translation-profile injectivity: false for each reduct separately; true for the ordered pair of left profiles and also for the ordered pair of right profiles;
- Value-Erasure: survives unchanged;
- external carrier labels: unnecessary; the construction is intrinsic up to isomorphism.

### Cell minimality

If either operation has zero defined cells, its active automorphism group is all of `S_3`; intersecting it with the other required nontrivial automorphism group cannot give `1`. Thus at least one defined cell per operation is necessary. DD-3 attains this lower bound.

---

## 4. DV-3 — minimal clean domain-value witness

Again let

\[
X=\{a,b,c\}.
\]

Keep

\[
a\oplus a=\alpha
\]

as the only `\oplus` cell. Thus `\oplus` contributes pure domain geometry and

\[
\operatorname{Aut}(\oplus)=\langle(b\ c)\rangle\cong C_2.
\]

For `\otimes`, use the maximally symmetric diagonal domain

\[
D_\otimes=\{(a,a),(b,b),(c,c)\}
\]

with two anonymous terminal values:

\[
a\otimes a=\beta_0,
\qquad
b\otimes b=\beta_1,
\qquad
c\otimes c=\beta_0.
\]

The domain alone has

\[
\operatorname{Aut}(D_\otimes)=S_3.
\]

The value fibers have sizes `2` and `1`, so they cannot be exchanged by an automorphism. Hence the singleton fiber fixes `b`, while `a,c` may be swapped:

\[
\operatorname{Aut}(\otimes)=\langle(a\ c)\rangle\cong C_2.
\]

Therefore

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

but after erasing the `\otimes` values,

\[
\operatorname{Aut}(D_\oplus,D_\otimes)
=
\langle(b\ c)\rangle
\cong C_2.
\]

Thus the joint rigidity is genuinely domain-value: domain geometry from `\oplus` is insufficient until the value partition of `\otimes` is restored.

### Jointly recoverable point

Let

\[
A(u)\iff D_\oplus(u,u).
\]

Then `c` is the unique active point satisfying

\[
\neg A(x)
\land
\exists u\bigl(A(u)\land x\otimes x=u\otimes u\bigr).
\]

Again the nontrivial automorphism of either reduct moves `c`, so the singleton is not recoverable from either reduct alone.

### Passport

- defined cells: `1+3`;
- `\otimes` definedness group: `S_3`;
- full groups: `C_2` and `C_2`, with trivial common stabilizer;
- commutation loci: size `1` for `\oplus`, size `3` for `\otimes`;
- translation-profile injectivity: false for `\oplus`, true for `\otimes` on the active carrier;
- Value-Erasure of `\otimes`: destroys hybrid rigidity;
- one output value for `\otimes` would be insufficient, because values would then carry no information beyond definedness.

Among nonempty `S_3`-invariant domains in `X^2`, the diagonal is the smallest, with three cells. Thus this is minimal inside the clean template “first reduct domain-only; second reduct has maximally symmetric nonempty domain and value-only symmetry reduction”.

---

## 5. VV-3 — minimal clean value-value witness

Let both operation domains be the diagonal

\[
\Delta_X=\{(a,a),(b,b),(c,c)\}.
\]

Hence

\[
\operatorname{Aut}(D_\oplus)=
\operatorname{Aut}(D_\otimes)=
\operatorname{Aut}(D_\oplus,D_\otimes)=S_3.
\]

Give `\oplus` the anonymous value partition

\[
a\oplus a=\alpha_1,
\qquad
b\oplus b=c\oplus c=\alpha_0,
\]

and give `\otimes` the transverse partition

\[
b\otimes b=\beta_1,
\qquad
a\otimes a=c\otimes c=\beta_0.
\]

Because each value partition has fiber sizes `1+2`, output swapping is impossible. Thus

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

The domain pair itself remains maximally symmetric. Hence all joint memory here is in the pair of value partitions.

### Jointly recoverable point

Define `U_\oplus(x)` to mean that the diagonal `\oplus`-value of `x` occurs on no other active diagonal cell, and similarly `U_\otimes(x)`. Then

\[
C(x)\iff\neg U_\oplus(x)\land\neg U_\otimes(x)
\]

selects exactly `c`.

Neither reduct alone can recover `{c}`, because its residual transposition moves `c`.

### Passport

- defined cells: `3+3`;
- output alphabet: exactly two used anonymous outputs per operation;
- full groups: `C_2` and `C_2`; joint group `1`;
- definedness groups: `S_3`, `S_3`, and jointly `S_3`;
- commutation locus of each operation: the full diagonal, size `3`;
- translation profiles: injective on the active carrier despite nontrivial automorphisms;
- Value-Erasure of either reduct destroys joint rigidity; erasing both values restores `S_3`.

For a value-only effect, at least two value fibers are necessary. On three points, the diagonal is the smallest nonempty `S_3`-invariant operation domain, so the `3+3` diagonal construction is minimal inside the clean maximally-domain-symmetric value-value template.

---

## 6. Small-case checkpoint

The minimal carrier theorem and the three explicit witnesses give:

| active size `n` | DD witness | DV witness | VV witness |
|---:|:---:|:---:|:---:|
| 1 | impossible | impossible | impossible |
| 2 | impossible | impossible | impossible |
| 3 | yes | yes | yes |

Scalable witnesses for `n=3,4,5` and all larger `n` are recorded separately in `SYNERGY_CLASSES.md`.

## 7. Current conclusion

The first hybrid-memory threshold is already strictly below G3-A/G4-A type single-operation rigidity:

\[
\boxed{
\text{two individually nonrigid partial operations can be jointly rigid on three active points.}
}
\]

Moreover, the phenomenon exists in all three requested forms: domain-domain, domain-value, and value-value.

This is an internal branch result only. It should not enter the main line before hostile audit of the automorphism convention, the minimality qualifiers, and the leakage classification.
