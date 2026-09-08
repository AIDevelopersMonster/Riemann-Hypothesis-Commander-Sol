import itertools

# Article A finite-witness verification.

V = range(5)
arcs = {(4,0),(4,1),(4,2),(4,3),(2,0),(2,1),(3,1),(3,2),(0,3),(1,0)}

def edge(a,b):
    return (a,b) in arcs

def is_auto(p, anti=False):
    for a,b in itertools.permutations(V,2):
        lhs = edge(a,b)
        rhs = edge(p[a],p[b])
        if anti:
            rhs = not rhs
        if lhs != rhs:
            return False
    return True

autos=[]
antis=[]
for perm in itertools.permutations(V):
    if is_auto(perm): autos.append(perm)
    if is_auto(perm, True): antis.append(perm)

cyc=[]
for tri in itertools.combinations(V,3):
    ds=[sum(edge(x,y) for y in tri if y != x) for x in tri]
    if ds == [1,1,1] or sorted(ds) == [1,1,1]:
        cyc.append(tri)

assert len(autos) == 1
assert len(antis) == 0
assert set(cyc) == {(0,1,3),(0,2,3)}

edges=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
vals=[0,0,0,1,0,0,2,1,0,0]
col={tuple(sorted(e)):v for e,v in zip(edges,vals)}

def color(a,b):
    return col[tuple(sorted((a,b)))]

g={0:1,1:0,2:2,3:3,4:4}

# No global output permutation realizes g.
assert not any(
    all(color(g[a],g[b]) == pi[color(a,b)] for a,b in edges)
    for pi in itertools.permutations(range(3))
)

# But every equality relation among ordered cells supported on <=3 vertices is preserved.
for k in range(1,4):
    for S in itertools.combinations(V,k):
        cells=[(a,b) for a in S for b in S if a != b]
        for p,q in itertools.product(cells,cells):
            lhs = color(*p) == color(*q)
            gp=(g[p[0]],g[p[1]])
            gq=(g[q[0]],g[q[1]])
            rhs = color(*gp) == color(*gq)
            assert lhs == rhs

print('PASS: Article A finite witnesses independently verified.')