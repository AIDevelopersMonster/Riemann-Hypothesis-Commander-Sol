# HATTER-SOL-11 · Exact Orbital Forgetting on Even Complete Hosts

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** closed theorem layer.

This file lifts the two-node separation theorem from `ORBITAL_NETWORK_FIBER_SEPARATION.md` to every even complete host and computes the exact scales at which orbit-labelled network information is lost.

---

## 1. Setup: one generic-odd forgetting fiber

Let `Delta<-3`, `Delta == 1 mod 4`, and let

\[
P>Q>0,
\qquad
S:=P+Q.
\]

By `FORGETTING_MAP_FIBER_CLASSIFICATION.md`, the folded pair `(P,Q)` has exactly three canonical orbital signatures:

\[
\Omega_I=(P;\{Q,0\}),
\qquad
\Omega_{II}=(Q;\{P,0\}),
\qquad
\Omega_{III}=(0;\{P,Q\}).
\]

Under the canonical orbit-total projection from `ORBITAL_NETWORK_FIBER_SEPARATION.md`,

\[
\Xi=(A,O),
\]

these become

\[
\boxed{
\Xi_I=(P,Q),
\qquad
\Xi_{II}=(Q,P),
\qquad
\Xi_{III}=(0,S).
}
\]

Here `A` is axial capacity and `O` is total oblique-orbit capacity.

Take the even complete host

\[
K_k,
\qquad
k=2m,
\qquad
c:=k-1=2m-1.
\]

The simple-support rule allows at most one edge total on each unordered vertex pair.

---

## 2. Exact uniform two-channel response

For any uniform orbit-total state `(A,O)` with

\[
A+O=S,
\]

write the Pareto boundary coordinates as `(B_A,B_O)`.

The exact uniform two-channel theorem of HATTER-SOL-09 applies verbatim after relabelling the channels as axial/oblique.

If

\[
S\le c,
\]

then both capacities can be saturated and

\[
\boxed{
\mathcal R_k(A,O)=\{(0,0)\}.
}
\]

Assume now

\[
S>c.
\]

Define

\[
D:=k(S-c),
\]

\[
L_A:=k(A-c)_+,
\qquad
L_O:=k(O-c)_+.
\]

Then

\[
\boxed{
\mathcal R_k(A,O)
=
\left\{(B_A,B_O):
\begin{array}{l}
B_A+B_O=D,\\
L_A\le B_A\le D-L_O,\\
B_A\equiv0\pmod2
\end{array}
\right\}.
}
\]

Because `k` is even, all endpoint values above have the required parity.

---

## 3. Substitute the three orbital fiber types

For `c<S`, put

\[
D=k(S-c)>0.
\]

### Type I

For

\[
\Xi_I=(P,Q),
\]

\[
\boxed{
\mathcal R_I(c)
=
\left\{(B_A,B_O):
B_A+B_O=D,
\quad
k(P-c)_+\le B_A\le D-k(Q-c)_+,
\quad
B_A\equiv0\pmod2
\right\}.
}
\]

### Type II

For

\[
\Xi_{II}=(Q,P),
\]

\[
\boxed{
\mathcal R_{II}(c)
=
\left\{(B_A,B_O):
B_A+B_O=D,
\quad
k(Q-c)_+\le B_A\le D-k(P-c)_+,
\quad
B_A\equiv0\pmod2
\right\}.
}
\]

### Type III

For

\[
\Xi_{III}=(0,S),
\]

we have

\[
L_A=0,
\qquad
L_O=D,
\]

and hence

\[
\boxed{
\mathcal R_{III}(c)=\{(0,D)\}
}
\]

for every `c<S`.

For `c>=S`, all three responses equal `{(0,0)}`.

---

## 4. Exact collision classification

### Theorem T11.24 — three-stage orbital forgetting law

Let `P>Q>0` and let `c=2m-1` be the degree of the even complete host.

Then:

### Stage I: fully orbit-visible

If

\[
\boxed{c<P,}
\]

then

\[
\boxed{
\mathcal R_I(c),
\mathcal R_{II}(c),
\mathcal R_{III}(c)
\text{ are pairwise distinct.}
}
\]

### Stage II: rank-swap forgotten, pure-oblique still visible

If

\[
\boxed{P\le c<S,}
\]

then

\[
\boxed{
\mathcal R_I(c)=\mathcal R_{II}(c)
e\mathcal R_{III}(c).
}
\]

