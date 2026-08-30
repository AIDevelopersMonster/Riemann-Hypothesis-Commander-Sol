# FCOA Admissibility Geometry — current state

**Canonical publication DOI:** 10.5281/zenodo.22129787  
**Publication date:** 2026-08-27  
**GitHub role:** theorem/reproducibility/demo companion  
**Maintenance boundary:** see [`WORKSPACE.md`](WORKSPACE.md)  
**State synchronized:** 2026-08-30

---

## 1. Fixed publication checkpoint

The published and audited chain remains

\[
\boxed{M0\to G1\to G2.}
\]

Later work does not silently revise that Zenodo publication.

Post-publication fixed results include G3 value-memory after repair, the relative typed Fiber-Transport theorem, G4-C/G4-A bounded-output amplification, exact generic order recovery in G4-A, and the G4-A Generic FO Collapse:

\[
\boxed{FO(\text{G4-A generic sector})=FO[<].}
\]

Thus G4-A is the fixed AL0/order wall.

---

## 2. Arithmetic leakage map

On the ordered generic base, `EqGap` and truncated `Add` are uniformly FO-interdefinable.

Programme levels:

- `AL0`: order wall / FO[<];
- `AL-INT`: intermediate non-order enrichments without full addition;
- `AL1`: uniform truncated addition / EqGap;
- `AL2`: full arithmetic gateway, in particular uniform truncated addition and multiplication.

The One-Cell Oracle phenomenon excludes arbitrary external size-dependent import from meaningful support optimization. Conversely, fixed-depth FO-definitional compilation from G4-A cannot leave AL0.

Hence admissible central mechanisms must be genuinely generated and non-oracular.

---

## 3. Fixed generation barriers

The unary finite-state wall gives

\[
AL0<AL\text{-}FS<AL1.
\]

The Regular-Primitive Barrier shows finite-copy position-regular expansions and fixed-depth nesting cannot uniformly define Add/EqGap.

Correct synchronization threshold:

\[
TC(S)\in AL0,
\qquad
TC(S\times S)=EqGap\in AL1.
\]

The leakage source is unbounded closure on the synchronized two-dimensional product.

---

## 4. Fixed support lower bound

For the explicit ordered base carrier `[m]`, fixed finite bounded-arity added signature, ordinary FO queries, all added primitive tuples charged, and no uncharged growing auxiliary carrier:

\[
\boxed{Add\text{ requires }\Omega(m)\text{ materialized added support}.}
\]

This lower bound allows arbitrary `m`-dependent relations and therefore applies to all narrower generated-history witnesses used below.

---

## 5. Binary history overshoot

The generated binary full-history construction has

\[
\Theta(m\log m)
\]

materialized support and exposes BIT/full arithmetic:

\[
\boxed{AL2.}
\]

This fixed result first established that support density and leakage strength are independent axes.

---

## 6. Zeckendorf selective additive memory — hostile-audited

The self-anchored incidence relation

\[
Z(n,p)
\]

records the Fibonacci weights occurring in the canonical Zeckendorf representation of `n`.

No Fibonacci-index, Add, Mul, EqGap, rank, or final-size oracle is queried. Digit anchors are internal:

\[
FibPos(p)\iff Z(p,p).
\]

The Fibonacci addition automaton used by the construction has an independently verified aperiodic transition monoid, permitting an FO addition definition over digit positions.

The infinite Zeckendorf incidence envelope is automatic/decidable. Therefore

\[
\boxed{Add,EqGap\in FO(<,Z),\qquad Mul\notin FO(<,Z).}
\]

So the generated Presburger Compression Corridor is nonempty. Full positive-incidence support is `Theta(m log m)`.

---

## 7. Optimal linear Zeckendorf event compression — hostile-audited

Files:

