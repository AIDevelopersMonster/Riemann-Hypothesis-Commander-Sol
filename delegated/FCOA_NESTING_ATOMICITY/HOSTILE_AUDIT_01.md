# FCOA Nesting & Atomicity — Hostile Audit 01

**Branch:** `director/fcoa-nesting-atomicity`  
**Scope:** definitions, local/global boundary theorem, well-founded rank, and quotient/carrier identification  
**Verdict:** `PASS_WITH_REPAIRS`

This audit deliberately tries to break the first theorem package. It does not revise the published M0-G1-G2 checkpoint and makes no claim about the still-separate G4 audit.

## 1. Finding H1 — the factor-graph universe was too small

### Attack

The first definitions placed the nontrivial factor graph on the active set `A\U`, while the branch passport explicitly allows an element originally classified as terminal to become an argument if the signature says so.

Then a legal witness

\[
t\star a=x,
\qquad t\notin U,
\]

with `t` admitted as an argument could make `x` non-atomic while contributing no graph edge if `t` was omitted from the vertex universe.

### Repair

The factor graph must live on the full nontrivial carrier

\[
N=X\setminus U,
\]

with edge

\[
y\triangleleft x
\]

whenever `y` is one of the two nontrivial factors of an allowed two-sided decomposition of `x`.

Atomicity may still be *interpreted* only on the declared active target sort, but the graph cannot silently discard legal factors.

**Status:** repaired in `DEFINITIONS.md` and `THEOREMS.md`.

---

## 2. Finding H2 — acyclicity was sufficient, not necessary

### Attack

The first upstream memo suggested that atoms coincide with nesting-minimal points "under acyclicity/well-foundedness" in a way that could be read as an exact necessity claim.

This is too strong.

Take a graph with an atom `a`, an edge from `a` into a separate component, and a directed cycle entirely above that boundary. The graph is cyclic, but the only minimal SCC can still be the singleton `{a}`. Then atoms and nesting-minimal elements coincide despite the cycle.

### Exact repair

For *every* sandbox:

\[
\boxed{\text{U-atom}\Longrightarrow\text{nesting-minimal}.}
\]

Conversely, a nesting-minimal element fails to be atomic exactly when its minimal strongly connected component contains an internal factor edge.

Hence globally

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
}
\]

if and only if every minimal SCC is an edge-free singleton.

Acyclicity is a clean sufficient condition, but it is not necessary. Cycles are harmless when they occur strictly above the minimal condensation layer.

**Status:** theorem strengthened and claim ceiling repaired.

---

## 3. Finding H3 — well-foundedness gives the correct infinite theorem

Let `triangleleft` be the repaired nontrivial factor relation on `N=X\U`.

If `triangleleft` is well-founded, the standard rank theorem for well-founded relations gives a unique ordinal-valued rank

\[
\boxed{
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}.
}
\]

The branch-specific consequence is immediate:

\[
\boxed{
x\text{ is a U-atom}\iff \rho(x)=0}
\]

for every element in the declared atomicity target sort.

Every nontrivial factor has strictly smaller rank than its result.

This is the correct replacement for the finite-DAG theorem. The ordinal-rank construction itself is classical set theory and is **not** claimed as new; the only branch claim is its application to the sandbox factor relation.

Well-foundedness is stronger than the exact atom/minimal-SCC criterion from H2: it excludes all directed cycles and all infinite descending factor chains, whereas atom/minimal equality only constrains the minimal SCCs.

**Status:** promoted to theorem with prior-art firewall.

---

## 4. Finding H4 — `U`-irreducibility was overnamed

### Attack

In an arbitrary sandbox, declaring `U` "trivial" does not make its elements units. A one-`U` decomposition

\[
u\star a=x
\]

need not make `a` equivalent to `x`, and two elements of `U` may even compose to a nontrivial active result unless explicitly prohibited.

Therefore the first unconditional term `U-irreducible` imported too much monoid intuition into a setting where no unit law was assumed.

### Repair

The unconditional notion is renamed **U-transport-irreducible**:

an active nontrivial `x` is U-transport-irreducible when every decomposition of `x` has exactly one factor in `U` and the other factor is mutually reachable with `x` by trivial-factor transport.

The unqualified shorthand **U-irreducible** is permitted only after a `U`-coherence contract is declared:

1. two `U` factors cannot produce a nontrivial active result;
2. every one-`U` decomposition of a nontrivial active result has its non-`U` cofactor in the same U-transport class as the result.

Under these hypotheses,

\[
\boxed{
U\text{-atom}\iff U\text{-transport-irreducible}.
}
\]

An optional trivial-realization axiom can be added when one wants the classical non-vacuous unit behavior in which every nontrivial element has at least one trivial-factor presentation.

**Status:** terminology and theorem repaired.

---

## 5. Finding H5 — quotient identification has two independent failure modes

Pure erasure preserves every decomposition witness. A quotient is different: it identifies carrier points and can change atomicity even when all quotient operations are perfectly well-defined.

Let

\[
q:X\twoheadrightarrow \bar X
\]

be a sort-respecting partial-algebra quotient, with

\[
\bar U=q(U).
\]

