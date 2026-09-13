# HATTER-SOL-10 · Witness-switching gain on a fixed host

Status: closed theorem layer isolating a genuinely nonprincipal interaction effect.

## 1. A no-go result for the naive definition

Let `Sigma` be a finite witness-configuration space and let `G(theta)` be the finite family of admissible typed graphs for configuration `theta`. For any objective `F(theta,G)`,

\[
\max_{\theta\in\Sigma}\max_{G\in G(\theta)}F(\theta,G)
=
\max_{(\theta,G)}F(\theta,G).
\]

Therefore there is no intrinsic distinction between

1. globally optimizing a witness configuration and then optimizing the network, and
2. optimizing witnesses and edges jointly,

provided both optimizations see the same global instance.

Any claimed gain based only on reordering these two maxima would be artificial.

The nontrivial question is different:

> Can witness states that are optimal for isolated factor subsystems become suboptimal after the subsystems are allowed to interact?

This gives a canonical comparison because the frozen baseline is selected by the isolated optimization problems themselves.

---

## 2. Host-restricted weighted utilization

Let `H` be a fixed simple host graph on the factor nodes. For a typed witness configuration

\[
\theta=((P_1,Q_1),\ldots,(P_k,Q_k)),
\]

let

\[
h_H(\theta;w_P,w_Q)
\]

be the maximum of

\[
w_P|E_P|+w_Q|E_Q|
\]

over all edge-disjoint typed subgraphs `E_P,E_Q subset E(H)` satisfying

\[
d_P(v_i)\le P_i,
\qquad
d_Q(v_i)\le Q_i.
\]

Connectedness is not imposed here; the goal is to isolate utilization from connectivity.

For a factor subsystem `A`, define its locally optimal witness set

\[
\operatorname{Opt}_A(w)
:=
\arg\max_{\theta_A\in\Sigma_A}h_{H_A}(\theta_A;w).
\]

For two subsystems `A,B` embedded in a common host `H`, define the **locally frozen baseline**

\[
\boxed{
H_{\rm frozen}(A,B;w)
:=
\max_{\substack{
\theta_A\in\operatorname{Opt}_A(w)\\
\theta_B\in\operatorname{Opt}_B(w)}}
 h_H(\theta_A\sqcup\theta_B;w).
}
\]

Define the fully adaptive value

\[
\boxed{
H_{\rm adapt}(A,B;w)
:=
\max_{\theta_A\in\Sigma_A,\theta_B\in\Sigma_B}
 h_H(\theta_A\sqcup\theta_B;w).
}
\]

and the witness-switching gain

\[
\boxed{
W_H(A,B;w)
:=H_{\rm adapt}-H_{\rm frozen}\ge0.
}
\]

This compares two optimizations on the **same combined host graph**. It therefore does not confuse witness switching with a topology change.

---

## 3. A nonprincipal prime ideal with incomparable states

Work in

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
O_K=\mathbb Z[\omega],
\qquad
\omega=\frac{1+\sqrt{-15}}2,
\]

with

\[
N(a+b\omega)=a^2+ab+4b^2.
\]

Since

\[
7^2-7+4=46\equiv0\pmod{23},
\]

define the prime ideal

\[
\boxed{
\mathfrak q=(23,\omega-7),
\qquad N(\mathfrak q)=23.
}
\]

There is no element of norm `23`: from

\[
a^2+ab+4b^2=23
\]

the discriminant in `a` is

\[
92-15b^2,
\]

so `|b|<=2`; direct checking of `b=0,+-1,+-2` gives no integral solution. Hence `q` is nonprincipal.

The elements

\[
7-\omega
\qquad\text{and}\qquad
2+3\omega
\]

belong to `q` because their coefficient pairs satisfy `a+7b congruent 0 mod 23`, and both have norm `46`. Since `q` is nonprincipal,

\[
\delta(\mathfrak q)\ge2,
\]

while these witnesses give ratio `46/23=2`; therefore

\[
\boxed{\delta(\mathfrak q)=2.}
\]

Solving

\[
a^2+ab+4b^2=46
\]

and imposing `a+7b congruent 0 mod 23` leaves, up to the units `+-1`, exactly the two witness orbits represented by

\[
7-\omega,
\qquad
2+3\omega.
\]

For the odd-discriminant HATTER-SOL capacity law,

\[
\Pi(7-\omega)=(6,1),
\qquad
\Pi(2+3\omega)=(3,2).
\]

Thus

\[
\boxed{
\Theta_K(\mathfrak q)=\{S,T\},
\qquad
S=(3,2),\quad T=(6,1).
}
\]

The two states are coordinatewise incomparable.

Because `Cl(Q(sqrt(-15)))` has order two and `q` is nonprincipal, its class has order two. Hence `q^4` and `q^8` are principal ideal systems, so the block experiment below can be embedded in principal inputs.

---

## 4. Isolated four-node subsystem

Take four copies of `q` with host graph

\[
H_A=K_4.
\]

Use weights

\[
\boxed{w_P=1,\qquad w_Q=2.}
\]

