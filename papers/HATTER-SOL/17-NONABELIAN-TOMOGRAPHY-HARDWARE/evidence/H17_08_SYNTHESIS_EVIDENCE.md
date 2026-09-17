# H17-08 synthesis evidence

Date: 2026-09-16  
Branch: `research/hatter-sol-17-nonabelian-tomography-hardware`

## Closure-aware run

GitHub Actions run:

```text
run_id    35130879081
head_sha  b3abd25ac78761ae9f852a8f8b6da21089ab1080
job       closure-aware-compare
job_id    104911284850
conclusion SUCCESS
```

Artifact:

```text
id      10460872822
name    h17-08-closure-aware-compare
sha256  72efde1beefb48bc0cdb7abbf1dc262affd03d3085e01c881f8edaf652a922b9
```

Extracted generic Yosys hierarchy counts:

```text
closure frontend        20485
closure flat core       24730
closure ROM-free core   23937
```

Isolated closure blocks in the same artifact:

```text
membership-only         1941
member-class-only       1393
```

## Full-classifier baseline run

GitHub Actions run:

```text
run_id    35131795906
head_sha  e1a9f91a617ea51cd261c006e095acab2a96c476
workflow  H17 baseline synthesis metrics
conclusion SUCCESS
```

Artifact:

```text
id      10461517986
name    h17-08-full-classifier-baseline
sha256  6674c2aba0fb0d1026f67b072fe7acd1051fc2e1b7f687b86b2c77fb746a279d
```

Extracted generic Yosys hierarchy counts:

```text
full-classifier frontend        38957
full-classifier flat core       43330
full-classifier ROM-free core   42484
```

## Apples-to-apples deltas

```text
frontend: 38957 -> 20485  delta -18472  reduction 47.42%
flat:     43330 -> 24730  delta -18600  reduction 42.93%
ROM-free: 42484 -> 23937  delta -18547  reduction 43.66%
```

After closure optimization:

```text
flat - ROM-free = 24730 - 23937 = 793 cells
```

so the ROM-free complete core is 3.21% smaller than the closure-aware flat core under this generic synthesis methodology.

These values are technology-independent Yosys Boolean-cell counts. They are not target FPGA LUT/FF/timing/power data.
