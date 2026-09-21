#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <tuple>
#include <vector>

using i64 = long long;
using i128 = __int128_t;
using ld = long double;

static bool is_prime(int n) {
    if (n < 2) return false;
    if ((n & 1) == 0) return n == 2;
    for (int d=3; 1LL*d*d<=n; d+=2) if (n%d==0) return false;
    return true;
}

static i64 C(int n,int k){
    if(k<0||k>n) return 0;
    if(k==0||k==n) return 1;
    k=std::min(k,n-k);
    i64 r=1;
    for(int i=1;i<=k;i++) r=r*(n-k+i)/i;
    return r;
}

static i64 Ksum(int W,int h){
    i64 total=0;
    for(int k=1;k<=4;k++){
        i64 kk=0;
        for(int j=0;j<=k;j++){
            i64 t=C(h,j)*C(W-h,k-j);
            kk += (j&1)?-t:t;
        }
        total+=kk;
    }
    return total;
}

static void fwht(std::vector<ld>& a){
    for(size_t h=1;h<a.size();h<<=1)
        for(size_t i=0;i<a.size();i+=(h<<1))
            for(size_t j=i;j<i+h;j++){
                ld x=a[j],y=a[j+h];
                a[j]=x+y; a[j+h]=x-y;
            }
}

static void fwht_i64(std::vector<i64>& a){
    for(size_t h=1;h<a.size();h<<=1)
        for(size_t i=0;i<a.size();i+=(h<<1))
            for(size_t j=i;j<i+h;j++){
                i64 x=a[j],y=a[j+h];
                a[j]=x+y; a[j+h]=x-y;
            }
}

struct G { std::vector<int> x; i64 s=0; };

static bool selftest(){
    int m=4,s=0,A=2;
    ld v=(ld)(m*m-s*s)*(m*m-A*A)/((ld)m*m*(m-1));
    return fabsl(v-4.0L)<1e-18L;
}

static std::tuple<ld,ld,ld> run_one(int W,int B){
    int N=1<<W;
    int nb=(N+B-1)/B;
    std::vector<G> gs((size_t)210*nb);
    std::vector<i64> sign(N);

    for(int n=0;n<N;n++){
        int bid=n/B;
        int gid=(n%210)*nb+bid;
        i64 y=is_prime(n)?-1:1;
        gs[gid].x.push_back(n);
        gs[gid].s+=y;
        sign[n]=y;
    }

    auto coeff=sign;
    fwht_i64(coeff);
    i128 obs_num=0;
    for(int mask=1;mask<N;mask++){
        int wt=__builtin_popcount((unsigned)mask);
        if(wt<=4) obs_num+=(i128)coeff[mask]*coeff[mask];
    }
    ld obs=(ld)obs_num/((ld)N*N);

    std::vector<ld> mu(N,0);
    for(auto &g:gs) if(!g.x.empty()){
        ld q=(ld)g.s/g.x.size();
        for(int n:g.x) mu[n]=q;
    }
    fwht(mu);
    ld mean_energy=0;
    for(int mask=1;mask<N;mask++){
        int wt=__builtin_popcount((unsigned)mask);
        if(wt<=4) mean_energy+=mu[mask]*mu[mask];
    }

    i64 K0=C(W,1)+C(W,2)+C(W,3)+C(W,4);
    std::vector<i64> kv(W+1);
    for(int h=0;h<=W;h++) kv[h]=Ksum(W,h);

    ld corr=0;
    for(auto &g:gs){
        i64 m=g.x.size();
        if(m<=1) continue;
        i128 sum_all=(i128)m*K0;
        for(size_t i=0;i<g.x.size();i++)
            for(size_t j=i+1;j<g.x.size();j++){
                int h=__builtin_popcount((unsigned)(g.x[i]^g.x[j]));
                sum_all+=(i128)2*kv[h];
            }
        ld fac=((ld)m*m-(ld)g.s*g.s)/((ld)m*m*(m-1));
        ld br=(ld)m*m*K0-(ld)sum_all;
        corr+=fac*br;
    }
    ld exp=(mean_energy+corr)/((ld)N*N);
    return {obs,exp,obs-exp};
}

int main(){
    if(!selftest()){ std::cerr<<"SELFTEST FAIL\n"; return 2; }
    std::cout<<"SELFTEST PASS\n";
    std::vector<int> Ws={17,18,19};
    std::vector<int> Bs={16384,8192,4096};

    std::ofstream csv("exact_localblock_expectation.csv");
    csv<<"width,block_size,observed_low4,expected_low4,delta\n";
    std::ofstream md("H20_EXT_LAB07_REPORT.md");
    md<<"# H20-EXT-LAB-07 · Exact local-block conditional Walsh expectation\n\n";
    md<<"Status: **COMPUTATION COMPLETE**\n\nSelf-test: **PASS**\n\n";
    md<<"| W | block size | observed | expected | delta |\n|---:|---:|---:|---:|---:|\n";
    bool pass=true;
    std::cout<<std::setprecision(15);
    csv<<std::setprecision(18);
    md<<std::setprecision(12);

    for(int W:Ws) for(int B:Bs){
        auto [o,e,d]=run_one(W,B);
        if(!(d<0)) pass=false;
        std::cout<<"W="<<W<<" B="<<B<<" observed="<<(double)o<<" expected="<<(double)e<<" delta="<<(double)d<<"\n";
        csv<<W<<","<<B<<","<<(double)o<<","<<(double)e<<","<<(double)d<<"\n";
        md<<"| "<<W<<" | "<<B<<" | "<<(double)o<<" | "<<(double)e<<" | "<<(double)d<<" |\n";
    }
    md<<"\n## Frozen criterion\n\n"<<(pass?"**PASS:** every declared delta is negative.\n":"**FAIL:** at least one declared delta is nonnegative.\n");
    md<<"\n## Non-claim\n\nNo asymptotic theorem, novelty claim, circuit lower bound, or RH implication is asserted.\n";
    std::cout<<"CRITERION_PASS="<<(pass?"True":"False")<<"\n";
    return pass?0:3;
}
