# HATTER-SOL-11 · v0.3 Patch-Set Erratum — Type-III witness sign

**Status:** closed editorial correction before EN/RU v0.9 freeze.

The audited patch set correctly chose

\[
\alpha_{III}=Q-(P+Q)F
\]

as an explicit witness for the pure-oblique placement, but misstated one coefficient sign.

For

\[
L=Q,\qquad W=-(P+Q),
\]

the median of

\[
\{L,-W,0\}=\{Q,P+Q,0\}
\]

is `m=Q`. Therefore the median-geodesic theorem gives

\[
\boxed{
g_\Delta(\alpha_{III})=(0,-P,Q),}
\]

not `(0,-P,-Q)`.

Taking absolute counts gives exactly

\[
\boxed{
\Omega_{III}=(0;\{P,Q\}),
\qquad
\Xi_{III}=(0,P+Q).
}
\]

The Type-III norm formula remains

\[
N_{III}=q(P^2+Q^2)+(2q-1)PQ,
\]

so no theorem statement or downstream result changes.

**Publication instruction:** EN/RU v0.9 must use `(0,-P,Q)` in the explicit witness proof.