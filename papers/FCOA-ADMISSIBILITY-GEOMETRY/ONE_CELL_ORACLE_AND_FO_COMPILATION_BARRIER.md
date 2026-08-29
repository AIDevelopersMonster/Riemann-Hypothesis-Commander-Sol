# One-Cell Oracle Degeneracy and the FO-Compilation Barrier

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate  
**Scope:** post-G4 Arithmetic Leakage programme; no new accepted G5 mechanism

## 1. Why this note is central

After the G4-A Generic FO Collapse, the main optimization problem was phrased as:

\[
\boxed{
\text{What is the cheapest FCOA mechanism that leaves }FO[<]?
}
\]

This question is ill-posed unless the source of the new mechanism is constrained.

A single externally conditioned operation cell can encode an arbitrary predicate of the carrier size. Therefore support cost, domain density, output-alphabet size and anchor count alone do not control logical leakage.

At the opposite extreme, any expansion compiled uniformly by first-order definitions from G4-A cannot leave the order wall at all.

These two facts create a sharp central dichotomy:

\[
\boxed{
\text{external oracle can leak arbitrarily much at }O(1)\text{ cell cost,}
}
\]

while

\[
\boxed{
\text{uniform FO compilation from G4-A leaks nothing beyond }FO[<].
}
\]

The real research target must therefore lie between these two extremes.

## 2. Exact G4-A background

Relationalize the partial operation by

\[
T(x,y,z)\iff x\otimes_{4A}y=z.
\]

Let \(\mathfrak A_N\) denote the one-sorted relationalized G4-A structure, and put

\[
m=N-1=|G_N|.
\]

The previously audited Generic FO Collapse states that, on generic tuples,

\[
\boxed{
FO(\mathfrak A_N)=FO([m],<)
}
\]

uniformly across the family.

The boundary point \(P_0\) is uniformly parameter-free definable in \(\mathfrak A_N\). Write \(B_0(x)\) for any fixed audited formula defining it.

## 3. One-Cell Oracle construction

Let

\[
S\subseteq\{2,3,4,\dots\}
\]

be an arbitrary set of generic-sector sizes.

Define \(\mathfrak A_N^S\) from G4-A by changing exactly one previously undefined cell:

\[
\boxed{
P_0\otimes_S P_0=P_0
\iff
m\in S.
}
\]

If \(m\notin S\), the cell remains undefined.

All other G4-A cells are unchanged.

No new output element is required.

The original left-zero characterization of \(P_0\) remains valid: whenever \(P_0\) has a defined left product, its value is still \(P_0\).

## 4. One-Cell Oracle Theorem

### Theorem 4.1

For every set \(S\subseteq\{2,3,\dots\}\), there is a single first-order sentence \(\chi_S\) in the fixed target language \(\{T\}\) such that

\[
\boxed{
\mathfrak A_N^S\models\chi_S
\iff
m\in S.
}
\]

In fact the same sentence works for every \(S\):

\[
\chi:=
\exists b\,[B_0(b)\land T(b,b,b)].
\]

### Proof

The formula \(B_0\) defines exactly \(P_0\) in every member of the oracle family. By construction,

\[
T(P_0,P_0,P_0)
\]

holds exactly when \(m\in S\). \(\square\)

Thus one optional operation cell can give a sentence an arbitrary prescribed size-spectrum.

## 5. Consequence: support-cost minimization is degenerate without an import firewall

The construction adds at most one operation cell, so the additional support cost is

\[
O(1).
\]

Nevertheless \(S\) can be:

- parity of \(m\);
- a residue class modulo any fixed integer;
- the set of primes;
- an arbitrary computable set;
- even an arbitrary noncomputable set, if unrestricted external specification is allowed.

Therefore:

\[
\boxed{
\text{constant cell cost does not bound family-level logical leakage.}
}
\]

The statement concerns the spectrum

\[
\{m:\mathfrak A_N^S\models\chi\},
\]

not the decidability of any single finite member.

This is the strongest reason so far that `external-import cost` must be an explicit coordinate of every FCOA optimization problem.

## 6. Exact global-bit collapse

Introduce a source class consisting of finite linear orders equipped with one zero-ary predicate \(B_S\), interpreted by

\[
B_S\text{ is true in }[m]
\iff
m\in S.
\]

Then the same fixed finite-copy transduction used for G4-A, with one additional clause

\[
B_S\Rightarrow T(b_0,b_0,b_0),
\]

produces \(\mathfrak A_N^S\).

Conversely, \(B_S\) is recoverable in the target by the sentence \(\chi\).

Hence, on generic tuples, the oracle family has exactly the expressive power of

\[
\boxed{
FO[<,B_S],
}
\]

where \(B_S\) is a **global size bit**, not an element predicate.

Every formula is therefore equivalent to a pair of order formulas selected according to whether \(B_S\) is true or false.

## 7. A strict intermediate example at one-cell cost

Take

\[
S_{2}=\{m:m\equiv0\pmod2\}.
\]

Then the oracle family uniformly defines parity of the generic-sector size, which pure \(FO[<]\) cannot define.

Therefore

\[
oxed{
FO[<]
\;<\;
FO[<,B_{\mathrm{even}}].
}
\]

Yet truncated rank addition is still not uniformly definable.

### Proposition 7.1

Canonical truncated addition is not uniformly first-order definable in the parity-oracle family.

### Proof

Suppose it were. Then in \(FO[<,B_{\mathrm{even}}]\) we could define whether

\[
m-1
\]

is divisible by \(3\), using the maximum \(M\) and the addition graph:

\[
\exists x,u\,[
\operatorname{Add}(x,x,u)
\land
\operatorname{Add}(u,x,M)
].
\]

