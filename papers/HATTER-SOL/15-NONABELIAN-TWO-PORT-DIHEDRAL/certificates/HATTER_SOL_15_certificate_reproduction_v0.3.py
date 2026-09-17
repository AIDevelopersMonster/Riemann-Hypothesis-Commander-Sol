# HATTER-SOL-15 v0.3 release certificate reproduction
# Exact rational assertions; Python standard library only.
from fractions import Fraction
from math import comb

class I:
    def __init__(self, lo, hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        if self.lo>self.hi: self.lo,self.hi=self.hi,self.lo
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self + (-(o if isinstance(o,I) else I(o)))
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o)
        assert o.lo>0 or o.hi<0
        vals=[self.lo/o.lo,self.lo/o.hi,self.hi/o.lo,self.hi/o.hi]
        return I(min(vals),max(vals))

def horner(c,x):
    out=I(c[-1])
    for a in reversed(c[:-1]): out=out*x+a
    return out

H_NUM={
2:[8,-5,-5],
3:[72,36,-200,-225,-63],
4:[256,608,-1120,-4730,-5316,-2503,-429],
5:[3200,16000,-8000,-186800,-457408,-520240,-313840,-97145,-12155],
6:[9216,77184,65408,-1234464,-5537280,-11191712,-12945888,-9082386,-3825100,-890589,-88179],
7:[50176,627200,1505280,-12418560,-95472384,-300811392,-552681600,-650654760,-506404360,-259754572,-84542976,-15833755,-1300075],
}
H_DEN={2:2,3:8,4:16,5:128,6:256,7:1024}
def h_interval(m,y):
    if m==1: return (I(2)-y)/(I(2)+y)
    r=horner(H_NUM[m],y); d=Fraction(H_DEN[m]); return I(r.lo/d,r.hi/d)

N=200
global_lb={}
for m in range(2,8):
    best=None
    for i in range(N):
        y=I(Fraction(i,6*N),Fraction(i+1,6*N))
        lb=h_interval(m,y).lo
        best=lb if best is None or lb<best else best
    assert best>0; global_lb[m]=best

BETA={1:Fraction(123,1000),2:Fraction(51,100),3:Fraction(129,100),4:Fraction(27,10),5:Fraction(101,20),6:Fraction(79,10),7:Fraction(19,10)}
near_lb={}
for m in range(1,8):
    best=None
    for i in range(N):
        lo=Fraction(1,7)+(Fraction(1,6)-Fraction(1,7))*Fraction(i,N)
        hi=Fraction(1,7)+(Fraction(1,6)-Fraction(1,7))*Fraction(i+1,N)
        y=I(lo,hi); q=y*h_interval(m,y); lb=q.lo
        best=lb if best is None or lb<best else best
    assert best>BETA[m]; near_lb[m]=best

near=Fraction(0)
for m in range(1,8):
    near += Fraction(comb(2*m,m),m)*Fraction(100,1281)**m*BETA[m]
assert near>0 and near*near>Fraction(4,3375)

y0=Fraction(400,441)
head=sum((y0**k)*Fraction(1,(k+8)**2) for k in range(15))
tail=y0**15*Fraction(1,23**2)*Fraction(1,1-y0)
series_bound=head+tail
assert series_bound<Fraction(1,15)

d0=Fraction(21,10); mu0=d0+2
q1sq=Fraction(16)*(mu0/(mu0*mu0-1))**8
tailsq=Fraction(4**16,3600)*Fraction(8,15)*d0**(-31)
assert q1sq>tailsq

nu=Fraction(1,14)
pos=2*nu**8+7*nu**7+15*nu**6+21*nu**5+25*nu**4+16*nu**3+nu**2
assert pos<1

print('PASS: all exact assertions succeeded')
print('near_lower =', float(near))
print('near_margin_sq =', float(near*near-Fraction(4,3375)))
print('series_bound =', float(series_bound), '<', float(Fraction(1,15)))
print('far_endpoint_squared_ratio =', float(q1sq/tailsq))
print('global_H_min =', min(float(v) for v in global_lb.values()))
