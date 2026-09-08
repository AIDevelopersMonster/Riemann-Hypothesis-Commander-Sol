# Zeckendorf Event Compression — Optimal Linear Generated AL1

**Project:** FCOA Admissibility Geometry  
**Date:** 2026-08-30  
**Status:** central theorem checkpoint; proof complete, independent hostile audit recommended before publication promotion  
**Depends on:** `HOSTILE_AUDIT_ZECKENDORF_SELECTIVE_MEMORY.md`, `BASE_SORT_LINEAR_SUPPORT_BARRIER.md`  
**Scope:** explicit ordered base carrier, fixed finite signature, prefix-generated history, ordinary FO query language

---

## 1. Central problem

The hostile-audited Zeckendorf history gives a provenance-safe exact-AL1 witness with

\[
|Z_m|=\Theta(m\log m).
\]

The remaining optimization question is whether the full row-by-row digit incidence is necessary.

It is not.

The history can be replaced by its **change events**. Because Zeckendorf successor creates exactly one new `1` digit at each increment, while deleted `1` digits telescope against the Zeckendorf weight count, the total event support is not merely subquadratic but exactly linear:

\[
\boxed{
|E_m|=2m-2-s_F(m-1)=\Theta(m).
}
\]

The event structure is FO-interdefinable with the full Zeckendorf incidence structure. Hence it still uniformly defines truncated addition and EqGap, and still does not uniformly define multiplication.

Combined with the already proved Base-Sort Linear Support Barrier, this reaches the optimal support scale:

\[
\boxed{
C_{AL1}^{\rm generated,base}(m)=\Theta(m)
}
\]

inside the declared generated-history/base-sort model.

---

## 2. Zeckendorf notation

Use shifted Fibonacci weights

\[
F_0=1,\qquad F_1=2,\qquad F_{j+2}=F_{j+1}+F_j.
\]

Every natural number has a unique canonical representation

\[
n=\sum_j\varepsilon_j(n)F_j,
\qquad
\varepsilon_j(n)\in\{0,1\},
\qquad
\varepsilon_j(n)\varepsilon_{j+1}(n)=0.
\]

Let

\[
s_F(n):=\sum_j\varepsilon_j(n)
\]

be its number of `1` digits.

The hostile-audited full incidence relation is

\[
Z(n,p)
\iff
p=F_j\text{ and }\varepsilon_j(n)=1.
\]

Carrier subscripts are omitted; all numerical equalities in this section are metamathematical correctness statements about the generated family.

---

## 3. Differential event relations

For `n>0`, define two binary event relations on the same base carrier:

\[
U(n,p)
\iff
Z(n,p)\land\neg Z(n-1,p),
\tag{3.1}
\]

\[
D(n,p)
\iff
\neg Z(n,p)\land Z(n-1,p).
\tag{3.2}
\]

`U` means that digit column `p` changes from `0` to `1`; `D` means `1` to `0`.

For the zero row no event is stored.

The final static event structure is

\[
\mathfrak E_m=([m],<,U,D).
\]

No full `Z` table is retained as a primitive relation.

---

## 4. Exact successor-change lemma

The key combinatorial fact is stronger than an average-case estimate.

### Lemma 4.1 — one-up Zeckendorf successor

For every `n>=1`, the transition from the canonical representation of `n-1` to that of `n` changes exactly one digit from `0` to `1`.

Equivalently,

\[
\boxed{
|\{p:U(n,p)\}|=1.
}
\tag{4.1}
\]

### Proof

Let `F_j` be the least Fibonacci summand in the canonical representation of `n`:

\[
n=H+F_j,
\]

where every summand in `H`, if any, has index at least `j+2`.

For `j=0`,

\[
F_0-1=0.
\]

For `j>=1`, the elementary Fibonacci identity is

\[
F_j-1
=
F_{j-1}+F_{j-3}+F_{j-5}+\cdots,
\tag{4.2}
\]

ending at `F_0` or `F_1` according to parity.

The summands on the right of (4.2) are pairwise nonconsecutive. The largest is `F_{j-1}`, while every summand of `H` has index at least `j+2`; hence the union remains a canonical Zeckendorf representation.

