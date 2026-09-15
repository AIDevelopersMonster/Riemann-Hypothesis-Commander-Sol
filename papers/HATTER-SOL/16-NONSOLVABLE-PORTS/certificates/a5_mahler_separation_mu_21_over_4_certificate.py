#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import permutations

N = 5
ID = tuple(range(N))


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    out = [0] * N
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def parity(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2


G = [p for p in permutations(range(N)) if parity(p) == 0]
assert len(G) == 60
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), INV[h])


def commutator(a, b):
    return compose(compose(compose(a, b), INV[a]), INV[b])


def subgroup_generated(a, b):
    seen = {ID}
    todo = deque([ID])
    gens = (a, b, INV[a], INV[b])
    while todo:
        x = todo.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def cycle_lengths(p):
    seen = [False] * N
    lengths = []
    for i in range(N):
        if seen[i]:
            continue
        j = i
        n = 0
        while not seen[j]:
            seen[j] = True
            n += 1
            j = p[j]
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))


g5 = (1, 2, 3, 4, 0)
g5_sq = compose(g5, g5)
C5A = {conjugate(h, g5) for h in G}
C5B = {conjugate(h, g5_sq) for h in G}
assert len(C5A) == len(C5B) == 12 and C5A.isdisjoint(C5B)


def class_name(g):
    ct = cycle_lengths(g)
    if ct == (1, 1, 1, 1, 1):
        return "1A"
    if ct == (2, 2, 1):
        return "2A"
    if ct == (3, 1, 1):
        return "3A"
    if ct == (5,):
        return "5A" if g in C5A else "5B"
    raise AssertionError(ct)


# chi_3(g) = (a + b sqrt(5))/2.
CHI_NUM = {
    "1A": (6, 0),
    "2A": (-2, 0),
    "3A": (0, 0),
    "5A": (1, 1),
    "5B": (1, -1),
}

# Complete generating-pair enumeration.
generating_pairs = []
for a in G:
    for b in G:
        if len(subgroup_generated(a, b)) == 60:
            generating_pairs.append((a, b))
assert len(generating_pairs) == 2280
assert Counter(class_name(commutator(a, b)) for a, b in generating_pairs) == Counter(
    {"3A": 1080, "5A": 600, "5B": 600}
)

# Simultaneous conjugacy representatives.
unseen = set(generating_pairs)
reps = []
while unseen:
    a, b = next(iter(unseen))
    orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
    assert len(orbit) == 60
    reps.append((a, b))
    unseen -= orbit
assert len(reps) == 38
assert Counter(class_name(commutator(a, b)) for a, b in reps) == Counter(
    {"3A": 18, "5A": 10, "5B": 10}
)


def balanced_moment_signatures(a, b, max_n=20):
    """Return exact torus moments S_n as numerators (A,B): S_n=(A+B sqrt5)/2."""
    state = {(ID, 0, 0): 1}
    steps = ((a, 1, 0), (INV[a], -1, 0), (b, 0, 1), (INV[b], 0, -1))
    out = {}
    for n in range(1, max_n + 1):
        nxt = defaultdict(int)
        for (g, ex, ey), count in state.items():
            for h, dx, dy in steps:
                nxt[(compose(g, h), ex + dx, ey + dy)] += count
        state = nxt
        if n % 2 == 0:
            A = 0
            B = 0
            for (g, ex, ey), count in state.items():
                if ex == 0 and ey == 0:
                    aa, bb = CHI_NUM[class_name(g)]
                    A += count * aa
                    B += count * bb
            out[n] = (A, B)
    return tuple(out[n] for n in range(2, max_n + 1, 2))


signature_sets = defaultdict(set)
for a, b in reps:
    signature_sets[class_name(commutator(a, b))].add(balanced_moment_signatures(a, b))
assert {k: len(v) for k, v in signature_sets.items()} == {"3A": 6, "5A": 4, "5B": 4}

# Universal fourth-moment check for d=3:
# S_4 = 84 + 8 chi_3(K).
for a, b in reps:
    sig = balanced_moment_signatures(a, b, 4)
    A4, B4 = sig[1]
    ka, kb = CHI_NUM[class_name(commutator(a, b))]
    # 84 + 8*(ka+kb sqrt5)/2 = (168 + 8 ka + 8 kb sqrt5)/2.
    assert (A4, B4) == (168 + 8 * ka, 8 * kb)

# Exact sqrt(5) enclosure.
SQ5_LO = Fraction(22360679, 10000000)
SQ5_HI = Fraction(22360680, 10000000)
assert SQ5_LO * SQ5_LO < 5 < SQ5_HI * SQ5_HI


def qsqrt_interval(a, b):
    a = Fraction(a)
    b = Fraction(b)
    if b >= 0:
        return (a + b * SQ5_LO, a + b * SQ5_HI)
    return (a + b * SQ5_HI, a + b * SQ5_LO)


def iadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def imul(x, y):
    values = (x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1])
    return (min(values), max(values))


def gap_coeff(sig_i, sig_j, m):
    """Coefficient c_m in M_i-M_j = sum c_m t^m, t=mu^{-2}."""
    ai, bi = sig_i[m - 1]
    aj, bj = sig_j[m - 1]
    return Fraction(-(ai - aj), 4 * m), Fraction(-(bi - bj), 4 * m)


def q_interval(sig_i, sig_j, ta, tb):
    """Interval for Q(t)=t^{-2} sum_{m=2}^{10} c_m t^m."""
    coeffs = [qsqrt_interval(*gap_coeff(sig_i, sig_j, m)) for m in range(2, 11)]
    T = (ta, tb)
    out = coeffs[-1]
    for c in reversed(coeffs[:-1]):
        out = iadd(imul(out, T), c)
    return out


# The theorem range mu >= 21/4 is t <= 16/441 and r=16t<1.
T0 = Fraction(16, 441)
assert 16 * T0 < 1


def normalized_tail_bound(t):
    """Bound |R|/t^2 for all even moments n>=22."""
    if t == 0:
        return Fraction(0)
    return Fraction(3, 11) * (16 ** 11) * (t ** 9) / (1 - 16 * t)


def certify_order(left_class, right_class, subdivisions=8):
    """Certify M_left > M_right throughout 0<t<=T0."""
    minimum_margin = None
    for s in range(subdivisions):
        ta = T0 * Fraction(s, subdivisions)
        tb = T0 * Fraction(s + 1, subdivisions)
        tail = normalized_tail_bound(tb)
        for sig_i in signature_sets[left_class]:
            for sig_j in signature_sets[right_class]:
                lower, _ = q_interval(sig_i, sig_j, ta, tb)
                margin = lower - tail
                assert margin > 0
                if minimum_margin is None or margin < minimum_margin:
                    minimum_margin = margin
    return minimum_margin


# Desired scalar Mahler ordering:
# M(5A) < M(3A) < M(5B).
margin_3_over_5a = certify_order("3A", "5A")
margin_5b_over_3 = certify_order("5B", "3A")

if __name__ == "__main__":
    print("HATTER-SOL-16 exact A5 Mahler separation certificate")
    print("ordered generating pairs =", len(generating_pairs))
    print("simultaneous-conjugacy orbits =", len(reps))
    print("moment signature counts =", {k: len(v) for k, v in sorted(signature_sets.items())})
    print("mu threshold = 21/4 =", float(Fraction(21, 4)))
    print("normalized minimum margin, 3A over 5A =", float(margin_3_over_5a))
    print("normalized minimum margin, 5B over 3A =", float(margin_5b_over_3))
    print("PASS: M(5A) < M(3A) < M(5B) for every generating pair and every mu >= 21/4")
