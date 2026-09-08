# FCOA Rigidity Cost — Beta-One Danger Saturation Theorem

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication theorem note plus targeted seven-carrier stress evidence.

## 1. Setup

Assume

\[
\beta(D,c)=1.
\]

Let

\[
W_{\rm kill}(D,c)
\]

be the set of undefined cells whose singleton addition kills every old bad automorphism.

Let

\[
R_1(D)
\]

be the one-cell replacement boundary from `REPLACEMENT_BOUNDARY_THEOREM.md`.

Let

\[
A^-(D,c)
\]

be the old globally anonymous automorphisms with global phase 1.

Call an undefined cell `e` **isolated relative to D** if it is an isolated vertex of

\[
\Lambda(D\cup\{e\}).
\]

Define the isolated phase trap

\[
\boxed{
F_-(D,c)=
\{e\notin D:
 e\text{ is isolated and }
 \exists g\in A^-(D,c),\ ge=e
\}.
}
\]

Finally define the one-cell danger set

\[
\boxed{
\mathcal D_1(D,c)=R_1(D)\cup F_-(D,c).
}
\]

## 2. Escape theorem

### Theorem 2.1 — Beta-One Escape

If

\[
\boxed{
W_{\rm kill}(D,c)\nsubseteq\mathcal D_1(D,c),
}
\]

then

\[
\boxed{\alpha(D,c)=\beta(D,c)=1.}
\]

### Proof

Choose

\[
e\in W_{\rm kill}(D,c)\setminus\mathcal D_1(D,c).
\]

Since `e notin F_-`, either `e` is anchored to an old incidence component or it is isolated but fixed by no old global phase-1 automorphism. By `BETA_ONE_PHASE_SAFE_CELL.md`, every enlarged-reduct automorphism preserving the old domain is therefore globally anonymous.

Since `e notin R_1(D)`, the Replacement Boundary Theorem rules out every automorphism of the one-cell enlarged domain that moves `D`.

Thus no bad automorphism survives or is created. The singleton extension is exact, so `alpha<=1`. Nonexactness of the original layer and `beta=1` give `alpha>=beta=1`. Hence `alpha=beta=1`. `square`

## 3. Necessary danger-saturation condition

### Corollary 3.1

Any counterexample to

\[
\beta=1\Longrightarrow\alpha=1
\]

must satisfy

\[
\boxed{
W_{\rm kill}(D,c)\subseteq\mathcal D_1(D,c).
}
\]

Call such a layer **beta-one danger-saturated**.

This is a strict strengthening of replacement saturation. Every beta-killing singleton must be trapped by at least one of two independent mechanisms:

1. **replacement danger:** `e in R_1(D)`, so a defect-1 domain replacement symmetry is geometrically possible;
2. **isolated phase danger:** `e in F_-(D,c)`, so an old global phase-1 automorphism can survive on `D` while fixing the isolated new cell with phase 0.

No other one-cell obstruction exists.

## 4. Consequence for anchored cells

Every anchored beta-killing cell is automatically phase-safe. Therefore a beta-one counterexample must satisfy

\[
\boxed{
W_{\rm kill}^{\rm anchored}(D,c)\subseteq R_1(D).
}
\]

Thus all anchored escape cells must be replacement-completion cells of the old definedness domain.

This is a strong domain-level saturation requirement.

## 5. Consequence when no old global swap exists

If

\[
A^-(D,c)=\varnothing,
\]

then

\[
F_-(D,c)=\varnothing
\]

and therefore any beta-one counterexample must satisfy the simpler condition

\[
\boxed{
W_{\rm kill}(D,c)\subseteq R_1(D).
}
\]

So in the absence of old global color-swapping symmetries, the only possible one-cell obstruction is deletion/replacement ambiguity of the domain.

## 6. Seven-carrier targeted stress audit

A new independent C++ search tested **300,000** random seven-carrier sparse binary layers. The generator was deliberately biased toward moderate-density and partially symmetrized domains rather than uniform generic domains, because positive overhead is expected only near unusually symmetric definedness structures.

The search found

\[
\boxed{4,024}
\]

nonexact layers with

\[
\beta=1.
\]

For every one of those 4,024 layers:

- a one-cell exact repair exists;
- more strongly, the beta-killing set is **not** danger-saturated:
  \[
  W_{\rm kill}\nsubseteq\mathcal D_1;
  \]
- therefore exactness follows from Theorem 2.1 for an explicit escape cell.

Observed count of danger-saturated beta-one layers:

\[
\boxed{0}.
\]

Observed count of `beta=1<alpha` layers:

\[
\boxed{0}.
\]

This is targeted stress evidence, not an exhaustive seven-carrier theorem.

## 7. Current beta-one proof target

The global theorem

\[
\boxed{\beta=1\Longrightarrow\alpha=1}
\]

is now reduced to a sharper combinatorial statement:

> **Danger-Saturation Exclusion Problem.** Can a finite sparse binary anonymous layer with `beta=1` satisfy
> \[
> W_{\rm kill}(D,c)\subseteq R_1(D)\cup F_-(D,c)?
> \]
> and still remain nonexact under both colors for every beta-killing cell?

A proof that danger saturation itself is impossible would settle the beta-one theorem immediately.

A weaker proof is also sufficient: show that every danger-saturated layer has at least one cell inside the danger set for which one of the two binary values makes every replacement symmetry globally anonymous.

## 8. Relation to the global alpha=beta conjecture

If the beta-one theorem is proved, every counterexample to

\[
\alpha=\beta
\]

must satisfy

\[
\boxed{\beta\ge2.}
\]

Combined with the two-component theorem, it must also have

\[
\boxed{\kappa(\Lambda(D))\ge3.}
\]

This would move the entire unresolved problem into the genuinely multi-cell regime.

## Claim firewall

1. The escape theorem is theorem-level.
2. The 300,000-state seven-carrier audit is targeted randomized evidence, not exhaustive.
3. Membership in `R_1(D)` or `F_-(D,c)` does not by itself imply that the corresponding singleton extension is unsafe; the danger set is necessary, not sufficient, for a beta-one counterexample.
4. The global beta-one theorem remains open.
