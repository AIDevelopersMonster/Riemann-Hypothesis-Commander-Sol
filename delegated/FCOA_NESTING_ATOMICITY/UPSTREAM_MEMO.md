# FCOA Nesting & Atomicity — Upstream Memo after Hostile Audit 01

**Direction:** `FCOA — SOL-NESTING — Sandbox Atomicity & Composition Boundary`  
**Status:** delegated branch, hostile-audited with repairs  
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

The reverse inclusion has an exact criterion:

\[
\boxed{
\operatorname{Atom}=\operatorname{MinNest}
\iff
\text{every minimal SCC is an edge-free singleton}.
}
\]

This supersedes the earlier emphasis on global acyclicity. Acyclicity is sufficient but not necessary; cycles strictly above the minimal condensation layer do not affect atom/minimal equality.

Thus the sharpened branch thesis is

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

If the factor relation `triangleleft` is well-founded, the standard well-founded recursion gives

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

This repair prevents ordinary monoid intuition from being imported by terminology alone.

## 4. Pure erasure and quotient identification separate sharply

Pure carrier erasure keeps all operation cells fixed and therefore preserves isolation, atomicity, nesting SCCs and well-founded rank exactly.

A genuine quotient

\[
q:X\twoheadrightarrow\bar X
\]

is different. It can alter atomicity through carrier identification.

With

\[
\bar U=q(U)
\]

and the **triviality-reflection** condition

\[
q^{-1}(\bar U)=U,
\]

one obtains the sharp quotient formula

\[
\boxed{
q(x)\in\operatorname{Atom}(\bar{\mathfrak S},\bar U)
\iff
q^{-1}(q(x))\subseteq\operatorname{Atom}(\mathfrak S,U).
}
\]

Hence quotient atomhood becomes a fiberwise universal property.

Two distinct failure modes are now explicit:

- **result-fiber contamination:** an atom can become composite when identified with a composite result;
- **triviality collapse:** if triviality reflection fails, a composite can become atomic because a nontrivial factor collapses into the quotient trivial class.

This is a substantially stronger answer to the original Carrier-Erasure question than the pure-erasure theorem alone.

## 5. Ordinary quotienting does not preserve nesting rank

An ordinary partial-algebra congruence quotient may turn an acyclic factor graph into one with a self-loop. Therefore no general quotient theorem for well-foundedness or ordinal factor rank is claimed.

A future theorem would require a stronger quotient notion, likely one that reflects definedness/factor incidence strongly enough to prevent new quotient cycles. This is an open obligation, not a hidden assumption.

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
- preservation of well-founded rank by arbitrary quotients;
- classical divisibility outside the integer multiplication sandbox;
- novelty of ordinal rank or general partial-algebra quotient theory;
- any revision of M0-G1-G2 or validation of G4.

## 10. Upstream recommendation

The theorem-level material now worth central consideration is:

1. **Sandbox Monotonicity of Atomicity**;
2. **Exact Minimal-SCC Boundary Theorem**;
3. **Well-Founded Factor Rank Corollary**;
4. **Terminal Value-Fiber Invariance of Active Atomicity**;
5. **Triviality-Reflecting Quotient Fiber Criterion**.

The most important conceptual change is that the phrase

\[
\text{“atomicity is a boundary state of composition”}
\]

can now be made exact without arithmetic:

\[
\boxed{
\text{atom}=\text{local boundary};\qquad
\text{minimal SCC}=\text{global boundary};\qquad
\text{rank }0=\text{well-founded boundary}.
}
\]

## 11. Publication status

The hostile audit materially improved the theory, but publication is **not yet declared ready**. One focused obligation remains scientifically important before publication hardening:

> characterize a strong quotient / composition-reflection condition under which factor well-foundedness and ordinal rank descend safely.

That is now the highest-value next mathematical strike; repeatedly elaborating finite atomicity examples would add less.