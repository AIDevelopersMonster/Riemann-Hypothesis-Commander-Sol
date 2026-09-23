#include <algorithm>
#include <array>
#include <cmath>
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
    for (int d = 3; 1LL*d*d <= n; d += 2) if (n % d == 0) return false;
    return true;
}

static int shell_of(int n) {
    if (n == 0) return -1;
    return 31 - __builtin_clz((unsigned)n);
}

static i64 choose_i64(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    k = std::min(k, n-k);
    i64 r = 1;
    for (int i=1;i<=k;i++) r = r * (n-k+i) / i;
    return r;
}

static i64 kraw_sum_1_4(int W, int h) {
    i64 total = 0;
    for (int k=1;k<=4;k++) {
        i64 kk = 0;
        for (int j=0;j<=k;j++) {
            i64 term = choose_i64(h,j) * choose_i64(W-h,k-j);
            kk += (j & 1) ? -term : term;
        }
        total += kk;
    }
    return total;
}

static void fwht(std::vector<ld>& a) {
    const size_t n = a.size();
    for (size_t h=1; h<n; h<<=1) {
        for (size_t i=0;i<n;i+=(h<<1)) {
            for (size_t j=i;j<i+h;j++) {
                ld x=a[j], y=a[j+h];
                a[j]=x+y; a[j+h]=x-y;
            }
        }
    }
}

static void fwht_i64(std::vector<i64>& a) {
    const size_t n = a.size();
    for (size_t h=1; h<n; h<<=1) {
        for (size_t i=0;i<n;i+=(h<<1)) {
            for (size_t j=i;j<i+h;j++) {
                i64 x=a[j], y=a[j+h];
                a[j]=x+y; a[j+h]=x-y;
            }
        }
    }
}

struct Stratum {
    int residue=0;
    int shell=-1;
    std::vector<int> x;
    i64 s=0; // sign sum
};

static bool self_test() {
    // m=4, signs +,+,-,-, character values +,+,+,-
    // Enumerate all 6 choices for positions of the two + signs.
    const int m=4;
    const int s=0;
    const std::array<int,4> chi = {1,1,1,-1};
    int A = std::accumulate(chi.begin(), chi.end(), 0);
    ld mean = (ld)s*A/m;
    ld var_formula = (ld)(m*m-s*s)*(m*m-A*A)/((ld)m*m*(m-1));
    ld ex2 = mean*mean + var_formula;

    ld acc=0;
    int count=0;
    for (int a=0;a<4;a++) for (int b=a+1;b<4;b++) {
        std::array<int,4> y = {-1,-1,-1,-1};
        y[a]=1; y[b]=1;
        int z=0;
        for (int i=0;i<4;i++) z += y[i]*chi[i];
        acc += (ld)z*z;
        count++;
    }
    ld brute = acc/count;
    return fabsl(ex2-brute) < 1e-18L;
}