More explicitly,

\[
\boxed{
\mathcal R_I(c)=\mathcal R_{II}(c)
=
\{(B_A,B_O):B_A+B_O=D,\ 0\le B_A\le D,\ B_A\equiv0\pmod2\},
}
\]

while

\[
\mathcal R_{III}(c)=\{(0,D)\}.
\]

### Stage III: complete closure

If

\[
\boxed{c\ge S,}
\]

then

\[
\boxed{
\mathcal R_I(c)=
\mathcal R_{II}(c)=
\mathcal R_{III}(c)=\{(0,0)\}.
}
\]

### Proof

If `c<P`, then

\[
k(P-c)_+>k(Q-c)_+.
\]

Indeed, if `c<Q`, this is `k(P-c)>k(Q-c)`; if `Q<=c<P`, it is `k(P-c)>0` while `k(Q-c)_+=0`. Thus the minimum attainable `B_A` values of Types I and II differ, so their Pareto sets differ.

Type III is a singleton. For `c<P`, Type I has strictly positive minimum `B_A`, so it cannot equal Type III. Type II either has positive minimum `B_A` (`c<Q`) or, when `Q<=c<P`, contains `B_A=0` but also contains further points because `Q>0`; hence it is not the singleton Type III response.

If `P<=c<S`, then also `Q<c`, so all lower-capacity truncations vanish:

\[
(P-c)_+=(Q-c)_+=0.
\]

Thus Types I and II both give the full step-two segment from `(0,D)` to `(D,0)`. Since `D>0` and `k>=2`, that segment has more than one point, whereas Type III remains the singleton `(0,D)`.

Finally, if `c>=S`, the total capacity fits inside the host degree and all three states saturate completely. QED.

---

## 5. Exact host thresholds

Define

\[
\boxed{
\sigma_{\mathrm{orb}}(P,Q)
:=
\min\{m:2m-1\ge P\}
=
\left\lceil\frac{P+1}{2}\right\rceil,
}
\]

and

\[
\boxed{
\tau_{\mathrm{orb}}(P,Q)
:=
\min\{m:2m-1\ge P+Q\}
=
\left\lceil\frac{P+Q+1}{2}\right\rceil.
}
\]

Then T11.24 becomes

\[
\boxed{
\begin{array}{rcl}
m<\sigma_{\mathrm{orb}}
&:& I,II,III\text{ all distinct},\\[1mm]
\sigma_{\mathrm{orb}}\le m<\tau_{\mathrm{orb}}
&:& I=II\ne III,\\[1mm]
m\ge\tau_{\mathrm{orb}}
&:& I=II=III.
\end{array}}
\]

Thus the orbit-aware network has two exact memory-loss thresholds:

1. at `sigma_orb`, it forgets whether the larger folded magnitude `P` belonged to the axial or oblique orbit;
2. at `tau_orb`, complete saturation erases the remaining distinction from the pure-oblique state.

---

## 6. When does the intermediate forgetting window exist?

The Stage-II interval is nonempty iff

\[
\sigma_{\mathrm{orb}}<\tau_{\mathrm{orb}}.
\]

Because the host degrees are odd, the first odd degree at least `P` is

\[
P
\quad\text{if `P` is odd},
\qquad
P+1
\quad\text{if `P` is even}.
\]

Therefore Stage II disappears exactly when

\[
P\text{ is even}
\qquad\text{and}\qquad
Q=1.
\]

Equivalently,

\[
\boxed{
\sigma_{\mathrm{orb}}=\tau_{\mathrm{orb}}
\iff
P\text{ even and }Q=1.
}
\]

In every other interior fiber there is at least one even complete host on which Types I and II have already collided while Type III remains visible.

---

## 7. Interpretation relative to the HATTER-SOL fold

The static map

\[
\Omega\longrightarrow(P,Q)
\]

forgets the three generic-odd orbital placements immediately.

The orbit-aware network does not.

Instead, it retains them dynamically according to

\[
\boxed{
3\ \text{states}
\longrightarrow
2\ \text{network classes}
\longrightarrow
1\ \text{closed class}.
}
\]

This is a genuine operational filtration of the forgetting fiber by host scale.

It is not an assumed activation hierarchy. It is derived from exact Pareto optimization.

---

## 8. Exact maximal-first probe on `K_{2m}`

