# HATTER-SOL-15 · Automatic Certificate Range p=31..43 and the First Template Obstruction

**Status:** exact certified theorem layer for `p=31,37,41`; partial exact layer for `p=43`.  
**Certificate engine:** `certificates/automatic_prime_certificate_range_31_43.py`.  
**Purpose:** turn the low-prime Mahler tomography arguments into a reusable proof pipeline, then push it until the first channel that genuinely escapes both existing certificate templates.

The outcome is structurally important:

- `p=31`, `p=37`, and `p=41` are fully closed on the whole half-line `mu>=4`;
- at `p=43`, all independent character channels except one are closed exactly;
- the first unresolved channel is `q=8` in the signless reaction group `C_21`;
- this `q=8` channel defeats both the **order-Abel** and the existing **single-phase shifted moment-Abel** templates.

Thus `p=43, q=8` is the first genuine obstruction to the current proof architecture, not yet a counterexample to tomography.

---

## 1. The two automatic certificate templates

Let

\[
G_p=\mathbf F_p^\times/\{\pm1\}
\cong C_m,
\qquad
m=\frac{p-1}{2}.
\]

For a nontrivial character frequency `q`, the corresponding Mahler coefficient is denoted `S_q`.

The automatic engine searches two sufficient certificate types.

### Template O — order-Abel

Write

\[
S_q=\sum_{r=1}^{m}d_r b_r,
\qquad
b_1<b_2<\cdots<b_m,
\]

where the `b_r` are the strictly angle-ordered primitive Mahler values.

Let

\[
D_k=\sum_{r=1}^{k}d_r.
\]

If there is a real phase `phi` such that

\[
\boxed{
\Re(e^{-i\phi}D_k)>0
\qquad
1\le k<m,
}
\]

then Abel summation gives

\[
\boxed{S_q\ne0}
\]

for every strictly increasing response profile, hence for every `mu>=4`.

### Template M — shifted moment-Abel

Use the exact positive-kernel expansion

\[
M_\mu(\alpha)
=C_\mu-
\sum_{j\ge1}D_{\mu,j}\cos^{2j}\alpha,
\qquad
D_{\mu,j}>0.
\]

Put

\[
x_r=\cos^2\frac{\pi r}{p}.
\]

For character `chi_q`, choose a phase `phi` and an integer shift `h>=1`.

If

\[
\boxed{
\Re\left(
 e^{-i\phi}
 \sum_{r=1}^{k}\chi_q(r)x_r^h
\right)>0
\quad
1\le k\le m,
}
\]

then Abel summation gives the same strict half-plane sign for all moments `j>=h`.

The finitely many moments

\[
1\le j<h
\]

are checked directly by rigorous rational interval arithmetic in the same phase.

If they are also strictly positive, then

\[
\boxed{S_q\ne0}
\]

for every `mu>=4`.

---

## 2. Exact certification method

The certificate engine uses only exact arithmetic.

It encloses `pi` using

\[
\frac{103993}{33102}<\pi<\frac{104348}{33215},
\]

and every required cosine is enclosed by a Taylor polynomial with a rigorous Lagrange remainder.

All subsequent operations are interval arithmetic over `fractions.Fraction`.

Therefore every quoted positive margin below is backed by a positive exact rational lower endpoint.

No floating-point sign is used in the theorem statements.

---

## Theorem H15.131 — full Mahler tomography for `p=31`

For

\[
p=31,
\qquad
|G_{31}|=15,
\]

all seven independent nontrivial frequencies are certified.

The automatic proof decomposes them as follows:

\[
\boxed{
\begin{array}{c|c}
q&\text{certificate type}\\
\hline
1&O\\
2&O\\
3&O\\
4&O\\
5&M(h=1)\\
6&M(h=8)\\
7&M(h=1)
\end{array}}
\]

The smallest exact positive margins include

\[
q=4:\quad >0.17192909,
\]

and for the hardest shifted channel

\[
q=6:\quad
\text{finite-moment margin}>0.16078174,
\qquad
\text{tail cumulative margin}>0.00499288.
\]

Hence every nontrivial Mahler character mode is nonzero for every `mu>=4`.

Therefore

\[
\boxed{
\mathcal E_{31}\cap[4,\infty)=\varnothing.
}
\]

