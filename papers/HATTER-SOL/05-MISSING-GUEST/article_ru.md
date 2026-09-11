# Чаепития в аддитивно-мультипликативном мире с Шляпником Sol — V

## Кого нет за столом? Пустые волокна, спектр точных опор и выживание перестановки \(3\leftrightarrow5\)

**Малачевский А.А.**  
ORCID: **0009-0008-6009-3196**

AI research collaborator: **Commander Sol · Hatter Sol**

---

## Аннотация

Рассматривается ориентированный граф простых чисел

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Он хранит только radical-predecessor информацию: какие простые делят \(p-1\), но забывает их кратности. В предыдущей статье серии задача об автоморфизмах \(\Pi\) была сведена к multiplicity tower точных predecessor-волокон

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Настоящая работа исследует первую нетривиальную локальную симметрию

\[
\tau=(3\ 5),
\]

возникающую из равенства

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

Мы доказываем: (i) невозможность уничтожить exact-support family конечным набором фиксированных делителей; (ii) cyclotomic dimension barrier для показателей; (iii) строгую локальную sieve-asymmetry между supports \(\{2,3\}\) и \(\{2,5\}\), включая weighted asymptotics; (iv) наследование этой асимметрии по exact-descendant chains; (v) cardinality wall, стирающий количественные различия после перехода к бесконечным countable fibers; (vi) finite-fiber compactness theorem, превращающий глобальную гибель seed symmetry в конечную obstruction tree under FFC; (vii) density-one forward-cone theorem и более сильный факт, что уже directed future на расстоянии не более двух имеет относительную prime density one; (viii) Causal Survival Theorem under Cone-Fiber Infinitude.

Центральный вопрос

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}
\]

остаётся открытым. Основной результат статьи состоит не в закрытии этого yes/no вопроса, а в резком сужении пространства возможных механизмов: локальная арифметическая асимметрия существует и даже усиливается, но сама по себе невидима multiplicity tower, пока соответствующие exact fibers бесконечны.

---

# 1. От первой чашки к пятой

В чисто мультипликативной структуре

\[
(\mathbb N_{>0},\times)
\]

положительные целые образуют свободный коммутативный моноид на множестве простых. Поэтому

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

С точки зрения одной операции умножения простые не имеют индивидуальных имён.

В полной натуральной арифметике

\[
(\mathbb N,+,\times,0,1)
\]

ситуация противоположна: каждое натуральное число фиксируется, и группа автоморфизмов тривиальна.

Вся серия HATTER-SOL спрашивает, где между этими крайностями простые перестают быть взаимозаменяемыми.

В HATTER-SOL-03 была рассмотрена более сильная predecessor-информация, достаточная для жёсткости. В HATTER-SOL-04 информация была ослаблена до графа

\[
D(q,p)\iff q\mid p-1.
\]

Именно здесь появляется первый по-настоящему тонкий вопрос: достаточно ли знать только support простых делителей \(p-1\), забывая их кратности, чтобы уничтожить все prime-renaming symmetries?

---

# 2. Exact predecessor fibers

Для простого \(p\) обозначим

\[
\operatorname{Pred}(p)=\{q\in\mathbb P:q\mid p-1\}.
\]

Для конечного \(S\subseteq\mathbb P\), \(2\in S\), положим

