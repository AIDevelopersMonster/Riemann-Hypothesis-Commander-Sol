#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using i64 = long long;
using ld = long double;

static constexpr int NSAMP=2048;
static constexpr int BATCH=32;
static constexpr uint64_t MASTER_SEED=0x48A7C20E5D1B9F31ULL;

static bool is_prime(int n){
    if(n<2) return false;
    if((n&1)==0) return n==2;
    for(int d=3;1LL*d*d<=n;d+=2) if(n%d==0) return false;
    return true;
}
struct RNG{
    uint64_t s;
    explicit RNG(uint64_t x):s(x){}
    uint64_t next(){
        s += 0x9E3779B97F4A7C15ULL;
        uint64_t z=s;
        z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL;
        z=(z^(z>>27))*0x94D049BB133111EBULL;
        return z^(z>>31);
    }
    uint64_t uniform(uint64_t n){ return n? next()%n:0; }
};

static void fwht_batch(std::vector<int>& a,int N,int B){
    for(int h=1;h<N;h<<=1){
        for(int i=0;i<N;i+=(h<<1)){
            for(int j=i;j<i+h;j++){
                int* p=&a[(size_t)j*B];
                int* q=&a[(size_t)(j+h)*B];
                #pragma GCC ivdep
                for(int b=0;b<B;b++){
                    int x=p[b],y=q[b];
                    p[b]=x+y;
                    q[b]=x-y;
                }
            }
        }
    }
}

static ld observed_low4(int W){
    int N=1<<W;
    std::vector<int> a(N);
    for(int n=0;n<N;n++) a[n]=is_prime(n)?-1:1;
    for(int h=1;h<N;h<<=1)
        for(int i=0;i<N;i+=(h<<1))
            for(int j=i;j<i+h;j++){
                int x=a[j],y=a[j+h];
                a[j]=x+y; a[j+h]=x-y;
            }
    long double e=0;
    for(int m=1;m<N;m++) if(__builtin_popcount((unsigned)m)<=4)
        e += (long double)a[m]*a[m];
    return e/((long double)N*N);
}

struct Group{
    std::vector<int> idx;
    int kprime=0;
};

static std::vector<Group> make_groups(int W){
    int N=1<<W, nb=(N+4095)/4096;
    std::vector<Group> g((size_t)210*nb);
    for(int n=0;n<N;n++){
        int id=(n%210)*nb+(n/4096);
        g[id].idx.push_back(n);
        if(is_prime(n)) g[id].kprime++;
    }
    std::vector<Group> out;
    out.reserve(g.size());
    for(auto &x:g) if(!x.idx.empty()) out.push_back(std::move(x));
    return out;
}

static std::vector<int> base_labels(int W){
    int N=1<<W;
    std::vector<int> y(N,1);
    // Groups with all-prime are essentially only singleton/special cases; setting true labels
    // here ensures fixed cells remain exact. Randomized groups are overwritten sample-wise.
    for(int n=0;n<N;n++) if(is_prime(n)) y[n]=-1;
    return y;
}

static void generate_batch(int W,int sample0,int B,std::vector<int>& a,const std::vector<Group>& groups){
    int N=1<<W;
    // Start all +1; randomized strata then receive exactly kprime minus labels.
    std::fill(a.begin(),a.end(),1);

    for(int b=0;b<B;b++){
        int sid=sample0+b;
        RNG rng(MASTER_SEED ^ (uint64_t(W)<<48) ^ uint64_t(sid)*0xD1342543DE82EF95ULL);
        for(const auto &g:groups){
            const int m=(int)g.idx.size(), k=g.kprime;
            if(k==0) continue;
            if(k==m){
                for(int n:g.idx) a[(size_t)n*B+b]=-1;
                continue;
            }
            // Choose k positions without replacement via partial Fisher-Yates on local 0..m-1.
            // m is about 19-20 for B=4096 x mod210.
            std::array<int,64> tmp{};
            if(m>64){ std::cerr<<"unexpected group size\n"; std::exit(3); }
            for(int i=0;i<m;i++) tmp[i]=i;
            for(int i=0;i<k;i++){
                int j=i+(int)rng.uniform(m-i);
                std::swap(tmp[i],tmp[j]);
                int n=g.idx[tmp[i]];
                a[(size_t)n*B+b]=-1;
            }
        }
    }
}

