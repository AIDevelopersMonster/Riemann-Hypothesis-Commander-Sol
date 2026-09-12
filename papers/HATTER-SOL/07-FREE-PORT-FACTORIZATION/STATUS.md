# HATTER-SOL-07 — continuity / handoff status

**Branch:** `research/hatter-sol-free-ports`  
**Path:** `papers/HATTER-SOL/07-FREE-PORT-FACTORIZATION/`  
**Status date:** 2026-09-12  
**Status:** active exploratory research; publication threshold not reached.

## Core picture

Treat a factor `m` as a capacity-`m` node. In the chain picture, two ports are reserved for through-flow, leaving `m-2` free external ports.

For an ordered factorization `n=a_1...a_k`, define

\[
F(a_1,...,a_k)=\sum_i(a_i-2).
\]

Proper refinement `ab -> a,b` strictly decreases `F` by

\[
(a-1)(b-1)+1.
\]

Complete prime factorization therefore minimizes `F` among multiplicative refinements.

## General graph formulation

For a connected factor network `G=(V,E)` with capacities `a_v`, the free boundary is

\[
B(G,\mathbf a)=\sum_v a_v-2|E|.
\]

For a tree,

\[
B(T,\mathbf a)=\sum_v(a_v-2)+2.
\]

Hence the original chain formula is exactly tree free boundary after two global terminals are designated as input/output.

## Important caution

Do not claim novelty for `sum(p-2)`, `sopfr(n)-2 Omega(n)`, the handshake identity, or basic tree degree facts. The programme is only interesting if the factorization/refinement + capacity-constrained topology combination yields a genuinely structural theorem.

## Immediate next strike

Study the **boundary spectrum**

\[
\mathcal B(n)=\{B(G,\mathbf a): \prod a_i=n,\ G\text{ connected and }\deg_G(v_i)\le a_i\}.
\]

First targets:

1. characterize the maximum and minimum possible boundary;
2. determine whether `\mathcal B(n)` is always an interval of integers of fixed parity or has arithmetic gaps;
3. repeat for trees only;
4. determine the effect of full prime resolution;
5. characterize the role of many factors `2` as forced degree-<=2 vertices.

## Narrative direction

Use the Wonderland/«Размышлизмы» layer first: Alice discovers that equal products need not represent equal architectures if factor nodes are allowed to keep unused external links. Then separate a visibly rigorous section containing definitions, lemmas, counterexamples, and publication claims.

## Publication gate

Not reached. Do not assemble Zenodo manuscript yet. A clean research seed / illustrated note may be produced later, but only a nontrivial realizability/extremal/rigidity theorem should trigger the standalone mathematical publication threshold.
