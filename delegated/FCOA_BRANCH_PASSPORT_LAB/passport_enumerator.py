from itertools import permutations


def points(N):
    return tuple(range(N + 1))


def times_m0(N, a, b):
    if a == 0 and 1 <= b <= N:
        return ("P", 0)
    if 2 <= a <= N and b == 0:
        return ("Es", a)
    if a == 1 and 2 <= b <= N:
        return ("P", b)
    if 2 <= a <= N and b == 1:
        return ("P", a)
    if 2 <= a <= N and a == b:
        return ("Ex", a)
    return None


def g3s(N, a, b):
    r = times_m0(N, a, b)
    if r is not None:
        return r
    if 2 <= a <= N and 2 <= b <= N and abs(a - b) == 1:
        return ("Om", 0)
    return None


def g3c(N, a, b):
    r = times_m0(N, a, b)
    if r is not None:
        return r
    if 2 <= a < N and b == a + 1:
        return ("Op", 0)
    if 2 <= b < N and a == b + 1:
        return ("Om", 0)
    return None


def g3a(N, a, b):
    r = g3c(N, a, b)
    if r is not None:
        return r
    if a == 1 and b == 0:
        return ("Op", 0)
    return None


def g4c(N, a, b):
    r = times_m0(N, a, b)
    if r is not None:
        return r
    if 2 <= a <= N and 2 <= b <= N and a != b:
        return ("Op", 0) if a < b else ("Om", 0)
    return None


def g4a(N, a, b):
    r = g4c(N, a, b)
    if r is not None:
        return r
    if a == 1 and b == 0:
        return ("Op", 0)
    return None


OPS = {
    "G3-S": g3s,
    "G3-C": g3c,
    "G3-A": g3a,
    "G4-C": g4c,
    "G4-A": g4a,
}


def all_base_permutations(N):
    base = points(N)
    for image in permutations(base):
        yield dict(zip(base, image))


def permute_backbone_output(value, p):
    tag, i = value
    if tag == "P":
        return ("P", p[i])
    if tag in ("Es", "Ex"):
        return (tag, p[i])
    return value


def definedness_automorphisms(N, op):
    base = points(N)
    domain = {(a, b) for a in base for b in base if op(N, a, b) is not None}
    good = []
    for p in all_base_permutations(N):
        if all(
            (((p[a], p[b]) in domain) == ((a, b) in domain))
            for a in base
            for b in base
        ):
            good.append(p)
    return good


def full_operation_base_automorphisms(N, op):
    """Enumerate base permutations extendable to full-operation automorphisms.

    Backbone P/Es/Ex outputs must transform with the base permutation. Anonymous
    Om/Op outputs are not fixed individually: only their equality partition must
    be transported bijectively. No expected automorphism formula is used.
    """
    base = points(N)
    cells = [(a, b, op(N, a, b)) for a in base for b in base if op(N, a, b) is not None]
    table = {(a, b): value for a, b, value in cells}
    good = []

    for p in all_base_permutations(N):
        forward = {}
        inverse = {}
        ok = True

        for a, b, value in cells:
            moved = table.get((p[a], p[b]))
            if moved is None:
                ok = False
                break

            tag = value[0]
            if tag in ("P", "Es", "Ex"):
                if permute_backbone_output(value, p) != moved:
                    ok = False
                    break
            else:
                if value in forward and forward[value] != moved:
                    ok = False
                    break
                if moved in inverse and inverse[moved] != value:
                    ok = False
                    break
                forward[value] = moved
                inverse[moved] = value

        if ok:
            good.append(p)

    return good


def cycle_signature(p):
    seen = set()
    cycles = []
    for x in sorted(p):
        if x in seen:
            continue
        cycle = []
        y = x
        while y not in seen:
            seen.add(y)
            cycle.append(y)
            y = p[y]
        if len(cycle) > 1:
            cycles.append(tuple(cycle))
    return tuple(cycles) if cycles else ("id",)


def main():
    for N in range(3, 7):
        print("N =", N)
        for name, op in OPS.items():
            d = definedness_automorphisms(N, op)
            f = full_operation_base_automorphisms(N, op)
            print(
                name,
                "DefAut=", len(d),
                "FullBaseAut=", len(f),
                "Full=", [cycle_signature(p) for p in f],
            )
        print()


if __name__ == "__main__":
    main()
