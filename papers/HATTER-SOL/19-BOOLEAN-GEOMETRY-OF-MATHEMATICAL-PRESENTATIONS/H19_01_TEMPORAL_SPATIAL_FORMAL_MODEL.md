# H19-01 · Temporal-Spatial Formal Model

Status: **FOUNDATIONAL DRAFT**

## 1. Adaptive finite presentation

Let \(X\) be a finite input/state set, \(Y\) a finite output set, and

\[
Q=\{q_1,\ldots,q_m\},
\qquad
q_i:X\to\Sigma_i
\]

a finite family of observers.

An adaptive decision presentation is a rooted finite DAG

\[
G=(V,E,r)
\]

whose nonterminal node \(v\) has:

- an observer label \(\lambda(v)\in Q\);
- one outgoing edge for each response used at that node;
- a transition map
  \[
  \delta_v:\Sigma_{\lambda(v)}\to V;
  \]
- terminal nodes carrying outputs through
  \[
  \omega:V_{\rm term}\to Y.
  \]

The induced semantic function is

\[
\Phi_M:X\to Y.
\]

A fault model may enlarge the input to \(X\times F\).  H19's first controlled
family will keep the fault encoding fixed, so its members are E0-equivalent.

## 2. Residual programmes

For any reachable node \(v\), define the **residual programme**

\[
M_v
\]

to be the sub-DAG rooted at \(v\), together with the observer functions and
terminal output semantics inherited from \(M\).

Two histories that arrive at the same DAG node have the same residual
programme.  This is the exact source-level meaning of decision-DAG sharing.

Define the residual set

\[
\mathcal R(M)=\{M_v:v\in V\}.
\]

For successful-answer depth \(t\), define the reachable residual frontier

\[
\mathcal R_t(M)
=
\{M_v:v\text{ reachable after }t\text{ successful observations}\}.
\]

The sequence

\[
R_t(M)=|\mathcal R_t(M)|
\]

is a structural characteristic of the adaptive presentation.  It is not yet a
Boolean lower bound.

## 3. Temporal realization

A canonical temporal realization stores the current node/state ID, evaluates
only the observer selected by that node, receives its response, and updates the
node ID.

Its transaction time depends on:

- adaptive path length;
- observer execution latency;
- controller/state-update latency;
- fault schedule.

Thus adaptive query depth is naturally a **temporal** resource.

## 4. Full spatial realization

A canonical full spatial realization computes the supported observer values in
parallel and replaces every nonterminal decision node by a combinational
selector over the already-computed child results.

Mutually exclusive future branches therefore coexist in space.

This is the exact phenomenon exposed by the H18-LAB-04 waveform:

\[
\text{same input}
\to
\text{different branch selection}
\to
\text{same certified output},
\]

while the unselected branch still physically exists as combinational logic.

## 5. Canonical compiled-DAG discipline

Freeze a discipline \(\Pi_{\rm DAG}\):

1. each distinct observer \(q_i\) is instantiated once;
2. observer values may fan out to every DAG node labelled by \(q_i\);
3. every nonterminal node is realized by one selector over child result words;
4. identical DAG nodes are shared exactly as in the source DAG;
5. no algebraic rewrite may flatten the whole semantic function;
6. input and output encodings are fixed.

Let

- \(S(q_i)\), \(D(q_i)\) be size/depth of the frozen observer circuit;
- \(b\) be encoded terminal-result width;
- \(s_{\rm sel}(r,b)\), \(d_{\rm sel}(r,b)\) be the declared size/depth of an
  \(r\)-way \(b\)-bit selector.

For node \(v\), let \(r_v\) be its realized response fanout.

## 6. Proposition — exact construction accounting

Under \(\Pi_{\rm DAG}\), before downstream synthesis rewriting, the generated
spatial circuit has structural size

\[
\boxed{
S_{\rm gen}(M)
=
\sum_{q_i\in Q_{\rm used}}S(q_i)
+
\sum_{v\in V_{\rm nt}}s_{\rm sel}(r_v,b)
+
S_{\rm shell}.
}
\]

### Proof

By construction, each used observer is instantiated exactly once, each
nonterminal source node contributes exactly one declared selector, and the
registered/input-validity shell contributes \(S_{\rm shell}\).  These generated
instances are disjoint before synthesis rewriting.  Summing their declared
instance costs gives the identity. \(\square\)

This is a theorem about the **compiler discipline**, not about the minimum
Boolean circuit for \(\Phi_M\).

## 7. Proposition — path-depth upper bound

For every root-to-terminal DAG path \(p\),

\[
D_{\rm gen}(M)
\le
\max_i D(q_i)
+
\max_p\sum_{v\in p}d_{\rm sel}(r_v,b)
+
D_{\rm shell}.
\]

If the generated netlist contains no cross-level logic sharing that changes
these declared stage depths, the right side is exact for the longest realized
dependency path.

Again this is a construction-level statement, not an unrestricted lower bound.

## 8. Spatialization burden

The previous accounting suggests separating two source costs:

\[
S_{\rm obs}(M)=\sum_{q_i\in Q_{\rm used}}S(q_i),
\]

\[
S_{\rm future}(M)
=
\sum_{v\in V_{\rm nt}}s_{\rm sel}(r_v,b).
\]

The first is the cost of making the observation vocabulary simultaneously
available.

The second is the cost of materializing mutually exclusive adaptive futures.

This decomposition will be tested against H18 physical data.

## 9. What H18 already says

On Cyclone V, the same H18 restricted-12 mathematics gave:

\[
1455\ {\rm ALM}+26\ {\rm DSP}
\]

for temporal reuse and

\[
10627\ {\rm ALM}+48\ {\rm DSP}
\]

for full spatialization.

This does not prove a general lower bound.  It supplies the first measured
point motivating the decomposition above.

## 10. Next exact target

Build DIRECT12, PREFIX19, NIELSEN12 and FLAT realizations of one E0 task and
record, before synthesis:

- observer instance counts;
- permutation-composition counts;
- selector/node counts;
- source dependency depth;
- structural sharing.

Then compare those source invariants with post-synthesis and post-route profiles.

The immediate scientific question is:

\[
\boxed{
\text{Which source-level structural quantities predict the technology-relative
hardware image?}
}
\]
