# Spectral epicycles and sieve filters — visualization concept

**Status:** saved research/visualization idea; not part of the Stationary Locality proof.

## 1. Three visual layers

A future interactive demo should distinguish three mathematically different objects that can nevertheless be drawn in one signal-processing language.

### Layer A — parity filter

A basic sinusoidal parity marker can separate the integer lattice into even and odd positions. This is only the simplest periodic filter and should be presented as a reference layer.

### Layer B — divisibility waves / harmonic sieve

For a fixed integer divisor d,

\[
\sin(\pi n/d)=0 \iff d\mid n.
\]

For prime d=p this gives a periodic detector of multiples of p. Overlaying such detectors for odd primes produces a harmonic rendering of Eratosthenes-type sieving: an odd integer n>1 is composite iff some prime p\le\sqrt n has a divisibility zero at n.

An exact Fourier projector is

\[
\mathbf 1_{p\mid n}=\frac1p\sum_{k=0}^{p-1}e^{2\pi i kn/p}.
\]

The demo may therefore show odd integers, odd composites removed by divisibility filters, and the surviving prime locations.

### Layer C — zeta-zero phasors / global prime-counting oscillation

The nontrivial zeros \(\rho=\beta+i\gamma\) enter explicit formulas through terms of the form

\[
\frac{x^\rho}{\rho}.
\]

With \(t=\log x\),

\[
\frac{x^\rho}{\rho}=\frac{e^{\beta t}e^{i\gamma t}}{\rho}.
\]

After normalization by \(e^{t/2}=\sqrt{x}\), a zero on the critical line contributes a constant-radius rotating phasor

\[
\frac{e^{i\gamma t}}{\rho}.
\]

Thus, under RH, the normalized spectral components can be visualized as epicyclic rotations with irregular angular frequencies \(\gamma\); their vector sum traces the oscillatory part of a prime-counting explicit formula. Off-critical zeros would produce expanding or contracting spiral components after the same normalization.

## 2. Important distinction

The divisibility waves are local periodic sieve filters. The zeta zeros are not their intersection points and are not the gaps between the local sine zeros. They belong to the global spectral correction in explicit prime-counting formulas.

The visual analogy is useful precisely because it lets us compare:

\[
\text{periodic divisibility spectrum}
\quad\text{vs}\quad
\text{irregular zeta-zero spectrum}.
\]

## 3. Desired future visualization

Build an HTML/interactive demonstration in which:

1. a simple periodic layer marks parity;
2. prime-period divisibility filters remove odd composites;
3. the remaining prime locations are shown on the integer axis;
4. separately, a finite set of zeta-zero phasors rotates in log-time and reconstructs a truncated explicit-formula oscillation;
5. a control toggles between the local sieve picture and the global spectral picture;
6. no claim is made that the zeta phasors themselves exactly `select` primes pointwise.

A particularly attractive visual would show the endpoint of the phasor chain drawing the reconstructed oscillatory curve while the integer axis below marks prime and composite positions.

## 4. Research question to revisit

Can one construct a mathematically meaningful visualization in which a truncated explicit formula, after smoothing/normalization, produces extrema or sign changes that correlate visually with prime locations or prime-counting jumps without confusing a distributional reconstruction with a pointwise primality test?

This question is reserved for the RH/Nyquist line after the Stationary Locality paper is completed.
