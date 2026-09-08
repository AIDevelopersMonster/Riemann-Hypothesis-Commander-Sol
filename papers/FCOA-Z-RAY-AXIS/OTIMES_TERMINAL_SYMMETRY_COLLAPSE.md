# FCOA-Z — Terminal `E*` Symmetry and Cross-Operation Collapse

Status: theorem package v0.1  
Date: 2026-08-31

This note continues the FCOA-Z mixed-memory line by returning to the second legacy operation `otimes`.

The motivating question was whether the terminal right-zero outputs

\[
x\otimes x_0\in E^*
\]

carry an intrinsic transport group larger than the `C_2` reflection phase found for `oplus`.

The answer depends sharply on the reduct.

- In the symmetry-rich `otimes` reduct alone, the terminal outputs inherit large symmetric/wreath-product actions and non-Abelian transport symmetry appears on finite truncations.
- In the combined FCOA-Z reduct, the radial memory already present in `oplus` labels depth and collapses the `otimes` terminal symmetry back to at most `C_2`.
- If the base carrier is fixed pointwise, the terminal port has no independent symmetry at all: every `E*` output is anchored by its source cell.

Thus the second operation does contain latent non-Abelian symmetry, but it is not an independent terminal phase of the full FCOA-Z axis.

---

## 1. FCOA framework and concrete reduct

The ambient framework is FCOA Definition 1.0:

A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026, DOI `10.5281/zenodo.22164246`.

We use a finite signed truncation

\[
X_N=\{x_0,x_{\pm1},x_{\pm2},\ldots,x_{\pm N}\},\qquad N\ge2.
\]

The `otimes` legacy rules used below are exactly the signed/reflected copies of the M0 rules needed to distinguish the two same-sign sectors:

1. left absorption:

\[
x_0\otimes x=x_0\qquad(x\neq x_0);
\]

2. right-zero terminal port:

\[
x_{\pm n}\otimes x_0=E^*_{\pm n}\qquad(n\ge2)
\]

in the split-fiber convention, or

\[
x_{+n}\otimes x_0=x_{-n}\otimes x_0=E^*_n
\]

in the shared-fiber convention;

3. same-sign local units:

\[
x_{+1}\otimes x_{+n}=x_{+n}\otimes x_{+1}=x_{+n},
\]

\[
x_{-1}\otimes x_{-n}=x_{-n}\otimes x_{-1}=x_{-n}
\]

for `n>=2`;

4. all mixed-sign generic cells are left outside the present reduct.

The standard same-sign diagonal `E^times` cells may be adjoined with the corresponding split/shared indexing; they do not alter the group calculations below when indexed coherently with the same source labels.

Let

\[
m=N-1
\]

be the number of generic depths `2,...,N` on each side.

---

## 2. Three notions of terminal symmetry

It is essential to separate three different automorphism questions.

### 2.1 Bare terminal-sort symmetry

If the sort `E*` is viewed in isolation, with no relation back to its source cells, it is a pure set. Its automorphism group is therefore the full symmetric group on that set.

This is not an intrinsic FCOA transport symmetry; it is only anonymous relabelling.

### 2.2 Anchored terminal symmetry

The right-zero port defines a source-output relation

\[
\theta(x)=x\otimes x_0.
\]

An automorphism of the full port structure must satisfy

\[
h_{E^*}(\theta(x))=\theta(h_X(x)).
\]

The output permutation is therefore constrained by the source action.

### 2.3 Relative terminal symmetry

If the base sort is fixed pointwise, then `theta` fixes every terminal output appearing in the port.

This gives the first rigidity theorem.

---

## 3. Terminal Anchor Theorem

### Theorem 3.1

In either the split-fiber or shared-fiber convention, every sort-preserving automorphism of the signed right-zero port that fixes the base carrier `X_N` pointwise fixes the reachable terminal sort `E*` pointwise.

Equivalently,

\[
\boxed{\operatorname{Aut}_{X_N}(E^*,\theta)=1.}
\]

#### Proof

Every terminal element in the declared `E*` port is the value of at least one inherited source cell.