The quotient operation is interpreted in the standard existential representative sense: a quotient cell exists when an allowed representative cell exists, and congruence compatibility makes its result class well-defined.

### Exact quotient criterion

Without any triviality-reflection hypothesis,

\[
q(x)\text{ is non-atomic}
\]

iff there is a representative result `z` in the fiber of `q(x)` and a witness

\[
\omega(a,b)=z
\]

such that both quotient factor classes are nontrivial:

\[
q(a),q(b)\notin\bar U.
\]

Now impose **triviality reflection**

\[
\boxed{q^{-1}(\bar U)=U.}
\]

Then quotient nontriviality of factor classes is exactly original nontriviality, and one obtains the sharp formula

\[
\boxed{
q(x)\in\operatorname{Atom}(\bar{\mathfrak S},\bar U)
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Thus under triviality reflection:

- a quotient cannot create an atom from a composite representative;
- it can destroy an atom by merging it with a composite result;
- atomicity is preserved pointwise iff atomhood is constant on every quotient fiber.

This gives the exact additional condition missing from the pure-erasure theorem.

---

## 6. Finding H6 — quotient can destroy an atom by result-fiber merging

Let

\[
X=\{u,a,b,x,y\},\qquad U=\{u\},
\]

with the single nontrivial cell

\[
a\star b=y.
\]

Then `x` is atomic and `y` is composite. Identify only

\[
x\sim y.
\]

and keep all other classes singleton. The quotient is triviality-reflecting, but

\[
[x]=[y]
\]

is composite because the witness for `y` descends to the quotient.

So an atomic representative can lose atomicity solely because its result fiber contains a composite representative.

**Failure mode:** result-fiber contamination.

---

## 7. Finding H7 — quotient can create an atom when triviality reflection fails

Let

\[
X=\{u,a,b,x\},\qquad U=\{u\},
\]

with

\[
a\star b=x,
\qquad
u\star b=x.
\]

The element `x` is non-atomic because of the witness `a star b=x`.

Identify

\[
a\sim u.
\]

The quotient is compatible with the displayed operation cells, but now the class `[a]=[u]` lies in `bar U`. The quotient has only the one-trivial-factor presentation

\[
[u]\star[b]=[x],
\]

so `[x]` is atomic.

Thus quotient identification can manufacture atoms by collapsing a formerly nontrivial factor into the trivial class.

**Failure mode:** triviality collapse.

---

## 8. Finding H8 — ordinary quotienting can destroy well-founded rank

Even when atom classes survive, an ordinary partial-algebra quotient need not preserve the nesting rank structure.

For example, with `U=emptyset`, take

\[
a\star b=c,
\qquad
c\star b=d.
\]

The original factor graph is acyclic. Identifying `c sim d` gives in the existential quotient

\[
[c]\star[b]=[c],
\]

so the quotient factor graph has a self-loop and is not well-founded.

This example uses an ordinary congruence quotient, not a strong definedness-saturated congruence. Therefore no rank-preservation theorem should be stated without a stronger quotient contract.

**Status:** rank preservation left deliberately unclaimed.

---

## 9. Finding H9 — the left/right symmetry theorem used the wrong word

The first theorem package called a map satisfying

\[
\rho(\omega(a,b))=\omega(\rho(b),\rho(a))
\]

an automorphism. It is a **side-reversing anti-automorphism** (or an isomorphism to the opposite operation), not an ordinary automorphism unless extra symmetry is present.

The theorem survives after this terminology repair:

\[
x\text{ left-U-atomic}
\iff
\rho(x)\text{ right-U-atomic}.
\]

**Status:** repaired.

---

## 10. Finding H10 — pure erasure preserves isolation too

The branch definition of isolation refers only to incidence in allowed operation cells. Therefore a pure erasure that deletes only external labels, orders, or relations while keeping the operation table fixed preserves isolation as well as all decomposition notions.

The earlier caveat saying isolation "may change" was inconsistent with the branch's own definition.

**Status:** repaired.

---

## 11. Prior-art firewall

Two ingredients used by the repaired theory are classical and must not be presented as novelty claims:

1. ordinal rank for a well-founded binary relation;
2. congruences and quotient constructions for partial algebras, including the distinction between ordinary and strong/definedness-reflecting behavior.

The branch contribution, if retained upstream, is the **FCOA-specific synthesis**:

- atomicity as absence of two-sided nontrivial incoming composition witnesses;
- the exact minimal-SCC criterion;
- the application of well-founded rank to composition nesting;
- the quotient fiber formula for atomhood relative to `U`;
- separation of atomicity from terminal value-fiber rigidity.

No priority claim is made here without a dedicated literature audit.

---

## 12. Audit verdict

\[
\boxed{\texttt{PASS\_WITH\_REPAIRS}}
\]

The core thesis survives, but in a sharper form:

\[
\boxed{
\text{atom} = \text{local zero-incoming composition boundary}
}
\]

while the global nesting boundary is the minimal condensation layer, and these coincide exactly when every minimal SCC is an edge-free singleton.

For well-founded nesting, the local boundary becomes rank zero of the canonical ordinal factor rank.

For quotient identification, atomicity is not invariant by default; under triviality reflection, quotient atomhood is a **fiberwise universal** property.