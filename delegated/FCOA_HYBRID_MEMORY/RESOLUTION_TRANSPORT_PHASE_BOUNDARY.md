# FCOA Hybrid Memory — Resolution–Transport Phase Boundary

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate in the flat sparse-channel normal form; proofs included; not claimed as an architecture-independent invariant of all possible FCOA encodings

## 1. Problem

The previous strikes established

\[
\operatorname{Cost}(AL0)=\Theta(N),\qquad
\operatorname{Cost}(AL1)=\Theta(N),\qquad
\operatorname{Cost}(AL2)=\Theta(N)
\]

in the auxiliary-carrier bounded-arity model.

Hence raw cell count does not separate the leakage levels. We now ask which resource parameter does.

## 2. Negative result: the obvious parameters fail

The balanced sparse realizations of all three levels can be arranged so that:

- total operation cells are `Theta(N)`;
- total auxiliary carriers after incidence compilation are `Theta(N)`;
- maximum Gaifman degree is `Theta(sqrt N)`;
- the recovering FO formulas have constant quantifier rank independent of `N`.

Thus none of these asymptotic scalars separates AL0, AL1, AL2.

### Why maximum degree does not separate

For AL0, the balanced `sqrt N x sqrt N` coordinate scaffold has coordinate/threshold vertices of degree `Theta(sqrt N)`.

For AL1, take residue channels of size `Theta(sqrt N)` and encode each local addition-table entry by an entry node. A residue value occurs in `Theta(sqrt N)` table entries, so maximum degree is again `Theta(sqrt N)`.

For AL2, the four prime residue channels of size `Theta(sqrt N)` have the same degree scale under the multiplication-table incidence encoding.

Hence

\[
\boxed{\Delta_{AL0}\asymp\Delta_{AL1}\asymp\Delta_{AL2}\asymp\sqrt N.}
\]

This is compatible with the earlier bounded-degree order wall: unbounded degree is necessary for AL0, but its growth exponent does not distinguish the higher AL levels.

## 3. Flat sparse-channel normal form

A **flat channel presentation** of an `N`-point target sector `X_N` consists of:

1. finitely many auxiliary channel sorts `C_1,...,C_k`;
2. channel cardinalities
   \[
   |C_i|=m_i;
   \]
3. coordinate maps
   \[
   \rho_i:X_N\to C_i;
   \]
4. on each channel, a fixed bounded-arity local law whose full binary functional table costs `Theta(m_i^2)` records;
5. no recursive compression inside a local table.

The last clause is essential: the theorem below concerns the primitive flat presentation, not a hierarchically recompiled one.

## 4. Resolution exponent

Define the **joint resolution product**

\[
R_N:=\prod_{i=1}^k m_i.
\]

Define its exponent

\[
\rho:=\limsup_{N\to\infty}\frac{\log R_N}{\log N}.
\]

Thus `rho=1` means the joint channels distinguish a range on the scale `N`; `rho=2` means they distinguish a range on the scale `N^2`.

This quantity is more stable than raw channel count: splitting or merging constant-many comparable channels may change `k` without changing the total resolution exponent.

## 5. Linear-table capacity theorem

### Theorem HM-RT-CAP

Suppose a flat `k`-channel presentation has total complete local-table cost

\[
\sum_{i=1}^k m_i^2\le C N
\]

for a fixed constant `C`. Then

\[
R_N=\prod_{i=1}^k m_i
\le
\left(\frac{CN}{k}\right)^{k/2}.
\]

In particular

\[
\rho\le \frac{k}{2}.
\]

### Proof

By AM-GM applied to `m_1^2,...,m_k^2`,

\[
\left(\prod_{i=1}^k m_i^2\right)^{1/k}
\le
\frac1k\sum_{i=1}^k m_i^2
\le
\frac{CN}{k}.
\]

Raising to the `k/2` power gives

\[
\prod_{i=1}^k m_i
\le
\left(\frac{CN}{k}\right)^{k/2}.
\]

`□`

## 6. Defect exponent and CRT exactness

Consider a target relation whose correctness can be written as

\[
E_N(\bar x,z)=0,
\]

where every candidate tuple in the target range satisfies

\[
|E_N(\bar x,z)|=O(N^d).
\]

Call `d` the **defect exponent** of this direct congruence test.

If the relation is checked by requiring

\[
E_N(\bar x,z)\equiv0\pmod{m_i}
\]

in every pairwise-coprime channel, exactness requires the product modulus to dominate the possible nonzero defect:

\[
R_N>cN^d.
\]

Hence necessarily

\[
\rho\ge d.
\]

Combining with HM-RT-CAP gives the flat-channel lower bound

\[
\boxed{k\ge 2d}
\]

for linear complete-table cost.

For fixed integer `d`, the bound is attained asymptotically by `2d` pairwise-coprime channels of size `Theta(sqrt N)`.

## 7. Addition

For exact truncated addition,

\[
E_+(x,y,z)=x+y-z.
\]

On `0\le x,y,z<N`,

\[
|E_+|=O(N),
\]

so

\[
d_+=1.
\]

Therefore exact CRT addition needs resolution exponent

\[
\rho\ge1.
\]

The two-modulus construction attains

\[
\rho=1
\]

with linear cost.

## 8. Multiplication

For exact truncated multiplication,

