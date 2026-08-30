# FCOA Hybrid Memory — Bridge to Standard Models

**Status:** literature-calibrated bridge note  
**Purpose:** identify the standard finite-model/circuit/CSP language closest to `CF(d,f)` and delimit what can and cannot be claimed as an embedding theorem.

## 1. Executive conclusion

No single standard class found in the current literature coincides exactly with `CF(d,f)`.

The closest standard decomposition is:

1. **NC^0-style bounded light cones** for the compositional dependency restriction;
2. **extensional/table constraints** from finite-domain CSP for the primitive bottom laws;
3. **immersive / strongly local FO transductions** as the nearest finite-model-theory analogue of locality, but this analogue is strictly more permissive than `CF(d,f)` unless additional degree/width restrictions are imposed.

Accordingly the correct external description is not “CF is standard guarded FO” or “CF is exactly NC^0”. A safer formulation is:

> `CF(d,f)` is a bounded-depth bounded-fan-in finite-domain incidence-circuit model with extensionally represented primitive gates; its Boolean light-cone behavior is NC^0-like, while its primitive gate-size measure is the standard table-size measure for extensional constraints.

This formulation is standard-language compatible without claiming a false equivalence.

---

## 2. FO transductions: what matches

Modern structural graph theory uses one-dimensional first-order transductions as a basic encoding quasi-order on graph classes. Braunfeld, Nešetřil, Ossona de Mendez, and Siebertz prove a local normal form: every transduction is subsumed by copying, an **immersive transduction** using strongly local formulas, and a perturbation. In their terminology, an immersive transduction is non-copying and its interpretation formulas are strongly local.

This matches the philosophical role of `CF3` compositional locality: output relations should be generated from local information rather than arbitrary global coding.

Reference:

- Samuel Braunfeld, Jaroslav Nešetřil, Patrice Ossona de Mendez, Sebastian Siebertz, *On first-order transductions of classes of graphs*, Logical Methods in Computer Science 21(2), 2025, DOI 10.46298/lmcs-21(2:26)2025.

---

## 3. Why immersive FO is still too broad

Strong locality is a radius condition, not a fan-in condition.

A strongly `r`-local formula may inspect an entire radius-`r` neighborhood. If the underlying incidence structure has unbounded degree, that neighborhood may contain an unbounded number of elements.

Therefore

\[
\text{strongly local FO}
\not\Rightarrow
\text{bounded dependency cone}.
\]

This is exactly where `CF(d,f)` is stricter: a depth-`d`, fan-in-`f` target dependency cone contains at most

\[
f^d
\]

primitive branches, independent of `N`.

Moreover, general FO transductions allow perturbations after the immersive part. Perturbations can globally complement adjacency between definable vertex classes and therefore violate the “no cross-branch shortcut” intent of CF3.

Hence the inclusion one should claim is only qualitative:

\[
\boxed{\text{CF locality is stronger than ordinary immersive-FO locality}.}
\]

There is no exact equivalence with general immersive transductions.

---

## 4. Standard circuit analogue: NC^0 light cones

The bounded-depth bounded-fan-in part of `CF(d,f)` has a direct standard circuit interpretation.

In a classical circuit of depth `d` and fan-in at most `f`, every output has a backward dependency cone containing at most

\[
f^d
\]

inputs.

This is the defining locality phenomenon behind constant-depth bounded-fan-in circuits, usually discussed as `NC^0`-style local computation.

Thus CF1 is exactly the finite-domain analogue of the standard Boolean light-cone bound.

The analogy is structural:

\[
\boxed{
\text{CF factorisation depth/fan-in}
\leftrightarrow
\text{bounded-depth bounded-fan-in circuit light cones}.
}
\]

---

## 5. Why CF is not literally Boolean NC^0

Primitive CF gates act on a bottom alphabet

\[
D_N
\]

whose size grows with `N`.

A primitive binary gate may therefore be an arbitrary function

\[
D_N^2\to D_N\times C
\]

represented by a table of size `Theta(|D_N|^2)`.

Standard Boolean NC^0, by contrast, works with a fixed finite Boolean gate basis and constant-arity Boolean gates. The description of one gate does not itself grow like `|D_N|^2`.

Therefore the Pair-Coverage lower bound in HM-CFPT is **not a standard NC^0 circuit-size lower bound**.

It is a lower bound on the extensional description size of a growing-alphabet primitive gate.

