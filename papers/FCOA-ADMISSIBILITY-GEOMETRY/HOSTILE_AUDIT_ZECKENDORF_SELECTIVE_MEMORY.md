# Hostile Audit — Zeckendorf Selective Additive Memory

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Role:** central hostile reconciliation for `ZECKENDORF_SELECTIVE_ADDITIVE_MEMORY.md`  
**Scope:** generated prefix-consistent subquadratic history, uniform FO addition, exclusion of uniform FO multiplication  
**Backend:** `FCOA_DEFINITION_1_0.md`, `UNIFORMITY_FIREWALL_AND_SPARSE_ORACLE.md`, `REGULAR_PRIMITIVE_BARRIER_AND_CLOSURE_PLACEMENT.md`, `BINARY_HISTORY_COMPRESSION_AND_OVERSHOOT.md`

---

## 1. Audit question

The candidate family stores Zeckendorf incidences

\[
Z(g_n,g_{F_j})
\iff
\varepsilon_j(n)=1,
\]

where

\[
F_0=1,\qquad F_1=2,\qquad F_{j+2}=F_{j+1}+F_j
\]

and

\[
n=\sum_j \varepsilon_j(n)F_j,
\qquad
\varepsilon_j(n)\in\{0,1\},
\qquad
\varepsilon_j(n)\varepsilon_{j+1}(n)=0.
\]

The intended conclusion is the exact selective corridor

\[
\boxed{
|Z_m|=\Theta(m\log m)=o(m^2),
\qquad
Add/EqGap\in FO(<,Z_m),
\qquad
Mul\notin FO(<,Z_m)
}
\]

uniformly over finite prefixes.

The hostile audit had ten targets. All ten are addressed below. One genuine presentation gap was found in the original candidate: merely saying that a finite-state normalization transducer produces digit positions does not by itself explain how those positions are attached to the *same-carrier points* `g_{F_j}` without a Fibonacci-rank oracle. Section 8 repairs this by a self-anchoring generator.

---

## 2. Audit item 1 — semantics of the Walnut Fibonacci adder

The source automaton used by the candidate is the Walnut custom-base file

`Custom Bases/msd_fib_addition.txt`

from `firetto/Walnut`, source blob

`cf7be811768be7aa981b3a7a38a9688783ee98e5`.

The repository file `experiments/fcoa-domain-compilation/verify_zeckendorf_adder_aperiodic.py` reproduces that transition table exactly, completes missing transitions by one rejecting sink, and performs independent finite semantic checks.

There is also an external verification route stronger than finite testing. In the Walnut/Ostrowski construction literature, this same Fibonacci adder is verified as a function and then by:

1. the base case `A(x,0)=x`;
2. an induction step transporting `A(x,y,z)` along simultaneous successors of `y` and `z`.

Thus the automaton is not being treated as an unexplained empirical object.

### Audit verdict

\[
\boxed{\mathbf F:\ \text{the cited Walnut automaton recognizes Zeckendorf addition on canonical inputs}.}
\]

This is a classical automata/numeration input, not a new FCOA theorem.

---

## 3. Audit item 2 — aperiodicity of the completed DFA

The committed verifier constructs the completed eight-state DFA:

- seven listed Walnut states;
- one rejecting sink for missing transitions.

It then enumerates the full transition monoid.

The exact certificate is:

\[
\boxed{|M|=83}
\]

and every transformation stabilizes at an idempotent power with exponent at most

\[
\boxed{4}.
\]

Therefore the transition monoid is aperiodic.

This computation was independently reproduced from the source transition table during the present hostile audit.

### Audit verdict

\[
\boxed{\mathbf F:\ \text{the completed Walnut Fibonacci-addition DFA has an aperiodic transition monoid}.}
\]

The certificate is finite and exactly reproducible by the committed script.

---

## 4. Audit item 3 — aperiodicity to FO[<]

Let `L_+` be the ternary digit language recognized by the completed DFA.

If a DFA transition monoid is aperiodic, then its syntactic monoid is aperiodic as well, because the syntactic monoid is a quotient of the transition action relevant to the recognized language. By the Schuetzenberger/McNaughton-Papert characterization, an aperiodic regular language is star-free, equivalently first-order definable over finite word positions with order.

Hence there exists one fixed sentence

\[
\psi_+
\]

in `FO[<]` over the eight letter predicates

\[
L_{abc},\qquad (a,b,c)\in\{0,1\}^3,
\]

such that for every finite canonical Zeckendorf triple word,

