# HATTER-SOL-10 · Purity theorem for witness states on even complete hosts

Status: closed theorem layer. This resolves the mixed-phase question in the exact complete-host regime.

## 1. Setup

Let `k` be even and

\[
c=k-1.
\]

Let every factor node have the same finite witness-state set

\[
\Theta\subset\mathbb Z_{\ge0}^2.
\]

A witness assignment is

\[
\theta=(\theta_1,\ldots,\theta_k),
\qquad
\theta_i=(P_i,Q_i)\in\Theta.
\]

On the complete host `K_k`, choose edge-disjoint typed subgraphs `E_P,E_Q` satisfying

\[
d_P(v_i)\le P_i,
\qquad
d_Q(v_i)\le Q_i.
\]

Fix weights

\[
w_Q\ge w_P\ge0.
\]

Let

\[
h_k(\theta)
:=
\max\bigl(w_P|E_P|+w_Q|E_Q|\bigr).
\]

For a single state `X=(P,Q)` define its local host score

\[
\boxed{
\phi_c(X)
:=
w_Q\min(Q,c)
+w_P\min\bigl(P,(c-Q)_+\bigr).
}
\]

By T10.15, the uniform assignment `X^k` has exact value

\[
\boxed{
h_k(X^k)=\frac{k}{2}\phi_c(X).}
\]

---

## 2. Local incidence bound

For any feasible typed graph and any vertex in state `X=(P,Q)`, put

\[
p=d_P(v),
\qquad
q=d_Q(v).
\]

Then

\[
0\le p\le P,
\qquad
0\le q\le Q,
\qquad
p+q\le c.
\]

Since `w_Q>=w_P`, the maximum possible weighted incidence at that vertex is obtained by filling Q-incidences first and then P-incidences. Therefore

\[
\boxed{
w_Pp+w_Qq\le\phi_c(X).}
\]

Summing over all vertices and using the handshake identity separately in the two colors gives

\[
2\bigl(w_P|E_P|+w_Q|E_Q|\bigr)
=
\sum_{i=1}^k
\bigl(w_Pd_P(v_i)+w_Qd_Q(v_i)\bigr).
\]

Hence every witness assignment satisfies

\[
\boxed{
h_k(\theta)
\le
\frac12\sum_{i=1}^k\phi_c(\theta_i).}
\]

---

## 3. Purity theorem

### Theorem T10.17 — no strict mixed phase

For an even complete host `K_k` with a common witness-state set `Theta`,

\[
\boxed{
\max_{\theta\in\Theta^k}h_k(\theta)
=
\frac{k}{2}\max_{X\in\Theta}\phi_c(X).
}
\]

In particular, a globally optimal witness assignment always exists that is **pure**:

\[
\boxed{\theta=X_*^k}
\]

for some

\[
X_*\in\arg\max_{X\in\Theta}\phi_c(X).
\]

No heterogeneous witness population can strictly outperform every pure phase.

### Proof

For every assignment `theta`, the local incidence bound gives

\[
h_k(\theta)
\le
\frac12\sum_i\phi_c(\theta_i)
\le
\frac{k}{2}\max_{X\in\Theta}\phi_c(X).
\]

Choose a state `X_*` attaining the maximum. Because `k` is even, the 1-factorization construction of T10.15 realizes the uniform assignment `X_*^k` with value

\[
h_k(X_*^k)=\frac{k}{2}\phi_c(X_*).
\]

Thus the upper bound is sharp. QED.

---

## 4. Two-state corollary

For

\[
\Theta=\{S,T\}
\]

and an assignment containing exactly `t` vertices in state `T`, let

\[
h_k(t)
\]

be its optimum. By symmetry of the complete host the value depends only on `t`.

Then

\[
\boxed{
h_k(t)
\le
\frac{k-t}{2}\phi_c(S)
+
\frac{t}{2}\phi_c(T).}
\]

Using

\[
h_k(0)=\frac{k}{2}\phi_c(S),
\qquad
h_k(k)=\frac{k}{2}\phi_c(T),
\]

we obtain

\[
\boxed{
h_k(t)
\le
\frac{k-t}{k}h_k(0)
+
\frac{t}{k}h_k(k).}
\]

Therefore

\[
\boxed{
h_k(t)\le\max\{h_k(0),h_k(k)\}.}
\]

If

\[
\phi_c(S)\ne\phi_c(T),
\]

then every strict mixture `0<t<k` satisfies

\[
\boxed{
h_k(t)<\max\{h_k(0),h_k(k)\}.}
\]

Thus away from the phase-transition point the better pure state strictly dominates every mixed population.

---

## 5. Coexistence can occur only on the phase boundary

A mixed assignment can tie the pure optimum only if every state used by that assignment belongs to

\[
\arg\max_{X\in\Theta}\phi_c(X).
\]

