# HATTER-SOL-19
# Boolean Geometry of Mathematical Presentations
## Temporal-Spatial Duality, Circuit Images, and the Cost of Adaptivity

**Branch:** \`research/hatter-sol-19-boolean-geometry\`  
**Parent:** HATTER-SOL-18 · Adaptive Word Tomography  
**Status:** OPEN / FOUNDATIONAL LAYER  
**Author:** Alex Malachevsky  
**AI research collaborator:** Commander Sol · Hatter Sol  
**Opened:** 20 September 2026

## Central question

H18 established that a finite mathematical model can be realized exactly by a
Boolean circuit after finite encoding, and produced the first controlled
hardware data showing that two different mathematical presentations and two
different execution disciplines have different physical images.

H19 asks the next question:

\[
\boxed{
\text{Which structural properties of a mathematical presentation survive}
\atop
\text{Booleanization, spatialization, synthesis, and physical mapping?}
}
\]

The programme separates four objects:

\[
M
\longrightarrow
B_\Pi(M)
\longrightarrow
S_\Theta(B_\Pi(M))
\longrightarrow
P_\Theta(M),
\]

where

- \(M\) is the mathematical presentation;
- \(B_\Pi\) is a declared presentation-aware Booleanization discipline;
- \(S_\Theta\) is synthesis / technology mapping / place-and-route;
- \(P_\Theta\) is the measured physical profile.

## First programme objective

The first H19 target is not another FPGA percentage.  It is an exact formal
model of the **temporal-spatial transformation of an adaptive decision DAG**.

For one fixed H18 restricted-12 certificate we will construct a family of
E0-equivalent implementations:

\[
M_{\rm direct},
\quad
M_{\rm prefix},
\quad
M_{\rm Nielsen},
\quad
M_{\rm flat},
\]

all implementing the same encoded finite task while preserving different
factorizations.

This gives a controlled experiment in which semantics, fault interface, device,
tool, and I/O timing convention are fixed while mathematical presentation is
varied.

## Parallel H18 closure

The exact value

\[
M_1(W_4)\in\{9,10,11,12\}
\]

remains a finite H18 closure problem.  It is being pursued independently on
\`research/hatter-sol-18-m1-closure\` and does not modify the frozen H18 paper.
