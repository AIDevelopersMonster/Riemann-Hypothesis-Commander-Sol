# FCOA Rigidity Cost — Orbit–Killing Duality at Beta One

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication structural theorem.

## 1. Setup
Assume `beta(D,c)=1` and write

\[
A^+(D,c)
\]

for the old globally color-preserving automorphism group. Let

\[
W_{anch}
\]

be the anchored beta-killing missing cells.

For `e in W_anch`, put

\[
S_e=D\cup\{e\},
\]

\[
\Gamma_e=\operatorname{Aut}(G;S_e),
\]

\[
A_e=\{a\in\operatorname{Aut}(G;D):a(e)=e\},
\]

and

\[
H_e=\{a\in A^+(D,c):a(e)=e\}.
\]

Thus `H_e` is the stabilizer of `e` in the old phase-0 group.

Define the exact replacement-transporter capacity

\[
\boxed{
\tau(e)=\frac{|\Gamma_e|-|A_e|}{|H_e|}.
}
\]

Since `H_e <= A_e <= Gamma_e`, this is a nonnegative integer.

Using

\[
|P(e)|=[\Gamma_e:A_e]-1
\]

and

\[
s(e)=[A_e:H_e],
\]

we have the exact factorization

\[
\boxed{\tau(e)=|P(e)|s(e).}
\]

It is the exact number of non-D-preserving `H_e`-cosets available in the singleton domain automorphism group.

## 2. A^+-invariance of the killing set

### Lemma 2.1
The set `W_anch` is invariant under `A^+(D,c)`.

### Proof
Let `a in A^+`. Conjugation by `a` preserves the old ternary reduct, preserves global phase 0, and carries old bad automorphisms to old bad automorphisms. A missing cell `e` kills every old bad automorphism iff `ae` kills every conjugate old bad automorphism. Anchoring is preserved because `a` is an automorphism of the old incidence graph. Hence `aW_anch=W_anch`. `square`

Therefore `W_anch` is a disjoint union of `A^+`-orbits.

## 3. Capacity is constant on killing orbits

### Lemma 3.1
If `e' = ae` for some `a in A^+`, then

