# HATTER-SOL-11 · Hostile Audit of the Regular-Factorizable Host Theorem

**Status:** publication gate passed for the theorem as currently stated.  
**Audited source:** `REGULAR_FACTORIZABLE_HOST_ORBITAL_MEMORY_THEOREM.md`.

This note tries to break RFH.1--RFH.4 at the assumption boundaries. It introduces no stronger theorem.

---

## 1. Audit target

The main exact statement assumes a fixed host `H` that is

- connected;
- simple;
- of even order `n`;
- `d`-regular;
- 1-factorizable;

and a uniform two-channel state `(A,O)` satisfying

\[
S=A+O\ge d.
\]

It claims the exact connected Pareto front

\[
B_A+B_O=D:=n(S-d),
\]

\[
L_A:=n(A-d)_+\le B_A\le D-L_O,
\qquad
L_O:=n(O-d)_+,
\]

with even parity.

The main risks are:

1. a hidden connectivity failure in the channel construction;
2. a parity gap in the claimed full segment;
3. an empty endpoint interval in extreme capacities;
4. failure for a pure channel;
5. failure at the critical threshold `S=d`;
6. an invalid domination argument for feasible points above the minimum-total line;
7. accidental promotion from fixed-host to geometry-class exactness;
8. accidental extrapolation to `S<d`.

---

## 2. Degree-window lemma audit

RFH.1 writes

\[
e=\frac n2 q+r,
\qquad0\le r<\frac n2,
\]

and takes `q` full perfect matchings plus `r` edges of the next matching.

### Boundary `e=nl/2`

Then `q=l`, `r=0`; every degree is exactly `l`.

### Boundary `e=nu/2`

Then `q=u`, `r=0`; every degree is exactly `u`.

### Interior `r>0`

Every degree is `q` or `q+1`. Since

\[
\frac{nl}{2}<e<\frac{nu}{2},
\]

we have

\[
l\le q<q+1\le u.
\]

Thus there is no off-by-one error at either endpoint.

### Availability of the next factor

If `r>0`, then `q<u<=d`, so `q+1<=d` and the next 1-factor exists. If `q=d`, necessarily `r=0`.

**Audit result:** RFH.1 survives.

---

## 3. Endpoint interval nonemptiness

The claimed interval is nonempty iff

\[
L_A+L_O\le D.
\]

Divide by `n`. We need

\[
(A-d)_+ +(O-d)_+\le A+O-d.
\]

This follows casewise:

- if `A,O<=d`, the left side is zero and `S>=d` makes the right side nonnegative;
- if `A>d>=O`, the inequality becomes `A-d<=A+O-d`, i.e. `0<=O`;
- symmetrically if `O>d>=A`;
- if `A,O>d`, it becomes `A+O-2d<=A+O-d`, i.e. `d>=0`.

**Audit result:** no empty-front pathology.

---

## 4. Pure-channel edge cases

### Case `A=0`

Since `S=O>=d`,

\[
l=(d-O)_+=0,
\qquad
u=\min(A,d)=0.
\]

RFH.1 selects the empty axial subgraph. Every host edge is oblique. The union of typed channels is therefore the full connected host `H`.

The front is the singleton

\[
(0,n(O-d)).
\]

which is exactly the unused oblique capacity after using all `nd/2` host edges.

### Case `O=0`

Symmetric: the full host is axial and the front is

\[
(n(A-d),0).
\]

**Audit result:** pure channels are correctly included; no positivity assumption on both channels is needed for RFH.2.

---

## 5. Critical threshold `S=d`

At

\[
A+O=d,
\]

we have

\[
D=0.
\]

Because `A,O>=0` and sum to `d`, neither exceeds `d`, so

\[
L_A=L_O=0.
\]

The claimed front is therefore exactly

\[
\{(0,0)\}.
\]

The realization uses all edges of `H`, partitioned into `A` perfect matchings of one channel and `O` of the other. Their union is the full connected host, so connectedness is automatic.

This verifies the `1` stage of the `3 -> 2 -> 1` filtration at `d=P+Q`.

**Audit result:** critical closure is exact.

---

## 6. Parity audit

Every boundary coordinate has form

\[
B_A=nA-2e_A,
\qquad
B_O=nO-2e_O.
\]

Since `n` is even, both coordinates are even.

Likewise

\[
D=n(S-d),
\quad
L_A=n(A-d)_+,
\quad
L_O=n(O-d)_+
\]

are even.

RFH.1 changes `e_A` by one edge at a time, so `B_A` changes by exactly two. Hence every even point in the stated interval is realized and no odd point can be feasible.

