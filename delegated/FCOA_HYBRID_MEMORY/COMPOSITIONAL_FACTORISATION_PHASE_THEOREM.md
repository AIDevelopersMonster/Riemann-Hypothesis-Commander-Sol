# FCOA Hybrid Memory — Compositional Factorisation Phase Theorem

**Status:** positive theorem for a semantic/compositional representation class  
**Scope:** post-Article-A resource theory; stronger than radix normal form, weaker than unrestricted FO

## 1. Why a new class is needed

The depth-`d` radix theorem showed a real resource gap between order and binary arithmetic transport once lower-level factorisation is frozen. But radix syntax is too presentation-specific.

At the opposite extreme, unrestricted FO is too powerful: global target-hosted lookup tables and cross-branch shortcuts can bypass the lowest unresolved scale entirely.

The correct middle class is therefore defined by **bounded compositional factorisation** rather than by a numeral system.

---

## 2. Compositional factorisation presentations

Fix constants

\[
d\ge1,\qquad f\ge2.
\]

A family of presentations is in class

\[
\mathsf{CF}(d,f)
\]

if every target element admits a dependency cone of depth at most `d` with the following properties.

### (CF1) Bounded fan-in

Every non-leaf factorisation node depends on at most `f` children at the next lower level.

Thus a target element depends on at most

\[
k=f^d
\]

primitive leaf coordinates.

### (CF2) Primitive bottom carrier

All leaves lie in a bottom carrier `D_N`, and elements of `D_N` are not further factorised inside the presentation.

To encode `N` distinct target values with at most `k` leaves per target, the bottom carrier must satisfy

\[
|D_N|^k\ge N.
\]

Hence

\[
s_N:=|D_N|\ge N^{1/k}=N^{1/f^d}.
\tag{1}
\]

Balanced constructions attain this exponent.

### (CF3) Compositional locality

A recovery computation may combine information only through a bounded-size local gate whose inputs belong to children of one common factorisation node.

There are no primitive relations joining arbitrary leaves belonging to unrelated dependency cones, and no target-hosted global lookup relation indexed by all pairs of bottom symbols.

This is the semantic prohibition that rules out the target-hosting counterexample.

### (CF4) Extensional primitive gates

At the primitive bottom level, a local gate is represented extensionally by bounded-size records. One primitive record certifies only `O(1)` input tuples.

Higher-level gates may reuse lower-level laws compositionally, but no hidden lower factorisation of `D_N` is allowed.

### (CF5) Full bottom exposure

Every bottom symbol occurs as a leaf value in target representations, and for binary target operations every ordered pair of bottom symbols occurs in a pair of target dependency cones in a context that isolates the corresponding lowest-level local interaction.

This excludes degenerate encodings that reserve most bottom pairs forever unused.

---

## 3. Bottom resource

Let

\[
M_{bot}(A_N)
\]

be the number of primitive records in the induced bottom structure and primitive local gates on `D_N`.

All target/factorisation attachment records may still total `Theta(N)`; the theorem separates the cost paid at the lowest unresolved compositional scale.

---

## 4. Order requires only unary/comparison organisation

### Proposition HM-CF-ORD-UP

There exist `\mathsf{CF}(d,f)` families recovering a uniform total order with

\[
M_{bot}=O(s_N).
\]

### Construction

Put a directed chain on the bottom carrier:

\[
d_0\to d_1\to\cdots\to d_{s_N-1}.
\]

Use any fixed balanced `f`-ary composition tree of depth `d` to represent target coordinates. Compare two targets lexicographically according to the fixed leaf order induced by that tree.

Since `d,f` are constants, the comparison is one fixed FO/compositional formula. The chain uses `Theta(s_N)` records. `□`

### Proposition HM-CF-ORD-LOW

Under CF2--CF5, a uniformly recovered strict total order requires

\[
M_{bot}=Omega(s_N).
\]

### Proof

Primitive records have bounded arity. If `M_{bot}=o(s_N)`, then at least two bottom symbols are untouched by every nontrivial bottom record.

By full bottom exposure both symbols occur in target representations. Swapping them preserves every primitive bottom relation and, by compositional locality, propagates to an automorphism of the factorisation skeleton on all contexts in which the two symbols occur symmetrically.

A uniform strict total order cannot be invariant under such a nontrivial swap. Contradiction. `□`

Hence, in balanced presentations with (1) at equality,

\[
\boxed{
M_{bot}(AL0)=Theta\left(N^{1/f^d}\right).
}
\tag{2}
\]

---

## 5. Pair-complete binary transport

Call a target binary law `T_N(x,y,z)` **pair-complete at the bottom layer** if for every ordered pair

\[
(a,b)\in D_N^2
\]

there are target inputs whose dependency cones isolate `a,b` at one lowest common local gate and for which correctness of `T_N` requires the gate to distinguish the local result associated with that ordered pair.

Canonical digit addition with carry and digit multiplication with split carry are pair-complete.

The definition is semantic: it speaks about which bottom interactions the target relation actually requires, not about radix notation.

---

## 6. Pair-Coverage Lemma

### Lemma HM-CF-PAIR

Let a pair-complete binary transport law be recovered in `\mathsf{CF}(d,f)`. Then the primitive bottom gates require

