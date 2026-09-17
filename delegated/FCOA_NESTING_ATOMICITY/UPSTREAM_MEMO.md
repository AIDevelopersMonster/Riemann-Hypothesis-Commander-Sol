# FCOA Nesting & Atomicity — Upstream Memo after Hostile Audit 01

**Direction:** `FCOA — SOL-NESTING — Sandbox Atomicity & Composition Boundary`  
**Status:** delegated branch, hostile-audited with repairs; mathematical core candidate for publication hardening  
**Scientific authority:** main Commander Sol retains acceptance/rejection authority for the central FCOA line.

## Audit verdict

\[
\boxed{\texttt{PASS\_WITH\_REPAIRS}}
\]

The central thesis survives, but the exact theorem is sharper than the first package.

## 1. Exact local/global boundary theorem

On the repaired nontrivial factor graph with vertex set

\[
X\setminus U,
\]

a bilateral U-atom is exactly a zero-indegree vertex.

Every atom is nesting-minimal:

\[
\boxed{
\operatorname{Atom}(\mathfrak S,U)
\subseteq
\operatorname{MinNest}(\mathfrak S,U).
}
\]

The reverse inclusion has the exact criterion

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
}
\]

This supersedes the earlier emphasis on global acyclicity. Acyclicity is sufficient but not necessary; cycles strictly above the minimal condensation layer do not affect atom/minimal equality.

Thus

\[
\boxed{
\text{atomicity = local zero-incoming composition boundary,}
}
\]

while

\[
\boxed{
\text{minimal SCC layer = global nesting boundary.}
}
\]

## 2. Well-founded rank theorem

If the factor relation `triangleleft` is well-founded, standard well-founded recursion gives

\[
\rho(x)=\sup\{\rho(y)+1:y\triangleleft x\}.
\]

Then

\[
\boxed{x\text{ is a U-atom}\iff\rho(x)=0.}
\]

Every factor edge strictly raises ordinal rank.

This is the correct infinite replacement for the finite-DAG statement. The ordinal rank theorem itself is classical set theory and is not a novelty claim; the branch contribution is its application to admissible-composition nesting.

## 3. `U`-irreducibility required a firewall

The first package used the word `U`-irreducible too freely. In an arbitrary sandbox, membership in `U` does not supply a unit law.

The repaired unconditional notion is **U-transport-irreducible**. The shorthand **U-irreducible** is allowed only under a declared U-coherence contract:

1. two U-factors cannot produce a nontrivial target result;
2. every one-U-factor decomposition has its non-U cofactor in the same U-transport class as the result.

Under these hypotheses,

\[
\boxed{U\text{-atom}\iff U\text{-transport-irreducible}.}
\]

## 4. Pure erasure and ordinary quotient identification separate sharply

Pure carrier erasure keeps all operation cells fixed and therefore preserves isolation, atomicity, nesting SCCs and well-founded rank exactly.

A genuine quotient

\[
q:X\twoheadrightarrow\bar X
\]

can alter atomicity through carrier identification.

With

\[
\bar U=q(U)
\]

and the **triviality-reflection** condition

\[
q^{-1}(\bar U)=U,
\]

the exact ordinary-quotient atom criterion is

