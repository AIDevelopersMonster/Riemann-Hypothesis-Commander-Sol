# HATTER-SOL-21 · HARDWARE ARCHITECTURE CONTRACT

Status: **PRE-RTL ARCHITECTURE FREEZE**

## 1. Design principle

For a fixed algebraic world family, changing world parameters should not
require FPGA reconfiguration.

For quadratic worlds the runtime descriptor is

[
D_W=(B,C,Delta,	ext{observer flags}).
]

The arithmetic datapath is shared.

Therefore:

[
oxed{
	ext{world rotation}=	ext{descriptor load},
}
]

not

[
	ext{world rotation}=	ext{new bitstream}.
]

## 2. Architecture A · sequential parametric world core

One candidate (n), one arithmetic core, one world descriptor at a time.

State machine:

1. load (n);
2. load (D_W);
3. run gcd/Jacobi precheck;
4. run quadratic modular Frobenius exponentiation;
5. compare with expected response;
6. on failure emit COMPOSITE;
7. on survival load the next world;
8. after declared world list is exhausted emit SURVIVES-LIST.

This is the reference architecture.

## 3. Why sequential first

H21-LAB-01 gives

[
1,801,205	o14	o0.
]

Thus among the declared odd composites, the first world rejects

[
1,801,191
]

of

[
1,801,205,
]

a rejection fraction of approximately

[
0.99999223.
]

For composite-heavy candidate streams the second world is almost never needed.

Therefore a fully duplicated two-world implementation would replicate expensive
modular arithmetic while providing little average-cycle benefit for those
inputs.

## 4. Architecture B · interleaved contexts

Maintain (k) world contexts:

[
C_0,ldots,C_{k-1},
]

but share one or a small number of modular multiplication pipelines.

Each context stores:

- (B,C,Delta);
- exponentiation accumulator;
- current base;
- exponent bits/state;
- response state.

Round-robin or adaptive scheduling allows several world evaluations to be in
flight.

This architecture tests whether

[
oxed{
	ext{temporal world multiplexing}
}
]

can approach parallel throughput without linear area replication.

## 5. Architecture C · full parallel world bank

Instantiate one complete arithmetic core per world.

Output:

[
mathbf r(n)
=
(r_1(n),ldots,r_k(n)).
]

This is the natural hardware implementation of simultaneous tomography.

It is retained as a control architecture, not the default design.

## 6. Reconfiguration boundary

Partial/dynamic FPGA reconfiguration is **not** justified for changing
(B,C,Delta) inside the quadratic family.

It becomes scientifically meaningful only when the arithmetic machine changes
class, for example:

[
	ext{quadratic extension}
	o
	ext{cubic extension},
]

[
	ext{scalar Frobenius observer}
	o
	ext{matrix/Artin observer},
]

or

[
	ext{abelian}
	o
	ext{non-Abelian H16--H18 observer}.
]

Then the static shell can preserve:

- candidate stream;
- world scheduler;
- response accumulator;
- host interface;
- timing counters;

while a reconfigurable region swaps the world engine class.

## 7. Hardware observers

Every RTL version must report at least:

- ALMs/LUTs;
- registers;
- DSPs;
- BRAM;
- Fmax;
- latency per world;
- average worlds evaluated per input;
- throughput;
- area x latency;
- area x average-cycle cost.

For adaptive sequential designs also report the empirical distribution

[
Pr[	au_gamma=t].
]

## 8. First FPGA comparison

Do not begin with partial reconfiguration.

Build in this order:

### H21-HW-01

one sequential parametric quadratic core;

### H21-HW-02

two-context interleaved core sharing arithmetic;

### H21-HW-03

two fully parallel cores.

Use identical arithmetic width and world descriptors.

Compare physical cost under the same FPGA backend.

Only if H21-HW-01..03 establish a meaningful architecture tradeoff should a
reconfigurable-world-class experiment be opened.

## 9. FPGA role

FPGA is not used to discover the underlying number-theory law.

Its scientific role is to measure the physical cost of world-response
tomography:

[
oxed{
	ext{mathematical observer architecture}
longrightarrow
	ext{physical observer architecture}.
}
]

That is the H17--H19 continuation inside H21.
