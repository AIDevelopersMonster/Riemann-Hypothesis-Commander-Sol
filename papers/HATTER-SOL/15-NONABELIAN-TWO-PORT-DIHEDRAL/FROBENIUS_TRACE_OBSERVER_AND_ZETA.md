# HATTER-SOL-15 · Frobenius Trace Observer and the Dedekind Zeta Function

**Status:** exact arithmetic/analytic bridge

Let `L/Q` be a finite Galois extension with group `G`, let `H<=G`, and let

\[
K=L^H.
\]

Let `X=H\backslash G` be the corresponding transitive permutation set and let

\[
\rho_X:G\to\operatorname{GL}(\mathbb C[X])
\]

be the permutation representation, with character

\[
\chi_X(g)=\#\operatorname{Fix}_X(g).
\]

For an unramified rational prime `q`, let `F_q` denote a Frobenius element, understood up to conjugacy.

## Theorem H15.17 — fixed-sector count is the permutation trace

The observer

\[
\boxed{O_m(q):=\#\operatorname{Fix}_X(F_q^m)}
\]

satisfies

\[
\boxed{O_m(q)=\chi_X(F_q^m)=\operatorname{Tr}(\rho_X(F_q)^m).}
\]

This quantity is canonical because `chi_X` is a class function.

If the residue degrees of the prime ideals of `K` above `q` are

\[
f_1,\ldots,f_g,
\]

then the Frobenius permutation has cycle lengths `f_1,...,f_g`, and hence

\[
\boxed{
O_m(q)=\sum_{j:\,f_j\mid m} f_j.
}
\]

### Proof

The first equality is the defining property of a permutation character. For the second formula, a cycle of length `f_j` contributes all `f_j` of its points to the fixed set of the `m`-th power exactly when `f_j|m`, and otherwise contributes none. QED.

## Theorem H15.18 — observer response sequence determines the local Euler factor

For an unramified prime `q`, the local Euler factor of the Dedekind zeta function of `K` is

\[
Z_q(T):=\prod_{j=1}^{g}(1-T^{f_j})^{-1},
\qquad T=q^{-s}.
\]

It satisfies the exact identity

\[
\boxed{
\log Z_q(T)
=
\sum_{m\ge1}\frac{O_m(q)}{m}T^m.
}
\]

Equivalently,

\[
\boxed{
Z_q(T)
=
\exp\left(\sum_{m\ge1}\frac{O_m(q)}{m}T^m\right).
}
\]

### Proof

Expand each factor:

\[
-\log(1-T^{f_j})
=\sum_{n\ge1}\frac{T^{nf_j}}n.
\]

The coefficient of `T^m` after summing over `j` is

\[
\frac1m\sum_{j:f_j|m}f_j
=\frac{O_m(q)}m.
\]

QED.

Thus the complete local Euler factor is exactly the exponential generating transform of the repeated Frobenius fixed-sector responses.

## Corollary H15.19 — first observer response in the dihedral degree-p world

Now specialize to

\[
G=D_{2p},
\qquad
H=\langle s\rangle,
\qquad
|X|=p.
\]

The permutation character on `X` is

\[
\boxed{
\chi_X(g)=
\begin{cases}
p,&g=1,\\
0,&g\in C_p\setminus\{1\},\\
1,&g\text{ is a reflection}.
\end{cases}}
\]

Therefore the single response

\[
O_1(q)=\#\operatorname{Fix}(F_q)
\]

already distinguishes the three unramified splitting regimes:

\[
\boxed{
\begin{array}{c|c|c}
F_q & O_1(q) & \text{splitting type in }K\\
\hline
1 & p & 1^p\\
\text{nontrivial rotation} & 0 & p\\
\text{reflection} & 1 & 1\,2^{(p-1)/2}
\end{array}}
\]

Thus the coarse H15 port observer is not merely analogous to arithmetic splitting: its output is the permutation-character trace of Frobenius.

## Corollary H15.20 — the fixed prime 2 reflection sequence

In the H15 infinite family where the fixed prime `2` has reflection Frobenius,

\[
F_2^m=
\begin{cases}
F_2,&m\text{ odd},\\
1,&m\text{ even}.
\end{cases}
\]

Hence

\[
\boxed{
O_m(2)=
\begin{cases}
1,&m\text{ odd},\\
p,&m\text{ even}.
\end{cases}}
\]

and therefore

\[
\boxed{
Z_2(T)
=(1-T)^{-1}(1-T^2)^{-(p-1)/2}.
}
\]

This is exactly the local factor corresponding to one degree-one prime and `(p-1)/2` degree-two primes above `2`.

## 5. Artin formalism interpretation

The permutation representation is

\[
\mathbb C[X]\cong\operatorname{Ind}_H^G\mathbf1.
\]

By Artin induction/formalism,

\[
L(s,\rho_X)=\zeta_K(s).
\]

At every unramified prime, the local Artin factor is

\[
\det(1-\rho_X(F_q)q^{-s})^{-1},
\]

and its logarithm is governed by the same traces `O_m(q)` above.

Hence the exact bridge is

\[
\boxed{
\text{Frobenius sector observer}
\longleftrightarrow
\text{permutation character}
\longleftrightarrow
\text{local Euler factor}
\longleftrightarrow
\zeta_K(s).
}
\]

## 6. Claim boundary

The trace/Euler-factor identity and Artin formalism are classical. H15 does **not** claim them as new representation theory or analytic number theory.

The H15-specific contribution is the structural synthesis with the fixed-prime two-port model:

- the same sectors are arithmetic prime-decomposition branches;
- their non-abelian two-port action supplies synchronization and path-order observables;
- the Frobenius fixed-sector observer is simultaneously a local network response and an exact zeta-function trace datum.

This is a genuine bridge to analytic number theory, but by itself it gives no new zero-free region and no progress on RH/GRH.