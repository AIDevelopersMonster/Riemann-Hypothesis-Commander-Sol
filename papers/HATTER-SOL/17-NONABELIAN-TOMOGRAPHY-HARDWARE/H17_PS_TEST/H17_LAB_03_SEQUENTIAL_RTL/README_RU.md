# H17-LAB-03 — sequential / time-multiplexed RTL

## Why LAB-03 exists

LAB-02 intentionally translated the closed H17-06/H17-07/H17-08 mathematics
into a fully combinational structural processor.

That architecture is synthesizable, but it creates an enormous zero-delay
event graph for Icarus.  A single test vector can require hours of wall-clock
time before the simulator reaches the testbench `#1` delay.

This is not "one FPGA clock taking hours".

LAB-02 has no clock inside its mathematical core.  The testbench does:

    A=...; B=...; mode=...;
    #1;

Before simulated time may advance by 1 ns, an event-driven simulator must
settle every zero-delay combinational dependency at the current time slot.
That includes the word DAG, membership logic, eight class engines, signature
logic and repair network, with repeated re-evaluation as intermediate nets
change.  One nanosecond of *simulated* time can therefore consume a very large
amount of *wall-clock* CPU time.

The observation on two Windows hosts is therefore a simulation-architecture
barrier, not evidence that a physical FPGA clock has stalled.

## Architectural response

LAB-03 deliberately trades area-parallelism for time:

    latch A,B
      -> 2 raw membership checks
      -> 14 H17-07 DAG compositions, one per clock
      -> ONE reused class engine
      -> 8 registered class coordinates
      -> erasure mask
      -> ONE H17-06 ROM-free repair network
      -> done

The mathematics is unchanged.

The important difference is that Icarus no longer has to settle eight complete
classifiers plus the full DAG as one giant combinational transaction.

## Frozen 14-operation schedule

    0  AB      = A * B
    1  Ab      = A * b
    2  BB      = B * B
    3  AAB     = A * AB       -> probe 0
    4  ABA     = AB * A
    5  ABa     = AB * a
    6  Abb     = Ab * b       -> probe 1
    7  AAAB    = A * AAB      -> probe 2
    8  AbAb    = Ab * Ab
    9  Abbb    = Abb * b      -> probe 3
    10 AABAb   = AAB * Ab     -> probe 4
    11 AAbAb   = A * AbAb     -> probe 5
    12 ABABB   = ABA * BB      -> probe 6
    13 ABaBB   = ABa * BB      -> probe 7

Exactly one `compose_perm` result is committed per composition state.

## Reused classifier

The generated H17-08 `psl27_member_class_only` block is instantiated once.

Derived words do not repeat membership tests because:

    A,B in PSL(2,7) => every word in A,B,a,b is in PSL(2,7).

The sequential controller presents each of the eight probe values to that one
classifier and registers its 3-bit class.

## Repair

After all eight class fields are registered, LAB-03 applies the same external
mode contract as LAB-02:

    mode 0    no visible erasure, repair tree e=0 validates the domain
    mode 1..8 overwrite the selected 3-bit field by 111
    mode >8   status 4

The same generated H17-06 ROM-free decision tree reconstructs the missing
coordinate or rejects the non-generating projected signature.

## Expected cycle structure

For a valid PSL input, the controller executes:

- one membership decision stage;
- 14 composition stages;
- 8 classifier capture stages;
- mask stage;
- repair capture stage;
- done stage.

From the accepted `start` edge to the `done` pulse the present state schedule
is deterministic.  The testbench measures the observed wait cycles rather than
using that number as a physical-frequency claim.

Invalid raw membership or illegal mode is rejected early.

## Run on Windows PowerShell

From this directory:

    .\tools\test_smoke.ps1

Only after smoke passes:

    .\tools\test_lab03.ps1 -Set quick

and then:

    .\tools\test_lab03.ps1 -Set full

Do not run LAB-02 quick/full in parallel while characterizing LAB-03.

## What success means

A full pass establishes equality with the existing LAB-01 golden-vector
contract for:

- status;
- raw robust8 fingerprint;
- observed erased fingerprint;
- repaired fingerprint.

It does **not** yet establish LUT/FF/Fmax/power on a target FPGA.

LAB-03 is the architecture needed to make pure RTL simulation practical before
hardware selection.
