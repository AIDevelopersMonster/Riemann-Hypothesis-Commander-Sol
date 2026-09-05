# FCOA Rigidity Cost — Exhaustive Zero-Overhead Frontier

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication exhaustive computation supporting the stronger conjecture `alpha=beta`.

## 1. New quantity

Recall

\[
\beta(D,c)=\text{minimum real-cell cost needed to destroy all old bad automorphisms},
\]

\[
\alpha(D,c)=\text{minimum real-cell cost needed to make the enlarged ternary reduct exact},
\]

and

\[
\eta(D,c)=\alpha(D,c)-\beta(D,c)\ge0.
\]

A positive value `eta>0` would be the first genuine instance of unavoidable symmetry-creation overhead.

## 2. Complete five-carrier result

A fresh independent exhaustive implementation checked the full five-carrier candidate space used in the post-Article-B audit.

After the theorem-level filters (disconnected `Lambda(D)` and nontrivial domain symmetry), the normalized candidate space contains

\[
\boxed{1,629,945}
\]

surjective binary layers.

Among them

\[
\boxed{89,880}
\]

are nonexact.

Every one of those nonexact layers has

\[
\boxed{\beta=\alpha=1.}
\]

Therefore

\[
\boxed{|G|=5\Longrightarrow\eta(D,c)=0.}
\]

Together with the previously exhaustive four-carrier audit, this gives

\[
\boxed{|G|\le5\Longrightarrow\eta(D,c)=0.}
\]

for every finite sparse binary anonymous terminal layer in the audited model.

## 3. Six-carrier frontier through seven defined cells

The same independent implementation was run over every potentially nontrivial normalized six-carrier layer with

\[
|D|\le7.
\]

Candidate layers:

\[
\boxed{9,880,360}.
\]

Nonexact layers:

\[
\boxed{2,587,635}.
\]

Of these,

\[
\boxed{2,587,575}
\]

have

\[
\beta=\alpha=1,
\]

while exactly

\[
\boxed{60}
\]

have

\[
\boxed{\beta=\alpha=2.}
\]

These 60 are the previously identified first genuine two-cell repair states, represented by the three-disjoint-bidirected-pair geometry.

Hence

\[
\boxed{|G|=6,\ |D|\le7\Longrightarrow\eta(D,c)=0.}
\]

## 4. Complete six-carrier layer |D|=8

The next full layer was also exhausted independently.

Potentially nontrivial normalized states at exactly eight defined cells:

\[
\boxed{22,372,320}.
\]

Nonexact states:

\[
\boxed{4,410,000}.
\]

Among them:

\[
\boxed{4,409,640}
\]

have

\[
\beta=\alpha=1,
\]

and exactly

\[
\boxed{360}
\]

have

\[
\boxed{\beta=\alpha=2.}
\]

No positive-overhead state occurs.

Therefore

\[
\boxed{|G|=6,\ |D|\le8\Longrightarrow\eta(D,c)=0.}
\]

## 5. Current exhaustive boundary

The stronger conjecture

\[
\boxed{\alpha(D,c)=\beta(D,c)}
\]

is now exhaustively verified for

\[
\boxed{|G|\le5}
\]

and for

\[
\boxed{|G|=6,\ |D|\le8.}
\]

The first unverified six-carrier layer is

\[
\boxed{|D|=9.}
\]

A direct exhaustive run at `|D|=9` did not complete within the current execution budget and is **not** counted as verified evidence.

## 6. Structural significance

This is materially stronger evidence than the finite audit in Article B. The search now distinguishes old-obstruction repair from full exactness repair and finds no unavoidable symmetry-creation cost on tens of millions of states.

In particular, positive symmetry creation certainly occurs for individual chosen extensions, but every audited layer admits an optimal old-obstruction repair that is also fully exact.

Thus the empirical picture now favors

\[
\boxed{\eta=0}
\]

rather than merely

\[
\boxed{\alpha\le\lambda}.
\]

## 7. Next proof target

The next theoretical target is a **safe optimal-extension theorem**:

> Given a minimum old-obstruction extension of size `beta`, there exists some extension of the same size which destroys all old bad automorphisms and creates no new bad automorphisms.

Equivalently,

\[
\boxed{\alpha=\beta.}
\]

A proof should exploit the freedom to choose both bridge positions and their binary values globally, not rely on monotonicity of domain automorphism groups, which is false.

The computational frontier suggests that the correct obstruction-elimination principle is global orbit separation rather than local color choice.

## 8. Claim firewall

1. The statements above are exhaustive finite computations, not a proof of the global conjecture.
2. The `|D|=9` six-carrier sector is not claimed audited.
3. The counts refer to normalized binary colorings modulo global complement after theorem-level domain filters.
4. Articles A and B remain frozen publications; this note records later research only.
5. The stronger conjecture `alpha=beta` remains open.
