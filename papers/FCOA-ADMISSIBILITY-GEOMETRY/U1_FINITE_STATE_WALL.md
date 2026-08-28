# U1 Finite-State Wall — Modular Memory Below the Additive Gateway

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate; director proof completed, hostile-audit checklist included  
**Scope:** prefix-consistent deterministic finite-state **unary** generators and their fixed FO-definitional FCOA compilations

## 1. Central question

The previous U1 construction proved that a two-state phase marker can leave the exact G4-A order wall:

\[
FO[<]
<
FO[<,M_{\mathrm{parity}}].
\]

The remaining question was whether finite-state phase information is already strong enough to recover the additive gateway:

\[
\operatorname{EqGap}
\quad\Longleftrightarrow\quad
\operatorname{Add}.
\]

The answer is **no** in the declared U1 class.

The resulting strict layer is

\[
\boxed{
AL0
<
AL\text{-}FS
<
AL1.
}
\]

Here `AL-FS` denotes finite-state / ultimately-periodic unary memory, not the whole informal `AL-INT` umbrella.

## 2. Exact U1 class audited here

Let

\[
G_N=\{P_2<\cdots<P_N\},
\qquad
m=N-1.
\]

A U1 unary generator is a deterministic finite-state machine

\[
\mathcal M=(Q,q_0,\delta,\lambda)
\]

with finite state set \(Q\), one initial state, transition

\[
\delta:Q\to Q,
\]

and finite output alphabet \(\Sigma\) through

\[
\lambda:Q\to\Sigma.
\]

It is run from the least generic point along successor:

\[
q(P_2)=q_0,
\qquad
q(\operatorname{Succ}(x))=\delta(q(x)).
\]

The same machine is used for every \(N\), and extending the carrier does not alter earlier outputs.

A finite family of such generators is allowed. Their outputs may be named as unary predicates, or compiled by any fixed FO-definitional template into fresh FCOA relations/partial-operation graphs.

This theorem does **not** claim to classify more general pair-automata, transitive closure, least fixed points, or generators whose transition depends on the final size \(N\).

## 3. Ultimately-periodic normal form

For one generator, the infinite output word

\[
w=w_0w_1w_2\cdots\in\Sigma^\omega
\]

is ultimately periodic because a single map \(\delta:Q\to Q\) is iterated on a finite set.

Thus there exist \(t\ge0\) and \(p\ge1\) such that

\[
w_{i+p}=w_i
\qquad(i\ge t).
\]

For finitely many U1 generators, take their product alphabet. The combined color word is again ultimately periodic.

Hence every finite U1 expansion of the generic order can be represented by the prefix family

\[
w\upharpoonright m=w_0\cdots w_{m-1}
\]

of one fixed ultimately periodic word.

## 4. Prefix regularity lemma

### Lemma 4.1

If \(w\in\Sigma^\omega\) is ultimately periodic, then

\[
\operatorname{Pref}(w)
=
\{w\upharpoonright m:m\ge0\}
\]

is a regular language.

### Proof

A finite automaton first checks the finite transient prefix. Once it reaches the eventual cycle, it loops through the period and accepts after every correctly matched prefix position. Any wrong letter moves to a rejecting sink. \(\square\)

No first-order definability of the prefix language is required; regularity is enough for the wall proof.

## 5. Word encoding of a hypothetical addition formula

Assume toward contradiction that one FO formula

\[
\varphi_+(x,y,z)
\]

in the language of order plus finitely many U1 unary colors uniformly defines canonical truncated rank addition on every finite prefix:

\[
\varphi_+(x,y,z)
\iff
\operatorname{rk}(z)=\operatorname{rk}(x)+\operatorname{rk}(y)<m.
\]

Introduce two marker tracks:

- `B` marks the unique position assigned simultaneously to \(x\) and \(y\);
- `Z` marks the unique position assigned to \(z\).

Require `Z` to mark the maximum position and require `B` and `Z` to be distinct.

Over the finite alphabet consisting of the U1 color together with these marker bits, let \(K\) be the language of marked prefixes satisfying these regular marker conditions and the translated formula

\[
\varphi_+(B,B,Z).
\]

The classical McNaughton-Papert theorem implies that every FO[<] language of finite words is star-free, hence regular. The formula part therefore defines a regular language. By Lemma 4.1 the valid-background prefix condition is also regular. Consequently

