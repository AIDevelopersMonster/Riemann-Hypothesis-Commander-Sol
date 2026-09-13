# HATTER-SOL-11 · Orbital Port Filtrations

Branch: `research/hatter-sol-orbital-port-filtrations`

Base: merged `main` after HATTER-SOL-07--10 publication chain.

Status: open research branch.

## Central question

Does a factor or minimal principalization witness carry a **canonical filtration of port orbits** that refines the HATTER-SOL typed capacity pair?

The target architecture is

\[
I
\longrightarrow
\mathscr W(I)
\longrightarrow
\mathcal O(\alpha)
\longrightarrow
F_1\subset F_2\subset\cdots
\longrightarrow
(P,Q)
\longrightarrow
\text{network response}.
\]

The words `orbit`, `stronger`, `weaker`, and `activation` are not assumptions. They must be derived from an intrinsic symmetry action or rejected.

## First hostile target

Before constructing any activation law, try to falsify the naive claim:

> The folded pair `(P,Q)` canonically comes from an ordered pair of port orbits in which the `P`-orbit is intrinsically stronger and must be saturated before the `Q`-orbit activates.

Search first for counterexamples showing that:

1. different symmetry-compatible coordinate choices exchange the proposed orbit ranking;
2. the stabilizer acts transitively on directions that the `(P,Q)` projection separates;
3. two witnesses with the same folded `(P,Q)` have non-isomorphic internal port-orbit structure;
4. an apparent strongest-first law depends on a chosen basis, embedding, metric, or weight rather than arithmetic structure.

If any of these occur, the naive filtration is not canonical and must be replaced by a weaker invariant.

## Candidate canonical data

For a witness `alpha`, possible intrinsic objects to test include:

- the unit/conjugation stabilizer of the witness orbit;
- the action of that stabilizer on primitive interface directions;
- orbit sizes and stabilizer indices;
- norm shells and shortest-step classes;
- incidence relations among direction orbits;
- principalization companion ideals and their automorphism action.

No ranking is accepted merely from numerical inequalities such as `P>=Q`.

## Mandatory recovery condition

Any successful orbital-port object `O(alpha)` must admit a well-defined forgetting map

\[
\boxed{
\mathcal O(\alpha)\longrightarrow\Pi(\alpha)=(P,Q)
}
\]

that exactly recovers the HATTER-SOL-09/10 typed model.

Thus HATTER-SOL-11 must refine, not replace, the published theory.

## First laboratory

Start with the nonprincipal prime ideal in

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
\omega=\frac{1+\sqrt{-15}}2,
\]

from HATTER-SOL-10:

\[
\mathfrak q=(23,\omega-7),
\]

with minimal witness states

\[
S=(3,2),
\qquad
T=(6,1).
\]

Determine whether their different host-size behavior can be explained by distinct canonical port-orbit structures, or whether `(P,Q)` already exhausts the invariant information visible to the natural symmetry group.

The HATTER-SOL-10 observation

\[
(6,1)=(5,0)+(1,1),
\qquad
(3,2)=(1,0)+(2,2)
\]

is only a heuristic decomposition and is **not** to be treated as a theorem.

## Publication discipline

Do not claim:

- a canonical port hierarchy without proving basis/symmetry invariance;
- strongest-first activation from the inequality `P>=Q` alone;
- new group-action facts that are standard orbit/stabilizer theory;
- a physical interpretation where only a combinatorial filtration has been proved.

A publishable HATTER-SOL-11 result requires at least one of:

1. a canonical nontrivial orbit filtration with an exact forgetting theorem;
2. a no-go theorem proving that no such filtration can be recovered from the natural symmetry data under stated axioms;
3. a classification theorem identifying precisely when an ordered port-orbit hierarchy exists.

## Immediate next step

Compute the natural symmetry/stabilizer actions for the `Q(sqrt(-15))` laboratory and attack the naive ordered-orbit hypothesis by counterexample first.