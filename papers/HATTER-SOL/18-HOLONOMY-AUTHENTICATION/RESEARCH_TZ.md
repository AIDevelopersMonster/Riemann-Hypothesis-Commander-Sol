# HATTER-SOL-18 · HOLONOMY AUTHENTICATION

## Research task

**Working title:** *Order-Sensitive Holonomy Authentication: A Physical Challenge–Response Primitive from Noncommuting Ports*

**Status:** security/application research branch.  
**Parents:** HATTER-SOL-15/16/17.  
**Goal:** test whether order-sensitive noncommuting physical transformations can provide a useful challenge–response authentication primitive.

---

## 1. Claim boundary

The motivating intuition is that changing the order of two noncommuting transformations,

`A -> B` versus `B -> A`,

produces a measurable commutator/holonomy response.

This does **not** by itself imply post-quantum security. In particular:

- “Shor cannot break it” is not a theorem and must not be asserted;
- hiding a finite group or Galois structure is not a recognized standalone security assumption;
- physical unclonability, computational hardness, and information-theoretic unpredictability are different properties;
- security requires a precise adversary model and reductions/attacks.

The first paper therefore studies a **holonomy challenge–response primitive**, not yet a post-quantum cryptosystem.

---

## 2. Primitive model

A device contains an ordered family of physically realized transformations

`T_1,...,T_m`.

A challenge is a word `w` in the generators and inverses. The response is a vector of externally measured observables of the resulting transformation, for example:

- commutator trace;
- selected representation traces;
- spectral moments;
- labelled primitive response channels;
- calibrated analogue measurements.

Authentication compares the measured response with a stored enrolled template using an error/noise model.

---

## 3. First mathematical questions

1. **Collision resistance of the observer map**  
   For a fixed secret device realization, how many challenge words produce the same observable response?

2. **Challenge entropy**  
   How large is the quotient of the free-word challenge space by the kernel induced by the device and observer?

3. **Learnability**  
   Given polynomially many challenge–response pairs, can an attacker reconstruct the effective representation/transfer model and predict unseen responses?

4. **Noise robustness**  
   What minimum response separation survives realistic measurement error?

5. **Replay and modeling attacks**  
   Does freshness/nonlinearity come from secret state, uncontrollable process variation, or merely obscurity of the port map?

The primitive is interesting only if the observer map is both sufficiently separated for the legitimate verifier and difficult to learn/predict for the attacker under an explicit model.

---

## 4. FPGA / photonic split

### FPGA demonstrator

Use a digital emulator of the port algebra first.

- secret/configurable noncommuting finite-group transformations;
- high-rate programmable challenge words;
- exact response channels;
- controlled insertion of noise/erasures on the host side;
- exhaustive attack experiments for small groups.

Purpose: validate protocol logic and quantify algebraic collisions. This is not a PUF because a deterministic FPGA configuration is clonable by anyone who knows the bitstream.

### Physical demonstrator

A later experiment may use integrated photonics, RF networks, coupled resonators, or another genuinely analogue path-dependent system in which manufacturing/calibration parameters are not exactly known to the verifier or attacker.

Only such a physical layer can support a meaningful PUF-style unclonability hypothesis.

---

## 5. Security work package

Before any “post-quantum” label, perform:

- complete small-instance key/model recovery;
- generic quantum speedup audit;
- hidden subgroup/period-finding applicability check;
- linear/system-identification attacks;
- chosen-challenge adaptive attacks;
- surrogate-model/ML prediction attacks;
- response-noise and helper-data leakage audit;
- comparison against standard PQ authentication/MAC constructions.

If a standard classical or quantum algorithm reconstructs the device efficiently, that negative result should be published.

---

## 6. Useful theorem targets

A publishable first result could be any one of:

1. an exact lower bound on challenge-response collision distance for a specified non-Abelian port family;
2. a theorem showing that a chosen finite observer set uniquely identifies a secret port configuration up to known gauge symmetries;
3. a rigorous attack demonstrating efficient learnability of a seemingly complex holonomy primitive;
4. a noise/separation theorem proving reliable authentication in a specified physical model.

A negative cryptographic result is preferable to an unsupported security claim.

---

## 7. Relationship to HATTER-SOL-17

H17 asks: can the observer reconstruct the hidden state?

H18 asks the deliberately opposite security question:

> if the legitimate observer can reconstruct or authenticate from the response, how much can an adversary reconstruct from the same interface?

The same tomography machinery is therefore both an enabling technology and a potential attack tool.

---

## 8. First active strike

Begin with the smallest exact challenge-response laboratory:

- `A5` and `PSL(2,7)` digital port pairs;
- enumerate challenge words up to bounded length;
- compute response collision spectra for several observer sets;
- measure how quickly the port pair can be reconstructed from chosen queries.

Do not call the construction post-quantum secure unless this attack program produces an explicit hardness basis that survives independent review.
