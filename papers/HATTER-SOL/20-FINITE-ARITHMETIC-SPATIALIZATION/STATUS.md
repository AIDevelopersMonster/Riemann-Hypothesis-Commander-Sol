# H20 finite arithmetic spatialization · STATUS

## Opened

Branch:

research/hatter-sol-finite-arithmetic-spatialization

## Frozen first experiment

Arithmetic function:

\[
S_W(x)=\min\{p>x:p\text{ prime}\}.
\]

Initial widths:

\[
W=4,5,6.
\]

Presentations:

- D = complete direct lookup;
- L = ordered linear threshold chain;
- B = balanced decision tree.

All three are required to be exhaustively equivalent before any synthesis comparison is interpreted.

## Independent model check

The Python semantic models were exhaustively checked for

\[
W=4,5,6,7,8,9,10.
\]

Results:

~~~text
PASS W=4: 16 inputs; primes=7; next after max=17
PASS W=5: 32 inputs; primes=12; next after max=37
PASS W=6: 64 inputs; primes=19; next after max=67
PASS W=7: 128 inputs; primes=32; next after max=131
PASS W=8: 256 inputs; primes=55; next after max=257
PASS W=9: 512 inputs; primes=98; next after max=521
PASS W=10: 1024 inputs; primes=173; next after max=1031
~~~

This verifies the mathematical direct/linear/balanced models only.

## Open gates

1. Icarus SystemVerilog exhaustive equivalence for W=4,5,6.
2. Matched Yosys proc / techmap / abc-fast profile.
3. First observer partitions of {D,L,B}.
4. If informative, scaling W=7..10.
5. Only after the baseline: add arithmetic/spectral/zeta-derived observers.

No RH-related claim is open at this stage.
