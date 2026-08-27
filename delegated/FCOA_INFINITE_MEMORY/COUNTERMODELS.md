# Countermodels and Adversarial Tests

## CM-1 — Rigid but FO-incomplete memory

Structure:

\[
(G_\omega,S)=(P_2\to P_3\to\cdots).
\]

Facts:

\[
\operatorname{Aut}(G_\omega,S)=1,
\]

but the full strict order/reachability relation is not FO-definable.

Use: defeats any argument of the form

\[
\text{trivial automorphism group}\Rightarrow\text{global FO recoverability}.
\]

---

## CM-2 — Per-size formulas without a uniform formula

For every finite \(N\), order on the path \(G_N\) is definable by a finite disjunction of successor distances. The required disjunction grows with \(N\).

Use: defeats

\[
\forall N\ \exists\varphi_N
\quad\Rightarrow\quad
\exists\varphi\ \forall N.
\]

EF strategy: for each quantifier rank \(q\), choose a sufficiently long finite path and two interior points \(a<b\) separated from one another and from the endpoints by more than the standard \(2^q\) locality radius. Duplicator matches bounded neighborhoods after swapping the distinguished pair. Strict order changes truth value, so no rank-q formula defines it uniformly.

---

## CM-3 — Local finite enrichment does not imply global order

Take the infinite successor ray and add any fixed finite family of relations each definable by a bounded successor pattern, such as:

- predecessor;
- exact distance \(k\) for finitely many fixed \(k\);
- finitely many named nodes;
- local two-valued orientation coloring on successor edges;
- finitely many boundary anchors.

This is a definitional expansion of the successor structure and therefore cannot define the full transitive order if successor alone cannot.

Use: defeats attempts to promote an infinite local G3 analogue into full FO order memory.

---

## CM-4 — Anonymous outputs behave differently on finite chains and on \(\omega\)

Finite complete comparison coloring:

\[
\Omega_+\text{ for }i<j,\qquad \Omega_-\text{ for }i>j
\]

retains reversal with output swap.

Infinite \(\omega\)-ray version has no order reversal because the least endpoint has no matching greatest endpoint. The positive output is intrinsically definable.

Use: defeats blind transfer of finite output-swap automorphisms to the infinite carrier.

---

## CM-5 — One output on complete domain cannot encode orientation

If every distinct pair receives the same terminal value, the complete off-diagonal domain is invariant under all permutations of the generic carrier. Full order is not recoverable.

Use: establishes lower bound |O|>1 inside the complete-domain terminal-color architecture.