\[
\boxed{K\text{ is regular}.}
\]

## 6. Erasing the finite-state colors exposes a nonregular skeleton

Define a letter-to-letter homomorphism

\[
h
\]

that forgets all U1 colors and keeps only the marker type:

- an unmarked position maps to `a`;
- the unique `B` position maps to `b`;
- the final `Z` position maps to `c`.

Regular languages are closed under homomorphism, so \(h(K)\) would be regular.

Let the `B` marker occur at zero-based position \(n\). Since `Z` is the maximum of an \(m\)-point chain, it has rank \(m-1\). The addition condition is

\[
n+n=m-1.
\]

Thus \(m=2n+1\), and the marker skeleton is exactly

\[
a^n b a^{n-1}c
\qquad(n\ge1).
\]

Therefore

\[
\boxed{
h(K)=L:=\{a^n b a^{n-1}c:n\ge1\}.}
\]

### Lemma 6.1

The language \(L\) is not regular.

### Proof

Assume pumping length \(r\). Take

\[
a^rba^{r-1}c.
\]

Every pumping decomposition with the pumped block contained in the first \(r\) letters changes the length of the first `a`-block while leaving the second block unchanged. The required difference of exactly one between the two block lengths is destroyed. Contradiction. \(\square\)

Hence \(h(K)\) cannot be regular, contradicting Section 5.

## 7. Finite-State Wall Theorem

### Theorem 7.1 — no additive leakage from fixed U1 unary memory

Let the G4-A generic order be expanded by any finite collection of prefix-consistent deterministic finite-state unary generators. Then canonical truncated rank addition is not uniformly first-order definable across the finite family.

Equivalently,

\[
\boxed{
\operatorname{Add}_N
\notin
FO[<,\text{finite U1 unary colors}].
}
\]

The proof is Sections 3-6. \(\square\)

## 8. EqGap is also beyond the finite-state wall

The already fixed additive-gateway equivalence is

\[
\operatorname{Add}(x,y,z)
\iff
\operatorname{EqGap}(0_G,y;x,z),
\]

where \(0_G\) is the least generic point.

Therefore, if EqGap were uniformly FO-definable from U1 colors, then addition would be as well.

Hence:

\[
\boxed{
\operatorname{EqGap}_N
\notin
FO[<,\text{finite U1 unary colors}].
}
\]

Thus finite-state phase memory is genuinely weaker than the additive gateway.

## 9. Infinite supply of periodic predicates does not change the conclusion

Let `UP` denote the collection of **all** ultimately periodic unary predicates on generic rank.

Consider the infinite-signature family

\[
([m],<,(P)_{P\in UP}).
\]

Any single FO formula mentions only finitely many predicates. Their product coloring is still ultimately periodic, so Theorem 7.1 applies.

Therefore:

\[
\boxed{
\operatorname{Add}_N,
\operatorname{EqGap}_N
\notin
FO[<,UP].
}
\]

This is a useful closure statement: arbitrarily many available fixed modular/ultimately-periodic unary scales do not become variable displacement merely by first-order combination.

## 10. Return to the full FCOA signature

The U1 marker may be compiled into a fresh constant-valued partial operation, for example

\[
P_0\,\mu\,x=\Omega_M
\iff
M(x),
\]

with all other \(\mu\)-cells undefined.

More generally, suppose finitely many new symbols are obtained from G4-A plus finitely many U1 unary colors by fixed FO-definitional templates.

The full expanded FCOA structure is then uniformly obtainable from the colored finite order by the same fixed-copy G4-A transduction together with finitely many extra FO clauses. Conversely, every such compiled symbol can be eliminated in favor of its defining formula.

Hence the finite-state wall survives these compilations:

### Corollary 10.1 — compiled U1 wall

No fixed FO-definitional FCOA compilation of finitely many U1 unary generators can uniformly recover EqGap or truncated addition.

So the result concerns FCOA domain/value presentations, not merely externally named unary predicates.

## 11. Exact strict hierarchy

The two-state alternating marker from `U1_FINITE_STATE_LEAKAGE.md` satisfies

\[
M(P_{k+2})\iff k\equiv0\pmod2
\]