---

## Theorem H15.132 — full Mahler tomography for `p=37`

For

\[
p=37,
\qquad
|G_{37}|=18,
\]

all nine independent frequencies are certified:

\[
\boxed{
\begin{array}{c|c}
q&\text{certificate type}\\
\hline
1&M(h=1)\\
2&O\\
3&M(h=1)\\
4&O\\
5&O\\
6&M(h=1)\\
7&O\\
8&M(h=14)\\
9&M(h=1)
\end{array}}
\]

The narrowest order margin is

\[
q=5:\quad >0.03664370,
\]

while the deepest shifted certificate is

\[
q=8:\quad h=14,
\]

with

\[
\text{finite-moment margin}>0.08210704,
\qquad
\text{tail cumulative margin}>0.00735299.
\]

Thus

\[
\boxed{
\mathcal E_{37}\cap[4,\infty)=\varnothing.
}
\]

---

## Theorem H15.133 — full Mahler tomography for `p=41`

For

\[
p=41,
\qquad
|G_{41}|=20,
\]

all ten independent frequencies are certified:

\[
\boxed{
\begin{array}{c|c}
q&\text{certificate type}\\
\hline
1&O\\
2&M(h=14)\\
3&O\\
4&O\\
5&M(h=1)\\
6&M(h=1)\\
7&M(h=1)\\
8&O\\
9&M(h=1)\\
10&M(h=1)
\end{array}}
\]

The tightest order margin is

\[
q=3:\quad >0.01047176,
\]

and the deepest shifted certificate is again

\[
q=2:\quad h=14,
\]

with exact positive lower bounds

\[
\text{finite-moment margin}>0.00253909,
\qquad
\text{tail cumulative margin}>0.00258035.
\]

Hence

\[
\boxed{
\mathcal E_{41}\cap[4,\infty)=\varnothing.
}
\]

---

## Corollary H15.134 — certified ladder through `p=41`

Combining the earlier manually structured worlds with the automatic range gives

\[
\boxed{
p\in
\{5,7,11,13,17,19,23,29,31,37,41\}}
\]

and for every such prime

\[
\boxed{
\mathcal E_p\cap[4,\infty)=\varnothing.
}
\]

Equivalently, full centered primitive Mahler tomography holds throughout

\[
\boxed{\lambda\le0.}
\]

for every prime in this certified ladder.

---

## 3. The `p=43` frontier

Now

\[
p=43,
\qquad
G_{43}\cong C_{21}.
\]

There are ten independent nontrivial frequencies.

The automatic engine certifies nine of them exactly:

\[
\boxed{
\begin{array}{c|c}
q&\text{certificate type}\\
\hline
1&O\\
2&M(h=1)\\
3&O\\
4&O\\
5&O\\
6&M(h=1)\\
7&M(h=1)\\
8&\text{unresolved}\\
9&M(h=18)\\
10&M(h=1)
\end{array}}
\]

In particular, the comparatively deep `q=9` mode is still closed by a single-phase shifted certificate:

\[
h=18,
\]

with

\[
\text{finite-moment margin}>0.04221521,
\qquad
\text{tail cumulative margin}>0.00734368.
\]

Thus the current architecture does **not** fail merely because the shift becomes large.

The exceptional channel is specifically

\[
\boxed{p=43,\quad q=8.}
\]

---

## Theorem H15.135 — `p=43, q=8` is not order-Abel certifiable

For the ordered response coefficients of the `q=8` character, consider the proper cumulative root sums

\[
D_k^{(8)}.
\]

A dense phase scan followed by exact geometric inspection shows that their directions are not contained in any open half-plane through the origin.

Equivalently, there is no real linear functional `ell` such that

\[
\ell(D_k^{(8)})>0
\qquad
\forall k<21.
\]

Therefore the pure order-Abel template cannot prove

\[
S_8\ne0.
\]

This is the first certified prime/channel in the scanned range where strict response ordering alone is insufficient for the automatic order template.

---

## Theorem H15.136 — the existing single-phase shifted moment template does not close `p=43,q=8`

The automatic search tested shifts

\[
1\le h\le80
\]

with phase optimization for the combined certificate consisting of

- all direct moments `1<=j<h`, and
- all cumulative shifted tail sums at level `h`.

