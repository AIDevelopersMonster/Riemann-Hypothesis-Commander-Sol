# HATTER-SOL-15 · Two-Port Sector Theorems

Let

\[
G=D_{2p}=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle,
\]

with `p` an odd prime, and let

\[
D=\langle s\rangle.
\]

Identify the right-coset sector space

\[
X=D\backslash G
\]

with `F_p` by

\[
i\longleftrightarrow Dr^i.
\]

Let the two labelled ports be right multiplication by `r` and `s`, denoted `R` and `S`.

## Theorem H15.1 — exact two-port action

On `F_p`,

\[
R(i)=i+1,
\qquad
S(i)=-i.
\]

Hence every word in the two ports induces exactly one of the affine maps

\[
\boxed{i\mapsto i+a}
\]

or

\[
\boxed{i\mapsto -i+a}
\]

for some `a in F_p`.

### Proof

Right multiplication by `r` gives

\[
Dr^i r=Dr^{i+1}.
\]

Using `r^i s=s r^{-i}` and `Ds=D`,

\[
Dr^i s=Ds r^{-i}=Dr^{-i}.
\]

The two transformations `i -> i+1` and `i -> -i` generate precisely the affine dihedral transformations `i -> +/- i+a`. QED.

## Corollary H15.2 — fixed-sector classification

For a nonidentity word action:

- a nontrivial translation `i -> i+a`, `a != 0`, has no fixed sector;
- a reflection-type action `i -> -i+a` has exactly one fixed sector, namely

\[
\boxed{i=a/2}.
\]

The identity fixes all `p` sectors.

Thus every nontrivial local closure test detects either zero sectors or exactly one sector.

## Theorem H15.3 — two-port sector identification

For each `j in F_p`, consider the word

\[
w_j=R^jS.
\]

Its action is

\[
i\mapsto -(i+j).
\]

Therefore

\[
w_j(i)=i
\iff
2i+j=0.
\]

Since `p` is odd, `2` is invertible modulo `p`, so for every sector `i` there is a unique closure word

\[
\boxed{w_{-2i}}
\]

that fixes it.

Equivalently, the family of two-port closure tests gives a structural address for every sector without attaching an external label to the vertex.

## Theorem H15.4 — exact closure-only identification complexity

Suppose an observer is allowed only binary tests of the form

\[
\delta_w(i)=\mathbf 1_{\{w(i)=i\}}
\]

for words `w(R,S)`.

Then at least

\[
\boxed{p-1}
\]

nontrivial closure tests are necessary to distinguish all `p` sectors, and `p-1` tests are sufficient.

### Proof

By H15.2, every useful nonidentity test is `1` on exactly one sector and `0` on every other sector. With `q` such tests, at most `q` sectors can receive a signature containing a `1`; every remaining sector has the all-zero signature. Hence at most `q+1` distinct sector signatures are possible. To distinguish `p` sectors one needs

\[
q+1\ge p,
\]

so `q>=p-1`.

Conversely choose reflection words fixing `p-1` distinct sectors. Those sectors are distinguished by their unique `1`, while the remaining sector has the all-zero signature. Hence `p-1` tests suffice. QED.

## Interpretation

Two labelled noncommuting ports generate all sector motions, but pure closure observation is deliberately weak: one nontrivial word can single out at most one sector. Thus non-abelianity creates exact structural addressing, while H15.4 quantifies the observational cost of recovering the full sector identity from closure bits alone.