# HATTER-SOL-07 · Free-Port Factorization

**Working Russian title:** «Алиса в Стране Свободных Нитей: множители как узлы и цена организации»  
**Working English title:** “Alice in the Land of Free Threads: Factors as Nodes and the Cost of Organization”

- Series: **HATTER-SOL · Arithmetic Tea Party**
- Human author: **Малачевский А.А. / Malachevsky, A.A.**
- ORCID: **0009-0008-6009-3196**
- AI research collaborator / persona: **Commander Sol · Hatter Sol**
- Branch: `research/hatter-sol-free-ports`
- Status: **exploratory research / Размышлизмы with a rigorous kernel**

## Seed idea

Do not collapse a factorization immediately to its numerical product. Interpret each factor `m` as a node with `m` available connection ports. In a through-chain, one port is used by the incoming connection and one by the outgoing connection, leaving

\[
f(m)=m-2
\]

free external ports.

Thus a factorization

\[
n=a_1a_2\cdots a_k
\]

is represented as an ordered chain of factor-nodes with free-port count

\[
F(a_1,\ldots,a_k)=\sum_{i=1}^k(a_i-2).
\]

Examples:

\[
12:\quad F(12)=10,
\]

\[
12=3\cdot4:\quad F(3,4)=1+2=3,
\]

\[
12=2\cdot6:\quad F(2,6)=0+4=4,
\]

\[
12=2\cdot2\cdot3:\quad F(2,2,3)=1.
\]

The same integer therefore supports distinct connection architectures depending on how much multiplicative structure is exposed.

## First rigorous kernel

If one node `ab` with `a,b>=2` is refined into two consecutive factor-nodes `a,b`, the free-port count changes by

\[
(ab-2)-[(a-2)+(b-2)]
=ab-a-b+2
=(a-1)(b-1)+1>0.
\]

Hence every nontrivial multiplicative refinement strictly decreases the free-port count.

Consequently, in the refinement poset of multiplicative decompositions of `n`:

- the undecomposed node `n` has maximal free-port count `n-2`;
- complete factorization into primes has minimal free-port count;
- for `n=p_1\cdots p_r` with prime factors counted with multiplicity,

\[
F_{\min}(n)=\sum_{j=1}^r(p_j-2)
=\operatorname{sopfr}(n)-2\Omega(n).
\]

This formula itself is not claimed as new. The research question is whether the **refinement architecture, boundary conditions, and rewiring possibilities of the free ports** produce structural invariants or extremal statements that are not merely renamings of classical additive functions.

## Claim discipline

This project deliberately begins in the Wonderland / «Размышлизмы» mode. Metaphor is allowed; mathematical claims are not.

In particular:

1. `m` as a node with `m` ports is a chosen model, not a canonical interpretation of multiplication.
2. `f(m)=m-2` depends on the through-chain boundary convention (one input and one output).
3. `F_min(n)` is immediately expressible through standard arithmetic functions and is not presented as a new invariant.
4. A genuinely new result would require a theorem about the space of factorizations / rewiring / topology / boundary response that does not collapse to a standard formula.
5. Prime numbers are not to be described as “geometrically rich” or “poor” without specifying the representation category.

## Immediate research directions

- Replace a linear chain by trees and general connected factor networks.
- Distinguish internal edges from free boundary ports and derive the general port-balance identity.
- Ask which network topologies are realizable for a fixed factor multiset.
- Optimize free boundary under different wiring rules.
- Study whether prime factorization is extremal only for chains or in broader topology classes.
- Compare ordered versus unordered factorizations.
- Determine whether refinement losses define a meaningful metric / energy on the factorization poset.
- Look for an arithmetic statement whose proof genuinely uses the network picture rather than merely restating `sopfr` or `Omega`.

See `RESEARCH_KERNEL.md` and `STATUS.md` for the current handoff state.
