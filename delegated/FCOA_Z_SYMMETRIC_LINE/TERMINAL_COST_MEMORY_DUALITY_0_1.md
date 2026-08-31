# FCOA-Z — Terminal Cost-Memory Duality 0.1

**Date:** 2026-08-31  
**Status:** PROVED CORE / HOSTILE AUDIT REQUIRED  
**Depends on:** `TERMINAL_LIFT_PROFILE_AND_RELATIVE_RECONSTRUCTION_0_1.md`, `FINITE_CHANNEL_COUPLING_CLASSIFICATION_0_1.md`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Question

After equality coupling forces global terminal uniformity, two canonical profiles remain:

\[
ZM0\text{-share}
\qquad\text{and}\qquad
ZM0\text{-split}.
\]

Pure equality constraints cannot choose between them because of global complement symmetry.

The next question is whether a **structurally natural FCOA criterion** can select one without inserting an arbitrary external bit.

Two natural criteria exist, but they select opposite endpoints:

- minimal output-extension cost selects `share`;
- maximal terminal branch-memory selects `split`.

More strongly, for every orbitwise profile there is an exact cost-memory identity.

---

## 2. Finite signed window

Fix

\[
W_N
=
\{x_0\}
\cup
\{x_n^+,x_n^-:1\le n\le N\}.
\tag{2.1}
\]

Let \(\mathcal I_N\) be the terminal-producing positive reflection-orbit indices visible in \(W_N\).

They are:

### `oplus` diagonal channel

\[
(+,n),
\qquad 1\le n\le N,
\]

so there are \(N\) such indices.

### `otimes` root-escape channel

\[
(*,n),
\qquad 2\le n\le N,
\]

so there are \(N-1\) such indices for \(N\ge2\).

### `otimes` diagonal channel

\[
(\times,n),
\qquad 2\le n\le N,
\]

again \(N-1\) indices.

Hence for \(N\ge2\),

\[
\boxed{
Q_N:=|\mathcal I_N|=3N-2.
}
\tag{2.2}
\]

For \(N=1\), only the `oplus` diagonal orbit occurs, so \(Q_1=1\).

---

## 3. Extension cost

The positive legacy M0 already contains one terminal element \(E_q\) for each \(q\in\mathcal I_N\).

### Definition 3.1 — mirror extension cost

For an orbitwise lift profile \(\epsilon\), define

\[
C_N(\epsilon)
\]

as the number of **new terminal elements** that must be added beyond the positive legacy output universe in order to realize the signed reflection closure on \(W_N\).

A shared orbit adds no new element.

A split orbit adds exactly one fresh reflected mate.

Therefore:

### Proposition 3.2

\[
\boxed{
C_N(\epsilon)
=
\sum_{q\in\mathcal I_N}\epsilon(q).
}
\tag{3.1}
\]

### Proof

Each profile bit equal to zero contributes no additional output; each bit equal to one contributes exactly one new mate, and the canonical orbitwise class forbids identifications between different indices. \(\square\)

---

## 4. Terminal branch-memory score

The reflected positive and negative source cells at orbit \(q\) are branch mirrors of each other.

### Definition 4.1 — separated mirror orbit

A terminal-producing orbit \(q\) is **branch-separated** if the positive and negative mirror cells have distinct terminal values.

This holds exactly for split fibers.

### Definition 4.2 — branch-memory score

Let

\[
M_N(\epsilon)
\]

be the number of terminal-producing reflection orbits in \(W_N\) whose two branch-mirror source cells remain distinguishable by terminal value.

Then:

### Proposition 4.3

\[
\boxed{
M_N(\epsilon)
=
\sum_{q\in\mathcal I_N}\epsilon(q).
}
\tag{4.1}
\]

### Proof

A shared orbit maps both mirror cells to the same output and contributes zero. A split orbit maps them to distinct reflected outputs and contributes one. \(\square\)

---

## 5. Exact Cost-Memory Duality Theorem

### Theorem 5.1

For every orbitwise canonical terminal profile \(\epsilon\) and every finite window \(W_N\),

\[
\boxed{
C_N(\epsilon)=M_N(\epsilon).
}
\tag{5.1}
\]

### Proof

Immediate from Propositions 3.2 and 4.3. \(\square\)

### Interpretation

Every extra reflected terminal element buys exactly one additional unit of branch-sensitive terminal memory.

There is neither a cheaper way to preserve one orbit nor a memory benefit without paying the corresponding new-output cost inside the canonical orbitwise lift class.

---

## 6. Extremal selectors

### Theorem 6.1 — Minimal-Cost Selector

For every \(N\ge1\), the unique profile minimizing \(C_N\) is global `share`:

\[
\boxed{
C_N(ZM0\text{-share})=0.
}
\tag{6.1}
\]

Every non-share profile has positive cost.

### Proof

By (3.1), \(C_N\) is the sum of nonnegative binary profile bits. Its unique minimum zero occurs when every visible bit is zero. Requiring this for all \(N\) gives the global all-zero profile. \(\square\)

### Theorem 6.2 — Maximal-Memory Selector

For every \(N\ge1\), the unique profile maximizing \(M_N\) is global `split`:

\[
\boxed{
M_N(ZM0\text{-split})=Q_N.
}
\tag{6.2}
\]

### Proof

By (4.1), the maximum equals the number of visible orbits and is attained only when every visible profile bit equals one. Requiring this for all windows gives the global all-one profile. \(\square\)

Thus two intrinsic-looking optimization principles select opposite canonical lifts.

---

## 7. Global cardinality does not distinguish the endpoints

A warning is essential.

On the full infinite terminal universe, both global `share` and global `split` have countably many terminal elements:

\[
|E_{share}|=|E_{split}|=\aleph_0.
\tag{7.1}
\]

