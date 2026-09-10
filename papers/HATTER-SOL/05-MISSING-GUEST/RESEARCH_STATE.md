# HATTER-SOL-05 · RESEARCH STATE

## Working title

**«Кого нет за столом? Пустые волокна, спектр точных опор и выживание перестановки 3↔5»**

English working title:

**“Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the 3↔5 Swap.”**

## Why a fifth paper is justified

HATTER-SOL-04 established a structural theorem package for the directed prime graph

\[
\Pi=(\mathbb P,D),\qquad D(q,p)\iff q\mid p-1,
\]

but deliberately left open whether

\[
\operatorname{Aut}(\Pi)=\{\mathrm{id}\}.
\]

The multiplicity-tower theorem showed that the obstruction is encoded by exact predecessor fibers

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

The fifth paper therefore should not add more general corollaries about hypothetical automorphisms. It should attack the arithmetic core directly.

## Primary seed symmetry

The first nontrivial local symmetry is

\[
\tau=(3\ 5),
\]

because

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

At the next layer, \(\tau\) survives if and only if all corresponding exact-support multiplicities match.

The sharp first target is therefore:

\[
\boxed{
\exists S\quad
\mu(S)\ne\mu(\tau S)?
}
\]

The strongest witness would be

\[
\boxed{
\mu(S)=0,
\qquad
\mu(\tau S)>0
}
\]

or the reverse.

Such a witness would be an unconditional finite-height killing certificate for the first Fermat-prime transposition.

## Arithmetic form

For a finite support \(S\ni2\),

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:e_q\ge1
\right\}.
\]

Thus the problem becomes a comparison of prime values in shifted finite-prime semigroups.

The simplest pair already asks for comparison between

\[
1+2^a3^b
\]

and

\[
1+2^a5^b,
\]

with positive exponents and exact support conditions.

The first family is closely related to Pierpont primes; infinitude is not known. Therefore the strategy must avoid assuming exact global cardinalities unless they can be proved.

## First attack programme

### Strike A — empty-fiber search

Search for supports \(S\) for which all numbers

\[
1+\prod_{q\in S}q^{e_q}
\]

are composite, using covering congruences or other uniform modular obstructions.

If \(X_S=\varnothing\) while \(X_{\tau S}\ne\varnothing\), the swap \((3\ 5)\) dies immediately.

### Strike B — exact finite multiplicity

If no empty fiber is accessible, search for supports for which \(\mu(S)\) can be proved finite and computed exactly, then compare with \(\mu(\tau S)\).

### Strike C — weaker asymmetry invariants

Look for an invariant of the exact-support family that is preserved by graph automorphisms but can be distinguished without knowing the whole cardinality \(\mu(S)\).

Candidates include:

- a provable covering-congruence type;
- forced exponent congruence classes;
- hereditary exact-support obstruction at the next Pratt layer;
- finite collections of exact fibers whose joint multiplicity profile is asymmetric.

### Strike D — survival theorem under a weaker hypothesis than FSI

If unconditional killing fails, formulate the minimal arithmetic hypothesis needed for the seed swap \((3\ 5)\) to survive all levels. This should be strictly weaker than the Full Support Infinitude hypothesis from HATTER-SOL-04.

## Publication threshold

Not reached.

HATTER-SOL-05 should be published only if at least one of the following is achieved:

1. an unconditional killing certificate for \((3\ 5)\) or another first-layer Fermat permutation;
2. a nontrivial theorem proving that a broad class of exact-support witnesses cannot exist;
3. a sharp necessary-and-sufficient arithmetic survival criterion significantly stronger than the generic multiplicity-tower restatement;
4. a rigorous covering-congruence theory for empty exact-support fibers with consequences for automorphism survival.

## Continuation sentence for HATTER-SOL-04

The final publication version of HATTER-SOL-04 should end with a short bridge:

> **Продолжение следует.** Следующая чашка будет спрашивать уже не о цене гипотетической симметрии, а о том, можно ли убить её арифметически: существует ли точная опора \(S\), для которой волокно \(X_S\) пусто или имеет другую мощность, чем волокно после перестановки \(3\leftrightarrow5\)?

English bridge:

> **To be continued.** The next cup will ask not how expensive a hypothetical symmetry must be, but whether arithmetic can kill it: is there an exact support \(S\) whose fiber is empty, or has a different cardinality, after the swap \(3\leftrightarrow5\)?