For two states this requires

\[
\boxed{\phi_c(S)=\phi_c(T).}
\]

Hence mixed coexistence is confined to the exact phase boundary. Even there, global parity and edge-disjointness can prevent some mixtures from attaining the local upper bound.

This produces a discrete coexistence phenomenon rather than a genuine mixed phase.

---

## 6. Exact parity-split coexistence example

Take

\[
k=6,
\qquad c=5,
\]

\[
S=(2,2),
\qquad
T=(5,1),
\]

and

\[
w_P=1,
\qquad
w_Q=2.
\]

Then

\[
\phi_5(S)=2\cdot2+1\cdot2=6,
\]

while

\[
\phi_5(T)=2\cdot1+1\cdot4=6.
\]

Thus both pure phases have

\[
\boxed{h_6(0)=h_6(6)=18.}
\]

Let `t` be the number of T-nodes.

### Proposition T10.18

\[
\boxed{
h_6(t)=
\begin{cases}
18,&t\text{ even},\\
17,&t\text{ odd}.
\end{cases}}
\]

### Upper bound for odd `t`

To attain the global upper bound `18`, every vertex must attain its local score `6`.

For an S-node, the unique local maximizing degree pair is

\[
(d_P,d_Q)=(2,2).
\]

For a T-node, the unique local maximizing pair is

\[
(d_P,d_Q)=(4,1).
\]

Hence an upper-bound-saturating configuration would have total Q-degree

\[
2(6-t)+t=12-t.
\]

If `t` is odd this number is odd, impossible by the handshake lemma. Thus

\[
h_6(t)\le17
\]

for odd `t`.

### Attainment for even `t`

For `t=0` and `t=6`, a 1-factorization of `K_6` gives the two pure optima.

For `t=2`, label T-vertices `0,1` and S-vertices `2,3,4,5`. Leave unused

\[
U=\{25,34\}.
\]

Take

\[
E_Q=\{01,23,24,35,45\}.
\]

Let `E_P` be the complement of `U union E_Q` in `K_6`. Then T-vertices have typed degrees `(4,1)` and S-vertices `(2,2)`, so the value is `18`.

For `t=4`, label T-vertices `0,1,2,3` and S-vertices `4,5`. Leave unused

\[
U=\{45\},
\]

and take

\[
E_Q=\{05,14,25,34\}.
\]

Again the complement is a P-graph with the required degrees, giving value `18`.

### Attainment for odd `t`

Explicit feasible edge sets give value `17`:

- `t=1`, with T-vertex `0`:
  \[
  E_P=\{01,02,03,04,05,25,34\},
  \]
  \[
  E_Q=\{12,13,24,35,45\};
  \]
- `t=3`, with T-vertices `0,1,2`:
  \[
  E_P=\{01,02,03,04,12,13,15,24,25\},
  \]
  \[
  E_Q=\{05,14,23,35\};
  \]
- `t=5`, with T-vertices `0,1,2,3,4`:
  \[
  E_P=\{01,03,04,12,13,14,15,23,24,25,34\},
  \]
  \[
  E_Q=\{02,35,45\}.
  \]

Thus the upper bounds are sharp. QED.

---

## 7. Interpretation

The exact complete-host theory therefore has the following structure:

\[
\boxed{
\text{pure phase S}
\longrightarrow
\text{coexistence boundary}
\longrightarrow
\text{pure phase T}.
}
\]

There is **no open interval of strict mixed optimality**.

At the equality point, mixed populations may coexist, but discrete graph constraints can split the coexistence set into allowed and forbidden compositions. In the example above the selection rule is simply

\[
\boxed{t\equiv0\pmod2.}
\]

Thus parity can act as a finite-size selection rule on the phase boundary.

---

## 8. Stronger conceptual consequence

The result is not restricted to two witness states. If a nonprincipal ideal has a finite state set

\[
\Theta_K(I)=\{X_1,\ldots,X_r\},
\]

then on every even complete host the witness-adaptive optimum is the upper envelope

\[
\boxed{
H_k(I)=\frac{k}{2}\max_j\phi_{k-1}(X_j).
}
\]

As `k` grows, the optimal state can jump between pure witness phases, but a strict heterogeneous phase cannot appear without an additional global coupling constraint.

Such a coupling could come from:

1. fixing a principalization residue fiber;
2. imposing a noncomplete host topology;
3. imposing additional global parity/congruence conditions;
4. coupling different ideal species with different witness sets.

These are the only remaining places where a genuine mixed phase can occur.

## 9. Next target

The most natural next problem is **residue-constrained coexistence**. Fix a principalization residue orbit `r` and optimize only over witness assignments whose companion product lies in that residue fiber. The purity theorem no longer applies directly because a uniform maximizing state may be excluded by the global product constraint.

This is the next HATTER-SOL-10 theorem target.