\[
X_S=\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Тогда

\[
p\in X_S
\]

эквивалентно существованию положительных показателей \((e_q)_{q\in S}\), для которых

\[
p=1+\prod_{q\in S}q^{e_q}
\]

является простым.

Следовательно, exact-support problem — это не внешняя задача о специальных экспоненциальных формах, а точная арифметическая форма условия \(\operatorname{Pred}(p)=S\).

HATTER-SOL-04 показал, что продолжение конечновысотного автоморфизма определяется равенствами соответствующих multiplicities \(\mu(S)\).

Отсюда естественный тест:

\[
\tau=(3\ 5).
\]

На первом слое он допустим, потому что

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

---

# 3. Первый ложный путь: конечное покрытие фиксированными делителями

Наивная идея состоит в том, чтобы найти support \(S\), для которого вся family

\[
1+\prod_{q\in S}q^{e_q}
\]

покрывается конечным набором фиксированных простых делителей.

Такое покрытие не работает.

## Теорема 3.1 — finite fixed-divisor escape

Пусть \(S\ni2\) — фиксированный конечный support, а \(T\) — конечное множество простых. Тогда существуют положительные exponent vectors \((e_q)_{q\in S}\), для которых

\[
1+\prod_{q\in S}q^{e_q}
\]

не делится ни на один \(\ell\in T\).

Следовательно, exact-support candidate family нельзя уничтожить конечным fixed-divisor covering argument.

Это важный отрицательный результат: если empty fiber существует, его пустота должна иметь более глубокую причину.

---

# 4. Cyclotomic dimension barrier

Пусть

\[
N_S(\mathbf e)=1+q_1^{e_1}\cdots q_k^{e_k}.
\]

## Теорема 4.1

Если \(N_S(\mathbf e)\) простое, то

\[
\boxed{\gcd(e_1,\ldots,e_k)\text{ является степенью }2.}
\]

### Доказательство

Если нечётное \(d>1\) делит все показатели, то \(e_i=df_i\), и

\[
N_S(\mathbf e)
=A^d+1,
\qquad
A=q_1^{f_1}\cdots q_k^{f_k}>1.
\]

При нечётном \(d\)

\[
A^d+1=(A+1)(A^{d-1}-A^{d-2}+\cdots-A+1),
\]

что противоречит простоте. \(\square\)

Для singleton support \(S=\{2\}\) это заставляет

\[
e_1=2^m,
\]

то есть приводит к classical Fermat collapse.

Но при \(k\ge2\) происходит качественно иное.

## Теорема 4.2 — dimension jump

Пусть

\[
\mathcal C_k(B)
=
\{\mathbf e\in[1,B]^k:\gcd(\mathbf e)\text{ не имеет нечётного простого делителя}\}.
\]

Тогда для \(k\ge2\)

\[
\boxed{
\frac{|\mathcal C_k(B)|}{B^k}
\longrightarrow
\frac1{\zeta(k)(1-2^{-k})}.
}
\]

В частности,

\[
\frac{|\mathcal C_2(B)|}{B^2}	o\frac8{\pi^2}.
\]

### Доказательство

По Möbius inversion по нечётным общим делителям,

\[
|\mathcal C_k(B)|
=
\sum_{\substack{d\le B\\d\text{ odd}}}
\mu(d)\left\lfloor\frac Bd\right\rfloor^k.
\]

Деление на \(B^k\) и dominated convergence дают

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^k}
=
\prod_{\ell\text{ odd prime}}(1-\ell^{-k})
=
\frac1{\zeta(k)(1-2^{-k})}.
\]

\(\square\)

Итак, между \(|S|=1\) и \(|S|=2\) существует реальный dimension threshold: universal cyclotomic obstruction превращает одномерную family в zero-density set, но оставляет positive-density exponent space во всех higher dimensions.

---

# 5. Первая арифметическая асимметрия: \(\{2,3\}\) против \(\{2,5\}\)

Рассмотрим

\[
1+2^a5^b.
\]

Modulo \(3\),

\[
2\equiv5\equiv-1,
\]

поэтому

\[
3\mid1+2^a5^b
\iff
 a+b\text{ odd}.
\]

Следовательно, prime value требует

\[
a+b\equiv0\pmod2,
\]

и surviving fraction равна \(1/2\).

Теперь рассмотрим

\[
1+2^a3^b.
\]

Modulo \(5\), поскольку \(3\equiv2^3\),

\[
5\mid1+2^a3^b
\iff
 a+3b\equiv2\pmod4.
\]

Запрещена ровно четверть residue pairs, значит surviving fraction равна \(3/4\).

После сочетания с cyclotomic density \(8/\pi^2\) получаем

\[
\boxed{
\{2,3\}:\frac6{\pi^2},
\qquad
\{2,5\}:\frac4{\pi^2}.
}
\]

Их отношение равно

\[
\boxed{\frac32.}
\]

Это строгая, а не heuristic asymmetry.

---

# 6. Weighted counting by numerical size

Параметрический box count не учитывает, что \(3^b\) и \(5^b\) растут с разной скоростью. Поэтому положим

\[
L=\log X.
\]

Условие

\[
2^a q^b\le X
\]

эквивалентно

\[
a\log2+b\log q\le L.
\]

