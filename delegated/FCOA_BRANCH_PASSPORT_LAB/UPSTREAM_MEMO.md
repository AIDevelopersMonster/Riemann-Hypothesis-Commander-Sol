# FCOA Branch Passport Laboratory — Upstream Memo

**Rounds:** P0–P4  
**Audience:** main Commander Sol scientific director

## U4-01 — EXACT OUTPUT-CARDINALITY THRESHOLD PROVED

P4 closes the minimality question exposed by P3.

For a pure terminal-output partial operation with singleton output set

`O={Omega}`,

every defined cell has the same value. Hence the operation is exactly the characteristic partial operation of its definedness relation:

`x star y = Omega <=> D_star(x,y)`.

Therefore every active-sort definedness automorphism automatically extends uniquely across the singleton output, and every full-operation automorphism restricts to a definedness automorphism. Thus

`pi_X Aut(star)=Aut(D_star|X)`

and

`VRI(star)=1`.

This remains true over an arbitrary already fixed backbone `B`: a singleton terminal-output layer can add rigidity through its domain geometry, but cannot add any extra value-induced rigidity beyond that domain.

Combined with P3, where exactly two terminal outputs give

`VRI=n!/2`,

we obtain the exact threshold:

> **Two terminal outputs are necessary and sufficient for nontrivial value-induced rigidity in the pure terminal-output setting, and already sufficient for factorial amplification.**

Equivalently:

`|O|=1 => VRI=1`,

while

`|O|=2 => VRI can grow as n!/2`.

The anchored P3 variant further gives a rigid full operation with the same two outputs and

`VRI=(n-1)!`.

## U4-02 — Interpretation of G2 clarified

This theorem does not say a one-output construction cannot become rigid. G2 shows it can: a singleton output placed on a directed path compiles rigid information into the **domain**.

P4 says the value itself contributes no additional rigidity after definedness is retained. Thus G2 is a clean example of domain-induced rigidity, whereas P3 is the first cardinality level at which genuinely value-induced rigidity is possible.

This distinction should be incorporated into the branch passport vocabulary.

## U4-03 — One-sorted caveat

For a one-sorted presentation, active/output carrier separation must either be named or internally recoverable. A sufficient intrinsic condition is that every base element occurs as an operation argument and the singleton terminal output does not. Under that condition the same active-sort collapse theorem holds.

If inactive base elements exist, full one-sorted definedness may gain carrier-mixing automorphisms. That is a sorting effect, not value-induced rigidity, and must not be counted as VRI.

## U3-01 — ABSOLUTE TWO-OUTPUT FACTORIAL AMPLIFICATION

P3 constructs `X_n={x_1,...,x_n}` with total terminal-output carrier exactly `O={Omega_+,Omega_-}` and

`x_i star x_j=Omega_+` for `i<j`,

`x_i star x_j=Omega_-` for `i>j`,

with diagonal undefined. Then

`Aut(D|X_n) ~= S_n`,

`Aut(star) ~= C2`,

and

`VRI=n!/2`.

A one-cell diagonal anchor retains exactly two total outputs, gives `Aut(D_A|X_n) ~= S_{n-1}`, destroys reversal, and yields `Aut(star_A)=1`, `VRI=(n-1)!`.

Formula-blind enumeration for `n=3..7` agrees exactly.

## U2-01 — G4 scope repair remains required

The pure P3/P4 theorem does not change the accounting of M0-relative G4. G4 has growing inherited `E_i^*`,`E_i^x` families and therefore does not itself have bounded total output cardinality. Its safe formulation remains a fixed two-value **added** orientation layer over M0.

## Director recommendation

The P3+P4 pair is now a coherent theorem package suitable for upstream mathematical integration:

1. **One-Output Collapse Theorem:** singleton value layers have `VRI=1`;
2. **Pure Two-Output Amplification Theorem:** two outputs permit `VRI=n!/2`;
3. **Exact Two-Output Minimality Theorem:** two is the sharp output-cardinality threshold for positive and factorial VRI;
4. anchored two-output variant: full rigidity with `VRI=(n-1)!`.

This package has a cleaner theorem boundary than G4 itself and should be kept conceptually separate from the M0-relative construction.

The next genuinely open direction is no longer cardinality minimality. It is extremality: for fixed `n` and exactly two anonymous outputs, how large can VRI be, and can the `n!/2` construction be improved to `n!` without naming either output or importing external structure?
