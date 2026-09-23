# HATTER-SOL-21 · H21-LAB-23 RESULT

Status: **CI REPRODUCED / RUNTIME-SAFE COMPILER ADVANTAGE MODEST BUT STABLE**

Run:

\`35740132618\`

## 1. Runtime safety

Every measured world execution uses only:

\[
n,\quad (B,C,\Delta),
\]

quadratic-algebra exponentiation, defect coordinates, and

\[
\gcd(n,d_j).
\]

No hidden factor \(p\) or \(q\) is used at runtime.

## 2. Broad common-core result, |D|<=127, n<2^18

Population:

\[
\boxed{6436}
\]

distinct odd semiprimes with

\[
p,q>127.
\]

Candidate worlds:

\[
\boxed{76}.
\]

Greedy first 20 worlds:

\[
5,\ 113,\ 109,\ -7,\ 85,\ -19,\ 37,\ -107,\ 89,\ 41,\ 69,\ -79,\ 53,\ 77,\ -95,\ -43,\ -11,\ -119,\ -23,\ -111.
\]

Coverage after 20 worlds:

\[
\boxed{36.761964\%}.
\]

Individual-world ranking:

\[
\boxed{36.124922\%}.
\]

Hand-extended schedule:

\[
\boxed{35.860783\%}.
\]

Thus at 20 worlds the greedy compiler gains about

\[
0.64
\]

percentage points over individual ranking and

\[
0.90
\]

percentage points over the hand schedule.

## 3. Early-prefix gain is larger

For the same broad scan:

### 5 worlds

\[
\boxed{
14.7141\%\quad\text{greedy}
}
\]

versus

\[
14.6520\%
\]

individual and

\[
13.0360\%
\]

hand.

### 10 worlds

\[
\boxed{
24.1765\%\quad\text{greedy}
}
\]

versus

\[
23.7881\%
\]

individual and

\[
23.3375\%
\]

hand.

Thus complementarity matters most when the runtime budget is short.

## 4. Stability across controls

The same qualitative pattern appears in all four CI configurations.

For example, \(|D|\le63,\ n<2^{18}\):

\[
42.1418\%
\]

greedy versus

\[
41.6905\%
\]

individual/hand at 20 worlds.

For \(|D|\le127,\ n<2^{17}\):

\[
42.8073\%
\]

greedy versus

\[
41.4124\%
\]

individual and

\[
40.7149\%
\]

hand.

Thus the coverage advantage is stable but not dramatic.

## 5. Important objective correction

The reported average revelation index among *covered* inputs is not the correct
hardware objective.

A schedule can increase coverage by adding harder inputs at later positions and
thereby increase the conditional average revelation index.

The runtime objective should instead use a capped cost such as

\[
\boxed{
C_K(n)=
\min(\tau(n),K+1),
}
\]

where uncovered inputs pay the full schedule cost \(K+1\).

Then compare

\[
\mathbb E[C_K].
\]

This is the correct expected-work metric for an early-stopping hardware
observer.

## 6. Publication consequence

The compiler has a real operational effect, but LAB-23 alone does not satisfy
the publication threshold.

Required next controls:

- train/test separation;
- capped expected runtime cost;
- schedule stability across number ranges;
- eventually FPGA cycle/energy measurement.