**Audit result:** the step-two segment is exact.

---

## 7. Connectivity audit

The axial degree-window subgraph `F` constructed from selected 1-factors need not be connected. This is harmless in RFH.2 because the oblique subgraph is its edge complement inside `H` and **every host edge is used**.

Thus the underlying untyped union is

\[
F\cup(H\setminus F)=H,
\]

which is connected by hypothesis.

This is exactly why the same argument cannot automatically be used in the underfull regime `S<d`: there one may choose only `S` of the `d` factors, and their union need not be connected.

**Audit result:** main theorem connectedness is sound; underfull caveat is necessary.

---

## 8. Domination argument audit

Take an arbitrary feasible boundary pair `(B_A,B_O)` above the minimum-total line:

\[
B_A+B_O>D.
\]

We need a realized even `b` such that

\[
L_A\le b\le D-L_O,
\]

\[
b\le B_A,
\qquad
D-b\le B_O.
\]

Equivalently, choose an even integer in

\[
I=
\left[
\max(L_A,D-B_O),
\min(B_A,D-L_O)
\right].
\]

All four quantities defining the endpoints are even.

The lower endpoint does not exceed `B_A` because

\[
L_A\le B_A
\]

and

\[
D-B_O\le B_A
\]

follows from `B_A+B_O>=D`.

The lower endpoint does not exceed `D-L_O` because

\[
L_A\le D-L_O
\]

by Section 3, and

\[
D-B_O\le D-L_O
\]

because `B_O>=L_O`.

Hence `I` is nonempty. Since its endpoints are even, it contains an even integer. The corresponding point `(b,D-b)` is realized by RFH.1 and componentwise dominates the original feasible point.

Thus every Pareto-minimal point lies on the minimum-total line.

**Audit result:** domination step is valid.

---

## 9. Degree-filtration audit

For interior `P>Q>0`, set `S=P+Q` and assume `d<=S`.

Mixed lower axial endpoints are

\[
n(P-d)_+,
\qquad
n(Q-d)_+.
\]

They coincide iff `P<=d`:

- if `d<P`, the first is positive; the second is either smaller positive (`d<Q`) or zero (`Q<=d<P`);
- if `d>=P`, both vanish.

For `d<S`, the pure state is the singleton endpoint

\[
(0,n(S-d)).
\]

If `d<P`, Type I has positive minimum axial boundary. Type II cannot equal the pure singleton: if its minimum axial boundary is positive they differ immediately; if it is zero, its mixed segment has positive length because `Q>0` and `d<S`.

If `P<=d<S`, the common mixed response is a nontrivial step-two segment, whereas pure is one endpoint.

At `d=S`, all are `(0,0)`.

**Audit result:** exact `3 / 2 / 1` class count survives all threshold equalities.

---

## 10. Fixed-host versus geometry-class audit

RFH.2 bounds total used edges by `nd/2` because the network is a subgraph of the **fixed host** `H`.

This does not by itself bound another graph in the same broad geometry class by `nd/2`.

Therefore the theorem must be written as fixed-host universality unless an independent geometry-class extremality result is supplied.

Approved lifts already available:

- `K_n` in unrestricted simple-support geometry;
- tetrahedron, octahedron, icosahedron at their orders in planar geometry, since they attain the planar edge ceiling.

**Audit result:** the theorem statement correctly preserves this distinction.

---

## 11. Underfull hostile test

A false extrapolation would be

\[
S<d\implies\mathcal R_H(A,O)=\{(0,0)\}.
\]

The 1-factorization supplies `S` factors, but their union can be disconnected. Thus connectedness of the HATTER network is not automatic.

RFH.4 correctly states only a sufficient condition: if a selected union of `S` factors is connected and spanning, it can be partitioned into `A` and `O` channel factors and gives zero boundary.

**Audit result:** no underfull theorem should be strengthened without a separate connected-factor analysis.

---

## 12. Audit verdict

No counterexample was found to RFH.1--RFH.4 under their written hypotheses.

The publication-critical assumptions are all necessary to keep visible in the statement:

\[
\boxed{
\text{connected + simple + even order + regular + 1-factorizable + }S\ge d.
}
\]

The two most dangerous overclaims are explicitly excluded:

1. replacing fixed-host exactness by geometry-class exactness without extremality;
2. extending automatic closure into `S<d` without a connected spanning factor.

**Publication gate:** PASS for inclusion in the HATTER-SOL-11 manuscript, subject to final literature/novelty audit and manuscript-level notation/numbering normalization.