For a split terminal element `E^*_{\pm n}`,

\[
E^*_{\pm n}=x_{\pm n}\otimes x_0.
\]

If `h_X=id`, operation preservation gives

\[
h(E^*_{\pm n})
=h(x_{\pm n}\otimes x_0)
=x_{\pm n}\otimes x_0
=E^*_{\pm n}.
\]

For a shared terminal element `E^*_n`, the same argument applies using either source `x_{+n}` or `x_{-n}`. Hence every reachable terminal is fixed. □

### Consequence

There is **no independent terminal gauge group** in the inherited port once source points are held fixed.

Any nontrivial `E*` symmetry must co-move source labels.

---

## 4. `otimes`-only split-fiber automorphism group

Let the two terminal copies be distinct:

\[
E^*_{+,n}\neq E^*_{-,n}.
\]

### Theorem 4.1 — Split Wreath Symmetry

For the finite signed `otimes` reduct described above,

\[
\boxed{
\operatorname{Aut}(\mathcal T^{\rm split}_N)
\cong
(S_m\times S_m)\rtimes C_2
= S_m\wr C_2.
}
\]

Its order is

\[
2(m!)^2.
\]

#### Proof

The root is structurally fixed by the left-absorber pattern.

The two points `x_{+1},x_{-1}` are the two signed local-unit points. Therefore an automorphism either fixes the two same-sign sectors or exchanges them.

If the sectors are fixed, the generic positive points

\[
\{x_{+2},\ldots,x_{+N}\}
\]

may be permuted arbitrarily, and independently the generic negative points may be permuted arbitrarily. Because each right-zero terminal is anchored to its source, these two permutations uniquely induce the corresponding permutations of the split `E*` outputs.

Thus the side-preserving subgroup is `S_m x S_m`.

The derived reflection exchanges the two sides and conjugates the two symmetric-group factors. Hence adjoining it gives the semidirect product with factor-swap action, exactly the wreath product `S_m wr C_2`.

Conversely every such permutation preserves all declared `otimes` rules. □

### Corollary 4.2

The split `otimes`-only reduct is already non-Abelian for

\[
m\ge2\quad\Longleftrightarrow\quad N\ge3.
\]

For `N=3`, the group has order `8` and is the standard `S_2 wr C_2` dihedral-type wreath group.

---

## 5. Shared-fiber automorphism group

Now identify mirror terminal outputs at equal source index:

\[
x_{+n}\otimes x_0=x_{-n}\otimes x_0=E^*_n.
\]

The shared terminal output couples the two side permutations.

### Theorem 5.1 — Shared Diagonal Symmetry

For the shared-fiber signed `otimes` reduct,

\[
\boxed{
\operatorname{Aut}(\mathcal T^{\rm shared}_N)
\cong S_m\times C_2.
}
\]

The `S_m` factor acts diagonally on equal-depth source pairs and on `E^*`; the `C_2` factor is side reflection.

#### Proof

Suppose first that the two local units are fixed. Let the positive generic permutation be `sigma_+` and the negative one `sigma_-`.

Because the terminal is shared,

\[
E^*_n=\theta(x_{+n})=\theta(x_{-n}).
\]

After applying an automorphism,

\[
h(E^*_n)=E^*_{\sigma_+(n)}=E^*_{\sigma_-(n)}.
\]

Distinct shared terminals imply

\[
\sigma_+=\sigma_-.
\]

Thus only the diagonal copy of `S_m` survives.

Reflection swaps the two source sides but fixes every shared `E^*_n`; it commutes with the diagonal `S_m` action. Hence the full group is the direct product `S_m x C_2`. □

### Corollary 5.2

The shared terminal action induced on `E*` is exactly `S_m`; the reflection factor lies in the kernel of the terminal action.

The shared reduct becomes non-Abelian exactly when

\[
m\ge3\quad\Longleftrightarrow\quad N\ge4.
\]

---

## 6. Reflection-compatible output transport threshold

For a transport phase to preserve the signed reflection law without adding a compensating state transformation, its output action should commute with the terminal reflection.

### Split case

Let `r` be the pure side-swap reflection in `S_m wr C_2`.