\[
\psi_+
\iff
x+y=z.
\]

### Audit verdict

\[
\boxed{\mathbf F:\ \text{the aperiodicity certificate is used in the correct direction}.}
\]

No converse or minimization assumption is needed.

---

## 5. Audit item 4 — carrier realization of digit positions

Define inside the final incidence structure

\[
FibPos(p):=Z(p,p).
\]

### Lemma 5.1 — diagonal anchor lemma

For every carrier point `p`,

\[
\boxed{
FibPos(p)
\iff
p=F_j\text{ for some }j.
}
\]

### Proof

By definition, a second-coordinate point can occur positively in `Z` only when it is a Fibonacci weight `F_j`. Hence `Z(p,p)` implies `p=F_j` for some `j`.

Conversely, the canonical Zeckendorf representation of `F_j` is the singleton basis word with digit `1` exactly at position `j`. Therefore

\[
Z(F_j,F_j)
\]

holds. `□`

Thus the ordered set of digit positions is internally available as the definable diagonal subset

\[
D_m:=\{p<m:FibPos(p)\}.
\]

For target points `x,y,z`, define the word-letter predicates on `D_m` by

\[
L_{abc}^{x,y,z}(p)
\]

iff

\[
FibPos(p)
\]

and the truth values of

\[
Z(x,p),\quad Z(y,p),\quad Z(z,p)
\]

are exactly `a,b,c`.

The ambient order on Fibonacci weights is the reverse of the usual MSD-to-LSD reading direction. Reversal is harmless: replace the word-order atom `<` in `\psi_+` by `>`.

### Audit verdict

\[
\boxed{\mathbf F:\ \text{word positions are uniformly FO-realized by }FibPos(p)=Z(p,p).}
\]

---

## 6. Audit item 5 — finite-prefix boundary

Fix a prefix

\[
G_m=\{0,\ldots,m-1\}.
\]

Every `x<m` uses only Fibonacci weights `<m`; hence every nonzero Zeckendorf digit of `x` is represented by an element of `D_m`.

The set `D_m` may contain additional weights above the highest nonzero digit of the particular triple `(x,y,z)`. On those positions all three tracks carry `0`.

In the source DFA, the initial state has the transition

\[
000\longmapsto 000
\]

as a self-loop. Therefore adding arbitrary leading zero columns does not change acceptance.

Consequently the translation of `\psi_+` to the definable finite position set `D_m` sees exactly the same word as the canonical adder, up to harmless leading zeros.

### Theorem 6.1 — exact finite-prefix addition

There is one fixed FO formula

\[
Add_Z(x,y,z)
\]

such that for every `m` and every `x,y,z<m`,

\[
\boxed{
Add_Z(x,y,z)
\iff
x+y=z<m.
}
\]

### Proof

Relativize every word-position quantifier of `\psi_+` to `FibPos`, reverse the order atom, and replace each letter predicate by the corresponding Boolean combination of `Z(x,p),Z(y,p),Z(z,p)`. Sections 4 and 5 identify the resulting finite word with the padded canonical Zeckendorf triple. The adder semantics from Section 2 completes the proof. `□`

Because `EqGap` and truncated addition are already uniformly interdefinable in the central programme,

\[
\boxed{EqGap\in FO(<,Z).}
\]

### Audit verdict

\[
\boxed{\mathbf F:\ \text{no false witness is created by the missing positions above the prefix}.}
\]

---

## 7. Audit item 6 — recognizability of the incidence relation

Consider canonical Zeckendorf words for `x` and `p`, synchronously padded in the standard automatic-presentation sense.

The relation

\[
Z(x,p)
\]

has the following regular description:

1. the representation of `p` contains exactly one `1`;
2. at the unique position where the `p`-track has `1`, the `x`-track also has `1`.

For canonical Fibonacci representations, a word with exactly one `1` represents exactly one basis weight `F_j`. A finite automaton needs only three control statuses: before the unique `1`, after the unique `1`, and reject, together with the regular validity checks for canonical Fibonacci words.

Hence

\[
\boxed{Z\subseteq\mathbb N^2\text{ is Fibonacci-recognizable}.}
\]

The canonical Fibonacci representation language is regular, and order is synchronously recognizable. Therefore the infinite structure

\[
\mathfrak Z=(\mathbb N,<,Z)
\]

has a word-automatic presentation.

### Audit verdict

\[
\boxed{\mathbf F:\ \mathfrak Z\text{ is word-automatic}.}
\]

---

