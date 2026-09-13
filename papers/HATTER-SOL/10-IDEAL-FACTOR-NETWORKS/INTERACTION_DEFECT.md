# HATTER-SOL-10 · Interaction defect

Status: closed structural layer separating cross-edge interaction from connectivity.

## 1. Unconstrained utilization set

Fix a typed witness configuration

\[
\theta=((P_1,Q_1),\ldots,(P_k,Q_k)).
\]

Let

\[
\mathcal U(\theta)\subset\mathbb Z_{\ge0}^2
\]

be the set of all pairs

\[
(e_P,e_Q)
\]

realized by simple typed graphs satisfying the capacity constraints, **without requiring connectedness**.

For weights

\[
w=(w_P,w_Q)\in\mathbb R_{\ge0}^2,
\]

define the support value

\[
\boxed{
h_\theta(w)
:=\max_{(e_P,e_Q)\in\mathcal U(\theta)}
(w_Pe_P+w_Qe_Q).
}
\]

The same definitions extend to a witness-adaptive ideal factor system by taking the union over all allowed witness configurations before maximizing.

## 2. Pure cross-interaction gain

Let two factor systems `A` and `B` have disjoint node sets. If cross-edges are forbidden, their utilization set is the Minkowski sum

\[
\mathcal U_A\oplus\mathcal U_B.
\]

When cross-edges are allowed, this block-diagonal region remains feasible, hence

\[
\mathcal U_A\oplus\mathcal U_B
\subseteq
\mathcal U_{A\cup B}.
\]

### Definition T10.9 — interaction defect/gain

\[
\boxed{
\Gamma_w(A,B)
:=h_{A\cup B}(w)-h_A(w)-h_B(w).
}
\]

### Theorem T10.10 — nonnegativity

For every nonnegative weight vector `w`,

\[
\boxed{\Gamma_w(A,B)\ge0.}
\]

### Proof

Take optimal unconstrained realizations of `A` and `B` and place them disjointly on the union. This is feasible when cross-edges are permitted and has weighted edge value `h_A(w)+h_B(w)`. Therefore the unrestricted optimum on the union cannot be smaller. QED.

This quantity measures only the extra utilization made possible by allowing edges between the two factor systems. No connectedness requirement appears in its definition.

## 3. Exact separation from the connectivity effect

Let

\[
h_A^c(w)
\]

denote the same weighted edge maximum when connectedness is required, whenever a connected realization exists. Define the connectivity penalty

\[
\boxed{
\kappa_A(w):=h_A(w)-h_A^c(w)\ge0.
}
\]

Then

\[
\boxed{
 h_{A\cup B}^c-h_A^c-h_B^c
 =
 \Gamma_w(A,B)
 -\kappa_{A\cup B}(w)
 +\kappa_A(w)+\kappa_B(w).
}
\]

Thus the connected-network response decomposes exactly into:

1. pure cross-edge interaction `Gamma`;
2. connectivity penalties of the separate and combined systems.

For a fixed witness configuration, weighted free boundary is

\[
\lambda_w^c(\theta)
=
\sum_i(w_PP_i+w_QQ_i)-2h_\theta^c(w).
\]

Hence

\[
\boxed{
\lambda_w^c(A\cup B)-\lambda_w^c(A)-\lambda_w^c(B)
=
-2\Gamma_w
+2\kappa_{A\cup B}
-2\kappa_A-2\kappa_B.
}
\]

This formula is the requested separation: interaction is not an artifact of the mandatory bridge needed to connect two components.

## 4. Exact non-UFD example in Q(sqrt(-15))

Let

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
\mathfrak p=(2,\omega),
\qquad
\bar{\mathfrak p}=(2,1-\omega),
\]

as in `WITNESS_ADAPTIVE_NETWORKS.md`.

Split

\[
(4)=A B,
\qquad
A=(2)=\mathfrak p\bar{\mathfrak p},
\qquad
B=(2)=\mathfrak p\bar{\mathfrak p}.
\]