Therefore

\[
n-1
=
H+(F_j-1)
\]

has exactly the same higher summands `H` as `n`, but replaces the single summand `F_j` by the alternating lower summands in (4.2).

Passing from `n-1` to `n` therefore:

1. deletes some lower `1` digits;
2. creates the single digit `F_j`;
3. leaves all higher digits unchanged.

Thus exactly one `0->1` event occurs. `□`

### Remark 4.2

The lemma also gives a transparent successor rule independent of the internal states of any particular normalization transducer. It is compatible with the self-anchored finite-state generator proved in `HOSTILE_AUDIT_ZECKENDORF_SELECTIVE_MEMORY.md`.

---

## 5. Exact linear event count

For increment `n-1 -> n`, let

\[
d_n:=|\{p:D(n,p)\}|
\]

be the number of deleted `1` digits.

By Lemma 4.1, one new `1` is created. Therefore

\[
s_F(n)-s_F(n-1)=1-d_n,
\]

so

\[
d_n=1+s_F(n-1)-s_F(n).
\tag{5.1}
\]

Summing from `n=1` to `m-1` telescopes:

\[
\sum_{n=1}^{m-1}d_n
=(m-1)+s_F(0)-s_F(m-1).
\]

Since

\[
s_F(0)=0,
\]

we obtain

\[
\boxed{
|D_m|=m-1-s_F(m-1).
}
\tag{5.2}
\]

Lemma 4.1 gives

\[
\boxed{|U_m|=m-1.}
\tag{5.3}
\]

Hence the total primitive event support is exactly

\[
\boxed{
|U_m|+|D_m|
=2m-2-s_F(m-1).
}
\tag{5.4}
\]

As

\[
0\le s_F(m-1)=O(\log m),
\]

we conclude

\[
\boxed{
|U_m|+|D_m|=2m+O(\log m)=\Theta(m).
}
\tag{5.5}
\]

This is a factor-`Theta(log m)` compression relative to the full positive digit-incidence relation.

---

## 6. FO recovery of the full Zeckendorf history

Define

\[
Event(t,p):=U(t,p)\lor D(t,p).
\]

For a time/row `x` and digit column `p`, say that `t` is the latest event at `p` not after `x`:

\[
Latest(t,p,x)
:\iff
Event(t,p)
\land t\le x
\land
\neg\exists u\,
(Event(u,p)\land t<u\le x).
\tag{6.1}
\]

All order comparisons are available in the AL0 background.

Now define

\[
\widehat Z(x,p)
:\iff
\exists t\,[Latest(t,p,x)\land U(t,p)].
\tag{6.2}
\]

### Theorem 6.1 — exact reconstruction

For every finite prefix and every `x,p<m`,

\[
\boxed{
\widehat Z(x,p)\iff Z(x,p).
}
\]

### Proof

A digit starts at `0`. Its value changes only at the stored `U` or `D` events. Hence at row `x` its current value is `1` exactly when its latest change not after `x` is a `0->1` event. Formula (6.2) states precisely this condition. `□`

Thus

\[
\boxed{
Z\in FO(<,U,D).
}
\tag{6.3}
\]

The diagonal Fibonacci anchor predicate is therefore recovered as

\[
FibPos(p)\iff\widehat Z(p,p).
\]

In fact a stronger direct identity holds:

\[
FibPos(p)\iff U(p,p),
\]

because a new Fibonacci weight first appears as the unique new top digit exactly at its own carrier point.

---

## 7. Reverse FO definition of the events

Let

\[
Pred(y,x)
\]

mean that `y<x` and no point lies strictly between them. This is FO-definable from `<`.

Then for `x>0`,

\[
U(x,p)
\iff
Z(x,p)
\land
\exists y[Pred(y,x)\land\neg Z(y,p)],
\tag{7.1}
\]

\[
D(x,p)
\iff
\neg Z(x,p)
\land
\exists y[Pred(y,x)\land Z(y,p)].
\tag{7.2}
\]

Therefore

\[
\boxed{
(U,D)\in FO(<,Z).
}
\tag{7.3}
\]