Therefore **plain infinite cardinality is not a selector**.

The correct invariant is finite-window extension cost or an equivalent orbitwise cost density.

This prevents the false argument

\[
\text{“share is smaller because }\aleph_0<2\aleph_0\text{.”}
\]

Since

\[
2\aleph_0=\aleph_0,
\]

that argument is invalid.

---

## 8. Asymptotic cost and memory densities

For \(N\ge2\),

\[
Q_N=3N-2.
\]

Define normalized densities

\[
c(\epsilon)
=
\limsup_{N\to\infty}
\frac{C_N(\epsilon)}{Q_N},
\tag{8.1}
\]

\[
m(\epsilon)
=
\limsup_{N\to\infty}
\frac{M_N(\epsilon)}{Q_N}.
\tag{8.2}
\]

### Corollary 8.1

For every profile,

\[
\boxed{c(\epsilon)=m(\epsilon).}
\tag{8.3}
\]

For the two global endpoints:

\[
\boxed{
(c,m)_{share}=(0,0),
}
\tag{8.4}
\]

\[
\boxed{
(c,m)_{split}=(1,1).
}
\tag{8.5}
\]

---

## 9. Weighted channel version

Different terminal channel families may later be assigned different structural costs or memory values.

Let

\[
w_+,w_*,w_\times>0
\]

be positive channel weights.

Define

\[
C_N^w(\epsilon)
=
\sum_{q=(\alpha,n)\in\mathcal I_N}
 w_\alpha\epsilon(q),
\tag{9.1}
\]

and define weighted branch memory by the same orbit weights:

\[
M_N^w(\epsilon)
=
\sum_{q=(\alpha,n)\in\mathcal I_N}
 w_\alpha\epsilon(q).
\tag{9.2}
\]

Then trivially but exactly:

### Theorem 9.1

\[
\boxed{C_N^w(\epsilon)=M_N^w(\epsilon).}
\tag{9.3}
\]

Thus the one-for-one tradeoff is stable under any positive channel weighting provided cost and retained memory use the same orbit weight.

---

## 10. Selector Conflict Theorem

### Theorem 10.1

Within the canonical signed-M0 lift class, the following two optimization principles are incompatible except in the degenerate zero-orbit case:

1. minimize mirror extension cost;
2. maximize branch-sensitive terminal memory.

For every nontrivial window, the first uniquely selects `share`, while the second uniquely selects `split`.

### Proof

Theorem 5.1 identifies cost and memory numerically. Minimizing the common count requires all bits zero; maximizing it requires all bits one. For \(Q_N>0\), these profiles are distinct. \(\square\)

### Consequence 10.2 — no optimization-free canonical lift

The current structure does not supply a canonical choice between `share` and `split` merely from the existence of two natural extremal principles, because the principles optimize opposite objectives.

A unique choice requires specifying which structural resource is primary or introducing an additional invariant that breaks the tie for a mathematically motivated reason.

---

## 11. Pareto interpretation

If the objectives are written in conventional optimization direction as

\[
\text{minimize }C_N,
\qquad
\text{maximize }M_N,
\]

then by \(C_N=M_N\), improving one objective necessarily worsens the other.

Every profile with a distinct value of

\[
k=C_N=M_N
\]

represents a distinct point on the exact cost-memory tradeoff line.

At the aggregate level, the attainable pairs are

\[
\boxed{
(k,k),
\qquad
0\le k\le Q_N.
}
\tag{11.1}
\]

Thus there is no hidden nonlinear efficiency gain in the canonical orbitwise lift class.

---

## 12. Relation to reconstruction cost

The published Shadow-Reconstruction paper left terminal branch information outside the base shadow.

The present theorem quantifies exactly how much additional terminal structure is needed to restore it on finite windows:

\[
\boxed{
\text{one new reflected output}
\longleftrightarrow
\text{one recovered branch-distinguishable terminal orbit}.
}
\tag{12.1}
\]

This turns terminal reconstruction from a qualitative missing-information statement into a quantitative law.

---

## 13. Dimensional firewall

No new coordinate, plane, or independently iterable direction is introduced.

The finite-window depth \(N\) is measured along the already published signed line. Terminal outputs remain terminal.

Hence

\[
\boxed{c_{coord}=0.}
\]

throughout.

---

## 14. Prior-art boundary

The identity between two deliberately matched counting functions is elementary. Pareto tradeoffs and finite-extension costs are standard mathematical ideas.

No novelty is claimed for those abstract notions.

The FCOA-specific content is the exact identification, for the audited signed-M0 terminal lift class, of:

- the mirror-extension cost;
- the branch-sensitive memory restored by split fibers;
- the exact equality of those quantities at every finite window;
- the resulting opposite canonical selectors `share` and `split`.

---

## 15. Publication implication

Together with:

- continuum terminal-profile classification;
- terminal-opacity / uniformity independence;
- finite equality-coupling classification;

this theorem closes a coherent post-publication layer:

\[
\boxed{
\text{terminal ambiguity}
\to
\text{regularity classes}
\to
\text{finite coupling cost}
\to
\text{exact output-cost / branch-memory duality}.
}
\]

Before promoting it to a new article, perform a hostile audit and a focused prior-art check on reconstruction/extension cost and memory-preserving covers.

---

## 16. Next strike

The remaining one-dimensional question is:

\[
\boxed{
\text{Is there a third intrinsic invariant that selects one endpoint without simply restating cost or branch memory?}
}
\]

The strongest candidates are:

1. automorphism rigidity;
2. faithfulness of terminal reflection action;
3. minimality of the terminal involutive extension in a categorical sense;
4. recoverability of branch sign from the full typed operation graph.

The next hostile strike should test these candidates against both `share` and `split` before any publication claim.