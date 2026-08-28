# FCOA Nesting & Atomicity — Quotient Composition-Reflection Theorem

**Status:** theorem-level delegated result after `HOSTILE_AUDIT_01.md`  
**Branch:** `director/fcoa-nesting-atomicity`  
**Publication boundary:** does not revise Zenodo DOI `10.5281/zenodo.22129787`

## 1. Problem

An ordinary congruence quotient can destroy a well-founded factor structure by identifying result classes. The minimal counterexample from the hostile audit is

\[
a\star b=c,
\qquad
c\star b=d,
\]

followed by `c sim d`, which creates the quotient self-loop

\[
[c]\star[b]=[c].
\]

The question is therefore:

> What explicit quotient condition is strong enough to guarantee that the nontrivial factor relation, its well-foundedness, and its ordinal rank survive carrier identification?

The answer is a predecessor-lifting condition.

## 2. Setup

Let

\[
\mathfrak S=(X,\Omega,U)
\]

be a composition sandbox and let

\[
\triangleleft
\]

be its repaired nontrivial factor relation on `X\U`.

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

## 3. Coherent Predecessor-Lifting Property

The quotient `q` has the **Coherent Predecessor-Lifting Property**, abbreviated `CPL`, if

\[
\boxed{
\bar y\ \bar\triangleleft\ q(x)
\Longrightarrow
\exists y\in q^{-1}(\bar y)\text{ such that }y\triangleleft x
}
\]

for every nontrivial representative `x in X\U` and every quotient predecessor class `bar y`.

The quantifier over **every** representative `x` of the result class is essential. Mere existence of some pair of representatives is the ordinary quotient semantics and is too weak.

Interpretation: quotient factor incidence must not be created by borrowing a predecessor from one representative of the result fiber and then attaching it to another representative that never had such a predecessor.

## 4. Forward Factor Preservation

Under ordinary quotient compatibility plus triviality reflection, every original factor edge descends:

\[
\boxed{
y\triangleleft x\Longrightarrow q(y)\ \bar\triangleleft\ q(x).}
\]

### Proof

Choose a two-sided nontrivial witness producing the edge `y triangleleft x`. Quotient compatibility sends that allowed cell to a quotient cell with result `q(x)`. Triviality reflection keeps both factor classes outside `bar U`. Therefore the quotient cell is still a two-sided nontrivial witness, and `q(y)` is a quotient predecessor of `q(x)`. `square`

## 5. Theorem — CPL preserves well-foundedness

### Theorem

Assume `triangleleft` is well-founded and `q` satisfies CPL. Then

\[
\boxed{\bar\triangleleft\text{ is well-founded}.}
\]

### Proof

Suppose for contradiction that the quotient relation is not well-founded. Then there is an infinite descending quotient chain

\[
\bar x_0
\succ
\bar x_1
\succ
\bar x_2
\succ\cdots,
\]

meaning

\[
\bar x_{n+1}\ \bar\triangleleft\ \bar x_n
\]

for every `n`.

Choose any representative

\[
x_0\in q^{-1}(\bar x_0).
\]

By CPL applied to

\[
\bar x_1\ \bar\triangleleft\ q(x_0),
\]

there exists

\[
x_1\in q^{-1}(\bar x_1)
\]

with

\[
x_1\triangleleft x_0.
\]

Apply CPL again to `x_1`; recursively obtain representatives

\[
x_{n+1}\triangleleft x_n
\]

for every `n`.

This is an infinite descending chain in the original factor relation, contradicting well-foundedness. Hence the quotient factor relation is well-founded. `square`

## 6. Theorem — exact ordinal-rank preservation

Assume now:

1. the original factor relation is well-founded;
2. `q` is quotient-compatible;
3. `q` is triviality-reflecting;
4. `q` satisfies CPL.

Let

\[
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}
\]

be the original factor rank, and let

\[
\bar\rho(\bar x)
=
\sup\{\bar\rho(\bar y)+1:
\bar y\ \bar\triangleleft\ \bar x\}
\]

be the quotient factor rank, whose existence follows from the preceding theorem.

### Rank-Preservation Theorem

For every nontrivial `x`,

\[
\boxed{\bar\rho(q(x))=\rho(x).}
\]

In particular, all representatives of one quotient fiber automatically have the same factor rank.

### Proof

Proceed by well-founded induction on `x` with respect to `triangleleft`.

