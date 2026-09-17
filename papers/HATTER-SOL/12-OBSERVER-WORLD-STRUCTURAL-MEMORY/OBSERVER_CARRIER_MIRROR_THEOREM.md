# HATTER-SOL-12 · OBSERVER–CARRIER MIRROR THEOREM

**Status:** exact theorem layer inherited from the HATTER-SOL-11 interior orbital fiber and regular-factorizable-host response theorem.

## 1. Fixed interior fiber

Fix integers

\[
P>Q>0,
\qquad S=P+Q.
\]

The generic odd folded interior fiber contains three orbital states whose orbit-total images are

\[
x_I=(P,Q),
\qquad
x_{II}=(Q,P),
\qquad
x_{III}=(0,S).
\]

Let

\[
F_{P,Q}:=\{x_I,x_{II},x_{III}\}.
\]

The point of this note is to compare two different operations on the same three-state set:

1. increasing observer resolution;
2. increasing carrier capacity.

They act in opposite directions on distinguishability.

---

## 2. Three nested observers

Define

\[
O_0(A,O):=A+O,
\]

\[
O_1(A,O):=\bigl(A+O,\mathbf 1_{\{AO=0\}}\bigr),
\]

and

\[
O_2(A,O):=(A,O).
\]

Thus `O_0` sees only total capacity, `O_1` additionally sees whether the state is pure or mixed, and `O_2` sees the ordered orbit-total pair.

The observers are nested:

\[
O_2\succeq O_1\succeq O_0.
\]

### Theorem OC12.1 — exact observer-resolution ladder

On `F_{P,Q}`,

\[
\boxed{
|O_0(F_{P,Q})|=1,
\qquad
|O_1(F_{P,Q})|=2,
\qquad
|O_2(F_{P,Q})|=3.
}
\]

Equivalently,

\[
\boxed{1\longrightarrow2\longrightarrow3.}
\]

### Proof

All three states have total capacity `S`, so `O_0` identifies all of them.

The states `x_I=(P,Q)` and `x_{II}=(Q,P)` are mixed because both coordinates are positive, whereas `x_{III}=(0,S)` is pure. Hence `O_1` has exactly two values.

Finally, because `P>Q>0`, the three ordered pairs `(P,Q)`, `(Q,P)` and `(0,S)` are pairwise distinct. Hence `O_2` has three values. QED.

This is an exact finite example of the general observer-coarsening law from `RESEARCH_KERNEL.md`: richer observation splits fibers.

---

## 3. Regular factorizable carrier response

Now let `H` be a connected simple graph of even order `n`, `d`-regular and 1-factorizable. Assume

\[
d\le S.
\]

For a uniform typed capacity state `(A,O)`, the HATTER-SOL-11 theorem gives the exact Pareto front

\[
\mathcal R_H^\Xi(A,O)
=
\{(B_A,B_O):
B_A+B_O=D,
L_A\le B_A\le D-L_O,
B_A\equiv0\pmod2\},
\]

where

\[
D=n(A+O-d),
\qquad
L_A=n(A-d)_+,
\qquad
L_O=n(O-d)_+.
\]

Let

\[
R_{H,d}(A,O):=\mathcal R_H^\Xi(A,O).
\]

We ask how many of the three states in `F_{P,Q}` remain distinguishable after passing through the carrier response.

### Theorem OC12.2 — exact carrier-collapse ladder

For the three-state interior fiber,

\[
\boxed{
|R_{H,d}(F_{P,Q})|
=
\begin{cases}
3,&d<P,\\
2,&P\le d<S,\\
1,&d=S.
\end{cases}
}
\]

Thus, as carrier degree crosses the two intrinsic thresholds,

\[
\boxed{3\xrightarrow{d=P}2\xrightarrow{d=S}1.}
\]

### Proof

Because every state in the fiber has total capacity `S`, all three have the same total residual boundary

\[
D=n(S-d).
\]

**Case 1: `d<P`.**

For `x_I=(P,Q)`,

\[
L_A^I=n(P-d)>0.
\]

For `x_{II}=(Q,P)`,

\[
L_O^{II}=n(P-d)>0.
\]

The pure state `x_{III}=(0,S)` has

\[
L_O^{III}=n(S-d)=D,
\]

so its response is the singleton

\[
\{(0,D)\}.
\]

If `Q\le d`, the response of `x_I` has positive minimum `B_A=n(P-d)`, while `x_{II}` contains `B_A=0`; hence they differ. If `Q>d`, their lower endpoints are respectively `n(P-d)` and `n(Q-d)`, which differ because `P>Q`. Thus the two mixed responses are distinct, and neither equals the pure singleton. Therefore all three survive.

**Case 2: `P\le d<S`.**

Both coordinates of `x_I` and `x_{II}` are at most `d`, so

\[
L_A=L_O=0
\]

for both states. Since their total `D` is the same, their Pareto fronts coincide.

For `x_{III}=(0,S)`, however,

\[
L_O=D,
\]

so the response is again the singleton `\{(0,D)\}`. Because `D>0`, this is different from the mixed front. Hence exactly two response classes remain.

**Case 3: `d=S`.**

Then `D=0`, so every feasible response is

\[
\{(0,0)\}.
\]

All three states collide. QED.

---

## 4. Mirror law

Combining OC12.1 and OC12.2 gives two exact filtrations on the same parent three-state fiber:

\[
\boxed{
\text{observer refinement:}\quad1\to2\to3,
}
\]

\[
\boxed{
\text{carrier enrichment:}\quad3\to2\to1.
}
\]

This is called a **mirror law** only in the finite distinguishability sense. No categorical duality is claimed.

The mathematical content is that two distinct mechanisms act oppositely:

- richer observers refine observational equivalence classes;
- sufficiently rich carriers can make different typed states produce the same optimal response.

Thus structural memory is controlled by both the observation map and the realization environment.

---

## 5. Memory counts

Let

\[
D_O(F):=|O(F)|
\]

be the number of states distinguished by an observer and

\[
D_R(F):=|R(F)|
\]

be the number distinguished by a carrier response.

For the present fiber,

\[
D_{O_0}=1,
\qquad D_{O_1}=2,
\qquad D_{O_2}=3,
\]

whereas

\[
D_{R_d}=3,2,1
\]

in the degree regimes `d<P`, `P<=d<S`, `d=S`.

A normalized distinguishability index may therefore be defined by

\[
\delta:=\frac{D-1}{|F|-1},
\]

which here takes the exact values

\[
0,\frac12,1.
\]

This index is only a finite laboratory statistic; it is not an information-theoretic entropy.

---

## 6. Significance for HATTER-SOL-12

The parent HATTER-SOL-11 theorem `3->2->1` is therefore not merely a geometry curiosity. Together with the observer ladder it gives the first exact example of a two-sided structural-memory calculus:

\[
\boxed{
\text{state generation}
\longrightarrow
\text{observer resolution}
\quad\text{versus}\quad
\text{carrier-induced response collapse}.
}
\]

This theorem should form part of the central theorem spine of HATTER-SOL-12.