# HATTER-SOL-11 · Quotient response injectivity in the Delta = -1155 laboratory

Status: closed exact laboratory theorem.

This note continues T11.17. The pair-flip theorem gives an unavoidable ordinary-response collision among exact residue sectors. The next question is whether, after quotienting that symmetry, the ordinary HATTER network creates any further collisions.

For the first two-dimensional laboratory

\[
K=\mathbb Q(\sqrt{-1155}),
\qquad n=17\cdot19=323,
\]

the answer is **no**: the four pair-flip quotient classes have four distinct ordinary Pareto responses.

---

## 1. The nine exact sectors

Retain the independent binary-tail types from T11.15:

\[
A_+=(17,\omega-1),\qquad A_-=(17,\omega),
\]

\[
B_+=(19,\omega-9),\qquad B_-=(19,\omega+8),
\]

where

\[
\omega=\frac{1+\sqrt{-1155}}2.
\]

There are two `A` factor nodes and two `B` factor nodes. Let

\[
j_A,j_B\in\{0,1,2\}
\]

count the number of plus-companion choices. By T11.15 the nine count vectors give nine distinct exact residue sectors.

Pair-flip conjugation acts by

\[
(j_A,j_B)\longmapsto(2-j_A,j_B),
\]

and

\[
(j_A,j_B)\longmapsto(j_A,2-j_B).
\]

Thus each coordinate has two quotient statuses:

- `E` (extreme): `j=0` or `j=2`;
- `M` (middle): `j=1`.

The nine sectors therefore collapse under pair-flip equivalence to four classes

\[
EE,\qquad EM,\qquad ME,\qquad MM.
\]

---

## 2. Local witness states

For the `A` pair the four node/companion products are

\[
A_+A_+=(\omega-1),\qquad A_+A_-=(17),
\]

\[
A_-A_+=(17),\qquad A_-A_-=(\omega).
\]

Their typed states are

\[
\Pi(\omega-1)=\Pi(\omega)=(1,0),
\]

\[
\Pi(17)=(17,0).
\]

Hence:

- in an extreme `A` sector the typed multiset is
  \[
  \boxed{A_E=\{(1,0),(17,0)\};}
  \]
- in the middle `A` sector the two witness configurations have typed multisets
  \[
  \boxed{A_M^- =\{(1,0),(1,0)\},}
  \]
  and
  \[
  \boxed{A_M^+ =\{(17,0),(17,0)\}.}
  \]

For the `B` pair,

\[
B_+B_+=(\omega-9),\qquad B_+B_-=(19),
\]

\[
B_-B_+=(19),\qquad B_-B_-=(\omega+8),
\]

with

\[
\Pi(\omega-9)=\Pi(\omega+8)=(8,1),
\]

\[
\Pi(19)=(19,0).
\]

Hence:

- in an extreme `B` sector
  \[
  \boxed{B_E=\{(8,1),(19,0)\};}
  \]
- in the middle `B` sector the two witness configurations are
  \[
  \boxed{B_M^- =\{(8,1),(8,1)\},}
  \]
  and
  \[
  \boxed{B_M^+ =\{(19,0),(19,0)\}.}
  \]

The sector-conditioned ordinary response is the union over all witness configurations in the fixed residue sector, followed by Pareto minimization, exactly as in HATTER-SOL-10.

---

## 3. Class EE

This is T11.17. Every configuration has typed multiset

\[
\{(1,0),(17,0),(8,1),(19,0)\}.
\]

The total capacities are

\[
P_{\rm tot}=45,\qquad Q_{\rm tot}=1.
\]

Only one vertex has positive `Q`, so no `Q` edge is possible and

\[
B_Q=1.
\]

The unique `P=1` vertex can have `P`-degree at most one, while the three remaining vertices can form a triangle. Thus at most four `P` edges are possible, and triangle plus pendant edge attains four. Hence

\[
\boxed{\mathcal F_{EE}=\{(37,1)\}.}
\]

---

