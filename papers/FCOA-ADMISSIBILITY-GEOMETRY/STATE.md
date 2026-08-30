# FCOA Admissibility Geometry — current state

**Canonical publication DOI:** 10.5281/zenodo.22129787  
**Publication date:** 2026-08-27  
**GitHub role:** theorem/reproducibility/demo companion  
**Maintenance boundary:** see [`WORKSPACE.md`](WORKSPACE.md)  
**State synchronized:** 2026-08-30

---

## 1. Publication checkpoint — fixed

The published and audited chain remains

\[
\boxed{M0\longrightarrow G1\longrightarrow G2.}
\]

Nothing in later G3/G4/Arithmetic-Leakage/generated-memory work silently revises that Zenodo publication.

---

## 2. Post-publication rigidity chain — fixed

The following remain fixed theorem checkpoints in their stated scopes:

- G3 value-memory after hostile-audit repair;
- Fiber-Transport theorem in its relative typed setup;
- G4-C and G4-A bounded-output amplification;
- uniform parameter-free recovery of the exact generic total order in G4-A;
- G4-A Generic FO Collapse / Arithmetic Leakage left wall.

In particular, after relationalizing G4-A,

\[
\boxed{FO(\text{G4-A generic sector})=FO[<].}
\]

Hence generic G4-A does not uniformly define canonical truncated Add, Mul, or EqGap.

---

## 3. Additive gateway — fixed

On the ordered generic base,

\[
EqGap\quad\text{and}\quad Add
\]

are uniformly FO-interdefinable.

Correct claim discipline:

\[
\boxed{EqGap\text{ is a canonical gateway to full additive leakage, not the globally weakest non-order enrichment}.}
\]

Arithmetic leakage levels used by the programme:

- `AL0`: order wall / FO[<];
- `AL-INT`: intermediate non-order enrichments without full addition;
- `AL1`: uniform truncated addition / EqGap;
- `AL2`: full arithmetic gateway, in particular uniform truncated addition and multiplication.

---

## 4. Oracle / compilation firewall — fixed after subsequent audits

The One-Cell Oracle phenomenon shows raw support minimization is meaningless if arbitrary external size-dependent data may be imported.

Conversely, uniform fixed-depth FO-definitional compilation from G4-A cannot leave AL0.

Thus the central programme uses a provenance firewall:

\[
\boxed{
\text{exclude arbitrary external oracle import; require genuinely generated non-oracular memory.}
}
\]

---

## 5. Finite-state and regular-primitive barriers — fixed

`U1_FINITE_STATE_WALL.md` proves, for prefix-consistent deterministic finite-state unary generators, a strict intermediate zone

\[
AL0<AL\text{-}FS<AL1.
\]

The broader Regular-Primitive Barrier proves that finite-copy position-regular expansions cannot uniformly define Add or EqGap. Fixed-depth nesting does not cross the barrier.

The corrected head-synchronization threshold is:

\[
TC(S)\in AL0,
\qquad
TC(S\times S)=EqGap\in AL1.
\]

The source of leakage is the unbounded closure of the synchronized two-dimensional product, not the local successor-product edge relation itself.

---

## 6. Base-sort support lower bound — fixed

For an explicit ordered base carrier `[m]`, one fixed finite bounded-arity added signature, ordinary FO query language, all added primitive tuples charged, and no uncharged growing auxiliary carrier, uniform recovery of canonical truncated addition requires

\[
\boxed{\Omega(m)}
\]

materialized added support.

This lower bound permits arbitrary `m`-dependent relations; therefore it applies a fortiori to the narrower generated-history families used below.

---

## 7. Binary history compression — fixed overshoot witness

A locally generated binary counter materializes full bit history with

\[
\Theta(m\log m)
\]

support.

The history uniformly exposes BIT and reaches the full arithmetic phase:

\[
\boxed{AL2.}
\]

Thus support density and arithmetic leakage are orthogonal: a sparser generated history can leak more arithmetic than a denser one.

---

## 8. Zeckendorf selective additive memory — hostile-audited exact AL1

The self-anchored Fibonacci/Zeckendorf history uses

\[
Z(n,p)\iff p\text{ is a Fibonacci weight used in the canonical representation of }n.
\]

The generator does not query Fibonacci indices, Add, Mul, EqGap, rank, or final size. Digit anchors are internal:

\[
FibPos(p)\iff Z(p,p).
\]

The synchronous Fibonacci adder used in the construction has an aperiodic transition monoid (verified independently in `verify_zeckendorf_adder_aperiodic.py`), so addition is FO-realizable over digit positions.

The infinite Zeckendorf incidence envelope is automatic/decidable, yielding the multiplication firewall by prefix lifting.

Therefore

\[
\boxed{Add,EqGap\in FO(<,Z),\qquad Mul\notin FO(<,Z).}
\]

Hence the generated Presburger Compression Corridor is nonempty.

Full positive-incidence support is

\[
\Theta(m\log m).
\]

---

## 9. Zeckendorf event compression — hostile-audited optimal linear AL1

Files:

- [`ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md`](ZECKENDORF_EVENT_COMPRESSION_OPTIMAL_AL1.md)
- [`HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md`](HOSTILE_AUDIT_ZECKENDORF_EVENT_COMPRESSION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_event_compression_phase_split.py`

Define differential event relations

\[
U(n,p):0\to1,
\qquad
D(n,p):1\to0.
\]

For every `n>=1`, Zeckendorf successor creates exactly one new `1` digit. If `s_F(n)` is the number of Zeckendorf summands, then for every prefix `[m]`

\[
|U_m|=m-1,
\]

\[
|D_m|=m-1-s_F(m-1),
\]

and therefore

\[
\boxed{|U_m|+|D_m|=2m-2-s_F(m-1)=\Theta(m).}
\]

Latest-event integration uniformly reconstructs the full Zeckendorf incidence relation, while `U,D` are uniformly FO-definable back from consecutive `Z` rows. Thus the full-state and event-state families are uniformly FO-interdefinable.

The arithmetic phase is unchanged:

\[
\boxed{\text{Zeckendorf events are exact }AL1.}
\]

Resource passport of the direct generator:

\[
\boxed{(\text{materialized support},\text{transient workspace})=(\Theta(m),O(\log m)).}
\]

Combining with the base-sort lower bound closes the support optimization problem in the declared model:

\[
\boxed{C_{AL1}^{generated,base}(m)=\Theta(m).}
\]

---

## 10. Equal-linear-cost binary event family — fixed comparison

Applying the same differential encoding to binary counting gives

\[
|U_m^{(2)}|+|D_m^{(2)}|
=2m-2-s_2(m-1)
=\Theta(m).
\]

Latest-event integration reconstructs BIT, and the event presentation is uniformly FO-interdefinable with the binary history.

Therefore

\[
\boxed{\text{binary/BIT events remain }AL2.}
\]

We now have two generated families with the same optimal linear materialized support but different arithmetic phases:

\[
\boxed{
\begin{array}{c|c|c}
\text{history} & \text{support} & \text{phase}\\
\hline
Zeckendorf\ events & \Theta(m) & AL1\\
binary/BIT\ events & \Theta(m) & AL2
\end{array}}
\]

Hence scalar support, event density, and amortized number of changes do not determine the arithmetic phase.

---

## 11. Decidable Coherent Envelope barrier — hostile-audited semantic separator

Files:

- [`DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md`](DECIDABLE_COHERENT_ENVELOPE_PHASE_BARRIER.md)
- [`HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md`](HOSTILE_AUDIT_DECIDABLE_COHERENT_ENVELOPE.md)

For a prefix-coherent family `A_m` on `[m]`, define `DCE` to mean existence of a coherent infinite envelope

\[
A_\infty=(\mathbb N,<,\ldots)
\]

with decidable FO theory and

\[
A_m=A_\infty\upharpoonright[m]
\]

for every `m`.

The prefix-relativization lemma gives a uniform lift of any prefix-coherent relation from fixed finite formulas to the infinite envelope.

Therefore:

### Decidable Coherent Envelope Barrier

If truncated addition is uniformly FO-definable and DCE holds, then truncated multiplication is not uniformly FO-definable:

\[
\boxed{DCE+AL1\Longrightarrow\neg AL2.}
\]

Equivalently, any prefix-coherent AL2 family admits no decidable coherent envelope:

\[
\boxed{AL2\Longrightarrow\neg DCE.}
\]

For the canonical linear examples:

\[
\boxed{DCE(Zeckendorf\ events)}
\]

because the infinite Fibonacci/Zeckendorf incidence/event structure is word-automatic and therefore has decidable FO theory, whereas

\[
\boxed{\neg DCE(binary/BIT\ events)}
\]

because their uniform Add+Mul would contradict the DCE barrier.

DCE is preserved under coherent uniform FO definitional reductions; under mutual definitional equivalence it is invariant.

Thus the equal-linear-cost phase split now has a rigorous semantic separator, not merely a presentation heuristic.

---

## 12. Current fixed ledger

\[
\mathbf F:\ M0,G1,G2\text{ published/audited checkpoint}
\]

\[
\mathbf F:\ G3/G4\text{ post-publication rigidity chain in stated scopes}
\]

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
\mathbf F:\ \text{binary full history }\Theta(m\log m)\text{ reaches }AL2
\]

\[
\mathbf F:\ \text{self-anchored Zeckendorf full history }\Theta(m\log m)\text{ is exact }AL1
\]

\[
\mathbf F:\ \text{Zeckendorf event history }\Theta(m)\text{ is optimal exact }AL1
\]

\[
\mathbf F:\ \text{binary event history }\Theta(m)\text{ remains }AL2
\]

\[
\mathbf F:\ DCE+AL1\Rightarrow\neg AL2\text{ for prefix-coherent same-base families}
\]

---

## 13. Immediate main-line question

The old question “can generated exact AL1 be compressed below quadratic/subquadratic support?” is closed in the declared base-sort model:

\[
\boxed{\Theta(m)\text{ is optimal}.}
\]

The old equal-linear-cost question “is there any intrinsic separator between the Zeckendorf and BIT event histories?” is also answered at the first semantic level:

\[
\boxed{DCE\text{ separates the canonical examples}.}
\]

The current central problem is now strictly sharper:

\[
\boxed{
\text{Can DCE, or a strengthening of it, be made invariant under broad FO interpretations}
}
\]

including multi-dimensional interpretations, quotients, and nontrivial carrier recodings, while retaining a usable AL1/AL2 barrier?

Parallel generalization target:

\[
\boxed{
\text{Aperiodic Automatic Numeration Corridor}
}
\]

— characterize numeration histories with (i) decidable/automatic coherent envelope, (ii) FO-realizable addition, and (iii) amortized `O(1)` successor changes, so that differential materialization yields optimal linear exact AL1.

These are the next publication-bearing strikes.
