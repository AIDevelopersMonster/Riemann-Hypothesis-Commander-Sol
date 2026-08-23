"""Shifted-lattice utilities for RH-SOL-02."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Sequence
import math
import numpy as np

FillRule = Literal["winding", "even-odd"]

@dataclass(frozen=True)
class ShiftCount:
    dx: float
    dy: float
    count: int

def _closed_vertices(vertices: np.ndarray) -> np.ndarray:
    v = np.asarray(vertices, dtype=float)
    if v.ndim != 2 or v.shape[1] != 2 or len(v) < 3:
        raise ValueError("vertices must have shape (N, 2) with N >= 3")
    if not np.allclose(v[0], v[-1]):
        v = np.vstack([v, v[0]])
    return v

def polygon_area(vertices: np.ndarray) -> float:
    """Absolute shoelace area; exact filled area only for simple polygons."""
    v = _closed_vertices(vertices)
    x0, y0 = v[:-1, 0], v[:-1, 1]
    x1, y1 = v[1:, 0], v[1:, 1]
    return 0.5 * abs(float(np.sum(x0 * y1 - x1 * y0)))

def _point_segment_distance_sq(points: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ab = b - a
    denom = float(np.dot(ab, ab))
    if denom == 0.0:
        d = points - a
        return np.einsum("ij,ij->i", d, d)
    t = np.clip(((points - a) @ ab) / denom, 0.0, 1.0)
    proj = a + t[:, None] * ab
    d = points - proj
    return np.einsum("ij,ij->i", d, d)

def boundary_mask(points: np.ndarray, vertices: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    v = _closed_vertices(vertices)
    p = np.asarray(points, dtype=float)
    mask = np.zeros(len(p), dtype=bool)
    tol2 = tol * tol
    for a, b in zip(v[:-1], v[1:]):
        mask |= _point_segment_distance_sq(p, a, b) <= tol2
    return mask

def winding_numbers(points: np.ndarray, vertices: np.ndarray) -> np.ndarray:
    v = _closed_vertices(vertices)
    p = np.asarray(points, dtype=float)
    wn = np.zeros(len(p), dtype=np.int32)
    px, py = p[:, 0], p[:, 1]
    for a, b in zip(v[:-1], v[1:]):
        ax, ay = a
        bx, by = b
        cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
        upward = (ay <= py) & (by > py) & (cross > 0)
        downward = (ay > py) & (by <= py) & (cross < 0)
        wn[upward] += 1
        wn[downward] -= 1
    return wn

def even_odd_inside(points: np.ndarray, vertices: np.ndarray) -> np.ndarray:
    v = _closed_vertices(vertices)
    p = np.asarray(points, dtype=float)
    x, y = p[:, 0], p[:, 1]
    inside = np.zeros(len(p), dtype=bool)
    for a, b in zip(v[:-1], v[1:]):
        x0, y0 = a
        x1, y1 = b
        crosses_y = (y0 > y) != (y1 > y)
        denom = y1 - y0
        x_cross = np.empty_like(x)
        x_cross.fill(np.inf)
        valid = crosses_y
        x_cross[valid] = x0 + (y[valid] - y0) * (x1 - x0) / denom
        inside ^= valid & (x < x_cross)
    return inside

def interior_mask(points: np.ndarray, vertices: np.ndarray, *, rule: FillRule = "winding", boundary_tol: float = 1e-10) -> np.ndarray:
    p = np.asarray(points, dtype=float)
    on_boundary = boundary_mask(p, vertices, tol=boundary_tol)
    if rule == "winding":
        inside = winding_numbers(p, vertices) != 0
    elif rule == "even-odd":
        inside = even_odd_inside(p, vertices)
    else:
        raise ValueError(f"unknown fill rule: {rule}")
    return inside & ~on_boundary

def filled_area(vertices: np.ndarray, *, rule: FillRule = "winding") -> float:
    """Area of the polygonal filled region under the declared fill rule.

    Shapely is imported lazily. The closed polyline is noded at crossings,
    polygonized into planar faces, and one representative point per face is
    classified by the same winding/even-odd rule used for lattice points.
    """
    try:
        from shapely.geometry import LineString
        from shapely.ops import polygonize, unary_union
    except ImportError as exc:
        raise RuntimeError("filled_area requires shapely>=2") from exc
    v = _closed_vertices(vertices)
    faces = list(polygonize(unary_union(LineString(v))))
    total = 0.0
    for face in faces:
        rp = face.representative_point()
        p = np.array([[rp.x, rp.y]], dtype=float)
        if rule == "winding":
            keep = winding_numbers(p, v)[0] != 0
        elif rule == "even-odd":
            keep = bool(even_odd_inside(p, v)[0])
        else:
            raise ValueError(f"unknown fill rule: {rule}")
        if keep:
            total += float(face.area)
    return total

def shifted_lattice_points(vertices: np.ndarray, delta: Sequence[float]) -> np.ndarray:
    v = _closed_vertices(vertices)
    dx, dy = map(float, delta)
    if not (0.0 <= dx < 1.0 and 0.0 <= dy < 1.0):
        raise ValueError("delta components must lie in [0, 1)")
    xmin, ymin = np.min(v[:, 0]), np.min(v[:, 1])
    xmax, ymax = np.max(v[:, 0]), np.max(v[:, 1])
    ix0 = math.floor(xmin - dx) - 1
    ix1 = math.ceil(xmax - dx) + 1
    iy0 = math.floor(ymin - dy) - 1
    iy1 = math.ceil(ymax - dy) + 1
    xs = np.arange(ix0, ix1 + 1, dtype=float) + dx
    ys = np.arange(iy0, iy1 + 1, dtype=float) + dy
    xx, yy = np.meshgrid(xs, ys, indexing="xy")
    return np.column_stack([xx.ravel(), yy.ravel()])

def shifted_count(vertices: np.ndarray, delta: Sequence[float], *, rule: FillRule = "winding", boundary_tol: float = 1e-10) -> int:
    points = shifted_lattice_points(vertices, delta)
    return int(np.count_nonzero(interior_mask(points, vertices, rule=rule, boundary_tol=boundary_tol)))

def interior_lattice_points(vertices: np.ndarray, delta: Sequence[float] = (0.0, 0.0), *, rule: FillRule = "winding", boundary_tol: float = 1e-10) -> np.ndarray:
    points = shifted_lattice_points(vertices, delta)
    return points[interior_mask(points, vertices, rule=rule, boundary_tol=boundary_tol)]

def translation_grid(q: int) -> np.ndarray:
    if q <= 0:
        raise ValueError("q must be positive")
    s = (np.arange(q, dtype=float) + 0.5) / q
    dx, dy = np.meshgrid(s, s, indexing="xy")
    return np.column_stack([dx.ravel(), dy.ravel()])

def scan_translations(vertices: np.ndarray, q: int, *, rule: FillRule = "winding", boundary_tol: float = 1e-10) -> list[ShiftCount]:
    out: list[ShiftCount] = []
    for dx, dy in translation_grid(q):
        out.append(ShiftCount(float(dx), float(dy), shifted_count(vertices, (dx, dy), rule=rule, boundary_tol=boundary_tol)))
    return out

def scan_translations_fast(vertices: np.ndarray, q: int, *, rule: FillRule = "winding", boundary_tol: float = 1e-10) -> list[ShiftCount]:
    """Evaluate all q^2 midpoint translations in one fine-grid classification.

    The union of lattices Z^2 + ((i+1/2)/q,(j+1/2)/q) is a Cartesian grid of
    spacing 1/q. Each fine-grid point is tagged by its translation residue and
    classified only once.
    """
    if q <= 0:
        raise ValueError("q must be positive")
    v = _closed_vertices(vertices)
    xmin, ymin = np.min(v[:, 0]), np.min(v[:, 1])
    xmax, ymax = np.max(v[:, 0]), np.max(v[:, 1])
    bx = np.arange(math.floor(xmin) - 1, math.ceil(xmax) + 1, dtype=float)
    by = np.arange(math.floor(ymin) - 1, math.ceil(ymax) + 1, dtype=float)
    frac = (np.arange(q, dtype=float) + 0.5) / q

    xs = (bx[:, None] + frac[None, :]).ravel()
    x_index = np.tile(np.arange(q, dtype=np.int32), len(bx))
    ys = (by[:, None] + frac[None, :]).ravel()
    y_index = np.tile(np.arange(q, dtype=np.int32), len(by))

    xx, yy = np.meshgrid(xs, ys, indexing="xy")
    ii, jj = np.meshgrid(x_index, y_index, indexing="xy")
    points = np.column_stack([xx.ravel(), yy.ravel()])
    inside = interior_mask(points, v, rule=rule, boundary_tol=boundary_tol)
    codes = jj.ravel()[inside] * q + ii.ravel()[inside]
    counts = np.bincount(codes, minlength=q * q)
    deltas = translation_grid(q)
    return [ShiftCount(float(dx), float(dy), int(counts[k])) for k, (dx, dy) in enumerate(deltas)]

def translation_mean(counts: Iterable[ShiftCount]) -> float:
    vals = [c.count for c in counts]
    if not vals:
        raise ValueError("no counts")
    return float(np.mean(vals))

def translation_variance(counts: Iterable[ShiftCount]) -> float:
    vals = [c.count for c in counts]
    if not vals:
        raise ValueError("no counts")
    return float(np.var(vals))