## 4. Class EM

Use the lower middle-`B` configuration

\[
A_E\cup B_M^-
=\{(1,0),(17,0),(8,1),(8,1)\}.
\]

Here

\[
P_{\rm tot}=34,\qquad Q_{\rm tot}=2.
\]

### No Q edge

With no `Q` edge, the two `B` vertices and the `P=17` vertex can form a `P` triangle and the `P=1` vertex can attach by one pendant `P` edge. Thus

\[
|E_P|=4,
\]

and

\[
\boxed{(B_P,B_Q)=(26,2).}
\]

### One Q edge

The only possible `Q` edge is the edge between the two `(8,1)` vertices. Once that pair is occupied by `Q`, among the three high-`P` vertices only the two edges from the `P=17` vertex to the two `P=8` vertices remain available for `P`. The `P=1` vertex can add at most one further `P` edge. Hence

\[
|E_P|\le3.
\]

The bound is attained with the `Q` edge joining the two `B` vertices and three suitable `P` edges, so

\[
\boxed{(B_P,B_Q)=(28,0).}
\]

These two points are incomparable and exhaust the Pareto frontier.

The alternative middle-`B` configuration

\[
A_E\cup B_M^+
=\{(1,0),(17,0),(19,0),(19,0)\}
\]

has no `Q` capacity and total `P` capacity `56`. The same `P=1` bottleneck allows at most four edges, giving best boundary `(48,0)`, which is dominated by `(28,0)`.

Therefore

\[
\boxed{\mathcal F_{EM}=\{(26,2),(28,0)\}.}
\]

---

## 5. Class ME

Use the lower middle-`A` configuration

\[
A_M^-\cup B_E
=\{(1,0),(1,0),(8,1),(19,0)\}.
\]

Then

\[
P_{\rm tot}=29,\qquad Q_{\rm tot}=1.
\]

Again only one vertex has positive `Q`, so

\[
B_Q=1.
\]

For the `P` layer, the two capacity-one vertices contribute total degree at most two. The two high-capacity vertices can use their mutual edge. Thus

\[
|E_P|\le3.
\]

A connected `P` tree consisting of the high-high edge and one pendant edge from each capacity-one vertex attains three edges. Hence

\[
\boxed{(B_P,B_Q)=(23,1).}
\]

The alternative middle-`A` configuration

\[
A_M^+\cup B_E
=\{(17,0),(17,0),(8,1),(19,0)\}
\]

has total `P` capacity `61`. Even the complete graph has only six `P` edges, so its best possible `P` boundary is `49`; with `Q` still equal to `1`, this is dominated by `(23,1)`.

Therefore

\[
\boxed{\mathcal F_{ME}=\{(23,1)\}.}
\]

---

## 6. Class MM

The lower-lower witness configuration is

\[
A_M^-\cup B_M^-
=\{(1,0),(1,0),(8,1),(8,1)\}.
\]

Thus

\[
P_{\rm tot}=18,\qquad Q_{\rm tot}=2.
\]

### No Q edge

The two `P=1` vertices have total `P` degree at most two, and the two `P=8` vertices can use their mutual edge. Hence at most three `P` edges are possible. A connected `P` tree attains three, giving

\[
\boxed{(B_P,B_Q)=(12,2).}
\]

### One Q edge

The only `Q` edge joins the two `(8,1)` vertices. For connected support, neither capacity-one vertex can spend its sole `P` port on the other capacity-one vertex: if they were joined to each other, the two pairs would form disconnected components. Therefore each capacity-one vertex must attach by a `P` edge to a high vertex. Exactly two `P` edges are then possible and sufficient for connectedness together with the `Q` edge. Hence

\[
\boxed{(B_P,B_Q)=(14,0).}
\]

The other three witness configurations in the same middle-middle residue sector are:

\[
A_M^-\cup B_M^+,
\qquad
A_M^+\cup B_M^-,
\qquad
A_M^+\cup B_M^+.
\]

