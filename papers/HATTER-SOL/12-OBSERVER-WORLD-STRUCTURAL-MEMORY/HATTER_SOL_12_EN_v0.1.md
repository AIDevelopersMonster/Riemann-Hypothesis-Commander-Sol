# HATTER-SOL-12
## Observer Laws, World Rotation, and Structural Memory of an Integer

**Version:** v0.1 theorem-spine draft, hostile-audit patched  
**Date:** 2026-09-14  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196

## Abstract

We study a finite structural-memory problem in which the same rational integer is examined across arithmetic worlds, carrier geometries, and observation maps. The basic object is a quadruple

\[
(n,W,C,O),
\]

where `n` is the integer, `W` an arithmetic world, `C` an admissible carrier class, and `O` an observer of the resulting structural state.

The general refinement laws for observation maps are standard partition theory and are used only as bookkeeping. The new content is a collection of exact HATTER laboratories inherited from the orbital-port and world-response framework. First, for a generic odd three-state orbital fiber

\[
(P,Q),\quad(Q,P),\quad(0,P+Q),\qquad P>Q>0,
\]

three nested observers distinguish respectively `1`, `2`, and `3` classes, while the exact response on even connected `d`-regular 1-factorizable carriers collapses the same three states according to

\[
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.
\]

Second, for the fixed probe `61^6`, the nine imaginary-quadratic class-number-one worlds split first into two scalar-response classes (split versus inert). Conditional on the four-world split sector, asymmetric weighted planar observations refine the resolution from one class at the symmetric direction to three classes with one generic sample and four classes with two samples; a single rich polynomial response also separates all four.

Third, for the four split worlds `Delta=-4,-3,-19,-163`, the same one-parameter weighted scalar observer has different exact resolving profiles on the planar class and on the full class `Tor_12` of connected simple twelve-vertex toroidal carriers:

\[
D_{Pl}(r)=
\begin{cases}
2,&0<r<1,\\
1,&r=1,\\
3,&r>1,
\end{cases}
\qquad
D_{Tor}(r)=
\begin{cases}
3,&0<r<1,\\
2,&r=1,\\
4,&r>1.
\end{cases}
\]

Hence

\[
\boxed{D_{Tor}(r)-D_{Pl}(r)=1\quad\text{for every }r>0.}
\]

The associated HATTER tomographic dimension drops from `2` on the planar carrier class to `1` on `Tor_12`. The results show that structural visibility is controlled jointly by arithmetic world, carrier, and observer, rather than by the integer alone.

---

## 1. Structural state and observation

For fixed integer `n`, arithmetic world `W`, and carrier `C`, let

\[
\mathsf S(n;W,C)
\]

be the admissible structural state set. An observer is a map

\[
O:\mathsf S(n;W,C)\to Y_O.
\]

For `s in \mathsf S`, define the observational fiber

\[
\mathcal F_O(s):=O^{-1}(O(s)).
\]

Two structural states may therefore be numerically associated with the same rational integer while remaining distinct before observation or becoming identified by a coarse observer.

We distinguish throughout:

1. numerical identity of the rational integer;
2. structural multiplicity across worlds or carriers;
3. observational indistinguishability;
4. independent information or payload capacity.

Only the first three are used in the present paper. No claim about arbitrary message capacity follows from the existence of multiple structural states.

### Proposition 1.1 — deterministic observer refinement

Let `O_1:S->Y_1` and `O_2:S->Y_2`. If

\[
O_2=f\circ O_1,
\]

then for every `s in S`,

\[
\mathcal F_{O_1}(s)\subseteq\mathcal F_{O_2}(s).
\]

This is the standard refinement relation induced by deterministic post-processing.

### Proposition 1.2 — joint observation

For

\[
O_1\vee O_2=(O_1,O_2),
\]

one has

\[
\mathcal F_{O_1\vee O_2}(s)
=
\mathcal F_{O_1}(s)\cap\mathcal F_{O_2}(s).
\]

These two propositions are background machinery, not novelty claims.

---

## 2. The three-state orbital fiber

The HATTER-SOL-11 generic odd orbital classification gives, for every strict interior folded state

\[
P>Q>0,
\]

three orbit-total states

\[
x_I=(P,Q),
\qquad
x_{II}=(Q,P),
\qquad
x_{III}=(0,P+Q).
\]

Let

\[
F_{P,Q}=\{x_I,x_{II},x_{III}\}.
\]

The three states arise from the exact fiber of the magnitude-sorting forgetful map in a generic odd imaginary-quadratic direction system.

Define three nested observers:

\[
O_0(A,O)=A+O,
\]

