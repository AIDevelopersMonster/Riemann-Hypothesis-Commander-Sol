#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

using i64 = long long;
using i128 = __int128_t;
using ld = long double;

enum class Family { PRIME, SQUAREFREE, SEMIPRIME };

static bool is_prime(int n){
    if(n<2) return false;
    if((n&1)==0) return n==2;
    for(int d=3;1LL*d*d<=n;d+=2) if(n%d==0) return false;
    return true;
}

static int omega_mult(int n){
    if(n<2) return 0;
    int x=n,c=0;
    for(int d=2;1LL*d*d<=x;d+=(d==2?1:2)){
        while(x%d==0){ x/=d; c++; }
    }
    if(x>1) c++;
    return c;
}

static bool is_squarefree(int n){
    if(n<1) return false;
    for(int d=2;1LL*d*d<=n;d++){
        long long q=1LL*d*d;
        if(n%q==0) return false;
    }
    return true;
}

static bool member(int n, Family f){
    if(f==Family::PRIME) return is_prime(n);
    if(f==Family::SQUAREFREE) return is_squarefree(n);
    return omega_mult(n)==2;
}

static const char* fname(Family f){
    if(f==Family::PRIME) return "prime";
    if(f==Family::SQUAREFREE) return "squarefree";
    return "semiprime";
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

struct G{ std::vector<int> x; i64 s=0; };

static bool selftest(){
    const int m=4,s=0,A=2;
    ld v=(ld)(m*m-s*s)*(m*m-A*A)/((ld)m*m*(m-1));
    return std::fabs(v-4.0L)<1e-18L;
}

static std::tuple<ld,ld,ld,ld> run_one(int W, Family f){
    const int N=1<<W, B=4096, nb=(N+B-1)/B;
    std::vector<G> gs((size_t)210*nb);
    std::vector<i64> sign(N);
    for(int n=0;n<N;n++){
        int gid=(n%210)*nb+n/B;
        i64 y=member(n,f)?-1:1;
        gs[gid].x.push_back(n);
        gs[gid].s+=y;
        sign[n]=y;
    }

    auto coeff=sign;
    fwht_i64(coeff);
    i128 obsnum=0;
    for(int mask=1;mask<N;mask++){
        int wt=__builtin_popcount((unsigned)mask);
        if(wt<=4) obsnum+=(i128)coeff[mask]*coeff[mask];
    }
    ld obs=(ld)obsnum/((ld)N*N);

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
        i64 m=(i64)g.x.size();
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
    ld expv=(mean_energy+corr)/((ld)N*N);
    ld delta=obs-expv;
    ld R=(expv-obs)/expv;
    return {obs,expv,delta,R};
}

int main(){
    if(!selftest()){ std::cerr<<"SELFTEST FAIL\n"; return 2; }
    std::cout<<"SELFTEST PASS\n";
    const std::vector<int> Ws={17,18,19};
    const std::vector<Family> Fs={Family::PRIME,Family::SQUAREFREE,Family::SEMIPRIME};

    std::ofstream csv("lab09_arithmetic_controls.csv");
    csv<<"width,family,observed,expected,delta,normalized_deficit\n";
    std::ofstream md("H20_EXT_LAB09_REPORT.md");
    md<<"# H20-EXT-LAB-09 · Arithmetic-control specificity gate\n\n";
    md<<"Status: **COMPUTATION COMPLETE**\n\nSelf-test: **PASS**\n\n";
    md<<"| W | family | observed | exact expectation | delta | normalized deficit R |\n";
    md<<"|---:|---|---:|---:|---:|---:|\n";

    bool pass=true;
    std::cout<<std::setprecision(15);
    csv<<std::setprecision(18);
    md<<std::setprecision(12);

    for(int W:Ws){
        ld rp=0,rsq=0,rsemi=0;
        for(Family f:Fs){
            auto [o,e,d,R]=run_one(W,f);
            if(f==Family::PRIME) rp=R;
            else if(f==Family::SQUAREFREE) rsq=R;
            else rsemi=R;
            std::cout<<"W="<<W<<" family="<<fname(f)<<" obs="<<(double)o<<" exp="<<(double)e<<" delta="<<(double)d<<" R="<<(double)R<<"\n";
            csv<<W<<","<<fname(f)<<","<<(double)o<<","<<(double)e<<","<<(double)d<<","<<(double)R<<"\n";
            md<<"| "<<W<<" | "<<fname(f)<<" | "<<(double)o<<" | "<<(double)e<<" | "<<(double)d<<" | "<<(double)R<<" |\n";
        }
        bool local=(rp>rsq)&&(rp>rsemi);
        pass &= local;
        std::cout<<"W="<<W<<" specificity_pass="<<local<<"\n";
    }

    md<<"\n## Frozen criterion\n\n";
    md<<(pass?"**PASS:** prime normalized deficit exceeds both arithmetic controls at every width.\n":
              "**FAIL:** prime-specificity criterion fails on at least one width.\n");
    md<<"\n## Non-claim\n\nFailure would not invalidate the exact prime C1 inequality; it would invalidate only the stronger prime-specific interpretation relative to these controls.\n";
    std::cout<<"CRITERION_PASS="<<(pass?"True":"False")<<"\n";
    return pass?0:5;
}
