# Terminology and notation

- `gamma_n` — ordinate of the n-th selected critical-line zero.
- `H_n` — Argand trajectory `zeta(1/2+it)` between consecutive selected zeros.
- `D_n` — explicitly defined filled domain associated with `H_n`; the fill rule MUST be stated for every experiment.
- `I(n,a,b)` — binary indicator for lattice point `(a,b)` in `D_n`.
- `M_N(a,b)` — multiplicity `sum_{n<=N} I(n,a,b)`.
- `J(n,a,b)` — double-centered dynamic tensor.
- Dirichlet frequency — angular frequency `omega_m = log m`.
- mixing frequency — combinations such as `|log m - log k| = |log(m/k)|`.
- shifted lattice — `(a+delta_x,b+delta_y)`, `(delta_x,delta_y) in [0,1)^2`.
- smooth zero coordinate — coordinate induced by the smooth Riemann-von Mangoldt count.
- actual-zero analysis — analysis performed directly at observed/selected `gamma_n` without replacing them by smooth inversion.

## Interior rule requirement

Every article must explicitly state one of the following (or another formal rule):

- even-odd fill;
- nonzero winding-number fill;
- positive winding-number fill;
- absolute winding-number convention.

Boundary points and numerical tolerance must also be specified.
