# HATTER-SOL · Finite Arithmetic Spatialization

Status: **EXPLORATORY LAB / FIRST BOOLEAN PRIME EXPERIMENT**

Author: Alex Malachevsky  
ORCID: 0009-0008-6009-3196  
AI research collaborator: Commander Sol · Hatter Sol

## Question

The first experiment tests a narrow form of the finite arithmetic spatialization idea:

> Can one finite arithmetic function, described by radically different computational presentations, collapse to the same Boolean circuit image after synthesis, or does the source presentation leave a measurable structural trace?

We deliberately begin with prime arithmetic small enough for exhaustive verification.

## Frozen arithmetic semantics

Two functions are used.

### P0 · prime membership

For fixed width \(W\),

\[
P_W(x)=1
\iff
x\text{ is prime},
\qquad
0\le x<2^W.
\]

### P1/P2 · strict next prime

\[
S_W(x)=\min\{p>x:p\text{ is prime}\}.
\]

The output width is \(W+1\), so the function is defined for every \(W\)-bit input, including values near \(2^W-1\).

Example for \(W=4\):

\[
0,1\mapsto2,\quad
2\mapsto3,\quad
3,4\mapsto5,\quad
5,6\mapsto7,
\]

\[
7,8,9,10\mapsto11,\quad
11,12\mapsto13,\quad
13,14,15\mapsto17.
\]

## Three presentations of the same function

For every width, the generator emits three SystemVerilog implementations with identical ports and semantics.

### D · DIRECT

A complete finite lookup:

\[
x\mapsto S_W(x).
\]

This presentation contains no explicit prime-search algorithm.

### L · LINEAR

A conventional ordered threshold chain returning the first prime strictly greater than \(x\).

This is close to a sequential search description after spatial unrolling.

### B · BALANCED

The same prime intervals are organized as a balanced binary decision tree.

The mathematical answer is unchanged, but the source decision geometry is different.

## First falsifiable question

For each width \(W\), define

\[
\mathcal F_W=\{D_W,L_W,B_W\}.
\]

Run the same Yosys flow on all three:

\[
\text{source}
\to
\text{proc/flatten/opt}
\to
\text{techmap/opt}
\to
\text{abc-fast}.
\]

At each stage compare at least total cells, wires, and wire bits. Later we can add cell histograms and normalized JSON netlists.

The first result will be one of the finite partitions of \(\{D,L,B\}\), for example

\[
\{\{D,L,B\}\},
\quad
\{\{D,L\},\{B\}\},
\quad
\{\{D\},\{L\},\{B\}\}.
\]

No outcome is assumed in advance.

## Why this is scientifically useful

The experiment separates three statements:

1. a finite arithmetic function exists;
2. a finite Boolean circuit realizing it exists;
3. a compact or presentation-independent circuit structure exists.

Only (1) -> (2) is automatic for a finite truth table.

The nontrivial question is what happens to structure as \(W\) grows and different presentations pass through synthesis.

## P3 · scaling experiment

After the first \(W=4,5,6\) run, extend to

\[
W=7,8,9,10.
\]

Then inspect not only absolute cost but the structural increment

\[
\Delta_W=C_{W+1}\ominus C_W.
\]

A repeating or finitely typed family of increments would be a genuinely new object worth formalizing.

## Files

- tools/generate_prime_spatial_lab.py
  - generates prime membership;
  - generates DIRECT / LINEAR / BALANCED next-prime RTL;
  - generates exhaustive SystemVerilog testbenches;
  - emits truth tables.

- tools/verify_python_models.py
  - independent Python semantic check.

- tools/run_exhaustive.ps1
  - generates W=4,5,6;
  - runs Icarus Verilog exhaustively for every input and every presentation.

- tools/run_yosys_compare.ps1
  - applies one matched Yosys flow;
  - records post-proc, post-techmap, and post-ABC structural counts;
  - writes PRIME_SPATIAL_YOSYS_SUMMARY.csv.

## Fast local run

From this directory:

~~~powershell
.\tools\run_exhaustive.ps1
~~~

Expected final line:

~~~text
PASS: all finite prime representations are exhaustively equivalent
~~~

Then:

~~~powershell
.\tools\run_yosys_compare.ps1
~~~

The first scientifically interesting artifact is:

~~~text
PRIME_SPATIAL_YOSYS_SUMMARY.csv
~~~

## Tool assumptions

The exhaustive script detects Icarus in PATH or:

~~~text
C:\iverilog\bin\iverilog.exe
C:\iverilog\bin\vvp.exe
~~~

The synthesis script expects yosys or yosys.exe in PATH.

## Claim boundary

This laboratory does **not** claim:

- a formula for the primes;
- a new prime-number theorem;
- a Riemann-hypothesis implication;
- a uniform compact circuit family;
- that finite truth-table realizability is novel.

The first objective is only to determine whether source arithmetic presentation leaves a reproducible Boolean structural signature and how that signature changes with width.

A later zeta-derived observer is justified only if this baseline experiment shows a stable framework for comparing arithmetic presentations.