This distinction is essential for publication claims.

---

## 6. Booleanization lands naturally in AC^0-like circuits

If each bottom symbol is one-hot encoded using `|D_N|` Boolean wires, an extensional binary table can be evaluated by a constant-depth DNF/CNF-style circuit:

- conjunctions recognize individual input pairs;
- an unbounded OR collects all pairs producing a given output symbol.

The depth remains constant, but the OR fan-in grows with `|D_N|` and the total Boolean circuit size reflects the table size.

Thus a one-hot Booleanization of a fixed-depth CF presentation is naturally closer to a nonuniform **AC^0-style** constant-depth circuit with explicit table expansion than to strict bounded-fan-in NC^0.

Conversely, arbitrary AC^0 is much stronger than CF because unbounded fan-in gates can aggregate globally and bypass the bounded compositional dependency condition.

So again there is no equivalence.

---

## 7. CSP analogue: extensional/table constraints

The primitive-law part of `CF(d,f)` has a standard exact analogue in finite-domain constraint programming.

An **extensional constraint** (table constraint) represents a relation by explicitly listing its allowed or forbidden tuples. For a binary total functional law on an `s`-element domain, an exhaustive positive table necessarily contains `Theta(s^2)` input rows.

This is precisely the representation assumption used by CF4 and the Pair-Coverage Lemma.

Standard CSP literature explicitly distinguishes:

- **intensional constraints**, defined by a predicate or compact rule;
- **extensional/table constraints**, defined by listing tuples.

The HM-CFPT lower bound is therefore best understood as a lower bound in an **extensional finite-domain local-gate representation model**.

This gives a clean standard interpretation of the otherwise FCOA-specific phrase “one primitive record certifies only O(1) bottom pairs”.

---

## 8. A standard-language reformulation

Define a **bounded-depth extensional factor circuit** informally as a layered finite-domain dependency DAG satisfying:

1. constant depth `d`;
2. constant fan-in `f` at composition nodes;
3. a growing finite leaf domain `D_N`;
4. primitive local relations/functions over `D_N` represented extensionally by table tuples;
5. no global relation bypassing the dependency DAG;
6. full exposure of leaf symbols/pairs required by the target relation.

Then `CF(d,f)` is an FCOA/incidence presentation of this model.

Under this terminology, HM-CFPT becomes:

> At fixed depth and fan-in, unary/comparison organization of the unresolved leaf alphabet has extensional cost `Theta(s)`, whereas pair-complete binary transport has extensional cost `Theta(s^2)`.

Together with `s >= N^{1/f^d}`, this yields

\[
M_{bot}(AL0)=Theta(N^{1/f^d}),
\]

\[
M_{bot}(AL1)=M_{bot}(AL2)=Theta(N^{2/f^d}).
\]

This statement no longer depends on radix language.

---

## 9. Exact embedding theorem available now

### Proposition HM-STDBRIDGE

Every `CF(d,f)` presentation has an incidence DAG whose target nodes have backward light cones of depth at most `d` and branching at most `f`; hence the number of primitive dependency branches of any target node is at most `f^d`.

Primitive bottom laws are extensional finite-domain constraints.

Therefore `CF(d,f)` embeds faithfully into the category of bounded-depth bounded-fan-in finite-domain factor DAGs with extensional primitive relations.

### Proof

Take the factorisation nodes and primitive leaves of the CF presentation as DAG nodes. Direct each parent to its children. CF1 gives fan-in at most `f`, and CF depth gives path length at most `d`. CF4 identifies each primitive bottom gate with a finite relation explicitly listed by its records. CF3 guarantees that all target recovery dependencies respect this DAG rather than bypassing it. Thus the resulting factor DAG preserves exactly the allowed dependency cones and bottom relation tables. `□`

This is an exact embedding, but the destination model is a standard **combination** of circuit and CSP notions rather than a single universally named complexity class.

---

## 10. Comparison table

| Model | Bounded dependency cone? | Locality notion | Growing-domain table cost visible? | Global shortcuts allowed? | Exact match to CF? |
|---|---:|---|---:|---:|---:|
| Immersive FO transduction | not in general | strong Gaifman locality | no canonical table metric | radius-local, but neighborhoods may be huge | no |
| General FO transduction | no | local normal form + perturbation | no | yes via perturbations/coloring | no |
| Boolean NC^0 | yes | bounded fan-in light cone | no, fixed Boolean basis | no global fan-in | no, but CF1 matches |
| Boolean AC^0 | no bounded light cone | constant depth | expanded table can be represented | yes via unbounded fan-in | no |
| Extensional CSP table constraints | not a circuit model | constraint scope | yes, exactly | depends on constraint hypergraph | matches CF4 |
| Bounded-depth extensional factor circuits | yes | compositional DAG | yes | forbidden by model | **yes** |