Their best attainable boundaries are respectively no better than

\[
(34,0),
\qquad
(38,2)\text{ or }(40,0),
\qquad
(60,0),
\]

all dominated by one of the two lower-lower points above.

Therefore

\[
\boxed{\mathcal F_{MM}=\{(12,2),(14,0)\}.}
\]

---

## 7. Exact nine-sector table

The sector-conditioned ordinary Pareto responses are therefore

| `j_A` | `j_B` | pair-flip class | ordinary Pareto response |
|---:|---:|:---:|:---|
| 0 | 0 | EE | `{(37,1)}` |
| 0 | 1 | EM | `{(26,2),(28,0)}` |
| 0 | 2 | EE | `{(37,1)}` |
| 1 | 0 | ME | `{(23,1)}` |
| 1 | 1 | MM | `{(12,2),(14,0)}` |
| 1 | 2 | ME | `{(23,1)}` |
| 2 | 0 | EE | `{(37,1)}` |
| 2 | 1 | EM | `{(26,2),(28,0)}` |
| 2 | 2 | EE | `{(37,1)}` |

Thus the nine exact residue sectors have exactly four ordinary response values, precisely matching the four pair-flip quotient classes.

---

## 8. Theorem T11.18 — quotient response injectivity in the first 2D laboratory

Let

\[
\mathscr R_{323}
\]

be the nine exact principalization-residue sectors of the `Delta=-1155`, `n=323` binary-tail system, and let `~pf` denote pair-flip equivalence generated by independent conjugate-pair flips.

Then the ordinary HATTER Pareto-response map factors as

\[
\mathscr R_{323}
\longrightarrow
\mathscr R_{323}/\!\sim_{pf}
\longrightarrow
\{\text{ordinary Pareto responses}\},
\]

where

\[
\boxed{|\mathscr R_{323}|=9,\qquad
|\mathscr R_{323}/\!\sim_{pf}|=4,}
\]

and the second map is injective.

Equivalently,

\[
\boxed{
R\text{ and }R'\text{ have the same ordinary response}
\iff
R\sim_{pf}R'
}
\]

for this laboratory.

### Proof

T11.17 proves constancy on every pair-flip class. Sections 3--6 compute the four quotient-class responses explicitly:

\[
\mathcal F_{EE}=\{(37,1)\},
\]

\[
\mathcal F_{EM}=\{(26,2),(28,0)\},
\]

\[
\mathcal F_{ME}=\{(23,1)\},
\]

\[
\mathcal F_{MM}=\{(12,2),(14,0)\}.
\]

They are pairwise distinct. Therefore no two inequivalent pair-flip classes collide. QED.

---

## 9. Interpretation

The first two-dimensional binary-tail laboratory separates two kinds of information loss cleanly:

1. **arithmetic conjugation blindness:** exact residues related by pair flips are invisible to the ordinary network;
2. **network optimization blindness beyond pair flips:** absent in this laboratory.

Thus the `4 -> 1` corner collapse of T11.17 is real, but it is completely explained here by the conjugate-pair symmetry. The network does not create an additional quotient on the remaining four classes.

This is a useful negative result: it prevents us from overclaiming T11.17 as evidence of a mysterious dynamical collapse.

---

## 10. Next target

The next search should leave this minimal laboratory.

A genuine post-quotient collision can first arise only when there is enough combinatorial freedom that two inequivalent composition profiles generate the same optimized Pareto frontier. Natural attack directions are:

1. increase multiplicities `m_t` beyond two, so one tail type has several non-extreme count levels;
2. use three or more independent binary-tail types;
3. combine binary and deterministic tail classes whose typed states can compensate each other under network optimization;
4. search for equal Pareto fronts under distinct quotient composition vectors before attempting a general theorem.

The publication-safe question is now precise:

\[
\boxed{
\text{Is the quotient response map injective for all rational binary-tail systems, or does a first genuine network-induced collision exist?}
}

This is the next HATTER-SOL-11 proof obligation.