static std::tuple<ld,ld,ld,ld> run_width(int W) {
    const int N = 1<<W;
    const int shells = W + 1; // shell -1 mapped to 0, shell j to j+1
    std::vector<Stratum> strata(210*shells);

    std::vector<i64> prime_sign(N);
    for (int n=0;n<N;n++) {
        int sh=shell_of(n);
        int si=sh+1;
        int id=(n%210)*shells+si;
        auto &g=strata[id];
        g.residue=n%210;
        g.shell=sh;
        g.x.push_back(n);
        i64 y=is_prime(n)?-1:1;
        g.s += y;
        prime_sign[n]=y;
    }

    // observed exact low-degree energy
    auto coeff = prime_sign;
    fwht_i64(coeff);
    i128 obs_num=0;
    for (int mask=1;mask<N;mask++) {
        int wt=__builtin_popcount((unsigned)mask);
        if (wt<=4) obs_num += (i128)coeff[mask]*coeff[mask];
    }
    ld observed = (ld)obs_num / ((ld)N*(ld)N);

    // exact conditional mean function mu(x)=s_g/m_g
    std::vector<ld> mu(N,0);
    for (auto &g: strata) if (!g.x.empty()) {
        ld muv=(ld)g.s/(ld)g.x.size();
        for (int n:g.x) mu[n]=muv;
    }
    fwht(mu);
    ld mean_energy=0;
    for (int mask=1;mask<N;mask++) {
        int wt=__builtin_popcount((unsigned)mask);
        if (wt<=4) mean_energy += mu[mask]*mu[mask];
    }

    const i64 K0 = choose_i64(W,1)+choose_i64(W,2)+choose_i64(W,3)+choose_i64(W,4);
    std::vector<i64> K(W+1);
    for (int h=0;h<=W;h++) K[h]=kraw_sum_1_4(W,h);

    ld correction=0;
    for (auto &g: strata) {
        i64 m=(i64)g.x.size();
        if (m<=1) continue;
        i128 sum_all=(i128)m*K0; // diagonal
        for (size_t i=0;i<g.x.size();i++) {
            for (size_t j=i+1;j<g.x.size();j++) {
                int h=__builtin_popcount((unsigned)(g.x[i]^g.x[j]));
                sum_all += (i128)2*K[h];
            }
        }
        ld factor=((ld)m*m-(ld)g.s*g.s)/((ld)m*m*(m-1));
        ld bracket=(ld)m*m*(ld)K0-(ld)sum_all;
        correction += factor*bracket;
    }

    ld expected=(mean_energy+correction)/((ld)N*(ld)N);
    ld delta=observed-expected;
    return {observed, expected, delta, correction/((ld)N*(ld)N)};
}

int main(int argc, char** argv) {
    if (!self_test()) {
        std::cerr << "SELFTEST FAIL\n";
        return 2;
    }
    std::cout << "SELFTEST PASS\n";

    std::vector<int> widths;
    std::string out_csv="exact_stratified_expectation.csv";
    std::string out_md="H20_EXT_LAB06_REPORT.md";
    for (int i=1;i<argc;i++) {
        std::string a=argv[i];
        if (a=="--csv" && i+1<argc) out_csv=argv[++i];
        else if (a=="--md" && i+1<argc) out_md=argv[++i];
        else widths.push_back(std::stoi(a));
    }
    if (widths.empty()) widths={13,14,15,16,17,18,19};

    std::ofstream csv(out_csv);
    csv << "width,observed_low4,expected_low4,delta,variance_correction\n";

    std::ofstream md(out_md);
    md << "# H20-EXT-LAB-06 · Exact conditional expectation of low-degree Walsh energy\n\n";
    md << "Status: **COMPUTATION COMPLETE**\n\n";
    md << "Self-test: **PASS**\n\n";
    md << "| W | observed low-4 | exact conditional expectation | delta |\n";
    md << "|---:|---:|---:|---:|\n";

    bool all_negative=true;
    std::cout << std::setprecision(15);
    csv << std::setprecision(18);
    md << std::setprecision(12);

    for (int W: widths) {
        auto [obs, expv, delta, corr]=run_width(W);
        if (!(delta<0)) all_negative=false;
        std::cout << "W=" << W
                  << " observed=" << (double)obs
                  << " expected=" << (double)expv
                  << " delta=" << (double)delta
                  << "\n";
        csv << W << "," << (double)obs << "," << (double)expv << "," << (double)delta << "," << (double)corr << "\n";
        md << "| " << W << " | " << (double)obs << " | " << (double)expv << " | " << (double)delta << " |\n";
    }

    md << "\n## Frozen criterion\n\n";
    md << (all_negative ? "**PASS:** delta is negative for every declared width W=13..19.\n"
                        : "**FAIL:** at least one declared width has nonnegative delta.\n");
    md << "\n## Exact finite statement\n\n";
    md << "Observed Walsh coefficients are exact integers. The conditional baseline expectation is evaluated from the exact finite stratum moment formula.\n";
    md << "\n## Non-claim\n\n";
    md << "No asymptotic theorem, novelty claim, circuit lower bound, or RH implication is asserted.\n";

    std::cout << "CRITERION_PASS=" << (all_negative ? "True" : "False") << "\n";
    return all_negative ? 0 : 3;
}
