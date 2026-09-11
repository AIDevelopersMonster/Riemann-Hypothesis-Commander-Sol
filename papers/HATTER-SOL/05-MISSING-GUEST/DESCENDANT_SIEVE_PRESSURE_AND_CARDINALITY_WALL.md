# HATTER-SOL-05 · Descendant Sieve Pressure and the Cardinality Wall

## 0. Status

Canonical v1.0 source after hostile proof audit.

The purpose of this note is twofold:

1. prove that the local \(3\)-versus-\(5\) sieve asymmetry persists along exact-support descendant chains;
2. state precisely what that asymmetry cannot prove about graph automorphisms.

The former draft overstated the descendant no-go theorem. What is proved below is a **levelwise finite fixed-divisor-cover barrier**. Cross-level correlated congruence mechanisms are not excluded.

---

# 1. Local divisor profile

For a finite support \(S\ni2\) define

\[
N_S(\mathbf e)=1+\prod_{q\in S}q^{e_q},
\qquad \mathbf e\in\mathbb N_{>0}^{S}.
\]

Let \(\ell\notin S\) be prime and set

\[
H_\ell(S)=\langle q\bmod\ell:q\in S\rangle
\le(\mathbb Z/\ell\mathbb Z)^\times.
\]

## Theorem 1.1 — one-prime local divisor density

As \(\mathbf e\) ranges over large boxes,

\[
\delta_\ell(S)
:=
\lim_{B\to\infty}
\frac{\#\{\mathbf e\in[1,B]^S:\ell\mid N_S(\mathbf e)\}}{B^{|S|}}
\]

exists and equals

\[
\boxed{
\delta_\ell(S)=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\
0,&-1\notin H_\ell(S).
\end{cases}
}
\]

### Proof

Let \(M\) be the least common multiple of the multiplicative orders of the elements of \(S\) modulo \(\ell\). The map

\[
(\mathbb Z/M\mathbb Z)^S\to H_\ell(S),
\qquad
\mathbf e\mapsto\prod_{q\in S}q^{e_q}
\]

is a surjective homomorphism, so its fibers are equicardinal. Divisibility by \(\ell\) is exactly the condition that the image equals \(-1\). \(\square\)

---

# 2. Universal \(3\)-versus-\(5\) gap

Since \(2\) generates both \((\mathbb Z/3\mathbb Z)^\times\) and \((\mathbb Z/5\mathbb Z)^\times\), for every finite support \(S\ni2\),

\[
3\notin S\Longrightarrow\delta_3(S)=\frac12,
\]

and

\[
5\notin S\Longrightarrow\delta_5(S)=\frac14.
\]

Call \(S\) **3-pure** if

\[
2,3\in S,
\qquad
5\notin S.
\]

If a partial or global graph automorphism \(g\) extends the seed transposition \((3\ 5)\) on \(S\), then \(gS\) is 5-pure:

\[
2,5\in gS,
\qquad
3\notin gS.
\]

Therefore

\[
\boxed{
1-\delta_5(S)=\frac34,
\qquad
1-\delta_3(gS)=\frac12,
}
\]

and the local survival ratio is

\[
\boxed{\frac32.}
\]

---

# 3. Hereditary purity under exact descendants

Suppose \(S\) is 3-pure and \(p\in X_S\), where

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\}.
\]

Then

\[
S^+=S\cup\{p\}
\]

is again 3-pure. Indeed, \(3\in S^+\), while \(p\ne5\) and \(5\notin S\).

Thus any chain formed recursively by adjoining an exact descendant,

\[
S_0\subset S_1\subset\cdots\subset S_m,
\]

remains 3-pure provided it starts 3-pure and \(5\) is never externally inserted. Its image under an extension of \((3\ 5)\) is correspondingly 5-pure.

Hence the factor \(3/2\) reappears at every level.

---

# 4. External pressure functional

For a finite 3-pure chain \(\mathcal S=(S_0,\ldots,S_m)\), define

\[
\mathfrak P_5(\mathcal S)
=
\prod_{j=0}^m(1-\delta_5(S_j)),
\]

and for its swapped chain

\[
\mathfrak P_3(g\mathcal S)
=
\prod_{j=0}^m(1-\delta_3(gS_j)).
\]

Then

\[
\boxed{
\frac{\mathfrak P_5(\mathcal S)}{\mathfrak P_3(g\mathcal S)}
=
\left(\frac32\right)^{m+1}.
}
\]

This is an **external bookkeeping functional** only. It is not:

- a joint probability across descendant levels;
- a joint density theorem for simultaneous prime values;
- an invariant definable in the language of the directed prime graph;
- evidence of independence between levels.