and is not uniformly FO-definable in pure finite order because the color of the maximum detects parity of \(m\).

Therefore the finite-state layer is strictly stronger than AL0.

Theorem 7.1 shows it is strictly weaker than the additive gateway.

We may now record the first fully witnessed strict post-G4 hierarchy:

\[
\boxed{
AL0
\;<\;
AL\text{-}FS
\;<\;
AL1.
}
\]

where

\[
AL0=FO[<],
\]

\[
AL\text{-}FS=FO[<,UP]
\]

for unary ultimately-periodic memory / any finite-state unary compilation used by a formula, and

\[
AL1=\text{EqGap / truncated-addition gateway}.
\]

`AL-FS` is a precise layer. The broader term `AL-INT` remains an umbrella for other possible intermediate mechanisms.

## 12. What crosses the wall and what does not

This theorem separates two kinds of memory.

Finite-state memory can preserve a **phase**:

\[
\operatorname{rk}(x)\bmod p.
\]

Additive memory must compare a **variable displacement**:

\[
\operatorname{rk}(b)-\operatorname{rk}(a)
=
\operatorname{rk}(d)-\operatorname{rk}(c).
\]

A fixed finite-state machine has only finitely many phases. EqGap asks the structure to transport an unbounded gap value from one interval to another.

The formal proof above turns that intuition into the nonregular marker language

\[
\{a^n b a^{n-1}c:n\ge1\}.
\]

Thus the new conceptual boundary is

\[
\boxed{
\text{finite phase memory}
\;<\;
\text{variable displacement memory}.
}
\]

## 13. Hostile-audit checklist

The proof was checked against the following failure modes.

1. **Finite transient:** harmless; the set of prefixes of an ultimately periodic word remains regular.
2. **Several U1 generators:** harmless; their product coloring is ultimately periodic.
3. **All ultimately periodic predicates in an infinite signature:** each formula uses only finitely many.
4. **Small carrier exceptions:** deleting or adding finitely many marked words cannot make the nonregular equal-block language regular.
5. **Use of terminal FCOA outputs:** harmless under fixed FO compilation; translate back to colored order first.
6. **Hidden rank arithmetic:** ranks occur only in the metamathematical specification of Add and in the analysis of marker positions. No rank operation is available to the defining formula.
7. **Background prefix not FO-definable:** not required; its language is regular, and regular languages are closed under intersection.
8. **FO-over-words theorem strength:** only the weak implication `FO[<] => regular` is used, although the classical theorem gives the stronger star-free characterization.

No defect was found in these checks.

## 14. Scope firewall

The theorem does **not** imply that every imaginable finite-state-looking binary or higher-arity generator is below addition.

The fixed class is:

\[
\boxed{
\text{prefix-consistent deterministic finite-state unary memory}
+
\text{fixed FO-definitional compilation}.
}
\]

Pair automata, synchronous transducers on two moving positions, reachability, transitive closure, least fixed points, or state spaces growing with \(N\) are outside this theorem and must be audited separately.

This scope restriction is essential.

## 15. Main-line consequence

The central question is no longer whether finite-state phase can reach EqGap. It cannot in the exact U1 class.

The next admissible attack is:

\[
\boxed{
\text{What is the weakest extension beyond finite unary phase that can carry an unbounded displacement value?}
}
\]

Natural candidates, in increasing apparent strength, are:

1. a two-position finite-state mechanism whose state depends on a moving interval rather than one absolute position;
2. a bounded-output relation generated by synchronized traversal of two intervals;
3. an unbounded but non-arithmetic closure/iteration mechanism;
4. hybrid memory in which two individually finite-state layers synchronize to transport a variable gap.

Any candidate must pass the Uniformity Firewall and must not assume EqGap in its generator.

## 16. Status

\[
\boxed{
\mathbf F:\ AL0<AL\text{-}FS
}
\]

from the two-state parity-phase witness.

\[
\boxed{
\mathbf F:\ AL\text{-}FS<AL1
}
\]

within the exact unary U1 / FO-compilation scope, by the regular-language obstruction above.

Thus:

\[
\boxed{
\mathbf F:\ AL0<AL\text{-}FS<AL1.
}
\]

The terminology `AL-FS` is programme terminology; the mathematical separation is the theorem.