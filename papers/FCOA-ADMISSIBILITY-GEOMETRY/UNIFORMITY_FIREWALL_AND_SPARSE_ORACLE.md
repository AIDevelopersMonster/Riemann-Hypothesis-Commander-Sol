# Uniformity Firewall and Sparse-Oracle Collapse

**Project:** FCOA Admissibility Geometry  
**Status:** main-line theorem candidate  
**Scope:** central Arithmetic Leakage programme; no new accepted FCOA operation cells

## 1. Why density-only optimization is ill-posed

After G4-A, the central optimization problem was phrased as:

\[
\text{What is the cheapest FCOA mechanism that leaves }FO[<]?
\]

The threshold examples show that support density and logical strength are different axes. There is an even sharper obstruction:

> If arbitrary size-dependent external choices are allowed, then support size alone admits no meaningful lower bound at all.

A single additional operation cell per finite structure can encode an arbitrary property of the structure size.

Therefore any minimality claim must include a **uniformity/import restriction** on how the new cells are generated.

## 2. Sparse-oracle construction

Let \(\mathfrak A_N\) be the hostile-audited G4-A structure on generic sector

\[
G_N=\{P_2,\dots,P_N\}.
\]

Let

\[
S\subseteq\{3,4,5,\dots\}
\]

be an arbitrary external set of sizes.

Introduce a fresh partial binary operation symbol \(\diamond\), but add at most one defined cell:

\[
P_1\diamond P_0=\Omega_+
\qquad\text{iff}\qquad
N\in S.
\]

If \(N\notin S\), \(\diamond\) is nowhere defined.

No new carrier element is required because \(P_0,P_1,\Omega_+\) are already internally recoverable in G4-A.

The additional operation support therefore satisfies

\[
\boxed{
|\operatorname{Dom}(\diamond)|\le1
}
\]

for every \(N\).

## 3. Sparse-Oracle Theorem

### Theorem 3.1

For every external set \(S\subseteq\{3,4,5,\dots\}\), the expansion

\[
\mathfrak A_N^S=(\mathfrak A_N,\diamond)
\]

uniformly first-order recognizes membership of \(N\) in \(S\).

### Proof

In G4-A, \(P_0\) and \(P_1\) are uniformly parameter-free definable. Therefore the sentence

\[
\exists x\exists y\exists z\,
[B_1(x)\land B_0(y)\land D_\diamond(x,y,z)]
\]

holds exactly when the single cell

\[
P_1\diamond P_0=\Omega_+
\]

is present, which by construction is equivalent to

\[
N\in S.
\]

Thus the family of expanded structures carries one externally supplied oracle bit per size, while using at most one additional operation cell. \(\square\)

## 4. Immediate consequence

Choose any set \(S\) of finite sizes that is not first-order definable over finite linear orders; parity is the simplest example.

Then the expanded family leaves the G4-A order wall although

\[
\boxed{
|\operatorname{Dom}(\diamond)|\le1.
}
\]

Therefore:

### Corollary 4.1 — No Density-Only Lower Bound

Without a restriction on the external rule that selects added cells, there is no nontrivial support-size lower bound for leaving

\[
FO[<].
\]

In particular, the optimization problem

\[
\min |\operatorname{Dom}(\text{new mechanism})|
\]

is mathematically degenerate if arbitrary size-dependent external information is permitted.

## 5. Why this is not a legitimate FCOA solution

The construction above is intentionally hostile.

It does **not** derive new structure from the FCOA carrier or operations. It simply imports one bit of external information about \(N\) and stores it in one operation cell.

Its role is to prove a methodological theorem:

\[
\boxed{
\text{support cost is meaningless unless import complexity is controlled.}
}
\]

Thus the Arithmetic Leakage programme needs an explicit **Uniformity Firewall**.

## 6. Uniformity Firewall

Every proposed extension family

