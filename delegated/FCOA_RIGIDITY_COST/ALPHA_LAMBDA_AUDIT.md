# FCOA Rigidity Cost — Audit of alpha <= lambda

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** unresolved global conjecture; strong finite evidence plus exact obstruction reduction  
**Scope:** sparse binary anonymous terminal layers  

Let

\[
\alpha(D,c)
\]

be the actual operation-cell extension cost from `ACTUAL_CELL_EXTENSION_COST.md`, and let

\[
\lambda(D,c)
\]

be the fixed-domain abstract phase-link number from `SPARSE_DOMAIN_PHASE_THEOREM.md`.

The target inequality is

\[
\boxed{\alpha(D,c)\le\lambda(D,c)\ ?}
\]

---

## 1. What has been proved

Take an optimal abstract link set

\[
L=\{(C_{i_s},C_{j_s}):1\le s\le\lambda\}
\]

between components of \(\Lambda(D)\), so every old realized non-diagonal phase signature violates at least one link equality.

For each link choose one actual bridge cell joining the two corresponding cell-incidence components, as guaranteed by the One-Cell Bridge Lemma.

Let the resulting extension be

\[
D'=D\cup E,
\qquad |E|=\lambda.
\]

### No-old-obstruction lemma

If

\[
g\in\operatorname{Aut}(G;D',Q_{D'})
\]

also preserves the old domain D setwise, then g is automatically a full anonymous automorphism of the extended colored layer.

### Reason

Restriction of g to D lies in the old ternary reduct group \(A_Q(D,c)\). Every bridge merges the linked pair of old phase components, so the old component phase signature of g satisfies every equality in L. Optimality of L means that every old realized signature satisfying all links is diagonal. Therefore g preserves all old colors or globally swaps them; the bridge-cell phase is forced to agree inside the merged incidence components, so the same global phase extends across E.

Hence any failure of exactness after a lambda-cell bridge realization must be caused by an automorphism which does **not** preserve D setwise.

Therefore:

\[
\boxed{
\alpha>\lambda
\Longrightarrow
\text{every lambda-cell realization creates a genuinely new bad carrier symmetry.}
}
\]

This isolates the only possible obstruction.

---

## 2. Symmetry creation under domain extension is real

Domain automorphism groups are not monotone under cell addition.

Already on three carrier points,

\[
D=\{(0,1)\}
\]

has trivial carrier automorphism group, while adding

\[
(2,1)
\]

gives

\[
D'=\{(0,1),(2,1)\}
\]

with a new transposition

\[
(0\ 2).
\]

So the obstruction identified above cannot be dismissed abstractly: adding a cell really can make the domain more symmetric.

However, in all audited binary phase instances so far, such newly created domain symmetries either remain globally color-admissible or some alternative extension of the same size avoids them.

---

## 3. Exhaustive finite audit at n=4

All surjective partial binary colorings of the 12 ordered off-diagonal cells on four carrier points were exhaustively enumerated.

Total audited layers:

\[
\boxed{523250.}
\]

Observed pairs \((\lambda,\alpha)\):

\[
\boxed{
(0,0),\quad(1,1),\quad(2,1).
}
\]

Exact counts:

- `(0,0)`: 522398 layers;
- `(1,1)`: 804 layers;
- `(2,1)`: 48 layers.

No case with

\[
\alpha>\lambda
\]

occurs at n=4.

In particular, the inequality holds for every four-point sparse binary layer.

---

## 4. Systematic sparse audit at n=5

A complete audit was performed for all surjective binary layers on five carrier points with at most five defined ordered cells, modulo the harmless global binary complement normalization used by the verifier.

Total audited layers:

\[
\boxed{270085.}
\]

Layers with \(\lambda>0\):

\[
\boxed{10640.}
\]

Observed positive cases include only

\[
(\lambda,\alpha)=(1,1)
\]

and

\[
(\lambda,\alpha)=(2,1).
\]

No counterexample occurs in this entire sparse sector.

Additional targeted random searches on n=5 and n=6 likewise found no \(\alpha>\lambda\) case.

These computations are evidence only beyond the fully enumerated sectors.

---

## 5. What remains unproved

The missing global step is a **safe bridge theorem**:

> Given an optimal abstract link system of size lambda, can one always choose lambda actual bridge cells and their binary values so that no genuinely new non-diagonal carrier symmetry is created?

A naive monotonicity proof is impossible because domain automorphism groups can increase after adding cells.

A naive color-choice proof is also false: finite examples exist in which both color assignments to a particular added cell enlarge the reduct automorphism group relative to the old one.

Therefore any proof of alpha <= lambda must use a more global selection principle over bridge positions, not merely choose colors locally.

---

## 6. Current theorem status

The unconditional statements remain

\[
\boxed{
\alpha(D,c)\le\mu(D)\le\kappa(\Lambda(D))-1,
}
\]

and

\[
\boxed{
\lambda(D,c)\text{ can exceed }\alpha(D,c)\text{ by an unbounded factor}.
}
\]

The new finite audit establishes

\[
\boxed{
\alpha(D,c)\le\lambda(D,c)
\quad\text{for every }|G|\le4,
}
\]

and for every audited five-point layer with at most five defined cells.

The global inequality

\[
\boxed{
\alpha(D,c)\le\lambda(D,c)
}

remains a **supported conjecture, not a theorem**.

---

## 7. Minimal-counterexample consequences

If a counterexample exists, then necessarily:

1. \(|G|\ge5\);
2. in the fully audited five-point sparse sector it must have at least six defined cells;
3. \(\lambda\ge1\);
4. every size-lambda bridge realization must create at least one new bad automorphism not preserving the old domain D;
5. the counterexample mechanism is therefore genuinely `symmetry creation under extension`, not failure to kill the old realized phase cocycle.

This sharply narrows the search space.

---

## 8. Recommended next attack

The next proof-oriented route is to study **one-cell deletion decks** of the extended domain.

For a lambda-cell bridge extension D', any genuinely new automorphism must send at least one new bridge cell into the old domain. Equivalently, D is isomorphic to a different lambda-cell deletion of D'.

Thus a counterexample is tied to a reconstruction-type ambiguity:

\[
\boxed{
D'\setminus E
\cong
D'\setminus E'
\quad\text{for some }E'\ne E,
}
\]

combined with a non-diagonal phase cocycle on D'.

This reframes the remaining problem from unrestricted phase synchronization to a much narrower **colored deletion-symmetry problem**.

---

## 9. Claim firewall

1. No global theorem alpha <= lambda is claimed.
2. The n=4 statement is exhaustive.
3. The n=5 statement is exhaustive only through five defined cells; larger five-point domains were not fully enumerated.
4. Random n=5/n=6 searches are evidence only.
5. The No-old-obstruction lemma is theorem-level and isolates the only possible failure mechanism.
6. Nothing here changes the status of G4.