Let `t` be the number of nodes assigned state `T=(6,1)`; the remaining `4-t` nodes use `S=(3,2)`.

On `K_4`, the P-capacity is never restrictive: both states have effective P-capacity at least the host degree whenever an edge is not colored Q. Since every Q-edge is worth one unit more than a P-edge, the optimum uses all six host edges and maximizes the number of Q-edges.

The total Q-degree budget is

\[
t+2(4-t)=8-t.
\]

The maximum Q-edge counts for `t=0,1,2,3,4` are respectively

\[
4,3,3,2,2.
\]

Hence

\[
h_{K_4}(t)=6+e_Q^{\max}(t)
\]

takes the values

\[
\boxed{10,9,9,8,8.}
\]

Therefore the isolated four-node system has the **unique** locally optimal witness configuration

\[
\boxed{S^4.}
\]

Let `B` be an identical second four-node subsystem. It also freezes locally to `S^4`.

---

## 5. Combine the same eight nodes on the fixed host K8

Now place the eight factor nodes in the common host

\[
\boxed{H=K_8.}
\]

The comparison below is entirely inside this fixed host.

### 5.1 Frozen local choices

The locally frozen configuration is

\[
S^8=(3,2)^8.
\]

For any typed graph under these capacities,

\[
|E_P|+2|E_Q|
\le
\frac12\sum_iP_i+\sum_iQ_i
=\frac{8\cdot3}{2}+8\cdot2
=28.
\]

This bound is attained. Label vertices by `Z/8Z`:

- take the Q-graph to be the 8-cycle with difference `+-1`, giving Q-degree `2` and `8` Q-edges;
- take the P-graph with differences `+-2` together with the four opposite pairs of difference `4`, giving P-degree `3` and `12` P-edges.

The two edge sets are disjoint. Hence

\[
\boxed{H_{\rm frozen}=12+2\cdot8=28.}
\]

### 5.2 Adaptive witness choices

Suppose `t` of the eight nodes use `T=(6,1)` and `8-t` use `S=(3,2)`. The weighted degree-capacity bound gives

\[
|E_P|+2|E_Q|
\le
\frac12\sum_iP_i+\sum_iQ_i.
\]

Now

\[
\sum_iP_i=6t+3(8-t)=24+3t,
\]

\[
\sum_iQ_i=t+2(8-t)=16-t.
\]

Therefore

\[
\boxed{
h_{K_8}\le 28+\frac t2\le32.}
\]

For `t=8`, assign `T=(6,1)` to every node. Choose

- a perfect matching as the Q-graph: `4` Q-edges, Q-degree `1`;
- its complement in `K_8` as the P-graph: `24` P-edges, P-degree `6`.

Thus

\[
\boxed{H_{\rm adapt}=24+2\cdot4=32.}
\]

The upper bound shows this is globally optimal.

### Theorem T10.14 — strict witness-switching gain

For the two principal four-node systems `A=B=q^4`, weight vector `(1,2)`, and fixed combined host `K_8`,

\[
\boxed{
W_{K_8}(A,B;(1,2))=32-28=4>0.
}
\]

The isolated optimum chooses `S=(3,2)` at every node, whereas the interacting optimum on the same eight nodes and same host chooses `T=(6,1)` at every node.

No change of factorization, node count, or combined host topology is involved.

---

## 6. Interpretation

This establishes a genuinely nonprincipal effect:

\[
\boxed{
\text{local witness optimum}
\not\Rightarrow
\text{global witness optimum after interaction}.
}
\]

The mechanism is an interface tradeoff.

- `S=(3,2)` is locally superior on `K_4` because its extra Q-capacity exploits the more valuable Q-channel.
- On `K_8`, the larger neighbor space makes the much larger P-capacity of `T=(6,1)` usable; the loss of one Q-port is overcompensated by three additional P-ports.

This is distinct from:

1. ordinary neighbor-space interaction with a fixed capacity state;
2. parity repair;
3. connectedness effects;
4. residue multiplication.

It depends essentially on a nonprincipal ideal carrying several incomparable minimal witness states.

## 7. Boundary-language version

For a fixed witness configuration `theta`, define the weighted unused interface resource

\[
B_w(\theta,G)
=\sum_i(w_PP_i+w_QQ_i)-2(w_P|E_P|+w_Q|E_Q|).
\]

The switching theorem is most naturally stated in utilization language because changing witnesses also changes total available weighted capacity. If one wants a boundary comparison, both the utilized edge value and the witness-dependent total capacity must be reported; subtracting only boundary numbers would mix resource creation with resource utilization.

Thus `W_H` is retained as a utilization-response observable, not mislabeled as a pure boundary release.

## 8. Next target

The next research question is whether the strict switching effect admits a general criterion. For two witness states

\[
S=(P_s,Q_s),\qquad T=(P_t,Q_t)
\]

with opposite tradeoff

\[
P_t>P_s,\qquad Q_t<Q_s,
\]

seek host-size thresholds at which the locally optimal state changes from `S` to `T` under a fixed weight vector. This would produce a witness-state phase transition law rather than a single example.