- [`ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md`](ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md)
- [`HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md`](HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_event_compression_phase_split.py`

Store only digit changes:

\[
U(n,p):0\to1,
\qquad
D(n,p):1\to0.
\]

Every Zeckendorf increment creates exactly one new `1`. Therefore for every prefix `[m]`, with `s_F` the Zeckendorf summand count,

\[
|U_m|=m-1,
\]

\[
|D_m|=m-1-s_F(m-1),
\]

and

\[
\boxed{|U_m|+|D_m|=2m-2-s_F(m-1)=\Theta(m).}
\]

Latest-event integration recovers the full `Z` relation, and the event relations are uniformly FO-definable back from consecutive `Z` rows. Hence full-state and event-state presentations are uniformly FO-interdefinable and remain exact AL1.

Direct generator resource passport:

\[
\boxed{(\text{materialized support},\text{transient workspace})=(\Theta(m),O(\log m)).}
\]

Combining with the base-sort lower bound closes the support optimization problem:

\[
\boxed{C_{AL1}^{generated,base}(m)=\Theta(m).}
\]

---

## 8. Equal-linear-cost AL1/AL2 phase split — fixed

Applying the same differential encoding to binary counting gives

\[
|U_m^{(2)}|+|D_m^{(2)}|
=2m-2-s_2(m-1)
=\Theta(m).
\]

Latest-event integration reconstructs BIT, so the differential binary history remains AL2.

Thus:

\[
\boxed{
\begin{array}{c|c|c}
\text{history} & \text{support} & \text{phase}\\
\hline
Zeckendorf\ events & \Theta(m) & AL1\\
binary/BIT\ events & \Theta(m) & AL2
\end{array}}
\]

Scalar support, event density, and amortized change count do not determine arithmetic phase.

---

## 9. Decidable Coherent Envelope barrier — hostile-audited

Files:

- [`DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md`](DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md)
- [`HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md`](HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md)

For a prefix-coherent family `A_m`, `DCE` means existence of a coherent infinite envelope `A_infty` with decidable FO theory and

\[
A_m=A_\infty\upharpoonright[m]
\]

for every `m`.

The prefix-relativization/lift theorem yields the semantic firewall

\[
\boxed{DCE+Add\Longrightarrow\neg Mul.}
\]

Hence

\[
\boxed{AL2\Longrightarrow\neg DCE.}
\]

For the equal-cost examples:

\[
\boxed{DCE(Zeckendorf\ events),}
\]

while

\[
\boxed{\neg DCE(binary/BIT\ events).}
\]

DCE is preserved under coherent uniform FO definitional reductions and is invariant under coherent mutual definitional equivalence.

---

## 10. Coherent FO-interpretation invariance — fixed theorem checkpoint

File:

- [`COHERENT_FO_INTERPRETATION_INVARIANCE.md`](COHERENT_FO_INTERPRETATION_INVARIANCE.md)

The DCE separator now survives fixed-dimensional FO interpretations with:

- definable tuple domains;
- definable equivalence relations / quotients;
- definable interpreted primitive relations;

provided the finite interpretations are restrictions of one coherent infinite interpretation and old interpreted elements/classes do not change identity as the prefix grows.

If `A` has DCE and `B` is obtained from `A` by such a coherently liftable FO interpretation, then

\[
\boxed{DCE(B).}
\]

Therefore no coherently liftable fixed-dimensional FO interpretation, even with quotient, can map the Zeckendorf event family to the binary/BIT event family:

\[
\boxed{
\mathcal E^F
\not\xrightarrow{\ coherent\ FO\ interpretation\ }
\mathcal E^2.
}
\]

This is the first rigorous non-collapse result against the “exotic recoding” objection at equal linear support.

---

## 11. Current fixed ledger

\[
\mathbf F:\ \text{G4-A order wall and Add/EqGap gateway}
\]

\[
\mathbf F:\ \text{oracle/FO-compilation firewall}
\]

\[
\mathbf F:\ \text{unary finite-state and regular-primitive barriers}
\]

\[
\mathbf F:\ \text{Base-Sort Linear Support Barrier }\Omega(m)
\]

\[
\mathbf F:\ \text{binary full history }\Theta(m\log m)\to AL2
\]

\[
\mathbf F:\ \text{self-anchored Zeckendorf full history }\Theta(m\log m)\to exact\ AL1
\]

\[
\mathbf F:\ \text{Zeckendorf events }\Theta(m)\to optimal\ exact\ AL1
\]

\[
\mathbf F:\ \text{binary events }\Theta(m)\to AL2
\]

\[
\mathbf F:\ DCE+Add\Rightarrow\neg Mul
\]

\[
\mathbf F:\ \text{DCE preserved by coherently liftable fixed-dimensional FO interpretations}
\]

---

## 12. Immediate main-line question

Two former central questions are now closed in the declared model:

\[
\boxed{\text{optimal generated exact-AL1 support}=\Theta(m),}
\]

and

\[
\boxed{\text{canonical equal-linear-cost AL1/AL2 families are semantically separated by DCE}.}
\]

The interpretation objection is also closed for **coherently liftable fixed-dimensional FO interpretations, including quotients**.

The remaining invariance frontier is therefore narrower:

\[
\boxed{
\text{When does a uniform sequence of finite FO interpretations automatically admit a coherent infinite lift?}
}
\]

Parallel publication-bearing generalization target:

\[
\boxed{\text{Aperiodic Automatic Numeration Corridor}.}
\]

Goal: characterize numeration histories with (i) decidable/automatic coherent envelope, (ii) FO-realizable addition, and (iii) amortized `O(1)` successor changes, so that differential materialization yields optimal linear exact AL1.
