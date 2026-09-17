# HATTER-SOL-11 · Odd-prime / odd-composite tail patrol

Status: first closed patrol theorem plus computational search protocol.

The purpose of this note is to formalize the question whether an odd rational prime or odd composite integer can develop an unpaired orbital "tail" when transported into different imaginary quadratic worlds.

The answer at the raw prime-ideal factorization level is negative. Any genuine tail must appear later, after witness choice, residue conditioning, or network projection.

## 1. Rational odd integers are conjugation-balanced at ideal level

Let `K/Q` be imaginary quadratic and let

\[
n=\prod_p p^{e_p}\in\mathbb Z_{>0}
\]

be odd. Its principal ideal is

\[
(n)=\prod_p (p)^{e_p}.
\]

For each odd rational prime `p`, exactly one of the usual quadratic cases occurs.

### Split

\[
(p)=\mathfrak p\bar{\mathfrak p}.
\]

Hence

\[
(p)^{e_p}=\mathfrak p^{e_p}\bar{\mathfrak p}^{e_p}.
\]

The two conjugate prime-ideal multiplicities are exactly equal.

### Ramified

\[
(p)=\mathfrak p^2,
\qquad \bar{\mathfrak p}=\mathfrak p.
\]

Hence

\[
(p)^{e_p}=\mathfrak p^{2e_p}.
\]

The unique ramified prime ideal occurs with even multiplicity.

### Inert

`(p)` remains prime and is fixed by conjugation.

Thus no unpaired conjugate factor exists.

### Theorem T11.7 — no raw ideal tail

For every odd rational integer `n`, the multiset of prime-ideal factors of `(n)` is invariant under conjugation with equal multiplicities on every non-fixed conjugate pair.

Equivalently:

\[
\boxed{
\text{a rational odd integer has no conjugation-unbalanced tail at the raw ideal-factorization level.}
}
\]

This remains true for both primes and composites.

## 2. Why this does not kill the tail question

HATTER-SOL-10 showed that a nonprincipal ideal can have several minimal principalization witnesses. Choosing one witness replaces a conjugation-balanced ideal-level object by a direction-labelled element-level object.

Therefore an orbital tail can still arise through one of the following symmetry-breaking operations:

1. selecting one witness orbit from a multistate ideal node;
2. fixing a principalization residue fiber;
3. optimizing a network with asymmetric host/weight constraints;
4. projecting a direction-labelled geodesic state to a coarser folded `(P,Q)` state;
5. composing several witness sectors whose residue product is constrained globally.

So the search target is not

\[
(n)\text{ itself},
\]

but the chain

\[
(n)
\to
\{\text{prime ideals}\}
\to
\{\text{minimal witnesses}\}
\to
\{\text{orbital signatures}\}
\to
\text{residue/network sector}.
\]

## 3. Orbit-fusion interaction with rational primes

The split/inert/ramified law and the direction-orbit law are independent layers:

- prime splitting tells us how many arithmetic factor ideals exist;
- orbit fusion tells us how many interface direction classes the world can distinguish.

This gives a 3-by-2 qualitative grid.

### Generic worlds

There are two direction orbits. A split rational prime may therefore produce factor witnesses whose geodesic signatures distribute capacity differently between the two orbits.

This is the natural hunting ground for an orbital tail.

### Gaussian / Eisenstein worlds

There is only one direction orbit. Any tail based solely on direction-orbit imbalance is erased by the extra unit symmetry.

Thus these high-symmetry worlds are natural **tail-erasure controls**.

This suggests a useful comparison:

\[
\boxed{
\text{generic world with two direction orbits}
\quad\leftrightarrow\quad
\text{Gaussian/Eisenstein fused world}.
}
\]

If an observable disappears exactly under orbit fusion, it is a credible orbital-tail candidate.

## 4. Small-prime reconnaissance

For a quadratic discriminant `Delta`, odd rational primes are classified by the Kronecker symbol

\[
\left(\frac{\Delta}{p}\right)
\in\{-1,0,+1\},
\]

corresponding to inert, ramified, and split behavior.

A reconnaissance over representative worlds immediately shows that no single odd prime has a fixed behavior across worlds. For example:

- `p=3` is ramified in `Delta=-3,-15,-24`, inert in `Delta=-4,-7,-19,-40`, and split in `Delta=-8,-11,-20,-23,-31`;
- `p=5` is split in several generic worlds, ramified in `Delta=-15,-20,-40`, and inert in others;
- `p=7` is ramified in `Delta=-7`, split in many even and odd generic worlds, and inert in the Gaussian world.

