# HATTER-SOL-18 · H18-06
# Adaptive one-erasure tomography: four successful answers still suffice

**Status:** CLOSED exact finite theorem layer.

## 1. Why the fault model must be frozen carefully

If an erased query could simply be repeated immediately, one erasure would add one trivial retry and there would be almost no mathematics.

H18 therefore uses the nontrivial analogue of H17's missing-coordinate model:

> at most one requested query may return **ERASED**, and that query is unavailable for the remainder of the transaction.

The observer knows which query failed, because it knows which word it attempted.

Thus an erasure is not an unknown wrong class.  It is a known missing observation from one now-unavailable probe.

---

## 2. Full identify-or-reject state space

To compare fairly with H17 admissibility, H18-06 does **not** assume in advance that the input pair is generating.

For

\[
G=PSL(2,7),
\]

the exact simultaneous-conjugacy quotient of all ordered pairs \(G^2\) has

\[
\boxed{197}
\]

pair orbits:

\[
\boxed{114\text{ generating}+83\text{ non-generating}.}
\]

The required terminal outputs are:

- one of the 114 generating orbit identities; or
- a common terminal output **REJECT** for every non-generating orbit.

So H18-06 solves both tomography and admissibility.

---

## 3. Query pool

As in H18-01, start from all freely reduced words of lengths \(1,\ldots,4\):

\[
4+12+36+108=160.
\]

After identifying words that induce exactly the same class-response vector on all 197 pair orbits, there remain

\[
\boxed{50}
\]

distinct class-valued queries.

Each successful query returns one of

\[
1A,\ 2A,\ 3A,\ 4A,\ 7A,\ 7B.
\]

One query attempt may instead return

\[
\mathrm{ERASED}.
\]

---

## 4. No-erasure baseline

For the full 197-orbit identify-or-reject task, exact dynamic programming gives:

\[
\boxed{
D_0=4.
}
\]

Three successful class queries are insufficient, while four suffice.

Thus the earlier H18 depth-four phenomenon survives after adding all 83 non-generating orbit types.

---

## 5. One-erasure theorem

Let \(S_1\) be the minimum worst-case number of **successful class answers** needed when the adversary may erase one requested query permanently.

The exact certificate gives:

\[
\boxed{
S_1=4.
}
\]

Therefore one known persistent erasure costs **no additional successful information**.

Since at most one attempt is erased, the worst-case number of query attempts is

\[
\boxed{
A_1=5.
}
\]

Equivalently:

\[
\boxed{
4\text{ successful answers}
+
1\text{ possible ERASED attempt}
}
\]

always suffice to either identify the generating H17 orbit or reject the pair as non-generating.

---

## 6. Why four is optimal

The lower bound is immediate once the exact no-erasure baseline is known.

If only three successful class answers were allowed under the one-erasure model, then even the easier no-erasure case would have to be solved with three successful answers.

But H18-06 certifies

\[
D_0>3.
\]

Hence

\[
S_1\ge4.
\]

The exact adaptive construction proves

\[
S_1\le4.
\]

Therefore

\[
\boxed{S_1=4}.
\]

---

## 7. What happens when the erasure occurs