Площадь соответствующего weighted triangle равна

\[
\frac{L^2}{2\log2\log q}.
\]

## Теорема 6.1

Пусть \(A_{23}(X)\) считает exponent pairs для \(2^a3^b\le X\), прошедшие cyclotomic obstruction и mod-5 sieve. Тогда

\[
\boxed{
A_{23}(X)
=
\frac{3}{\pi^2\log2\log3}(\log X)^2
+O((\log X)\log\log X).
}
\]

Аналогично,

\[
\boxed{
A_{25}(X)
=
\frac{2}{\pi^2\log2\log5}(\log X)^2
+O((\log X)\log\log X).
}
\]

Поэтому

\[
\boxed{
\frac{A_{23}(X)}{A_{25}(X)}
\longrightarrow
\frac{3\log5}{2\log3}
\approx2.197460281.
}
\]

### Доказательство

Для нечётного \(d\), делящего \(a,b\), пишем

\[
a=du,\qquad b=dv.
\]

Тогда weighted triangle уменьшается в \(d\) раз:

\[
u\log2+v\log q\le\frac Ld.
\]

Поскольку \(d\) нечётно, local residue condition сохраняется. Для periodic residue set density \(r\) стандартный lattice count даёт

\[
N_d(L)
=
\frac{r}{2\log2\log q}\frac{L^2}{d^2}
+O\left(\frac Ld+1\right).
\]

Möbius inversion по нечётным common divisors приводит к

\[
A(L)
=
\frac{rL^2}{2\log2\log q}
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}
+O(L\log L).
\]

Но

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}=\frac8{\pi^2}.
\]

Для \(q=3\) имеем \(r=3/4\), для \(q=5\) — \(r=1/2\). Подстановка даёт формулы. \(\square\)

---

# 7. Descendant sieve pressure

Для prime \(\ell\notin S\) определим

\[
H_\ell(S)
=
\langle q\bmod\ell:q\in S\rangle
\le(\mathbb Z/\ell\mathbb Z)^\times.
\]

## Теорема 7.1 — one-prime local divisor density

Плотность exponent vectors, для которых

\[
\ell\mid N_S(\mathbf e),
\]

равна

\[
\boxed{
\delta_\ell(S)=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\
0,&-1\notin H_\ell(S).
\end{cases}
}
\]

Поскольку \(2\) — primitive root modulo \(3\) и modulo \(5\), для любого \(S\ni2\)

\[
3\notin S\Longrightarrow\delta_3(S)=\frac12,
\]

\[
5\notin S\Longrightarrow\delta_5(S)=\frac14.
\]

Назовём support 3-pure, если

\[
2,3\in S,\qquad5\notin S.
\]

Под действием extension of \((3\ 5)\) такой support переходит в 5-pure support. Поэтому one-level survival ratio снова равен \(3/2\).

Если exact descendant \(p\in X_S\) присоединяется к support,

\[
S^+=S\cup\{p\},
\]

3-purity сохраняется. Следовательно, gap \(3/2\) наследуется по всей такой descendant chain.

Для bookkeeping можно определить

\[
\mathfrak P_5(\mathcal S)=\prod_j(1-\delta_5(S_j)),
\]

\[
\mathfrak P_3(g\mathcal S)=\prod_j(1-\delta_3(gS_j)),
\]

и тогда

\[
\frac{\mathfrak P_5(\mathcal S)}{\mathfrak P_3(g\mathcal S)}
=
\left(\frac32\right)^{m+1}.
\]

Но \(\mathfrak P\) — только external bookkeeping functional. Это не joint probability across levels, не доказанная joint density и не graph invariant.

---

# 8. Cardinality wall

На этом месте возникает главный барьер статьи.

Multiplicity tower не видит sieve density. Он видит только

\[
\mu(S)=|X_S|.
\]

## Теорема 8.1

Если exact fibers \(X_S\) и \(X_T\) бесконечны, то

\[
\boxed{\mu(S)=\mu(T)=\aleph_0.}
\]

Следовательно, никакая разница в local densities, asymptotic constants, singular-series heuristics или growth laws сама по себе не препятствует one-level extension между этими fibers.

### Доказательство

Оба fibers — бесконечные подмножества countable set \(\mathbb P\), следовательно, countably infinite. \(\square\)

