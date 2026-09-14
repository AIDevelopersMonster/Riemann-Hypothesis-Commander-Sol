# HATTER-SOL-11 · WORLD_ROTATION_PLANAR_BALANCING_BRIDGE

**Status:** closed structural bridge / new research direction.  
**Scope:** connects HATTER-SOL-09 arithmetic world toggles to HATTER-SOL-11 planar orbit-total responses.

## 1. Why the current `r` is world-dependent

The long planar balancing programme studied the orbit-total state

`Xi=(6,5)`.

For a 5-regular planar support on even `n`, the number of triangulation-complement edges is

`r=(3n-6)-5n/2=n/2-6`.

Thus `r=17` corresponds to `n=46` only because the secondary capacity is five.

After an arithmetic world rotation, the same rational integer can acquire a different canonical interface pair `(P,Q)`. The relevant planar mechanism then changes. There is no reason for the old `r` to be preserved.

This is important: the sequence `r=14,15,16,17,...` is a coordinate chart for one world state, not an intrinsic invariant of the rational integer.

## 2. The prime 61 as the exact bridge example

The Gaussian world gives

`61=6^2+5^2`,

hence the folded Gaussian capacity is

`Pi_G(61)=(6,5)`.

This is exactly the critical planar state whose all-even frontier required the growing complement-balancing programme.

The Eisenstein world has

`61=5^2+5*4+4^2`,

hence

`Pi_E(61)=(5,4)`.

Now examine the class-number-one odd-discriminant worlds using the HATTER-SOL-09 canonical discriminant capacity

`rho_Delta(L+W F_Delta)=max(|L|,|W|,|L+W|)`.

For `Delta=-19`, the norm form is

`N(L,W)=L^2+LW+5W^2`.

The identity

`61=7^2+7*1+5*1^2`

gives the absolute step triple `(7,1,8)` and therefore

`Pi_{-19}(61)=(7,1)`.

For `Delta=-163`, the norm form is

`N(L,W)=L^2+LW+41W^2`.

The identity

`61=4^2+4*1+41*1^2`

gives the step triple `(4,1,5)` and hence

`Pi_{-163}(61)=(4,1)`.

Among the nine imaginary quadratic class-number-one fields, 61 is split in

`Delta=-4,-3,-19,-163`

and inert in

`Delta=-8,-7,-11,-43,-67`.

Thus the same rational prime has, across this finite UFD laboratory, the interface states

- `(-4): (6,5)`;
- `(-3): (5,4)`;
- `(-19): (7,1)`;
- `(-163): (4,1)`;
- inert worlds: `(61,0)` at the rational-line level.

The arithmetic world rotation therefore moves the same prime through qualitatively different planar regimes.

## 3. Immediate theorem transfer in the `Delta=-19` world

The state `(7,1)` lies in the exact unit-tail family T11.46. Hence for every even `n>=4`,

`R^Xi_Pl,n(7,1)={(n+12+2t,n-2t):0<=t<=n/2}`.

Consequently the generic-odd forgetting fiber associated with `(7,1)` remains fully separated on every even planar host:

`nu^Xi_Pl,n(7,1)=3`.

So a single world rotation takes the prime 61 from the difficult Gaussian critical-tail state `(6,5)` into a world where the full all-even planar response is already elementary and exact.

This is not merely a numerical change of capacities. It is a change of proof regime.

## 4. The Eisenstein and `Delta=-163` worlds are different again

The Eisenstein pair `(5,4)` has both capacities below six. Therefore neither the Euler-defect high-channel theorem nor the `(6,5)` complement-balancing theorem is the natural tool. It belongs to the finite-degree planar threshold regime exemplified by T11.42--T11.43.

The `Delta=-163` pair `(4,1)` is lower still. On the Platonic host sequence its response follows the exact degree-threshold law, including eventual collisions that do not occur for the high-channel unit-tail state `(7,1)`.

Thus the world orbit of 61 passes through at least three genuinely different planar memory mechanisms:

1. `(6,5)` — critical five-tail complement balancing;
2. `(7,1)` — permanent high-channel unit-tail memory;
3. `(5,4)` and `(4,1)` — sub-six host-degree threshold behaviour;
4. inert `(61,0)` — pure axial/rational-line state.

## 5. World derivative should act after planar response

HATTER-SOL-09 defines the arithmetic world derivative

`nabla_q Z_n(R)=Z_R(n)-Z_{T_qR}(n)`.

HATTER-SOL-11 supplies geometry-dependent orbital response polynomials. The natural composed observable is therefore

`Z^{Pl}_{R,n}(p;X,Y)`

for a fixed rational prime `p`, arithmetic world `R`, and planar host size `n`.

Then define the planar world derivative

`nabla_q^{Pl} Z_{p,n}(R)=Z^{Pl}_{R,n}(p)-Z^{Pl}_{T_qR,n}(p)`.

This is not a new Laplacian construction; it is the existing HATTER-SOL-09 prime-toggle operator applied to the HATTER-SOL-11 planar response signal.

For `p=61`, the `3`-toggle edge

`[-1] <-> [-3]`

compares the Gaussian `(6,5)` critical-tail response with the Eisenstein `(5,4)` threshold response. Other class-number-one directions compare Gaussian `(6,5)` with `(7,1)`, `(4,1)`, or an inert pure state.

## 6. Structural conclusion

The current `r=17` problem is therefore only the Gaussian slice of a larger object.

The more invariant object is the world-indexed planar response field

`R -> Z^{Pl}_{R,n}(p;X,Y)`.

Its singular features are not just changes in numerical boundary values. A world toggle can change the *type of theorem* controlling the response:

`critical-tail balancing <-> unit-tail factor law <-> Platonic threshold law <-> pure state`.

This suggests a new notion.

### Definition — proof-regime transition

A world edge is a proof-regime transition for `(p,n)` if the canonical interface state crosses between two regions governed by different exact planar mechanisms, even when the scalar free-boundary value changes smoothly or not at all.

For the prime 61, Gaussian to `Delta=-19` is such a transition:

`(6,5) -> (7,1)`.

## 7. Next target

After closing `r=17`, do not immediately continue only with `r=18`.

Compute the finite class-number-one world response table for 61 and then for the next primes whose Gaussian interface has tail five. For each world edge record:

- split/inert/ramified type;
- canonical `(P,Q)`;
- applicable planar theorem regime;
- exact response polynomial where already known;
- whether the three forgetting-fiber members remain separated;
- the world derivative of the planar response.

This will test whether the apparent `r=18` three-center phase transition is intrinsic to the number or only to the Gaussian world chart.