# Hostile Audit — Third Strike / Finite-Carrier Arithmetic Jump

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-29  
**Verdict:** PASS after edge-case audit

## 1. Claims audited

The audit targets the theorem package in `THIRD_STRIKE_FINITE_CARRIER_ARITHMETIC_JUMP.md`:

1. definability of squarefree finite-set carriers;
2. definability of support equality and atom membership;
3. recovery of successor order from finite carriers;
4. definability of coordinate divisibility from `Add_idx` using a finite carrier;
5. application of Julia Robinson's `(Succ,Div)` definability theorem;
6. nondefinability of `Add_idx` in the decidable abstract-successor layer;
7. maximal finite-pattern recurrence separation using a computable disjunctive word and Semenov's criterion.

## 2. Squarefree carrier check

For nonempty `(A,e)`,

`(A,e) star (A,e) = (A,1)`.

Hence `(A,0)` is exactly a nonempty squarefree carrier and `(A,1)` exactly an idempotent defective element. The unit `(empty,0)` must be included separately. No state `(empty,1)` occurs in the quotient image.

Support equality via equality of squares is valid including the unit case.

Membership of an atom `p` in a squarefree carrier `X` via equality of squared supports is valid.

**Verdict:** PASS.

## 3. Successor-order check

The proposed formula says that a finite carrier containing `x,y` is forward-successor closed except at `y`.

- If `x<=y`, the finite interval `[x,y]` witnesses the formula.
- If `x>y`, forward closure from `x` never reaches `y`; therefore it forces an infinite forward chain inside a finite carrier, impossible.

No hidden appeal to transitive closure is made: the transitive effect comes from first-order quantification over an internally represented finite set.

**Verdict:** PASS.

## 4. Divisibility formula — hostile edge cases

For coordinates `a>0`, the carrier `X` is required to contain `0` and `b`, stay bounded by `b`, and be closed under `t -> t+a` whenever `t<b`.

### Case `a|b`

`X={0,a,2a,...,b}` is a witness.

### Case `a<b` and `a does not divide b`

Let `ka<b<(k+1)a`. Closure forces `(k+1)a` into `X`, contradicting boundedness by `b`.

### Case `a>b>0`

Since `0<b`, closure at `0` forces `a` into `X`, immediately contradicting boundedness.

### Case `b=0`, `a>0`

There is no element of `X` below `b=0`; `X={0}` witnesses the formula. This agrees with `a|0`.

### Case `a=0`

The closure formulation is unsuitable because `t+0=t`; this case is explicitly separated and defined by `0|b iff b=0`, matching ordinary divisibility.

Thus the formula defines exactly coordinate divisibility on `N`.

**Verdict:** PASS.

## 5. Robinson dependency check

Julia Robinson, `Definability and decision problems in arithmetic`, JSL 14 (1949), 98-114, DOI `10.2307/2266510`, explicitly states that both addition and multiplication of positive integers are first-order definable from successor and divisibility.

Our atom coordinate includes zero. The zero atom is definable as the unique atom without predecessor. Restricting Robinson's formulas to positive coordinates and treating zero by finite case distinctions gives the standard `N` version.

Therefore once coordinate divisibility is definable, coordinate multiplication and ordinary arithmetic are definable.

**Verdict:** PASS.

## 6. Decidability contradiction check

The uncoloured structure `(P0^odd; star,S)` is effectively mutually interpretable with WS1S. WS1S is decidable.

If `Add_idx` were definable there, the divisibility construction plus Robinson would define ordinary arithmetic, whose first-order theory is undecidable. Hence `Add_idx` is not definable.

The same implication applies to any finitely labelled word whose WMSO theory is decidable.

**Verdict:** PASS.

## 7. Maximal recurrence construction check

Let `B_n` concatenate all binary words of lengths at most `n` and let `w*=B_1B_2...`.

Every finite binary word `u` appears explicitly in each `B_n` for all sufficiently large `n`. Therefore every finite binary word occurs infinitely often. Since every finite factor of a binary word is itself a finite binary word, `w*` is recurrent and has full factor language `{0,1}*`.

For any effectively presented regular language `L` of finite binary words:

- if `L` is empty, no factor in `L` occurs;
- if `L` is nonempty, choose `u in L`; `u` occurs arbitrarily far out in `w*`.

Regular-language emptiness is decidable, so a recursive recurrence indicator exists. `w*` is computable. Semenov's theorem therefore gives decidable full MSO theory.

Hence maximal finite-pattern recurrence does not force coordinate addition.

**Verdict:** PASS.

## 8. Important scope restriction

The theorem does **not** prove that the actual prime-residue word `w_4` fails to define coordinate addition.

It proves:

1. complete finite-pattern recurrence alone is insufficient;
2. if `w_4` defines coordinate addition, then its recursive word predicate cannot have a recursive Semenov recurrence indicator;
3. therefore arithmetic recovery requires a stronger global synchronization property than mere local factor richness.

This restriction must remain explicit in any manuscript.

## 9. Final hostile-audit verdict

**PASS.** No fatal defect found in the Third Strike theorem package.

The central statement is now suitable for publication assembly after literature/priority positioning is completed.