## 8. Audit item 9 — generator firewall and the self-anchoring repair

This was the genuinely dangerous point.

The specification

\[
Z(n,F_j)\iff\varepsilon_j(n)=1
\]

is not by itself an admissible generator. A normalization transducer naturally produces a digit sequence indexed by abstract positions `j`; if one then silently places the `j`-th output at carrier rank `F_j`, the construction has imported the Fibonacci scale it was supposed to generate.

The repair is to let the accumulated history create its own coordinate anchors.

### Classical finite-state input

Fibonacci/Zeckendorf normalization is realizable by a fixed finite transducer; successor is a special case. Equivalently, there exists one finite-state transduction

\[
T_{succ}:rep_F(n)\mapsto rep_F(n+1).
\]

This is a standard consequence of finite-state normalization in the Fibonacci/Pisot numeration system; finite-state and on-line addition in the golden-ratio/Fibonacci setting are classical results of Frougny and related work.

### Definition 8.1 — self-anchored row generator

Assume rows through `n` have already been generated. Let

\[
A(p):=Z(p,p).
\]

Scan the old carrier in increasing order, but feed a symbol to `T_succ` only at positions satisfying `A(p)`. At such a position the input digit is

\[
Z(n,p)\in\{0,1\}.
\]

At non-anchor positions the finite control simply skips the point.

For every existing anchor `p`, write

\[
Z(n+1,p)
\]

iff the successor transducer outputs `1` at that digit position.

If the successor transducer creates one new most-significant digit beyond all old digit positions, place that new digit at the newly appended carrier maximum itself:

\[
Z(n+1,n+1).
\]

No other new second-coordinate point is activated.

A finite seed handles `0,1,2`.

### Lemma 8.2 — self-anchor invariant

After generation of row `n`, the anchor sequence is exactly

\[
\{p\le n:A(p)\}
=
\{F_j:F_j\le n\},
\]

and the row values on those anchors are exactly the canonical Zeckendorf digits of `n`.

### Proof

Induct on `n`.

Assume the claim for row `n`. Reading the previous row only at diagonal anchors therefore supplies `T_succ` with the canonical digit word `rep_F(n)` in digit order. The fixed transducer outputs `rep_F(n+1)`.

If no new most-significant digit is required, all output positions correspond to already existing anchors, so the generated row is correct and the anchor set is unchanged.

If a new most-significant digit is required, then `n+1` is exactly the first integer using the next Fibonacci weight, hence

\[
n+1=F_{k+1}
\]

when the previous largest anchor was `F_k`. Its canonical representation has singleton new top digit `1`. The rule therefore writes

\[
Z(n+1,n+1),
\]

so the new carrier maximum becomes precisely the next diagonal anchor. No numerical test `n+1=F_{k+1}` is performed by the generator; that equality is the induction invariant proved from the finite-state successor semantics.

Thus both the anchor set and the new row remain correct. `□`

### Corollary 8.3 — no Fibonacci-rank oracle

The generator uses only:

- the recovered carrier order/successor traversal;
- the previous generated row;
- the already generated diagonal anchor predicate `Z(p,p)`;
- one fixed finite-state successor/normalization transducer;
- the newly appended maximum when a fresh top digit is emitted.

It does **not** query:

- numerical rank;
- the function `j\mapsto F_j`;
- addition, multiplication or EqGap;
- the final prefix size `m`;
- any arbitrary size-dependent oracle.

Hence the same-carrier realization is prefix-consistent and generated rather than imported.

### Relation to earlier barriers

This does not contradict `U1_FINITE_STATE_WALL.md`: that theorem is explicitly restricted to finitely many deterministic **unary** finite-state color generators. The present mechanism is a growing two-dimensional history whose next row is generated by finite control from the previous row.

It also does not contradict the Regular-Primitive Barrier. The final relation `Z` is not a fixed position-regular primitive. Unbounded history has been materialized, exactly as required by the Closure-Placement Principle.

### Audit verdict

\[
\boxed{\mathbf F:\ \text{the Zeckendorf history admits a self-anchored prefix generator without an arithmetic oracle}.}
\]

The term “finite-state generator” must always be qualified as **row-recursive generated history**, not confused with unary `AL-FS` memory.

---

## 9. Audit items 7 and 8 — a cleaner multiplication obstruction

The original candidate used prefix-spectrum decidability plus a Hilbert-10 reduction. That route is valid in spirit, but a shorter argument removes several moving parts.

### Classical automatic-structure theorem