### Theorem 6.1

\[
\boxed{
C_{S_m\wr C_2}(r)
\cong S_m\times C_2,
}
\]

where `S_m` is the diagonal subgroup `(sigma,sigma)`.

#### Proof

Write a side-preserving element as `(sigma_+,sigma_-)`. Conjugation by `r` exchanges the two coordinates. Hence commuting with `r` forces

\[
\sigma_+=\sigma_-.
\]

The same condition holds after multiplying by the central side-swap factor. □

### Shared case

Terminal reflection is trivial on `E*`, so the full induced terminal `S_m` action is reflection-compatible.

### Corollary 6.2 — Robust non-Abelian threshold

In both split and shared conventions, the reflection-compatible terminal transport group is non-Abelian once

\[
\boxed{m\ge3\iff N\ge4.}
\]

Thus three generic source labels `2,3,4` are the first robust finite truncation at which `otimes` alone supports reflection-compatible non-Abelian terminal relabelling.

---

## 7. Cross-operation collapse under `oplus`

The previous groups belong to the `otimes` reduct alone.

Now retain the FCOA-Z `oplus` zero-port law

\[
x_0\oplus x=x,
\]

\[
x_{\pm n}\oplus x_0=x_{\pm(n-1)}.
\]

This relation recovers radial depth recursively.

### Theorem 7.1 — Cross-Operation Symmetry Collapse

In the combined signed reduct containing both the inherited `oplus` radial port and the inherited `otimes` terminal port,

\[
\boxed{
\operatorname{Aut}(\mathcal T_N,\oplus)\cong C_2
}
\]

provided the explicit orientation/shift direction is erased and reflection is allowed.

If the oriented successor `T` itself is retained as a primitive directed symbol, the automorphism group is trivial.

#### Proof

The `oplus` right-zero law defines the parent relation along each ray:

\[
\rho(x_{\pm n})=x_{\pm(n-1)}.
\]

Any automorphism fixes the root and preserves radial depth. At depth one there are exactly two points. An automorphism either fixes them or swaps them. Once their action is chosen, preservation of `rho` recursively fixes the action at every larger depth.

Therefore the only carrier automorphisms are identity and global reflection.

Every terminal output is anchored to its carrier source through `otimes`, so its action is uniquely induced by the carrier action. Thus no additional `S_m` freedom remains.

If the directed successor `T` is retained, reflection reverses `T` and is no longer an automorphism, leaving only the identity. □

### Corollary 7.2 — Terminal action after collapse

- Split `E*`: the induced terminal action is at most `C_2`, generated by mirror exchange at each depth.
- Shared `E*`: reflection fixes the shared terminal at each depth, so the induced terminal action is trivial.

Hence the full FCOA-Z axis does **not** carry an intrinsic non-Abelian `E*` transport group.

---

## 8. The symmetry-transfer interpretation

The result can be summarized as

\[
\boxed{
\text{`otimes` exchangeability}
\xrightarrow{\text{add `oplus` radial memory}}
\text{depth anchoring}
\xrightarrow{}
\text{symmetry collapse}.
}
\]

This is a cross-operation phenomenon: one operation destroys a latent symmetry of another operation without modifying the latter's inherited cells.

On finite truncations the collapse is drastic.

### Split terminal convention

\[
S_m\wr C_2\longrightarrow C_2.
\]

### Shared terminal convention

\[
S_m\times C_2\longrightarrow C_2
\]

on the full structure, while the action on `E*` itself collapses

\[
S_m\longrightarrow 1.
\]

Thus the memory encoded by `oplus` acts as a symmetry firewall for `otimes` terminal values.

---

## 9. Consequence for group-valued transport phases

Suppose a future mixed `otimes` extension is generated by radial cancellation followed by a terminal transport chosen from an intrinsic automorphism group.

### `otimes`-only reduct

For `N>=4`, a reflection-compatible transport clock may take values in a non-Abelian group containing `S_m`.

Thus non-Abelian **group-valued transport is available in principle** if one deliberately studies the symmetry-rich `otimes` reduct without the `oplus` depth anchor.