Итак, graph-visible obstruction должен в конце концов стать одним из трёх:

\[
\boxed{\text{empty vs nonempty},}
\]

\[
\boxed{\text{finite vs infinite},}
\]

или

\[
\boxed{\text{different finite cardinalities}.}
\]

Это и есть cardinality wall.

---

# 9. Что локальный sieve действительно не может

Finite fixed-divisor escape не позволяет сделать следующий чрезмерный вывод: нельзя утверждать, что никакой congruence mechanism на нескольких descendant levels не способен убить seed symmetry.

Доказан только более узкий барьер.

## Теорема 9.1 — levelwise finite fixed-divisor-cover barrier

На любом фиксированном exact-support level невозможно доказать emptiness соответствующей candidate family при помощи конечного набора фиксированных простых делителей, покрывающего все exponent vectors.

Тот же вывод применим по отдельности к конечному набору levels.

Но остаются открытыми:

- variable-divisor mechanisms;
- correlated congruence conditions между разными levels;
- cross-level arithmetic constraints;
- любые глубокие prime-value arguments, способные доказать конечность или пустоту exact fiber.

---

# 10. Finite-fiber compactness

Рассмотрим противоположный структурный regime.

## Определение 10.1 — FFC

Будем говорить, что выполняется finite-fiber condition, если

\[
\mu(S)<\infty
\]

для каждого finite exact support \(S\ni2\).

Under FFC every Pratt truncation \(P_{\le n}\) finite, hence every automorphism group

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n})
\]

finite.

Для seed \(\tau\in G_m\) обозначим через \(T_n(\tau)\) множество его extensions до height \(n\).

## Теорема 10.2 — finite-fiber compactness

Under FFC следующие условия эквивалентны:

1. \(\tau\) extends globally;
2. \(\tau\) survives every finite Pratt height;
3. \(T_n(\tau)\ne\varnothing\) for all \(n\ge m\).

### Доказательство

Extension sets образуют finitely branching tree. Если every finite level nonempty, König's infinity lemma даёт infinite compatible branch. HATTER-SOL-04 inverse-limit theorem превращает её в global automorphism. \(\square\)

## Следствие 10.3 — finite obstruction family

Если under FFC seed dies globally, существует least death height \(N\). Для каждого surviving partial extension

\[
g\in T_{N-1}(\tau)
\]

существует support \(S_g\), для которого

\[
\mu(S_g)\ne\mu(gS_g).
\]

Поскольку \(T_{N-1}(\tau)\) finite, получается finite obstruction family/tree.

Это structural certificate, а не algorithmic decidability theorem.

На immediate next level одного mismatch может быть достаточно. На later heights generally нужен whole finite obstruction tree.

---

# 11. Forward cone

Для \(A\subseteq\mathbb P\) определим \(C^+(A)\) как наименьшее множество, содержащее \(A\) и замкнутое вперёд относительно \(D\):

\[
q\in C^+(A),\ q\mid p-1
\Longrightarrow
p\in C^+(A).
\]

## Теорема 11.1 — density-one forward cone

Для любого нечётного простого \(a\),

\[
\boxed{d_{\mathbb P}(C^+(a))=1.}
\]

### Доказательство

Пусть

\[
N^+(a)=\{q\in\mathbb P:q\equiv1\pmod a\}.
\]

Для конечного \(Q\subset N^+(a)\) prime \(p\notin C^+(a)\) обязан удовлетворять

\[
p\not\equiv1\pmod q
\qquad(q\in Q),
\]

иначе существует path \(a\to q\to p\).

По CRT доля reduced residue classes modulo

\[
M=\prod_{q\in Q}q
\]

переживающих все запреты, равна

\[
\prod_{q\in Q}\left(1-\frac1{q-1}\right).
\]

PNT in arithmetic progressions даёт тот же upper bound для relative upper prime density complement of the cone.

Но

\[
\sum_{q\equiv1\pmod a}\frac1q=\infty,
\]

следовательно,

\[
\prod_{q\in Q}\left(1-\frac1{q-1}\right)\to0.
\]

Значит complement has relative prime density zero. \(\square\)

## Следствие 11.2 — двух шагов достаточно

Доказательство использует только paths

