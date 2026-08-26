"""Frozen spectral scoring utilities for RH-SOL-02 EXP-01.

The calibration deliberately mirrors the RH-SOL-01 smooth-warp procedure:
1000-loop blocks, linear detrending, median-normalized rFFT power, mapping
f_loop = omega * (dt/dn) / (2*pi), and block aggregation by mean log1p power.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.signal import detrend


@dataclass(frozen=True)
class SpectrumResult:
    omega: np.ndarray
    score: np.ndarray
    valid_blocks: np.ndarray


@dataclass(frozen=True)
class CombResult:
    score: float
    null_median: float
    null_q95: float
    null_q99: float
    empirical_p_ge: float
    best_common_shift: float
    best_common_shift_score: float


def warped_spectrum(
    series: np.ndarray,
    time_proxy: np.ndarray,
    *,
    block_size: int = 1000,
    omega_min: float = 0.40,
    omega_max: float = 3.50,
    omega_step: float = 0.0005,
    fmin_for_median: float = 0.01,
    fmax_for_median: float = 0.48,
) -> SpectrumResult:
    """Compute the frozen RH-SOL-01-style physical-frequency score."""
    x = np.asarray(series, dtype=float)
    t = np.asarray(time_proxy, dtype=float)
    if x.ndim != 1 or t.ndim != 1 or len(x) != len(t):
        raise ValueError("series and time_proxy must be 1D arrays of equal length")
    if len(x) < block_size or len(x) % block_size:
        raise ValueError("series length must be a positive multiple of block_size")

    n = np.arange(1, len(x) + 1, dtype=float)
    omega = np.arange(
        omega_min,
        omega_max + 0.5 * omega_step,
        omega_step,
        dtype=float,
    )
    acc = np.zeros_like(omega)
    valid = np.zeros_like(omega)

    for s0 in range(0, len(x), block_size):
        s1 = s0 + block_size
        slope = float(np.polyfit(n[s0:s1], t[s0:s1], 1)[0])
        z = detrend(x[s0:s1], type="linear")
        f = np.fft.rfftfreq(block_size)
        energy = np.abs(np.fft.rfft(z)) ** 2
        pos = (f >= fmin_for_median) & (f <= fmax_for_median)
        med = float(np.median(energy[pos]))
        energy = energy / (med + 1e-30)

        ft = omega * slope / (2.0 * math.pi)
        ok = (ft >= f[1]) & (ft <= f[-1])
        vals = np.interp(ft[ok], f, energy)
        acc[ok] += np.log1p(vals)
        valid[ok] += 1.0

    score = np.divide(
        acc,
        valid,
        out=np.full_like(acc, np.nan),
        where=valid > 0,
    )
    return SpectrumResult(omega=omega, score=score, valid_blocks=valid)


def comb_targets(m_min: int = 2, m_max: int = 13) -> np.ndarray:
    if m_min < 2 or m_max < m_min:
        raise ValueError("require 2 <= m_min <= m_max")
    return np.log(np.arange(m_min, m_max + 1, dtype=float))


def comb_score(
    spectrum: SpectrumResult,
    *,
    m_min: int = 2,
    m_max: int = 13,
) -> float:
    targets = comb_targets(m_min, m_max)
    vals = np.interp(targets, spectrum.omega, spectrum.score)
    return float(np.nanmean(vals))


def common_shift_scan(
    spectrum: SpectrumResult,
    *,
    m_min: int = 2,
    m_max: int = 13,
    shift_min: float = -0.25,
    shift_max: float = 0.25,
    n_shift: int = 2001,
) -> tuple[np.ndarray, np.ndarray]:
    targets = comb_targets(m_min, m_max)
    shifts = np.linspace(shift_min, shift_max, n_shift)
    scores = np.empty_like(shifts)
    for i, delta in enumerate(shifts):
        scores[i] = np.nanmean(
            np.interp(targets + delta, spectrum.omega, spectrum.score)
        )
    return shifts, scores


def jitter_null(
    spectrum: SpectrumResult,
    *,
    m_min: int = 2,
    m_max: int = 13,
    B: int = 20000,
    half_width: float = 0.20,
    seed: int = 20260822,
) -> tuple[float, np.ndarray]:
    """Independent per-target uniform-jitter diagnostic null."""
    targets = comb_targets(m_min, m_max)
    observed = comb_score(spectrum, m_min=m_min, m_max=m_max)
    rng = np.random.default_rng(seed)
    null = np.empty(B, dtype=float)
    for i in range(B):
        jitter = rng.uniform(-half_width, half_width, size=len(targets))
        null[i] = np.nanmean(
            np.interp(targets + jitter, spectrum.omega, spectrum.score)
        )
    return observed, null


def score_comb_with_null(
    spectrum: SpectrumResult,
    *,
    m_min: int = 2,
    m_max: int = 13,
    B: int = 20000,
    half_width: float = 0.20,
    seed: int = 20260822,
) -> CombResult:
    observed, null = jitter_null(
        spectrum,
        m_min=m_min,
        m_max=m_max,
        B=B,
        half_width=half_width,
        seed=seed,
    )
    p = (1.0 + float(np.sum(null >= observed))) / (B + 1.0)
    shifts, shifted_scores = common_shift_scan(
        spectrum, m_min=m_min, m_max=m_max
    )
    j = int(np.nanargmax(shifted_scores))
    return CombResult(
        score=observed,
        null_median=float(np.median(null)),
        null_q95=float(np.quantile(null, 0.95)),
        null_q99=float(np.quantile(null, 0.99)),
        empirical_p_ge=p,
        best_common_shift=float(shifts[j]),
        best_common_shift_score=float(shifted_scores[j]),
    )


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    p = np.asarray(p_values, dtype=float)
    if p.ndim != 1:
        raise ValueError("p_values must be 1D")
    m = len(p)
    order = np.argsort(p)
    ranked = p[order]
    adjusted = ranked * m / np.arange(1, m + 1, dtype=float)
    adjusted = np.minimum.accumulate(adjusted[::-1])[::-1]
    adjusted = np.clip(adjusted, 0.0, 1.0)
    out = np.empty_like(adjusted)
    out[order] = adjusted
    return out