Assume the equality already holds for every predecessor `y triangleleft x`.

#### Lower bound

For every predecessor `y triangleleft x`, forward factor preservation gives

\[
q(y)\ \bar\triangleleft\ q(x).
\]

Therefore

\[
\bar\rho(q(x))
\ge
\bar\rho(q(y))+1
=
\rho(y)+1.
\]

Taking the supremum over all `y triangleleft x`,

\[
\bar\rho(q(x))\ge\rho(x).
\]

#### Upper bound

Let

\[
\bar y\ \bar\triangleleft\ q(x).
\]

By CPL, there exists a representative

\[
y\in q^{-1}(\bar y)
\]

such that

\[
y\triangleleft x.
\]

By the induction hypothesis,

\[
\bar\rho(\bar y)
=
\bar\rho(q(y))
=
\rho(y).
\]

Hence every term in the quotient rank supremum satisfies

\[
\bar\rho(\bar y)+1
=
\rho(y)+1
\le
\rho(x).
\]

Taking the supremum over quotient predecessors,

\[
\bar\rho(q(x))\le\rho(x).
\]

Combining both inequalities gives

\[
\bar\rho(q(x))=\rho(x).
\]

This completes the induction. `square`

## 7. Corollary — exact preservation of atomicity

Under the same hypotheses,

\[
\boxed{
x\text{ is a U-atom}
\iff
q(x)\text{ is a }\bar U\text{-atom}.}
\]

### Proof

By the well-founded rank theorem,

\[
x\text{ is atomic}\iff\rho(x)=0,
\]

and similarly in the quotient. Rank preservation gives the equivalence. `square`

This is stronger than the earlier fiberwise-universal quotient criterion because CPL prevents a quotient result fiber from mixing different factor-boundary behavior in the first place.

## 8. Corollary — CPL forbids result-fiber contamination

Suppose `q(x)=q(z)` and the hypotheses above hold. Then

\[
\rho(x)=\bar\rho(q(x))=\bar\rho(q(z))=\rho(z).
\]

Hence a CPL quotient cannot identify an atom with a positive-rank composite.

The hostile-audit example that merged an atom `x` with a composite `y` therefore necessarily violates CPL.

## 9. Why ordinary congruence is weaker

Ordinary quotient semantics only requires that a quotient cell have *some* representative witness. Symbolically,

\[
\bar y\ \bar\triangleleft\ \bar x
\]

may be witnessed by

\[
y'\triangleleft x'
\]

for one special pair

\[
y'\in q^{-1}(\bar y),
\qquad
x'\in q^{-1}(\bar x).
\]

CPL requires lifting that same quotient predecessor class to **every** representative of `bar x`.

This is precisely what fails when quotienting manufactures a self-loop or contaminates an atomic result class with a composite representative.

## 10. Minimal failure witness

Take

\[
a\star b=c,
\qquad
c\star b=d,
\]

with `U=emptyset`, and identify

\[
c\sim d.
\]

In the quotient,

\[
[c]\ \bar\triangleleft\ [c]
\]

because `c triangleleft d` before quotienting.

For CPL to hold at representative `c`, the quotient self-predecessor `[c]` would need a representative `y in {c,d}` with

\[
y\triangleleft c.
\]

No such edge exists. Therefore CPL fails exactly where the quotient self-loop is created.

## 11. Exact hierarchy of quotient contracts

The branch now distinguishes:

\[
\boxed{
\text{pure erasure}
\;\Rightarrow\;
\text{literal factor-graph preservation}
}
\]

from

\[
\boxed{
\text{ordinary quotient}
\;\Rightarrow\;
\text{atomicity/rank may change}
}
\]

from

\[
\boxed{
\text{triviality reflection + CPL}
\;\Rightarrow\;
\text{exact factor-rank and atomicity preservation}.
}
\]

No claim is made that CPL is necessary for every possible well-foundedness-preserving quotient. It is a clean, checkable sufficient composition-reflection contract, and it is exact enough to prove rank equality rather than only rank monotonicity.

## 12. Claim boundary and prior-art firewall

This theorem uses standard ideas from quotient structures and well-founded recursion. The branch does not claim priority for quotient lifting principles or ordinal ranks in general.

The FCOA-specific result is the identification of a concrete **composition predecessor-lifting contract** that separates safe carrier identification from quotients that fabricate new nesting geometry.

The novelty status of this formulation remains subject to a dedicated literature audit before publication.