# QGE3 LQR — Coding-Theory Closure of the Hyperplane-Dense Exceptional Case

**Branch:** `research/fcoa-lqr-prestabilization`  
**Status:** analytic closure of the exceptional `m_H>=3` regime  
**Scope:** fifteen pairwise disjoint projective lines in `PG(5,2)`; no partition-realizability assumption is needed  
**Proof status:** theorem, using the published classification of binary `[18,6,8]` codes together with the previously proved hyperplane moment identities

---

## 1. Setup

Let

\[
\mathcal L=\{L_1,\dots,L_{15}\}
\]

be fifteen pairwise point-disjoint projective lines in

\[
PG(5,2).
\]

Let `Holes` be the set of the 18 nonzero points not covered by the fifteen lines. For every nonzero functional `a in F_2^6`, let

\[
m_a=\#\{i:L_i\subseteq\ker a\}.
\]

From `LQR_R7_HYPERPLANE_PDS.md` we already have

\[
\sum_{a\ne0}m_a=225,
\qquad
\sum_{a\ne0}\binom{m_a}{2}=315,
\]

and

\[
|\mathrm{Holes}\cap\ker a|=16-2m_a.
\]

Assume the hyperplane-dense condition

\[
\boxed{m_a\ge3\quad\text{for all }a\ne0.}
\]

---

## 2. The hole code

Use the 18 hole points as the columns of a `6 x 18` binary matrix `G_H`. Let

\[
C_H=\{aG_H:a\in\mathbb F_2^6\}.
\]

### Lemma 2.1
`C_H` is a binary `[18,6,8]` code.

### Proof
The holes span `F_2^6`. Indeed, if they were contained in a hyperplane `ker a`, then

\[
|\mathrm{Holes}\cap\ker a|=18,
\]

whereas the hyperplane formula gives

\[
16-2m_a\le10.
\]

Hence `rank G_H=6`.

For nonzero `a`, the Hamming weight of the codeword `aG_H` is

\[
\operatorname{wt}(aG_H)
=18-|\mathrm{Holes}\cap\ker a|
=18-(16-2m_a)
=2+2m_a.
\]

Since `m_a>=3`, every nonzero codeword has weight at least eight. Since

\[
\sum_{a\ne0}m_a=225<4\cdot63,
\]

some `m_a` equals three, so the minimum distance is exactly eight. Thus

\[
\boxed{C_H\text{ is }[18,6,8].}
\]
\(\square\)

The columns are distinct nonzero projective points, so `C_H` is projective.

---

## 3. Published classification of `[18,6,8]` codes

Dodunekov and Encheva proved that, up to equivalence, there are exactly two binary `[18,6,8]` linear codes:

S. M. Dodunekov and S. B. Encheva,
“Uniqueness of Some Linear Subcodes of the Extended Binary Golay Code,”
*Problems of Information Transmission* 29 (1993), 38–43
(Russian original: *Problemy Peredachi Informatsii* 29:1, 45–51).

A modern tabulation of the two classes is given in:

I. Bouyukliev, S. Bouyuklieva, M. Dzhumalieva-Stoeva, D. Bikov,
“Linear Codes and Self-Polarity,”
*Mathematics* 12 (2024), 3555,
DOI `10.3390/math12223555`.

Their weight enumerators are

\[
W_1(y)=1+45y^8+18y^{12},
\]

and

\[
W_2(y)=1+46y^8+16y^{12}+y^{16}.
\]

---

## 4. The partial-spread second moment excludes the second code

Since

\[
\operatorname{wt}(aG_H)=2+2m_a,
\]

we have

\[
m_a=\frac{\operatorname{wt}(aG_H)-2}{2}.
\]

### First code

For

\[
W_1=1+45y^8+18y^{12},
\]

we obtain

\[
45\text{ values }m_a=3,
\qquad
18\text{ values }m_a=5.
\]

Its second hyperplane moment is

\[
45\binom32+18\binom52
=45\cdot3+18\cdot10
=315.
\]

So this class is compatible with the fifteen-line partial-spread identity.

### Second code

For

\[
W_2=1+46y^8+16y^{12}+y^{16},
\]

we would have

\[
46\text{ values }m_a=3,
\qquad
16\text{ values }m_a=5,
\qquad
1\text{ value }m_a=7.
\]

Then

\[
\sum_{a\ne0}\binom{m_a}{2}
=46\binom32+16\binom52+\binom72
=138+160+21
=319,
\]

contradicting the exact partial-spread identity

\[
\sum_{a\ne0}\binom{m_a}{2}=315.
\]

Therefore the second `[18,6,8]` code class cannot occur as the hole code of a fifteen-line partial spread.

---

## 5. Exceptional-case theorem

### Theorem 5.1 — hyperplane-dense fifteen-line partial spreads

Let fifteen pairwise disjoint projective lines lie in `PG(5,2)`. If every hyperplane contains at least three of the selected lines, then necessarily

\[
\boxed{
\#\{a:m_a=3\}=45,
\qquad
\#\{a:m_a=5\}=18,
}
\]

and no other hyperplane multiplicities occur.

Equivalently, the hole code has weight enumerator

\[
\boxed{1+45y^8+18y^{12}.}
\]

### Proof
By Lemma 2.1 the hole code is `[18,6,8]`. The published classification gives exactly the two possibilities above. The second hyperplane moment excludes the three-weight code, leaving only the two-weight class. \(\square\)

---

## 6. Consequences

From the earlier hyperplane/Fourier analysis, the spectrum

\[
3^{45}5^{18}
\]

implies

\[
\boxed{L_{\mathrm{Holes}}=6.}
\]

The hole Fourier spectrum is

\[
18;\quad 2^{(45)},\quad(-6)^{(18)}.
\]

Therefore the holes form a regular partial difference set

\[
\boxed{(64,18,2,6).}
\]

and the eighteen holes partition uniquely into six projective lines. Hence every hyperplane-dense fifteen-line partial spread extends to a full 21-line spread.

This closes the exceptional regime completely, and it does so without using partition-realizability of the original fifteen lines.

---

## 7. Remaining global parity barrier

The fifteen-line parity theorem now needs to be proved only in the complementary regime

\[
\boxed{\exists\text{ hyperplane }H\text{ with }m_H\le2.}
\]

The exceptional case

\[
m_H\ge3\quad\forall H
\]

is fully classified and reduced to the PDS/full-spread geometry above.

The LQR extremal status is still

\[
\boxed{14\le M_7\le21,}
\]

because the even resolution parity of every exceptional configuration has not yet been proved analytically from the code classification alone. The next attack is on the generic `m_H<=2` case via the hyperplane block-Pfaffian / prescribed-difference minor decomposition.
