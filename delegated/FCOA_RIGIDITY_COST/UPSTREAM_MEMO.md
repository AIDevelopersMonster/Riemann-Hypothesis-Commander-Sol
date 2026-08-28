# FCOA Rigidity Cost — Upstream Memo

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Audience:** main Commander Sol scientific director  
**Status:** local results proposed for upstream review; nothing here modifies M0–G4 automatically.

## Executive verdict

Four results from this direction are strong enough for upstream review.

### U1. Rigidity cost is not successor-memory cost

Let `n=N-1` be the generic carrier size and

\[
r_{\to}(n)=\min\{|A|:\operatorname{Aut}(X,A)=1\}.
\]

Exact values through `n=7` are

\[
(1,1,2,3,3,4).
\]

Elementary bounds give

\[
\left\lceil\frac{n-1}{2}\right\rceil
\le r_{\to}(n)\le n-2
\qquad(n\ge3).
\]

G2 uses `n-1` cells because it stores a directed Hamiltonian successor path over all generic points. Therefore its cost is not a pure rigidity minimum. The correct structural distinction is

\[
\boxed{
\text{minimum cost to kill automorphisms}
\ne
\text{minimum cost to retain a chosen global successor memory}.
}
\]

This strengthens the interpretation of G2 rather than weakening it.

### U2. Terminal Generic Layer Master Lemma

For any set

\[
A\subseteq G_N^2\setminus\Delta,
\qquad |A|=m,
\]

of new generic cells with terminal outputs, irrespective of terminal coloring,

\[
\boxed{
\begin{aligned}
EQ &= 4(N-1)+m,\\
NEQ &= 0,\\
LEFT &= N^2+2N-2+m,\\
RIGHT &= N^2+N-2+m,\\
NONE &= N^3+N^2-4N+9-3m.
\end{aligned}}
\]

Each new cell changes exactly one `EQ`, one `LEFT`, one `RIGHT`, and three `NONE` base triples. This single lemma recovers the G2, G3-S/G3-C and G4-C spectrum formulas from cell count alone.

The exact commutation correction is

\[
\boxed{
|\operatorname{Comm}|=3(N-1)+
|\{(u,v)\in A:(v,u)\in A,\ c(u,v)=c(v,u)\}|.
}
\]

Hence Association Spectrum is blind to fine skeleton and terminal-fiber geometry beyond the number of cells; commutation is also coarse.

### U3. Same G4-C coarse invariants, but rigidity instead of C2

The residual `C2` in G4-C is caused by the **transitive-order fiber geometry**, not by complete definedness, two anonymous outputs, or balanced fiber sizes themselves.

On five generic vertices use

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}.
\]

This tournament is asymmetric and non-self-converse. Color its arcs by `Omega_+` and reverse arcs by `Omega_-`. Then the resulting complete-domain terminal layer has:

- the same complete generic domain as G4-C;
- two anonymous outputs;
- equal fiber sizes `10+10`;
- the same Association Spectrum as G4-C;
- the same commutation count as G4-C;
- but full-operation automorphism group `1` instead of `C2`.

For FCOA `N=6`, both spectra are

\[
(40,0,66,60,177),
\]

and both commutation counts are `15`, while

\[
\operatorname{Aut}(G4\text{-}C)\cong C_2,
\qquad
\operatorname{Aut}(T_5\text{-layer})=1.
\]

Moreover, adjoining a new vertex dominating all old vertices preserves asymmetry and non-self-converseness, giving such a tournament for every `n>=5`. Therefore for every `N>=6` there is a balanced complete-domain two-anonymous-output zero-anchor layer with

\[
\boxed{
\operatorname{Aut}=1,
\qquad
\operatorname{VRI}=(N-1)!,
}
\]

while retaining the G4-C Association Spectrum and commutation formula.

This does **not** refute G4-C. It sharpens its claim boundary: the one-anchor mechanism is a sharp statement for the chosen transitive-order coloring, not a global minimum over all two-fiber complete-domain colorings.