\[
\{\mathfrak A_N'\}
\]

must specify not only its operation cells, but also a **generation rule** explaining how those cells are obtained uniformly across \(N\).

A candidate is not eligible for a minimality claim unless its generation rule belongs to a declared admissible class.

At minimum, every candidate passport must record:

1. **background structure used by the generator**;
2. **whether external order is available**;
3. **whether external arithmetic, numerical rank, or a unary function is available**;
4. **whether the rule is FO-definable from the current structure**;
5. **whether it uses a finite-state/local recurrence, MSO/automata mechanism, or a stronger oracle**;
6. **whether the rule depends on \(N\) globally**;
7. **support/domain growth**;
8. **output alphabet size**;
9. **anchor cost**;
10. **resulting logical leakage level**.

## 7. Definitional-expansion floor

There is a trivial but important lower layer.

If every new relation or operation graph is uniformly FO-definable in the existing G4-A structure, then adding it is a definitional expansion. It cannot increase first-order expressive power on the generic sector.

Hence:

\[
\boxed{
\text{FO-generated extension}\Rightarrow\text{no escape from AL0}.
}
\]

Therefore every genuine transition out of the order wall requires a generation mechanism not already uniformly FO-definable in G4-A.

This does not mean such a mechanism must be arithmetic; it may be finite-state, modular, automatic, recursive, geometric, or value/domain based. But it must add genuinely new uniform information.

## 8. Relative, not absolute, minimality

The correct optimization problem is therefore conditional.

For a declared generator class \(\mathcal G\), define schematically

\[
\operatorname{Cost}_{\mathcal G}(\mathcal E)
=
(
\text{support growth},
\text{alphabet},
\text{anchors},
\text{arity},
\text{generator complexity},
\text{leakage}
).
\]

Then meaningful questions have the form:

\[
\boxed{
\text{What is the cheapest }\mathcal G\text{-admissible mechanism that leaves }FO[<]?
}
\]

or

\[
\boxed{
\text{What is the cheapest }\mathcal G\text{-admissible mechanism that reaches EqGap?}
}
\]

There is no generator-independent minimum.

## 9. Relation to threshold compression

The square-threshold example

\[
R(x,y)\iff x^2\le y
\]

has

\[
|R\cap[N]^2|=\Theta(N^{3/2}),
\]

but it imports the nonlinear scale \(x\mapsto x^2\).

The sparse-oracle theorem shows that one can push support much lower—even to \(O(1)\)—if arbitrary external information is allowed.

Therefore the real content of a sparse FCOA construction is not merely that its support is small. The scientific question is:

\[
\boxed{
\text{How much structure is produced by how weak a uniform generator?}
}
\]

This is the corrected central optimization principle.

## 10. A useful hierarchy of generator strength

The following is a working research hierarchy, not yet a theorem that every level is strict.

### U0 — Internal FO

New cells are uniformly FO-definable from current G4-A.

Consequence: definitional expansion only; no logical leakage increase.

### U1 — Local / finite-state carrier mechanism

New cells are produced by a fixed finite-state or bounded-local rule along the recovered successor/order, without numerical rank or arithmetic oracle.

Potentially capable of modular/intermediate leakage.

### U2 — Regular / automatic external scaffold

A fixed automatic or MSO-definable coloring/scaffold may be used.

This can add non-FO[<] information while often remaining decidable.

### U3 — Explicit external unary function / numerical scaffold

Examples include

\[
x^2,
\quad2^x,
\quad f(x),
\]

used to generate threshold or value geometry.

These are calibration mechanisms, not FCOA-native discoveries unless independently reconstructed internally.

### U4 — Arbitrary size-dependent oracle

Any global choice depending on \(N\), including the one-cell sparse-oracle construction.

This level is forbidden for minimality claims because it trivializes support optimization.

## 11. New main-line problem

The central road should now attack the first nontrivial class above definitional expansion:

\[
\boxed{
U1:\ \text{local / finite-state mechanisms over the recovered carrier geometry.}
}
\]

Two questions separate naturally:

1. Can a U1 mechanism leave \(FO[<]\) at all?
2. If yes, can it remain strictly below EqGap/addition?

If the answer to (1) is negative under a sufficiently precise U1 definition, that itself would be a strong impossibility theorem: a new lower bound on how much external/global structure is required for arithmetic leakage.

If the answer is positive, the cheapest witness would give a genuine, non-oracular AL-INT layer.

## 12. Status

The sparse-oracle theorem and the definitional-expansion observation are elementary and fixed once the exact G4-A boundary points are available.

The proposed U0-U4 hierarchy and cost-vector language are working programme architecture and require hostile audit/refinement before being treated as canonical.

\[
\boxed{
\mathbf F:\ \text{No Density-Only Lower Bound under arbitrary external import}
}
\]

\[
\boxed{
\mathbf F:\ \text{uniform FO-definitional expansions cannot leave AL0}
}
\]

\[
\boxed{
\mathbf W:\ \text{Uniformity Firewall and U0-U4 generator hierarchy}
}
\]