\[
a\to q\to p.
\]

Следовательно, уже множество простых, достижимых из \(a\) за не более чем два directed steps, имеет relative prime density one.

Это один из самых сильных структурных выводов HATTER-SOL-05: почти весь prime universe попадает в causal future одного odd prime уже через два слоя.

---

# 12. Causal localization

Пусть

\[
C=C^+(A),
\qquad
A\subseteq P_{\le n}.
\]

## Лемма 12.1 — generated-cone localization

Пусть \(g_n\in G_n\) фиксирует every vertex outside \(C\). Если exact support \(S\subseteq P_{\le n}\) удовлетворяет

\[
S\cap C=\varnothing,
\]

то

\[
g_nS=S,
\]

и every next-layer vertex \(p\in X_S\cap L_{n+1}\) lies outside \(C\).

### Доказательство

Все элементы \(S\) лежат вне \(C\), значит фиксируются.

Если \(p\in C\), то \(p\notin A\), потому что \(A\subseteq P_{\le n}\), а \(p\in L_{n+1}\). Следовательно, directed path from \(A\) to \(p\) имеет последнюю стрелку \(q\to p\), где \(q\in C\cap\operatorname{Pred}(p)=C\cap S\), contradiction. \(\square\)

Важно: для arbitrary forward-closed set без generated-cone hypothesis обратное утверждение может быть ложным, потому что vertex мог быть inserted as a seed. Эта scope correction является частью hostile proof audit.

---

# 13. Cone-Fiber Infinitude

Пусть \(g_1\in G_1\) и

\[
C=C^+(\operatorname{supp}(g_1)).
\]

## Определение 13.1 — CFI\((g_1)\)

CFI\((g_1)\) означает:

\[
\boxed{
\mu(S)=\aleph_0
}
\]

для каждого finite exact support \(S\), удовлетворяющего

\[
S\cap C\ne\varnothing.
\]

No condition is imposed on supports disjoint from \(C\).

Это строго локальнее прежней Higher-Fiber Infinitude hypothesis.

---

# 14. Causal Survival Theorem

## Теорема 14.1

Пусть \(g_1\in G_1\) и

\[
C=C^+(\operatorname{supp}(g_1)).
\]

Если выполняется CFI\((g_1)\), то \(g_1\) extends to a global automorphism

\[
g\in\operatorname{Aut}(\Pi)
\]

такой, что

\[
\boxed{g(p)=p\qquad(p\notin C).}
\]

### Доказательство

Строим compatible sequence \(g_n\in G_n\), сохраняя invariant: outside \(C\) все вершины фиксированы.

Пусть рассматривается next-layer exact support \(S\subseteq P_{\le n}\).

Если

\[
S\cap C=\varnothing,
\]

то по Lemma 12.1 support fixed и whole next-layer fiber lies outside \(C\); его можно фиксировать pointwise.

Если

\[
S\cap C\ne\varnothing,
\]

то и \(g_nS\cap C\ne\varnothing\), а CFI даёт

\[
\mu(S)=\aleph_0=\mu(g_nS).
\]

Multiplicity-tower theorem разрешает выбрать bijections между соответствующими fibers. Поскольку support meets \(C\), every vertex of such a fiber lies in \(C\) by forward closure. Следовательно, новые moved vertices never appear outside \(C\).

Индукция даёт compatible inverse-limit element, то есть global automorphism. \(\square\)

Для

\[
\tau=(3\ 5),
\qquad
C_\tau=C^+(\{3,5\}),
\]

CFI\((\tau)\) therefore implies global survival of the transposition, with all primes outside \(C_\tau\) fixed.

---

# 15. Что мы узнали о \(3\leftrightarrow5\)

Пятая статья не отвечает “да” или “нет” на global automorphism question.

Зато она резко изменила форму задачи.

С одной стороны, арифметика видит \(3\) и \(5\) по-разному уже на first higher exact supports. Эта разница не исчезает; она наследуется и multiplicatively accumulates в external sieve bookkeeping.

С другой стороны, graph forgets almost all of this quantitative information. Если оба exact fibers countably infinite, multiplicity tower объявляет их равными.

Получается необычная ситуация:

\[
\boxed{
\text{арифметическая асимметрия может быть сильной, но графово невидимой.}
}
\]

