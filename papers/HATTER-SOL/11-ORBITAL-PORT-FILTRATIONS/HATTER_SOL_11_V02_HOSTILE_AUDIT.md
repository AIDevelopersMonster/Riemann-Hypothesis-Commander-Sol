# HATTER-SOL-11 · EN v0.2 Hostile Audit

**Target:** `HATTER_SOL_11_EN_v0.2_publication_candidate.md`  
**Audit date:** 2026-09-14  
**Status:** theorem spine passes; two local exposition repairs required before promotion to v0.3/v0.9. No central theorem is rejected.

---

## 1. Audit protocol

The candidate was tested against the branch theorem files for:

1. arithmetic scope (`Delta`, unit action, conjugation quotient);
2. exact `Omega -> Xi -> Pi` semantics;
3. fiber cardinalities and explicit realizers;
4. fixed-host versus geometry-class quantifiers;
5. connectedness of HATTER realizations;
6. parity of boundary coordinates;
7. low-capacity exceptional cases (`Q=1,2`, `S=3`);
8. critical equality case `S=d`;
9. the underfull boundary `S<d`;
10. planar lifting at orders `4,6,12`;
11. explicit icosahedral 1-factorization;
12. novelty wording relative to classical graph-factor theory.

The audit deliberately attempted to falsify the main theorem rather than merely check notation.

---

## 2. Central results that survive unchanged

### 2.1 Generic-odd geodesic theorem

The parametrization

\[
(x,y,z)=(L-t,W+t,t)
\]

and minimization of

\[
|L-t|+|W+t|+|t|
\]

at the median of `L,-W,0` are correct. The odd number of sites gives a unique median, hence a unique minimizing integer `t`.

The consequence that at least one coefficient vanishes is valid.

### 2.2 Folding theorem

The two nonzero absolute geodesic counts are the adjacent gaps among the ordered triple `L,-W,0`. Sorting them gives the previously defined pair `(P,Q)`. No additional hypothesis is being used silently.

### 2.3 Fiber cardinalities

For `P>Q>0`, modulo exchange of the two oblique slots, there are exactly three placements:

\[
(P;\{Q,0\}),\quad(Q;\{P,0\}),\quad(0;\{P,Q\}).
\]

Boundary and diagonal counts are also correct.

### 2.4 Two-node operational separation

The exact one-edge response is correct. The pure state is a singleton while both interior mixed states have two incomparable points; their minimum axial coordinates differ because `P>Q`.

### 2.5 Strict 1D theorem

The path color-count interval is correct:

- capacity zero forbids the channel;
- capacity one imposes a matching bound;
- capacity at least two imposes no local obstruction on a path.

Every realized point lies on the same total-boundary line, so the attainable set is Pareto-minimal. The permanent `3`-class conclusion for interior fibers survives.

### 2.6 Complete outerplanar class law

The proof spine survives hostile checking:

- pure `S=3` boundary floor `2` is forced by two vertices of degree at most two and attained by `G_m`;
- pure `S>=4` floor `n(S-4)+6` follows from `|E|<=2n-3` and is attained by the chain-of-triangles host `H_n` with maximum degree at most four;
- for a channel capacity `A=3`, axial floor `2` is exact;
- for `A>=4`, axial floor `n(A-4)+6` is exact;
- the floor is strictly increasing for `A>=3`;
- `Q=1,2` swapped states can attain zero axial boundary using a perfect matching or Hamiltonian cycle in `H_n`;
- therefore the unique mixed/mixed collision is `(2,1)`;
- the pure state remains distinct from both mixed states.

No additional outerplanar collision family was exposed by the audit.

### 2.7 Regular-factorizable host theorem

The theorem is correct under its written hypotheses:

- `H` connected;
- `n` even;
- `H` `d`-regular;
- a fixed 1-factorization exists;
- total local capacity `S=A+O>=d`.

The degree-window interpolation lemma is sufficient because only one channel subgraph is interpolated; the complementary channel uses all remaining host edges, and the **union of both channels is the full connected host**.

The boundary floors

\[
D=n(S-d),\quad L_A=n(A-d)_+,\quad L_O=n(O-d)_+
\]

are correct.

The domination argument above the line `B_A+B_O=D` is valid. Since `n` is even, `D,L_A,L_O,B_A,B_O` have even parity, so the interval used to choose the dominating lower-line point contains an admissible even integer whenever it is nonempty.

### 2.8 Degree filtration

For an interior fiber with `S=P+Q` and `d<=S`, the exact class count remains

\[
\boxed{
3,&d<P,\\
2,&P\le d<S,\\
1,&d=S.
}
\]

The first transition follows from equality of the mixed lower axial endpoints; the second from complete saturation at `d=S`.

### 2.9 Underfull boundary

