# HATTER-SOL-14 · Infinite Equivariant Homology Separation

**Status:** exact theorem layer / publication-level positive result

## 1. Arithmetic subsequence

Let

\[
k\equiv 15\pmod{30}.
\]

Then `k` is odd and divisible by `15`. Therefore

\[
7=2^3-1\mid 2^k-1,
\qquad
31=2^5-1\mid 2^k-1.
\]

Write

\[
m_k=2^k-1,
\qquad
\Gamma_k=(\mathbb Z/m_k\mathbb Z)^\times/\langle2\rangle.
\]

Because `k` is odd, the cyclic subgroup `<2>` has odd order. Hence quotienting by `<2>` does not alter the 2-primary direct factor of the unit group.

The CRT factors at the prime powers above `7` and `31` contribute

\[
(\mathbb Z/7^a\mathbb Z)^\times_{(2)}\cong C_2,
\qquad
(\mathbb Z/31^b\mathbb Z)^\times_{(2)}\cong C_2,
\]

because `v_2(7-1)=v_2(31-1)=1`.

Therefore for every `k=15 mod 30` there is a direct decomposition

\[
\boxed{\Gamma_k\cong C_2\oplus C_2\oplus H_k}
\]

for some finite abelian group `H_k`.

Let `a,c` denote the two standard nonzero basis involutions in the displayed `C_2^2` factor.

## 2. Small inverse-closed generating sets for `H_k`

The unit group modulo `m_k` is a product of at most `omega(m_k)` cyclic prime-power unit groups. Hence

\[
d(H_k)\le d(\Gamma_k)\le \omega(m_k),
\]

where `d(A)` is the minimum number of generators of a finite abelian group `A`.

Choose a generating set of `H_k` with at most `omega(m_k)` elements and symmetrize it under inversion. This gives an inverse-closed generating set `R_k` satisfying

\[
|R_k|\le 2\omega(m_k).
\]

The standard elementary bound

\[
\omega(N)=O\!\left(\frac{\log N}{\log\log N}\right)
\]

implies, for `N=m_k=2^k-1`,

\[
\omega(m_k)=O\!\left(\frac{k}{\log k}\right)=o(k).
\]

Consequently

\[
|R_k|+2\le k
\]

for all sufficiently large `k` in the progression `15 mod 30`.

Thus the carriers below are HATTER-capacity feasible for infinitely many `k`.

## 3. Two isomorphic equivariant carriers

Define

\[
S_{k,1}=R_k\cup\{a,c\},
\qquad
S_{k,2}=R_k\cup\{a+c,c\}.
\]

Both are inverse-closed and generate `Gamma_k`, hence define connected Galois-equivariant carriers

\[
C_{k,i}=\operatorname{Cay}(\Gamma_k,S_{k,i}).
\]

They have the same degree

\[
d_k=|R_k|+2,
\]

the same vertex count `n_k=|Gamma_k|`, and the same HATTER boundary

\[
B_f=n_k(k-d_k).
\]

Define an automorphism `phi_k` of `Gamma_k` by

\[
\phi_k(a)=a+c,
\qquad
\phi_k(c)=c,
\qquad
\phi_k|_{H_k}=\operatorname{id}.
\]

Then

\[
\phi_k(S_{k,1})=S_{k,2}.
\]

Therefore

\[
\boxed{C_{k,1}\cong C_{k,2}}
\]

as abstract graphs. In particular, every ordinary graph invariant, including orientable genus, is identical for the two carriers.

## 4. Equivariant first homology separates them

By Theorem H14.12, the rational equivariant cycle-space character remembers exactly which involutions occur in the connection set.

The set `S_{k,1}` contains `a`, whereas `S_{k,2}` does not contain `a`. Since `R_k` lies in the direct factor `H_k`, none of its elements equals `a`.

Hence at the group element `a`,

\[
\chi_{H_1(C_{k,1};\mathbb Q)}(a)=1-\frac{n_k}{2},
\]

while

\[
\chi_{H_1(C_{k,2};\mathbb Q)}(a)=1.
\]

Thus

\[
\boxed{
H_1(C_{k,1};\mathbb Q)
\not\cong
H_1(C_{k,2};\mathbb Q)
}
\]

as `Q[Gamma_k]`-modules.

## Theorem H14.14 — infinite same-graph homology separation

For infinitely many arithmetic worlds, namely all sufficiently large

\[
\boxed{k\equiv15\pmod{30}},
\]

there exist two connected simple capacity-feasible Galois-equivariant HATTER carriers that have

- the same arithmetic world;
- the same vertex set size;
- the same degree;
- the same scalar boundary;
- the same abstract graph isomorphism type;
- hence the same ordinary orientable genus;

but have non-isomorphic rational equivariant first-homology modules.

Therefore

\[
\boxed{
\text{abstract carrier geometry + scalar boundary}
\;<\;
\text{arithmetic-action-aware homological memory}
}
\]

for an infinite family of HATTER worlds.

## Claim boundary

The theorem does not say that the abstract graph has different ordinary homology: the abstract graphs are isomorphic, so their ordinary `H_1` groups agree. The additional information is specifically the retained `Gamma_k` action on the cycle space.

This is the first H14 theorem that survives both scalar and ordinary-topological quotienting and therefore crosses the intended structural threshold for a serious publication candidate.