### Combined FCOA-Z reduct

The intrinsic terminal transport group is at most `C_2`, and in the shared convention it is trivial on terminal values.

Therefore:

\[
\boxed{
\text{full axis + inherited cross-operation coherence}
\Longrightarrow
\text{no intrinsic non-Abelian terminal phase}.
}
\]

This is an obstruction theorem, not a failure of the programme: it identifies exactly which inherited structure kills the larger phase group.

---

## 10. Non-Abelian group does not yet imply noncommuting phase history

There is a second obstruction.

Even if a transport group `G` is non-Abelian, a homogeneous unary inward chain with one fixed step transport `g in G` produces only

\[
g^k.
\]

All observed transports lie in the cyclic subgroup generated by `g`.

### Proposition 10.1 — Unary Homogeneous Abelianization

A one-step homogeneous transport law on a one-dimensional cancellation chain cannot witness noncommuting transport products, regardless of how non-Abelian the ambient group `G` is.

#### Proof

Every `k`-step transport is a power of the same element `g`. Powers of one element commute. □

Thus genuinely noncommuting phase history requires at least two transport generators selected by additional intrinsic information: multiple step types, branching, or an added internal controller state.

---

## 11. Minimal route to genuine noncommuting transport

The present theorem narrows the next frontier sharply.

There are two possible routes.

### Route A — deliberately weaken cross-operation coherence

Work in the `otimes`-only reduct and permit a finite-state transport controller whose step labels select two noncommuting elements of the reflection-compatible `S_m` subgroup.

This creates a group-valued clock but the controller is additional structure.

### Route B — branching carrier

Replace the two-ray axis by a rooted branching carrier. The rooted radial automorphism group of a branching tree is naturally an iterated wreath product, so multiple noncommuting local generators can arise from the carrier geometry itself rather than from an externally supplied controller.

This route preserves the guiding FCOA-Z principle more faithfully.

---

## 12. Verification

The group orders were independently checked by exhaustive enumeration of the finite signed `otimes` reduct for small truncations:

- `N=2`: split `2`, shared `2`;
- `N=3`: split `8`, shared `4`;
- `N=4`: split `72`, shared `12`.

These equal

\[
2((N-1)!)^2
\]

and

\[
2(N-1)!
\]

respectively.

Adding the signed `oplus` radial port reduces the enumerated automorphism count to `2` for the tested truncations, in agreement with Theorem 7.1.

---

## 13. Classical comparison boundary

The wreath-product mechanism itself is classical. Wreath products are standard semidirect products encoding independent component symmetries together with permutation of isomorphic components; see the Encyclopedia of Mathematics entry *Wreath product* and classical work of Krasner-Kaloujnine.

Likewise group-valued cocycles and skew-product constructions are standard objects in dynamical systems and cohomology. No novelty is claimed for those general mechanisms.

The FCOA-Z-specific content is the exact conjunction:

1. the signed M0 `otimes` reduct has a calculable large source/terminal symmetry;
2. shared versus split terminal provenance changes the automorphism group from a wreath product to a diagonal symmetric group times reflection;
3. the independently inherited `oplus` radial law collapses that symmetry to `C_2` or to trivial terminal action;
4. relative terminal symmetry with the source carrier fixed is already trivial;
5. therefore a non-Abelian terminal phase is obstructed in the full two-ray FCOA-Z structure.

---

## 14. Current conclusion

The previous question was:

\[
\text{does the second legacy operation supply a larger terminal phase group?}
\]

The exact answer is:

\[
\boxed{
\begin{array}{ll}
\text{`otimes` alone:} & \text{yes, large and eventually non-Abelian};\\
\text{full FCOA-Z axis:} & \text{no, cross-operation depth memory collapses it};\\
\text{base fixed pointwise:} & \text{terminal symmetry is trivial}.
\end{array}}
\]

The strongest next strike is therefore no longer to search the same axis for a hidden non-Abelian terminal fiber.

It is to determine the **minimal branching carrier for which radial geometry itself has a non-Abelian transport group and can feed a genuinely noncommuting mixed interaction law**.