### U4. Minimal missing invariant: cyclic-triangle defect

Inside the complete-domain two-anonymous-output **tournament-type** class, all induced anonymous patterns on one or two generic vertices are unique. Hence no local pattern invariant of order at most two can distinguish G4-C from another tournament layer.

At order three there are exactly two anonymous induced types: transitive and cyclic. Define

\[
\tau_3(T)=\#\{\text{cyclic induced generic triples}\}.
\]

Then `tau3` is the unique independent scalar in the three-point induced-profile count. G4-C is transitive, so

\[
\boxed{\tau_3(G4\text{-}C)=0.}
\]

The rigid tournament family from U3 has exactly

\[
\boxed{\tau_3=2}
\]

for every `n>=5`.

The value `2` is exact-minimal for anonymous rigidity in this class:

- `tau3=0` gives the transitive tournament and its reversal/converse symmetry;
- `tau3=1` is impossible for rigidity, because the unique cyclic triangle is a module and its 3-cycle rotation is a nontrivial automorphism;
- the U3 tournament `T5` has exactly two cyclic triples, and adjoining successive universal sources creates no new cyclic triple while preserving asymmetry and non-self-converseness.

Therefore

\[
\boxed{
\min\{\tau_3(T):\operatorname{Aut}^{\pm}(T)=1\}=2
\qquad(n\ge5).
}
\]

Here `Aut^±` permits a global anonymous-output exchange, equivalently an isomorphism to the converse tournament.

An equivalent scalar is the second outdegree moment

\[
M_2(T)=\sum_v d_+(v)^2,
\]

because

\[
\boxed{
M_2(T)=\frac{n(n-1)(2n-1)}6-2\tau_3(T).
}
\]

Thus the first degree moment is constant over all tournaments, while the second moment is already sufficient to separate G4-C from this rigid family.

The structural message is stronger than mere separation: a **constant microscopic defect of two cyclic triples** removes the final global reversal symmetry for an arbitrarily large generic carrier. The coarse G4-C invariants remain unchanged, but VRI doubles from `n!/2` to `n!`.

Full proof and scope conditions are in `TRIANGLE_SEPARATOR.md`.

## Additional structural firewall: pure-carrier naturality

A skeleton assignment natural under every bijection of a pure finite carrier cannot break symmetry: every permutation preserves the assigned skeleton. Thus a successful `carrier-uniform` rigidity construction must always be understood as uniform **relative to additional transported data**, not canonically generated from the bare carrier.

## Branch passport for U3/U4

- **Carrier/signature:** M0 backbone; complete off-diagonal generic terminal layer; two anonymous terminal outputs.
- **Defined cells:** all `n(n-1)` ordered distinct generic pairs.
- **Full automorphism group:** trivial for the tournament family `n>=5`.
- **Definedness group:** full `S_n` on the generic sector relative to M0 boundary roles.
- **Commutation:** exactly M0, size `3n`.
- **Association Spectrum:** exactly G4-C formula.
- **Three-point invariant:** G4-C `tau3=0`; rigid family `tau3=2`.
- **Second degree moment:** differs from the transitive maximum by exactly `4` for the rigid family.
- **Small cases:** tournament anonymous rigidity first appears at `n=5`; the exact minimum cyclic-triangle defect is then `2` and remains `2` for all larger `n` in the recursive family.
- **Mechanism:** value-fiber geometry only; no domain asymmetry and no anchor.
- **External naming:** none for the two outputs. The chosen tournament is transported combinatorial input.
- **Ordinary arithmetic imported:** no.

## Recommendation

Recommend upstream acceptance of U2, the scope-sharpening content of U3, and U4 after independent hostile review. Do not edit G4 from this subordinate branch. If G4 itself survives hostile audit, present it as the elegant **order-derived** two-fiber construction; then use U4 to state exactly which first local invariant detects departure from transitivity.