\[
|H_{e'}|=|H_e|,
\qquad
|A_{e'}|=|A_e|,
\qquad
|\Gamma_{e'}|=|\Gamma_e|,
\]

and hence

\[
\boxed{\tau(e')=\tau(e).}
\]

### Proof
Conjugation by `a` identifies the singleton domains `D union {e}` and `D union {ae}` and conjugates the corresponding stabilizer groups. `square`

Thus each `A^+`-orbit `O subseteq W_anch` has a well-defined capacity `tau(O)`.

## 4. Orbit budget identity

Let

\[
O=A^+\cdot e
\]

be one anchored killing orbit. Orbit-stabilizer gives

\[
|O|=\frac{|A^+|}{|H_e|}.
\]

The total number of non-D-preserving singleton-domain transporter permutations over all cells of `O` is therefore

\[
\sum_{f\in O}(|\Gamma_f|-|A_f|)
=|O|(|\Gamma_e|-|A_e|)
=|A^+|\tau(O).
\]

Hence:

### Theorem 4.1 — Orbit Transporter Budget
For every anchored beta-killing orbit `O`,

\[
\boxed{
N_{tr}(O)=|A^+|\tau(O).
}
\]

The remarkable point is that the orbit size cancels completely.

## 5. Fatality consumes two units of orbit capacity

Persistent Exclusion proves that one replacement `H_e`-coset cannot be bad for both binary colors of an anchored beta-killing cell.

Therefore if `e` is fatal for both colors, at least two distinct non-D-preserving `H_e`-cosets are required. Equivalently,

\[
\boxed{\tau(e)\ge2.}
\]

Since `tau` is constant on `A^+`-orbits:

### Corollary 5.1
If every cell in an anchored killing orbit `O` is fatal, then

\[
\boxed{
N_{tr}(O)\ge2|A^+|.
}
\]

Thus every fully fatal `A^+`-orbit consumes at least two complete `A^+`-cosets of transporter budget, regardless of the number of cells in the orbit.

## 6. Global orbit-count criterion

Let

\[
\nu_+(W_{anch})
\]

be the number of `A^+`-orbits contained in `W_anch`.

Define the exact anchored transporter budget

\[
N_{tr}(W_{anch})
=
\sum_{e\in W_{anch}}
(|\Gamma_e|-|A_e|).
\]

### Theorem 6.1 — Orbit–Killing Duality
If

\[
\boxed{
N_{tr}(W_{anch})
<
2|A^+|\,\nu_+(W_{anch}),
}

then at least one anchored beta-killing orbit is not fatal. Therefore one binary color on some anchored beta-killing cell gives an exact singleton repair, and

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

### Proof
If every anchored killing cell were fatal, Corollary 5.1 would contribute at least `2|A^+|` transporter permutations per `A^+`-orbit. Summing over the `nu_+` orbits gives the opposite inequality. `square`

This is the exact orbit-normalized form of the Replacement Capacity Bound.

## 7. Shell relaxation

Let

\[
A=\operatorname{Aut}(G;D).
\]

Every transporter counted in `N_tr(W_anch)` has defect one relative to `D`. The total number of defect-one carrier permutations is

\[
|A|\,|\mathcal O_1(D)|.
\]

Not every defect-one permutation preserves a singleton union `D union {e}`, so in general only the upper bound

\[
\boxed{
N_{tr}(W_{anch})
\le
|A|\,|\mathcal O_1(D)|
}
\]

is valid.

Hence a coarser sufficient criterion is

\[
\boxed{
|A|\,|\mathcal O_1(D)|
<
2|A^+|\,\nu_+(W_{anch})
\Longrightarrow
\alpha=\beta=1.
}
\]

This corrects the temptation to identify the raw defect-one shell with the exact singleton transporter budget.

## 8. Killing scarcity forces fixed-point mass

From the exact singleton survival formula

\[
W_{anch}=M_{anch}\setminus
\bigcup_{g\in B_{old}}(S_g\cap M_{anch}),
\]

we obtain

\[
|M_{anch}|-|W_{anch}|
\le
\sum_{g\in B_{old}}|S_g\cap M_{anch}|.
\]

Thus if `W_anch` is unusually small, the old bad automorphisms must collectively carry unusually large fixed-cell mass on the anchored missing-cell set.

In particular, if `B_old` is nonempty, then some `g in B_old` satisfies

\[
\boxed{
|S_g\cap M_{anch}|
\ge
\frac{|M_{anch}|-|W_{anch}|}{|B_{old}|}.
}
\]

Since every fixed ordered cell uses two carrier fixed points,

\[
|S_g|\le f(g)(f(g)-1),
\]

where `f(g)` is the number of fixed carrier points of `g`. Therefore a beta-one counterexample with very small `W_anch` forces at least one old bad automorphism with a large carrier fixed set.

This is the second half of the duality:

\[
\boxed{
\text{small killing set}
\Longrightarrow
\text{large old-bad fixed-point mass}.}
\]

## 9. Quantitative trichotomy for a beta-one counterexample

If

\[
\beta=1<\alpha,
\]

then all of the following must hold simultaneously:

1. **replacement budget condition**
   \[
   N_{tr}(W_{anch})
   \ge
   2|A^+|\nu_+(W_{anch});
   \]
2. **shell relaxation**
   \[
   |A||\mathcal O_1(D)|
   \ge
   2|A^+|\nu_+(W_{anch});
   \]
3. **killing scarcity/fixed-point condition**
   \[
   \max_{g\in B_{old}}|S_g\cap M_{anch}|
   \ge
   \frac{|M_{anch}|-|W_{anch}|}{|B_{old}|};
   \]
4. every anchored killing orbit has exact local capacity
   \[
   \tau(O)\ge2;
   \]
5. all isolated beta-killing cells, if any, must have both color states trapped by isolated phase or replacement mechanisms.

Thus a counterexample needs **large replacement mobility and large old-bad fixed-point rigidity at the same time**.

These demands pull the domain in opposite geometric directions: defect-one mobility requires many near-isomorphic replacements, whereas scarcity of killing cells requires many missing ordered cells to be fixed by old bad symmetries.

This incompatibility is the precise content of the Orbit–Killing Duality programme.

## 10. Phase-clean corollary

If

\[
A=A^+,
\]

then the shell criterion reduces to

\[
\boxed{
|\mathcal O_1(D)|
<2\nu_+(W_{anch})
\Longrightarrow
\alpha=\beta=1.
}
\]

This can be much sharper than counting individual missing cells when the killing set decomposes into many symmetry orbits.

## 11. Next target

The remaining global step is to exploit the tension in Section 9. Two promising routes are:

1. prove that a large fixed-point mass for old bad symmetries forces the defect-one shell `O_1(D)` to collapse;
2. prove that a large defect-one shell forces `W_anch` to split into many `A^+`-orbits, raising the right-hand side of the orbit-budget inequality.

Either statement, even with explicit constants on a broad class, would turn the current sufficient criterion into a structural theorem.

## Claim firewall

1. The exact transporter budget is `N_tr`, not the raw number of all defect-one permutations.
2. The shell bound is only an upper bound on the exact transporter budget.
3. The orbit-budget theorem concerns anchored beta-killing cells.
4. The fixed-point statement is a necessary consequence of a small killing set, not by itself a contradiction.
5. The global theorem `beta=1 => alpha=1` remains open.