No common open half-plane was found.

The best optimized minimum projection remains negative even at the top of the scan.

Hence the current Template M does not furnish a certificate for `q=8`.

This statement is about failure of the **certificate class**, not failure of Mahler tomography itself.

---

## 4. Numerical reconnaissance of the unresolved channel

To determine whether `q=8` looks like a genuine observer resonance or merely a proof obstruction, the actual Mahler coefficient was evaluated numerically at high precision.

At the physical point

\[
\mu=4,
\]

one finds approximately

\[
\boxed{
F_{43,8}(4)
\approx
-0.05123594955
+0.16827968058\,i,
}
\]

so

\[
\boxed{|F_{43,8}(4)|\approx0.175906718.}
\]

It is therefore emphatically nonzero numerically at `lambda=0`.

Further samples over

\[
\mu=4.1,4.5,5,6,8,10,15,20,30,50,100
\]

remain nonzero and approach the nonzero large-`mu` asymptotic direction predicted by H15.106.

No zero was observed.

This numerical evidence is not promoted to theorem status.

---

## 5. Why `q=8` is genuinely different

The moment sequence

\[
T_j(\chi_8)
=
\sum_{r=1}^{21}
\chi_8(r)
\cos^{2j}\frac{\pi r}{43}
\]

rotates substantially in argument as `j` grows.

For example its argument numerically moves from near one side of the complex plane for small `j` toward the dominant first-residue direction for large `j`.

Thus the entire moment family is not contained in a single open half-plane.

This explains exactly why the `p=23` and `p=29` moment-half-plane certificates do not generalize mechanically.

The unresolved channel is therefore the first place where one must exploit **the actual Mahler weights**

\[
D_{\mu,j},
\]

not merely their positivity.

Up to `p=41`, positivity plus finite character geometry was enough.

At `p=43,q=8`, the relative sizes of the positive weights become mathematically relevant.

This is a genuine increase in difficulty.

---

## 6. New research boundary

The current proof architecture has now reached its natural limit:

\[
\boxed{
\text{order geometry}
+
\text{positive moment cone}
}
\]

is insufficient for the first time at

\[
\boxed{(p,q)=(43,8).}
\]

The next theorem must add one of the following stronger ingredients.

### Route A — quantitative Mahler-weight inequalities

Prove decay or ratio bounds such as

\[
D_{\mu,j+1}\le \rho(\mu)D_{\mu,j},
\qquad \rho(\mu)<1,
\]

strong enough to prevent the rotating moment vectors from cancelling under the actual positive weights.

### Route B — blockwise sector domination

Partition the moment sequence into blocks whose weighted sums each lie in a common open sector, even though individual moments do not.

### Route C — direct character integral

Return before the positive-power expansion and represent

\[
F_{p,\chi}(\mu)
\]

directly as an integral against a cyclotomic character kernel. A sign or winding argument at the integral level may retain information destroyed by splitting into individual moments.

### Route D — analytic zero exclusion

Use real-analyticity plus a winding/argument principle in `mu` to show that the observed nonzero channel cannot cross zero on `[4,infinity)`.

---

## 7. Structural conclusion

The automatic scan has produced both a success and a meaningful failure.

Success:

\[
\boxed{
p=31,37,41
\text{ are closed automatically and exactly}.}
\]

Failure:

\[
\boxed{
p=43,q=8
\text{ is the first channel outside both existing certificate cones}.}
\]

This is scientifically preferable to continuing prime-by-prime with ad hoc manipulations: the scan has identified the first precise point at which the present mathematical idea stops being sufficient.

The next attack should therefore be directed at the new obstruction itself, not at `p=47`.

---

## 8. Immediate next target

The active problem is now

\[
\boxed{
F_{43,8}(\mu)\stackrel{?}{\ne}0
\quad\forall\mu\ge4.
}
\]

with strong numerical evidence for nonvanishing but no proof yet.

The preferred next strike is to derive **quantitative bounds for the Mahler harmonic weights `D_{mu,j}`** and test whether the rotating `T_j(chi_8)` sequence can be grouped into rigorously noncancelling weighted sectors.

If this succeeds, it should extend beyond `p=43` and produce the next generation of the automatic certificate engine.
