# HATTER-SOL-21 · INTERWORLD PRIMALITY TOMOGRAPHY
## Working codename: RUBIK WORLD-RESPONSE MACHINE

Status: **EXPLORATORY RESEARCH LAB / NOT A PAPER**

Branch: `research/hatter-sol-world-response-rubik-machine`

## 1. Starting point

HATTER-SOL-09--15 already established the correct conceptual direction:

[
oxed{
	ext{fixed arithmetic object}
	o
	ext{many arithmetic worlds}
	o
	ext{world-response field}
	o
	ext{tomographic reconstruction}.
}
]

The new question is whether primality itself can be probed more effectively by
**rotating the arithmetic world** rather than observing a single copy of
(mathbb Z).

The Rubik analogy is:

- the integer (n) is held fixed;
- a world descriptor is changed;
- each world exposes a different response channel;
- the sequence/vector of responses is the actual object of interest.

## 2. First exact world family

Use quadratic algebras

[
A_{n;B,C}
=
(mathbb Z/nmathbb Z)[x]/
(x^2-Bx-C).
]

The world discriminant is

[
Delta=B^2+4C.
]

For a prime (p
mid 2CDelta), Frobenius gives the exact response

[
x^pequiv x
]

when

[
left(rac{Delta}{p}ight)=+1,
]

and

[
x^pequiv B-x
]

when

[
left(rac{Delta}{p}ight)=-1.
]

Thus each quadratic world supplies a necessary prime-response law.

For composite (n), failure of the corresponding congruence is an exact
compositeness witness.

## 3. Literature boundary

This mechanism lies inside the established theory of Frobenius probable-prime
tests, Lucas/Frobenius pseudoprimes and quadratic extensions.

Therefore H21 does **not** claim invention of a new primality test merely from
using several quadratic worlds.

The HATTER-specific research question is instead:

[
oxed{
	ext{Can world-response tomography be organized as a finite observer system}
atop
	ext{whose mathematical and physical architecture are both measurable?}
}
]

## 4. First finite discovery result

A local exhaustive discovery scan was performed on odd integers

[
3le n<2^{22}.
]

Worlds:

[
W_1:(B,C)=(1,-2),qquad Delta=-7,
]

[
W_2:(B,C)=(1,1),qquad Delta=5.
]

There are

[
1,801,205
]

odd composite integers in the scanned interval.

After the first world (W_1), only

[
14
]

composites remain.

After the second world (W_2),

[
oxed{0}
]

composites remain.

Thus on this finite range the two-world sequence

[
oxed{-7	o 5}
]

acts as an exact deterministic prime/composite separator, after explicitly
handling the small exceptional primes dividing the world parameters.

This is a **finite computational observation**, not a novelty or asymptotic
claim.

## 5. Surviving composites after the first world

The first world (Delta=-7) leaves only 14 odd composites below (2^{22}).

The second world (Delta=5) rejects all of them.

This is exactly the type of world rotation that motivates the Rubik model:

[
	ext{one face ambiguous}
quad	oquad
	ext{rotate world}
quad	oquad
	ext{ambiguity disappears}.
]

## 6. Hardware question

The quadratic-world arithmetic core is unchanged when (B,C,Delta) change.

Therefore world rotation is naturally implemented as **data/configuration
register update**, not FPGA reconfiguration.

Candidate architectures:

### A · sequential world engine

One modular/Frobenius arithmetic core.

[
W_1	o W_2	ocdots
]

with early exit at the first failed world.

Advantages:

- minimum area;
- one verified arithmetic datapath;
- trivial scaling to more worlds;
- adaptive world choice is natural.

### B · fully parallel world bank

Instantiate one complete world core per world.

Advantages:

- minimum decision latency;
- all responses form one simultaneous tomography vector.

Cost:

- modular arithmetic is replicated approximately with number of worlds.

### C · interleaved/hybrid engine

Share one or several pipelined modular multipliers while keeping multiple world
contexts in flight.

This is likely the most interesting FPGA architecture:

[
oxed{
	ext{shared arithmetic}
+
	ext{parallel world contexts}.
}
]

It can approach parallel throughput without full core replication.

### D · partial reconfiguration / bitstream swapping

Not justified for changing (B,C,Delta) inside the same quadratic family.

The world descriptor is too small and the datapath is the same.

Partial reconfiguration becomes relevant only when changing the **world
machine itself**, e.g.

- quadratic (	o) cubic extension;
- scalar (	o) matrix/Artin observer;
- different multiplication architecture;
- different word/tomography engine.

## 7. Current architecture decision

For the first hardware laboratory:

[
oxed{	ext{SEQUENTIAL PARAMETRIC CORE FIRST}.}
]

Reason:

on the current finite discovery range the first world (Delta=-7) already
rejects all but 14 of 1,801,205 odd composites.

Thus for composite inputs the expected number of world evaluations under the
frozen order is extremely close to one.

A fully parallel two-world design would spend nearly twice the arithmetic
hardware to save latency mainly on primes and a tiny pseudoprime residue.

The second architecture to test is therefore not full duplication but an
**interleaved two-context pipeline**.

## 8. Why FPGA can matter

The research role of FPGA is not to discover the number-theoretic law.

Analytics must come first.

FPGA becomes useful after the world operator is frozen, because it can answer:

1. temporal vs spatial cost of world tomography;
2. whether many worlds share enough arithmetic to avoid linear area growth;
3. whether adaptive world selection beats full parallelism physically;
4. whether different world families leave distinct hardware images;
5. whether a world-response protocol can be streamed at high candidate rate.

This continues the H17--H19 line naturally.

## 9. First experiment

H21-LAB-01 is CPU-only and must reproduce the finite scan independently.

It emits:

- exact composite survivor counts after each world;
- complete survivor list after the first world;
- prime sanity check;
- CSV/JSON/Markdown report.

Only after that report is reproduced in CI do we create RTL.

## 10. Publication threshold

No article is opened by the finite (2^{22}) observation.

A publishable H21 result would require at least one of:

- a genuinely new world-tomography theorem not reducible to known Frobenius
  probable-prime theory;
- a new adaptive/parallel observer theorem;
- a nontrivial lower bound or exact minimal world set under a declared model;
- a new representation-transport result connecting arithmetic world response
  to hardware realization;
- a hardware result with an interpretation stronger than "FPGA accelerates
  modular arithmetic".

## 11. No RH claim

[
oxed{	ext{NO RH CLAIMS}}
]