Чтобы убить symmetry, необходимо превратить quantitative difference в cardinality difference.

Именно здесь проходит настоящий frontier.

---

# 16. Literature boundary

Сам directed prime graph

\[
p\to q\iff p\mid q-1
\]

и роль одинаковых incoming predecessor sets уже обсуждались в 2012 году в MathOverflow question David Feldman и answer Gjergji Zaimi. Там также была ясно замечена связь между размерами таких classes и возможностью automorphisms.

Поэтому настоящая работа не заявляет priority за exact-support architecture как таковую и не заявляет broad principle “infinite fibers give symmetry / finite fibers give rigidity” как новый.

Классическими являются также:

- factorization \(A^d+1\) for odd \(d\);
- Fermat- and Pierpont-prime background;
- PNT in arithmetic progressions;
- divergence of reciprocal primes in reduced progressions;
- CRT;
- Möbius inversion;
- standard periodic lattice counting;
- König's infinity lemma;
- generalized Fermat pairwise-coprimality mechanism.

Работа претендует только на строго очерченную structural synthesis этих ingredients внутри HATTER-SOL multiplicity-tower programme и на доказанные теоремы о descendant pressure, cardinality wall, finite-fiber compactness, density-one causal cones и CFI survival.

---

# 17. Открытые вопросы

Остаются три естественных направления.

### 17.1. Unconditional killing

Найти support \(S\) in the causal cone, для которого можно доказать

\[
\mu(S)<\infty
\]

или

\[
\mu(S)=0,
\]

и построить finite obstruction tree blocking all extensions of \((3\ 5)\).

### 17.2. Orbitwise minimal survival

CFI всё ещё чрезмерно сильна: она требует infinitude for every support meeting the cone, хотя конкретная extension может реально посещать лишь часть support orbits.

Следующий вопрос:

\[
\boxed{
\text{каков exact orbitwise necessary-and-sufficient survival criterion?}
}
\]

Это естественная задача HATTER-SOL-06.

### 17.3. Mixed finite/infinite regime

FFC полностью контролирует compactness, а CFI даёт sufficient survival in an infinite-fiber regime. Между ними остаётся mixed world, где некоторые fibers finite, другие infinite. Именно там может возникать genuinely noncompact branching.

---

# 18. Заключение

Начав с простой перестановки

\[
3\leftrightarrow5,
\]

мы пришли к неожиданному разделению двух типов информации.

Арифметика exponent spaces очень быстро различает \(3\) и \(5\). Уже первый local sieve даёт ratio \(3/2\), а weighted counting усиливает различие до asymptotic ratio

\[
\frac{3\log5}{2\log3}.
\]

Exact descendants продолжают нести эту асимметрию.

Но radical-predecessor graph спрашивает не “сколько кандидатов приблизительно выживает?”, а лишь “сколько exact primes реально существует?”. И если ответа на обеих сторонах “счётно бесконечно много”, вся тонкая quantitative arithmetic схлопывается в одно

\[
\aleph_0.
\]

Поэтому пятая чашка обнаруживает не отсутствующего гостя, а правило рассадки:

\[
\boxed{
\text{симметрия погибает только тогда, когда арифметическое различие становится различием мощности exact fibers.}
}
\]

А causal geometry показывает ещё более странное: если один odd prime всё-таки начинает двигаться, его арифметическое будущее уже за два шага охватывает множество relative prime density one.

Так что следующая чашка должна спросить не “есть ли асимметрия?”, а “какая минимальная часть multiplicity tower обязана её увидеть?”.

**Продолжение следует.**

---

# References

1. D. Feldman, *Automorphisms of a certain digraph defined on the set of primes?*, MathOverflow, 2012; answer by G. Zaimi.
2. A. Languasco, F. Luca, P. Moree, S. Togbé, *Sequences of integers generated by two fixed primes*, Abh. Math. Semin. Univ. Hambg. 95 (2025), 123–148. DOI: 10.1007/s12188-025-00293-9.
3. Classical results used: prime number theorem in arithmetic progressions; divergence of reciprocal primes in reduced arithmetic progressions; Chinese remainder theorem; Möbius inversion; König's infinity lemma.
4. Classical background on Fermat and Pierpont primes; infinitude of Pierpont primes remains unproved.