Therefore odd primes supply many natural cross-world probes of the interaction

\[
\text{splitting type}
\times
\text{direction-orbit count}.
\]

The patrol should prioritize primes that are split in a generic two-orbit world and compare them with a fused world in which the same rational prime is also split when possible.

## 5. Multistate prime ideals are the first tail candidates

The HATTER-SOL-10 laboratory already supplies the prototype:

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
\mathfrak q=(23,\omega-7),
\]

with two minimal witness states

\[
S=(3,2),
\qquad
T=(6,1).
\]

HATTER-SOL-11 refines these to different axial/oblique orbital signatures. Thus the raw split arithmetic is balanced, but witness resolution exposes distinct orbital allocations.

A broader small search also finds the same phenomenon repeatedly in generic fields: split prime ideals can have more than one minimal witness orbit. Examples worth retaining for exact follow-up include:

### `Delta=-15`

Split prime ideals above

\[
p=17,23,47,53
\]

already exhibit two minimal witness orbits in a bounded exact norm search; the known `p=23` case is one member of this family.

### `Delta=-35`

Several split prime ideals (for example above `13,17,47`) show two minimal witness orbits with principalization cost `3`.

### `Delta=-84`

Several split prime ideals (for example above `17,41`) show two minimal witness orbits with principalization cost `5`.

These numerical observations are **research leads, not theorem claims** until each candidate is proved by an exact norm-form argument as was done for `Delta=-15,p=23`.

The pattern is nevertheless suggestive: the principalization cost itself can carry an odd value (`3`, `5`, ...), while the rational input remains conjugation-balanced. This is one plausible source of the user's anticipated "tail" after witness resolution.

## 6. Composite odd integers

For an odd composite

\[
n=\prod p_i^{e_i},
\]

raw ideal balance still holds factor by factor by T11.7.

However composite systems allow a new effect unavailable to a single prime:

\[
\boxed{
\text{different local witness asymmetries can cancel or reinforce globally.}
}
\]

The principalization residue product from HATTER-SOL-10 is therefore the correct bookkeeping device.

A composite-tail observable should compare:

1. the total axial/oblique witness usage;
2. its conjugate-swapped partner;
3. the principalization residue ideal/orbit;
4. whether the ordinary folded network response erases the difference.

A particularly interesting case is when the total principal ideal is completely balanced but a fixed residue fiber forces an asymmetric mixture of witness orbit types. HATTER-SOL-10's residue-enforced `S^4T^4` construction is already the first controlled example of this mechanism, though it was not yet interpreted as an orbital-tail observable.

## 7. Tail observable candidates

Do not define a single scalar prematurely. Retain at least the following candidate data for a witness configuration `theta`:

\[
A(\theta)=\text{total usage in the axial norm-one orbit},
\]

\[
O(\theta)=\text{total usage in the outer/oblique orbit},
\]

and the signed difference

\[
\boxed{
\tau(\theta)=A(\theta)-O(\theta).
}
\]

This `tau` is only a **diagnostic candidate**, not yet a canonical network invariant. It can be tested for:

- change under conjugation;
- disappearance under Gaussian/Eisenstein orbit fusion;
- additivity or non-additivity under composite multiplication;
- dependence on residue fibers;
- survival after network optimization.

The stronger object is the full orbit-count vector rather than `tau`.

## 8. Patrol protocol

For each selected imaginary quadratic world and each odd `n` in a finite window:

1. factor `(n)` into prime ideals;
2. verify conjugation balance at the raw ideal level;
3. compute minimal witness sets for nonprincipal prime ideals;
4. resolve every witness into its canonical direction-orbit/geodesic signature;
5. record all attainable orbit-count vectors;
6. form composite witness products and residue fibers;
7. compare generic two-orbit worlds with Gaussian/Eisenstein fused controls;
8. flag any observable that survives arithmetic recombination but disappears under orbit fusion.

Only flagged patterns should be promoted to theorem targets.

## 9. Current conclusion

The first patrol gives a sharp localization result:

\[
\boxed{
\text{no tail in rational prime-ideal multiplicities;}
}
\]

but

\[
\boxed{
\text{possible tail after minimal-witness resolution and residue conditioning.}
}
\]

This is now the main experimental/theoretical search lane alongside the orbit-fusion classification.