\[
\boxed{
q(x)\in\operatorname{Atom}(\bar{\mathfrak S},\bar U)
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Hence ordinary quotient atomhood is a fiberwise universal property.

Two failure modes are explicit:

- **result-fiber contamination:** an atom becomes composite when identified with a composite result;
- **triviality collapse:** if triviality reflection fails, a composite can become atomic because a nontrivial factor collapses into the quotient trivial class.

## 5. Quotient Composition-Reflection Theorem — closed obligation

The hostile audit left one important question open: what stronger quotient contract guarantees that well-founded nesting and ordinal rank actually descend?

This is now answered in `QUOTIENT_COMPOSITION_REFLECTION.md`.

Define **Coherent Predecessor Lifting (CPL)** by

\[
\boxed{
\bar y\ \bar\triangleleft\ q(x)
\Longrightarrow
\exists y\in q^{-1}(\bar y):y\triangleleft x
}
\]

for **every** representative `x` of the quotient result class.

Under:

1. original well-foundedness;
2. quotient compatibility;
3. triviality reflection;
4. CPL;

one obtains first

\[
\boxed{
\bar\triangleleft\text{ is well-founded}
}
\]

and then the stronger exact rank theorem

\[
\boxed{
\bar\rho(q(x))=\rho(x)
}
\]

for every nontrivial `x`.

Consequently

\[
\boxed{
x\text{ atomic}\iff q(x)\text{ atomic}.}
\]

The proof is by recursive chain lifting for well-foundedness and by well-founded induction for the two rank inequalities.

CPL also forces all representatives of a quotient fiber to have the same factor rank, so it rules out result-fiber contamination automatically.

This closes the principal mathematical obligation named at the end of Hostile Audit 01.

No claim is made that CPL is logically necessary for every well-foundedness-preserving quotient. It is a clean sufficient composition-reflection contract strong enough to give exact rank equality.

## 6. Atomicity monotonicity survives the audit

For fixed carrier, typing and `U`, if sandbox `S1` is a restriction of `S2`, then

\[
\boxed{
\operatorname{Atom}(S_2,U)
\subseteq
\operatorname{Atom}(S_1,U).
}
\]

Expanding admissible composition can only destroy atoms; restricting it can only create them.

## 7. Rigidity memory remains orthogonal to active atomicity

If two sandboxes differ only in terminal-output value-fiber partition while active-result cells are unchanged, their active atomicity classes coincide.

Thus G3-style value-fiber rigidity and this branch's composition-boundary atomicity remain distinct structural coordinates.

## 8. Additional hostile-audit repairs

- the factor graph must use every legal nontrivial factor in `X\U`, not only a historically active subset;
- the left/right reversal theorem requires a side-reversing **anti-automorphism**, not an ordinary automorphism;
- pure erasure preserves isolation too, because isolation was defined solely by operation-cell incidence.

## 9. Current claim ceiling

The branch establishes an abstract theory of decomposition witnesses and nesting for typed partial-composition sandboxes. It does **not** establish:

- unique factorization;
- atomic decomposition existence for every element;
- a canonical `U` for arbitrary signatures;
- preservation by arbitrary ordinary quotients;
- classical divisibility outside the integer multiplication sandbox;
- novelty of ordinal rank, congruence quotients, or lifting principles in general;
- any revision of M0-G1-G2 or validation of G4.

## 10. Upstream theorem package now worth consideration

1. **Sandbox Monotonicity of Atomicity**;
2. **Exact Minimal-SCC Boundary Theorem**;
3. **Well-Founded Factor Rank Theorem**;
4. **U-Coherence Atom/Transport-Irreducible Theorem**;
5. **Terminal Value-Fiber Invariance of Active Atomicity**;
6. **Triviality-Reflecting Quotient Fiber Criterion**;
7. **CPL Quotient Composition-Reflection and Exact Rank-Preservation Theorem**.

The compact synthesis is now

\[
\boxed{
\text{atom}=\text{local boundary};\qquad
\text{minimal SCC}=\text{global boundary};\qquad
\text{rank }0=\text{well-founded boundary}.
}
\]

and, under safe quotienting,

\[
\boxed{
\text{triviality reflection + CPL}
\Longrightarrow
\bar\rho\circ q=\rho.
}
\]

## 11. Publication status

The principal internal mathematical gaps identified by Hostile Audit 01 are now closed at theorem/proof level.

The branch has therefore crossed from exploratory definition-building into **publication-candidate mathematical core**.

Before any Zenodo recommendation, the required next stage is no longer another mathematical extension. It is a conservative publication-hardening audit:

- dedicated prior-art search for the exact terminology and quotient-lifting formulation;
- proof-by-proof adversarial reread;
- claim/novelty discipline;
- notation and theorem numbering;
- bibliography and metadata;
- RU/EN publication package only after those checks pass.

No further theorem should be added merely to make the branch larger.