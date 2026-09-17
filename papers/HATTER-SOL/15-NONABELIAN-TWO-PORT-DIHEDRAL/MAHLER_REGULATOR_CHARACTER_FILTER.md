# HATTER-SOL-15 · Mahler Regulator Character Filter

**Status:** exact theorem layer for the natural Mahler regulator form and for the rationalized Milnor `K_2` symbol.  
**Main consequence:** the natural Mahler observer is supported in the single `abc` character sector of the multiquadratic spectral curve. The three elliptic Kani–Rosen factors are invisible to this observer at the regulator-character level.

## 1. Setup

Continue with the multiquadratic mirror-channel spectral curve

\[
K(C)=K(u)\bigl(\sqrt a,\sqrt b,\sqrt c\bigr),
\]

where

\[
a=u^2-4,\qquad b=Q(u),\qquad c=Q(u)-4.
\]

Write

\[
z=\frac{u+\sqrt a}{2},
\qquad
w=\frac{\sqrt b+\sqrt c}{2}.
\]

Then

\[
z+z^{-1}=u,
\qquad
w+w^{-1}=\sqrt b.
\]

Let

\[
G=\langle \sigma_a,\sigma_b,\sigma_c\rangle\cong(C_2)^3
\]

act by independent sign changes of the three square roots.

The induced action on the torus coordinates is

\[
\boxed{\sigma_a:z\mapsto z^{-1},\quad w\mapsto w,}
\]

\[
\boxed{\sigma_b:z\mapsto z,\quad w\mapsto-\,w^{-1},}
\]

\[
\boxed{\sigma_c:z\mapsto z,\quad w\mapsto w^{-1}.}
\]

Indeed,

\[
\frac{-\sqrt b+\sqrt c}{2}=-w^{-1},
\qquad
\frac{\sqrt b-\sqrt c}{2}=w^{-1}.
\]

## 2. The natural Mahler regulator form

On the smooth locus away from zeros and poles of `z,w`, define

\[
\eta(z,w)
=
\log|z|\,d\arg w
-
\log|w|\,d\arg z.
\]

This is the standard real regulator 1-form attached to the Milnor symbol `\{z,w\}`.

Let `chi_abc` be the character of `G` defined by

\[
\chi_{abc}(\sigma_a)
=
\chi_{abc}(\sigma_b)
=
\chi_{abc}(\sigma_c)
=-1.
\]

### Theorem H15.59 — pure `abc` character of the Mahler form

For every `g in G`,

\[
\boxed{g^*\eta=\chi_{abc}(g)\eta.}
\]

Equivalently,

\[
\boxed{
\sigma_a^*\eta
=
\sigma_b^*\eta
=
\sigma_c^*\eta
=-\eta.
}
\]

#### Proof

Under `z -> z^{-1}` both `log|z|` and `d arg z` change sign, while the `w` terms are fixed. Hence `eta -> -eta`.

Under `w -> w^{-1}`, both `log|w|` and `d arg w` change sign, while the `z` terms are fixed. Hence again `eta -> -eta`.

Under `w -> -w^{-1}`, the factor `-1` changes `arg w` only by a locally constant `pi`; therefore

\[
d\arg(-w^{-1})=-d\arg w,
\qquad
\log|-w^{-1}|=-\log|w|,
\]

and once more `eta -> -eta`.

Since the three involutions generate `G`, the full character law follows. QED.

## 3. Character projector

For a character `chi` of `G`, let

\[
e_\chi
=\frac1{8}\sum_{g\in G}\chi(g)g^*.
\]

### Corollary H15.60 — exact projector selection

\[
\boxed{e_{abc}\eta=\eta,}
\]

while for every other character `psi != chi_abc`,

\[
\boxed{e_\psi\eta=0.}
\]

Thus the natural Mahler regulator form is not a mixture of the four positive-genus Jacobian sectors. It is a single character vector.

## 4. Vanishing on the three elliptic quotients

The three elliptic quotient fields are

\[
K(E_{ab})=K(u,\sqrt{ab}),
\quad
K(E_{ac})=K(u,\sqrt{ac}),
\quad
K(E_{bc})=K(u,\sqrt{bc}).
\]

Their quotient subgroups are

\[
H_{ab}=\ker\chi_{ab},
\qquad
H_{ac}=\ker\chi_{ac},
\qquad
H_{bc}=\ker\chi_{bc}.
\]

Now `sigma_c in H_ab`, `sigma_b in H_ac`, and `sigma_a in H_bc`, while each of these involutions sends `eta` to `-eta`.

Therefore subgroup averaging cancels exactly.

### Theorem H15.61 — elliptic pushforward annihilation

For the quotient maps

\[
\pi_{ab}:C\to E_{ab},
\quad
\pi_{ac}:C\to E_{ac},
\quad
\pi_{bc}:C\to E_{bc},
\]

the trace/pushforward of the natural regulator form vanishes:

\[
\boxed{
(\pi_{ab})_*\eta
=(\pi_{ac})_*\eta
=(\pi_{bc})_*\eta
=0.
}
\]

Hence the three elliptic factors in

\[
J(C)\sim E_{ab}\times E_{ac}\times E_{bc}\times J(C_{abc})
\]

are spectrally present but are not seen by the natural Mahler regulator observer.

## 5. Descent to the genus-two quotient

The genus-two quotient is

\[
C_{abc}:Y^2=abc.
\]

Its fixed subgroup is

\[
H_{abc}=\ker\chi_{abc},
\]

the order-four subgroup of even sign changes. Since `eta` changes sign under each single generator, it is invariant under every even product. Therefore it descends through

\[
\pi_{abc}:C\to C_{abc}.
\]

### Theorem H15.62 — genus-two descent

There is a real regulator form `\bar\eta` on the quotient, away from the projected divisor locus, such that

\[
\boxed{\pi_{abc}^*\bar\eta=\eta.}
\]

Consequently every period of the natural Mahler form factors through the genus-two quotient:

\[
\boxed{
\int_\gamma\eta
=
\int_{(\pi_{abc})_*\gamma}\bar\eta.
}
\]

This is the exact observer-selection statement. It does **not** yet identify the resulting genus-two regulator period with a specific `L`-value.

## 6. Rationalized `K_2` strengthening

Let

\[
\xi=\{z,w\}\in K_2^M(K(C)).
\]

Then

\[
\sigma_a\xi=-\xi,
\qquad
\sigma_c\xi=-\xi.
\]

For `sigma_b`,

\[
\sigma_b\xi
=\{z,-w^{-1}\}
=-\{z,w\}+\{z,-1\}.
\]

But `\{z,-1\}` is `2`-torsion, because

\[
2\{z,-1\}=\{z,(-1)^2\}=\{z,1\}=0.
\]

Hence after tensoring with `Q`,

\[
\boxed{
\sigma_a\xi
=
\sigma_b\xi
=
\sigma_c\xi
=-\xi
\quad\text{in}\quad
K_2^M(K(C))\otimes\mathbb Q.
}
\]

So the rationalized Milnor symbol itself is `chi_abc`-pure, not merely its real regulator form.

**Boundary:** this statement is in the function-field Milnor `K_2`. To promote it to a motivic/curve `K_2` class used in a Beilinson formula one must still verify the relevant tame-symbol/temperedness conditions at the compactification boundary.

## 7. The `p=3`, `lambda=0` laboratory

For

\[
p=3,\qquad \mu=4,\qquad \vartheta=-1,
\]

we have

\[
Q(u)=u^2+4u+13,
\qquad
Q(u)-4=u^2+4u+9.
\]

The full determinant simplifies to

\[
\boxed{
\det L
=(4-X-Y)\bigl(X^2+4X+13-Y^2\bigr).
}
\]

On the physical torus, `X,Y in [-2,2]`, and

\[
X^2+4X+13-Y^2
=(X+2)^2+9-Y^2
\ge5.
\]

Thus the nontrivial block is strictly positive on the physical contour and has no logarithmic branch ambiguity there.

The selected genus-two quotient is

\[
\boxed{
C_{abc}:
Y^2=(u^2-4)(u^2+4u+13)(u^2+4u+9).
}
\]

With `x=u+2`, this becomes

\[
\boxed{
Y^2=x(x-4)(x^2+5)(x^2+9).
}
\]

The previous working expectation that the Mahler value should be a sum of three elliptic contributions plus a genus-two contribution is therefore rejected for the **natural** Mahler observer. The correct first candidate is the `abc` genus-two motive alone, unless that genus-two Jacobian itself admits a further arithmetic splitting.

## 8. Immediate next obstruction

The next decisive questions are now sharply separated:

1. determine whether `J(C_{abc})` in the `p=3` laboratory is geometrically or rationally simple, or isogenous to elliptic factors;
2. identify its conductor/local Euler factors and modular/automorphic data;
3. verify tame-symbol conditions for the descended `K_2` class;
4. compare the one-dimensional Jensen regulator numerically and then exactly with the `L`-data of `J(C_{abc})`;
5. perform a hostile literature audit specifically for **symmetry-forced character selection of a Mahler regulator on a multiquadratic dihedral Floquet curve**.

## Claim boundary

Kani–Rosen decomposition, Mahler measure, Jensen reduction, regulator forms, and character projectors are classical machinery. The potentially H15-specific theorem is the exact composition

\[
\boxed{
\text{dihedral Floquet multiquadratic curve}
\;\Longrightarrow\;
\{z,w\}\text{ has pure }abc\text{ character}
\;\Longrightarrow\;
\text{three elliptic quotient sectors cancel}
\;\Longrightarrow\;
\text{natural Mahler observer descends to }C_{abc}.
}
\]

No novelty priority is claimed until the targeted literature audit is complete.