The first-order theory of every word-automatic structure is decidable. Equivalently, from an automatic presentation and a first-order formula one can effectively construct an automaton for its satisfying tuples.

By Section 7,

\[
\mathfrak Z=(\mathbb N,<,Z)
\]

is word-automatic. Hence

\[
Th_{FO}(\mathfrak Z)
\]

is decidable.

### Lemma 9.1 — prefix-lift lemma

Let `\varphi(x_1,\ldots,x_r)` be one fixed FO formula that has an intended meaning uniformly on every induced prefix

\[
\mathfrak Z_m=\mathfrak Z\upharpoonright [m].
\]

For a boundary variable `b`, let

\[
\varphi^{<b}
\]

be obtained by relativizing every quantifier to elements `<b`.

Then

\[
\exists b\,[x_1<b\land\cdots\land x_r<b\land\varphi^{<b}(x_1,\ldots,x_r)]
\]

holds in the infinite structure exactly when `\varphi` holds in at least one sufficiently large finite prefix containing the tuple.

### Proof

The substructure induced by

\[
\{u:u<b\}
\]

is exactly the finite prefix `\mathfrak Z_b`, because the family is prefix-consistent. Relativized FO semantics is therefore identical to evaluation in that induced prefix. `□`

### Theorem 9.2 — Automatic Prefix-Lift Barrier

There is no fixed FO formula that uniformly defines canonical truncated multiplication in every finite prefix `\mathfrak Z_m`.

### Proof

Section 6 gives one fixed formula `Add_Z` defining truncated addition on every prefix.

Assume for contradiction that a fixed formula `Mul_Z` defines truncated multiplication on every prefix.

Use Lemma 9.1 to define on the infinite structure:

\[
Add_\infty(x,y,z)
:\iff
\exists b>x,y,z\; Add_Z^{<b}(x,y,z),
\]

and

\[
Mul_\infty(x,y,z)
:\iff
\exists b>x,y,z\; Mul_Z^{<b}(x,y,z).
\]

Exactness on every prefix gives

\[
Add_\infty(x,y,z)\iff x+y=z,
\]

\[
Mul_\infty(x,y,z)\iff xy=z.
\]

Hence ordinary first-order arithmetic

\[
(\mathbb N,+,\times)
\]

would be first-order definable in the word-automatic structure `\mathfrak Z`.

But `\mathfrak Z` has decidable first-order theory, whereas first-order arithmetic with addition and multiplication is undecidable. Contradiction. `□`

### Consequence

The Hilbert-10 prefix-spectrum route may be retained as an alternative calibration, but it is no longer needed for the main theorem.

### Audit verdict

\[
\boxed{\mathbf F:\ Mul\text{ is not uniformly FO-definable on the Zeckendorf prefix family}.}
\]

---

## 10. Audit item 10 — support on arbitrary prefixes

Let

\[
s_F(n)
\]

be the number of summands in the Zeckendorf expansion of `n`. Then

\[
|Z_m|
=
\sum_{n<m}s_F(n).
\]

Classical Lekkerkerker theory gives, on a Fibonacci block

\[
[F_k,F_{k+1}),
\]

average summand count

\[
\Theta(k).
\]

Since

\[
F_k=\Theta(\varphi^k),
\]

we have

\[
k=\Theta(\log F_k).
\]

For arbitrary `m`, choose `k` with

\[
F_k\le m<F_{k+1}.
\]

Every representation below `m` has `O(k)` digits and therefore at most `O(k)` summands, giving

\[
|Z_m|=O(mk)=O(m\log m).
\]

For the lower bound, the complete preceding Fibonacci block already contributes

\[
\Theta(F_{k-1}k).
\]

Because `m<F_{k+1}=\Theta(F_{k-1})`, this is

\[
\Omega(mk)=\Omega(m\log m)
\]

up to fixed Fibonacci-ratio constants.

Therefore

\[
\boxed{|Z_m|=\Theta(m\log m).}
\]

In particular,

\[
\boxed{|Z_m|=o(m^2).}
\]

### Audit verdict

\[
\boxed{\mathbf F:\ \text{the subquadratic support estimate holds for arbitrary prefixes, not only Fibonacci endpoints}.}
\]

---

## 11. Consolidated theorem

### Theorem 11.1 — Generated Zeckendorf Selective Compression

There exists a fixed finite-signature, prefix-consistent generated FCOA history family whose active base carrier is the recovered ordered chain and whose principal added incidence relation has support

\[
\Theta(m\log m),
\]

such that:

