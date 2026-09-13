# HATTER-SOL-10 · Exact uniform interaction law

Status: closed scalar baseline for interaction.

This file studies the one-channel specialization of the interaction functional from `INTERACTION_DEFECT.md`. It is used as a theorem-level baseline before returning to the full typed `(P,Q)` system.

## 1. Uniform block optimum

Let `k` vertices each have one-channel capacity `c>=0`. Define

\[
H_c(k):=\max\{|E(G)|:G\text{ simple on }k\text{ vertices},\ \Delta(G)\le c\}.
\]

### Theorem T10.12

\[
\boxed{
H_c(k)=\min\left\{\binom{k}{2},\left\lfloor\frac{kc}{2}\right\rfloor\right\}.
}
\]

### Proof

The two upper bounds are immediate from simplicity and the handshake lemma.

If `c>=k-1`, the complete graph attains `C(k,2)`.

If `c<k-1`, there exists a simple graph on `k` vertices with maximum degree at most `c` and exactly `floor(kc/2)` edges: when `kc` is even take a `c`-regular graph; when `kc` is odd, both `k` and `c` are odd and one may take a degree sequence with one vertex of degree `c-1` and the other `k-1` vertices of degree `c`, which has an almost-regular simple realization. QED.

Thus `k=c+1` is the exact transition between complete-support limitation and capacity limitation.

## 2. Exact interaction of two uniform blocks

Let block `A` have `n` vertices and block `B` have `m` vertices, all with the same capacity `c`. For scalar edge weight one, define

\[
\boxed{
\Gamma_c(n,m)
:=H_c(n+m)-H_c(n)-H_c(m).
}
\]

This is exactly the pure cross-interaction gain of `INTERACTION_DEFECT.md`.

### Theorem T10.13 — exact law

\[
\boxed{
\Gamma_c(n,m)
=
\min\left\{\binom{n+m}{2},\left\lfloor\frac{(n+m)c}{2}\right\rfloor\right\}
-
\min\left\{\binom n2,\left\lfloor\frac{nc}{2}\right\rfloor\right\}
-
\min\left\{\binom m2,\left\lfloor\frac{mc}{2}\right\rfloor\right\}.
}
\]

In particular `Gamma>=0`, as already follows abstractly from T10.10.

The formula separates two mechanisms.

## 3. Capacity-limited regime: pure parity interaction

Assume

\[
n\ge c+1,
\qquad
m\ge c+1.
\]

Then both separate systems and the union are capacity-limited, so

\[
\Gamma_c(n,m)
=
\left\lfloor\frac{(n+m)c}{2}\right\rfloor
-\left\lfloor\frac{nc}{2}\right\rfloor
-\left\lfloor\frac{mc}{2}\right\rfloor.
\]

Hence

\[
\boxed{
\Gamma_c(n,m)=
\begin{cases}
1,& nc\text{ and }mc\text{ are both odd},\\
0,&\text{otherwise}.
\end{cases}}
\]

Equivalently,

\[
\boxed{
\Gamma_c(n,m)=1
\iff
c,n,m\text{ are all odd}.
}
\]

Thus once both blocks are large enough to saturate their degree capacities internally, cross-system interaction disappears except for a single parity-repair edge.

This gives an exact zero-interaction criterion in the fully capacity-limited uniform regime.

## 4. Complete-support regime: geometric interaction

If

\[
n+m\le c+1,
\]

then each separate block and the union are complete-support limited. Therefore

\[
H_c(n+m)=\binom{n+m}{2},
\]

and

\[
H_c(n)=\binom n2,
\qquad
H_c(m)=\binom m2.
\]

Hence

\[
\boxed{
\Gamma_c(n,m)=nm.
}
\]

Every possible cross-edge is new usable capacity.

## 5. Mixed regime

Assume for example

\[
n\le c+1\le m.
\]

Then

\[
\boxed{
\Gamma_c(n,m)
=
\left\lfloor\frac{(n+m)c}{2}\right\rfloor
-inom n2
-\left\lfloor\frac{mc}{2}\right\rfloor.
}
\]

Equivalently,

\[
\boxed{
\Gamma_c(n,m)
=
\left\lfloor\frac{nc}{2}\right\rfloor
-inom n2
+\varepsilon,
}
\]

where

\[
\varepsilon=
\begin{cases}
1,&mc\text{ and }nc\text{ are both odd},\\
0,&\text{otherwise}.
\end{cases}
\]

The first term is the **geometric release** caused by giving the small block additional external neighbors; `epsilon` is the parity repair.

Since

\[
\frac{nc}{2}-\binom n2
=
\frac{n(c-n+1)}2,
\]

the geometric gain vanishes exactly at the transition `n=c+1` and grows as the small block becomes more neighbor-limited.

## 6. Interpretation

The interaction functional therefore has two conceptually distinct sources:

\[
\boxed{
\text{interaction}
=
\text{neighbor-space release}
+
\text{parity repair}
}
\]

in the uniform one-channel model.

The first is geometric/combinatorial; the second is arithmetic parity of the degree budget.

This distinction is useful for HATTER-SOL-10 because witness-adaptive ideal nodes can change capacities without changing the number of factor vertices, while ideal multiplication can also change the available cross-neighbor space.

## 7. Relation to connected boundary

For `c>=2` and block size at least two, the maximizing almost-regular graphs above may be chosen connected except in trivial small cases. In those regimes the connectivity penalties `kappa` of `INTERACTION_DEFECT.md` vanish, so `Gamma_c` passes directly to boundary release:

\[
\lambda^c(A\cup B)-\lambda^c(A)-\lambda^c(B)=-2\Gamma_c(n,m).
\]

Where a separate block has no connected realization, `Gamma_c` remains well-defined because its definition intentionally uses the unconstrained utilization problem.

## 8. Next target

Lift the exact uniform law to typed capacities `(P,Q)`. The first goal is not a full closed formula but a rigorous decomposition of interaction into:

1. total neighbor-space release;
2. P/Q competition on cross pairs;
3. parity repair;
4. witness-switching gain specific to nonprincipal ideal nodes.

The last term has no analogue in the scalar uniform model and is the genuinely new HATTER-SOL-10 phenomenon to isolate.