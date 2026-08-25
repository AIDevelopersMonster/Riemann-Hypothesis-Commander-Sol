"""Upstream Riemann-zeta Argand-loop generation for RH-SOL-02.

The module is deliberately explicit about precision, zero source, curve sampling,
and closure. It produces polygonal approximations only; convergence must be
checked before a geometric classification is treated as stable.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping
import csv
import hashlib
import json

import mpmath as mp
import numpy as np


@dataclass(frozen=True)
class LoopMetadata:
    loop: int
    gamma0: float
    gamma1: float
    dps: int
    initial_segments: int
    adaptive: bool
    curve_rel_tol: float
    curve_abs_tol: float
    max_depth: int
    vertices: int
    zeta_evaluations: int
    zero_source: str


@dataclass(frozen=True)
class ZetaLoop:
    metadata: LoopMetadata
    t: np.ndarray
    vertices: np.ndarray


def load_zero_table(path: str | Path) -> dict[int, float]:
    """Load CSV with columns n/index and gamma/t."""
    path = Path(path)
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"zero table is empty: {path}")
    names = set(rows[0])
    n_key = "n" if "n" in names else "index" if "index" in names else None
    g_key = "gamma" if "gamma" in names else "t" if "t" in names else None
    if n_key is None or g_key is None:
        raise ValueError("zero table must contain n/index and gamma/t columns")
    out: dict[int, float] = {}
    for row in rows:
        out[int(row[n_key])] = float(row[g_key])
    return out


def zero_pair(
    loop: int,
    *,
    dps: int = 40,
    zeros: Mapping[int, float] | None = None,
) -> tuple[mp.mpf, mp.mpf, str]:
    if loop < 1:
        raise ValueError("loop must be >= 1")
    if zeros is not None:
        try:
            return (
                mp.mpf(str(zeros[loop])),
                mp.mpf(str(zeros[loop + 1])),
                "csv-zero-table",
            )
        except KeyError as exc:
            raise KeyError(f"zero table must include indices {loop} and {loop + 1}") from exc
    with mp.workdps(dps):
        return (
            mp.im(mp.zetazero(loop)),
            mp.im(mp.zetazero(loop + 1)),
            "mpmath.zetazero",
        )


def _critical_zeta(t: mp.mpf) -> complex:
    z = mp.zeta(mp.mpf("0.5") + 1j * t)
    return complex(float(mp.re(z)), float(mp.im(z)))


def sample_argand_loop(
    loop: int,
    *,
    dps: int = 40,
    initial_segments: int = 60,
    adaptive: bool = False,
    curve_rel_tol: float = 2e-5,
    curve_abs_tol: float = 2e-8,
    max_depth: int = 10,
    zeros: Mapping[int, float] | None = None,
) -> ZetaLoop:
    """Sample the critical-line Argand curve between zeros loop and loop+1.

    Endpoints are set exactly to 0+0j after their ordinates are obtained.
    With adaptive=True, each seed segment is recursively bisected until the
    actual midpoint is close to the chord midpoint according to the declared
    tolerance, or max_depth is reached.
    """
    if dps < 20:
        raise ValueError("dps < 20 is not supported for research runs")
    if initial_segments < 4:
        raise ValueError("initial_segments must be >= 4")
    if max_depth < 0:
        raise ValueError("max_depth must be >= 0")

    with mp.workdps(dps):
        g0, g1, source = zero_pair(loop, dps=dps, zeros=zeros)
        cache: dict[str, complex] = {}
        evaluations = 0

        def value(t: mp.mpf) -> complex:
            nonlocal evaluations
            key = mp.nstr(t, dps + 5)
            if key not in cache:
                cache[key] = _critical_zeta(t)
                evaluations += 1
            return cache[key]

        seed_t = [
            g0 + (g1 - g0) * j / initial_segments
            for j in range(initial_segments + 1)
        ]
        seed_z = [0j]
        seed_z.extend(value(t) for t in seed_t[1:-1])
        seed_z.append(0j)

        out_t: list[mp.mpf] = [seed_t[0]]
        out_z: list[complex] = [seed_z[0]]

        def refine(
            ta: mp.mpf,
            za: complex,
            tb: mp.mpf,
            zb: complex,
            depth: int,
        ) -> None:
            if not adaptive:
                out_t.append(tb)
                out_z.append(zb)
                return
            tm = (ta + tb) / 2
            zm = value(tm)
            chord_mid = 0.5 * (za + zb)
            err = abs(zm - chord_mid)
            scale = max(abs(za), abs(zm), abs(zb), 1e-12)
            needs_refine = err > curve_abs_tol + curve_rel_tol * scale
            if needs_refine and depth < max_depth:
                refine(ta, za, tm, zm, depth + 1)
                refine(tm, zm, tb, zb, depth + 1)
            else:
                out_t.append(tb)
                out_z.append(zb)

        for j in range(initial_segments):
            refine(seed_t[j], seed_z[j], seed_t[j + 1], seed_z[j + 1], 0)

        t_arr = np.array([float(x) for x in out_t], dtype=np.float64)
        vertices = np.array(
            [[z.real, z.imag] for z in out_z], dtype=np.float64
        )
        vertices[0] = (0.0, 0.0)
        vertices[-1] = (0.0, 0.0)

    meta = LoopMetadata(
        loop=loop,
        gamma0=float(g0),
        gamma1=float(g1),
        dps=dps,
        initial_segments=initial_segments,
        adaptive=adaptive,
        curve_rel_tol=float(curve_rel_tol),
        curve_abs_tol=float(curve_abs_tol),
        max_depth=max_depth,
        vertices=len(vertices),
        zeta_evaluations=evaluations,
        zero_source=source,
    )
    return ZetaLoop(meta, t_arr, vertices)


def save_loop(loop: ZetaLoop, path: str | Path) -> None:
    """Save one polygonal loop and metadata as compressed NPZ."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    metadata_json = json.dumps(loop.metadata.__dict__, sort_keys=True)
    np.savez_compressed(
        path,
        t=loop.t,
        vertices=loop.vertices,
        metadata=metadata_json,
    )


def load_loop(path: str | Path) -> ZetaLoop:
    with np.load(path, allow_pickle=False) as data:
        t = data["t"].astype(np.float64)
        vertices = data["vertices"].astype(np.float64)
        raw = data["metadata"].item()
    meta = LoopMetadata(**json.loads(str(raw)))
    return ZetaLoop(meta, t, vertices)


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