\[
Omega(s_N^2)
\]

records.

### Proof

There are `s_N^2` ordered bottom pairs. By pair completeness, each such pair must have a correct local outcome certified at the lowest unresolved interaction scale.

By CF3, a certificate for `(a,b)` cannot be imported from an unrelated branch or from a global target-hosted table. By CF4, one primitive record certifies only `O(1)` ordered input pairs. Therefore covering all `s_N^2` exposed pairs requires

\[
Omega(s_N^2)
\]

primitive records. `□`

A full extensional local table gives the matching upper bound.

Thus

\[
\boxed{
M_{bot}(\text{pair-complete transport})
=Theta(s_N^2).
}
\tag{3}
\]

---

## 7. Addition and multiplication

Canonical truncated addition is pair-complete because at the lowest unresolved scale every pair of bottom values must determine a low output symbol and bounded carry state.

Canonical truncated multiplication is pair-complete for the same reason: every bottom pair must determine the local product decomposition needed by the higher compositional layers.

Therefore balanced `\mathsf{CF}(d,f)` presentations satisfy

\[
\boxed{
M_{bot}(AL1)=Theta\left(N^{2/f^d}\right),
}
\tag{4}
\]

and

\[
\boxed{
M_{bot}(AL2)=Theta\left(N^{2/f^d}\right).
}
\tag{5}
\]

As before, AL1 and AL2 are not separated by this exponent. Their distinction is semantic, not pair-coverage cost.

---

## 8. Compositional Factorisation Phase Theorem

### Theorem HM-CFPT

Fix bounded factorisation depth `d` and bounded fan-in `f`. In balanced compositional factorisation presentations `\mathsf{CF}(d,f)` satisfying CF1--CF5,

\[
\boxed{
M_{bot}(AL0)
=Theta\left(N^{1/f^d}\right),
}
\]

while every pair-complete binary arithmetic transport law, including canonical addition and multiplication, satisfies

\[
\boxed{
M_{bot}(AL1)
=M_{bot}(AL2)
=Theta\left(N^{2/f^d}\right).
}
\]

Hence

\[
\boxed{
\lambda_{d,f}(AL1)
=\lambda_{d,f}(AL2)
=2\lambda_{d,f}(AL0).
}
\]

This extends HM-BDRS from binary radix syntax to any bounded-fan-in compositional decomposition with full bottom exposure and no cross-branch shortcuts.

---

## 9. Why the theorem is more semantic than the radix version

The proof never uses positional numerals, base-`b` arithmetic, or a specific coordinate geometry.

It uses only:

1. bounded compositional depth;
2. bounded fan-in;
3. a primitive unresolved leaf carrier;
4. compositional locality;
5. full exposure of bottom symbols/pairs;
6. bounded-capacity primitive records.

Thus the gap is generated by the **arity of the information that must be resolved at the lowest unresolved scale**:

\[
\text{order: one-symbol organisation}
\]

versus

\[
\text{transport: all ordered symbol pairs}.
\]

This is the structural content behind the factor-of-two exponent.

---

## 10. Why unrestricted FO still escapes

HM-CFPT is not an unrestricted FO lower bound.

If CF3 is removed, the target-hosting construction stores the entire `D_N^2` binary table on target points and makes the endpoint-based bottom cost vanish.

If CF2 is removed, each bottom symbol can itself be factorised and the exponent drops again.

If CF4 is removed, a primitive intensional oracle may represent an arbitrary binary law without paying one record per exposed pair.

Therefore all three restrictions are mathematically substantive, not cosmetic.

---

## 11. Relation to circuit language

The class can be viewed as a bounded-depth, bounded-fan-in **incidence circuit** whose leaves are primitive symbols and whose internal nodes compose local relations.

Under this view:

- `d` is circuit/factorisation depth;
- `f` is fan-in;
- `s_N` is the unresolved alphabet size at the leaves;
- `M_bot` is leaf-law table size.

The phase theorem becomes a bounded-depth incidence-circuit separation between unary/comparison organisation and pair-complete transport.

This is a better bridge to descriptive complexity and circuit lower-bound language than radix-specific terminology.

---

## 12. Current boundary of the result

The theorem now survives:

- change of numeral system;
- arbitrary balanced `f`-ary decomposition trees;
- fixed bounded-size incidence compilation;
- replacement of explicit operation symbols by equivalent local relational gadgets.

It does **not yet** survive:

- arbitrary FO cross-branch quantification;
- unbounded fan-in;
- hidden oracle predicates;
- target-hosted global tables;
- unbounded factorisation depth.

Accordingly it is a genuine representation-class theorem, but not yet a full interpretation-invariant theorem.

---

## 13. Stronger next target

The next possible upgrade is to replace the explicit CF3 locality axiom by an established semantic width notion, for example a bounded-depth/bounded-fan-in incidence-circuit model or an FO transduction class with a locality/guardedness restriction.

The desired statement would have the form

\[
\boxed{
\text{bounded compositional width + bounded depth}
\Longrightarrow
\lambda(AL1/AL2)\ge 2\lambda(AL0).
}
\]

Proving that in a standard model would make the phase theorem externally portable rather than FCOA-specific.