Choose the `(2,0)` witness state on every prime-ideal node. Each two-node subsystem has only one possible simple edge, so for scalar weight `w=(1,0)`,

\[
h_A=h_B=1.
\]

On all four nodes, degree cap `2` allows a four-cycle, so

\[
h_{A\cup B}=4.
\]

Therefore

\[
\boxed{\Gamma_{(1,0)}(A,B)=4-1-1=2.}
\]

All three maximizing graphs can be connected, hence

\[
\kappa_A=\kappa_B=\kappa_{A\cup B}=0.
\]

Thus the boundary release on combination is exactly

\[
\boxed{-2\Gamma=-4.}
\]

Indeed the two separate two-node systems have total free boundary `4`, while the combined four-cycle has boundary `0`.

This is a genuine interaction effect: the same gain is present before connectedness is imposed.

## 5. Residue-fibered interaction

For a principal ideal factor system `A`, each witness configuration `theta` has a principalization residue orbit

\[
r(\theta)=[\beta_\theta]
\in K^\times/O_K^\times.
\]

Define the residue fiber

\[
\mathcal U_A(r)
:=
\bigcup_{\theta:r(\theta)=r}\mathcal U(\theta)
\]

and its support function

\[
h_A(r;w)
:=
\max_{u\in\mathcal U_A(r)}w\cdot u.
\]

If `A` and `B` are principal factor systems, residue multiplication satisfies

\[
r(\theta_A\sqcup\theta_B)=r(\theta_A)r(\theta_B).
\]

Therefore for every residue orbit `r`,

\[
\boxed{
\bigcup_{r_1r_2=r}
\left(
\mathcal U_A(r_1)\oplus\mathcal U_B(r_2)
\right)
\subseteq
\mathcal U_{A\cup B}(r).
}
\]

Define the residue-convolution baseline

\[
\boxed{
(h_A\star h_B)(r;w)
:=
\max_{r_1r_2=r}
\bigl(h_A(r_1;w)+h_B(r_2;w)\bigr).
}
\]

### Theorem T10.11 — fiber interaction nonnegativity

\[
\boxed{
\Gamma_w(A,B\mid r)
:=
h_{A\cup B}(r;w)
-(h_A\star h_B)(r;w)
\ge0.
}
\]

This is the clean separation between the two layers:

\[
\boxed{
\text{residue arithmetic combines by convolution,}
\qquad
\text{network cross-edges create a nonnegative interaction gain inside each residue fiber.}
}
\]

## 6. Residue collision at zero boundary

For `(4)` in the same field, two witness choices give fully closed networks with

\[
(B_P,B_Q)=(0,0)
\]

but distinct principalization residues.

- choosing the witness `2` on every prime-ideal node gives residue generator `4`, with typed residue pair `(4,0)`;
- choosing `omega` on both `p`-nodes and `2` on both conjugate nodes gives residue generator `omega^2=omega-4`, with typed residue pair `(3,1)`.

Both residue generators have norm `16`.

Hence

\[
\boxed{
\text{same network boundary + same residue norm}
\not\Rightarrow
\text{same residue geometry}.}
\]

The residue orbit must therefore be retained before any scalar norm projection.

## 7. Consequence for HATTER-SOL-10

The current response hierarchy is now

\[
\boxed{
\text{prime-ideal factors}
\to
\text{minimal witness states}
\to
\text{principalization residue fibers}
\to
\text{typed utilization regions}
\to
\Gamma_w(A,B\mid r)
\to
\text{connected Pareto response}.
}
\]

A third additive class-group boundary coordinate is unnecessary. Class data act as conserved labels; interaction lives in enlargement of utilization regions by cross-edges.

## 8. Next target

Determine whether `Gamma_w` admits sharp capacity-only upper bounds and characterize the zero-interaction condition. In particular, seek an exact criterion for

\[
\Gamma_w(A,B)=0
\]

in terms of saturation of all potentially useful cross-edge endpoint capacities.