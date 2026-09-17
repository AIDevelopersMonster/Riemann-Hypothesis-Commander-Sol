# FCOA Nesting & Atomicity — Quotient Composition Reflection

**Status:** theorem-level delegated result after `HOSTILE_AUDIT_01.md`; prior-art repaired  
**Branch:** `director/fcoa-nesting-atomicity`  
**Publication boundary:** does not revise Zenodo DOI `10.5281/zenodo.22129787`

## 1. Problem

An ordinary congruence quotient of a partial algebra can destroy a well-founded factor structure by identifying result classes. The hostile-audit witness is

\[
a\star b=c,
\qquad
c\star b=d,
\]

followed by `c sim d`, which creates the quotient self-loop

\[
[c]\star[b]=[c].
\]

We ask for an explicit condition ensuring that nontrivial predecessor structure is reflected through the quotient strongly enough to preserve atomicity and ordinal factor rank.

## 2. Setup

Let

\[
\mathfrak S=(X,\Omega,U)
\]

be a composition sandbox and let `triangleleft` be its nontrivial factor relation on `X\U`.

Let

\[
q:X\twoheadrightarrow\bar X
\]

be a sort-respecting quotient compatible with the partial operations, with

\[
\bar U=q(U).
\]

Write

\[
\bar y\ \bar\triangleleft\ \bar x
\]

for the quotient nontrivial factor relation.

Assume **triviality reflection**:

\[
\boxed{q^{-1}(\bar U)=U.}
\]

This guarantees that a factor is nontrivial before quotienting iff its quotient class is nontrivial.

## 3. Coherent predecessor lifting (CPL)

For internal branch bookkeeping, say that `q` has **coherent predecessor lifting (CPL)** if

\[
\boxed{
\bar y\ \bar\triangleleft\ q(x)
\Longrightarrow
\exists y\in q^{-1}(\bar y)\text{ such that }y\triangleleft x
}
\]

for every nontrivial representative `x in X\U` and every quotient predecessor class `bar y`.

The quantifier over **every** representative `x` is essential. Ordinary quotient semantics requires only that some representative cell exist.

### Prior-art identification

`CPL` is **not claimed as a new general morphism concept**. Once one passes from the partial operations to the binary factor relation, the displayed condition is exactly the usual **back condition** of a bounded morphism (p-morphism) of relational/Kripke frames, with the factor relation used as the accessibility relation. See Blackburn--de Rijke--Venema, *Modal Logic* (2001), Chapter 3.

Likewise, in classical monoid factorization theory, transfer homomorphisms impose a stronger factorization-lifting condition: if the image of an element factors, an appropriate source factorization must lift it. The present relational condition is best regarded as a one-step factor-predecessor shadow of that general lifting philosophy, not as a replacement for transfer homomorphisms.

Accordingly, the publication should use **bounded-morphism back condition on the factor relation** as the standard mathematical description. `CPL` may remain as an FCOA-local mnemonic.

## 4. Forward factor preservation

Under quotient compatibility plus triviality reflection, every original factor edge descends:

\[
\boxed{
y\triangleleft x\Longrightarrow q(y)\ \bar\triangleleft\ q(x).}
\]

### Proof

Choose a two-sided nontrivial witness producing the edge `y triangleleft x`. Quotient compatibility sends that allowed cell to a quotient cell with result `q(x)`. Triviality reflection keeps both factor classes outside `bar U`. Hence the quotient cell remains a two-sided nontrivial witness and `q(y)` is a predecessor of `q(x)`. `square`

Together with CPL, this says precisely that

\[
q:(X\setminus U,\triangleleft)
\twoheadrightarrow
(\bar X\setminus\bar U,\bar\triangleleft)
\]

is a surjective bounded morphism of factor frames.

## 5. Theorem — bounded factor morphisms preserve well-foundedness

Assume `triangleleft` is well-founded and the factor-frame map above satisfies the bounded-morphism back condition (equivalently, CPL). Then

\[
\boxed{\bar\triangleleft\text{ is well-founded}.}
\]

### Proof

Suppose instead that there is an infinite descending quotient chain

\[
\bar x_0\succ\bar x_1\succ\bar x_2\succ\cdots,
\qquad
\bar x_{n+1}\ \bar\triangleleft\ \bar x_n.
\]

Choose any representative `x_0` of `bar x_0`. The back condition lifts `bar x_1` to a predecessor `x_1 triangleleft x_0` in its prescribed fiber. Iterating the same argument gives

\[
x_{n+1}\triangleleft x_n
\]

for every `n`, contradicting well-foundedness of the source relation. `square`

This proof is a direct relational consequence of the standard bounded-morphism back condition; no priority claim is made for the general mechanism.

## 6. Theorem — exact ordinal-rank preservation

Assume:

1. the source factor relation is well-founded;
2. `q` is quotient-compatible;
3. `q` is triviality-reflecting;
4. the induced factor-frame map is a surjective bounded morphism (equivalently, forward preservation plus CPL).

Let

\[
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}
\]

and

\[
\bar\rho(\bar x)
=
\sup\{\bar\rho(\bar y)+1:
\bar y\ \bar\triangleleft\ \bar x\}.
\]

Then for every nontrivial `x`,

\[
\boxed{\bar\rho(q(x))=\rho(x).}
\]

In particular, all representatives of a quotient fiber have the same factor rank.

### Proof

Proceed by well-founded induction on `x`.

For the lower bound, every predecessor `y triangleleft x` maps by the forth condition to

\[
q(y)\ \bar\triangleleft\ q(x).
\]

By the induction hypothesis,

\[
\bar\rho(q(y))=\rho(y),
\]

so

\[
\bar\rho(q(x))\ge\rho(y)+1.
\]

Taking the supremum gives

\[
\bar\rho(q(x))\ge\rho(x).
\]

For the upper bound, let

\[
\bar y\ \bar\triangleleft\ q(x).
\]

The back condition gives `y triangleleft x` with `q(y)=bar y`. By induction,

\[
\bar\rho(\bar y)=\rho(y),
\]

hence

\[
\bar\rho(\bar y)+1\le\rho(x).
\]

Taking the quotient-predecessor supremum gives

\[
\bar\rho(q(x))\le\rho(x).
\]

Thus equality holds. `square`

### Prior-art boundary

Ordinal ranks of well-founded relations are classical; see Jech, *Set Theory*, Theorem 2.27. Bounded/p-morphisms and their forth/back clauses are standard in modal logic. The theorem above is retained as a short explicit **application to the FCOA factor relation**, not as a claim that ordinal rank or bounded morphisms are new.

## 7. Corollary — exact preservation of atomicity

Under the same hypotheses,

\[
\boxed{
x\text{ is a U-atom}
\iff
q(x)\text{ is a }\bar U\text{-atom}.}
\]

### Proof

In a well-founded factor relation,

\[
x\text{ atomic}\iff\rho(x)=0.
\]

Apply rank preservation. `square`

## 8. Corollary — no result-fiber contamination

If `q(x)=q(z)`, then

\[
\rho(x)=\bar\rho(q(x))=\bar\rho(q(z))=\rho(z).
\]

Hence a factor-bounded quotient cannot identify an atom with a positive-rank composite.

The hostile-audit example merging an atom with a composite necessarily violates the back condition.

## 9. Why ordinary congruence is weaker

Ordinary partial-algebra quotient semantics only requires a quotient cell to have *some* representative witness. Thus

\[
\bar y\ \bar\triangleleft\ \bar x
\]

may be witnessed by

\[
y'\triangleleft x'
\]

for one special pair of representatives.

The bounded-morphism back clause instead requires every chosen representative `x` of `bar x` to admit a predecessor in the requested quotient predecessor fiber.

This is precisely what fails when quotienting manufactures a self-loop or contaminates an atomic result class with a composite representative.

## 10. Minimal failure witness

Take

\[
a\star b=c,
\qquad
c\star b=d,
\]

with `U=emptyset`, and identify `c sim d`.

The quotient has

\[
[c]\ \bar\triangleleft\ [c]
\]

because `c triangleleft d` before quotienting.

At representative `c`, the back clause would require a `y in {c,d}` with

\[
y\triangleleft c,
\]

but no such edge exists. Therefore the quotient map is not a bounded morphism of factor frames.

## 11. Exact hierarchy of quotient contracts

The branch distinguishes

\[
\boxed{
\text{pure erasure}
\Rightarrow
\text{literal factor-graph preservation}
}
\]

from

\[
\boxed{
\text{ordinary partial-algebra quotient}
\Rightarrow
\text{atomicity/rank may change}
}
\]

from

\[
\boxed{
\text{triviality reflection + factor-frame bounded morphism}
\Rightarrow
\text{exact factor-rank and atomicity preservation}.
}
\]

No necessity claim is made: bounded-morphism reflection is a clean sufficient contract for exact rank equality, not a classification of every quotient that happens to preserve well-foundedness or atomhood.

## 12. Claim boundary

The standard ingredients are explicitly inherited:

- ordinary and strong congruence concepts for partial algebras;
- well-founded ordinal rank;
- bounded/p-morphism forth/back conditions;
- factorization-lifting ideas such as transfer homomorphisms in monoid theory.

The FCOA contribution claimed at this checkpoint is the **assembled sandbox-specific boundary analysis**: how a typed family of partial compositions induces a nontrivial factor relation, how ordinary carrier identification can fabricate predecessor geometry, and how a standard relational back condition supplies a transparent sufficient safety contract for preserving the resulting atomicity/rank layer.

No broad novelty or priority claim is made without a dedicated literature review.