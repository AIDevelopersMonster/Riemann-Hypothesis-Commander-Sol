# U1 Finite-State Leakage — First Honest Escape from the Order Wall

**Project:** FCOA Admissibility Geometry  
**Status:** main-line theorem candidate / construction checkpoint  
**Scope:** central Arithmetic Leakage programme; no arithmetic oracle, no size-dependent oracle

## 1. Goal

The Uniformity Firewall leaves open the first nontrivial question:

\[
\boxed{\text{Can a fixed local/finite-state generator leave }FO[<]\text{ at all?}}
\]

The answer is **yes**. A two-state periodic phase marker already leaves the G4-A order wall. This gives a genuine intermediate leakage layer.

## 2. A precise U1 class

Fix the recovered generic successor chain

\[
P_2<P_3<\cdots<P_N.
\]

A **prefix-consistent deterministic finite-state generator** consists of a finite state set \(Q\), an initial state \(q_0\), a fixed transition map \(\delta:Q\to Q\), and a fixed output map \(\lambda:Q\to\{0,1\}\).

Starting at the least generic point, define

\[
q(P_2)=q_0,
\qquad
q(\operatorname{Succ}(x))=\delta(q(x)),
\]

and mark

\[
M(x)\iff \lambda(q(x))=1.
\]

The same automaton is used for every \(N\), and extending \(N\) does not alter earlier marks. Thus the family is prefix-consistent and contains no global size oracle.

This is the working formal meaning of `U1` in the central line.

## 3. Two-state phase witness

Take

\[
Q=\{0,1\},\quad q_0=0,\quad \delta(0)=1,\quad \delta(1)=0,
\]

with

\[
\lambda(0)=1,\qquad \lambda(1)=0.
\]

Externally, on generic ranks,

\[
M(P_{k+2})\iff k\equiv0\pmod2.
\]

Rank notation here is only the metamathematical description of the automaton run; rank is not added to the signature.

## 4. FCOA compilation with constant value

Compile the marker into a fresh partial operation \(\mu\):

\[
P_0\,\mu\,x=\Omega_M
\iff
x\in G_N\land M(x),
\]

with all other \(\mu\)-cells undefined and \(\Omega_M\) terminal.

Then

\[
M(x)\iff G(x)\land\operatorname{Def}(P_0\mu x).
\]

Thus the new information lives entirely in definedness; no differentiated output alphabet is needed.

## 5. U1 Escape Theorem

### Theorem 5.1

The two-state phase expansion is not a uniform FO-definitional expansion of G4-A. Hence it strictly leaves the exact G4-A order wall.

### Proof

Let

\[
m=N-1=|G_N|,
\]

and let \(M_G\) be the greatest generic element. Because the least generic point has phase `0` and the phases alternate,

\[
M(M_G)
\]

holds exactly when \(m-1\) is even, i.e. exactly when \(m\) is odd.

If \(M\) were uniformly FO-definable in G4-A, then by the hostile-audited Generic FO Collapse theorem it would be uniformly FO-definable in finite linear order. The sentence

\[
\exists x\,[\operatorname{Max}(x)\land M(x)]
\]

would define parity of finite-chain cardinality in FO[<], contradiction.

Therefore

\[
\boxed{U1\text{ finite-state generation can genuinely leave }FO[<].}
\]

\(\square\)

## 6. Candidate intermediate zone

The phase marker records only a residue class modulo a fixed finite period. It contains no rule comparing arbitrary interval lengths and no rule of the form

\[
\operatorname{rk}(z)=\operatorname{rk}(x)+\operatorname{rk}(y).
\]

Thus it is a natural candidate for an intermediate leakage layer

\[
AL0<AL\text{-}INT<AL1.
\]

The strict left inequality is proved above. The strict right inequality — nondefinability of EqGap/truncated addition from a fixed finite-state periodic marker — remains a theorem candidate and requires a separate hostile model-theoretic audit.

## 7. Prefix-consistent finite-state outputs are ultimately periodic

Because one fixed map

\[
\delta:Q\to Q
\]

is iterated on a finite set, every run has a finite transient followed by a cycle. Hence every unary marker produced by this exact U1 class is ultimately periodic.

Therefore every infinite U1 marker set has positive rational eventual density. In particular, if it is infinite then

\[
|M\cap G_N|=\Theta(N).
\]

Otherwise it is eventually empty and has only \(O(1)\) marked points.

Thus:

\[
\boxed{\text{prefix-consistent finite-state unary support is }O(1)\text{ or }\Theta(N).}
\]

There is no genuinely unbounded \(o(N)\) unary support inside this exact class.

## 8. State-complexity minimum

A one-state deterministic generator produces a constant marker: either every generic point is marked or none is. Both are already FO-definable from the generic sort and do not leave AL0.

The alternating witness uses two states. Therefore:

\[
\boxed{\text{minimum U1 state complexity for escaping }FO[<]\text{ is }2.}
\]

## 9. Operation-cell cost

For the alternating marker,

\[
|\operatorname{Dom}(\mu)|
=\left\lceil\frac{N-1}{2}\right\rceil
=\Theta(N).
\]

Only one anonymous terminal output is required. The boundary point \(P_0\) is not newly named; it is already internally definable in G4-A.

The working cost vector is therefore

\[
(\Theta(N),\ 1\text{ output},\ 2\text{ states},\ AL\text{-}INT).
\]

## 10. Extension-stability versus sparse oracle

The U1 witness differs fundamentally from the one-cell sparse oracle. For the oracle, whether the unique cell exists may depend arbitrarily on the final size \(N\), so extending the carrier may retroactively change the prefix. For U1, each point's mark is fixed when the point is reached and never changes under extension.

Thus:

\[
\boxed{\text{size-oracle sparsity}\neq\text{prefix-consistent finite-state memory}.}
\]

## 11. Revised central map

The central Arithmetic Leakage ladder now has an explicit candidate witness in the intermediate zone:

\[
AL0=FO[<],
\]

\[
AL\text{-}INT:\ \text{finite-state phase / modular information},
\]

\[
AL1:\ \text{EqGap / truncated addition},
\]

\[
AL2:\ \text{full arithmetic interpretation}.
\]

Only

\[
AL0<AL\text{-}INT
\]

is fixed here. The strict separation

\[
AL\text{-}INT<AL1
\]

is the next target.

## 12. Immediate next attack

The next exact question is:

\[
\boxed{\text{Can EqGap or truncated rank addition be uniformly FO-defined from finite order plus any fixed ultimately periodic finite-state coloring?}}
\]

A negative answer would establish a genuine **Finite-State Wall** between modular leakage and additive leakage.

## 13. Status

\[
\boxed{\mathbf F:\ \text{two-state prefix-consistent U1 marker leaves }FO[<]}
\]

\[
\boxed{\mathbf F:\ \text{one state cannot leave }FO[<]}
\]

\[
\boxed{\mathbf F:\ \text{unary U1 support is }O(1)\text{ or }\Theta(N)}
\]

\[
\boxed{\mathbf W:\ \text{Finite-State Wall: no EqGap/addition from fixed periodic coloring}}
\]