The manuscript correctly refuses to extrapolate the theorem to `S<d`. A 1-factorization alone does not guarantee that a selected union of `S` factors is connected. The stated connected-factor criterion is sufficient and no converse is claimed.

This restriction is essential and must remain visible in the abstract/discussion.

### 2.10 Platonic planar lift

At orders `4,6,12`, the tetrahedron, octahedron, and icosahedron are planar triangulations and therefore attain the full planar edge ceiling. Thus the fixed-host total-boundary lower bound is also the geometry-class lower bound at those orders.

The lift is therefore valid.

---

## 3. Explicit computational check of the icosahedral factorization

The five matchings printed in Appendix A were checked against the stated icosahedral edge set

\[
N-u_i,\ S-v_i,\ u_i-u_{i+1},\ v_i-v_{i+1},\ u_i-v_i,\ u_i-v_{i-1}.
\]

The check confirms:

- the edge set has exactly `30` distinct edges;
- each displayed `M_i` contains exactly `6` edges;
- every `M_i` is contained in the icosahedral edge set;
- the five matchings are pairwise edge-disjoint;
- their union contains `30` edges;
- their union equals the full edge set.

Therefore the explicit icosahedral 1-factorization used for the planar theorem is internally consistent.

---

## 4. Two required local repairs

These do **not** alter any theorem statement, but they should be repaired before promotion.

### Repair A — explicit Type-III arithmetic realizer

In the proof of Theorem 4.1 the candidate currently says that the third orbital placement is realized by “an element using the two oblique directions.” This is mathematically adequate only if the reader reconstructs the earlier branch calculation.

Replace it by an explicit witness. One valid choice is

\[
\boxed{\alpha_{III}=Q-(P+Q)F.}
\]

For this element the median-geodesic calculation gives axial count zero and oblique absolute counts `P,Q`, hence

\[
\Omega(\alpha_{III})=(0;\{P,Q\}).
\]

The other two realizers may be kept as

\[
\alpha_I=P+QF,
\qquad
\alpha_{II}=Q+PF.
\]

This makes the fiber-existence part entirely self-contained.

### Repair B — state connectedness correctly in the low-`Q` outerplanar construction

In the `Q=1,2` rank-swap argument, the proof uses a perfect matching / Hamiltonian cycle for the small axial channel and the complement for the large channel.

The required HATTER connectedness condition applies to the **union of the two typed edge sets**. That union is the full chain-of-triangles host `H_n`, which is connected.

The complement of the small-channel factor need not independently be connected, and no such claim is needed.

The publication text should state explicitly:

> The two color classes partition `E(H_n)`, so their union is the connected host `H_n`; only the per-channel degree constraints, not per-channel connectedness, must be checked.

This prevents a reader from attributing an unnecessary connectivity claim to the complement.

---

## 5. Minor editorial corrections

1. In the novelty paragraph the phrase `topics [1--7]` should become `topics [1--8]` if the color-degree `b`-matching citation is retained in the same sentence.
2. Use one notation consistently for the geometry-class response: either `Z_{O,n}` / `Z_{Pl,n}` or `Z_{\mathcal C,n}` with `\mathcal C=O,Pl`.
3. Use `\bar F` consistently instead of alternating text forms such as `bar F` in prose formulas.
4. The status block should continue to call v0.2 a **publication candidate**, not a final preprint.
5. The bibliography entries H07--H10 still require final DOI/version verification before v0.9.

None of these changes affects the mathematics.

---

## 6. Novelty audit status

The graph-factor mechanism itself remains classical and should be cited as such. The closest checked literature covers:

- degree-constrained factors and minimum deficiency;
- factor decompositions reducible to edge colorings;
- `[a,b]`-factorizations;
- factors with multiple degree constraints;
- regular graph 1-factorization;
- degree-sequence optimization;
- color-degree `b`-matching.

No checked source in the preliminary search formulated the specific composition

\[
\text{arithmetic direction-orbit fiber}
\to
\text{exact Pareto network response}
\to
\text{geometry/degree-controlled collision filtration}.
\]

This remains a **negative search result**, not a proof of novelty. A specialized arithmetic-interface literature search is still required before v1.0.

---

## 7. Publication gate verdict

### Mathematical gate

**PASS, conditional on the two local exposition repairs above.**

No open theorem obligation in the large-order Gaussian planar programme is a dependency of the manuscript.

### Metadata gate

**NOT YET PASSED.** HATTER-SOL-07--10 DOI/version metadata must be verified and frozen.

### Literature gate

**NOT YET FINAL.** Preliminary graph literature boundary is adequate for v0.2, but the final novelty paragraph should wait for the specialized arithmetic-direction search.

### Current recommendation

Promote next to `EN v0.3 audited candidate`, incorporating Repairs A and B plus bibliography/notation cleanup. Do not yet create the final PDF or Zenodo record.