At a node with candidate state set \(X'\), suppose the controller asks \(q_w\).

### Successful answer

If the response is a class \(c\), update

\[
X'\leftarrow
\{x\in X':q_w(x)=c\}
\]

and continue with the erasure budget still unused.

### ERASED answer

If the response is ERASED,

\[
X'
\]

does not shrink at all.

Instead:

- \(q_w\) is permanently banned;
- the one-erasure budget is consumed;
- the controller switches to an exact no-erasure decision tree using the remaining query pool.

This is the adaptive analogue of losing one known coordinate.

---

## 8. A canonical first query

One admissible first query is again

\[
\boxed{\texttt{AAB}}.
\]

On all 197 pair-orbit states its branches are:

| class | all states | generating | non-generating |
|---|---:|---:|---:|
| \(1A\) | 6 | 0 | 6 |
| \(2A\) | 27 | 10 | 17 |
| \(3A\) | 58 | 30 | 28 |
| \(4A\) | 46 | 32 | 14 |
| \(7A\) | 30 | 21 | 9 |
| \(7B\) | 30 | 21 | 9 |

If the very first \(AAB\) observation is erased, the state set remains all 197 states, \(AAB\) is banned, and four other successful class queries still suffice.

That is the strongest part of the result: the strategy is not relying on being allowed to retry the lost first question.

---

## 9. Sixteen robust first queries

The certificate finds 16 canonical first-query representatives from the \(W_4\) pool that admit an exact four-successful-answer one-erasure strategy:

\[
\begin{aligned}
&AAB,\ AAb,\ ABB,\ Abb,\ BBa,\ Baa,\ aab,\ abb,\\
&AAAB,\ AAAb,\ ABBB,\ Abbb,\ BBBa,\ Baaa,\ aaab,\ abbb.
\end{aligned}
\]

Their appearance in symmetry-related families is itself a clue for a future structural reduction of the adaptive controller.

---

## 10. Comparison with H17 robust8

H17 solves one known erasure with a **fixed** robust code:

\[
\boxed{8\text{ predetermined probes}.}
\]

H18-06 solves the corresponding identify-or-reject task adaptively with

\[
\boxed{\le5\text{ total attempts}}
\]

and at most

\[
\boxed{4\text{ successful class answers}.}
\]

So at the level of identification/admissibility query count:

\[
\boxed{
8_{\rm fixed}
\longrightarrow
5_{\rm adaptive\ attempts}.
}
\]

This comparison needs one important boundary:

- H17 robust8 reconstructs a fixed 24-bit robust fingerprint;
- H18-06 returns an orbit identity or REJECT through a data-dependent decision program.

Therefore H18-06 has fewer observations but a controller, branching, variable query sequence and data-dependent execution.

It is not a statement that the adaptive hardware must have lower LUT count, lower latency or higher throughput.

That becomes an engineering question.

---

## 11. A stronger surprise: depth-four words are enough

H17 robust8 required exact-depth-five probes in the fixed erasure code.

H18-06 uses only the \(W_4\) pool:

\[
\boxed{|w|\le4.}
\]

Thus adaptivity removes not only three fixed observations in the worst-case attempt count, but also removes the need for length-five queries for this identify-or-reject fault model.

Again, this does **not** mean the two output contracts are identical; it means that sequential information acquisition can replace part of the redundancy built into a fixed fingerprint.

---

## 12. Exact recurrence

Let

\[
N(X',s;q_{\rm ban})
\]

mean that after the erasure has occurred, candidate set \(X'\) can be resolved using at most \(s\) further successful queries while query \(q_{\rm ban}\) is unavailable.

Let

\[
E(X',s)
\]

mean that the erasure is still available.

For a chosen query \(q\),

\[
E(X',s)
\]

requires simultaneously:

\[
N(X',s;q)
\]

for the ERASED branch, and

\[
E(X'_c,s-1)
\]

for every nonempty successful class branch

\[
X'_c=\{x\in X':q(x)=c\}.
\]

The certificate evaluates this recurrence exactly on finite bit masks.

No statistical error model and no heuristic tree search is used.

---

## 13. Certificate

Run:

\`\`\`text
python certificates/h18_adaptive_one_erasure_certificate.py
\`\`\`

Optional metadata output:

\`\`\`text
python certificates/h18_adaptive_one_erasure_certificate.py \
  --emit-json generated/h18_adaptive_one_erasure.json
\`\`\`

Expected conclusion:

\`\`\`text
exact successful-query complexity = 4
exact worst-case total attempts = 5
PASS: exact identify-or-reject under one persistent known query erasure
\`\`\`

---

## 14. Consequence for H18

We now have three qualitatively different observation regimes:

\[
\boxed{
5\text{ fixed queries}
\quad\text{for no-erasure H16 identification},
}
\]

\[
\boxed{
8\text{ fixed probes}
\quad\text{for H17 one-known-erasure robust fingerprint},
}
\]

and

\[
\boxed{
4\text{ successful adaptive queries}
+
1\text{ possible erasure}
}
\]

for H18 identify-or-reject tomography.

So the central H18 thesis is now stronger:

> a family of words can behave not merely as a code, but as a fault-aware interrogation program.

The next engineering layer is to synthesize such a controller and compare it with H17 LAB-02/LAB-03 under a common area/latency/throughput model.
