# HATTER-SOL-17 · Reproducibility appendix v1.0

Canonical path:

`papers/HATTER-SOL/17-NONABELIAN-TOMOGRAPHY-HARDWARE/`

## Principal certificates

| File | Claim | Git blob SHA |
|---|---|---|
| `psl27_signature_admissibility_certificate.py` | generating/non-generating signature admissibility | `922f2be81c06c7812a1210c6529aee431eac76c3` |
| `psl27_depth5_erasure_certificate.py` | depth-4 barrier / depth-5 separator | `00381ab3580b511980d4ff60e79f4609e0913ab2` |
| `psl27_joint_one_erasure_code_certificate.py` | robust8 joint one-known-erasure code | `8a3c3ebe360594c0a4ccb523034fc71be0e3d5f7` |
| `psl27_structural_class_engine_certificate.py` | 40,320-permutation structural classifier | `254ae271eb067ab284040e663e5ef07e1b78eeec` |
| `psl27_erasure_repair_tree_certificate.py` | ROM-free repair trees | `745e7bc967af64f4baa6c7e9f7d1a6c58b21c888` |
| `psl27_word_dag_certificate.py` | optimal 14-composition DAG in the stated model | `c6c9732c4a9af2d7b292de9584b0cc4c37a865e2` |

Golden-model note:

- `H17_01_CANONICAL_GOLDEN_MODEL.md` — blob `2a08d5cc7d55aa664b091e254bd3ccea169acedc`.

Synthesis evidence:

- `evidence/H17_08_SYNTHESIS_EVIDENCE.md` — blob `224e9f9cf7bb7b34c2a61581b74cff014dc3c00b`.

## Generic synthesis values

- closure frontend: 20,485
- closure flat core: 24,730
- closure ROM-free core: 23,937
- full-classifier frontend: 38,957
- full-classifier flat core: 43,330
- full-classifier ROM-free core: 42,484

These are technology-independent Yosys Boolean-cell counts.

## Evidence boundary

The release distinguishes exact finite certificates, RTL verification and generic synthesis from target synthesis and measured hardware. A fresh full rerun transcript is desirable for archival provenance but is not represented as having been performed by this publication assembly unless a transcript is later added.