1. the history is generated by a fixed self-anchored finite-state row recurrence with no final-size, rank, addition, multiplication or Fibonacci-scale oracle;
2. canonical truncated addition is uniformly first-order definable;
3. EqGap is uniformly first-order definable;
4. canonical truncated multiplication is not uniformly first-order definable.

Hence the family lies exactly at the additive phase:

\[
\boxed{FTR=1.}
\]

and realizes

\[
\boxed{
AL1\ \text{with}\ o(m^2)\ \text{materialized support}.}
\]

### Proof

Generation is Section 8; support is Section 10; addition/EqGap are Sections 4-6; multiplication exclusion is Section 9. `□`

---

## 12. Main programme consequence

The former open corridor

\[
\boxed{
\text{generated }o(m^2)\text{ memory}
+ Add
- Mul
}
\]

is nonempty.

Therefore the central question is no longer whether selective subquadratic additive compression exists. It does.

The binary and Zeckendorf histories now give a direct same-cost-scale phase split:

\[
\boxed{
\begin{array}{rcl}
\text{binary history} &:& \Theta(m\log m),\quad AL2,\\[2mm]
\text{Zeckendorf history} &:& \Theta(m\log m),\quad AL1.
\end{array}}
\]

This strengthens Density-Leakage Orthogonality:

\[
\boxed{
\text{even the same asymptotic support and the same broad “digit-history” architecture can occupy different arithmetic phases}.}
\]

The separator is no longer density alone. It lies in the logical/automata structure of the exposed digit coordinate system.

---

## 13. New frontier

The next central problem should not reopen the solved existence question. The sharper problems are:

1. **Optimal support:** can exact generated AL1 be reduced from `Theta(m log m)` to `Theta(m)` or another smaller asymptotic class under a declared generator model?
2. **Generator-class invariant:** characterize the weakest row-recursive/history generator class that permits AL1 but still excludes AL2.
3. **Interpretation invariance:** identify a representation-independent obstruction preventing an exotic recoding of the Zeckendorf witness from exposing multiplication.
4. **Automatic-prefix principle:** determine how broadly the Prefix-Lift Barrier extends to other automatic or decidable generated histories.
5. **Same-cost phase taxonomy:** classify which numeration histories of `Theta(m log m)` support are exact AL1 and which overshoot to AL2.

The most immediate mathematical strike is (1):

\[
\boxed{
\text{is }\Theta(m\log m)\text{ optimal for provenance-safe generated exact AL1, or can one reach }\Theta(m)?
}
\]

This is now a genuine optimization question because existence of the corridor itself is closed.

---

## 14. Status ledger

Promoted by this hostile reconciliation:

\[
\boxed{\mathbf F:\ \text{self-anchored Zeckendorf history is prefix-generated without a Fibonacci oracle}.}
\]

\[
\boxed{\mathbf F:\ |Z_m|=\Theta(m\log m).}
\]

\[
\boxed{\mathbf F:\ Add,EqGap\in FO(<,Z_m)\text{ uniformly}.}
\]

\[
\boxed{\mathbf F:\ Mul\notin FO(<,Z_m)\text{ uniformly}.}
\]

Therefore:

\[
\boxed{\mathbf F:\ \text{the generated Presburger Compression Corridor is nonempty}.}
\]

Working/open:

\[
\boxed{\mathbf O:\ \text{optimal support of generated exact AL1}.}
\]

\[
\boxed{\mathbf W:\ \text{canonical resource name/class for self-anchored row-recursive finite-state history}.}
\]

No claim is made that the Zeckendorf construction is support-optimal.

---

## References used in the audit

- `firetto/Walnut`, `Custom Bases/msd_fib_addition.txt`, blob `cf7be811768be7aa981b3a7a38a9688783ee98e5`.
- Christiane Frougny, “On-line finite automata for addition in some numeration systems,” *RAIRO. Theoretical Informatics and Applications* 33(1), 1999, 79–101, DOI `10.1051/ita:1999107`.
- Classical Schuetzenberger / McNaughton-Papert equivalence between aperiodic regular languages, star-free languages and `FO[<]` on finite words.
- Classical Khoussainov-Nerode / Blumensath-Graedel decidability theorem for first-order theories of automatic structures.
- Murat Kologlu, Gene S. Kopp, Steven J. Miller, Yinghui Wang, “On the Number of Summands in Zeckendorf Decompositions,” *The Fibonacci Quarterly* 49(2), 2011, 116–130, DOI `10.1080/00150517.2011.12428056`.
