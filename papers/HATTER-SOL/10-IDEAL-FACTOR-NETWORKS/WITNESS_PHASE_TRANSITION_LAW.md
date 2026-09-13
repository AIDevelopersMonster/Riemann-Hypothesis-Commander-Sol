# HATTER-SOL-10 · Exact witness-state phase transition on even complete hosts

Status: closed theorem layer generalizing the strict witness-switching example.

## 1. Uniform typed state on an even complete host

Let `k` be even and let

\[
c:=k-1.
\]

Consider a uniform typed state

\[
(P,Q)
\]

on every vertex of the complete host `K_k`. Let edge weights satisfy

\[
w_Q\ge w_P\ge0.
\]

Define

\[
h_k(P,Q;w_P,w_Q)
\]

as the maximum of

\[
w_P|E_P|+w_Q|E_Q|
\]

over edge-disjoint typed subgraphs `E_P,E_Q subset E(K_k)` with

\[
d_P(v)\le P,
\qquad
d_Q(v)\le Q.
\]

### Theorem T10.15 — exact uniform typed utilization law

Put

\[
q_c:=\min(Q,c),
\qquad
p_c:=\min(P,c-q_c).
\]

Then

\[
\boxed{
h_k(P,Q;w_P,w_Q)
=\frac{k}{2}\bigl(w_Qq_c+w_Pp_c\bigr).
}
\]

### Proof

Write the objective as

\[
w_P(|E_P|+|E_Q|)+(w_Q-w_P)|E_Q|.
\]

Thus for `w_Q>=w_P` an optimum first maximizes the possible number of Q-edges and, subject to that, the total number of used edges.

At each vertex the Q-degree is at most `q_c=min(Q,c)`, so

\[
|E_Q|\le\frac{kq_c}{2}.
\]

After allocating Q-degree `q_c`, at most `c-q_c` unused incident host edges remain per vertex; hence the P-degree is at most

\[
p_c=\min(P,c-q_c),
\]

and

\[
|E_P|\le\frac{kp_c}{2}.
\]

Because `k` is even, `K_k` has a 1-factorization into exactly `c=k-1` perfect matchings. Take `q_c` factors for the Q-channel and a disjoint set of `p_c` factors for the P-channel. This realizes both bounds simultaneously. QED.

Define the per-vertex doubled score

\[
\boxed{
\phi_c(P,Q)
:=w_Q\min(Q,c)
+w_P\min\bigl(P,(c-Q)_+\bigr),
}
\]

so that

\[
h_k=\frac{k}{2}\phi_c.
\]

---

## 2. Two incomparable witness states

Let

\[
S=(P_s,Q_s),
\qquad
T=(P_t,Q_t),
\]

with the strict tradeoff

\[
\boxed{
P_t>P_s,
\qquad
Q_t<Q_s.
}
\]

Assume

\[
w_Q>w_P>0.
\]

Write

\[
\Delta_P=P_t-P_s>0,
\qquad
\Delta_Q=Q_s-Q_t>0,
\]

and

\[
C_s=P_s+Q_s,
\qquad
C_t=P_t+Q_t.
\]

The fully saturated weighted scores are

\[
W_s=w_PP_s+w_QQ_s,
\]

\[
W_t=w_PP_t+w_QQ_t.
\]

Hence

\[
\boxed{
W_t-W_s=w_P\Delta_P-w_Q\Delta_Q.
}
\]

### No-switch condition

If

\[
\boxed{
w_P\Delta_P\le w_Q\Delta_Q,}
\]

then `T` cannot become strictly better than `S` in the large-host regime. In particular there is no permanent `S -> T` phase transition.

### Switch condition

Assume from now on

\[
\boxed{
w_P\Delta_P>w_Q\Delta_Q.}
\]

Then automatically

\[
\Delta_P>\Delta_Q,
\qquad
C_t>C_s.
\]

Thus `S` reaches full capacity before `T` as the host degree `c` grows.

---

## 3. Exact transition threshold

Define the real threshold

\[
\boxed{
 c_*:=
 C_s+
 \left(\frac{w_Q}{w_P}-1\right)\Delta_Q.
}
\]

Equivalently,

\[
c_*=P_s+Q_t+\frac{w_Q}{w_P}(Q_s-Q_t).
\]

### Theorem T10.16 — witness-state phase transition law

Under the strict switch condition

\[
w_P\Delta_P>w_Q\Delta_Q,
\]