Combining (6.3) and (7.3):

### Theorem 7.1 — FO interdefinability

The finite families

\[
([m],<,Z)
\]

and

\[
([m],<,U,D)
\]

are uniformly first-order interdefinable.

Hence they have exactly the same uniform FO-definable base-sort relations.

This is stronger than merely saying that both define addition.

---

## 8. Exact arithmetic phase

The hostile audit of the full Zeckendorf family established:

\[
Add,EqGap\in FO(<,Z),
\]

while

\[
Mul\notin FO(<,Z)
\]

uniformly on finite prefixes.

By Theorem 7.1, substitute the FO reconstruction of `Z` from `(U,D)` into the fixed addition formula. Hence

\[
\boxed{
Add,EqGap\in FO(<,U,D).
}
\tag{8.1}
\]

If multiplication were uniformly FO-definable from `(U,D)`, then replacing `U,D` by their definitions (7.1)-(7.2) would uniformly define multiplication from `Z`, contradicting the hostile-audited Zeckendorf separation.

Therefore

\[
\boxed{
Mul\notin FO(<,U,D).
}
\tag{8.2}
\]

Thus the differential history is exact AL1:

\[
\boxed{FTR(\mathfrak E)=1.}
\tag{8.3}
\]

---

## 9. Generator provenance

The event representation does not require an external arithmetic table.

Use the self-anchored prefix generator from `HOSTILE_AUDIT_ZECKENDORF_SELECTIVE_MEMORY.md`. When producing the next Zeckendorf row, compare each emitted digit with the previous current digit:

- emit `U(n,p)` if `0->1`;
- emit `D(n,p)` if `1->0`;
- emit nothing if the digit is unchanged.

The generator may maintain the current Zeckendorf word as transient working state, or equivalently recover the current value of a digit from the latest previously materialized event while scanning the generated history.

Only change events are retained in the final FCOA structure.

The rule is:

- prefix-consistent;
- independent of final `m`;
- based on fixed finite-state Zeckendorf successor normalization plus the growing digit coordinate already justified by the self-anchor invariant;
- free of numerical rank, addition, multiplication, EqGap, Fibonacci-index and arbitrary size oracles.

### Resource distinction

The final materialized support is `Theta(m)`. The generator itself has a growing current-word workspace of `O(log m)` bits (or may rescan prior events). This transient generator workspace is not silently identified with materialized FCOA support and must be recorded separately in any resource passport.

Hence the correct statement is not “finite-state unary generation”; it is:

\[
\boxed{
\text{self-anchored row-recursive finite-control generation with }O(\log m)\text{ transient workspace}.}
\]

This remains outside the unary `AL-FS` class and inside the generated-history route of the Closure-Placement Principle.

---

## 10. Optimality from the Base-Sort Linear Support Barrier

`BASE_SORT_LINEAR_SUPPORT_BARRIER.md` proves the following broad theorem.

For an explicit ordered `m`-element base carrier, one fixed finite bounded-arity added signature, ordinary FO query language, and all added primitive tuples charged, uniform recovery of canonical truncated addition requires

\[
\boxed{\Omega(m)}
\]

added support.

The theorem permits the added relations to vary arbitrarily with `m`; therefore it certainly applies to the narrower provenance-safe generated family constructed here.

Our event history supplies the matching upper bound

\[
\boxed{O(m)}.
\]

Hence:

### Theorem 10.1 — Optimal Generated Base-Sort AL1 Support

Within the declared model

- explicit ordered base carrier `[m]`;
- fixed finite bounded-arity primitive signature;
- no uncharged growing auxiliary carrier;
- ordinary FO query language;
- materialized primitive tuples charged;
- prefix-consistent self-anchored generated histories allowed;

exact AL1 has optimal support scale

\[
\boxed{
C_{AL1}^{\rm generated,base}(m)=\Theta(m).
}
\tag{10.1}
\]

The lower bound is representation-independent within this model; the upper bound is realized by Zeckendorf change events.

---

## 11. Density-Leakage Orthogonality strengthened again

The central line now contains three especially informative presentations:

\[
\begin{array}{c|c|c}
\text{memory} & \text{support} & \text{phase}\\
\hline
\text{direct Add graph} & \Theta(m^2) & AL1\\
\text{full Zeckendorf digit history} & \Theta(m\log m) & AL1\\
\text{Zeckendorf event history} & \Theta(m) & AL1\\
\text{binary full digit history} & \Theta(m\log m) & AL2
\end{array}
\]

Moreover, the same differential trick applied to binary counting would compress materialized BIT changes to `Theta(m)` while preserving FO-recoverability of BIT, and therefore would still be AL2.

So even at the **same optimal linear support scale**, a generated history can occupy different arithmetic phases:

\[
\boxed{
\Theta(m)\text{ support does not determine }AL1\text{ versus }AL2.
}
\]

This moves the phase separator decisively away from scalar density.

---

## 12. Closure-placement interpretation

The full Zeckendorf table stored every historical state. The event representation stores only the **discrete derivative** of that history.

FO then performs temporal integration by taking the latest event in a digit column.

Thus:

\[
\boxed{
\text{row history}
\longrightarrow
\text{change-event derivative}
\longrightarrow
\text{FO latest-event integration}.
}
\]

The missing unbounded information has not disappeared. It is represented sparsely by the event chronology, and linear order lets FO reconstruct persistent state.

This suggests a general FCOA compression principle:

> If a generated state history changes only amortized `O(1)` primitive features per carrier step, and current feature values are determined by their latest change events, then full history may admit linear event materialization without reducing uniform FO query power.

This principle is working terminology/theory until abstracted and hostile-audited separately.

---

## 13. New central frontier

The support optimization problem for base-sorted generated exact AL1 is now closed at the asymptotic level:

\[
\boxed{\Theta(m).}
\]

Therefore the next central question should **not** ask whether exact AL1 can be compressed further in this model; the Base-Sort Linear Support Barrier forbids `o(m)`.

The next genuinely structural questions are:

1. **Phase separator at equal linear cost.** What intrinsic property distinguishes linear event histories that are exact AL1 from linear event histories that expose BIT/AL2?
2. **Interpretation-invariant resource.** Can that separator be defined independently of a chosen digit/event presentation?
3. **Generator complexity lower bound.** What minimum transient workspace / recurrence width / synchronization width is required to cross from `AL-FS` to exact AL1 when final support is already optimal `Theta(m)`?
4. **Event-Compression Theorem.** Abstract the latest-event mechanism and identify necessary/sufficient hypotheses for FO-preserving differential compression of generated histories.
5. **Automatic versus arithmetic phase.** Determine whether decidable/automatic infinite envelopes provide a robust sufficient firewall against AL2 for prefix-generated exact-AL1 memories.

The strongest immediate strike is (1): compare the linear differential Zeckendorf history with the linear differential binary/BIT history and isolate the invariant that makes one exact AL1 and the other AL2.

---

## 14. Status ledger

Proved in this note, conditional only on the already hostile-audited Zeckendorf exact-AL1 theorem and the existing Base-Sort Linear Support Barrier:

\[
\boxed{\mathbf F:\ \text{each Zeckendorf increment has exactly one }0\to1\text{ digit event}.}
\]

\[
\boxed{\mathbf F:\ |U_m|+|D_m|=2m-2-s_F(m-1)=\Theta(m).}
\]

\[
\boxed{\mathbf F:\ ([m],<,Z)\text{ and }([m],<,U,D)\text{ are uniformly FO-interdefinable}.}
\]

\[
\boxed{\mathbf F:\ \text{event history is exact }AL1.}
\]

\[
\boxed{\mathbf F:\ C_{AL1}^{\rm generated,base}(m)=\Theta(m)\text{ in the declared model}.}
\]

Working/open:

\[
\boxed{\mathbf O:\ \text{equal-linear-cost intrinsic separator between AL1 and AL2 generated histories}.}
\]

\[
\boxed{\mathbf W:\ \text{general Event-Compression / FO latest-event integration principle}.}
\]

No claim is made here for models with uncharged growing auxiliary carriers, stronger query logics, growing arity, or compressed-program cost conventions.