# HATTER-SOL-10 · Residue-constrained coexistence

Status: closed theorem layer. This file shows that a genuine mixed witness phase can be forced by arithmetic residue data even though unconstrained even-complete-host optimization is pure.

## 1. Residue-constrained score

Let a principal ideal factor system have minimal witness configurations `theta`. Each `theta` determines a principalization companion product

\[
R(\theta):=\prod_j J_j,
\qquad
J_j=(\alpha_j)\mathfrak p_j^{-1}.
\]

For a principal input this product is principal. Its generator modulo units is the principalization residue orbit; equivalently one may retain the principal residue ideal `R(theta)` itself.

For a fixed host `H`, weights `w=(w_P,w_Q)`, and a fixed principal residue ideal `R`, define

\[
\boxed{
H_H(R;w)
:=
\max_{\theta:R(\theta)=R}
 h_H(\theta;w).
}
\]

The unrestricted witness-adaptive value is

\[
H_H^{\rm free}(w)=\max_R H_H(R;w).
\]

Define the residue-selection penalty

\[
\boxed{
\Delta_{\rm res}(R;w)
:=
H_H^{\rm free}(w)-H_H(R;w)
\ge0.
}
\]

---

## 2. Two witness orbits and companion ideals

Let a fixed nonprincipal ideal `I` have two minimal witness orbits represented by

\[
\alpha_S,\qquad\alpha_T,
\]

with companion ideals

\[
J_S=(\alpha_S)I^{-1},
\qquad
J_T=(\alpha_T)I^{-1}.
\]

Assume

\[
J_S\ne J_T.
\]

Let `k` be such that `I^k` is principal. A configuration containing exactly `t` witnesses of type `T` and `k-t` of type `S` has residue ideal

\[
\boxed{
R_t=J_S^{k-t}J_T^t.
}
\]

### Theorem T10.19 — residue/composition injectivity

If `J_S != J_T`, then

\[
\boxed{
R_t=R_s\iff t=s.
}
\]

Hence the residue ideal uniquely determines the number of `T`-state nodes.

### Proof

Suppose `R_t=R_s`. Then

\[
J_S^{k-t}J_T^t=J_S^{k-s}J_T^s,
\]

so in the group of nonzero fractional ideals,

\[
(J_TJ_S^{-1})^{t-s}=O_K.
\]

The fractional ideal group of a Dedekind domain is free abelian on the nonzero prime ideals, hence torsion-free. Therefore if `t!=s`, then `J_TJ_S^{-1}=O_K`, i.e. `J_T=J_S`, contradiction. Thus `t=s`. The converse is immediate. QED.

### Consequence

For a two-state ideal species, fixing a principalization residue is equivalent to fixing the witness composition count `t`.

This is an arithmetic selection rule, not a network optimization rule.

---

## 3. Residue-constrained purity bound

Now let the host be an even complete graph `K_k`, and let the two typed states be

\[
S=(P_s,Q_s),
\qquad
T=(P_t,Q_t).
\]

Write

\[
\phi_c(S),\qquad\phi_c(T),
\qquad c=k-1,
\]

for the local host scores of `WITNESS_PHASE_TRANSITION_LAW.md`.

Assume

\[
\boxed{\phi_c(T)>\phi_c(S).}
\]

Then by the purity theorem the unrestricted optimum is the pure phase `T^k`:

\[
\boxed{
H_{K_k}^{\rm free}
=\frac{k}{2}\phi_c(T).
}
\]

If a fixed residue is `R_t`, T10.19 forces exactly `t` vertices into state `T` and `k-t` into state `S`. The local incidence bound gives

\[
\boxed{
H_{K_k}(R_t)
\le
\frac12\bigl((k-t)\phi_c(S)+t\phi_c(T)\bigr).
}
\]

Therefore

\[
\boxed{
\Delta_{\rm res}(R_t)
\ge
\frac{k-t}{2}\bigl(\phi_c(T)-\phi_c(S)\bigr).
}
\]

For every interior composition

\[
0<t<k,
\]

the residue fiber excludes both pure phases and forces a genuinely mixed witness population.

If the mixed degree targets saturate the local incidence bound, the inequality is an equality.

### Interpretation

The unconstrained complete-host theory is pure, but arithmetic residue fibers slice that pure phase diagram into composition sectors. Interior residue sectors can therefore create **forced mixed phases** even though no mixed phase is energetically preferred without the residue constraint.

---

## 4. Exact laboratory in Q(sqrt(-15))

Work in

\[
K=Q(\sqrt{-15}),
\qquad
O_K=Z[\omega],
\qquad
\omega=\frac{1+\sqrt{-15}}2.
\]

Retain

\[
\mathfrak p=(2,\omega),
\qquad
\bar{\mathfrak p}=(2,1-\omega),
\]

with

\[
(2)=\mathfrak p\bar{\mathfrak p},
\qquad
\mathfrak p^2=(\omega),
\qquad
\bar{\mathfrak p}^{\,2}=(1-\omega).
\]

Let

\[
\mathfrak q=(23,\omega-7)
\]

be the nonprincipal prime ideal from `WITNESS_SWITCHING_GAIN.md`. Its two minimal witness orbits are represented by

\[
\alpha_S=2+3\omega,
\qquad
\alpha_T=7-\omega,
\]

with typed states

\[
S=(3,2),
\qquad
T=(6,1).
\]

### Proposition T10.20 — exact companion identification

\[
\boxed{
J_S=\mathfrak p,
\qquad
J_T=\bar{\mathfrak p}.
}
\]

