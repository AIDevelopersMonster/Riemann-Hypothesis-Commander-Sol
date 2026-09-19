# HATTER-SOL-18 · H18-04
# Does the Higman lift trace improve adaptive tomography?

**Status:** CLOSED negative result.

H18-03 identified the hidden \(32+32\) split by the canonical commutator-lift trace

\[
\tau(A,B)=\operatorname{tr}([\widetilde A,\widetilde B])\in\mathbb F_7.
\]

A natural next question is whether giving the adaptive observer this additional query improves the exact H18-01 decision complexity.

We therefore augment the 50 class-valued \(W_4\) queries by one new four-valued query \(\tau\).

The exact dynamic-programming certificate gives:

\[
\boxed{D^\*_{\;W_4+\tau}=4}.
\]

Depth 3 is still impossible.

More strongly, the optimum total path length among depth-4 trees remains

\[
\boxed{382},
\]

so the optimum mean depth remains

\[
\boxed{\frac{191}{57}\approx3.350877}.
\]

A selected optimum still has:

- root \(AAB\);
- 48 internal nodes.

Thus the lift invariant is **structurally decisive for Nielsen dynamics** but **informationally redundant for the optimal \(W_4\) adaptive classifier**.

This is an important distinction:

\[
\boxed{
\text{good dynamical invariant}
\not\Rightarrow
\text{better adaptive query complexity}.
}
\]

Interpretation: the existing short-word class queries already contain enough indirect information to resolve the same four trace sectors without explicitly asking for \(\tau\).

The next useful direction is therefore not to add \(\tau\) as a free query, but to study one of:

1. a restricted cheap-query pool where \(\tau\) may become valuable;
2. hardware-weighted adaptive cost;
3. one-query erasure;
4. temporal/Nielsen histories inside each fixed \(\tau\)-component.

Certificate:

\`\`\`text
python certificates/h18_adaptive_with_tau_certificate.py
\`\`\`