static std::vector<ld> sample_width(int W){
    int N=1<<W;
    auto groups=make_groups(W);
    std::vector<ld> vals(NSAMP);
    std::vector<int> a((size_t)N*BATCH);

    for(int s0=0;s0<NSAMP;s0+=BATCH){
        generate_batch(W,s0,BATCH,a,groups);
        fwht_batch(a,N,BATCH);
        std::array<long double,BATCH> e{};
        for(int mask=1;mask<N;mask++){
            if(__builtin_popcount((unsigned)mask)>4) continue;
            const int* p=&a[(size_t)mask*BATCH];
            #pragma GCC ivdep
            for(int b=0;b<BATCH;b++) e[b]+=(long double)p[b]*p[b];
        }
        long double den=(long double)N*N;
        for(int b=0;b<BATCH;b++) vals[s0+b]=e[b]/den;
        if((s0+ BATCH)%256==0) std::cout<<"W="<<W<<" samples="<<(s0+BATCH)<<"\n";
    }
    return vals;
}

int main(){
    const std::array<int,3> Ws={17,18,19};
    const std::array<ld,3> exactExp={
        0.0413314797766160L,
        0.0348420660751401L,
        0.0299468618386511L
    };

    std::ofstream csv("lab08_tail_summary.csv");
    csv<<"width,observed,exact_expectation,mc_mean,mc_sd,se,k_le_obs,p_hat,z,mean_consistency_5se,tail_pass\n";
    std::ofstream md("H20_EXT_LAB08_REPORT.md");
    md<<"# H20-EXT-LAB-08 · Conditional permutation tail significance\n\n";
    md<<"Status: **COMPUTATION COMPLETE**\n\n";
    md<<"Master seed: `0x48A7C20E5D1B9F31`\n\n";
    md<<"Samples per width: **2048**\n\n";
    md<<"| W | observed | exact mean | MC mean | SD | K<=obs | p-hat | z | PASS |\n";
    md<<"|---:|---:|---:|---:|---:|---:|---:|---:|---|\n";

    bool overall=true;
    for(int wi=0;wi<3;wi++){
        int W=Ws[wi];
        ld obs=observed_low4(W);
        auto v=sample_width(W);
        ld mean=std::accumulate(v.begin(),v.end(),(ld)0)/v.size();
        ld ss=0;
        int k=0;
        for(ld x:v){ ss+=(x-mean)*(x-mean); if(x<=obs) k++; }
        ld sd=std::sqrt(ss/(v.size()-1));
        ld se=sd/std::sqrt((ld)v.size());
        ld phat=(k+1.0L)/(v.size()+1.0L);
        ld z=(obs-mean)/sd;
        bool meanok=std::fabs(mean-exactExp[wi])<=5*se;
        bool tail=phat<=0.001L;
        bool pass=meanok&&tail;
        overall &= pass;

        std::cout<<std::setprecision(15)
                 <<"W="<<W<<" obs="<<(double)obs<<" exact="<<(double)exactExp[wi]
                 <<" mean="<<(double)mean<<" sd="<<(double)sd<<" K="<<k
                 <<" p="<<(double)phat<<" z="<<(double)z
                 <<" mean5se="<<meanok<<" pass="<<pass<<"\n";

        csv<<std::setprecision(18)<<W<<","<<(double)obs<<","<<(double)exactExp[wi]<<","
           <<(double)mean<<","<<(double)sd<<","<<(double)se<<","<<k<<","
           <<(double)phat<<","<<(double)z<<","<<meanok<<","<<pass<<"\n";

        md<<"| "<<W<<" | "<<std::setprecision(12)<<(double)obs<<" | "<<(double)exactExp[wi]
          <<" | "<<(double)mean<<" | "<<(double)sd<<" | "<<k<<" | "<<(double)phat
          <<" | "<<(double)z<<" | "<<(pass?"YES":"NO")<<" |\n";
    }
    md<<"\n## Frozen criterion\n\n";
    md<<(overall?"**PASS:** all three widths satisfy the frozen tail and mean-consistency criteria.\n":
                 "**FAIL:** at least one width fails the frozen LAB-08 criterion.\n");
    md<<"\n## Non-claim\n\nThis is finite conditional randomization evidence only; no asymptotic theorem, novelty claim, or RH implication follows.\n";
    std::cout<<"CRITERION_PASS="<<(overall?"True":"False")<<"\n";
    return overall?0:4;
}