### Proof

The witness `alpha_S=2+3omega` lies in `p`: modulo `p` one has `2=0` and `omega=0`. It also lies in `q` by construction. Since `p` and `q` lie over distinct rational primes, they are coprime, so

\[
(\alpha_S)\subseteq\mathfrak q\mathfrak p.
\]

Both ideals have norm `46`, hence equality:

\[
(\alpha_S)=\mathfrak q\mathfrak p.
\]

Therefore

\[
J_S=(\alpha_S)\mathfrak q^{-1}=\mathfrak p.
\]

Similarly, modulo `pbar` one has `omega=1` and `2=0`, so

\[
7-\omega\equiv6\equiv0\pmod{\bar{\mathfrak p}}.
\]

Again norms force

\[
(\alpha_T)=\mathfrak q\bar{\mathfrak p},
\]

hence

\[
J_T=\bar{\mathfrak p}.
\]

QED.

Since the class group has order two and `q` is nonprincipal, `q^8` is principal. For eight q-nodes, a configuration with `t` T-witnesses has residue

\[
\boxed{
R_t=\mathfrak p^{8-t}\bar{\mathfrak p}^{\,t}.
}
\]

The residues are pairwise distinct by T10.19.

In particular,

\[
R_0=\mathfrak p^8=(\omega^4),
\]

\[
\boxed{
R_4=\mathfrak p^4\bar{\mathfrak p}^{\,4}=(2)^4=(16),
}
\]

and

\[
R_8=\bar{\mathfrak p}^{\,8}=((1-\omega)^4).
\]

Thus the residue `(16)` forces exactly four S-states and four T-states.

---

## 5. Exact forced mixed phase on K8

Take host

\[
K_8
\]

and weights

\[
w_P=1,
\qquad
w_Q=2.
\]

For `c=7`,

\[
\phi_7(S)=3+2\cdot2=7,
\]

\[
\phi_7(T)=6+2\cdot1=8.
\]

Hence the unrestricted optimum is the pure T-phase:

\[
\boxed{
H_{K_8}^{\rm free}=\frac82\cdot8=32.
}
\]

Fix instead the residue

\[
\boxed{R_4=(16).}
\]

By residue/composition injectivity, every admissible witness assignment has exactly four T-nodes and four S-nodes.

The local incidence bound gives

\[
H_{K_8}(R_4)
\le
\frac12(4\cdot7+4\cdot8)
=30.
\]

This bound is attained.

Label T-vertices

\[
0,1,2,3
\]

and S-vertices

\[
4,5,6,7.
\]

Leave the four S-cycle edges unused:

\[
U=\{45,56,67,74\}.
\]

Take the Q-graph

\[
E_Q=\{04,15,26,37,46,57\}.
\]

Then every T-vertex has Q-degree `1`, and every S-vertex has Q-degree `2`.

Let `E_P` be the complement of `U union E_Q` in `K_8`. Then

- every T-vertex has P-degree `6`;
- every S-vertex has P-degree `3`;
- `|E_P|=18`;
- `|E_Q|=6`.

Therefore

\[
\boxed{
H_{K_8}(R_4)=18+2\cdot6=30.
}
\]

### Theorem T10.21 — residue-enforced mixed witness phase

For the principal ideal system `q^8`, fixed host `K_8`, and weights `(1,2)`:

\[
\boxed{
H^{\rm free}=32
}
\]

is attained by the pure phase `T^8`, but in the residue fiber

\[
R=(16)
\]

both pure phases are arithmetically forbidden and the exact optimum is the mixed phase

\[
\boxed{S^4T^4}
\]

with value

\[
\boxed{H(R)=30.}
\]

Hence

\[
\boxed{
\Delta_{\rm res}((16))=2.
}
\]

This realizes equality in the general lower bound

\[
\frac{k-t}{2}(\phi_T-\phi_S)
=
\frac42(8-7)=2.
\]

---

## 6. Conceptual consequence

There are now two different reasons for witness mixtures:

1. **free network optimization:** on even complete hosts, strict mixed phases are impossible by T10.17;
2. **arithmetic residue selection:** a fixed principalization residue can exclude all pure phases and force an interior composition.

Thus

\[
\boxed{
\text{mixed witness phase}
=
\text{arithmetic constraint}
+\text{network optimization inside the selected fiber}.
}
\]

The residue is therefore not passive metadata. It acts as a global arithmetic selection rule on the allowed witness population.

The term “superselection” may be used as an analogy only; the proved statement is the residue/composition injectivity and the resulting constrained optimization theorem above.

---

## 7. Prior-art boundary

The following ingredients are classical and are not claimed as new:

- unique prime-ideal factorization in Dedekind domains;
- the free-abelian structure of the fractional ideal group;
- ideal class groups and principal ideals.

The HATTER-SOL result is the composition of these classical facts with the witness-adaptive typed network model, producing a residue-indexed family of network optimization sectors and an exact example where an interior witness mixture is arithmetically forced.

---

## 8. Next target

The natural next step is the **residue-refined response polynomial**. Instead of projecting all witness configurations to a single ordinary response polynomial, retain the principal residue orbit as a formal label:

\[
\mathcal Z_K(A;X,Y;R)
\]

or equivalently an element of a group/monoid algebra over principal residue orbits.

The target is to prove:

1. a convolution law under multiplication of principal factor systems;
2. ordinary HATTER-SOL-10 response is recovered by forgetting the residue label;
3. residue-conditioned Pareto fronts can differ even when the ordinary front is identical.

This is the next theorem layer before publication audit.