for every even complete host `K_k`, `c=k-1`, one has:

\[
\boxed{
\phi_c(S)\ge\phi_c(T)
\quad\text{for }c\le c_*,
}
\]

and

\[
\boxed{
\phi_c(T)>\phi_c(S)
\quad\text{for }c>c_*.
}
\]

At an admissible integer `c=c_*`, if equality is possible, the two witness states tie.

### Proof

Because the switch condition implies `C_t>C_s`, both states can use every available host incidence while `c<=C_s`, except that `S` has at least as much of the more valuable Q-resource. Therefore `S` is never worse before it saturates.

For

\[
C_s<c<C_t,
\]

state `S` is fully saturated, so

\[
\phi_c(S)=W_s=w_PP_s+w_QQ_s.
\]

State `T` has its Q-capacity saturated but is still P-unsaturated, hence

\[
\phi_c(T)=w_QQ_t+w_P(c-Q_t).
\]

Therefore

\[
\phi_c(T)-\phi_c(S)
=
w_P(c-C_s)-(w_Q-w_P)\Delta_Q.
\]

This is positive exactly when

\[
c>
C_s+
\left(\frac{w_Q}{w_P}-1\right)\Delta_Q
=c_*.
\]

Finally, the strict switch condition gives

\[
c_*<C_t,
\]

because

\[
C_t-c_*
=
\Delta_P-\frac{w_Q}{w_P}\Delta_Q>0.
\]

Thus the crossing occurs before `T` saturates. For `c>=C_t`, both states are saturated and

\[
\phi_c(T)-\phi_c(S)=W_t-W_s>0,
\]

so `T` remains strictly optimal thereafter. QED.

---

## 4. First even host after the transition

Since `k` is even, the host degree

\[
c=k-1
\]

is odd. Therefore the first complete host in this exact theorem family on which `T` strictly dominates is

\[
\boxed{
 k_{\rm switch}
 =
 \min\{k\in2\mathbb Z_{\ge2}:k-1>c_*\}.
}
\]

This discretization is the only parity correction to the real threshold.

---

## 5. Recovery of the Q(sqrt(-15)) witness switch

For the nonprincipal prime ideal

\[
\mathfrak q=(23,\omega-7)
\]

from `WITNESS_SWITCHING_GAIN.md`, the two minimal witness states are

\[
S=(3,2),
\qquad
T=(6,1),
\]

with weights

\[
w_P=1,
\qquad
w_Q=2.
\]

Then

\[
\Delta_P=3,
\qquad
\Delta_Q=1,
\]

and the strict switch condition is

\[
3>2.
\]

The threshold is

\[
 c_*
 =5+(2-1)\cdot1
 =6.
\]

Hence `T` strictly wins exactly on even hosts with

\[
k-1>6.
\]

The first such host is

\[
\boxed{k_{\rm switch}=8.}
\]

Thus the previously found

\[
K_4:\ S\text{ preferred},
\qquad
K_8:\ T\text{ preferred}
\]

is the first discrete instance of the general phase-transition theorem.

---

## 6. Interpretation

The threshold consists of two terms:

\[
\boxed{
 c_*=C_s+
 \left(\frac{w_Q}{w_P}-1\right)\Delta_Q.
}
\]

- `C_s=P_s+Q_s` is the host degree at which the locally Q-rich state `S` exhausts its total interface capacity.
- The correction
  \[
  \left(\frac{w_Q}{w_P}-1\right)\Delta_Q
  \]
  is the extra neighbor space required to compensate for replacing `Delta_Q` expensive Q-ports by cheaper P-ports.

Thus the transition is not merely a capacity crossover. It is a weighted compensation law between channel quality and newly usable neighbor space.

## 7. Scope

The theorem is exact for:

1. uniform witness state on all nodes;
2. even complete hosts `K_k`;
3. two channels with simple-support exclusion;
4. `w_Q>w_P>0`;
5. opposite-tradeoff witness states.

It does not yet cover heterogeneous mixtures of `S` and `T`, odd host size, noncomplete host graphs, or connectedness-constrained optima.

## 8. Next target

The next natural question is whether mixed populations of witness states can beat both uniform phases near `c_*`. Define, for `t` nodes in state `T` and `k-t` in state `S`, the exact optimum

\[
h_k(t).
\]

Determine whether the transition is always all-or-nothing or whether an intermediate mixed phase exists. This is the next theorem target.