Its role is to record the repeated one-level sieve discrepancy and nothing more.

---

# 5. Compatibility with the cyclotomic obstruction

For \(|S|=k\ge2\), the density of exponent vectors whose common gcd has no odd prime divisor is

\[
c_k=\frac1{\zeta(k)(1-2^{-k})}.
\]

Because the omitted-prime bad condition is preserved under odd common dilation of the exponent vector, the Möbius argument combines with the local sieve exactly. Thus for 3-pure \(S\), the density surviving both the common-odd-divisor obstruction and the omitted-5 sieve is

\[
\boxed{\frac34c_k,}
\]

whereas the swapped support has corresponding density

\[
\boxed{\frac12c_k.}
\]

The ratio remains \(3/2\) in every support dimension.

---

# 6. Cardinality wall

The multiplicity tower records only

\[
\mu(S)=|X_S|.
\]

Since the prime set is countable,

\[
\mu(S)\in\{0,1,2,\ldots,\aleph_0\}.
\]

## Theorem 6.1 — blindness to quantitative asymptotics

If exact fibers \(X_S\) and \(X_T\) are both infinite, then

\[
\boxed{\mu(S)=\mu(T)=\aleph_0,}
\]

regardless of differences in local sieve densities, asymptotic constants, exponent distributions, or growth laws.

Thus an extension obstruction visible to the multiplicity tower must ultimately take one of the forms

\[
\boxed{\text{empty vs nonempty},}
\]

\[
\boxed{\text{finite vs infinite},}
\]

or

\[
\boxed{\text{different finite cardinalities}.}
\]

### Proof

Every infinite subset of the countable prime set is countably infinite. The one-level extension criterion compares only fiber cardinalities. \(\square\)

---

# 7. The precise descendant barrier

The previous draft stated a stronger no-go claim than the argument justified. The correct theorem is the following.

## Theorem 7.1 — levelwise finite fixed-divisor-cover barrier

Fix any finite collection of exact-support levels in a descendant construction. At each chosen level, suppose the proposed killing argument uses only a finite set of **fixed prime divisors** to cover all candidate exponent vectors for that level.

Then such a levelwise covering argument cannot prove emptiness of the corresponding exact fiber.

### Proof

For every fixed finite support \(S\ni2\), the finite-cover escape theorem from the preceding HATTER-SOL-05 note gives candidate exponent vectors avoiding any prescribed finite set of prime divisors. Therefore no individual exact-support family can be annihilated by a finite fixed-divisor cover. Applying this independently to each member of a finite collection of levels proves the statement. \(\square\)

### Scope

This theorem does **not** rule out:

- congruence conditions whose controlling divisor varies with the exponent vector;
- mechanisms coupling several descendant levels simultaneously;
- correlated cross-level congruence obstructions;
- deep prime-value theorems forcing finite or empty exact fibers.

Accordingly, the valid conclusion is narrower:

\[
\boxed{
\text{finite levelwise fixed-divisor covers do not kill }(3\ 5).
}
\]

The remaining arithmetic problem is not reduced to local covering congruences.

---

# 8. Heuristic dimension test — not a theorem

For a support \(S=\{q_1,\ldots,q_k\}\), the number of exponent vectors with

\[
\sum e_i\log q_i\le L
\]

is of order \(L^k\). After the controlled cyclotomic and finitely many local exclusions, a positive proportion survives when \(k\ge2\). A naive prime-probability factor of order \(1/L\) would therefore predict cumulative growth of order \(L^{k-1}\).

This suggests, but does not prove, a phase transition between \(|S|=1\) and \(|S|\ge2\). In particular, infinitude of the Pierpont-prime exact fiber is still open.

No part of this heuristic is used in the rigorous automorphism conclusions.

---

# 9. Publication conclusion

The descendant strike has reached a clean structural endpoint for HATTER-SOL-05:

1. local \(3\)-versus-\(5\) asymmetry is hereditary along exact-descendant chains;
2. the repeated factor is exactly \(3/2\);
3. the pressure product is only an external summary of separate levelwise effects;
4. the multiplicity tower erases every quantitative distinction once both fibers are infinite;
5. finite fixed-divisor covers cannot kill a fiber levelwise, but more sophisticated correlated mechanisms remain possible.

This note is frozen for HATTER-SOL-05 v1.0. Any attempt to derive an orbitwise necessary-and-sufficient survival condition or a genuinely cross-level arithmetic obstruction belongs to the next research stage rather than to the publication gate of the fifth paper.