---

## 11. Literature-facing claim ceiling

The branch should **not** state:

- “HM-CFPT is an NC^0 lower bound”;
- “CF(d,f) is the same as guarded FO”;
- “strongly local FO implies bounded fan-in”;
- “the pair-coverage theorem separates standard AC^0/NC^0 classes”.

The defensible statement is:

\[
\boxed{
\text{HM-CFPT is a size-depth tradeoff for bounded-depth extensional finite-domain factor circuits,}
}
\]

with clear analogies to NC^0 light-cone locality and strongly local FO transductions.

---

## 12. What would be needed for a genuinely standard complexity theorem

There are two promising upgrade routes.

### Route A — Boolean circuit translation

Choose a fixed Boolean encoding of bottom symbols and prove a lower bound for the resulting restricted Boolean circuit class that is invariant under encoding changes.

This would require genuine circuit lower-bound techniques; the extensional `s^2` counting argument alone is insufficient because a compact Boolean circuit may compute a highly structured table.

### Route B — standard logical locality class

Define a class of FO transductions with both:

- strongly local formulas;
- a uniform bound on the number of source elements on which each output fact can depend (a light-cone/fan-in condition).

Then prove HM-CFPT in that class. Ordinary immersive FO supplies the first condition but not the second.

The literature on FO transductions provides the right locality framework, while the bounded-dependency condition would be the extra ingredient supplied by this programme.

---

## 13. Relation to recent FO-transduction work

Braunfeld et al. (2025) prove that every FO transduction admits a local normal form involving copying, an immersive strongly-local component, and perturbation. This is directly relevant because it identifies the **immersive part** as the location where a CF-style locality restriction should be imposed.

Their framework also emphasizes that one-dimensional transductions are preferred in structural graph theory partly to avoid polynomial tuple-space blowups. This independently supports the earlier SOL-HYBRID no-go analysis of unrestricted higher-dimensional interpretations.

Thus the natural finite-model-theory reformulation of the open problem is:

\[
\boxed{
\text{Can the immersive component be refined by a bounded light-cone parameter that yields HM-CFPT-type resource lower bounds?}
}
\]

That question is now stated entirely in standard FO-transduction language plus one explicit additional resource parameter.

---

## 14. Current research verdict

The requested bridge is partially successful.

### Successful

- factorisation depth/fan-in maps cleanly to NC^0-style light-cone locality;
- primitive bottom laws map exactly to extensional CSP/table constraints;
- compositional locality is naturally compared with immersive/strongly local FO transductions;
- the HM-CFPT theorem can be reformulated without radix notation as an extensional factor-circuit theorem.

### Not successful — and this is important

There is no justified exact identification with an existing standard class such as ordinary FO transductions, guarded FO, NC^0, or AC^0.

The missing standard parameter is **bounded semantic dependency / light-cone size inside a local FO transduction**.

This is therefore not merely a terminology problem. It identifies a concrete model-theoretic research question at the interface between FO transductions and local circuit complexity.

## 15. References used for calibration

1. S. Braunfeld, J. Nešetřil, P. Ossona de Mendez, S. Siebertz, *On first-order transductions of classes of graphs*, Logical Methods in Computer Science 21(2), 2025. DOI: 10.46298/LMCS-21(2:26)2025.
2. J. Gajarský, S. Kreutzer, J. Nešetřil, P. Ossona de Mendez, M. Pilipczuk, S. Siebertz, S. Toruńczyk, *First-Order Interpretations of Bounded Expansion Classes*, ICALP 2018. DOI: 10.4230/LIPIcs.ICALP.2018.126.
3. Standard NC^0/local-computation literature; for a broad treatment see B. Applebaum, *Cryptography in Constant Parallel Time*, Springer, 2014, DOI 10.1007/978-3-642-17367-7.
4. Standard finite-domain CSP terminology: extensional/table constraints explicitly list allowed or forbidden tuples; this is the exact representation model used at the CF bottom layer.