\[
E_\times(x,y,z)=xy-z.
\]

On the same target range,

\[
|E_\times|=O(N^2),
\]

so

\[
d_\times=2.
\]

Therefore direct CRT multiplication needs

\[
\rho\ge2.
\]

The four-`sqrt N`-channel construction attains

\[
\rho=2
\]

with linear cost.

Thus the real difference between additive and multiplicative CRT memory is not the total number of cells, but the **range of collisions that the joint channel code must destroy**.

## 9. Why channel count alone is not intrinsic

The flat model gives:

\[
\text{addition: }k=2,
\qquad
\text{multiplication: }k=4.
\]

But `k` is not an architecture-independent invariant. A large channel can itself be represented by a sparse hierarchy of smaller channels, or a channel can be split into tagged subchannels.

Therefore the robust content of the flat theorem is not literally “2 versus 4 channels”. It is

\[
\boxed{\rho_+=1,\qquad \rho_\times=2.}
\]

Channel count is merely one implementation of that resolution requirement.

## 10. Resolution does not separate AL0 from AL1

The exact-AL0 coordinate grid also has joint coordinate capacity

\[
|B|\cdot|P|=N,
\]

hence

\[
\rho_{AL0}=1.
\]

So resolution exponent alone gives

\[
AL0: \rho=1,
\qquad
AL1: \rho=1,
\qquad
AL2: \rho=2.
\]

A second parameter is necessary.

## 11. Transport grade

We therefore grade the **local semantic law** carried by the channels.

### Grade 0 — comparison coordinates

The channel supplies only rigid comparison/threshold geometry sufficient to compare coordinates. It does not supply a cancellative displacement law.

This is the sparse exact-AL0 construction.

### Grade 1 — additive transport

The channel carries a uniform cancellative additive law, such as cyclic addition, allowing equality of displacements to be tested after CRT synchronization.

This is the AL1 layer.

### Grade 2 — bilinear/ring transport

The channel additionally carries multiplication compatible with the residue representation, allowing quadratic defects to be tested.

This is the AL2 layer.

Denote this local-law grade by `tau`.

This grading is a normal-form semantic parameter, not yet claimed to be invariant under arbitrary definitional reinterpretations.

## 12. Resolution–Transport Profile

Define

\[
\boxed{RTP=(\rho,\tau).}
\]

For the sparse normal forms constructed in this branch:

\[
\boxed{
AL0=(1,0),\qquad
AL1=(1,1),\qquad
AL2=(2,2).
}
\]

This separates all three levels while raw `Theta(N)` memory does not.

The two phase transitions are therefore qualitatively different.

### AL0 -> AL1

No extra asymptotic resolution is required:

\[
(1,0)\to(1,1).
\]

The transition is **semantic**: absolute coordinates acquire a displacement/translation law.

### AL1 -> AL2

Both components increase:

\[
(1,1)\to(2,2).
\]

The channels must now resolve a quadratic error range and support a bilinear law.

## 13. General polynomial consequence

Let `P` be any fixed integer polynomial of total degree `d` in a fixed number of variables, and consider the truncated graph

\[
z=P(\bar x),
\qquad \bar x,z<N.
\]

A direct CRT verifier has defect

\[
E=P(\bar x)-z=O(N^d).
\]

Therefore `2d` primitive `Theta(sqrt N)` channels suffice to recover the exact graph using only `Theta(N)` total complete-table memory, provided the modular evaluation law of `P` is available in each channel.

Hence there is **no superlinear cell wall for any fixed polynomial degree** in this flat channel architecture; increasing degree is paid for by a larger constant number of channels / larger resolution exponent, not by a larger exponent of `N`.

This suggests that the first genuine superlinear wall, if one exists under the current permissive auxiliary-carrier model, must involve one of:

- unbounded algebraic degree;
- a restriction on the number of primitive channels;
- a restriction on auxiliary carrier growth;
- a restriction forbidding hierarchical channel compilation;
- or a logical task whose ambiguity range cannot be bounded by `N^d` for fixed `d`.

## 14. Interpretation

The resource hierarchy is therefore not

\[
N<N^{1+\epsilon}<N^2.
\]

Instead, at fixed linear memory it is a hierarchy of **what the channels know how to do** and **how much collision range their joint code resolves**:

\[
\boxed{
\text{comparison geometry}
\to
\text{transport geometry}
\to
\text{bilinear transport geometry}.
}
\]

The cell exponent stays equal to one throughout.

## 15. Status

What is proved here:

1. raw linear cell count does not separate the three exhibited AL levels;
2. maximum degree, auxiliary count and asymptotic quantifier rank do not separate the exhibited balanced realizations;
3. in the flat complete-table channel normal form, the AM-GM capacity bound is exact at the exponent level;
4. addition has defect exponent `1`, multiplication defect exponent `2`;
5. the Resolution–Transport Profile separates the three constructed sparse normal forms.

What is **not** yet claimed:

- that `(rho,tau)` is invariant under every possible FCOA interpretation;
- that no exotic non-CRT skeleton can realize AL2 with a different profile;
- that four channels are absolutely minimal outside the flat complete-table normal form.

The next hostile-audit target is therefore clear:

\[
\boxed{\text{Can RTP be made interpretation-invariant, or can an exotic encoding collapse }(2,2)\text{ to }(1,*)?}
\]