\[
O_1(A,O)=\bigl(A+O,\mathbf1_{\{AO=0\}}\bigr),
\]

and

\[
O_2(A,O)=(A,O).
\]

The first sees only total capacity, the second also distinguishes pure from mixed states, and the third retains the ordered orbit-total pair.

### Theorem 2.1 — exact observer ladder

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

Hence observer enrichment gives

\[
\boxed{1\longrightarrow2\longrightarrow3.}
\]

### Proof

All three states have total capacity `P+Q`, so `O_0` gives one class. The first two states are mixed while the third is pure, so `O_1` gives two classes. Since `P>Q>0`, the three ordered pairs are pairwise distinct, so `O_2` gives three classes. \(\square\)

---

## 3. Carrier-induced collapse on the same fiber

Let `H` be a connected simple graph of even order `n`, `d`-regular and 1-factorizable. For a uniform typed state `(A,O)` with `A+O>=d`, HATTER-SOL-11 proved the exact Pareto response

\[
\mathcal R_H^\Xi(A,O)=
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

Apply this response to the same fiber `F_{P,Q}`.

### Theorem 3.1 — exact carrier-collapse ladder

For `P>Q>0` and `d<=P+Q`, the three orbital states induce

\[
\boxed{
3\text{ distinct responses},&d<P,\\
2\text{ distinct responses},&P\le d<P+Q,\\
1\text{ response},&d=P+Q.
}
\]

Equivalently,

\[
\boxed{3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1.}
\]

### Proof

All three states have the same total capacity `S=P+Q`, hence the same total residual boundary `D=n(S-d)`.

If `d<P`, at least one lower endpoint in the mixed states is positive, and the two mixed response intervals differ because `P>Q`; the pure state has the singleton response concentrated at `B_A=0`. Thus all three are distinct.

If `P<=d<S`, both coordinates in the two mixed states are at most `d`, so their lower endpoint constraints vanish and their Pareto fronts coincide. The pure state remains the singleton at one endpoint and is distinct because `D>0`.

If `d=S`, then `D=0`, so every response is the singleton `{(0,0)}`. \(\square\)

### Corollary 3.2 — finite mirror law

The same three-state parent fiber supports two opposite exact laws:

\[
\boxed{
\text{observer refinement: }1\to2\to3,
}
\]

\[
\boxed{
\text{carrier response: }3\to2\to1.
}
\]

We call this a mirror law of finite distinguishability. No categorical duality is asserted.

---

## 4. Rotation through arithmetic worlds

HATTER-SOL-09 introduced prime-toggle world operators `T_q` satisfying

\[
T_q^2=I,
\qquad
T_pT_q=T_qT_p.
\]

Fix a finite prime set `Q`, a base world `R_0`, and assume that the chosen HATTER response `Z_R(n;X,Y)` is defined at **every** vertex of the generated prime-toggle cube

\[
\mathcal C_Q(R_0)=\{T_AR_0:A\subseteq Q\}.
\]

This domain condition is automatic for the abstract squareclass signal but is not automatic for the current element-factorization response if a toggle leaves the chosen UFD laboratory.

Write

\[
T_A=\prod_{q\in A}T_q
\]

for `A subseteq Q` and define

\[
F_n(A)=Z_{T_AR_0}(n;X,Y).
\]

For each `B subseteq Q`, define the mixed world digit

\[
D_B=
\left[\prod_{q\in B}(I-T_q)Z_n\right](R_0).
\]

These are standard Boolean-lattice finite differences applied to the HATTER world field.

### Proposition 4.1 — finite world-cube reconstruction

Under the full-cube response-domain assumption above, for every `A subseteq Q`,

\[
Z_{T_AR_0}(n)
=
\sum_{B\subseteq A}(-1)^{|B|}D_B,
\]

with the inverse relation supplied by the same Boolean-lattice Möbius calculus.

The algebraic transform itself is standard. The HATTER role of the transform is to provide exact coordinates for a polynomial-valued arithmetic-world response field on any admissible finite cube.

---

## 5. Observation horizons

A potentially large or infinite response field must be read through finite truncations. Let `H` be a finite set of retained response coordinates and define

\[
O_H=\pi_H\circ O_\infty.
\]

If

\[
H_1\subseteq H_2,
\]

then `O_{H_2}` refines `O_{H_1}` and therefore

\[
\mathcal F_{O_{H_2}}(s)
\subseteq
\mathcal F_{O_{H_1}}(s).
\]

Examples of HATTER observation horizons include:

- world-digit order `|B|<=r` on an admissible response cube;
- polynomial support cutoff `a+b<=L`;
- finite world radius inside an admissible response domain;
- finite orbit set;
- bounded carrier scale.

An infinite coordinate family does not by itself imply unbounded independent information. In particular, if a chosen world model depends only on the split/inert states of `s` rational prime divisors of `n`, then the number of coarse world states is bounded by `2^s`; with split/inert/ramified local states the corresponding coarse bound is `3^s`.

---

## 6. The `61^6` same-integer laboratory

Consider the nine imaginary-quadratic class-number-one UFD worlds. For the fixed rational integer

\[
N=61^6,
\]

four worlds are split:

\[
\Delta=-4,-3,-19,-163,
\]

with local folded states

\[
(6,5),\quad(5,4),\quad(7,1),\quad(4,1),
\]

while the five remaining worlds are inert with rational-axis state `(61,0)`.

### Stage A: the nine-world laboratory

The numerical observer

\[
O_{num}(W)=61^6
\]

assigns the same value to all nine worlds, hence gives one class.

For the scalar geometry gain

\[
g_W=\Lambda_{1D}(W)-\Lambda_{Pl}(W),
\]

HATTER-SOL-11 gives

\[
\boxed{g_W=38\text{ on split worlds},\qquad g_W=14\text{ on inert worlds}.}
\]

Thus on the fixed nine-world domain

\[
\boxed{1\longrightarrow2.}
\]

### Stage B: conditional resolution inside the split sector

Now restrict explicitly to

\[
\mathcal W_{split}=\{-4,-3,-19,-163\}.
\]

At the symmetric planar direction `r=1`, all four worlds have the same weighted gain and therefore form one class.

For every fixed `r>1`, the planar weighted responses are

\[
38r,
\qquad
12+26r,
\qquad
38,
\qquad
38,
\]

and therefore form three classes.

Choose

\[
0<r_-<1<r_+.
\]

The two-sample map

\[
W\mapsto\bigl(G_W(r_-),G_W(r_+)\bigr)
\]

is injective on the four split worlds. A single polynomial-valued typed response is also injective on this four-world laboratory.

Hence the split-sector resolving diagram is

\[
\boxed{1\longrightarrow3\longrightarrow4,}
\]

where the first arrow changes the observation direction and the second enriches the observation to two scalar samples (or one rich polynomial observation).

The two stages together should **not** be read as one refinement chain `1->2->3->4` on a fixed world domain. They form a nested-domain resolving diagram for the same rational integer.

---

## 7. Exact planar world-separation phase diagram

For the four split worlds, the normalized planar weighted responses are

\[
F_{-4}^{Pl}(r)=
\begin{cases}
38,&r\le1,\\
38r,&r\ge1,
\end{cases}
\]

\[
F_{-3}^{Pl}(r)=
\begin{cases}
38,&r\le1,\\
12+26r,&r\ge1,
\end{cases}
\]

\[
F_{-19}^{Pl}(r)=38,
\]

\[
F_{-163}^{Pl}(r)=
\begin{cases}
26+12r,&r\le1,\\
38,&r\ge1.
\end{cases}
\]

Define

\[
D_C(r)=\#\{F_R^C(r):R\in\{-4,-3,-19,-163\}\}.
\]

### Theorem 7.1 — planar resolving profile

\[
\boxed{
D_{Pl}(r)=
\begin{cases}
2,&0<r<1,\\
1,&r=1,\\
3,&r>1.
\end{cases}}
\]

The symmetric direction `r=1` is therefore a complete one-shot blind direction in the planar laboratory.

No one planar sample separates all four worlds, while two samples on opposite sides of `1` do. Hence the HATTER tomographic dimension of this planar laboratory is

\[
\boxed{\operatorname{tdim}_{Pl}=2.}
\]

---

## 8. Twelve-vertex toroidal carrier class

Let `Tor_12` be the class of connected simple twelve-vertex graphs embeddable in the torus. Every member satisfies

\[
|E|\le3\cdot12=36.
\]

As an extremal witness, let `T_12` have

\[
V=\mathbb Z_3\times\mathbb Z_4
\]

and join each vertex `x` to

\[
x\pm e_1,
\qquad
x\pm e_2,
\qquad
x\pm(e_1+e_2).
\]

This is a simple 6-regular 36-edge toroidal graph. Its three generator directions are pairwise edge-disjoint 2-factors, and the `e_2` factor contains a perfect matching of six edges.

For any twelve-vertex toroidal carrier and uniform typed state `(A,O)`, the channel bounds imply

\[
e_A\le6A,
\qquad e_O\le6O,
\qquad e_A+e_O\le36.
\]

For each of the four split states `(6,5),(5,4),(7,1),(4,1)`, the explicit host `T_12` attains the corresponding linear upper bound in every positive weight regime. Therefore the following are exact **geometry-class** signatures on `Tor_12`:

\[
F_{-4}^{Tor}(r)=
\begin{cases}
50,&r\le1,\\
12+38r,&r\ge1,
\end{cases}
\]

\[
F_{-3}^{Tor}(r)=
\begin{cases}
38+12r,&r\le1,\\
24+26r,&r\ge1,
\end{cases}
\]

\[
F_{-19}^{Tor}(r)=50,
\]

\[
F_{-163}^{Tor}(r)=
\begin{cases}
26+12r,&r\le1,\\
38,&r\ge1.
\end{cases}
\]

### Theorem 8.1 — toroidal resolving profile

\[
\boxed{
D_{Tor}(r)=
\begin{cases}
3,&0<r<1,\\
2,&r=1,\\
4,&r>1.
\end{cases}}
\]

### Proof

For `0<r<1`, the Gaussian and `Delta=-19` values coincide at `50`, while the Eisenstein and `Delta=-163` values are distinct and strictly smaller. Thus there are three classes.

At `r=1`, the values are `50,50,50,38`, hence two classes.

For `r>1`, the values are

\[
12+38r,
\qquad
24+26r,
\qquad
50,
\qquad
38.
\]

The first exceeds the second by `12(r-1)>0`, the second exceeds `50` for every `r>1`, and `50\ne38`. Therefore all four are pairwise distinct. \(\square\)

It follows that

\[
\boxed{\operatorname{tdim}_{Tor}=1.}
\]

---

## 9. Constant carrier resolution gain

The planar and toroidal profiles can now be compared pointwise.

### Theorem 9.1 — exact carrier resolution gain

For every positive weight ratio,

\[
\boxed{
D_{Tor}(r)-D_{Pl}(r)=1,
\qquad r>0.
}
\]

### Proof

For `0<r<1`, the counts are `3` and `2`; at `r=1`, they are `2` and `1`; for `r>1`, they are `4` and `3`. \(\square\)

Thus the twelve-vertex toroidal carrier class resolves exactly one additional arithmetic-world class at every observation direction in this finite laboratory.

This statement is stronger than the minimum-sample comparison

\[
\operatorname{tdim}_{Pl}=2,
\qquad
\operatorname{tdim}_{Tor}=1,
\]

because it compares the entire one-parameter resolving profile.

---

## 10. Interpretation

The results separate three mechanisms.

### World

Changing the arithmetic world changes the factor-interface state of the same rational integer.

### Observer

Changing the observer changes which structural distinctions remain visible. Standard refinement laws control this side abstractly.

### Carrier

Changing the carrier changes which typed structural states can be realized or optimized into the same response. The HATTER response theorems show that carrier enrichment can either collapse distinctions, as in the regular-factorizable `3->2->1` theorem, or reveal distinctions, as in the planar-to-toroidal `61^6` comparison.

Therefore there is no universal monotone slogan such as “richer geometry always stores more memory” or “richer geometry always erases memory.” The correct object is the joint dependence

\[
\boxed{(n,W,C,O).}
\]

Structural visibility is a property of this quadruple.

---

## 11. Scope limits

The present article does not claim:

- a new general theory of partition refinement;
- a new Möbius transform;
- a universal theory of observability;
- a general genus-memory law;
- unlimited information capacity from infinitely many worlds;
- a cryptographic construction or hardness result.

The exact claims are the HATTER arithmetic/network theorem packages stated above.

---

## 12. Outlook

The next mathematical targets are:

1. homology-resolved typed carrier states on the torus;
2. exact examples with the same ordinary boundary response but different homological memory;
3. extension of carrier-resolving profiles to higher-genus surfaces;
4. strict world-digit order hierarchies on natural admissible prime-toggle cubes;
5. a proof or obstruction for unbounded fixed-number structural diversity in richer arithmetic world families.

These are future directions and are not used in the present theorem spine.

---

## 13. Publication status

This file is an EN v0.1 theorem-spine draft patched after a hostile mathematical audit. The inherited `61^6` formulas, the regular-factorizable host theorem, the generic-odd fiber classification, and the prime-toggle operator relations have been checked directly against their source theorem layers. The toroidal witness formulas have additionally been lifted to the full twelve-vertex simple toroidal carrier class in `TORUS_GEOMETRY_CLASS_LIFT.md`.

Before publication-candidate status it still requires:

- full bibliography insertion and DOI verification;
- notation and theorem-number harmonization;
- final novelty wording audit against the bibliography;
- Russian counterpart after the English theorem spine stabilizes.