Now impose the optional search rule `pi_max` from `MAXIMAL_FIRST_GEOMETRY_PROBE.md`:

> prioritize the orbit channel with the larger available total capacity; after saturating what the host allows in that channel, use remaining support for the smaller channel. Ties are retained rather than arbitrarily broken.

For the interior fiber `P>Q>0`, there is no initial tie.

The one-trace maximal-first responses are:

### Type I

\[
\boxed{
\mathcal M_I(c)=
\begin{cases}
\{(k(P-c),kQ)\},&c<P,\\
\{(0,D)\},&P\le c<S,\\
\{(0,0)\},&c\ge S.
\end{cases}}
\]

### Type II

\[
\boxed{
\mathcal M_{II}(c)=
\begin{cases}
\{(kQ,k(P-c))\},&c<P,\\
\{(D,0)\},&P\le c<S,\\
\{(0,0)\},&c\ge S.
\end{cases}}
\]

### Type III

\[
\boxed{
\mathcal M_{III}(c)=
\begin{cases}
\{(0,D)\},&c<S,\\
\{(0,0)\},&c\ge S.
\end{cases}}
\]

These traces are attainable on even complete hosts by the same 1-factorization / uniform-factor constructions used in the exact HATTER-SOL-09 theorem.

---

## 9. Maximal-first collision law

### Theorem T11.25 — probe blindness is different from full-response forgetting

For `P>Q>0`:

1. while `c<P`, Types I and II have the same maximal-first trace iff

\[
\boxed{c=P-Q.}
\]

Because `c=2m-1` is odd, such an even complete host exists iff `P-Q` is odd, in which case

\[
\boxed{
m=\frac{P-Q+1}{2}.}
\]

2. for every

\[
\boxed{P\le c<S,}
\]

we have

\[
\boxed{
\mathcal M_I(c)=\mathcal M_{III}(c)
e\mathcal M_{II}(c).
}
\]

3. for `c>=S`, all three traces are `(0,0)`.

### Proof

For `c<P`, equality of the Type-I and Type-II trace points requires

\[
k(P-c)=kQ,
\]

which is equivalent to `c=P-Q`; the second coordinate equation is identical.

For `P<=c<S`, the displayed formulas give

\[
\mathcal M_I(c)=\mathcal M_{III}(c)=\{(0,D)\},
\qquad
\mathcal M_{II}(c)=\{(D,0)\},
\]

and `D>0`.

Closure is immediate for `c>=S`. QED.

---

## 10. Why the probe cannot replace the full model

T11.24 and T11.25 show that the two equivalence relations are genuinely different.

In the intermediate open regime

\[
P\le c<S,
\]

the **full** orbit-labelled Pareto response says

\[
\boxed{I=II\ne III,}
\]

whereas the **maximal-first probe** says

\[
\boxed{I=III\ne II.}
\]

Thus the restricted probe does not merely lose some Pareto points. It can change **which orbital states appear indistinguishable**.

This is the exact mathematical version of the methodological warning:

\[
\boxed{
\text{maximal-first is useful for controlled exploration, but it is not the orbital law.}
}
\]

The two-node blind line `P-Q=1` from T11.23 is the special case `c=1` of the general probe-collision condition

\[
\boxed{c=P-Q.}
\]

---

## 11. What is now closed

For every generic-odd interior forgetting fiber `(P,Q)`, `P>Q>0`, we now know exactly:

- the three canonical orbital members;
- their orbit-total capacities;
- their full Pareto fronts on every even complete host;
- the first host scale where Types I and II collide;
- the final closure scale where all three collide;
- the exact condition for a nonempty intermediate memory phase;
- the complete maximal-first probe collision law on the same hosts.

This closes the first host-scale operational classification of the HATTER-SOL-11 forgetting map.

---

## 12. Next target

The next question should no longer be another uniform complete-host calculation.

The natural next strike is to ask which part of T11.24 survives when the host geometry itself changes:

\[
\text{path / 1D}
\subset
\text{outerplanar}
\subset
\text{planar}
\subset
\text{unrestricted}.
\]

The strongest candidate is a **geometry-dependent orbital memory theorem**:

> for one fixed generic-odd forgetting fiber, determine how the first collision scale between Types I, II, III moves when the admissible architecture class changes.

The maximal-first trajectory may be used as a cheap first probe, but the theorem target remains the full orbit-labelled response.