This sentence holds exactly when

\[
m\equiv1\pmod3.
\]

But every sentence of \(FO[<,B_{\mathrm{even}}]\) is, on even sizes and odd sizes separately, equivalent to a pure-order sentence. A pure-order sentence is eventually constant as a function of the size of a finite linear order. Therefore every size-spectrum definable in \(FO[<,B_{\mathrm{even}}]\) is eventually constant on each parity class.

The set

\[
\{m:m\equiv1\pmod3\}
\]

is not eventually constant on either parity class. Contradiction. \(\square\)

Thus we have an explicit strict intermediate calibration:

\[
\boxed{
FO[<]
\;<\;
FO[<,B_{\mathrm{even}}]
\;<\;
\text{truncated-addition strength}.
}
\]

This confirms that an intermediate leakage zone is real, although the example is deliberately an **external oracle benchmark**, not an accepted FCOA-native mechanism.

## 8. FO-Compilation Barrier

The opposite direction is equally important.

### Theorem 8.1 — No leakage under uniform FO-definitional expansion

Let \(\mathfrak B_N\) be any expansion of the G4-A family by finitely many new relations or partial-operation graphs such that each new symbol is uniformly parameter-free first-order definable in \(\mathfrak A_N\).

Then on generic tuples

\[
\boxed{
FO(\mathfrak B_N)=FO[<]
}
\]

uniformly across the family.

### Proof

Every formula in the expanded language can be translated back to the original G4-A language by replacing each new atomic predicate with its uniform defining formula. The audited G4-A Generic FO Collapse then translates the resulting formula to pure finite order. The reverse inclusion already holds because G4-A order is definable. \(\square\)

Therefore no finite definitional expansion of G4-A can cross AL0.

## 9. Fixed-depth composition cannot escape the wall

A graph of any fixed partial-operation term built from the existing G4-A operation is first-order definable from \(T\).

For example, the graph of a fixed bracketing

\[
(x\otimes y)\otimes z=w
\]

is expressed relationally by

\[
\exists u\,[T(x,y,u)\land T(u,z,w)].
\]

The same applies to every fixed finite composition tree.

Hence:

### Corollary 9.1

Adding any finite collection of fixed-depth derived operations, translations, commutation tests, association tests, or other uniformly FO-definable observables to G4-A does not leave the order wall.

More generally, even if one names every fixed term operation as a separate symbol, any individual first-order formula uses only finitely many such symbols and translates back to the original language.

Thus:

\[
\boxed{
\text{fixed-depth nesting/composition cannot by itself generate arithmetic leakage from G4-A.}
}
\]

## 10. What can escape without a raw oracle?

The two theorems leave only genuinely stronger possibilities.

To cross the order wall without simply importing an external predicate, a candidate must use at least one ingredient not uniformly FO-definable in the current G4-A structure. Natural possibilities include:

1. an unbounded iteration or closure whose depth grows with the carrier;
2. transitive closure / least fixed point / reachability-type semantics;
3. a genuinely new primitive partial operation with cells not FO-compilable from existing order memory;
4. interaction of two primitive operations where the second contributes new non-FO geometry rather than a definitional copy of the first;
5. a family-generation rule with its own independently justified structure, whose import cost is explicitly accounted for.

This is not a claim that every such mechanism escapes. It is a necessary classification of where an escape can come from.

## 11. Import-Generation Dichotomy

The central programme should distinguish:

\[
\boxed{
\textbf{imported leakage}
}
\]

from

\[
\boxed{
\textbf{generated leakage}.
}
\]

**Imported leakage** means that a relation not available in G4-A is injected by an external rule, such as parity of \(m\), squaring, threshold geometry, or another oracle-like predicate.

**Generated leakage** means that the stronger relation arises from an allowed internal mechanism whose own construction does not already assume the relation to be recovered.

The one-cell oracle theorem shows why this distinction is mathematically mandatory: without it, every density/minimality question collapses.

## 12. Revised central optimization problem

The main question is therefore no longer simply

\[
\text{minimize number of new cells subject to leaving }FO[<].
\]

That minimum is at most one under unrestricted import and is therefore uninteresting.

The correct optimization problem is constrained:

\[
\boxed{
\text{Minimize structural cost subject to a bounded/declared import budget and genuine generated leakage.}
}
\]

A useful cost vector is

\[
(
\text{new support},
\text{output alphabet},
\text{anchor cost},
\text{arity},
\text{iteration depth},
\text{external-import complexity},
\text{leakage level}
).
\]

## 13. Consequence for the side directions

This theorem gives a precise filter for delegated work without changing their autonomy.

- A **hybrid** two-operation result matters centrally only if the second operation contributes genuinely new non-FO structure; a definitional companion operation cannot cross AL0.
- A **nesting/atomicity** result matters to Arithmetic Leakage if it supplies an unbounded composition/closure mechanism rather than fixed-depth term nesting.
- A **rigidity-cost** optimum based only on number of cells is insufficient unless its import budget is also specified.
- An **infinite-memory** result can test which closure mechanisms remain decidable before additive or full arithmetic strength appears.

No subordinate result is adopted automatically.

## 14. Status

The one-cell oracle theorem and FO-definitional barrier are direct formal consequences of the exact G4-A setup and standard closure of first-order logic under definitional expansion.

The parity-oracle strict-intermediate example uses only the standard eventual indistinguishability of sufficiently long pure finite linear orders.

Current classification:

\[
\boxed{
\mathbf W:\ \text{One-Cell Oracle Degeneracy / FO-Compilation Barrier; hostile audit pending.}
}
\]

No new primitive mechanism has yet been accepted as the next FCOA stage.
